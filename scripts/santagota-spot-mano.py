"""SANTA GOTA · spot TV · V3 · 08 REVEAL — la mano real sostiene el packshot OFICIAL.

La regla del cliente: el packaging no se genera ni se redibuja. La regla de Valeria: prohibido el
producto flotando; una mano real lo sostiene. Las dos se cumplen así:
  1. Nano Banana genera «una mano sostiene ESTE squeeze horizontal» (packshot de referencia) → la pose,
     la escala y la luz vienen de ahí, pero ESE envase no se entrega.
  2. Se mide el eje del envase generado (píxeles oscuros del cuerpo: PCA → ángulo y largo).
  3. El packshot oficial se rota y escala a ese eje y se pega ENCIMA del envase generado.
  4. Los dedos vuelven DELANTE: máscara de piel (HSV) sobre la zona del envase, pegada encima del packshot.
  5. Verificación: la etiqueta del packshot pegado es el original (no pasa por ningún modelo).

Uso: python3 scripts/santagota-spot-mano.py <v3_mano_vN.png> [--out v3_reveal_compuesto.png]
"""
import sys, os, pathlib, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ
from PIL import Image, ImageFilter, ImageOps
import numpy as np

PL = RAIZ / "public/assets/santagota/spot/plates"
PR = RAIZ / "public/assets/santagota/producto"


def eje_envase(img: Image.Image):
    """Eje del cuerpo oscuro (verde casi negro) del envase generado: centro, ángulo, largo, ancho."""
    a = np.asarray(img.convert("RGB")).astype(float)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    lum = a.mean(axis=2)
    # cuerpo: oscuro pero no negro puro (el fondo), con un pelo de verde
    cuerpo = (lum > 12) & (lum < 95) & (g >= r - 6) & (g >= b - 6)
    ys, xs = np.where(cuerpo)
    if len(xs) < 500:
        raise SystemExit("no encuentro el cuerpo del envase")
    pts = np.stack([xs, ys], 1).astype(float)
    c = pts.mean(0)
    cov = np.cov((pts - c).T)
    w_, v = np.linalg.eigh(cov)
    d = v[:, np.argmax(w_)]               # dirección principal (eje largo)
    proj = (pts - c) @ d
    perp = (pts - c) @ np.array([-d[1], d[0]])
    largo = np.percentile(proj, 99) - np.percentile(proj, 1)
    ancho = np.percentile(perp, 98) - np.percentile(perp, 2)
    ang = np.degrees(np.arctan2(d[1], d[0]))  # 0° = horizontal hacia la derecha
    return c, ang, largo, ancho, cuerpo


def mascara_piel(img: Image.Image, x_min: int = 0) -> Image.Image:
    """Piel: tono rojizo-anaranjado, saturación media (los amarillos de la tapa y del aceite quedan fuera),
    y sólo a la derecha de `x_min` (el lado por donde entra la mano)."""
    hsv = np.asarray(img.convert("HSV")).astype(float)
    h, s, v = hsv[..., 0] / 255 * 360, hsv[..., 1] / 255, hsv[..., 2] / 255
    piel = ((h < 32) | (h > 340)) & (s > 0.16) & (s < 0.58) & (v > 0.2)
    piel[:, :x_min] = False
    m = Image.fromarray((piel * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(3))
    return m.filter(ImageFilter.GaussianBlur(1.2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mano"); ap.add_argument("--out", default="v3_reveal_compuesto.png")
    ap.add_argument("--nozzle", choices=["izq", "der"], default="izq", help="hacia dónde apunta la boquilla en la imagen generada")
    ap.add_argument("--escala", type=float, default=1.06, help="factor sobre el largo medido para cubrir el envase generado")
    a = ap.parse_args()

    base = Image.open(PL / a.mano).convert("RGB")
    W, H = 1920, 1080
    base = ImageOps.fit(base, (W, H), Image.LANCZOS)
    c, ang, largo, ancho, cuerpo = eje_envase(base)
    print(f"envase generado: centro=({c[0]:.0f},{c[1]:.0f}) ángulo={ang:.1f}° largo={largo:.0f} ancho={ancho:.0f}")

    # packshot oficial: vertical con la boquilla ARRIBA. PIL rota ANTIHORARIO con ángulo positivo:
    # rotate(90) deja la boquilla a la IZQUIERDA; se suma la inclinación del eje medido (±90° alrededor de horizontal).
    delta = ((ang + 90) % 180) - 90            # inclinación del eje respecto a la horizontal
    pk = Image.open(RAIZ / "public/assets/santagota/spot/producto/hero3-750.png").convert("RGBA")  # oficial + rim fino
    escala = (largo * a.escala) / (pk.height * 0.87)   # el cuerpo del packshot ≈ 87 % de su alto
    pk = pk.resize((int(pk.width * escala), int(pk.height * escala)), Image.LANCZOS)
    pk_rot = pk.rotate((90 if a.nozzle == "izq" else -90) - delta, expand=True, resample=Image.BICUBIC)
    # centro del CUERPO del packshot: el PNG entero incluye la boquilla, que va hacia la punta →
    # el centro del cuerpo está desplazado ~6,5 % del largo del PNG hacia la base
    d = np.array([np.cos(np.radians(delta)), np.sin(np.radians(delta))])   # eje horizontal (hacia la derecha)
    hacia_base = d if a.nozzle == "izq" else -d
    centro = c + hacia_base * (pk.height * 0.065)
    comp = base.convert("RGBA")
    px0, py0 = int(centro[0] - pk_rot.width / 2), int(centro[1] - pk_rot.height / 2)
    comp.alpha_composite(pk_rot, (px0, py0))
    # la punta de la boquilla (para poner el hilo REAL desde Remotion)
    tip = centro - hacia_base * (pk.height / 2)
    print(f"punta de la boquilla ≈ ({tip[0]:.0f}, {tip[1]:.0f})")

    # MATTE: todo lo que no sea piel (con margen) ni packshot oficial se va a negro. Así desaparecen la tapa
    # dibujada, el cuerpo dibujado que sobresale y el hilo CG. El hilo REAL entra desde Remotion en la punta.
    alfa_pk = Image.new("L", (W, H), 0); alfa_pk.paste(pk_rot.getchannel("A"), (px0, py0))
    x_min = int(c[0] - largo * 0.3) if a.nozzle == "izq" else 0
    piel_t = mascara_piel(base, x_min)
    zona_mano = piel_t.filter(ImageFilter.MaxFilter(15))
    keep = np.maximum(np.asarray(alfa_pk), np.asarray(zona_mano))
    keep_m = Image.fromarray(keep).filter(ImageFilter.GaussianBlur(1.5))
    comp = Image.composite(comp, Image.new("RGBA", comp.size, (0, 0, 0, 255)), keep_m)

    # los dedos vuelven delante
    piel = mascara_piel(base, x_min)
    comp = Image.composite(base.convert("RGBA"), comp, piel)
    comp.convert("RGB").save(PL / a.out)
    print("guardado", PL / a.out)


if __name__ == "__main__":
    main()

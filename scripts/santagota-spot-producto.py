"""SANTA GOTA · spot TV — packshots oficiales con la luz del set integrada (sin tocar la etiqueta).

El set de los keyframes 08–10 es un black studio a contraluz: horizonte dorado detrás,
acento lima a la izquierda y naranja a la derecha. Un packshot de e-commerce viene con luz
frontal neutra y ahí se lee pegado. Esta receta (la de CAVA, 28-08-2026) le pone:
  1. penumbra de cuerpo (baja luminosidad + toque de saturación; nunca mezcla con color plano),
  2. rim light en el contorno — sacado de la SILUETA BINARIA, no del alfa crudo,
  3. rebote cálido lamiendo el canto de la base.
y protege las luces (la etiqueta no se apaga al ritmo del envase).

Verificación: la zona de etiqueta cambia Δ < 6 (intacta). Si Δ > 18 se redibujó: no se entrega.

Entrada:  public/assets/santagota/producto/*-frente.png   (packshots oficiales, recortados, alfa real)
Salida:   public/assets/santagota/spot/producto/hero-*.png
"""
import pathlib, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ
from PIL import Image, ImageChops, ImageEnhance, ImageFilter
import numpy as np

SRC = RAIZ / "public/assets/santagota/producto"
DST = RAIZ / "public/assets/santagota/spot/producto"
DST.mkdir(parents=True, exist_ok=True)

LIMA = (195, 214, 0)
NARANJA = (242, 101, 19)
ORO = (255, 196, 90)


def silueta(a: np.ndarray) -> np.ndarray:
    return (a > 128).astype(np.uint8) * 255


def anillo(mask: np.ndarray, px: int, lado: str) -> Image.Image:
    """Borde interior de `px` de ancho, sólo del lado pedido (izq/der/abajo)."""
    m = Image.fromarray(mask)
    ero = m.filter(ImageFilter.MinFilter(px * 2 + 1))
    ring = ImageChops.subtract(m, ero)
    r = np.asarray(ring).astype(np.float32) / 255
    h, w = r.shape
    ys, xs = np.mgrid[0:h, 0:w]
    # limitar al lado: comparar con el centro de la silueta por fila
    cols = np.where(mask.any(axis=0))[0]
    cx = (cols.min() + cols.max()) / 2 if len(cols) else w / 2
    if lado == "izq":
        r *= (xs < cx)
    elif lado == "der":
        r *= (xs > cx)
    elif lado == "abajo":
        rows = np.where(mask.any(axis=1))[0]
        r *= (ys > rows.max() - px * 3)
    return Image.fromarray((r * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(px * 0.6))


def integra_luz(src: pathlib.Path, dst: pathlib.Path, rim_izq=LIMA, rim_der=NARANJA, penumbra=0.88, fuerza=0.55):
    im = Image.open(src).convert("RGBA")
    rgb = im.convert("RGB")
    a = np.asarray(im.getchannel("A"))
    mask = silueta(a)
    lum = np.asarray(rgb.convert("L")).astype(np.float32) / 255

    # 1. penumbra: el cuerpo se apaga, las luces (etiqueta clara) se protegen
    oscuro = ImageEnhance.Brightness(rgb).enhance(penumbra)
    oscuro = ImageEnhance.Color(oscuro).enhance(1.08)
    # protección: las luces (etiqueta clara) Y el color (la etiqueta es saturada; el envase es casi negro)
    hsv = np.asarray(rgb.convert("HSV")).astype(np.float32) / 255
    sat = hsv[..., 1] * hsv[..., 2]                        # saturación efectiva (0 en negro)
    prot = np.maximum(np.clip((lum - 0.45) / 0.35, 0, 1), np.clip((sat - 0.12) / 0.25, 0, 1))
    m_pen = Image.fromarray(((1 - prot) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))
    base = Image.composite(oscuro, rgb, m_pen)

    # 2. rim light por lado (contraluz de estudio: dorado arriba, lima izq, naranja der)
    def pinta(img, ring, color, k):
        capa = Image.new("RGB", img.size, color)
        m = ring.point(lambda v: int(v * k))
        return Image.composite(ImageChops.screen(img, capa), img, m)

    px = max(3, int(im.width * 0.012))
    base = pinta(base, anillo(mask, px, "izq"), rim_izq, fuerza)
    base = pinta(base, anillo(mask, px, "der"), rim_der, fuerza)
    # (sin rim superior: la tapa ya es clara)

    # 3. rebote cálido en el canto de la base
    base = pinta(base, anillo(mask, px * 2, "abajo"), ORO, fuerza * 0.7)

    out = base.convert("RGBA")
    out.putalpha(im.getchannel("A"))
    out.save(dst)

    # verificación: la etiqueta (tercio central del alto, mitad central del ancho) no se redibujó
    h, w = a.shape
    caja = (int(w * 0.34), int(h * 0.42), int(w * 0.66), int(h * 0.68))   # centro de la etiqueta, sin bordes
    d = ImageChops.difference(rgb.crop(caja), base.crop(caja))
    delta = float(np.asarray(d).mean())
    ok = "intacta" if delta < 6 else ("aceptable" if delta < 18 else "⛔ REDIBUJADA")
    print(f"  {dst.name:26} Δetiqueta={delta:5.2f}  {ok}")
    return delta


if __name__ == "__main__":
    pares = [
        ("squeeze-750-frente.png", "hero-750.png"),
        ("squeeze-500-frente.png", "hero-500.png"),
        ("lata-cocinar-frente.png", "hero-lata-cocinar.png"),
        ("lata-aderezar-frente.png", "hero-lata-aderezar.png"),
    ]
    for s, d in pares:
        integra_luz(SRC / s, DST / d)
    print("listo →", DST.relative_to(RAIZ))

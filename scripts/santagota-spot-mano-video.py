"""SANTA GOTA · animatic · 08 REVEAL en movimiento — la mano real se mueve, el packaging es el packshot OFICIAL.

Kling animó el ensayo de la mano con el envase GENÉRICO (clips/mano_gesto.mp4). Ese envase no se entrega:
cuadro a cuadro se mide el eje del envase generado (PCA, igual que en la foto fija), se suaviza la trayectoria
(ventana de 9 cuadros: el modelo tiembla un poco, la mano no), se pega el packshot oficial rotado/escalado a ese
eje, todo lo que no es piel / aceite / packshot se va a negro, y los dedos y el hilo vuelven DELANTE.

Uso: python3 scripts/santagota-spot-mano-video.py <carpeta_frames_png> [--out public/assets/santagota/spot/reveal]
Escribe NNNN.png (1920×1080) + reveal.json con la punta de la boquilla por cuadro.
"""
import argparse, importlib.util, json, os, sys, pathlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np

spec = importlib.util.spec_from_file_location("mano", pathlib.Path(__file__).with_name("santagota-spot-mano.py"))
mano = importlib.util.module_from_spec(spec); spec.loader.exec_module(mano)
W, H = 1920, 1080


def mascara_aceite(img, x_max, y_min):
    """El hilo de aceite generado: amarillo-dorado saturado, sólo a la izquierda de la punta y bajo ella."""
    hsv = np.asarray(img.convert("HSV")).astype(float)
    h, s, v = hsv[..., 0] / 255 * 360, hsv[..., 1] / 255, hsv[..., 2] / 255
    m = (h > 28) & (h < 75) & (s > 0.11) & (v > 0.14)      # el hilo generado es dorado OSCURO y poco saturado (medido: s 0,16–0,37)
    m[:, int(x_max):] = False; m[: int(y_min), :] = False
    return Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(0.8))


def punta_generada(img, cy):
    """Punta de la boquilla dibujada: el amarillo saturado más a la izquierda en la banda del envase."""
    hsv = np.asarray(img.convert("HSV")).astype(float)
    h, s, v = hsv[..., 0] / 255 * 360, hsv[..., 1] / 255, hsv[..., 2] / 255
    m = (h > 38) & (h < 68) & (s > 0.5) & (v > 0.5)
    m[: int(cy - 220), :] = False; m[int(cy + 220):, :] = False
    ys, xs = np.where(m)
    i = np.argmin(xs)
    return float(xs[i]), float(np.median(ys[xs < xs[i] + 12]))


def suaviza(v, n=9):
    v = np.asarray(v, float); k = np.ones(n) / n
    pad = np.pad(v, (n // 2, n // 2), mode="edge")
    return np.convolve(pad, k, mode="valid")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("frames"); ap.add_argument("--out", default=str(RAIZ / "public/assets/santagota/spot/reveal"))
    ap.add_argument("--escala", type=float, default=1.06); ap.add_argument("--packshot", default="hero4-750.png")
    ap.add_argument("--lifestyle", action="store_true", help="escena real (no se mattea a negro); el envase se busca sólo en --caja")
    ap.add_argument("--caja", default="0,0,1,1", help="x0,y0,x1,y1 en fracciones del cuadro donde vive el envase")
    ap.add_argument("--punta", help="x,y de la punta de la boquilla dibujada (px 1920×1080): salta la detección")
    ap.add_argument("--base", help="x,y del fondo del envase dibujado (px): con --punta fija el eje y el tamaño")
    a = ap.parse_args()
    cx0, cy0, cx1, cy1 = [float(v) for v in a.caja.split(",")]
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    archivos = sorted(pathlib.Path(a.frames).glob("*.png"))
    bases, ejes = [], []
    for f in archivos:
        im = ImageOps.fit(Image.open(f).convert("RGB"), (W, H), Image.LANCZOS)
        # el envase se busca sólo dentro de la caja: fuera de ella todo se tapa de blanco (no cuenta como cuerpo ni como tapa)
        busca = im.copy()
        if a.lifestyle:
            tapa = Image.new("RGB", (W, H), (255, 255, 255)); tapa.paste(im.crop((int(cx0 * W), int(cy0 * H), int(cx1 * W), int(cy1 * H))), (int(cx0 * W), int(cy0 * H))); busca = tapa
        c, ang, largo, ancho, _ = mano.eje_envase(busca)
        tx, ty = punta_generada(busca, c[1])
        bases.append(im); ejes.append((c[0], c[1], ((ang + 90) % 180) - 90, largo, tx, ty))
    e = np.array(ejes)
    cx, cy, delta = suaviza(e[:, 0]), suaviza(e[:, 1]), suaviza(e[:, 2])
    gx, gy = suaviza(e[:, 4]), suaviza(e[:, 5])
    manual = None
    if a.punta and a.base:
        px_, py_ = [float(v) for v in a.punta.split(",")]; bx_, by_ = [float(v) for v in a.base.split(",")]
        ang_m = np.degrees(np.arctan2(by_ - py_, bx_ - px_))       # dirección punta → base
        gx[:] = px_ - 6; gy[:] = py_; delta[:] = ang_m
        manual = float(np.hypot(bx_ - px_, by_ - py_))
        print(f"eje manual: punta ({px_:.0f},{py_:.0f}) → base ({bx_:.0f},{by_:.0f}) · {ang_m:.1f}° · largo total {manual:.0f}")
    print(f"punta generada x {gx.min():.0f}–{gx.max():.0f} · y {gy.min():.0f}–{gy.max():.0f}")
    largo = float(np.median(e[:, 3]))            # el envase no cambia de tamaño: escala fija
    print(f"{len(bases)} cuadros · centro x {cx.min():.0f}–{cx.max():.0f} · y {cy.min():.0f}–{cy.max():.0f} · "
          f"inclinación {delta.min():.1f}°–{delta.max():.1f}° · largo mediano {largo:.0f} (crudo {e[:,3].min():.0f}–{e[:,3].max():.0f})")

    pk0 = Image.open(RAIZ / "public/assets/santagota/spot/producto" / a.packshot).convert("RGBA")
    esc = (manual * a.escala) / pk0.height if manual else (largo * a.escala) / (pk0.height * 0.87)
    pk = pk0.resize((int(pk0.width * esc), int(pk0.height * esc)), Image.LANCZOS)
    puntas = []
    for i, base in enumerate(bases):
        d = np.array([np.cos(np.radians(delta[i])), np.sin(np.radians(delta[i]))])
        tip = np.array([gx[i] + 6, gy[i]])              # la punta oficial cae sobre la punta dibujada (el hilo nace ahí)
        centro = tip + d * (pk.height / 2)
        pk_rot = pk.rotate(90 - delta[i], expand=True, resample=Image.BICUBIC)
        px0, py0 = int(centro[0] - pk_rot.width / 2), int(centro[1] - pk_rot.height / 2)
        comp = base.convert("RGBA"); comp.alpha_composite(pk_rot, (px0, py0))
        alfa = Image.new("L", (W, H), 0); alfa.paste(pk_rot.getchannel("A"), (px0, py0))
        x_min = int(cx[i] - largo * 0.3)
        piel = mano.mascara_piel(base, x_min)
        aceite = mascara_aceite(base, tip[0] + 28, tip[1] + 12)   # cuelga recto bajo la punta; bajo ella para no rescatar la tapa dibujada
        if a.lifestyle:
            # escena real: nada se mattea. El packshot tapa el envase dibujado; los dedos vuelven delante SÓLO donde tapan el
            # packshot (piel ∧ alfa dilatada) y el hilo sólo en una banda angosta bajo la punta.
            alfa_d = alfa.filter(ImageFilter.MaxFilter(9))
            piel_pk = Image.fromarray(np.minimum(np.asarray(piel), np.asarray(alfa_d)))
            banda = Image.new("L", (W, H), 0); ImageDraw.Draw(banda).rectangle((int(tip[0]) - 34, int(tip[1]) + 6, int(tip[0]) + 34, H), fill=255)
            aceite_b = Image.fromarray(np.minimum(np.asarray(aceite), np.asarray(banda)))
            # y el envase dibujado que asome fuera del packshot se disimula: se rellena con el propio fondo desenfocado alrededor
            comp = Image.composite(base.convert("RGBA"), comp, piel_pk)
            comp = Image.composite(base.convert("RGBA"), comp, aceite_b)
        else:
            keep = np.maximum.reduce([np.asarray(alfa), np.asarray(piel.filter(ImageFilter.MaxFilter(15))), np.asarray(aceite)])
            comp = Image.composite(comp, Image.new("RGBA", comp.size, (0, 0, 0, 255)), Image.fromarray(keep).filter(ImageFilter.GaussianBlur(1.5)))
            comp = Image.composite(base.convert("RGBA"), comp, piel)          # dedos delante
            comp = Image.composite(base.convert("RGBA"), comp, aceite)        # el hilo delante
        comp.convert("RGB").save(out / f"{i + 1:04d}.png")
        puntas.append([round(float(tip[0])), round(float(tip[1]))])
    json.dump({"n": len(bases), "fps": 24, "tip": puntas}, open(out / "reveal.json", "w"))
    print("punta cuadro 1:", puntas[0], "· cuadro final:", puntas[-1], "→", out)


if __name__ == "__main__":
    main()

"""BETWEEN · FEED 01-10 carrusel To Go — una sola ESCALA de cámara para las láminas de producto.

Eli, 01-10 (r14): «vuelve a hacer las imágenes para que se vean coherentes los tamaños, es lo que más
comentarios tendré». Medido sobre las escenas (alto del vaso ÷ alto real, con el XL = 1):
    n°3 sándwich  vaso chico  1354 px → escala 1904      n°4 dulce (3-a)  chico 1200 px → 1688
    n°5 los tres  XL          1264 px → escala 1264      trío (n°2)       1336/1654/1934 → ~1900
O sea, el XL de la última se veía MÁS BAJO en el cuadro que el chico del sándwich. Los vasos aprobados
(`out/hilton/between/vasos-togo/BW-ToGo-*.png`, a escala real entre sí) dan alto 0,711 · 0,861 · 1 y
tapa 0,507 · 0,552 · 0,587.

La escala común es **1500**: es lo máximo que deja la n°5, donde además del XL entra la bolsa bajo la
fila de precios. La portada (vaso en mano) ya está en ~1450. El trío queda como plano de detalle.

`guias`   arma las guías para Nano Banana (lo gris se rellena; el vaso Grande va pegado a su tamaño):
            n°3  la 2-a achicada a 0,788        n°4  la 3-a achicada a 0,889 con el vaso Grande
`cerrar`  repone los píxeles originales al centro de cada relleno (la IA devuelve todo con dominante)
          e iguala el color del relleno a ellos.

    py scripts/bw-fd-01-10-escala.py guias | cerrar
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
G = RAIZ / "raw/hilton/between/oct/gen"
REFS = RAIZ / "raw/hilton/between/oct/refs-gen"
PUB = RAIZ / "public/assets/hilton/between/oct/gen"
VASOS = RAIZ / "out/hilton/between/vasos-togo"
W, H = 3712, 4608
S = 1500            # px de alto del vaso XL en todas las láminas
BASE = 3480         # fila donde se apoya el vaso
# lámina: (escena, escala propia medida, x del eje del vaso, fila de su base)
N3 = dict(src=PUB / "gen-fd01-2-a.jpg", escala=1904, eje=1855, base=3336)
N4 = dict(src=PUB / "gen-fd01-3-a.jpg", escala=1688, eje=1910, base=3420)


def lienzo(im, d):
    """La escena achicada a la escala común sobre gris, con el vaso apoyado en BASE y centrada en x."""
    k = S / d["escala"]
    ch = im.resize((round(W * k), round(H * k)), Image.LANCZOS)
    x0, y0 = (W - ch.width) // 2, round(BASE - d["base"] * k)
    L = Image.new("RGB", (W, H), (128, 128, 128))
    L.paste(ch, (x0, y0))
    return L, ch, (x0, y0), k


def con_vaso_grande():
    """La 3-a con el vaso chico borrado y el Grande aprobado pegado a su tamaño real en esa escena."""
    a = np.asarray(Image.open(N4["src"]).convert("RGB"))
    m = np.zeros(a.shape[:2], np.uint8)
    cv2.fillPoly(m, [np.array([[1445, 2195], [2375, 2195], [2375, 2475], [2340, 2475], [2265, 3440], [1555, 3440],
                               [1480, 2475], [1445, 2475]], np.int32)], 255)
    limpio = Image.fromarray(cv2.inpaint(a, m, 9, cv2.INPAINT_TELEA))
    vaso = Image.open(VASOS / "BW-ToGo-grande-12oz.png").convert("RGBA")
    vaso = vaso.crop(vaso.getchannel("A").getbbox())
    alto = round(0.861 * N4["escala"])
    vaso = vaso.resize((round(vaso.width * alto / vaso.height), alto), Image.LANCZOS)
    limpio.paste(vaso, (round(N4["eje"] - vaso.width / 2), N4["base"] + 6 - alto), vaso)
    return limpio


if sys.argv[1] == "guias":
    L, _, _, k = lienzo(Image.open(N3["src"]).convert("RGB"), N3)
    L.save(REFS / "gen-fd01-n3-lienzo.jpg", quality=95)
    print(f"n°3: 2-a × {k:.3f}")
    L, _, _, k = lienzo(con_vaso_grande(), N4)
    L.save(REFS / "gen-fd01-n4-lienzo.jpg", quality=95)
    print(f"n°4: 3-a × {k:.3f} con el vaso Grande ({round(0.861 * S)} px de alto en la lámina)")

if sys.argv[1] == "cerrar":
    for nombre, d, vaso in (("n3", N3, None), ("n4", N4, True)):
        suf = sys.argv[2] if len(sys.argv) > 2 else "a"
        rell = Image.open(G / f"gen-fd01-{nombre}-{suf}.png").convert("RGB").resize((W, H), Image.LANCZOS)
        orig = Image.open(d["src"]).convert("RGB")
        _, ch, (x0, y0), k = lienzo(orig, d)
        caja = (max(0, x0), max(0, y0), min(W, x0 + ch.width), min(H, y0 + ch.height))
        a = np.asarray(ch.crop((caja[0] - x0, caja[1] - y0, caja[2] - x0, caja[3] - y0))).astype(np.float32)
        b = np.asarray(rell.crop(caja)).astype(np.float32)
        fuera = np.ones(a.shape[:2], bool)
        if vaso:  # el vaso de la n°4 es el de la IA (integrado a la luz): no entra en la medida ni se repone
            vx, vy = x0 + d["eje"] * k, y0 + d["base"] * k
            fuera[: int(vy - caja[1] + 40), int(vx - caja[0] - 480): int(vx - caja[0] + 480)] = False
        gan = a[fuera].mean(0) / b[fuera].mean(0)
        corr = np.clip(np.asarray(rell).astype(np.float32) * gan, 0, 255).astype(np.uint8)
        masc = Image.new("L", (W, H), 0)
        masc.paste(255, (caja[0] + 60, caja[1] + 60, caja[2] - 60, caja[3] - (60 if caja[3] < H else 0)))
        if vaso:
            hueco = Image.new("L", (W, H), 0)
            alto = 0.861 * S
            hueco.paste(255, (int(vx - 500), int(vy - alto - 90), int(vx + 500), int(vy + 50)))
            masc = Image.composite(Image.new("L", (W, H), 0), masc, hueco)
        masc = masc.filter(ImageFilter.GaussianBlur(20))
        base_ = Image.new("RGB", (W, H))
        base_.paste(ch, (x0, y0))
        out = Image.composite(base_, Image.fromarray(corr), masc)
        out.save(G / f"gen-fd01-{nombre}-final.png")
        print(f"{nombre}: ganancia {gan.round(3)} → gen-fd01-{nombre}-final.png")

if sys.argv[1] == "n5":
    # n°5: la 5h-a (bolsa con las asas caídas) tiene el XL a 1264 px → se acerca 1,187 recortando, sin IA.
    # Ventana: el vaso queda apoyado en BASE y el conjunto (sándwich … bolsa) centrado.
    k = S / 1264
    x0, y0 = 360, round(3609 - BASE / k)
    im = Image.open(G / "gen-fd01-5h-a.png").convert("RGB")
    im.crop((x0, y0, x0 + round(W / k), y0 + round(H / k))).resize((W, H), Image.LANCZOS).save(G / "gen-fd01-n5-final.png")
    cara = [(1609, 1948), (3408, 2035), (3268, 3840), (1680, 3561)]  # cara frontal de la bolsa en la 5h-a
    print("n5: ×%.3f desde (%d, %d) · cara de la bolsa:" % (k, x0, y0),
          " ".join("%d,%d" % (round((x - x0) * k), round((y - y0) * k)) for x, y in cara))

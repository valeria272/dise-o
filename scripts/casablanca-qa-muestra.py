#!/usr/bin/env python3
"""QA: ¿la muestra de la tarjeta es el MISMO piso que está en el suelo?

Es el error más caro de esta marca —«el cliente compra lo que ve»— y es el que
volvió la entrega de septiembre 2026 en la ronda 1: muestra café rojizo sobre
piso miel. Acá se mide ΔE entre la muestra montada y el piso que la rodea, sobre
la pieza YA renderizada. Umbral: ΔE < 12 se lee como el mismo piso.
"""
import glob
import sys

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
MUESTRA = (124.8, 258.0, 139.7, 470.0)      # medido en las fichas de Paulina
MUESTRA_ST = (161.6, 418.6, 155.0, 522.0)


def lab(rgb):
    r, g, b = [c / 255 for c in rgb]
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = f(r), f(g), f(b)
    X = (r * .4124 + g * .3576 + b * .1805) / .95047
    Y = r * .2126 + g * .7152 + b * .0722
    Z = (r * .0193 + g * .1192 + b * .9505) / 1.08883
    g2 = lambda t: t ** (1 / 3) if t > .008856 else 7.787 * t + 16 / 116
    fx, fy, fz = g2(X), g2(Y), g2(Z)
    return np.array([116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)])


def main(rutas):
    malas = 0
    for r in sorted(rutas):
        im = Image.open(r).convert("RGB")
        W, H = im.size
        k = W / 1080
        x, y, w, h = MUESTRA_ST if H / W > 1.4 else MUESTRA
        a = np.asarray(im).astype(float)
        m = a[int((y + h * .30) * k):int((y + h * .92) * k),
              int((x + w * .18) * k):int((x + w * .82) * k)].reshape(-1, 3).mean(axis=0)
        piso = a[int((y + h * 1.12) * k):int((y + h * 1.45) * k),
                 int(x * k):int((x + w * 2.4) * k)].reshape(-1, 3).mean(axis=0)
        dE = np.linalg.norm(lab(m) - lab(piso))
        ok = dE < 12
        malas += 0 if ok else 1
        print(f"  {r.split('/')[-1]:44s} ΔE muestra↔piso {dE:5.1f}  {'OK' if ok else '⚠ NO CALZA'}")
    return 1 if malas else 0


if __name__ == "__main__":
    rutas = sys.argv[1:] or glob.glob("out/casablanca/septiembre/cb_sep_c1-*.png")
    sys.exit(main(rutas))

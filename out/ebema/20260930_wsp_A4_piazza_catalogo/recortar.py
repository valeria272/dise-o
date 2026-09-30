# -*- coding: utf-8 -*-
"""A4 Piazza catálogo — recorta los packshots reales de las fichas (sin IA sobre el producto).
rembg sólo da la máscara; el píxel del producto es el de la ficha. Se queda con la
componente conexa más grande (el producto) y descarta textos y planos técnicos."""
from pathlib import Path
import numpy as np, cv2
from PIL import Image
from rembg import remove, new_session
RAIZ = Path(__file__).resolve().parents[3]
SRC = RAIZ / "raw/ebema/piazza-catalogo-a4a5"
OUT = Path(__file__).parent / "recortes"
# franja vertical del packshot en la ficha 3508x4961 (bajo la cabecera, sobre las specs)
# ronda 4: la franja baja más para no cortar las bases (Calyx y Azteca salían mochas)
FRANJA = {"PZ6000": (500, 3100), "PZ6002": (500, 3050), "PZ6009": (500, 3350),
          "PZ6012": (500, 3050), "PZ20000NE": (500, 3150), "AZ3214": (500, 3250),
          "GR317": (500, 3000)}
SOLO_MAYOR = set(FRANJA)   # sólo el producto: fuera planos técnicos y textos
ses = new_session("isnet-general-use")
for k, (y0, y1) in FRANJA.items():
    im = Image.open(SRC / f"{k}.jpg").convert("RGB").crop((0, y0, 3508, y1))
    m = np.array(remove(im, session=ses, only_mask=True))
    n, lab, st, _ = cv2.connectedComponentsWithStats((m > 40).astype(np.uint8), 8)
    grande = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    x, y, w, h = st[grande, :4]
    # conserva toda componente que toque la caja del producto (piezas sueltas: manillas, flexibles)
    keep = np.zeros_like(m)
    for i in range(1, n):
        xi, yi, wi, hi, a = st[i]
        if k in SOLO_MAYOR and i != grande:
            continue    # el lavaplato tiene el plano técnico pegado a la base
        if a > 3000 and xi < x + w and xi + wi > x and yi < y + h and yi + hi > y:
            keep[lab == i] = 255
    alpha = np.minimum(m, keep)
    rgba = np.dstack([np.array(im), alpha])
    ys, xs = np.where(alpha > 10)
    rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    Image.fromarray(rgba).save(OUT / f"{k}.png"); print(k, rgba.shape[1], rgba.shape[0])

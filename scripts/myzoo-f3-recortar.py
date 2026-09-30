#!/usr/bin/env python3
"""MyZoo Fase 3 — recorta los packshots de Pet Wipes que Paulina entregó sobre blanco.

Relleno desde los bordes (no umbral): la tapa de las toallitas es blanca y un umbral
se la come. Salida RGBA recortada al contenido en public/assets/myzoo/producto/.
"""
import glob, os
import numpy as np
from PIL import Image, ImageFilter
from PIL import ImageDraw

SRC = "raw/myzoo/fase3/packshots"
DST = "public/assets/myzoo/producto"
# Fondo = gris NEUTRO claro conectado al borde: así se va también la sombra gris del
# render. El beige del envase tiene ~30 de diferencia entre canales y no es neutro.
NEUTRO = 8     # máx. diferencia entre canales
CLARO = 140    # mín. valor del canal más oscuro

for f in sorted(glob.glob(f"{SRC}/*.png")):
    im = Image.open(f).convert("RGB")
    a = np.asarray(im).astype(int)
    casi_blanco = ((a.max(axis=2) - a.min(axis=2)) <= NEUTRO) & (a.min(axis=2) >= CLARO)
    m = Image.fromarray(np.where(casi_blanco, 255, 0).astype("uint8")).copy()  # sin .copy() queda de sólo lectura y floodfill no escribe
    W, H = m.size
    semillas = [(x, y) for x in range(0, W, 40) for y in (0, H - 1)] + [(x, y) for y in range(0, H, 40) for x in (0, W - 1)]
    for s in semillas:
        if m.getpixel(s) == 255:
            ImageDraw.floodfill(m, s, 128)
    fondo = np.asarray(m) == 128
    alfa = Image.fromarray(np.where(fondo, 0, 255).astype("uint8"))
    alfa = alfa.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    out = im.convert("RGBA"); out.putalpha(alfa)
    out = out.crop(alfa.getbbox())
    nombre = "MyZoo_" + os.path.basename(f).replace("-", "_")
    out.save(f"{DST}/{nombre}")
    print(nombre, out.size)

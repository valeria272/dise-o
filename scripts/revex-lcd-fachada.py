#!/usr/bin/env python3
"""
REVEX R4 — encuadres de la fachada de Las Condes Design (brief septiembre 2026).
Parte de lcd_fachada.jpg (2250x1520), foto real y limpia del local con el logo
GRUPOREVEX sobre la entrada.
"""
import os, sys
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ

DEST = RAIZ / "public/assets/revex/sep"
src = Image.open(DEST / "lcd_fachada.jpg").convert("RGB"); W, H = src.size

# ---------- FEED 2250x2250 : cuadrado centrado en el logo de la entrada ------
x0 = 190                                   # deja el logo GRUPOREVEX centrado
feed = src.crop((x0, 0, x0 + H, H)).resize((2250, 2250), Image.LANCZOS)
feed.save(DEST / "lcd_fachada_feed.jpg", quality=95)
print("lcd_fachada_feed.jpg  2250x2250  (crop", x0, "..", x0 + H, ")")

# ---------- STORY 2250x4000 : la foto a lo ancho, extendida arriba y abajo ---
# El wordmark GRUPOREVEX ocupa casi todo el ancho: recortarlo en vertical lo
# partiría. Se conserva completo y se estiran las bandas de hormigón (arriba) y
# de vitrina (abajo), que son lisas y no delatan el estirado.
fw = 2250; fh = int(H * fw / W)
foto = src.resize((fw, fh), Image.LANCZOS)
story = Image.new("RGB", (fw, 4000))
top = 1150                                  # la foto queda en el 2º cuarto del cuadro
story.paste(foto, (0, top))
a = np.asarray(story).astype(np.float64)
f = np.asarray(foto).astype(np.float64)

banda_sup = f[0:30].mean(axis=0)             # hormigón del cielo raso
for y in range(top):
    t = y / top
    a[y] = banda_sup * (0.42 + 0.58 * t)
banda_inf = f[-30:].mean(axis=0)             # vitrina oscura
h2 = 4000 - (top + fh)
for i in range(h2):
    t = (i / h2) ** 0.9
    a[top + fh + i] = banda_inf * (1 - 0.55 * t)
Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(DEST / "lcd_fachada_story.jpg", quality=95)
print("lcd_fachada_story.jpg 2250x4000  (foto completa + bandas estiradas)")

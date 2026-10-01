"""BETWEEN · FEED 01-10 carrusel To Go — devuelve el color original a la escena rellenada.

`gen-fd01-4d-a` (la 4c-b achicada al 86 % sobre lienzo gris + bordes rellenados por la IA) volvió
con dominante magenta en TODO el cuadro: vaso y pan rosados, bolsa lila (213·189·213). No se
corrige a ojo: la foto original sigue ahí adentro, así que
  1. el relleno se iguala a ella canal por canal (ganancia medida en la zona que comparten), y
  2. el centro se reemplaza por los píxeles ORIGINALES de la 4c-b, con borde difuminado.

    py scripts/bw-fd-01-10-bolsa-blanca.py   →  raw/hilton/between/oct/gen/gen-fd01-4d-a-color.png
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

G = Path(__file__).resolve().parent.parent / "raw/hilton/between/oct/gen"
K = 0.86
orig = Image.open(G / "gen-fd01-4c-b.png").convert("RGB")
rell = Image.open(G / "gen-fd01-4d-a.png").convert("RGB")
W, H = orig.size
ch = orig.resize((int(W * K), int(H * K)), Image.LANCZOS)
x0, y0 = (W - ch.width) // 2, H - ch.height
a, b = np.asarray(ch).astype(np.float32), np.asarray(rell.crop((x0, y0, x0 + ch.width, H))).astype(np.float32)
print("diferencia media centro (antes):", np.abs(a - b).mean(axis=(0, 1)).round(1))
gan = a.reshape(-1, 3).mean(0) / b.reshape(-1, 3).mean(0)
print("ganancia por canal:", gan.round(3))
corr = Image.fromarray(np.clip(np.asarray(rell).astype(np.float32) * gan, 0, 255).astype(np.uint8))
print("diferencia media centro (relleno igualado):",
      np.abs(a - np.asarray(corr.crop((x0, y0, x0 + ch.width, H))).astype(np.float32)).mean(axis=(0, 1)).round(1))
masc = Image.new("L", (W, H), 0)
m = 60  # el original entra 60 px adentro de su borde y se funde en 40
masc.paste(255, (x0 + m, y0 + m, x0 + ch.width - m, H))
masc = masc.filter(ImageFilter.GaussianBlur(20))
lienzo = Image.new("RGB", (W, H))
lienzo.paste(ch, (x0, y0))
Image.composite(lienzo, corr, masc).save(G / "gen-fd01-4d-a-color.png")
print("ok gen-fd01-4d-a-color.png")

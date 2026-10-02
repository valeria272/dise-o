"""PISO18 · OCTUBRE 2026 — FEED 20-10: recorta los dos racimos de globos como capas con alfa.

Ronda 9 (Eli 02-10): la foto queda sobria y «algunas cosas van apareciendo, por ejemplo
globos». `f20-globos` es la misma foto de `f20-base40` con los globos agregados; acá se
sacan por DIFERENCIA entre las dos tiradas y quedan como PNG para animarlos encima de la
base. Las cajas (en píxeles de la tirada 9:16 de 1536×2752) quedan escritas acá (R-17).

    python scripts/p18-oct-globos.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = Path(__file__).resolve().parent.parent
GEN = RAIZ / "raw/hilton/piso18/oct/gen"
OUT = RAIZ / "public/assets/hilton/piso18/oct"

# nombre: (caja x0, y0, x1, y1 · hasta dónde llegan los globos · columna de las cintas x0, x1)
CAPAS = {
    "f2010-globos-izq.png": ((140, 1220, 540, 1920), 1595, (270, 440)),
    "f2010-globos-der.png": ((1010, 1260, 1380, 1920), 1615, (1110, 1290)),
}

A = Image.open(GEN / "f20-base40.jpg").convert("RGB")
B = Image.open(GEN / "f20-globos.jpg").convert("RGB")
d = np.abs(np.asarray(A, dtype=np.float32) - np.asarray(B, dtype=np.float32)).max(axis=2)
m = Image.fromarray(((d > 20) * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(7))
# los globos: se abre la máscara (erosiona y dilata) para botar las motas sueltas — las dos
# tiradas no son idénticas al píxel y las luces del fondo también «difieren»
globos = m.filter(ImageFilter.MinFilter(17)).filter(ImageFilter.MaxFilter(27))
m = m.filter(ImageFilter.MaxFilter(9))
for nombre, ((x0, y0, x1, y1), fondo, (c0, c1)) in CAPAS.items():
    alfa = np.asarray(m.crop((x0, y0, x1, y1)), dtype=np.float32).copy()
    alfa[: fondo - y0] = np.asarray(globos.crop((x0, y0, x1, fondo)), dtype=np.float32)
    # bajo los globos sólo van las cintas: una columna angosta, que se desvanece hacia el amarre
    h = y1 - y0
    for y in range(fondo - y0, h):
        alfa[y, : max(0, c0 - x0)] = 0
        alfa[y, c1 - x0:] = 0
        alfa[y] *= max(0.0, 1 - (y - (fondo - y0)) / (h - (fondo - y0)) * 0.9)
    alfa = Image.fromarray(alfa.astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))
    capa = B.crop((x0, y0, x1, y1)).convert("RGBA")
    capa.putalpha(alfa)
    capa.save(OUT / nombre)
    print(f"✓ {nombre} ← f20-globos.jpg caja ({x0}, {y0}, {x1}, {y1}) · {capa.size[0]}×{capa.size[1]}")

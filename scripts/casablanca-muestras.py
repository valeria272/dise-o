#!/usr/bin/env python3
"""Muestras verticales de tabla, recortadas de la FOTO OFICIAL del producto.

La muestra es «el cuadro que muestra a detalle el producto» (Paulina, 25-08-2026):
por eso sale de la foto de pisoscasablanca.cl y no del render del ambiente. Ahí es
donde se ven las marcas de sierra del Aserrado y los nudos del roble.

Proporción medida en las piezas de Paulina: 139,7 × 470 px sobre 1080 → 1 : 3,365.
La veta corre VERTICAL, así que la foto (que viene con la tabla horizontal) se gira.

Salida: public/assets/casablanca/muestra_<sku>.png
"""
import os
import pathlib
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

RAIZ = pathlib.Path(str(_RAIZ))
FUENTE = RAIZ / "raw/casablanca/productos-sitio"
DEST = RAIZ / "public/assets/casablanca"
RAZON = 470 / 139.7          # alto / ancho, medido
ANCHO = 460                  # master de la muestra

# Qué franja de la foto se usa. (x0, y0) en fracción, y el ancho de la franja.
# Se eligió a ojo sobre cada foto para que la muestra caiga en una tabla entera y
# muestre lo que distingue al producto.
RECORTES = {
    "natural_uv_grande": ("roble-natural-143x190x1900.jpg", 0.06, 0.02, 0.90),
    "natural_uv_chico": ("roble-122x150x1900-chapa-2-mm-color-natural.jpg", 0.05, 0.02, 0.90),
    "aserrado": ("roble-aserrado-14.jpg", 0.02, 0.02, 0.95),
    "cumaru": ("camaru-uv.jpg", 0.02, 0.025, 0.62),
}


def main():
    alto = int(round(ANCHO * RAZON))
    for sku, (archivo, fx, fy, fw) in RECORTES.items():
        im = Image.open(FUENTE / archivo).convert("RGB")
        W, H = im.size
        # se toma una franja HORIZONTAL larga y se gira: así la veta queda vertical
        x0, y0 = int(W * fx), int(H * fy)
        w = int(W * fw)
        h = max(8, int(round(w / RAZON)))
        h = min(h, H - y0)
        w = min(w, int(round(h * RAZON)), W - x0)
        franja = im.crop((x0, y0, x0 + w, y0 + h)).rotate(-90, expand=True)
        franja = franja.resize((ANCHO, alto), Image.LANCZOS)
        destino = DEST / f"muestra_{sku}.png"
        franja.save(destino)
        print(f"  ✓ {destino.name}  {franja.size}  (de {archivo})")


if __name__ == "__main__":
    main()

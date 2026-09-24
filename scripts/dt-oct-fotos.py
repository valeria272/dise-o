#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · OCTUBRE 2026 — recorta y revela las fotos de las piezas de octubre.

Todas son del banco profesional del hotel (`JPG DT,QB,BW,HABITACIÓNES`,
`1XhKQS8XlQTLCSk_59ZVjbs8tqnAroz7n`), bajadas en alta a
`raw/hilton/dt/sesion-real/alta/`. Nada generado con IA.

Revelado: el mismo del estático de Honors (contraste ×1,06, sin tocar el color).

Uso:  python scripts/dt-oct-fotos.py [--solo ft-hab]
"""
import argparse
import sys
from pathlib import Path

from PIL import Image, ImageEnhance

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
Image.MAX_IMAGE_PIXELS = None

RAIZ = Path(__file__).resolve().parent.parent
ALTA = RAIZ / "raw/hilton/dt/sesion-real/alta"
SALIDA = RAIZ / "public/assets/hilton/dt/oct"

# nombre → (archivo, ancho, alto, centro x, centro y, zoom)
# El centro es la fracción de la foto donde cae el centro del recorte; zoom 1 =
# el recorte más grande que entra con esa proporción.
FOTOS = {
    # ST 01-10 Family Time — escena 1: habitación de dos camas (la familia
    # entra en dos camas; «Habitación doble» es el primer incluido).
    "ft-hab": ("HDT_57.jpg", 2250, 4000, 0.70, 0.60, 1.0),
    # escena 2: el desayuno buffet, tercer incluido.
    "ft-desayuno": ("HDT_60.jpg", 2250, 4000, 0.48, 0.50, 1.0),
    # ST 13-10 Servicios — fondo: el lobby lounge (va desenfocado detrás del
    # cristal, como la referencia).
    "sv-fondo": ("HDT_36-lobby.jpg", 2250, 4000, 0.50, 0.55, 1.0),
    # las tres tarjetas, en el orden de los servicios del brief
    "sv-bar": ("HDT_39.jpg", 700, 1000, 0.52, 0.55, 1.15),
    "sv-cowork": ("HDT_53.jpg", 700, 1000, 0.50, 0.55, 1.1),
    "sv-gym": ("HDT_82.jpg", 700, 1000, 0.45, 0.55, 1.1),
    # FEED 10-10 Opinión — «fondo institucional DoubleTree, colores cálidos»:
    # el lobby lounge (`HDT_37`), la más cálida del banco.
    "op-fondo": ("HDT_37.jpg", 2250, 2813, 0.50, 0.55, 1.0),
    # ST 30-10 Hilton Honors — la habitación con Santiago por la ventana.
    "hh-hab": ("HDT_67-hab-vista.jpg", 2250, 4000, 0.58, 0.55, 1.0),
}

CONTRASTE = 1.06


def recortar(im: Image.Image, ancho: int, alto: int, cx: float, cy: float, zoom: float):
    W, H = im.size
    prop = ancho / alto
    cw, ch = (H * prop, H) if W / H > prop else (W, W / prop)
    cw, ch = cw / zoom, ch / zoom
    x0 = min(max(cx * W - cw / 2, 0), W - cw)
    y0 = min(max(cy * H - ch / 2, 0), H - ch)
    return im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize(
        (ancho, alto), Image.LANCZOS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", nargs="*")
    a = ap.parse_args()
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre, (arch, w, h, cx, cy, z) in FOTOS.items():
        if a.solo and nombre not in a.solo:
            continue
        im = Image.open(ALTA / arch).convert("RGB")
        out = ImageEnhance.Contrast(recortar(im, w, h, cx, cy, z)).enhance(CONTRASTE)
        destino = SALIDA / f"{nombre}.jpg"
        out.save(destino, quality=92)
        print(f"{nombre:12s} ← {arch:22s} {w}×{h}  → {destino.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

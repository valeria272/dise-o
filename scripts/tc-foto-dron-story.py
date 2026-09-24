#!/usr/bin/env python3
"""Prepara la banda fotográfica de `st-12-10` desde una aérea REAL del dron.

    python scripts/tc-foto-dron-story.py

Diego, 24-09-2026: *"cambiemos la imagen a una de las que se tomó con el dron"*.
La story llevaba un render de IA de dos casas; ahora lleva el sitio de verdad.

**La toma: `DJI_20260807093622_0312_D`** del rodaje del 07-08. Se eligió entre
las 44 porque es la única que cuenta la historia de la pieza en un solo cuadro:
a la izquierda el **llano de Padre Hurtado** con sus parcelas y casas, a la
derecha la **ladera con el camino de ripio ocre** — o sea, la relación
ciudad ↔ proyecto que el titular enuncia.

⚠️ **El material del 07-08 es HLG y sale plano.** Sin gradar se ve lavado y
grisáceo, que es justo lo que el manual llama «no es el lugar». La receta de acá
levanta contraste, calienta la luz y recupera el verde **sin inventarle una
primavera europea**: sigue siendo agosto, con la tierra asomando.

La banda de la composición es **888 × 416** (proporción 2,135), así que de una
foto 5280 × 3956 se toma una franja horizontal — no la foto entera reescalada,
que aplastaría el encuadre.
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np
from PIL import Image, ImageEnhance

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = pathlib.Path(RAIZ) / "raw/tierracalma/fotos-reales/dron/DJI_20260807093622_0312_D.JPG"
DESTINO = pathlib.Path(RAIZ) / "public/assets/tierracalma/oct/h-dron.jpg"
ANCHO, ALTO = 888, 416
# Desde qué altura de la foto sale la franja. 0,30 deja el llano con las casas
# arriba y la ladera con el ripio abajo, que es el reparto que cuenta la historia.
DESDE = 0.30


def gradua(im: Image.Image) -> Image.Image:
    """Saca el HLG plano: contraste, calidez y verde, sin irse a la postal."""
    a = np.asarray(im).astype(float) / 255.0
    # Curva en S suave: levanta medios sin quemar el cielo ni tapar la sombra.
    a = np.clip(a, 0, 1)
    a = a * a * (3 - 2 * a) * 0.45 + a * 0.55
    # Balance: un punto de calidez, porque el original tira a gris azulado.
    a[:, :, 0] *= 1.045
    a[:, :, 2] *= 0.975
    im = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    im = ImageEnhance.Color(im).enhance(1.28)      # el verde de agosto, vivo
    im = ImageEnhance.Contrast(im).enhance(1.10)
    return ImageEnhance.Sharpness(im).enhance(1.15)


def main() -> int:
    if not ORIGEN.exists():
        print(f"✗ Falta la toma: {ORIGEN}")
        print("  El rodaje del dron vive en raw/ y NO viaja en el repo — ver el manual § 7.")
        return 1
    im = Image.open(ORIGEN).convert("RGB")
    w, h = im.size
    banda = int(w / (ANCHO / ALTO))
    y0 = int(h * DESDE)
    if y0 + banda > h:
        y0 = h - banda
    recorte = im.crop((0, y0, w, y0 + banda)).resize((ANCHO, ALTO), Image.LANCZOS)
    gradua(recorte).save(DESTINO, quality=93)
    print(f"origen  {ORIGEN.name}  {w}×{h}")
    print(f"franja  {w}×{banda} desde la fila {y0}  ({DESDE:.0%} del alto)")
    print(f"→ {DESTINO.relative_to(RAIZ)}  {ANCHO}×{ALTO}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

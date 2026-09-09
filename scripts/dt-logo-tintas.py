#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deja el logotipo principal de DT en `public/assets` en sus DOS tintas.

§B del manual (`clients/hilton/CLAUDE.md`, ley de Eli del 09-09-2026):

  1. Siempre el **logotipo principal** — el vertical de cuatro líneas
     (ícono · DoubleTree · by Hilton · SANTIAGO–VITACURA).
  2. El horizontal es excepción y **lo pide el cliente**.
  3. El color por defecto es **blanco**.
  4. Va en **azul DoubleTree** cuando el fondo es demasiado blanco y el logo se
     pierde.

El archivo de origen (`raw/hilton/dt/identidad/logos/logo-DT-principal.png`) es
blanco puro con alfa, así que la versión azul se obtiene **recoloreando el RGB y
dejando el alfa intacto** — nunca con un filtro CSS, que ensucia los bordes.

⚠️ El logotipo NO se deforma: se escala uniforme desde su proporción real.
Medida del archivo (bbox opaco): **1,2254 : 1**, y coincide con las plantillas de
márgenes de Eli (`logo-ST.png` 1,2254 · `logo-post.png` 1,2279) y con la pieza
aprobada `C1 FT N1` (1,226). Cuatro fuentes, el mismo número.

Uso:
    python scripts/dt-logo-tintas.py
"""
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/dt/identidad/logos/logo-DT-principal.png"
DESTINO = RAIZ / "public/assets/hilton/dt"
AZUL = (9, 25, 78)          # DoubleTree Blue #09194E, confirmado por medición


def recorta_al_alfa(im: Image.Image) -> Image.Image:
    """Deja el PNG pegado a su tinta: si el archivo trae aire alrededor, la
    geometría medida (ancho 167 @1080) no calzaría con lo que se dibuja."""
    caja = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    return im.crop(caja) if caja else im


def main() -> int:
    if not ORIGEN.exists():
        print(f"⛔ No está el logotipo de origen: {ORIGEN}")
        return 1

    im = recorta_al_alfa(Image.open(ORIGEN).convert("RGBA"))
    w, h = im.size
    print(f"origen recortado al alfa  {w}×{h}  proporción {w / h:.4f}")

    DESTINO.mkdir(parents=True, exist_ok=True)

    blanco = DESTINO / "logo-dt-blanco.png"
    im.save(blanco)
    print(f"→ {blanco.relative_to(RAIZ)}  ({blanco.stat().st_size // 1024} KB)")

    a = np.asarray(im).copy()
    a[..., 0], a[..., 1], a[..., 2] = AZUL          # el alfa queda intacto
    azul = DESTINO / "logo-dt-azul.png"
    Image.fromarray(a, "RGBA").save(azul)
    print(f"→ {azul.relative_to(RAIZ)}  ({azul.stat().st_size // 1024} KB)  "
          f"tinta #{AZUL[0]:02X}{AZUL[1]:02X}{AZUL[2]:02X}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

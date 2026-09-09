#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deja las dos escenas de la S4 en el formato de ENTREGA: 2250x4000 JPEG.

Las escenas salen de Nano Banana Pro en 3072x5504, que es 0,5581 de proporcion
contra el 0,5625 de una historia. La diferencia es chica pero real: si se
reescala sin mas, la pieza se estira un 0,8 % en vertical. Se hace COVER y se
recorta CENTRADO en el eje que sobra, que es lo que hizo la S3.

⚠️ Y OJO CON EL ORDEN: este script es el que decide qué foto RINDE la pieza.
El 09-09 se generó una segunda tirada del strudel (plato más chico) y NO se
volvió a correr esto antes de rendir la entrega, así que la pieza que se subió
—y que Eli aprobó— salió con la tirada 1. Cuando después sí se corrió, el repo
dejó de reproducir lo entregado. La tirada 1 quedó restaurada como
`gen-21-09-strudel.png` y la otra como `_alternativa-21-09-plato-chico.png`.
**Regla: después de regenerar una escena, correr este script ANTES de rendir, y
cerrar con `cmp` contra el archivo entregado.**

⚠️ NO se grada. El manual es explicito con esto («la comida clara se grada con
mano SUAVE»): la pasada estandar de `between-gradar.py` le quemo las altas al
croissant y el cliente lo cazo. Las dos escenas salieron ya bien expuestas —
medido, el tercio de arriba del strudel esta en L=26-45 y el de la primavera en
L=21-41, que es justo lo que el titular beige necesita— asi que tocarlas solo
puede empeorarlas.

Uso:  python scripts/between-st-s4-fotos.py
"""
import sys
from pathlib import Path
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/between/s4"
DESTINO = RAIZ / "public/assets/hilton/between/s4"
DESTINO.mkdir(parents=True, exist_ok=True)
W, H = 2250, 4000

PIEZAS = {
    "gen-21-09-strudel.png": "st-21-09-strudel.jpg",
    "gen-22-09-primavera.png": "st-22-09-primavera.jpg",
}

for src, dst in PIEZAS.items():
    im = Image.open(ORIGEN / src).convert("RGB")
    escala = max(W / im.width, H / im.height)
    nw, nh = round(im.width * escala), round(im.height * escala)
    im = im.resize((nw, nh), Image.LANCZOS)
    x, y = (nw - W) // 2, (nh - H) // 2
    im = im.crop((x, y, x + W, y + H))
    im.save(DESTINO / dst, quality=94, subsampling=1)
    print(f"  {src}  ->  {dst}  {im.size}  {(DESTINO / dst).stat().st_size // 1024} KB")

#!/usr/bin/env python3
"""
REVEX R3 — foto LIMPIA de la fachada de Temuco para el brief de septiembre.

La única copia en alta de esa foto es la gráfica de febrero 2026 (2250x2250) con
el texto encima. MEDIDO: la fachada está intacta hasta y=1100; de ahí para abajo
todo el pavimento tiene gráfica (incluidos filetes finos que no se ven a simple
vista). Así que se usa SOLO la zona limpia:

  · FEED  — crop cuadrado con zoom sobre la señalética. 100 % foto real.
  · STORY — la fachada arriba y el resto en degradado oscuro limpio. Nada de
            texturas clonadas ni desenfoques parciales (Paulina: "si se desenfoca,
            se desenfoca completa").
"""
import os, sys
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ

SRC  = RAIZ / "raw/revex/ref/feb_post-temuco.png"
DEST = RAIZ / "public/assets/revex/sep"; DEST.mkdir(parents=True, exist_ok=True)

src = Image.open(SRC).convert("RGB"); W, H = src.size
LIMPIO_HASTA = 1100          # medido


# ---------- FEED 2250x2250 : crop cuadrado sobre la señalética --------------
alto  = LIMPIO_HASTA
ancho = alto                                   # 1:1
x0    = 470                                    # centra GRUPOREVEX + etersol y deja el panel completo
feed  = src.crop((x0, 0, x0 + ancho, alto)).resize((2250, 2250), Image.LANCZOS)
feed.save(DEST/"temuco_fachada_feed.jpg", quality=95)
print("temuco_fachada_feed.jpg  2250x2250  (crop", x0, "..", x0+ancho, "· 100% foto real)")

# ---------- STORY 2250x4000 : crop vertical de la misma zona limpia --------
# 9:16 sobre 1100 px de alto limpio => 619 px de ancho. Queda cerrado, pero es
# 100 % foto real y el bloque rojo de la gráfica vieja queda fuera del encuadre.
alto_s  = LIMPIO_HASTA
ancho_s = int(round(alto_s * 2250 / 4000))
xs      = 455
story = src.crop((xs, 0, xs + ancho_s, alto_s)).resize((2250, 4000), Image.LANCZOS)
story.save(DEST/"temuco_fachada_story.jpg", quality=95)
print("temuco_fachada_story.jpg 2250x4000  (crop", xs, "..", xs+ancho_s, "· 100% foto real)")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PISO18 · S4 ronda 6 — el primer plano de la historia animada del 23-09.

    python scripts/p18-s4-r6.py

⭐ EL ENCARGO, LITERAL (grilla de septiembre, hoja STORIES, columna M, 17-09-2026):

    «Aquí, pedimos que cambiaran la primera imagen que sale, que no sea ese
     video, sino que otra foto de arreglos»

El comentario es NUEVO —se prepende sobre el anterior— y la celda volvió de
`CORREGIDO` a `EN CAMBIOS`. Verificado por diff de CONJUNTO de cadenas contra
`clients/hilton/grillas/api/p18-sept-20260916.json`, que es la única forma de
verlo: la celda «modificada» no se nota y el comentario viejo sigue debajo.

⭐ Y en la MISMA celda, el comentario *«Podría ser un texto orientado a ''Dejando
todo listo, para que solo te preocupes de celebrar''»* aparece ahora **TACHADO**.
En la ronda 4 se quitó esa bajada porque la grilla la había borrado, y quedó
anotado como duda abierta. El tachado la cierra: la bajada NO vuelve.

══════════════════════════════════════════════════════════════════════════════
QUÉ ENTRA EN LUGAR DEL VIDEO — `piso_18-101`
══════════════════════════════════════════════════════════════════════════════
El plano 1 era `salon-vacio.mp4`, un recorte del `IMG_4177.MOV` con el salón sin
montar. Entró en la ronda 3 por un pedido de Eli («trata de buscar una que se vea
más vacía») y es justo lo que el cliente ahora saca.

Se elige `piso_18-101` de `Piso 18_28 ago decoración 2024` —la sesión que Eli
mandó usar para todo lo de flores— y NO es una elección de gusto:

  1. **Es una foto de arreglos**, que es lo único que pidió el cliente: el arreglo
     alto ocupa el centro del cuadro y es el protagonista.
  2. **Conserva la progresión** de vacío a montado que Eli fijó en la ronda 3: el
     piso está desnudo, el salón todavía no tiene mesas puestas.
  3. **Es el mismo arreglo que el plano 2** (`mt-90`, de `piso_18-90`), visto de
     lejos. O sea que el primer empuje hace literalmente lo que Eli describió:
     *«hace como una transición de una foto y se mueve hacia el otro lado y
     aparece la misma foto, u otra con más montaje»*.
  4. Sin rostros y sin el logotipo de la pared — las dos cosas que Eli pidió
     cuidar en esta cuenta.

⚠️ EL RECORTE, ANOTADO (regla 3 del criterio de Eli, `clients/piso18/reglas.yaml`):

    origen  raw/hilton/piso18/deco-ago2024/piso_18-101.jpg   3840×5760
    caja    3240×5760 desde (300, 0)          ← centrada, deja 300 px a cada lado
    destino public/assets/hilton/piso18/mt-101.jpg           1080×1920
    reduce  1080/3240 = 0,333                 ← nunca amplía

El tope de zoom de esta marca es 1,0 —«un recorte que ampliaría se rechaza, no se
fuerza»—. Acá se reduce a un tercio, así que sobra resolución de lejos.
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/piso18/deco-ago2024/piso_18-101.jpg"
DESTINO = RAIZ / "public/assets/hilton/piso18/mt-101.jpg"

# La caja, escrita. (x0, y0, ancho, alto) sobre el original.
CAJA = (300, 0, 3240, 5760)
SALIDA = (1080, 1920)


def main() -> int:
    if not ORIGEN.exists():
        sys.exit(f"✗ No está el original: {ORIGEN}\n"
                 "  Es material de `raw/`, que no viaja en git — bájalo del Drive.")

    im = Image.open(ORIGEN)
    x0, y0, w, h = CAJA
    if x0 + w > im.width or y0 + h > im.height:
        sys.exit(f"✗ La caja {CAJA} no cabe en {im.size}.")

    reduce = SALIDA[0] / w
    if reduce > 1.0:
        # ⛔ El tope de la marca. Si algún día hace falta un plano más cerrado, se
        #    vuelve al banco a buscarlo; esta foto no se fuerza.
        sys.exit(f"✗ El recorte AMPLIARÍA (×{reduce:.3f}). Se rechaza, no se fuerza.")

    corte = im.crop((x0, y0, x0 + w, y0 + h)).resize(SALIDA, Image.LANCZOS)
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    corte.save(DESTINO, quality=94, subsampling=0)

    kb = DESTINO.stat().st_size // 1024
    print(f"origen   {ORIGEN.name}  {im.width}×{im.height}")
    print(f"caja     {w}×{h} desde ({x0}, {y0})   reduce ×{reduce:.3f}")
    print(f"✓ {DESTINO.relative_to(RAIZ)}  {SALIDA[0]}×{SALIDA[1]}  ({kb} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

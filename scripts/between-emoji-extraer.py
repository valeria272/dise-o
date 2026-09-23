#!/usr/bin/env python3
"""Saca los cuatro emojis de la lámina 2 APROBADA del carrusel de cumpleaños y
los deja como PNG con transparencia en public/assets/hilton/between/emoji/.

POR QUÉ EXISTE ESTO
-------------------
La pieza aprobada de Eli lleva emojis de estilo Apple. En Windows, Chrome cae en
`Segoe UI Emoji` y el ☕ sale LILA — es el defecto que ella ya había cazado en
los renders del estudio («el ☕ lila […] es un defecto de la pila de fuentes en
Windows, no de diseño»). Apple Color Emoji no se puede redistribuir, así que en
vez de imitarlos se recortan LOS DE LA PIEZA APROBADA: son la obra del propio
cliente y calzan exacto con el carrusel.

Las cajas están medidas a mano sobre `C1 S2 CUMPLE N2.png` en coordenadas de
lienzo 1080; el archivo es 2250 de ancho, así que se escalan por 2250/1080.

Uso:  python3 scripts/between-emoji-extraer.py
"""
import pathlib
import sys

import numpy as np
from PIL import Image

# La consola de Windows entrega cp1252 y estos mensajes llevan acentos y ✓.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTE = RAIZ / 'raw/hilton/between/de-eli/cumple-s2-v2/C1 S2 CUMPLE N2.png'
DESTINO = RAIZ / 'public/assets/hilton/between/emoji'

# nombre -> caja (x0, y0, x1, y1) en coordenadas @1080
CAJAS = {
    'cafe':     (730, 388, 779, 430),
    'regalo':   (642, 504, 690, 550),
    'estrella': (639, 617, 685, 663),
    'sonrisa':  (731, 703, 773, 745),
}


def extraer(im, caja, s):
    """Recorta y saca el fondo taupe con una máscara suave.

    El fondo se estima con la MEDIANA del anillo de borde (no con el color de
    marca) porque la caja taupe va a 0,93 de opacidad sobre la foto: detrás de
    cada emoji el color real varía un poco. Después se des-premultiplica para
    que los bordes suaves no arrastren el tinte del taupe.
    """
    x0, y0, x1, y1 = caja
    c = np.array(im.crop((int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s)))).astype(float)
    ring = np.concatenate([c[0:3].reshape(-1, 3), c[-3:].reshape(-1, 3),
                           c[:, 0:3].reshape(-1, 3), c[:, -3:].reshape(-1, 3)])
    bg = np.median(ring, 0)
    d = np.sqrt(((c - bg) ** 2).sum(2))
    al = np.clip((d - 16) / 28, 0, 1)
    al = al * al * (3 - 2 * al)                     # smoothstep
    rgb = np.clip(bg + (c - bg) / np.maximum(al, 0.05)[..., None], 0, 255)
    rgb = np.where(al[..., None] > 0.999, c, rgb)   # el interior queda intacto
    return Image.fromarray(np.dstack([rgb, al * 255]).astype(np.uint8), 'RGBA')


def main():
    im = Image.open(FUENTE).convert('RGB')
    s = im.width / 1080
    DESTINO.mkdir(parents=True, exist_ok=True)
    for nombre, caja in CAJAS.items():
        e = extraer(im, caja, s)
        e.save(DESTINO / f'{nombre}.png')
        print(f'  ✓ {nombre}.png  {e.size[0]}×{e.size[1]}')


if __name__ == '__main__':
    main()

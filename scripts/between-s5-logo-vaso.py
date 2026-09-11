#!/usr/bin/env python3
"""
Estampa el logotipo real de BETWEEN sobre el vaso To Go GIGANTE de la ST del
28-09 (S5), que viene INCLINADO.

Por qué hace falta otro script
------------------------------
`between-logo-vaso.py` resuelve el caso normal: vaso vertical, logotipo
horizontal. Acá el vaso va tumbado ~24° sobre el hombro de la chica, y un
logotipo horizontal estampado sobre un cilindro inclinado se lee **pegado**:
la línea de base no sigue al objeto. Es la misma familia de error que el
cliente cazó en la ronda 5 («el vaso de café nada que ver jajajaja»).

⛔ LA REGLA DEL 31-08 SIGUE EN PIE: EL LOGOTIPO NO SE DEFORMA.
Lo que se hace acá es una **rotación rígida** — una transformación que conserva
la forma y la proporción exactas de la marca (3,0278:1, medida sobre la tinta
del propio archivo). No hay comba cilíndrica, no hay acortado lateral, no hay
alto independiente del ancho. Rotar no es deformar; arquear sí.

Cómo decide dónde va
--------------------
Las dos proporciones salen de MEDIR la foto real del vaso vigente
(`togo-vaso-real-nobg.png`), no de estimarlas a ojo:

  · el bloque del logotipo ocupa **0,75 del ancho del vaso** a esa altura;
  · su centro cae a **0,43 del alto del CUERPO** (desde el borde de la tapa).

Y el ancho horizontal de una fila del vaso inclinado NO es su diámetro: hay que
corregirlo por `cos(ángulo)`, o el logotipo sale un 10 % más grande de la cuenta.

La fusión es la misma de `between-logo-vaso.py`: MULTIPLY contra el cartón,
la tinta se apaga donde el vaso ya está en sombra y no llega a negro puro
(sobre kraft la serigrafía deja ver la fibra).

Uso:
    python scripts/between-s5-logo-vaso.py <entrada> <salida> \
        --centro CX CY --ancho W --angulo -24 [--fuerza 0.95] [--absorcion 0.18]
"""
import argparse
import math
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
LOGO = RAIZ / 'public/assets/hilton/between/logo-negro.png'


def logo_rigido(ruta, ancho, angulo):
    """Devuelve el logotipo recortado a su tinta, escalado UNIFORMEMENTE a
    `ancho` y rotado `angulo` grados. Ninguna de las tres operaciones altera
    su proporción."""
    im = Image.open(ruta).convert('RGBA')
    a = np.asarray(im)
    ys, xs = np.nonzero(a[:, :, 3] > 8)
    im = im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))

    ratio = im.width / im.height           # 3,0278 en el archivo oficial
    alto = max(int(round(ancho / ratio)), 2)
    im = im.resize((ancho, alto), Image.LANCZOS)

    # expand=True para que la rotación no recorte las esquinas del bloque
    return im.rotate(angulo, resample=Image.BICUBIC, expand=True), ratio


def estampar(base, logo, centro, fuerza, absorcion):
    """MULTIPLY del logotipo sobre el cartón, respetando la sombra del vaso.

    Copiado de `between-logo-vaso.py` — mismo criterio, para que las dos piezas
    de To Go se vean con la misma serigrafía."""
    cx, cy = centro
    x1 = int(round(cx - logo.width / 2))
    y1 = int(round(cy - logo.height / 2))

    X1, Y1 = max(x1, 0), max(y1, 0)
    X2, Y2 = min(x1 + logo.width, base.width), min(y1 + logo.height, base.height)
    if X2 <= X1 or Y2 <= Y1:
        raise SystemExit('el logo cae completamente fuera de la imagen')
    logo = logo.crop((X1 - x1, Y1 - y1, X2 - x1, Y2 - y1))

    zona = np.asarray(base.crop((X1, Y1, X2, Y2))).astype(np.float64)
    lg = np.asarray(logo).astype(np.float64)

    tinta_lum = lg[:, :, :3].mean(axis=2) / 255.0        # 0 = tinta, 1 = papel
    alfa = lg[:, :, 3] / 255.0
    densidad = alfa * (1.0 - tinta_lum) * fuerza

    # la tinta sigue la sombra del vaso: no ilumina lo que ya está oscuro
    lum = (0.299 * zona[..., 0] + 0.587 * zona[..., 1] + 0.114 * zona[..., 2]) / 255.0
    densidad *= np.clip(lum * 1.25, 0.25, 1.0)

    fuera = zona * (1.0 - densidad[..., None] * (1.0 - absorcion))

    base = base.copy()
    base.paste(Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)), (X1, Y1))
    return base, (X1, Y1, X2, Y2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--centro', nargs=2, type=int, required=True, metavar=('CX', 'CY'))
    ap.add_argument('--ancho', type=int, required=True,
                    help='ancho del logotipo ANTES de rotar, sobre la superficie del vaso')
    ap.add_argument('--angulo', type=float, required=True,
                    help='grados; negativo = el extremo derecho baja (vaso inclinado a la derecha)')
    ap.add_argument('--fuerza', type=float, default=0.95)
    ap.add_argument('--absorcion', type=float, default=0.18)
    ap.add_argument('--logo', default=str(LOGO))
    a = ap.parse_args()

    base = Image.open(a.entrada).convert('RGB')
    logo, ratio = logo_rigido(a.logo, a.ancho, a.angulo)
    fuera, caja = estampar(base, logo, tuple(a.centro), a.fuerza, a.absorcion)
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    fuera.save(a.salida)

    print(f'logotipo: proporcion {ratio:.4f} (intacta) · ancho {a.ancho} · '
          f'angulo {a.angulo}° · bloque rotado {logo.width}x{logo.height}')
    print(f'estampado en {caja}  ->  {a.salida}')


if __name__ == '__main__':
    main()

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

⛔ LA REGLA DEL 31-08 SIGUE EN PIE: EL LOGOTIPO NO SE DEFORMA A MANO.
La transformación base es una **rotación rígida** — conserva la forma y la
proporción exactas de la marca (3,0278:1, medida sobre la tinta del propio
archivo). No hay alto independiente del ancho.

⭐ RONDA 3 (11-09) — `--radio`: la envoltura cilíndrica, que SÍ corresponde
Eli: «que el logo se vea más centrado al vaso, como un mockup. El logo debe
verse realista que está en el vaso, como los originales».

`--radio` aplica la **proyección cilíndrica real**: el logotipo se trata como
impreso sobre la superficie del vaso, así que su ancho plano es un ARCO y lo que
se ve en pantalla es su CUERDA. Cada columna se coloca en `x = R·sin(s/R)`, con
`s` la distancia sobre el papel. Eso comprime progresivamente hacia los bordes y
es exactamente lo que hace la realidad.

**No es la comba del 31-08.** Aquella era una sinusoide inventada con un acortado
lateral fijo del 18 % que arqueaba la línea de base y aplastaba las letras de los
extremos hasta que «COFFEE & BAR» quedaba irreconocible. Acá:
  · el radio sale de MEDIR el ancho aparente del propio vaso, no se elige;
  · la línea de base queda RECTA (no se arquea nada);
  · con el logotipo ocupando 0,4 del diámetro, la compresión máxima —en el
    borde— es de un 8 %, y es progresiva.
Si `--radio` no se pasa, el comportamiento es el de antes: rotación rígida sola.

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


def envolver(logo, radio):
    """Proyecta el logotipo sobre un cilindro de `radio` px visto de frente.

    El ancho del logotipo es la longitud del ARCO que ocupa sobre el papel; lo
    que se ve en pantalla es la CUERDA. Para cada columna de salida a distancia
    `d` del centro, el punto que le corresponde en el logotipo plano está a
    `s = R·asin(d/R)` del centro. La línea de base no se toca: sólo se comprime
    en horizontal, y de forma progresiva.
    """
    W, H = logo.size
    if radio <= 0 or W / 2 >= radio:
        return logo                      # el logotipo no cabe en el cilindro
    theta = (W / 2) / radio              # medio arco, en radianes
    ancho_vis = int(round(2 * radio * math.sin(theta)))
    a = np.asarray(logo).astype(np.float64)
    d = np.linspace(-ancho_vis / 2, ancho_vis / 2, ancho_vis)
    s = radio * np.arcsin(np.clip(d / radio, -1, 1))      # posición sobre el papel
    col = np.clip(s + W / 2, 0, W - 1)
    i0 = np.floor(col).astype(int); i1 = np.minimum(i0 + 1, W - 1)
    t = (col - i0)[None, :, None]
    fuera = a[:, i0, :] * (1 - t) + a[:, i1, :] * t
    return Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8), 'RGBA')


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
    ap.add_argument('--radio', type=int, default=0,
                    help='radio aparente del vaso en px; activa la envoltura cilíndrica')
    ap.add_argument('--logo', default=str(LOGO))
    a = ap.parse_args()

    base = Image.open(a.entrada).convert('RGB')
    logo, ratio = logo_rigido(a.logo, a.ancho, a.angulo)
    plano = logo.width
    if a.radio:
        logo = envolver(logo, a.radio)
    fuera, caja = estampar(base, logo, tuple(a.centro), a.fuerza, a.absorcion)
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    fuera.save(a.salida)

    print(f'logotipo: proporcion {ratio:.4f} (intacta) · ancho {a.ancho} · '
          f'angulo {a.angulo}° · bloque {logo.width}x{logo.height}')
    if a.radio:
        import math as _m
        th = _m.degrees((plano / 2) / a.radio)
        print(f'  envoltura cilindrica: radio {a.radio} px · el logotipo abarca '
              f'{2*th:.1f}° del vaso · compresion en el borde {_m.cos(_m.radians(th))*100:.1f} % '
              f'· ancho aparente {logo.width} (plano {plano})')
    print(f'estampado en {caja}  ->  {a.salida}')


if __name__ == '__main__':
    main()

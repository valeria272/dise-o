#!/usr/bin/env python3
"""
Estampa el logo BETWEEN sobre el vaso To Go de una imagen generada con IA.

Por qué existe
--------------
Ronda 4 de septiembre 2026: el cliente pidió lo mismo en TRES piezas distintas
—«Café con logo Between!», «que el vaso tenga logo», «que el vaso sea como el
del resto de las slides»—. La causa es una sola: **los generadores de imagen
devuelven el vaso kraft liso, sin marca**. Las fotos reales del cliente sí lo
traen, así que la regla es usar foto real siempre que exista; este script es
para cuando la escena NO existe en el banco (el vaso con vela de cumpleaños,
las manos entregando el café) y hay que conservar el fondo ya aprobado.

Cómo lo hace
------------
No pega el PNG plano —se nota—. Lo envuelve sobre el cilindro del vaso:
  1. curva el logo con un desplazamiento vertical sinusoidal (el borde del vaso
     cae respecto al centro) y lo estrecha en los costados, que es lo que hace
     la perspectiva de un cilindro;
  2. lo funde en modo MULTIPLY contra el cartón, para que tome su textura y su
     sombra en vez de flotar encima;
  3. respeta la iluminación: la opacidad baja en la zona donde el vaso ya está
     en sombra, medida sobre la propia imagen.

Uso:
    python3 scripts/between-logo-vaso.py <entrada> <salida> \
        --caja X1 Y1 X2 Y2      # rectángulo del cuerpo del vaso donde va el logo
        [--curva 0.16]          # 0 = plano · 0,25 = muy cilíndrico
        [--fuerza 0.86]         # cuánto marca la tinta
"""
import argparse

import numpy as np
from PIL import Image, ImageDraw

RAIZ = __file__.rsplit('/scripts/', 1)[0]
LOGO = f'{RAIZ}/public/assets/hilton/between/logo-negro.png'


def curvar(logo, curva):
    """Envuelve el logo sobre un cilindro: comba vertical + acortado lateral."""
    a = np.asarray(logo).astype(np.float64)
    h, w = a.shape[:2]
    salida = np.zeros_like(a)
    xs = np.arange(w)
    # u va de -1 (borde izq) a +1 (borde der) del arco visible del vaso
    u = (xs / max(w - 1, 1)) * 2 - 1
    # el centro del logo sube y los extremos bajan: eso es la comba del cilindro
    desliz = curva * h * (u ** 2)
    # y los extremos se comprimen porque el cilindro se aleja de la cámara
    escala = 1.0 - 0.18 * (u ** 2)
    for i, x in enumerate(xs):
        col = a[:, x, :]
        alto = max(int(round(h * escala[i])), 2)
        # remuestreo vertical de la columna
        idx = np.linspace(0, h - 1, alto)
        col_esc = np.stack([np.interp(idx, np.arange(h), col[:, c]) for c in range(a.shape[2])], axis=1)
        arriba = int(round(desliz[i] + (h - alto) / 2))
        fin = min(arriba + alto, h)
        ini = max(arriba, 0)
        if fin > ini:
            salida[ini:fin, x, :] = col_esc[(ini - arriba):(fin - arriba), :]
    return Image.fromarray(salida.astype(np.uint8))


def limpiar_zona(im, caja):
    """Borra un logotipo inventado por la IA clonando el cartón inmediatamente
    de arriba. El vaso es liso en vertical, así que la clonación no deja costura;
    se difumina el empalme para que no aparezca un rectángulo."""
    from PIL import ImageFilter
    x1, y1, x2, y2 = caja
    alto = y2 - y1
    origen = im.crop((x1, max(y1 - alto - 6, 0), x2, max(y1 - 6, alto)))
    if origen.height < alto:
        origen = origen.resize((x2 - x1, alto), Image.LANCZOS)
    parche = origen.resize((x2 - x1, alto), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
    mascara = Image.new('L', (x2 - x1, alto), 255)
    mascara = mascara.filter(ImageFilter.GaussianBlur(0))
    borde = Image.new('L', (x2 - x1, alto), 0)
    ImageDraw.Draw(borde).rectangle((10, 10, x2 - x1 - 10, alto - 10), fill=255)
    mascara = borde.filter(ImageFilter.GaussianBlur(9))
    im = im.copy()
    im.paste(parche, (x1, y1), mascara)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--caja', nargs=4, type=int, required=True, metavar=('X1', 'Y1', 'X2', 'Y2'))
    ap.add_argument('--curva', type=float, default=0.16)
    ap.add_argument('--fuerza', type=float, default=0.86)
    ap.add_argument('--logo', default=LOGO)
    ap.add_argument('--limpiar', nargs=4, type=int, default=None, metavar=('X1', 'Y1', 'X2', 'Y2'),
                    help='borra primero un logotipo inventado por la IA clonando el cartón de al lado')
    args = ap.parse_args()

    base = Image.open(args.entrada).convert('RGB')
    if args.limpiar:
        base = limpiar_zona(base, tuple(args.limpiar))
    x1, y1, x2, y2 = args.caja
    ancho, alto = x2 - x1, y2 - y1
    if ancho <= 0 or alto <= 0:
        raise SystemExit('la caja está vacía o invertida')

    logo = Image.open(args.logo).convert('RGBA')
    logo = logo.resize((ancho, alto), Image.LANCZOS)
    logo = curvar(logo, args.curva)

    zona = np.asarray(base.crop((x1, y1, x2, y2))).astype(np.float64)
    lg = np.asarray(logo).astype(np.float64)
    tinta = lg[:, :, :3] / 255.0
    alfa = (lg[:, :, 3] / 255.0) * args.fuerza

    # la tinta se apaga donde el cartón ya está oscuro: un logo impreso no
    # ilumina la sombra del vaso, la sigue
    lum = (0.299 * zona[:, :, 0] + 0.587 * zona[:, :, 1] + 0.114 * zona[:, :, 2]) / 255.0
    alfa = alfa * np.clip(lum * 1.25, 0.25, 1.0)

    mezcla = zona * tinta                      # MULTIPLY: toma la textura del cartón
    fuera = zona * (1 - alfa[..., None]) + mezcla * alfa[..., None]
    base.paste(Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)), (x1, y1))
    base.save(args.salida, quality=96)
    print(f'{args.salida}  logo {ancho}×{alto} en ({x1},{y1})  curva {args.curva}  fuerza {args.fuerza}')


if __name__ == '__main__':
    main()

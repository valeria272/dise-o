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

⛔ RONDA 5 (31-08-2026) — POR QUÉ ESTE SCRIPT SE REESCRIBIÓ
-----------------------------------------------------------
La versión anterior **deformaba el logotipo** y el cliente lo cazó:
«El vaso de café tiene el logo de between completamente distinto» y
«el vaso de café nada que ver jajajaja» (Scarlette Muñoz, 31-08).

Tenía DOS deformaciones encadenadas:

1. `logo.resize((ancho, alto))` metía el logo en la caja que le pasaran,
   **ignorando su proporción real**. Si la caja no venía en 3,0298:1, el
   logotipo salía achatado o estirado. Medido en las piezas entregadas:
   ratios de **2,18 · 2,28 · 2,33** contra el 3,03 real.
2. `curvar()` lo envolvía sobre un cilindro con una comba sinusoidal y un
   acortado lateral del 18 %. Eso **arquea la línea de base y aplasta las
   letras de los extremos**: «COFFEE & BAR» quedaba irreconocible y la «R»
   final se leía como «Ꞅ».

**La regla ahora: el logotipo NO se deforma. Nunca.**
Es una marca registrada; su forma es intocable. Un logo impreso sobre un vaso
se integra por **tono** (multiply contra el cartón, respetando su sombra), no
por geometría. Si la curvatura del vaso se nota demasiado, la respuesta es
**achicar el logo o correrlo al centro del vaso** —donde el cilindro es
ópticamente plano—, jamás doblarlo.

Cómo lo hace ahora
------------------
  1. Escala el logo **uniformemente**: se le da el ancho y el alto sale de la
     proporción real del propio archivo. No hay forma de pedir otra cosa.
  2. Lo funde en MULTIPLY contra el cartón, así toma su textura y su veta en
     vez de flotar encima.
  3. Respeta la iluminación: la tinta se apaga donde el vaso ya está en
     sombra, medido sobre la propia imagen.
  4. La tinta no llega a negro puro (`--absorcion`): sobre kraft, la
     serigrafía real deja ver la fibra del cartón.

Uso:
    python3 scripts/between-logo-vaso.py <entrada> <salida> \
        --centro CX CY --ancho W    # dónde y de qué ancho va el logo
        [--limpiar X1 Y1 X2 Y2]     # borra antes el logotipo que inventó la IA
        [--fuerza 0.95]

También acepta `--caja X1 Y1 X2 Y2` por compatibilidad: se usa su centro y su
ancho, y **el alto se recalcula** con la proporción real (se ignora el que
venga en la caja).
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
LOGO = RAIZ / 'public/assets/hilton/between/logo-negro.png'


def proporcion(logo):
    """Ancho/alto REAL del logotipo, medido sobre su propia tinta.

    Se mide con el canal alfa y no con el tamaño del lienzo: si el PNG trae
    margen transparente, el lienzo miente sobre la proporción de la marca.
    """
    a = np.asarray(logo)
    if a.shape[2] == 4:
        ys, xs = np.where(a[:, :, 3] > 8)
        if len(xs):
            return (xs.max() - xs.min() + 1) / (ys.max() - ys.min() + 1)
    return logo.width / logo.height


def _parche_lateral(im, caja, muestra=14):
    """Reconstruye la zona interpolando el cartón que queda a sus dos costados.

    Para cada fila toma una franja de `muestra` px a la izquierda y otra a la
    derecha del logo, promedia cada una y cruza en degradado de una a otra. Le
    devuelve al parche el grano del cartón copiando la textura de la franja
    izquierda, para que no quede una mancha lisa entre cartón con veta.
    """
    x1, y1, x2, y2 = caja
    ancho, alto = x2 - x1, y2 - y1
    a = np.asarray(im).astype(np.float64)

    ix1 = max(x1 - muestra, 0)
    dx2 = min(x2 + muestra, im.width)
    izq = a[y1:y2, ix1:x1].mean(axis=1) if x1 > ix1 else a[y1:y2, x1:x1 + 1].mean(axis=1)
    der = a[y1:y2, x2:dx2].mean(axis=1) if dx2 > x2 else a[y1:y2, x2 - 1:x2].mean(axis=1)

    t = np.linspace(0.0, 1.0, ancho)[None, :, None]
    plano = izq[:, None, :] * (1 - t) + der[:, None, :] * t

    # grano: la desviación de la franja izquierda respecto de su propia media,
    # repetida a lo ancho. Devuelve la veta del cartón sin repetir un dibujo.
    franja = a[y1:y2, ix1:x1] if x1 > ix1 else a[y1:y2, x1:x1 + 1]
    grano = franja - franja.mean(axis=1, keepdims=True)
    veces = int(np.ceil(ancho / max(grano.shape[1], 1)))
    grano = np.tile(grano, (1, veces, 1))[:, :ancho, :] * 0.7

    return Image.fromarray(np.clip(plano + grano, 0, 255).astype(np.uint8))


def limpiar_zona(im, caja, desde='auto'):
    """Borra un logotipo inventado por la IA (o el mal estampado de la ronda 4)
    clonando cartón limpio del propio vaso.

    `desde` elige de dónde sale el parche:
      · 'abajo'  — por defecto en 'auto': el cuerpo del vaso suele ser lo más limpio.
      · 'arriba' — cuando abajo hay MANOS sujetando el vaso; clonar de abajo
                   traería los dedos y dejaría un fantasma (pasó en `cumple-manos`).
      · 'lados'  — cuando NI arriba NI abajo sirve: arriba está la tapa negra y
                   abajo los dedos, que es justo el caso de `cumple-manos`.
                   Rellena cada fila interpolando el cartón limpio que queda a la
                   izquierda y a la derecha del logo. Funciona porque el vaso es
                   un cilindro vertical: dentro de una fila el tono apenas
                   cambia, y el degradado lateral se reconstruye solo.

    El empalme se difumina para que no quede un rectángulo visible.
    """
    x1, y1, x2, y2 = caja
    ancho, alto = x2 - x1, y2 - y1
    H = im.height

    holgura = 8
    cabe_abajo = y2 + holgura + alto <= H
    cabe_arriba = y1 - holgura - alto >= 0

    if desde == 'lados':
        origen = _parche_lateral(im, caja)
    elif desde == 'arriba' and cabe_arriba:
        origen = im.crop((x1, y1 - holgura - alto, x2, y1 - holgura))
    elif desde == 'abajo' and cabe_abajo:
        origen = im.crop((x1, y2 + holgura, x2, y2 + holgura + alto))
    elif cabe_abajo:
        origen = im.crop((x1, y2 + holgura, x2, y2 + holgura + alto))
    elif cabe_arriba:
        origen = im.crop((x1, y1 - holgura - alto, x2, y1 - holgura))
    else:                                           # último recurso: estirar lo que haya
        arriba = max(y1 - holgura - alto, 0)
        origen = im.crop((x1, arriba, x2, max(y1 - holgura, arriba + 1))).resize(
            (ancho, alto), Image.LANCZOS)

    parche = origen.resize((ancho, alto), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.1))

    # El difuminado del empalme va PROPORCIONAL a la zona, no fijo en 10 px.
    # Con valores fijos, en un vaso chico el anillo sin opacidad se come el
    # borde de lo que hay que borrar y el logotipo viejo asoma por arriba:
    # pasó en `togo-salida-2`, donde la zona mide 128×52 px.
    inset = max(2, min(10, min(ancho, alto) // 8))
    borde = Image.new('L', (ancho, alto), 0)
    ImageDraw.Draw(borde).rectangle((inset, inset, ancho - inset, alto - inset), fill=255)
    mascara = borde.filter(ImageFilter.GaussianBlur(max(1.0, inset * 0.9)))

    im = im.copy()
    im.paste(parche, (x1, y1), mascara)
    return im


def estampar(base, logo, centro, ancho, fuerza, absorcion):
    """Funde el logo sobre el cartón SIN tocar su forma.

    El alto sale siempre de la proporción real: la escala es uniforme y no hay
    parámetro que permita alterarla.
    """
    ratio = proporcion(logo)
    alto = max(int(round(ancho / ratio)), 2)
    logo = logo.resize((ancho, alto), Image.LANCZOS)

    cx, cy = centro
    x1, y1 = int(round(cx - ancho / 2)), int(round(cy - alto / 2))

    # recorte seguro si el logo se sale del lienzo
    X1, Y1 = max(x1, 0), max(y1, 0)
    X2, Y2 = min(x1 + ancho, base.width), min(y1 + alto, base.height)
    if X2 <= X1 or Y2 <= Y1:
        raise SystemExit('el logo cae completamente fuera de la imagen')
    logo = logo.crop((X1 - x1, Y1 - y1, X2 - x1, Y2 - y1))

    zona = np.asarray(base.crop((X1, Y1, X2, Y2))).astype(np.float64)
    lg = np.asarray(logo).astype(np.float64)

    tinta_lum = lg[:, :, :3].mean(axis=2) / 255.0        # 0 = tinta, 1 = papel
    alfa = (lg[:, :, 3] / 255.0) if lg.shape[2] == 4 else np.ones(tinta_lum.shape)
    densidad = alfa * (1.0 - tinta_lum) * fuerza

    # la tinta sigue la sombra del vaso: no ilumina lo que ya está oscuro
    lum = (0.299 * zona[..., 0] + 0.587 * zona[..., 1] + 0.114 * zona[..., 2]) / 255.0
    densidad *= np.clip(lum * 1.25, 0.25, 1.0)

    # MULTIPLY hacia un negro que NO es puro: sobre kraft se ve la fibra
    fuera = zona * (1.0 - densidad[..., None] * (1.0 - absorcion))

    base = base.copy()
    base.paste(Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)), (X1, Y1))
    return base, (X1, Y1, X2, Y2), ratio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--caja', nargs=4, type=int, metavar=('X1', 'Y1', 'X2', 'Y2'),
                    help='compatibilidad: se toma su centro y su ancho; el alto se recalcula')
    ap.add_argument('--centro', nargs=2, type=int, metavar=('CX', 'CY'))
    ap.add_argument('--ancho', type=int)
    ap.add_argument('--fuerza', type=float, default=0.95)
    ap.add_argument('--absorcion', type=float, default=0.18,
                    help='0 = tinta negra total · 0,18 = serigrafía sobre kraft (por defecto)')
    ap.add_argument('--logo', default=str(LOGO))
    ap.add_argument('--limpiar', nargs=4, type=int, default=None, metavar=('X1', 'Y1', 'X2', 'Y2'))
    ap.add_argument('--clonar', choices=('auto', 'arriba', 'abajo', 'lados'), default='auto',
                    help="de dónde sale el parche al limpiar. 'arriba' si abajo hay manos; 'lados' si arriba está la tapa Y abajo los dedos")
    args = ap.parse_args()

    if args.caja:
        x1, y1, x2, y2 = args.caja
        centro = ((x1 + x2) // 2, (y1 + y2) // 2)
        ancho = x2 - x1
    elif args.centro and args.ancho:
        centro, ancho = tuple(args.centro), args.ancho
    else:
        raise SystemExit('hace falta --caja X1 Y1 X2 Y2  o  --centro CX CY --ancho W')

    base = Image.open(args.entrada).convert('RGB')
    if args.limpiar:
        base = limpiar_zona(base, tuple(args.limpiar), args.clonar)

    logo = Image.open(args.logo).convert('RGBA')
    base, puesto, ratio = estampar(base, logo, centro, ancho, args.fuerza, args.absorcion)

    Path(args.salida).parent.mkdir(parents=True, exist_ok=True)
    base.save(args.salida, quality=96)
    px1, py1, px2, py2 = puesto
    print(f'{args.salida}  logo {px2 - px1}x{py2 - py1} en ({px1},{py1})  '
          f'proporcion {ratio:.4f} SIN deformar  fuerza {args.fuerza}')


if __name__ == '__main__':
    main()

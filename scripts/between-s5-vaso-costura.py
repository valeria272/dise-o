#!/usr/bin/env python3
"""
Borra la COSTURA vertical del vaso To Go gigante de la ST del 28-09 (S5).

Por qué existe
--------------
Ronda 3 (11-09-2026). Eli: «Tienes que borrar esa línea que se ve y que el logo
se vea más centrado al vaso, como un mockup».

La línea la pedí yo. El prompt de la ronda 2 decía «una costura vertical del
cartón» —estaba en la lista de detalles físicos que hacen que el vaso se vea
real— y el generador la puso **justo al medio de la cara visible**, partiendo el
logotipo en «BETW | EEN». En el vaso real la costura existe, pero cae al costado
y casi no se ve.

> ⭐ **La lección:** al pedirle a un generador los detalles físicos de un objeto,
> hay que decir **DÓNDE** van los que son direccionales. «Costura vertical» sin
> ubicación la pone donde más molesta, que es el centro.

Cómo lo hace
------------
La costura es una columna más oscura que su entorno sobre un cartón de textura
pareja. Para cada fila se reemplaza la franja por una interpolación del cartón
que queda a izquierda y derecha, y se le devuelve el grano copiando la textura de
la franja izquierda — el mismo criterio de `_parche_lateral` de
`between-logo-vaso.py`, que ya se usó para borrar logotipos inventados.

⚠️ Se detecta la columna por fila, no se asume recta: el vaso está levemente
inclinado y la costura sigue su eje.

Uso:
    python scripts/between-s5-vaso-costura.py <entrada> <salida> \
        --x 1982 --desde 3600 --hasta 5504 [--ancho 26] [--busqueda 40]
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


def columna_de_la_costura(g, y, x_guia, busqueda, suavizado=61):
    """Devuelve la columna más oscura respecto de su entorno, cerca de `x_guia`."""
    x0, x1 = max(x_guia - busqueda, 0), min(x_guia + busqueda, g.shape[1] - 1)
    franja = g[max(y - 6, 0):y + 7]
    perfil = franja.mean(axis=0)
    suave = np.convolve(perfil, np.ones(suavizado) / suavizado, mode='same')
    dif = (perfil - suave)[x0:x1]
    return int(np.argmin(dif)) + x0, float(dif.min())


def borrar(im, x_guia, desde, hasta, ancho, busqueda, umbral):
    a = np.asarray(im).astype(np.float64)
    g = a.mean(axis=2)
    H, W, _ = a.shape
    fuera = a.copy()
    mitad = ancho // 2
    muestra = max(ancho, 18)
    tocadas = 0
    x = x_guia

    for y in range(max(desde, 0), min(hasta, H)):
        cx, caida = columna_de_la_costura(g, y, x, busqueda)
        if caida > -umbral:              # acá la costura ya no se nota
            continue
        x = cx                            # la costura sigue el eje del vaso
        tocadas += 1
        i0, i1 = cx - mitad, cx + mitad + 1
        if i0 - muestra < 0 or i1 + muestra >= W:
            continue
        izq = a[y, i0 - muestra:i0].mean(axis=0)
        der = a[y, i1:i1 + muestra].mean(axis=0)
        t = np.linspace(0.0, 1.0, i1 - i0)[:, None]
        plano = izq[None, :] * (1 - t) + der[None, :] * t
        # grano: la desviación de la franja izquierda respecto de su media
        franja = a[y, i0 - muestra:i0]
        grano = (franja - franja.mean(axis=0)) * 0.8
        veces = int(np.ceil((i1 - i0) / max(len(grano), 1)))
        grano = np.tile(grano, (veces, 1))[:i1 - i0]
        fuera[y, i0:i1] = np.clip(plano + grano, 0, 255)

    parche = Image.fromarray(fuera.astype(np.uint8))
    # un desenfoque mínimo SÓLO sobre la banda, para que no quede un canto duro
    suave = parche.filter(ImageFilter.GaussianBlur(1.2))
    mascara = Image.new('L', im.size, 0)
    m = np.asarray(mascara).copy()
    m[max(desde, 0):min(hasta, H), max(x_guia - mitad - busqueda, 0):x_guia + mitad + busqueda] = 255
    mascara = Image.fromarray(m).filter(ImageFilter.GaussianBlur(6))
    parche = Image.composite(suave, parche, mascara)
    return parche, tocadas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--x', type=int, required=True, help='columna aproximada de la costura')
    ap.add_argument('--desde', type=int, required=True)
    ap.add_argument('--hasta', type=int, required=True)
    ap.add_argument('--ancho', type=int, default=26)
    ap.add_argument('--busqueda', type=int, default=40)
    ap.add_argument('--umbral', type=float, default=2.5,
                    help='caída mínima de luminancia para considerar que hay costura')
    a = ap.parse_args()

    im = Image.open(a.entrada).convert('RGB')
    fuera, n = borrar(im, a.x, a.desde, a.hasta, a.ancho, a.busqueda, a.umbral)
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    fuera.save(a.salida)
    print(f'costura borrada en {n} filas (de {a.hasta - a.desde})  ->  {a.salida}')


if __name__ == '__main__':
    main()

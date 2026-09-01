#!/usr/bin/env python3
"""
Acerca el tono del vaso To Go generado con IA al del vaso REAL fotografiado.

Por qué
-------
Ronda 5 (31-08-2026): «el vaso no se parece al real… se ve como quemado y
extraño. Debe verse hiperrealista».

Medido sobre el cuerpo del vaso, la sesión real del cliente
(`Double Tree 25 jul 25-257` y `-266`, las que traen el vaso VIGENTE) da un
greige pálido y casi neutro. Los montajes con IA devuelven un kraft mucho más
oscuro y del orden del DOBLE de saturación:

    REAL  frame 257     RGB(166,148,127)  lum 151  sat 39
    REAL  frame 266     RGB(178,155,134)  lum 160  sat 44
    IA    cumple-vela   RGB(112, 61, 29)  lum  73  sat 84   ← el doble de cálido
    IA    cumple-manos  RGB(164,123, 91)  lum 132  sat 73
    IA    togo-trio     RGB(138, 92, 55)  lum 101  sat 83

Ese exceso de calidez y esa falta de luz son lo que se lee como «quemado».

Qué hace
--------
Aísla el cartón del vaso dentro de la caja que se le indique y lo lleva a la
media y la saturación del vaso real, conservando su propio modelado —las
sombras siguen siendo las suyas, solo se recentra el tono—.

⚠️ Esto ACERCA el montaje, no lo vuelve una fotografía. Cuando la escena existe
en el banco del cliente, la regla del manual sigue mandando: se usa la foto real.
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

# Media del cuerpo del vaso REAL (promedio de los frames 257 y 266)
REAL_RGB = np.array([172.0, 151.5, 130.5])
REAL_SAT = 41.7


def mascara_carton(a, caja, suavizado=2.5):
    """Cartón del vaso: cálido, ni la tapa negra ni el fondo."""
    x1, y1, x2, y2 = caja
    H, W = a.shape[:2]
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    lum = .299 * R + .587 * G + .114 * B
    m = (R > B + 18) & (lum > 35) & (lum < 235)
    caj = np.zeros((H, W), bool)
    caj[max(y1, 0):min(y2, H), max(x1, 0):min(x2, W)] = True
    m = m & caj
    suave = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(suavizado))
    return np.asarray(suave).astype(np.float64) / 255.0


def corrige(entrada, salida, caja, fuerza=1.0):
    im = Image.open(entrada).convert('RGB')
    a = np.asarray(im).astype(np.float64)
    m = mascara_carton(a, caja)
    if m.sum() < 200:
        raise SystemExit('la caja no contiene cartón de vaso reconocible')

    peso = m[..., None]
    actual = (a * peso).sum((0, 1)) / peso.sum((0, 1))          # media del cartón
    gris = a.mean(2, keepdims=True)

    # 1. recentrar el tono hacia el del vaso real, sin tocar el modelado
    corregida = a + (REAL_RGB - actual)

    # 2. bajar la saturación a la del vaso real
    sat_actual = ((a.max(2) - a.min(2)) * m).sum() / m.sum()
    k = min(REAL_SAT / max(sat_actual, 1e-6), 1.0)
    corregida = gris + (corregida - gris) * k

    fuera = a * (1 - peso * fuerza) + corregida * (peso * fuerza)
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)).save(salida, quality=96)

    nueva = (np.clip(fuera, 0, 255) * peso).sum((0, 1)) / peso.sum((0, 1))
    print(f'{Path(salida).name}  cuerpo {tuple(actual.round(0).astype(int))} -> '
          f'{tuple(nueva.round(0).astype(int))}  · saturacion x{k:.2f}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--caja', nargs=4, type=int, required=True, metavar=('X1', 'Y1', 'X2', 'Y2'))
    ap.add_argument('--fuerza', type=float, default=1.0)
    a = ap.parse_args()
    corrige(a.entrada, a.salida, tuple(a.caja), a.fuerza)


if __name__ == '__main__':
    main()

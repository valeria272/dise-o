#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saca las medallas quemadas en los packshots del catálogo de CAVA.

    ~/copylab-venv/bin/python3 scripts/cava-quitar-sellos.py

POR QUÉ. Los packshots que el e-commerce publica de 7Colores Single Vineyard,
Vitis Única Cabernet y Selección de Viñedos traen el sello del premio pegado
sobre la foto. Repetidos seis veces en un banner de pack ensucian la pieza y
obligan a achicar las botellas — y además anuncian premios que el brief del mes
no declara (el Vitis trae un «RP 93» y el Selección un «91 pts» que no están en
el brief del Cyber). Coni, 01-10: «en los banners con fondo blanco quítale los
sellos; el único que tiene premio es el 7Colores Single Vineyard, y ése va en
el banner principal».

CÓMO. No se inventa nada ni se pide a un modelo que rellene: **una botella es
simétrica respecto de su eje**, así que el lado tapado se reconstruye espejando
el lado limpio. Sólo se toca la franja de filas donde está el sello, y sólo del
eje hacia el lado sucio; la etiqueta, que es lo asimétrico, queda intacta
porque los sellos van sobre el hombro, más arriba.
"""
import pathlib
import sys

import numpy as np
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BT = RAIZ / "public/assets/cava/bottles"

# Qué archivos y de qué lado sobresale el sello. La FRANJA no se declara: se
# detecta. Dársela a mano salió mal a la primera —en el Selección de Viñedos la
# franja alcanzó la etiqueta y el espejo escribió «MORAROM»—, y el dato está en
# la propia silueta: donde hay sello, el objeto es más ancho que el cuerpo.
TRABAJOS = {
    "vitis-unica-cabernet.png": "der",
}

# ⛔ Dos vinos NO están acá, y es a propósito. En los dos el sello baja hasta la
# ETIQUETA, y ahí el espejo deja de servir: la etiqueta es lo único asimétrico
# de una botella, así que reconstruirla es inventarla. El Selección de Viñedos
# quedó escrito «MORAROM» en el primer intento; el 7Colores Single Vineyard
# terminó con un parche rectangular sobre las plumas.
#   · Selección de Viñedos Gran Reserva Carmenere → se usa la foto oficial de
#     seis botellas que publica la tienda, que viene limpia.
#   · 7Colores Single Vineyard Red Blend → se deja con sus sellos reales (92
#     Descorchados y 91 James Suckling, que son los que el brief le declara)
#     hasta que la marca entregue un packshot limpio.

# ⛔ El Selección de Viñedos Gran Reserva Carmenere NO está acá y es a
# propósito: su sello baja hasta la mitad de la etiqueta y el espejo la rompía
# —escribió «MORAROM»—. Para ese pack se usa la imagen oficial de seis botellas
# que publica la tienda, que ya viene limpia. Reconstruir a mano lo que la marca
# ya tiene fotografiado es inventar; bajarlo es copiar.


def eje_del_cuerpo(al, y_fin):
    """El eje de la botella, medido abajo, donde no hay sello."""
    filas = []
    for y in range(y_fin, al.shape[0]):
        xs = np.where(al[y])[0]
        if len(xs):
            filas.append((xs.min() + xs.max()) / 2)
    return float(np.median(filas))


def franja_del_sello(al, lado, eje):
    """Las filas donde el objeto se sale del cuerpo: ahí está el sello.

    El cuerpo se mide en la mitad baja de la botella, que nunca lleva sello.
    Una fila cuenta como «con sello» si sobresale más de un 6 % del cuerpo por
    el lado sucio. Después se devuelve el bloque contiguo más alto, para no
    arrastrar la base, que también ensancha por el reflejo.
    """
    H = al.shape[0]
    bajo = range(int(H * 0.55), int(H * 0.90))
    cuerpo = []
    for y in bajo:
        xs = np.where(al[y])[0]
        if len(xs):
            cuerpo.append(xs.max() - eje if lado == "der" else eje - xs.min())
    medio = float(np.median(cuerpo))

    marcadas = []
    for y in range(0, int(H * 0.60)):
        xs = np.where(al[y])[0]
        if not len(xs):
            continue
        salida = xs.max() - eje if lado == "der" else eje - xs.min()
        if salida > medio * 1.06:
            marcadas.append(y)
    if not marcadas:
        return None
    bloques, ini = [], marcadas[0]
    for a, b in zip(marcadas, marcadas[1:]):
        if b - a > 6:
            bloques.append((ini, a)); ini = b
    bloques.append((ini, marcadas[-1]))
    y0, y1 = max(bloques, key=lambda t: t[1] - t[0])
    return max(0, y0 - 3), min(H, y1 + 4)


def limpia(nombre, lado):
    im = Image.open(BT / nombre).convert("RGBA")
    im = im.crop(im.split()[3].getbbox())
    a = np.asarray(im).copy()
    al = a[..., 3] > 40
    H, W = al.shape
    e = int(round(eje_del_cuerpo(al, int(H * 0.60))))
    franja = franja_del_sello(al, lado, e)
    if franja is None:
        print(f"  — {nombre}: no se encontró sello, se deja igual")
        return
    y0, y1 = franja

    # Se espeja media botella en la franja del sello. Funciona cuando el sello
    # no baja más allá del arranque de la etiqueta; cuando sí baja, este método
    # NO sirve y hay que ir a buscar la foto limpia (ver la nota de TRABAJOS).
    # ⛔ EL CANTO BAJO EL SELLO SALE DEL LADO LIMPIO, NO DE UNA INTERPOLACIÓN.
    # Interpolando en línea recta entre la fila limpia de arriba (el cuello) y
    # la de abajo (el cuerpo), el hombro quedaba rebanado en diagonal y las
    # botellas se veían CORTADAS. El contorno del hombro ya está en la mitad
    # limpia: el canto que corresponde es su espejo.
    #
    # Y hay DOS regímenes, porque el sello baja más que el arranque de la
    # etiqueta: arriba de la etiqueta todo es vidrio y se espeja media botella;
    # sobre la etiqueta se espeja sólo desde un poco antes de su canto, lo justo
    # para tapar el resto del sello. Espejar media etiqueta escribe al revés
    # —«MORANDÉ» salió «MORAROM»—; no espejar nada deja el «JAMES SUCK» a la
    # vista. La franja que se altera son 28 px del borde de la etiqueta, que a
    # tamaño de entrega son menos de 6.
    col = a[:, max(0, e - 6):e + 6, :3].astype(float).mean(axis=(1, 2))
    saltos = [y for y in range(int(H * 0.25), int(H * 0.75))
              if col[y] - col[y - 6] > 18]
    etiqueta = saltos[0] if saltos else H

    bordes = []
    for y in range(y1 + 10, int(H * 0.80)):
        xs = np.where(al[y])[0]
        if not len(xs):
            continue
        c0 = xs.max() if lado == "der" else xs.min()
        paso = -1 if lado == "der" else 1
        vidrio = a[y, c0 - paso * 4, :3].astype(float).mean()
        for d in range(6, abs(c0 - e)):
            x = c0 + paso * d
            if a[y, x, :3].astype(float).mean() > vidrio + 26:
                bordes.append(x)
                break
    etiq_x = int(np.median(bordes)) if bordes else e

    for y in range(y0, y1):
        xs = np.where(al[y])[0]
        if not len(xs):
            continue
        c = 2 * e - (xs.min() if lado == "der" else xs.max())
        if y < etiqueta:
            desde = e
        else:
            desde = etiq_x - 28 if lado == "der" else etiq_x + 28
        if lado == "der":
            for x in range(max(e, desde), W):
                a[y, x] = a[y, 2 * e - x] if (x <= c and 0 <= 2 * e - x < W) else 0
        else:
            for x in range(0, min(e, desde) + 1):
                a[y, x] = a[y, 2 * e - x] if (x >= c and 0 <= 2 * e - x < W) else 0

    out = Image.fromarray(a)
    out = out.crop(out.split()[3].getbbox())
    destino = BT / nombre.replace(".png", "-sin-sello.png")
    out.save(destino)
    print(f"  ✓ {destino.name}  {out.width}x{out.height}  (eje {e} · "
          f"filas {y0}–{y1} · etiqueta en la fila {etiqueta}, canto x={etiq_x})")


def main():
    for nombre, lado in TRABAJOS.items():
        if not (BT / nombre).exists():
            sys.exit(f"falta {nombre}")
        limpia(nombre, lado)


if __name__ == "__main__":
    main()

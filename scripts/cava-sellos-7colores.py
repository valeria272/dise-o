#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Levanta los sellos de premio del 7Colores Single Vineyard desde su packshot.

    ~/copylab-venv/bin/python3 scripts/cava-sellos-7colores.py

El brief del Cyber le declara a este vino **92 puntos Descorchados** y **91
puntos James Suckling**, y los dos están impresos en el único packshot que la
marca publica. Como archivo suelto no existen en el repo, se copian de ahí: son
círculos completos, uno pegado al otro pero sin superponerse, así que un recorte
circular los entrega enteros.

⛔ No se redibujan ni se le cambia el número a los de 98 puntos que ya hay en el
repo. Un sello es una marca registrada: se copia el dibujo real o se pide. Esto
es copiar —misma imagen, mismo tamaño relativo— y por eso vale.

Miden ~140 px. En la pieza entregada (1080 de ancho) van a ~152 px, así que el
aumento es de 1,1×: no se inventa detalle que no esté.
"""
import pathlib

import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import (binary_closing, binary_fill_holes,
                           binary_opening, label)

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "public/assets/cava/bottles/7colores-single-vineyard-red-blend.png"
DESTINO = RAIZ / "public/assets/cava/sellos"

# Ventanas donde buscar cada sello, medidas sobre el packshot de 1000×1000.
VENTANAS = {
    "descorchados-92": ((545, 200, 718, 362), "oro"),
    "james-suckling-91": ((535, 345, 700, 500), "negro"),
}


def circulo(a, ventana, tipo):
    """Centro y radio del sello dentro de esa ventana.

    El radio sale de la CAJA de la mancha, no de un percentil de distancias: el
    sello es un disco macizo y su caja lo encierra justo. Con el percentil, el
    recorte se pasaba y entraba vidrio de la botella alrededor.
    """
    x0, y0, x1, y1 = ventana
    sub = a[y0:y1, x0:x1].astype(int)
    r, g, b, al = sub[..., 0], sub[..., 1], sub[..., 2], sub[..., 3]
    if tipo == "oro":
        # El sello dorado se apoya sobre el vidrio oscuro y su mitad
        # izquierda queda en sombra: pedirle brillo alto se comía
        # «DescorChadOS». Lo que define al dorado es el ORDEN de los canales
        # —rojo sobre verde sobre azul— y eso se mantiene en la sombra.
        m = (r > 80) & (r > g + 8) & (g > b + 12) & (r - b > 45) & (al > 60)
    else:
        # Negro de verdad: casi sin color. El vidrio de la botella también es
        # oscuro, pero tira a rojo y por ahí se separan.
        mx, mn = sub[..., :3].max(axis=2), sub[..., :3].min(axis=2)
        m = (mx < 70) & (mx - mn < 26) & (al > 60)
    # El texto negro del sello parte la mancha dorada en trozos: se cierra
    # primero para que el disco vuelva a ser uno solo. Sin esto el recorte se
    # comía «DescorChadOS» por la izquierda.
    m = binary_opening(m, np.ones((3, 3)))
    m = binary_fill_holes(binary_closing(m, np.ones((27, 27))))
    lab, _ = label(m)
    tam = np.bincount(lab.ravel())
    tam[0] = 0
    m = lab == tam.argmax()
    ys, xs = np.where(m)
    cx = (xs.min() + xs.max()) / 2 + x0
    cy = (ys.min() + ys.max()) / 2 + y0
    rad = min(xs.max() - xs.min(), ys.max() - ys.min()) / 2
    return cx, cy, float(rad)


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    im = Image.open(ORIGEN).convert("RGBA")
    a = np.asarray(im)
    for nombre, (ventana, tipo) in VENTANAS.items():
        cx, cy, rad = circulo(a, ventana, tipo)
        lado = int(round(rad * 2)) + 2
        caja = (int(round(cx - lado / 2)), int(round(cy - lado / 2)))
        rec = im.crop((caja[0], caja[1], caja[0] + lado, caja[1] + lado))
        mask = Image.new("L", (lado, lado), 0)
        ImageDraw.Draw(mask).ellipse([1, 1, lado - 2, lado - 2], fill=255)
        rec.putalpha(mask)
        ruta = DESTINO / f"{nombre}.png"
        rec.save(ruta)
        print(f"  ✓ {ruta.name}  {lado}x{lado}  (centro {cx:.0f},{cy:.0f} · radio {rad:.1f})")


if __name__ == "__main__":
    main()

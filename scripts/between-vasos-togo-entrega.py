#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · arma la entrega de los vasos To Go sin fondo.

Toma los tres recortes revelados (between-vasos-togo-recorte.py) y la
proporcion real medida (between-vasos-togo-proporcion.py) y saca:

  BW-ToGo-vaso-chico.png      ·  los tres sueltos, ya a ESCALA COMUN: si se
  BW-ToGo-vaso-mediano.png       colocan los tres al 100 % quedan bien
  BW-ToGo-vaso-grande.png        proporcionados entre si sin tocar nada
  BW-ToGo-tres-tamanos.png    ·  los tres juntos, de chico a grande, con aire
  BW-ToGo-tres-tamanos-invertido.png  ·  el mismo, de grande a chico

Todos PNG con transparencia real, sin sombra y sin fondo.

La separacion entre vasos es el 22 % del ancho promedio: en la foto original se
tocaban casi, y el pedido fue justamente que «no esten tan apegados».
"""
import json
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

TRABAJO = RAIZ / "out/hilton/between/vasos-togo/_trabajo"
SALIDA = RAIZ / "out/hilton/between/vasos-togo"
BANCO = RAIZ / "public/assets/hilton/between/togo-sep2026"

ORDEN = ["chico", "mediano", "grande"]
SEPARACION = 0.22        # del ancho promedio de los vasos
MARGEN = 0.05            # del alto del vaso mas alto


def recortar(im):
    a = np.array(im)[:, :, 3]
    ys, xs = np.nonzero(a > 4)
    return im.crop((int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1))


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    rel = json.load(open(TRABAJO / "proporcion.json"))["proporcion"]

    vasos = {n: recortar(Image.open(TRABAJO / (n + "-listo.png")).convert("RGBA"))
             for n in ORDEN}
    alto_ref = vasos["grande"].height          # el grande se queda en su tamano nativo

    print("ESCALA COMUN (el grande no se toca)")
    escalados = {}
    for n in ORDEN:
        objetivo = int(round(alto_ref * rel[n]))
        f = objetivo / vasos[n].height
        w = int(round(vasos[n].width * f))
        escalados[n] = vasos[n].resize((w, objetivo), Image.LANCZOS)
        print("   %-8s proporcion %.4f · %d x %d px  (del nativo %d, factor %.3f)"
              % (n, rel[n], w, objetivo, vasos[n].height, f))

    # --- los tres sueltos, con un margen parejo
    m = int(round(alto_ref * MARGEN))
    for n in ORDEN:
        im = escalados[n]
        lienzo = Image.new("RGBA", (im.width + 2 * m, im.height + 2 * m), (0, 0, 0, 0))
        lienzo.alpha_composite(im, (m, m))
        p = SALIDA / ("BW-ToGo-vaso-%s.png" % n)
        lienzo.save(p)
        print("   ->", p.name, lienzo.size)

    # --- los tres juntos, apoyados en la misma linea de piso
    anchos = [escalados[n].width for n in ORDEN]
    sep = int(round(SEPARACION * float(np.mean(anchos))))
    for nombre, secuencia in (("BW-ToGo-tres-tamanos.png", ORDEN),
                              ("BW-ToGo-tres-tamanos-invertido.png", ORDEN[::-1])):
        W = sum(escalados[n].width for n in secuencia) + 2 * sep + 2 * m
        H = alto_ref + 2 * m
        lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        x = m
        for n in secuencia:
            im = escalados[n]
            lienzo.alpha_composite(im, (x, H - m - im.height))   # misma linea de piso
            x += im.width + sep
        lienzo.save(SALIDA / nombre)
        print("   ->", nombre, lienzo.size, "· separacion %d px" % sep)

    # el banco de marca se queda con los recortes sueltos
    BANCO.mkdir(parents=True, exist_ok=True)
    for n in ORDEN:
        escalados[n].save(BANCO / ("togo-vaso-%s-nobg.png" % n))
    print("\nbanco de marca ->", BANCO)


if __name__ == "__main__":
    main()

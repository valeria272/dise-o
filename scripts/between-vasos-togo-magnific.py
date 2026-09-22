#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · los vasos To Go por Magnific — preparar y rearmar.

Pedido de Eli (21-09-2026): «hazlo en Magnific para que guardes los vasos como
prompt en un space… que se vean producto profesional y usarlos en distintas
aplicaciones».

Magnific entra a hacer UNA cosa: subir la calidad del pixel con el upscaler de
PRECISIÓN. ⛔ El upscaler CREATIVO no se usa acá: alucina detalle y sobre una
marca impresa **te cambia el dibujo del logotipo** — está escrito en
`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md` y es la misma razón por la que el manual de
Between prohíbe generar el vaso en tomas frontales. Lo que sube es la foto real.

Este script hace las dos puntas; las llamadas a Magnific van por el conector.

  preparar → deja los tres vasos con el ENTORNO PLANO. Un upscaler mira el
             contraste local: si le llega el recorte sobre transparencia (que se
             aplana a negro) o sobre un fondo cualquiera, dibuja un halo en todo
             el canto. Rellenando el exterior con el color del píxel interior más
             cercano no hay borde que realzar, y el canto sale limpio.

  rearmar  → vuelve a poner el alfa. ⛔ No se escala el mapa de bits del mate:
             el contorno se guardó como POLÍGONO y se rasteriza al tamaño nuevo,
             que es la única forma de que el canto no se ablande.
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402

TRABAJO = RAIZ / "out/hilton/between/vasos-togo/_trabajo"
MAG = TRABAJO / "magnific"
VASOS = ["chico", "mediano", "grande"]


def preparar():
    MAG.mkdir(parents=True, exist_ok=True)
    fichas = {}
    for n in VASOS:
        rgba = np.array(Image.open(TRABAJO / (n + "-listo.png")).convert("RGBA"))
        rgb, a = rgba[:, :, :3], rgba[:, :, 3]
        dentro = a > 128
        idx = ndimage.distance_transform_edt(~dentro, return_indices=True)[1]
        plano = rgb[tuple(idx)]
        # el canto blando se compone sobre su propio relleno, para que no quede
        # una orla oscura que el upscaler despues realce
        al = (a.astype(np.float32) / 255.0)[:, :, None]
        salida = (rgb.astype(np.float32) * al + plano.astype(np.float32) * (1 - al))
        p = MAG / ("%s-plano.png" % n)
        Image.fromarray(salida.astype(np.uint8)).save(p)
        fichas[n] = dict(archivo=str(p), ancho=int(rgb.shape[1]), alto=int(rgb.shape[0]))
        print("   %-8s %s  %d x %d px" % (n, p.name, rgb.shape[1], rgb.shape[0]))
    json.dump(fichas, open(MAG / "fichas.json", "w"), indent=2)
    print("\nlisto para subir a Magnific ->", MAG)


def _rasterizar(poly, escala, alto, ancho, super_=4):
    lienzo = np.zeros((alto * super_, ancho * super_), np.uint8)
    cv2.fillPoly(lienzo, [np.round(poly * escala * super_).astype(np.int32)], 255)
    return cv2.resize(lienzo, (ancho, alto), interpolation=cv2.INTER_AREA)


def rearmar():
    """Toma lo que bajó de Magnific y le devuelve el alfa, rasterizado al tamaño
    nuevo desde el polígono del contorno."""
    for n in VASOS:
        sub = MAG / ("%s-magnific.jpg" % n)
        if not sub.exists():
            print("   ⚠️  falta %s" % sub.name)
            continue
        im = np.array(Image.open(sub).convert("RGB"))
        alto, ancho = im.shape[:2]
        poly = np.load(TRABAJO / (n + "-contorno.npy"))
        orig = Image.open(TRABAJO / (n + "-listo.png"))
        escala = ancho / orig.width
        assert abs(escala - alto / orig.height) < 0.01, "%s cambió de proporción" % n
        alpha = _rasterizar(poly, escala, alto, ancho)
        Image.fromarray(np.dstack([im, alpha])).save(TRABAJO / (n + "-listo.png"))
        print("   %-8s %d x %d px  (x%.2f desde %d x %d)"
              % (n, ancho, alto, escala, orig.width, orig.height))
    print("\nrearmado. Ahora corre between-vasos-togo-entrega.py")


if __name__ == "__main__":
    accion = sys.argv[1] if len(sys.argv) > 1 else "preparar"
    print("BETWEEN · vasos To Go por Magnific — %s" % accion)
    {"preparar": preparar, "rearmar": rearmar}[accion]()

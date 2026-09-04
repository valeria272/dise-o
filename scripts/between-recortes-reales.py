#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta productos REALES de la sesión del cliente, con alfa limpio.

Para qué existe: hasta ahora, cuando faltaba un producto en una escena, se
generaba. El cliente lleva tres rondas reclamando exactamente eso —vasos con el
logo inventado, tazas con marca ajena, comida que no es la suya—. La sesión
`25 jul 2025` tiene los productos reales sobre la mesa y el muro del local, así
que lo que corresponde es RECORTARLOS, no dibujarlos.

Se usa grabCut de OpenCV con una caja de arranque medida a mano: el fondo (loza
lisa y madera desenfocada) es exactamente el caso para el que sirve. Después se
limpia con morfología, se queda la mancha más grande y se difumina 2 px el canto.

Salidas en `public/assets/hilton/between/recortes/` — y ESAS SÍ se versionan
(`git add -f`, que `public/assets/**` está en el .gitignore). Los originales
viven en `raw/`, que no viaja, así que sin los recortes en el repo las piezas no
se rehacen en otra máquina. Es la lección del 03-09: se perdieron 8 historias
por no guardar el material de origen junto con la pieza.

Si hay que volver a bajar los originales, están en el Drive del cliente, carpeta
**BETWEEN 25 JULIO MODELOS** `1gI00XGbBV5YjqcSjG3SmmkMuxr-ev_60`, y se bajan sin
token con el visor público:

    curl -sL "https://drive.google.com/thumbnail?id=<ID>&sz=w4000" -o foto.jpg

(con `sz=w4000` Drive devuelve el ORIGINAL, no una miniatura). El croissant de
jamón queso es `1gsZIrP7db5j-xP5Jdh8PqzSZpzuAai4m` (`25-278`).

Uso:
    python scripts/between-recortes-reales.py
    python scripts/between-recortes-reales.py --revisar   # hoja de contacto
"""
import argparse
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SALIDA = RAIZ / "public/assets/hilton/between/recortes"
SESION = RAIZ / "raw/hilton/between/togo-25jul2025"

#: (nombre, archivo, caja de arranque en píxeles de la ORIGINAL)
#: Las cajas están MEDIDAS sobre una rejilla de décimos, no estimadas.
PIEZAS = [
    # el salado que pide el cliente: «un crosant jamon queso»
    ("croissant-jamon-queso", "Double Tree 25 jul 25-278.jpg", (600, 2880, 2760, 4120)),
    # el dulce que pide el cliente: «que el dulce sea un muffin»
    ("muffin-chocolate", "Double Tree 25 jul 25-266.jpg", (1800, 1500, 3380, 2800)),
    # el plato ENTERO con el muffin, para montar el bodegón de la slide 4 del
    # carrusel To Go sin sacar el producto de su loza
    ("plato-muffin", "Double Tree 25 jul 25-266.jpg", (880, 1560, 3960, 3400)),
    # y el plato entero con el croissant de jamón queso, por si hace falta
    ("plato-croissant-jq", "Double Tree 25 jul 25-278.jpg", (160, 2680, 3300, 4520)),
]


#: recortes que hay que PODAR: grabCut se lleva pegado un reflejo de la mesa que
#: toca el canto del plato, así que no lo separa la componente conexa. Se borra
#: a mano, con la caja medida sobre el alfa (fracciones del recorte).
PODAR = {
    "plato-muffin": [(0.955, 0.0, 1.0, 1.0), (0.90, 0.10, 1.0, 0.42)],
}


def recorta(ruta, caja, iteraciones=6):
    bgr = cv2.imread(str(ruta))
    if bgr is None:
        sys.exit(f"⛔ No pude abrir {ruta}")
    x0, y0, x1, y1 = caja
    # se trabaja sobre un margen alrededor de la caja: grabCut necesita fondo
    # seguro por fuera para aprender el modelo
    m = 140
    rx0, ry0 = max(0, x0 - m), max(0, y0 - m)
    rx1, ry1 = min(bgr.shape[1], x1 + m), min(bgr.shape[0], y1 + m)
    trozo = bgr[ry0:ry1, rx0:rx1]
    mascara = np.zeros(trozo.shape[:2], np.uint8)
    rect = (x0 - rx0, y0 - ry0, x1 - x0, y1 - y0)
    fondo = np.zeros((1, 65), np.float64)
    frente = np.zeros((1, 65), np.float64)
    cv2.grabCut(trozo, mascara, rect, fondo, frente, iteraciones, cv2.GC_INIT_WITH_RECT)
    binaria = np.where((mascara == cv2.GC_FGD) | (mascara == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)

    # limpieza: cerrar agujeros del hojaldre y quedarse con la mancha grande
    nucleo = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    binaria = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, nucleo)
    binaria = cv2.morphologyEx(binaria, cv2.MORPH_OPEN,
                               cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13)))
    n, etiquetas, stats, _ = cv2.connectedComponentsWithStats(binaria, 8)
    if n > 1:
        mayor = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        binaria = np.where(etiquetas == mayor, 255, 0).astype(np.uint8)
    # rellenar huecos interiores (el queso brillante se le escapa a grabCut)
    relleno = binaria.copy()
    h, w = binaria.shape
    cv2.floodFill(relleno, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 255)
    binaria = binaria | cv2.bitwise_not(relleno)

    alfa = cv2.GaussianBlur(binaria, (0, 0), 1.8)
    rgba = np.dstack([cv2.cvtColor(trozo, cv2.COLOR_BGR2RGB), alfa])
    ys, xs = np.where(alfa > 8)
    if len(ys) == 0:
        sys.exit("⛔ grabCut no encontró producto: revisa la caja")
    return Image.fromarray(rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true",
                    help="deja una hoja de contacto sobre damero para mirar el alfa")
    a = ap.parse_args()
    SALIDA.mkdir(parents=True, exist_ok=True)
    hechos = []
    for nombre, archivo, caja in PIEZAS:
        png = recorta(SESION / archivo, caja)
        for fx0, fy0, fx1, fy1 in PODAR.get(nombre, []):
            recorte = (int(fx0 * png.width), int(fy0 * png.height),
                       int(fx1 * png.width), int(fy1 * png.height))
            png.paste((0, 0, 0, 0), recorte)
            png = png.crop(png.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())
        destino = SALIDA / f"{nombre}.png"
        png.save(destino)
        print(f"✓ {destino.relative_to(RAIZ)}  {png.size}")
        hechos.append((nombre, png))

    if a.revisar:
        ancho = sum(p.width for _, p in hechos) + 60 * len(hechos)
        alto = max(p.height for _, p in hechos) + 60
        damero = Image.new("RGB", (ancho, alto), (255, 255, 255))
        px = damero.load()
        for y in range(alto):
            for x in range(ancho):
                if ((x // 40) + (y // 40)) % 2:
                    px[x, y] = (210, 214, 220)
        x = 30
        for _, p in hechos:
            damero.paste(p, (x, 30), p)
            x += p.width + 60
        ruta = RAIZ / "out/hilton-between-r10/recortes-revision.png"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        damero.resize((min(1600, ancho), int(alto * min(1600, ancho) / ancho))).save(ruta)
        print(f"→ revisión: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""BETWEEN · carta R6 (30-09-2026) — mockup CENITAL en funda de cuero abierta, a proporción exacta.

Eli sobre el mockup en ángulo: «se ven poco profesionales, debes seguir la proporción y la perspectiva,
que no se vea falso». La primera versión estiraba la carta (1,76) a la hoja de la foto (1,61–1,66).
Acá la foto es cenital (`_plano-abierto-2.jpg`, sin perspectiva) y la carta NO se deforma: se calza por
el ALTO de la hoja de la foto con su ancho real 17:30, cubriéndola; se le devuelve la luz de la foto y
lleva una sombra de contacto suave, como un papel apoyado en la funda.

    python scripts/between-carta-r6-funda-plana.py [A B D]
Salida: out/hilton/between/carta-oficial/r6/mockup/BW-CARTA-BETWEEN-OPCION-<X>-FUNDA-{PORTADA,CONTRAPORTADA}.jpg
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
R6 = RAIZ / "out/hilton/between/carta-oficial/r6"
FOTO = R6 / "mockup/funda/_plano-abierto-2.jpg"
PROP = 300 / 170


def hoja(im):
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    m = ((hsv[..., 2] > 200) & (hsv[..., 1] < 40)).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    i = max(range(1, n), key=lambda i: st[i, 4])
    x, y, w, h = st[i, :4]
    return x, y, w, h, (lab == i)


def montar(foto, png, caja):
    x, y, w, h, mh = caja
    H, W = foto.shape[:2]
    alto = h + 4                                     # cubre el filo de la hoja de la foto
    ancho = round(alto / PROP)
    cx = x + w / 2
    x0, y0 = round(cx - ancho / 2), y - 2
    pg = cv2.resize(cv2.imread(str(png)), (ancho, alto), interpolation=cv2.INTER_AREA).astype(np.float32)
    # luz: la de la hoja en blanco de la foto, suavizada y llevada al tamaño de la carta
    L = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY).astype(np.float32)[y:y + h, x:x + w]
    L = cv2.GaussianBlur(L, (0, 0), 25)
    luz = cv2.resize(L / np.percentile(L, 70), (ancho, alto))
    luz = np.clip(0.97 + (luz - 1) * 1.0, .88, 1.03)[..., None]   # el beige no se agrisa
    pg = np.clip(pg * luz, 0, 255)
    out = foto.astype(np.float32)
    # sombra de contacto: suave y corta (luz de estudio pareja, desde arriba a la izquierda)
    sh = np.zeros((H, W), np.float32)
    cv2.rectangle(sh, (x0 + 3, y0 + 5), (x0 + ancho + 3, y0 + alto + 5), 1, -1)
    sh = cv2.GaussianBlur(sh, (0, 0), 7)[..., None] * .38
    out = out * (1 - sh)
    # borde del papel: 1 px apenas más oscuro, que es como se lee el corte de una hoja
    pg[:1, :] *= .9; pg[-1:, :] *= .88; pg[:, :1] *= .9; pg[:, -1:] *= .88
    out[y0:y0 + alto, x0:x0 + ancho] = pg
    return out.astype(np.uint8)


def main():
    foto = cv2.imread(str(FOTO))
    caja = hoja(foto)
    print(f"hoja de la foto {caja[2]}×{caja[3]} px = {caja[3] / caja[2]:.3f} · la carta va a {PROP:.3f}")
    info = json.loads((R6 / "paginas.json").read_text(encoding="utf-8"))
    for op in (sys.argv[1:] or ["A", "B", "D"]):
        n = info[op]["paginas"]
        for k, nom in ((1, "PORTADA"), (n, "CONTRAPORTADA")):
            im = montar(foto, R6 / "png" / f"BW-CARTA-OFICIAL-R6-OP{op}-{k}.png", caja)
            dst = R6 / "mockup" / f"BW-CARTA-BETWEEN-OPCION-{op}-FUNDA-{nom}.jpg"
            cv2.imwrite(str(dst), im, [cv2.IMWRITE_JPEG_QUALITY, 93])
            print("✓", dst.name)


if __name__ == "__main__":
    main()

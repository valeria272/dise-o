#!/usr/bin/env python3
"""BETWEEN · carta R6 (30-09-2026) — mockup en FUNDA DE CUERO ABIERTA: portada a la izquierda,
contraportada a la derecha, cada una dentro de su bolsillo de plástico.

La foto (`_cuero-abierto.jpg`, Mystic, `between-carta-r6-funda-gen.py`) trae las dos hojas en blanco
puro. Acá se detectan sus cuatro esquinas, se calza el render EXACTO de la hoja en perspectiva y se le
devuelve la luz de la foto: la sombra del papel multiplica y los brillos del plástico se suman encima
(sobre la tinta café se ven como el reflejo real de la funda). La IA no toca ninguna letra.

    python scripts/between-carta-r6-funda.py [A B D]
Salida: out/hilton/between/carta-oficial/r6/mockup/BW-CARTA-BETWEEN-OPCION-<X>-FUNDA.jpg
"""
import json
import sys
from pathlib import Path

import cv2
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
R6 = RAIZ / "out/hilton/between/carta-oficial/r6"
# Eli 30-09: «haz el mockup en Magnific». La escena la hace Nano Banana Pro con las hojas EN BLANCO y en
# vista cenital (hojas de 1,74, a 1 % de 17:30); la carta exacta se calza encima. Pedirle a Magnific la
# carta ya puesta reescribe precios y palabras («LUNES A MONNES», $8.200 por $6.900) y la achata (1,35)
import os
FOTO = Path(os.environ.get("FUNDA_FOTO", R6 / "mockup/magnific/funda-blanca.png"))
SUFIJO = os.environ.get("FUNDA_SUFIJO", "MAGNIFIC")


def hojas_blancas(im):
    """Las dos hojas en blanco más grandes → cuadriláteros ordenados TL, TR, BR, BL (izquierda primero)."""
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    m = ((hsv[..., 2] > 200) & (hsv[..., 1] < 40)).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((15, 15), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    quads = []
    for i in sorted(range(1, n), key=lambda i: -st[i, 4])[:2]:
        cs, _ = cv2.findContours((lab == i).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        hull = cv2.convexHull(max(cs, key=cv2.contourArea))
        q = cv2.approxPolyDP(hull, 0.02 * cv2.arcLength(hull, True), True).reshape(-1, 2).astype(np.float32)
        if len(q) != 4:   # esquineros de plástico: en vista cenital vale el rectángulo mínimo que la contiene
            q = cv2.boxPoints(cv2.minAreaRect(max(cs, key=cv2.contourArea))).astype(np.float32)
        s, d = q.sum(1), np.diff(q, axis=1).ravel()
        quads.append(np.array([q[s.argmin()], q[d.argmin()], q[s.argmax()], q[d.argmax()]], np.float32))
        c = quads[-1].mean(0)                     # 14 px hacia afuera (foto 4K): que no asome el filo blanco de la hoja
        quads[-1] = c + (quads[-1] - c) * (1 + 14 / np.linalg.norm(quads[-1] - c, axis=1, keepdims=True))
    return sorted(quads, key=lambda q: q[:, 0].mean())


def calzar(foto, hoja_png, quad):
    H, W = foto.shape[:2]
    pg = cv2.imread(str(hoja_png))
    h, w = pg.shape[:2]
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), quad)
    warp = cv2.warpPerspective(pg, M, (W, H), flags=cv2.INTER_AREA).astype(np.float32)
    mask = cv2.warpPerspective(np.full((h, w), 255, np.uint8), M, (W, H), flags=cv2.INTER_AREA)
    mask = cv2.GaussianBlur(mask, (3, 3), 0).astype(np.float32)[..., None] / 255
    # luz del papel en la foto: normalizada a su blanco típico
    L = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY).astype(np.float32)
    ref = np.percentile(L[mask[..., 0] > .9], 75)
    sombra = np.clip(L / ref, 0, 1)[..., None]
    brillo = np.clip(L - ref * .985, 0, None)[..., None] * 2.2          # reflejos del plástico
    out = warp * sombra + brillo * (1 - warp / 255) + brillo * .15
    return foto.astype(np.float32) * (1 - mask) + np.clip(out, 0, 255) * mask


def main():
    foto0 = cv2.imread(str(FOTO))
    qi, qd = hojas_blancas(foto0)
    info = json.loads((R6 / "paginas.json").read_text(encoding="utf-8"))
    for op in (sys.argv[1:] or ["A", "B", "D"]):
        n = info[op]["paginas"]
        png = lambda k: R6 / "png" / f"BW-CARTA-OFICIAL-R6-OP{op}-{k}.png"
        f = calzar(foto0, png(1), qi)
        f = calzar(f.astype(np.uint8), png(n), qd)
        dst = R6 / "mockup" / f"BW-CARTA-BETWEEN-OPCION-{op}-FUNDA-{SUFIJO}.jpg"
        cv2.imwrite(str(dst), f.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])
        print("✓", dst.name, f"portada + hoja {n}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Mide las piezas aprobadas de Casablanca. Sin estimaciones.

    python3 scripts/casablanca-medir.py raw/casablanca/ref/*  > medidas.txt
    python3 scripts/casablanca-medir.py --json raw/casablanca/ref/*

Todo sale normalizado a 1080 px de ancho. Lo que mide, pieza por pieza:

  logo      caja blanca pegada al borde superior (x, y, w, h, centro)
  gris      manchas del gris institucional exacto (#626260 ±6)
  bandas    filas de texto blanco en la mitad inferior (y, alto, x0, x1, centro)
  filetes   reglas blancas horizontales de 1 px que enmarcan la bajada

El "alto" de una banda de texto es la altura real de tinta: en mayúsculas es la
altura de mayúscula; en la itálica con descendentes ("Spritz") incluye la 'p'.
"""
import json
import sys

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
GRIS = (0x62, 0x62, 0x60)


def _rect(mask, min_frac, min_lado):
    ys = np.where(mask.sum(axis=1) > min_lado)[0]
    if not len(ys):
        return None
    grupos, ini = [], ys[0]
    for i in range(1, len(ys)):
        if ys[i] != ys[i - 1] + 1:
            grupos.append((ini, ys[i - 1]))
            ini = ys[i]
    grupos.append((ini, ys[-1]))
    mejor = None
    for y0, y1 in grupos:
        if y1 - y0 < min_lado:
            continue
        sub = mask[y0:y1 + 1]
        xs = np.where(sub.sum(axis=0) > (y1 - y0) * min_frac)[0]
        if len(xs) < min_lado:
            continue
        x0, x1 = int(xs.min()), int(xs.max())
        if sub[:, x0:x1 + 1].mean() < min_frac:
            continue
        area = (y1 - y0) * (x1 - x0)
        if mejor is None or area > mejor[0]:
            mejor = (area, x0, y0, x1, y1)
    if mejor is None:
        return None
    _, x0, y0, x1, y1 = mejor
    return x0, y0, x1 - x0 + 1, y1 - y0 + 1


def medir(ruta):
    a = np.asarray(Image.open(ruta).convert("RGB")).astype(int)
    H, W = a.shape[:2]
    k = 1080 / W
    n = lambda v: round(float(v) * k, 1)
    mn, mx = a.min(axis=2), a.max(axis=2)
    d = {"archivo": ruta.split("/")[-1], "px": [W, H],
         "a1080": [1080, round(H * k)], "aspecto": round(W / H, 3)}

    # 1 · tarjeta de logo: blanco puro y neutro, tercio superior
    blanco = (mn > 248) & ((mx - mn) < 6)
    caja = _rect(blanco[: int(H * 0.45)], 0.55, int(W * 0.05))
    d["logo"] = None if caja is None else {
        "x": n(caja[0]), "y": n(caja[1]), "w": n(caja[2]), "h": n(caja[3]),
        "cx": n(caja[0] + caja[2] / 2)}

    # 2 · gris institucional exacto
    cerca = (abs(a[:, :, 0] - GRIS[0]) < 7) & (abs(a[:, :, 1] - GRIS[1]) < 7) \
        & (abs(a[:, :, 2] - GRIS[2]) < 7)
    if caja:
        lx, ly, lw, lh = caja
        cerca[max(0, ly - 4): ly + lh + 4, max(0, lx - 4): lx + lw + 4] = False
    caja_g = _rect(cerca, 0.85, int(W * 0.02))
    d["gris_626260"] = None if caja_g is None else {
        "x": n(caja_g[0]), "y": n(caja_g[1]), "w": n(caja_g[2]), "h": n(caja_g[3])}
    d["gris_cobertura_%"] = round(float(cerca.mean()) * 100, 2)

    # 3 · bandas de texto blanco bajo la mitad
    texto = (mn > 232) & ((mx - mn) < 14)
    y0 = int(H * 0.45)
    sub = texto[y0:]
    filas = sub.sum(axis=1) > max(6, W * 0.004)
    bandas, i = [], 0
    while i < len(filas):
        if filas[i]:
            j = i
            while j < len(filas) and filas[j]:
                j += 1
            if j - i > H * 0.004:
                xs = np.where(sub[i:j].sum(axis=0) > 0)[0]
                bandas.append({"y": n(y0 + i), "alto": n(j - i), "x0": n(xs.min()),
                               "x1": n(xs.max()), "cx": n((xs.min() + xs.max()) / 2)})
            i = j
        else:
            i += 1
    d["bandas"] = bandas

    # 4 · filetes: fila mucho más clara que su entorno, tramo largo y contiguo
    gris_med = a.mean(axis=2)
    filetes = []
    for y in range(int(H * 0.45), H - 10):
        delta = gris_med[y] - (gris_med[y - 9] + gris_med[y + 9]) / 2
        m = delta > 25
        if m.sum() < W * 0.25:
            continue
        xs = np.where(m)[0]
        tramo = max(np.split(xs, np.where(np.diff(xs) != 1)[0] + 1), key=len)
        if len(tramo) < W * 0.25:
            continue
        if filetes and y - filetes[-1]["_y"] < 4:
            continue
        filetes.append({"_y": y, "y": n(y), "x0": n(tramo[0]), "x1": n(tramo[-1]),
                        "ancho": n(tramo[-1] - tramo[0]),
                        "cx": n((tramo[0] + tramo[-1]) / 2)})
    for f in filetes:
        f.pop("_y")
    d["filetes"] = filetes
    return d


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if x != "--json"]
    salida = [medir(f) for f in args]
    if "--json" in sys.argv:
        print(json.dumps(salida, ensure_ascii=False, indent=1))
    else:
        for d in salida:
            print(f"\n=== {d['archivo']}  {d['px'][0]}x{d['px'][1]} → {d['a1080'][0]}x{d['a1080'][1]}")
            print("  logo   ", d["logo"])
            print("  gris   ", d["gris_626260"], f"cobertura {d['gris_cobertura_%']}%")
            for b in d["bandas"]:
                print("  banda  ", b)
            for f in d["filetes"]:
                print("  filete ", f)

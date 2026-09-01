#!/usr/bin/env python3
"""Mide el bloque de texto de una pieza de Between, normalizado a lienzo 1080.

Aísla la tinta beige #FFF9EB por umbral y la caja taupe #675B49 opaca, y saca
el bbox de cada línea. Es el método del manual (§ LA GRAMÁTICA MEDIDA): se mide
la TINTA, no la caja del layout.

    python scripts/between-medir-bloque.py out/cowork-v2
"""
import sys, pathlib
from PIL import Image
import numpy as np

REF = {"titular_ancho_pc": 52.5, "caja_ancho_pc": 55.3, "titular_alto": 85, "caja_alto": 66}

def bandas(mask, minpx):
    filas = mask.sum(1); out=[]; ini=None
    for y, v in enumerate(filas):
        if v >= minpx and ini is None: ini = y
        elif v < minpx and ini is not None:
            if y - ini > 6: out.append((ini, y-1))
            ini = None
    if ini is not None: out.append((ini, len(filas)-1))
    return out

def medir(p):
    im = Image.open(p).convert("RGB"); k = 1080 / im.width
    a = np.asarray(im).astype(int); R,G,B = a[...,0], a[...,1], a[...,2]
    beige = (R>235)&(G>228)&(B>200)&(abs(R-G)<28)&((R-B)>18)&((R-B)<70)
    taupe = (abs(R-0x67)<10)&(abs(G-0x5b)<10)&(abs(B-0x49)<10)
    print(f"\n=== {p.name}")
    fl = np.where(taupe.sum(1) > im.width*0.45)[0]
    if len(fl):
        y0,y1 = fl.min(), fl.max()
        xs = np.where(taupe[y0:y1+1].sum(0) > (y1-y0)*0.5)[0]
        w = (xs.max()-xs.min()+1)*k
        print(f"  caja taupe   y {y0*k:6.0f}..{y1*k:<6.0f} alto {(y1-y0+1)*k:5.0f}"
              f"  ancho {w:5.0f} = {w/1080*100:4.1f}%   (ref {REF['caja_ancho_pc']}% · alto {REF['caja_alto']})")
    for (y0,y1) in bandas(beige, int(40/k)):
        xs = np.where(beige[y0:y1+1].any(0))[0]
        if not len(xs): continue
        w = (xs.max()-xs.min())*k
        marca = "  ⛔ pasa el 80%" if w/1080 > 0.80 else ""
        print(f"  tinta beige  y {y0*k:6.0f}..{y1*k:<6.0f} alto {(y1-y0)*k:5.1f}"
              f"  ancho {w:5.0f} = {w/1080*100:4.1f}%{marca}")

for arg in sys.argv[1:]:
    p = pathlib.Path(arg)
    for f in (sorted(p.glob("*.png")) if p.is_dir() else [p]):
        medir(f)

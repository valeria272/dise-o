#!/usr/bin/env python3
"""Mide una story del esquema EBEMA CLICK y la compara con la referencia de Paulina.
Uso: python scripts/ebema-medir-click.py <pieza.png> [--ref <ref.png>]"""
import sys, pathlib, numpy as np
from PIL import Image

def bloques(mask, W, k, hueco, minfrac):
    filas = np.nonzero(mask.sum(axis=1) > W*minfrac)[0]
    out=[]
    if not len(filas): return out
    ini=prev=filas[0]
    for y in filas[1:]:
        if y-prev>hueco: out.append((ini,prev)); ini=y
        prev=y
    out.append((ini,prev))
    res=[]
    for y0,y1 in out:
        xs=np.nonzero(mask[y0:y1+1].any(axis=0))[0]
        res.append(dict(y0=y0*k, y1=(y1+1)*k, h=(y1-y0+1)*k,
                        x0=xs[0]*k, x1=(xs[-1]+1)*k, w=(xs[-1]-xs[0]+1)*k,
                        cx=((xs[0]+xs[-1])/2)*k))
    return res

def medir(p):
    im = Image.open(p).convert("RGB"); W,H = im.size; k = 1080/W
    a = np.asarray(im).astype(int)
    rojo = (np.abs(a[:,:,0]-236)<14)&(np.abs(a[:,:,1]-28)<26)&(np.abs(a[:,:,2]-35)<26)
    blanco = (a>236).all(axis=2)
    print(f"\n=== {pathlib.Path(p).name}  {W}x{H}  (normalizado a 1080x1920)")
    if rojo.sum():
        print(f"  rojo medio {tuple(a[rojo].mean(axis=0).round().astype(int))}  ({rojo.sum()} px)")
    print("  ROJO:")
    for b in bloques(rojo, W, k, 12, 0.0):
        if b['h'] < 4: continue
        print(f"    y {b['y0']:7.1f}-{b['y1']:7.1f} (h {b['h']:6.1f})  x {b['x0']:6.1f}-{b['x1']:6.1f} (w {b['w']:6.1f})  centro {b['cx']:6.1f}")
    print("  BLANCO:")
    for b in bloques(blanco, W, k, 16, 0.003):
        print(f"    y {b['y0']:7.1f}-{b['y1']:7.1f} (h {b['h']:6.1f})  x {b['x0']:6.1f}-{b['x1']:6.1f} (w {b['w']:6.1f})  centro {b['cx']:6.1f}")
    g = np.asarray(im.convert("L")).astype(float)
    print("  LUZ por franja (0-255):", end=" ")
    for y0,y1 in [(255,330),(490,600),(1090,1320),(1450,1560)]:
        print(f"y{y0}:{g[int(y0/k):int(y1/k)].mean():.0f}", end="  ")
    print()

for p in sys.argv[1:]:
    medir(p)

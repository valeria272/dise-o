#!/usr/bin/env python3
"""Mide la gramática de GRILLA de EBEMA. Normaliza todo a 1080 de ancho."""
import sys, pathlib, numpy as np
from PIL import Image

def bloques(mask, W, k, hueco=14, minfrac=0.0):
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
        res.append(dict(y0=y0*k,y1=(y1+1)*k,h=(y1-y0+1)*k,
                        x0=xs[0]*k,x1=(xs[-1]+1)*k,w=(xs[-1]-xs[0]+1)*k,
                        cx=((xs[0]+xs[-1])/2)*k))
    return res

def medir(p, mostrar_blanco=True):
    im=Image.open(p).convert("RGB"); W,H=im.size; k=1080/W
    a=np.asarray(im).astype(int)
    rojo=(np.abs(a[:,:,0]-236)<16)&(np.abs(a[:,:,1]-28)<30)&(np.abs(a[:,:,2]-35)<30)
    blanco=(a>236).all(axis=2)
    print(f"\n--- {pathlib.Path(p).name}   {W}x{H} -> 1080x{round(H*k)}")
    for b in bloques(rojo,W,k):
        if b['h']<6 or b['w']<20: continue
        tipo = "CAJA/BANDA roja" if b['w']>200 else "pastilla/boton"
        print(f"   ROJO   y {b['y0']:7.1f}-{b['y1']:7.1f} h {b['h']:6.1f} | x {b['x0']:6.1f}-{b['x1']:6.1f} w {b['w']:6.1f} | cx {b['cx']:6.1f}  {tipo}")
    if mostrar_blanco:
        for b in bloques(blanco,W,k,16,0.004):
            print(f"   BLANCO y {b['y0']:7.1f}-{b['y1']:7.1f} h {b['h']:6.1f} | x {b['x0']:6.1f}-{b['x1']:6.1f} w {b['w']:6.1f} | cx {b['cx']:6.1f}")

for p in sys.argv[1:]:
    medir(p)

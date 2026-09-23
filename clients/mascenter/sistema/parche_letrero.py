#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pega el letrero circular REAL de Jumbo (foto original) sobre la foto generada con IA.
La IA reescribe el texto de los letreros ajenos («cencusud»); un logo de un tercero deformado
no sale en una pieza de cliente. La jerarquía de SISTEMA-DE-MARCAS §2 es la misma que para un
packshot: la IA hace el ambiente, el logo va real."""
import sys, numpy as np
from PIL import Image, ImageFilter
def disco_verde(im):
    a=np.asarray(im.convert("RGB")).astype(int); r,g,b=a[...,0],a[...,1],a[...,2]
    m=(g>120)&(g>r+40)&(g>b+60)&(r<200)   # verde Jumbo
    ys,xs=np.where(m[:int(a.shape[0]*0.6)])          # el disco está en la mitad superior
    # el disco es la componente más densa: recorte por percentiles para sacar los paneles verdes de la fachada
    cy,cx=np.median(ys),np.median(xs); d=np.hypot(ys-cy,xs-cx); keep=d<np.percentile(d,80)
    ys,xs=ys[keep],xs[keep]; cx,cy=(xs.min()+xs.max())/2,(ys.min()+ys.max())/2; rad=max(xs.max()-xs.min(),ys.max()-ys.min())/2
    return cx,cy,rad
real=Image.open(sys.argv[1]).convert("RGB"); ia=Image.open(sys.argv[2]).convert("RGB")
cxr,cyr,rr=disco_verde(real); cxi,cyi,ri=disco_verde(ia)
print("real disco",round(cxr),round(cyr),round(rr),"| ia disco",round(cxi),round(cyi),round(ri))
# recorte del disco real con margen (el aro blanco), reescalado al radio de la IA
m=1.10; box=(int(cxr-rr*m),int(cyr-rr*m),int(cxr+rr*m),int(cyr+rr*m)); parche=real.crop(box)
s=(ri*m*2)/parche.width; parche=parche.resize((int(parche.width*s),int(parche.height*s)),Image.LANCZOS)
# máscara circular con borde suave
w=parche.width; yy,xx=np.mgrid[:w,:w]; d=np.hypot(yy-w/2,xx-w/2); alfa=np.clip((w/2*0.985-d)/3,0,1)*255
mask=Image.fromarray(alfa.astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
out=ia.copy(); out.paste(parche,(int(cxi-w/2),int(cyi-w/2)),mask); out.save(sys.argv[3],quality=94); print("→",sys.argv[3])

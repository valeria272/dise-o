#!/usr/bin/env python3
"""Identifica una tipografía comparando GLIFOS AISLADOS, no anchos de línea.

    python3 scripts/casablanca-tipografia.py

El ancho de una línea depende del tracking, así que sirve para calibrar espaciado
pero NO para decidir qué fuente es (lección de la corrida de Revex, 26-08-2026).
Acá se recorta cada letra de la pieza real, se normaliza por altura de mayúscula y
se compara contra cada candidata con IoU de forma.
"""
import glob
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None


def glifos_de(ruta, y0, y1, texto, umbral=232, min_ancho=6):
    """Recorta las letras de una banda de texto blanco. Devuelve [(char, bitmap)]."""
    a = np.asarray(Image.open(ruta).convert("RGB")).astype(int)
    banda = a[y0:y1]
    mn, mx = banda.min(axis=2), banda.max(axis=2)
    tinta = (mn > umbral) & ((mx - mn) < 16)
    cols = tinta.sum(axis=0) > 0
    tramos, i = [], 0
    while i < len(cols):
        if cols[i]:
            j = i
            while j < len(cols) and cols[j]:
                j += 1
            if j - i >= min_ancho:
                tramos.append((i, j))
            i = j
        else:
            i += 1
    letras = [c for c in texto if c != " "]
    if len(tramos) != len(letras):
        return None, len(tramos), len(letras)
    out = []
    for (x0, x1), ch in zip(tramos, letras):
        sub = tinta[:, x0:x1]
        ys = np.where(sub.sum(axis=1) > 0)[0]
        out.append((ch, sub[ys.min(): ys.max() + 1]))
    return out, len(tramos), len(letras)


def render(ch, path, wght, alto_px):
    """Dibuja un glifo a la altura de tinta pedida y lo devuelve recortado."""
    for size in range(20, 900, 2):
        f = ImageFont.truetype(path, size)
        if wght:
            try:
                f.set_variation_by_axes([wght])
            except Exception:
                pass
        im = Image.new("L", (size * 3, size * 3), 0)
        ImageDraw.Draw(im).text((size // 2, size // 2), ch, 255, font=f)
        b = np.asarray(im) > 100
        ys = np.where(b.sum(axis=1) > 0)[0]
        if not len(ys):
            continue
        if ys.max() - ys.min() + 1 >= alto_px:
            xs = np.where(b.sum(axis=0) > 0)[0]
            return b[ys.min(): ys.max() + 1, xs.min(): xs.max() + 1]
    return None


def iou(a, b):
    """IoU tras llevar los dos a una malla común normalizada por alto."""
    H = 64
    def norm(m):
        h, w = m.shape
        nw = max(2, int(round(w * H / h)))
        return np.asarray(Image.fromarray((m * 255).astype("uint8")).resize((nw, H))) > 127
    A, B = norm(a), norm(b)
    W = max(A.shape[1], B.shape[1])
    def pad(m):
        o = np.zeros((H, W), bool)
        d = (W - m.shape[1]) // 2
        o[:, d:d + m.shape[1]] = m
        return o
    A, B = pad(A), pad(B)
    u = (A | B).sum()
    return (A & B).sum() / u if u else 0.0


def comparar(muestras, candidatas):
    res = {}
    for nombre, path, wght in candidatas:
        puntajes, anchos = [], []
        for ch, bm in muestras:
            r = render(ch, path, wght, bm.shape[0])
            if r is None:
                continue
            puntajes.append(iou(bm, r))
            anchos.append(abs((bm.shape[1] / bm.shape[0]) - (r.shape[1] / r.shape[0]))
                          / (bm.shape[1] / bm.shape[0]))
        if puntajes:
            res[nombre] = (float(np.mean(puntajes)), float(np.mean(anchos)) * 100, len(puntajes))
    return dict(sorted(res.items(), key=lambda kv: -kv[1][0]))

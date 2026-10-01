#!/usr/bin/env python3
"""Arma las tiras de revisión de noviembre (un carrusel se juzga montado en tira,
manual § 4 sexies · 10). Salida: out/tierracalma/nov2026/_tiras/"""
import pathlib, sys
from PIL import Image, ImageDraw
RAIZ = pathlib.Path(__file__).resolve().parent.parent
E = RAIZ / "out/tierracalma/nov2026/entrega"; T = RAIZ / "out/tierracalma/nov2026/_tiras"; T.mkdir(exist_ok=True)
G = {"E": [f"c-09-11-{i}" for i in range(1, 6)], "F1": [f"c-11-11-{i}" for i in range(1, 5)], "F2": [f"c-11-11-{i}" for i in range(5, 8)],
     "M1": [f"c-30-11-{i}" for i in range(1, 4)], "M2": [f"c-30-11-{i}" for i in range(4, 7)], "P": ["p-17-11", "p-24-11"], "S": ["st-13-11", "st-20-11", "st-26-11"]}
alto = int(sys.argv[1]) if len(sys.argv) > 1 else 900
for k, ids in G.items():
    ims = [Image.open(E / f"{i}.png").convert("RGB") for i in ids]
    ims = [im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS) for im in ims]
    s = Image.new("RGB", (sum(i.width + 10 for i in ims) - 10, alto), "white"); x = 0
    for im in ims: s.paste(im, (x, 0)); x += im.width + 10
    s.save(T / f"{k}.jpg", quality=90); print(k, s.size)

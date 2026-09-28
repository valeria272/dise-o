#!/usr/bin/env python3
"""BETWEEN · carta — vectoriza las ilustraciones a mano y el logo (potrace en Python puro).

La máscara PNG (alfa = tinta) se binariza y se traza con potrace: curvas Bézier, esquinas
optimizadas, motas de < 3 px fuera. Sale UN trazado compuesto por dibujo (evenodd), en
negro: el color se lo pone quien lo usa (beige, café o degradé).

`vtracer` da segfault en este Python (28-09-2026); potracer tarda ~1 min por dibujo.

    python scripts/between-carta-vectorizar.py [clave ...]     # sin claves: todas
Salida: public/assets/hilton/between/carta/vector/<clave>.svg
"""
import sys
from pathlib import Path
import numpy as np
import potrace
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
C = RAIZ / "public/assets/hilton/between/carta"
FUENTES = {f"mano-{k}": C / f"mano-{k}.png" for k in
           ("vitrina2", "desayuno", "cafeteria", "almuerzo", "ensalada", "postres", "coctel", "cerveza")}
FUENTES["logo"] = RAIZ / "public/assets/hilton/between/logo-blanco.png"


def trazar(k):
    im = Image.open(FUENTES[k]).convert("RGBA")
    if k == "logo":  # el logo es chico: se traza al doble para que las curvas salgan limpias
        im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    a = np.asarray(im)[..., 3]
    # potracer toma True como FONDO: se le pasa la máscara invertida (probado 28-09)
    curvas = potrace.Bitmap(a <= 110).trace(turdsize=3, alphamax=1.0, opticurve=True, opttolerance=0.2)
    d = []
    for c in curvas:
        p = c.start_point
        d.append(f"M{p.x:.1f} {p.y:.1f}")
        for s in c.segments:
            if s.is_corner:
                d.append(f"L{s.c.x:.1f} {s.c.y:.1f}L{s.end_point.x:.1f} {s.end_point.y:.1f}")
            else:
                d.append(f"C{s.c1.x:.1f} {s.c1.y:.1f} {s.c2.x:.1f} {s.c2.y:.1f} {s.end_point.x:.1f} {s.end_point.y:.1f}")
        d.append("Z")
    w, h = im.size
    (C / "vector").mkdir(exist_ok=True)
    (C / "vector" / f"{k}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
        f'<path fill="#000" fill-rule="evenodd" d="{"".join(d)}"/></svg>', encoding="utf-8")
    print(k, (w, h), len(curvas), "curvas")


if __name__ == "__main__":
    for k in (sys.argv[1:] or FUENTES):
        trazar(k)

#!/usr/bin/env python3
"""Tierra Calma — ¿hay dos fotos del mes que sean la misma? (R-20)

    python scripts/tc-parecido.py public/assets/tierracalma/nov [public/assets/tierracalma/oct]

Compara todas las imágenes de la primera carpeta entre sí y, si se da una
segunda, contra las de ésa (el mes anterior). La medida es la del manual
(§ «Una foto no se repite»): correlación de la imagen en gris a 64×64,
normalizada. **> 0,85 = es la misma imagen, aunque el md5 difiera.**

Sale con código 1 si algún par pasa el umbral.
"""
import itertools, pathlib, sys
import numpy as np
from PIL import Image

UMBRAL = 0.85

def firma(p, k=64):
    a = np.asarray(Image.open(p).convert("L").resize((k, k))).astype(float)
    return (a - a.mean()) / (a.std() + 1e-9)

def fotos(d):
    return sorted(p for p in pathlib.Path(d).iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png"))

def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    a = fotos(sys.argv[1]); b = fotos(sys.argv[2]) if len(sys.argv) > 2 else []
    f = {p: firma(p) for p in a + b}
    pares = [(x, y) for x, y in itertools.combinations(a, 2)] + [(x, y) for x in a for y in b]
    res = sorted(((float((f[x] * f[y]).mean()), x.name, y.name) for x, y in pares), reverse=True)
    for r, x, y in res[:8]:
        print(f"  {r:+.3f}  {x}  ·  {y}")
    malos = [t for t in res if t[0] > UMBRAL]
    print(f"\n{len(pares)} pares · máximo {res[0][0]:+.3f} · {'⛔ ' + str(len(malos)) + ' repetidas' if malos else '✓ ninguna repetida'}")
    return 1 if malos else 0

if __name__ == "__main__":
    raise SystemExit(main())

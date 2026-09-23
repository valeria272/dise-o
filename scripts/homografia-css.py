#!/usr/bin/env python3
"""matrix3d de CSS para pegar un plano (w×h, origen 0 0) sobre un cuadrilátero
medido en el frame. Uso: homografia-css.py W H x0,y0 x1,y1 x2,y2 x3,y3
(esquinas destino: arriba-izq, arriba-der, abajo-der, abajo-izq)."""
import sys
import numpy as np

w, h = float(sys.argv[1]), float(sys.argv[2])
dst = [tuple(map(float, a.split(","))) for a in sys.argv[3:7]]
src = [(0, 0), (w, 0), (w, h), (0, h)]
A = []; b = []
for (x, y), (u, v) in zip(src, dst):
    A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
    A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
hcoef = np.linalg.solve(np.array(A), np.array(b))
H = np.append(hcoef, 1).reshape(3, 3)
# CSS matrix3d (column-major): [[a,b,0,c],[d,e,0,f],[0,0,1,0],[g,h,0,i]]
m = [H[0,0], H[1,0], 0, H[2,0],  H[0,1], H[1,1], 0, H[2,1],  0, 0, 1, 0,  H[0,2], H[1,2], 0, H[2,2]]
print("matrix3d(" + ", ".join(f"{v:.6f}" for v in m) + ")")

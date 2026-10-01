#!/usr/bin/env python3
"""MyZoo Fase 3 — le devuelve el grano de cámara a la etiqueta calzada.

Por qué existe (01-10-2026): la escena pedida como fotografía real trae grano de sensor;
el packshot que `myzoo-f3-calzar.py` pone encima viene limpio, y un envase más nítido
y más liso que la foto que lo rodea se lee «pegado». Se mide el grano de la escena en
un parche de madera libre y se le suma el mismo grano SÓLO a los píxeles que el calce
cambió. La semilla es fija: el resultado se reproduce igual.

Uso:  python scripts/myzoo-f3-grano.py <escena> <calzada> <salida> [x0,y0,x1,y1 del parche]
"""
import sys

import cv2
import numpy as np

escena, calzada, salida = sys.argv[1:4]
x0, y0, x1, y1 = [int(v) for v in sys.argv[4].split(",")] if len(sys.argv) > 4 else (700, 700, 1000, 1000)

S = cv2.imread(escena).astype(np.float32)
C = cv2.imread(calzada).astype(np.float32)
d = S - cv2.GaussianBlur(S, (0, 0), 1.2)
grano = float(d[y0:y1, x0:x1].std())
cambiado = np.abs(C - S).max(axis=2) > 2
rng = np.random.default_rng(7)
g = cv2.GaussianBlur(rng.normal(0, 1, S.shape[:2]).astype(np.float32), (0, 0), 0.6)
g /= g.std()
m = cv2.GaussianBlur(cambiado.astype(np.float32), (0, 0), 2)[..., None]
out = np.clip(C + g[..., None] * min(grano, 3.0) * 0.7 * m, 0, 255).astype(np.uint8)
cv2.imwrite(salida, out)
print(f"✓ {salida}  (grano de la escena {grano:.2f})")

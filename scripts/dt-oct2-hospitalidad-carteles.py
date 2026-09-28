"""Repone los carteles REALES de la recepción sobre la hospitalidad generada (variante h2a).

Nano Banana reescribió los rótulos: «Hilton HONORS» salió «Hlhoo» y «SANTIAGO» bajo el reloj salió
«KARTOKIE». Se pega de vuelta la foto real (`fondos/checkin.jpg`) SÓLO en el recuadro de los carteles,
alineada por correlación de fase y con el borde fundido. Las personas no se tocan.
    py scripts/dt-oct2-hospitalidad-carteles.py
"""
import cv2, numpy as np
from PIL import Image
R = "raw/hilton/dt/familia/r3/"
g = np.asarray(Image.open(R + "nb-checkin-h2a.png").convert("RGB")).astype(np.float32)
H, W = g.shape[:2]
r = np.asarray(Image.open(R + "fondos/checkin.jpg").convert("RGB").resize((W, H), Image.LANCZOS)).astype(np.float32)
x0, y0, x1, y1 = 190, 1450, 560, 1805          # reloj + busto + cartel; la mamá empieza en x≈640
a = cv2.cvtColor(g[y0:y1, x0:x1], cv2.COLOR_RGB2GRAY); b = cv2.cvtColor(r[y0:y1, x0:x1], cv2.COLOR_RGB2GRAY)
(dx, dy), _ = cv2.phaseCorrelate(b, a)
M = np.float32([[1, 0, dx], [0, 1, dy]])
ra = cv2.warpAffine(r, M, (W, H), borderMode=cv2.BORDER_REFLECT)
m = np.zeros((H, W), np.float32); m[y0 + 20:y1 - 12, x0 + 20:x1 - 20] = 1
m = cv2.GaussianBlur(m, (0, 0), 10)[..., None]
out = ra * m + g * (1 - m)
Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(R + "final-checkin-h2a.png")
print("desfase", round(dx, 1), round(dy, 1))

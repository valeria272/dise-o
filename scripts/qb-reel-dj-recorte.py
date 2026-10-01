# -*- coding: utf-8 -*-
"""QB · Reel DJ — limpieza suave de un recorte de Magnific y hoja de comparación (R-101).

    python scripts/qb-reel-dj-recorte.py <fuente.jpg> <magnific.png> <salida.png> <hoja.jpg>

Limpieza: 1 px hacia adentro, suavizado ~1 px, color del borde tomado de adentro
(sin halo del fondo original) y desvanecido donde el sujeto toca el marco de la foto.
La hoja pone la foto original al lado del recorte sobre verde y sobre negro: se MIRA
antes de subirlo a Canva (cabeza, pelo, audífonos, manos).
"""
import sys
import cv2
import numpy as np
from PIL import Image

fuente, mag, salida, hoja = sys.argv[1:5]
src = Image.open(fuente).convert("RGB")
m = Image.open(mag).convert("RGBA")
if m.size != src.size:
    m = m.resize(src.size, Image.LANCZOS)
a = np.asarray(m).astype(np.float32)
rgb, al = a[..., :3], a[..., 3] / 255.0
k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
al2 = cv2.GaussianBlur(cv2.erode(al, k, iterations=1), (0, 0), 0.9)
# color del borde desde adentro: promedio ponderado por el alfa de un núcleo erosionado
nuc = cv2.erode((al > 0.95).astype(np.float32), k, iterations=3)
num = cv2.GaussianBlur(rgb * nuc[..., None], (0, 0), 4)
den = cv2.GaussianBlur(nuc, (0, 0), 4)[..., None]
dentro = np.where(den > 1e-3, num / np.maximum(den, 1e-3), rgb)
borde = ((al2 < 0.97) & (den[..., 0] > 0.02))[..., None]
rgb2 = np.where(borde, dentro, rgb)
# desvanecer donde toca el marco (abajo y costados)
h, w = al2.shape
f = np.ones((h, w), np.float32)
d = int(0.045 * h)
f[h - d:, :] *= np.linspace(1, 0, d)[:, None]
dx = int(0.02 * w)
for lado in (0, 1):
    col = al2[:, :3].mean() if lado == 0 else al2[:, -3:].mean()
    if col > 0.02:
        r = np.linspace(0, 1, dx)[None, :]
        if lado == 0: f[:, :dx] *= r
        else: f[:, w - dx:] *= r[:, ::-1]
al2 *= f
out = np.dstack([rgb2, al2 * 255]).clip(0, 255).astype(np.uint8)
ys, xs = np.where(al2 > 0.02)
caja = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
res = Image.fromarray(out, "RGBA").crop(caja)
res.save(salida)
print(salida, res.size, "caja en la fuente", caja)
def sobre(color):
    bg = Image.new("RGBA", src.size, color + (255,)); bg.alpha_composite(Image.fromarray(out, "RGBA")); return bg.convert("RGB")
t = [src, sobre((0, 200, 60)), sobre((0, 0, 0))]
H = 1100
t = [i.resize((round(i.width * H / i.height), H), Image.LANCZOS) for i in t]
c = Image.new("RGB", (sum(i.width for i in t), H)); x = 0
for i in t: c.paste(i, (x, 0)); x += i.width
c.save(hoja, quality=88)
# detalle de la cabeza a tamaño real (tercio superior del sujeto)
x0, y0, x1, y1 = caja; alto = int((y1 - y0) * 0.42)
det = [i.crop((x0, y0, x1, y0 + alto)) for i in (src, sobre((0, 200, 60)), sobre((0, 0, 0)))]
c = Image.new("RGB", (sum(i.width for i in det), alto)); x = 0
for i in det: c.paste(i, (x, 0)); x += i.width
if c.width > 3000: c = c.resize((3000, round(c.height * 3000 / c.width)), Image.LANCZOS)
c.save(hoja.replace(".jpg", "-cabeza.jpg"), quality=90)

"""Retoque LOCAL sobre el maestro: recorta una zona, Nano Banana la limpia, y se pega de vuelta sólo lo que
cambió (con borde suave). Para borrar una persona del fondo o un reflejo sin tocar al resto de la foto.
Uso: py scripts/dt-familia/retoque_local.py <escena> <x0> <y0> <x1> <y1> "<instrucción>" """
import sys, subprocess, shutil, os
import numpy as np, cv2
from PIL import Image
R = "raw/hilton/dt/familia/r3/"
k, x0, y0, x1, y1, ins = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
M = Image.open(R + f"maestro-{k}.jpg").convert("RGB")
if not os.path.exists(R + f"maestro-{k}-antes-retoque.jpg"): shutil.copy(R + f"maestro-{k}.jpg", R + f"maestro-{k}-antes-retoque.jpg")
crop = M.crop((x0, y0, x1, y1)); crop.save(R + f"ret-{k}-in.png")
prompt = (f"This is a crop of a real photograph. {ins} Fill the area with exactly the surrounding background "
          "(same wall, materials, texture, light). Change NOTHING else: same framing, size, colors and all other details.")
ratio = (x1 - x0) / (y1 - y0)
asp = "wide" if ratio > 1.4 else "feed" if ratio > 0.9 else "carrusel"
subprocess.run(["py", "scripts/magnific.py", "pro", prompt, "--refs", R + f"ret-{k}-in.png", "--aspecto", asp,
                "--resolucion", "2K", "--out", R + f"ret-{k}-out.png"], check=True, capture_output=True)
out = np.asarray(Image.open(R + f"ret-{k}-out.png").convert("RGB").resize(crop.size, Image.LANCZOS)).astype(float)
inp = np.asarray(crop).astype(float)
d = np.abs(cv2.GaussianBlur(out, (0, 0), 3) - cv2.GaussianBlur(inp, (0, 0), 3)).mean(2)
m = cv2.morphologyEx((d > 14).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
n, lb, st, _ = cv2.connectedComponentsWithStats(m); keep = np.zeros_like(m)
for i in range(1, n):
    if st[i, cv2.CC_STAT_AREA] > 0.003 * m.size: keep[lb == i] = 1
keep = cv2.dilate(keep, np.ones((25, 25), np.uint8))
a = cv2.GaussianBlur(keep.astype(float), (0, 0), 8)[..., None]
Mx = np.asarray(M).astype(float); Mx[y0:y1, x0:x1] = out * a + inp * (1 - a)
Image.fromarray(Mx.clip(0, 255).astype(np.uint8)).save(R + f"maestro-{k}.jpg", quality=93)
Image.fromarray(np.hstack([inp, Mx[y0:y1, x0:x1]]).clip(0, 255).astype(np.uint8)).save(f"out/_verificacion/ret-{k}.jpg", quality=88)
print(k, f"cambió {a.mean() * 100:.1f} % del recorte")

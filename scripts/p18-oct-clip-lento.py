"""Estira el clip de la ST 05-10 (Kling 2.5, 5 s a 24 fps) a 9 s a 30 fps con
interpolación por flujo óptico (DIS de OpenCV). El ffmpeg de Remotion no trae
`minterpolate`, y ralentizar sin interpolar se ve a saltos (12 fps efectivos).
Entrada: raw/hilton/piso18/oct/clips/st05_a.mp4 → public/assets/hilton/piso18/oct/s0510.mp4
"""
import subprocess, sys
from pathlib import Path
import cv2
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
ENT = RAIZ / "raw/hilton/piso18/oct/clips/st05_a.mp4"
TMP = RAIZ / "raw/hilton/piso18/oct/clips/st05_a-lento-mp4v.mp4"
OUT = RAIZ / "public/assets/hilton/piso18/oct/s0510.mp4"
SEG, FPS = 9.0, 30

c = cv2.VideoCapture(str(ENT))
fr = []
while True:
    ok, f = c.read()
    if not ok:
        break
    fr.append(f)
n = len(fr)
h, w = fr[0].shape[:2]
dis = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
gris = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY) for f in fr]
cache = {}
def flujo(i):
    if i not in cache:
        cache[i] = (dis.calc(gris[i], gris[i + 1], None), dis.calc(gris[i + 1], gris[i], None))
    return cache[i]
yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
vw = cv2.VideoWriter(str(TMP), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (w, h))
total = int(SEG * FPS)
for k in range(total):
    t = k * (n - 1) / (total - 1)
    i = min(int(t), n - 2)
    a = t - i
    if a < 1e-3:
        vw.write(fr[i]); continue
    fab, fba = flujo(i)
    # retro-warp de cada extremo hacia el instante intermedio
    A = cv2.remap(fr[i], xx - fab[..., 0] * a, yy - fab[..., 1] * a, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    B = cv2.remap(fr[i + 1], xx - fba[..., 0] * (1 - a), yy - fba[..., 1] * (1 - a), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    vw.write(cv2.addWeighted(A, 1 - a, B, a, 0))
vw.release()
OUT.parent.mkdir(parents=True, exist_ok=True)
npx = "npx.cmd" if sys.platform == "win32" else "npx"
subprocess.run([npx, "remotion", "ffmpeg", "-v", "error", "-i", str(TMP), "-c:v", "libx264", "-crf", "15",
                "-pix_fmt", "yuv420p", "-an", str(OUT), "-y"], check=True, cwd=str(RAIZ))
print(f"✓ {OUT.name}: {total} cuadros a {FPS} fps ({SEG} s) desde {n}")

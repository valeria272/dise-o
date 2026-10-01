#!/usr/bin/env python3
"""MyZoo — arma el reel 14 de octubre 2026 con los clips corregidos, SIN audio, texto ni logo.

Paulina lo edita en Canva: ahí pone textos, logo, música y la placa de cierre. Acá sólo
se unen las seis escenas con los mismos cortes de su reel original (medidos sobre
`14-reel.mp4`: 2,72 · 5,30 · 7,33 · 11,40 · 13,80 · 16,45 s), cada una desde su primer
cuadro y a velocidad normal, que es como ella las usó.

Sale a 1080×1920 y 24 fps, la cadencia nativa de los clips: sin escalar a 4K ni
interpolar a 60 fps, que es lo que dejaba el pelaje «de cera».

Uso:  python scripts/myzoo-reel14-armar.py
"""
import os
import subprocess
import sys

import cv2
import imageio_ffmpeg

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(RAIZ, "out/myzoo/reel-14-octubre")
SALIDA = os.path.join(DIR, "myzoo_reel14_sin-texto.mp4")
W, H, FPS = 1080, 1920, 24
# (clip, cuadros a 24 fps) — los cortes del reel original llevados a 24 fps
ESCENAS = [("01_corre.mp4", 65), ("02_revuelca.mp4", 62), ("03_pelo.mp4", 49),
           ("04_producto.mp4", 98), ("05_sentado.mp4", 57), ("06_cuerda.mp4", 64)]
# La cuerda es el clip ORIGINAL de Paulina: la versión regenerada (el perro mascando) «se ve
# muy rara» y ella prefiere la suya, donde sólo mueve la cabeza (01-10-2026).
FUENTE = {}


def encajar(f):
    """Escala al ancho y recorta el alto sobrante al centro (los clips no son 9:16 exactos)."""
    h, w = f.shape[:2]
    k = max(W / w, H / h)
    g = cv2.resize(f, (round(w * k), round(h * k)), interpolation=cv2.INTER_AREA if k < 1 else cv2.INTER_LANCZOS4)
    y, x = (g.shape[0] - H) // 2, (g.shape[1] - W) // 2
    return g[y:y + H, x:x + W]


tmp = SALIDA + ".part.mp4"
ff = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
                       "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-crf", "14",
                       "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp],
                      stdin=subprocess.PIPE)
total = 0
for clip, n in ESCENAS:
    cap = cv2.VideoCapture(FUENTE.get(clip, os.path.join(DIR, clip)))
    for i in range(n):
        ok, f = cap.read()
        if not ok:
            sys.exit(f"{clip}: sólo tiene {i} cuadros y se pidieron {n}")
        ff.stdin.write(encajar(f).tobytes())
    total += n
    print(f"  {clip}: {n} cuadros ({n / FPS:.2f} s) → corte en {total / FPS:.2f} s")
ff.stdin.close()
if ff.wait() != 0:
    sys.exit("ffmpeg falló")
os.replace(tmp, SALIDA)
print(f"✓ {SALIDA} — {total} cuadros, {total / FPS:.2f} s")

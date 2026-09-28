#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""De los clips de Kling (24 fps) a lo que usa la composición: 30 fps interpolados.

⛔ Lección de la story del 07/10 (24-09-2026): a 24 fps con `playbackRate`,
OffthreadVideo repetía cuadros («se queda pegado y con glitches»). Todo clip se pasa
ANTES a 30 fps con interpolación de movimiento y se reproduce a velocidad 1. Si un
tramo de voz es más largo que el clip, el clip se ralentiza acá (setpts), nunca en
Remotion. Requiere el ffmpeg completo de imageio-ffmpeg (el de Remotion no trae
minterpolate).
aza_k2: sólo los primeros 5 s — después la cámara se aleja de las puntas verdes y el
acero se lee galvanizado, que no es el Aza real (revisado cuadro a cuadro el 28-09).
"""
import os
import subprocess

import imageio_ffmpeg

AQUI = os.path.dirname(os.path.abspath(__file__))
FF = imageio_ffmpeg.get_ffmpeg_exe()
MI = "minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"

# id: (desde_s, hasta_s, factor de lentitud)  → salida <id>_30.mp4
PLAN = {
    "click_k1": (0, 5.04, 1.0),
    "click_k3": (0, 5.04, 1.0),
    "cat_k1": (0, 10.04, 1.0),
    "cat_k1b": (0, 5.04, 1.0),   # ronda 1: segunda escena del T1
    "cat_k4": (0, 5.04, 1.0),
    "aza_k1": (0, 5.04, 1.1),
    "aza_k2": (0, 5.0, 1.95),
    "aza_k3": (0, 5.04, 1.3),
    "lp_k1": (0, 5.04, 1.0),
    "lp_k2": (0, 10.04, 1.0),
    "lp_k3": (0, 5.04, 1.3),
}

for k, (a, b, lento) in PLAN.items():
    out = os.path.join(AQUI, f"{k}_30.mp4")
    vf = (f"setpts={lento}*PTS," if lento != 1 else "") + MI
    subprocess.run([FF, "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", os.path.join(AQUI, k + ".mp4"),
                    "-vf", vf, "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", "-an", out],
                   check=True)
    print("ok", k)

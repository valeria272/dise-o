#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · Reel DJ — deja la entrega de una semana: copia el MP4 «tiempos ajustados» a
`entrega/Reel n°1 S<n> QB OCT 26.mp4` y arma su GIF (360×640, 12,5 cps, sin difuminado).

    python scripts/qb-reel-dj-gif.py 2 3 5
"""
import os
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import imageio_ffmpeg  # el ffmpeg de Remotion no trae los filtros de paleta

FF = imageio_ffmpeg.get_ffmpeg_exe()
FILTRO = ("fps=12.5,scale=360:640:flags=lanczos,split[a][b];"
          "[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=none")

for n in [int(a) for a in sys.argv[1:] if a.isdigit()]:
    d = f"out/qb/oct/reel-dj-s{n}"
    video = f"{d}/Reel DJ 2026 S{n} OCT QB 26 - tiempos ajustados.mp4"
    os.makedirs(f"{d}/entrega", exist_ok=True)
    mp4, gif = f"{d}/entrega/Reel n°1 S{n} QB OCT 26.mp4", f"{d}/entrega/Reel n°1 S{n} QB OCT 26.gif"
    shutil.copyfile(video, mp4)
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-filter_complex", FILTRO, gif], check=True)
    print(f"S{n}: mp4 {os.path.getsize(mp4) / 1e6:.1f} MB · gif {os.path.getsize(gif) / 1e6:.1f} MB")

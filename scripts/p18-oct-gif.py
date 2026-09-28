#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — el GIF de la ST animada 05-10 «Primavera en Piso18».

Las decisiones son las de `scripts/p18-s4-gif.py` (R-35) —cadencia exacta en
centésimas y sin difuminado— salvo el tamaño: el acercamiento continuo cambia
todo el cuadro y a 540×960 pesaba 45,5 MB a 25 fps y 38,8 MB a 20 fps. Va a
432×768 y 20 fps (5 cs por cuadro, exacto). El GIF es para la grilla; lo que se
publica es el MP4. Video = MP4 + GIF, siempre (memoria `video-siempre-con-gif`).

    python scripts/p18-oct-gif.py
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
MP4 = RAIZ / "out/piso18/oct/entrega/S2/STS/P18 ST 05-10 Primavera en Piso18.mp4"
GIF = MP4.with_suffix(".gif")

ff = imageio_ffmpeg.get_ffmpeg_exe()
filtro = ("fps=20,scale=432:768:flags=lanczos,split[a][b];"
          "[a]palettegen=max_colors=255:stats_mode=diff[p];"
          "[b][p]paletteuse=dither=none:diff_mode=rectangle")
subprocess.run([ff, "-v", "error", "-i", str(MP4), "-filter_complex", filtro, "-loop", "0", str(GIF), "-y"],
               check=True)
print(f"✓ {GIF.name} ({GIF.stat().st_size / 1e6:.1f} MB)")

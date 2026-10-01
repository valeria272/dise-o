#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — el GIF de la ST animada 05-10 «Primavera en Piso18».

Las decisiones son las de `scripts/p18-s4-gif.py` (R-35) —cadencia exacta en
centésimas y sin difuminado— salvo el tamaño: el acercamiento continuo cambia
todo el cuadro y a 540×960 pesaba 45,5 MB a 25 fps y 38,8 MB a 20 fps. Va a
432×768 y 20 fps (5 cs por cuadro, exacto). El GIF es para la grilla; lo que se
publica es el MP4. Video = MP4 + GIF, siempre (memoria `video-siempre-con-gif`).

    python scripts/p18-oct-gif.py [0510 1610 2010 3010]
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
ENTREGA = RAIZ / "out/piso18/oct/entrega"
# pieza → (mp4, tamaño). Las de video real (16 y 30-10) cambian el cuadro entero en cada
# fotograma: van a 360×640 para no pasar los ~25 MB. El post del 20-10 tiene la foto quieta
# y pesa poco: va a 540×675.
PIEZAS = {
    "0510": ("S2/STS/P18 ST 05-10 Primavera en Piso18.mp4", "432:768"),
    "1610": ("S3/STS/P18 ST 16-10 Equipo Piso18.mp4", "360:640"),
    "2010": ("S4/FEED/P18 FEED 20-10 Cumpleanos en Piso18.mp4", "540:675"),
    "3010": ("S5/STS/P18 ST 30-10 Broche perfecto.mp4", "360:640"),
}

ff = imageio_ffmpeg.get_ffmpeg_exe()
for clave in (sys.argv[1:] or ["0510"]):
    rel, tam = PIEZAS[clave]
    mp4 = ENTREGA / rel
    gif = mp4.with_suffix(".gif")
    filtro = (f"fps=20,scale={tam}:flags=lanczos,split[a][b];"
              "[a]palettegen=max_colors=255:stats_mode=diff[p];"
              "[b][p]paletteuse=dither=none:diff_mode=rectangle")
    subprocess.run([ff, "-v", "error", "-i", str(mp4), "-filter_complex", filtro, "-loop", "0", str(gif), "-y"],
                   check=True)
    print(f"✓ {gif.name} ({gif.stat().st_size / 1e6:.1f} MB)")

"""PISO18 · OCTUBRE 2026 — mide una animada fotograma a fotograma (R-29).

Cero fotogramas congelados (diferencia 0,00 con el anterior) y cero negros. En las de
video real no se mide «salto > 25» como corte: el cruce entre planos dura 8 fotogramas.

    python scripts/p18-oct-medir-animada.py "out/piso18/oct/entrega/S3/STS/P18 ST 16-10 Equipo Piso18.mp4"
"""
import subprocess
import sys

import imageio_ffmpeg
import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W, H = 108, 192
for ruta in sys.argv[1:]:
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    crudo = subprocess.run([ff, "-v", "error", "-i", ruta, "-vf", f"scale={W}:{H}", "-f", "rawvideo",
                            "-pix_fmt", "gray", "-"], capture_output=True).stdout
    f = np.frombuffer(crudo, np.uint8).reshape(-1, H, W).astype(np.float32)
    d = np.abs(np.diff(f, axis=0)).mean(axis=(1, 2))
    medias = f.mean(axis=(1, 2))
    congelados = [i + 1 for i, v in enumerate(d) if v < 0.005]
    negros = [i for i, v in enumerate(medias) if v < 4]
    print(f"{ruta.split('/')[-1]}: {len(f)} fotogramas · congelados {congelados or 'ninguno'} · negros {negros or 'ninguno'}"
          f" · dif. media {d.mean():.2f} · máx {d.max():.2f} en el {int(d.argmax()) + 1}")

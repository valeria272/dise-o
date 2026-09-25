#!/usr/bin/env python3
"""Hoja de contacto de un clip: un cuadro cada N segundos, rotulado con su tiempo.

El QC de canon se hace mirando cuadros a buen tamaño, no reproduciendo el mp4
(lección del night run del Cap. 02). Usa el ffmpeg embebido de Remotion, que no
trae los filtros fps/tile: saca cuadro por cuadro con -ss y los pega con PIL.

    python3 scripts/hoja-clip.py clip.mp4 hoja.jpg [--cada 0.5] [--ancho 300]
"""
import argparse, os, subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageDraw

FF = Path(__file__).resolve().parent.parent / "node_modules/@remotion/compositor-darwin-arm64"
ENV = dict(os.environ, DYLD_LIBRARY_PATH=str(FF))

ap = argparse.ArgumentParser()
ap.add_argument("clip"); ap.add_argument("salida")
ap.add_argument("--cada", type=float, default=0.5); ap.add_argument("--ancho", type=int, default=300)
a = ap.parse_args()
info = subprocess.run([str(FF / "ffprobe"), "-v", "error", "-show_entries", "format=duration",
                       "-of", "csv=p=0", a.clip], env=ENV, capture_output=True, text=True).stdout
dur = float(info.strip() or 5)
tmp = Path(tempfile.mkdtemp())
cuadros, t = [], 0.0
while t < dur - 0.05:
    f = tmp / f"{t:05.2f}.png"
    subprocess.run([str(FF / "ffmpeg"), "-loglevel", "error", "-y", "-ss", f"{t:.2f}", "-i", a.clip,
                    "-frames:v", "1", str(f)], env=ENV)
    if f.exists():
        cuadros.append((t, Image.open(f).convert("RGB")))
    t += a.cada
w = a.ancho; h = int(cuadros[0][1].height * w / cuadros[0][1].width)
cols = min(6, len(cuadros)); filas = -(-len(cuadros) // cols)
hoja = Image.new("RGB", (cols * (w + 4), filas * (h + 22)), "black"); d = ImageDraw.Draw(hoja)
for i, (t, im) in enumerate(cuadros):
    x, y = (i % cols) * (w + 4), (i // cols) * (h + 22)
    hoja.paste(im.resize((w, h)), (x, y + 20)); d.text((x + 4, y + 4), f"{t:.1f}s", fill="yellow")
hoja.save(a.salida, quality=88)
print(f"{len(cuadros)} cuadros · {dur:.2f} s · {cuadros[0][1].size}")

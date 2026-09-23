#!/usr/bin/env python3
"""CAP. 02 — las hojas de control del FULL ROUGH.

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-qc-hojas.py out/gcl/cap02/full/GCL_CAP02_FULL_ROUGH_V1.mp4

Saca del render final:
  CAP02_CONTACT_SHEET.jpg   un frame representativo de cada plano, con su timecode
  G_CONTINUITY_SHEET.jpg    todos los frames principales donde aparece G, lado a
                            lado, con el G CHARACTER MASTER y el mejor frame del
                            bloque 1 como referencia a la izquierda
  R01_CONTINUITY_SHEET.jpg  lo mismo para R.01, con su madre a la izquierda

Los frames se extraen con el ffmpeg de Remotion (sin filtros: -ss + -frames:v 1).
"""
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FF = RAIZ / "node_modules/@remotion/compositor-darwin-arm64/ffmpeg"
os.environ["DYLD_LIBRARY_PATH"] = str(FF.parent)
FONT = str(RAIZ / "public/assets/fonts/copywriters/IBMPlexMono-Medium.ttf")
FPS = 30

# (plano, frame representativo)
PLANOS = [
    ("01 el tubo", 12), ("02a Marta", 27), ("02b Server", 40), ("02c R.01", 50), ("02d G eh?", 66),
    ("03 el único que camina", 120), ("04 el post-it", 190), ("04 macro", 200), ("05 la bandeja", 240),
    ("05 inserto copy", 158 + 72 + 20), ("06 dos hojas", 320), ("07 nueve", 410),
    ("08 la misión de R.01", 490), ("09 el cable · G", 555), ("09 el cielo", 588), ("09 el ticker", 625),
    ("10 medio Nivel -1", 700), ("10b un kilómetro", 820), ("10c el que baja", 890), ("ráfaga", 935),
    ("11 la carpeta", 1000), ("12 sube", 1120), ("13 calma", 1240), ("14 una cosita más", 1360),
    ("15 NO.", 1440), ("16 G", 1478), ("firma", 1540),
]
G_FRAMES = [("02d", 68), ("03 ini", 84), ("03 fin", 130), ("04", 175), ("06", 300), ("09", 550),
            ("10 ini", 650), ("10 med", 700), ("10 fin", 760), ("13", 1200), ("13 fin", 1300), ("16", 1478)]
R_FRAMES = [("02c", 52), ("07", 425), ("08 ini", 440), ("08 med", 490), ("08 fin", 528), ("10", 720),
            ("10b ini", 780), ("10b med", 820), ("ráfaga b", 935), ("11", 1035), ("12", 1080), ("13", 1290)]


def frame(video, f, out):
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{f / FPS:.3f}", "-i", str(video), "-frames:v", "1", str(out)], check=True)
    return Image.open(out).convert("RGB")


def hoja(titulo, items, w, cols, refs=None, out=None):
    """items: [(etiqueta, imagen)] · refs: [(etiqueta, imagen)] a la izquierda, separadas."""
    h = int(w * 16 / 9)
    font = ImageFont.truetype(FONT, 14); big = ImageFont.truetype(FONT, 22)
    todo = (refs or []) + items
    nref = len(refs or [])
    filas = (len(todo) + cols - 1) // cols
    W = cols * (w + 6) + 6 + (30 if nref else 0); H = 56 + filas * (h + 26)
    im = Image.new("RGB", (W, H), (10, 12, 14)); d = ImageDraw.Draw(im)
    d.text((10, 14), titulo, font=big, fill=(255, 45, 141))
    for i, (lab, img) in enumerate(todo):
        c, r = i % cols, i // cols
        x = 6 + c * (w + 6) + (30 if (nref and i >= nref) else 0); y = 56 + r * (h + 26)
        img = img.copy(); img.thumbnail((w, h)); im.paste(img, (x, y + 20))
        d.text((x + 4, y + 2), lab, font=font, fill=(255, 45, 141) if i < nref else (230, 230, 225))
        if nref and i == nref - 1:
            d.line([(x + w + 18, y), (x + w + 18, y + h + 24)], fill=(255, 45, 141), width=2)
    im.save(out, quality=90); print(f"  ✓ {out}")


def main(video):
    video = Path(video); out = video.parent; tmp = out / "_frames"; tmp.mkdir(exist_ok=True)
    # contact sheet: un frame por plano
    items = [(f"{n}  ·  {f // FPS:d}:{(f % FPS) * 100 // FPS:02d}s  f.{f}", frame(video, f, tmp / f"c_{f}.png")) for n, f in PLANOS]
    hoja("CAP.02 «ES UN CAMBIO CHICO» · FULL ROUGH V1 · un frame por plano", items, 200, 9, out=out / "CAP02_CONTACT_SHEET.jpg")
    # G: la madre y el mejor frame del bloque 1 a la izquierda
    ref_master = Image.open(RAIZ / "gcl-agent/character-master/gcl_master_frontal_logo.png").convert("RGB")
    ref_b1 = frame(video, 100, tmp / "g_ref_b1.png")
    gi = [(f"{n}  f.{f}", frame(video, f, tmp / f"g_{f}.png")) for n, f in G_FRAMES]
    hoja("G · CONTINUIDAD · madre + mejor frame del bloque 1 | todos los planos con G", gi, 210, 7,
         refs=[("G MASTER", ref_master), ("BLOQUE 1 · f.100", ref_b1)], out=out / "G_CONTINUITY_SHEET.jpg")
    # R.01
    ref_r = Image.open(RAIZ / "gcl-agent/universo/03_G_CREW/R01/laminas/01_master_34.png").convert("RGB")
    ri = [(f"{n}  f.{f}", frame(video, f, tmp / f"r_{f}.png")) for n, f in R_FRAMES]
    hoja("R.01 · CONTINUIDAD · madre | todos los planos con R.01", ri, 210, 7, refs=[("R.01 MASTER V2", ref_r)], out=out / "R01_CONTINUITY_SHEET.jpg")


if __name__ == "__main__":
    main(sys.argv[1])

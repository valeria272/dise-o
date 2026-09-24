#!/usr/bin/env python3
"""Reconstruye Scotch Display (titulares del estilo nuevo de Selfie) en esta máquina.

    ~/copylab-venv/bin/python3 scripts/selfie-fuentes-scotch.py

POR QUÉ EXISTE (24-09-2026). Scotch Display es de ADOBE FONTS: no se empaqueta con el
editable y NO va al repo (misma regla que IvyOra, IvyPresto y la Bebas Neue Pro de
CAVA). Pero los .ai de Coni traen incrustados los subconjuntos CFF que usaron. Este
script:
  1. baja los tres editables de sept S2-S3 de Drive si no están en raw/,
  2. extrae los subconjuntos Scotch con scripts/cava-fuentes-desde-editable.py
     (FILTRO=Scotch) y
  3. los convierte a TrueType (Chrome rechaza las OTF CFF: ver la memoria de
     Brushwell) en public/assets/fonts/selfie-2026/, que es lo que leen las
     composiciones de Selfie.
⚠️ Es un SUBCONJUNTO: sólo las letras que Coni ya usó. El script lista cuáles hay. Para
un copy libre, activa Scotch Display en Creative Cloud.
"""
import os
import subprocess
import sys
from pathlib import Path

from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont, newTable

RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "raw/selfie/editables-sep2026"
OTF = RAW / "fuentes"
DEST = RAIZ / "public/assets/fonts/selfie-2026"
EDITABLES = {  # Drive, carpeta EDITABLES de Coni (1kQJzz3qtKexpwpO6XPRxOJMwJql0FFl2)
    "GRILLA SEPT_S2-S3.ai": "1gGQbVh0MrIx3U9oBP1VonjkZeF0WMUrY",
    "BANNER SEPT_S3-S3.ai": "1ab9sP7NN1NRqxnpCbO3w-wmga_hLqifU",
    "MAILSEPT_S2-S3.ai": "17BbOFOkH5m9tt36BxjbsIaCF8x9VLj5Y",
}


def a_ttf(otf: Path, ttf: Path):
    ft = TTFont(otf)
    gs, orden = ft.getGlyphSet(), ft.getGlyphOrder()
    glifos = {}
    for g in orden:
        pen = TTGlyphPen(gs)
        gs[g].draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
        glifos[g] = pen.glyph()
    del ft["CFF "]
    ft["glyf"] = newTable("glyf")
    ft["glyf"].glyphs, ft["glyf"].glyphOrder = glifos, orden
    ft["loca"] = newTable("loca")
    mx = ft["maxp"]
    mx.tableVersion = 0x00010000
    for a in ("maxZones", "maxTwilightPoints", "maxStorage", "maxFunctionDefs", "maxInstructionDefs",
              "maxStackElements", "maxSizeOfInstructions", "maxComponentElements", "maxPoints",
              "maxContours", "maxCompositePoints", "maxCompositeContours", "maxComponentDepth"):
        setattr(mx, a, 0)
    mx.maxZones = 1
    ft["head"].glyphDataFormat, ft["head"].indexToLocFormat = 0, 0
    ft["post"].formatType, ft["post"].extraNames, ft["post"].mapping = 2.0, [], {}
    ft.sfntVersion = "\x00\x01\x00\x00"
    ft.save(ttf)


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    for nombre, fid in EDITABLES.items():
        ruta = RAW / nombre
        if not ruta.exists() or ruta.stat().st_size < 1_000_000:
            print(f"↓ {nombre}")
            subprocess.run(["curl", "-sL", "-o", str(ruta),
                            f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"], check=True)
    env = dict(os.environ, FILTRO="Scotch")
    subprocess.run([sys.executable, str(RAIZ / "scripts/cava-fuentes-desde-editable.py"), str(OTF),
                    *[str(RAW / n) for n in EDITABLES]], env=env, check=True)
    DEST.mkdir(parents=True, exist_ok=True)
    for otf in sorted(OTF.glob("ScotchDisplay*.otf")):
        a_ttf(otf, DEST / (otf.stem + ".ttf"))
        print(f"✓ {otf.stem}.ttf")


if __name__ == "__main__":
    main()

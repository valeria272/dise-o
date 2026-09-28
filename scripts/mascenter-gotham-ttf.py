#!/usr/bin/env python3
"""MÁS CENTER — convierte la Gotham de los editables de Diego a TrueType para Chrome y Remotion.

Por qué: Chrome (OTS) rechaza en silencio algunos .otf con contornos CFF y el texto sale con
una fuente de reemplazo sin avisar (memoria brushwell-no-cargaba-en-chrome). Se convierten los
contornos CFF a TrueType (glyf) con fontTools + cu2qu.

De dónde salen (lo que usan los .ai de 2026, leídos con PyMuPDF el 25-09-2026):
  Gotham-Black          → titular en pastilla, display          (instalada en Windows por Diego)
  GothamRnd-Bold/Book/Medium, GothamRounded-Light/Medium        (paquete FEB 2026 del disco KINGSTON
                                                                 o instaladas en Windows)
Uso:
    python scripts/mascenter-gotham-ttf.py            # busca en las carpetas de fuentes de esta máquina
    python scripts/mascenter-gotham-ttf.py <carpeta>  # o en una carpeta dada
Escribe en clients/mascenter/sistema/assets/fonts/ y public/assets/fonts/mascenter/.
"""
import os
import sys
from pathlib import Path

from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent
DESTINOS = [RAIZ / "clients/mascenter/sistema/assets/fonts", RAIZ / "public/assets/fonts/mascenter"]

# nombre PostScript → archivo de salida
QUIERO = {
    "Gotham-Black": "Gotham-Black.ttf",
    "GothamRnd-Bold": "GothamRnd-Bold.ttf",
    "GothamRnd-Medium": "GothamRnd-Medium.ttf",
    "GothamRnd-Book": "GothamRnd-Book.ttf",
    "GothamRounded-Light": "GothamRounded-Light.ttf",
    "GothamRounded-Medium": "GothamRounded-Medium.ttf",
    "GothamRounded-Bold": "GothamRounded-Bold.ttf",      # titular del reel de pauta (PERFOMANCE MASCENTER AGOSTO.aep)
}


def carpetas():
    if len(sys.argv) > 1:
        return [Path(sys.argv[1])]
    la, ad = os.environ.get("LOCALAPPDATA", ""), os.environ.get("APPDATA", "")
    return [Path(la) / "Microsoft/Windows/Fonts", Path(r"C:\Windows\Fonts"),
            Path(r"D:\DIEGO 2023\COPYWRITERS\MAS CENTER\MAS CENTER TRASPASO\FEB 2026, DISEÑO NUEVO\IFB_FEB_Carpeta\Fonts"),
            Path.home() / "Library/Fonts"]


def buscar():
    hallado = {}
    for base in carpetas():
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if p.suffix.lower() not in (".otf", ".ttf") or not p.is_file():
                continue
            try:
                ps = TTFont(p, lazy=True)["name"].getDebugName(6)
            except Exception:
                continue
            if ps in QUIERO and ps not in hallado:
                hallado[ps] = p
    return hallado


def a_truetype(src: Path) -> TTFont:
    f = TTFont(src)
    if "CFF " not in f:
        return f                                   # ya es TrueType
    orden = f.getGlyphOrder()
    gs = f.getGlyphSet()
    glyf = newTable("glyf"); glyf.glyphOrder = orden; glyf.glyphs = {}
    for nombre in orden:
        pen = TTGlyphPen(gs)
        gs[nombre].draw(Cu2QuPen(pen, max_err=1.0, reverse_direction=True))
        glyf.glyphs[nombre] = pen.glyph()
    f["glyf"] = glyf
    f["loca"] = newTable("loca")
    del f["CFF "]
    if "VORG" in f:
        del f["VORG"]
    maxp = f["maxp"]; maxp.tableVersion = 0x00010000
    for k in ("maxZones", "maxTwilightPoints", "maxStorage", "maxFunctionDefs", "maxInstructionDefs",
              "maxStackElements", "maxSizeOfInstructions", "maxComponentElements"):
        setattr(maxp, k, 0)
    maxp.maxZones = 1
    f["head"].glyphDataFormat = 0
    f["post"].formatType = 2.0
    f["post"].extraNames = []; f["post"].mapping = {}
    f.sfntVersion = "\x00\x01\x00\x00"
    return f


def arreglar_nbsp(f: TTFont) -> TTFont:
    """Las GothamRnd (Bold, Book, Medium) traen el espacio duro U+00A0 con un avance de 25.000 unidades (el espacio
    normal mide 300). Chrome lo respeta: un «14:00&nbsp;hrs.» o un «Más&nbsp;Center» sale partido con un hueco
    enorme. Hallado el 28-09-2026 en el post del Mercado Campesino. El espacio duro mide lo mismo que el espacio."""
    cm, hm = f.getBestCmap(), f["hmtx"]
    if 0xA0 in cm and 0x20 in cm and hm[cm[0xA0]][0] != hm[cm[0x20]][0]:
        hm[cm[0xA0]] = (hm[cm[0x20]][0], hm[cm[0xA0]][1])
    return f


def main():
    hallado = buscar()
    faltan = [ps for ps in QUIERO if ps not in hallado]
    for d in DESTINOS:
        d.mkdir(parents=True, exist_ok=True)
    for ps, src in sorted(hallado.items()):
        f = arreglar_nbsp(a_truetype(src))
        for d in DESTINOS:
            f.save(d / QUIERO[ps])
        print(f"✓ {ps:22s} ← {src}")
    if faltan:
        print("✗ faltan:", ", ".join(faltan), "— instálalas o pasa la carpeta como argumento")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""BETWEEN · carta oficial R5 — PDF de IMPRENTA desde el PDF en bruto que deja Illustrator
(`between-carta-oficial-ai-r5.jsx`: mesas de 176 × 306 mm = hoja 170 × 300 + 3 mm por lado).

Illustrator por script no respeta el sangrado del PDF (probado con los pendones DT, 28-09), así que
el sangrado va en la mesa y acá se arma la hoja de imprenta: marcas de corte FUERA del sangrado,
TrimBox 170 × 300 mm y BleedBox 176 × 306 mm. Además revisa lo que pidió Eli:
  · que el fondo llegue al borde del sangrado (sin franja blanca en ningún lado)
  · el cuerpo de texto más chico de todo el PDF (mínimo 7,5 pt)

    python scripts/between-carta-oficial-imprenta-r5.py [A B C D]
Salida: …/r5/editable/maestro/BW-CARTA-BETWEEN-OPCION-<X>-IMPRENTA.pdf
"""
import sys
from pathlib import Path
import pymupdf as fitz
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
MAE = RAIZ / "out/hilton/between/carta-oficial/r5/editable/maestro"
MM = 72 / 25.4
SANG, MARGEN, LARGO, SEP = 3 * MM, 12 * MM, 6 * MM, 2 * MM


def revisar_borde(pag):
    """¿El sangrado queda pintado hasta el filo? Mira una franja de 1 mm en los cuatro bordes."""
    pix = pag.get_pixmap(dpi=40, colorspace=fitz.csRGB)
    w, h, s = pix.width, pix.height, pix.samples
    blancos = 0
    for x in range(w):
        for y in (0, h - 1):
            i = (y * w + x) * 3
            if min(s[i:i + 3]) > 250:
                blancos += 1
    for y in range(h):
        for x in (0, w - 1):
            i = (y * w + x) * 3
            if min(s[i:i + 3]) > 250:
                blancos += 1
    return blancos


def cuerpos(doc):
    minimo, donde = 99, ""
    for n, p in enumerate(doc, 1):
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for sp in l["spans"]:
                    if sp["text"].strip() and sp["size"] < minimo:
                        minimo, donde = sp["size"], f"hoja {n}: «{sp['text'].strip()[:30]}»"
    return minimo, donde


def armar(op):
    bruto = MAE / f"BW-CARTA-BETWEEN-OPCION-{op}-IMPRENTA-BRUTO.pdf"
    salida = MAE / f"BW-CARTA-BETWEEN-OPCION-{op}-IMPRENTA.pdf"
    src = fitz.open(bruto)
    out = fitz.open()
    malos = []
    for i, sp in enumerate(src):
        w, h = sp.rect.width, sp.rect.height
        if abs(w - (170 * MM + 2 * SANG)) > 1 or abs(h - (300 * MM + 2 * SANG)) > 1:
            sys.exit(f"x {bruto.name} hoja {i + 1}: mide {w / MM:.1f} × {h / MM:.1f} mm, se esperaba 176 × 306")
        if revisar_borde(sp):
            malos.append(i + 1)
        pg = out.new_page(width=w + 2 * MARGEN, height=h + 2 * MARGEN)
        pg.show_pdf_page(fitz.Rect(MARGEN, MARGEN, MARGEN + w, MARGEN + h), src, i)
        t = fitz.Rect(MARGEN + SANG, MARGEN + SANG, MARGEN + w - SANG, MARGEN + h - SANG)
        for x in (t.x0, t.x1):
            for y, s in ((t.y0, -1), (t.y1, 1)):
                a = y + s * (SANG + SEP)
                pg.draw_line((x, a), (x, a + s * LARGO), color=(0, 0, 0), width=0.25)
        for y in (t.y0, t.y1):
            for x, s in ((t.x0, -1), (t.x1, 1)):
                a = x + s * (SANG + SEP)
                pg.draw_line((a, y), (a + s * LARGO, y), color=(0, 0, 0), width=0.25)
        pg.set_mediabox(pg.rect)
        pg.set_bleedbox(fitz.Rect(MARGEN, MARGEN, MARGEN + w, MARGEN + h))
        pg.set_trimbox(t)
        pg.insert_text((MARGEN, MARGEN - 4 * MM),
                       f"Between · carta {op} · hoja {i + 1} de {len(src)} · corte 170 × 300 mm · sangrado 3 mm · CMYK Coated FOGRA39",
                       fontsize=6, color=(0, 0, 0))
    out.save(salida, garbage=3, deflate=True)
    minimo, donde = cuerpos(src)
    print(("✓" if not malos else "⚠"), salida.name, f"{len(src)} hojas",
          f"· cuerpo mínimo {minimo:.2f} pt ({donde})",
          f"· ⚠ borde sin color en hojas {malos}" if malos else "· sangrado pintado en las 4 orillas")


if __name__ == "__main__":
    for op in sys.argv[1:] or "ABCD":
        armar(op)

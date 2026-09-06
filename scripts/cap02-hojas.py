#!/usr/bin/env python3
"""CAP. 02 — LAS HOJAS DE MARTA. Todo lo que tiene que LEERSE se compone acá.

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-hojas.py

Regla del capítulo (V1.6 §D): nunca se genera texto legible. Las hojas se
generan en blanco (papel continuo de rayas verdes, bordes perforados — es
Marta) y el contenido se pone encima en Post. Este script hace las placas.

EL CAMBIO CHICO, por fin con nombre: **GRATIS → SIN COSTO.**
Es el cambio que toda agencia ha recibido de legal, es una sola palabra, y es
más larga que la original — por eso rompe la caja del layout y arrastra los
nueve formatos. ME RECONOZCO, sin explicar nada.

Salen en public/assets/gcl/cap02/hojas/:
  copy.png        el copy con GRATIS encerrado en rosa y SIN COSTO escrito a mano encima
  layout.png      el layout: la caja con ENVÍO SIN COSTO desbordándose (exagerado, V1.6)
  f_1-1.png …     las nueve etiquetas de formato, una por hoja
  NO.png          la hoja del final
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
F = RAIZ / "public/assets/fonts/copywriters"
OUT = RAIZ / "public/assets/gcl/cap02/hojas"
OUT.mkdir(parents=True, exist_ok=True)

ROSA = (255, 45, 141, 255)
TINTA = (24, 28, 32, 255)
MONO = str(F / "IBMPlexMono-Medium.ttf")
MANO = str(F / "Caveat-Variable.ttf")
IMPACTO = str(F / "Archivo-Variable.ttf")


def papel(w=1100, h=1500):
    """Papel continuo de Marta: rayas verdes tenues y bordes perforados."""
    im = Image.new("RGBA", (w, h), (246, 247, 240, 255))
    d = ImageDraw.Draw(im)
    for y in range(0, h, 44):
        if (y // 44) % 2 == 0:
            d.rectangle([0, y, w, y + 22], fill=(220, 234, 220, 255))
    for x in (40, w - 40):                                  # las tiras perforadas
        d.line([(x, 0), (x, h)], fill=(200, 200, 195, 255), width=1)
        for y in range(30, h, 60):
            d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=(120, 120, 115, 255))
            d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=(246, 247, 240, 255))
    return im


def fuente(ruta, tam, variacion=None):
    f = ImageFont.truetype(ruta, tam)
    if variacion:
        try:
            f.set_variation_by_axes(variacion)
        except Exception:
            pass
    return f


# ── copy.png ─────────────────────────────────────────────────────────────────
im = papel(); d = ImageDraw.Draw(im)
mono = fuente(MONO, 30); grande = fuente(MONO, 62)
d.text((90, 120), "COPY · CAMPAÑA PRIMAVERA · v07", font=mono, fill=(90, 95, 100, 255))
d.text((90, 175), "TITULAR:", font=mono, fill=(90, 95, 100, 255))
d.text((90, 240), "ENVÍO GRATIS", font=grande, fill=TINTA)
d.text((90, 330), "A TODO CHILE", font=grande, fill=TINTA)
d.text((90, 440), "BAJADA: compra hoy, recibe mañana.", font=mono, fill=TINTA)
# el círculo rosado a mano alrededor de GRATIS (Marta ya lo marcó)
x0, y0, x1, y1 = 300, 218, 560, 318
for k in range(3):
    d.ellipse([x0 - k, y0 - k, x1 + k, y1 + k], outline=ROSA, width=5)
mano = fuente(MANO, 84, {"wght": 600})
d.text((320, 130), "SIN COSTO", font=mano, fill=ROSA)
d.line([(430, 205), (440, 225)], fill=ROSA, width=5)        # la flechita
im.save(OUT / "copy.png"); print("  ✓ copy.png")

# ── layout.png ───────────────────────────────────────────────────────────────
im = papel(); d = ImageDraw.Draw(im)
d.text((90, 120), "LAYOUT · FEED 1:1 · v07 → v08", font=mono, fill=(90, 95, 100, 255))
# la caja del titular: la palabra nueva NO CABE — exagerado, para leerse a 85 mm
caja = [140, 300, 760, 560]
d.rectangle(caja, outline=TINTA, width=4)
d.rectangle([140, 300, 760, 340], fill=TINTA)
d.text((156, 306), "TITULAR", font=fuente(MONO, 22), fill=(246, 247, 240, 255))
imp = fuente(IMPACTO, 118, {"wght": 900, "wdth": 80})
d.text((160, 360), "ENVÍO", font=imp, fill=TINTA)
d.text((160, 470), "SIN COSTO", font=imp, fill=TINTA)      # se sale por la derecha: 160 + ~780 > 760
# el desborde marcado en rosa
d.line([(760, 460), (760, 580)], fill=ROSA, width=6)
d.text((790, 470), "!!", font=fuente(MANO, 90, {"wght": 700}), fill=ROSA)
d.text((520, 610), "no cabe", font=fuente(MANO, 56, {"wght": 600}), fill=ROSA)
im.save(OUT / "layout.png"); print("  ✓ layout.png")

# ── las nueve ────────────────────────────────────────────────────────────────
for etiqueta in ["1:1", "4:5", "9:16", "16:9", "STORY", "CARRUSEL", "BANNER", "MAIL", "PPT"]:
    im = papel(900, 1100); d = ImageDraw.Draw(im)
    d.text((80, 90), "FORMATO", font=fuente(MONO, 26), fill=(90, 95, 100, 255))
    d.text((80, 150), etiqueta, font=fuente(IMPACTO, 150, {"wght": 900, "wdth": 78}), fill=TINTA)
    d.text((80, 360), "ENVÍO SIN COSTO", font=fuente(MONO, 40), fill=TINTA)
    d.rectangle([80, 440, 820, 1000], outline=(160, 160, 155, 255), width=3)
    nombre = "f_" + etiqueta.replace(":", "-").lower() + ".png"
    im.save(OUT / nombre); print(f"  ✓ {nombre}")

# ── NO.png ───────────────────────────────────────────────────────────────────
im = papel(1100, 800); d = ImageDraw.Draw(im)
d.text((90, 200), "NO.", font=fuente(IMPACTO, 420, {"wght": 900, "wdth": 78}), fill=TINTA)
im.save(OUT / "NO.png"); print("  ✓ NO.png")

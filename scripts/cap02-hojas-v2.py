#!/usr/bin/env python3
"""CAP. 02 · CLARITY CUT V2 — LAS HOJAS CON SELLO. La cadena de consecuencias,
legible en un vistazo.

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-hojas-v2.py

Diagnóstico de la V1 (06-09): el copy y el layout se veían 0,4 s y nada decía
QUÉ era cada consecuencia. La V2 les da tiempo (1,2–1,4 s) y a cada hoja de
Marta le pone un SELLO de goma en rosa con el nombre de lo que cambió:
COPY → DISEÑO → FORMATOS ×9 → VIDEO → LANDING → PAUTA → PRESENTACIÓN.
Es diegético (es el sello del departamento sobre la hoja), no es una placa.
El sello es lo único que hace falta leer; el resto de la hoja es textura.

Salen en public/assets/gcl/cap02/hojas/v2_*.png
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
F = RAIZ / "public/assets/fonts/copywriters"
OUT = RAIZ / "public/assets/gcl/cap02/hojas"
ROSA = (255, 45, 141, 255)
TINTA = (24, 28, 32, 255)
GRIS = (90, 95, 100, 255)
MONO = str(F / "IBMPlexMono-Medium.ttf")
MANO = str(F / "Caveat-Variable.ttf")
IMPACTO = str(F / "Archivo-Variable.ttf")


def papel(w=1100, h=1500):
    im = Image.new("RGBA", (w, h), (246, 247, 240, 255)); d = ImageDraw.Draw(im)
    for y in range(0, h, 44):
        if (y // 44) % 2 == 0: d.rectangle([0, y, w, y + 22], fill=(220, 234, 220, 255))
    for x in (40, w - 40):
        d.line([(x, 0), (x, h)], fill=(200, 200, 195, 255), width=1)
        for y in range(30, h, 60):
            d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=(120, 120, 115, 255)); d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=(246, 247, 240, 255))
    return im


def fuente(ruta, tam, variacion=None):
    f = ImageFont.truetype(ruta, tam)
    if variacion:
        try: f.set_variation_by_axes(variacion)
        except Exception: pass
    return f


def sello(im, texto, xy=(70, 40), rot=-4, tam=150):
    """El sello de goma: marco rosa, texto en Archivo 900 estrecho, un poco torcido y con la tinta gastada."""
    f = fuente(IMPACTO, tam, {"wght": 900, "wdth": 78})
    tw = int(f.getlength(texto)); pad = 34
    w, h = tw + pad * 2, tam + pad
    s = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    d.rounded_rectangle([20, 20, 20 + w, 20 + h], radius=18, outline=ROSA, width=9)
    d.text((20 + pad, 20 + pad // 2 - tam * 0.08), texto, font=f, fill=ROSA)
    # tinta gastada: agujeros de alfa
    import random
    rnd = random.Random(len(texto) * 7)
    px = s.load()
    for _ in range(int(w * h * 0.012)):
        x, y = rnd.randrange(s.width), rnd.randrange(s.height)
        if px[x, y][3] > 0: px[x, y] = (255, 45, 141, rnd.randrange(60, 200))
    s = s.rotate(rot, resample=Image.BICUBIC, expand=True)
    im.alpha_composite(s, (xy[0], xy[1]))
    return im


def cabecera(d, texto, y=270):
    d.text((90, y), texto, font=fuente(MONO, 30), fill=GRIS)


# ── 1 · COPY ─────────────────────────────────────────────────────────────────
im = papel(); d = ImageDraw.Draw(im)
im = sello(im, "COPY"); d = ImageDraw.Draw(im)
cabecera(d, "COPY · CAMPAÑA PRIMAVERA · v07 → v08", 300)
grande = fuente(MONO, 62); mono = fuente(MONO, 30)
d.text((90, 355), "TITULAR:", font=mono, fill=GRIS)
d.text((90, 420), "ENVÍO GRATIS", font=grande, fill=TINTA)
d.text((90, 510), "A TODO CHILE", font=grande, fill=TINTA)
d.text((90, 620), "BAJADA: compra hoy, recibe mañana.", font=mono, fill=TINTA)
x0, y0, x1, y1 = 300, 398, 560, 498
for k in range(3): d.ellipse([x0 - k, y0 - k, x1 + k, y1 + k], outline=ROSA, width=5)
d.text((330, 300), "SIN COSTO", font=fuente(MANO, 84, {"wght": 600}), fill=ROSA)
d.line([(440, 380), (450, 400)], fill=ROSA, width=5)
d.text((90, 760), "un cambio chico: una palabra.", font=fuente(MANO, 52, {"wght": 500}), fill=GRIS)
im.save(OUT / "v2_copy.png"); print("  ✓ v2_copy.png")

# ── 2 · DISEÑO ───────────────────────────────────────────────────────────────
im = papel(); d = ImageDraw.Draw(im)
im = sello(im, "DISEÑO"); d = ImageDraw.Draw(im)
cabecera(d, "LAYOUT · FEED 1:1 · v07 → v08", 300)
caja = [140, 420, 760, 680]
d.rectangle(caja, outline=TINTA, width=4); d.rectangle([140, 420, 760, 460], fill=TINTA)
d.text((156, 426), "TITULAR", font=fuente(MONO, 22), fill=(246, 247, 240, 255))
imp = fuente(IMPACTO, 118, {"wght": 900, "wdth": 80})
d.text((160, 480), "ENVÍO", font=imp, fill=TINTA); d.text((160, 590), "SIN COSTO", font=imp, fill=TINTA)
d.line([(760, 580), (760, 700)], fill=ROSA, width=6)
d.text((790, 590), "!!", font=fuente(MANO, 90, {"wght": 700}), fill=ROSA)
d.text((520, 730), "no cabe", font=fuente(MANO, 56, {"wght": 600}), fill=ROSA)
im.save(OUT / "v2_layout.png"); print("  ✓ v2_layout.png")

# ── 3 · FORMATOS ×9 ──────────────────────────────────────────────────────────
im = papel(); d = ImageDraw.Draw(im)
im = sello(im, "FORMATOS ×9", tam=120); d = ImageDraw.Draw(im)
cabecera(d, "ADAPTACIONES · v08 · todas de nuevo", 280)
etq = ["1:1", "4:5", "9:16", "16:9", "STORY", "CARRUSEL", "BANNER", "MAIL", "PPT"]
fe = fuente(IMPACTO, 46, {"wght": 900, "wdth": 78}); fm = fuente(MONO, 20)
for i, e in enumerate(etq):
    c, r = i % 3, i // 3; x, y = 90 + c * 310, 340 + r * 360
    d.rectangle([x, y, x + 280, y + 320], fill=(250, 250, 246, 255), outline=(160, 160, 155, 255), width=3)
    d.text((x + 16, y + 14), e, font=fe, fill=TINTA)
    d.text((x + 16, y + 80), "ENVÍO SIN COSTO", font=fm, fill=GRIS)
    d.rectangle([x + 16, y + 120, x + 264, y + 300], outline=(200, 200, 195, 255), width=2)
    d.line([(x + 30, y + 150), (x + 250, y + 270)], fill=ROSA, width=4)   # tachado: hay que rehacerla
im.save(OUT / "v2_formatos.png"); print("  ✓ v2_formatos.png")


# ── 4–7 · VIDEO · LANDING · PAUTA · PRESENTACIÓN (hojas rápidas: el sello manda) ──
def rapida(nombre, sello_txt, cab, lineas, tam=150):
    im = papel(); d = ImageDraw.Draw(im)
    im = sello(im, sello_txt, tam=tam); d = ImageDraw.Draw(im)
    cabecera(d, cab, 300)
    y = 380
    for l in lineas:
        d.text((90, y), l, font=fuente(MONO, 40), fill=TINTA); y += 64
    d.line([(90, y + 20), (1010, y + 20)], fill=ROSA, width=5)
    d.text((90, y + 40), "→ de nuevo", font=fuente(MANO, 64, {"wght": 600}), fill=ROSA)
    im.save(OUT / nombre); print(f"  ✓ {nombre}")


rapida("v2_video.png", "VIDEO", "REEL 9:16 · v08 · re-render", ["ESC.03  «ENVÍO GRATIS» → «SIN COSTO»", "SUBTÍTULOS  ×9", "RENDER  0/9"])
rapida("v2_landing.png", "LANDING", "copywriters.cl/primavera · v08", ["H1  ENVÍO SIN COSTO", "BOTÓN  «Compra hoy»", "DEPLOY  pendiente"])
rapida("v2_pauta.png", "PAUTA", "META + GOOGLE · v08", ["ANUNCIOS  27", "TITULARES  ×3 c/u", "PRESUPUESTO  igual"])
rapida("v2_presentacion.png", "PRESENTACIÓN", "PPT · cliente · v08", ["LÁMINAS  42", "MOCKUPS  ×9", "IMPRESA  ×2"], tam=112)

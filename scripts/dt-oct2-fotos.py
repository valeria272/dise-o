"""DT · octubre 2026, segunda tanda (las 6 que pasaron a OK PARA DISEÑO el 28-09): prepara las fotos.

Todo sale de material REAL del hotel (sesión HDT en alta) o del banco de la familia
aprobado el 25-09 (`out/hilton/dt/familia/entrega/`). Se recorta al formato y se deja
a la resolución del máster (2250 de ancho), así el render a --scale=2.0833 no estira.

    py scripts/dt-oct2-fotos.py
"""
import os
from PIL import Image

ALTA = "raw/hilton/dt/sesion-real/alta/"
BANCO = "out/hilton/dt/familia/entrega/"
OUT = "public/assets/hilton/dt/oct2/"
os.makedirs(OUT, exist_ok=True)

FEED = (2250, 2813)
STORY = (2250, 4000)


def recorta(src, dst, fmt, cx=0.5, cy=0.5, zoom=1.0):
    """Recorte al formato `fmt` centrado en (cx, cy) de la foto; `zoom` > 1 acerca."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    r = fmt[0] / fmt[1]
    cw, ch = (h * r, h) if w / h > r else (w, w / r)
    cw, ch = cw / zoom, ch / zoom
    x0 = min(max(0, cx * w - cw / 2), w - cw)
    y0 = min(max(0, cy * h - ch / 2), h - ch)
    im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize(fmt, Image.LANCZOS).save(OUT + dst, quality=92)
    print("ok", dst)


# ── STORIES 05-10 · feriado ──
recorta(ALTA + "HDT_65-hab.jpg", "er-hab-story.jpg", STORY, cx=0.215)          # copas + espumante junto a la cama
recorta(BANCO + "DT-familia-hab-2camas-story-2160x3840.jpg", "ft-hab-story.jpg", STORY)  # se corre hacia arriba en la pieza
recorta(ALTA + "HDT_43-frontis.jpg", "feriado-fondo-story.jpg", STORY, cx=0.5)  # la fachada con cielo
recorta(BANCO + "DT-familia-restaurante-post-2250x2813.jpg", "card-familia.jpg", (900, 900), cy=0.62)

# ── FEED 28-10 · Family Time ──
recorta(BANCO + "DT-familia-almohadas-post-2250x2813.jpg", "ft-feed.jpg", FEED)

# ── STORY 22-10 · Coworking (fotos de apoyo del lounge) ──
recorta(ALTA + "HDT_37.jpg", "cw-lounge.jpg", STORY, cx=0.55)
recorta(ALTA + "HDT_38.jpg", "cw-lounge-2.jpg", STORY, cx=0.35)

# ── FEED 21-10 · carrusel «5 cosas» ──
recorta(ALTA + "HDT_43-frontis.jpg", "c5-portada.jpg", FEED, cy=0.45)
recorta(BANCO + "DT-familia-checkin-post-1080x1350.jpg", "c5-hospitalidad.jpg", FEED)
recorta(ALTA + "HDT_66-hab.jpg", "c5-habitacion.jpg", FEED, cx=0.62)
recorta(ALTA + "HDT_36-lobby.jpg", "c5-espacios.jpg", FEED, cx=0.45)
recorta(ALTA + "HDT_67-hab-vista.jpg", "c5-ubicacion.jpg", FEED, cx=0.78)
recorta(ALTA + "HDT_82.jpg", "c5-gym.jpg", FEED, cx=0.5)
recorta(ALTA + "HDT_37.jpg", "c5-cierre.jpg", FEED, cx=0.5)

# La pareja brindando (Nano Banana Pro sobre HDT_65 real, variante C — `scripts/dt-oct2-pareja.py`)
recorta("raw/hilton/dt/oct2-pareja/nb-c.png", "card-pareja.jpg", (900, 900), cx=0.62, cy=0.42, zoom=1.9)

# ── RONDA 2 (Eli, 28-09): «utiliza imágenes nuevas, más bonitas, para que se vaya actualizando el feed» ──
# Todas de la sesión nueva «Hotel general sesión SEP 2026» (raw/hilton/sesion-sep2026/alta, a 3200 px).
SEP = "raw/hilton/sesion-sep2026/alta/sep_26-"
recorta(SEP + "246.jpg", "c5-portada.jpg", FEED, cy=0.56)          # A · el sillón del lounge, como la REF 2
recorta(BANCO + "DT-familia-vista-post-2250x2813.jpg", "c5-portada-b.jpg", FEED)  # B · la familia en el sofá
recorta(SEP + "515.jpg", "c5-habitacion.jpg", FEED, cx=0.42)
recorta(SEP + "237.jpg", "c5-espacios.jpg", FEED, cy=0.5)            # Winter Garden
recorta(SEP + "366.jpg", "c5-ubicacion.jpg", FEED, cy=0.45)           # la ciudad desde arriba
recorta(SEP + "250.jpg", "c5-cierre.jpg", FEED, cx=0.5)               # el lobby iluminado
# coworking: tres tomas nuevas del cowork del lobby
recorta(SEP + "270.jpg", "cw-1.jpg", STORY, cy=0.55)
recorta(SEP + "267.jpg", "cw-2.jpg", STORY, cx=0.36)
recorta(SEP + "264.jpg", "cw-3.jpg", STORY, cx=0.45)
recorta("raw/hilton/dt/familia/r3/final-checkin-h2a.png", "c5-hospitalidad.jpg", FEED)  # ronda 2: sin el niño fantasma (scripts/dt-oct2-hospitalidad*.py)
recorta(SEP + "250.jpg", "c5-cierre.jpg", FEED, cx=0.30)             # ronda 2: el lounge iluminado, otro ángulo que la portada

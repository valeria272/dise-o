#!/usr/bin/env python3
"""Titulares del reel vertical de SANTA GOTA, con las fuentes del Brand Soul.

El spot original es 1920x1080 y sus titulares van casi borde a borde, escalonados
en horizontal. En 9:16 el ancho util cae a 1080, asi que cada bloque se REAPILA
centrado: el mensaje no cambia, cambia el layout. Las fuentes son las medidas
contra el video (ver public/assets/fonts/santagota/LEEME.md).
"""
import os, sys, json
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUENTES = os.path.join(RAIZ, "public", "assets", "fonts", "santagota")
QM = os.path.join(FUENTES, "TheQueenMarker-Completa.ttf")
IMP = os.path.join(FUENTES, "Impact-Sistema.ttf")

BLANCO = (255, 255, 255)
LIMA = (195, 214, 0)          # #C3D600 — el lima Santa Gota del brand kit

def linea(texto, fuente, px, color, tracking=0):
    """Escribe una linea y la recorta a su tinta. Devuelve RGBA."""
    f = ImageFont.truetype(fuente, px)
    anchos = [f.getlength(c) for c in texto]
    w = int(sum(anchos) + tracking * max(0, len(texto) - 1)) + px
    im = Image.new("RGBA", (w, int(px * 2.4)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = px * 0.5
    for c, a in zip(texto, anchos):
        d.text((x, px * 0.55), c, font=f, fill=color + (255,))
        x += a + tracking
    return im.crop(im.getbbox())

def a_ancho(im, objetivo):
    """Escala por ancho conservando proporcion."""
    if im.width == objetivo:
        return im
    h = max(1, round(im.height * objetivo / im.width))
    return im.resize((objetivo, h), Image.LANCZOS)

# Cada bloque: lista de (texto, fuente, color, ancho_objetivo_px, dx)
# dx = corrimiento horizontal en px para conservar el escalonado del original,
# que es un gesto de la pieza y no un accidente.
BLOQUES = {
    "una_sola_gota": [("UNA SOLA GOTA", QM, BLANCO, 900, 0)],
    "lo_cambia_todo": [
        ("LO CAMBIA", IMP, BLANCO, 620, -40),
        ("TODO",      QM,  LIMA,   540,  60),
    ],
    "revolucion": [
        ("SOMOS",               IMP, BLANCO, 330, -250),
        ("LA REVOLUCIÓN",       QM,  LIMA,   980,    0),
        ("DEL ACEITE DE OLIVA", IMP, BLANCO, 860,   50),
    ],
    "cta": [
        ("CÓMPRALO",      IMP, BLANCO, 560, 0),
        ("EN TODO CHILE", IMP, BLANCO, 820, 0),
    ],
}

def construir(destino):
    os.makedirs(destino, exist_ok=True)
    meta = {}
    for nombre, lineas in BLOQUES.items():
        piezas = []
        for texto, fuente, color, ancho, dx in lineas:
            im = a_ancho(linea(texto, fuente, 260, color), ancho)
            piezas.append((im, dx))
        sep = 18
        W = max(p.width + abs(dx) * 2 for p, dx in piezas)
        H = sum(p.height for p, _ in piezas) + sep * (len(piezas) - 1)
        lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        y = 0
        for p, dx in piezas:
            lienzo.paste(p, ((W - p.width) // 2 + dx, y), p)
            y += p.height + sep
        lienzo = lienzo.crop(lienzo.getbbox())
        ruta = os.path.join(destino, nombre + ".png")
        lienzo.save(ruta)
        meta[nombre] = [lienzo.width, lienzo.height]
        print(f"  {nombre:16s} {lienzo.width:4d}x{lienzo.height:4d}  ({len(lineas)} linea/s)")
    json.dump(meta, open(os.path.join(destino, "meta.json"), "w"), indent=1)
    return meta

if __name__ == "__main__":
    destino = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "out", "santagota", "reel", "titulares")
    construir(destino)

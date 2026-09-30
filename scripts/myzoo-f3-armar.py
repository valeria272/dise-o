#!/usr/bin/env python3
"""MyZoo · Paid Fase 3 «Convive» (octubre 2026) — arma los estáticos del brief.

Brief: «MyZoo | Brief Diseño Fase 3.xlsx» (15fHOTTtr2L18vcKCn88aTr5MljQ9rXUX), de
Sebastián Córdova. Los TEXTOS van literales del brief (columna TEXTO SOBRE LA IMAGEN).

GRAMÁTICA — la del paid de la Fase 2, medida sobre las piezas publicadas
(`clients/myzoo/APRENDIZAJES.md` E-06, `DRIVE-AGENCIA.md` §4), que Paulina pidió
seguir el 30-09 «variando para que no se vea exactamente igual»:
  · 1080 × 1080 (brief). Se compone a 2160 y se baja a 1080.
  · Titular Neutraface Text mayúsculas blanco, centrado, dos pesos (Book + Bold).
    Book sólo si el texto NO tiene «í»: el archivo rompe esa letra (R-15).
  · Pincelada coral #FF6969 irregular con la bajada en Roboto, blanca.
  · Logo grande ABAJO A LA IZQUIERDA (~25 % del ancho), como en F2 — no el de 145 px
    arriba del orgánico.
  · Escena IA (Seedream 5 Pro): casa cálida de atardecer, perro/gato protagonista,
    casi sin personas.
  · Producto = packshot REAL de Paulina, con la luz integrada por código (tinte cálido,
    sombra de contacto y sombra proyectada). La etiqueta no se toca.
  · Sin punto final (R-18).

Uso:  python scripts/myzoo-f3-armar.py [p01 p07 …]   → out/myzoo/paid-fase3/
"""
import os
import sys as _s
try:
    _s.stdout.reconfigure(encoding="utf-8", errors="replace")  # consola cp1252 de Windows
except Exception:
    pass
import random
import sys

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEU = os.path.join(RAIZ, "public/assets/fonts/myzoo/NeutrafaceText-")
ROB = os.path.join(RAIZ, "public/assets/fonts/roboto/Roboto-")
ESC = os.path.join(RAIZ, "raw/myzoo/fase3/escenas/")
PROD = os.path.join(RAIZ, "public/assets/myzoo/producto/")
LOGO = os.path.join(RAIZ, "public/assets/myzoo/marca/logo.png")
OUT = os.path.join(RAIZ, "out/myzoo/paid-fase3")

CORAL = (255, 105, 105)
BLANCO = (255, 255, 255)
TINTA = (17, 17, 17)
K = 2  # se compone al doble y se baja al final


def neu(peso, px, texto=""):
    if peso == "Book" and "í" in texto.lower():
        peso = "Bold"  # R-15: Book deja un hueco tras la «í»
    return ImageFont.truetype(NEU + peso + ".otf", px * K)


def rob(peso, px):
    return ImageFont.truetype(ROB + peso + ".ttf", px * K)


def escena(nombre, lado):
    im = Image.open(ESC + nombre).convert("RGB")
    w, h = im.size
    s = max(lado[0] / w, lado[1] / h)
    im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    x, y = (im.width - lado[0]) // 2, (im.height - lado[1]) // 2
    return im.crop((x, y, x + lado[0], y + lado[1]))


def velo(lienzo, arriba=0.42, fuerza=150):
    """Oscurece la franja superior para que el titular blanco se lea (sin tocar el centro)."""
    w, h = lienzo.size
    g = np.zeros((h, 1), np.float32)
    corte = int(h * arriba)
    g[:corte, 0] = np.linspace(1, 0, corte) ** 1.4
    a = Image.fromarray((g * fuerza).astype("uint8")).resize((w, h))
    negro = Image.new("RGB", (w, h), (20, 12, 6))
    return Image.composite(negro, lienzo, a)


def velo_abajo(lienzo, desde=0.78, fuerza=120):
    w, h = lienzo.size
    g = np.zeros((h, 1), np.float32)
    ini = int(h * desde)
    g[ini:, 0] = np.linspace(0, 1, h - ini) ** 1.6
    a = Image.fromarray((g * fuerza).astype("uint8")).resize((w, h))
    return Image.composite(Image.new("RGB", (w, h), (20, 12, 6)), lienzo, a)


def centrado(d, cx, y, texto, fuente, color=BLANCO, sombra=True):
    bb = d.textbbox((0, 0), texto, font=fuente)
    x = cx - (bb[2] - bb[0]) / 2 - bb[0]
    if sombra:
        d.text((x, y + 3 * K), texto, font=fuente, fill=(0, 0, 0, 70))
    d.text((x, y), texto, font=fuente, fill=color)
    return bb[3] - bb[1]


def pincelada(w, h, semilla=3):
    """Pincelada coral de borde irregular, como la banda de la F2."""
    rnd = random.Random(semilla)
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    pts_arriba, pts_abajo = [], []
    paso = 6 * K
    for x in range(0, w + paso, paso):
        pts_arriba.append((x, h * 0.10 + rnd.uniform(-1, 1) * h * 0.07))
        pts_abajo.append((x, h * 0.90 + rnd.uniform(-1, 1) * h * 0.07))
    d.polygon(pts_arriba + pts_abajo[::-1], fill=255)
    # extremos deshilachados
    for lado in (0, 1):
        for _ in range(28):
            yy = rnd.uniform(0.15, 0.85) * h
            largo = rnd.uniform(0.01, 0.05) * w
            x0 = 0 if lado == 0 else w - largo
            d.rectangle((x0, yy, x0 + largo, yy + rnd.uniform(1, 4) * K), fill=0)
    m = m.filter(ImageFilter.GaussianBlur(0.8 * K))
    capa = Image.new("RGBA", (w, h), CORAL + (0,))
    capa.putalpha(m)
    return capa


def banda(lienzo, cx, y, lineas, fuente, pad_x=34, pad_y=16, semilla=3):
    d = ImageDraw.Draw(lienzo)
    anchos = [d.textbbox((0, 0), t, font=fuente) for t in lineas]
    lh = max(b[3] - b[1] for b in anchos)
    inter = int(lh * 0.35)
    w = max(b[2] - b[0] for b in anchos) + 2 * pad_x * K
    h = lh * len(lineas) + inter * (len(lineas) - 1) + 2 * pad_y * K
    p = pincelada(w, h, semilla)
    lienzo.paste(p, (int(cx - w / 2), int(y)), p)
    yy = y + pad_y * K
    for t in lineas:
        centrado(d, cx, yy - d.textbbox((0, 0), t, font=fuente)[1], t, fuente, sombra=False)
        yy += lh + inter
    return h


def logo(lienzo, x, y, ancho):
    lg = Image.open(LOGO).convert("RGBA")
    lg = lg.resize((ancho, round(lg.height * ancho / lg.width)), Image.LANCZOS)
    lienzo.paste(lg, (x, y), lg)


def producto(lienzo, archivo, cx, base_y, alto, tinte=(255, 214, 170), fuerza=0.30, luz_desde="izq"):
    """Monta el packshot real apoyado en base_y con la luz de la escena.

    Tinte cálido por multiplicación suave + sombra de contacto + sombra proyectada al
    lado contrario de la luz. La etiqueta sólo recibe el tinte global: no se retoca.
    """
    p = Image.open(PROD + archivo).convert("RGBA")
    p = p.resize((round(p.width * alto / p.height), alto), Image.LANCZOS)
    rgb, a = p.convert("RGB"), p.getchannel("A")
    calido = ImageChops.multiply(rgb, Image.new("RGB", rgb.size, tinte))
    rgb = Image.blend(rgb, calido, fuerza)
    # lado en sombra: un degradé suave hacia el lado contrario a la luz
    g = np.linspace(0, 1, rgb.width) if luz_desde == "izq" else np.linspace(1, 0, rgb.width)
    osc = Image.fromarray((np.tile(g ** 2, (rgb.height, 1)) * 60).astype("uint8"))
    rgb = Image.composite(Image.new("RGB", rgb.size, (40, 25, 15)), rgb, osc)
    p = rgb.convert("RGBA"); p.putalpha(a)
    x, y = int(cx - p.width / 2), int(base_y - p.height)
    # sombra proyectada (larga, hacia el lado opuesto a la luz) y de contacto
    som = Image.new("L", lienzo.size, 0)
    ds = ImageDraw.Draw(som)
    dx = 1 if luz_desde == "izq" else -1
    ds.polygon([(x + p.width * 0.1, base_y), (x + p.width * 0.9, base_y),
                (x + p.width * 0.9 + dx * p.width * 0.55, base_y - p.height * 0.10),
                (x + p.width * 0.1 + dx * p.width * 0.55, base_y - p.height * 0.10)], fill=110)
    som = som.filter(ImageFilter.GaussianBlur(p.width * 0.06))
    ds = ImageDraw.Draw(som)
    contacto = Image.new("L", lienzo.size, 0)
    ImageDraw.Draw(contacto).ellipse((x + p.width * 0.04, base_y - p.width * 0.035,
                                      x + p.width * 0.96, base_y + p.width * 0.035), fill=190)
    contacto = contacto.filter(ImageFilter.GaussianBlur(p.width * 0.025))
    som = ImageChops.lighter(som, contacto)
    lienzo.paste(Image.new("RGB", lienzo.size, (25, 14, 6)), (0, 0), som)
    lienzo.paste(p, (x, y), p)
    return x, y, p.width, p.height


def pildora(lienzo, cx, cy, texto, fuente, fondo=CORAL, color=BLANCO, pad_x=26, pad_y=12):
    d = ImageDraw.Draw(lienzo)
    bb = d.textbbox((0, 0), texto, font=fuente)
    w, h = bb[2] - bb[0] + 2 * pad_x * K, bb[3] - bb[1] + 2 * pad_y * K
    x0, y0 = cx - w / 2, cy - h / 2
    d.rounded_rectangle((x0, y0, x0 + w, y0 + h), radius=h / 2, fill=fondo)
    d.text((x0 + pad_x * K - bb[0], y0 + pad_y * K - bb[1]), texto, font=fuente, fill=color)
    return w, h


def guardar(lienzo, nombre, lado):
    os.makedirs(OUT, exist_ok=True)
    fin = lienzo.convert("RGB").resize(lado, Image.LANCZOS)
    ruta = os.path.join(OUT, nombre)
    fin.save(ruta, quality=95)
    print("→", ruta, fin.size)


# ───────────────────────────── piezas ─────────────────────────────

def p01():
    """[VENTAS WEB] Estático «¿Cuál es para tu mascota?» — el precio manda."""
    L = (1080 * K, 1080 * K)
    c = velo(escena("p01_a.png", L), 0.45, 170)
    c = velo_abajo(c, 0.80, 110)
    d = ImageDraw.Draw(c)
    cx = L[0] // 2
    # TÍTULO: Pet Wipes desde $2.990 — el precio es lo más grande
    y = 58 * K
    y += centrado(d, cx, y, "PET WIPES DESDE", neu("Book", 58)) + 18 * K
    centrado(d, cx, y, "$2.990", neu("Bold", 170))
    y += 150 * K + 22 * K
    # BAJADA en la pincelada
    banda(c, cx, y, ["110 UNIDADES A $9.990", "USO FRECUENTE O PIEL SENSIBLE"], rob("Medium", 30), semilla=7)
    # los 3 envases sobre la mesa, cada uno con su precio al lado
    base = 792 * K
    envases = [("MyZoo_wipes_azul_15u.png", 560, 235, "$2.990"),
               ("MyZoo_wipes_azul_110u.png", 745, 300, "$9.990"),
               ("MyZoo_wipes_rosa_110u.png", 930, 300, "$9.990")]
    for arch, x, alto, precio in envases:
        _, _, w, _ = producto(c, arch, x * K, base, alto * K)
        pildora(c, x * K, base + 40 * K, precio, neu("Bold", 34))
    # APOYO + logo abajo a la izquierda
    pildora(c, 745 * K, 1010 * K, "Compra online en myzoo.cl", rob("Medium", 26), fondo=BLANCO, color=TINTA)
    logo(c, 44 * K, 830 * K, 250 * K)
    guardar(c, "MYZOO_P01_Feed_1080x1080.png", (1080, 1080))


def p07():
    """[PERFIL IG] Estático tip piel sensible — la pregunta es la protagonista."""
    L = (1080 * K, 1080 * K)
    c = velo(escena("p07_a.png", L), 0.50, 175)
    c = velo_abajo(c, 0.78, 120)
    d = ImageDraw.Draw(c)
    cx = L[0] // 2
    y = 62 * K
    y += centrado(d, cx, y, "¿CÓMO LIMPIAR A UNA MASCOTA", neu("Book", 56)) + 22 * K
    y += centrado(d, cx, y, "CON PIEL SENSIBLE?", neu("Bold", 92)) + 34 * K
    banda(c, cx, y, ["TE LO CONTAMOS EN NUESTRO PERFIL"], rob("Medium", 30), semilla=11)
    pildora(c, 745 * K, 1010 * K, "Tips de higiene y cuidado · MyZoo", rob("Medium", 26), fondo=BLANCO, color=TINTA)
    logo(c, 44 * K, 830 * K, 250 * K)
    guardar(c, "MYZOO_P07_Feed_1080x1080.png", (1080, 1080))


PIEZAS = {"p01": p01, "p07": p07}

if __name__ == "__main__":
    for n in (sys.argv[1:] or PIEZAS):
        PIEZAS[n]()

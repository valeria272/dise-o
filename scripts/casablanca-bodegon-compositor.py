"""Casablanca C1 — arma el bodegón cenital de tablas con las fotos REALES.

En vez de que la IA invente madera, recorta tablas de la foto oficial de cada
producto (pisoscasablanca.cl) y las dispone sobre hormigón greige cálido, en el
lenguaje de agosto: tablas largas entrando desde los bordes en ángulos
irregulares, canto visible, sombras suaves y un claro central para el texto.

La disposición es FIJA: las 4 tarjetas comparten composición exacta y solo cambia
la madera, que es la regla nº1 del brief.

Salida: public/assets/casablanca/bodegon_<producto>.jpg (2048x2048)
"""
import math
import pathlib
import random

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


RAIZ = pathlib.Path(str(_RAIZ))
FUENTE = RAIZ / "raw/casablanca/productos"
DEST = RAIZ / "public/assets/casablanca"

S = 2048  # lienzo cuadrado
GREIGE = (188, 180, 166)

PRODUCTOS = {
    "natural_uv_grande": "roble-natural-143x190x1900.jpg",
    "natural_uv_chico": "roble-natural-uv-formato-chico.jpg",
    "aserrado": "roble-aserrado.jpg",
    "cumaru": "cumaru.jpg",
}

# (cx, cy, ángulo°, largo, ancho, recorte_y) — posiciones fijas para las 4.
# Tres racimos con dos huecos deliberados (derecha-medio y abajo-centro) para
# que no se lea como un anillo.
TABLAS = [
    # racimo superior izquierdo → superior
    (300, 150, -38, 1150, 250, 0.05),
    (610, 60, -14, 1000, 225, 0.30),
    (980, 95, 6, 1080, 240, 0.55),
    (1330, 175, 22, 980, 215, 0.15),
    (1660, 330, 44, 1050, 245, 0.70),
    # racimo derecho alto
    (1900, 640, 74, 900, 220, 0.40),
    (1960, 980, 92, 980, 235, 0.10),
    # racimo inferior derecho
    (1720, 1640, 133, 1020, 240, 0.62),
    (1430, 1880, 158, 950, 220, 0.22),
    # racimo inferior izquierdo
    (620, 1950, 192, 1080, 245, 0.48),
    (270, 1720, 216, 980, 230, 0.08),
    # lateral izquierdo
    (110, 1260, 262, 900, 215, 0.66),
    (170, 830, 292, 950, 225, 0.35),
]


def textura(path, frac_y, largo, ancho):
    """Recorta una franja horizontal de la foto del producto y la escala."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    alto_crop = max(40, int(h * 0.22))
    y0 = int((h - alto_crop) * frac_y)
    tira = im.crop((0, y0, w, y0 + alto_crop))
    return tira.resize((largo, ancho), Image.LANCZOS)


def tabla(path, largo, ancho, frac_y, luz=1.0):
    """Devuelve una tabla RGBA con canto y bisel, lista para rotar.

    `luz` simula la caída de la luz cálida que entra por arriba-derecha: las
    tablas de esa zona van más claras y las del extremo opuesto más apagadas.
    """
    canto = max(10, ancho // 16)
    cap = Image.new("RGBA", (largo, ancho + canto), (0, 0, 0, 0))

    cara = textura(path, frac_y, largo, ancho)
    cara = ImageEnhance.Brightness(cara).enhance(luz)
    cap.paste(cara, (0, 0))

    # canto aserrado: la misma madera, apenas más clara
    borde = cara.crop((0, ancho - canto, largo, ancho)).point(
        lambda v: min(255, int(v * 1.10 + 8))
    )
    cap.paste(borde, (0, ancho))

    d = ImageDraw.Draw(cap)
    d.line([(0, 0), (largo, 0)], fill=(255, 250, 242, 55), width=3)          # brillo arriba
    d.line([(0, ancho - 1), (largo, ancho - 1)], fill=(60, 45, 32, 90), width=2)  # quiebre
    d.line([(0, ancho + canto - 1), (largo, ancho + canto - 1)],
           fill=(70, 55, 40, 105), width=3)                                   # base del canto
    return cap


def fondo():
    """Hormigón greige cálido con grano suave y viñeta."""
    base = Image.new("RGB", (S, S), GREIGE)
    px = base.load()
    rnd = random.Random(7)
    for y in range(0, S, 2):
        for x in range(0, S, 2):
            n = rnd.randint(-7, 7)
            r, g, b = px[x, y]
            v = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)))
            px[x, y] = v
            if x + 1 < S:
                px[x + 1, y] = v
            if y + 1 < S:
                px[x, y + 1] = v
                if x + 1 < S:
                    px[x + 1, y + 1] = v
    base = base.filter(ImageFilter.GaussianBlur(1.2))

    # luz cálida desde arriba-derecha + viñeta
    luz = Image.new("L", (S, S), 0)
    dl = ImageDraw.Draw(luz)
    dl.ellipse([-int(S * 0.25), -int(S * 0.45), int(S * 1.35), int(S * 1.05)], fill=64)
    luz = luz.filter(ImageFilter.GaussianBlur(S // 7))
    base = Image.composite(Image.new("RGB", (S, S), (222, 215, 201)), base, luz)

    vin = Image.new("L", (S, S), 0)
    dv = ImageDraw.Draw(vin)
    dv.ellipse([int(S * 0.06), int(S * 0.06), int(S * 0.94), int(S * 0.94)], fill=255)
    vin = vin.filter(ImageFilter.GaussianBlur(S // 9))
    base = Image.composite(base, Image.new("RGB", (S, S), (168, 160, 148)), vin)
    return base


def construye(nombre, archivo):
    path = FUENTE / archivo
    lienzo = fondo()
    sombras = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    piezas = []

    for cx, cy, ang, largo, ancho, fy in TABLAS:
        # luz cálida entrando por arriba-derecha
        luz = 1.06 - 0.16 * ((cy / S) * 0.65 + (1 - cx / S) * 0.35)
        cap = tabla(path, largo, ancho, fy, luz).rotate(
            ang, expand=True, resample=Image.BICUBIC
        )
        x, y = cx - cap.width // 2, cy - cap.height // 2
        piezas.append((cap, x, y))

        sil = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        sil.paste(Image.new("RGBA", cap.size, (58, 44, 30, 104)), (x - 20, y + 32), cap)
        sombras = Image.alpha_composite(sombras, sil)

    sombras = sombras.filter(ImageFilter.GaussianBlur(30))
    lienzo = Image.alpha_composite(lienzo.convert("RGBA"), sombras)
    for cap, x, y in piezas:
        lienzo.alpha_composite(cap, (x, y))

    out = DEST / f"bodegon_{nombre}.jpg"
    lienzo.convert("RGB").save(out, quality=93)
    print(f"  {out.name}  ({out.stat().st_size // 1024} KB)")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for nombre, archivo in PRODUCTOS.items():
        construye(nombre, archivo)
    print("\nListo. Misma composición en las 4, solo cambia la madera.")


if __name__ == "__main__":
    main()

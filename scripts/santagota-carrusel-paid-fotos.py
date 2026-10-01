#!/usr/bin/env python3
"""
SANTA GOTA · carrusel de pauta «Elige tu pecado» — prepara las fotos de las 5 láminas (01-10-2026).

Material: jornada audiovisual del 10-09 (Drive 1F7cx_nO4HygXW9qwH_-RV_p3q8qenHVN), originales en
raw/santa-gota/jornada-10-09/. Producto: packshot oficial del e-commerce (la IA no toca producto).

Cada lámina: recorte 4:5 → 2160×2700 (2× de 1080×1350) + color subido para calzar con el feed publicado
(la jornada es luz natural sobre rosado; el carrusel del 24-09 la sube a rojo-rosado saturado).
Lámina 5: la banqueta vacía (DSC08030) recortada SIN el parquet (madera = código prohibido) y el Pack
Completo oficial apoyado en el asiento, con sombra de contacto.

Salida: public/assets/santagota/paid-carrusel/{01..05}.jpg
"""
import os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageChops

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = os.path.join(RAIZ, "raw/santa-gota/jornada-10-09")
SAL = os.path.join(RAIZ, "public/assets/santagota/paid-carrusel")
os.makedirs(SAL, exist_ok=True)
W, H = 2160, 2700

# (archivo, centro x relativo, y0 relativo del recorte, ancho relativo del recorte)
LAMINAS = {
    "01": ("DSC00267.JPG", 0.43, 0.04, 0.84),  # portada: la lata al oído
    "02": ("DSC00058.JPG", 0.50, 0.03, 1.00),  # cocinar: 750 al hombro
    "03": ("DSC08076.JPG", 0.50, 0.02, 1.00),  # aderezar: el 500 a la boca
    "04": ("DSC00105.JPG", 0.50, 0.12, 1.00),  # relleno: las latas en la cabeza
}


def color(im: Image.Image) -> Image.Image:
    """Sube color y contraste como el feed; el rosado polvoso pasa a rosado-rojo."""
    im = ImageEnhance.Color(im).enhance(1.32)
    im = ImageEnhance.Contrast(im).enhance(1.10)
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * 1.04)))
    b = b.point(lambda v: int(v * 0.95))
    return Image.merge("RGB", (r, g, b))


def recorte(im, cx, y0, ancho):
    w = int(im.width * ancho)
    h = int(w * 5 / 4)
    x = int(im.width * cx - w / 2)
    x = max(0, min(im.width - w, x))
    y = max(0, min(im.height - h, int(im.height * y0)))
    return im.crop((x, y, x + w, y + h)).resize((W, H), Image.LANCZOS)


for n, (f, cx, y0, a) in LAMINAS.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(J, f))).convert("RGB")
    color(recorte(im, cx, y0, a)).save(os.path.join(SAL, f"{n}.jpg"), quality=92)
    print(n, f)

# ── Lámina 5: MILAGRO — los cuatro productos del Pack Completo LEVITAN contra la pared del set ──
# 01-10: la versión con el pack apoyado en la banqueta «se ve feo» (Valeria): un packshot de estudio pegado,
# chico y sin peso. La levitación es un truco publicitario a la vista (calza con «milagro») y no finge un apoyo.
# Fondo: la pared rosada REAL de DSC08030, sin banqueta ni parquet. Producto: los 4 packshots oficiales sueltos.
im = ImageOps.exif_transpose(Image.open(os.path.join(J, "DSC08030.JPG"))).convert("RGB")  # 3376×6000
# sólo pared: bajo el borde del fondo (y ≈ 1025) y sobre la lata que quedó en la banqueta (tapa en y ≈ 2765)
cw = 1290
x0, y0 = 1690 - cw // 2, 1130
base = im.crop((x0, y0, x0 + cw, y0 + int(cw * 5 / 4))).resize((W, H), Image.LANCZOS)
# más expuesta que las otras: la pared se lleva, canal por canal, al rosado-rojo de las láminas 1–4
pared = [sum(c) / len(c) for c in zip(*base.crop((900, 1900, 1300, 2300)).getdata())]
mult = [t / m for t, m in zip((178, 86, 92), pared)]
base = Image.merge("RGB", [c.point(lambda v, f=f: min(255, int(v * f))) for c, f in zip(base.split(), mult)])
base = ImageEnhance.Contrast(base).enhance(1.06)

P = os.path.join(RAIZ, "public/assets/santagota/producto")
# (archivo, centro x, base y, alto, giro°) — de atrás hacia adelante: latas detrás, squeeze delante.
# Altos en proporción real: 750 > 500 > latas.
GRUPO = [
    ("lata-cocinar-frente.png", 470, 1600, 660, -14),
    ("lata-aderezar-frente.png", 1700, 1560, 660, 15),
    ("squeeze-750-frente.png", 900, 1640, 1100, -6),
    ("squeeze-500-frente.png", 1300, 1600, 970, 7),
]


def integra(prod: Image.Image) -> Image.Image:
    """Penumbra hacia la base + rebote rosado de la pared en el canto (sobre la silueta, no el área)."""
    a = prod.split()[3]
    rgb = prod.convert("RGB")
    # penumbra: la base un 14 % más oscura, protegiendo las luces de la etiqueta
    grad = Image.linear_gradient("L").resize(prod.size)  # 0 arriba → 255 abajo
    lum = rgb.convert("L")
    m = ImageChops.multiply(grad.point(lambda v: int(v * 0.55)), lum.point(lambda v: 255 - int(v * 0.6)))
    rgb = Image.composite(ImageEnhance.Brightness(rgb).enhance(0.72), rgb, m)
    # canto: anillo de la silueta binaria, teñido con el rosado de la pared
    sil = a.point(lambda v: 255 if v > 128 else 0)
    anillo = ImageChops.subtract(sil, sil.filter(ImageFilter.MinFilter(15))).filter(ImageFilter.GaussianBlur(3))
    rosa = Image.new("RGB", prod.size, (255, 150, 160))
    rgb = Image.composite(ImageChops.screen(rgb, rosa), rgb, anillo.point(lambda v: int(v * 0.45)))
    out = rgb.filter(ImageFilter.GaussianBlur(0.7))  # la foto es más blanda que el packshot de estudio
    out.putalpha(a)
    return out


capas = []
for f, cx, by, h, rot in GRUPO:
    pr = Image.open(os.path.join(P, f)).convert("RGBA")
    pr = pr.crop(pr.getbbox())
    pr = pr.resize((int(pr.width * h / pr.height), h), Image.LANCZOS)
    pr = integra(pr).rotate(rot, resample=Image.BICUBIC, expand=True)
    capas.append((pr, int(cx - pr.width / 2), int(by - pr.height)))

# sombras proyectadas en la pared: el objeto flota a ~30 cm, la sombra cae abajo-derecha y difusa
sombra = Image.new("L", base.size, 0)
for pr, x, y in capas:
    sombra.paste(pr.split()[3], (x + 60, y + 95), pr.split()[3])
sombra = sombra.filter(ImageFilter.GaussianBlur(38)).point(lambda v: int(v * 0.42))
base = Image.composite(Image.new("RGB", base.size, (92, 26, 36)), base, sombra)
for pr, x, y in capas:
    base.paste(pr, (x, y), pr)

# grano parejo sobre todo, para que producto y pared compartan textura
ruido = Image.effect_noise(base.size, 7).convert("RGB")
base = Image.blend(base, ImageChops.add(base, ruido, 1, -128), 0.5)
base.save(os.path.join(SAL, "05.jpg"), quality=92)
print("05 levitación", [(x, y, pr.size) for pr, x, y in capas])

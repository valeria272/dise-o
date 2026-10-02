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

# ── Lámina 5: el Pack Completo en el «altar» ──
im = ImageOps.exif_transpose(Image.open(os.path.join(J, "DSC08030.JPG"))).convert("RGB")  # 3376×6000
# La lata que quedó sobre la banqueta asoma entre los productos del pack: se tapa con la pared real de la
# izquierda, a la misma altura (la pared es pareja; el degradé vertical se conserva al copiar fila por fila).
LATA = (1480, 2700, 1700, 3245)
parche = im.crop((LATA[0] - 300, LATA[1], LATA[2] - 300, LATA[3]))
im.paste(parche, LATA[:2])
# asiento medido: x 1150–2025, borde superior y ≈ 3250; el parquet empieza en y ≈ 4400
cw = 1800
ch = int(cw * 5 / 4)
x0, y0 = 1588 - cw // 2, 4250 - ch
base = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.LANCZOS)
# Esta toma está más expuesta: el realce general la manda a salmón. Se lleva la pared, canal por canal,
# al rosado-rojo medido en las láminas 1–4 (≈ 175, 85, 90).
pared = [sum(c) / len(c) for c in zip(*base.crop((200, 300, 700, 900)).getdata())]
mult = [t / m for t, m in zip((175, 85, 90), pared)]
base = Image.merge("RGB", [ch_.point(lambda v, f=f: min(255, int(v * f))) for ch_, f in zip(base.split(), mult)])
base = ImageEnhance.Contrast(base).enhance(1.08)
k = W / cw
asiento_x0, asiento_x1, asiento_y = (1150 - x0) * k, (2025 - x0) * k, (3262 - y0) * k

pack = Image.open(os.path.join(RAIZ, "public/assets/santagota/producto/pack-completo.png")).convert("RGBA")
bb = pack.getbbox()
pack = pack.crop(bb)
pw = int((asiento_x1 - asiento_x0) * 1.02)
ph = int(pack.height * pw / pack.width)
pack = pack.resize((pw, ph), Image.LANCZOS)
px = int((asiento_x0 + asiento_x1) / 2 - pw / 2)
py = int(asiento_y - ph + 6)

# sombra de contacto: la silueta aplastada y difusa sobre el asiento
sombra = Image.new("L", base.size, 0)
sil = pack.split()[3].resize((pw, max(1, int(ph * 0.06))))
sombra.paste(sil, (px, int(asiento_y - ph * 0.03)))
sombra = sombra.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.55))
oscuro = Image.new("RGB", base.size, (40, 12, 14))
base = Image.composite(oscuro, base, sombra)
# luz ambiente del set sobre el producto: un velo rosado muy leve en el lado de sombra
velo = Image.new("RGBA", pack.size, (235, 120, 125, 0))
grad = Image.linear_gradient("L").rotate(90).resize(pack.size).point(lambda v: int(v * 0.10))
velo.putalpha(ImageChops.multiply(grad, pack.split()[3]))
pack = Image.alpha_composite(pack, velo)
base.paste(pack, (px, py), pack)
base.save(os.path.join(SAL, "05.jpg"), quality=92)
print("05 DSC08030 + pack-completo", (px, py, pw, ph))

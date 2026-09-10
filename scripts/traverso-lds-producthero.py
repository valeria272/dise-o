#!/usr/bin/env python3
"""k08 · PRODUCT HERO — los tres packshots REALES (escalados 4x) sobre el set del
corredor, con reflejo en el piso húmedo y su foco. Cero IA sobre el producto."""
import os, numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(RAIZ, "public", "assets", "traverso", "lds")
set_ = Image.open(os.path.join(A, "sets", "corredor.png")).convert("RGBA")
W, H = set_.size

def recorta(nombre):
    im = Image.open(os.path.join(A, "packshots", nombre)).convert("RGB")
    a = np.asarray(im).astype(int)
    # fondo blanco → alfa (suave)
    dist = 255 - a.min(axis=2)
    alpha = np.clip((dist - 8) * 6, 0, 255).astype(np.uint8)
    # borde: erosionar 1 px y suavizar para que no quede el halo blanco del recorte
    al = Image.fromarray(alpha).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    rgba = np.dstack([np.asarray(im), np.asarray(al)])
    out = Image.fromarray(rgba, "RGBA")
    bbox = out.split()[3].point(lambda v: 255 if v > 40 else 0).getbbox()
    return out.crop(bbox)

# Originales de r.bolder.run/4093/original/ (1920 / 1500 / 1000 px), recortados sin la banda azul.
packs = [recorta(n) for n in ("aji-crema-350g-hi.png", "mostaza-350g-hi.png", "ketchup-350g-hi.png")]
alto = int(H * 0.30)                       # tamaño real, proporcionado al set
piso = int(H * 0.735)                      # línea de apoyo (donde pisan en el master)
centros = [0.27, 0.50, 0.73]
lienzo = set_.copy()
# luz cálida sobre el plástico: leve tinte tungsteno + contraste
for p, cx in zip(packs, centros):
    h = alto; w = int(p.width * h / p.height)
    p = p.resize((w, h), Image.LANCZOS)
    p = ImageEnhance.Contrast(p).enhance(1.08)
    # luz del set: foco cálido arriba, penumbra abajo (la botella vive en la misma luz que el piso)
    a3 = np.asarray(p).astype(float)
    g = np.linspace(1.10, 0.62, h)[:, None, None]
    calido = np.array([1.04, 0.97, 0.88])[None, None, :]
    rgb = np.clip(a3[:, :, :3] * g * calido, 0, 255)
    p = Image.fromarray(np.dstack([rgb, a3[:, :, 3]]).astype(np.uint8), "RGBA")
    p = p.filter(ImageFilter.GaussianBlur(0.4))   # apenas más blanda que el fondo nítido de los focos
    x = int(W * cx - w / 2); y = piso - h
    # sombra de contacto
    sombra = Image.new("RGBA", (w + 80, 60), (0, 0, 0, 0))
    from PIL import ImageDraw
    ImageDraw.Draw(sombra).ellipse([10, 10, w + 70, 50], fill=(0, 0, 0, 170))
    sombra = sombra.filter(ImageFilter.GaussianBlur(14))
    lienzo.alpha_composite(sombra, (x - 40, piso - 30))
    # reflejo en el piso húmedo
    ref = ImageOps.flip(p)
    grad = Image.linear_gradient("L").resize((w, h)).point(lambda v: int(max(0, 120 - v * 0.9)))
    ref.putalpha(Image.eval(ref.split()[3], lambda v: v) )
    ra = Image.fromarray((np.asarray(ref.split()[3]).astype(int) * np.asarray(grad).astype(int) // 255).astype(np.uint8))
    ref.putalpha(ra); ref = ref.filter(ImageFilter.GaussianBlur(2))
    lienzo.alpha_composite(ref, (x, piso + 2))
    lienzo.alpha_composite(p, (x, y))
os.makedirs(os.path.join(A, "keyframes"), exist_ok=True)
out = os.path.join(A, "keyframes", "k08.png"); lienzo.convert("RGB").save(out); print("✓", out, lienzo.size)

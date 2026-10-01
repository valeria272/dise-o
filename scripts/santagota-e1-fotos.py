#!/usr/bin/env python3
"""
SANTA GOTA · E1 «Uno para el fuego. Otro para el final.» — fotos del díptico (01-10-2026).

Producto EN MANOS REALES de la jornada del 10-09 (sin recortes): DSC00197 = 750 cocinar en alto,
DSC00227 = 500 aderezar sostenido con las dos manos. Mismo color que el carrusel «Elige tu pecado».

Salida (public/assets/santagota/e1/):
  fuego-45.jpg / final-45.jpg   → mitades del 4:5, 1080×2700 cada una (2× de 540×1350)
  fuego-916.jpg / final-916.jpg → mitades del 9:16, 2160×1920 cada una (2× de 1080×960)
"""
import os
import importlib.util
from PIL import Image, ImageOps

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = os.path.join(RAIZ, "raw/santa-gota/jornada-10-09")
SAL = os.path.join(RAIZ, "public/assets/santagota/e1")
os.makedirs(SAL, exist_ok=True)

# el mismo color que el carrusel: se importa la función para no tener dos recetas
spec = importlib.util.spec_from_file_location("fotos", os.path.join(RAIZ, "scripts/santagota-carrusel-paid-fotos.py"))
color = None
with open(spec.origin) as f:
    src = f.read()
ns: dict = {}
exec(src[src.index("def color"):src.index("def recorte")], {"Image": Image, "ImageEnhance": __import__("PIL.ImageEnhance").ImageEnhance}, ns)
color = ns["color"]


def extiende(im, arriba=0, derecha=0, limpia=600):
    """Agranda la pared lisa (sin IA) repitiendo SÓLO la banda de pared limpia del borde, alternando el
    sentido para que no haya costura. `limpia` = alto en px de esa banda (sobre la tapa de la botella)."""
    from PIL import ImageFilter
    w, h = im.size
    out = Image.new("RGB", (w + derecha, h + arriba))
    out.paste(im, (0, arriba))
    if arriba:
        banda = im.crop((0, 0, w, limpia))
        y, k = arriba, 0
        while y > 0:
            pieza = banda.transpose(Image.FLIP_TOP_BOTTOM) if k % 2 == 0 else banda
            y -= limpia
            out.paste(pieza, (0, y))
            k += 1
        costura = out.crop((0, max(0, arriba - 40), w, arriba + 40)).filter(ImageFilter.GaussianBlur(8))
        out.paste(costura, (0, max(0, arriba - 40)))
    if derecha:
        # pared plana fila por fila: el color de cada fila sale de la franja derecha donde ES pared
        # (rosado: r > g + 40); donde la botella llega al borde se usa la última fila de pared vista.
        import numpy as np
        a_ = np.asarray(out.crop((w - 300, 0, w, h + arriba))).astype(np.float32)
        pared = (a_[..., 0] > a_[..., 1] + 40) & (a_[..., 0] > 120)
        filas = np.zeros((a_.shape[0], 3), np.float32)
        ult = a_[0, :, :].mean(0)
        for y in range(a_.shape[0]):
            if pared[y].sum() > 50:
                ult = np.median(a_[y][pared[y]], axis=0)
            filas[y] = ult
        ext = np.repeat(filas[:, None, :], derecha, axis=1)
        ruido = np.random.default_rng(7).normal(0, 2.2, ext.shape)
        out.paste(Image.fromarray(np.clip(ext + ruido, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)), (w, 0))
        costura = out.crop((w - 30, 0, w + 30, h + arriba)).filter(ImageFilter.GaussianBlur(10))
        out.paste(costura, (w - 30, 0))
    return out


def corte(nombre, caja, tam, arriba=0, derecha=0, limpia=600):
    """caja en px de la foto ORIGINAL (antes de extender); arriba/derecha = px de pared agregada."""
    im = ImageOps.exif_transpose(Image.open(os.path.join(J, nombre))).convert("RGB")
    im = extiende(im, arriba, derecha, limpia)
    x0, y0, x1, y1 = caja
    return color(im.crop((x0, y0 + arriba if y0 else 0, x1, y1 + arriba)).resize(tam, Image.LANCZOS))


# 4:5 — mitades 0,4 (ancho/alto). La pared de arriba se extiende para dar aire a la botella y lugar al titular.
corte("DSC00197.JPG", (360, 0, 3400, 6000), (1080, 2700), arriba=1600, limpia=650).save(os.path.join(SAL, "fuego-45.jpg"), quality=92)
corte("DSC00227.JPG", (1000, 0, 3800, 6000), (1080, 2700), arriba=1000, limpia=750).save(os.path.join(SAL, "final-45.jpg"), quality=92)
# 9:16 — mitades apaisadas 1,125. Al 750 se le suma pared a la derecha para que la base no toque el borde.
corte("DSC00197.JPG", (0, 0, 5300, 4711), (2160, 1920), arriba=550, derecha=1300, limpia=650).save(os.path.join(SAL, "fuego-916.jpg"), quality=92)
corte("DSC00227.JPG", (0, 500, 4000, 4055), (2160, 1920)).save(os.path.join(SAL, "final-916.jpg"), quality=92)
print("ok")

#!/usr/bin/env python3
"""
QB · GRILLA OCTUBRE 2026 — prepara los fondos de las 11 historias.

Toma los fotogramas reales (`raw/hilton/qb/oct-fotogramas/`, salidos de
`qb-oct-fotogramas.py`) y las tres imágenes generadas (`raw/hilton/qb/oct-ia/`),
les da la gradación de cada pieza y los deja en
`public/assets/hilton/qb/oct/<pieza>.jpg`, a 2250 px de ancho cuando la fuente
alcanza.

⚠️ La gradación se hace EN CÓDIGO y no con IA porque la API de Magnific se quedó
sin créditos el 24-09-2026 a media grilla. Lo que se hace acá no inventa nada:
exposición, temperatura, curva, viñeta y desenfoque sobre la foto real.

Qué es real y qué no (define si la pieza lleva «Imagen referencial»):
  REAL  01 · 08 · 09 · 14 · 15 · 20 · 23   (fotogramas de las sesiones de QB)
  IA    06 · 21 · 22                        (Seedream 5 Pro)

Uso:  python scripts/qb-oct-fondos.py
"""
import os
import sys

import numpy as np
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOT = os.path.join(RAIZ, "raw", "hilton", "qb", "oct-fotogramas")
IA = os.path.join(RAIZ, "raw", "hilton", "qb", "oct-ia")
SES = os.path.join(RAIZ, "raw", "hilton", "qb", "sesiones-25-09", "orig")  # las que pasó Eli el 25-09
SAL = os.path.join(RAIZ, "public", "assets", "hilton", "qb", "oct")


def a_float(im):
    return np.asarray(im.convert("RGB"), dtype=np.float32) / 255.0


def a_img(x):
    return Image.fromarray((np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8))


def grado(x, expo=1.0, temp=(1, 1, 1), contraste=0.0, gamma=1.0, sat=1.0):
    x = x * expo
    x = x * np.array(temp, dtype=np.float32)
    if gamma != 1.0:
        x = np.clip(x, 0, 1) ** gamma
    if contraste:
        # curva S suave alrededor de 0,5
        x = np.clip(x, 0, 1)
        x = x + contraste * (x - 0.5) * (1 - np.abs(2 * x - 1))
    if sat != 1.0:
        l = (x * np.array([0.299, 0.587, 0.114])).sum(-1, keepdims=True)
        x = l + (x - l) * sat
    return x


def vineta(x, fuerza=0.45, radio=0.75):
    h, w = x.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    m = 1 - fuerza * np.clip((d - radio) / (1.45 - radio), 0, 1) ** 1.6
    return x * m[..., None]


def resplandor(x, cx, cy, radio, color=(1.0, 0.62, 0.25), fuerza=0.55):
    """Sol bajo: luz que se SUMA (no un velo), cálida, con caída gaussiana."""
    h, w = x.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d2 = ((xx - cx * w) ** 2 + (yy - cy * h) ** 2) / (radio * w) ** 2
    g = np.exp(-d2)[..., None] * np.array(color, dtype=np.float32) * fuerza
    return 1 - (1 - x) * (1 - g)   # screen


def recorte_vertical(im, cx):
    """De un cuadro 16:9 saca un 9:16 a alto completo, centrado en `cx` (0–1)."""
    w, h = im.size
    cw = int(h * 9 / 16)
    x0 = int(min(max(cx * w - cw / 2, 0), w - cw))
    return im.crop((x0, 0, x0 + cw, h))


def guardar(im, nombre, ancho=2250):
    if im.width != ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    d = os.path.join(SAL, nombre + ".jpg")
    im.save(d, quality=92, subsampling=0)
    print(f"✓ {nombre}.jpg  {im.size[0]}×{im.size[1]}")


def main():
    os.makedirs(SAL, exist_ok=True)
    f = lambda n: Image.open(os.path.join(FOT, n))
    g = lambda n: Image.open(os.path.join(IA, n))

    # 01 · BANCO DE CHILE — ⭐ Eli 25-09: «se ve como quemado, muy saturado, no me
    # gusta… usa del shooting nuevo, una foto mucho más bonita, más elegante».
    # ⇒ foto de estudio de la carta de enero 2026 («Ostiones parmesanos a la
    # batayaki 20»): brindis con vino blanco sobre el risotto y la trucha. Ya
    # viene bien expuesta: SIN gradación, sólo +4 % de luz. Nada de saturar.
    from PIL import ImageEnhance
    im = Image.open(os.path.join(SES, "carta__Ostiones parmesanos a la batayaki 20.jpg")).convert("RGB")
    guardar(ImageEnhance.Brightness(im).enhance(1.04), "01-bancochile")

    # 06 · ALL YOU CAN DRINK — escena generada (Seedream) con los tragos del KV.
    x = a_float(g("06-aycd-A.png"))
    x = grado(x, contraste=0.12)
    guardar(a_img(x), "06-aycd")

    # 08 · CMR FALABELLA — los tres cócteles reales en la terraza (C4146, Sony
    # 4K 16:9). Se saca el 9:16 centrado en la copa naranja.
    im = recorte_vertical(f("C4146_t5.50.png"), 0.60)
    x = a_float(im)
    x = grado(x, expo=0.9, temp=(1.05, 1.0, 0.9), contraste=0.25, gamma=1.08)
    x = vineta(x, 0.55, 0.6)
    guardar(a_img(x), "08-cmr")

    # 09 · SUNSET — ⭐ 25-09: foto REAL de la sesión de Víctor «QB 13 oct» (n°60):
    # el trago con rodaja de naranja deshidratada al sol de la tarde en la terraza,
    # bokeh de las guirnaldas detrás. Reemplaza al spritz de IMG_3077 que había
    # que llevar a atardecer en código. Sólo se calienta un punto: la luz ya es
    # de tarde. (La foto es 1500×2250: se sube a 2250 con lanczos.)
    x = a_float(Image.open(os.path.join(SES, "13oct__QB 13 oct-60.jpg")))
    x = grado(x, expo=0.97, temp=(1.04, 1.0, 0.92), contraste=0.12, sat=1.04)
    x = vineta(x, 0.45, 0.62)
    guardar(a_img(x), "09-sunset")

    # 14 · ADIVINA EL TRAGO — el mismo spritz, desenfocado: «que se intuya su
    # forma, color o tipo de copa, pero sin revelar demasiado».
    im = f("IMG_3077_t2.00.png").convert("RGB")
    im = im.filter(ImageFilter.GaussianBlur(38))
    x = grado(a_float(im), expo=0.85, temp=(1.05, 1.0, 0.92), contraste=0.15)
    x = vineta(x, 0.55, 0.5)
    guardar(a_img(x), "14-adivina")

    # 15 · MEJORES AMIGOS — foto real de noche en la terraza (C4182). Look flash:
    # más contraste y un poco más de saturación.
    x = a_float(f("C4182_t11.56.png"))
    x = grado(x, expo=1.02, contraste=0.3, gamma=1.02, sat=1.08)
    x = vineta(x, 0.5, 0.6)
    guardar(a_img(x), "15-mejoresamigos")

    # 20 · AYCD «CONTESTA LA LLAMADA» — dos tragos reales brindando (C4216).
    x = a_float(f("C4216_t1.50.png"))
    x = grado(x, expo=1.0, temp=(1.03, 1.0, 0.95), contraste=0.3, sat=1.05)
    x = vineta(x, 0.55, 0.55)
    guardar(a_img(x), "20-aycd-llamada")

    # 21 · ESTACIONAMIENTO — mano con ticket en blanco (Seedream).
    guardar(g("21-ticket-A.png").convert("RGB"), "21-ticket")

    # 22 · ENSALADA — plato generado (Seedream), para la ST animada.
    guardar(g("22-ensalada-A.png").convert("RGB"), "22-ensalada")
    guardar(g("22-ensalada-detalle.png").convert("RGB"), "22-ensalada-detalle")

    # 23 · CLOSE FRIENDS — ⭐ 25-09: foto REAL «Fotos 4 agosto / Editadas»
    # IMG_4797: manos brindando con cuatro tragos sobre la mesa de listones de
    # QB, semicenital, de noche y con flash cálido. Es lo que pedía el brief
    # («2 o 3 tragos, manos, momento real entre amigos») y la foto anterior no
    # tenía. La madera libre de abajo recibe la nota.
    x = a_float(Image.open(os.path.join(SES, "fotos-4ago-editadas__IMG_4797.jpg")))
    x = grado(x, expo=0.9, temp=(1.02, 1.0, 0.94), contraste=0.18, gamma=1.05)
    x = vineta(x, 0.5, 0.6)
    guardar(a_img(x), "23-closefriends")

if __name__ == "__main__":
    main()

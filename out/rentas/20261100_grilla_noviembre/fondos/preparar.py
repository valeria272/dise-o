#!/usr/bin/env python3
"""Fondos de la grilla NOVIEMBRE 2026 · Rentas — recorte y escala a lienzo de entrega.

Fotos REALES de `PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO` (bajadas en
raw/nuevaurbe/rentas/fotos/) y los IA de `ia/` (Seedream 5 Pro con foto real de
referencia, ver generar_ia.sh). Salida: feed 4500×5625 · historia 4500×8000.

Uso: ~/copylab-venv/Scripts/python.exe out/rentas/20261100_grilla_noviembre/fondos/preparar.py
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

AQUI = Path(__file__).parent
RAIZ = AQUI.parents[3]
FOTOS = RAIZ / "raw/nuevaurbe/rentas/fotos"
FEED, STORY = (4500, 5625), (4500, 8000)


def recorte(im, tam, cx=0.5, cy=0.5):
    """Recorta al aspecto de `tam` centrado en (cx, cy) y escala con Lanczos."""
    W, H = im.size
    ar = tam[0] / tam[1]
    if W / H > ar:
        w, h = round(H * ar), H
    else:
        w, h = W, round(W / ar)
    x = min(max(round(cx * W - w / 2), 0), W - w)
    y = min(max(round(cy * H - h / 2), 0), H - h)
    out = im.crop((x, y, x + w, y + h)).resize(tam, Image.LANCZOS)
    esc = tam[0] / w
    if esc > 1.6:   # al escalar mucho, un unsharp suave devuelve el borde perdido
        out = out.filter(ImageFilter.UnsharpMask(radius=3, percent=60, threshold=2))
    return out, esc


def grano(im, sigma=2.6, semilla=11):
    """R-20: un fondo desenfocado liso lleva grano fino o la compuerta lo bloquea."""
    a = np.asarray(im).astype(np.float32)
    a += np.random.default_rng(semilla).normal(0, sigma, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def sale(nombre, im, esc):
    (AQUI / nombre).parent.mkdir(parents=True, exist_ok=True)
    im.save(AQUI / nombre, quality=92)
    print(f"  {nombre:32s} escala {esc:.2f}×")


def abre(p):
    return Image.open(p).convert("RGB")


# ── carrusel VIVE AL AIRE LIBRE 24-11 (IA con el quincho real de referencia)
for n, cy in [(1, .5), (2, .5), (3, .5), (4, .5), (5, .55)]:
    sale(f"aire/al_{n}.jpg", *recorte(abre(AQUI / f"ia/al_{n}.png"), FEED, cy=cy))

# ── carrusel PAID 17-11 · portada y cierre con FOTO REAL; 2-4 IA
sale("paid/pd_1.jpg", *recorte(abre(FOTOS / "IMG_7934.jpg"), FEED, cx=.42))
for n, f in [(2, "pd_2.png"), (4, "pd_4.png")]:
    sale(f"paid/pd_{n}.jpg", *recorte(abre(AQUI / "ia" / f), FEED, cy=.6))
# pd_3: se come el 6 % izquierdo — el granito y la llave del lavaplatos pegados al
# filo daban «texto pegado al borde» en la compuerta (textura, no texto).
_p3 = abre(AQUI / "ia/pd_3b.png")
sale("paid/pd_3.jpg", *recorte(_p3.crop((int(_p3.width * .06), 0, _p3.width, _p3.height)), FEED, cy=.6))
sale("paid/pd_5.jpg", *recorte(abre(FOTOS / "Exterior.jpg"), FEED, cx=.45))

# ── estático 10-11 · quincho REAL con relight de cambio mínimo (luz de tarde)
sale("estatico_quincho.jpg", *recorte(abre(AQUI / "ia/es_quincho.png"), FEED, cy=.5))

# ── ST proyecto 04-11 · áreas comunes reales (juegos + torre + árbol)
sale("st_proyecto.jpg", *recorte(abre(FOTOS / "20210513123811_IMG_9628.jpg"), STORY, cx=.40))

# ── ST encuesta 25-11 · áreas verdes al atardecer (relight) + blur suave + grano
im, esc = recorte(abre(AQUI / "ia/st_areas.png"), STORY)
sale("st_encuesta.jpg", grano(im.filter(ImageFilter.GaussianBlur(18))), esc)


# ══ MAILINGS 03-11 y 24-11 · a 2× del bloque (1201 px) para que el correo no se vea blando ══
OCT = RAIZ / "out/rentas/20261000_grilla_octubre/fondos/mail"
BANNER, FICHA_FOTO, FICHA, CIERRE = (2402, 1500), (2402, 1862), (2402, 3002), (2402, 1102)
sale("mail/m1_banner.jpg", *recorte(abre(FOTOS / "20210513122924_IMG_9578.jpg"), BANNER, cy=.55))
# living REAL del proyecto (IMG_7729-Edit-Pano, el mismo de la ficha de octubre): la foto
# ocupa el 62 % alto de la ficha vertical (1201×931); se recorta hacia el sofá y la ventana.
sale("mail/m1_ficha.jpg", *recorte(abre(OCT / "m1_ficha.jpg"), FICHA_FOTO, cx=.36))
sale("mail/m1_cierre.jpg", *recorte(abre(AQUI / "ia/m1_cierre.png"), CIERRE, cy=.55))
sale("mail/m2_banner.jpg", *recorte(abre(AQUI / "ia/m2_banner.png"), BANNER, cy=.62))
sale("mail/m2_ficha.jpg", *recorte(abre(AQUI / "ia/m2_ficha.png"), FICHA, cy=.5))
sale("mail/m2_cierre.jpg", *recorte(abre(AQUI / "ia/m2_cierre.png"), CIERRE, cy=.55))

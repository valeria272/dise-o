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
# 02-10 · ronda de Constanza: al_3 → al_3b (sofá bajo la pérgola, a la sombra) y al_4 → al_4b
# (el quincho con su techo, igual al original). Los de la ronda 1 quedan en ia/ como registro.
for n, f, cy in [(1, "al_1", .5), (2, "al_2", .5), (5, "al_5", .55)]:
    sale(f"aire/al_{n}.jpg", *recorte(abre(AQUI / f"ia/{f}.png"), FEED, cy=cy))
# al_3b respeta el encuadre de la foto real y la mujer queda chica: se escaló 2× con el
# upscaler de precisión (magnific.py escalar --escala 2 --precision → al_3b_x2.jpg) y se
# cierra el recorte sobre el sofá. Una toma más cerrada pedida a la IA lo volvía a sacar al sol.
_a3 = abre(AQUI / "ia/al_3b_x2.jpg")
# El recorte arranca en y=950 para que la cabeza del farol izquierdo quede BAJO la bajada
# (a 1470 la bajada caía encima del farol).
sale("aire/al_3.jpg", *recorte(_a3.crop((0, 950, 2800, 4450)), FEED))
# al_4b respeta el encuadre de la foto real y la gente queda chica: se cierra el recorte
# sobre la mitad baja (ancho 1600 de 1770) para que el grupo pese en la lámina.
_a4 = abre(AQUI / "ia/al_4b.png")
sale("aire/al_4.jpg", *recorte(_a4.crop((60, 360, 1660, 2360)), FEED))

# ── carrusel PAID 17-11 · portada y cierre con FOTO REAL; 2-4 IA
sale("paid/pd_1.jpg", *recorte(abre(FOTOS / "IMG_7934.jpg"), FEED, cx=.42))
for n, f in [(2, "pd_2.png"), (4, "pd_4.png")]:
    sale(f"paid/pd_{n}.jpg", *recorte(abre(AQUI / "ia" / f), FEED, cy=.6))
# pd_3: se come el 6 % izquierdo — el granito y la llave del lavaplatos pegados al
# filo daban «texto pegado al borde» en la compuerta (textura, no texto).
# 02-10 · ronda de Constanza («arréglala»): pd_3b tenía a la pareja DETRÁS del mesón, que va
# contra el muro. pd_3c los pone en el pasillo, delante. cy=.4: se recorta por abajo para que
# las cabezas queden bajo el bloque de texto.
sale("paid/pd_3.jpg", *recorte(abre(AQUI / "ia/pd_3c.png"), FEED, cy=.4))
sale("paid/pd_5.jpg", *recorte(abre(FOTOS / "Exterior.jpg"), FEED, cx=.45))

# ── estático 10-11 · quincho REAL con relight de cambio mínimo (luz de tarde)
sale("estatico_quincho.jpg", *recorte(abre(AQUI / "ia/es_quincho.png"), FEED, cy=.5))

# ── ST proyecto 04-11 · áreas comunes reales (juegos + torre + árbol)
sale("st_proyecto.jpg", *recorte(abre(FOTOS / "20210513123811_IMG_9628.jpg"), STORY, cx=.40))

# ── ST encuesta 25-11 · áreas verdes al atardecer (relight) + blur suave + grano
im, esc = recorte(abre(AQUI / "ia/st_areas.png"), STORY)
# 02-10 · Constanza: «necesita más color». El desenfoque baja de 18 a 7 px (sigue siendo
# «blur suave», como pide el brief) y la saturación sube 18 %: a 18 px la foto quedaba lavada.
from PIL import ImageEnhance
im = ImageEnhance.Color(im.filter(ImageFilter.GaussianBlur(7))).enhance(1.18)
sale("st_encuesta.jpg", grano(im), esc)


# ══ MAILINGS 03-11 y 24-11 · a 2× del bloque (1201 px) para que el correo no se vea blando ══
OCT = RAIZ / "out/rentas/20261000_grilla_octubre/fondos/mail"
BANNER, FICHA_FOTO, FICHA, CIERRE = (2402, 1500), (2402, 1862), (2402, 3002), (2402, 1102)
sale("mail/m1_banner.jpg", *recorte(abre(FOTOS / "20210513122924_IMG_9578.jpg"), BANNER, cy=.55))
# living REAL del proyecto (IMG_7729-Edit-Pano, el mismo de la ficha de octubre): la foto
# ocupa el 62 % alto de la ficha vertical (1201×931); se recorta hacia el sofá y la ventana.
sale("mail/m1_ficha.jpg", *recorte(abre(OCT / "m1_ficha.jpg"), FICHA_FOTO, cx=.36))
sale("mail/m1_cierre.jpg", *recorte(abre(AQUI / "ia/m1_cierre_b.png"), CIERRE, cy=.55))
sale("mail/m2_banner.jpg", *recorte(abre(AQUI / "ia/m2_banner.png"), BANNER, cy=.62))
sale("mail/m2_ficha.jpg", *recorte(abre(AQUI / "ia/m2_ficha.png"), FICHA, cy=.5))
sale("mail/m2_cierre.jpg", *recorte(abre(AQUI / "ia/m2_cierre_c.png"), CIERRE, cy=.55))

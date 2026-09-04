#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La IMAGEN CONTINUA del carrusel de CUMPLEAÑOS (FEED 3-sep, S1) — v2.

⭐⭐ RONDA 10 · segunda pasada (04-09-2026). La primera versión movía el vaso y
borraba el plato, y Eli la devolvió:

    «las slides de cumpleaños se ve extraño el montaje, tiene que ser realista y
     no pegoteado. Se ve mal montado el café, y el color está muy oscuro.
     …que en la primera slide se vea el café CON LAS MEDIALUNAS y sea una
     continuidad con la slide dos. Puede ser solamente el fondo mismo de la mesa.
     Tienes que borrar los detalles que se vean rayones o extraño en la mesa.»

**El cambio de criterio: se deja de montar.** La slide 1 pasa a ser la
fotografía del cliente TAL CUAL —el vaso con las medialunas, sin mover nada, sin
borrar nada— y la slide 2 es la misma mesa siguiendo hacia la derecha. Todo el
trabajo se va al REVELADO, que es lo que faltaba: la sesión viene subexpuesta, la
mesa está llena de rayones y el hojaldre sale plano.

    v1: recortar el vaso, borrar el plato, espejar la escena  → «pegoteado»
    v2: no tocar la escena, revelarla                         → foto

⛔ Una tensión que hay que dejar dicha: Scarlette pidió «sacar el plato de los
   vigilantes» y Eli pide ahora ver «el café con las medialunas». Manda Eli, que
   es quien firma la marca, pero **hay que avisarle a la CM** para que no llegue
   como sorpresa en la ronda siguiente.

⚠️ Por qué el plato queda cortado por el canto izquierdo, y no es un descuido:
   el grupo (plato + vaso) mide 4.262 px de ancho en un cuadro de 3.840 de alto.
   Un 4:5 da como máximo 3.072 px de ancho, así que **no existe recorte que
   muestre las dos medialunas Y el vaso entero**. Se elige lo que manda la
   gramática de la marca —el vaso entero, el plato cortado por la izquierda,
   igual que en la referencia aprobada «El Match» y en las slides 2 y 3 del
   carrusel To Go— y se muestra todo el hojaldre que cabe.

Uso:
    python scripts/between-cumple-panorama.py
    python scripts/between-cumple-panorama.py --diagnostico
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402
from between_retoque import (apetitoso, borrosa, limpia_madera,  # noqa: E402
                             nitidez, revela)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-257.jpg"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas"
PASOS = RAIZ / "out/hilton-between-r10/pasos"

W0, H0 = 5760, 3840
#: el canto de la mesa contra el muro vegetal (medido, apenas inclinado)
BORDE_IZQ, BORDE_DER = 1843, 1786

#: la SLIDE 1 recortada de la original: 2800×3500 = 4:5 exacto.
#: 3072×3840 = 4:5 exacto, que es el recorte MÁS ANCHO que da la original.
#: Arranca en 1830 para que entren las dos medialunas (1150–3570) todo lo que se
#: pueda, y termina en 4902 para que el vaso (3600–4752) quede entero con 150 px
#: de aire hasta la costura — pegado al canto se leería como cortado.
SLIDE1 = (1830, 0, 4902, 3840)
#: de la slide 2, 860 px son reales (el flanco despejado a la derecha del vaso) y
#: el resto se teje espejando ese mismo flanco.
BANDA_LIMPIA = (4900, 5760)

PANORAMA = (4500, 2812)
SLIDE = (2250, 2812)

#: el plato con las dos medialunas, para el retoque de comida (no se toca nada
#: más: subirle claridad a la loza o a la madera las ensucia)
COMIDA = (900, 2000, 4150, 3320)
#: el vaso, que se protege del limpiador de madera
VASO = (3480, 1140, 4880, 2910)


def mascara(caja, tamano, elipse=False):
    m = Image.new("L", tamano, 0)
    d = ImageDraw.Draw(m)
    (d.ellipse if elipse else d.rectangle)(caja, fill=255)
    return np.asarray(m) > 127


def zona_mesa(alto, ancho):
    xs = np.arange(ancho, dtype=np.float32)
    borde = BORDE_IZQ + (BORDE_DER - BORDE_IZQ) * xs / W0
    ys = np.arange(alto, dtype=np.float32)[:, None]
    return ys > (borde[None, :] + 30)


def alarga_escena(im, hasta_x):
    """Alarga la escena hacia la derecha. La mesa y el muro, por separado.

    ⛔ El primer intento tejió las dos zonas espejando el mismo flanco y el MURO
       lo delató: las hojas desenfocadas son manchas grandes y reconocibles, y
       espejadas dibujan mariposas. La mesa aguanta el espejo —la veta no tiene
       dirección de lectura— pero el follaje no.

    Así que:
      · MESA  → espejo del flanco despejado. Cada unión es continua (el píxel
        del borde se toca consigo mismo) y, con la madera ya limpia de rayones,
        no queda nada que reconocer.
      · MURO  → el mismo espejo, pero PERDIENDO FOCO en rampa hacia el canto:
        el follaje deja de tener formas reconocibles y se lee como profundidad.
    """
    if hasta_x <= im.width:
        return im
    x0, x1 = BANDA_LIMPIA
    paso = x1 - x0
    salida = Image.new("RGB", (hasta_x, im.height))
    salida.paste(im, (0, 0))

    # ── la mesa, espejada ──
    banda = im.crop((x0, 0, x1, im.height))
    espejo = banda.transpose(Image.FLIP_LEFT_RIGHT)
    x, vuelta = im.width, 0
    while x < hasta_x:
        salida.paste(espejo if vuelta % 2 == 0 else banda, (x, 0))
        x += paso
        vuelta += 1
    a = np.asarray(salida).astype(np.float32)

    # ── el muro: el mismo flanco, pero PERDIENDO FOCO hacia el canto ──
    # ⛔ El intento de reconstruirlo con el color medio de cada fila más ruido
    #    salió peor que el espejo: un rectángulo granulado con canto duro. El
    #    ruido gaussiano no se parece en nada al bokeh, que son manchas grandes
    #    y blandas.
    # ⭐ Lo que sí funciona es no inventar nada y **desenfocar de más**: el
    #    follaje espejado deja de tener formas reconocibles y, de paso, se lee
    #    como profundidad —el muro se va de foco hacia el fondo del encuadre—,
    #    que es lo que hace de verdad un 50 mm a f/3,5. El desenfoque entra en
    #    rampa desde la costura, así que no hay canto.
    ancho = hasta_x - im.width
    zona = a[:, im.width:]
    difuso = borrosa(zona, 95)
    t = np.clip(np.arange(ancho, dtype=np.float32) / max(1.0, ancho * 0.45), 0, 1)
    ys = np.arange(im.height, dtype=np.float32)[:, None, None]
    es_muro = np.clip((BORDE_IZQ - 60 - ys) / 120.0, 0, 1)
    peso = t[None, :, None] * es_muro
    a[:, im.width:] = zona * (1 - peso) + difuso * peso

    # ── y la mesa se ALISA en la misma rampa ──
    # Las vetas largas y de bajo contraste no las caza el limpiador —no son
    # marcas oscuras, son dibujo de la madera— pero espejadas trazan un festón
    # simétrico que sí se ve. Un alisado suave, entrando en rampa desde la
    # costura, las apaga sin que aparezca ningún canto.
    zona = a[:, im.width:]
    liso = borrosa(zona, 20)
    peso_mesa = t[None, :, None] * (1 - es_muro) * 0.85
    a[:, im.width:] = zona * (1 - peso_mesa) + liso * peso_mesa
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def apaga_hacia_afuera(im, desde_x, caida=0.10):
    """La mesa se apaga un punto hacia el extremo derecho.

    Dos cosas de una: rompe la simetría que deja el tejido y reproduce la caída
    de luz que tiene cualquier mesa hacia el borde del encuadre. Muy suave — por
    encima de 0,12 se lee como viñeta, y la marca no usa viñetas.
    """
    a = np.asarray(im).astype(np.float32)
    xs = np.arange(a.shape[1], dtype=np.float32)
    t = np.clip((xs - desde_x) / max(1.0, a.shape[1] - desde_x), 0, 1)
    return Image.fromarray(
        np.clip(a * (1 - caida * t)[None, :, None], 0, 255).astype(np.uint8))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--diagnostico", action="store_true")
    a = ap.parse_args()
    if not ORIGEN.exists():
        sys.exit(f"⛔ Falta la original: {ORIGEN}")
    DESTINO.mkdir(parents=True, exist_ok=True)
    if a.diagnostico:
        PASOS.mkdir(parents=True, exist_ok=True)

    im = Image.open(ORIGEN).convert("RGB")
    print(f"origen  {im.size}")

    # 1 · la mesa, sin rayones ni grietas
    proteger = mascara((820, 1950, 4150, 3500), im.size) | mascara(VASO, im.size)
    im, marcas = limpia_madera(im, zona=zona_mesa(im.height, im.width),
                               proteger=proteger, umbral=10, nucleo=61)
    print(f"mesa limpia ✓  ({marcas} px de rayones y grietas borrados)")
    # ⭐ y una segunda pasada, más dura, SÓLO sobre el flanco que después se
    #    espeja: cualquier marca que sobreviva ahí se ve DOS veces y en simetría,
    #    que es justo lo que el ojo caza. En el resto de la mesa esta dureza se
    #    comería la veta.
    solo_banda = np.zeros((im.height, im.width), bool)
    solo_banda[:, BANDA_LIMPIA[0]:BANDA_LIMPIA[1]] = True
    im, extra = limpia_madera(im, zona=zona_mesa(im.height, im.width) & solo_banda,
                              umbral=6, nucleo=81)
    print(f"flanco a espejar, segunda pasada ✓  ({extra} px)")
    if a.diagnostico:
        im.save(PASOS / "1-mesa-limpia.jpg", quality=95)

    # 2 · la escena sigue hacia la derecha: misma mesa, mismo muro
    ancho_total = SLIDE1[2] + (SLIDE1[2] - SLIDE1[0])       # 4900 + 2800
    im = alarga_escena(im, ancho_total)
    im = apaga_hacia_afuera(im, BANDA_LIMPIA[1])
    pano = im.crop((SLIDE1[0], SLIDE1[1], ancho_total, SLIDE1[3]))
    print(f"escena alargada ✓  {pano.size}  (real hasta x={W0}, tejido hasta {ancho_total})")
    pano = pano.resize(PANORAMA, Image.LANCZOS)
    if a.diagnostico:
        pano.save(PASOS / "2-panorama-crudo.jpg", quality=95)

    # 3 · revelado: la sesión viene subexpuesta y apagada
    pano = revela(pano, luces=213.0, negros=0.010, contraste=1.07)

    # 4 · que las medialunas den hambre
    escala = PANORAMA[0] / (ancho_total - SLIDE1[0])
    caja = tuple(int((c - o) * escala) for c, o in
                 zip(COMIDA, (SLIDE1[0], SLIDE1[1], SLIDE1[0], SLIDE1[1])))
    pano = apetitoso(pano, mascara(caja, PANORAMA, elipse=True),
                     claridad=0.62, cuerpo=1.16, calor=7.0)

    # 5 · el remate
    pano = nitidez(pano, cantidad=0.46, radio=1.4)

    pano.save(DESTINO.parent / "cumple-panorama.jpg", quality=96)
    pano.crop((0, 0, *SLIDE)).save(DESTINO / "cumple-continua-1.jpg", quality=95)
    pano.crop((SLIDE[0], 0, *PANORAMA)).save(DESTINO / "cumple-continua-2.jpg", quality=95)
    print(f"✓ cumple-continua-1.jpg  {SLIDE}")
    print(f"✓ cumple-continua-2.jpg  {SLIDE}")


if __name__ == "__main__":
    main()

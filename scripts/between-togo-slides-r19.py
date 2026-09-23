#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · slides 2, 3 y 4 (S4, 22-sep) — ronda 19: generadas, no compuestas.

Eli, 07-09-2026:

    «Pero las demás se ven extrañas, desde la slide dos, tres, cuatro, la foto
     ya deja de tener sentido. Los logos están mal puestos, y en el último slide
     número cuatro, borra los logos porque se ve muy mal, solamente déjala en el
     vaso de TOGO. Necesito que seas más eficiente y me generes en magnific
     mejores imágenes, realistas y de calidad. Parecen de paint pegoteados […]
     Ahora quiero que generes con prompt cada foto de fondo.»

⭐⭐⭐ EL CAMBIO DE MÉTODO, Y ES LA LECCIÓN GRANDE DE ESTA CUENTA

Eli rehízo el carrusel de cumpleaños ella misma y dejó su prompt a la vista:

    «Reemplaza el vaso de la @img1 por la del vaso igual al de la @img2.
     Necesito que el plato con medialunas quede en la derecha y mejora calidad,
     que se vea delicioso y apetitoso, añade detalles de serpentina de
     cumpleaños elegante y dorada alrededor, debe ser realista y de alta
     calidad 4k»

O sea: **ella no compone, GENERA.** Le pasa las fotos reales como referencia y le
pide la escena terminada. El vaso, el logotipo impreso, la serpentina dorada, la
luz y las sombras nacen DENTRO de la imagen, así que no hay nada que integrar
después.

Yo venía haciendo lo contrario: generaba un fondo y le pegaba encima recortes
reales, logotipos vectoriales, sombras de contacto y campos de luz calculados. Y
por eso «parecen de paint pegoteados» — cada elemento agregado es una costura
más, y ninguna receta de montaje compite con un render que ya nace unido.

> **Regla: si el generador puede producir la escena COMPLETA con las fotos reales
> como referencia, se genera completa. Componer recortes encima es el camino de
> último recurso, no el primero.**
>
> El corolario para la jerarquía de imagen del manual: la IA sí puede rehacer el
> producto **cuando va guiada por la foto del producto real**, porque entonces su
> forma, su proporción y su logotipo impreso salen de la cosa real. Eso es
> distinto de inventar un producto, que sigue prohibido.

⭐ Y de paso desaparece la mitad del código: acá NO se estampa ningún logotipo.
El vaso ya lo trae impreso desde la generación, y la bolsa de la slide 4 se pidió
**lisa a propósito** — es la instrucción literal de Eli, «borra los logos, déjala
sólo en el vaso de TOGO».

⚠️ Lo único que hace falta después de generar es igualar el TONO al de la
portada, que es la única foto de este carrusel que Eli dejó aprobada. Medido:

    pieza                          mediana    p10   calidez   saturación
    PORTADA (aprobada)               123,8   25,6      34,2        34,4
    slide 2 generada cruda           137,5   52,3      77,3        51,6
    slide 3 generada cruda           141,2   57,2      71,5        48,6
    slide 4 generada cruda           165,1   34,9      67,5        47,1

Las tres vienen consistentemente más cálidas y más saturadas: el generador tira a
la hora dorada. Se llevan a las cifras de la portada con `iguala_tono()`, que es
la misma función que ya pasó por cuatro rondas de correcciones del cliente.

Salidas: fotos-gradadas/togo-s{2,3,4}-r19.jpg (2250×2812)
"""
import importlib.util
import sys
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from between_retoque import hombro, informe  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# se reusa `iguala_tono` de la ronda 12: cada línea suya está justificada allí
_spec = importlib.util.spec_from_file_location(
    "between_togo4_r12", RAIZ / "scripts/between-togo4-r12.py")
_r12 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_r12)
iguala_tono = _r12.iguala_tono

BASE = RAIZ / "public/assets/hilton/between"
SALIDA_PX = (2250, 2812)
RECORTE_ARRIBA = 160

#: el objetivo sale de la PORTADA, la única foto de este carrusel que Eli aprobó
# ⚠️ La CALIDEZ se pide en 60 y no en 34, aunque la portada mida 34,2. No es un
# error: `iguala_tono()` corrige primero la calidez y DESPUÉS la saturación, y el
# paso de saturación (×0,55 acá) vuelve a comprimir la diferencia R−B. Pidiendo
# 34 el resultado terminaba en 19-20, o sea MÁS FRÍO que la portada y visible en
# el carrusel. Pidiendo 60 el final cae en ~34, que es el objetivo real.
# Medido, no estimado: 34 → 19,2 · 60 → ver el control de abajo.
OBJ_MEDIANA, OBJ_CALIDEZ, OBJ_SATURACION = 124, 60.0, 35.0

SLIDES = ("s2", "s3", "s4")

#: ⭐ RONDA 20 — la ronda se pasa por entorno para no duplicar el script: la
#: tubería es la misma, cambian las generaciones de entrada.
#:     BW_TOGO_RONDA=r20 python scripts/between-togo-slides-r19.py
import os  # noqa: E402
RONDA = os.environ.get("BW_TOGO_RONDA", "r19")

#: ⚠️ Y QUÉ slides procesar, porque a partir de la ronda 21 cada una vive en una
#: ronda distinta: la 2 quedó bien en la r20, la 3 se rehizo en la r21 (medialuna
#: exagerada) y la 4 en la r22 (el plato de cerámica del muffin). Procesar las
#: tres con una sola RONDA sobreescribiría las buenas con generaciones que no
#: existen.
#:     BW_TOGO_RONDA=r21 BW_TOGO_SLIDES=s3 python scripts/between-togo-slides-r19.py


def cifras(im, nom):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114
    mx, mn = a.max(axis=2), a.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1) * 100, 0)
    print(f"   {nom:12s} mediana {np.median(g):6.1f} · p10 {np.percentile(g, 10):5.1f} · "
          f"calidez {(a[..., 0] - a[..., 2]).mean():5.1f} · saturación {sat.mean():5.1f}")


def una(slug):
    gen = BASE / f"ia-sept/togo-{slug}-{RONDA}.png"
    if not gen.exists():
        sys.exit(f"falta la generación: {gen}")
    im = Image.open(gen).convert("RGB")
    alto = int(round(im.width / 0.8))
    y0 = min(RECORTE_ARRIBA, im.height - alto)
    im = im.crop((0, y0, im.width, y0 + alto)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"\n-- {slug}: generación {gen.name} · recorte 4:5 desde y={y0}")
    cifras(im, "generada")

    im = iguala_tono(im, mediana=OBJ_MEDIANA, calidez=OBJ_CALIDEZ,
                     saturacion=OBJ_SATURACION)
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    cifras(im, "final")
    informe(im, slug)

    destino = BASE / f"fotos-gradadas/togo-{slug}-{RONDA}.jpg"
    destino.parent.mkdir(parents=True, exist_ok=True)
    im.save(destino, quality=95, subsampling=0)
    print(f"   -> {destino.relative_to(RAIZ)}")


def main():
    print(f"objetivo (la PORTADA aprobada): mediana {OBJ_MEDIANA} · "
          f"calidez {OBJ_CALIDEZ} · saturación {OBJ_SATURACION}")
    pedidas = os.environ.get("BW_TOGO_SLIDES", "").split()
    for s in (pedidas or SLIDES):
        una(s)
    print("\nlisto. ⚠️ Ningún logotipo estampado: vienen nativos en la generación, "
          "y la bolsa de la slide 4 va LISA por instrucción de Eli.")


if __name__ == "__main__":
    main()

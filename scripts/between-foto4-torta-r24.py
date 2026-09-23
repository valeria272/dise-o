#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PRIMERO LA FOTO… ¿O NO? · slide 4 (FEED 14-sep) — la torta casi comida.

Eli, 07-09-2026 (cambio de último minuto):

    «para el carrusel slide último 14/09/2026 del 14, debe ser una torta casi en
     totalidad comida, pero que se vea lindo aún […] esa es la torta real»

Y coincide con el comentario del cliente que seguía SIN TACHAR en `FEED!H15`:

    «G4: Aquí la idea es que se vea más vacío el plato, veamos otra opción de
     foto, que sea desde arriba también como los 2 anteriores (como la refe)»

O sea que el encargo trae dos condiciones, no una: **plato casi vacío** y **toma
CENITAL**, como las slides 1 y 2.

⚠️ OJO CON EL CARRUSEL: el del 14-09 NO es Promos To Go (ése se movió a la S4 del
22-09). Es «PRIMERO LA FOTO… ¿O NO?» —columna H de la grilla, semana 3—, cuyo
remate es «¡NOOO! Se me olvidó la foto». La torta comida ES el chiste de la pieza.

⭐ PRIMERO SE BUSCÓ EN LA SESIÓN, que es la regla del manual antes de generar.
Eli dejó una carpeta de dulces y tortas con 9 videos verticales 2160×3840 a 60
fps (ver `raw/hilton/between/dulces-tortas/LEEME.md`). Un fotograma de esos
videos es una foto 4K, así que sirven como banco de imagen. Se revisó:

    IMG_3544  el que Eli marcó — pie de limón CENITAL, intacto
    IMG_3545  los 11,1 s completos, fotograma a fotograma — intacto de principio
              a fin, sólo gira en las manos

⛔ **La torta comida no existe en el material.** Por eso hubo que generarla — pero
después de comprobarlo, no antes.

⭐ CÓMO SE GENERÓ, y son dos pasadas con UNA VARIABLE cada una

  1. la torta real (`frames/frame-3.800.png` del IMG_3544, el fotograma más
     nítido: varianza del laplaciano 33,3 contra 30,5 del 2,799 que marcó Eli —
     misma toma, diferencia despreciable) como referencia, pidiendo el mismo
     postre y la misma vajilla pero casi comido y cenital;
  2. ⚠️ la primera pasada dejó **más de media porción** en el plato: eso es
     «parcialmente comida», no «casi en su totalidad», y es justo lo que el
     cliente pedía corregir. La segunda pasada le pasó la PRIMERA como
     referencia y cambió una sola cosa: que quedara **sólo un último bocado**.

Lo que se conserva del postre real y hay que verificar en cada pasada: el plato
de cerámica verde oliva con anillos concéntricos, el mármol blanco, la rodaja de
limón deshidratado, la placa amarilla con la flor de pensamiento, la frutilla y
las perlitas doradas. Es lo que lo mantiene «lindo aún» con el plato vacío.

⚠️ EL TONO se iguala a las TRES HERMANAS del carrusel, no a la pieza anterior.
Medido:

    pieza                        mediana    p10   calidez   saturación
    h1 desayuno cenital            103,1   28,2      20,9        32,7
    h2 latte cenital               108,9   24,2      20,4        27,4
    h3 croissant jamón              93,8   29,1      21,1        30,9
    h4 ANTERIOR (postre empezado)   91,9   39,3      21,6      **49,8**  ← el patito feo
    objetivo (media de h1-h3)        102      —       20,8        30,3

La h4 anterior estaba 19 puntos de saturación por encima de sus hermanas. Con el
objetivo puesto en la media de las tres, el carrusel cierra parejo.

Salida: fotos-gradadas/h4-torta-comida-r24.jpg (2250×2812)
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

_spec = importlib.util.spec_from_file_location(
    "between_togo4_r12", RAIZ / "scripts/between-togo4-r12.py")
_r12 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_r12)
iguala_tono = _r12.iguala_tono

BASE = RAIZ / "public/assets/hilton/between"
# ⭐ RONDA 25 — la torta pasa del MÁRMOL BLANCO a la MESA DE LISTONES OSCURA.
# Al montar la r24 en el carrusel apareció un defecto que la foto sola no
# mostraba: sus tres hermanas están sobre listones de madera oscura y la torta
# sobre mármol, así que rompía el mundo del carrusel — y encima dejaba el texto
# blanco sobre fondo claro, casi ilegible. Medido: la r24 daba mediana 219
# contra ~102 de las hermanas, y forzarla al tono de ellas dejaba el mármol gris.
# Releyendo el comentario del cliente, «que sea desde arriba también como los 2
# anteriores» no hablaba sólo del ÁNGULO: hablaba de la MESA.
GEN = BASE / "ia-sept/foto-torta-comida-r25.png"
SALIDA = BASE / "fotos-gradadas/h4-torta-comida-r25.jpg"
HERMANAS = ("h1-desayuno-cenital.jpg", "h2-latte-cenital.jpg",
            "h3-croissant-jamon.jpg")

SALIDA_PX = (2250, 2812)
#: ⚠️ La r25 viene 3584×4800 y el recorte 4:5 pide 4480 de alto, así que sólo
#: sobran 320 px. El plato queda centrado en el máximo (y0=320); menos que eso
#: deja aire muerto arriba y corta el mango de la cuchara abajo.
RECORTE_ARRIBA = 320

#: ⚠️ La CALIDEZ se pide más alta de la que se quiere. `iguala_tono()` corrige
#: calidez y DESPUÉS saturación, y el paso de saturación vuelve a comprimir la
#: diferencia R−B. El factor NO es fijo: depende de cuánto desature esa foto en
#: particular. Acá se midió sobre la propia r25 —pedir 36 terminó en 28,3, o sea
#: un x0,786— y se afinó en dos pasadas hasta el 22,8 que aterriza en 20,8.
OBJ_MEDIANA, OBJ_CALIDEZ, OBJ_SATURACION = 102, 22.8, 30.0


def cifras(im, nom):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114
    mx, mn = a.max(axis=2), a.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1) * 100, 0)
    print(f"   {nom:14s} mediana {np.median(g):6.1f} · p10 {np.percentile(g, 10):5.1f} · "
          f"calidez {(a[..., 0] - a[..., 2]).mean():5.1f} · saturación {sat.mean():5.1f}")


def main():
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN}")

    print("las tres hermanas del carrusel:")
    for n in HERMANAS:
        p = BASE / "fotos-gradadas" / n
        if p.exists():
            cifras(Image.open(p), n.split("-")[0])
    print(f"objetivo: mediana {OBJ_MEDIANA} · calidez {OBJ_CALIDEZ} "
          f"(real ~20,8) · saturación {OBJ_SATURACION}")

    im = Image.open(GEN).convert("RGB")
    alto = int(round(im.width / 0.8))
    y0 = min(RECORTE_ARRIBA, im.height - alto)
    im = im.crop((0, y0, im.width, y0 + alto)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"\nrecorte 4:5 desde y={y0} -> {im.width}×{im.height}")
    cifras(im, "generada")

    im = iguala_tono(im, mediana=OBJ_MEDIANA, calidez=OBJ_CALIDEZ,
                     saturacion=OBJ_SATURACION)
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    cifras(im, "final")
    informe(im, "torta comida")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    im.save(SALIDA, quality=95, subsampling=0)
    print(f"-> {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

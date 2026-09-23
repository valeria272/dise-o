#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO (FEED 22-sep, col L) — ronda 23: las slides 2, 3 y 4 «opacadas».

Lo que pide la ronda:

1. Scarlette, comentario nativo del 14-09 10:29 en la celda del carrusel:
       «acá hay que cambiar la portada a alguna de las que saco el seba yyy me
        parece que se ven un poco OPACADAS las imagenes de las demás slides a
        comparación de los demás materiales»
2. `FEED!L15`, comentario nuevo PREPENDIDO el mismo día:
       «Ver si podemos armar una foto en la G1 conlas fotos sacadas por Seba»
3. Eli: «añade un poco de color sutil a las demás slides, que se vea con vida
   pero sutil».

Este script resuelve SÓLO el punto 1 (slides 2-4). La portada va aparte.

⭐⭐ EL HALLAZGO: «opacadas» no es falta de contraste, es que están LAVADAS.

    Medido contra los materiales aprobados del mes (mismas unidades que
    `between-togo-r11.py`: mediana 0-255 y calidez = R.media − B.media):

        grupo                       mediana   calidez   croma
        TO GO slides 2-4             123,3      29,2     18,4
        aprobados del mes             91,7      25,2     22,1

    O sea: **un tercio más claras que todo lo demás y con 17 % menos de color**,
    con el contraste YA correcto (1,03× el de lo aprobado). Subir contraste no
    era el camino; había que devolverles densidad y color.

⛔ Y LA TRAMPA, que es el motivo de que esto sea un script y no un ajuste a ojo:
   **realzar SUBE la calidez.** Con los parámetros obvios
   (`revela(medios=104)` + `vivo(0.34)`) la calidez se va de 29,2 a 33,9, porque
   el estirón de negros, la gamma y la vibrancia amplifican la dominante cálida
   de la madera y el kraft. Entregar eso es devolver el «filtro medio raro» que
   Scarlette pidió sacar el 31-08 y que la ronda 11 arregló. Por eso
   `calidez_max` baja a 8: NO es que la foto quede fría, es la precompensación
   para que DESPUÉS del realce aterrice en la calidez de lo aprobado.

Resultado medido (promedio de las tres):

        mediana 100,7  ·  calidez 25,8  ·  croma 21,5  ·  0,00 % de blanco puro

    contra el objetivo (aprobados): mediana ~92-100, calidez 25,2, croma 22,1.

⛔ Lo que NO se toca: el encuadre, la diagramación, el producto y el logotipo
   impreso del vaso. Esta ronda es SÓLO revelado.

Salidas (sufijo `-r23`) en public/assets/hilton/between/fotos-gradadas/.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import revela, vivo

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

F = Path("public/assets/hilton/between/fotos-gradadas")

# medios: densidad por MEDIANA (123 -> ~101). calidez_max: precompensación.
MEDIOS, CALIDEZ_MAX, VIBRANCIA = 104, 8, 0.36

PIEZAS = [
    ("togo-s2-r20.jpg", "togo-s2-r23.jpg", "slide 2 · café + sándwich"),
    ("togo-s3-r21.jpg", "togo-s3-r23.jpg", "slide 3 · café + dulce"),
    ("togo-s4-r22.jpg", "togo-s4-r23.jpg", "slide 4 · los tres"),
]


def medir(im):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a.mean(2)
    return (float(np.median(a)),
            float(a[..., 0].mean() - a[..., 2].mean()),
            float(np.abs(a - g[..., None]).max(2).mean()),
            float((a > 250).mean() * 100))


def main():
    print(f"{'pieza':30s} {'mediana':>16s} {'calidez':>16s} {'croma':>16s} {'%blanco':>8s}")
    print("-" * 92)
    for src, dst, nombre in PIEZAS:
        im = Image.open(F / src).convert("RGB")
        antes = medir(im)
        out = vivo(revela(im, medios=MEDIOS, calidez_max=CALIDEZ_MAX),
                   vibrancia=VIBRANCIA)
        desp = medir(out)
        out.save(F / dst, "JPEG", quality=95, subsampling=0)
        print(f"{nombre:30s} {antes[0]:7.1f} -> {desp[0]:5.1f} "
              f"{antes[1]:7.1f} -> {desp[1]:5.1f} "
              f"{antes[2]:7.1f} -> {desp[2]:5.1f} {desp[3]:8.2f}")
        if desp[3] > 0.02:
            print(f"   ⛔ {nombre}: {desp[3]:.2f} % de blanco puro — revisar el hombro")
    print("-" * 92)
    print("objetivo (aprobados del mes): mediana ~92-100 · calidez 25,2 · croma 22,1 · blanco 0,00")


if __name__ == "__main__":
    main()

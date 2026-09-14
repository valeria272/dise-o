#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO (FEED 22-sep, col L) — ronda 24: las slides piden MÁS luz y MÁS color.

Eli, sobre la ronda 23:
    «Para las demás slide, casi mejora necesito una mejora más de luz y un poco
     de color.»

⭐ LO QUE CORRIGE, y es un error de lectura mío en la ronda 23. «Opacadas» lo
   diagnostiqué como «lavadas» y bajé la mediana de 124 a 101 para pegarle al
   promedio de lo aprobado del mes. El color sí faltaba —eso estaba bien—, pero
   la DENSIDAD no sobraba: Eli quiere las piezas luminosas, no densas. Perseguir
   la mediana del resto del mes fue perseguir la métrica equivocada; el promedio
   del mes incluye piezas de interior oscuro (Cumple está en 70) y estos
   bodegones son de luz natural sobre madera clara.

    versión              mediana   calidez   croma
    original (r20-r22)     124,0      29,2     18,4
    ronda 23               100,7      25,8     21,5   <- demasiado densa
    ronda 24               110,0      26,4     24,1   <- acá

   O sea: se devuelve buena parte de la luz (101 -> 110) y se sube el color por
   encima de lo que tenía la r23 (21,5 -> 24,1), que es exactamente el pedido.

⛔ Se mantiene la precompensación de calidez, por el mismo motivo de la r23:
   subir vibrancia a 0,60 empuja la calidez a 29,1 y eso es devolver el «filtro
   medio raro» del 31-08. Con `calidez_max=5` aterriza en 26,4.

⛔ Y el hombro sigue garantizando que no clipee: 0,00 % de blanco puro. El
   hojaldre del croissant conserva sus capas — es la regla «la comida clara se
   grada con mano SUAVE» del manual.

⛔ Lo que NO se toca: encuadre, diagramación, producto y el logotipo impreso del
   vaso. Esta ronda es SÓLO revelado, y parte SIEMPRE de los originales
   (r20/r21/r22), nunca del resultado de la ronda 23: revelar dos veces
   acumularía el estirón de negros.

Salidas (sufijo `-r24`) en public/assets/hilton/between/fotos-gradadas/.
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

MEDIOS, CALIDEZ_MAX, VIBRANCIA = 114, 5, 0.60

PIEZAS = [
    ("togo-s2-r20.jpg", "togo-s2-r24.jpg", "slide 2 · café + sándwich"),
    ("togo-s3-r21.jpg", "togo-s3-r24.jpg", "slide 3 · café + dulce"),
    ("togo-s4-r22.jpg", "togo-s4-r24.jpg", "slide 4 · los tres"),
]


def medir(im):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a.mean(2)
    return (float(np.median(a)),
            float(a[..., 0].mean() - a[..., 2].mean()),
            float(np.abs(a - g[..., None]).max(2).mean()),
            float((a > 250).mean() * 100),
            float((a > 244).mean() * 100))


def main():
    print(f"{'pieza':30s} {'mediana':>16s} {'calidez':>16s} {'croma':>16s} {'>250':>7s} {'>244':>7s}")
    print("-" * 106)
    for src, dst, nombre in PIEZAS:
        im = Image.open(F / src).convert("RGB")
        a = medir(im)
        out = vivo(revela(im, medios=MEDIOS, calidez_max=CALIDEZ_MAX), vibrancia=VIBRANCIA)
        d = medir(out)
        out.save(F / dst, "JPEG", quality=95, subsampling=0)
        print(f"{nombre:30s} {a[0]:7.1f} -> {d[0]:5.1f} {a[1]:7.1f} -> {d[1]:5.1f} "
              f"{a[2]:7.1f} -> {d[2]:5.1f} {d[3]:7.2f} {d[4]:7.2f}")
        if d[3] > 0.02:
            print(f"   ⛔ {nombre}: {d[3]:.2f} % de blanco puro — revisar el hombro")
    print("-" * 106)
    print("ronda 23 fue: mediana 100,7 · calidez 25,8 · croma 21,5   (Eli: «más luz y un poco de color»)")


if __name__ == "__main__":
    main()

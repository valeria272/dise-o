#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 28 (Eli 30-09): Sunset con el cóctel protagonista y carrusel CMR
sin sombra detrás del 40 %.

    python scripts/qb-oct-r28-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r28/_antes/", "out/qb/oct/r28/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 28", "Sunset con el cóctel protagonista y carrusel CMR",
           "30-09-2026 · 4 archivos reemplazados en Drive (md5 igual)", N + "revision-r28.html",
           origen="scripts/qb-oct-r28-revision.py")
p.comparar((A + "ST n°5 S1 QB OCT 26.png", "antes (r27)"), (N + "ST n°5 S1 QB OCT 26.png", "ahora (r28)"),
           titulo="ST 09-10 · Sunset QB  (ST n°5 S1)", ancho=400,
           que="Eli: «los platos para compartir destacan mucho; la idea es que el cóctel destaque más. Agrega sólo una "
               "tabla para compartir y que esté un poco más desenfocada… y un poco más de luz de atardecer en algún "
               "costado, como un rayito muy natural, muy sutil. Lo demás lo veía bastante bien».",
           notas=("Qué cambió", ["Sale el plato de papas: queda UNA sola tabla, más chica y un poco más atrás.",
                                 "La tabla va desenfocada; el spritz queda nítido y es lo primero que se ve.",
                                 "Un rayo de sol tibio, muy suave, entra desde la derecha sobre la mesa y el trago.",
                                 "Fondo: la misma foto real de la terraza de QB. Diseño y posiciones: iguales a la r27.",
                                 "Textos: sin cambios."]))
p.laminas([(A + "C3 S1 N°%d QB OCT 26.png" % i, "<b>antes (r27)</b> — N°%d" % i) for i in (1, 2, 3)],
          titulo="FEED 09-10 · Carrusel CMR — ANTES", ancho=330)
p.laminas([(N + "C3 S1 N°%d QB OCT 26.png" % i, "<b>ahora (r28)</b> — N°%d" % i) for i in (1, 2, 3)],
          titulo="FEED 09-10 · Carrusel CMR — AHORA", ancho=330,
          que="Eli (con una línea roja al pie y un círculo en la mano de la N°2): «el 40… se ve muy oscuro detrás, quita "
              "ese degradado negro; beneficios especiales, sábados y el legal, y reserva: bájalos».",
          notas=("Qué cambió", ["N°2: fuera el degradado negro detrás del 40 %.",
                                "N°2: se borró de la foto la mano derecha con la ribs (la del círculo); detrás de la promo "
                                "queda el spritz y la mesa.",
                                "Los tres textos de abajo bajan juntos a la misma línea (y=1150): «Beneficios especiales…» "
                                "(N°1), «Sábados pagando…» y el legal (N°2) y el botón «RESERVA AHORA» (N°3).",
                                "Ojo: el legal de la N°2 queda más abajo que el 12 % de margen de feed (cierra en ≈1255 de 1350).",
                                "Textos: sin cambios."]))
p.escribir()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 27 (Eli 30-09): Sunset con la terraza REAL de QB, carrusel CMR sin
tono oscuro y carrusel de cumpleaños parejo.

    python scripts/qb-oct-r27-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r27/_antes/", "out/qb/oct/r27/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 27", "Sunset con la terraza real, carruseles CMR y cumpleaños",
           "30-09-2026 · 7 archivos reemplazados en Drive (md5 igual)", N + "revision-r27.html",
           origen="scripts/qb-oct-r27-revision.py")
p.comparar((A + "ST n°5 S1 QB OCT 26.png", "antes (r26)"), (N + "ST n°5 S1 QB OCT 26.png", "ahora (r27)"),
           titulo="ST 09-10 · Sunset QB  (ST n°5 S1)", ancho=400,
           que="Eli: «el fondo tiene que ser realista, igual a QB. Tienes muchas imágenes y sesiones de cómo es; hazlo muy "
               "realista, porque es uno de los mayores comentarios que llega: que no se parece a QB».",
           notas=("Qué cambió", ["El fondo ahora es una FOTO REAL de la terraza de QB (sesión «QB 13 oct», foto 49): el techo "
                                 "de tela drapeada con vigas negras, ventiladores y ampolletas, las plantas, las estufas y las "
                                 "mesas y sillas reales. No es una terraza inventada.",
                                 "La IA sólo agregó el spritz y la Tabla Argentina sobre la mesa de adelante y unos invitados "
                                 "lejos, desenfocados. Sin manos y una sola mesa, que llega hasta abajo.",
                                 "Luz: la luz de día real de la foto, natural.",
                                 "«Cocktails seleccionados / al mejor precio / DESDE $3.990» pasa a la izquierda, sobre la "
                                 "copa, con la flecha hacia el trago.",
                                 "El bloque «EL VIERNES CAMBIA de mood», la pastilla y la bajada bajan a la mesa libre, bajo "
                                 "la tabla. El legal no se mueve.",
                                 "Textos: sin cambios."]))
p.laminas([(A + "C3 S1 N°%d QB OCT 26.png" % i, "<b>antes (r24)</b> — N°%d" % i) for i in (1, 2, 3)],
          titulo="FEED 09-10 · Carrusel CMR — ANTES", ancho=330)
p.laminas([(N + "C3 S1 N°%d QB OCT 26.png" % i, "<b>ahora (r27)</b> — N°%d" % i) for i in (1, 2, 3)],
          titulo="FEED 09-10 · Carrusel CMR — AHORA", ancho=330,
          que="Eli: «no necesito tono oscuro cuando no hay mucho texto; baja “beneficios especiales” casi al final pero no "
              "tanto; organiza todo para que se vea cerca y armónico con el segundo slide».",
          notas=("Qué cambió", ["Menos oscuro: el velo de arriba baja del 88 % al 80 % y abajo queda casi nada; la sombra va "
                                "sólo detrás del texto de abajo, ovalada y centrada.",
                                "N°1: «Beneficios especiales para disfrutar en QB» baja hasta y=1070, a la MISMA altura que "
                                "«Sábados pagando con tu tarjeta CMR» de la N°2: al deslizar, los dos textos quedan alineados.",
                                "N°2: sombra detrás de la promo un poco más firme para que la ribs no se vea dentro del marco.",
                                "N°3: menos oscura abajo.",
                                "Textos: sin cambios."]))
p.laminas([(A + "C1 S1 N°%d QB OCT 26.png" % i, "<b>antes (r21)</b> — N°%d" % i) for i in range(1, 5)],
          titulo="FEED 05-10 · Carrusel cumpleaños — ANTES", ancho=300)
p.laminas([(N + "C1 S1 N°%d QB OCT 26.png" % i, "<b>ahora (r27)</b> — N°%d" % i) for i in range(1, 5)],
          titulo="FEED 05-10 · Carrusel cumpleaños — AHORA", ancho=300,
          que="Eli: «mejora el carrusel de cumpleaños, se ve un poco desordenado; que mejore la jerarquía y que cada slide "
              "se vea pareja en todo el carrusel; si hay muchos textos, déjalo armónico; y no tan oscuro abajo si no hay texto».",
          notas=("Qué cambió", ["Una sola grilla para la N°2, N°3 y N°4, con las mismas alturas en las tres: titular (ExtraBold "
                                "56) → línea de apoyo en itálica → dato destacado (ExtraBold 52) → detalle → pie.",
                                "Una sola voz: sólo Raleway. Sale la caligráfica de «Hay más para celebrar» en la N°3.",
                                "N°3: «Hay más para celebrar · el cumpleañero recibe:» en la línea de apoyo, «REFILL "
                                "ILIMITADO» como destacado y «de 1 trago a elección» debajo (mismas palabras).",
                                "N°4: la lista con íconos ocupa el mismo lugar que el apoyo y el destacado; el botón queda "
                                "a la altura del pie de las demás.",
                                "Abajo, donde no hay texto, el velo baja a un 20 %: se ve la foto.",
                                "N°1 (la portada de la referencia): sin cambios.",
                                "Textos: las mismas palabras; sólo cambia cómo se ordenan."]))
p.escribir()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 16 (Eli 29-09, leyendo el comentario de Constanza): aire bajo
el nombre y legal más grande y abajo en el AYCD 06-10, legal del Sunset 09-10 más
abajo y margen entre legal y lista de tragos en el AYCD 13-10.

    python scripts/qb-oct-r16-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/r16/_antes/"
N = "out/qb/oct/r16/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 16", "Aire y legales abajo",
           "29-09-2026 · 3 historias corregidas · reemplazadas en Drive", "out/qb/oct/r16/revision-r16.html",
           origen="scripts/qb-oct-r16-revision.py")
p.pedido("All You Can Drink está súper bien, pero «Tus favoritos, las veces que quieras» tiene que verse más "
         "alineado, como en las otras historias que están al lado: darle un poco de aire. Y el legal está "
         "demasiado pequeño: auméntale el tamaño, recordando lo que dijo ella, y déjalo mucho más abajo para que "
         "no destaque. Cumpleaños está súper bien. En Sunset, el legal lo dejaría más abajo. Y en la del 13-10 "
         "de All You Can Drink, deja como un margen porque se ve mucho legal y muy pesado: que esas líneas queden "
         "en dos o máximo tres líneas de párrafo.", "Eli", "29-09")


def par(archivo, titulo, que, notas, detalle=None, escala=1.2):
    p.comparar((A + archivo, "ronda 15"), (N + archivo, "ronda 16"), titulo=titulo, que=que,
               detalle=detalle, escala=escala, ancho=420, notas=("Qué cambió", notas))


par("ST06.png", "ST 06-10 · All You Can Drink  (ST n°2 S1)", "Aire bajo el nombre y el legal abajo.",
    ["«Tus favoritos, las veces que quieras» baja 12 px: del nombre a la línea hay 33 px (antes 21), el mismo aire que en Cumpleaños",
     "El legal pasa de 14 a 19 px, el tamaño del de las otras historias",
     "Va en dos líneas cortadas por frase, sin palabras sueltas, y mucho más abajo: cierra a 1660 px (antes 1560), lejos del bloque de precio"],
    detalle=(0, 380, 1080, 1700), escala=0.8)
par("ST09.png", "ST 09-10 · Sunset QB  (ST n°5 S1)", "El legal más abajo.",
    ["El legal baja 86 px y cierra a 1660 px. Mismo tamaño (19 px) y el mismo corte en dos líneas. Nada más cambió"],
    detalle=(60, 1300, 1020, 1720), escala=1.0)
par("AP-AYCD13.png", "ST 13-10 · All You Can Drink  (ST n°2 S2)", "Un margen entre el legal y la lista de tragos.",
    ["El legal queda en dos líneas de párrafo",
     "La lista de tragos bajaba pegada al legal y se leía como un solo bloque de cuatro líneas: ahora hay 32 px de margen entre los dos",
     "La lista cierra a 1577 px, dentro de la zona segura. La 27-10, que comparte el diseño, no cambió"],
    detalle=(60, 1200, 1020, 1640), escala=1.0)

p.medido([
    ("AYCD 06-10 · nombre → «Tus favoritos»", "21 → 33 px", "ok", "como Cumpleaños"),
    ("AYCD 06-10 · legal", "14 → 19 px", "ok", "2 líneas, cierra a 1660"),
    ("Sunset 09-10 · legal", "cierra 1573 → 1660", "ok", "19 px, 2 líneas"),
    ("AYCD 13-10 · legal → lista de tragos", "6 → 32 px", "ok", "la lista cierra a 1577"),
    ("Zona que cambió en cada pieza", "sólo esos textos", "ok", "diferencia píxel a píxel contra la ronda 15"),
], titulo="Lo medido (en px de 1080 × 1920)")
p.notas(["⚠️ Los legales del AYCD 06-10 y del Sunset 09-10 ahora quedan bajo el margen de paid (1580 px), aunque siguen dentro del margen de Instagram orgánico (1670). Si alguna de las dos va a paid, hay que subirlos.",
         "Cumpleaños y Banco de Chile quedan como en la ronda 15.",
         "QA de QB: 0 bloqueantes. El aviso de desenfoque del Sunset es el falso positivo conocido de esa foto.",
         "Las 3 piezas se reemplazaron en Drive con el mismo nombre (conservan el enlace). Si la vista previa muestra la versión vieja, es caché: descarga el archivo."],
        titulo="Lo demás")
p.escribir()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 11 (Eli 28-09 tarde): piscola alta en la G2 del AYCD, bloque
del Sunset más abajo con el tamaño de la r9, cumpleaños en mayúscula con recuadros
y torta nueva, el plato del pulpo restaurado y «¿Este o este?» en Bell.

    python scripts/qb-oct-r11-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/_antes-r10/"
N = "out/qb/oct/r9/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 11", "Los últimos ajustes",
           "28-09-2026 · 5 láminas corregidas · 4 aprobadas", "out/qb/oct/r9/revision-r11.html",
           origen="scripts/qb-oct-r11-revision.py")
p.pedido("La G2, creo que en la piscola el vaso es más alto. El Sunset: el tamaño estaba bien el anterior, "
         "sólo decía que lo bajaras más, que no tape ni esté cerca de las manos. En el cumpleaños, la torta tiene "
         "decoraciones extrañas; «Convierte tu cumpleaños» en mayúscula y «tu cumpleaños» abajo; los íconos en "
         "recuadros oscurecidos, estilo botones. En la del 12-10 el plato desapareció y hay una parte de arriba "
         "difuminada. Y «¿Este o este?» en Bell, igual que Medusa y Perséfone.", "Eli", "28-09")

def par(archivo, titulo, que, notas, detalle=None, escala=1.2):
    p.comparar((A + archivo, "ronda 10"), (N + archivo, "ronda 11"), titulo=titulo, que=que,
               detalle=detalle, escala=escala, ancho=420, notas=("Qué cambió", notas))

par("C1 S1 N°2 QB OCT 26.png", "FEED 07-10 · AYCD · G2", "La piscola en vaso alto.",
    ["La piscola va en un vaso alto y delgado, más alto que el schop. Lo demás, igual"])
par("C1 S2 N°2 QB OCT 26.png", "FEED 12-10 · Sunset · G2", "El tamaño de antes, todo más abajo.",
    ["Titular de vuelta al tamaño de la ronda 9, en dos líneas",
     "Todo el bloque baja, desde «El viernes» hasta el legal, y ya no toca las manos",
     "Se mantienen la pastilla redondeada verde claro a 5 px y el legal al pie"], detalle=(0, 850, 1080, 1350), escala=1.0)
par("ST n°3 S1 QB OCT 26.png", "ST 07-10 · Cumpleaños", "Torta bonita, titular en mayúscula y recuadros.",
    ["Torta nueva: blanca lisa, con perlas, cinta verde QB y unas ramitas finas arriba, sin las decoraciones raras",
     "CONVIERTE / TU CUMPLEAÑOS en Bell MT, en mayúscula y en dos líneas; «en una noche inolvidable» se queda en Raleway",
     "Cada beneficio en un recuadro oscuro, como botón, con su ícono"], detalle=(60, 300, 1020, 1100), escala=1.0)
par("ST n°1 S2 QB OCT 26.png", "ST 12-10 · Pulpo ✅", "El plato de vuelta y la mesa sin difuminar.",
    ["La limpieza de la ronda 10 había alisado el borde del plato (se fundía con la mesa) y había borroneado la veta de arriba",
     "Ahora el plato es el de la foto original, idéntico, y la mesa conserva su veta: sólo se sacaron las pintitas, las vetas anaranjadas y el nudo gris, que se tapó con madera de la misma tabla"],
    detalle=(0, 700, 1080, 1700), escala=0.8)
par("ST n°3 S4 QB OCT 26.png", "ST 28-10 · ¿Este o este?", "Titular en Bell.",
    ["«¿Este o este?» en Bell MT itálica, la misma letra de «Medusa» y «Perséfone». El signo de pregunta ya no se ve raro"],
    detalle=(100, 300, 980, 640), escala=1.2)

p.notas(["Aprobadas por ti: FEED 07-10 G1, FEED 12-10 G1, FEED 16-10 Afrodita, ST 16-10 Primavera y ST 12-10 Pulpo (con este ajuste).",
         "QA de QB: 0 bloqueantes. Los 3 avisos son falsos positivos: el desenfoque real de las fotos y, en el spritz, las plantas leídas como croma.",
         "⚠️ En el Sunset el legal quedó bajo el margen de pauta del feed (el 12 % de abajo), como pediste. Si esa pieza va a paid, hay que subirlo.",
         "Nada subido a Drive todavía: con tu visto, lo subo."], titulo="Lo demás")
p.escribir()

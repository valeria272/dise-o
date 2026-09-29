#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 18 (Eli 29-09): «haz algo similar en los otros legales de QB,
verifica que no se vean tan pequeños». Legal en UNA línea en todas las piezas de octubre,
al tamaño más grande que cabe (19 px con «Imagen referencial», 22 sin); el CMR 40 %,
que es el doble de largo, en dos líneas exactas a 21.

    python scripts/qb-oct-r18-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/r18/_antes/"
N = "out/qb/oct/r18/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 18", "Todos los legales en una línea",
           "29-09-2026 · sólo lo que está en OK PARA DISEÑAR · reemplazado en Drive", "out/qb/oct/r18/revision-r18.html",
           origen="scripts/qb-oct-r18-revision.py")
p.pedido("¿Puedes hacer algo similar en los otros legales de QB? Verifica que no se vean tan pequeños y me muestras.",
         "Eli", "29-09")

ST = (40, 1400, 1040, 1680)


def par(nombre, titulo, que, notas, detalle=ST):
    p.comparar((A + nombre + ".png", "antes"), (N + nombre + " QB OCT 26.png", "ahora"), titulo=titulo, que=que,
               detalle=detalle, escala=1.0, ancho=420, notas=("Qué cambió", notas))


L19 = "Legal en UNA línea a 19 px (con «Imagen referencial» es el tamaño más grande que cabe con 60 px de margen por lado)"
L22 = "Legal en UNA línea y más grande: de 19 a 22 px, el tamaño del CMR 08-10 que ya estaba aprobado"
par("ST n°2 S3", "ST 20-10 · AYCD llamada  (ST n°2 S3)", "Más grande y en una línea.",
    ["Estaba a 17 px, el más chico de octubre: ahora 19 px, en una línea (con «Imagen referencial» es el tamaño más grande que cabe con 60 px de margen por lado)"])
par("C1 S2 N°2", "FEED 12-10 · Carrusel Sunset · G2  (C1 S2 N°2)", "Más grande.", [L22], detalle=(40, 1100, 1040, 1350))

p.medido([
    ("Legal con «Imagen referencial» (~110 caracteres)", "19 px · 1 línea", "ok", "mide 935–945 px; columna de 960"),
    ("Legal sin «Imagen referencial» (~88 caracteres)", "22 px · 1 línea", "ok", "mide 892 px"),
    ("Zona que cambió en cada pieza", "sólo el legal", "ok", "diferencia píxel a píxel contra lo entregado"),
], titulo="Lo medido (en px de 1080 × 1920)")
p.pedido("Sólo los ajustes son a los que están OK para diseñar en la grilla.", "Eli", "29-09")
p.notas(["Grilla leída hoy: de las 14 piezas con legal, sólo estas dos están en OK PARA DISEÑAR. Las otras 12 quedan como estaban entregadas: Banco de Chile 01-10, AYCD 06-10 y el carrusel AYCD 07-10 (EN CAMBIOS / EN REVISIÓN), Sunset 09-10 (PENDIENTE POR CLIENTE) y las 8 historias repetidas de AYCD, Sunset y CMR 40 % (APROBADO).",
         "Sin cambios: el CMR 08-10 (ya estaba en una línea a 22 px), el estacionamiento 21-10 (su nota es información, no legal) y las piezas que sólo dicen «*Imagen referencial».",
         "Las dos se reemplazaron en Drive con el mismo nombre (mismo enlace)."], titulo="Lo demás")
p.escribir()

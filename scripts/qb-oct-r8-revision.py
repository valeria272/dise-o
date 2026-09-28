#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 8 (Eli 28-09): la copa real del AYCD a la altura de las
otras dos, y el ticket más chico con la tinta sólo sobre el papel.

    python scripts/qb-oct-r8-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/_antes-r7/"
N = "out/qb/oct/r4/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 8", "Pie fino en la copa y dos tickets en la mano",
           "28-09-2026 · 2 historias corregidas", "out/qb/oct/r4/revision-r8.html",
           origen="scripts/qb-oct-r8-revision.py")
p.pedido("La copa se ve un poco extraña, con la parte de abajo muy gruesa… El ticket se ve muy gigante "
         "todavía, y el OFF está muy cerca del cero, se solapan, y el porcentaje también: que se vea mucho "
         "más armónico, y que en vez de un ticket sean dos, que ella los tenga en la mano, que uno destaque… "
         "y el legal, lo de nuestro personal en otra línea, alineado a la izquierda.", "Eli", "28-09")
p.comparar((A + "ST n°2 S1 QB OCT 26.png", "ronda 7"), (N + "ST n°2 S1 QB OCT 26.png", "ronda 8"),
           titulo="ST 06-10 · All You Can Drink", que="El pie de la copa del centro, fino.",
           detalle=(360, 900, 720, 1300), ancho=420, escala=1.3,
           notas=("Qué cambió", ["El pie de la sangría pasa a ser fino como el del spritz y el espumante, sin el nudo grueso del medio",
                                  "Bowl, fruta, altura del borde y todo lo demás, igual"]))
p.comparar((A + "ST n°3 S3 QB OCT 26.png", "ronda 7"), (N + "ST n°3 S3 QB OCT 26.png", "ronda 8"),
           titulo="ST 21-10 · Estacionamiento", que="Dos tickets en la mano, más chicos, y el 50 % OFF con aire.",
           detalle=(330, 700, 860, 1400), ancho=420, escala=1.0,
           notas=("Qué cambió", ["Foto nueva: la mano sostiene dos tickets en abanico; el de adelante destaca y el de atrás asoma a la izquierda, en sombra. Cada uno con su máscara de papel: el pulgar y el de adelante quedan encima",
                                  "Conjunto al 80 %: el ticket de adelante queda en ~326 px de ancho (antes ~387)",
                                  "50 · % · OFF rediseñados: el 50 a 140, y el % y el OFF parten 14 px después del 0, sin tocarse",
                                  "Legal en dos líneas y alineado a la izquierda: «*Imagen referencial.» / «Solicita tu ticket a nuestro personal.»"]))
p.notas(["Aprobadas: 08 CMR y 09 Sunset. Sin cambios: Banco de Chile, 14, 15 y el post de cumpleaños.",
         "Nada subido a Drive todavía: con tu visto, se sube con nombre nuevo."], titulo="Lo demás")
p.escribir()

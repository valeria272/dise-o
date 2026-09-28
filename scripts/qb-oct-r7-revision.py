#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 7 (Eli 28-09): la copa real del AYCD a la altura de las
otras dos, y el ticket más chico con la tinta sólo sobre el papel.

    python scripts/qb-oct-r7-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/_antes-r6/"
N = "out/qb/oct/r4/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 7", "La copa real, nivelada, y el ticket en su lugar",
           "28-09-2026 · 2 historias corregidas · 09 Sunset aprobada",
           "out/qb/oct/r4/revision-r7.html", origen="scripts/qb-oct-r7-revision.py")
p.pedido("Realiza de nuevo la imagen del fondo, porque la copa cambió de forma; la copa del centro tiene que "
         "ser a la misma altura de las otras dos, y realista… La de estacionamiento está demasiado grande, "
         "achica un poco el ticket; la línea de puntitos sobresale de la uña, se solapa.", "Eli", "28-09")
p.comparar((A + "ST n°2 S1 QB OCT 26.png", "ronda 6"), (N + "ST n°2 S1 QB OCT 26.png", "ronda 7"),
           titulo="ST 06-10 · All You Can Drink", que="La copa del centro con su forma real y el borde a la altura de las otras dos.",
           detalle=(60, 680, 1020, 1300), ancho=420, escala=0.9,
           notas=("Qué cambió", ["Escena rehecha: la copa es la de la ronda 3 (bowl tallado, pie largo, fruta y rodaja de naranja), sin estirarla",
                                  "Agrandada pareja ~12 % para que los tres bordes queden en una línea (±3 px)",
                                  "Mismo encuadre y bloque AYCD"]))
p.comparar((A + "ST n°3 S3 QB OCT 26.png", "ronda 6"), (N + "ST n°3 S3 QB OCT 26.png", "ronda 7"),
           titulo="ST 21-10 · Estacionamiento", que="Ticket más chico y la tinta sólo sobre el papel.",
           detalle=(520, 1000, 1000, 1400), ancho=420, escala=1.2,
           notas=("Qué cambió", ["Mano y ticket al 85 %, anclados abajo a la derecha; detrás, la misma terraza desenfocada",
                                  "La tinta del ticket va dentro de una máscara del papel medida en la foto: la línea punteada pasa por debajo del pulgar, ya no se imprime sobre la uña",
                                  "El legal se corre a la izquierda para no cruzar la muñeca"]))
p.notas(["Aprobadas: 08 CMR y 09 Sunset. Sin cambios: Banco de Chile, 14, 15 y el post de cumpleaños.",
         "Nada subido a Drive todavía: con tu visto, se sube con nombre nuevo."], titulo="Lo demás")
p.escribir()

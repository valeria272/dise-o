#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 15 (Constanza, jefa de diseño, comentarios en la grilla 29-09):
misma separación logo→titular en Banco de Chile, AYCD y Cumpleaños; bullets del
cumpleaños más cortos; y sin palabras solas en los legales (Sunset 09-10 y, por el
mismo criterio, Banco de Chile, AYCD 13-10 y la G2 del carrusel AYCD 07-10).

    python scripts/qb-oct-r15-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/r15/_antes/"
N = "out/qb/oct/r15/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 15", "Los comentarios de Constanza",
           "29-09-2026 · 6 piezas corregidas · reemplazadas en Drive", "out/qb/oct/r15/revision-r15.html",
           origen="scripts/qb-oct-r15-revision.py")
p.pedido("En estas 3 historias de Banco de Chile, All You Can Drink y la de cumpleaños, ojo con la separación "
         "del título de historia con el logo. Mantengamos a todas la misma separación. Y en cuanto a la historia "
         "de cumpleaños me encanta, pero creo que los bullets de los beneficios están muuuy largos, que sean un "
         "poco más cortos, manda el primer beneficio porque es el más largo, pero déjale un poco menos de aire "
         "al fin de la frase.", "Constanza Lizana (comentario en la grilla, ST 06-10)", "29-09")
p.pedido("Aquí en la letra chica, se ve raro con la palabra beneficios solita abajo, porfis no debemos palabras "
         "solitas.", "Constanza Lizana (comentario en la grilla, ST 09-10)", "29-09")


def par(antes, ahora, titulo, que, notas, detalle=None, escala=1.2):
    p.comparar((A + antes, "antes"), (N + ahora, "ahora"), titulo=titulo, que=que,
               detalle=detalle, escala=escala, ancho=420, notas=("Qué cambió", notas))


par("ST01.png", "ST n°1 S1 QB OCT 26.png", "ST 01-10 · Banco de Chile  (ST n°1 S1)",
    "Misma separación logo→titular que el AYCD, y el legal sin palabras colgando.",
    ["Del logo a la pastilla «Banco de Chile» había 43 px; ahora hay 53, igual que en el AYCD",
     "El logo no se movió (ya está en el borde de la zona segura): bajó 10 px el bloque de abajo (marco, pastilla, titular y cajas)",
     "El legal dejaba «ofertas y beneficios.» colgando: ahora se corta por frase en dos líneas parejas. El legal y las tarjetas no se movieron"],
    detalle=(60, 200, 1020, 1060), escala=1.0)
par("ST06.png", "ST06.png", "ST 06-10 · All You Can Drink  (ST n°2 S1) · sin cambios",
    "Es la medida que manda: 53 px del logo a ALL YOU CAN DRINK.",
    ["No se tocó. El logo y el nombre son el bloque cerrado del KV (Eli, 17-09), así que su separación es la que se copió en las otras dos"],
    detalle=(60, 200, 1020, 700), escala=1.0)
par("ST07.png", "ST n°3 S1 QB OCT 26.png", "ST 07-10 · Cumpleaños  (ST n°3 S1)",
    "Misma separación logo→titular y recuadros más cortos.",
    ["Del logo a CONVIERTE había 36 px; ahora hay 53, igual que en el AYCD. El logo queda donde estaba y el texto baja 16,5 px",
     "Los cinco recuadros ahora miden lo que mide el primer beneficio, que es el más largo, y cierran con el mismo aire con que abren (26 px por lado). Antes sobraban ~125 px al final de la frase",
     "Los recuadros quedan centrados; la torta, la foto y «Imagen referencial» no cambiaron"],
    detalle=(60, 220, 1020, 1060), escala=1.0)
par("ST09.png", "ST n°5 S1 QB OCT 26.png", "ST 09-10 · Sunset QB  (ST n°5 S1)",
    "La palabra «beneficios» ya no queda sola.",
    ["El legal se corta por frase: «*Imagen referencial. *Sujeto a consumo de alimentos.» / «*Promoción no acumulable con otras ofertas y beneficios.»",
     "Mismo tamaño (19 px) y mismo lugar, dentro de la zona segura. Nada más cambió"],
    detalle=(80, 1380, 1000, 1620), escala=1.1)
par("AP-AYCD13.png", "ST n°2 S2 QB OCT 26.png", "ST 13-10 · AYCD aprobada  (ST n°2 S2) · mismo criterio",
    "Tenía la misma viuda: «beneficios.» sola.",
    ["No estaba en el comentario, pero Constanza lo dijo como regla («no debemos palabras solitas») y revisé los legales de todo octubre",
     "Al llevar «Imagen referencial» el legal se alargaba y dejaba «beneficios.» sola: ahora va cortado por frase, igual que el Sunset"],
    detalle=(80, 1300, 1000, 1600), escala=1.1)
par("FEED07-G2.png", "C1 S1 N°2 QB OCT 26.png", "FEED 07-10 · Carrusel AYCD · G2  (C1 S1 N°2) · mismo criterio",
    "Tenía la misma viuda: «beneficios.» sola.",
    ["Mismo arreglo: el legal se corta por frase en dos líneas. Nada más cambió en la lámina"],
    detalle=(80, 950, 1000, 1250), escala=1.1)

p.medido([
    ("Logo → primer elemento · Banco de Chile", "43 → 53 px", "ok", "a la pastilla del banco"),
    ("Logo → primer elemento · AYCD", "53 px", "ok", "la medida que manda (bloque del KV)"),
    ("Logo → primer elemento · Cumpleaños", "36 → 53 px", "ok", "a CONVIERTE"),
    ("Tope del logo en las tres", "≈ 251 px", "ok", "no se movió: está en la zona segura (≥ 250)"),
    ("Zona que cambió · Sunset, AYCD 13-10 y G2", "sólo el legal", "ok", "diferencia píxel a píxel contra lo entregado"),
], titulo="Lo medido (en px de 1080 × 1920)")
p.notas(["Revisé los legales de todas las promos de octubre (13 piezas). Sólo esas cuatro tenían palabras solas; las de CMR, Sunset aprobadas y el carrusel Sunset ya cortaban bien.",
         "El tamaño del logo no es igual en las tres (Banco 168, AYCD 179, Cumpleaños 160 px de ancho). Constanza no lo pidió y no se tocó; si quieres que también lo igualemos, es un cambio de 5 minutos.",
         "QA de QB: 0 bloqueantes. Los 2 avisos de desenfoque son los falsos positivos conocidos de esas fotos.",
         "Las 5 piezas corregidas se reemplazaron en Drive con el mismo nombre (conservan el enlace). Si la vista previa muestra la versión vieja, es caché: descarga el archivo."],
        titulo="Lo demás")
p.escribir()

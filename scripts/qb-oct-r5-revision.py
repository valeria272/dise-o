#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 5 (Eli 28-09, sobre la ronda 4): sangría real en el AYCD,
terraza real en el Sunset, barra real y curva sin tocar el 20 en CMR, y el ticket
de estacionamiento como la imagen que mandó Eli.

    python scripts/qb-oct-r5-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/_antes-r4/"
N = "out/qb/oct/r4/"

p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 5",
           "Material real de QB donde lo pediste",
           "28-09-2026 · 4 historias corregidas · Banco de Chile, 14 y 15 sin cambios",
           "out/qb/oct/r4/revision-r5.html", origen="scripts/qb-oct-r5-revision.py")

p.pedido("La historia del All You Can Drink me parece muy bien, sin embargo el cóctel del centro, "
         "la sangría, tiene que ser igual a la real de QB… Para la del Sunset, lo que no me gusta es "
         "que se vea una playa al fondo… tiene que ser con la terraza real que tenemos en QB… la ST de "
         "CMR Falabella me gusta, sin embargo quiero que sea una foto real de barra… y el «todos los "
         "días» solapa un poco el 2 del 20… te adjunté cómo es acá el ticket.", "Eli", "28-09")

def par(titulo, nombre, que, notas):
    p.comparar((A + nombre, "ronda 4"), (N + nombre, "ronda 5"), titulo=titulo, que=que,
               ancho=420, notas=("Qué cambió", notas))

par("ST 06-10 · All You Can Drink", "ST n°2 S1 QB OCT 26.png",
    "La sangría del centro ahora es la real, la de la ronda 3.",
    ["Misma escena (campana, guante, cortina, mármol); sólo cambia la copa del centro por la sangría de la ronda 3: copa tallada, cubos de fruta y rodaja de naranja",
     "Encuadre igual al de la ronda 4: la campana cruza el titular y los tragos terminan sobre «TODOS LOS MARTES»"])

par("ST 09-10 · Sunset QB", "ST n°5 S1 QB OCT 26.png",
    "Sin playa: la terraza de QB.",
    ["Fondo rehecho sobre la terraza real («QB 13 oct-31»): pérgola, plantas, maceteros de concreto y la ciudad detrás del vidrio",
     "Mesa de listones como la de QB («QB 13 oct-56»)",
     "El trago, el plato, el rótulo con flecha, el titular y el logo Sunset QB, sin cambios"])

par("ST 08-10 · CMR Falabella", "ST n°4 S1 QB OCT 26.png",
    "Foto real de barra y la curva ya no toca el 2.",
    ["Foto REAL: la barra iluminada con el cóctel naranjo y romero (sesión terraza 10-10, «QB oct-31»), asomando arriba a la izquierda como en la aprobada",
     "«¡Todos los días!» sube 14 px: queda aire entre el ¡ y el 2",
     "Como la foto es real, el legal ya no dice «Imagen referencial»"],
)
p.comparar((A + "ST n°4 S1 QB OCT 26.png", "ronda 4"), (N + "ST n°4 S1 QB OCT 26.png", "ronda 5"),
           titulo="CMR · el ¡ y el 2, de cerca", detalle=(250, 700, 850, 1000), ancho=420, escala=1.2)

p.opciones([("raw/hilton/qb/ref-oct/R-21-ticket-eli-28sep.png", "<b>TU IMAGEN</b>"),
            (A + "ST n°3 S3 QB OCT 26.png", "<b>ANTES</b> — ronda 4"),
            (N + "ST n°3 S3 QB OCT 26.png", "<b>AHORA</b> — ronda 5")],
           titulo="ST 21-10 · Estacionamiento", ancho=300, elige=False,
           que="Armada como la imagen que mandaste.",
           notas=("Qué cambió", [
               "Foto: «Muhammara siria 1» de la sesión de platos de la carta, la misma de tu imagen, extendida hacia arriba para el 9:16 → «Imagen referencial»",
               "Dos tickets sobre la mesa como los tuyos: flechas, código de barras, la P, TICKET / ESTACIONAMIENTO y el 50 % con el OFF apilado; abajo «Ingreso por Encomenderos 275»",
               "En tu imagen los tickets van debajo del plato, pero ahí caen en los 340 px de abajo que tapa Instagram: los dejé un poco más chicos y arriba, pisando sólo el borde del plato. Si prefieres que bajen, se bajan"]))

p.medido([
    ("QA de QB sobre las 4", "0 bloqueantes", "ok", "3 avisos: franja superior que el velo lleva a negro (09, 21) y el chip verde de CMR leído como croma (08)"),
    ("Formato", "2250 × 4000", "ok", "el de las entregadas"),
], titulo="Lo medido")

p.notas(["Sin cambios, como dijiste: Banco de Chile, 14 Adivina y 15 Mejores amigos (esta la ibas a revisar mejor), y el post de cumpleaños del 05-10.",
         "Nada subido a Drive todavía."], titulo="Lo demás")

p.escribir()

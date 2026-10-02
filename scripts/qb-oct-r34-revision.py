#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 34 (Eli 02-10): POST + ST «20 % dcto. almuerzo» — más impacto,
«cualquier tarjeta» destacado, foto del brindis y el descuento como bloque.

    python scripts/qb-oct-r34-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r33/", "out/qb/oct/r34/"
POST, ST = "Post S1 QB OCT 26 - 20 ALMUERZO.png", "ST S1 QB OCT 26 - 20 ALMUERZO.png"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 34", "Post + historia — 20 % dcto. en tu almuerzo, con cualquier tarjeta",
           "02-10-2026 · FEED col. D de la S1 (EN REVISIÓN en la grilla) · sin subir a Drive todavía",
           N + "revision-r34.html", origen="scripts/qb-oct-r34-revision.py")
p.pedido("La idea es destacar que cualquier tarjeta, y por favor quiero que impacte más (que no se parezca al del menú del chef). "
         "Por favor usa una foto del shooting que sea más instagram y bonita. El descuento que mejore la diagramación", "Eli", "02-10-2026")
p.comparar((A + POST, "r33: cenital de risotto sobre la mesa negra"), (N + POST, "r34: el brindis de vino blanco"),
           titulo="POST 4:5  ·  2250×2812", ancho=420,
           notas=("Qué cambió", ["<b>Foto:</b> el brindis de vino blanco sobre la mesa de almuerzo, con el follaje detrás (shooting de la carta, enero 2026; real, sin IA). Abajo asoma el risotto.",
                                 "<b>Cualquier tarjeta:</b> pasa a la franja verde de marca, en negrita, pegada a la cifra: «PAGANDO CON <b>CUALQUIER TARJETA BANCARIA</b>».",
                                 "<b>El descuento:</b> ahora es un bloque cerrado — «20» grande, el «%» arriba y «dcto.» debajo del «%», calzados al alto de la cifra.",
                                 "<b>Titular:</b> en una línea y dos pesos, para que mande la cifra.",
                                 "<b>CTA:</b> deja de ser botón (habría dos verdes): va en versales sobre el legal.",
                                 "<b>Textos:</b> los mismos del brief. Lo único que cambia es que «Pagando con cualquier tarjeta bancaria» va en mayúsculas."]))
p.comparar((A + ST, "r33: cenital de trucha"), (N + ST, "r34: el mismo brindis, con más aire arriba"),
           titulo="HISTORIA 9:16  ·  2250×4000", ancho=340,
           notas=("Qué cambió", ["Lo mismo que el post. Logo en 250, legal al pie; el follaje se alargó hacia arriba con el mismo follaje para dar sitio al bloque.",
                                 "Textos: sin cambios respecto del post."]))
p.opciones([("raw/hilton/qb/kv-chef/Post n°1 S4 JUL CHEF QB.jpg", "KV «Recomendación del chef» (lo que NO debe parecer)"),
            (N + POST, "r34")], titulo="Contra el del chef", ancho=380, elige=False,
           que="El del chef es un plato oscuro con una pila de textos y un botón blanco. Acá hay manos y copas, una cifra que manda y una sola franja verde.")
p.notas(["<b>Los platos</b> quedan abajo y en penumbra (el risotto se ve detrás del CTA). Si quieres que la comida pese más, hay otra toma del mismo brindis con el risotto y la trucha grandes («batayaki 19»), pero ahí las copas ocupan casi todo el cuadro y el texto las pisa.",
         "<b>El legal</b> cae sobre el plato de abajo, como en tu KV de CMR.",
         "<b>Drive:</b> sigue sin subir (la celda está EN REVISIÓN). Con tu visto lo dejo en S1 / QB / FEED y STS.",
         "QA de QB con textos: las 9 reglas pasan en las dos piezas."], titulo="Dudas y notas")
p.escribir()

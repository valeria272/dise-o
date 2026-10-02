#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 37 (Eli 02-10): POST + ST «20 % dcto. almuerzo» — la cifra como en
la referencia SUPER SALE: «20» enorme en serif y «DCTO. %» girado al costado.

    python scripts/qb-oct-r37-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N, R = "out/qb/oct/r36/", "out/qb/oct/r37/", "raw/hilton/qb/oct-r33/"
POST, ST = "Post S1 QB OCT 26 - 20 ALMUERZO.png", "ST S1 QB OCT 26 - 20 ALMUERZO.png"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 37", "Post + historia — el 20 % como en la referencia",
           "02-10-2026 · FEED col. D de la S1 (EN REVISIÓN en la grilla) · sin subir a Drive todavía",
           N + "revision-r37.html", origen="scripts/qb-oct-r37-revision.py")
p.pedido("Intentemos el 20 % así, a ver si se ve más atractivo", "Eli (con la referencia SUPER SALE · 50 % OFF)", "02-10-2026")
p.opciones([(R + "ref-eli-super-sale.png", "Tu referencia"), (N + POST, "r37 · post"), (N + ST, "r37 · historia")],
           titulo="La referencia y las dos piezas", ancho=360, elige=False,
           que="De la referencia: la cifra enorme en una serif alta y de mucho contraste, y «% OFF» girado en vertical al costado, "
               "del alto de la cifra. Acá: «20» + «DCTO. %» girado.")
p.comparar((A + POST, "r36: cifra en Raleway con «%» y «dcto.» apilados"), (N + POST, "r37: «20» en serif + «DCTO. %» vertical"),
           titulo="POST 4:5  ·  2250×2812", ancho=420,
           notas=("Qué cambió", ["<b>La cifra:</b> «20» en serif, de 192 a 272 px de alto; «DCTO. %» va girado al costado, del alto exacto de la cifra.",
                                 "La foto bajó un poco para darle sitio a la cifra; el plato, la copa y el cuchillo siguen completos.",
                                 "Todo lo demás (titular, tarjeta, horario, botón, legal) queda igual que en la r36.",
                                 "<b>Textos:</b> sin cambios; «dcto.» pasó a mayúsculas («DCTO.») porque va girado."]))
p.comparar((A + ST, "r36"), (N + ST, "r37"), titulo="HISTORIA 9:16  ·  2250×4000  ·  márgenes de paid", ancho=340,
           notas=("Qué cambió", ["Lo mismo que el post. El texto sigue entre 250 y 1580."]))
p.opciones([(R + "_bell.png", "Así son los números de Bell MT (arriba la normal, abajo la itálica)")],
           titulo="⚠️ La tipografía de la cifra — necesito tu decisión", ancho=620, elige=False,
           que="La serif de QB es Bell MT, pero sus números son bajos y con rulo: no dan el efecto de la referencia. "
               "Para esta prueba usé <b>Bodoni Moda</b> (libre, estilo Didot, la más parecida a la referencia), que <b>no es una fuente de QB</b>. "
               "Si te gusta el resultado, tú decides si entra para esta pieza o si prefieres otra serif que ya tengas en tus editables.")
p.notas(["QA de QB con textos: las 9 reglas pasan en las dos piezas.",
         "Drive: sigue sin subir (la celda está EN REVISIÓN y falta tu decisión sobre la serif)."], titulo="Notas")
p.escribir()

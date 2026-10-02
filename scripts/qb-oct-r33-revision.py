#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 33 (Eli 02-10): POST + ST «20 % dcto. almuerzo» — FEED col. D, S1.
Pieza nueva: no hay «antes». Se muestra la referencia del brief junto a las dos piezas.

    python scripts/qb-oct-r33-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

N = "out/qb/oct/r33/"
POST, ST = N + "Post S1 QB OCT 26 - 20 ALMUERZO.png", N + "ST S1 QB OCT 26 - 20 ALMUERZO.png"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 33", "Post + historia — 20 % dcto. en tu almuerzo",
           "02-10-2026 · FEED col. D de la S1 (EN REVISIÓN en la grilla) · pieza nueva, sin subir a Drive todavía",
           N + "revision-r33.html", origen="scripts/qb-oct-r33-revision.py")
p.pedido("Diseña el post del 20 % que es de la S1 · ten en cuenta el comentario de Scar así tenemos el diseño antes", "Eli", "02-10-2026")
p.pedido("( Tiene que ser ST Y POST )", "Scarlette · celda REFERENCIA de la grilla", "01-10-2026")
p.pedido("Te dejo el 20% con cualquier tarjeta bancaria (no efectivo)", "Nicolás → Scarlette · hilo en FEED!D11", "01-10-2026")
p.opciones([("raw/hilton/qb/oct-r33/ref-20-almuerzo-pin.jpg", "Referencia del brief (pin «Menú Ejecutivo»)"),
            (POST, "POST 4:5 · 2250×2812 · risotto de camarones"),
            (ST, "HISTORIA 9:16 · 2250×4000 · trucha arcoíris")],
           titulo="La referencia y las dos piezas", ancho=380, elige=False,
           que="De la referencia se tomó la toma cenital, el texto sobre la mesa limpia y el plato abajo; "
               "y la jerarquía: una cifra enorme con líneas livianas debajo. Con la gramática de QB: centrado, "
               "logo arriba, titular en dos pesos y el botón verde.")
p.notas(["<b>Texto principal:</b> TU PAUSA DE ALMUERZO / AHORA TIENE / 20% dcto. — literal del brief. «dcto.» va en minúscula, como en los KV de bancos.",
         "<b>Bajada:</b> De lunes a viernes · 12:30 a 16:00 hrs · Pagando con cualquier tarjeta bancaria — literal, <b>sin los puntos finales</b> (regla del cliente: ni títulos ni bajadas llevan punto).",
         "<b>CTA (botón):</b> ARMA TU ALMUERZO Y RESERVA AHORA — literal.",
         "<b>Legal:</b> literal y con sus puntos, en tres líneas cortadas por frase (sin palabras solas), a 19 px en el post y 20 px en la historia. Incluye «No válido para pagos en efectivo» (el hilo de Nicolás).",
         "Sin logos de banco, tarjetas ni marco: el brief pide que no parezca comunicación bancaria."],
        titulo="Los textos — qué va y de dónde sale")
p.notas(["<b>Fotos reales, sin IA</b> y sin «Imagen referencial»: shooting de la carta de enero 2026 — «Risotto de camarones al azafrán 3» (post) y «Trucha arcoíris 4» (historia). No repiten lo de la semana (ostiones del KV de CMR, ribs, pollo, papas).",
         "A las dos fotos se les <b>borró el salero</b>, que caía detrás del texto, y la mesa se alargó hacia arriba con la misma mesa para dejar el aire del bloque. El plato, la copa y los cubiertos no se tocaron.",
         "Una sola tipografía (Raleway), cifras de caja alta, un solo elemento verde (el botón, al ancho de su texto).",
         "Historia: logo en 250, titular 53 px bajo el logo, legal al pie (≈1722–1800). Post: todo el bloque sobre la mesa; el legal al pie, como en el KV de CMR.",
         "QA de QB con textos: las 9 reglas pasan en las dos piezas, sin avisos."],
        titulo="Cómo está hecho")
p.notas(["<b>Luz de día:</b> el brief pide una escena «luminosa». Las tomas cenitales del shooting son sobre la mesa negra; elegí éstas porque son las que dejan la mesa limpia para el texto, como la referencia. Si la prefieres más de día, la alternativa real es la mesa de madera (entraña + copa de tinto), pero ahí el texto queda sobre la veta y la copa.",
         "<b>El legal</b> cae sobre el borde de abajo del plato (en la historia, sobre la punta de la trucha). Si molesta, la foto puede subir un poco y dejar menos plato.",
         "<b>Drive:</b> no lo subí porque la celda está EN REVISIÓN. Con tu visto lo dejo en S1 / QB / FEED y STS, con el número que le toque según la grilla (va entre el Sunset del 01-10 y el CMR del 02-10)."],
        titulo="Dudas para ti")
p.escribir()

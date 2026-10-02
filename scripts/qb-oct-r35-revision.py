#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 35 (Eli 02-10): POST + ST «20 % dcto. almuerzo» — más jerarquía en
el titular y el descuento, el grupo de tarjeta + horario + botón + legal abajo, ST para paid.

    python scripts/qb-oct-r35-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r34/", "out/qb/oct/r35/"
POST, ST = "Post S1 QB OCT 26 - 20 ALMUERZO.png", "ST S1 QB OCT 26 - 20 ALMUERZO.png"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 35", "Post + historia — 20 % dcto. en tu almuerzo",
           "02-10-2026 · FEED col. D de la S1 (EN REVISIÓN en la grilla) · sin subir a Drive todavía",
           N + "revision-r35.html", origen="scripts/qb-oct-r35-revision.py")
p.pedido("Al veinte por ciento de descuento le falta más jerarquía. El porcentaje se ve muy extraño, que se vea mejor compensado. "
         "Necesito que el título principal con el descuento sea más grande y el pagando con cualquier tarjeta bancaria baje hasta donde "
         "dice arma tu almuerzo y reserva ahora, ya que ese es el verdadero botón. «Tarjeta bancaria» abajo de «pagando con cualquier», "
         "y abajo «de lunes…»; eso más abajo, en conjunto con los legales. Los legales se ven difuminados en esa parte. Hay muchos textos: "
         "el legal, ajústalo; lo mismo para la story. Y van a ser para paid también: ajusta la ST a eso.", "Eli", "02-10-2026")
p.comparar((A + POST, "r34"), (N + POST, "r35"), titulo="POST 4:5  ·  2250×2812", ancho=420,
           notas=("Qué cambió", ["<b>Arriba quedan sólo el titular y el descuento</b>, más grandes: titular en dos líneas (48 px en vez de 34) y la cifra a 290 (antes 236).",
                                 "<b>El porcentaje, compensado:</b> el «%» creció y ahora mide el mismo ancho que «dcto.», y entre los dos calzan el alto del «20». Antes «dcto.» era más ancho que el «%» y el bloque quedaba cojo.",
                                 "<b>Abajo, un solo grupo:</b> PAGANDO CON CUALQUIER / TARJETA BANCARIA (en dos líneas) → De lunes a viernes · 12:30 a 16:00 hrs → el botón verde con el CTA → el legal.",
                                 "<b>El botón verde vuelve a ser el CTA</b> «ARMA TU ALMUERZO Y RESERVA AHORA»; la franja verde de «cualquier tarjeta» se fue.",
                                 "<b>Legal:</b> de tres líneas a dos, cortadas por frase, sobre una base oscura limpia (ya no hay un plato a medio ver detrás).",
                                 "<b>Textos:</b> las mismas palabras; sólo cambió el orden y el corte de líneas."]))
p.comparar((A + ST, "r34"), (N + ST, "r35 · con márgenes de paid"), titulo="HISTORIA 9:16  ·  2250×4000", ancho=340,
           notas=("Qué cambió", ["Lo mismo que el post.",
                                 "<b>Paid:</b> todo el texto queda entre 250 y 1580 (el legal cierra en ≈1575) y dentro de la columna central, lejos de los 115 px de la derecha. Antes el CTA y el legal estaban al pie (1664–1800), dentro de la zona que Instagram tapa.",
                                 "Los 340 px de abajo quedan sin texto: ahí se ve el plato de trucha.",
                                 "El legal va en tres líneas (en dos no cabe a 19 px dentro de la columna de paid)."]))
p.notas(["QA de QB con textos: el post pasa las 9 reglas; en la historia queda el mismo aviso de la ronda anterior (la franja de más arriba, sobre el logo y sin texto, es follaje alargado y oscuro).",
         "El legal del post va a 17,5 px para caber en dos líneas; si lo prefieres a 19 px, vuelve a tres líneas.",
         "Drive: sigue sin subir (la celda está EN REVISIÓN). Con tu visto lo dejo en S1 / QB / FEED y STS."], titulo="Notas")
p.escribir()

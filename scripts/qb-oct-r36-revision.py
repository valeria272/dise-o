#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 36 (Eli 02-10): POST + ST «20 % dcto. almuerzo» — que el plato y el
vino destaquen, «ahora tiene» más grande, tamaños escalonados y botón corto.

    python scripts/qb-oct-r36-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r35/", "out/qb/oct/r36/"
POST, ST = "Post S1 QB OCT 26 - 20 ALMUERZO.png", "ST S1 QB OCT 26 - 20 ALMUERZO.png"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 36", "Post + historia — 20 % dcto. en tu almuerzo",
           "02-10-2026 · FEED col. D de la S1 (EN REVISIÓN en la grilla) · sin subir a Drive todavía",
           N + "revision-r36.html", origen="scripts/qb-oct-r36-revision.py")
p.pedido("Está demasiado oscuro la parte de abajo, ya que no se ve el plato. La idea es que el almuerzo con el vino destaquen, y además "
         "tiene que ser una imagen atractiva. El «ahora tiene» puede crecer un poco, para que esté en conjunto con el 20 %. A «pagando con "
         "cualquier tarjeta bancaria» le sumaría un punto. Aquí existen tamaños: el título más grande con el 20 %, y lo demás va escalando "
         "hacia abajo hasta que lo más chiquito sea el legal. El botón me parece bastante bien, pero es un poco largo: arriba o al lado "
         "puede decir «arma tu almuerzo», y «reserva ahora» sería el botón.", "Eli", "02-10-2026")
p.comparar((A + POST, "r35: el brindis, con los platos tapados abajo"), (N + POST, "r36: entraña y copa de tinto sobre la mesa de madera"),
           titulo="POST 4:5  ·  2250×2812", ancho=420,
           notas=("Qué cambió", ["<b>Foto:</b> entraña con copa de tinto sobre la mesa de madera (shooting de la carta, enero 2026; real, sin IA). Es una toma horizontal, así que la copa, el plato y el cuchillo entran completos <b>entre</b> el bloque de arriba y el grupo de abajo: ya no hay plato debajo del texto.",
                                 "<b>«AHORA TIENE»</b> creció (de 48 a 60 px) y ahora es más grande que la primera línea: se lee pegado al 20 %.",
                                 "<b>«PAGANDO CON CUALQUIER / TARJETA BANCARIA»</b> subió de 32 a 36 px.",
                                 "<b>Tamaños escalonados:</b> titular 46/60 y cifra → tarjeta 36 → horario 28 → CTA 23 → legal 17,5.",
                                 "<b>Botón corto:</b> «ARMA TU ALMUERZO Y» va como texto y al lado el botón verde «RESERVA AHORA».",
                                 "<b>Textos:</b> las mismas palabras del brief."]))
p.comparar((A + ST, "r35"), (N + ST, "r36"), titulo="HISTORIA 9:16  ·  2250×4000  ·  márgenes de paid", ancho=340,
           notas=("Qué cambió", ["Lo mismo que el post, con la misma foto.",
                                 "Todo el texto sigue entre 250 y 1580 y dentro de la columna central (paid).",
                                 "Los 340 px de abajo quedan en negro, sin texto: la foto es horizontal y la mesa se pierde en sombra ahí. Es la zona que Instagram tapa."]))
p.notas(["La mesa no se alargó hacia abajo: probé continuarla con su propia madera y los listones quedaban en zigzag. Por eso se funde a sombra bajo el grupo de texto.",
         "Si prefieres vino blanco o dos platos, hay otra horizontal real: palta rellena + tiradito con spritz y copa de blanco, sobre la mesa negra con el biombo de mimbre.",
         "Drive: sigue sin subir (la celda está EN REVISIÓN). Con tu visto lo dejo en S1 / QB / FEED y STS."], titulo="Notas")
p.escribir()

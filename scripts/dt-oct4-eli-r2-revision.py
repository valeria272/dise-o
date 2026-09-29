#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · octubre · ronda de Eli sobre la ronda de Constanza (29-09) — antes y después."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/oct4-constanza"
A, D, O = f"{R}/r1", f"{R}/despues", f"{R}/antes"
p = Pagina("dt", "DOUBLETREE · OCTUBRE · RONDA 2 (ELI)",
           "Títulos más arriba y feriados legibles",
           "29-09-2026 · tus correcciones sobre la ronda de Constanza · 6 piezas",
           f"{R}/revision-r2.html", origen="scripts/dt-oct4-eli-r2-revision.py")

p.pedido("Yo subiría el «Días más largos» y las demás, según lo que ella dice, pero un poco más arriba, porque después "
         "tapa a la familia «el momento exacto para una escapada en familia». Lo ideal sería que los subas todos",
         "Eli", "29-09",
         que="<b>Qué cambió:</b> se mantiene la regla de Constanza (todas a la MISMA distancia del logo), pero esa "
             "distancia es 48 px más corta: la mayúscula del título pasa de y = 488 a <b>y = 440</b> en todas las "
             "historias. Como es una sola regla en el código, subieron juntas la Family Time (los dos textos), "
             "las 3 feriado, Servicios y Honors.")
p.comparar((f"{A}/ft-2.png", "ronda 1 · el texto 2 tapaba la cabeza de la familia"),
           (f"{D}/ft-2.png", "ahora · 48 px más arriba, la familia despejada"),
           titulo="ST 01-10 Family Time · «¡El momento exacto…!»")
p.comparar((f"{A}/ft-1.png", "ronda 1"), (f"{D}/ft-1.png", "ahora · «Días más largos» a la misma altura que el texto 2"),
           titulo="ST 01-10 Family Time · «Días más largos, clima perfecto»")

p.pedido("Para la ST del 30-10 de Hilton Honors, la verdad creo que quedó exactamente igual. No sé qué es lo que cambió",
         "Eli", "29-09",
         que="<b>Tenías razón en que se notaba poco:</b> en la ronda 1 el título sólo subió 30 px (de 518 a 488) y la "
             "interlínea bajó de 1,10 a 1,06, así que a tamaño de celular casi no se veía. Con la altura nueva sube "
             "<b>78 px en total</b> respecto de la original y ahora sí se nota. Abajo están las tres versiones.")
p.opciones([(f"{O}/DT ST 30-10 Hilton Honors beneficios.png", "original · versal en 518"),
            (f"{A}/DT ST 30-10 Hilton Honors beneficios.png", "ronda 1 · 488"),
            (f"{D}/DT ST 30-10 Hilton Honors beneficios.png", "ahora · 440")],
           titulo="ST 30-10 Hilton Honors · las tres versiones")
p.comparar((f"{A}/DT ST 13-10 Servicios del hotel.png", "ronda 1"), (f"{D}/DT ST 13-10 Servicios del hotel.png", "ahora"),
           titulo="ST 13-10 Servicios del hotel")

p.pedido("La flechita que está abajo de «para cada uno» no se ve, podrías dejarla en algún recuadro. Y el «IVA incluido, "
         "válido…» más abajo, con un recuadrito o algún fondo para que se pueda notar, porque no se lee", "Eli", "29-09",
         que="<b>Qué cambió:</b> la flecha va dentro de un <b>círculo blanco</b> con la flecha en azul DT. El legal "
             "bajó (queda justo sobre la zona segura) y va en una <b>píldora azul DT</b> con el texto blanco.")
p.comparar((f"{A}/DT ST 05-10 Feriado ER y FT.png", "ronda 1"), (f"{D}/DT ST 05-10 Feriado ER y FT.png", "ahora"),
           titulo="ST 05-10 · ¿Fin de semana largo?")
p.comparar((f"{A}/DT ST 05-10 Feriado ER y FT.png", "ronda 1"), (f"{D}/DT ST 05-10 Feriado ER y FT.png", "ahora"),
           titulo="La flecha y el legal, de cerca", detalle=(0, 560, 1080, 1600))

p.pedido("En «escápate en pareja» me incomoda mucho que salga del recuadro ese texto. Que quede alineado; lo mismo "
         "para la última ST de Family Time", "Eli", "29-09",
         que="<b>Qué cambió:</b> el título ya no parte en el canto del recuadro. Ahora se alinea con el <b>texto de "
             "adentro</b> (precio, «IVA incluido», píldoras): todo arranca en la misma vertical. En la de Family Time "
             "se igualó el margen interior del recuadro para que la línea sea la misma en las dos.")
p.comparar((f"{A}/DT ST 05-10 Feriado Escapada Romantica.png", "ronda 1 · el título salía del recuadro"),
           (f"{D}/DT ST 05-10 Feriado Escapada Romantica.png", "ahora · alineado con el texto de adentro"),
           titulo="ST 05-10 · Escápate en pareja", detalle=(60, 380, 760, 1100))
p.comparar((f"{A}/DT ST 05-10 Feriado Family Time.png", "ronda 1"),
           (f"{D}/DT ST 05-10 Feriado Family Time.png", "ahora · alineado con el texto de adentro"),
           titulo="ST 05-10 · Fin de semana largo en familia")

p.notas([
    "Todo lo de Constanza se mantiene: sin letras separadas, incluye en Stag y todas las historias con el título a la "
    "misma distancia del logo (ahora más corta).",
    "<b>En Drive (reemplazadas, md5 verificado):</b> S1/STS Family Time MP4 + GIF · S2/STS las 3 feriado · "
    "S3/STS Servicios · S5/STS Honors.",
    "Sigue pendiente de la ronda anterior: <b>Coworking</b> no está subido (Constanza no lo comentó) y la "
    "interlínea de la portada del carrusel quedó en 1,16, entre tu 1,3 y lo que pidió ella.",
])
p.escribir()

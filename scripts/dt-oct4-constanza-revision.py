#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · octubre · ronda de Constanza Lizana (jefa de diseño), 29-09 — antes y después."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/oct4-constanza"
A, D = f"{R}/antes", f"{R}/despues"
p = Pagina("dt", "DOUBLETREE · OCTUBRE · RONDA DE CONSTANZA",
           "Tipografía y títulos de octubre",
           "29-09-2026 · 4 comentarios de Constanza Lizana en la grilla DT · 7 piezas corregidas",
           f"{R}/revision.html", origen="scripts/dt-oct4-constanza-revision.py")

# ── 1 · la regla de los títulos ────────────────────────────────────────────
p.pedido("Aquí tengamos ojo con la ubicación del título de las historias (ya sea animada o estática), deben estar en la "
         "misma separación del logo. Y le bajaría un poco al interlineado de los mismos títulos, porfis apliquemos esto "
         "a todas las historias con estas características", "Constanza Lizana · para la ST Family Time S1", "29-09",
         que="<b>Qué cambió:</b> ahora todas las historias de octubre con titular bajo el logo arrancan en el mismo punto. "
             "La mayúscula del título queda en <b>y = 488</b> (la de Servicios, que ya estaba bien). La interlínea de los "
             "títulos baja de <b>1,14 a 1,06</b>. Antes cada historia arrancaba a una altura distinta: 416, 488, 495, "
             "518, y dos lo tenían dentro del panel, en 530 y 1064.")
p.comparar((f"{A}/ft-1.png", "antes · texto 1, versal en 488"), (f"{D}/ft-1.png", "ahora · versal en 488, interlínea 1,06"),
           titulo="ST 01-10 Family Time (animada) · texto 1")
p.comparar((f"{A}/ft-2.png", "antes · el texto 2 subía a 416: el título saltaba 72 px entre escenas"),
           (f"{D}/ft-2.png", "ahora · el texto 2 arranca en el mismo punto que el 1"),
           titulo="ST 01-10 Family Time (animada) · texto 2 y bajada",
           notas=("Qué era", ["Esta era la falla que marcó Constanza: dentro de la misma historia los dos títulos no quedaban a la "
                  "misma distancia del logo.",
                  "De pasada, «IVA INCLUIDO» de la bajada va sin letras espaciadas."]))
p.comparar((f"{A}/DT ST 13-10 Servicios del hotel.png", "antes · interlínea 1,14"),
           (f"{D}/DT ST 13-10 Servicios del hotel.png", "ahora · misma altura, interlínea 1,06"),
           titulo="ST 13-10 Servicios del hotel", detalle=(0, 300, 1080, 760))
p.comparar((f"{A}/DT ST 30-10 Hilton Honors beneficios.png", "antes · versal en 518, 30 px más abajo que el resto"),
           (f"{D}/DT ST 30-10 Hilton Honors beneficios.png", "ahora · versal en 488, interlínea 1,06"),
           titulo="ST 30-10 Hilton Honors", detalle=(0, 300, 1080, 900))

# ── 2 · feriado ER + FT (col E) ────────────────────────────────────────────
p.pedido("Ojo con los destacados que hay en cada bullet con una flecha al lado, pasa lo mismo que en el carrusel del "
         "feed, porque en DT no se usan las palabras con cada letra tan separada", "Constanza Lizana", "29-09",
         que="<b>Qué cambió:</b> «EN PAREJA →» y «EN FAMILIA →» pasan de letras muy separadas (0,16 em) a versales Trade "
             "casi sin tracking (0,03 em), un poco más grandes para que sigan leyéndose. El título sube a la separación "
             "común del logo.")
p.comparar((f"{A}/DT ST 05-10 Feriado ER y FT.png", "antes"), (f"{D}/DT ST 05-10 Feriado ER y FT.png", "ahora"),
           titulo="ST 05-10 · ¿Fin de semana largo? (ER + FT)")
p.comparar((f"{A}/DT ST 05-10 Feriado ER y FT.png", "antes · EN PAREJA con letras separadas"),
           (f"{D}/DT ST 05-10 Feriado ER y FT.png", "ahora · letras juntas"),
           titulo="El destacado con flecha, de cerca", detalle=(110, 930, 970, 1510))

# ── 3 · feriado ER sola y FT sola (col F y G) ──────────────────────────────
p.pedido("En estas 2 historias lo mismo con las tipografías separadas en cada palabra, y en los bullets creo que "
         "habitualmente usas la tipografía con serif", "Constanza Lizana · para «escápate en pareja» y «largo en familia»", "29-09",
         que="<b>Qué cambió:</b> (1) lo que incluye el programa estaba en versales Trade espaciadas y ahora va en "
             "<b>Stag, en minúscula</b>, como el punteo del carrusel; las píldoras de contorno de la referencia se quedan. "
             "(2) «IVA INCLUIDO» sin tracking abierto. (3) Por la regla de los títulos, el titular <b>sale del panel</b> y "
             "sube bajo el logo, a la misma separación que el resto; el panel queda con precio, incluye, correo y legal.")
p.comparar((f"{A}/DT ST 05-10 Feriado Escapada Romantica.png", "antes · titular dentro del panel, incluye en versales espaciadas"),
           (f"{D}/DT ST 05-10 Feriado Escapada Romantica.png", "ahora · titular bajo el logo, incluye en Stag"),
           titulo="ST 05-10 · Escápate en pareja")
p.comparar((f"{A}/DT ST 05-10 Feriado Escapada Romantica.png", "antes"),
           (f"{D}/DT ST 05-10 Feriado Escapada Romantica.png", "ahora"),
           titulo="Los incluye, de cerca", detalle=(88, 900, 700, 1500))
p.comparar((f"{A}/DT ST 05-10 Feriado Family Time.png", "antes · titular abajo, en el panel"),
           (f"{D}/DT ST 05-10 Feriado Family Time.png", "ahora · titular bajo el logo; la foto baja 130 px para que la familia quede entera entre el título y el panel"),
           titulo="ST 05-10 · Fin de semana largo en familia")
p.comparar((f"{A}/DT ST 05-10 Feriado Family Time.png", "antes"),
           (f"{D}/DT ST 05-10 Feriado Family Time.png", "ahora"),
           titulo="El panel, de cerca", detalle=(88, 1000, 992, 1580))

# ── 4 · portada del carrusel ───────────────────────────────────────────────
p.pedido("En la portada donde dice «escapada romántica» que cada tipografía esté más junta, creo que ese recurso no lo "
         "usas en DT. Y el interlineado entre un break... y sin salir... que sea menos, se ve muy separado",
         "Constanza Lizana", "29-09",
         que="<b>Qué cambió:</b> «ESCAPADA ROMÁNTICA» pasa de 0,34 em de tracking a 0,03 em (y de cuerpo 26 a 30 para que "
             "no se achique). La interlínea del titular baja de <b>1,30 a 1,16</b>. «IVA INCLUIDO» también sin espaciado.")
p.comparar((f"{A}/C1 S2 DT n°1.png", "antes"), (f"{D}/C1 S2 DT n°1.png", "ahora"),
           titulo="FEED 07-10 · portada Escapada Romántica", detalle=(0, 250, 1080, 560), lienzo=1080)

# ── 5 · coworking ──────────────────────────────────────────────────────────
p.comparar((f"{A}/cw-2.png", "antes · UBICACIÓN con letras separadas"), (f"{D}/cw-2.png", "ahora · letras juntas"),
           titulo="ST 22-10 Coworking (animada) · por la misma regla", detalle=(140, 900, 940, 1400),
           notas=("Ojo", ["Constanza no la comentó, pero tenía el mismo recurso que ella dice que no se usa en DT.",
                  "El título de Coworking NO se movió: va dentro del cristal al centro, no bajo el logo, así que no es "
                  "una historia «con estas características». Si quieres que también suba bajo el logo, dime y lo hago.",
                  "⚠️ <b>NO está subido a Drive</b>: como Constanza no la comentó, espera tu OK."]))

p.notas([
    "⚠️ <b>Choque con una regla tuya de hoy.</b> En la ronda 3 del carrusel pediste interlínea 1,3 en lo apilado "
    "(«están muy juntos los textos cuando se trata de stack», R-105) y Constanza pide bajarla. La dejé en <b>1,16</b>, a "
    "medio camino: más junta que tu 1,3 pero sin volver al 1,10–1,14 que te pareció apretado. Si prefieres uno de los "
    "dos extremos, es un cambio de un número.",
    "El resto del carrusel (lámina 2) no se tocó: Constanza no la comentó.",
    "La separación se verificó midiendo cada render: la mayúscula del titular cae en y = 487–489 en las 7 historias.",
    "Las animadas se re-rindieron completas (MP4 + GIF). Family Time es la ronda 9 con este solo cambio de títulos.",
    "<b>En Drive (reemplazadas, md5 verificado):</b> S1/STS Family Time MP4 + GIF · S2/STS las 3 feriado · S2/FEED portada C1 S2 DT n°1 · S3/STS Servicios · S5/STS Honors. Coworking queda sin subir hasta tu OK.",
])
p.escribir()

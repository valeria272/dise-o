#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 11 (01-10) — cambios de la grilla: reel de cumpleaños, carrusel To Go,
opción de «Reúnete» con foto real y fechas corridas.

Uso:  python scripts/between-oct-r11-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
R = B + "oct-r11/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 11",
           "Cambios de la grilla del 01-10",
           "01-10-2026 · reel 02-10 · carrusel To Go 01-10 · Reúnete 07-10 · fechas",
           R + "revision-r11.html")

# ── 1 · reel ──
p.pedido("Agregar legales. No decir gratis, que diga Ven por tu café de regalo",
         "cliente, grilla FEED G15 (con una captura del legal del reel anterior)", "01-10",
         que="Y Nicolás, en el hilo de G12: «Cuando hagamos los cambios, preocupémonos de los tiempos de los "
             "textos. Hay harta información, así que asegurémonos de que se alcance a leer todo».",
         titulo="1 · Reel café de cumpleaños (02-10)")
p.comparar((R + "antes/BW FEED 02-10 Cafe de cumpleanos - PORTADA.png", "12,5 s · 5 botones"),
           (R + "BW FEED 02-10 Cafe de cumpleanos - PORTADA.png", "16,5 s · 6 botones"),
           titulo="Reel · cierre con el legal", lienzo=1080,
           notas=("Qué cambió", [
               "<b>«CAFÉ GRATIS» → «CAFÉ DE REGALO»</b>, misma voz (Raleway Black), a 104 para que quepa en la zona segura.",
               "<b>Legal</b>: se suma «Extras y personalizaciones no incluidas.» como sexto botón. La otra línea de la "
               "captura del cliente (presentar la cédula) ya estaba dicha en «presentando carnet de identidad al momento de "
               "solicitarlo», así que no se repite. Los botones bajan de 37 a 34 px para que la pila termine sobre el confeti, como antes.",
               "<b>Tiempos</b>: 12,5 → 16,5 s. El gancho queda igual (2,5 s); «El café va por nuestra cuenta» 3 → 3,5 s; "
               "«Ven por tu café de regalo» 3 → 4 s; el legal 4 → 6,5 s y los botones entran más espaciados. Cada texto queda "
               "quieto más de 1 s después de terminar de escribirse.",
               "<b>Música</b>: es la misma pista aprobada, alargada repitiendo un tramo de 5,45 s (empalme en 1,78 s). "
               "⚠️ No la puedo escuchar: <b>óyela una vez</b> por si el empalme se nota.",
               "<b>Ya reemplazado en Drive</b> (S1/BW/FEED): MP4 + GIF + PORTADA, mismo nombre y enlace, md5 = local. "
               "Local: <code>out/hilton/between/oct-r11/BW FEED 02-10 Cafe de cumpleanos.mp4</code>",
           ]))
p.laminas([(R + "cuadros/f0170.png", "3,5 s — el café va por nuestra cuenta"),
           (R + "cuadros/f0275.png", "4 s — café de regalo"),
           (R + "cuadros/f0494.png", "6,5 s — legal completo")],
          titulo="Reel · los tres bloques", ancho=300)

# ── 2 · carrusel ──
p.pedido("Acá falta una slide de introducción, como lo hemos hecho anteriormente, donde vaya la infor de horarios y "
         "esas cosas. En la G2 se elimina la info de horarios y en la G4 debemos poner logo Between a la bolsa, les dejo "
         "ejemplo de bolsa que se usa, debe ser con logo actual",
         "cliente, grilla FEED E15 (con la foto de la bolsa blanca)", "01-10",
         titulo="2 · Carrusel To Go (01-10)")
p.laminas([(R + f"C1 n°{k} togo S1.png", pie) for k, pie in (
    (1, "n°1 · NUEVA — introducción con el horario"),
    (2, "n°2 · sin el horario"), (3, "n°3 · sin el horario"),
    (4, "n°4 · sin el horario"), (5, "n°5 · bolsa blanca con logo, sin el horario"))],
          titulo="Carrusel · las 5 láminas", ancho=300,
          notas=("Qué cambió y qué decidí", [
              "<b>Lámina de introducción</b> (nueva n°1): una mano se lleva la bolsa junto al vaso, en la misma mesa y muro "
              "verde del carrusel. Textos sólo del brief: «Promos To Go» + «De lunes a viernes» + «De 8:00 a 10:00 hrs». "
              "<b>No inventé un gancho</b>: si contenido quiere una frase como la de septiembre («Tu desayuno va contigo»), que la escriba y la pongo.",
              "<b>Horarios</b>: los saqué de <b>todas</b> las láminas de producto, no sólo de la G2, porque en el carrusel de "
              "septiembre el horario vivía sólo en la portada («como lo hemos hecho anteriormente»). ⚠️ <b>Es mi lectura</b>: "
              "si el cliente quería sacarlo sólo de una, se devuelve en un minuto.",
              "<b>Bolsa</b>: es la blanca de la foto del cliente, con el logotipo vigente (Between Coffee &amp; Bar) calzado en café "
              "de marca; la IA generó la bolsa en blanco y el logo es el archivo real. ⚠️ La bolsa real de la foto imprime en "
              "terracota: ¿el logo va en café o en ese tono?",
              "<b>Probé una persona saliendo con el vaso y la bolsa</b> y la descarté: sin cara y con aire arriba, la IA "
              "disolvía el torso en las plantas (se notaba IA).",
              "<b>Drive</b> (S1/BW/FEED/C1 togo S1): las 4 que estaban se <b>renombraron</b> un número arriba (mismos enlaces), "
              "se les reemplazó el contenido y la introducción subió como n°1. Las 5 con md5 = local.",
          ]))
p.comparar((R + "antes/C1 n°4 togo S1.png", "bolsa kraft, con horario"),
           (R + "C1 n°5 togo S1.png", "bolsa blanca con logo"),
           titulo="Carrusel · la lámina de la bolsa", detalle=(380, 380, 1000, 1000), escala=1.2)

# ── 3 · Reúnete ──
p.pedido("Veamos opción de foto que haya sacado la scar o nannel el día del shooting?",
         "cliente, grilla FEED I15", "01-10", titulo="3 · Reúnete en Between (ahora 07-10)")
p.opciones([(B + "oct-r3/f05-r4.png", "VIGENTE en Drive — foto generada"),
            (R + "BW FEED 07-10 Reunete en Between - OPCION foto real.png", "OPCIÓN — foto real de Nannel (sep_26-269)")],
           titulo="Reúnete · vigente y opción con foto real",
           notas=("Lo que hay", [
               "Revisé las 523 fotos de la sesión de septiembre: de Between hay espacios sin gente. Lo más cercano a "
               "«reunión» es esta serie de notebook + café en el lounge (267–270); <b>no hay una toma de dos personas</b>.",
               "Otras reales posibles: el lounge con mesas y banqueta (263–266) o el jardín de invierno (228–234).",
               "<b>La vigente no se tocó.</b> La opción subió al lado, con otro nombre: "
               "<code>BW FEED 07-10 Reunete en Between - OPCION foto real.png</code> (S1/BW/FEED).",
               "Las fotos que haya sacado Scarlette con su teléfono no las tengo: si existen, pásamelas y la armo con ésa.",
           ]))

# ── 4 · fechas ──
p.medido([
    ("ST Cowork", "19-10 → 12-10", "ok", "renombrada en S3/BW/STS (mismo enlace)"),
    ("ST Lo dicen ustedes", "20-10 → 13-10", "ok", "renombrada en S3/BW/STS"),
    ("ST Espacio para tu evento", "27-10 → 22-10", "ok", "renombrada en S4/BW/STS"),
    ("FEED Reúnete", "09-10 → 07-10", "ojo", "sigue como «BW FEED 05-10 Esa reunion…» en S1: no la renombré"),
    ("ST 01-10 ganador", "CORREGIDO", "ok", "la de «por interno», ya en la grilla"),
    ("ST 02-10 · 05-10 · 08-10", "APROBADO", "ok", "no se tocan"),
    ("ST 15-10 Promos To Go (ajuste)", "CORREGIDO", "", "no la diseñé yo; no la toqué"),
], titulo="4 · Fechas que corrió la grilla y estados")

print(p.escribir())

#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 8 (30-09) — reglas nuevas aplicadas desde la S3.

Uso:  python scripts/between-oct-r8-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

R = "out/hilton/between/oct-r8/"
A = R + "antes/"

p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 8",
           "Reglas nuevas aplicadas desde la S3",
           "30-09-2026 · S1 y S2 no se tocaron (ya están en revisión)",
           R + "revision-r8.html")

p.pedido("Hay unas nuevas reglas que quiero que apliques en las historias y también en todo el feed… "
         "solamente desde la S3 en adelante. También verifica si están bien guardados según semanas… "
         "el reel del «Por qué vienes» ese es de la S3 ahora. La S1 y S2 déjalo tal cual.", "Eli", "30-09")

p.notas([
    "<b>Reglas que se revisaron en cada pieza:</b> máx. 3 voces Raleway y sin itálica suelta (R-140, Constanza) · "
    "interlineado cerrado sin que se toquen tildes, «¿» ni «Ñ» (R-142) · cajas de una pila del mismo ancho (R-144) · "
    "bajada de feed que se lea, Bold ~38 (R-118) · títulos y bajadas sin punto (R-60) · CTA sólo si el brief lo pide · "
    "letras sin espaciar.",
    "<b>Cambiaron 4 piezas</b> (Bonjour, Evento, Lo dicen ustedes, Espacios). <b>Cowork 19-10 y el reel 12-10 ya cumplían</b>: no se tocaron.",
    "<b>Ya está todo reemplazado en Drive</b>, con el mismo nombre y el mismo enlace, y el md5 es igual al archivo local. Si algo no te gusta, se vuelve atrás en un minuto.",
], titulo="Resumen")

p.comparar((A + "BW ST 28-10 Desayuno Bonjour.png", "entrega 24-09"),
           (R + "BW ST 28-10 Desayuno Bonjour.png", "ronda 8"),
           titulo="ST 28-10 · Desayuno Bonjour (S5)", detalle=(230, 1420, 850, 1610), escala=1.4,
           notas=("Qué cambió", ["<b>El horario se leía «1 1:30»</b>: los dos «1» seguidos quedaban separados. Ahora se lee «11:30».",
                  "<b>Las dos cajas, del mismo ancho</b> (560 px). Antes la del horario era más angosta (R-144).",
                  "<b>Interlineado más cerrado</b> en «ASÍ PARTEN / LAS BUENAS MAÑANAS»: ~13 px menos, sin que la tilde de la Ñ toque la línea de arriba.",
                  "<b>La bajada «Desayuno Bonjour…» pasa de Medium a SemiBold</b>, para que se lea mejor sobre la taza."]))
p.comparar((A + "BW ST 28-10 Desayuno Bonjour.png", "entrega 24-09"),
           (R + "BW ST 28-10 Desayuno Bonjour.png", "ronda 8"),
           titulo="Bonjour · detalle del titular", detalle=(120, 660, 960, 1000), escala=1.2)

p.comparar((A + "BW ST 27-10 Espacio para tu evento.png", "entrega 24-09"),
           (R + "BW ST 27-10 Espacio para tu evento.png", "ronda 8"),
           titulo="ST 27-10 · Espacio para tu evento (S4)", detalle=(84, 420, 996, 720), escala=1.1,
           notas=("Qué cambió", ["<b>Interlineado cerrado</b> entre «¿BUSCAS UN ESPACIO» y «PARA TU PRÓXIMO EVENTO?»: ~12 px menos, y el panel se acorta lo mismo. La «Ó» y el «¿» no se tocan.",
                  "Es un cambio chico: se ve mejor en el detalle ampliado."]))

p.comparar((A + "BW ST 20-10 Lo dicen ustedes.png", "entrega 24-09"),
           (R + "BW ST 20-10 Lo dicen ustedes.png", "ronda 8"),
           titulo="ST 20-10 · Lo dicen ustedes (S3)", detalle=(240, 1460, 840, 1600), escala=1.5,
           notas=("Qué cambió", ["<b>Fuera la itálica</b> del cierre «Gracias por hacer de Between parte de sus días»: queda en la misma Raleway SemiBold que las tarjetas. Pasa de 4 voces a 3 (R-140).",
                  "Sobre la madera se lee más firme.",
                  "⚠️ <b>Sigue abierto de antes:</b> los cuatro textos son los ejemplos del brief. Antes de publicar hay que reemplazarlos por reseñas reales (lo tiene que pasar contenido)."]))

p.comparar((A + "BW FEED 14-10 Espacios Between.png", "entrega 24-09"),
           (R + "BW FEED 14-10 Espacios Between.png", "ronda 8"),
           titulo="FEED 14-10 · Espacios Between (S3)", detalle=(180, 210, 900, 500), escala=1.2, lienzo=1080,
           notas=("Qué cambió", ["<b>La bajada de la caja se lee más</b>: Raleway Bold 38, antes SemiBold 34. Es la regla de la bajada de feed que diste el 29-09 (R-118).",
                  "<b>Interlineado del titular cerrado</b>: ~15 px menos entre «ESPACIOS QUE INVITAN» y «A QUEDARSE».",
                  "<b>Semana:</b> la grilla la pone en el bloque SEMANA 3. Estaba en S4, así que se movió a <b>S3/BW/FEED</b>."]))

p.opciones([(R + "../entrega-oct/BW ST 19-10 Cowork.png", "ST 19-10 Cowork · sin cambios"),
            (R + "../oct-r2/BW FEED 12-10 Por que vienes por que te quedas - PORTADA.png",
             "Reel FEED 12-10 · sin cambios · movido a S3")],
           titulo="Revisadas y sin cambios", elige=False,
           notas=("Qué cambió", ["<b>Cowork 19-10:</b> 3 voces (rótulo con pin, titular, dato con barra), interlineado ya cerrado, sin punto y sin logo (como pediste). Cumple.",
                  "<b>Reel 12-10 «Por qué vienes / Por qué te quedas»:</b> una sola voz, zona segura de pauta respetada. Estaba en S4 y la grilla ahora lo pone en la <b>SEMANA 3</b>: MP4, GIF y PORTADA se movieron a <b>S3/BW/FEED</b>, con el mismo enlace."]))

p.medido([
    ("S3/BW/STS", "ST 19-10 Cowork · ST 20-10 Lo dicen ustedes", "ok", "20-10 reemplazada"),
    ("S3/BW/FEED", "Reel 12-10 (MP4 + GIF + PORTADA) · FEED 14-10 Espacios", "ok", "movidos desde S4"),
    ("S4/BW/STS", "ST 27-10 Espacio para tu evento", "ok", "reemplazada"),
    ("S4/BW/FEED", "vacía", "ok", "el FEED 28-10 spooky sigue PENDIENTE POR CLIENTE"),
    ("S5/BW/STS", "ST 28-10 Desayuno Bonjour", "ok", "reemplazada"),
    ("md5 Drive = local", "4 de 4", "ok", ""),
], titulo="Cómo quedó Drive, por semana")

p.notas([
    "<b>Carruseles:</b> en octubre de Between todavía no hay ninguno diseñado. El FEED 01-10 To Go está en REVISAR CONTENIDO (Scarlette le pidió a Nicolás ajustarlo con la info de Promos To Go) y el FEED 07-10 de almuerzos está en REVISAR CONTENIDO.",
    "<b>Sin diseñar, y no toca todavía:</b> ST 22-10 Info (PENDIENTE POR CLIENTE), ST 25-10 To Go animada (CORREGIDO, esperando contenido), ST 26-10 WTF (grabación orgánica), ST 29-10 y FEED 28-10 spooky (PENDIENTE POR CLIENTE).",
    "<b>En S1–S2 no toqué nada.</b> Sólo lo anoto: el FEED «Reúnete en Between» (fecha 09-10, bloque SEMANA 2 de la grilla) sigue en S1/BW/FEED con el nombre viejo «BW FEED 05-10 Esa reunion podria ser un cafe». Lo muevo y renombro si me dices.",
], titulo="Lo demás de la grilla")

print(p.escribir())

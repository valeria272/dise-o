#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · octubre · hilos de Carlos Figueroa (contenido) del 02-10 — ST Escapada con adicionales y ST nueva Noche de Bodas."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/oct6"
A, D, F = f"{R}/antes", f"{R}/despues", f"{R}/refs"
p = Pagina("dt", "DOUBLETREE · OCTUBRE · HILOS DE CONTENIDO",
           "Dos historias: Escapada con adicionales y Noche de Bodas",
           "02-10-2026 · ronda 3 · Escapada APROBADA · Noche de Bodas con la toma del brindis, logo y titular en blanco · las dos en Drive S2/DT/STS (md5 verificado)",
           f"{R}/revision.html", origen="scripts/dt-oct6-revision.py")

# ── RONDA 3 · logo y titular en blanco ──────────────────────────────────────
p.pedido("antes de cerrar deja el texto y logo en blanco de noche de bodas… ya que es una secuencia, no debe verse "
         "diferente", "Eli", "02-10 · ronda 3",
         que="<b>Qué cambió:</b> el logo y el titular pasan de azul a <b>blanco</b>, con el mismo velo azul y la misma "
             "sombra que llevan las otras historias del feriado, para que las cuatro se lean como una sola secuencia. "
             "La foto, el panel y los textos no cambian.")
p.comparar((f"{R}/r2/DT ST S2 Noche de Bodas.png", "ronda 2 · logo y titular en azul"),
           (f"{D}/DT ST S2 Noche de Bodas.png", "ahora · en blanco, con velo"),
           titulo="ST Noche de Bodas · ronda 2 y ronda 3")
p.opciones([(f"{R}/secuencia-s2.jpg", "ER + FT · Escapada · Family Time · Noche de Bodas")],
           titulo="La secuencia completa de la semana 2")

# ── RONDA 2 · Noche de Bodas con la toma del brindis ────────────────────────
p.pedido("para la de noche de bodas, lo veo bastante bien, pero la foto: que las copitas que se ven ahí, las llenes de un "
         "poco de espumante y utilices esa toma. No arriba de las flores, sino más abajo. Donde están las flores, la "
         "botella de champán con las copitas. Esa es la toma que quieren añadir", "Eli", "02-10 · ronda 2",
         que="<b>Qué cambió:</b> la mitad de arriba ya no es el acercamiento a las rosas: es <b>el conjunto completo</b> — "
             "el ramo, la cubeta con la botella y <b>las dos copas servidas con espumante</b>, enteras sobre la mesa. "
             "La foto de contenido es vertical y, a lo ancho de la historia, ese conjunto mide 745 px de alto y quedaba "
             "detrás del titular; por eso la toma es la misma escena con más pared arriba (Nano Banana Pro sobre la foto "
             "de contenido: sirvió las copas y continuó la pared y la mesa, sin tocar los objetos). El titular vuelve al "
             "centro, como la referencia, y el corte entre las dos fotos baja de y = 1000 a 1100. El panel y la tina "
             "bajan con él; los textos no cambian.")
p.comparar((f"{R}/r1/DT ST S2 Noche de Bodas.png", "ronda 1 · sólo las rosas"),
           (f"{R}/r2/DT ST S2 Noche de Bodas.png", "ronda 2 · rosas, botella y copas servidas"),
           titulo="ST Noche de Bodas · ronda 1 y ronda 2")
p.comparar((f"{R}/r1/DT ST S2 Noche de Bodas.png", "ronda 1"), (f"{R}/r2/DT ST S2 Noche de Bodas.png", "ronda 2"),
           titulo="La toma, de cerca", detalle=(60, 400, 1020, 1110))
p.opciones([(f"{F}/v-nb-foto1.jpg", "foto 1 de contenido · copas vacías"),
            (f"{R}/noche-bodas-guia.png", "ahora · guía de zonas seguras")],
           titulo="De dónde sale la toma")
p.pedido("Para la ST de este fin de semana largo, me parece perfecto. Me gustó cómo lo añadiste", "Eli", "02-10 · ronda 2",
         que="<b>ST Escapada Romántica feriado: APROBADA.</b> No se tocó; es la misma que está en Drive desde la ronda 1.")

# ── 1 · ST Escapada Romántica feriado (STORIES col F) ──────────────────────
p.pedido("me ayudas con esto? hay que añadirle los ad ons", "Carlos Figueroa · hilo en STORIES!F10 (ST Escapada Romántica feriado)", "02-10",
         que="<b>Qué cambió:</b> el brief sumó «Agrega sunset: +$21.000…» y «Agrega masajes…» y la celda pasó a EN CAMBIOS. "
             "Los dos adicionales entran <b>dentro del mismo panel azul</b>, en dos filas separadas por filetes, escritos "
             "igual que en la lámina 2 del carrusel Escapada que aprobaste el 29-09: los dos «Agrega…» al mismo peso, "
             "«+» en los dos precios y el punteo con punto final. Para que quepan, el panel crece hacia abajo (cierra en "
             "y = 1566, dentro de la zona segura), el precio baja de cuerpo 92 a 84 con «IVA INCLUIDO» al lado, y las "
             "píldoras se aprietan un punto. El titular, la foto y el ancho del panel no se movieron.")
p.comparar((f"{A}/DT ST 05-10 Feriado Escapada Romantica.png", "antes · sin adicionales"),
           (f"{D}/DT ST 05-10 Feriado Escapada Romantica.png", "ahora · con sunset y masajes"),
           titulo="ST 05-10 · Este fin de semana largo, escápate en pareja")
p.comparar((f"{A}/DT ST 05-10 Feriado Escapada Romantica.png", "antes"),
           (f"{D}/DT ST 05-10 Feriado Escapada Romantica.png", "ahora"),
           titulo="El panel, de cerca", detalle=(70, 720, 720, 1590))

# ── 2 · ST Noche de Bodas (STORIES col H) ──────────────────────────────────
p.pedido("pidieron esta ST adicional", "Carlos Figueroa · hilo en STORIES!H10 (ESTÁTICA NOCHE DE BODAS, OK PARA DISEÑO)", "02-10",
         que="<b>Brief:</b> «Imagen de flores y pétalos (dividida en 2 ref aquí, te comparto aquí foto 1 y foto 2)». "
             "La pieza va <b>partida en dos fotos</b>, como la referencia: arriba las rosas con el titular, abajo la tina "
             "con pétalos y el programa en el panel azul con píldoras y botón (la referencia de la celda LINK, la misma "
             "de las historias del feriado). «Noche de Bodas» va como lo escribes en tu carrusel de septiembre: Stag "
             "itálica a dos pesos.")
p.opciones([(f"{F}/ref-nb-dividida.jpg", "referencia del brief · dividida en 2"),
            (f"{F}/ref-panel.jpg", "referencia de la celda LINK · panel con píldoras"),
            (f"{F}/v-nb-foto1.jpg", "foto 1 de contenido · rosas"),
            (f"{F}/v-nb-foto2.jpg", "foto 2 de contenido · tina con pétalos")],
           titulo="Las referencias y las dos fotos que dejó contenido")

p.medido([
    ("Versal del titular bajo el logo", "y = 439", "ok", "la norma de las historias DT es 440 ±2"),
    ("Titular blanco contra la pared con velo (peor tercio)", "3,9 : 1", "ok", "vara de titular grande: 3 : 1; los otros dos tercios dan 4,9 y 6,3"),
    ("Logotipo blanco contra la pared con velo", "5,9 a 6,6 : 1", "ok", "sin velo daba 3,5 : 1"),
    ("«perfecto» contra la cortina", "50 px de aire", "ok", "el titular termina en x = 839 y la cortina empieza en 890"),
    ("Cierre del panel", "y = 1558", "ok", "la zona segura inferior empieza en 1580"),
    ("QA de la marca (qa/motor.py --marca hilton)", "2 de 2", "ok", "las dos piezas pasan (Noche de Bodas, vuelta a pasar en la ronda 2)"),
], titulo="Lo medido en las dos piezas")

p.notas([
    "<b>Dudas para ti (o para Carlos):</b>",
    "1 · El brief de Noche de Bodas dice <b>«Reserva tu escapada de invierno»</b> y la pieza sale en octubre. Lo dejé "
    "literal, en el botón, porque el texto es de contenido. Si lo cambian, es una línea.",
    "3 · En la toma nueva <b>no está la lámpara</b> de la foto de contenido (su pantalla caía detrás del titular) ni la "
    "tarjeta con QR de la mesa. El ramo, la cubeta, la botella, la servilleta y las copas son los de la foto. Si el "
    "cliente quiere la lámpara, se puede pedir con ella a la derecha.",
    "4 · La columna H no tiene fecha en la grilla. La nombré <b>«DT ST S2 Noche de Bodas.png»</b> y quedó en la carpeta "
    "de la semana 2, junto a las del feriado. Si va en otra semana, la muevo.",
    "5 · En la ST de Escapada, masajes dice <b>+$100.000</b>, igual que en el carrusel aprobado (el brief dice «Dos "
    "masajes de 60 minutos por $100.000»).",
    "<b>En Drive:</b> S2/DT/STS «DT ST 05-10 Feriado Escapada Romantica.png» (aprobada) y «DT ST S2 Noche de Bodas.png» "
    "reemplazada con la ronda 2 (mismo enlace). Una copia de cada una, md5 verificado.",
    "No cambié ningún estado ni respondí hilos en la grilla. Respaldos en <code>out/hilton/dt/oct6/antes/</code> y <code>r1/</code>.",
])
p.escribir()

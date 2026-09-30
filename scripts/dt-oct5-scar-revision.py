#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · octubre · hilos de Scarlette Muñoz (contenido) en la grilla, 29-09 noche → 30-09 — antes y después."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/oct5-scar"
A, D = f"{R}/antes", f"{R}/despues"
p = Pagina("dt", "DOUBLETREE · OCTUBRE · HILOS DE CONTENIDO",
           "Lo que pidió Scarlette en la grilla",
           "30-09-2026 · 3 piezas EN CAMBIOS · las 3 ya reemplazadas en Drive (md5 verificado)",
           f"{R}/revision.html", origen="scripts/dt-oct5-scar-revision.py")

# ── 1 · Family Time animada (STORIES col C) ────────────────────────────────
p.pedido("cambiemos la imagen de la familia tomando desayuno por: [foto] y la que salen caminando por una de la "
         "habitación: [video]", "Scarlette Muñoz · hilo en STORIES!C15 (Family Time 01-10)", "29-09",
         que="<b>Qué cambió:</b> la escena del lobby (la familia caminando con la maleta) ahora es <b>el video real de "
             "la habitación doble</b> que mandó Scarlette, un paneo de 3,7 s. La del desayuno ahora es <b>su foto real del "
             "buffet</b>. La tercera escena, la familia en la cama, se queda porque Family Time tiene que mostrar una "
             "familia. Los textos, la bajada y los tiempos no cambian.")
p.opciones([(f"{R}/scar-video-hab.jpg", "lo que mandó · video de la habitación (cuadro)"),
            (f"{R}/scar-foto-buffet.jpg", "lo que mandó · foto del buffet (3:4)")],
           titulo="El material de Scarlette")
p.comparar((f"{A}/ft-1.5.png", "antes · lobby, familia generada caminando"),
           (f"{D}/ft-1.5.png", "ahora · video real de la habitación"),
           titulo="Escena 1 · «Días más largos, clima perfecto» (1,5 s)")
p.comparar((f"{A}/ft-6.5.png", "antes · familia generada en el desayuno"),
           (f"{D}/ft-6.5.png", "ahora · foto real del buffet"),
           titulo="Escena 2 · el desayuno (6,5 s)",
           notas=("Cómo se encuadró", ["La foto es 3:4; para la historia se recortó a 9:16 desde más abajo. Así la lámpara "
                  "de bronce queda sobre el logo y no detrás: con el recorte centrado, el árbol del logo caía encima del "
                  "disco iluminado y no se leía.",
                  "También queda fuera la persona que aparecía de espaldas en el borde derecho de la foto."]))
p.comparar((f"{A}/ft-12.png", "antes"), (f"{D}/ft-12.png", "ahora · igual"),
           titulo="Escena 3 · la familia en la habitación (12 s), sin cambios")

# ── 2 · carrusel Escapada lámina 2 (FEED col C) ─────────────────────────────
p.pedido("me parece que la 2da slide es la que está más débil por temas de copas (no tenemos con mango rosado) y el "
         "plato (pongamos imagen de algún producto de QB, esos panes no se encuentran en la carta)",
         "Scarlette Muñoz · hilo en FEED!C14 (carrusel Escapada 07-10)", "29-09",
         que="<b>Qué cambió:</b> salió la foto generada (copa de pie rosado y bruschettas que no existen). Entró una "
             "<b>foto real de la carta de QB</b> de la sesión que pasaste el 25-09 («Ostiones parmesanos a la batayaki "
             "20»): un brindis con las copas de la casa sobre los ostiones y la trucha arcoíris. Textos iguales.")
p.comparar((f"{A}/C1 S2 DT n°2.png", "antes · foto generada"), (f"{D}/C1 S2 DT n°2.png", "ahora · foto real de QB"),
           titulo="FEED 07-10 · lámina 2 «Personaliza tu experiencia»", lienzo=1080)

# ── 3 · feriado ER + FT (STORIES col E) ────────────────────────────────────
p.pedido("@carlos.figueroa podemos incluir Noche de bodas?", "Scarlette Muñoz a Carlos (contenido) · STORIES!E15", "29-09",
         que="<b>Qué cambió:</b> contenido sumó al brief la línea «Recién casados → Noche de Bodas, $189.000», así que "
             "la historia pasa de dos planes a <b>tres tarjetas</b>. Para que quepan, las tarjetas bajan de 250 a 220 px de "
             "alto y arrancan justo bajo la flecha. El legal queda bajo la última. La foto de la tarjeta nueva es "
             "<b>la pareja de tu carrusel Noche de Bodas de septiembre</b> (C1 S1 N°1): es material ya aprobado del "
             "programa y es otra pareja, distinta de la de Escapada.")
p.comparar((f"{A}/DT ST 05-10 Feriado ER y FT.png", "antes · dos planes"),
           (f"{D}/DT ST 05-10 Feriado ER y FT.png", "ahora · tres planes"),
           titulo="ST 05-10 · ¿Fin de semana largo? (ER + FT + Noche de Bodas)")
p.comparar((f"{A}/DT ST 05-10 Feriado ER y FT.png", "antes"), (f"{D}/DT ST 05-10 Feriado ER y FT.png", "ahora"),
           titulo="Las tarjetas, de cerca", detalle=(100, 800, 980, 1680))

p.notas([
    "<b>Dudas para ti (o para Scarlette):</b>",
    "1 · En la lámina 2, el plato que manda abajo es la <b>trucha</b> (un fondo); los ostiones, que sí son una entrada, "
    "quedan en la mitad, detrás de la tabla. Son las copas de vino de QB, no dos tragos de coctelería. Si prefieres dos "
    "cócteles reales de QB (la sesión de Sunset tiene varios), cambio la foto.",
    "2 · El brief de la ST del feriado dice «(confirmar tarifa vigente)». Usé <b>$189.000</b>, que es el precio "
    "confirmado de Noche de Bodas (R-28). Esa nota es para contenido y no va en la pieza.",
    "3 · Family Time ahora tiene dos escenas de habitación: la del video, sin gente, y la de la familia en la cama. "
    "Así lo pidió Scarlette. Si prefieres otra foto para el cierre, dime.",
    "<b>En Drive (reemplazadas, 1 copia c/u, md5 verificado):</b> S1/DT/STS Family Time MP4 + GIF · S2/DT/STS "
    "«DT ST 05-10 Feriado ER y FT» · S2/DT/FEED «C1 S2 DT n°2».",
    "En la grilla las tres ya estaban EN CAMBIOS (FEED C15, STORIES C16 y E16). No cambié ningún estado.",
    "Respaldo de lo anterior en <code>out/hilton/dt/oct5-scar/antes/</code>.",
])
p.escribir()

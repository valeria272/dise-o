#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — página de revisión de la grilla (ronda 1): cada pieza al
lado de la referencia que dejó el brief. Molde `scripts/_revision.py`.

    python scripts/p18-oct-revision.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "raw/hilton/piso18/oct/refs/"
E = "out/piso18/oct/entrega/"

p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 1",
    "Las 11 piezas en OK PARA DISEÑAR",
    "28-09-2026 · FEED 06, 09, 13, 16, 23 y 27-10 · STORIES 05, 07, 09, 23 y 27-10 · cada una al lado de su referencia",
    "out/piso18/oct/revision-r1.html",
    origen="scripts/p18-oct-revision.py",
)
p.pedido(
    "Trabajaremos diseñando la grilla de piso18 que esté okey para diseñar feed y stories, "
    "tómalo, guíate de las referencias, que sea muy igual solo que con la identidad visual de PISO18",
    "Eli", "28-09-2026",
    que="Grilla leída en vivo el 28-09. Quedan fuera las que no están en OK PARA DISEÑAR: FEED 20-10 "
        "(REVISAR CONTENIDO) y STORIES 08, 13, 15, 16, 19, 21 y 30-10 (REVISAR CONTENIDO o PENDIENTE POR CLIENTE).",
)

FEED = [
    ("FEED 06-10 · Post arreglos florales de primavera", [R + "fd-06-10-arreglos-0.jpg"],
     [E + "S2/FEED/P18 FEED 06-10 Arreglos florales.png"],
     ["Sin texto ni logotipo, como la ref y el brief («Texto: sin texto»).",
      "Foto real (deco ago-2024 · piso_18-7): rosas terracota, follaje oliva y vela, la paleta del brief."]),
    ("FEED 09-10 · Carrusel fechas 2027", [R + "fd-09-10-fechas-2027-s2-0.jpg"],
     [E + "S2/FEED/P18 FEED 09-10 Fechas 2027 1.png", E + "S2/FEED/P18 FEED 09-10 Fechas 2027 2.png"],
     ["S1: el salón real (3-Finales 2026 · 0161) extendido a 4:5 con IA, sin cambiar la escena.",
      "S2 calca la ref: papel, titular a dos voces y calendario con el día encerrado. El calendario es un "
      "fin de semana real de 2027 (viernes 15, sábado 16 y domingo 17 de enero). El rojo de la ref pasa al fucsia."]),
    ("FEED 13-10 · Carrusel atardecer desde Piso18", [R + "fd-13-10-atardecer-texto-0.jpg"],
     [E + "S3/FEED/P18 FEED 13-10 Atardecer 1.png", E + "S3/FEED/P18 FEED 13-10 Atardecer 2.png"],
     ["No hay atardecer en ninguna sesión: los dos son fotos reales de Piso18 reiluminadas a la hora dorada.",
      "S2 como la ref: versales chicas + palabra gigante en itálica + firma. La línea de arriba es el cotiza.",
      "El cliente anotó «Ojo que no queden todos los carruseles juntos»: es de calendario, no de diseño."]),
    ("FEED 16-10 · Carrusel tu próxima celebración", [R + "fd-16-10-celebracion-0.jpg"],
     [E + "S3/FEED/P18 FEED 16-10 Tu proxima celebracion %d.png" % n for n in range(1, 6)],
     ["Portada: collage 2×2 con el fajo de hojas y el clip de la ref, todo con fotos reales.",
      "La hoja se repite con el nombre de cada evento, para que el carrusel se lea como un archivo.",
      "S3 «Cumpleaños»: el banco sólo tiene copas oscuras en primer plano; la barra con la torta se produjo con IA "
      "sobre la barra y el salón reales, sin personas (el público de cumpleaños es adulto, hilo de Scarlette)."]),
    ("FEED 23-10 · Carrusel estación Tex-Mex", [R + "fd-23-10-texmex-s1-2.jpg"],
     [E + "S4/FEED/P18 FEED 23-10 Estacion Tex Mex %d.png" % n for n in range(1, 5)],
     ["La ref es el carrusel propio «Estación de trinchado»: se calcó su portada (logo, «Estación», versales, «Desliza»).",
      "No existe una estación Tex-Mex en el banco: las cuatro fotos son IA sobre el buffet real de Piso18 de noche."]),
    ("FEED 27-10 · Post wedding planner", [R + "fd-27-10-wedding-planner-0.jpg"],
     [E + "S5/FEED/P18 FEED 27-10 Wedding planner.png"],
     ["La celda de la ref dice «SIN TEXTO NI CUADRO, DEJAR LOGO PISO18»: foto + logo. "
      "«Tu matrimonio, sin complicaciones» queda para el copy.",
      "Foto IA sobre la mesa real (no hay fotos del equipo montando): una planner, gesto natural, revisada con zoom."]),
]

STORIES = [
    ("STORIES 05-10 · Animada primavera en Piso18",
     [R + "st-05-10-primavera-texto-0.jpg", R + "st-05-10-primavera-foto-0.jpg"],
     [E + "S2/STS/P18 ST 05-10 Primavera en Piso18 portada.png"],
     ["Video de 9 s (MP4 + GIF en la carpeta): la mesa real con follaje colgante y esferas de vidrio, animada con IA "
      "(las esferas se mecen, avance lento); el texto entra escalonado. Aquí va el último fotograma.",
      "Titular a la izquierda en el tercio alto, como la ref de texto."]),
    ("STORIES 07-10 · Encuesta estación favorita", [R + "st-07-10-estacion-favorita-0.jpg"],
     [E + "S2/STS/P18 ST 07-10 Estacion favorita.png"],
     ["«This / That» pasa a «Dulce / Salada» calados en fucsia; fotos reales de postres y quesos de Piso18.",
      "El hueco de la izquierda, entre las flechas, es para la barra «💖» que pone el CM."]),
    ("STORIES 09-10 · Encuesta recuerdos de matrimonio", [R + "st-09-10-recuerdos-0.jpg"],
     [E + "S2/STS/P18 ST 09-10 Recuerdos de matrimonio.png"],
     ["La nota con cintas de la ref; la encuesta (La fiesta / La comida / La decoración) la pega el CM dentro de la nota.",
      "⚠️ El brief dice «de <b>una</b> matrimonio»: se corrigió a «un matrimonio».",
      "Pista real de Piso18 con invitados producidos con IA (los rostros reales no se publican), de espaldas y en movimiento."]),
    ("STORIES 23-10 · Evento corporativo fin de año", [R + "st-23-10-corporativo-0.jpg"],
     [E + "S4/STS/P18 ST 23-10 Evento corporativo.png"],
     ["Cuadro de vidrio de la ref, con el titular y la bajada adentro, y el botón de la marca.",
      "Foto IA sobre el lounge real de noche: cóctel corporativo con mesas altas, como pide el brief."]),
    ("STORIES 27-10 · Visita virtual web", [],
     [E + "S5/STS/P18 ST 27-10 Visita virtual.png"],
     ["La ref es la historia anterior de recorrido (dos teléfonos): se repite la gramática.",
      "La pantalla del frente es el tour real de Matterport; la de atrás, el lounge real.",
      "Sin botón: el CTA «Descúbrelo aquí» es el sticker de enlace, y los 300 px de abajo quedan libres para él."]),
]

for titulo, refs, piezas, notas in FEED + STORIES:
    items = [(r, "<b>REFERENCIA</b>") for r in refs] + [(x, "<b>PISO18</b> · " + Path(x).stem) for x in piezas]
    p.laminas(items, titulo=titulo, ancho=560 if "STORIES" in titulo else 620, notas=("Qué se hizo", notas))

p.notas([
    "Nombres para el portal: <code>P18 FEED DD-MM Tema N.png</code> y <code>P18 ST DD-MM Tema.png</code>.",
    "En Drive: <code>S&lt;n&gt; HILTON OCT 2026 / PISO18 / {FEED, STS}</code>, igual que DT, QB y BW, "
    "con la semana de la grilla de Piso18.",
    "Todo lo producido con IA parte de una foto real de Piso18 como referencia de espacio y luz.",
], titulo="Entrega")
p.escribir()

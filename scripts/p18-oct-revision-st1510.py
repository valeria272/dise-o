#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ST 15-10 «encuesta cumpleaños», primera versión, junto a su referencia.

    python scripts/p18-oct-revision-st1510.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · ST 15-10",
    "ST 15-10 con papel y fondo nuevos, y la transición del carrusel 2027",
    "29-09-2026 · segunda versión · nada de esto se subió a Drive todavía",
    "out/piso18/oct/revision-st1510.html",
    origen="scripts/p18-oct-revision-st1510.py",
)
p.pedido(
    "Visual: sticker de encuesta con 3 paletas visuales (retro, tropical, blanco y dorado). "
    "TEXTO: ¿Cuál sería la temática de tu cumpleaños soñado? · Interacción: bloque de respuestas · "
    "Dejémos cuadro de respuesta a ver si prende",
    "Brief y cliente, en la grilla", "29-09-2026",
    que="Pasó a OK PARA DISEÑAR el 29-09.",
)
p.opciones([("raw/hilton/piso18/oct/refs/st-15-10-cumple-0.jpg", "<b>REFERENCIA</b>"),
            ("out/piso18/oct/entrega/S3/STS/P18 ST 15-10 Cumpleanos sonado.png", "<b>PISO18</b>")],
           titulo="ST 15-10 · la historia, calcada de la referencia", elige=False, ancho=460,
           notas=("Qué cambió en esta vuelta", [
               "<b>El papel</b> ahora es una textura de papel arrugado, con pliegues, fibra y manchas suaves, como el de la "
               "referencia; el borde de abajo está rasgado con mordidas hondas e irregulares, del mismo tono del papel.",
               "<b>El fondo</b> es otra foto real del salón de noche: las esferas de vidrio con velas quedan arriba, "
               "alrededor del logo, y abajo asoman las flores y la mesa. Casi sin desenfoque, para que las luces brillen.",
               "Las tres fotos de las temáticas no cambiaron."]))
p.notas([
               "Como la ref: el salón de noche de fondo, una <b>hoja de papel rasgada</b> con la pregunta arriba y una "
               "<b>tira de tres fotos</b> con marco blanco que la cruza. La hoja es el beige de Piso18 con textura de papel.",
               "Las tres fotos son las tres temáticas del brief, cada una con su nombre: <b>retro</b>, <b>tropical</b> y "
               "<b>blanco y dorado</b>. Son la misma mesa larga real de Piso18 ambientada con IA (foto de evento, sin personas): "
               "en el banco no hay cumpleaños tematizados.",
               "El papel de abajo queda libre para el <b>cuadro de respuestas</b> que pone el CM.",
               "Sin «Cotiza…» ni botón: el brief no trae CTA.",
               "La tira no se sale de la hoja por la derecha, como en la ref, porque ahí la tapa la interfaz de Instagram."],
    titulo="Cómo está hecha")

p.laminas([("out/piso18/oct/entrega/S2/FEED/P18 FEED 09-10 Fechas 2027 1.png", "<b>AHORA</b> · G1"),
           ("out/piso18/oct/entrega/S2/FEED/P18 FEED 09-10 Fechas 2027 2.png", "<b>AHORA</b> · G2")],
          titulo="FEED «Fechas 2027» · la transición del fondo negro", ancho=520,
          notas=("Qué cambió", [
              "La G2 sigue entera oscura, con el calendario, como la aprobaste.",
              "La capa negra ahora <b>empieza en la G1</b>: desde un poco más allá de la mitad se va oscureciendo hasta "
              "llegar al corte con el mismo tono de la G2. Al deslizar, el negro fluye de una lámina a la otra sin "
              "escalón (medido en el borde: 52,4 contra 52,8).",
              "El logo y la mitad izquierda de la G1 quedan como estaban."]))
p.escribir()

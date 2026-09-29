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
               "<b>tira de tres fotos</b> con marco blanco que la cruza. La hoja es el beige de Piso18 con textura
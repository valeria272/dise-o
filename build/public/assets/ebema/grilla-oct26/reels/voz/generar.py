#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Locución de los 4 reels de grilla de octubre 2026 — es-CL-LorenzoNeural.

Mismo ajuste que Paulina aprobó en la story animada del 07/10 (24-09-2026): velocidad
normal, tono +11 Hz, volumen +8 %, frases con «¡…!» y anglicismos escritos como suenan.
Los 5 reels de septiembre dicen el brief palabra por palabra (transcritos el 28-09), así
que acá se lee el «Texto / Voz off» de la grilla tal cual; sólo cambia la ortografía de
lo que el sintetizador lee mal («24/7» → «veinticuatro siete», «gift card» → «guift kard»).
Uso: python voz/generar.py
"""
import asyncio
import os

import edge_tts

AQUI = os.path.dirname(os.path.abspath(__file__))
VOZ, TONO, VOLUMEN = "es-CL-LorenzoNeural", "+11Hz", "+8%"
REELS = {
    # 01/10 · REEL — VOZ OFF IA + SUBTÍTULOS · Ebema Click
    "click": [
        "¿Sigues perdiendo horas pidiendo materiales por teléfono?",
        "¡Con Ebema Click compras online veinticuatro siete, sin filas y con despacho directo!",
        "Disponible de Santiago al sur: Rancagua, Chillán, Concepción, Temuco y Puerto Montt.",
        "¡Regístrate gratis y participa en el sorteo de una guift kard cada mes!",
    ],
    # 03/10 · REEL — VOZ OFF IA + NARRADOR · catálogo Ebema.cl
    "catalogo": [
        "Cuando tienes que cotizar materiales para distintas partidas de una obra, lo último que necesitas es perder tiempo buscando uno por uno.",
        "En Ebema punto cl puedes revisar el catálogo por categorías y encontrar los materiales que necesitas en un solo lugar.",
        "Seleccionas lo que necesitas y puedes solicitar una cotización personalizada por WhatsApp.",
        "Así puedes avanzar con lo importante: tu obra. Revisa el catálogo en Ebema punto cl. Link en la bio.",
    ],
    # 15/10 · REEL — VOZ OFF IA + SUBTÍTULOS · Perfiles Aza
    "aza": [
        "Reforzar una estructura también puede ser una decisión más consciente con el planeta.",
        "Los Perfiles Aza son ángulos estructurales fabricados con Acero Verde: acero reciclado, con menor huella de carbono y el mismo desempeño de un perfil convencional.",
        "Se sueldan y atornillan igual que un perfil convencional, para reforzar o armar cierres y estructuras.",
        "¡Perfiles Aza, disponibles en Ebema!",
    ],
    # 17/10 · REEL — VOZ OFF IA + SUBTÍTULOS · Tablero OSB LP TechShield
    "lp": [
        "Hay tableros que también trabajan por bajar la temperatura.",
        "El Tablero OSB LP Tech Shield suma una barrera que refleja el calor, además de la resistencia estructural de un OSB.",
        "Se corta e instala igual que un tablero OSB estructural, para revestir muro, piso o techumbre.",
        "¡Tablero OSB LP Tech Shield, disponible en Ebema!",
    ],
    # 27/10 · EBEMA SAN BERNARDO — ZONA OFERTAS CONSTRUCTOR (metraje real, sin IA)
    "sb": [
        "Si estás con una obra en marcha, esta zona de Ebema San Bernardo te puede ahorrar más de un peso.",
        "Acá encontrarás variedad de productos para tu obra a precios de oferta: cerámicas, pisos, aditivos, pinturas, adhesivos ¡y mucho más!",
        "Con stock disponible para llevar de inmediato y nuevas oportunidades que se renuevan cada semana.",
        "Ven a descubrir la Zona Ofertas Constructor de Ebema San Bernardo, en Avenida General Velásquez diez mil novecientos ochenta y cinco, ¡y encuentra la mejor opción para tu obra!",
    ],
}


async def main():
    for reel, lineas in REELS.items():
        for i, t in enumerate(lineas, 1):
            await edge_tts.Communicate(t, VOZ, rate="+0%", pitch=TONO, volume=VOLUMEN).save(
                os.path.join(AQUI, f"{reel}_t{i}.mp3"))


if __name__ == "__main__":
    asyncio.run(main())

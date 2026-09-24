#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Locución de la story animada Click 07/10 — es-CL-LorenzoNeural con entusiasmo.

Paulina, 24-09-2026: «no apures lo que dice, enfatiza el entusiasmo» y «gift card»
se oía «jitcar». Velocidad normal, tono +11 Hz, volumen +8 %, «¡…!» y «guift kard».
En pantalla el texto sigue siendo el del brief: esto es sólo lo que se LEE.
Uso: python voz/generar.py   (requiere edge-tts en el venv)
"""
import asyncio
import os

import edge_tts

AQUI = os.path.dirname(os.path.abspath(__file__))
VOZ, TONO, VOLUMEN = "es-CL-LorenzoNeural", "+11Hz", "+8%"
LINEAS = ["¿Cuánto tiempo pierdes abasteciéndote?",
          "¡Con Ebema Click compras online, veinticuatro siete y sin filas!",
          "¡Para ferreteros y contratistas de Santiago, Rancagua, Chillán, Concepción, Temuco y Puerto Montt!",
          "¡Y cada mes sorteamos una guift kard entre quienes compran!",
          "¡Toca el enlace!"]


async def main():
    for i, t in enumerate(LINEAS, 1):
        await edge_tts.Communicate(t, VOZ, rate="+0%", pitch=TONO, volume=VOLUMEN).save(
            os.path.join(AQUI, f"t{i}.mp3"))


if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python3
"""G.CL CAP.02 «TURNO DE NOCHE» — las cuatro líneas habladas (GUION_FINAL §5, §12, §14).

Voces neuronales chilenas de Microsoft vía edge-tts (sin clave; la misma vía que
la locución del Cap. 01 en scripts/voz-gcl.py). Es voz TEMPORAL de montaje: si
Valeria quiere actores o ElevenLabs, se reemplazan los archivos con el mismo id.

  · Pancho — es-CL-LorenzoNeural, relajado, «cero culpa»
  · Marta  — es-CL-CatalinaNeural, lenta y grave: seca, cansada, cero drama

    /Users/Vale/copylab-venv/bin/python3 scripts/gcl-cap02-voces.py

Salida: public/assets/gcl/cap02-v3/voz/<id>.mp3
"""
import asyncio, os, sys
import edge_tts

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "public/assets/gcl/cap02-v3/voz")

# id: (voz, rate, pitch, texto)
LINEAS = {
    "pancho-manana":  ("es-CL-LorenzoNeural", "-8%", "-2Hz", "Ya... lo vemos mañana."),
    "marta-otra-vez": ("es-CL-CatalinaNeural", "-22%", "-12Hz", "Otra vez."),
    "pancho-cosita":  ("es-CL-LorenzoNeural", "-6%", "+0Hz", "Oye... una cosita más."),
    "pancho-solito":  ("es-CL-LorenzoNeural", "-4%", "+2Hz", "¿Ven? Salió solito."),
}


async def main():
    os.makedirs(OUT, exist_ok=True)
    for k, (voz, rate, pitch, texto) in LINEAS.items():
        destino = os.path.join(OUT, f"{k}.mp3")
        await edge_tts.Communicate(texto, voz, rate=rate, pitch=pitch).save(destino)
        print(f"✓ {k}  ({voz}) «{texto}»")


if __name__ == "__main__":
    asyncio.run(main())

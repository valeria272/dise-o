#!/usr/bin/env python3
"""
Locución del reel de Rentas Nueva Urbe con voz sintética chilena.

POR QUÉ ESTA VOZ: se midió la del reel de septiembre del cliente
(`reel_valle_sept.mp4`) por autocorrelación — f0 mediana **138 Hz**, rango
118–174, o sea voz masculina de tono medio. `es-CL-LorenzoNeural` cae unos
puntos más grave, así que se le sube el pitch para acercarlo y, de paso, darle
el tono algo más claro que pidió Valeria.

Las cifras y la URL van escritas COMO SE LEEN: el TTS lee «$715.000» como
«dólar setecientos quince punto cero cero cero» y «rentas.inu.cl» letra por
letra mal. El texto que se muestra en pantalla sigue siendo el del brief.

Uso:  python3 scripts/rentas-voz.py [--rate -6%] [--pitch +6Hz]
"""
import argparse, asyncio, pathlib, sys
import edge_tts

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ

VOZ = "es-CL-LorenzoNeural"
DEST = pathlib.Path(RAIZ) / "public/assets/rentas/vo"

# (archivo, lo que se dice). El guion es el del brief de octubre; sólo cambia
# la ortografía de cifras y URL para que el TTS las lea bien.
LINEAS = [
    ("01_gancho",  "¿Buscando departamento en Calama? Octubre llegó con mejores condiciones."),
    ("02_areas",   "Valle Altiplánico: espacios para disfrutar todo el año."),
    ("03_precio",  "Desde setecientos quince mil pesos al mes."),
    ("04_garantia","Garantía de un mes y medio hasta en seis cuotas, y sin comisión. "
                   "Te mudas más liviano."),
    ("05_cierre",  "Agenda tu visita en rentas punto i ene u punto ce ele, "
                   "o escríbenos por WhatsApp."),
]


async def generar(rate: str, pitch: str) -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    for nombre, texto in LINEAS:
        salida = DEST / f"{nombre}.mp3"
        com = edge_tts.Communicate(texto, VOZ, rate=rate, pitch=pitch)
        await com.save(str(salida))
        print(f"  {salida.name:16s} {salida.stat().st_size // 1024:4d} KB  «{texto[:46]}…»")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--rate", default="-6%", help="más lento que el neutro: tono comercial pausado")
    ap.add_argument("--pitch", default="+26Hz", help="acerca Lorenzo a los 138 Hz medidos del cliente")
    a = ap.parse_args()
    print(f"Voz {VOZ} · rate {a.rate} · pitch {a.pitch}")
    asyncio.run(generar(a.rate, a.pitch))

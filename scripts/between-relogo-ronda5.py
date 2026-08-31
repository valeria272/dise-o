#!/usr/bin/env python3
"""
RONDA 5 (31-08-2026) — vuelve a estampar el logotipo BETWEEN, esta vez SIN deformarlo.

Por qué
-------
En la ronda 4 el logo se estampó con `between-logo-vaso.py` en su versión vieja,
que lo arqueaba sobre un cilindro y además lo metía a la fuerza en la caja que
se le diera, ignorando su proporción. El cliente lo cazó el 31-08:

    «El vaso de café tiene el logo de between completamente distinto»
    «el vaso de café nada que ver jajajaja»          — Scarlette Muñoz

Medido sobre las piezas entregadas, el logotipo salió con proporciones de
2,59 · 2,80 · 2,85 · 2,95 · 3,02 cuando la real es **3,0278**: hasta un 15 %
achatado, más el arqueo de la línea de base.

Qué hace
--------
Para cada montaje: borra el logotipo mal estampado clonando cartón limpio del
propio vaso y vuelve a ponerlo con **escala uniforme** —el alto sale de la
proporción real del archivo— y fusión multiply contra el cartón.

Las cajas están medidas a mano sobre cada imagen (rejilla de coordenadas), no
detectadas: el vaso, la mano y la tapa negra confunden a cualquier umbral.

Uso:
    python3 scripts/between-relogo-ronda5.py [--revisar]

`--revisar` deja además una tira comparativa antes/después en out/.
"""
import argparse
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
IA = RAIZ / 'public/assets/hilton/between/ia-sept'
SCRIPT = RAIZ / 'scripts/between-logo-vaso.py'

# Bloque de tinta del logotipo MAL estampado, medido sobre cada imagen.
# (x1, y1, x2, y2) — se borra con un margen y el logo nuevo se centra ahí.
# El tercer valor es de dónde se clona el cartón para borrar el logo viejo.
# 'abajo' sirve cuando el cuerpo del vaso sigue limpio bajo el logo.
# 'lados' es obligatorio en cumple-manos: arriba tiene la tapa negra y abajo los
# dedos, así que el parche sólo puede venir del cartón de los costados.
BLOQUES = {
    'togo-salida-2-logo':    ((536, 1083, 630, 1117), 'abajo'),
    'togo-cafe-dulce-logo':  ((792, 1388, 1086, 1508), 'abajo'),
    'togo-trio-45-logo':     ((1156, 1320, 1414, 1420), 'abajo'),
    'cumple-manos-logo':     ((680, 1068, 996, 1182), 'lados'),
    'cumple-vela-logo':      ((596, 1702, 926, 1818), 'abajo'),
}

# El logo ocupaba menos ancho del que manda el manual (≈55 % del vaso). No se
# toca acá: la ronda 5 reclama la FORMA, no el tamaño. Cambiarlo de paso sería
# meter una variable nueva en una entrega que ya tiene bastantes.
MARGEN = 0.18   # cuánto se agranda la zona a borrar respecto del bloque


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--revisar', action='store_true')
    args = ap.parse_args()

    for nombre, ((x1, y1, x2, y2), clonar) in BLOQUES.items():
        origen = IA / f'{nombre}.png'
        if not origen.exists():
            print(f'⚠ falta {origen.name} — se salta')
            continue

        w, h = x2 - x1, y2 - y1
        mx, my = int(w * MARGEN), int(h * MARGEN)
        limpiar = (x1 - mx, y1 - my, x2 + mx, y2 + my)
        centro = ((x1 + x2) // 2, (y1 + y2) // 2)

        cmd = [sys.executable, str(SCRIPT), str(origen), str(origen),
               '--centro', str(centro[0]), str(centro[1]),
               '--ancho', str(w),
               '--limpiar', *map(str, limpiar),
               '--clonar', clonar,
               '--fuerza', '0.95']
        print(f'· {nombre}')
        subprocess.run(cmd, check=True)

    if args.revisar:
        tira(BLOQUES)


def tira(bloques):
    """Recorta cada vaso ya corregido para mirarlos juntos."""
    from PIL import Image
    salida = RAIZ / 'out/hilton-between-relogo'
    salida.mkdir(parents=True, exist_ok=True)
    for nombre, ((x1, y1, x2, y2), _) in bloques.items():
        im = Image.open(IA / f'{nombre}.png')
        pad = int((x2 - x1) * 0.45)
        im.crop((x1 - pad, y1 - pad, x2 + pad, y2 + pad)).save(salida / f'{nombre}.png')
    print(f'\nrecortes de revisión en {salida}')


if __name__ == '__main__':
    main()

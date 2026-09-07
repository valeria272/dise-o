#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parte la foto CONTINUA del cumpleaños en los dos fondos de story.

⭐ Eli, 07-09-2026: «debe ser una transición de la foto el slide 1 y la 2».

Es la misma orden que ya había dado el 04-09 para el carrusel de feed («que sea
una continuidad con la slide dos. Puede ser solamente el fondo mismo de la
mesa»), y se resuelve igual: NO se generan dos escenas parecidas — se genera UNA
sola fotografía y se recortan los dos cuadros. Así la continuidad es real y al
deslizar la historia la cámara parece moverse por la mesa.

    origen  raw/hilton/between/ia/st-cumple-panorama-v2.png   4096 × 4096
    ST 1    mitad izquierda  → el vaso
    ST 2    mitad derecha    → el plato con las medialunas

LA GEOMETRÍA, Y POR QUÉ ES ASÍ
------------------------------
Dos cuadros 9:16 pegados dan una proporción de 1,125. Del cuadrado de 4096 salen
dos de 2048 de ancho, y entonces el alto es 2048 / 0,5625 = 3641: sobran 455 px
que hay que soltar por algún lado.

Se sueltan ABAJO. La escena se generó con el vaso y el plato en el tercio
superior y un primer plano amplio de mesa vacía, justo para poder recortar por
ahí. Soltándolos abajo el vaso queda con su tapa en y≈568 de 1920 —o sea con
aire de sobra para el titular— y la mesa limpia llega hasta el borde.

⚠️ Los dos cuadros NO se superponen: comparten el canto, así que la mesa, las
cintas y el follaje siguen de una historia a la otra sin repetir nada.

Uso:  python3 scripts/between-st-cumple-panorama.py
"""
import pathlib
import sys

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/between/ia/st-cumple-panorama-v2.png"
DESTINO = RAIZ / "public/assets/hilton/between/ia-sept"

ENTREGA = (2250, 4000)          # el master de story de Eli


def main():
    im = Image.open(ORIGEN).convert("RGB")
    w, h = im.size
    ancho = w // 2                       # 2048
    alto = round(ancho / (9 / 16))       # 3641
    if alto > h:
        sys.exit(f"ABORTA: harían falta {alto} px de alto y la foto tiene {h}.")

    for i, (nombre, x0) in enumerate((("st-cumple-1-fondo", 0),
                                      ("st-cumple-2-fondo", ancho))):
        # se suelta por ABAJO: el interés está arriba y la mesa sobra
        cuadro = im.crop((x0, 0, x0 + ancho, alto)).resize(ENTREGA, Image.LANCZOS)
        cuadro.save(DESTINO / f"{nombre}.png")
        print(f"  ✓ {nombre}.png  {cuadro.size[0]}×{cuadro.size[1]}"
              f"   (recorte x {x0}–{x0 + ancho}, y 0–{alto})")

    print(f"\n  Se soltaron {h - alto} px por abajo, de {h}.")


if __name__ == "__main__":
    main()

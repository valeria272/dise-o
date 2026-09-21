#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las mediciones de la RONDA 13 del carrusel CONCURSO de Between (21-09-2026).

La ronda entra dos cambios de contenido de Nicolás —el legal completo y la
frase con «en Between» adentro— y los dos hacen CRECER la slide 2, que es la
lámina que menos sitio tiene: abajo están la polaroid y el vaso con el logotipo
impreso, y el manual prohíbe taparlos. Todo lo que el código afirma sobre ese
encaje se comprueba acá.

    python scripts/between-concurso-s3-r13-medir.py            # las tres
    python scripts/between-concurso-s3-r13-medir.py frase      # la cita
    python scripts/between-concurso-s3-r13-medir.py legal      # el párrafo
    python scripts/between-concurso-s3-r13-medir.py encaje     # sobre el render
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFont

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "public/assets/hilton/between/fonts"
BOLD = FUENTES / "Raleway-Bold.ttf"
SEMI_IT = FUENTES / "Raleway-SemiBoldItalic.ttf"

#: Tarjeta medida sobre `C1 S2 CUMPLE N2.png`: 686 de ancho, 28 de relleno.
UTIL = 686 - 28 * 2                      # 630 px de ancho de texto
#: Escala de medición. `getlength` redondea al entero de píxel del cuerpo que
#: se le pide, así que se mide 8× y se divide: el error baja de 1 px a 0,125.
ESC = 8

FRASE_L1 = "«Si yo fuera CEO del café en Between,"
FRASE_L2 = "mi primera acción sería…»"
#: El corte alternativo que se evaluó y se botó: parte la marca de su «en».
ALT_L1 = "«Si yo fuera CEO del café"
ALT_L2 = "en Between, mi primera acción sería…»"

LEGAL = (
    "*Concurso válido del 21 al 30 de septiembre. El ganador será anunciado "
    "el 1 de octubre. Premio: un café diario, para disfrutar en local o en "
    "formato To Go durante todo el mes de octubre de 2026. Premio personal e "
    "intransferible."
)


def ancho(texto: str, ruta: Path, px: int, tracking_em: float = 0.0) -> float:
    """Ancho de una línea en px del lienzo de 1080, con el tracking de CSS."""
    f = ImageFont.truetype(str(ruta), px * ESC)
    return f.getlength(texto) / ESC + tracking_em * px * len(texto)


def envolver(texto: str, ruta: Path, px: int, maximo: float, tracking_em=0.0):
    """El salto de línea de Chrome: palabra por palabra, sin partir palabras."""
    f = ImageFont.truetype(str(ruta), px * ESC)

    def w(s):
        return f.getlength(s) / ESC + tracking_em * px * len(s)

    lineas, act = [], ""
    for palabra in texto.split(" "):
        tentativa = (act + " " + palabra).strip()
        if w(tentativa) <= maximo or not act:
            act = tentativa
        else:
            lineas.append(act)
            act = palabra
    lineas.append(act)
    return [(l, w(l)) for l in lineas]


def frase() -> None:
    """¿A qué cuerpo la cita sigue cabiendo en DOS líneas?"""
    print(f"LA CITA — ancho útil de la tarjeta: {UTIL} px\n")
    print("  corte en la coma (el que va):")
    for px in (36, 35, 34, 33):
        w1 = ancho(FRASE_L1, BOLD, px, -0.012)
        w2 = ancho(FRASE_L2, BOLD, px, -0.012)
        veredicto = "entra" if w1 <= UTIL else "SE PARTE → 3 líneas"
        print(f"    cuerpo {px}:  {w1:6.1f} / {w2:6.1f}   {veredicto}")
    print("\n  corte antes de «en Between» (descartado, parte la marca):")
    w1 = ancho(ALT_L1, BOLD, 36, -0.012)
    w2 = ancho(ALT_L2, BOLD, 36, -0.012)
    print(f"    cuerpo 36:  {w1:6.1f} / {w2:6.1f}   "
          f"{'entra' if w2 <= UTIL else 'SE PARTE → 3 líneas'}")
    print(f"\n  → va a 34: {ancho(FRASE_L1, BOLD, 34, -0.012):.1f} px, "
          f"{UTIL - ancho(FRASE_L1, BOLD, 34, -0.012):.1f} px de aire.")


def legal() -> None:
    """¿A qué cuerpo el legal entero entra en TRES líneas?

    Es la pregunta que dejó Eli: «achica un poco más el texto del legal… al
    menos en 3 líneas que quede, sin quitar texto». La respuesta no se elige,
    se mide — y 17 es el cuerpo MÁS GRANDE que lo consigue.
    """
    print(f"EL LEGAL — ancho útil {UTIL} px, interlineado 1,34\n")
    elegido = None
    for px in (21, 18, 17, 16, 15):
        lineas = envolver(LEGAL, SEMI_IT, px, UTIL)
        alto = len(lineas) * px * 1.34
        marca = ""
        if len(lineas) <= 3 and elegido is None:
            elegido, marca = px, "   ← el que va (el mayor que entra en 3)"
        print(f"  cuerpo {px}:  {len(lineas)} líneas · {alto:5.1f} px de alto{marca}")
        for l, w in lineas:
            print(f"      {w:6.1f}  {l}")
        print()

    lineas = envolver(LEGAL, SEMI_IT, elegido, UTIL)
    alto = len(lineas) * elegido * 1.34
    antes = 2 * 21 * 1.34          # el legal de dos frases de la ronda 12
    print(f"  el legal de la r12 eran 2 líneas a 21 px · {antes:.1f} px")
    print(f"  el de ahora son {len(lineas)} a {elegido} px · {alto:.1f} px"
          f"   →   +{alto - antes:.1f} px")
    print("  la cita, 36 → 34                              −5,0")
    print(f"  ──────────────────────────────────────────── +{alto - antes - 5:.1f}")
    print("\n  Por eso la lámina VUELVE a su geometría aprobada: titular 150,")
    print("  tarjeta 320, separadores 18/14. Con cuatro líneas hubo que moverlos")
    print("  28 px hacia arriba; con tres no hace falta, y lo que no hace falta")
    print("  se devuelve.")


def encaje(ruta: Path | None = None) -> None:
    """Sobre el render: dónde cierra la tarjeta y qué hay debajo."""
    p = ruta or (RAIZ / "out/hilton/between/concurso-s3-r13/slide2.png")
    if not p.is_file():
        print(f"✗ falta el render {p}")
        return
    im = Image.open(p).convert("RGB")
    a = np.asarray(im).astype(int)
    k = im.width / 1080.0
    print(f"EL ENCAJE — medido sobre {p.name} ({im.width}×{im.height})\n")

    # La tarjeta es crema #FFF9EB. Se lee en x=870, que es marco sin tinta.
    crema = np.abs(a - np.array([255, 249, 235])).sum(axis=2) < 18
    ys = np.where(crema[: int(1000 * k), int(870 * k)])[0]
    arriba, abajo = ys.min() / k, ys.max() / k
    print(f"  tarjeta            y {arriba:6.1f} → {abajo:6.1f}   (alto {abajo - arriba:.1f})")

    # El titular es tinta café sobre el papel, arriba de la tarjeta.
    tinta = np.abs(a[: int(int(arriba - 5) * k), :] - np.array([103, 91, 73])).sum(axis=2) < 90
    yt = np.where(tinta)[0]
    print(f"  tinta del titular  y {yt.min() / k:6.1f} → {yt.max() / k:6.1f}"
          f"   (margen de marca: 84)")
    print(f"  aire titular → tarjeta                {arriba - yt.max() / k:5.1f} px")

    # Lo que hay DEBAJO en las columnas de la tarjeta: el marco blanco del
    # recorte y el de la polaroid. Es el techo que la tarjeta no puede cruzar.
    franja = a[:, int(197 * k): int(883 * k)]
    for y in range(int(abajo) + 1, 1080):
        fila = franja[int(y * k)]
        if (fila.min(axis=1) > 238).sum() > 40:
            print(f"  primer blanco debajo               y {y:6.1f}"
                  f"   → {y - abajo:5.1f} px de aire")
            break
    else:
        print("  no hay nada blanco debajo hasta y=1080")


if __name__ == "__main__":
    cual = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if cual in ("frase", "todo"):
        frase()
        print()
    if cual in ("legal", "todo"):
        legal()
        print()
    if cual in ("encaje", "todo"):
        encaje()

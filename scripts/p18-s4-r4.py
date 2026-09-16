#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PISO18 · S4 · RONDA 4 — los recortes de foto que pidió el cliente el 16-09.

    python scripts/p18-s4-r4.py

Tres piezas de la S4 quedaron **EN CAMBIOS** en la grilla del 16-09 por un
motivo de FOTOGRAFÍA, no de diagramación. Este script produce los tres recortes;
la encuesta y la animada se rinden después con `scripts/p18-rendir.py`.

════════════════════════════════════════════════════════════════════════════
1 · CARRUSEL (FEED 21-09) — «Hagámosle + zoom a la G3 para que no sea tan
    protagonista el mesón, el resto OK!»
════════════════════════════════════════════════════════════════════════════
La G3 es `piso_18-100`: el arreglo alto sobre la mesa de madera. El recorte
entregado era **ancho completo** (3840 px) desde y=256, y por eso entraba el
mesón entero **con patas**: el tablero caía al 63 % del alto y las patas se
comían el tercio inferior.

El recorte nuevo cierra sobre el arreglo: 3199×4000 desde la esquina superior
izquierda. El tablero baja al **85 %** del alto —queda de base, no de
protagonista— y **el arreglo no se toca**: las pampas siguen enteras arriba
porque el recorte sube a y=0 en vez de bajar el corte.

⚠️ Reduce a 0,703 (3199 → 2250). **No amplía nada.** Las otras tres G no se
tocan: «el resto OK!».

════════════════════════════════════════════════════════════════════════════
2 · ENCUESTA (STORIES 25-09) — «En la B, pongamos una opción más de mesa para
    cenar, ya que las otras 2 propuestas son más de esa onda.»
════════════════════════════════════════════════════════════════════════════
Tenía razón, y se ve en la pieza: la A y la C son **centros de mesa puestos**
—con copas, platos y mantel—, y la B era el arreglo del **mesón** suelto, con
patas y piso. No es el mismo tipo de montaje, así que no se pueden comparar.

La B nueva sale de `piso_18-28`: mantel negro, bajoplato dorado, copas moradas
y un centro bajo de rosas crema y palo rosa con vela. Es mesa para cenar, como
las otras dos.

⭐ Y NO se eligió `piso_18-85`, que también es mesa para cenar y era la primera
opción: **es el mismo montaje de la G1 del carrusel** (`piso_18-72`, la mesa
larga con tulipanes, globos de vidrio y copa azul). Carrusel el 21 y encuesta
el 25 con la misma escena a cuatro días es repetir el feed. La `28` es un
tercer montaje: negro y dorado, formal, y las rosas clásicas no se parecen ni
a la pampa seca de la A ni al blanco y verde de la C.

Geometría heredada de las otras dos tiras: 536×1400 (la tira es 268×700 en la
mesa de 1080, y se entrega a 2250). El ramo queda a media anchura y cae al
40 % del alto, que es como se calcularon la A y la C para que las tres se lean
a la misma escala.

════════════════════════════════════════════════════════════════════════════
3 · POST DE FEED (25-09) — «Que sea esta foto, con logo y estamos»
════════════════════════════════════════════════════════════════════════════
El enlace que dejó el cliente es
`drive.google.com/file/d/1XIfam4-nFartLYN3yrf0iCumzQt-s6EP` = **`piso_18-128.jpg`**
(5760×3840, 16,9 MB, de la sesión 28/AGO de Eli). Ya estaba en el estudio, en
`raw/hilton/piso18/deco-ago2024/` — mismo tamaño en bytes que el de Drive.

Es horizontal y el feed de esta marca es 4:5, así que se recorta a alto
completo (3071×3840) y se abre hacia la **izquierda**, que es donde está el
salón: mesas vestidas, sillas y los ventanales. Eso responde el comentario
anterior del mismo hilo —*«tenemos opciones con planos más amplios? la idea de
estas gráficas simples es principalmente mostrar el espacio»*— y el de
*«que sean de ambiente, sin caras directas»*: no hay una sola persona.

⭐ Y el recorte izquierdo además resuelve el logotipo: la banda donde va
(y 190–480) queda en **luminancia 20–35 por tercios** —techo oscuro—, contra
88 del recorte centrado, que cae sobre las flores claras. Blanco sobre eso se
lee; sobre las flores, no.

Logotipo: ancho 568 px y tope y=218, centrado. No es un número puesto a ojo —
es el de la G1 ya aprobada, medido por correlación de plantilla sobre ella, y
coincide con la geometría de marca (272 y 105 en la mesa de 1080, ×2,0833).

⚠️ `piso_18-128` es también el **tercer plano de la historia animada del 23-09**.
El cliente eligió esta foto con nombre y apellido, así que se usa; queda
anotado para que Eli decida si cambia el plano de la animada.
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

Image.MAX_IMAGE_PIXELS = None

RAIZ = Path(__file__).resolve().parent.parent
BANCO = RAIZ / "raw/hilton/piso18/deco-ago2024"
ASSETS = RAIZ / "public/assets/hilton/piso18"
SALIDA = RAIZ / "out/piso18/s4"

# Máster de feed de la cuenta, medido sobre las piezas aprobadas.
FEED = (2250, 2813)
# La tira de la encuesta, heredada de la A y la C.
TIRA = (536, 1400)


def recorta(origen: Path, caja: tuple[int, int, int, int], destino: Path,
            tamano: tuple[int, int], calidad: int = 95) -> Image.Image:
    """Recorta, reduce y guarda. Avisa si alguna vez tuviera que ampliar."""
    im = Image.open(origen)
    x0, y0, x1, y1 = caja
    escala = tamano[0] / (x1 - x0)
    if escala > 1.0:
        raise SystemExit(f"✗ {destino.name} AMPLIARÍA ×{escala:.2f} — busca otro recorte")
    out = im.crop(caja).resize(tamano, Image.LANCZOS)
    destino.parent.mkdir(parents=True, exist_ok=True)
    if destino.suffix.lower() in {".jpg", ".jpeg"}:
        out.convert("RGB").save(destino, quality=calidad, subsampling=0)
    else:
        out.convert("RGB").save(destino)
    print(f"  ✓ {destino.relative_to(RAIZ)}  {tamano[0]}×{tamano[1]}  "
          f"(recorte {x1-x0}×{y1-y0}, reduce a {escala:.3f})")
    return out


def main() -> int:
    print("PISO18 · S4 · ronda 4 — recortes de foto\n")

    # ── 1 · La G3 del carrusel, con más zoom ────────────────────────────
    print("1 · carrusel G3 — menos mesón, el arreglo entero")
    recorta(BANCO / "piso_18-100.jpg", (0, 0, 3199, 4000),
            SALIDA / "slide3.jpg", FEED)
    recorta(BANCO / "piso_18-100.jpg", (0, 0, 3199, 4000),
            SALIDA / "entrega/C1 S4 PISO18/C1 S4 N°3.png", FEED)

    # ── 2 · La opción B de la encuesta ──────────────────────────────────
    print("\n2 · encuesta opción B — mesa para cenar (piso_18-28)")
    recorta(BANCO / "piso_18-28.jpg", (2182, 700, 3618, 4450),
            ASSETS / "tira-b.jpg", TIRA)

    # ── 3 · El post del 25-09 ───────────────────────────────────────────
    print("\n3 · post 25-09 — la foto que pidió el cliente, con logotipo")
    foto = recorta(BANCO / "piso_18-128.jpg", (365, 0, 3436, 3840),
                   ASSETS / "post-espacio.jpg", FEED)

    logo = Image.open(ASSETS / "logo.png").convert("RGBA")
    ancho = 568
    alto = int(round(ancho / 2.482456))          # proporción real del logotipo
    logo = logo.resize((ancho, alto), Image.LANCZOS)
    pieza = foto.convert("RGBA")
    pieza.alpha_composite(logo, ((FEED[0] - ancho) // 2, 218))
    destino = SALIDA / "entrega/Post n°2 S4 PISO18 25-09.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    pieza.convert("RGB").save(destino)
    print(f"  ✓ {destino.relative_to(RAIZ)}  logotipo {ancho}×{alto} en y=218, centrado")

    print("\nListo. Falta rendir la encuesta y la animada:  python scripts/p18-rendir.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

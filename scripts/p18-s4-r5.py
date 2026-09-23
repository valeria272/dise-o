#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PISO18 · S4 · RONDA 5 — los dos cambios que pidió Eli el 16-09 sobre el carrusel.

    python scripts/p18-s4-r5.py

    «Las historias quedaron ok. Para el carrusel necesito que la foto que te junté
     la aumentes más el zoom. No tiene que verse en los costados ni la mesa. La idea
     es que se vea la captura que te dejé. […] Y para la portada necesito que
     oscurezcas un poco arriba con una transparencia muy sutil para que el logo se
     pueda visualizar de mejor manera. Con opacidad. La idea es que el logo se vea
     mucho mejor, visible.»

════════════════════════════════════════════════════════════════════════════
1 · LA G3 — más zoom todavía, y ahora con una captura de referencia
════════════════════════════════════════════════════════════════════════════
La ronda 4 ya había cerrado el recorte, pero se quedó corta: seguía entrando el
mesón como mueble y una franja de ventanal a cada lado. Eli mandó una captura con
el encuadre que quiere, y el recorte se dedujo de ella, no a ojo — se midieron
tres puntos de la foto que aparecen en los dos encuadres (la boca de la vasija,
la base del farol de alambre y el canto del tablero) y de ahí salió la caja.

| | Ronda 4 | Ronda 5 |
|---|---|---|
| Caja en el original | 3199×4000 desde (0,0) | **2300×2876 desde (600,704)** |
| Reduce a | 0,703 | **0,978** |
| Mesa | tablero al 85 % del alto | **sólo la superficie, al borde inferior** |
| Costados | ventanal a la derecha | **un filo** |

⚠️ 0,978 es casi 1:1. **Es el último recorte posible sin ampliar**: cualquier
zoom mayor sobre esta foto ya interpola y se va a ver blando. Si Eli pidiera más,
hay que volver al banco a buscar un plano más cerrado, no forzar éste.

════════════════════════════════════════════════════════════════════════════
2 · LA PORTADA — el velo que la marca YA tiene
════════════════════════════════════════════════════════════════════════════
El problema está medido: en la banda donde va el logotipo (y 190–480 de 2813) la
luminancia por TERCIOS es 78 / 82 / **95**, y el percentil 90 del peor tercio es
**253** — o sea que detrás del logotipo blanco hay globos de vidrio y follaje
iluminado que llegan a blanco puro. Por eso no se lee: no es que esté oscuro, es
que hay reflejos del mismo valor que la tinta.

⭐ Y el velo **no se inventa**: es el que la marca ya usa. `logo PISO18.png` no es
un logotipo suelto, es una plantilla de historia 2250×4000 con un **velo negro en
degradado, alfa 150 en y=0 que llega a 0 en y≈1667** — el 41,7 % del alto. Acá se
aplica ese mismo velo, con la misma proporción, sobre el 4:5:

    alfa 0,588 en y=0  →  0 en y = 0,417 × 2813 = 1173

A la altura del logotipo (su centro cae en y=332) eso da **alfa 0,42**, que baja
el peor tercio de 95 a unos 55. Se ve como lo que Eli pidió —«un poco», «muy
sutil»— porque el degradado se desvanece antes del primer tercio de la pieza, y
al mismo tiempo es suficiente para que el blanco despegue.

⛔ El velo va **debajo** del logotipo, así que la portada se rehace desde la foto
limpia. El `slide1.jpg` entregado ya trae el logotipo estampado: si se velara
encima, el logotipo blanco se apagaría junto con el fondo. El recorte original se
recuperó por correlación contra la foto de origen: `piso_18-72`, ancho completo,
**y=594** (residuo 2,0 sobre 255, que es ruido de JPEG).

⚠️ Sólo lleva velo la PORTADA. Las otras tres no tienen logotipo y el brief las
quiere limpias.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
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

FEED = (2250, 2813)

# El velo de la marca, medido sobre `logo PISO18.png`.
VELO_ALFA = 150 / 255          # 0,588 en el borde superior
VELO_HASTA = 0.417             # llega a 0 al 41,7 % del alto

# Logotipo en feed: medido por correlación sobre la G1 aprobada, y coincide con
# la geometría de marca (272 px y tope 105 en la mesa de 1080, ×2,0833).
LOGO_ANCHO = 568
LOGO_Y = 218
LOGO_PROPORCION = 2.482456


def recorta(origen: Path, caja: tuple[int, int, int, int]) -> Image.Image:
    im = Image.open(origen)
    escala = FEED[0] / (caja[2] - caja[0])
    if escala > 1.0:
        raise SystemExit(
            f"✗ {origen.name} AMPLIARÍA ×{escala:.3f}. No se fuerza un recorte: "
            f"se busca otro plano en el banco.")
    print(f"     recorte {caja[2]-caja[0]}×{caja[3]-caja[1]} desde "
          f"({caja[0]},{caja[1]}) · reduce a {escala:.3f}")
    return im.crop(caja).resize(FEED, Image.LANCZOS)


def luminancia_por_tercios(im: Image.Image) -> list[float]:
    """La banda del logotipo, medida por tercios. El promedio de la franja miente:
    manda el peor tercio, que es donde el blanco se pierde."""
    a = np.asarray(im.convert("L"), dtype=np.float32)[190:480, 780:1470]
    n = a.shape[1] // 3
    return [float(a[:, i * n:(i + 1) * n].mean()) for i in range(3)]


def velo(im: Image.Image) -> Image.Image:
    """El velo de marca: negro en degradado lineal de arriba hacia abajo."""
    alto = im.size[1]
    hasta = int(round(alto * VELO_HASTA))
    columna = np.zeros(alto, dtype=np.float32)
    columna[:hasta] = np.linspace(VELO_ALFA, 0.0, hasta)
    alfa = np.repeat(columna[:, None], im.size[0], axis=1)[:, :, None]
    base = np.asarray(im.convert("RGB"), dtype=np.float32)
    return Image.fromarray(np.clip(base * (1.0 - alfa), 0, 255).astype(np.uint8))


def pon_logo(im: Image.Image) -> Image.Image:
    logo = Image.open(ASSETS / "logo.png").convert("RGBA")
    alto = int(round(LOGO_ANCHO / LOGO_PROPORCION))
    logo = logo.resize((LOGO_ANCHO, alto), Image.LANCZOS)
    sobre = im.convert("RGBA")
    sobre.alpha_composite(logo, ((FEED[0] - LOGO_ANCHO) // 2, LOGO_Y))
    return sobre.convert("RGB")


def main() -> int:
    print("PISO18 · S4 · ronda 5 — el carrusel\n")
    entrega = SALIDA / "entrega/C1 S4 PISO18"
    entrega.mkdir(parents=True, exist_ok=True)

    # ── 1 · G3 ──────────────────────────────────────────────────────────
    print("1 · G3 — el encuadre de la captura que mandó Eli")
    g3 = recorta(BANCO / "piso_18-100.jpg", (600, 704, 2900, 3580))
    g3.save(SALIDA / "slide3.jpg", quality=95, subsampling=0)
    g3.save(entrega / "C1 S4 N°3.png")
    print("     ✓ C1 S4 N°3.png")

    # ── 2 · portada ─────────────────────────────────────────────────────
    print("\n2 · G1 — el velo de marca, para que el logotipo despegue")
    limpia = recorta(BANCO / "piso_18-72.jpg", (0, 594, 3840, 5395))
    antes = luminancia_por_tercios(limpia)
    velada = velo(limpia)
    ahora = luminancia_por_tercios(velada)
    print(f"     banda del logotipo, luminancia por tercios:")
    print(f"       antes  {[round(v, 1) for v in antes]}  · peor {max(antes):.1f}")
    print(f"       ahora  {[round(v, 1) for v in ahora]}  · peor {max(ahora):.1f}")
    g1 = pon_logo(velada)
    g1.save(SALIDA / "slide1.jpg", quality=95, subsampling=0)
    g1.save(entrega / "C1 S4 N°1.png")
    print("     ✓ C1 S4 N°1.png")

    print("\nListo. Las G2 y G4 no se tocan.")
    print("Sube con:  python scripts/p18-s4-subir.py --solo \"C1 S4 N°1.png\" \"C1 S4 N°3.png\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

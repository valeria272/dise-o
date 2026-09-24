#!/usr/bin/env python3
"""Prepara las versiones de MAPA-3 que usan las piezas de octubre.

    python scripts/tc-mapas-duotono.py

POR QUÉ EXISTE: `MAPA-3` es la **única cartografía real** que tiene la cuenta —
`MAPA-1` y `MAPA-2` salieron de IA y traen topónimos corruptos y escudos G-68
alrededor de Padre Hurtado, el error que el manual persigue hace meses—. Pero es
una captura de Google Maps: blanca, saturada y con su propia tipografía, así que
no se puede pegar tal cual sobre una pieza de marca.

⭐ EL CAMBIO DEL 24-09 (2ª vuelta): EL MAPA ES UN OBJETO, NO UN FONDO
─────────────────────────────────────────────────────────────────────
Diego, sobre la story: *"mejoremos la forma en que mostramos el mapa, que se vea
integrado de buena forma y que se lea bien, quita el pin de Tierra Calma, solo
deja el del mapa original"*. Y sobre la slide 2 del carrusel: *"quitar pin de
Tierra Calma, que sea fondo sólido con el color verde de la marca más un
**recuadro** con el mapa del lugar"*.

Son el mismo pedido dicho dos veces, y cambia tres cosas de raíz:

1. **El mapa se recorta a un rectángulo declarado.** Antes iba a sangre (slide 2)
   o difuminado con una máscara radial (story): en los dos casos leía como una
   mancha, no como un mapa. Ahora cada pieza recibe **su propio recorte**, con
   las proporciones exactas de su caja, y el archivo se muestra 1:1 — sin
   `objectPosition` buscando el pin a ojo.
2. **El duotono se da vuelta: el mapa es PAPEL, no velo.** Antes el mapa era
   oscuro sobre fondo oscuro y los topónimos no se leían. Ahora la luz del
   duotono es el crema de marca, así que el recuadro es lo más claro de la
   pieza y la cartografía se lee.
3. ⭐ **EL PIN ROJO SOBREVIVE AL DUOTONO.** Es el punto entero del pedido: el
   mapa YA trae el pin y YA dice «Tierra Calma» —es un lugar registrado en
   Google Maps—, así que nuestro rótulo encima era una segunda marca tapando la
   primera. Un duotono por luminancia convierte ese rojo en un gris cualquiera,
   así que acá se **aísla y se repone en su color**: es lo único cromático de
   la pieza y por eso es lo primero que se mira.

   ⚠️ Se repone SÓLO el rojo de la zona del pin. El mapa trae otro rojo —el POI
   «CESFAM Presidenta Michelle Bachelet»— que no es nuestro y tiene que
   apagarse con el resto.

| Salida | Para | Tratamiento |
|---|---|---|
| `mapa3-recuadro-st.jpg` | `st-12-10` | recorte 800×297 · duotono navy→crema · pin vivo |
| `mapa3-recuadro-k2.jpg` | `c-20-10-2` | recorte 800×423 · duotono verde→crema · pin vivo |

🗄️ Retirados el 24-09 (los archivos siguen en disco, ya no los genera nadie):
`mapa3-verde.jpg` (slide 2 a sangre) · `mapa3-cuadro.jpg` (story con máscara) ·
`mapa3-story.jpg`. El día que llegue el mapa oficial de Carlos se cambia
`mapa3.jpg` y se corre esto: las dos piezas se rehacen solas.
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OCT = pathlib.Path(RAIZ) / "public/assets/tierracalma/oct"

# El pin rojo de «Tierra Calma» en mapa3.jpg (1170×711), medido sobre el archivo.
PIN = (287, 315)
# La caja que contiene el pin Y su etiqueta roja. Fuera de acá el rojo se apaga:
# el POI del CESFAM (x 650-830, y 145-185) no es nuestro.
PIN_ZONA = (262, 286, 402, 346)

# Recortes, medidos sobre mapa3.jpg. La proporción de cada uno es la de su caja
# en la pieza, así que el archivo se muestra 1:1 y nadie reencuadra después.
#
#   story     888 × 345  → 2,574 : 1
#   carrusel  888 × 470  → 1,889 : 1
#
# Qué tiene que entrar, y por qué:
#   · el pin (287,315) con aire a su alrededor
#   · «Padre Hurtado» (690,365) — el topónimo que la pieza nombra
#   · el escudo de la **Ruta 78** (687,263) — la vía correcta, la que el manual
#     persigue desde que una pieza publicó «Ruta 68»
#   · «Maipú» (855,120) — el ancla de Santiago que sostiene el titular
#   · en el carrusel, además Peñaflor (459,515) y el segundo escudo 78 (549,411)
RECORTES = {
    "mapa3-recuadro-st": {
        "caja": (150, 88, 950, 399),
        "duo": ("#0B2C49", "#F3EEE3"),  # navy → crema · story sobre navy
        "pieza": "st-12-10 · caja 888×345",
    },
    "mapa3-recuadro-k2": {
        "caja": (150, 60, 950, 483),
        "duo": ("#00291E", "#F3EEE3"),  # verde profundo → crema · slide sobre verde
        "pieza": "c-20-10-2 · caja 888×470",
    },
}


def _rgb(hex_: str) -> np.ndarray:
    return np.array([int(hex_[i : i + 2], 16) for i in (1, 3, 5)], dtype=float)


def duotono(a: np.ndarray, sombra: str, luz: str) -> np.ndarray:
    """Mapea la luminancia entre dos colores de marca. Entra y sale float RGB."""
    g = (0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]) / 255.0
    s, l = _rgb(sombra), _rgb(luz)
    return s[None, None, :] + g[:, :, None] * (l - s)[None, None, :]


def alfa_del_pin(a: np.ndarray, zona: tuple[int, int, int, int]) -> np.ndarray:
    """Cuánto de cada píxel es «rojo del pin», de 0 a 1.

    Se usa como alfa —no como máscara dura— para que el antialias del pin y de
    la tipografía de la etiqueta se funda con el duotono en vez de quedar con
    borde de recorte.
    """
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    # «rojez» = cuánto supera el rojo al más alto de los otros dos canales
    rojez = (r - np.maximum(g, b)) / 90.0
    alfa = np.clip(rojez, 0, 1)
    alfa[r < 110] = 0  # sombras oscuras que casualmente tiran a rojo
    fuera = np.ones_like(alfa, dtype=bool)
    x0, y0, x1, y1 = zona
    fuera[y0:y1, x0:x1] = False
    alfa[fuera] = 0
    return alfa


def main() -> int:
    origen = OCT / "mapa3.jpg"
    if not origen.exists():
        print(f"✗ Falta {origen}")
        return 1
    base = Image.open(origen).convert("RGB")
    a = np.asarray(base).astype(float)
    print(f"MAPA-3: {base.size[0]}×{base.size[1]}  ·  pin en {PIN}")

    alfa = alfa_del_pin(a, PIN_ZONA)
    ys, xs = np.nonzero(alfa > 0.25)
    if len(xs) == 0:
        print("✗ No se encontró el pin rojo en PIN_ZONA — revisar mapa3.jpg")
        return 1
    print(f"· pin + etiqueta: {len(xs)} px en x {xs.min()}-{xs.max()} · y {ys.min()}-{ys.max()}")

    for nombre, cfg in RECORTES.items():
        x0, y0, x1, y1 = cfg["caja"]
        sub, alf = a[y0:y1, x0:x1], alfa[y0:y1, x0:x1, None]
        # duotono en todo, y encima el pin en su color original
        out = duotono(sub, *cfg["duo"]) * (1 - alf) + sub * alf
        Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(OCT / f"{nombre}.jpg", quality=92)
        w, h = x1 - x0, y1 - y0
        fx, fy = (PIN[0] - x0) / w, (PIN[1] - y0) / h
        print(f"· {nombre}.jpg  {w}×{h} ({w / h:.3f}:1) desde ({x0},{y0})  →  {cfg['pieza']}")
        print(f"    duotono {cfg['duo'][0]} → {cfg['duo'][1]} · pin vivo en ({fx:.3f}, {fy:.3f})")
        if not (0.08 < fx < 0.92 and 0.08 < fy < 0.92):
            print("    ⚠️ el pin quedó pegado a un borde del recorte")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

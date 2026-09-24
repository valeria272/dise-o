#!/usr/bin/env python3
"""Prepara las versiones de MAPA-3 que usan las piezas de octubre.

    python scripts/tc-mapas-duotono.py

POR QUÉ EXISTE: `MAPA-3` es la **única cartografía real** que tiene la cuenta —
`MAPA-1` y `MAPA-2` salieron de IA y traen topónimos corruptos y escudos G-68
alrededor de Padre Hurtado, el error que el manual persigue hace meses—. Pero es
una captura de Google Maps: blanca, saturada y con su propia tipografía, así que
no se puede pegar tal cual sobre una pieza de marca.

Cada pieza necesita una versión distinta, y las tres se generan acá para que el
día que llegue el mapa oficial de Carlos se cambie **un archivo** y no tres
recetas escritas en tres composiciones:

| Salida | Para | Tratamiento |
|---|---|---|
| `mapa3-verde.jpg` | `c-20-10-2` | duotono VERDE de marca, a sangre |
| `mapa3-cuadro.jpg` | `st-12-10` | recorte centrado en el pin + duotono navy |
| `mapa3-story.jpg` | *(histórico)* | el que usaba la story antes del rediseño |

⛔ **El pin rojo del mapa NO se borra.** Diego, 24-09-2026: *"tapa el pin del mapa
con nuestro rótulo"*. Por eso `mapa3-cuadro` deja el pin en una posición
**conocida y fija** —se imprime al final— y la composición pone el rótulo encima.
Recortar el mapa a mano en cada pieza y después buscar el pin con `objectPosition`
es lo que hacía que se leyeran dos marcas.
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

# El pin rojo de «Tierra Calma» en mapa3.jpg, medido sobre el archivo.
PIN = (287, 315)


def duotono(im: Image.Image, sombra: str, luz: str) -> Image.Image:
    """Mapea la luminancia entre dos colores de marca."""
    g = np.asarray(im.convert("L")).astype(float) / 255.0
    s = np.array([int(sombra[i : i + 2], 16) for i in (1, 3, 5)], dtype=float)
    l = np.array([int(luz[i : i + 2], 16) for i in (1, 3, 5)], dtype=float)
    out = s[None, None, :] + g[:, :, None] * (l - s)[None, None, :]
    return Image.fromarray(out.clip(0, 255).astype(np.uint8))


def main() -> int:
    origen = OCT / "mapa3.jpg"
    if not origen.exists():
        print(f"✗ Falta {origen}")
        return 1
    base = Image.open(origen).convert("RGB")
    w, h = base.size
    print(f"MAPA-3: {w}×{h}  ·  pin en {PIN}")

    # ── 1. El verde de la slide 2 ────────────────────────────────────────────
    # Diego (24-09): "las slides 2 y 3 quedan muy cortadas de las demás, cambiar
    # por el color verde del manual". La slide tiene que LEERSE verde, así que el
    # duotono va de verde profundo a un verde grisáceo claro: el mapa sigue
    # legible y el texto crema despega.
    verde = duotono(base, "#00291E", "#A8BFAE")
    verde.save(OCT / "mapa3-verde.jpg", quality=90)
    print(f"· mapa3-verde.jpg   duotono #00291E → #A8BFAE")

    # ── 2. El recorte de la story, centrado en el pin ────────────────────────
    # La caja de la story es 530×470 (1,128). Se recorta a esa proporción
    # dejando el pin adentro y con aire, y se deja dicho DÓNDE quedó.
    cw, ch = 800, 709
    x0, y0 = max(0, min(PIN[0] - int(cw * 0.36), w - cw)), max(0, min(PIN[1] - int(ch * 0.44), h - ch))
    cuadro = base.crop((x0, y0, x0 + cw, y0 + ch))
    duotono(cuadro, "#08233C", "#BFCBD6").save(OCT / "mapa3-cuadro.jpg", quality=90)
    fx, fy = (PIN[0] - x0) / cw, (PIN[1] - y0) / ch
    print(f"· mapa3-cuadro.jpg  recorte {cw}×{ch} desde ({x0},{y0}) · duotono navy")
    print(f"\n  ⭐ EL PIN QUEDÓ EN LA FRACCIÓN ({fx:.4f}, {fy:.4f}) del recorte.")
    print(f"     En una caja de 530×470 eso es ({fx*530:.0f}, {fy*470:.0f}) px.")
    print(f"     Ahí va NUESTRO rótulo, encima del pin del mapa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

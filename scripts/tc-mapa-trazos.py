#!/usr/bin/env python3
"""Convierte `MAPA-PADRE HURTADO` en un mapa DE TRAZOS para `st-12-10`.

    python scripts/tc-mapa-trazos.py [--probar]

POR QUÉ EXISTE: Diego, 25-09-2026: *"necesito que el mapa [sea] en trazos, ocupa
el MAPA-PADRE HURTADO para generar esa parte del contenido"*.

⛔ **TRAZAR NO ES DIBUJAR.** El 23-09 se rechazó un mapa de celdas inventado
(*"el mapa no es así realmente"*). Acá no se inventa nada: la geometría sale
**píxel a píxel del archivo real** que subió Diego —una captura de Google Maps
centrada en Padre Hurtado— y lo único que se cambia es la TINTA. Si mañana
llega el mapa oficial de Carlos, se reemplaza el PNG y se corre esto.

CÓMO SE SACAN LOS TRAZOS
────────────────────────
No sirve el duotono por luminancia que usa `tc-mapas-duotono.py`: en este estilo
de Google Maps **los caminos son más CLAROS que el fondo** (#F5F4F4 sobre
#E7E8E9, catorce niveles de diferencia), así que mapear luminancia a tinta deja
los caminos invisibles y la mancha de relleno pintada.

Lo que sí funciona es medir el **gradiente**: todo lo que es línea —el casco de
cada camino, la orilla del río, el borde entre el verde rural y el gris urbano,
la letra de cada topónimo y el punteado del límite comunal— produce un salto de
color. El relleno plano, no. Así que:

    trazo = |∇color| normalizado     →  se entinta
    relleno plano                    →  se deja en el fondo

El gradiente se calcula sobre los **tres canales**, no sobre la luminancia: el
borde verde/gris del área urbana casi no cambia de brillo pero sí de color, y
sobre luminancia sola se perdía.

⭐ EL LÍMITE DE LA COMUNA ES EL PROTAGONISTA
─────────────────────────────────────────────
El archivo trae el contorno de **Padre Hurtado** dibujado por Google en punteado
rojo (1.785 px, x 247-657 · y 144-472). Es el mismo caso del pin del `MAPA-3`:
lo trae el material, no lo ponemos nosotros, y un tratamiento por brillo lo
mata. Se aísla y se repone como **el único acento** del mapa.

⚠️ LO QUE ESTE MAPA NO TIENE: **la ubicación de Tierra Calma.** Medido contra
`mapa3.jpg` usando «Casas de La Esperanza» y «Padre Hurtado» como anclas
comunes, la escala entre los dos archivos es 1,72 y el pin del proyecto cae en
x ≈ -166: **queda fuera del encuadre por la izquierda**. Este mapa muestra la
COMUNA, no la parcela. Si la pieza tiene que mostrar dónde está el proyecto,
hace falta otra captura que lo incluya.
"""
from __future__ import annotations

import argparse
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

# ⚠️ El origen vive en public/assets y NO en raw/: raw/ está en .gitignore, y una
# pieza entregada tiene que poder reproducirse desde el repo solo. Es la misma
# razón por la que `mapa3.jpg` vive acá.
RAW = pathlib.Path(RAIZ) / "public/assets/tierracalma/oct/MAPA-PADRE-HURTADO.png"
OCT = pathlib.Path(RAIZ) / "public/assets/tierracalma/oct"

# El punteado rojo del límite comunal, medido sobre el archivo.
LIMITE = {"min_rojo": 150, "margen": 55}


def _rgb(hex_: str) -> np.ndarray:
    return np.array([int(hex_[i : i + 2], 16) for i in (1, 3, 5)], dtype=float)


def trazos(a: np.ndarray, ganancia: float) -> np.ndarray:
    """Cuánto de cada píxel es LÍNEA, de 0 a 1.

    Sobel sobre los tres canales y se queda con el canal que más responde. El
    relleno plano da 0; un camino, una orilla o una letra dan 1.
    """
    k = np.array([1.0, 0.0, -1.0])
    s = np.array([1.0, 2.0, 1.0])
    fuerza = np.zeros(a.shape[:2])
    for c in range(3):
        canal = a[:, :, c]
        # Sobel separable, sin scipy
        gx = np.abs(_conv1(_conv1(canal, s, eje=0), k, eje=1))
        gy = np.abs(_conv1(_conv1(canal, k, eje=0), s, eje=1))
        fuerza = np.maximum(fuerza, np.hypot(gx, gy))
    return np.clip(fuerza / ganancia, 0, 1)


def _conv1(m: np.ndarray, nucleo: np.ndarray, eje: int) -> np.ndarray:
    """Convolución 1-D de 3 taps, con borde replicado."""
    m = m if eje == 0 else m.T
    pad = np.vstack([m[:1], m, m[-1:]])
    out = nucleo[0] * pad[:-2] + nucleo[1] * pad[1:-1] + nucleo[2] * pad[2:]
    return out if eje == 0 else out.T


def alfa_limite(a: np.ndarray, engrosar: int = 1) -> np.ndarray:
    """Cuánto de cada píxel es el punteado rojo del límite comunal.

    Se **engrosa** un píxel a cada lado: en el original es un punteado fino de
    1 px pensado para mirarse al 100 %, y en la pieza va reducido. Sin engrosar
    se deshilacha y deja de leerse como un contorno.
    """
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    rojez = (r - np.maximum(g, b)) / float(LIMITE["margen"])
    alfa = np.clip(rojez, 0, 1)
    alfa[r < LIMITE["min_rojo"]] = 0
    for _ in range(engrosar):
        alfa = np.maximum.reduce(
            [
                alfa,
                np.roll(alfa, 1, 0),
                np.roll(alfa, -1, 0),
                np.roll(alfa, 1, 1),
                np.roll(alfa, -1, 1),
            ]
        )
    return alfa


# ⚠️ `fuerza` NO es un capricho de gusto: es la JERARQUÍA. Con la red de caminos
# a tinta llena, el contorno de la comuna se pierde dentro de ella y el mapa se
# lee como una textura. Bajando la red al 70 % y dejando el contorno al 100 %,
# el mapa dice primero PADRE HURTADO y después cómo se llega.
VERSIONES = {
    # El que va en la pieza: trazo crema sobre el navy de marca. Es un mapa
    # grabado, no una fotografía de mapa: pesa lo justo sobre el fondo oscuro.
    "mapa-ph-trazos-navy": {
        "fondo": "#0B2C49", "tinta": "#F3EEE3", "acento": "#C9B99A",
        "ganancia": 150.0, "fuerza": 0.70,
    },
    # La alternativa en papel, por si el titular necesita fondo claro.
    "mapa-ph-trazos-papel": {
        "fondo": "#F3EEE3", "tinta": "#0B2C49", "acento": "#6C473D",
        "ganancia": 150.0, "fuerza": 0.70,
    },
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--probar", action="store_true", help="escribe en el scratchpad, no en public/")
    ap.add_argument("--ganancia", type=float, default=None)
    a_ = ap.parse_args()

    if not RAW.exists():
        print(f"✗ Falta {RAW}")
        return 1
    base = Image.open(RAW).convert("RGB")
    a = np.asarray(base).astype(float)
    print(f"MAPA-PADRE HURTADO: {base.size[0]}×{base.size[1]}")

    lim = alfa_limite(a)
    ys, xs = np.nonzero(lim > 0.25)
    print(f"· límite comunal: {len(xs)} px  ·  x {xs.min()}-{xs.max()}  y {ys.min()}-{ys.max()}")

    destino = pathlib.Path(a_.probar and "." or OCT)
    for nombre, cfg in VERSIONES.items():
        g = a_.ganancia or cfg["ganancia"]
        t = trazos(a, g) * cfg["fuerza"]
        fondo, tinta, acento = _rgb(cfg["fondo"]), _rgb(cfg["tinta"]), _rgb(cfg["acento"])
        out = fondo[None, None, :] * (1 - t[:, :, None]) + tinta[None, None, :] * t[:, :, None]
        # el límite comunal encima, como único acento
        out = out * (1 - lim[:, :, None]) + acento[None, None, :] * lim[:, :, None]
        ruta = (destino / f"{nombre}.jpg") if not a_.probar else pathlib.Path(f"{nombre}.jpg")
        Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(ruta, quality=93)
        print(f"· {ruta}  fondo {cfg['fondo']} · trazo {cfg['tinta']} · límite {cfg['acento']}")
        print(f"    ganancia {g:.0f} · cobertura de trazo {100 * t.mean():.1f}% del cuadro")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

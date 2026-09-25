#!/usr/bin/env python3
"""
Genera una LUT .cube S-Log3 / S-Gamut3.Cine → Rec.709 para ffmpeg (`lut3d`).

Por qué existe: los clips de la carpeta «videos / CAM» de QB (Sony XAVC 4K 60p
10 bits, 25-09-2026) vienen en S-Log3 — el metadato del archivo lo dice
literal: «S-Log3/S-Gamut3.Cine». Sin convertir se ven grises y lavados.

La conversión es la de Sony, sin inventar nada:
  1. S-Log3 → lineal de escena (fórmula publicada por Sony, código 10 bits)
  2. S-Gamut3.Cine → primarios Rec.709 (matriz 3×3 lineal)
  3. exposición + curva fílmica (ACES ajustada de Narkowicz) para bajar el
     rango de escena a pantalla sin quemar las guirnaldas
  4. OETF Rec.709

Uso:  python scripts/slog3-a-709.py <salida.cube> [--expo 1.6] [--n 33]
      ffmpeg ... -vf "format=rgb48le,lut3d=<salida.cube>,format=yuv420p" ...
"""
import argparse
import sys

sys.stdout.reconfigure(encoding="utf-8")

import numpy as np

# S-Gamut3.Cine → Rec.709 (lineal)
M = np.array([[1.6269474, -0.5401385, -0.0868089],
              [-0.1785155, 1.4179409, -0.2394254],
              [-0.0444361, -0.1959199, 1.2403560]])


def slog3_a_lineal(v):
    cv = v * 1023.0
    return np.where(cv >= 171.2102946929,
                    10 ** ((cv - 420.0) / 261.5) * (0.18 + 0.01) - 0.01,
                    (cv - 95.0) * 0.01125000 / (171.2102946929 - 95.0))


def filmica(x):
    return np.clip(x * (2.51 * x + 0.03) / (x * (2.43 * x + 0.59) + 0.14), 0, 1)


def oetf709(l):
    return np.where(l < 0.018, 4.5 * l, 1.099 * np.power(np.maximum(l, 0), 0.45) - 0.099)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("salida")
    ap.add_argument("--expo", type=float, default=1.6)
    ap.add_argument("--n", type=int, default=33)
    a = ap.parse_args()
    n = a.n
    g = np.linspace(0, 1, n)
    # orden .cube: R varía más rápido
    b, gg, r = np.meshgrid(g, g, g, indexing="ij")
    rgb = np.stack([r, gg, b], -1).reshape(-1, 3)
    lin = slog3_a_lineal(rgb) @ M.T
    out = oetf709(filmica(np.maximum(lin, 0) * a.expo))
    with open(a.salida, "w") as f:
        f.write(f'TITLE "S-Log3 SGamut3.Cine a Rec709 expo {a.expo}"\nLUT_3D_SIZE {n}\n')
        for p in out:
            f.write(f"{p[0]:.6f} {p[1]:.6f} {p[2]:.6f}\n")
    print(f"✓ {a.salida}  ({n}³, expo {a.expo})")


if __name__ == "__main__":
    main()

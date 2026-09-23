#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL DÍA DEL TURISMO — rinde los seis MP4 con nombre de entrega.

    python scripts/dt-c1-turismo-rendir.py
    python scripts/dt-c1-turismo-rendir.py --solo portada golf
    python scripts/dt-c1-turismo-rendir.py --con-logo      # variante: logo en todas

Misma receta que `dt-c1-s5-rendir.py`: mesa 1080×1350, **`--scale=2`** →
2160×2700 (entero PAR; 1,3333 y 1,5 revientan, ver su cabecera), H.264 CRF 16.

⭐ Nombre de entrega: Eli abrió el 23-09 la carpeta `C1 N°1 S5 TURISMO` en
`S5 HILTON SEP 2026 › DT` — o sea que este carrusel es el **C1** de la semana
(27-09) y el de «Tu día» (28-09) pasó a `C2-28SEP`. El tema va en la CARPETA,
no en el archivo (`docs/COMO-DISENA-EL-EQUIPO.md`).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "src/DtEntry.tsx"
SALIDA = RAIZ / "out/hilton/dt/c1-turismo/entrega"

# El orden ES el del brief (G1…G5, con los dos «G4» en el orden escrito).
PIEZAS = [
    ("DT-V-Tur-Portada", "C1 S5 DT n°1.mp4"),
    ("DT-V-Tur-Mut", "C1 S5 DT n°2.mp4"),
    ("DT-V-Tur-Bicentenario", "C1 S5 DT n°3.mp4"),
    ("DT-V-Tur-Sky", "C1 S5 DT n°4.mp4"),
    ("DT-V-Tur-SanCristobal", "C1 S5 DT n°5.mp4"),
    ("DT-V-Tur-Golf", "C1 S5 DT n°6.mp4"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", nargs="*", default=None)
    ap.add_argument("--con-logo", action="store_true")
    a = ap.parse_args()
    piezas = PIEZAS
    if a.solo:
        quiere = {x.lower() for x in a.solo}
        piezas = [p for p in PIEZAS if p[0].replace("DT-V-Tur-", "").lower() in quiere]
    salida = SALIDA if not a.con_logo else SALIDA.parent / "variante-con-logo"
    salida.mkdir(parents=True, exist_ok=True)
    extra = []
    if a.con_logo:
        props = salida / "props.json"
        props.write_text(json.dumps({"conLogo": True}))
        extra = [f"--props={props}"]
    npx = "npx.cmd" if sys.platform == "win32" else "npx"
    for comp, nombre in piezas:
        destino = salida / nombre
        print(f"→ {comp}  →  {nombre}")
        r = subprocess.run(
            [npx, "remotion", "render", str(ENTRADA), comp, str(destino),
             "--codec=h264", "--scale=2", "--crf=16", "--pixel-format=yuv420p",
             "--log=error", *extra],
            cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            print(f"  ⛔ falló {comp}")
            return 1
        print(f"  ✅ {destino.stat().st_size / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())

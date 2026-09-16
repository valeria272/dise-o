#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rinde las piezas de PISO18 al máster con el que entrega la diseñadora.

    python scripts/p18-rendir.py                 # las de la ronda abierta
    python scripts/p18-rendir.py P18-ST-Encuesta # sólo una
    python scripts/p18-rendir.py --listar

⭐ La mesa es 1080 de ancho y la cuenta ENTREGA a **2250** (×2,0833): la historia
aprobada `ST N°1 S1.png` es 2250×4000 y el carrusel `C2 S1 n°*.png` es 2250×2813.
Esto corrige la lectura de los `.ai`, cuya mesa es 1080×1350.

⚠️ Los nombres de entrega llevan espacios y el símbolo «°» —así entrega Eli y así
los levanta el portal—, y en Windows eso rompe el shell: se invoca por lista de
argumentos, nunca por línea armada a mano. Mismo patrón que `dt-rendir.py`.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "src/P18Entry.tsx"
ESCALA = "2.0833"          # historia 1080×1920 → 2250×4000

# id de composición → ruta de salida, relativa a la raíz.
NOMBRES = {
    # STORIES 25-09 · encuesta — ronda 4: cambia la opción B.
    "P18-ST-Encuesta": "out/piso18/s4/entrega/STS/ST N°4 S4.png",
    "P18-ST-Encuesta-Guia": "out/piso18/s4/guias/ST N°4 S4 - GUIA.png",
    # STORIES 23-09 · animada — ronda 4: titular nuevo, sin bajada.
    "P18-ST-Montaje": "out/piso18/s4/entrega/STS/ST N°3 S4.mp4",
    "P18-ST-Montaje-Guia": "out/piso18/s4/guias/ST N°3 S4 - GUIA.png",
}
# Las que se rinden si no se pide nada.
POR_DEFECTO = ["P18-ST-Encuesta", "P18-ST-Montaje"]


def npx() -> str:
    return "npx.cmd" if sys.platform == "win32" else "npx"


def rinde(comp: str, guia_frame: int | None = None) -> bool:
    destino = RAIZ / NOMBRES[comp]
    destino.parent.mkdir(parents=True, exist_ok=True)
    video = destino.suffix.lower() == ".mp4"
    # ⛔ EL VIDEO NO SE ESCALA, y no es una elección de calidad: `stitchFramesToVideo`
    # exige dimensiones ENTERAS y 1920 × 2,0833 da 3999,936 — el render aborta.
    # La `still` sí redondea, por eso las historias fijas salen a 2250×4000.
    # Y la entrega anterior ya iba a 1080×1920, que es el nativo de historia de
    # Instagram: verificado con ffprobe sobre `ST N°3 S4.mp4`.
    escala = "1" if video else ESCALA
    orden = [npx(), "remotion", "render" if video else "still",
             str(ENTRADA), comp, str(destino), f"--scale={escala}"]
    if not video and guia_frame is not None:
        orden += [f"--frame={guia_frame}"]
    if video:
        orden += ["--codec=h264", "--crf=17"]
    print(f"\n▶ {comp}  →  {NOMBRES[comp]}")
    r = subprocess.run(orden, cwd=str(RAIZ))
    if r.returncode != 0:
        print(f"  ✗ falló {comp} (código {r.returncode})")
        return False
    kb = destino.stat().st_size // 1024 if destino.exists() else 0
    print(f"  ✓ {destino.name}  ({kb} KB)")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("comps", nargs="*", help="ids a rendir; por defecto, la ronda abierta")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--guias", action="store_true",
                    help="rinde también las guías de zona segura")
    a = ap.parse_args()

    if a.listar:
        for k, v in NOMBRES.items():
            print(f"  {k:26s} → {v}")
        return 0

    pedidos = a.comps or list(POR_DEFECTO)
    if a.guias:
        # ⚠️ En una pieza ANIMADA la zona segura se mide en el ÚLTIMO fotograma:
        # es donde vive el botón. Medirla en el primero no prueba nada.
        pedidos = pedidos + [c + "-Guia" for c in pedidos if c + "-Guia" in NOMBRES]

    ok = True
    for c in pedidos:
        if c not in NOMBRES:
            print(f"  ⚠ no conozco «{c}» — usa --listar")
            ok = False
            continue
        frame = 389 if c == "P18-ST-Montaje-Guia" else None
        ok = rinde(c, frame) and ok
    print("\nListo." if ok else "\nTerminó con errores.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

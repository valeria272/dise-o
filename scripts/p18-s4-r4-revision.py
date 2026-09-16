#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma las imágenes de la página de revisión de la RONDA 4 de la S4 de PISO18.

    python scripts/p18-s4-r4-revision.py

Eli aprueba MIRANDO y comparado: cada ronda se entrega como una página con el
antes, el después y —cuando existe— la referencia. Los números van abajo, no
arriba. Este script sólo prepara las imágenes; el HTML se escribe aparte.

⚠️ El «antes» de la G3 sale de `out/piso18/s4/revision/img/c3.jpg`, que es la
copia web de la ronda 3. El PNG grande de esa ronda ya está reemplazado (en
disco y en Drive) y ésta es la prueba que queda — por eso la carpeta `revision/`
de cada ronda no se borra.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

Image.MAX_IMAGE_PIXELS = None

RAIZ = Path(__file__).resolve().parent.parent
R3 = RAIZ / "out/piso18/s4/revision/img"
DEST = RAIZ / "out/piso18/s4/revision-r4/img"
ENTREGA = RAIZ / "out/piso18/s4/entrega"
FFMPEG = RAIZ / "node_modules/@remotion/compositor-win32-x64-msvc/ffmpeg.exe"


def web(origen: Path, nombre: str, ancho: int, alto: int, calidad: int = 84) -> None:
    im = Image.open(origen).convert("RGB")
    im.thumbnail((ancho, alto), Image.LANCZOS)
    DEST.mkdir(parents=True, exist_ok=True)
    im.save(DEST / nombre, quality=calidad, optimize=True)
    print(f"  ✓ {nombre}  {im.size[0]}×{im.size[1]}")


def frame(video: Path, segundo: float, nombre: str, ancho: int) -> None:
    tmp = DEST / "_tmp.png"
    DEST.mkdir(parents=True, exist_ok=True)
    subprocess.run([str(FFMPEG), "-v", "error", "-y", "-ss", str(segundo),
                    "-i", str(video), "-frames:v", "1", str(tmp)], check=True)
    web(tmp, nombre, ancho, ancho * 3)
    tmp.unlink(missing_ok=True)


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    print("Imágenes de la revisión · ronda 4\n")

    print("1 · carrusel G3")
    web(R3 / "c3.jpg", "a-g3.jpg", 720, 900)                       # antes (ronda 3)
    web(ENTREGA / "C1 S4 PISO18/C1 S4 N°3.png", "g3.jpg", 720, 900)
    # Las otras tres G, para ver la G3 dentro del carrusel — «el resto OK!».
    for n in (1, 2, 4):
        web(ENTREGA / f"C1 S4 PISO18/C1 S4 N°{n}.png", f"g{n}.jpg", 420, 525)

    print("\n2 · encuesta")
    web(R3 / "st4.jpg", "a-st4.jpg", 506, 900)
    web(ENTREGA / "STS/ST N°4 S4.png", "st4.jpg", 506, 900)
    web(RAIZ / "public/assets/hilton/piso18/tira-b.jpg", "tira-b.jpg", 300, 780, 88)
    # ⭐ La tira B anterior la pisó este mismo script de recortes, pero NO se
    # perdió: estaba versionada desde la ronda 3 (commit 3da9d9e). Se saca de
    # git, que es la copia verdadera — reconstruirla a ojo daría un «antes»
    # inventado, y un antes/después con un antes falso no sirve de nada.
    # Es exactamente para esto que los fondos de una entrega se commitean.
    bruto = subprocess.run(["git", "show", "HEAD:public/assets/hilton/piso18/tira-b.jpg"],
                           cwd=str(RAIZ), capture_output=True, check=True).stdout
    tmp = DEST / "_tira.jpg"
    tmp.write_bytes(bruto)
    web(tmp, "a-tira-b.jpg", 300, 780, 88)
    tmp.unlink(missing_ok=True)

    print("\n3 · animada")
    frame(R3 / "st3.mp4", 2.0, "a-st3.jpg", 506)
    frame(ENTREGA / "STS/ST N°3 S4.mp4", 2.0, "st3.jpg", 506)
    frame(ENTREGA / "STS/ST N°3 S4.mp4", 12.8, "st3-cierre.jpg", 506)
    shutil.copy2(R3 / "st3.mp4", DEST / "a-st3.mp4")
    subprocess.run([str(FFMPEG), "-v", "error", "-y", "-i",
                    str(ENTREGA / "STS/ST N°3 S4.mp4"),
                    "-vf", "scale=506:-2", "-c:v", "libx264", "-crf", "30",
                    "-preset", "fast", "-an", str(DEST / "st3.mp4")], check=True)
    print("  ✓ st3.mp4 (copia liviana)")

    print("\n4 · post 25-09")
    web(RAIZ / "raw/hilton/piso18/deco-ago2024/piso_18-128.jpg", "ref-post.jpg", 900, 620)
    web(ENTREGA / "Post n°2 S4 PISO18 25-09.png", "post.jpg", 720, 900)
    web(ENTREGA / "Post S4 PISO18 25-09.png", "post-noche.jpg", 420, 525)

    print("\nListo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

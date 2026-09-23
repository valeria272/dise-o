#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL DÍA DEL TURISMO — la copia en GIF de las seis láminas.

    python scripts/dt-c1-turismo-gif.py
    python scripts/dt-c1-turismo-gif.py --ancho 540    # para mandar por chat

Pedido de Eli el 23-09: «necesito que dejes en gif ahora» (la regla del encargo
era GIF sólo con la pieza aprobada). El master sigue siendo el MP4 de 2160×2700.

Parte de `dt-c1-s5-gif.py` (720 px, paleta propia por lámina con
`stats_mode=diff`) con las dos correcciones medidas después en Piso 18
(memoria `gif-de-una-pieza-animada`):

  · **12,5 fps y no 12.** El GIF guarda la duración de cada cuadro en
    CENTÉSIMAS: 12 fps son 8,33 cs y el formato redondea (la lámina deriva);
    12,5 son 8 cs exactos y los 5,0 s quedan clavados (63 × 80 ms ≈ 5,04 s).
  · **Sin difuminado.** Con paleta sacada del propio video, el dither sólo mete
    trama en las zonas lisas —acá, el velo azul y el cielo—. `none` dio menos
    error y casi el mismo peso.
"""
import argparse
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

FF = imageio_ffmpeg.get_ffmpeg_exe()
RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "out/hilton/dt/c1-turismo/entrega"
DESTINO = RAIZ / "out/hilton/dt/c1-turismo/entrega-gif"
FPS = 12.5


def gif(src: Path, destino: Path, ancho: int) -> None:
    paleta = destino.with_suffix(".paleta.png")
    vf = f"fps={FPS},scale={ancho}:-1:flags=lanczos"
    subprocess.run([FF, "-y", "-v", "error", "-i", str(src),
                    "-vf", vf + ",palettegen=max_colors=255:stats_mode=diff",
                    str(paleta)], check=True)
    subprocess.run([FF, "-y", "-v", "error", "-i", str(src), "-i", str(paleta),
                    "-lavfi", vf + "[x];[x][1:v]paletteuse=dither=none:diff_mode=rectangle",
                    "-loop", "0", str(destino)], check=True)
    paleta.unlink()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ancho", type=int, default=720)
    a = ap.parse_args()
    fuentes = sorted(ORIGEN.glob("C1 S5 DT n°*.mp4"))
    if not fuentes:
        print(f"⛔ no hay mp4 en {ORIGEN.relative_to(RAIZ)}")
        return 1
    DESTINO.mkdir(parents=True, exist_ok=True)
    for src in fuentes:
        destino = DESTINO / (src.stem + ".gif")
        gif(src, destino, a.ancho)
        print(f"  {destino.name:<22} {a.ancho} px · {FPS} fps · "
              f"{destino.stat().st_size / 1e6:5.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — la copia en GIF de las seis láminas.

    python scripts/dt-c1-s5-gif.py            # las 6, a 720 px
    python scripts/dt-c1-s5-gif.py --ancho 540

⭐ Por qué existe. Eli pidió el 21-09 «formato gif de todas en una carpeta
adicional además de los mp4». **El GIF no reemplaza a la entrega**: el master
sigue siendo el `.mp4` de 2160×2700 que sube al Drive y que ve el cliente. El
GIF es la copia que se mira sin reproductor —se anima sola en cualquier vista
previa, en el portal y en un correo— y por eso vive en su propia carpeta.

⭐⭐ LOS DOS NÚMEROS, Y POR QUÉ ÉSOS. Se probaron cuatro combinaciones sobre la
lámina del gym y se miró el bloque de texto recortado, que es lo que se pierde
primero:

  | tamaño | peso por lámina | veredicto |
  |---|---|---|
  | 1080 px @ 12 fps |  40,9 MB | igual de nítido que 720 y pesa el doble |
  | **720 px @ 12 fps** | **19,5 MB** | **el titular y la versalita se leen enteros** |
  | 720 px @ 15 fps |  24,3 MB | +25 % de peso por un movimiento que ya es lento |
  | 540 px @ 12 fps |  11,6 MB | la versalita de la firma empieza a empastarse |

⚠️ **Un GIF de 20 MB no entra por WhatsApp** (el tope anda en 16 MB y además lo
convierte a mp4). Para mandarlos por chat hay que bajar a `--ancho 540`, con el
costo que dice la tabla. Para Drive, el portal y un correo, 720 va bien.

⭐ **12 fps y no 30.** El GIF no tiene compresión entre fotogramas: el peso es
casi lineal con la cantidad de cuadros. Estos clips son travellings lentos —los
únicos que se aceleran son a 0,47×— así que a 12 fps el movimiento sigue
leyéndose continuo. A 30 fps el archivo se iría sobre los 45 MB por lámina.

⭐ **Paleta propia por lámina, calculada con `stats_mode=diff`.** Un GIF sólo
tiene 256 colores y estas piezas son fotografía con un velo azul encima: con la
paleta por defecto el degradado del velo sale a bandas. `stats_mode=diff` arma
la paleta mirando lo que CAMBIA entre fotogramas, que es donde el ojo ve el
banding, y `dither=bayer:bayer_scale=3` reparte el error sin el hormigueo que
deja el dither por difusión cuando la imagen se mueve.
"""
import argparse
import os
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
ORIGEN = RAIZ / "out/hilton/dt/c1-s5/entrega"
DESTINO = RAIZ / "out/hilton/dt/c1-s5/entrega-gif"
FPS = 12


def gif(src: Path, destino: Path, ancho: int) -> None:
    paleta = destino.with_suffix(".paleta.png")
    vf = f"fps={FPS},scale={ancho}:-1:flags=lanczos"
    subprocess.run(
        [FF, "-y", "-v", "error", "-i", str(src),
         "-vf", vf + ",palettegen=stats_mode=diff", str(paleta)], check=True)
    subprocess.run(
        [FF, "-y", "-v", "error", "-i", str(src), "-i", str(paleta),
         "-lavfi", vf + "[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=3:"
                        "diff_mode=rectangle",
         # 0 = bucle infinito, que es lo que hace el carrusel en Instagram
         "-loop", "0", str(destino)], check=True)
    paleta.unlink()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ancho", type=int, default=720,
                    help="ancho en px (720 por defecto; 540 para mandar por chat)")
    a = ap.parse_args()

    fuentes = sorted(ORIGEN.glob("C1 S5 DT n°*.mp4"))
    if not fuentes:
        print(f"⛔ no hay mp4 en {ORIGEN.relative_to(RAIZ)}")
        return 1
    DESTINO.mkdir(parents=True, exist_ok=True)

    total = 0
    for src in fuentes:
        destino = DESTINO / (src.stem + ".gif")
        gif(src, destino, a.ancho)
        peso = destino.stat().st_size
        total += peso
        print(f"  {destino.name:<24} {a.ancho} px · {FPS} fps · {peso / 1e6:5.1f} MB")
    print(f"\n{len(fuentes)} GIF en {DESTINO.relative_to(RAIZ)} · "
          f"{total / 1e6:.0f} MB en total")
    return 0


if __name__ == "__main__":
    sys.exit(main())

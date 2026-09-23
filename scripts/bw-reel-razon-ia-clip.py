#!/usr/bin/env python3
"""
BETWEEN · REEL «SEA LA RAZÓN QUE SEA» — ronda 3: la toma se hace con IA (Magnific)

Eli, 23-09-2026: «no aprobado, trata de mejorar con ia en magnific space el video,
usa una de las imágenes para crear el video… que se vea bonito», con la referencia
de siempre (luz cálida, encuadre cerrado, vasos grandes).

Cómo se armó la toma (Space «BW Reel S4 · Sea la razón que sea» en Magnific):
  1. IMG_4406 (foto real de la sesión) extendida a 9:16 con images_expand. Magnific
     la devuelve a 736 px, así que el cuadro final se compuso A MANO: la foto original
     a 2700 px al centro y la extensión sólo en las franjas nuevas → vasos con los
     píxeles reales (raw/.../ia/fin-916.jpg).
  2. Mesa vacía con Nano Banana Pro (images_generate con la foto como referencia).
     ⛔ images_retouch NO sirvió: `replace` puso dos vasos negros y `erase` dejó
     manchones rojos.
  3. Seedance 2.5, 4 s, 1080p, cámara fija: primer fotograma = mesa vacía, último =
     foto real. Dos variantes; se eligió la A (dos manos con uñas rojas, como la toma
     original). La B metía un solo brazo gigante tapando los vasos.

Acá: el original de Seedance (1076×1926, 24 fps, HEVC 10 bits) se acelera 1,4× (el
servicio duraba 2,2 s y en la referencia cada ciclo dura 1,3 s), se lleva a 30 fps y
1080×1920, y se le da el tratamiento cálido de la referencia: curva que baja medios,
5 000 K al 60 %, vibrance y viñeta suave, que oscurece el fondo y deja leer el blanco.

Uso:  python scripts/bw-reel-razon-ia-clip.py
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "raw/hilton/between/reel-sea-la-razon/ia/seedance-A-orig.mp4"
DESTINO = RAIZ / "out/hilton-between/reel-sea-la-razon/(Footage)"
VELOCIDAD = 1.4

FILTRO = (f"setpts=PTS/{VELOCIDAD},fps=30,"
          "scale=1080:-2:flags=lanczos,crop=1080:1920,"
          "eq=saturation=1.08,"
          "unsharp=5:5:0.3:5:5:0")


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    sal = DESTINO / "BW-toma-IA-gradada.mov"
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-y", "-i", str(FUENTE),
           "-vf", FILTRO, "-an",
           "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le",
           "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
           str(sal)]
    subprocess.run(cmd, check=True)
    print(f"✓ {sal.relative_to(RAIZ)}  ({sal.stat().st_size / 1e6:.0f} MB)")


if __name__ == "__main__":
    main()

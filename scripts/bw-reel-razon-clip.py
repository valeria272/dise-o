#!/usr/bin/env python3
"""
BETWEEN · REEL ORGÁNICO «SEA LA RAZÓN QUE SEA» (ORGÁNICOS, semana 4, 24-09-2026)

Saca de la toma cruda (iPhone 4K60 HLG, IMG_4389.MOV) la entrega elegida y la deja
gradada, en ProRes 422 HQ 1080×1920 a 30 fps, para montarla en After Effects.

La toma trae ~10 entregas del mismo servicio (garzón deja un helado y un To Go).
Ronda 2 (Eli, 23-09: «muy quemado… que la toma sea bonita»): se eligió la de
58,0–59,3 s — con el reencuadre es la única que deja los dos vasos ENTEROS con aire
a AMBOS lados: la de 48 s (ronda 1) corta el helado y la de 33 s deja el To Go a
15 px del borde en el crudo, así que el reencuadre se lo come. Se mide el margen
sobre el fotograma YA reencuadrado, no sobre una miniatura.
Se deja con MANIJAS (56,5–61,5 s) para correr el ciclo en AE sin re-exportar.

Tratamiento, ronda 2 — lo que quemaba la ronda 1 eran dos errores míos:
  · `tonemap=hable:desat=0` → sin desaturar las altas, verdes y amarillos del
    fondo salían fosforescentes. Ahora hable con su desat por defecto y npl=203
    (menos exposición: mediana 187 → 155).
  · denoise espacial + `cas` → el follaje quedaba «pintado». Ahora sólo denoise
    temporal suave y unsharp leve en luma.
  · reencuadre 1,11× (crop 1944×3456) para achicar la franja blanca del techo.
  · curva en S suave, vibrance 0,12 (no saturación: respeta el kraft del vaso) y
    temperatura 5900 K al 50 %.

Uso:  python scripts/bw-reel-razon-clip.py
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "raw/hilton/between/reel-sea-la-razon/IMG_4389.MOV"
DESTINO = RAIZ / "out/hilton-between/reel-sea-la-razon/(Footage)"
INICIO, DURACION = 56.5, 5.0          # manijas alrededor de la entrega 58,0–59,3

TONEMAP = ("crop=1944:3456:108:384,"
           "zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,"
           "tonemap=hable,zscale=t=bt709:m=bt709:r=tv,format=yuv420p10le")
GRADO = ("curves=m='0/0 0.18/0.13 0.5/0.5 0.82/0.84 1/0.96',"
         "vibrance=intensity=0.12,colortemperature=temperature=5900:mix=0.5,"
         "hqdn3d=0:0:2:2,scale=1080:1920:flags=lanczos,"
         "unsharp=5:5:0.35:5:5:0,fps=30")


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    sal = DESTINO / "BW-toma-entrega-gradada.mov"
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-y",
           "-ss", str(INICIO), "-t", str(DURACION), "-i", str(FUENTE),
           "-vf", f"{TONEMAP},{GRADO}", "-an",
           "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le",
           "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
           str(sal)]
    subprocess.run(cmd, check=True)
    print(f"✓ {sal.relative_to(RAIZ)}  ({sal.stat().st_size / 1e6:.0f} MB)")


if __name__ == "__main__":
    main()

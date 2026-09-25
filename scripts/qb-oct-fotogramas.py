#!/usr/bin/env python3
"""
QB · GRILLA OCTUBRE 2026 — fotogramas de la sesión «2026 | Shooting QB orgánico».

La sesión del Drive (`1lt6lvhZ9uXLYh4wKWA5mveGowOVKzACj`) NO son fotos: son 90
videos de iPhone 4K en **HDR HLG / BT.2020** a 60 fps. Las miniaturas de Drive
muestran el primer fotograma y por eso parecen fotos.

Método de la marca (Eli, 15-09): «de los videos se sacan fotos». Acá se saca el
fotograma y se **tonemapea HLG → Rec.709** con `zscale` + `tonemap=hable`, la
receta ya medida con el dron de Tierra Calma (`scripts/tc-proxies.sh`): sin eso
el HLG se ve lavado y verdoso.

Uso:
    python scripts/qb-oct-fotogramas.py IMG_3088 --hoja            # 8 momentos, hoja de contacto
    python scripts/qb-oct-fotogramas.py IMG_3088 --t 2.4           # un fotograma a tamaño completo
"""
import argparse
import os
import subprocess
import sys

import imageio_ffmpeg
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESION = os.path.join(RAIZ, "raw", "hilton", "qb", "sesiones-full", "shooting-organico-2026")
SALIDA = os.path.join(RAIZ, "raw", "hilton", "qb", "oct-fotogramas")
FF = imageio_ffmpeg.get_ffmpeg_exe()

TONEMAP = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
           "tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=pc,format=rgb24")


def duracion(ruta):
    r = subprocess.run([FF, "-i", ruta], capture_output=True, text=True)
    for l in r.stderr.splitlines():
        if "Duration" in l:
            h, m, s = l.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0


def ruta_clip(clip):
    for ext in (".MOV", ".MP4", ".mov", ".mp4"):
        r = os.path.join(SESION, clip + ext)
        if os.path.exists(r):
            return r
    raise FileNotFoundError(clip)


def es_hlg(ruta):
    """Sólo el iPhone viene en HLG; la Sony de la sesión de Víctor es Rec.709."""
    r = subprocess.run([FF, "-i", ruta], capture_output=True, text=True)
    return "arib-std-b67" in r.stderr


def fotograma(clip, t, destino, ancho=None):
    ruta = ruta_clip(clip)
    base = TONEMAP if es_hlg(ruta) else "format=rgb24"
    vf = base + (f",scale={ancho}:-2:flags=lanczos" if ancho else "")
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", ruta,
                    "-frames:v", "1", "-vf", vf, destino], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clips", nargs="+")
    ap.add_argument("--t", type=float)
    ap.add_argument("--hoja", action="store_true")
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument("--sesion", help="otra carpeta de raw/hilton/qb/sesiones-full/")
    a = ap.parse_args()
    global SESION
    if a.sesion:
        SESION = os.path.join(os.path.dirname(SESION), a.sesion)
    os.makedirs(SALIDA, exist_ok=True)
    for clip in a.clips:
        if a.t is not None:
            d = os.path.join(SALIDA, f"{clip}_t{a.t:.2f}.png")
            fotograma(clip, a.t, d)
            print("✓", os.path.relpath(d, RAIZ), Image.open(d).size)
            continue
        dur = duracion(ruta_clip(clip))
        tiempos = [dur * (i + 0.5) / a.n for i in range(a.n)]
        cuadros = []
        for t in tiempos:
            d = os.path.join(SALIDA, f"_{clip}_{t:.2f}.jpg")
            fotograma(clip, t, d, ancho=360)
            cuadros.append((t, Image.open(d).convert("RGB")))
        w, h = cuadros[0][1].size
        hoja = Image.new("RGB", (w * len(cuadros), h + 30), "white")
        dr = ImageDraw.Draw(hoja)
        for i, (t, im) in enumerate(cuadros):
            hoja.paste(im, (i * w, 0))
            dr.text((i * w + 6, h + 6), f"{clip} t={t:.2f}s", fill="black")
        d = os.path.join(SALIDA, f"hoja-{clip}.jpg")
        hoja.save(d, quality=85)
        print("✓", os.path.relpath(d, RAIZ), f"{dur:.1f}s")


if __name__ == "__main__":
    main()

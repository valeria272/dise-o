"""PISO18 · OCTUBRE 2026 — corta los clips REALES de las historias animadas del 16 y 30-10.

El material es del disco F: (`SESIONES HILTON/SESIONES PISO18/Capsula N marzo 2026`): .MOV
de iPhone 4K vertical, HEVC 10 bit **HLG** (bt2020 / arib-std-b67) con rotación por
metadato y casi todos a 59,94 fps. Chrome no los lee así: acá se cortan, se pasan a SDR
bt709 con mapa de tonos, a 1080×1920 y 30 fps, H.264.

⚠️ El ffmpeg de `npx remotion ffmpeg` no trae `zscale`; va el de `imageio_ffmpeg`.

Uso:  python scripts/p18-oct-clips-reales.py [s1610 | s3010 | s1610-a …]
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
DISCO = Path("F:/SESIONES HILTON/SESIONES PISO18")
OUT = RAIZ / "public/assets/hilton/piso18/oct"
FF = imageio_ffmpeg.get_ffmpeg_exe()

# salida: (origen, desde s, duración s[, filtro extra antes de escalar]) — el tramo queda escrito acá (R-17)
CLIPS = {
    # ST 16-10 «Equipo Piso18»: la experiencia de servicio, de la barra a la sala
    "s1610-a.mp4": ("Capsula 2 marzo 2026/IMG_1820.MOV", 0.1, 2.7),   # barman terminando los spritz
    "s1610-b.mp4": ("Capsula 1 marzo 2026/IMG_1831.MOV", 0.4, 3.0),   # garzón armando la bandeja de copas
    "s1610-c.mp4": ("Capsula 3 marzo 2026 parte 1/IMG_1847.MOV", 1.3, 2.8),  # garzona con la bandeja de cóctel
    "s1610-d.mp4": ("Capsula 1 marzo 2026/IMG_5740.MOV", 3.4, 3.8),   # la bandeja de cerca, sin rostros
    # ST 30-10 «El broche perfecto para tu historia»: recorrido que termina en el letrero.
    # Ronda 8 (Eli 02-10: «trata de utilizar mejores videos que no se vean tan extraños o tan
    # difuminados»). Los cuatro de la ronda 7 salieron: 5671 (cámara chueca y un técnico parado
    # en la pista), 5664 (hojas desenfocadas en primer plano), 5746 (ventanal torcido) y el
    # letrero 5690 tal cual (inclinado 13°, con la licuadora y los enchufes a la vista).
    "s3010-a.mp4": ("sesion 27 de febrero 2026/IMG_5760.MOV", 0.8, 3.0),   # atardecer por el ventanal, mesa montada
    "s3010-b.mp4": ("Capsula 4 marzo 2026/IMG_5669.MOV", 4.0, 3.0),        # centro de flores y puestos, de cerca
    "s3010-c.mp4": ("Capsula 4 marzo 2026/IMG_1876.MOV", 0.2, 2.8),        # salón de noche con las guirnaldas
    # el letrero de neón, NIVELADO (gira 9°, lo que deja el cuadro sin esquinas vacías) y recortado sobre el 4K para dejar fuera la
    # licuadora; la cámara panea y a los 2,4 s el «8» toca el borde: va 0–1,85 s a mitad de
    # velocidad (el original es de 59,94 fps, así que a 30 fps no se inventa ningún fotograma).
    "s3010-d.mp4": ("Capsula 3 marzo 2026 parte 1/IMG_5690.MOV", 0.0, 1.85,
                    "rotate=-9*PI/180:bilinear=1,crop=1460:2596:130:130,setpts=2*PTS"),
}

HLG_A_SDR = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
             "tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p")


def main():
    solo = sys.argv[1:]
    for nombre, (origen, desde, dur, *extra) in CLIPS.items():
        if solo and not any(s in nombre for s in solo):
            continue
        src = DISCO / origen
        if not src.is_file():
            print(f"x falta {src}")
            continue
        vf = f"{HLG_A_SDR},{extra[0] + ',' if extra else ''}scale=1080:1920:flags=lanczos,fps=30"
        r = subprocess.run([FF, "-y", "-ss", f"{desde}", "-t", f"{dur}", "-i", str(src), "-an",
                            "-vf", vf, "-c:v", "libx264", "-crf", "16", "-preset", "medium",
                            "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUT / nombre)],
                           capture_output=True, text=True, errors="replace")
        ok = (OUT / nombre).is_file() and r.returncode == 0
        print(f"{'✓' if ok else 'x'} {nombre} ← {origen} [{desde}s +{dur}s]" + ("" if ok else "\n" + r.stderr[-600:]))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
QB · GRILLA OCTUBRE 2026 — proxies de los clips reales para las ST animadas.

Remotion no digiere bien el HEVC 10 bits HLG del iPhone ni el 4K de la Sony a
64 Mbps. Acá cada tramo elegido sale como H.264 1080×1920 a 30 fps, SDR:
  · iPhone (HLG)  → tonemap HLG→Rec.709 hable (receta de `tc-proxies.sh`)
  · Sony (709)    → sin tonemap
  · si el clip es horizontal se saca el 9:16 a alto completo, centrado en `cx`

Salida: public/assets/hilton/qb/oct/clips/<nombre>.mp4 (sin audio).
Uso:    python scripts/qb-oct-proxies.py
"""
import os
import subprocess
import sys

import imageio_ffmpeg

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SES = os.path.join(RAIZ, "raw", "hilton", "qb", "sesiones-full")
SAL = os.path.join(RAIZ, "public", "assets", "hilton", "qb", "oct", "clips")
FF = imageio_ffmpeg.get_ffmpeg_exe()
TONEMAP = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
           "tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,")

# nombre: (sesión, clip, desde s, duración s, cx del recorte si es horizontal)
TRAMOS = {
    # ST 26-10 · TERRAZA — las 5 escenas del brief
    "t1-terraza":  ("victor-13-10", "C4144.MP4", 0.4, 3.4, 0.5),
    "t2-tragos":   ("victor-13-10", "C4147.MP4", 1.6, 3.4, 0.55),
    "t3-compartir": ("shooting-organico-2026", "IMG_3049.MOV", 0.3, 3.4, 0.5),
    "t4-risas":    ("victor-13-10", "C4219.MP4", 12.2, 3.4, 0.5),
    "t5-brindis":  ("victor-13-10", "C4182.MP4", 0.4, 3.6, 0.5),
}


def info(ruta):
    r = subprocess.run([FF, "-i", ruta], capture_output=True, text=True).stderr
    hlg = "arib-std-b67" in r
    # tamaño mostrado (considera rotación)
    import re
    m = re.search(r"Video:.*?(\d{3,5})x(\d{3,5})", r)
    w, h = int(m.group(1)), int(m.group(2))
    if "rotate" in r or "displaymatrix" in r:
        if re.search(r"rotation of -?90", r):
            w, h = h, w
    return hlg, w, h


def main():
    os.makedirs(SAL, exist_ok=True)
    for n, (ses, clip, t0, dur, cx) in TRAMOS.items():
        ruta = os.path.join(SES, ses, clip)
        hlg, w, h = info(ruta)
        vf = TONEMAP if hlg else "format=yuv420p,"
        if w > h:  # horizontal → 9:16 a alto completo
            cw = int(h * 9 / 16) // 2 * 2
            x0 = int(min(max(cx * w - cw / 2, 0), w - cw))
            vf += f"crop={cw}:{h}:{x0}:0,"
        vf += "scale=1080:1920:flags=lanczos,fps=30"
        d = os.path.join(SAL, n + ".mp4")
        subprocess.run([FF, "-v", "error", "-y", "-ss", str(t0), "-t", str(dur), "-i", ruta,
                        "-vf", vf, "-an", "-c:v", "libx264", "-crf", "17", "-preset", "slow",
                        "-pix_fmt", "yuv420p", "-movflags", "+faststart", d], check=True)
        print(f"✓ {n}.mp4  ({'HLG→709' if hlg else '709'}, {w}×{h}) {os.path.getsize(d)//1024} KB")


if __name__ == "__main__":
    main()

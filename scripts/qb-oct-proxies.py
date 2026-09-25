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

# ⭐ 25-09-2026: la terraza se rehizo con la carpeta «videos / CAM» que pasó Eli
# (Sony XAVC 4K 60p, S-Log3/S-Gamut3.Cine, 10-10-2025 de tarde). S-Log3 se pasa a
# Rec.709 con la LUT de `slog3-a-709.py` (fórmula de Sony, sin inventar color).
CAM = os.path.join(RAIZ, "raw", "hilton", "qb", "sesiones-25-09", "cam")
LUT = os.path.join(CAM, "slog3_709.cube")

# nombre: (sesión, clip, desde s, duración s, cx del recorte si es horizontal)
TRAMOS = {
    # ST 26-10 · TERRAZA — las 5 escenas del brief, todas de la tarde del 10-10
    # ⛔ Eli 25-09: «salen trabajadores del hotel, no se puede usar». Fuera 8519
    # (brindis con dos ejecutivos del hotel), 8566 (gente de pie que puede ser
    # del local) y 8503 (garzón de uniforme). Sólo invitados.
    "t1-terraza":   ("cam", "nanvo8526.MP4", 0.5, 3.4, 0.5),   # invitados en la mesa larga
    "t2-tragos":    ("cam", "nanvo8586.MP4", 0.5, 3.4, 0.5),   # el trago servido, barman desenfocado
    "t3-compartir": ("cam", "nanvo8516.MP4", 1.0, 3.4, 0.5),   # manos y platos al centro
    "t4-risas":     ("cam", "nanvo8574.MP4", 0.5, 3.4, 0.5),   # amigos riendo
    "t5-brindis":   ("cam", "nanvo8536.MP4", 0.6, 3.6, 0.5),   # pareja de invitados brindando
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
        ruta = os.path.join(CAM, clip) if ses == "cam" else os.path.join(SES, ses, clip)
        hlg, w, h = info(ruta)
        if ses == "cam":
            lut = os.path.relpath(LUT, RAIZ).replace(os.sep, "/")
            vf = f"format=rgb48le,lut3d={lut},format=yuv420p,"
        else:
            vf = TONEMAP if hlg else "format=yuv420p,"
        if w > h:  # horizontal → 9:16 a alto completo
            cw = int(h * 9 / 16) // 2 * 2
            x0 = int(min(max(cx * w - cw / 2, 0), w - cw))
            vf += f"crop={cw}:{h}:{x0}:0,"
        vf += "scale=1080:1920:flags=lanczos,fps=30"
        d = os.path.join(SAL, n + ".mp4")
        subprocess.run([FF, "-v", "error", "-y", "-ss", str(t0), "-t", str(dur), "-i", ruta,
                        "-vf", vf, "-an", "-c:v", "libx264", "-crf", "17", "-preset", "slow",
                        "-pix_fmt", "yuv420p", "-movflags", "+faststart", d], check=True, cwd=RAIZ)
        print(f"✓ {n}.mp4  ({'S-Log3→709' if ses == 'cam' else 'HLG→709' if hlg else '709'}, {w}×{h}) {os.path.getsize(d)//1024} KB")


if __name__ == "__main__":
    main()

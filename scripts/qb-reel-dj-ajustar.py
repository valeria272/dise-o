#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reel DJ de QB: deja la 1.ª y la 2.ª página con la duración pedida y la música
cubriendo todo el video, a partir del MP4 exportado de Canva (la API de Canva no
toca duraciones ni audio). Alarga sólo el tramo quieto de cada página; entradas y
transiciones quedan a velocidad normal. La música se estira sin cambiar el tono.

    python scripts/qb-reel-dj-ajustar.py <export.mp4> <salida.mp4> [p1=2.8] [p2=2.5]
"""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
M = importlib.import_module("qb-reel-dj-medir")

src, out = sys.argv[1], sys.argv[2]
p1 = float(sys.argv[3]) if len(sys.argv) > 3 else 2.8
p2 = float(sys.argv[4]) if len(sys.argv) > 4 else 2.5
dur, tramos, fin, _ = M.medir(src)
tr = [t for t in tramos if t[0] > 0.5 and (t[1] - t[0]) >= 0.5][:2]      # las dos primeras transiciones de página
(a1, b1, _), (a2, b2, _) = tr
m1, m2 = (a1 + b1) / 2, (a2 + b2) / 2
add1, add2 = max(0, p1 - m1), max(0, p2 - (m2 - m1))
h1 = (0.7, a1 - 0.15); h2 = (b1 + 0.15, a2 - 0.15)                        # tramos quietos
f1 = 1 + add1 / (h1[1] - h1[0]); f2 = 1 + add2 / (h2[1] - h2[0])
total = dur + add1 + add2
print(f"página 1: {m1:.2f} → {m1+add1:.2f} s · página 2: {m2-m1:.2f} → {m2-m1+add2:.2f} s · total {dur:.2f} → {total:.2f} s · música {fin:.2f} s")
fc = (f"[0:v]trim=0:{h1[0]},setpts=PTS-STARTPTS[v1];"
      f"[0:v]trim={h1[0]}:{h1[1]},setpts=(PTS-STARTPTS)*{f1:.4f}[v2];"
      f"[0:v]trim={h1[1]}:{h2[0]},setpts=PTS-STARTPTS[v3];"
      f"[0:v]trim={h2[0]}:{h2[1]},setpts=(PTS-STARTPTS)*{f2:.4f}[v4];"
      f"[0:v]trim={h2[1]},setpts=PTS-STARTPTS[v5];"
      f"[v1][v2][v3][v4][v5]concat=n=5:v=1:a=0,fps=30[v];"
      f"[0:a]atrim=0:{fin+0.02:.2f},asetpts=PTS-STARTPTS,atempo={fin/(total-0.05):.4f},apad=whole_dur={total:.4f}[a]")
subprocess.run([M.FF, "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k",
                "-movflags", "+faststart", "-t", f"{total:.4f}", out], check=True)
d2, t2, fin2, sil = M.medir(out)
tr2 = [t for t in t2 if t[0] > 0.5 and (t[1] - t[0]) >= 0.5][:2]
n1, n2 = [(a + b) / 2 for a, b, _ in tr2]
print(f"MEDIDO en la salida: página 1 = {n1:.2f} s · página 2 = {n2-n1:.2f} s · total {d2:.2f} s · música hasta {fin2:.2f} s · silencios {sil}")

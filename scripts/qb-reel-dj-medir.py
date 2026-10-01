#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mide un Reel DJ de QB exportado de Canva: cuánto dura cada página (por las
transiciones) y si la música cubre de principio a fin. La API de Canva no deja
tocar la duración de página ni el audio, así que esto es lo que se revisa antes
de entregar. Uso: python scripts/qb-reel-dj-medir.py <video.mp4>"""
import sys, os, glob, subprocess, tempfile, wave, shutil
import numpy as np
from PIL import Image
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()

def medir(video):
    d = tempfile.mkdtemp()
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vf", "fps=30,scale=108:192", os.path.join(d, "f%05d.png")], check=True)
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "8000", os.path.join(d, "a.wav")], check=True)
    fs = sorted(glob.glob(os.path.join(d, "f*.png")))
    A = np.stack([np.asarray(Image.open(f).convert("L"), dtype=np.float32)[55:165, 10:98] for f in fs])
    dur = len(fs) / 30
    dif = np.abs(A[1:] - A[:-1]).mean(axis=(1, 2))
    act = dif > 0.6
    tramos, s = [], None
    for i, x in enumerate(act):
        if x and s is None: s = i
        if (not x) and s is not None:
            if i - s >= 6: tramos.append((s / 30, i / 30, float(dif[s:i].sum())))
            s = None
    w = wave.open(os.path.join(d, "a.wav")); sr = w.getframerate()
    a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    k = int(sr * 0.1)
    rms = np.array([np.sqrt((a[i:i + k] ** 2).mean() + 1e-12) for i in range(0, len(a) - k, k)])
    db = 20 * np.log10(rms + 1e-9)
    suena = np.where(db > -45)[0]
    fin_musica = (suena[-1] + 1) * 0.1 if len(suena) else 0.0
    silencios = []
    s = None
    for i, x in enumerate(db < -45):
        if x and s is None: s = i
        if (not x) and s is not None:
            if (i - s) * 0.1 >= 0.3 and s * 0.1 > 0.6: silencios.append((round(s * 0.1, 1), round(i * 0.1, 1)))
            s = None
    shutil.rmtree(d, ignore_errors=True)
    return dur, tramos, fin_musica, silencios

if __name__ == "__main__":
    dur, tramos, fin, sil = medir(sys.argv[1])
    print(f"duración {dur:.2f} s · música hasta {fin:.2f} s · silencios internos {sil}")
    for a, b, f in tramos: print(f"  movimiento {a:5.2f}–{b:5.2f} s  (fuerza {f:.0f})")

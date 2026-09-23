#!/usr/bin/env python3
"""CAP. 02 — BLOQUE 2 · SHOTS 04–07 · 0:04,8 – 0:14,6 · 294 frames

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-audio-bloque2.py

El setup y el nivel 1. Frames LOCALES del bloque (0 = f.144 del capítulo):

  SHOT 04 · EL POST-IT     0–71    la música se va a CERO. «mm.» en el f.50 (silencio)
  SHOT 05 · LA BANDEJA    72–137   vuelve el groove en el primer rodillo (f.72).
                                   Tres hojas = tres golpes: f.72 · f.100 · f.128
  SHOT 06 · DOS HOJAS    138–209   el tap (f.180) = cut on impact al cajón (f.181).
                                   Entra el bajo = el motor de R.01
  SHOT 07 · NUEVE        210–293   nueve golpes acelerando: las hojas llegando

Rejilla 112,5 BPM (16 f por beat), continuando la del bloque 1: el groove entró
en el f.72 del capítulo; el compás 2 empieza en 136, el 3 en 200, el 4 en 264,
el 5 en 328, el 6 en 392. En frames locales (−144): 56 · 120 · 184 · 248.
El groove se APAGA en el post-it y VUELVE en el f.72 local — que no es un
downbeat (el 56 lo es). Se acepta: vuelve por acción (el primer rodillo), no por
compás, igual que entró.

Instrumentos: los mismos del bloque 1 (se copian, no se importan).
"""
import os
import wave
from pathlib import Path

import numpy as np
from scipy.signal import lfilter

SR = 48_000
FPS = 30
FRAMES = 294
BEAT_F = 16
DUR = FRAMES / FPS + 0.4
RAIZ = Path(__file__).resolve().parent.parent
_V = os.environ.get("VOZ_G", "D")
SALIDA = RAIZ / "public/assets/gcl/cap02/bloque2_audio.wav"
VOZ_MM = RAIZ / "public/assets/gcl/voz/G_eh_mm.wav"

pista = np.zeros(int(DUR * SR))
_rng = np.random.default_rng(20260906)


def f2s(f): return f / FPS


def poner(s, frame, gain=1.0):
    i = int(round(f2s(frame) * SR)); n = min(len(s), len(pista) - i)
    if n > 0: pista[i:i + n] += s[:n] * gain


def env(n, ataque=0.002, caida=None, curva=3.0):
    caida = caida if caida is not None else n / SR
    t = np.arange(n) / SR
    return np.clip(t / max(ataque, 1e-6), 0, 1) * np.exp(-curva * t / caida)


def n_ruido(n): return _rng.standard_normal(n)


def lp(x, corte, orden=2):
    a = np.exp(-2 * np.pi * corte / SR)
    for _ in range(orden): x = lfilter([1 - a], [1, -a], x)
    return x


def hp(x, corte): return x - lp(x, corte, 1)


def cabezal_marta(dur, lineas=6):
    n = int(dur * SR); v = np.zeros(n); por = dur / lineas
    for i in range(lineas):
        a = int(i * por * SR); k = int(por * 0.72 * SR); t = np.arange(k) / SR
        ag = (np.sign(np.sin(2 * np.pi * 1380 * t)) * 0.35 + np.sin(2 * np.pi * 690 * t) * 0.25) * (0.7 + 0.3 * np.sign(np.sin(2 * np.pi * 47 * t)))
        v[a:a + k] += lp(ag, 5200, 1) * np.clip(np.minimum(t, por * 0.72 - t) / 0.006, 0, 1) * 0.16
        j = a + k; k2 = int(0.035 * SR)
        if j + k2 < n: v[j:j + k2] += lp(n_ruido(k2), 1400) * env(k2, 0.0003, 0.02, 10) * 0.30
    return v


def zumbido_server(dur, gain=0.012):
    n = int(dur * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 59 * t) * 0.5 + np.sin(2 * np.pi * 118 * t) + 0.35 * np.sin(2 * np.pi * 236 * t) + lp(n_ruido(n), 1600) * 0.6) * gain


def kick(dur=0.13):
    n = int(dur * SR); t = np.arange(n) / SR
    c = np.sin(2 * np.pi * np.cumsum(110 * np.exp(-28 * t) + 44) / SR) * env(n, 0.0006, dur, 5)
    return np.tanh((c + n_ruido(n) * env(n, 0.0002, 0.004, 9) * 0.3) * 1.5) * 0.9


def clap(dur=0.2):
    n = int(dur * SR); v = hp(n_ruido(n), 1400) * env(n, 0.001, dur, 6)
    for d in (0.010, 0.021, 0.033):
        i = int(d * SR); v[i:] += hp(n_ruido(n - i), 1800) * env(n - i, 0.0005, 0.05, 9) * 0.6
    return v * 0.42


def hat(dur=0.045): n = int(dur * SR); return hp(n_ruido(n), 7000) * env(n, 0.0003, dur, 7) * 0.13


def bajo(hz, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    saw = 2 * (t * hz - np.floor(0.5 + t * hz))
    return lp(saw * 0.55 + np.sin(2 * np.pi * hz * t) * 0.75, 700, 2) * env(n, 0.004, dur, 2.6) * 0.34


def hoja_desliza(dur=0.22):
    """Una hoja de papel deslizándose sobre madera: fricción corta, seca."""
    n = int(dur * SR); t = np.arange(n) / SR
    return hp(lp(n_ruido(n), 2600, 1), 500) * np.sin(np.pi * t / dur) ** 0.7 * 0.22


def tap(dur=0.05):
    n = int(dur * SR)
    return (hp(n_ruido(n), 2000) * env(n, 0.0002, 0.012, 12) * 0.45 + np.sin(2 * np.pi * 1500 * np.arange(n) / SR) * env(n, 0.0003, 0.01, 12) * 0.2)


def cajon(dur=0.45):
    """Un cajón de archivo metálico abriéndose: rodamientos + tope."""
    n = int(dur * SR); t = np.arange(n) / SR
    rod = lp(n_ruido(n), 900, 2) * np.clip(np.minimum(t, dur - 0.06 - t) / 0.03, 0, 1) * 0.35
    j = int((dur - 0.07) * SR); k = n - j
    tope = np.sin(2 * np.pi * np.cumsum(180 * np.exp(-14 * np.arange(k) / SR) + 70) / SR) * env(k, 0.0006, 0.07, 6) * 0.6
    v = rod; v[j:] += tope
    return v


def motor_r01(dur, gain=0.05):
    n = int(dur * SR); t = np.arange(n) / SR
    v = (np.sin(2 * np.pi * 86 * t) + 0.4 * np.sin(2 * np.pi * 172 * t) + lp(n_ruido(n), 900) * 0.5) * gain
    for i in range(int(dur / 2)):
        j = int((i * 2 + 0.7) * SR); k = int(0.02 * SR)
        if j + k < n: v[j:j + k] += hp(n_ruido(k), 3000) * env(k, 0.0002, 0.008, 12) * gain * 6
    return v


def compas(inicio, hasta, gain=1.0, con_bajo=True):
    NOTAS = [55.0, 55.0, 82.41, 55.0, 73.42, 55.0, 65.41, 61.74]
    for b in range(4):
        f = inicio + b * BEAT_F
        if f < hasta: poner(kick() if b in (0, 2) else clap(), f, gain * (1.0 if b in (0, 2) else 0.9))
        for s16 in range(4):
            g = f + s16 * 4
            if g < hasta and not (b in (1, 3) and s16 == 0): poner(hat(), g, gain * (0.55 if s16 % 2 else 1.0))
    if con_bajo:
        for i, nz in enumerate(NOTAS):
            f = inicio + i * 8
            if f < hasta: poner(bajo(nz, 8 / FPS * 0.92), f, gain)


# ─────────────────────────────────────────────────────────────────────────────
poner(zumbido_server(f2s(FRAMES)), 0)                          # el fondo, apenas

# SHOT 04 · 0–71 · MÚSICA A CERO. Marta borrosa al fondo, apenas se oye
poner(cabezal_marta(f2s(72), lineas=9) * 0.35, 0)
w = wave.open(str(VOZ_MM)); mm = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, 2).mean(1) / 32768.0
poner(mm, 50, 0.9)                                              # «mm.» · f.50 local = f.194 del capítulo

# SHOT 05 · 72–137 · VUELVE EL GROOVE en el primer rodillo. Cada hoja, un golpe
compas(72, 136, gain=0.8, con_bajo=False)
for f in (72, 100, 128):
    poner(cabezal_marta(f2s(14), lineas=3), f)
    poner(hoja_desliza(0.18), f + 12, 0.8)

# SHOT 06 · 138–209 · capa 1: entra el bajo (el motor de R.01 está debajo)
compas(136, 200, gain=0.9)
compas(200, 210, gain=0.9)
poner(motor_r01(f2s(72), gain=0.04), 138)
poner(tap(), 180)                                               # el tap
poner(cajon(), 181, 0.9)                                        # = cut on impact: el cajón

# SHOT 07 · 210–293 · NUEVE golpes acelerando: las hojas llegan
compas(200, 264, gain=0.95)
compas(264, FRAMES, gain=0.95)
llegadas = [212, 222, 231, 239, 246, 252, 257, 261, 264]         # aceleran: 10 · 9 · 8 · 7 · 6 · 5 · 4 · 3
for f in llegadas:
    poner(hoja_desliza(0.2), f, 1.0)
    poner(hat() * 1.6, f + 4)
poner(motor_r01(f2s(40), gain=0.05), 250)                       # R.01 pasa con la regla

pico = float(np.max(np.abs(pista)))
pista = np.tanh(pista / max(pico, 1e-9) * 0.92) * 0.95
SALIDA.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(SALIDA), "wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
    wv.writeframes((np.clip(np.stack([pista, pista], 1), -1, 1) * 32767).astype("<i2").tobytes())
print(f"✓ {SALIDA.relative_to(RAIZ)}  ·  {FRAMES} f = {FRAMES/FPS:.2f} s  ·  pico previo {pico:.2f}")

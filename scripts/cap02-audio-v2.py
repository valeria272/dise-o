#!/usr/bin/env python3
"""CAP. 02 «ES UN CAMBIO CHICO» — CLARITY CUT V2 · 1454 frames = 48,5 s


    VOZ_G=D /Users/Vale/copylab-venv/bin/python3 scripts/cap02-audio-v2.py

Mismos instrumentos que el FULL ROUGH (se copian del script V1, no se importan).
Lo que cambia es la LÓGICA: el sonido es puntuación narrativa. Al principio
cada consecuencia tiene SU sonido, separado: clic → COPY · ping → DISEÑO ·
trrr → FORMATOS · hum + ticker → VIDEO · motor → R.01. Después se acumulan.
Después saturan. Corte a muestra cero en la carpeta. Silencio. Café. tsh-TUNK.

TIMELINE V2:
  01 0–20 · 02 21–71 · 03 72–119 · 04 120–216 (macro 172) · 05 217–324
  (copy 235–276 · layout 289–324) · 06 325–384 · 07 385–480 (formatos 433–468) ·
  08 481–546 · 09 547–646 (ticker 607) · LANDING 647–670 · 10 671–736 ·
  PAUTA 737–760 · 10b 761–808 · 10c 809–853 · ráfaga 854–889 ·
  PRESENTACIÓN 890–913 · 11 914–1003 (golpe 1001) · 12 1004–1081 ·
  13 1082–1201 · 14 1202–1279 · 15 1280–1357 · 16 1358–1393 · firma 1394–1453
"""
import os
import wave
from pathlib import Path

import numpy as np
from scipy.signal import lfilter

SR = 48_000
FPS = 30
FRAMES = 1454
BEAT_F = 16
DUR = FRAMES / FPS + 0.5
RAIZ = Path(__file__).resolve().parent.parent
_V = os.environ.get("VOZ_G", "D")
SALIDA = RAIZ / "public/assets/gcl/cap02/v2_audio.wav"
VOZ = RAIZ / "public/assets/gcl/voz" / f"G_eh_{_V}.wav"
VOZ_MM = RAIZ / "public/assets/gcl/voz/G_eh_mm.wav"

pista = np.zeros(int(DUR * SR))
_rng = np.random.default_rng(20260907)


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


def wav(ruta):
    w = wave.open(str(ruta)); return np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, 2).mean(1) / 32768.0


# ── instrumentos (mismos que los bloques) ────────────────────────────────────
def tsh_tunk(dur=0.75):
    n = int(dur * SR); v = np.zeros(n)
    k = int(0.16 * SR); v[:k] += hp(lp(n_ruido(k), 3800, 1), 900) * np.sin(np.pi * np.arange(k) / k) ** 1.4 * 0.42
    i = int(0.15 * SR); k2 = int(0.32 * SR); tt = np.arange(k2) / SR
    golpe = np.sin(2 * np.pi * np.cumsum(140 * np.exp(-18 * tt) + 62) / SR) * env(k2, 0.0006, 0.32, 6)
    alambre = (np.sin(2 * np.pi * 1840 * tt) * 0.5 + np.sin(2 * np.pi * 2710 * tt) * 0.3) * env(k2, 0.0004, 0.16, 7)
    v[i:i + k2] += np.tanh((golpe * 1.6 + lp(n_ruido(k2), 700) * env(k2, 0.0004, 0.05, 9) * 0.6)) * 0.9 + alambre * 0.28
    for d, g in ((0.38, 1.0), (0.47, 0.55)):
        j = int(d * SR); k3 = int(0.26 * SR); t3 = np.arange(k3) / SR
        v[j:j + k3] += (np.sin(2 * np.pi * 2093 * t3) * 0.55 + np.sin(2 * np.pi * 3520 * t3) * 0.3 + np.sin(2 * np.pi * 5274 * t3) * 0.12) * env(k3, 0.0005, 0.26, 5.5) * 0.30 * g
    return v


def cabezal_marta(dur, lineas=6, gain=1.0):
    n = int(dur * SR); v = np.zeros(n); por = dur / lineas
    for i in range(lineas):
        a = int(i * por * SR); k = int(por * 0.72 * SR); t = np.arange(k) / SR
        ag = (np.sign(np.sin(2 * np.pi * 1380 * t)) * 0.35 + np.sin(2 * np.pi * 690 * t) * 0.25) * (0.7 + 0.3 * np.sign(np.sin(2 * np.pi * 47 * t)))
        v[a:a + k] += lp(ag, 5200, 1) * np.clip(np.minimum(t, por * 0.72 - t) / 0.006, 0, 1) * 0.16
        j = a + k; k2 = int(0.035 * SR)
        if j + k2 < n: v[j:j + k2] += lp(n_ruido(k2), 1400) * env(k2, 0.0003, 0.02, 10) * 0.30
    return v * gain


def zumbido_server(dur, gain=0.012, hz=118):
    n = int(dur * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * hz / 2 * t) * 0.5 + np.sin(2 * np.pi * hz * t) + 0.35 * np.sin(2 * np.pi * hz * 2 * t) + lp(n_ruido(n), 1600) * 0.6) * gain


def r01_frena(dur=0.5):
    n = int(dur * SR); t = np.arange(n) / SR; v = np.zeros(n)
    k = int(0.11 * SR)
    v[:k] += (np.sin(2 * np.pi * np.cumsum(2900 - 900 * np.arange(k) / k) / SR) * env(k, 0.002, 0.11, 4) * 0.6 + hp(n_ruido(k), 2500) * env(k, 0.001, 0.08, 6) * 0.4) * 0.28
    j = int(0.12 * SR); k2 = int(0.03 * SR); v[j:j + k2] += hp(n_ruido(k2), 1800) * env(k2, 0.0002, 0.012, 12) * 0.5
    j = int(0.15 * SR); k3 = min(int(0.34 * SR), n - j); t3 = np.arange(k3) / SR
    if k3 > 0:
        v[j:j + k3] += np.sin(2 * np.pi * (210 + 26 * np.sin(2 * np.pi * 9 * t3) * np.exp(-6 * t3)) * t3) * env(k3, 0.001, 0.34, 4.5) * 0.24
    return v


def toing(dur=0.34):
    t = np.arange(int(dur * SR)) / SR
    return np.sin(2 * np.pi * (210 + 26 * np.sin(2 * np.pi * 9 * t) * np.exp(-6 * t)) * t) * env(len(t), 0.001, dur, 4.5) * 0.22


def motor_r01(dur, gain=0.05):
    n = int(dur * SR); t = np.arange(n) / SR
    v = (np.sin(2 * np.pi * 86 * t) + 0.4 * np.sin(2 * np.pi * 172 * t) + lp(n_ruido(n), 900) * 0.5) * gain
    for i in range(int(dur / 2)):
        j = int((i * 2 + 0.7) * SR); k = int(0.02 * SR)
        if j + k < n: v[j:j + k] += hp(n_ruido(k), 3000) * env(k, 0.0002, 0.008, 12) * gain * 6
    return v


def kick(dur=0.13):
    n = int(dur * SR); t = np.arange(n) / SR
    c = np.sin(2 * np.pi * np.cumsum(110 * np.exp(-28 * t) + 44) / SR) * env(n, 0.0006, dur, 5)
    return np.tanh((c + n_ruido(n) * env(n, 0.0002, 0.004, 9) * 0.3) * 1.5) * 0.9


def clap(dur=0.2):
    n = int(dur * SR); v = hp(n_ruido(n), 1400) * env(n, 0.001, dur, 6)
    for d in (0.010, 0.021, 0.033):
        i = int(d * SR); v[i:] += hp(n_ruido(n - i), 1800) * env(n - i, 0.0005, 0.05, 9) * 0.6
    return v * 0.42


def hat(dur=0.045, abierto=False):
    d = 0.13 if abierto else dur; n = int(d * SR)
    return hp(n_ruido(n), 7000) * env(n, 0.0003, d, 7) * (0.16 if abierto else 0.13)


def bajo(hz, dur, corte=700):
    n = int(dur * SR); t = np.arange(n) / SR
    saw = 2 * (t * hz - np.floor(0.5 + t * hz))
    return lp(saw * 0.55 + np.sin(2 * np.pi * hz * t) * 0.75, corte, 2) * env(n, 0.004, dur, 2.6) * 0.34


def hoja_desliza(dur=0.22):
    n = int(dur * SR); t = np.arange(n) / SR
    return hp(lp(n_ruido(n), 2600, 1), 500) * np.sin(np.pi * t / dur) ** 0.7 * 0.22


def tap(dur=0.05):
    n = int(dur * SR)
    return hp(n_ruido(n), 2000) * env(n, 0.0002, 0.012, 12) * 0.45 + np.sin(2 * np.pi * 1500 * np.arange(n) / SR) * env(n, 0.0003, 0.01, 12) * 0.2


def cajon(dur=0.45):
    n = int(dur * SR); t = np.arange(n) / SR
    rod = lp(n_ruido(n), 900, 2) * np.clip(np.minimum(t, dur - 0.06 - t) / 0.03, 0, 1) * 0.35
    j = int((dur - 0.07) * SR); k = n - j
    rod[j:] += np.sin(2 * np.pi * np.cumsum(180 * np.exp(-14 * np.arange(k) / SR) + 70) / SR) * env(k, 0.0006, 0.07, 6) * 0.6
    return rod


def papel_continuo(dur, gain=0.3):
    """Un kilómetro de papel deslizándose por hormigón: fricción continua con
    el traqueteo de las perforaciones."""
    n = int(dur * SR); t = np.arange(n) / SR
    v = hp(lp(n_ruido(n), 2200, 1), 400) * 0.5
    v *= 0.8 + 0.2 * np.sign(np.sin(2 * np.pi * 11 * t))            # las perforaciones
    borde = np.clip(t / 0.15, 0, 1) * np.clip((dur - t) / 0.2, 0, 1)
    return v * borde * gain


def tiron(dur=0.16):
    """El tirón de papel de G: seco, corto, un desgarro."""
    n = int(dur * SR); t = np.arange(n) / SR
    return (hp(n_ruido(n), 1800) * env(n, 0.001, 0.09, 6) * 0.9 + lp(n_ruido(n), 600) * env(n, 0.0005, 0.03, 10) * 0.5) * 0.5


def tono_viaja(dur=1.2):
    """La luz corriendo por el cable: un tono que sube y va de izquierda a
    derecha (la pista es mono: se emula con un tremolo que acelera)."""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 320 * 2 ** (t / dur * 1.5)
    v = np.sin(2 * np.pi * np.cumsum(f) / SR) * (0.6 + 0.4 * np.sign(np.sin(2 * np.pi * (6 + 14 * t / dur) * t)))
    return lp(v, 3000, 1) * env(n, 0.05, dur, 2) * 0.16


def ticker_tick(dur=0.04):
    n = int(dur * SR)
    return (np.sin(2 * np.pi * 2400 * np.arange(n) / SR) * 0.6 + hp(n_ruido(n), 4000) * 0.4) * env(n, 0.0002, 0.015, 12) * 0.2


def carpeta_cierra(dur=0.3):
    n = int(dur * SR); t = np.arange(n) / SR
    v = np.sin(2 * np.pi * np.cumsum(160 * np.exp(-20 * t) + 55) / SR) * env(n, 0.0005, 0.22, 6)
    v += lp(n_ruido(n), 1200) * env(n, 0.0003, 0.04, 10) * 0.8
    return np.tanh(v * 1.6) * 0.8


def ding_ascensor(dur=0.9):
    n = int(dur * SR); t = np.arange(n) / SR
    v = (np.sin(2 * np.pi * 1318 * t) * 0.6 + np.sin(2 * np.pi * 1976 * t) * 0.3 + np.sin(2 * np.pi * 2637 * t) * 0.1) * env(n, 0.001, dur, 4)
    return v * 0.3


def puertas(dur=0.7, gain=0.28):
    n = int(dur * SR); t = np.arange(n) / SR
    v = lp(n_ruido(n), 700, 2) * np.sin(np.pi * t / dur) ** 0.8
    j = int((dur - 0.08) * SR); k = n - j
    v[j:] += lp(n_ruido(k), 500) * env(k, 0.0004, 0.06, 9) * 1.4
    return v * gain


def paso(dur=0.12):
    n = int(dur * SR)
    return lp(n_ruido(n), 900, 2) * env(n, 0.001, 0.08, 7) * 0.4


def clic_contador(dur=0.06):
    n = int(dur * SR)
    return (hp(n_ruido(n), 2500) * env(n, 0.0002, 0.012, 12) * 0.5 + np.sin(2 * np.pi * 900 * np.arange(n) / SR) * env(n, 0.0003, 0.03, 8) * 0.3) * 0.35


def sorbo(dur=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    return lp(n_ruido(n), 1200, 2) * np.sin(np.pi * t / dur) ** 2 * 0.12


def tick_visor(dur=0.06):
    n = int(dur * SR); return hp(n_ruido(n), 4000) * env(n, 0.0002, 0.012, 12) * 0.13


def muerte_electrica(dur=0.45):
    n = int(dur * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(700 * np.exp(-7 * t) + 45) / SR) * env(n, 0.001, dur, 4) * 0.22


def nota_grave(dur, hz=98, gain=0.05):
    n = int(dur * SR); t = np.arange(n) / SR
    v = np.sin(2 * np.pi * hz * t) * 0.6 + np.sin(2 * np.pi * hz * 2 * t) * 0.22 + np.sin(2 * np.pi * hz * 3 * t) * 0.08
    return v * np.clip(t / 0.25, 0, 1) * np.clip((dur - t) / 0.6, 0, 1) * gain


NOTAS = [55.0, 55.0, 82.41, 55.0, 73.42, 55.0, 65.41, 61.74]


def compas(inicio, hasta, gain=1.0, capas=3):
    """capas: 1 = sólo hats y kick · 2 = + clap · 3 = + bajo · 4 = + hats abiertos y bajo al frente"""
    for b in range(4):
        f = inicio + b * BEAT_F
        if f < hasta:
            if b in (0, 2): poner(kick(), f, gain)
            elif capas >= 2: poner(clap(), f, gain * 0.9)
        for s16 in range(4):
            g = f + s16 * 4
            if g < hasta and not (b in (1, 3) and s16 == 0):
                poner(hat(abierto=(capas >= 4 and s16 == 2)), g, gain * (0.55 if s16 % 2 else 1.0))
    if capas >= 3:
        for i, nz in enumerate(NOTAS):
            f = inicio + i * 8
            if f < hasta: poner(bajo(nz, 8 / FPS * 0.92, corte=700 if capas < 4 else 1400), f, gain * (1.0 if capas < 4 else 1.25))


# ═════════════════════════════════════════════════════════════════════════════
# EL MONTAJE
# ═════════════════════════════════════════════════════════════════════════════

# ambiente del Nivel -1: el zumbido del Server, que muere en el 33 y vuelve en el 72


def ping(hz=1568, dur=0.28):
    """El ping de «llegó otra cosa»: dos parciales, ataque limpio."""
    n = int(dur * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * hz * t) * 0.6 + np.sin(2 * np.pi * hz * 1.5 * t) * 0.25) * env(n, 0.001, dur, 4.5) * 0.22


def clic(dur=0.05):
    n = int(dur * SR)
    return (hp(n_ruido(n), 2500) * env(n, 0.0002, 0.01, 12) * 0.5 + np.sin(2 * np.pi * 1200 * np.arange(n) / SR) * env(n, 0.0003, 0.012, 10) * 0.25) * 0.9


def sello_golpe(dur=0.18):
    """El sello de goma cayendo sobre la hoja: golpe sordo + el papel."""
    n = int(dur * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * np.cumsum(220 * np.exp(-30 * t) + 90) / SR) * env(n, 0.0005, 0.12, 6) * 0.7 + lp(n_ruido(n), 1500) * env(n, 0.0003, 0.03, 10) * 0.5) * 0.5


# ═════════════════════════════════════════════════════════════════════════════
# EL MONTAJE V2
# ═════════════════════════════════════════════════════════════════════════════
z = zumbido_server(f2s(33)); z[-int(0.004 * SR):] *= np.linspace(1, 0, int(0.004 * SR)); poner(z, 0)
poner(zumbido_server(f2s(1001 - 72)), 72)
poner(zumbido_server(f2s(FRAMES - 1004), gain=0.006), 1004)

# ── INTRIGA · hook (igual que V1) ────────────────────────────────────────────
poner(tsh_tunk(), 0)
poner(cabezal_marta(f2s(12), lineas=4), 21)
poner(r01_frena(), 45)
poner(wav(VOZ), 60, 0.9)
compas(72, 120, gain=1.0, capas=2)                             # el groove entra con el wide, 48 f
poner(cabezal_marta(f2s(48), lineas=8, gain=0.55), 72)

# ── REVELACIÓN · 04 · 120–216 · música a CERO · el post-it 1,5 s · «mm.» ─────
poner(cabezal_marta(f2s(50), lineas=6, gain=0.3), 120)
poner(wav(VOZ_MM), 190, 0.9)

# ── CONSECUENCIA 1 · COPY · 217–288 · clic → la hoja ─────────────────────────
compas(217, 281, gain=0.75, capas=2)
poner(cabezal_marta(f2s(14), lineas=3), 217); poner(hoja_desliza(0.18), 229, 0.8)
poner(clic(), 235); poner(sello_golpe(), 238)                  # CLIC → COPY
poner(cabezal_marta(f2s(10), lineas=2), 277); poner(hoja_desliza(0.18), 283, 0.8)
# ── CONSECUENCIA 2 · DISEÑO · 289–324 · ping → no cabe ──────────────────────
compas(281, 325, gain=0.8, capas=2)
poner(ping(), 289); poner(sello_golpe(), 292)                  # PING → DISEÑO
poner(ping(1760, 0.2) * 0.6, 313)                              # el «!!»

# ── 06 · 325–384 · G arregla el copy (tap) → un cajón se abre solo ──────────
compas(325, 389, gain=0.9, capas=3)
poner(motor_r01(f2s(60), gain=0.04), 325)
poner(tap(), 367); poner(cajon(), 368, 0.9)

# ── CONSECUENCIA 3 · FORMATOS · 385–480 · trrr × 9 ───────────────────────────
compas(389, 453, gain=0.95, capas=3); compas(453, 481, gain=0.95, capas=3)
poner(cabezal_marta(f2s(46), lineas=9, gain=0.9), 385)         # Marta imprime las nueve
for f in (387, 396, 404, 411, 417, 422, 426, 429, 432): poner(hoja_desliza(0.2), f); poner(hat() * 1.6, f + 4)
poner(sello_golpe(), 433)                                      # FORMATOS ×9
for i in range(9): poner(ticker_tick() * 1.3, 436 + i * 3)     # nueve ticks: nueve hojas tachadas
poner(motor_r01(f2s(14), gain=0.05), 469)                      # R.01 con la regla

# ── ACELERACIÓN · 08 · 481–546 · R.01 trabado ────────────────────────────────
compas(481, 545, gain=0.95, capas=3)
poner(motor_r01(f2s(66), gain=0.06), 481)
for f in (503, 515, 527): poner(r01_frena(0.25) * 0.7, f)
for f in (507, 519, 531): poner(toing(0.25), f, 0.8)
poner(lp(n_ruido(int(0.3 * SR)), 500) * env(int(0.3 * SR), 0.01, 0.25, 4) * 0.35, 538)
poner(ticker_tick() * 1.5, 545)

# ── CONSECUENCIA 4 · VIDEO · 547–646 · hum + ticker ──────────────────────────
compas(545, 609, gain=1.0, capas=3); compas(609, 647, gain=1.0, capas=4)
poner(wav(VOZ_MM), 553, 0.9)
poner(tap(), 580)
poner(tono_viaja(0.9), 583)                                    # la luz corre por el cable
poner(zumbido_server(f2s(46), gain=0.02, hz=130), 600)
poner(sello_golpe() * 0.8, 607)
for i, f in enumerate([609, 615, 620, 624, 628, 631, 634, 636, 638]): poner(ticker_tick() * (1.0 + i * 0.08), f)
poner(ping(2093, 0.3) * 0.7, 642)                              # RENDER 9/9

# ── CONSECUENCIA 5 · LANDING · 647–666 → 10 · 667–736 · medio Nivel -1 ───────
compas(647, 711, gain=1.1, capas=4); compas(711, 737, gain=1.1, capas=4)
poner(sello_golpe(), 647); poner(ping(1318, 0.25) * 0.8, 650)
poner(cabezal_marta(f2s(66), lineas=13, gain=0.8), 671)
poner(motor_r01(f2s(66), gain=0.07), 671)
for f in range(676, 737, 14): poner(cajon(0.35) * 0.7, f)
poner(papel_continuo(f2s(36), gain=0.25), 700)

# ── CONSECUENCIA 6 · PAUTA · 737–756 → 10b · 757–808 · un kilómetro ──────────
compas(737, 801, gain=1.1, capas=4); compas(801, 809, gain=1.1, capas=4)
poner(sello_golpe(), 737); poner(ping(1046, 0.25) * 0.8, 740); poner(ping(1318, 0.2) * 0.6, 748)
poner(papel_continuo(f2s(48), gain=0.35), 761)
poner(cabezal_marta(f2s(48), lineas=9, gain=0.5), 761)
poner(motor_r01(f2s(40), gain=0.07), 761)
poner(tiron(), 799, 1.2)                                       # G arranca una línea

# ── 10c · 809–853 · el que baja y se va · la orquesta BAJA un beat ───────────
compas(809, 854, gain=0.55, capas=4)
poner(ding_ascensor(), 809); poner(puertas(), 813); poner(paso(), 823); poner(paso() * 0.8, 835)
poner(tap() * 0.6, 841); poner(puertas(0.5), 845); poner(ding_ascensor(0.6), 850)

# ── SATURACIÓN · ráfaga · 854–889 ────────────────────────────────────────────
compas(854, 890, gain=1.15, capas=4)
poner(cabezal_marta(f2s(12), lineas=3, gain=1.2), 854)
poner(motor_r01(f2s(12), gain=0.09), 866)
for f in (878, 882, 886): poner(ticker_tick() * 1.6, f)

# ── CONSECUENCIA 7 · PRESENTACIÓN · 890–913 → 11 · la carpeta · 914–1003 ─────
compas(890, 954, gain=1.15, capas=4); compas(954, 1001, gain=1.15, capas=4)
poner(sello_golpe() * 1.1, 890); poner(ping(880, 0.3) * 0.8, 893)
poner(hoja_desliza(0.25), 950)
i0 = int(round(f2s(1001) * SR)); pista[i0:] = 0                 # MUERE A MUESTRA CERO
poner(carpeta_cierra(), 1001)                                  # EL GOLPE

# ── RESOLUCIÓN · 12 · sube · 1004–1081 · silencio + máquina ──────────────────
poner(hoja_desliza(0.3) * 0.8, 1006)
poner(motor_r01(f2s(60), gain=0.06), 1010)
poner(papel_continuo(f2s(50), gain=0.12), 1010)
poner(puertas(), 1058)
poner(ding_ascensor(), 1074)                                   # DING · sube · todo para
poner(muerte_electrica(0.6) * 0.6, 1076)

# ── SILENCIO · CAFÉ · 13 · 1082–1201 ─────────────────────────────────────────
poner(ding_ascensor(0.7) * 0.5, 1112); poner(puertas(0.5, gain=0.15), 1118)
poner(clic_contador(), 1152)                                   # 000 → 001
poner(tick_visor() * 0.8, 1160)
poner(sorbo(), 1176)                                           # G recupera el café

# ── 14 · 1202–1279 · tsh-TUNK · «una cosita más…» ────────────────────────────
poner(tsh_tunk(), 1202)
# ── 15 · 1280–1357 · un rodillo. NO. ─────────────────────────────────────────
poner(cabezal_marta(f2s(8), lineas=2), 1288)
poner(lp(n_ruido(int(0.12 * SR)), 1500, 2) * env(int(0.12 * SR), 0.001, 0.08, 8) * 0.25, 1314)
# ── 16 · 1358–1393 · el visor −15 % ──────────────────────────────────────────
poner(tick_visor(), 1372)
# ── firma · 1394 ─────────────────────────────────────────────────────────────
poner(nota_grave(f2s(60)), 1394)

pico = float(np.max(np.abs(pista)))
pista = np.tanh(pista / max(pico, 1e-9) * 0.92) * 0.95
SALIDA.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(SALIDA), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(np.stack([pista, pista], 1), -1, 1) * 32767).astype("<i2").tobytes())
print(f"✓ {SALIDA.relative_to(RAIZ)}  ·  {FRAMES} f = {FRAMES/FPS:.2f} s  ·  pico previo {pico:.2f}")

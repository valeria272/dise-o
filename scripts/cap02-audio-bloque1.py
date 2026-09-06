#!/usr/bin/env python3
"""CAP. 02 «ES UN CAMBIO CHICO» — BLOQUE 1 · SHOTS 01–03 · 0:00,0 – 0:04,8

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-audio-bloque1.py

El bloque de prueba del capítulo: 144 frames = 4,8 s. Los sonidos de serie
nacen acá —el tsh-TUNK del tubo, el «eh?» de G— y por eso se sintetizan con
cuidado: lo que suene en este bloque es lo que va a sonar en toda la serie.

Reutiliza los instrumentos del prototipo (`cap02-audio.py`) y agrega los que el
storyboard V1.6 pide para el hook:

  f.  0   tsh-TUNK        aire comprimido + golpe seco + campanita vieja del tubo
  f. 21   rodillos Marta  el cabezal de una matricial: zumbido agudo por líneas
  f. 36   el Server muere el zumbido de fondo se corta a MUESTRA CERO
  f. 51   R.01 frena      chirrido de goma + clic de relé + «toing» del mástil
  f. 63   «eh?»           el chirp de G: dos notos que suben y una caída corta
  f. 78   ENTRA EL GROOVE el corte al wide. Los rodillos ya son percusión
  f.144   fin del bloque

Rejilla: 112,5 BPM = 16 frames por beat, igual que el prototipo. El groove
entra en el f.78 (no en downbeat: es un corte por acción, y el compás se ancla
ahí — el compás 1 EMPIEZA en el 78).

Registro de G (LOCK 6): «eh?» es curioso, no alarmado. Sube, se detiene, cae
un poco. Corto. Sin vibrato. Electrónico pero no de juguete.
"""
import sys
import wave
from pathlib import Path

import numpy as np

# Los instrumentos del prototipo se copian acá en vez de importarse:
# cap02-audio.py ejecuta su montaje al importarse. Misma paleta sonora.

SR = 48_000
FPS = 30
FRAMES = 138            # V2 hard cuts: 21 · 12 · 12 · 12 · 15 · 66
BEAT_F = 16
DUR = FRAMES / FPS + 0.4

RAIZ = Path(__file__).resolve().parent.parent
_V = __import__("os").environ.get("VOZ_G", "D")
SALIDA = RAIZ / "public/assets/gcl/cap02" / (f"bloque1_audio_{_V}.wav" if __import__("os").environ.get("SUFIJO") else "bloque1_audio.wav")
VOZ = RAIZ / "public/assets/gcl/voz" / f"G_eh_{_V}.wav"   # VOZ_G=A..E · 4A · 4B · 4C

pista = np.zeros(int(DUR * SR))
_rng = np.random.default_rng(20260905)


def f2s(f):
    return f / FPS


def poner(sonido, frame, gain=1.0):
    i = int(round(f2s(frame) * SR))
    n = min(len(sonido), len(pista) - i)
    if n > 0:
        pista[i:i + n] += sonido[:n] * gain


def env(n, ataque=0.002, caida=None, curva=3.0):
    caida = caida if caida is not None else n / SR
    t = np.arange(n) / SR
    return np.clip(t / max(ataque, 1e-6), 0, 1) * np.exp(-curva * t / caida)


def n_ruido(n):
    return _rng.standard_normal(n)


from scipy.signal import lfilter  # noqa: E402


def lp(x, corte, orden=2):
    a = np.exp(-2 * np.pi * corte / SR)
    y = x
    for _ in range(orden):
        y = lfilter([1 - a], [1, -a], y)
    return y


def hp(x, corte):
    return x - lp(x, corte, 1)


# ─────────────────────────────────────────────────────────────────────────────
# LOS SONIDOS DE SERIE — nacen acá
# ─────────────────────────────────────────────────────────────────────────────

def tsh_tunk(dur=0.75):
    """El tubo neumático. Aire que llega, el golpe de la carpeta en la canasta
    de alambre, y la campanita mecánica que los tubos viejos tenían para avisar.
    ES EL SONIDO DE SERIE: el mismo sample en el 0:00 y en el 0:44."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = np.zeros(n)
    # tsh: aire comprimido, sube y se corta
    k = int(0.16 * SR)
    v[:k] += hp(lp(n_ruido(k), 3800, 1), 900) * np.sin(np.pi * np.arange(k) / k) ** 1.4 * 0.42
    # TUNK: golpe seco + la canasta de alambre vibrando
    i = int(0.15 * SR); k2 = int(0.32 * SR)
    tt = np.arange(k2) / SR
    golpe = np.sin(2 * np.pi * np.cumsum(140 * np.exp(-18 * tt) + 62) / SR) * env(k2, 0.0006, 0.32, 6)
    alambre = (np.sin(2 * np.pi * 1840 * tt) * 0.5 + np.sin(2 * np.pi * 2710 * tt) * 0.3) * env(k2, 0.0004, 0.16, 7)
    v[i:i + k2] += np.tanh((golpe * 1.6 + lp(n_ruido(k2), 700) * env(k2, 0.0004, 0.05, 9) * 0.6)) * 0.9 + alambre * 0.28
    # la campanita del tubo: dos golpecitos de campana de bronce, chicos
    for d, g in ((0.38, 1.0), (0.47, 0.55)):
        j = int(d * SR); k3 = int(0.26 * SR); t3 = np.arange(k3) / SR
        camp = (np.sin(2 * np.pi * 2093 * t3) * 0.55 + np.sin(2 * np.pi * 3520 * t3) * 0.3
                + np.sin(2 * np.pi * 5274 * t3) * 0.12) * env(k3, 0.0005, 0.26, 5.5)
        v[j:j + k3] += camp * 0.30 * g
    return v


def cabezal_marta(dur, lineas=6):
    """Una matricial imprimiendo: el cabezal zumba línea por línea (un buzz de
    ~1,4 kHz con textura de agujas) y el tractor avanza con un tac entre líneas."""
    n = int(dur * SR)
    v = np.zeros(n)
    por_linea = dur / lineas
    for i in range(lineas):
        a = int(i * por_linea * SR)
        k = int(por_linea * 0.72 * SR)
        t = np.arange(k) / SR
        agujas = np.sign(np.sin(2 * np.pi * 1380 * t)) * 0.35 + np.sin(2 * np.pi * 690 * t) * 0.25
        agujas *= (0.7 + 0.3 * np.sign(np.sin(2 * np.pi * 47 * t)))       # textura de puntos
        v[a:a + k] += lp(agujas, 5200, 1) * np.clip(np.minimum(t, por_linea * 0.72 - t) / 0.006, 0, 1) * 0.16
        # el tac del tractor
        j = a + k; k2 = int(0.035 * SR)
        if j + k2 < n:
            v[j:j + k2] += lp(n_ruido(k2), 1400) * env(k2, 0.0003, 0.02, 10) * 0.30
    return v


def zumbido_server(dur, gain=0.02):
    """El fondo del Nivel -1. Hum de 118 Hz con armónicos, sub y ventiladores."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = (np.sin(2 * np.pi * 59 * t) * 0.5 + np.sin(2 * np.pi * 118 * t) + 0.35 * np.sin(2 * np.pi * 236 * t)
         + lp(n_ruido(n), 1600) * 0.6)
    return v * gain


def r01_frena(dur=0.5):
    """Chirrido corto de goma sobre hormigón, clic de relé al invertir, y el
    «toing» del mástil: un resorte real, grave, corto. Nada de dibujo animado."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = np.zeros(n)
    k = int(0.11 * SR)
    chirr = np.sin(2 * np.pi * np.cumsum(2900 - 900 * np.arange(k) / k) / SR) * env(k, 0.002, 0.11, 4)
    v[:k] += (chirr * 0.6 + hp(n_ruido(k), 2500) * env(k, 0.001, 0.08, 6) * 0.4) * 0.28
    j = int(0.12 * SR); k2 = int(0.03 * SR)
    v[j:j + k2] += hp(n_ruido(k2), 1800) * env(k2, 0.0002, 0.012, 12) * 0.5      # clic de relé
    j = int(0.15 * SR); k3 = int(0.34 * SR); t3 = np.arange(k3) / SR
    toing = np.sin(2 * np.pi * (210 + 26 * np.sin(2 * np.pi * 9 * t3) * np.exp(-6 * t3)) * t3) * env(k3, 0.001, 0.34, 4.5)
    v[j:j + k3] += toing * 0.24
    return v


def eh_de_g(dur=0.42):
    """«eh?». El chirp de G. Dos notas que suben (curiosidad), una pausa de nada,
    y una caída corta (la pregunta). Onda cuadrada suavizada con un poco de
    portamento: electrónico, no de juguete. LOCK 6: curioso, no alarmado."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = np.where(t < 0.13, 520 + 160 * (t / 0.13),
        np.where(t < 0.22, 690,
        np.where(t < 0.30, 690 + 120 * ((t - 0.22) / 0.08),
                 810 - 190 * ((t - 0.30) / 0.12))))
    fase = 2 * np.pi * np.cumsum(f) / SR
    v = np.sign(np.sin(fase)) * 0.45 + np.sin(fase) * 0.55
    v = lp(v, 2400, 2)
    amp = np.clip(t / 0.01, 0, 1) * np.clip((dur - t) / 0.05, 0, 1)
    amp *= np.where((t > 0.20) & (t < 0.225), 0.15, 1.0)           # la micro-pausa antes de la pregunta
    return v * amp * 0.30


def kick(dur=0.13):
    n = int(dur * SR); t = np.arange(n) / SR
    cuerpo = np.sin(2 * np.pi * np.cumsum(110 * np.exp(-28 * t) + 44) / SR) * env(n, 0.0006, dur, 5)
    return np.tanh((cuerpo + n_ruido(n) * env(n, 0.0002, 0.004, 9) * 0.3) * 1.5) * 0.9


def clap(dur=0.2):
    n = int(dur * SR)
    v = hp(n_ruido(n), 1400) * env(n, 0.001, dur, 6)
    for d in (0.010, 0.021, 0.033):
        i = int(d * SR); v[i:] += hp(n_ruido(n - i), 1800) * env(n - i, 0.0005, 0.05, 9) * 0.6
    return v * 0.42


def hat(dur=0.045):
    n = int(dur * SR)
    return hp(n_ruido(n), 7000) * env(n, 0.0003, dur, 7) * 0.13


def bajo(hz, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    saw = 2 * (t * hz - np.floor(0.5 + t * hz))
    v = lp(saw * 0.55 + np.sin(2 * np.pi * hz * t) * 0.75, 700, 2)
    return v * env(n, 0.004, dur, 2.6) * 0.34


# ─────────────────────────────────────────────────────────────────────────────
# EL MONTAJE DEL BLOQUE
# ─────────────────────────────────────────────────────────────────────────────

# V2 · hard cuts. Estaciones: Marta 21–32 · Server 33–44 · R.01 45–56 · G 57–71 · wide 72–137
# el zumbido del Server existe desde el frame 0 y MUERE a muestra cero en el f.33
zum = zumbido_server(f2s(33))
zum[-int(0.004 * SR):] *= np.linspace(1, 0, int(0.004 * SR))       # 4 ms para que no haga clic
poner(zum, 0)

poner(tsh_tunk(), 0)                                  # SHOT 01 · f.0

poner(cabezal_marta(f2s(12), lineas=4), 21)           # 02a · Marta, f.21–32
# f.33 · el Server se apaga: el zumbido ya se cortó arriba. Silencio de 12 frames.
poner(r01_frena(), 45)                                # 02c · R.01, f.45
# 02d · «eh?» · f.60 — la voz viene de un archivo: es la que se está probando
def _voz():
    w = wave.open(str(VOZ)); x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, 2).mean(1) / 32768.0
    return x
poner(_voz(), 60, 0.9)

# SHOT 03 · f.72 · smash cut al wide: ENTRA EL GROOVE. El compás empieza acá.
INICIO = 72
NOTAS = [55.0, 55.0, 82.41, 55.0, 73.42, 55.0, 65.41, 61.74]
for b in range(4):
    f = INICIO + b * BEAT_F
    if f >= FRAMES: break
    poner(kick() if b in (0, 2) else clap(), f, 1.0 if b in (0, 2) else 0.9)
    for s16 in range(4):
        g = f + s16 * 4
        if g < FRAMES and not (b in (1, 3) and s16 == 0):
            poner(hat(), g, 0.55 if s16 % 2 else 1.0)
for i, nz in enumerate(NOTAS):
    f = INICIO + i * 8
    if f < FRAMES:
        poner(bajo(nz, 8 / FPS * 0.92), f)
# los rodillos de Marta como percusión, por debajo del groove
poner(cabezal_marta(f2s(FRAMES - INICIO), lineas=11) * 0.55, INICIO)
# el zumbido vuelve con el groove, más bajo — el Server "volvió"
poner(zumbido_server(f2s(FRAMES - INICIO), gain=0.012), INICIO)

pico = float(np.max(np.abs(pista)))
pista = np.tanh(pista / max(pico, 1e-9) * 0.92) * 0.95
SALIDA.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(SALIDA), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(np.stack([pista, pista], 1), -1, 1) * 32767).astype("<i2").tobytes())
print(f"✓ {SALIDA.relative_to(RAIZ)}  ·  {FRAMES} f = {FRAMES/FPS:.2f} s  ·  pico previo {pico:.2f}")

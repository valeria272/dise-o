#!/usr/bin/env python3
"""LA VOZ DE G — cinco alternativas para el «eh?», aisladas y sincronizables.

    /Users/Vale/copylab-venv/bin/python3 scripts/g-voz-eh.py

Salen seis archivos en public/assets/gcl/voz/:
    G_eh_A.wav … G_eh_E.wav   las cinco, cada una de 0,42 s, con el ataque en t=0
    G_eh_5_alternativas.wav   las cinco seguidas con un segundo de silencio entre
                              cada una, para compararlas de una sola escuchada

Todas miden lo mismo y empiezan en el mismo instante: se pueden intercambiar
en el montaje sin mover nada. Ninguna es infantil, adorable, caricaturesca,
de personaje conocido ni de asistente virtual. La idea es una vocalización
propia que ACCIDENTALMENTE comunica «¿eh?» — LOCK 6: curioso, no alarmado.

  A · electrónica y seca      dos notas que suben, onda cuadrada, sin portamento,
                              decaimiento instantáneo. Un fragmento de módem
  B · algo vocal, no humana   pulso pasado por dos formantes (la «e» abierta)
                              con el tono subiendo, y un poco de bitcrush para
                              que nadie la confunda con una garganta
  C · curiosidad mínima       un solo blip suave que sube una quinta y se
                              detiene. 0,22 s de sonido. Casi nada
  D · micro glitch            tres granos de un mismo tono, el último más
                              agudo: la pregunta como sample corrupto
  E · la propuesta            LA VOZ ES EL VISOR. Una ráfaga de ticks
                              diminutos —los píxeles de la matriz
                              reescribiéndose— que se resuelve en un chirp de
                              dos tonos que sube y cae apenas. Sólo G puede
                              sonar así, porque sólo G tiene esa cara
"""
import wave
from pathlib import Path

import numpy as np
from scipy.signal import lfilter

SR = 48_000
DUR = 0.42
N = int(DUR * SR)
T = np.arange(N) / SR
RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "public/assets/gcl/voz"
_rng = np.random.default_rng(6)


def lp(x, corte, orden=2):
    a = np.exp(-2 * np.pi * corte / SR)
    for _ in range(orden):
        x = lfilter([1 - a], [1, -a], x)
    return x


def bp(x, f0, q=6.0):
    """Resonador de dos polos: un formante."""
    w = 2 * np.pi * f0 / SR
    r = 1 - w / (2 * q)
    return lfilter([1 - r], [1, -2 * r * np.cos(w), r * r], x)


def borde(x, ataque=0.004, caida=0.03):
    n = len(x)
    t = np.arange(n) / SR
    d = n / SR
    return x * np.clip(t / ataque, 0, 1) * np.clip((d - t) / caida, 0, 1)


def fase(freq):
    return 2 * np.pi * np.cumsum(freq) / SR


def norm(x, pico=0.36):
    m = np.max(np.abs(x)) or 1
    return x / m * pico


# ── A · electrónica y seca ───────────────────────────────────────────────────
def voz_A():
    v = np.zeros(N)
    for (t0, t1, f) in ((0.00, 0.11, 640), (0.15, 0.30, 905)):
        i, j = int(t0 * SR), int(t1 * SR)
        tt = np.arange(j - i) / SR
        s = np.sign(np.sin(2 * np.pi * f * tt)) * 0.6 + np.sin(2 * np.pi * f * 2 * tt) * 0.15
        v[i:j] = borde(lp(s, 3200, 1), 0.002, 0.012)
    return norm(v)


# ── B · algo vocal, no humana ────────────────────────────────────────────────
def voz_B():
    f0 = np.where(T < 0.26, 172 + 70 * (T / 0.26), 242 - 60 * ((T - 0.26) / 0.16))
    pulso = (np.sin(fase(f0)) > 0.92).astype(float)                # tren de pulsos: la glotis
    v = bp(pulso, 640, 5) * 1.0 + bp(pulso, 1750, 7) * 0.55 + bp(pulso, 2600, 8) * 0.2
    v = np.round(v * 24) / 24                                        # bitcrush: no es una garganta
    v = lp(v, 3800, 1)
    amp = np.where(T < 0.30, 1.0, 0.75)
    return norm(borde(v * amp, 0.012, 0.05))


# ── C · curiosidad mínima ────────────────────────────────────────────────────
def voz_C():
    n = int(0.22 * SR)
    tt = np.arange(n) / SR
    f = 520 * 2 ** (np.clip(tt / 0.16, 0, 1) * (7 / 12))            # sube una quinta y se detiene
    s = np.sin(fase(f)) * 0.8 + np.sin(fase(f) * 2) * 0.12
    v = np.zeros(N); v[:n] = borde(s, 0.010, 0.05)
    return norm(v, 0.30)


# ── D · micro glitch interrogativo ───────────────────────────────────────────
def voz_D():
    v = np.zeros(N)
    for k, (t0, d, f) in enumerate(((0.00, 0.045, 700), (0.075, 0.045, 700), (0.16, 0.14, 990))):
        i = int(t0 * SR); n = int(d * SR)
        tt = np.arange(n) / SR
        s = np.sign(np.sin(2 * np.pi * f * tt)) * 0.5 + np.sin(2 * np.pi * f * tt) * 0.5
        s = np.round(s * 6) / 6                                       # el sample corrupto
        s = lp(s, 3000, 1)
        v[i:i + n] = borde(s, 0.001, 0.008 if k < 2 else 0.05)
    return norm(v)


# ── E · la voz es el visor ───────────────────────────────────────────────────
def voz_E():
    v = np.zeros(N)
    # 1 · los píxeles: 9 ticks diminutos, cada uno un poco más agudo, en 0,14 s
    for k in range(9):
        i = int(k * 0.0155 * SR); n = int(0.006 * SR)
        tt = np.arange(n) / SR
        f = 1900 + k * 160
        v[i:i + n] += np.sin(2 * np.pi * f * tt) * borde(np.ones(n), 0.0004, 0.003) * (0.5 + k * 0.05)
    # 2 · el chirp: dos tonos que suben y caen apenas — la pregunta
    i = int(0.15 * SR); n = N - i
    tt = np.arange(n) / SR
    f = np.where(tt < 0.10, 470 + 190 * (tt / 0.10), np.where(tt < 0.17, 660, 660 - 110 * ((tt - 0.17) / 0.10)))
    s = np.sin(fase(f)) * 0.7 + np.sign(np.sin(fase(f))) * 0.18 + np.sin(fase(f) * 1.5) * 0.12
    s = lp(s, 2600, 2)
    v[i:] += borde(s, 0.006, 0.06)
    return norm(v)


# ── LA MICRO-RONDA SOBRE LA D (05-09 · Valeria eligió la 4 como dirección) ───
# «G no está diciendo eh? deliberadamente. Su sistema acaba de emitir un sonido
# que nosotros entendemos como eh?». Tres variaciones mínimas, misma identidad.
def _granos(granos, crush=6, mezcla_seno=0.5, lp_hz=3000, caida_final=0.05):
    v = np.zeros(N)
    for k, (t0, d, f0, f1) in enumerate(granos):
        i = int(t0 * SR); n = int(d * SR); tt = np.arange(n) / SR
        f = f0 + (f1 - f0) * (tt / d)                                # f0 → f1 dentro del grano
        ph = fase(f)
        s = np.sign(np.sin(ph)) * (1 - mezcla_seno) + np.sin(ph) * mezcla_seno
        s = np.round(s * crush) / crush
        s = lp(s, lp_hz, 1)
        ultimo = k == len(granos) - 1
        v[i:i + n] = borde(s, 0.001, caida_final if ultimo else 0.008)
    return norm(v)


def voz_4A():
    """Prácticamente idéntica, 10–15 % más corta y más seca: los granos más
    juntos, el último más corto y con la cola cortada. Menos filtro: más crujido."""
    return _granos(((0.00, 0.040, 700, 700), (0.065, 0.040, 700, 700), (0.135, 0.120, 990, 990)),
                   crush=6, mezcla_seno=0.5, lp_hz=3400, caida_final=0.028)


def voz_4B():
    """Misma identidad, un poco menos humana: más bitcrush (4 niveles), sin seno
    —onda cuadrada pura—, y los dos primeros granos apenas desafinados entre sí,
    como si el sistema no los generara idénticos."""
    return _granos(((0.00, 0.045, 700, 700), (0.075, 0.045, 716, 716), (0.16, 0.14, 990, 990)),
                   crush=4, mezcla_seno=0.0, lp_hz=3600, caida_final=0.05)


def voz_4C():
    """Misma identidad, con la interrogación un poco más perceptible: el último
    grano ya no es plano, SUBE de 900 a 1180 Hz dentro de sí mismo, y dura un
    poco más. Lo demás no cambia."""
    return _granos(((0.00, 0.045, 700, 700), (0.075, 0.045, 700, 700), (0.16, 0.165, 900, 1180)),
                   crush=6, mezcla_seno=0.5, lp_hz=3000, caida_final=0.05)


def voz_mm():
    """«mm.» — el otro sonido de G. Misma familia que la 4: un solo grano,
    más grave (580 Hz), plano, sin subida. Es registrar, no preguntar. 0,2 s."""
    return _granos(((0.00, 0.20, 580, 580),), crush=6, mezcla_seno=0.5, lp_hz=2600, caida_final=0.07)


VOCES = {"mm": voz_mm, "A": voz_A, "B": voz_B, "C": voz_C, "D": voz_D, "E": voz_E,
         "4A": voz_4A, "4B": voz_4B, "4C": voz_4C}


def escribe(ruta, x):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(np.stack([x, x], 1), -1, 1) * 32767).astype("<i2").tobytes())


if __name__ == "__main__":
    todas, ronda = [], []
    for k, fn in VOCES.items():
        x = fn()
        escribe(OUT / f"G_eh_{k}.wav", x)
        (ronda if k.startswith("4") else todas).extend([x, np.zeros(SR)])
        print(f"  ✓ G_eh_{k}.wav  {len(x)/SR:.2f} s  pico {np.max(np.abs(x)):.2f}")
    escribe(OUT / "G_eh_5_alternativas.wav", np.concatenate(todas))
    escribe(OUT / "G_eh_ronda4_ABC.wav", np.concatenate([VOCES["D"](), np.zeros(SR)] + ronda))
    print("  ✓ G_eh_5_alternativas.wav · G_eh_ronda4_ABC.wav (la 4 base, y después 4A · 4B · 4C)")

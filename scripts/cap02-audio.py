#!/usr/bin/env python3
"""CAP. 02 «REVISIÓN 7» — la pista de trabajo y los SFX, sintetizados.

    /Users/Vale/copylab-venv/bin/python3 scripts/cap02-audio.py

POR QUÉ EXISTE. El montaje del capítulo está clavado a una rejilla de **112,5 BPM
a 30 fps**, que da beat = 16 frames exactos. Un tema descargado nunca cae ahí solo,
y para el ROUGH CUT no hace falta que caiga: hace falta comprobar si el episodio
entretiene. Así que la pista se **sintetiza sobre la rejilla**, y todos los golpes
caen en el frame que dice `_timeline.json` porque se calculan desde el frame.

v3 · 04-09-2026 — el capítulo pasó de 584 a **776 frames**. La escalada creció a
256 frames, que son **4 compases exactos**, así que el drop sigue cayendo en el
downbeat del f.464 y no hubo que recronometrar nada del colapso.

⚠️ ESTO ES UNA PISTA DE TRABAJO, NO LA MÚSICA DEL CAPÍTULO. La decisión v4 fue
que la serie NO tiene identidad musical fija (sólo el boot de G). Esta pista
cumple las cuatro condiciones de portabilidad de `07_MONTAJE.md §5` — downbeat
limpio en el f.80, 16avos libres desde el compás 3, golpe anclable en el f.272 y
corte a muestra cero en el f.136 y el f.432 — para que cambiarla sea cambiar un
archivo, no rehacer el montaje.

Los dos sonidos que SÍ son de la serie y no de la pista: el **boot del visor** y
el **PING**. El ping es el mismo sample en el f.136 y en el f.568 — es lo que
cierra el episodio en loop.
"""
import sys
import wave
from pathlib import Path

import numpy as np

SR = 48_000
FPS = 30
FRAMES = 776
BPM = 112.5
BEAT_F = 16                      # 60/112,5 = 0,5333 s = 16 frames exactos
DUR = FRAMES / FPS + 0.5         # medio segundo de cola de seguridad

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "public/assets/gcl/cap02/audio_rough.wav"

pista = np.zeros(int(DUR * SR), dtype=np.float64)


def f2s(f):
    return f / FPS


def poner(sonido, frame, gain=1.0):
    """Mete un sonido en la pista en un frame exacto. Suma, no reemplaza."""
    i = int(round(f2s(frame) * SR))
    n = min(len(sonido), len(pista) - i)
    if n > 0:
        pista[i:i + n] += sonido[:n] * gain


def env(n, ataque=0.002, caida=None, curva=3.0):
    """Envolvente percusiva: ataque casi instantáneo, caída exponencial."""
    caida = caida if caida is not None else n / SR
    t = np.arange(n) / SR
    a = np.clip(t / max(ataque, 1e-6), 0, 1)
    d = np.exp(-curva * t / caida)
    return a * d


def ruido(n):
    return np.random.default_rng(7).standard_normal(n) if n < 0 else None


_rng = np.random.default_rng(20260904)


def n_ruido(n):
    return _rng.standard_normal(n)


def paso_bajo(x, corte, orden=2):
    """Un polo IIR sencillo, repetido. No es Butterworth y no hace falta."""
    a = np.exp(-2 * np.pi * corte / SR)
    y = x.copy()
    for _ in range(orden):
        out = np.empty_like(y)
        z = 0.0
        for i in range(len(y)):
            z = (1 - a) * y[i] + a * z
            out[i] = z
        y = out
    return y


def paso_bajo_rapido(x, corte, orden=2):
    """Versión vectorizada con lfilter — el bucle de arriba tarda demasiado."""
    from scipy.signal import lfilter
    a = np.exp(-2 * np.pi * corte / SR)
    y = x
    for _ in range(orden):
        y = lfilter([1 - a], [1, -a], y)
    return y


try:
    from scipy.signal import lfilter  # noqa: F401
    lp = paso_bajo_rapido
except ImportError:                    # sin scipy, filtro FIR por convolución
    def lp(x, corte, orden=2):
        k = max(2, int(SR / max(corte, 20)))
        nucleo = np.hanning(k)
        nucleo /= nucleo.sum()
        y = x
        for _ in range(orden):
            y = np.convolve(y, nucleo, mode="same")
        return y


def hp(x, corte):
    return x - lp(x, corte, 1)


# ─────────────────────────────────────────────────────────────────────────────
# LOS SONIDOS
# ─────────────────────────────────────────────────────────────────────────────

def kick(dur=0.13):
    n = int(dur * SR)
    t = np.arange(n) / SR
    barrido = 110 * np.exp(-28 * t) + 44
    cuerpo = np.sin(2 * np.pi * np.cumsum(barrido) / SR) * env(n, 0.0006, dur, 5)
    click = n_ruido(n) * env(n, 0.0002, 0.004, 9) * 0.30
    return np.tanh((cuerpo + click) * 1.5) * 0.9


def clap(dur=0.20):
    n = int(dur * SR)
    cuerpo = hp(n_ruido(n), 1400) * env(n, 0.001, dur, 6)
    # tres micro-golpes = suena a palmas, no a ruido
    for d in (0.010, 0.021, 0.033):
        i = int(d * SR)
        cuerpo[i:] += hp(n_ruido(n - i), 1800) * env(n - i, 0.0005, 0.05, 9) * 0.6
    return cuerpo * 0.42


def hat(dur=0.045, abierto=False):
    d = 0.13 if abierto else dur
    n = int(d * SR)
    return hp(n_ruido(n), 7000) * env(n, 0.0003, d, 7) * (0.16 if abierto else 0.13)


def bajo(nota_hz, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    # diente de sierra suavizado + sub — el bajo funky vive en el filtro
    saw = 2 * (t * nota_hz - np.floor(0.5 + t * nota_hz))
    sub = np.sin(2 * np.pi * nota_hz * t)
    corte = 300 + 900 * np.exp(-9 * t)          # envolvente de filtro
    v = lp(saw * 0.55 + sub * 0.75, float(np.mean(corte)), 2)
    return v * env(n, 0.004, dur, 2.6) * 0.34


def ping(dur=0.55):
    """El ancla de la serie. Mismo sample en el f.136 y en el f.568."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = (np.sin(2 * np.pi * 1568 * t) * 0.6 +
         np.sin(2 * np.pi * 2349 * t) * 0.35 +
         np.sin(2 * np.pi * 3136 * t) * 0.14)
    return v * env(n, 0.0008, dur, 5.5) * 0.34


def sub_creciente(dur):
    """EL HUECO del CUT 04: no hay música, hay un sub que crece."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = np.sin(2 * np.pi * 41 * t) + 0.3 * np.sin(2 * np.pi * 82 * t)
    return v * (t / dur) ** 2 * 0.55


def boom(dur=0.55):
    n = int(dur * SR)
    t = np.arange(n) / SR
    barrido = 90 * np.exp(-11 * t) + 36
    v = np.sin(2 * np.pi * np.cumsum(barrido) / SR) * env(n, 0.0008, dur, 3.4)
    v += lp(n_ruido(n), 500) * env(n, 0.0005, 0.09, 8) * 0.45
    return np.tanh(v * 1.7) * 0.95


def click_mouse(dur=0.035):
    n = int(dur * SR)
    return hp(n_ruido(n), 2200) * env(n, 0.0002, 0.010, 12) * 0.30


def whoosh(dur=0.42):
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = n_ruido(n) * np.sin(np.pi * t / dur) ** 2
    return hp(lp(v, 4000, 1), 400) * 0.20


def thunk(dur=0.22, hz=150):
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = np.sin(2 * np.pi * hz * np.exp(-6 * t) * t) * env(n, 0.001, dur, 6)
    v += lp(n_ruido(n), 900) * env(n, 0.0004, 0.04, 9) * 0.5
    return v * 0.34


def ceramica(dur=0.20):
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = np.sin(2 * np.pi * 2600 * t) * 0.5 + np.sin(2 * np.pi * 4100 * t) * 0.3
    return v * env(n, 0.0004, 0.06, 10) * 0.16


def ruedas(dur=0.40):
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = lp(n_ruido(n), 700, 2) * np.sin(np.pi * t / dur)
    return v * 0.26


def zumbido(dur, hz=118, gain=0.012):
    """Zumbido de monitor. −38 dB: se siente, no se escucha."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = np.sin(2 * np.pi * hz * t) + 0.4 * np.sin(2 * np.pi * hz * 2 * t)
    v += lp(n_ruido(n), 2000) * 0.5
    borde = np.clip(np.minimum(t, dur - t) / 0.08, 0, 1)
    return v * borde * gain


def boot_visor(dur=0.53):
    """LA FIRMA DE LA SERIE. Fuera de tempo por definición: es lo único que no
    pertenece al capítulo sino a G. Zumbido eléctrico que sube + tick al encajar."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    sube = 60 * np.exp(3.1 * t / dur)                    # 60 → ~1300 Hz
    v = np.sin(2 * np.pi * np.cumsum(sube) / SR) * 0.30
    v += np.sin(2 * np.pi * np.cumsum(sube * 1.5) / SR) * 0.12
    v *= np.clip(t / 0.06, 0, 1) * np.clip((dur - t) / 0.10, 0, 1)
    v += lp(n_ruido(n), 1200) * (t / dur) ** 3 * 0.10    # arranque eléctrico
    tick = int(0.455 * SR)                               # el TICK de encaje
    k = int(0.05 * SR)
    v[tick:tick + k] += hp(n_ruido(k), 3000) * env(k, 0.0002, 0.012, 11) * 0.55
    v[tick:tick + k] += np.sin(2 * np.pi * 900 * np.arange(k) / SR) * env(k, 0.0004, 0.03, 8) * 0.35
    return v * 0.85


def muerte_electrica(dur=0.45):
    n = int(dur * SR)
    t = np.arange(n) / SR
    baja = 700 * np.exp(-7 * t) + 45
    v = np.sin(2 * np.pi * np.cumsum(baja) / SR) * env(n, 0.001, dur, 4)
    return v * 0.22


def tick_visor(dur=0.06):
    n = int(dur * SR)
    return hp(n_ruido(n), 4000) * env(n, 0.0002, 0.012, 12) * 0.13


def nota_sostenida(dur, hz=98):
    """CUT 07 · una sola nota a −24 dB. Nada más."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = (np.sin(2 * np.pi * hz * t) * 0.6 + np.sin(2 * np.pi * hz * 2 * t) * 0.22 +
         np.sin(2 * np.pi * hz * 3 * t) * 0.08)
    borde = np.clip(t / 0.25, 0, 1) * np.clip((dur - t) / 0.6, 0, 1)
    return v * borde * 0.055


def lapiz(dur=0.75):
    """El remate lo escribe una mano de verdad: tacha el 7 y escribe el 1."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    grano = hp(n_ruido(n), 1800)
    # dos gestos: el tachón (rápido) y el trazo del 1 (más corto)
    g1 = np.exp(-((t - 0.10) / 0.075) ** 2)
    g2 = np.exp(-((t - 0.44) / 0.055) ** 2)
    return grano * (g1 + g2 * 0.8) * 0.11


# ─────────────────────────────────────────────────────────────────────────────
# EL MONTAJE SONORO — cada golpe en el frame que dice _timeline.json
# ─────────────────────────────────────────────────────────────────────────────

# ── OPENING · f.0–15 · FUERA DE TEMPO ────────────────────────────────────────
poner(boot_visor(), 0)

# ── HISTORIAL · f.16–79 · el gancho. Todavía sin música ──────────────────────
# Un tick seco por cada versión que aparece. Es sonido de interfaz, no de
# arreglo: la música todavía no entra y el silencio de acá hace que el beat del
# f.144 pegue más fuerte.
poner(zumbido(f2s(64), gain=0.010), 16)
for k in range(7):
    poner(tick_visor(0.05) * 1.1, 22 + k * 6)
poner(click_mouse() * 0.7, 66)            # se posa sobre la séptima

# ── CUT 01 · f.80–143 · SILENCIO. Sólo el mouse ──────────────────────────────
poner(ruedas(0.25) * 0.35, 96)            # el mouse deslizando
poner(click_mouse(), 128)                 # EL CLICK
poner(whoosh(), 134)                      # el archivo se va

# ── CUT 02 · f.144–207 · ENTRA EL BEAT en el downbeat ────────────────────────
# La música muere a MUESTRA CERO en el f.200, cuando la cabeza baja hacia el
# teléfono. Por eso el compás se escribe con `hasta=200` y no un frame más.
NOTAS = [55.0, 55.0, 82.41, 55.0, 73.42, 55.0, 65.41, 61.74]   # A1 · E2 · D2 · C2 · B1


def compas(inicio, indice, hasta=None, gain=1.0, filtrado=False):
    """Un compás de 4/4 = 64 frames. 16 frames por beat, 4 por 16avo."""
    hasta = hasta if hasta is not None else inicio + 64
    g = gain * (0.45 if filtrado else 1.0)
    for b in range(4):                                   # los 4 beats
        f = inicio + b * BEAT_F
        if f < hasta:
            if b in (0, 2):
                poner(kick(), f, g)
            else:
                poner(clap(), f, g * 0.9)
        for s16 in range(4):                             # los 16avos
            f = inicio + b * BEAT_F + s16 * 4
            if f < hasta and not (b in (1, 3) and s16 == 0):
                poner(hat(abierto=(s16 == 2)), f, g * (0.55 if s16 % 2 else 1.0))
    for i, nz in enumerate(NOTAS):                       # el bajo, un 8avo por nota
        f = inicio + i * 8
        if f < hasta:
            poner(bajo(nz, 8 / FPS * 0.92), f, g)


compas(144, 3, hasta=200)
poner(ping(), 200)                        # EL PING. Ancla de la serie

# ── LA ESCALADA · f.208–431 · los pings SON la percusión ─────────────────────
# Los mensajes están en `MENSAJES` de Cap02Revision7.tsx y cada uno trae su ping.
# La forma de la rampa es el chiste: los primeros tienen aire para leerse, los
# últimos caen encima. El beat vuelve contaminado recién en el compás 6.
poner(zumbido(f2s(52), gain=0.008), 208)          # ambiente a −44 dB
MENSAJES = [210, 262, 302, 336, 366, 388, 404, 416, 426]
compas(336, 6, hasta=400, filtrado=True)          # el beat vuelve por debajo
compas(400, 7, hasta=432, filtrado=True)
for i, f in enumerate(MENSAJES):
    # el ping se acorta y se aprieta a medida que la cosa se descontrola
    poner(ping(max(0.20, 0.55 - i * 0.045)), f, 0.85 + i * 0.02)

# ── EL HUECO · f.432–463 · todo se detiene y llega la sentencia ──────────────
poner(sub_creciente(f2s(32)), 432)
poner(ping(0.40), 434, 1.0)                       # «¿Podemos volver a la primera?»

# ── TÍTULO · f.464 · EL DROP, exacto en el downbeat ──────────────────────────
poner(boom(), 464)
for i in (464, 528, 592):                         # compases 8, 9 y 10
    compas(i, 8, hasta=min(i + 64, 624), gain=1.05)
# el bajo al frente durante el rewind
for f in range(496, 624, 8):
    poner(bajo(NOTAS[((f - 496) // 8) % len(NOTAS)] * 0.5, 8 / FPS * 0.95), f, 0.5)
# el contador 07→01 tictaqueando cada 8 frames
for f in range(504, 560, 8):
    poner(tick_visor(0.04) * 1.6, f)
poner(thunk(0.26, 120), 576, 0.9)                 # el impacto en la silla
poner(whoosh(0.30), 608, 0.7)                     # el archivo se abre

# ── CUT 06 · f.624–671 · SILENCIO ABSOLUTO ───────────────────────────────────
poner(zumbido(f2s(48)), 624)
poner(tick_visor(), 652)
poner(muerte_electrica(), 664)

# ── CUT 07 · f.672–751 · una nota, y el lápiz ────────────────────────────────
poner(nota_sostenida(f2s(80)), 672)
# El tachón se dibuja en el f.710 y el 1 en el f.722. El sample arranca 3 frames
# antes porque el lápiz suena cuando toca el papel, no cuando termina el trazo.
poner(lapiz(), 707)

# ── CUT 09 · f.752–775 · el mismo PING del f.200. Cierra en loop ─────────────
poner(ping(), 760)

# ─────────────────────────────────────────────────────────────────────────────
pico = float(np.max(np.abs(pista)))
pista = np.tanh(pista / max(pico, 1e-9) * 0.92) * 0.95
estereo = np.stack([pista, pista], axis=1)
SALIDA.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(SALIDA), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((np.clip(estereo, -1, 1) * 32767).astype("<i2").tobytes())
print(f"✓ {SALIDA.relative_to(RAIZ)}  ·  {DUR:.2f} s  ·  pico previo {pico:.2f}")
print(f"  rejilla {BPM} BPM · beat {BEAT_F} frames · {FRAMES} frames = {FRAMES/FPS:.2f} s")

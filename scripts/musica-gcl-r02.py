#!/usr/bin/env python3
"""
R02 «Turno de noche» — banda sonora del EPISODIO, 40 s. **v4.**

LA REGLA NUEVA DE ESTE CAPÍTULO: **si algo pasa en pantalla, suena.**
El feedback fue textual — «tiene que haber un golpe de sonido cada vez que pase
algo». Así que la partitura ya no es una cama con tres acentos: son **15 golpes
puestos al frame** sobre una cama que se aparta para dejarlos sonar.

MISMA FAMILIA QUE EL R01 — mismo taller de síntesis, rejilla de 120 BPM, y las
cuatro reglas duras de la mezcla:
  1. Nunca ruido blanco continuo en la cama (los golpes son ráfagas cortas).
  2. Nada de ducking por envolvente de voz: hueco de ecualización FIJO 300–3500 Hz.
  3. Dinámica por arreglo, en el compás, nunca en la sílaba.
  4. El peso grave va en 110 Hz, no en 55: un tono sostenido de 55 Hz zumba.

LOS 15 ACENTOS
   2,0  clac del interruptor
   3,5  golpe grave: la sala queda apagada
   6,0  RASGADO de la grieta + chispas
   7,5  swell: el portal se abre
   9,5  whoosh del salto + impacto del aterrizaje
  11,5  tintineo del guiño
  13,5  crack del chasquido + arranca la percusión
  15,0  dato 1 aterriza
  18,0  dato 2 aterriza
  19,0  EL HALLAZGO: acorde ascendente + campana
  20,5  boing del saltito
  22,0  braam coral de la alerta
  23,5  tick de la corrección (dos notas que resuelven)
  25,5  máquina de escribir del resumen
  27,0  el respiro (−10 dB, medio segundo)
  30,0  llega el equipo: la música se abre
  32,55 ¡PLAF! el choque de manos — el golpe más humano del reel. Va sobre el
        instante del contacto (medido en el clip), no sobre el corte del plano.
  35,0  el cierre resuelve

Salida: public/assets/gcl/r02/music_r02.mp3
"""
import wave, os
import numpy as np

SR = 44100
DUR = 40.0
N = int(SR * DUR)
t = np.arange(N) / SR

BPM = 120.0
BEAT = 60.0 / BPM        # 0,5 s
BAR = BEAT * 4           # 2,0 s

OUT_WAV = "/tmp/music_r02.wav"

# ---------------- utilidades ----------------
def suave(x0, x1):
    u = np.clip((t - x0) / max(1e-6, x1 - x0), 0, 1)
    return u * u * (3 - 2 * u)

def ventana(a, b, fi=1.0, fo=1.0):
    return suave(a, a + fi) * (1 - suave(b - fo, b))

def _filtro(x, curva):
    n = 1 << int(np.ceil(np.log2(len(x) + 1)))
    X = np.fft.rfft(x, n)
    f = np.fft.rfftfreq(n, 1 / SR)
    return np.fft.irfft(X * curva(f), n)[:len(x)]

def lp(x, fc, orden=2):
    return _filtro(x, lambda f: 1.0 / (1 + (f / fc) ** orden))

def hp(x, fc, orden=2):
    return _filtro(x, lambda f: ((f / fc) ** orden) / (1 + (f / fc) ** orden))

def banda(x, f1, f2):
    return lp(hp(x, f1), f2)

def reverb(x, decay=2.2, mezcla=0.30, pre=0.018):
    L = int(decay * SR)
    rng = np.random.default_rng(7)
    ir = rng.standard_normal(L) * np.exp(-np.linspace(0, 6.0, L))
    ir[: int(pre * SR)] = 0
    ir /= np.abs(ir).sum() / 8
    n = 1 << int(np.ceil(np.log2(len(x) + L)))
    y = np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(ir, n), n)[: len(x)]
    return (1 - mezcla) * x + mezcla * y

# ---------------- notas ----------------
def nota(n):
    """MIDI -> Hz. 69 = La4 = 440."""
    return 440.0 * 2 ** ((n - 69) / 12.0)

A1, A2, A3, A4 = nota(33), nota(45), nota(57), nota(69)
C2, C3, C4, C5 = nota(36), nota(48), nota(60), nota(72)
E2, E3, E4 = nota(40), nota(52), nota(64)
F2, F3, F4 = nota(41), nota(53), nota(65)
G2, G3, G4 = nota(43), nota(55), nota(67)
D3, D4 = nota(50), nota(62)
Bb2, Bb3 = nota(46), nota(58)

ACORDES = {
    "Am":  [A2, C4, E4, A4],
    "F":   [F2, A3, C4, F4],
    "C":   [C3, E4, G4, C5],
    "G":   [G2, D4, G4, nota(71)],
    "Dm":  [D3, F3, A3, D4],
    "Bb":  [Bb2, D4, F4, Bb3 * 2],
}

# ---------------- generadores ----------------
def saw_seg(f, L, nh=16, detune=0.0):
    tt = np.arange(L) / SR
    y = np.zeros(L)
    for k in range(1, nh + 1):
        fk = f * k * (1 + detune)
        if fk > 15000:
            break
        y += np.sin(2 * np.pi * fk * tt + k * 0.7) / k
    return y / np.log(nh + 1)

def pad(secciones, gan=1.0, fc=1400, ataque=0.9, cola=1.4, nh=14, oct_baja=True):
    """secciones: [(t0, t1, 'Am'), ...] — pad de sierras apiladas y desafinadas."""
    y = np.zeros(N)
    for (a, b, nom) in secciones:
        i0, i1 = int(a * SR), int(min(b + cola, DUR) * SR)
        L = i1 - i0
        if L <= 0:
            continue
        s = np.zeros(L)
        for j, f in enumerate(ACORDES[nom]):
            s += saw_seg(f, L, nh, +0.0018 * (j % 2 * 2 - 1)) * (0.9 if j == 0 else 0.55)
            s += saw_seg(f, L, nh, -0.0021 * (j % 2 * 2 - 1)) * (0.6 if j == 0 else 0.35)
        if oct_baja:
            # la octava baja del pad caía en el mismo 55 Hz del sub y sumaba al
            # zumbido: se baja y se le quitan armónicos
            s += saw_seg(ACORDES[nom][0] / 2, L, 4) * 0.07
        env = np.ones(L)
        na = int(min(ataque, (b - a) * 0.5) * SR)
        env[:na] = np.linspace(0, 1, na) ** 1.6
        nd = int(min(cola, (b - a)) * SR)
        env[-nd:] *= np.linspace(1, 0, nd) ** 1.4
        y[i0:i1] += s * env
    return lp(y, fc) * gan

def cuerdas(secciones, gan=1.0, fc=3000):
    """Cuerdas: sierras con vibrato lento y ataque largo. Registro medio-alto."""
    y = np.zeros(N)
    for (a, b, nom) in secciones:
        i0, i1 = int(a * SR), int(min(b + 1.6, DUR) * SR)
        L = i1 - i0
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        s = np.zeros(L)
        for f in ACORDES[nom][1:]:
            vib = 1 + 0.0035 * np.sin(2 * np.pi * 4.6 * tt + f)
            for k in range(1, 12):
                if f * k > 12000:
                    break
                s += np.sin(2 * np.pi * f * k * vib * tt + k) / (k ** 1.25)
        env = np.ones(L)
        na = int(min(1.3, (b - a) * 0.6) * SR)
        env[:na] = np.linspace(0, 1, na) ** 2
        nd = int(min(1.6, (b - a)) * SR)
        env[-nd:] *= np.linspace(1, 0, nd) ** 1.5
        y[i0:i1] += s * env * 0.08
    return lp(y, fc) * gan

def braam(t0, nom, dur=2.4, gan=0.5):
    """Metal grave de cine: sierras apiladas, ataque de 120 ms, mucho grave."""
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(dur * SR), N - i0)
    if L <= 0:
        return y
    tt = np.arange(L) / SR
    s = np.zeros(L)
    raiz = ACORDES[nom][0]
    for f, g in [(raiz / 2, 1.0), (raiz, 0.9), (raiz * 1.5, 0.45), (raiz * 2, 0.4)]:
        for d in (-0.004, 0.0, 0.004):
            s += saw_seg(f * (1 + d), L, 20) * g
    env = np.minimum(1.0, tt / 0.12) * np.exp(-tt * 1.15)
    y[i0:i0 + L] = lp(s, 900, 3) * env * gan * 0.06
    return y

def sub(t0, t1, f=A1, gan=0.3, fi=1.5, fo=2.0):
    """Peso grave. OJO: la v3 usaba DOS senos desafinados (f y f*1.004). Los dos
    batían entre sí y producían un zumbido continuo — medido en el render:
    +29 dB sobre el fondo espectral y presente en el 70% del reel. Feedback
    textual de Valeria: «una especie de zumbido en el audio muy molesto».
    Ahora es UN solo seno, más bajo, y con una respiración de un compás para que
    sea peso y no un tono sostenido."""
    # SEGUNDA CORRECCIÓN DEL ZUMBIDO (20-08): bajar el nivel no bastó — un tono
    # sostenido de 55 Hz zumba a cualquier volumen. El peso grave sube UNA
    # OCTAVA (110 Hz en vez de 55): se escucha en teléfono, sostiene igual y
    # deja de ser un dron. Los 55 Hz quedan solo en los impactos, que son
    # transitorios y no alcanzan a leerse como zumbido.
    e = ventana(t0, t1, fi, fo)
    respira = 0.66 + 0.34 * (0.5 - 0.5 * np.cos(2 * np.pi * t / (BAR * 2)))
    cuerpo = np.sin(2 * np.pi * f * t) + 0.22 * np.sin(2 * np.pi * f * 2 * t + 0.9)
    return cuerpo * e * respira * gan

def piano(eventos, gan=0.09, dec=4.0):
    """Pluck tipo piano/celesta: parciales con decaimiento exponencial."""
    y = np.zeros(N)
    for (tt0, f) in eventos:
        i0 = int(tt0 * SR); L = min(int(dec * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        s = np.zeros(L)
        for k, g in [(1, 1.0), (2, 0.42), (3, 0.20), (4, 0.11), (6, 0.05)]:
            s += np.sin(2 * np.pi * f * k * tt) * g * np.exp(-tt * (2.0 + k * 0.55))
        s *= np.minimum(1.0, tt / 0.004)
        y[i0:i0 + L] += s
    return y * gan

def bombo(tiempos, gan=0.5):
    y = np.zeros(N)
    rng = np.random.default_rng(5)
    for tt0 in tiempos:
        i0 = int(tt0 * SR); L = min(int(0.55 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        f = 48 * np.exp(-tt * 26) + 41
        ph = 2 * np.pi * np.cumsum(f) / SR
        s = np.sin(ph) * np.exp(-tt * 7.5)
        clic = lp(rng.standard_normal(L) * np.exp(-tt * 190), 3600) * 0.30
        y[i0:i0 + L] += (s + clic) * gan
    return y

def taiko(tiempos, gan=0.34):
    y = np.zeros(N)
    rng = np.random.default_rng(23)
    for tt0, g in tiempos:
        i0 = int(tt0 * SR); L = min(int(0.9 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        f = 130 * np.exp(-tt * 13) + 74
        ph = 2 * np.pi * np.cumsum(f) / SR
        cuerpo = np.sin(ph) * np.exp(-tt * 5.2)
        parche = banda(rng.standard_normal(L) * np.exp(-tt * 30), 180, 1800) * 0.5
        y[i0:i0 + L] += (cuerpo + parche) * gan * g
    return y

def hats(tiempos, gan=0.05):
    y = np.zeros(N)
    rng = np.random.default_rng(31)
    for tt0, g in tiempos:
        i0 = int(tt0 * SR); L = min(int(0.10 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        y[i0:i0 + L] += hp(rng.standard_normal(L) * np.exp(-tt * 95), 7500) * gan * g
    return y

def ostinato(t0, t1, notas, gan=0.11, paso=None, fc=4200):
    """Semicorcheas plucked — el motor rítmico melódico."""
    paso = paso or BEAT / 4
    y = np.zeros(N)
    i = 0
    tt0 = t0
    while tt0 < t1:
        f = notas[i % len(notas)]
        i0 = int(tt0 * SR); L = min(int(0.42 * SR), N - i0)
        if L > 0:
            tt = np.arange(L) / SR
            s = (np.sin(2 * np.pi * f * tt)
                 + 0.5 * np.sin(2 * np.pi * f * 2 * tt)
                 + 0.22 * np.sin(2 * np.pi * f * 3 * tt))
            acento = 1.0 if i % 4 == 0 else 0.55
            y[i0:i0 + L] += s * np.exp(-tt * 11) * acento
        tt0 += paso
        i += 1
    return lp(y, fc) * gan

def riser(t_fin, dur=2.0, gan=0.30):
    """Carga: ruido filtrado que abre + tono que sube. Solo antes del impacto."""
    y = np.zeros(N)
    i1 = int(t_fin * SR); i0 = max(0, i1 - int(dur * SR))
    L = i1 - i0
    rng = np.random.default_rng(19)
    u = np.linspace(0, 1, L)
    n = rng.standard_normal(L)
    barrido = lp(n, 500) * (1 - u) + lp(n, 6500) * u
    tt = np.arange(L) / SR
    f = 180 * np.exp(u * 2.0)
    tono = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.5
    y[i0:i1] = (barrido + tono) * (u ** 1.9) * gan
    return y

def platillo_invertido(t_fin, dur=1.8, gan=0.16):
    y = np.zeros(N)
    i1 = int(t_fin * SR); i0 = max(0, i1 - int(dur * SR))
    L = i1 - i0
    rng = np.random.default_rng(41)
    s = hp(rng.standard_normal(L), 4200)
    y[i0:i1] = s * np.linspace(0, 1, L) ** 3.2 * gan
    return y

def luz_enciende(t0, gan=0.5):
    """El sonido de la luz cuando se presenta. Un foco de escenario: zumbido
    que sube, chasquido del arranque y campana metálica que queda resonando.
    Se le sube SOLO a este momento (pedido 20-08)."""
    y = np.zeros(N)
    i0 = int(t0 * SR)
    # zumbido que sube justo antes
    pre = int(0.9 * SR); j0 = max(0, i0 - pre)
    tt = np.arange(i0 - j0) / SR
    u = np.linspace(0, 1, i0 - j0)
    f = 70 * np.exp(u * 1.5)
    y[j0:i0] += np.sin(2 * np.pi * np.cumsum(f) / SR) * (u ** 3) * gan * 0.45
    # chasquido + campana
    L = min(int(2.6 * SR), N - i0)
    if L <= 0:
        return y
    tk = np.arange(L) / SR
    rng = np.random.default_rng(91)
    chasquido = banda(rng.standard_normal(L), 1200, 11000) * np.exp(-tk * 55)
    campana = np.zeros(L)
    for fq, g, d in [(1480, 1.0, 3.4), (2210, 0.62, 4.2), (3320, 0.34, 5.6),
                     (4460, 0.18, 7.0)]:
        campana += np.sin(2 * np.pi * fq * tk) * g * np.exp(-tk * d)
    y[i0:i0 + L] += (chasquido * 0.9 + campana * 0.5) * gan
    return y


def crack(t0, gan=0.3):
    """Transitorio brillante y corto. Le da definición al golpe: sin esto, el
    impacto es solo grave y en un teléfono no se escucha nada."""
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(0.35 * SR), N - i0)
    if L <= 0:
        return y
    tt = np.arange(L) / SR
    rng = np.random.default_rng(int(t0 * 7) + 3)
    n = rng.standard_normal(L)
    y[i0:i0 + L] = (banda(n, 900, 9000) * np.exp(-tt * 26)
                    + hp(n, 6000) * np.exp(-tt * 70) * 0.7) * gan
    return y


def maquina(t0, n_car, paso=0.088, gan=0.3):
    """Máquina de escribir: un clac por carácter, con la palanca al final.
    Va con el colofón «Turno de noche» del cierre."""
    y = np.zeros(N)
    rng = np.random.default_rng(77)
    for i in range(n_car):
        # paso FIJO: la animación del texto en Remotion usa exactamente
        # t0 + i * paso, así que el clac y la letra tienen que caer juntos.
        tt0 = t0 + i * paso
        i0 = int(tt0 * SR); L = min(int(0.16 * SR), N - i0)
        if L <= 0:
            continue
        tk = np.arange(L) / SR
        ruido = rng.standard_normal(L)
        golpe = banda(ruido, 1400, 7000) * np.exp(-tk * 105)
        cuerpo = np.sin(2 * np.pi * 210 * tk) * np.exp(-tk * 90) * 0.5
        y[i0:i0 + L] += (golpe + cuerpo) * gan * (0.75 + 0.35 * ((i * 3) % 4) / 3.0)
    # el retorno del carro
    i0 = int((t0 + n_car * paso + 0.28) * SR); L = min(int(0.5 * SR), N - i0)
    if L > 0:
        tk = np.arange(L) / SR
        rr = rng.standard_normal(L)
        y[i0:i0 + L] += (banda(rr, 700, 5000) * np.exp(-tk * 12)
                         * (0.4 + 0.6 * np.abs(np.sin(2 * np.pi * 34 * tk)))) * gan * 0.8
        y[i0:i0 + L] += banda(rr, 1200, 8000) * np.exp(-(tk - 0.34) ** 2 * 900) * gan * 1.1
    return y


def impacto(t0, gan=0.55, dec=3.2):
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(dec * SR), N - i0)
    if L <= 0:
        return y
    tt = np.arange(L) / SR
    f = 82 * np.exp(-tt * 2.2) + 31
    ph = 2 * np.pi * np.cumsum(f) / SR
    y[i0:i0 + L] += np.sin(ph) * np.exp(-tt * 1.9) * gan
    rng = np.random.default_rng(int(t0 * 100))
    y[i0:i0 + L] += lp(rng.standard_normal(L) * np.exp(-tt * 9.0), 1600) * 0.18 * gan
    return y

# ---------------- rejilla ----------------
def compases(a, b):
    """downbeats en [a, b)"""
    k = int(np.ceil(a / BAR))
    r = []
    while k * BAR < b:
        r.append(k * BAR)
        k += 1
    return r

def pulsos(a, b, div=BEAT):
    r = []
    x = a
    while x < b:
        r.append(x)
        x += div
    return r
# ============ generadores de ACCIÓN (v4) ============
# Todos son transitorios cortos. Ninguno sostiene ruido: la regla 1 de la mezcla
# se rompió una vez en el R01 y costó un rehecho entero.

def pizz(eventos, gan=0.14):
    """Pizzicato: cuerda pellizcada, decaimiento cortísimo."""
    y = np.zeros(N)
    for (tt0, f) in eventos:
        i0 = int(tt0 * SR); L = min(int(0.45 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        s = np.zeros(L)
        for k, g in [(1, 1.0), (2, 0.55), (3, 0.3), (4, 0.16), (5, 0.09)]:
            s += np.sin(2 * np.pi * f * k * tt + k * 0.4) * g * np.exp(-tt * (9 + k * 3.5))
        s *= np.minimum(1.0, tt / 0.002)
        y[i0:i0 + L] += s
    return y * gan


def rasgado(t0, gan=0.30):
    """La grieta que se abre en el aire. Ruido de banda que sube de frecuencia
    mientras se abre, con chisporroteo encima. Dura 0,5 s: es un transitorio."""
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(0.5 * SR), N - i0)
    if L <= 0:
        return y
    rng = np.random.default_rng(int(t0 * 17) + 2)
    u = np.linspace(0, 1, L)
    n = rng.standard_normal(L)
    s = banda(n, 400, 2000) * (1 - u) + banda(n, 2500, 9000) * u
    tt = np.arange(L) / SR
    y[i0:i0 + L] += s * np.exp(-tt * 5.5) * gan
    return y


def swell(t0, dur=1.2, gan=0.24):
    """El portal abriéndose: armónicos que se abren en abanico."""
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(dur * SR), N - i0)
    if L <= 0:
        return y
    tt = np.arange(L) / SR
    u = tt / dur
    s = np.zeros(L)
    for k, f in enumerate([220, 330, 440, 660, 880]):
        s += np.sin(2 * np.pi * f * (1 + 0.02 * u) * tt) * (1 - k * 0.16) * \
            np.clip((u - k * 0.12) * 3, 0, 1)
    y[i0:i0 + L] += lp(s, 5000) * np.sin(np.pi * u) ** 0.8 * gan * 0.25
    return y


def whoosh(t0, dur=0.45, gan=0.26):
    """El salto. Ruido de banda barriendo de agudo a grave."""
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(dur * SR), N - i0)
    if L <= 0:
        return y
    rng = np.random.default_rng(int(t0 * 23) + 7)
    u = np.linspace(0, 1, L)
    n = rng.standard_normal(L)
    s = banda(n, 3000, 9000) * (1 - u) + banda(n, 300, 1400) * u
    y[i0:i0 + L] += s * np.sin(np.pi * u) * gan
    return y


def tintineo(t0, gan=0.20):
    """El guiño. Dos notas brillantes, la segunda más aguda: es un «tin-tin»
    de complicidad, no una campanada."""
    y = np.zeros(N)
    for k, (dt, f) in enumerate([(0.0, 1320), (0.14, 1980)]):
        i0 = int((t0 + dt) * SR); L = min(int(1.2 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        s = (np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(2 * np.pi * f * 2.76 * tt)
             + 0.2 * np.sin(2 * np.pi * f * 5.4 * tt))
        y[i0:i0 + L] += s * np.exp(-tt * (5.0 + k)) * gan * (1.0 - 0.25 * k)
    return y


def tick(t0, gan=0.22):
    """La corrección. Dos notas que BAJAN y resuelven: el sonido de «listo»."""
    y = np.zeros(N)
    for dt, f in [(0.0, 880), (0.13, 587.33)]:
        i0 = int((t0 + dt) * SR); L = min(int(0.8 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        s = np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(2 * np.pi * f * 3 * tt)
        y[i0:i0 + L] += s * np.exp(-tt * 9) * gan
    return y


def acorde_arriba(t0, gan=0.26):
    """EL HALLAZGO. Arpegio que sube y se queda arriba, con campana. Es el
    momento en que el capítulo dice «acá está»."""
    y = np.zeros(N)
    for k, f in enumerate([A3, C4, E4, A4]):
        i0 = int((t0 + k * 0.075) * SR); L = min(int(1.8 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        s = np.sin(2 * np.pi * f * tt) + 0.5 * np.sin(2 * np.pi * f * 2 * tt)
        y[i0:i0 + L] += s * np.exp(-tt * 3.4) * gan * 0.5
    # la campana encima
    i0 = int((t0 + 0.3) * SR); L = min(int(2.4 * SR), N - i0)
    if L > 0:
        tt = np.arange(L) / SR
        c = np.zeros(L)
        for fq, g, d in [(1760, 1.0, 2.6), (2640, 0.5, 3.4), (3960, 0.25, 4.8)]:
            c += np.sin(2 * np.pi * fq * tt) * g * np.exp(-tt * d)
        y[i0:i0 + L] += c * gan * 0.35
    return y


def boing(t0, gan=0.22):
    """El saltito del hallazgo confirmado."""
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(0.42 * SR), N - i0)
    if L <= 0:
        return y
    tt = np.arange(L) / SR
    u = tt / (L / SR)
    f = 210 * np.exp(u * 1.35) * (1 + 0.09 * np.sin(2 * np.pi * 17 * tt))
    y[i0:i0 + L] += (np.sin(2 * np.pi * np.cumsum(f) / SR)
                     + 0.3 * np.sin(4 * np.pi * np.cumsum(f) / SR)) \
        * np.exp(-tt * 6.5) * gan
    return y


def palmada(t0, gan=0.42):
    """EL CHOQUE DE MANOS. Es el golpe más humano del reel y tiene que sonar a
    piel, no a percusión electrónica: transitorio ancho, cuerpo en medios, y una
    reflexión corta de sala 18 ms después."""
    y = np.zeros(N)
    rng = np.random.default_rng(int(t0 * 41) + 11)
    for dt, g in [(0.0, 1.0), (0.018, 0.34), (0.041, 0.14)]:
        i0 = int((t0 + dt) * SR); L = min(int(0.22 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        n = rng.standard_normal(L)
        s = (banda(n, 700, 5500) * np.exp(-tt * 48)
             + banda(n, 180, 900) * np.exp(-tt * 26) * 0.7)
        y[i0:i0 + L] += s * gan * g
    return y


def apagon(t0, gan=0.34):
    """La sala que queda a oscuras: un golpe grave corto con cola, sin brillo."""
    y = np.zeros(N)
    i0 = int(t0 * SR); L = min(int(2.2 * SR), N - i0)
    if L <= 0:
        return y
    tt = np.arange(L) / SR
    f = 90 * np.exp(-tt * 3.0) + 42
    y[i0:i0 + L] += np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 2.2) * gan
    return y



def chispas(t0, dur=1.6, gan=0.10):
    """Las partículas del portal. Ráfagas cortas de armónicos agudos — NUNCA
    ruido sostenido (regla 1 de la mezcla)."""
    y = np.zeros(N)
    rng = np.random.default_rng(int(t0 * 31) + 5)
    for _ in range(int(dur * 30)):
        tt0 = t0 + rng.random() * dur
        f = 2200 + rng.random() * 5200
        i0 = int(tt0 * SR); L = min(int(0.09 * SR), N - i0)
        if L <= 0:
            continue
        tt = np.arange(L) / SR
        y[i0:i0 + L] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 55) * (0.4 + rng.random())
    return y * gan


# ================= ARREGLO =================
APAGON = 3.5
GRIETA = 6.0
ABRE = 7.5
SALTO = 10.5
GUINO = 12.0
TRABAJO = 14.0
HALLAZGO = 16.5
SALTITO = 19.5
ALERTA = 21.0
CORRIGE = 23.0
RESPIRO = 27.0
AMANECE = 27.5
EQUIPO = 30.0
CHOQUE = 32.55   # el instante en que las manos SE TOCAN, no el corte
CIERRE = 35.0

# --- I · se van (0–6,0) --------------------------------------------------
# Tibio y humano: todavía hay gente y se están riendo. NO abrir en misterio.
irse_pad = pad([(0.0, 6.2, "Am")], 0.26, fc=1000, ataque=1.0, cola=1.0)
irse_sub = sub(0.8, 6.4, f=nota(45), gan=0.09, fi=1.8, fo=0.8)
irse_pizz = pizz([(0.5, A3), (1.5, C4), (2.6, E4), (4.6, A3)], 0.10)
g_clac = crack(2.5, 0.20)                                   # ♪ baja el interruptor
g_apagon = apagon(APAGON, 0.34) + crack(APAGON, 0.12)       # ♪ queda apagado

# --- II · la llegada (6,0–13,5) -----------------------------------------
g_grieta = rasgado(GRIETA, 0.46) + chispas(GRIETA, 1.8, 0.10)   # ♪ se rasga
g_abre = (swell(ABRE, 1.4, 0.34) + chispas(ABRE, 1.0, 0.09)
          + crack(ABRE + 0.9, 0.38))                             # ♪ la abre de golpe
g_salto = whoosh(SALTO - 0.25, 0.45, 0.26) \
    + impacto(SALTO + 0.20, 0.52, 2.4) + crack(SALTO + 0.20, 0.36)   # ♪ aterriza
g_guino = tintineo(GUINO + 0.35, 0.36)                          # ♪ el guiño
lleg_pad = pad([(6.0, 10.5, "F"), (10.5, 14.1, "C")], 0.38, fc=1700,
               ataque=0.3, cola=0.9)
lleg_sub = sub(6.0, 14.2, f=nota(45), gan=0.13, fi=0.5, fo=0.6)

# --- III · a trabajar (13,5–27,0) ---------------------------------------
TRAB = [(14.0, 16.0, "Am"), (16.0, 18.0, "C"), (18.0, 20.0, "F"),
        (20.0, 22.0, "G"), (22.0, 24.0, "Am"), (24.0, 27.0, "F")]
tra_pad = pad(TRAB, 0.42, fc=1800, ataque=0.25, cola=0.8)
tra_sub = sub(14.0, 25.5, f=nota(45), gan=0.16, fi=0.3, fo=1.5)
tra_ost = (ostinato(14.0, 18.0, [A3, C4, E4, A4, E4, C4], 0.10, paso=BEAT / 4)
           + ostinato(18.0, 22.0, [F3, A3, C4, F4, C4, A3], 0.10, paso=BEAT / 4)
           + ostinato(22.0, 25.0, [A3, C4, E4, A4], 0.09, paso=BEAT / 4))
g_chasquido = crack(TRABAJO, 0.30) + impacto(TRABAJO, 0.28, 2.0)   # ♪ chasquea
g_dato1 = impacto(15.5, 0.24, 1.6) + crack(15.5, 0.19)             # ♪ dato 1
g_dato2 = impacto(20.0, 0.30, 1.8) + crack(20.0, 0.24)             # ♪ dato 2
g_hallazgo = acorde_arriba(HALLAZGO, 0.46) + crack(HALLAZGO, 0.26)                          # ♪ ¡encontró!
g_saltito = boing(SALTITO, 0.22)                                    # ♪ el saltito
g_alerta = (braam(ALERTA, "G", 1.6, 0.30) + crack(ALERTA, 0.38)
            + impacto(22.0, 0.28, 1.6) + crack(22.0, 0.22))   # ♪ + dato 3      # ♪ la alerta
g_corrige = tick(CORRIGE + 0.5, 0.60)                               # ♪ lo corrige
g_maquina = maquina(25.2, 51, paso=0.62 / 30.0, gan=0.10)           # ♪ el resumen

# --- IV · amanece y llega el equipo (27,5–35,0) -------------------------
# Acá el capítulo cambia de temperatura: es lo más cálido de toda la serie.
ama_pad = pad([(27.1, 30.0, "F"), (30.0, 32.0, "C"), (32.0, 35.1, "F")],
              0.52, fc=2200, ataque=0.5, cola=1.6)
ama_cuer = cuerdas([(28.0, 30.0, "F"), (30.0, 35.1, "C")], 0.72)
ama_sub = sub(27.6, 35.2, f=nota(41), gan=0.11, fi=1.4, fo=1.2)
g_equipo = (piano([(EQUIPO, C5), (EQUIPO + 0.5, G4), (EQUIPO + 1.1, E4)], 0.13, 4.5)
            + tintineo(EQUIPO, 0.20))
g_choque = palmada(CHOQUE, 0.78) + impacto(CHOQUE, 0.20, 1.4)       # ♪ ¡PLAF!
g_juntos = braam(33.5, "C", 2.2, 0.42)                              # ♪ el equipo

# --- V · el cierre (35,0–40,0) ------------------------------------------
cie_pad = pad([(35.0, 40.0, "C")], 0.56, fc=2600, ataque=0.5, cola=2.2)
cie_cuer = cuerdas([(35.0, 40.0, "C")], 0.68)
cie_sub = sub(35.0, 40.0, f=nota(48), gan=0.13, fi=0.5, fo=2.4)
g_cierre = impacto(CIERRE, 0.40, 3.0) + crack(CIERRE, 0.26)
# el punto que aterriza en la «g» del logo: frame 1050+104 = 1154 → 38,47 s
g_punto = crack(38.47, 0.22) + impacto(38.47, 0.18, 1.4)
# colofón «Nueve minutos» (13 caracteres) — mismo paso que TW_PASO del montaje
escribiendo = maquina(CIERRE + 112 / 30.0, 13, paso=2 / 30.0, gan=0.22)

# --- percusión: sólo en el tramo de trabajo y en los remates -------------
kicks = [x for x in pulsos(14.0, 25.0, BEAT)][::2] + [CIERRE, EQUIPO, CHOQUE]
bombos = bombo(sorted(set(kicks)), 0.40)
taikos = ([(x, 0.9 if abs(x % BAR) < 1e-6 else 0.42) for x in pulsos(14.0, 25.0, BEAT)]
          + [(CIERRE, 1.0), (SALTO + 0.2, 0.8), (CHOQUE, 0.6), (GRIETA, 0.5)])
taikos_s = taiko(taikos, 0.23)
hats_s = hats([(x, 0.65 if i % 2 else 0.32)
               for i, x in enumerate(pulsos(14.25, 25.0, BEAT / 2))], 0.038)

# ---------------- mezcla ----------------
# CAMA y GOLPES van por separado a propósito. Subirles la ganancia a los golpes
# hasta que se oigan sobre la cama sólo los distorsiona; lo que se hace en cine
# es **abrirles un hueco**: la cama baja 4,5 dB durante 150 ms en cada acento y
# vuelve. Medido antes de esto, seis de los quince golpes no despegaban ni 2 dB
# del fondo — o sea, no existían.
cama = np.sum([
    irse_pad, irse_sub, irse_pizz,
    lleg_pad, lleg_sub,
    tra_pad, tra_sub, tra_ost,
    ama_pad, ama_cuer, ama_sub,
    cie_pad, cie_cuer, cie_sub,
    bombos, taikos_s, hats_s,
], axis=0)

golpes = np.sum([
    g_clac, g_apagon, g_grieta, g_abre, g_salto, g_guino,
    g_chasquido, g_dato1, g_dato2, g_hallazgo, g_saltito, g_alerta,
    g_corrige, g_maquina, g_equipo, g_choque, g_juntos,
    g_cierre, g_punto, escribiendo,
], axis=0)

# el hueco por acento: 40 ms de bajada, 110 ms abajo, 200 ms de vuelta
ACENTOS = [2.5, APAGON, GRIETA, ABRE + 0.9, SALTO + 0.2, GUINO + 0.35,
           TRABAJO, 15.5, 20.0, 22.0, HALLAZGO, SALTITO, ALERTA, CORRIGE + 0.5,
           EQUIPO, CHOQUE, CIERRE]
hueco_golpes = np.ones(N)
for tt0 in ACENTOS:
    i0 = int((tt0 - 0.04) * SR); i1 = int((tt0 + 0.11) * SR); i2 = int((tt0 + 0.31) * SR)
    if i0 < 0 or i2 > N:
        continue
    hueco_golpes[i0:i1] = np.minimum(hueco_golpes[i0:i1], 10 ** (-3.5 / 20))
    hueco_golpes[i1:i2] = np.minimum(
        hueco_golpes[i1:i2],
        np.linspace(10 ** (-3.5 / 20), 1.0, i2 - i1))

# Los golpes van 3,5 dB por encima de la cama. Medido: sin esto, diez de los
# dieciséis no despegaban del groove ni 2,5 dB de pico y se perdían.
mezcla = cama * hueco_golpes + golpes * 1.28
mezcla = hp(reverb(mezcla, 2.2, 0.25), 34, 2)

# --- dinámica POR ARREGLO. El respiro es la firma: −10 dB medio segundo, una
#     sola vez en todo el reel, y vuelve rápido: si tarda, se lee como un error.
NIV = [(0.0, 0.72), (GRIETA, 0.94), (TRABAJO, 1.00), (RESPIRO, 0.50),
       (AMANECE, 0.86), (EQUIPO, 1.00), (CIERRE, 1.00)]
niv = np.full(N, NIV[0][1])
for i, (tt0, g) in enumerate(NIV):
    if i == 0:
        continue
    r = 0.1 if g == 0.50 or NIV[i - 1][1] == 0.50 else 1.0
    i0 = int((tt0 - r) * SR); i1 = int(tt0 * SR)
    niv[i1:] = g
    niv[i0:i1] = np.linspace(NIV[i - 1][1], g, i1 - i0)
mezcla *= niv

# --- HUECO DE VOZ: −6,5 dB fijos entre 300 Hz y 3,5 kHz. Constante, no bombea.
hueco = banda(mezcla, 300, 3500)
mezcla = mezcla - hueco * (1 - 10 ** (-6.5 / 20))

mezcla *= 0.72 / (np.abs(mezcla).max() + 1e-9)
rms = 20 * np.log10(np.sqrt((mezcla ** 2).mean()))
mezcla *= 10 ** ((-27.5 - rms) / 20)
mezcla = np.tanh(mezcla * 1.10) / 1.10

izq = mezcla + 0.10 * np.roll(mezcla, int(0.011 * SR))
der = np.roll(mezcla, int(0.013 * SR)) * 0.97 + 0.10 * mezcla
st = np.empty(N * 2)
st[0::2] = np.clip(izq, -1, 1)
st[1::2] = np.clip(der, -1, 1)

w = wave.open(OUT_WAV, "wb")
w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st * 32767).astype(np.int16).tobytes()); w.close()
print("música R02 v4: %.1f s · RMS %.1f dBFS · pico %.1f dBFS -> %s"
      % (DUR, 20 * np.log10(np.sqrt((mezcla ** 2).mean())),
         20 * np.log10(np.abs(mezcla).max()), OUT_WAV))

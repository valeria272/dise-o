#!/usr/bin/env python3
"""
R01 «Cómo llegó G.CL» — banda sonora v3, 60 s. Reescrita entera 19-08-2026.

Qué estaba mal en la v2 y por qué se rehizo:

  1. RUIDO. La v2 tenía una capa llamada `aire` que era literalmente ruido
     blanco pasa-altos sonando los 57 s. Medido: −28 dB en 8–16 kHz, o sea
     26 dB MÁS FUERTE que el residuo de ruido de la locución. Lo que se oía
     como "ruido de fondo" no era la voz: era la música. Eliminada.

  2. BOMBEO. La v2 hacía ducking siguiendo la envolvente de la voz
     (`duck = 1 - 0.62 * env`). Con 14 bloques de voz y silencios de hasta 7 s
     entre medio, la música subía y bajaba 8,4 dB catorce veces sin relación
     con la música. Eso es «la música a veces baja y sube de la nada».
     Reemplazado por dos cosas que hacen los mezcladores de cine:
       · un HUECO DE ECUALIZACIÓN fijo de −4,5 dB entre 300 Hz y 3,5 kHz, que
         es donde vive la inteligibilidad de la voz. Es constante: no bombea.
       · dinámica POR ARREGLO: los tramos con voz tienen menos capas y menos
         nivel, pero el cambio ocurre en el compás, no en la sílaba.

  3. PLANA. La v2 eran tres pads y un pulso. No había progresión armónica, ni
     percusión, ni forma. Ahora hay rejilla de 120 BPM (compás de 2 s, alineado
     a los cortes de imagen), progresión Am–F–C–G que resuelve a Do mayor,
     bombo/taiko/hats, braams de metales, ostinato de semicorcheas, riser y
     platillo invertido en la llegada.

Estructura (s):
   0–12   la noche      drone Am, piano disperso, sin pulso
  12–14   la carga      riser + platillo invertido + redoble de toms
  14      LA LLEGADA    impacto sub + braam + entra la percusión
  14–17,6 el arranque   ostinato completo (no hay voz encima)
  17,6–27 el sistema    bajo voz: se van los agudos, queda pulso y pad
  27–33,6 la ficha      bajo voz NO hay: es la presentación → tutti
  33,6–46 el equipo     bajo voz: Fa mayor cálido, cuerdas, percusión liviana
  46–52   la tesis      vuelve a cargar
  52–60   el cierre     resuelve en Do, grande, y decae con el logo

Salida: public/assets/gcl/music_r01.mp3
"""
import wave, os
import numpy as np

SR = 44100
DUR = 60.0
N = int(SR * DUR)
t = np.arange(N) / SR

BPM = 120.0
BEAT = 60.0 / BPM        # 0,5 s
BAR = BEAT * 4           # 2,0 s

OUT_WAV = "/tmp/music_r01.wav"

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

# ================= ARREGLO =================
LLEGADA = 14.0

# --- I · la noche (0–12) --------------------------------------------------
noche_pad = pad([(0.0, 12.6, "Am")], gan=0.30, fc=760, ataque=2.6, cola=2.2)
noche_sub = sub(0.0, 13.2, A2, 0.075, 2.4, 2.0)
noche_piano = piano([(1.0, E4), (3.5, C4), (6.0, A3), (8.5, E4), (10.5, C4)], gan=0.075, dec=4.5)

# --- II · la carga (12–14) ------------------------------------------------
carga = (riser(LLEGADA, 2.4, 0.40)
         + platillo_invertido(LLEGADA, 2.2, 0.20)
         + taiko([(12.0, .35), (12.5, .45), (13.0, .55), (13.25, .6),
                  (13.5, .75), (13.75, .9)], 0.30))

# --- III · la llegada + el arranque (14–17,6) -----------------------------
# La llegada pedía más peso ("esa parte está potente, dale más énfasis"):
# impacto + braam más fuertes, un crack de definición y un segundo braam.
llegada = (impacto(LLEGADA, 0.85) + braam(LLEGADA, "Am", 3.2, 0.85)
           + braam(LLEGADA + 2.0, "F", 2.0, 0.42)
           + crack(LLEGADA, 0.34) + taiko([(LLEGADA, 1.25)], 0.42))
arranque_ost = ostinato(LLEGADA, 17.6, [A3, C4, E4, C4, A3, E4, A3, C4], gan=0.115)
arranque_pad = pad([(14.0, 16.0, "Am"), (16.0, 17.6, "F")], gan=0.17, fc=1800, ataque=0.05, cola=0.8)
arranque_sub = sub(14.0, 17.8, A2, 0.10, 0.02, 0.6)

# --- IV · el sistema (17,6–27) · bajo voz --------------------------------
sist_sec = [(17.7, 19.0, "Am"), (19.0, 21.0, "F"), (21.0, 23.0, "C"),
            (23.0, 25.0, "G"), (25.0, 27.0, "Am")]
sist_pad = pad(sist_sec, gan=0.20, fc=1100, ataque=0.35, cola=1.0)
sist_ost = ostinato(17.7, 27.0, [A3, C4, E4, C4], gan=0.045, fc=2400)
sist_sub = sub(17.7, 27.2, A2, 0.075, 0.4, 0.5)

# --- V · la ficha (27–33,6) · sin voz → tutti ----------------------------
ficha_sec = [(27.0, 29.0, "Am"), (29.0, 31.0, "F"), (31.0, 33.6, "C")]
ficha_pad = pad(ficha_sec, gan=0.24, fc=2400, ataque=0.05, cola=1.0)
ficha_cuer = cuerdas(ficha_sec, gan=0.9)
ficha_ost = ostinato(27.0, 33.6, [A3, C4, E4, A4, E4, C4], gan=0.10)
# Cuando cobra vida (27 s) la música también tiene que encender.
ficha_braam = (braam(27.0, "Am", 2.8, 0.95) + braam(31.0, "C", 2.6, 0.52)
               + impacto(27.0, 0.85) + crack(27.0, 0.50)
               + platillo_invertido(27.0, 1.8, 0.30)
               + luz_enciende(27.0, 0.62))
ficha_sub = sub(27.0, 33.8, A2, 0.10, 0.02, 0.7)

# --- VI · el equipo (33,6–46) · bajo voz, Fa mayor -----------------------
eq_sec = [(33.6, 35.0, "F"), (35.0, 37.0, "C"), (37.0, 39.0, "Dm"),
          (39.0, 41.0, "Bb"), (41.0, 43.0, "F"), (43.0, 46.0, "C")]
eq_pad = pad(eq_sec, gan=0.32, fc=1350, ataque=0.5, cola=1.2)
eq_cuer = cuerdas(eq_sec, gan=1.05)
eq_sub = sub(33.6, 46.2, F2, 0.085, 0.8, 0.8)
eq_piano = piano([(34.5, C5), (36.5, G4), (38.5, F4), (40.5, D4),
                  (42.5, C5), (44.5, G4)], gan=0.06, dec=3.5)

# --- VII · la tesis (46–52) ---------------------------------------------
tesis_sec = [(46.0, 48.0, "Am"), (48.0, 50.0, "F"), (50.0, 53.5, "C")]
tesis_pad = pad(tesis_sec, gan=0.22, fc=1500, ataque=0.3, cola=1.0)
tesis_cuer = cuerdas(tesis_sec, gan=0.8)
tesis_sub = sub(46.0, 53.9, A2, 0.085, 0.5, 0.5)
tesis_braam = braam(50.0, "C", 3.0, 0.40)

# --- máquina de escribir del colofón «Turno de noche» (14 caracteres) ---
escribiendo = maquina(56.90, 14, 0.088, 0.30)

# --- VIII · el cierre (52–60) -------------------------------------------
cierre_sec = [(53.5, 57.0, "C"), (57.0, 60.0, "F")]
cierre_pad = pad(cierre_sec, gan=0.34, fc=2600, ataque=0.06, cola=3.6)
cierre_cuer = cuerdas(cierre_sec, gan=1.5)
cierre_sub = sub(53.5, 59.8, C2, 0.10, 0.05, 4.5)
cierre_hit = impacto(53.5, 0.58) + braam(53.5, "C", 3.4, 0.62)
cierre_pun = impacto(57.0, 0.30, 3.0)      # el punto aterriza en el logo
cierre_piano = piano([(53.5, C5), (54.5, G4), (55.5, E4), (57.0, C5)], gan=0.075, dec=5.0)

# --- percusión (una sola línea, con la rejilla de 120 BPM) ---------------
kicks = []
kicks += [x for x in pulsos(14.0, 17.6, BEAT)][::2]         # negras 1 y 3
kicks += [x for x in pulsos(17.7, 27.0, BEAT)][::2]
kicks += [x for x in pulsos(27.0, 33.6, BEAT)][::2]
kicks += [x for x in pulsos(33.6, 46.0, BAR)]              # más espaciado
kicks += [x for x in pulsos(46.0, 53.5, BEAT)][::2]
kicks += [53.5, 54.5, 55.5, 57.0]
bombos = bombo(sorted(set(kicks)), 0.42)

taikos = ([(x, 0.9 if abs(x % BAR) < 1e-6 else 0.45) for x in pulsos(14.0, 17.6, BEAT)]
          + [(x, 0.85 if abs(x % BAR) < 1e-6 else 0.4) for x in pulsos(27.0, 33.6, BEAT)]
          + [(x, 0.34) for x in compases(33.6, 46.0)]
          + [(x, 0.8) for x in compases(46.0, 53.5)]
          + [(53.5, 1.0), (55.5, 0.8), (57.0, 0.9)])
taikos_s = taiko(taikos, 0.30)

hats_l = ([(x, 0.6 if i % 2 else 0.3) for i, x in enumerate(pulsos(17.95, 27.0, BEAT / 2))]
          + [(x, 0.7 if i % 2 else 0.35) for i, x in enumerate(pulsos(27.25, 33.6, BEAT / 2))]
          + [(x, 0.4 if i % 2 else 0.2) for i, x in enumerate(pulsos(33.85, 46.0, BEAT))])
hats_s = hats(hats_l, 0.045)

# ---------------- mezcla ----------------
capas = [
    noche_pad, noche_sub, noche_piano,
    carga,
    llegada, arranque_ost, arranque_pad, arranque_sub,
    sist_pad, sist_ost, sist_sub,
    ficha_pad, ficha_cuer, ficha_ost, ficha_braam, ficha_sub,
    eq_pad, eq_cuer, eq_sub, eq_piano,
    tesis_pad, tesis_cuer, tesis_sub, tesis_braam,
    cierre_pad, cierre_cuer, cierre_sub, cierre_hit, cierre_pun, cierre_piano,
    escribiendo,
    bombos, taikos_s, hats_s,
]
mezcla = np.sum(capas, axis=0)
mezcla = hp(reverb(mezcla, 2.4, 0.26), 34, 2)

# --- dinámica POR ARREGLO: solo cambia en el compás, con rampas de medio
#     compás. Nada de seguir la envolvente de la voz.
NIV = [(0.0, 0.78), (12.0, 1.00), (17.7, 0.66), (27.0, 1.00),
       (33.6, 0.70), (46.0, 0.80), (53.5, 1.00)]
niv = np.full(N, NIV[0][1])
for i, (tt0, g) in enumerate(NIV):
    if i == 0:
        continue
    r = 1.0                                   # rampa de medio compás
    i0 = int((tt0 - r) * SR); i1 = int(tt0 * SR)
    niv[i1:] = g
    niv[i0:i1] = np.linspace(NIV[i - 1][1], g, i1 - i0)
mezcla *= niv

# --- HUECO DE VOZ: −6,5 dB fijos entre 300 Hz y 3,5 kHz. Constante, no bombea.
hueco = banda(mezcla, 300, 3500)
mezcla = mezcla - hueco * (1 - 10 ** (-6.5 / 20))   # hueco de voz más profundo

# --- nivel final
mezcla *= 0.72 / (np.abs(mezcla).max() + 1e-9)
rms = 20 * np.log10(np.sqrt((mezcla ** 2).mean()))
obj = -27.5   # la voz se perdía: 3,5 dB menos de cama
mezcla *= 10 ** ((obj - rms) / 20)
mezcla = np.tanh(mezcla * 1.10) / 1.10

# --- estéreo
izq = mezcla + 0.10 * np.roll(mezcla, int(0.011 * SR))
der = np.roll(mezcla, int(0.013 * SR)) * 0.97 + 0.10 * mezcla
st = np.empty(N * 2)
st[0::2] = np.clip(izq, -1, 1)
st[1::2] = np.clip(der, -1, 1)

w = wave.open(OUT_WAV, "wb")
w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st * 32767).astype(np.int16).tobytes()); w.close()
print("música v3: %.1f s · RMS %.1f dBFS · pico %.1f dBFS -> %s"
      % (DUR, 20*np.log10(np.sqrt((mezcla**2).mean())), 20*np.log10(np.abs(mezcla).max()), OUT_WAV))

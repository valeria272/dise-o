#!/usr/bin/env python3
"""
Locución de R01 — cadena v3 (reescrita 19-08-2026).

Por qué v3: la v2 usaba sustracción espectral agresiva. Eso baja el número del
piso de ruido, pero deja "musical noise" — un burbujeo que el oído lee como
RUIDO, no como silencio. Feedback textual: «la voz sigue limpiándola, el ruido
de fondo suena como eso, ruido».

Cadena nueva, en el orden en que la haría un ingeniero de sonido:
  1. pasa-altos 85 Hz            quita rumble y pisadas
  2. estimador de ruido por mínimos estadísticos (no percentil global)
  3. supresión MMSE-LSA con SNR a priori "decision-directed"  <- el cambio clave
     (Ephraim-Malah: la ganancia se suaviza en el tiempo, así que no hay
      burbujeo; es lo que usan iZotope/Adobe por debajo)
  4. suelo espectral con FORMA de ruido a -26 dB: deja un lecho de aire natural
     en vez de un agujero digital, que es lo que delata el procesado
  5. de-reverb espectral suave   la pieza tenía cola; la cola es lo que suena
     "sucio" cuando la voz para
  6. de-esser, presencia, expansor suave (no puerta), compresor, nivel
  7. monta cada bloque en su beat del reel

Uso: procesa-vo-gcl.py <origen> <salida.wav>
"""
import wave, sys, os
import numpy as np

SR = 44100
TOTAL_S = 60.0
RITMO = 1.085   # 8,5% más lenta — ver estirar()

BLOQUES = [
    # Locución v2 — voz clonada, archivo magnific_bxLolbK5Y2.mp3 (19-08-2026).
    # 14 bloques, detectados por energía y calzados uno a uno con el guion.
    # (inicio_src, fin_src, destino_reel, texto)
    (0.72,  2.08,  0.90, "Un lunes cualquiera."),
    (2.26,  3.36,  2.45, "Once de la noche."),
    (3.90,  6.70,  4.30, "Alguien dijo en voz alta lo que todos pensabamos."),
    (7.10,  8.96, 10.70, "Nadie creyo que fuera a existir."),
    (9.64, 12.12, 17.70, "Partio auditando tres anos de campanas."),
    (12.48, 14.98, 23.20, "Encontro un patron que estuvo siempre ahi."),
    (15.66, 17.66, 33.60, "Hoy trabaja al lado nuestro."),
    (18.10, 19.26, 38.30, "Ve lo mismo que tu."),
    (20.22, 21.88, 39.60, "Y lo que el ojo ya no alcanza."),
    (22.48, 23.94, 43.20, "Apagamos las luces."),
    (24.36, 25.36, 44.85, "El no se apaga."),
    (26.00, 27.32, 47.70, "Pero no decide el."),
    (27.70, 29.18, 50.20, "Decidimos nosotros."),
    (29.46, 30.54, 51.85, "Con mas criterio."),
]

# ---------------- io ----------------
def leer_wav(p):
    w = wave.open(p)
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64) / 32768.0
    if w.getnchannels() == 2:
        x = x.reshape(-1, 2).mean(axis=1)
    return x, w.getframerate()

def escribir_wav(p, x, sr):
    x = np.clip(x, -1, 1)
    w = wave.open(p, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()

# ---------------- stft ----------------
NFFT, HOP = 2048, 512
VENT = np.hanning(NFFT + 1)[:-1]

def stft(x):
    n = 1 + max(0, (len(x) - NFFT)) // HOP
    idx = np.arange(NFFT)[None, :] + HOP * np.arange(n)[:, None]
    return np.fft.rfft(x[idx] * VENT, axis=1)

def istft(S, largo):
    y = np.zeros(largo + NFFT); nrm = np.zeros(largo + NFFT)
    seg = np.fft.irfft(S, NFFT, axis=1) * VENT
    for i in range(S.shape[0]):
        y[i*HOP:i*HOP+NFFT] += seg[i]
        nrm[i*HOP:i*HOP+NFFT] += VENT ** 2
    nrm[nrm < 1e-8] = 1e-8
    return (y / nrm)[:largo]

# ---------------- E1 (integral exponencial) sin scipy ----------------
def exp1(x):
    """Abramowitz & Stegun 5.1.53 (x<1) y 5.1.56 (x>=1)."""
    x = np.maximum(x, 1e-9)
    y = np.empty_like(x)
    m = x < 1.0
    xa = x[m]
    y[m] = (-np.log(xa) - 0.57721566 + 0.99999193*xa - 0.24991055*xa**2
            + 0.05519968*xa**3 - 0.00976004*xa**4 + 0.00107857*xa**5)
    xb = x[~m]
    num = xb**4 + 8.5733287401*xb**3 + 18.059016973*xb**2 + 8.6347608925*xb + 0.2677737343
    den = xb**4 + 9.5733223454*xb**3 + 25.6329561486*xb**2 + 21.0996530827*xb + 3.9584969228
    y[~m] = np.where(xb > 300, 0.0, num / (den * xb * np.exp(np.minimum(xb, 300))))
    return y

# ---------------- filtros ----------------
def _fft_filtro(x, curva_fn):
    n = 1 << int(np.ceil(np.log2(len(x) + 1)))
    X = np.fft.rfft(x, n)
    f = np.fft.rfftfreq(n, 1 / SR)
    return np.fft.irfft(X * curva_fn(f), n)[:len(x)]

def pasa_altos(x, fc, orden=2):
    return _fft_filtro(x, lambda f: ((f / fc) ** orden) / (1 + (f / fc) ** orden))

def pasa_bajos(x, fc, orden=2):
    return _fft_filtro(x, lambda f: 1.0 / (1 + (f / fc) ** orden))

# ---------------- ruido: mínimos estadísticos ----------------
def perfil_ruido(mag, ventana_tramas=90):
    """Mínimo corrido por bin sobre ~1 s. Sigue al ruido si cambia, y no se
    contamina con la voz (la voz nunca es el mínimo de una ventana de 1 s)."""
    T, F = mag.shape
    pot = mag ** 2
    # suavizado temporal previo para que el mínimo no sea un valle puntual
    a = 0.7
    s = np.empty_like(pot); s[0] = pot[0]
    for i in range(1, T):
        s[i] = a * s[i-1] + (1 - a) * pot[i]
    mn = np.empty_like(s)
    for i in range(T):
        lo = max(0, i - ventana_tramas // 2); hi = min(T, i + ventana_tramas // 2)
        mn[i] = s[lo:hi].min(axis=0)
    return mn * 1.9      # corrección de sesgo del estimador de mínimos

# ---------------- supresión MMSE-LSA ----------------
def suprimir(x, suelo_db=-30.0):
    S = stft(x)
    mag = np.abs(S); fase = np.angle(S)
    pot = mag ** 2
    # Sobre-sustraccion por banda: dura donde el ruido molesta (rumble de sala
    # bajo 300 Hz, siseo sobre 5 kHz) y suave donde vive la voz. Aplicarla plana
    # era el error de la v2: para bajar el rumble habia que pasarse en la banda
    # de la voz, y ahi es donde aparece el burbujeo.
    fbin = np.fft.rfftfreq(NFFT, 1 / SR)
    sobre = np.interp(fbin, [0, 200, 320, 700, 4500, 6000, 12000],
                            [3.4, 3.0, 1.85, 1.6,  1.6,  2.4,   2.8])
    lam = perfil_ruido(mag) * sobre[None, :]              # potencia de ruido
    T, F = mag.shape

    alfa = 0.96                                           # decision-directed
    G = np.empty((T, F))
    prev_amp2 = np.zeros(F)
    prev_gam = np.ones(F)
    for i in range(T):
        gam = np.clip(pot[i] / (lam[i] + 1e-14), 1e-6, 1e6)          # SNR a posteriori
        xi = alfa * (prev_amp2 / (lam[i] + 1e-14)) + (1 - alfa) * np.maximum(gam - 1, 0)
        xi = np.maximum(xi, 10 ** (-2.2))                            # xi_min ~ -22 dB
        v = xi / (1 + xi) * gam
        g = xi / (1 + xi) * np.exp(0.5 * exp1(v))                    # ganancia LSA
        g = np.clip(g, 0.0, 1.0)
        G[i] = g
        prev_amp2 = (g * mag[i]) ** 2
        prev_gam = gam

    # suavizado de la ganancia en frecuencia: mata el burbujeo residual
    k = np.array([0.10, 0.20, 0.40, 0.20, 0.10])
    Gs = np.empty_like(G)
    for j in range(F):
        lo = max(0, j - 2); hi = min(F, j + 3)
        w = k[(lo - (j - 2)):(5 - ((j + 3) - hi))]
        Gs[:, j] = (G[:, lo:hi] * w).sum(axis=1) / w.sum()

    # SUELO CON FORMA DE RUIDO: en vez de dejar un agujero, se deja un lecho de
    # aire al nivel del ruido -26 dB. Suena a sala, no a procesado.
    piso = 10 ** (suelo_db / 20)
    Gs = np.maximum(Gs, piso)

    return istft(Gs * mag * np.exp(1j * fase), len(x)), lam

# ---------------- de-reverb espectral ----------------
def dereverb(x, gan=0.55, retardo=4, decaimiento=0.62):
    """Estima la cola tardía como una copia atenuada del espectro anterior y la
    resta. Suave: solo quita el 'baño' que se oye cuando la voz corta."""
    S = stft(x)
    mag = np.abs(S); fase = np.angle(S)
    T = mag.shape[0]
    cola = np.zeros_like(mag)
    for i in range(retardo, T):
        cola[i] = decaimiento * (mag[i - retardo] * 0.6 + cola[i - 1] * 0.55)
    limpio = np.maximum(mag - gan * cola, mag * 0.20)
    return istft(limpio * np.exp(1j * fase), len(x))

# ---------------- vocoder de fase: alargar sin bajar el tono ----------------
def estirar(x, factor):
    """Alarga la locución preservando el tono (factor 1.08 = 8% más lenta).

    Por qué: el feedback fue «la voz es muy casual, debería ser más tipo
    documental». Lo que separa una locución documental de una conversacional es
    sobre todo el RITMO — una narración documental va entre un 6% y un 10% más
    lenta y con las sílabas más sostenidas. Bajarle el tono no sirve (ya se
    probó: quedó «muy grave»); alargarla sí.
    """
    S = stft(x)
    T, F = S.shape
    if T < 3:
        return x
    mag = np.abs(S); ph = np.angle(S)
    omega = 2 * np.pi * np.arange(F) * HOP / NFFT      # avance de fase esperado
    dphi = np.diff(ph, axis=0) - omega[None, :]
    dphi = np.mod(dphi + np.pi, 2 * np.pi) - np.pi      # desviación envuelta
    frec = omega[None, :] + dphi                        # frecuencia instantánea

    t_new = np.arange(0, T - 1, 1.0 / factor)
    Y = np.empty((len(t_new), F), dtype=complex)
    acum = ph[0].copy()
    for i, tt in enumerate(t_new):
        i0 = int(tt); fr = tt - i0
        m = (1 - fr) * mag[i0] + fr * mag[min(i0 + 1, T - 1)]
        Y[i] = m * np.exp(1j * acum)
        acum = acum + frec[min(i0, T - 2)]
    return istft(Y, int(len(x) * factor))


def color_documental(x):
    """Peso de pecho y menos brillo de charla.

    +2 dB entre 170 y 340 Hz (cuerpo, autoridad) y −1,8 dB entre 3 y 5,5 kHz,
    que es la banda que hace que una voz suene 'conversada' y cercana al
    micrófono. No toca la inteligibilidad (1-3 kHz)."""
    cuerpo = pasa_bajos(pasa_altos(x, 170), 340)
    charla = pasa_bajos(pasa_altos(x, 3000), 5500)
    return x + cuerpo * (10 ** (2.0 / 20) - 1) - charla * (1 - 10 ** (-1.8 / 20))


# ---------------- utilidades de dinámica ----------------
def envolvente(x, ms_at=5, ms_rel=90):
    a_at = np.exp(-1.0 / (SR * ms_at / 1000.0))
    a_rl = np.exp(-1.0 / (SR * ms_rel / 1000.0))
    e = np.empty_like(x); y = 0.0
    ax = np.abs(x)
    for i in range(len(x)):
        v = ax[i]
        a = a_at if v > y else a_rl
        y = a * y + (1 - a) * v
        e[i] = y
    return e

def expansor(x, umbral_db=-46, razon=2.2, piso_db=-16):
    """Expansor suave hacia abajo. NO es puerta: nunca cierra del todo, así que
    no se oye 'abrir y cerrar'."""
    e = envolvente(x, 4, 140)
    edb = 20 * np.log10(e + 1e-9)
    exceso = np.minimum(edb - umbral_db, 0.0)
    gdb = np.maximum(exceso * (razon - 1.0), piso_db)
    return x * 10 ** (gdb / 20)

def comprimir(x, umbral_db=-24, razon=2.4, ms_at=8, ms_rel=140):
    e = envolvente(x, ms_at, ms_rel)
    edb = 20 * np.log10(e + 1e-9)
    exceso = np.maximum(edb - umbral_db, 0.0)
    return x * 10 ** (-exceso * (1 - 1 / razon) / 20)

def deesser(x, red=0.5):
    s = pasa_altos(pasa_bajos(x, 9000), 5200)
    cuerpo = pasa_bajos(pasa_altos(x, 300), 3000)
    es = envolvente(s, 2, 40); ec = envolvente(cuerpo, 2, 40) + 1e-6
    r = np.clip((es / ec - 0.32) / 0.5, 0, 1)
    return x - s * r * red

def presencia(x, db=2.2):
    banda = pasa_bajos(pasa_altos(x, 2000), 4200)
    return x + banda * (10 ** (db / 20) - 1)

def normalizar_rms(x, obj_db):
    r = np.sqrt(np.mean(x ** 2)) + 1e-12
    return x * 10 ** ((obj_db - 20 * np.log10(r)) / 20)

# ---------------- programa ----------------
def main():
    src, out = sys.argv[1], sys.argv[2]
    x, sr = leer_wav(src)
    assert sr == SR, f"esperaba {SR}, vino {sr}"

    x = pasa_altos(x, 118, 4)
    y, lam = suprimir(x)
    y = dereverb(y)
    y = deesser(y, 0.5)
    y = presencia(y, 1.4)          # menos filo: la presencia alta suena casual
    y = color_documental(y)

    N = int(TOTAL_S * SR)

    # CAMA DE SALA. Entre bloques el montaje quedaba en silencio digital
    # absoluto; el oido nota ese salto y lee el fondo de la voz como "ruido".
    # Con una cama constante al nivel del residuo, el fondo deja de aparecer y
    # desaparecer: simplemente esta. Se sintetiza con la forma espectral del
    # ruido real de la sala, no con ruido blanco.
    rng = np.random.default_rng(11)
    cama = rng.standard_normal(N)
    cama = pasa_bajos(pasa_altos(cama, 150, 2), 5200, 2)
    cama *= 10 ** (-62.0 / 20) / (np.sqrt(np.mean(cama ** 2)) + 1e-12)
    f0 = int(0.8 * SR)
    cama[:f0] *= np.linspace(0, 1, f0)
    cama[-f0:] *= np.linspace(1, 0, f0)
    pista = cama
    print("bloques:")
    for (a, b, dest, txt) in BLOQUES:
        seg = y[int(a * SR):int(b * SR)].copy()
        if len(seg) == 0:
            continue
        seg = estirar(seg, RITMO)      # cadencia documental
        seg = expansor(seg)
        seg = comprimir(seg, -22, 1.9) # menos compresión: comprimir de más
                                       # aplana la frase y suena a radio
        seg = normalizar_rms(seg, -22.5)
        # techo por bloque: la voz no debe pasar de -6 dBFS. Se aplica saturacion
        # suave, no recorte duro, para no ensuciar las consonantes.
        seg = np.tanh(seg * 2.0) / 2.0
        f = int(0.020 * SR)                       # fundidos de 20 ms
        seg[:f] *= np.linspace(0, 1, f)
        seg[-f:] *= np.linspace(1, 0, f)
        i0 = int(dest * SR)
        i1 = min(N, i0 + len(seg))
        pista[i0:i1] += seg[:i1 - i0]
        print("  %5.2f→%5.2f s  (%4.2f s)  %s" % (dest, dest + len(seg)/SR, len(seg)/SR, txt))

    pico = np.abs(pista).max()
    if pico > 0.89:
        pista *= 0.89 / pico
    escribir_wav(out, pista, SR)
    r = np.sqrt(np.mean(pista[pista != 0] ** 2))
    print("salida: %s  pico %.1f dBFS  RMS-voz %.1f dBFS"
          % (out, 20*np.log10(np.abs(pista).max()), 20*np.log10(r)))

if __name__ == "__main__":
    main()

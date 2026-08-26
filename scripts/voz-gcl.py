#!/usr/bin/env python3
"""
Locución de G.CL con voz sintética chilena — es-CL-LorenzoNeural (Microsoft).

Por qué existe este script aparte de procesa-vo-gcl.py:
  · La fuente es TTS, o sea NO tiene ruido de sala. Aplicarle la cadena de
    limpieza (supresión + cama de sala a -62 dBFS) solo AGREGA ruido. Feedback
    19-08: «tiene ruido de fondo». Acá no hay supresión ni cama: no hace falta.
  · Se genera UN ARCHIVO POR FRASE, así que las marcas del montaje se respetan
    al frame y no hay que detectar bloques por energía.

Tono documental: rate negativo (más lenta) + peso de pecho + poca compresión.
Ver la nota de `estirar()` en procesa-vo-gcl.py sobre por qué el ritmo importa
más que el timbre.

Uso:
  voz-gcl.py generar [--voz es-CL-LorenzoNeural] [--rate -10%]
  voz-gcl.py montar  <salida.wav>
  voz-gcl.py demo                  # una frase en varias voces, para elegir
"""
import asyncio, os, sys, wave, subprocess
import numpy as np

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


SR = 44100
TOTAL_S = 60.0
RAIZ = str(_RAIZ)
CRUDO = os.path.join(RAIZ, "gcl-agent/videos/vo/tts")
FF = os.path.join(RAIZ, "node_modules/@remotion/compositor-darwin-arm64/ffmpeg")

VOZ_DEF = "es-CL-LorenzoNeural"      # masculina chilena
RATE_DEF = "-10%"                    # cadencia documental
PITCH_DEF = "-3Hz"                   # apenas más asentada, sin engravecer

# (id, destino en el reel, texto)
FRASES = [
    ("01",  0.90, "Un lunes cualquiera."),
    ("02",  2.45, "Once de la noche."),
    ("03",  4.30, "Alguien dijo en voz alta lo que todos pensábamos."),
    ("04", 10.70, "Nadie creyó que fuera a existir."),
    ("05", 17.70, "Partió auditando tres años de campañas."),
    ("06", 23.20, "Encontró un patrón que estuvo siempre ahí."),
    ("07", 33.60, "Hoy trabaja al lado nuestro."),
    ("08", 38.30, "Ve lo mismo que tú."),
    ("09", 39.75, "Y lo que el ojo ya no alcanza."),
    ("10", 43.20, "Apagamos las luces."),
    ("11", 44.90, "Él no se apaga."),
    ("12", 47.70, "Pero no decide él."),
    ("13", 50.20, "Decidimos nosotros."),
    ("14", 51.95, "Con más criterio."),
]

# ---------------- generación ----------------
async def _gen(texto, salida, voz, rate, pitch):
    import edge_tts
    com = edge_tts.Communicate(texto, voz, rate=rate, pitch=pitch)
    await com.save(salida)

def generar(voz=VOZ_DEF, rate=RATE_DEF, pitch=PITCH_DEF):
    os.makedirs(CRUDO, exist_ok=True)
    for (i, _, texto) in FRASES:
        mp3 = os.path.join(CRUDO, f"{i}.mp3")
        asyncio.run(_gen(texto, mp3, voz, rate, pitch))
        wav = os.path.join(CRUDO, f"{i}.wav")
        subprocess.run([FF, "-v", "error", "-y", "-i", mp3, "-ac", "1",
                        "-ar", str(SR), "-c:a", "pcm_s16le", wav],
                       cwd=os.path.dirname(FF), check=True)
        print(f"  {i}  {os.path.getsize(mp3):>7} B  {texto}")
    print(f"voz {voz} · rate {rate} · pitch {pitch} -> {CRUDO}")

# ---------------- io ----------------
def leer(p):
    w = wave.open(p)
    x = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(np.float64) / 32768.0
    if w.getnchannels() == 2:
        x = x.reshape(-1, 2).mean(axis=1)
    return x

def escribir(p, x):
    w = wave.open(p, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()

# ---------------- filtros ----------------
def _f(x, curva):
    n = 1 << int(np.ceil(np.log2(len(x) + 1)))
    X = np.fft.rfft(x, n); f = np.fft.rfftfreq(n, 1 / SR)
    return np.fft.irfft(X * curva(f), n)[:len(x)]

def pa(x, fc, o=2): return _f(x, lambda f: ((f / fc) ** o) / (1 + (f / fc) ** o))
def pb(x, fc, o=2): return _f(x, lambda f: 1.0 / (1 + (f / fc) ** o))
def banda(x, a, b): return pb(pa(x, a), b)

# ---------------- cambio de tono ----------------
NFFT, HOP = 2048, 512
VENT = np.hanning(NFFT + 1)[:-1]

def _stft(x):
    n = 1 + max(0, (len(x) - NFFT)) // HOP
    if n < 3:
        return None
    idx = np.arange(NFFT)[None, :] + HOP * np.arange(n)[:, None]
    return np.fft.rfft(x[idx] * VENT, axis=1)

def _istft(S, largo):
    y = np.zeros(largo + NFFT); nrm = np.zeros(largo + NFFT)
    seg = np.fft.irfft(S, NFFT, axis=1) * VENT
    for i in range(S.shape[0]):
        y[i * HOP:i * HOP + NFFT] += seg[i]
        nrm[i * HOP:i * HOP + NFFT] += VENT ** 2
    nrm[nrm < 1e-8] = 1e-8
    return (y / nrm)[:largo]

def _estirar(x, factor):
    """Vocoder de fase: alarga sin tocar el tono."""
    S = _stft(x)
    if S is None:
        return x
    T, F = S.shape
    mag = np.abs(S); ph = np.angle(S)
    omega = 2 * np.pi * np.arange(F) * HOP / NFFT
    dphi = np.diff(ph, axis=0) - omega[None, :]
    dphi = np.mod(dphi + np.pi, 2 * np.pi) - np.pi
    frec = omega[None, :] + dphi
    t_new = np.arange(0, T - 1, 1.0 / factor)
    Y = np.empty((len(t_new), F), dtype=complex)
    acum = ph[0].copy()
    for i, tt in enumerate(t_new):
        i0 = int(tt); fr = tt - i0
        m = (1 - fr) * mag[i0] + fr * mag[min(i0 + 1, T - 1)]
        Y[i] = m * np.exp(1j * acum)
        acum = acum + frec[min(i0, T - 2)]
    return _istft(Y, int(len(x) * factor))

def bajar_tono(x, semitonos):
    """Baja el tono sin cambiar la duración.

    Receta estándar: se alarga con vocoder de fase por alfa = 2^(n/12) y después
    se remuestrea por el mismo alfa. La duración vuelve a la original y el tono
    queda multiplicado por alfa. Hacerlo al revés (remuestrear y estirar) mete más
    artefactos en las consonantes.
    """
    if semitonos <= 0:
        return x
    # OJO CON EL SIGNO: remuestrear con paso alfa acelera la reproducción, y
    # acelerar SUBE el tono. Para BAJAR n semitonos alfa tiene que ser < 1.
    # (Primera versión tenía 2**(n/12) y subía el tono: 134 Hz -> 169 Hz.)
    alfa = 2 ** (-semitonos / 12.0)
    y = _estirar(x, alfa)
    idx = np.arange(0, len(y) - 1, alfa)
    i0 = idx.astype(int); fr = idx - i0
    return y[i0] * (1 - fr) + y[i0 + 1] * fr


def color_documental(x):
    """+2,5 dB de cuerpo (170-340 Hz) y -2 dB de la banda 'conversada' (3-5,5k)."""
    cuerpo = banda(x, 170, 340)
    charla = banda(x, 3000, 5500)
    return x + cuerpo * (10 ** (2.5 / 20) - 1) - charla * (1 - 10 ** (-2.0 / 20))

def envolvente(x, ms_at=6, ms_rel=150):
    a1 = np.exp(-1.0 / (SR * ms_at / 1000.0)); a2 = np.exp(-1.0 / (SR * ms_rel / 1000.0))
    e = np.empty_like(x); y = 0.0; ax = np.abs(x)
    for i in range(len(x)):
        v = ax[i]; a = a1 if v > y else a2
        y = a * y + (1 - a) * v; e[i] = y
    return e

def comprimir(x, umbral_db=-22, razon=1.9):
    e = envolvente(x)
    exceso = np.maximum(20 * np.log10(e + 1e-9) - umbral_db, 0.0)
    return x * 10 ** (-exceso * (1 - 1 / razon) / 20)

def deesser(x, red=0.42):
    s = banda(x, 5200, 9000); cuerpo = banda(x, 300, 3000)
    r = np.clip((envolvente(s, 2, 40) / (envolvente(cuerpo, 2, 40) + 1e-6) - 0.30) / 0.5, 0, 1)
    return x - s * r * red

def normalizar(x, obj_db):
    return x * 10 ** ((obj_db - 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)) / 20)

def recortar_silencio(x, umbral_db=-48):
    """El TTS deja aire al principio y al final; se saca para que la frase caiga
    exactamente en su marca."""
    n = int(SR * 0.01)
    e = 20 * np.log10(np.sqrt(np.array([np.mean(x[i:i + n] ** 2) for i in range(0, len(x) - n, n)])) + 1e-12)
    act = np.where(e > umbral_db)[0]
    if len(act) == 0:
        return x
    a = max(0, (act[0] - 2)) * n
    b = min(len(x), (act[-1] + 3) * n)
    return x[a:b]

# ---------------- montaje ----------------
def montar(salida):
    N = int(TOTAL_S * SR)
    pista = np.zeros(N)
    print("montaje:")
    fin_prev = 0.0
    for (i, dest, texto) in FRASES:
        x = leer(os.path.join(CRUDO, f"{i}.wav"))
        x = recortar_silencio(x)
        x = pa(x, 95, 4)
        x = deesser(x)
        x = color_documental(x)
        x = comprimir(x)
        x = normalizar(x, -22.5)
        x = np.tanh(x * 2.0) / 2.0
        f = int(0.018 * SR)
        x[:f] *= np.linspace(0, 1, f); x[-f:] *= np.linspace(1, 0, f)
        i0 = int(dest * SR); i1 = min(N, i0 + len(x))
        pista[i0:i1] += x[:i1 - i0]
        fin = dest + len(x) / SR
        aviso = "  <-- SE PISA" if dest < fin_prev - 0.02 else ""
        print("  %s  %5.2f→%5.2f s (%4.2f s)  %s%s" % (i, dest, fin, len(x) / SR, texto, aviso))
        fin_prev = fin
    pico = np.abs(pista).max()
    if pico > 0.89:
        pista *= 0.89 / pico
    escribir(salida, pista)
    voz = pista[np.abs(pista) > 1e-4]
    print("salida: %s  pico %.1f dBFS  RMS-voz %.1f dBFS"
          % (salida, 20 * np.log10(np.abs(pista).max()), 20 * np.log10(np.sqrt(np.mean(voz ** 2)))))

# ---------------- montaje desde un archivo único ----------------
BLOQUES_FINAL = [
    # Locución definitiva: ElevenLabs, voz «Ignacio - Natural Chilean,
    # unhurried pace» (20-08-2026, 08:31). Masculina, 123 Hz de fundamental,
    # piso de ruido -63 dBFS. NO se le cambia el tono: los intentos de bajarlo
    # con vocoder sonaban raros.
    # 13 bloques para 14 frases: ElevenLabs unió «Ve lo mismo que tú» con «Y lo
    # que el ojo ya no alcanza», que es exactamente lo que pedía la dirección
    # («seguido, sin respirar»). Calce verificado por núcleos silábicos.
    # (inicio_src, fin_src, destino_reel, texto)
    (2.30,  3.46,  0.90, "Un lunes cualquiera."),
    (4.00,  4.96,  2.45, "Once de la noche."),
    (5.92,  8.82,  4.30, "Alguien dijo en voz alta lo que todos pensábamos."),
    (9.44, 11.48, 10.70, "Nadie creyó que fuera a existir."),
    (12.40, 15.42, 17.70, "Partió auditando tres años de campañas."),
    (15.82, 18.14, 23.20, "Encontró un patrón que estuvo siempre ahí."),
    (19.00, 20.72, 33.60, "Hoy trabaja al lado nuestro."),
    (21.10, 24.22, 38.30, "Ve lo mismo que tú / Y lo que el ojo ya no alcanza."),
    (24.82, 26.18, 43.20, "Apagamos las luces."),
    (26.30, 27.50, 44.85, "Él no se apaga."),
    (28.66, 30.08, 47.70, "Pero no decide él."),
    (30.46, 31.76, 50.20, "Decidimos nosotros."),
    (32.00, 33.24, 51.70, "Con más criterio."),
]

# ---------------- generación ----------------
async def _gen(texto, salida, voz, rate, pitch):
    import edge_tts
    com = edge_tts.Communicate(texto, voz, rate=rate, pitch=pitch)
    await com.save(salida)

def generar(voz=VOZ_DEF, rate=RATE_DEF, pitch=PITCH_DEF):
    os.makedirs(CRUDO, exist_ok=True)
    for (i, _, texto) in FRASES:
        mp3 = os.path.join(CRUDO, f"{i}.mp3")
        asyncio.run(_gen(texto, mp3, voz, rate, pitch))
        wav = os.path.join(CRUDO, f"{i}.wav")
        subprocess.run([FF, "-v", "error", "-y", "-i", mp3, "-ac", "1",
                        "-ar", str(SR), "-c:a", "pcm_s16le", wav],
                       cwd=os.path.dirname(FF), check=True)
        print(f"  {i}  {os.path.getsize(mp3):>7} B  {texto}")
    print(f"voz {voz} · rate {rate} · pitch {pitch} -> {CRUDO}")

# ---------------- io ----------------
def leer(p):
    w = wave.open(p)
    x = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(np.float64) / 32768.0
    if w.getnchannels() == 2:
        x = x.reshape(-1, 2).mean(axis=1)
    return x

def escribir(p, x):
    w = wave.open(p, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()

# ---------------- filtros ----------------
def _f(x, curva):
    n = 1 << int(np.ceil(np.log2(len(x) + 1)))
    X = np.fft.rfft(x, n); f = np.fft.rfftfreq(n, 1 / SR)
    return np.fft.irfft(X * curva(f), n)[:len(x)]

def pa(x, fc, o=2): return _f(x, lambda f: ((f / fc) ** o) / (1 + (f / fc) ** o))
def pb(x, fc, o=2): return _f(x, lambda f: 1.0 / (1 + (f / fc) ** o))
def banda(x, a, b): return pb(pa(x, a), b)

# ---------------- cambio de tono ----------------
NFFT, HOP = 2048, 512
VENT = np.hanning(NFFT + 1)[:-1]

def _stft(x):
    n = 1 + max(0, (len(x) - NFFT)) // HOP
    if n < 3:
        return None
    idx = np.arange(NFFT)[None, :] + HOP * np.arange(n)[:, None]
    return np.fft.rfft(x[idx] * VENT, axis=1)

def _istft(S, largo):
    y = np.zeros(largo + NFFT); nrm = np.zeros(largo + NFFT)
    seg = np.fft.irfft(S, NFFT, axis=1) * VENT
    for i in range(S.shape[0]):
        y[i * HOP:i * HOP + NFFT] += seg[i]
        nrm[i * HOP:i * HOP + NFFT] += VENT ** 2
    nrm[nrm < 1e-8] = 1e-8
    return (y / nrm)[:largo]

def _estirar(x, factor):
    """Vocoder de fase: alarga sin tocar el tono."""
    S = _stft(x)
    if S is None:
        return x
    T, F = S.shape
    mag = np.abs(S); ph = np.angle(S)
    omega = 2 * np.pi * np.arange(F) * HOP / NFFT
    dphi = np.diff(ph, axis=0) - omega[None, :]
    dphi = np.mod(dphi + np.pi, 2 * np.pi) - np.pi
    frec = omega[None, :] + dphi
    t_new = np.arange(0, T - 1, 1.0 / factor)
    Y = np.empty((len(t_new), F), dtype=complex)
    acum = ph[0].copy()
    for i, tt in enumerate(t_new):
        i0 = int(tt); fr = tt - i0
        m = (1 - fr) * mag[i0] + fr * mag[min(i0 + 1, T - 1)]
        Y[i] = m * np.exp(1j * acum)
        acum = acum + frec[min(i0, T - 2)]
    return _istft(Y, int(len(x) * factor))

def bajar_tono(x, semitonos):
    """Baja el tono sin cambiar la duración.

    Receta estándar: se alarga con vocoder de fase por alfa = 2^(n/12) y después
    se remuestrea por el mismo alfa. La duración vuelve a la original y el tono
    queda multiplicado por alfa. Hacerlo al revés (remuestrear y estirar) mete más
    artefactos en las consonantes.
    """
    if semitonos <= 0:
        return x
    # OJO CON EL SIGNO: remuestrear con paso alfa acelera la reproducción, y
    # acelerar SUBE el tono. Para BAJAR n semitonos alfa tiene que ser < 1.
    # (Primera versión tenía 2**(n/12) y subía el tono: 134 Hz -> 169 Hz.)
    alfa = 2 ** (-semitonos / 12.0)
    y = _estirar(x, alfa)
    idx = np.arange(0, len(y) - 1, alfa)
    i0 = idx.astype(int); fr = idx - i0
    return y[i0] * (1 - fr) + y[i0 + 1] * fr


def color_documental(x):
    """+2,5 dB de cuerpo (170-340 Hz) y -2 dB de la banda 'conversada' (3-5,5k)."""
    cuerpo = banda(x, 170, 340)
    charla = banda(x, 3000, 5500)
    return x + cuerpo * (10 ** (2.5 / 20) - 1) - charla * (1 - 10 ** (-2.0 / 20))

def envolvente(x, ms_at=6, ms_rel=150):
    a1 = np.exp(-1.0 / (SR * ms_at / 1000.0)); a2 = np.exp(-1.0 / (SR * ms_rel / 1000.0))
    e = np.empty_like(x); y = 0.0; ax = np.abs(x)
    for i in range(len(x)):
        v = ax[i]; a = a1 if v > y else a2
        y = a * y + (1 - a) * v; e[i] = y
    return e

def comprimir(x, umbral_db=-22, razon=1.9):
    e = envolvente(x)
    exceso = np.maximum(20 * np.log10(e + 1e-9) - umbral_db, 0.0)
    return x * 10 ** (-exceso * (1 - 1 / razon) / 20)

def deesser(x, red=0.42):
    s = banda(x, 5200, 9000); cuerpo = banda(x, 300, 3000)
    r = np.clip((envolvente(s, 2, 40) / (envolvente(cuerpo, 2, 40) + 1e-6) - 0.30) / 0.5, 0, 1)
    return x - s * r * red

def normalizar(x, obj_db):
    return x * 10 ** ((obj_db - 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)) / 20)

def recortar_silencio(x, umbral_db=-48):
    """El TTS deja aire al principio y al final; se saca para que la frase caiga
    exactamente en su marca."""
    n = int(SR * 0.01)
    e = 20 * np.log10(np.sqrt(np.array([np.mean(x[i:i + n] ** 2) for i in range(0, len(x) - n, n)])) + 1e-12)
    act = np.where(e > umbral_db)[0]
    if len(act) == 0:
        return x
    a = max(0, (act[0] - 2)) * n
    b = min(len(x), (act[-1] + 3) * n)
    return x[a:b]

# ---------------- montaje ----------------
def montar(salida):
    N = int(TOTAL_S * SR)
    pista = np.zeros(N)
    print("montaje:")
    fin_prev = 0.0
    for (i, dest, texto) in FRASES:
        x = leer(os.path.join(CRUDO, f"{i}.wav"))
        x = recortar_silencio(x)
        x = pa(x, 95, 4)
        x = deesser(x)
        x = color_documental(x)
        x = comprimir(x)
        x = normalizar(x, -22.5)
        x = np.tanh(x * 2.0) / 2.0
        f = int(0.018 * SR)
        x[:f] *= np.linspace(0, 1, f); x[-f:] *= np.linspace(1, 0, f)
        i0 = int(dest * SR); i1 = min(N, i0 + len(x))
        pista[i0:i1] += x[:i1 - i0]
        fin = dest + len(x) / SR
        aviso = "  <-- SE PISA" if dest < fin_prev - 0.02 else ""
        print("  %s  %5.2f→%5.2f s (%4.2f s)  %s%s" % (i, dest, fin, len(x) / SR, texto, aviso))
        fin_prev = fin
    pico = np.abs(pista).max()
    if pico > 0.89:
        pista *= 0.89 / pico
    escribir(salida, pista)
    voz = pista[np.abs(pista) > 1e-4]
    print("salida: %s  pico %.1f dBFS  RMS-voz %.1f dBFS"
          % (salida, 20 * np.log10(np.abs(pista).max()), 20 * np.log10(np.sqrt(np.mean(voz ** 2)))))

def montar_archivo(origen_wav, salida, semitonos=0.0):
    x = leer(origen_wav)
    N = int(TOTAL_S * SR)
    pista = np.zeros(N)
    print("montaje desde archivo único:")
    fin_prev = 0.0
    for (a, b, dest, texto) in BLOQUES_FINAL:
        seg = recortar_silencio(x[int(a * SR):int(b * SR)], -52)
        seg = bajar_tono(seg, semitonos)
        seg = pa(seg, 95, 4)
        seg = deesser(seg)
        seg = color_documental(seg)
        seg = comprimir(seg)
        seg = normalizar(seg, -20.5)
        seg = np.tanh(seg * 2.0) / 2.0
        f = int(0.018 * SR)
        seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
        i0 = int(dest * SR); i1 = min(N, i0 + len(seg))
        pista[i0:i1] += seg[:i1 - i0]
        fin = dest + len(seg) / SR
        print("  %5.2f→%5.2f s (%4.2f s)  %s%s" % (dest, fin, len(seg) / SR, texto,
              "  <-- SE PISA" if dest < fin_prev - 0.02 else ""))
        fin_prev = fin
    pico = np.abs(pista).max()
    if pico > 0.89:
        pista *= 0.89 / pico
    escribir(salida, pista)
    voz = pista[np.abs(pista) > 1e-4]
    print("salida: %s  pico %.1f dBFS  RMS-voz %.1f dBFS  ·  cierre de marca entra en 53,5 s"
          % (salida, 20 * np.log10(np.abs(pista).max()), 20 * np.log10(np.sqrt(np.mean(voz ** 2)))))


# ---------------- demo de voces ----------------
DEMO = ("Partió auditando tres años de campañas. "
        "Encontró un patrón que estuvo siempre ahí.")
CANDIDATAS = [
    ("es-CL-LorenzoNeural", "-10%", "-3Hz",  "chileno"),
    ("es-CL-LorenzoNeural", "-18%", "-8Hz",  "chileno mas lento y asentado"),
    ("es-MX-JorgeNeural",   "-10%", "-3Hz",  "neutro latino"),
    ("es-PE-AlexNeural",    "-10%", "-3Hz",  "peruano"),
    ("es-UY-MateoNeural",   "-10%", "-3Hz",  "uruguayo"),
    ("es-ES-AlvaroNeural",  "-10%", "-3Hz",  "peninsular"),
]

def demo():
    dest = os.path.join(RAIZ, "gcl-agent/videos/vo/demo")
    os.makedirs(dest, exist_ok=True)
    for k, (voz, rate, pitch, nota) in enumerate(CANDIDATAS, 1):
        o = os.path.join(dest, f"{k}_{voz}_{rate.replace('%','pc').replace('-','m')}.mp3")
        asyncio.run(_gen(DEMO, o, voz, rate, pitch))
        print("  %d. %-22s rate %-5s pitch %-5s  %s" % (k, voz, rate, pitch, nota))
    print("->", dest)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "demo"
    if cmd == "generar":
        generar(*(sys.argv[2:5] or [VOZ_DEF, RATE_DEF, PITCH_DEF]))
    elif cmd == "montar":
        montar(sys.argv[2])
    elif cmd == "montar-archivo":
        montar_archivo(sys.argv[2], sys.argv[3],
                       float(sys.argv[4]) if len(sys.argv) > 4 else 0.0)
    else:
        demo()

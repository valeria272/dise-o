#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Story animada Click 07/10 — la mezcla: música original de julio + locución.

Ronda 3 · 24-09-2026, Paulina: «necesito que lleve música como las referencias y que
hable lo que va diciendo en pantalla con una voz masculina agradable de aprox 30
años, comercial pero no exagerada».

⛔ 1er intento RECHAZADO («quedó súper mal»):
  · se usó como música el audio de `storie_click_jun.mp4`, que trae la LOCUCIÓN de
    julio mezclada. Un análisis por bandas no la detectó: nunca sacar una «pista
    musical» de un video terminado.
  · voz «Andre» (preset de ElevenLabs vía Higgsfield): «como una persona de habla
    inglesa tratando de hablar en español». Los presets de Higgsfield son todos de
    habla inglesa.
Ahora:
· LOCUCIÓN: `es-CL-LorenzoNeural` (Microsoft, edge-tts), nativa chilena, elegida por
  Paulina entre 4 voces nativas (voz/pruebas2/). Texto literal de pantalla; «24/7» se
  escribe «veinticuatro siete». Sin estirar ni acelerar.
  ⛔ La neutra sonó «triste y seria» y decía «jitcar». Paulina: «no apures lo que dice,
  enfatiza el entusiasmo». Ahora: velocidad normal, tono +11 Hz, volumen +8 %, frases
  con «¡…!» (la entonación sube sin hablar más rápido) y «gift card» escrito
  «guift kard» (elegido entre 3 grafías, voz/pruebas3/). Generador: ver voz/generar.py.
· MÚSICA: `audio_fondo3.mp3` de Paulina (Drive EBEMA/2-referencias/musica, una de 3
  pistas de fondo), guardada acá como `musica_original.mp3`. Paulina: «úsala desde el
  segundo 00:08, siempre con un volumen moderado para que no sobrepase la voz».
· MEZCLA: sin ducking que siga a la voz; hueco de EQ FIJO −6,5 dB 300 Hz–3,5 kHz en
  la música, que va 13 dB bajo la voz. A la voz sintética no se le limpia ruido.

Salida: mezcla.wav (48 kHz estéreo), que se une al video con ffmpeg.
"""
import os
import subprocess
import sys
import wave

import imageio_ffmpeg
import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", "..", ".."))
FF = imageio_ffmpeg.get_ffmpeg_exe()
SR = 48000
FPS = 30
import glob
MUSICA = (glob.glob(os.path.join(AQUI, "musica_original.*")) or [None])[0]

# (archivo, cuadro del video donde ARRANCA la voz). Tiene que calzar con la línea de
# tiempo de EbemaGrillaStoryClickOct.tsx (VOZ_EN).
LINEAS = [("voz/t1.mp3", 8), ("voz/t2.mp3", 116), ("voz/t3.mp3", 244),
          ("voz/t4.mp3", 432), ("voz/t5.mp3", 556)]
DURACION = 624 / FPS
# 15 dB quedó «demasiado baja, apenas se escucha» (Paulina, 24-09). 8 dB: presente,
# sin tapar la voz («volumen moderado para que no sobrepase la voz»).
SEPARACION_DB = 8.0
DESDE = 8.0            # s de la pista donde arranca (lo pidió Paulina)


def lee(ruta, canales):
    crudo = subprocess.run([FF, "-v", "error", "-i", ruta, "-vn", "-f", "f32le", "-ac", str(canales),
                            "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(crudo, np.float32).reshape(-1, canales).astype(np.float64)


def eq_hueco(x, f0=300, f1=3500, db=-6.5):
    """Hueco FIJO en la banda de la voz (FFT de toda la pista, sin bombeo)."""
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.ones_like(f)
    banda = (f >= f0) & (f <= f1)
    g[banda] = 10 ** (db / 20)
    # bordes suaves de media octava
    for a, b in ((f0 / 1.41, f0), (f1, f1 * 1.41)):
        m = (f > a) & (f < b)
        t = np.log(f[m] / a) / np.log(b / a)
        g[m] = 10 ** (db / 20 * (t if a < f0 else 1 - t))
    return np.fft.irfft(X * g[:, None], n=len(x), axis=0)


def pasa_altos(x, fc=90):
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** 4)
    return np.fft.irfft(X * g[:, None], n=len(x), axis=0)


def rms_db(x):
    return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)


def extiende(m, objetivo):
    """Repite un tramo del medio para llegar a `objetivo` s. El empalme se busca por
    parecido de envolvente espectral entre la toma original y la repetida."""
    falta = objetivo - len(m) / SR
    mono = m.mean(1)
    # periodo de negra por autocorrelación de la envolvente de ataques
    hop = 512
    e = np.array([np.sqrt(np.mean(mono[i:i + 1024] ** 2)) for i in range(0, len(mono) - 1024, hop)])
    on = np.maximum(np.diff(e), 0)
    ac = np.correlate(on - on.mean(), on - on.mean(), "full")[len(on) - 1:]
    lags = np.arange(len(ac)) * hop / SR
    v = (lags > 0.55) & (lags < 0.85)
    negra = lags[v][np.argmax(ac[v])]
    compases = max(1, round(falta / (4 * negra)))
    L = int(round(compases * 4 * negra * SR))
    mejor, t1 = None, None
    win = int(0.25 * SR)
    for s in np.arange(6.0, 12.0, 0.01):
        a = int(s * SR)
        A = np.abs(np.fft.rfft(mono[a:a + win]))
        B = np.abs(np.fft.rfft(mono[a - L:a - L + win]))
        d = np.linalg.norm(np.log1p(A) - np.log1p(B))
        if mejor is None or d < mejor:
            mejor, t1 = d, a
    xf = int(0.04 * SR)
    rampa = np.linspace(0, 1, xf)[:, None]
    cola = m[t1 - L:].copy()
    cola[:xf] = m[t1:t1 + xf] * (1 - rampa) + cola[:xf] * rampa
    out = np.concatenate([m[:t1], cola])
    print(f"  música: negra {negra:.3f} s ({60 / negra:.1f} BPM) · repite {compases} compases "
          f"({L / SR:.2f} s) empalmando en {t1 / SR:.2f} s → {len(out) / SR:.2f} s")
    return out


def main():
    if not MUSICA:
        sys.exit("✗ falta musica_original.* (la pista de julio que pasa Paulina)")
    musica = lee(MUSICA, 2)[int(DESDE * SR):]
    ini = int(0.15 * SR)                      # arranca a mitad de pista: sin clic
    musica[:ini] *= np.linspace(0, 1, ini)[:, None]
    if len(musica) / SR < DURACION:
        musica = extiende(musica, DURACION)
    n = int(round(DURACION * SR))
    musica = np.pad(musica, ((0, max(0, n - len(musica))), (0, 0)))[:n]
    # cola: fundido de 0,6 s al final del video
    fin = int(0.6 * SR)
    musica[-fin:] *= np.linspace(1, 0, fin)[:, None]
    musica = eq_hueco(musica)

    voz = np.zeros((n, 2))
    for ruta, cuadro in LINEAS:
        v = pasa_altos(lee(os.path.join(AQUI, ruta), 1))
        a = int(round(cuadro / FPS * SR))
        b = min(n, a + len(v))
        voz[a:b] += v[: b - a]              # mono al centro
    activo = np.abs(voz[:, 0]) > 1e-3
    nivel_voz = rms_db(voz[activo])
    # voz a −17 dBFS RMS mientras habla, música 13 dB abajo
    voz *= 10 ** ((-17 - nivel_voz) / 20)
    musica *= 10 ** ((-17 - SEPARACION_DB - rms_db(musica)) / 20)
    mezcla = voz + musica
    pico = np.abs(mezcla).max()
    if pico > 0.89:
        mezcla *= 0.89 / pico
    guarda(os.path.join(AQUI, "mezcla.wav"), mezcla)
    print(f"✓ mezcla.wav · {n / SR:.2f} s · voz {rms_db(mezcla[activo]):.1f} dBFS · "
          f"música sola {rms_db(mezcla[~activo]):.1f} dBFS · pico {20 * np.log10(np.abs(mezcla).max()):.1f} dBFS")


def guarda(ruta, x):
    x16 = (np.clip(x, -1, 1) * 32767).astype("<i2")
    tmp = ruta + ".tmp"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(x.shape[1])
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(x16.tobytes())
    os.replace(tmp, ruta)


if __name__ == "__main__":
    main()

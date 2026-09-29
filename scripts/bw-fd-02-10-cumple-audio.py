"""BETWEEN · FEED 02-10 REEL CUMPLEAÑOS — mezcla de audio y montaje final.

Eli, 29-09: música en tendencia y un sonido que acompañe CADA texto que aparece
(hooks sonoros). La música (ElevenLabs Music v2) y los efectos (ElevenLabs SFX)
salen de Magnific y viven en `raw/hilton/between/oct/audio-f02/`.

Los golpes caen en el mismo fotograma que en `BetweenFeed0210Cumple.tsx` (TIEMPOS):
  pop en «¿ESTÁS», plumón en cada manuscrita, tecla en cada letra de la máquina de
  escribir (1 de cada 2 cuando teclea rápido, para que no metralle), destello cuando
  se dibujan los rayos de la vela y un whoosh suave en cada cambio de escena.
Reglas de [[audio-y-post-de-reels]]: nada de ruido continuo ni ducking que bombee;
la música va pareja, con un hueco fijo de EQ para que los efectos se oigan.

    py scripts/bw-fd-02-10-cumple-audio.py
"""
import os
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = Path(__file__).resolve().parent.parent
A = RAIZ / "raw/hilton/between/oct/audio-f02"
CUADROS = RAIZ / os.environ.get("BW_F02_CUADROS", "raw/_reel-chrome/f02")  # ronda 4: raw/_reel-chrome/f02-r4
OUT = RAIZ / os.environ.get("BW_F02_OUT", "out/hilton/between/oct-r2")
NOMBRE = "BW FEED 02-10 Cafe de cumpleanos"
FF = r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
SR, FPS, N = 48000, 30, 375
DUR = N / FPS


def leer(nombre, recortar=True):
    with wave.open(str(A / f"{nombre}.wav")) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, 2).astype(np.float32) / 32768
    if recortar:  # el golpe tiene que caer justo en el fotograma: fuera el silencio del comienzo
        umbral = np.abs(x).max() * 0.08
        x = x[max(0, int(np.argmax(np.abs(x).max(1) > umbral)) - 48):]
    return x / (np.abs(x).max() + 1e-9)


pista = np.zeros((int(DUR * SR) + SR, 2), np.float32)


def poner(x, cuadro, gan):
    i = int(cuadro / FPS * SR)
    if i < 0:  # arranca antes del cuadro 0: se oye sólo la cola
        x, i = x[-i:], 0
    j = min(len(pista), i + len(x))
    pista[i:j] += x[: j - i] * gan


teclas = [leer(f"tecla{k}") for k in (1, 2, 3)]
for k, t in enumerate(teclas):  # sólo el golpe: 90 ms con cola corta
    n = int(0.09 * SR)
    teclas[k] = t[:n] * np.linspace(1, 0, n)[:, None] ** 2


def tecleo(texto, desde, por_letra, gan=0.46, cada=1):
    letras = [i for i, ch in enumerate(texto) if ch != " "]
    for k, i in enumerate(letras[::cada]):
        poner(teclas[k % 3], desde + i * por_letra, gan * (0.85 + 0.3 * ((k * 7) % 5) / 4))


pop, plumon, brillo = leer("pop1"), leer("plumon"), leer("brillo")
whoosh = leer("whoosh2")

# TIEMPOS de la composición
# ronda 3: la vela se enciende AL INICIO (el hook). El raspado del fósforo termina en f4
poner(leer("fosforo"), -18, 0.60)
poner(pop, 12, 0.55)                      # ¿ESTÁS
poner(plumon, 20, 0.30)                   # de
tecleo("CUMPLEAÑOS?", 28, 2.3)
poner(whoosh, 67, 0.28)                   # sale el hook
tecleo("EL CAFÉ", 80, 2.4)
poner(plumon, 98, 0.30)                   # va por
tecleo("NUESTRA CUENTA", 112, 2.2)
pop2 = leer("pop2")
poner(pop2, 120, 0.26)                    # surgen los globos (ronda 2: ilustraciones de Eli)
poner(whoosh, 157, 0.28)                  # sale «nuestra cuenta»
tecleo("Ven por tu", 170, 2.2)
poner(pop2, 178, 0.22)                    # surge el globo de la derecha
poner(plumon, 194, 0.30)                  # café gratis
tecleo("el día de tu cumpleaños", 210, 1.3, cada=2)
poner(brillo, 262, 0.32)                  # se abre el confeti desde la llama
for k in range(5):                        # cada botón del legal
    poner(pop, 268 + 6 * k, 0.20 + 0.03 * (k % 2))

# música: pareja, sin ducking; fundido de 0,8 s al final
musica = leer("musica", recortar=False)[: len(pista)]
env = np.ones(len(musica), np.float32)
fin = int(DUR * SR)
env[fin - int(0.8 * SR): fin] = np.linspace(1, 0, int(0.8 * SR))
env[fin:] = 0
env[: int(0.03 * SR)] = np.linspace(0, 1, int(0.03 * SR))
tmp_m = A / "_musica_env.wav"
tmp_s = A / "_efectos.wav"


def escribir(ruta, x):
    x = np.clip(x, -1, 1)
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


escribir(tmp_m, musica * env[:, None] * 0.9)
escribir(tmp_s, pista[: fin])

OUT.mkdir(parents=True, exist_ok=True)
mp4 = OUT / f"{NOMBRE}.mp4"
# hueco fijo de EQ en la música (−4,5 dB 300 Hz–3,5 kHz) + suma + loudnorm a −14 LUFS
filtro = ("[1:a]equalizer=f=1000:t=h:w=3200:g=-4.5,volume=0.62[m];"
          "[2:a]volume=1.0[s];[m][s]amix=inputs=2:normalize=0,"
          "loudnorm=I=-14:TP=-1.5:LRA=9[a]")
subprocess.run([FF, "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(CUADROS / "f%04d.png"),
                "-i", str(tmp_m), "-i", str(tmp_s), "-filter_complex", filtro,
                "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "slow", "-crf", "16",
                "-pix_fmt", "yuv420p", "-profile:v", "high", "-movflags", "+faststart",
                "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{DUR:.3f}", str(mp4)], check=True)
# GIF (Eli lo sube a la grilla): 25 fps, 540×960, paleta propia y sin difuminado
gif = OUT / f"{NOMBRE}.gif"
subprocess.run([FF, "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(CUADROS / "f%04d.png"),
                "-vf", "fps=25,scale=540:960:flags=lanczos,split[a][b];[a]palettegen=max_colors=256:stats_mode=full[p];"
                       "[b][p]paletteuse=dither=none", str(gif)], check=True)
# portada = el último cuadro, que junta toda la información
subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(CUADROS / f"f{N - 1:04d}.png"),
                str(OUT / f"{NOMBRE} - PORTADA.png")], check=True)
for f in (mp4, gif, OUT / f"{NOMBRE} - PORTADA.png"):
    print("✓", f.relative_to(RAIZ), f"{f.stat().st_size / 1e6:.1f} MB")

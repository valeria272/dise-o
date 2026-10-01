"""BETWEEN · FEED 02-10 REEL CUMPLEAÑOS — alarga la música aprobada sin cambiarla.

Ronda 11 (01-10): el reel pasa de 12,5 a 16,5 s para que se alcance a leer todo (hilo de Nicolás)
y `musica.wav` dura 14,0 s. En vez de generar otra pista (la aprobada por Eli es ésta), se repite
un tramo de compases enteros: se busca el desfase L (2,6–6 s) y el punto t donde la pista se
parece más a sí misma L segundos después, y se empalma `musica[:t+L] + musica[t:]` con un cruce
de 40 ms. Imprime la correlación del empalme: bajo ~0,6 se oye el salto y conviene otra salida.

    py scripts/bw-fd-02-10-cumple-musica-larga.py   →  raw/hilton/between/oct/audio-f02/musica-larga.wav
"""
import wave
from pathlib import Path

import numpy as np

A = Path(__file__).resolve().parent.parent / "raw/hilton/between/oct/audio-f02"
with wave.open(str(A / "musica.wav")) as w:
    SR = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, 2).astype(np.float32) / 32768
m = x.mean(1)
# espectrograma grueso (ventanas de 46 ms, paso 11,6 ms): la forma del sonido, no la fase
N, H = 2048, 512
cuadros = np.lib.stride_tricks.sliding_window_view(m, N)[::H] * np.hanning(N)
E = np.log1p(np.abs(np.fft.rfft(cuadros, axis=1))[:, :400] * 50)
E = (E - E.mean(1, keepdims=True)) / (E.std(1, keepdims=True) + 1e-6)
paso = H / SR
VEN = int(1.5 / paso)  # se comparan 1,5 s después del empalme
mejor = (-1, 0, 0)
for L in range(int(2.6 / paso), int(6.0 / paso)):
    for t in range(int(1.0 / paso), len(E) - L - VEN - int(1.5 / paso), 2):
        c = float((E[t:t + VEN] * E[t + L:t + L + VEN]).mean())
        if c > mejor[0]:
            mejor = (c, t, L)
c, t, L = mejor
print(f"empalme: t = {t * paso:.2f} s · tramo repetido L = {L * paso:.2f} s · parecido {c:.2f}")
# afinar a la muestra: máxima correlación de la onda en ±25 ms
i, j = int(t * H), int((t + L) * H)
v = int(0.2 * SR)
k = max(range(-int(0.025 * SR), int(0.025 * SR), 4),
        key=lambda d: float(np.dot(m[i:i + v], m[j + d:j + d + v])))
j += k
r = float(np.corrcoef(m[i:i + v], m[j:j + v])[0, 1])
print(f"onda en el empalme: r = {r:.2f}")
X = int(0.04 * SR)
rampa = np.linspace(0, 1, X)[:, None]
larga = np.concatenate([x[:j], x[j:j + X] * (1 - rampa) + x[i:i + X] * rampa, x[i + X:]])
with wave.open(str(A / "musica-larga.wav"), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(larga, -1, 1) * 32767).astype(np.int16).tobytes())
print(f"musica-larga.wav: {len(larga) / SR:.2f} s (antes {len(x) / SR:.2f} s)")

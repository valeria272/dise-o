#!/usr/bin/env python3
"""Tierra Calma — ¿dos pistas del prompt corporativo salieron CLONADAS? (R-33)

    python scripts/tc-musica-parecido.py nueva.mp3 [otra.mp3 ...]

Compara la primera pista contra las demás (por defecto, las `mus_corporativa_*`
ya instaladas). No se detecta escuchando por encima ni con md5: se mide la
EVOLUCIÓN DEL ARREGLO — energía por banda de frecuencia cada 0,25 s, normalizada
por banda — y se correlaciona alineada desde el inicio.

Escala de ESTE script, medida el 01-10-2026 sobre pistas de la cuenta:
    dos pistas realmente distintas (corporativa_a · corporativa_b)   −0,09
    una pista contra un clon de arreglo (corporativa_c · _a)         +0,56
⚠️ No es la escala del manual § 8 (allá el control era +0,53 con otra huella):
los números no se comparan entre sí, sólo dentro de este script.
Sobre +0,35 conviene volver a tirar la pista con el MISMO prompt.
"""
import pathlib, subprocess, sys, tempfile, wave
import numpy as np

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FF = RAIZ / ("node_modules/.bin/remotion" + (".cmd" if sys.platform == "win32" else ""))

def lee(p):
    with tempfile.TemporaryDirectory() as t:
        w = pathlib.Path(t) / "a.wav"
        subprocess.run([str(FF), "ffmpeg", "-y", "-loglevel", "error", "-i", str(p), "-ac", "1", "-ar", "16000", str(w)], check=True)
        # En Windows el directorio temporal no se puede borrar con el wav abierto.
        with wave.open(str(w)) as f:
            a = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16).astype(float) / 32768
            sr = f.getframerate()
        return a, sr

def huella(x, sr, bandas=8, paso=0.25):
    n = int(paso * sr); M = []
    ed = np.logspace(np.log10(60), np.log10(sr / 2), bandas + 1) * n / sr
    for i in range(len(x) // n):
        s = np.abs(np.fft.rfft(x[i * n:(i + 1) * n] * np.hanning(n))) ** 2
        M.append([s[int(ed[j]):int(ed[j + 1])].sum() + 1e-12 for j in range(bandas)])
    M = np.log(np.array(M)); return (M - M.mean(0)) / (M.std(0) + 1e-9)

def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    nueva = pathlib.Path(sys.argv[1])
    otras = [pathlib.Path(p) for p in sys.argv[2:]] or sorted(
        p for p in (RAIZ / "public/assets/tierracalma/audio").glob("mus_corporativa_*.mp3") if p.resolve() != nueva.resolve())
    a, sr = lee(nueva); ha = huella(a, sr)
    seg = [round(20 * np.log10(np.sqrt((a[int(t * sr):int((t + 1) * sr)] ** 2).mean()) + 1e-9)) for t in range(int(len(a) / sr))]
    fin = max(i for i, v in enumerate(seg) if v > -40) + 1
    print(f"{nueva.name}: {len(a) / sr:.1f} s · la música suena hasta el segundo {fin}")
    peor = 0.0
    for o in otras:
        b, _ = lee(o); hb = huella(b, sr); k = min(len(ha), len(hb)); r = float((ha[:k] * hb[:k]).mean()); peor = max(peor, r)
        print(f"  vs {o.name:26s} {r:+.2f} {'⛔ clon de arreglo' if r > 0.35 else '✓'}")
    return 1 if peor > 0.35 else 0

if __name__ == "__main__":
    raise SystemExit(main())

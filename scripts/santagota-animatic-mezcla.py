"""SANTA GOTA · animatic — mezcla de audio y mux sobre el render.

Sound design (temporal) alineado por ONSET: cada efecto se coloca de modo que su primer transitorio caiga en el
timecode del montaje (no el inicio del archivo). Dos salidas: con cama musical temporal y sin música (la de TV).

Uso: python3 scripts/santagota-animatic-mezcla.py <render.mp4> <carpeta_salida>
"""
import os, subprocess, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ

FF = str(RAIZ / "tools/ffmpeg")
AU = RAIZ / "public/assets/santagota/spot/audio"
SR = 48000
MUSICA = os.environ.get("SG_MUSICA", "musica-v3")
DUR = 599 / 29.97


def carga(nombre):
    """mp3 → float32 estéreo 48 k, NORMALIZADO a pico 1,0 (los generados llegan entre 0,01 y 1,4 de pico:
    sin esto las ganancias no significan nada — el pushin era inaudible y el click reventaba)."""
    raw = subprocess.run([FF, "-v", "error", "-i", str(AU / f"{nombre}.mp3"), "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()
    pico = np.abs(x).max()
    return x / pico if pico > 0 else x


def onset(x, umbral=0.25):
    """Primer instante con energía ≥ umbral del pico (ventana de 5 ms)."""
    v = np.abs(x).max(axis=1)
    n = int(SR * 0.005)
    env = np.convolve(v, np.ones(n) / n, mode="same")
    i = np.argmax(env >= umbral * env.max())
    return i / SR


def db(g):
    return 10 ** (g / 20)


def envolvente(n, fin_in, fin_out, total):
    e = np.ones(n, dtype=np.float32)
    a = int(fin_in * SR); b = int(fin_out * SR)
    if a > 0: e[:a] = np.linspace(0, 1, a)
    if b > 0: e[-b:] = np.linspace(1, 0, b)
    return e[:, None]


def pon(mix, x, t, gain_db, fade_in=0.0, fade_out=0.05, alinear=True, recorte=None):
    """Coloca `x` en el mix: si `alinear`, su onset cae en t; `recorte` = duración máxima en s."""
    off = onset(x) if alinear else 0.0
    if recorte:
        x = x[: int(recorte * SR)]
    x = x * envolvente(len(x), fade_in, fade_out, len(x)) * db(gain_db)
    i0 = int((t - off) * SR)
    if i0 < 0:
        x = x[-i0:]; i0 = 0
    i1 = min(i0 + len(x), len(mix))
    mix[i0:i1] += x[: i1 - i0]


def mezcla_v5(con_musica):
    mix = np.zeros((int(DUR * SR) + 1, 2), dtype=np.float32)
    fr = lambda f: f / 29.97
    pon(mix, carga("cocina"), 0.0, -24, fade_in=0.4, fade_out=0.6, alinear=False, recorte=fr(84))
    pon(mix, carga("plop"), fr(84), -4)                                                   # UNA SOLA GOTA
    pon(mix, carga("bigbang"), fr(108), -5, fade_out=0.5, recorte=fr(150 - 108) + 0.5)    # LO CAMBIA TODO
    pon(mix, carga("pizza"), fr(150), -15, fade_in=0.05, fade_out=0.15, alinear=False, recorte=fr(45))
    pon(mix, carga("sizzle"), fr(195), -17, fade_in=0.05, fade_out=0.2, alinear=False, recorte=fr(54))
    pon(mix, carga("whoof"), fr(197), -7)
    pon(mix, carga("pasta"), fr(249), -14, fade_in=0.05, fade_out=0.2, alinear=False, recorte=fr(57))
    pon(mix, carga("cocina"), fr(306), -20, fade_in=0.2, fade_out=0.4, alinear=False, recorte=fr(69))   # la mesa: aire cálido
    pon(mix, carga("hilo"), fr(306), -20, fade_in=0.3, fade_out=0.5, alinear=False, recorte=fr(60))
    pon(mix, carga("plop"), fr(381), -6)                                                  # la gota toca el set: placement
    pon(mix, carga("sting"), fr(381), -16, fade_out=0.3)
    pon(mix, carga("pushin"), fr(381), -18, fade_in=0.4, fade_out=0.6, alinear=False, recorte=fr(528 - 381))
    pon(mix, carga("plop"), fr(528), -3)
    pon(mix, carga("sting"), fr(531), -6, fade_out=0.3)
    if con_musica:
        pon(mix, carga(MUSICA), 0.0, -14, fade_in=0.2, fade_out=1.0, alinear=False, recorte=DUR)
    pico = np.abs(mix).max()
    if pico > 0.89:
        mix *= 0.89 / pico
    return mix


def mezcla_v2(con_musica, plop_hero=375):
    """Animatic V2: tres PLOP hermanos (apertura · desprendimiento en el reveal · cierre) como firma sonora; el
    cambio del universo en CAMBIA TODO; dos stings (llegada al hero suave, descubrimiento de la familia)."""
    mix = np.zeros((int(DUR * SR) + 1, 2), dtype=np.float32)
    fr = lambda f: f / 29.97
    pon(mix, carga("cocina"), 0.0, -26, fade_in=0.3, fade_out=0.8, alinear=False, recorte=fr(96))
    pon(mix, carga("plop"), fr(96), -4)                                                   # UNA GOTA.
    pon(mix, carga("bigbang"), fr(118), -5, fade_out=0.5, recorte=fr(150 - 118) + 0.5)    # CAMBIA TODO: el cambio
    pon(mix, carga("pizza"), fr(150), -15, fade_in=0.05, fade_out=0.15, alinear=False, recorte=fr(45))
    pon(mix, carga("sizzle"), fr(195), -17, fade_in=0.05, fade_out=0.2, alinear=False, recorte=fr(54))
    pon(mix, carga("whoof"), fr(197), -7)                                                 # el flare: unos cuadros
    pon(mix, carga("pasta"), fr(249), -14, fade_in=0.05, fade_out=0.2, alinear=False, recorte=fr(57))
    pon(mix, carga("hilo"), fr(306), -17, fade_in=0.3, fade_out=0.5, alinear=False, recorte=fr(354 - 306))
    pon(mix, carga("squeeze"), fr(336), -10)                                              # último squeeze
    pon(mix, carga("click"), fr(340), -7)
    pon(mix, carga("plop"), fr(plop_hero), -6)                                            # la gota que se desprende toca el piso del hero
    pon(mix, carga("sting"), fr(plop_hero), -16, fade_out=0.3)
    pon(mix, carga("pushin"), fr(375), -18, fade_in=0.4, fade_out=0.6, alinear=False, recorte=fr(528 - 375))
    pon(mix, carga("plop"), fr(528), -3)                                                  # PLOP final: la onda
    pon(mix, carga("sting"), fr(531), -6, fade_out=0.3)                                   # la familia se descubre
    if con_musica:
        pon(mix, carga(MUSICA), 0.0, -14, fade_in=0.2, fade_out=1.0, alinear=False, recorte=DUR)
    pico = np.abs(mix).max()
    if pico > 0.89:
        mix *= 0.89 / pico
    return mix


def mezcla(con_musica):
    mix = np.zeros((int(DUR * SR) + 1, 2), dtype=np.float32)
    fr = lambda f: f / 29.97
    # 01–02 · normalidad: aire de cocina, se apaga con la gota
    pon(mix, carga("cocina"), 0.0, -26, fade_in=0.3, fade_out=0.8, alinear=False, recorte=fr(96))
    # 03 · PLOP (silencio alrededor) y 04 · el big bang
    pon(mix, carga("plop"), fr(96), -4)
    pon(mix, carga("bigbang"), fr(114), -3, fade_out=0.4, recorte=fr(150 - 114) + 0.4)
    # 05 · pizza: el queso reacciona
    pon(mix, carga("pizza"), fr(150), -14, fade_in=0.05, fade_out=0.15, alinear=False, recorte=fr(45))
    # 06 · sartén: sizzle de base + WHOOF en el flare
    pon(mix, carga("sizzle"), fr(195), -16, fade_in=0.05, fade_out=0.2, alinear=False, recorte=fr(54))
    pon(mix, carga("whoof"), fr(199), -5)
    # 07 · pasta: el giro y el hilo
    pon(mix, carga("pasta"), fr(249), -14, fade_in=0.05, fade_out=0.2, alinear=False, recorte=fr(57))
    # 08 · reveal: el hilo continuo, el apriete y el CLICK
    pon(mix, carga("hilo"), fr(306), -16, fade_in=0.3, fade_out=0.6, alinear=False, recorte=fr(75))
    pon(mix, carga("squeeze"), fr(348), -10)
    pon(mix, carga("click"), fr(352), -6)
    # 09–10 · hero: un sting suave al corte + aire tenso que sube (push-in)
    pon(mix, carga("sting"), fr(381), -16, fade_out=0.3)
    pon(mix, carga("pushin"), fr(381), -18, fade_in=0.4, fade_out=0.6, alinear=False, recorte=fr(546 - 381))
    # 11 · firma: sting en el logo, PLOP final, negro
    pon(mix, carga("sting"), fr(546), -6, fade_out=0.3)
    pon(mix, carga("plop"), fr(584), -3)
    if con_musica:
        pon(mix, carga(MUSICA), 0.0, -14, fade_in=0.2, fade_out=1.0, alinear=False, recorte=DUR)   # v3: RMS −10 constante hasta 15 s y se apaga sola bajo el hero
    pico = np.abs(mix).max()
    if pico > 0.89:
        mix *= 0.89 / pico
    return mix


def escribe(mix, wav):
    p = subprocess.Popen([FF, "-v", "error", "-y", "-f", "f32le", "-ac", "2", "-ar", str(SR), "-i", "-", "-c:a", "pcm_s24le", wav], stdin=subprocess.PIPE)
    p.communicate(mix.astype(np.float32).tobytes())


def main():
    render, out = sys.argv[1], sys.argv[2]
    v2 = "--v2" in sys.argv or "--v3" in sys.argv
    v3 = "--v3" in sys.argv or "--v4" in sys.argv
    v4 = "--v4" in sys.argv
    v5 = "--v5" in sys.argv
    os.makedirs(out, exist_ok=True)
    for tag, musica in (("con-cama-temporal", True), ("sin-musica", False)):
        wav = os.path.join(out, f"mezcla-{tag}.wav")
        escribe(mezcla_v5(musica) if v5 else ((lambda m: mezcla_v2(m, 381)) (musica) if v3 else (mezcla_v2 if v2 else mezcla)(musica)), wav)
        mp4 = os.path.join(out, f"SANTA_GOTA_ANIMATIC{'_V5' if v5 else ('_V4' if v4 else ('_V3' if v3 else ('_V2' if v2 else '')))}_{tag}.mp4")
        subprocess.run([FF, "-v", "error", "-y", "-i", render, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-shortest", mp4], check=True)
        print("✔", mp4)


if __name__ == "__main__":
    main()

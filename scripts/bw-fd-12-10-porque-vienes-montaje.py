"""BETWEEN · FEED 12-10 «POR QUÉ VIENES / POR QUÉ TE QUEDAS» — montaje con ffmpeg.

Es la MISMA pieza que `src/compositions/hilton/BetweenFeed1210PorQue.tsx`
(tomas, encuadres, tiempos y rótulos), armada fuera de Remotion porque desde el
29-09-2026 Windows bloquea `remotion.exe` (memoria `remotion-exe-bloqueado-windows`).
El reel es sólo clips + dos rótulos fijos, así que ffmpeg lo arma igual:
  · cada mitad = 7 tramos recortados a 540 px (objectPosition x %) y concatenados;
  · hstack de las dos mitades;
  · encima, la capa de rótulos (PNG con Raleway SemiBold real y la sombra café).
Si cambias la composición .tsx, cambia TOMAS acá (y al revés).

Salidas: out/hilton/between/oct-r2/BW FEED 12-10 Por que vienes por que te quedas.{mp4,gif}

    python scripts/bw-fd-12-10-porque-vienes-montaje.py
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
FF = r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
CLIPS = RAIZ / "public/assets/hilton/between/oct/porque"
FUENTE = RAIZ / "public/assets/hilton/between/fonts/Raleway-SemiBold.ttf"
OUT = RAIZ / "out/hilton/between/oct-r2"
NOMBRE = "BW FEED 12-10 Por que vienes por que te quedas"

FPS, TOMA, COLA = 30, 48, 18
BEIGE = (255, 249, 235)
SOMBRA = (36, 26, 18)

# (clip, objectPosition x %) — idéntico a VIENES / QUEDAS del .tsx
VIENES = [("v1-cafe", 38), ("v2-latte", 45), ("v3-desayuno", 50), ("v4-croissant", 60),
          ("v5-dulce", 52), ("v6-osito", 50), ("v7-togo", 84)]
QUEDAS = [("q1-barista", 40), ("q2-sirviendo", 32), ("q3-mesa", 55), ("q4-espacio", 50),
          ("q5-detalle", 55), ("q6-cowork", 50), ("q7-relajo", 62)]


def rotulos(dst: Path) -> None:
    """Capa 1080×1920 transparente con los dos rótulos (top 330, 40 px, tracking 0,02 em)."""
    f = ImageFont.truetype(str(FUENTE), 40)
    track = 40 * 0.02
    texto = Image.new("L", (1080, 1920), 0)
    d = ImageDraw.Draw(texto)
    for cx, s in ((270, "POR QUÉ VIENES"), (810, "POR QUÉ TE QUEDAS")):
        ancho = sum(f.getlength(c) for c in s) + track * (len(s) - 1)
        x = cx - ancho / 2
        for c in s:
            d.text((x, 330), c, font=f, fill=255)
            x += f.getlength(c) + track
    capa = Image.new("RGBA", (1080, 1920), SOMBRA + (0,))
    # text-shadow: 0 2px 18px α0,8  +  0 1px 3px α0,6 (como el .tsx)
    for dy, blur, alfa in ((2, 9, 0.8), (1, 1.5, 0.6)):
        m = Image.new("L", (1080, 1920), 0)
        m.paste(texto, (0, dy))
        m = m.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * alfa))
        s = Image.new("RGBA", (1080, 1920), SOMBRA + (0,))
        s.putalpha(m)
        capa = Image.alpha_composite(capa, s)
    t = Image.new("RGBA", (1080, 1920), BEIGE + (0,))
    t.putalpha(texto)
    Image.alpha_composite(capa, t).save(dst)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    capa = OUT / "_rotulos-12-10.png"
    rotulos(capa)
    ins, fil = [], []
    n = 0
    for lado, tomas in (("a", VIENES), ("b", QUEDAS)):
        etiquetas = []
        for i, (clip, x) in enumerate(tomas):
            dur = (TOMA + (COLA if i == len(tomas) - 1 else 0)) / FPS
            ins += ["-i", str(CLIPS / f"{clip}.mp4")]
            ox = round((1080 - 540) * x / 100)
            fil.append(f"[{n}:v]trim=0:{dur:.4f},setpts=PTS-STARTPTS,fps={FPS},"
                       f"crop=540:1920:{ox}:0,setsar=1[{lado}{i}]")
            etiquetas.append(f"[{lado}{i}]")
            n += 1
        fil.append(f"{''.join(etiquetas)}concat=n={len(tomas)}:v=1:a=0[{lado}]")
    ins += ["-i", str(capa)]
    fil.append(f"[a][b]hstack=inputs=2[ab];[ab][{n}:v]overlay=0:0:format=auto,format=yuv420p[v]")
    mp4 = OUT / f"{NOMBRE}.mp4"
    subprocess.run([FF, "-y", "-v", "error", *ins, "-filter_complex", ";".join(fil), "-map", "[v]",
                    "-r", str(FPS), "-c:v", "libx264", "-profile:v", "high", "-crf", "16",
                    "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mp4)],
                   check=True)
    gif = OUT / f"{NOMBRE}.gif"
    subprocess.run([FF, "-y", "-v", "error", "-i", str(mp4), "-vf",
                    "fps=25,scale=540:960:flags=lanczos,split[a][b];[a]palettegen=stats_mode=diff[p];"
                    "[b][p]paletteuse=dither=none", str(gif)], check=True)
    portada = OUT / f"{NOMBRE} - PORTADA.png"
    subprocess.run([FF, "-y", "-v", "error", "-ss", "0.8", "-i", str(mp4), "-frames:v", "1",
                    str(portada)], check=True)
    capa.unlink()
    print("ok", mp4.name, gif.name, portada.name)


if __name__ == "__main__":
    main()

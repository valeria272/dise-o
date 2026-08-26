#!/usr/bin/env python3
"""Convierte cualquier pieza en algo que se pueda MIRAR y revisar.

    python3 scripts/ver-pieza.py <archivo|carpeta> [salida.png] [--frames 12]

  · .mp4 / .mov  → hoja de contacto con N fotogramas repartidos, con su segundo
  · .pdf         → una imagen por página
  · .png / .jpg  → hoja de contacto de la carpeta, con medidas y proporción

Para qué: un reel no se puede revisar sin verlo, y una carpeta de 40 referencias
no se revisa abriendo una por una. Se mira todo junto o no se mira.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEO = (".mp4", ".mov", ".m4v", ".webm", ".avi")
IMAGEN = (".png", ".jpg", ".jpeg", ".webp", ".gif")


def ffmpeg():
    local = os.path.join(RAIZ, "tools", "ffmpeg")
    if os.path.isfile(local) and os.access(local, os.X_OK):
        return local
    from shutil import which
    return which("ffmpeg") or sys.exit(
        "✗ No hay ffmpeg. Instálalo (brew install ffmpeg) o deja el binario en tools/ffmpeg")


def duracion(ruta):
    ff = ffmpeg()
    r = subprocess.run([ff, "-i", ruta], capture_output=True, text=True)
    for linea in r.stderr.splitlines():
        if "Duration:" in linea:
            t = linea.split("Duration:")[1].split(",")[0].strip()
            h, m, s = t.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0


def frames_de_video(ruta, n, tmp):
    ff, dur = ffmpeg(), duracion(ruta)
    if dur <= 0:
        sys.exit(f"✗ No pude leer la duración de {ruta}")
    os.makedirs(tmp, exist_ok=True)
    salida = []
    for i in range(n):
        t = dur * (i + 0.5) / n
        p = os.path.join(tmp, f"f{i:03}.png")
        subprocess.run([ff, "-y", "-ss", f"{t:.3f}", "-i", ruta, "-frames:v", "1",
                        "-loglevel", "error", p], check=False)
        if os.path.exists(p):
            salida.append((p, t))
    return salida, dur


def hoja(items, destino, cols=4, mini=460, titulo=""):
    """items = [(ruta, etiqueta)]"""
    if not items:
        sys.exit("✗ No hay nada que mostrar")
    filas = (len(items) + cols - 1) // cols
    alto_tit = 40 if titulo else 0
    h = Image.new("RGB", (cols * mini, filas * (mini + 30) + alto_tit), "white")
    d = ImageDraw.Draw(h)
    if titulo:
        d.text((10, 14), titulo, fill="black")
    for i, (ruta, etiqueta) in enumerate(items):
        x, y = (i % cols) * mini, (i // cols) * (mini + 30) + alto_tit
        try:
            im = Image.open(ruta).convert("RGB")
            w0, h0 = im.size
            im.thumbnail((mini - 8, mini - 8))
            h.paste(im, (x + (mini - im.width) // 2, y + 30))
            etiqueta = f"{etiqueta}  {w0}x{h0} ({w0/h0:.2f})"
        except Exception as e:
            d.rectangle([x + 4, y + 30, x + mini - 4, y + mini], fill="#B00020")
            d.text((x + 14, y + 44), "NO ABRE", fill="white")
            etiqueta = f"✗ {etiqueta} — {type(e).__name__}"
        d.text((x + 4, y + 10), etiqueta[:60], fill="black")
    os.makedirs(os.path.dirname(os.path.abspath(destino)), exist_ok=True)
    h.save(destino)
    print(f"→ {destino}  ({len(items)} cuadros)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    origen = sys.argv[1]
    destino = (sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--")
               else os.path.join(RAIZ, "out/_verificacion",
                                 os.path.basename(origen.rstrip("/")) + "-vista.png"))
    n = 12
    if "--frames" in sys.argv:
        n = int(sys.argv[sys.argv.index("--frames") + 1])

    ext = os.path.splitext(origen)[1].lower()

    if os.path.isdir(origen):
        fs = sorted(os.path.join(d, f) for d, _, files in os.walk(origen)
                    for f in files if os.path.splitext(f)[1].lower() in IMAGEN)
        hoja([(f, os.path.relpath(f, origen)) for f in fs], destino,
             titulo=f"{origen} — {len(fs)} imágenes")

    elif ext in VIDEO:
        tmp = os.path.join(RAIZ, "out/_verificacion/_frames")
        fr, dur = frames_de_video(origen, n, tmp)
        hoja([(p, f"{t:.1f}s") for p, t in fr], destino,
             titulo=f"{os.path.basename(origen)} — {dur:.1f}s, {len(fr)} cuadros")

    elif ext == ".pdf":
        tmp = os.path.join(RAIZ, "out/_verificacion/_pdf")
        os.makedirs(tmp, exist_ok=True)
        subprocess.run(["sips", "-s", "format", "png", origen, "--out", tmp],
                       capture_output=True)
        fs = sorted(os.path.join(tmp, f) for f in os.listdir(tmp))
        hoja([(f, os.path.basename(f)) for f in fs], destino,
             titulo=os.path.basename(origen))

    elif ext in IMAGEN:
        hoja([(origen, os.path.basename(origen))], destino, cols=1, mini=900)

    else:
        sys.exit(f"✗ No sé mostrar un {ext}")

    print("  Ábrela y MÍRALA. No la des por buena sin verla.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PISO18 · S4 — la historia animada, también en GIF.

    python scripts/p18-s4-gif.py                 # el de entrega, 540x960
    python scripts/p18-s4-gif.py --grande        # además, uno a 1080x1920
    python scripts/p18-s4-gif.py --medir         # sólo pesa las variantes

Encargo de Eli (22-09-2026, ronda 7): «guárdalo igual en gif».

══════════════════════════════════════════════════════════════════════════════
⭐ LAS TRES DECISIONES, Y POR QUÉ — todas medidas sobre esta pieza
══════════════════════════════════════════════════════════════════════════════

**1 · 25 fps, no 30.** No es una concesión de peso: **el GIF mide los tiempos en
centésimas de segundo**. A 30 fps cada fotograma dura 3,33 centésimas, que no
existe — el formato redondea y la pieza se desfasa. 25 fps son 4 centésimas
exactas, así que los 13,00 s se respetan al milisegundo (325 fotogramas × 40 ms).
Las otras cadencias exactas son 20, 16,67, 12,5 y 10.

**2 · SIN dithering.** Contra la intuición, es a la vez lo más liviano y lo más
fiel. Medido contra el fotograma 300 del MP4, a 540×960 y 20 fps:

    dither            error medio   error en el velo   peso
    sierra2_4a             5,00          3,83          41,6 MB
    bayer (escala 3)       5,14          4,35          13,1 MB
    ninguno                3,91          3,32          14,3 MB   ←

El difuminado sirve cuando la paleta es pobre; acá la paleta se calcula del
propio video (`stats_mode=diff`, 255 colores) y el material es fotografía de
interior con una gama estrecha. Lo que hacen los dos difuminados es **meter ruido
en el cielo oscuro del velo**, que es la zona más lisa de la pieza: el bayer deja
una trama cruzada visible sobre todo el fondo. Sin difuminar no hay trama, el
error baja y encima pesa casi lo mismo que el bayer.

**3 · 540×960.** Es la mitad exacta del nativo, así que el reescalado es limpio.
El GIF no es formato de publicación —Instagram no recibe historias en GIF—, es
para mirar y mandar, y a tamaño completo se va a un peso que no se puede mandar:

    540×960      18,2 MB   ← el de entrega
    720×1280     30,8 MB
    1080×1920    64,2 MB   (--grande, si hace falta el nativo)

⚠️ Y para referencia de lo que se descartó: a 1080×1920 y 30 fps con difuminado
sierra el GIF pesa **240 MB**. Un GIF de 13 s a tamaño completo no es una opción.

══════════════════════════════════════════════════════════════════════════════
⚠️ SE VERIFICA QUE LA TRANSICIÓN SIGA VIVA
══════════════════════════════════════════════════════════════════════════════
El GIF de esta pieza existe *después* de la ronda 7, que arregló justamente la
transición. Bajar de 30 a 25 fps descarta uno de cada seis fotogramas, así que el
script comprueba sobre el GIF ya escrito que el empuje siga siendo continuo: sin
fotogramas congelados y sin saltos fuera de las cuatro transiciones. Si eso falla,
el GIF no sirve aunque pese poco.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "out/piso18/s4/entrega/STS/ST N°3 S4.mp4"
ENTREGA = RAIZ / "out/piso18/s4/entrega/STS/ST N°3 S4.gif"
GRANDE = RAIZ / "out/piso18/s4/ST N°3 S4 - 1080.gif"

FPS = 25                    # 4 centésimas exactas; ver la cabecera
ENTRADAS = (84, 150, 216, 282)   # las cuatro transiciones, en fotogramas de 30 fps


def ffmpeg() -> str:
    """El ffmpeg del entorno. En esta máquina viene con imageio-ffmpeg."""
    for cand in ("ffmpeg", "ffmpeg.exe"):
        try:
            subprocess.run([cand, "-version"], capture_output=True, check=True)
            return cand
        except Exception:                                          # noqa: BLE001
            pass
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:                                              # noqa: BLE001
        sys.exit("✗ No encuentro ffmpeg. `pip install imageio-ffmpeg` o instálalo.")


def arma(ff: str, destino: Path, ancho: int, alto: int) -> Path:
    destino.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        paleta = Path(tmp) / "paleta.png"
        # Paso 1 · la paleta sale del propio video, no de una tabla fija.
        subprocess.run([
            ff, "-v", "error", "-i", str(FUENTE),
            "-vf", f"fps={FPS},scale={ancho}:{alto}:flags=lanczos,"
                   "palettegen=max_colors=255:stats_mode=diff",
            "-y", str(paleta)], check=True)
        # Paso 2 · sin difuminado, y `diff_mode=rectangle` para que sólo se
        # reescriba el rectángulo que cambia entre fotograma y fotograma.
        subprocess.run([
            ff, "-v", "error", "-i", str(FUENTE), "-i", str(paleta),
            "-lavfi", f"fps={FPS},scale={ancho}:{alto}:flags=lanczos[x];"
                      "[x][1:v]paletteuse=dither=none:diff_mode=rectangle",
            "-y", str(destino)], check=True)
    return destino


def verifica(ff: str, gif: Path) -> bool:
    """Que el GIF dure lo mismo y que la transición no se haya roto al bajar a 25."""
    import numpy as np
    from PIL import Image

    im = Image.open(gif)
    n = getattr(im, "n_frames", 1)
    ms = im.info.get("duration", 0)
    seg = n * ms / 1000
    ok = abs(seg - 13.0) < 0.05
    print(f"  · {im.size[0]}×{im.size[1]} · {n} fotogramas × {ms} ms = {seg:.2f} s "
          f"{'✓' if ok else '✗ NO son los 13,00 s del video'}")

    with tempfile.TemporaryDirectory() as tmp:
        crudo = Path(tmp) / "g.raw"
        w, h = 135, 240
        subprocess.run([ff, "-v", "error", "-i", str(gif),
                        "-vf", f"scale={w}:{h},format=gray",
                        "-f", "rawvideo", "-pix_fmt", "gray", "-y", str(crudo)], check=True)
        d = np.fromfile(crudo, dtype=np.uint8)
        m = d.size // (w * h)
        v = d[:m * w * h].reshape(m, h, w).astype(np.int16)
    dif = np.abs(np.diff(v, axis=0)).mean(axis=(1, 2))

    # Las entradas, llevadas de 30 fps a la cadencia del GIF.
    ventana: set[int] = set()
    for e in ENTRADAS:
        g = round(e * FPS / 30)
        ventana |= set(range(g - 2, g + 16))
    fuera = [(i, round(float(x), 1)) for i, x in enumerate(dif)
             if x > 25 and i not in ventana]
    if fuera:
        print(f"  ✗ salto fuera de las transiciones: {fuera}")
        return False
    print("  · sin saltos fuera de las cuatro transiciones ✓")

    # Y que dentro de cada empuje no haya un fotograma muerto — el defecto que
    # arregló la ronda 7 y que no se puede volver a colar por el remuestreo.
    for e in ENTRADAS:
        g = round(e * FPS / 30)
        tramo = dif[g:g + 12]
        muertos = int((tramo < 1.0).sum())
        if muertos:
            print(f"  ✗ el empuje de f{e} trae {muertos} fotograma(s) congelado(s)")
            return False
    print("  · ningún fotograma congelado dentro de los empujes ✓")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grande", action="store_true",
                    help="además, el GIF a 1080×1920 (pesa ~64 MB, no va a Drive)")
    ap.add_argument("--medir", action="store_true",
                    help="pesa las tres medidas y no escribe la entrega")
    a = ap.parse_args()

    if not FUENTE.exists():
        sys.exit(f"✗ No está el video: {FUENTE}\n"
                 "  Rinde antes: python scripts/p18-rendir.py P18-ST-Montaje")
    ff = ffmpeg()

    if a.medir:
        with tempfile.TemporaryDirectory() as tmp:
            for w, h in ((540, 960), (720, 1280), (1080, 1920)):
                g = arma(ff, Path(tmp) / f"{w}.gif", w, h)
                print(f"  {w}×{h}  {FPS} fps  →  {g.stat().st_size / 1048576:.1f} MB")
        return 0

    print(f"PISO18 · S4 · «ST N°3 S4» → GIF ({FPS} fps, sin difuminado)")
    arma(ff, ENTREGA, 540, 960)
    print(f"  ✓ {ENTREGA.name}  ({ENTREGA.stat().st_size / 1048576:.1f} MB)")
    bien = verifica(ff, ENTREGA)

    if a.grande:
        arma(ff, GRANDE, 1080, 1920)
        print(f"  ✓ {GRANDE.name}  ({GRANDE.stat().st_size / 1048576:.1f} MB)"
              "   ⚠️ no va a Drive: es para archivo")

    print("\nListo." if bien else "\n⚠️ Revisa los avisos de arriba antes de entregar.")
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())

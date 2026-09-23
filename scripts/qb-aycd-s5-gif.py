#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · S5 — la ST animada de ALL YOU CAN DRINK, también en GIF.

    python scripts/qb-aycd-s5-gif.py            # el de entrega, 540x960
    python scripts/qb-aycd-s5-gif.py --medir    # sólo pesa las variantes

Encargo del 23-09-2026: junto con el cambio de texto que pidió Nicolás Ávila
(contenido), la carpeta de entrega queda con la estática, el video **y el GIF**.

══════════════════════════════════════════════════════════════════════════════
LAS TRES DECISIONES SON LAS MISMAS QUE SE MIDIERON EN PISO 18
══════════════════════════════════════════════════════════════════════════════
Ver `scripts/p18-s4-gif.py`, que trae la tabla completa. En resumen:

**1 · 25 fps, no 30.** El GIF guarda la duración de cada fotograma en centésimas
de segundo. A 30 fps serían 3,33 centésimas, que el formato no representa: lo
redondea y la pieza se desfasa. A 25 fps son 4 centésimas exactas, y los 8,00 s
de esta historia quedan clavados: **200 fotogramas × 40 ms**.

**2 · SIN difuminado.** La paleta se calcula del propio video
(`palettegen=max_colors=255:stats_mode=diff`) y el material es fotografía de
interior de gama estrecha. El difuminado sólo mete trama en las zonas más lisas
—acá, el velo negro del pie y el fondo desenfocado del bar—.

**3 · 540×960**, la mitad exacta del nativo, así que el reescalado es limpio.

══════════════════════════════════════════════════════════════════════════════
⚠️ LO QUE ESTA PIEZA OBLIGA A VERIFICAR, Y QUE NO ES LO DE PISO 18
══════════════════════════════════════════════════════════════════════════════
Acá no hay transiciones: la pieza entera está quieta y **lo único que se mueve
son las tres bandas de UNLIMITED**, a velocidad constante y en bucle perfecto
(ver la cabecera de `src/compositions/qb/QBStAycdS5.tsx`). Entonces el defecto
que hay que buscar no es un salto, sino lo contrario:

  · que el movimiento siga siendo **parejo** —bajar de 30 a 25 fps descarta uno
    de cada seis fotogramas y no puede dejar tirones—, y
  · que **no haya ningún fotograma congelado**, que delataría un descarte mal
    alineado, y
  · que **el bucle siga cerrando**: el último fotograma tiene que empalmar con
    el primero igual que cualquier par consecutivo. Si no, el GIF —que sí se
    reproduce en bucle— muestra un tirón en cada vuelta que el MP4 no tiene.

⚠️ Instagram no recibe historias en GIF. Lo que se publica es el MP4; el GIF es
para mirar y mandar. Y al subirlo a Drive hay que declararle `image/gif`, o se
sube como `application/octet-stream` y no se previsualiza.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "out/qb/ST S5 QB AYCD 28-09 - v7 (texto nuevo).mp4"
ENTREGA = RAIZ / "out/qb/ST S5 QB AYCD 28-09 - v7 (texto nuevo).gif"

FPS = 25                    # 4 centésimas exactas; ver la cabecera
SEGUNDOS = 8.0              # 240 fotogramas a 30 fps


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
    """Duración exacta, movimiento parejo, sin congelados y con el bucle cerrado."""
    import numpy as np
    from PIL import Image

    im = Image.open(gif)
    n = getattr(im, "n_frames", 1)
    ms = im.info.get("duration", 0)
    seg = n * ms / 1000
    ok = abs(seg - SEGUNDOS) < 0.05
    print(f"  · {im.size[0]}×{im.size[1]} · {n} fotogramas × {ms} ms = {seg:.2f} s "
          f"{'✓' if ok else f'✗ NO son los {SEGUNDOS:.2f} s del video'}")

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
    cierre = float(np.abs(v[0].astype(np.int16) - v[-1]).mean())

    congelados = [i for i, x in enumerate(dif) if x < 0.05]
    if congelados:
        print(f"  ✗ fotograma(s) congelado(s) en {congelados}")
        ok = False
    else:
        print(f"  · sin fotogramas congelados ✓  (movimiento medio {dif.mean():.2f})")

    # Movimiento parejo: ningún paso puede salirse del triple de la mediana.
    mediana = float(np.median(dif))
    tirones = [(i, round(float(x), 2)) for i, x in enumerate(dif) if x > 3 * mediana]
    if tirones:
        print(f"  ✗ tirón en el desplazamiento de las bandas: {tirones}")
        ok = False
    else:
        print(f"  · desplazamiento parejo ✓  (mediana {mediana:.2f}, "
              f"máximo {dif.max():.2f})")

    # El bucle: el salto del último al primero tiene que parecerse a los demás.
    if cierre > 3 * mediana:
        print(f"  ✗ el bucle no cierra: del último al primero salta {cierre:.2f} "
              f"contra una mediana de {mediana:.2f}")
        ok = False
    else:
        print(f"  · el bucle cierra ✓  (empalme {cierre:.2f})")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--medir", action="store_true",
                    help="pesa las tres medidas y no escribe la entrega")
    a = ap.parse_args()

    if not FUENTE.exists():
        sys.exit(f"✗ No está el video: {FUENTE}\n"
                 "  Rinde antes:\n"
                 "  npx remotion render src/QbEntry.tsx QB-ST-AYCD-S5 "
                 f'"{FUENTE.relative_to(RAIZ)}" --codec=h264 --crf=16')
    ff = ffmpeg()

    if a.medir:
        with tempfile.TemporaryDirectory() as tmp:
            for w, h in ((540, 960), (720, 1280), (1080, 1920)):
                g = arma(ff, Path(tmp) / f"{w}.gif", w, h)
                print(f"  {w}×{h}  {FPS} fps  →  {g.stat().st_size / 1048576:.1f} MB")
        return 0

    print(f"QB · S5 · «ST S5 QB AYCD 28-09» → GIF ({FPS} fps, sin difuminado)")
    arma(ff, ENTREGA, 540, 960)
    print(f"  ✓ {ENTREGA.name}  ({ENTREGA.stat().st_size / 1048576:.1f} MB)")
    bien = verifica(ff, ENTREGA)

    print("\nListo." if bien else "\n⚠️ Revisa los avisos de arriba antes de entregar.")
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())

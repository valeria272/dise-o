#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL DÍA DEL TURISMO — la compuerta de contraste.

    python scripts/dt-c1-turismo-qa.py            # rinde los controles y mide
    python scripts/dt-c1-turismo-qa.py --sin-rendir

Reglas que aplica, todas ya escritas en `clients/hilton/CLAUDE.md`:

  · ⭐⭐ En una pieza animada el contraste se mide en los DOS extremos (f0 y el
    último) y manda el peor.
  · ⭐⭐⭐ El fondo se MIDE sobre un fotograma de control SIN tinta
    (`soloFondo`), no se estima enmascarando por color.
  · ⛔⛔ La banda sale de la TINTA, no se dibuja a ojo: acá la caja de cada
    renglón es la diferencia entre la lámina con texto y su control, así que
    cubre cada glifo tal como lo armó Chrome.
  · Peor TERCIO de la banda (para tinta blanca, el más claro), no el promedio.
  · Varas: 3:1 titular y nombre de lugar (texto grande), 4,5:1 bajada.
  · ⭐⭐⭐ `el-contraste-no-ve-la-textura`: además se informa la energía de
    gradiente del fondo en la banda, por el peor tramo.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
DIR = RAIZ / "out/hilton/dt/c1-turismo/qa"
ENTRADA = RAIZ / "src/DtEntry.tsx"
LAMINAS = ["Portada", "Mut", "Bicentenario", "Sky", "SanCristobal", "Golf"]
ULTIMO = 149
TINTA = (250, 250, 250)                           # DT.colores.blanco


def lum(rgb: np.ndarray) -> np.ndarray:
    c = rgb.astype(np.float64) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contraste(l1: float, l2: float) -> float:
    a, b = max(l1, l2), min(l1, l2)
    return (a + 0.05) / (b + 0.05)


def rendir() -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    props = DIR / "fondo.json"
    props.write_text(json.dumps({"soloFondo": True}))
    npx = "npx.cmd" if sys.platform == "win32" else "npx"
    for c in LAMINAS:
        for f in (0, ULTIMO):
            for fondo in (False, True):
                out = DIR / f"{c}-{f}{'-fondo' if fondo else ''}.png"
                cmd = [npx, "remotion", "still", str(ENTRADA), f"DT-V-Tur-{c}",
                       str(out), f"--frame={f}", "--log=error"]
                if fondo:
                    cmd.append(f"--props={props}")
                subprocess.run(cmd, cwd=RAIZ, check=True)


def renglones(mascara: np.ndarray) -> list[tuple[int, int, int, int]]:
    """Cajas de tinta por renglón: corridas de filas con tinta, y su ancho."""
    filas = mascara.any(axis=1)
    cajas, y = [], 0
    while y < len(filas):
        if filas[y]:
            y0 = y
            while y < len(filas) and filas[y]:
                y += 1
            if y - y0 >= 4:                        # descarta el filete (2 px) y ruido
                cols = np.where(mascara[y0:y].any(axis=0))[0]
                cajas.append((int(cols[0]), y0, int(cols[-1]) + 1, y))
        y += 1
    return cajas


def mide(c: str) -> list[dict]:
    res = []
    lt = lum(np.array(TINTA, dtype=np.float64)[None, None, :])[0, 0]
    # La máscara sale del ÚLTIMO fotograma, donde toda la tinta existe.
    con = np.asarray(Image.open(DIR / f"{c}-{ULTIMO}.png").convert("RGB"), dtype=np.int16)
    sin = np.asarray(Image.open(DIR / f"{c}-{ULTIMO}-fondo.png").convert("RGB"), dtype=np.int16)
    mascara = np.abs(con - sin).max(axis=2) > 40
    cajas = renglones(mascara)
    for i, (x0, y0, x1, y1) in enumerate(cajas):
        peor, textura = 99.0, 0.0
        for f in (0, ULTIMO):
            fondo = np.asarray(Image.open(DIR / f"{c}-{f}-fondo.png").convert("RGB"))
            banda = lum(fondo[y0:y1, x0:x1])
            tercios = np.array_split(banda, 3, axis=1)
            claro = max(float(t.mean()) for t in tercios)
            peor = min(peor, contraste(lt, claro))
            g = np.abs(np.diff(banda, axis=1)).mean(axis=0)   # energía por columna
            tramos = np.array_split(g, 6)
            textura = max(textura, max(float(t.mean()) for t in tramos))
        alto = y1 - y0
        vara = 4.5 if alto < 45 else 3.0
        res.append(dict(lamina=c, renglon=i + 1, caja=(x0, y0, x1, y1),
                        contraste=round(peor, 2), vara=vara,
                        textura=round(textura * 1000, 1),
                        ok=peor >= vara))
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-rendir", action="store_true")
    a = ap.parse_args()
    if not a.sin_rendir:
        rendir()
    malos = 0
    for c in LAMINAS:
        for r in mide(c):
            marca = "✅" if r["ok"] else "⛔"
            malos += 0 if r["ok"] else 1
            print(f"{marca} {r['lamina']:<13} renglón {r['renglon']}  "
                  f"caja {r['caja']}  {r['contraste']:>5}:1 (vara {r['vara']})  "
                  f"textura {r['textura']}")
    print("\nlimpio" if not malos else f"\n{malos} banda(s) bajo la vara")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())

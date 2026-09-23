#!/usr/bin/env python3
"""Instala el audio de los reels de Tierra Calma y RECALCULA las marcas de tiempo.

    python scripts/tc-audio-instalar.py ~/Downloads/voz1.mp3 ~/Downloads/voz2.mp3 \
        ~/Downloads/voz3.mp3 --como vm1 vm2 vm3
    python scripts/tc-audio-instalar.py ~/Downloads/pista.mp3 --como mus_primavera_v3
    python scripts/tc-audio-instalar.py --solo-medir        ← lee lo ya instalado

POR QUÉ EXISTE: la locución de esta cuenta se genera **línea por línea** —en una
sola toma las pausas no calzan con los cortes y los subtítulos salen
descuadrados— y el manual exige que las duraciones del array `VOZ` estén
**medidas sobre los mp3, no estimadas**. Cambiar de voz cambia todas esas
duraciones, así que el paso «medir y reescribir el array» no es opcional: es
donde se rompe el reel si alguien lo salta.

El script no edita el TSX. Imprime el array listo para pegar y **avisa si el
audio ya no cabe** en la ranura de su corte, que es lo que un cambio de voz
suele provocar.

⚠️ Lo que este script NO hace es GENERAR el audio. Ni la voz ni la música salen
de la API de Freepik/Magnific: `text-to-speech` no existe (404 en todas sus
formas) y `music-generation` responde **410, retirado** (verificado 23-09-2026).
Los dos se generan a mano en la app web de Magnific y se bajan. Ver
`clients/tierra-calma/CLAUDE.md` § 8.
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

VERDE, ROJO, AMARILLO, GRIS, FIN = (
    "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[0m")

DEST = pathlib.Path(RAIZ) / "public/assets/tierracalma/audio"
FPS = 30

# El reel de primavera (`r-01-10`). Cada línea entra en su corte y el corte dura
# SLOT = 140 frames; el subtítulo aparece unos frames antes que la voz.
#   nombre  ·  frame en que entra la voz  ·  frame en que entra su subtítulo
LINEAS = [
    ("vm1", 30, 25, "La primavera ya llegó a Tierra Calma"),
    ("vm2", 170, 165, "Más verde, más luz, más espacio"),
    ("vm3", 310, 305, "Así se siente el cambio de estación acá"),
]
SLOT = 140          # separación entre cortes, en frames
COLCHON = 12        # frames de aire que tiene que quedar antes del corte siguiente


def segundos(p: pathlib.Path) -> float:
    """Duración real del archivo. Se usa el ffprobe que trae Remotion."""
    r = subprocess.run(
        ["npx", "remotion", "ffprobe", "-v", "error", "-show_entries",
         "format=duration", "-of", "default=nw=1:nk=1", str(p)],
        capture_output=True, text=True, cwd=RAIZ, shell=(sys.platform == "win32"))
    if r.returncode != 0 or not r.stdout.strip():
        raise SystemExit(f"{ROJO}No se pudo medir {p.name}: {r.stderr.strip()[:200]}{FIN}")
    return float(r.stdout.strip())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivos", nargs="*", type=pathlib.Path,
                    help="los mp3 bajados de Magnific, en orden")
    ap.add_argument("--como", nargs="*", default=[],
                    help="con qué nombre se instala cada uno (vm1 vm2 vm3, mus_primavera_v3…)")
    ap.add_argument("--solo-medir", action="store_true",
                    help="no instala nada: mide lo que ya está en public/assets")
    a = ap.parse_args()

    if not a.solo_medir:
        if len(a.archivos) != len(a.como):
            return int(bool(print(f"{ROJO}Dame un --como por cada archivo.{FIN}")))
        DEST.mkdir(parents=True, exist_ok=True)
        for src, nombre in zip(a.archivos, a.como):
            if not src.exists():
                return int(bool(print(f"{ROJO}No existe: {src}{FIN}")))
            destino = DEST / f"{nombre}.mp3"
            destino.write_bytes(src.read_bytes())
            print(f"{VERDE}·{FIN} {src.name} → {destino.relative_to(RAIZ)}")

    # ── medir la locución y reescribir el array ───────────────────────────────
    faltan = [n for n, *_ in LINEAS if not (DEST / f"{n}.mp3").exists()]
    if faltan:
        print(f"\n{AMARILLO}Sin locución instalada: {', '.join(faltan)}. "
              f"No se puede recalcular el array.{FIN}")
        return 0

    print(f"\n{GRIS}Duraciones medidas sobre los mp3:{FIN}")
    filas, problemas = [], []
    for nombre, desde, sub, texto in LINEAS:
        s = segundos(DEST / f"{nombre}.mp3")
        f = round(s * FPS)
        filas.append((nombre, desde, f))
        print(f"  {nombre}  {s:5.2f} s  = {f:3d} frames   {GRIS}«{texto}»{FIN}")
        # ¿Se pasa del corte? El subtítulo siguiente entra en `sub + SLOT`.
        tope = sub + SLOT - COLCHON
        if desde + f > tope:
            problemas.append(
                f"{nombre}: termina en el frame {desde + f} y el corte siguiente "
                f"empieza en el {sub + SLOT}. Se pasa por {desde + f - tope} frames.")

    print(f"\n{GRIS}Pega esto en src/compositions/tierracalma/OctubreVideoV3.tsx:{FIN}\n")
    print("const VOZ: {a: string; desde: number; dura: number}[] = [")
    for nombre, desde, f in filas:
        print(f'  {{a: "{nombre}", desde: {desde}, dura: {f}}},')
    print("];")

    if problemas:
        print(f"\n{ROJO}⚠️ La voz nueva NO cabe en los cortes:{FIN}")
        for p in problemas:
            print(f"   · {p}")
        print(f"{ROJO}   Hay que acortar el texto de esa línea o alargar el corte "
              f"(SLOT en OctubreVideo.tsx, y entonces cambia la duración del reel).{FIN}")
        return 1

    print(f"\n{VERDE}✓ Las tres líneas caben en sus cortes.{FIN}")
    print(f"{GRIS}  Después: npx remotion render TCV3ReelPrimavera …{FIN}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

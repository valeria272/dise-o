#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Empaqueta y sube el CARRUSEL CONCURSO de la S3 de Between.

Hace dos cosas:

  1. Copia los renders con el nombre que pidió Eli —`C1 S3 CONCURSO N1/N2.png`,
     que sigue la nomenclatura de su propio carrusel `C1 S2 CUMPLE N1/N2.png`—
     y les escribe **150 ppp** en el `pHYs`. No reescala: la pieza sigue
     midiendo 2250×2812, sólo se declara la densidad que pide el manual para
     todo lo digital.
  2. Con `--subir`, las sube a la carpeta **`C1 S3 CONCURSO`** que cuelga de
     `S3 HILTON SEP 2026 / BW`.

⚠️ El token del estudio tiene scope `drive.file`: puede CREAR en una carpeta
ajena pero NO puede listarla. Si Google responde 404 por la carpeta, el archivo
cae en «Mi unidad» y el uploader lo avisa — hay que mirar su salida, no darla
por buena. Por eso se imprime el enlace de cada pieza.

Uso:
    python scripts/between-concurso-s3-entrega.py            # sólo empaqueta
    python scripts/between-concurso-s3-entrega.py --subir    # empaqueta y sube
"""
import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
RENDERS = RAIZ / "out/hilton/between/concurso-s3"
ENTREGA = RAIZ / "out/hilton/between/entrega-c1-s3-concurso"
PPP = 150

#: Carpeta creada el 16-09-2026 dentro de `S3 HILTON SEP 2026 / BW`
#: (`1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ`), con el nombre que pidió Eli.
CARPETA_DRIVE = "1eXZnhj5-2j7o4AuwClf5dngcn6k9oQzC"

PIEZAS = {
    "BW-F-Concurso-1": "C1 S3 CONCURSO N1.png",
    "BW-F-Concurso-2": "C1 S3 CONCURSO N2.png",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subir", action="store_true")
    a = ap.parse_args()

    ENTREGA.mkdir(parents=True, exist_ok=True)
    salidas = []
    for cid, nombre in PIEZAS.items():
        src = RENDERS / f"{cid}.png"
        if not src.is_file():
            sys.exit(f"✗ falta el render {src}\n"
                     f'  npx remotion still src/index.ts {cid} "{src}" --scale=2.0833')
        dst = ENTREGA / nombre
        im = Image.open(src)
        im.save(dst, dpi=(PPP, PPP))
        salidas.append(dst)
        print(f"✓ {nombre}  {im.size}  {PPP} ppp  ({dst.stat().st_size // 1024} KB)")

    if not a.subir:
        print(f"\nQuedaron en {ENTREGA}\n  (para subirlas:  --subir)")
        return 0

    for dst in salidas:
        print(f"\n→ subiendo {dst.name}")
        r = subprocess.run(
            [sys.executable, str(RAIZ / "scripts/drive-subir.py"), str(dst),
             "--carpeta", CARPETA_DRIVE, "--enlace"],
            cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            sys.exit(f"✗ falló la subida de {dst.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

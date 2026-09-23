#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Empaqueta y sube las DOS stories de la S4 de Between (21 y 22-09).

Existe desde la ronda 2 del CLIENTE (16-09-2026), que pidió dos cambios en la
grilla viva, hoja STORIES:

    col Q · 21-09 Strudel   → «Eliminar MASA y agregar legal Imagen referencial»
    col R · 22-09 Primavera → «Agregar legal Imagen referencial»

Hace lo mismo que `between-st-s3-entrega.py`:

  1. Copia los renders con el nombre que ya tienen en Drive —así el archivo se
     REEMPLAZA y el enlace que el cliente tiene en la grilla no cambia— y les
     escribe 150 ppp en el `pHYs`.
  2. Deja las copias `GUIA CM` en su subcarpeta. **Esas no se suben.**
  3. Con `--subir`, sube las dos piezas del cliente a `S4 HILTON SEP 2026/BW/STS`.

⚠️ El token del estudio tiene scope `drive.file`: ve sólo lo que esta app creó.
Estos dos archivos los subió ella misma el 09-09, así que los ve y los
reemplaza. Aun así hay que MIRAR la salida del uploader: si respondiera 404 por
la carpeta, el archivo caería en «Mi unidad».

Uso:
    python scripts/between-st-s4-entrega.py            # sólo empaqueta
    python scripts/between-st-s4-entrega.py --subir    # empaqueta y sube
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
RENDERS = RAIZ / "out/hilton/between/s4-r2"
ENTREGA = RAIZ / "out/hilton/between/entrega-st-s4-21-22-09"
PPP = 150

#: `S4 HILTON SEP 2026 / BW / STS` — el padre de los dos PNG del 09-09.
CARPETA_STS = "1iqFXHn9uYy16c_liM1qVQgsRLUdqpd4Z"

PIEZAS = {
    "BW-S4-Strudel": "BW ST 21-09 Strudel de manzana.png",
    "BW-S4-Primavera": "BW ST 22-09 Primavera en Between.png",
}
GUIAS = {
    "BW-S4-Strudel-Guia": "BW ST 21-09 Strudel de manzana - GUIA CM.png",
    "BW-S4-Primavera-Guia": "BW ST 22-09 Primavera en Between - GUIA CM.png",
}


def copiar(cid: str, nombre: str, destino: Path) -> Path:
    src = RENDERS / f"{cid}.png"
    if not src.is_file():
        sys.exit(f"✗ falta el render {src}\n"
                 f'  npx remotion still src/index.ts {cid} "{src}" --scale=2.0833')
    destino.mkdir(parents=True, exist_ok=True)
    dst = destino / nombre
    im = Image.open(src)
    im.save(dst, dpi=(PPP, PPP))
    print(f"✓ {nombre}  {im.size}  {PPP} ppp  ({dst.stat().st_size // 1024} KB)")
    return dst


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subir", action="store_true")
    a = ap.parse_args()

    salidas = [copiar(c, n, ENTREGA) for c, n in PIEZAS.items()]
    for c, n in GUIAS.items():
        copiar(c, n, ENTREGA / "GUIAS CM")

    if not a.subir:
        print(f"\nQuedaron en {ENTREGA}\n  (para subirlas:  --subir)")
        return 0

    for dst in salidas:
        print(f"\n→ subiendo {dst.name}")
        r = subprocess.run(
            [sys.executable, str(RAIZ / "scripts/drive-subir.py"), str(dst),
             "--carpeta", CARPETA_STS, "--enlace"],
            cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            sys.exit(f"✗ falló la subida de {dst.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

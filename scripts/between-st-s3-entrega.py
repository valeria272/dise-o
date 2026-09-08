#!/usr/bin/env python3
"""Empaqueta y sube las tres STORIES de la S3 de Between (14, 16 y 18-09).

Hace tres cosas, y sólo tres:

  1. Copia los renders con el NOMBRE que espera el portal de validaciones
     —`<SIGLA> <TIPO> <DD-MM> <Descripción>.png`, ver
     `docs/PORTAL-VALIDACIONES.html`— y les escribe **150 ppp** en el `pHYs`.
     No reescala nada: la pieza sigue midiendo 2250×4000, sólo se declara la
     densidad que pide el manual de la marca para todo lo digital.
  2. Deja las copias `GUIA CM` en una subcarpeta aparte. **Esas no se suben ni
     se mandan al cliente**: llevan dibujada la zona del sticker y son para que
     el community manager sepa dónde va. La regla salió del 07-09.
  3. Con `--subir`, sube LAS TRES piezas del cliente (no las guías) a la carpeta
     STORIES del Drive que indicó Eli.

⚠️ Idempotente por nombre: `scripts/drive-subir.py` reemplaza el archivo si ya
existe uno igual en la carpeta, así que correrlo dos veces no duplica.

⚠️ El token del estudio tiene scope `drive.file`: puede CREAR en una carpeta
ajena pero no puede LISTARLA. Si Google responde 404 por la carpeta, el archivo
cae en «Mi unidad» y el uploader lo avisa — hay que mirar su salida, no darla por
buena. Por eso este script imprime el enlace de cada pieza.

Uso:
    python scripts/between-st-s3-entrega.py            # sólo empaqueta
    python scripts/between-st-s3-entrega.py --subir     # empaqueta y sube
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
RENDERS = RAIZ / "out/hilton/between/st-s3"
ENTREGA = RAIZ / "out/hilton/between/entrega-st-s3"
PPP = 150

#: Carpeta STORIES del Drive — enlace que pasó Eli el 08-09-2026.
CARPETA_STORIES = "1SNBRIvKLvQSC2bYF3u5_oPL5UumIo-gM"

#: id de composición → nombre de entrega. La fecha va adelante para que la
#: carpeta quede ordenada como el calendario, que es como la revisa la
#: diseñadora, y los nombres son los mismos del set del 31-08 para que el portal
#: siga levantando la misma fila de la grilla.
PIEZAS = {
    "BW-S3-HoraCafe":  "BW ST 14-09 Cuando es hora de cafe.png",
    "BW-S3-Cowork":    "BW ST 16-09 Cowork te esperamos.png",
    "BW-S3-Dieciocho": "BW ST 18-09 Saludo Fiestas Patrias.png",
}

#: Las guías del CM. Mismo nombre + « GUIA CM», y a su propia subcarpeta.
GUIAS = {
    "BW-S3-HoraCafe-Guia": "BW ST 14-09 Cuando es hora de cafe GUIA CM.png",
    "BW-S3-Cowork-Guia":   "BW ST 16-09 Cowork te esperamos GUIA CM.png",
}


def copiar(cid: str, nombre: str, destino: Path) -> Path:
    src = RENDERS / f"{cid}.png"
    if not src.is_file():
        sys.exit(f"✗ falta el render {src}\n"
                 f"  npx remotion still src/index.ts {cid} \"{src}\" --scale=2.0833")
    destino.mkdir(parents=True, exist_ok=True)
    dst = destino / nombre
    im = Image.open(src)
    if im.size != (2250, 4000):
        sys.exit(f"✗ {cid} mide {im.size} y la entrega de story es 2250×4000. "
                 f"¿Se rindió sin --scale=2.0833?")
    im.save(dst, dpi=(PPP, PPP))
    print(f"  · {nombre}   {im.size[0]}×{im.size[1]} · {PPP} ppp · "
          f"{dst.stat().st_size // 1024} KB")
    return dst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subir", action="store_true",
                    help="sube las piezas del cliente a la carpeta STORIES")
    ap.add_argument("--solo", nargs="*", metavar="FECHA",
                    help="sube sólo estas fechas (14-09 · 16-09 · 18-09). Sirve "
                         "para no re-subir una pieza YA APROBADA: la del 14-09 "
                         "quedó aprobada en la ronda 3 y no se vuelve a tocar.")
    a = ap.parse_args()

    print(f"Entrega en {ENTREGA}")
    listas = [copiar(cid, n, ENTREGA) for cid, n in PIEZAS.items()]
    print("Guías del CM (NO se suben ni se mandan al cliente):")
    for cid, n in GUIAS.items():
        copiar(cid, n, ENTREGA / "GUIAS CM")

    if not a.subir:
        print("\nNo se subió nada. Para subir:  --subir")
        return

    if a.solo:
        listas = [p for p in listas if any(f in p.name for f in a.solo)]
        if not listas:
            sys.exit(f"✗ --solo {a.solo} no calza con ninguna pieza")

    print(f"\nSubiendo a la carpeta STORIES ({CARPETA_STORIES})")
    for p in listas:
        r = subprocess.run(
            [sys.executable, str(RAIZ / "scripts/drive-subir.py"), str(p),
             "--carpeta", CARPETA_STORIES],
            cwd=RAIZ, capture_output=True, text=True,
            encoding="utf-8", errors="replace")
        print(f"  {p.name}")
        for linea in (r.stdout + r.stderr).strip().splitlines():
            print(f"      {linea}")
        if r.returncode != 0:
            sys.exit(f"✗ falló la subida de {p.name}")


if __name__ == "__main__":
    main()

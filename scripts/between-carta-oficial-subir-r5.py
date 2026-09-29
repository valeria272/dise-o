#!/usr/bin/env python3
"""BETWEEN · carta oficial R5 (29-09-2026) — sube a la carpeta de Eli y verifica md5.

Destino: carpeta de Eli con el Word y las referencias (1gAZNJkaw5SKAHEmLo1yIctD-MNCE1p6v)
  └ CARTA BETWEEN · R5 29-09
      ├ BW-CARTA-BETWEEN-OPCION-A-R5.pdf … D   (diseño aprobado: jerarquía, mín. 8 pt, Menú en Brushwell)
      └ (cuando estén) BW-CARTA-BETWEEN-OPCION-X.ai + PDF DIGITAL / IMPRENTA, desde
        r5/editable/maestro/ — los arma between-carta-r5-por-hoja.py
Si un archivo ya existe con el mismo nombre, se REEMPLAZA (mismo id, no duplica).

    python scripts/between-carta-oficial-subir-r5.py
"""
import hashlib
import importlib.util
import pathlib
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
_s = importlib.util.spec_from_file_location("sub", pathlib.Path(__file__).with_name("between-carta-oficial-subir.py"))
sub = importlib.util.module_from_spec(_s)
_s.loader.exec_module(sub)

R5 = sub.RAIZ / "out/hilton/between/carta-oficial/r5"
NOMBRE = "CARTA BETWEEN · R5 29-09"


def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()


def main():
    d = sub.servicio()
    raiz = sub.carpeta(d, NOMBRE, sub.PADRE)
    lista = []
    for op in "ABCD":
        lista.append((R5 / "pdf" / f"BW-CARTA-OFICIAL-R5-OP{op}.pdf", f"BW-CARTA-BETWEEN-OPCION-{op}-R5.pdf"))
        m = R5 / "editable/maestro"
        for f in (f"BW-CARTA-BETWEEN-OPCION-{op}.ai", f"BW-CARTA-BETWEEN-OPCION-{op}-DIGITAL.pdf",
                  f"BW-CARTA-BETWEEN-OPCION-{op}-IMPRENTA.pdf"):
            if (m / f).exists():
                lista.append((m / f, f))
    malos = 0
    ent = R5 / "entrega"                     # copia local idéntica a lo que queda en Drive
    ent.mkdir(exist_ok=True)
    for src, nombre in lista:
        tmp = ent / nombre
        tmp.write_bytes(src.read_bytes())
        sub.subir(d, tmp, raiz)
        fid = sub.buscar(d, nombre, raiz)
        rem = d.files().get(fileId=fid, fields="md5Checksum", supportsAllDrives=True).execute().get("md5Checksum")
        ok = rem == md5(src)
        malos += not ok
        print(("✓" if ok else "✗ md5 distinto"), nombre)
    print(f"\nhttps://drive.google.com/drive/folders/{raiz}")
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    main()

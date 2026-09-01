#!/usr/bin/env python3
"""
Baja una carpeta COMPARTIDA de Google Drive (link público) sin credenciales.

Reemplaza a `hilton-drive-pull.sh`, que era de Mac y en Windows fallaba por dos
motivos que costaron una tarde el 31-08-2026:

  · llamaba a `/usr/bin/python3`, que en Git Bash no existe;
  · el listado salía con CRLF y el `\\r` se colaba dentro del nombre del archivo.
    Windows no admite ese carácter y lo sustituía por `_`, así que todo quedaba
    guardado como `foto.jpg_` y ningún script lo encontraba después.

Lee el visor público (`embeddedfolderview`), que no pide autenticación, y baja
cada archivo con su nombre real. Es idempotente: lo ya bajado no se repite.

Uso:
    python scripts/drive-carpeta.py <ID_CARPETA> <destino>
        [--solo .jpg,.png]      # extensiones a bajar
        [--miniaturas]          # baja miniaturas de 320 px en vez de originales
        [--limite N]

⭐ Las miniaturas son el truco para revisar una sesión de 353 fotos sin bajar
   12 GB: se hace una hoja de contactos y solo se bajan enteras las que sirven.
"""
import argparse
import html
import re
import sys
import urllib.request
from pathlib import Path

VISOR = "https://drive.google.com/embeddedfolderview?id={}#list"
DESCARGA = "https://drive.usercontent.google.com/download?id={}&export=download&confirm=t"
MINIATURA = "https://drive.google.com/thumbnail?id={}&sz=w320"

# Windows no admite estos caracteres en un nombre de archivo.
PROHIBIDOS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def listar(folder_id):
    """(id, nombre) de cada archivo, leídos del visor público."""
    with urllib.request.urlopen(VISOR.format(folder_id)) as r:
        src = r.read().decode("utf-8", "replace")
    pares = re.findall(r'id="entry-([-\w]{25,})".*?flip-entry-title">([^<]+)</div>', src, re.S)
    return [(fid, html.unescape(n).strip()) for fid, n in pares]


def seguro(nombre):
    """Nombre válido en cualquier sistema: sin CR/LF ni caracteres prohibidos."""
    return PROHIBIDOS.sub("-", nombre).strip().rstrip(". ") or "sin-nombre"


def ordenar(pares):
    """Ordena por el número final del nombre cuando lo hay (foto-2 antes que foto-10)."""
    def clave(t):
        m = re.search(r"(\d+)\.\w+$", t[1])
        return (0, int(m.group(1))) if m else (1, 0)
    return sorted(pares, key=clave)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("destino")
    ap.add_argument("--solo", default="", help="extensiones separadas por coma, p.ej. .jpg,.png")
    ap.add_argument("--miniaturas", action="store_true")
    ap.add_argument("--limite", type=int, default=0)
    a = ap.parse_args()

    dst = Path(a.destino); dst.mkdir(parents=True, exist_ok=True)
    pares = ordenar(listar(a.carpeta))
    if a.solo:
        exts = tuple(e.strip().lower() for e in a.solo.split(",") if e.strip())
        pares = [p for p in pares if p[1].lower().endswith(exts)]
    if a.limite:
        pares = pares[:a.limite]

    print(f"{len(pares)} archivos en la carpeta")
    bajados = saltados = fallos = 0
    for i, (fid, nombre) in enumerate(pares, 1):
        salida = dst / seguro(nombre)
        if a.miniaturas:
            salida = salida.with_suffix(".jpg")
        if salida.exists() and salida.stat().st_size > 1024:
            saltados += 1
            continue
        url = (MINIATURA if a.miniaturas else DESCARGA).format(fid)
        try:
            urllib.request.urlretrieve(url, salida)
            kb = salida.stat().st_size // 1024
            print(f"[{i}/{len(pares)}] {salida.name} — {kb} KB")
            bajados += 1
        except Exception as e:                      # noqa: BLE001
            print(f"[{i}/{len(pares)}] {nombre} — FALLÓ: {e}", file=sys.stderr)
            fallos += 1

    print(f"\n{bajados} bajados · {saltados} ya estaban · {fallos} fallos → {dst}")


if __name__ == "__main__":
    main()

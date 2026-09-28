#!/usr/bin/env python3
"""BETWEEN · carta oficial APROBADA (28-09-2026) — sube PDF + editables a la carpeta de Eli.

Destino: la carpeta que dejó Eli con el Word y las referencias (1gAZNJkaw5SKAHEmLo1yIctD-MNCE1p6v)
  └ CARTA BETWEEN · EDITABLES APROBADOS 28-09
      ├ OPCION A … D  →  BW-CARTA-BETWEEN-OPCION-X.ai (UN archivo: CMYK, una mesa y una capa por hoja)
      │                  + BW-CARTA-BETWEEN-OPCION-X.pdf (sale de ese mismo .ai)
      │   (corrección de Eli 28-09: nada de un .ai por hoja; la subcarpeta «EDITABLES AI» se borra)
      └ ILUSTRACIONES VECTORIALES  →  los dibujos a mano y el logo trazados (SVG)
El token del estudio (drive.file) SÍ escribe en esa carpeta (probado 28-09). Si un archivo ya
existe con el mismo nombre en su carpeta, se reemplaza (no duplica).

    python scripts/between-carta-oficial-subir.py [A B C D]
"""
import os, pathlib, sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ED = RAIZ / "out/hilton/between/carta-oficial/r4/editable"
VEC = RAIZ / "public/assets/hilton/between/carta/vector"
PADRE = "1gAZNJkaw5SKAHEmLo1yIctD-MNCE1p6v"
NOMBRE = "CARTA BETWEEN · EDITABLES APROBADOS 28-09"
TIPOS = {".pdf": "application/pdf", ".ai": "application/postscript", ".svg": "image/svg+xml"}


def servicio():
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def buscar(d, nombre, padre, carpeta=False):
    q = f"name = '{nombre}' and '{padre}' in parents and trashed = false"
    if carpeta:
        q += " and mimeType = 'application/vnd.google-apps.folder'"
    r = d.files().list(q=q, fields="files(id)", supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
    return r["files"][0]["id"] if r["files"] else None


def carpeta(d, nombre, padre):
    return buscar(d, nombre, padre, True) or d.files().create(
        body={"name": nombre, "mimeType": "application/vnd.google-apps.folder", "parents": [padre]},
        fields="id", supportsAllDrives=True).execute()["id"]


def subir(d, archivo, padre):
    media = MediaFileUpload(str(archivo), mimetype=TIPOS[archivo.suffix], resumable=True)
    viejo = buscar(d, archivo.name, padre)
    if viejo:
        d.files().update(fileId=viejo, media_body=media, supportsAllDrives=True).execute()
    else:
        d.files().create(body={"name": archivo.name, "parents": [padre]}, media_body=media,
                         fields="id", supportsAllDrives=True).execute()
    print("  ↑", archivo.name, f"({archivo.stat().st_size / 1e6:.1f} MB)")


def main():
    d = servicio()
    # el PDF de prueba de la D quedó suelto en la raíz: se saca de ahí
    suelto = buscar(d, "BW-CARTA-BETWEEN-OPCION-D.pdf", PADRE)
    if suelto:
        d.files().delete(fileId=suelto, supportsAllDrives=True).execute()
    raiz = carpeta(d, NOMBRE, PADRE)
    for op in (sys.argv[1:] or "ABCD"):
        c = carpeta(d, f"OPCION {op}", raiz)
        print(f"OPCION {op}")
        for ext in (".ai", ".pdf"):
            subir(d, ED / "maestro" / f"BW-CARTA-BETWEEN-OPCION-{op}{ext}", c)
        viejo = buscar(d, "EDITABLES AI", c, True)
        if viejo:
            d.files().delete(fileId=viejo, supportsAllDrives=True).execute()
            print("  ✗ EDITABLES AI (un .ai por hoja) borrada")
    if sys.argv[1:]:
        print(f"\nhttps://drive.google.com/drive/folders/{raiz}")
        return
    cv = carpeta(d, "ILUSTRACIONES VECTORIALES", raiz)
    print("ILUSTRACIONES VECTORIALES")
    for s in sorted(VEC.glob("*.svg")):
        subir(d, s, cv)
    print(f"\nhttps://drive.google.com/drive/folders/{raiz}")


if __name__ == "__main__":
    main()

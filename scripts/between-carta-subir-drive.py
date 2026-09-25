#!/usr/bin/env python3
"""BETWEEN · carta — sube las 3 opciones (25-09-2026) a la carpeta de referencias de Eli.

    python scripts/between-carta-subir-drive.py          # ronda 1 (raíz de la propuesta)
    python scripts/between-carta-subir-drive.py r2       # ronda 2 → subcarpeta «RONDA 2»
    python scripts/between-carta-subir-drive.py r3       # ronda 3 → subcarpeta «RONDA 3»
    python scripts/between-carta-subir-drive.py r4       # ronda 4 (sólo opción C) → «RONDA 4»

Destino: «referencias carta BW DISEÑO» (1QddD1LjdwE1rbp2AMACacNYXn8kT1bQo)
  └ PROPUESTA CARTA BW 3 OPCIONES 25-09 / OPCION A|B|C / <PNG + PDF de cada hoja>
    + la hoja de comparación en JPG y el index.html.
Si un archivo ya existe con el mismo nombre, se reemplaza (no duplica).
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
OUT = RAIZ / "out/hilton/between/carta-opciones"
PADRE = "1QddD1LjdwE1rbp2AMACacNYXn8kT1bQo"
NOMBRE = "PROPUESTA CARTA BW 3 OPCIONES 25-09"


def servicio():
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def carpeta(svc, nombre, padre):
    q = (f"name = '{nombre}' and '{padre}' in parents and trashed = false "
         "and mimeType = 'application/vnd.google-apps.folder'")
    r = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                         includeItemsFromAllDrives=True).execute().get("files", [])
    if r:
        return r[0]["id"]
    return svc.files().create(body={"name": nombre, "parents": [padre],
                                    "mimeType": "application/vnd.google-apps.folder"},
                              fields="id", supportsAllDrives=True).execute()["id"]


def subir(svc, ruta, destino, nombre=None):
    nombre = nombre or ruta.name
    q = f"name = '{nombre}' and '{destino}' in parents and trashed = false"
    prev = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                            includeItemsFromAllDrives=True).execute().get("files", [])
    media = MediaFileUpload(str(ruta), resumable=True)
    if prev:
        f = svc.files().update(fileId=prev[0]["id"], media_body=media,
                               fields="id,parents", supportsAllDrives=True).execute()
    else:
        f = svc.files().create(body={"name": nombre, "parents": [destino]}, media_body=media,
                               fields="id,parents", supportsAllDrives=True).execute()
    ok = destino in (f.get("parents") or [])
    print(f"{'✓' if ok else '⚠️ FUERA DE LUGAR'} {nombre}")


def main():
    ronda = sys.argv[1] if len(sys.argv) > 1 else ""
    svc = servicio()
    raiz = carpeta(svc, NOMBRE, PADRE)
    out, pref, etiqueta = OUT, "BW-CARTA-OP", ""
    if ronda in ("r2", "r3", "r4"):
        n = ronda[1]
        raiz = carpeta(svc, f"RONDA {n}", raiz)
        out, pref, etiqueta = OUT / ronda, f"BW-CARTA-R{n}-OP", f" R{n}"
    print("carpeta:", f"https://drive.google.com/drive/folders/{raiz}")
    for k in ("C" if ronda == "r4" else "ABC"):
        sub = carpeta(svc, f"OPCION {k}", raiz)
        for ext in ("png", "pdf"):
            for f in sorted((out / ext).glob(f"{pref}{k}-*.{ext}")):
                subir(svc, f, sub)
    subir(svc, out / "_hoja.jpg", raiz, f"BW CARTA{etiqueta} - COMPARACION 3 OPCIONES (filas A B C).jpg")
    subir(svc, out / "index.html", raiz, f"BW CARTA{etiqueta} - comparacion.html")


if __name__ == "__main__":
    main()

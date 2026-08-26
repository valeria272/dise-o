#!/usr/bin/env python3
"""
Sube las 8 piezas de REVEX septiembre 2026 a Drive, dentro de
GRUPO REVEX / 2026 / 9. Septiembre / DISEÑO PAID / v2

Usa el token OAuth compartido del monorepo con los 6 scopes completos.
NUNCA pedir un subconjunto: degrada el token de todos los proyectos.

Uso: ~/copylab-venv/bin/python3 scripts/revex-sep-subir-v2.py [--dry-run]
"""
import os, pathlib, sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
TOKEN     = pathlib.Path(str(_token_google()))
CARPETA   = pathlib.Path(str(_RAIZ / "out/revex/sep2026"))
DISENO_PAID = "1uMPBBoOpspRKBEqtiZOElJuMEDuaisl2"
NOMBRE_V2 = "v2"
DRY = "--dry-run" in sys.argv


def creds():
    c = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        faltan = set(SCOPES) - set(c.scopes or [])
        if faltan:
            sys.exit(f"ABORTA: el refresco perdió scopes {faltan}. No se guarda el token.")
        TOKEN.write_text(c.to_json())
        print("token refrescado, 6 scopes intactos")
    return c


def main():
    svc = build("drive", "v3", credentials=creds())

    # ¿ya existe la carpeta v2? si no, se crea
    r = svc.files().list(
        q=f"'{DISENO_PAID}' in parents and name='{NOMBRE_V2}' "
          f"and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id,name)", supportsAllDrives=True).execute()
    if r.get("files"):
        v2 = r["files"][0]["id"]; print(f"carpeta v2 ya existe: {v2}")
    else:
        v2 = svc.files().create(
            body={"name": NOMBRE_V2, "mimeType": "application/vnd.google-apps.folder",
                  "parents": [DISENO_PAID]},
            fields="id", supportsAllDrives=True).execute()["id"]
        print(f"carpeta v2 creada: {v2}")

    archivos = sorted(CARPETA.glob("rvx_*.png")) + [CARPETA / "LEEME.md"]
    archivos = [a for a in archivos if a.exists()]
    print(f"{len(archivos)} archivos → v2")
    if DRY:
        for a in archivos: print(f"    (dry) {a.name}  {a.stat().st_size//1024} KB")
        return

    existentes = {}
    r = svc.files().list(q=f"'{v2}' in parents and trashed=false",
                         fields="files(id,name)", pageSize=200,
                         supportsAllDrives=True).execute()
    for f in r.get("files", []):
        existentes[f["name"]] = f["id"]

    for a in archivos:
        mime = "image/png" if a.suffix == ".png" else "text/markdown"
        media = MediaFileUpload(str(a), mimetype=mime, resumable=True)
        if a.name in existentes:
            f = svc.files().update(fileId=existentes[a.name], media_body=media,
                                   fields="id,name,size", supportsAllDrives=True).execute()
            print(f"    ↻ {f['name']} ({int(f.get('size',0))//1024} KB) reemplazado")
        else:
            f = svc.files().create(
                body={"name": a.name, "parents": [v2]}, media_body=media,
                fields="id,name,size", supportsAllDrives=True).execute()
            print(f"    ✓ {f['name']} ({int(f.get('size',0))//1024} KB)")
    print(f"\nLINK: https://drive.google.com/drive/folders/{v2}")


if __name__ == "__main__":
    main()

"""Sube las piezas de paid a las carpetas de Drive de cada cliente.

Sube los PNG DIRECTO a la carpeta del mes, sin subcarpetas: criterio de Valeria
(25-08-2026) — "sin tanta subcarpeta, hazlo directo y fácil". Si un archivo con el
mismo nombre ya está, lo reemplaza en vez de duplicarlo.
Usa el token OAuth compartido del monorepo con los 6 scopes completos
(NUNCA pedir un subconjunto: degrada el token de todos los proyectos).

Uso: ~/copylab-venv/bin/python3 scripts/subir-piezas-drive.py [--dry-run]
"""
import pathlib, sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
TOKEN = pathlib.Path(
    str(_token_google())
)
OUT = pathlib.Path(str(_RAIZ / "out"))

# Carpetas de destino: los PNG van DIRECTO acá, sin subcarpeta intermedia
DESTINOS = [
    # DISEÑO PAID, dentro de GRUPO REVEX / 2026 / 9. Septiembre
    ("REVEX", "1uMPBBoOpspRKBEqtiZOElJuMEDuaisl2", OUT / "revex/sep2026"),
    # Diseño Casablanca Septiembre 2026, dentro de PISOS CASABLANCA / 2026 / 8. Septiembre
    ("CASABLANCA", "13pOfaekruRWq8PEHrG0be20Bq6eG4yCB", OUT / "casablanca/sep2026"),
]
# Renombres a aplicar EN DRIVE antes de subir. Si el archivo local cambió de
# nombre y el de Drive no, `files().create` haría un duplicado y se perderían los
# comentarios anclados de la diseñadora. Renombrando primero, el update calza por
# nombre y el archivo conserva su ID, su link y su hilo de comentarios.
RENOMBRES = {
    # ronda 2: el carrusel del showroom cambió de orden (abre la fachada), así que
    # el número por sí solo ya no dice qué es cada tarjeta
    "cb_sep_c2-showroom-1_feed.png": "cb_sep_c2-showroom-1-fachada_feed.png",
    "cb_sep_c2-showroom-1_story.png": "cb_sep_c2-showroom-1-fachada_story.png",
    "cb_sep_c2-showroom-2_feed.png": "cb_sep_c2-showroom-2-interior_feed.png",
    "cb_sep_c2-showroom-2_story.png": "cb_sep_c2-showroom-2-interior_story.png",
    "cb_sep_c2-showroom-3_feed.png": "cb_sep_c2-showroom-3-direccion_feed.png",
    "cb_sep_c2-showroom-3_story.png": "cb_sep_c2-showroom-3-direccion_story.png",
}

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
    for marca, parent, carpeta in DESTINOS:
        archivos = sorted(carpeta.glob("*.png"))
        print(f"\n=== {marca}: {len(archivos)} piezas → carpeta {parent}")
        if DRY:
            for a in archivos:
                print(f"    (dry) {a.name}")
            continue
        # lo que ya está arriba, para reemplazar en vez de duplicar
        existentes = {}
        r = svc.files().list(
            q=f"'{parent}' in parents and trashed=false",
            fields="files(id,name)", pageSize=200, supportsAllDrives=True,
        ).execute()
        for f in r.get("files", []):
            existentes[f["name"]] = f["id"]

        # renombrar en Drive lo que cambió de nombre, para reemplazar y no duplicar
        for viejo, nuevo in RENOMBRES.items():
            if viejo in existentes and nuevo not in existentes:
                svc.files().update(
                    fileId=existentes[viejo], body={"name": nuevo},
                    fields="id,name", supportsAllDrives=True,
                ).execute()
                existentes[nuevo] = existentes.pop(viejo)
                print(f"    ✎ {viejo} → {nuevo}")

        for a in archivos:
            media = MediaFileUpload(str(a), mimetype="image/png", resumable=True)
            if a.name in existentes:
                f = svc.files().update(
                    fileId=existentes[a.name], media_body=media,
                    fields="id,name,size", supportsAllDrives=True,
                ).execute()
                print(f"    ↻ {f['name']} ({int(f.get('size', 0)) // 1024} KB) reemplazado")
            else:
                f = svc.files().create(
                    body={"name": a.name, "parents": [parent]}, media_body=media,
                    fields="id,name,size", supportsAllDrives=True,
                ).execute()
                print(f"    ✓ {f['name']} ({int(f.get('size', 0)) // 1024} KB)")
        print(f"  LINK {marca}: https://drive.google.com/drive/folders/{parent}")


if __name__ == "__main__":
    main()

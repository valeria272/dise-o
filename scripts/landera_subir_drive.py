#!/usr/bin/env python3
"""Sube la entrega de Landera a la carpeta de Drive del proyecto.

⚠️ Carga SIEMPRE los scopes que el token ya trae. Pedirle un subconjunto y
dejar que se refresque devuelve un token recortado, y eso deja sin Sheets ni
Calendar a todo el monorepo (pasó el 29-07-2026).
"""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _entorno
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

CARPETA = "1fBPC6EYUB4QvdTHRE_ERvfWUOnK5L1Q5"
RAIZ = Path(__file__).resolve().parent.parent
ARCHIVOS = [
    (RAIZ/"out/landera/manual/LANDERA-manual-de-marca.pdf", "application/pdf"),
    (RAIZ/"out/landera/manual/LANDERA-guia-de-tono.pdf",    "application/pdf"),
    (RAIZ/"out/landera/manual/LANDERA-editables.zip",       "application/zip"),
]

ruta = _entorno.token_google()
scopes = json.load(open(ruta)).get("scopes")          # los que ya tiene, ni uno menos
cred = Credentials.from_authorized_user_file(ruta, scopes)
if cred.expired and cred.refresh_token:
    cred.refresh(Request())
    nuevos = set(cred.scopes or [])
    if not set(scopes) <= nuevos:                     # guardia anti-degradación
        sys.exit(f"El refresco perdió scopes ({set(scopes)-nuevos}); NO se guarda el token.")
    Path(ruta).write_text(cred.to_json())

drive = build("drive", "v3", credentials=cred)
for f, mime in ARCHIVOS:
    if not f.exists():
        print(f"  ✗ falta {f.name}"); continue
    # si ya existe uno con ese nombre en la carpeta, se reemplaza el contenido
    prev = drive.files().list(
        q=f"name='{f.name}' and '{CARPETA}' in parents and trashed=false",
        fields="files(id)", supportsAllDrives=True).execute().get("files", [])
    media = MediaFileUpload(str(f), mimetype=mime, resumable=True)
    if prev:
        r = drive.files().update(fileId=prev[0]["id"], media_body=media,
                                 fields="id,name,webViewLink",
                                 supportsAllDrives=True).execute()
        print(f"  ↻ actualizado  {r['name']}  {r['webViewLink']}")
    else:
        r = drive.files().create(
            body={"name": f.name, "parents": [CARPETA]}, media_body=media,
            fields="id,name,webViewLink", supportsAllDrives=True).execute()
        print(f"  ✓ subido       {r['name']}  {r['webViewLink']}")

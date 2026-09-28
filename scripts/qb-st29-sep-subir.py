#!/usr/bin/env python3
"""QB · ST 29-09 (Trivia de brindis) — cambio de texto «tomar» → «beber».

Pedido del cliente vía Nicolás Ávila (Slack, 28-09-2026). Reemplaza el contenido
de «ST n°2 s5.png» de Eli en QB / STS (1Ve22wlyaFlOMe4FGgyPw4J-nXKYiP4UU) conservando
el enlace; si el scope drive.file no lo deja, sube un archivo nuevo con el mismo nombre.
"""
import os, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PNG = RAIZ / "out/qb/sep/ST n°2 s5.png"
FILE_ID = "1vKJjlTfppwowyPhp-cVB8HGxlyj76g6v"
CARPETA = "1Ve22wlyaFlOMe4FGgyPw4J-nXKYiP4UU"

ruta = token_google()
creds = Credentials.from_authorized_user_file(str(ruta))
if not creds.valid:
    creds.refresh(Request()); pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
svc = build("drive", "v3", credentials=creds, cache_discovery=False)
media = MediaFileUpload(str(PNG), mimetype="image/png", resumable=True)
modo = sys.argv[1] if len(sys.argv) > 1 else "reemplazar"
if modo == "reemplazar":
    try:
        r = svc.files().update(fileId=FILE_ID, media_body=media, fields="id,name,size,modifiedTime",
                               supportsAllDrives=True).execute()
        print("REEMPLAZADO", r)
    except HttpError as e:
        print("NO SE PUDO REEMPLAZAR:", e.resp.status)
else:
    r = svc.files().create(body={"name": "ST n°2 s5.png", "parents": [CARPETA]}, media_body=media,
                           fields="id,name,size,webViewLink", supportsAllDrives=True).execute()
    print("SUBIDO NUEVO", r)

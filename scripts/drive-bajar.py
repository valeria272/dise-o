#!/usr/bin/env python3
"""Baja todos los archivos de una carpeta de Drive a un directorio local.
Uso: ~/copylab-venv/bin/python3 scripts/drive-bajar.py <folderId> <destino>"""
import io, os, pathlib, sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google as _token_google

SCOPES = ["https://www.googleapis.com/auth/calendar",
          "https://www.googleapis.com/auth/gmail.send",
          "https://www.googleapis.com/auth/gmail.modify",
          "https://www.googleapis.com/auth/gmail.labels",
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file"]

def creds():
    tok = pathlib.Path(str(_token_google()))
    c = Credentials.from_authorized_user_file(str(tok), SCOPES)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        faltan = set(SCOPES) - set(c.scopes or [])
        if faltan: sys.exit(f"ABORTA: el refresco perdió scopes {faltan}.")
        tok.write_text(c.to_json())
    return c

fid, destino = sys.argv[1], pathlib.Path(sys.argv[2])
destino.mkdir(parents=True, exist_ok=True)
d = build("drive", "v3", credentials=creds())
files = d.files().list(q=f"'{fid}' in parents and trashed=false",
                       fields="files(id,name,mimeType)", pageSize=200).execute()["files"]
for f in sorted(files, key=lambda x: x["name"]):
    if f["mimeType"] == "application/vnd.google-apps.folder": continue
    buf = io.BytesIO()
    dl = MediaIoBaseDownload(buf, d.files().get_media(fileId=f["id"]))
    done = False
    while not done: _, done = dl.next_chunk()
    (destino / f["name"]).write_bytes(buf.getvalue())
    print(f"  ✓ {f['name']}  {len(buf.getvalue())//1024} KB")

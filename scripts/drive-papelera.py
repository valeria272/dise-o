#!/usr/bin/env python3
"""Manda archivos de Drive a la PAPELERA (no los borra definitivamente).

    python scripts/drive-papelera.py <ID> [<ID> ...]

POR QUÉ EXISTE. El conector MCP de Drive responde "caller does not have
permission" sobre archivos que subió la app del estudio. Este script usa el
mismo token OAuth que `drive-subir.py`, que sí es dueño de lo que subió.

Es papelera, no borrado: se recupera desde Drive durante 30 días.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
import certifi  # noqa: E402
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
from google.auth.transport.requests import Request           # noqa: E402
from google.oauth2.credentials import Credentials            # noqa: E402
from googleapiclient.discovery import build                  # noqa: E402
from googleapiclient.errors import HttpError                 # noqa: E402

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

def main():
    ids = sys.argv[1:]
    if not ids:
        print("uso: drive-papelera.py <ID> [<ID> ...]"); return 1
    creds = Credentials.from_authorized_user_file(token_google(), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    svc = build("drive", "v3", credentials=creds)
    for fid in ids:
        try:
            meta = svc.files().get(fileId=fid, fields="name,trashed").execute()
            if meta.get("trashed"):
                print(f"  = {meta['name']}  (ya estaba en la papelera)"); continue
            svc.files().update(fileId=fid, body={"trashed": True}).execute()
            print(f"  x {meta['name']}  -> papelera")
        except HttpError as e:
            print(f"  ! {fid}  ERROR {e.resp.status}: {e._get_reason()}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

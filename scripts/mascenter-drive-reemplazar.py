#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reemplaza EN SITIO los reels 9:16 de Más Center octubre 2026 en Drive (v5, QA del 24-09-2026).

La v4 dejaba la última línea del titular bajo la franja que tapa Reels (420 px abajo, 180 px
a la derecha, según el brief). Esta versión sube los titulares; el montaje no cambia.

files().update(media_body=...) → mismo fileId, mismo link; la versión anterior queda en el
historial de Drive. Verifica el md5 de cada archivo contra el local.

Carpeta: PERFORMANCE/2026/OCTUBRE/ADS OCTUBRE
    https://drive.google.com/drive/folders/12rXhFTlWlBEof1ugHmSM52gmOxIktwgN

Correr:  ~/copylab-venv/bin/python3 scripts/mascenter-drive-reemplazar.py
Usa credentials/token-drive-serena.json (scope drive completo): el token del llavero es
drive.file y da 404 sobre archivos que no creó él.
"""
import hashlib, os, sys
from pathlib import Path
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

TOKEN = RAIZ / "credentials/token-drive-serena.json"
ORIGEN = RAIZ / "out/mascenter/2026-10/v5"

# fileId de cada pieza ya subida (leídos del Drive el 24-09-2026)
PIEZAS = [
    ("MASCENTER_P02_Reel_1080x1920.mp4", "1hkp0XHDU0QMPVRv6QBmWbhczntPic-kc", "video/mp4"),
    ("MASCENTER_P03_Reel_1080x1920.mp4", "1E6BrTiSQ1ANTKoWkiaJ0qVDxxAcqZfwe", "video/mp4"),
]


def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> int:
    creds = Credentials.from_authorized_user_file(str(TOKEN))
    if not creds.valid:
        creds.refresh(Request())
        TOKEN.write_text(creds.to_json())
    srv = build("drive", "v3", credentials=creds, cache_discovery=False)
    fallos = 0
    for nombre, fid, mime in PIEZAS:
        local = ORIGEN / nombre
        if not local.exists():
            print(f"✗ falta {local}"); fallos += 1; continue
        media = MediaFileUpload(str(local), mimetype=mime, resumable=True)
        r = srv.files().update(fileId=fid, media_body=media, supportsAllDrives=True,
                               fields="id,name,md5Checksum,modifiedTime").execute()
        ok = r.get("md5Checksum") == md5(local)
        print(f"{'✓' if ok else '✗ md5 distinto'} {r['name']}  {r['modifiedTime']}")
        fallos += 0 if ok else 1
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · OCTUBRE 2026 — sube los Reels DJ (MP4 + GIF) a `S<n> HILTON OCT 2026 / QB / FEED`.

Crea QB y FEED si la semana todavía no las tiene; si el archivo ya existe con ese nombre,
reemplaza su contenido (mismo ID y enlace). Verifica por md5.

    python scripts/qb-oct-reel-dj-drive.py 3 5            # sólo lista lo que ve
    python scripts/qb-oct-reel-dj-drive.py 3 5 --hacer
"""
import hashlib
import os
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

SEMANAS = {1: "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN", 2: "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh",
           3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz", 4: "1QBaEKSMFFn9EefWZQRWilzXUl6gsTxh7",
           5: "1fEkiPToyFK3rVK3M4ynPMdnHm5R21qZZ"}
HACER = "--hacer" in sys.argv
QUIERO = [int(a) for a in sys.argv[1:] if a.isdigit()]
K = dict(supportsAllDrives=True, includeItemsFromAllDrives=True)
TIPO = {".mp4": "video/mp4", ".gif": "image/gif"}

ruta = token_google()
creds = Credentials.from_authorized_user_file(str(ruta))
if not creds.valid:
    creds.refresh(Request())
    pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
svc = build("drive", "v3", credentials=creds, cache_discovery=False)


def hijos(padre):
    q = f"'{padre}' in parents and trashed = false"
    return svc.files().list(q=q, fields="files(id,name,mimeType,md5Checksum)", pageSize=200, **K).execute().get("files", [])


def carpeta(nombre, padre):
    for f in hijos(padre):
        if f["name"].strip() == nombre and "folder" in f["mimeType"]:
            return f["id"]
    if not HACER:
        print(f"  (crearía la carpeta {nombre})")
        return None
    r = svc.files().create(body={"name": nombre, "mimeType": "application/vnd.google-apps.folder", "parents": [padre]},
                           fields="id", supportsAllDrives=True).execute()
    print(f"  + carpeta {nombre}")
    return r["id"]


for n in QUIERO:
    print(f"== S{n}")
    qb = carpeta("QB", SEMANAS[n])
    feed = carpeta("FEED", qb) if qb else None
    ya = {f["name"]: f for f in hijos(feed)} if feed else {}
    for ext in (".mp4", ".gif"):
        nombre = f"Reel n°1 S{n} QB OCT 26{ext}"
        local = pathlib.Path(f"out/qb/oct/reel-dj-s{n}/entrega/{nombre}")
        md5 = hashlib.md5(local.read_bytes()).hexdigest()
        f = ya.get(nombre)
        print(f"  {nombre}: local {md5[:8]} · Drive {f['md5Checksum'][:8] if f else '—'}")
        if not HACER or (f and f["md5Checksum"] == md5):
            continue
        media = MediaFileUpload(str(local), mimetype=TIPO[ext], resumable=True)
        if f:
            r = svc.files().update(fileId=f["id"], media_body=media, fields="id,md5Checksum,mimeType", supportsAllDrives=True).execute()
        else:
            r = svc.files().create(body={"name": nombre, "parents": [feed]}, media_body=media,
                                   fields="id,md5Checksum,mimeType", supportsAllDrives=True).execute()
        print("    →", "md5 OK" if r["md5Checksum"] == md5 else "x md5 DISTINTO", r["mimeType"], f"https://drive.google.com/file/d/{r['id']}/view")

#!/usr/bin/env python3
"""QB · OCTUBRE 2026 · RONDA 31 (01-10) — reemplaza en Drive el carrusel AYCD (C2 S1).

Comentario del cliente en FEED!E14: tragos fuera de proporción en la G2 y G1 más simple.
Reemplaza el contenido de `S1 / QB / FEED / C2 S1 AYCD / C2 S1 N°1 y N°2` (mismo ID y
enlace) y verifica por md5.

    python scripts/qb-oct-r29-drive.py            # sólo lista lo que ve
    python scripts/qb-oct-r29-drive.py --hacer
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

S1 = "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN"
R = pathlib.Path("out/qb/oct/r31")
HACER = "--hacer" in sys.argv
K = dict(supportsAllDrives=True, includeItemsFromAllDrives=True)

ruta = token_google()
creds = Credentials.from_authorized_user_file(str(ruta))
if not creds.valid:
    creds.refresh(Request())
    pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
svc = build("drive", "v3", credentials=creds, cache_discovery=False)


def hijos(padre):
    q = f"'{padre}' in parents and trashed = false"
    return svc.files().list(q=q, fields="files(id,name,mimeType,md5Checksum)", pageSize=200, **K).execute().get("files", [])


def hijo(padre, nombre):
    for f in hijos(padre):
        if f["name"].strip() == nombre:
            return f
    sys.exit(f"x no encuentro «{nombre}» en {padre}: {[f['name'] for f in hijos(padre)]}")


aycd = hijo(hijo(hijo(S1, "QB")["id"], "FEED")["id"], "C2 S1 AYCD")
en_drive = {f["name"]: f for f in hijos(aycd["id"])}
print("C2 S1 AYCD:", sorted(en_drive))
for n in (1, 2):
    nombre = f"C2 S1 N°{n} QB OCT 26.png"
    local = R / nombre
    md5 = hashlib.md5(local.read_bytes()).hexdigest()
    f = en_drive.get(nombre) or sys.exit(f"x falta {nombre} en Drive")
    print(f"  {nombre}: Drive {f['md5Checksum'][:8]} · local {md5[:8]}", "(igual)" if f["md5Checksum"] == md5 else "")
    if HACER and f["md5Checksum"] != md5:
        r = svc.files().update(fileId=f["id"], media_body=MediaFileUpload(str(local), mimetype="image/png"),
                               fields="id,md5Checksum", supportsAllDrives=True).execute()
        print("    → reemplazado ·", "md5 OK" if r["md5Checksum"] == md5 else "x md5 DISTINTO", f"· https://drive.google.com/file/d/{r['id']}/view")

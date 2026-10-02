#!/usr/bin/env python3
"""QB · OCTUBRE 2026 · RONDA 37 (02-10) — sube a Drive el POST + ST «20 % dcto. almuerzo»
(FEED col. D de la S1), aprobados por Eli: «me gusta, guarda en tu memoria y en su
respectiva semana en Drive».

Van a `S1 HILTON OCT 2026 / QB / FEED` y `… / STS` con el número libre que sigue (no se
renombra nada de lo que ya está). Si el archivo ya existe con ese tema, se reemplaza su
contenido (mismo ID y enlace). Verifica por md5.

    python scripts/qb-oct-r37-drive.py            # sólo lista lo que ve
    python scripts/qb-oct-r37-drive.py --hacer
"""
import hashlib
import os
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

QB_S1 = "1jjzSls7cN0j_aHL9te3Wu7yxBWO1n-Ab"  # S1 HILTON OCT 2026 / QB
R = pathlib.Path("out/qb/oct/r37")
TEMA = "20 ALMUERZO"
PIEZAS = [("FEED", "Post", R / "Post S1 QB OCT 26 - 20 ALMUERZO.png"),
          ("STS", "ST", R / "ST S1 QB OCT 26 - 20 ALMUERZO.png")]
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


carpetas = {f["name"].strip(): f for f in hijos(QB_S1)}
print("S1 / QB:", sorted(carpetas))
for carpeta, prefijo, local in PIEZAS:
    c = carpetas.get(carpeta) or sys.exit(f"x no encuentro la carpeta {carpeta}")
    dentro = hijos(c["id"])
    print(f"\n{carpeta}:")
    for f in sorted(dentro, key=lambda f: f["name"]):
        print("   ", f["name"])
    md5 = hashlib.md5(local.read_bytes()).hexdigest()
    ya = next((f for f in dentro if TEMA in f["name"] and f["name"].startswith(prefijo)), None)
    if ya:
        nombre = ya["name"]
    else:
        usados = [int(m.group(1)) for f in dentro if (m := re.match(rf"{prefijo} n°(\d+) S1", f["name"]))]
        # en STS hay dos «n°1» (KV Sunset y Banco de Chile): se cuenta cuántas piezas hay
        nombre = f"{prefijo} n°{max(max(usados, default=0), len(usados)) + 1} S1 QB OCT 26 - {TEMA}.png"
    print(f"  → {nombre}", "(reemplaza)" if ya else "(nuevo)")
    if not HACER:
        continue
    media = MediaFileUpload(str(local), mimetype="image/png")
    if ya:
        r = svc.files().update(fileId=ya["id"], media_body=media, fields="id,md5Checksum", supportsAllDrives=True).execute()
    else:
        r = svc.files().create(body={"name": nombre, "parents": [c["id"]]}, media_body=media,
                               fields="id,md5Checksum", supportsAllDrives=True).execute()
    print("    ", "md5 OK" if r["md5Checksum"] == md5 else "x md5 DISTINTO", f"· https://drive.google.com/file/d/{r['id']}/view")

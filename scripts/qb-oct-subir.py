#!/usr/bin/env python3
"""QB · OCTUBRE 2026 — sube UNA pieza a su carpeta de semana y verifica el md5.

    S<n> HILTON OCT 2026 / QB / <ruta…> / <archivo>

Mismo mecanismo que `qb-oct-r9-subir-drive.py` (idempotente: un archivo con el mismo
nombre se REEMPLAZA y conserva el enlace), pero sin lista fija: la semana y la ruta
van por argumento, para ir subiendo pieza a pieza a medida que se terminan.
⚠️ Scope `drive.file`: verificar después con el conector de Drive.

Uso:
  python scripts/qb-oct-subir.py 1 FEED "out/qb/oct/r4/Post n°1 S1 QB OCT 26.png"
  python scripts/qb-oct-subir.py 2 STS  "out/qb/oct/r14/ST n°2 S2 QB OCT 26.png"
  python scripts/qb-oct-subir.py 2 "FEED/C1 S2 SUNSET" "…png"
"""
import hashlib
import mimetypes
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

SEMANAS = {  # carpetas S<n> HILTON OCT 2026 que creó Eli
    1: "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN",
    2: "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh",
    3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz",
    4: "1QBaEKSMFFn9EefWZQRWilzXUl6gsTxh7",
    5: "1fEkiPToyFK3rVK3M4ynPMdnHm5R21qZZ",
}


def servicio():
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def carpeta(svc, nombre, padre):
    q = (f"name = '{nombre}' and '{padre}' in parents and trashed = false "
         "and mimeType = 'application/vnd.google-apps.folder'")
    r = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                         includeItemsFromAllDrives=True).execute().get("files", [])
    if r:
        return r[0]["id"]
    return svc.files().create(
        body={"name": nombre, "parents": [padre],
              "mimeType": "application/vnd.google-apps.folder"},
        fields="id", supportsAllDrives=True).execute()["id"]


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    sem, ruta_c, local = int(sys.argv[1]), sys.argv[2], pathlib.Path(sys.argv[3])
    if not local.is_file():
        sys.exit(f"x falta {local}")
    svc = servicio()
    padre = carpeta(svc, "QB", SEMANAS[sem])
    for sub in [p for p in ruta_c.split("/") if p]:
        padre = carpeta(svc, sub, padre)
    nombre = local.name
    q = f"name = '{nombre}' and '{padre}' in parents and trashed = false"
    prev = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                            includeItemsFromAllDrives=True).execute().get("files", [])
    tipo = mimetypes.guess_type(nombre)[0] or "application/octet-stream"
    media = MediaFileUpload(str(local), mimetype=tipo, resumable=True)
    if prev:
        f = svc.files().update(fileId=prev[0]["id"], media_body=media,
                               fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
        accion = "reemplazado"
    else:
        f = svc.files().create(body={"name": nombre, "parents": [padre]}, media_body=media,
                               fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
        accion = "subido"
    md5 = hashlib.md5(local.read_bytes()).hexdigest()
    ok = padre in (f.get("parents") or []) and f.get("md5Checksum") == md5
    print(f"{'✓' if ok else '⚠️ REVISAR'} S{sem}/QB/{ruta_c}/{nombre} — {accion} · "
          f"md5 {'igual' if f.get('md5Checksum') == md5 else 'DISTINTO'} · "
          f"https://drive.google.com/file/d/{f['id']}/view")


if __name__ == "__main__":
    main()

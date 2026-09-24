#!/usr/bin/env python3
"""QB · OCTUBRE 2026 — sube las 11 historias a las carpetas de semana de Eli.

Eli (24-09-2026): «cuando termines puedes subirlo a grilla en la carpeta
correspondiente de drive que te dejé». Misma estructura que DT:

    S<n> HILTON OCT 2026 / QB / STS

La semana es la de la hoja STORIES de la grilla de QB. Las animadas van con MP4,
estática y GIF (el GIF es el que Eli pega en la grilla).

Idempotente: QB/STS las crea esta app y las vuelve a encontrar; un archivo con el
mismo nombre se REEMPLAZA (conserva el enlace). ⚠️ Scope `drive.file`: verificar
después con el conector MCP.

Uso:  python scripts/qb-oct-subir-drive.py [--solo "S3"]
"""
import argparse
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

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ENTREGA = RAIZ / "out/qb/oct/entrega"

SEMANAS = {  # carpetas S<n> HILTON OCT 2026 que creó Eli
    1: "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN",
    2: "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh",
    3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz",
    4: "1QBaEKSMFFn9EefWZQRWilzXUl6gsTxh7",
    5: "1fEkiPToyFK3rVK3M4ynPMdnHm5R21qZZ",
}

# (semana, subcarpeta, archivo) — en el orden de la grilla
PIEZAS = [(1, "STS", f"ST n°{n} S1 QB OCT 26.png") for n in (1, 2, 4, 5)] + [
    (2, "STS", "ST n°2 S2 QB OCT 26.png"),
    (2, "STS", "ST n°3 S2 QB OCT 26.png"),
    (3, "STS", "ST n°1 S3 QB OCT 26.png"),
    (3, "STS", "ST n°3 S3 QB OCT 26.png"),
    (3, "STS", "ST n°4 S3 QB OCT 26.mp4"),
    (3, "STS", "ST n°4 S3 QB OCT 26 (estática).png"),
    (3, "STS", "ST n°4 S3 QB OCT 26.gif"),
    (3, "STS", "ST n°5 S3 QB OCT 26.png"),
    (4, "STS", "ST n°1 S4 QB OCT 26.mp4"),
    (4, "STS", "ST n°1 S4 QB OCT 26 (estática).png"),
    (4, "STS", "ST n°1 S4 QB OCT 26.gif"),
]


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", default="")
    a = ap.parse_args()
    svc = servicio()
    cache = {}
    for sem, sub, nombre in PIEZAS:
        if a.solo and a.solo not in nombre:
            continue
        ruta = ENTREGA / nombre
        if not ruta.is_file():
            sys.exit(f"x falta {ruta}")
        if (sem, sub) not in cache:
            bw = cache.get((sem, "QB")) or carpeta(svc, "QB", SEMANAS[sem])
            cache[(sem, "QB")] = bw
            cache[(sem, sub)] = carpeta(svc, sub, bw)
        destino = cache[(sem, sub)]
        q = f"name = '{nombre}' and '{destino}' in parents and trashed = false"
        prev = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                                includeItemsFromAllDrives=True).execute().get("files", [])
        mime = {".gif": "image/gif", ".mp4": "video/mp4", ".png": "image/png"}[ruta.suffix]
        media = MediaFileUpload(str(ruta), mimetype=mime, resumable=True)
        if prev:
            f = svc.files().update(fileId=prev[0]["id"], media_body=media,
                                   fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
            accion = "reemplazado"
        else:
            f = svc.files().create(body={"name": nombre, "parents": [destino]}, media_body=media,
                                   fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
            accion = "subido"
        ok = destino in (f.get("parents") or [])
        print(f"{'✓' if ok else '⚠️ FUERA DE LUGAR'} S{sem}/QB/{sub}/{nombre} — {accion} · md5 {f.get('md5Checksum')}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""BETWEEN · OCTUBRE 2026 — sube la entrega aprobada a las carpetas oficiales de Eli.

Estructura que pidió Eli (24-09-2026), «como siempre lo hago»:

    10. OCTUBRE / S<n> HILTON OCT 2026 / BW / STS    ← historias
                                         BW / FEED   ← feed

La semana de cada pieza es la que le da la GRILLA (hoja STORIES y hoja FEED por
separado): el feed del 05-10 cae en la SEMANA 1 de la hoja FEED y el del 14-10 en
la SEMANA 4, aunque el calendario diga otra cosa.

Las GUIAS CM no se suben: son para el community manager, como en septiembre.

Idempotente: las carpetas BW/STS/FEED las crea esta app, así que las puede
volver a encontrar; y un archivo con el mismo nombre se REEMPLAZA (conserva el
enlace). ⚠️ Scope `drive.file`: verificar después con el conector MCP.

Uso:  python scripts/between-oct-subir-drive.py [--solo "BW ST 19-10"]
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
ENTREGA = RAIZ / "out/hilton/between/entrega-oct"

SEMANAS = {  # carpetas S<n> HILTON OCT 2026 que creó Eli
    1: "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN",
    2: "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh",
    3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz",
    4: "1QBaEKSMFFn9EefWZQRWilzXUl6gsTxh7",
    5: "1fEkiPToyFK3rVK3M4ynPMdnHm5R21qZZ",
}

# (semana, subcarpeta, archivo) — EN ORDEN de publicación
PIEZAS = [
    (1, "STS", "BW ST 01-10 Anuncio ganador concurso.png"),
    (1, "STS", "BW ST 02-10 Promos To Go POV.mp4"),
    (1, "STS", "BW ST 02-10 Promos To Go POV - PORTADA.png"),
    (1, "FEED", "BW FEED 05-10 Esa reunion podria ser un cafe.png"),
    (2, "STS", "BW ST 05-10 Paso por un cafe y.png"),
    (2, "STS", "BW ST 07-10 Cafe gratis por cumpleanos.png"),
    (2, "STS", "BW ST 08-10 Trivia Between.png"),
    (3, "STS", "BW ST 19-10 Cowork.png"),
    (3, "STS", "BW ST 20-10 Lo dicen ustedes.png"),
    (4, "FEED", "BW FEED 14-10 Espacios Between.png"),
    (4, "STS", "BW ST 27-10 Espacio para tu evento.png"),
    (5, "STS", "BW ST 28-10 Desayuno Bonjour.png"),
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
            bw = cache.get((sem, "BW")) or carpeta(svc, "BW", SEMANAS[sem])
            cache[(sem, "BW")] = bw
            cache[(sem, sub)] = carpeta(svc, sub, bw)
        destino = cache[(sem, sub)]
        q = f"name = '{nombre}' and '{destino}' in parents and trashed = false"
        prev = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                                includeItemsFromAllDrives=True).execute().get("files", [])
        media = MediaFileUpload(str(ruta), resumable=True)
        if prev:
            f = svc.files().update(fileId=prev[0]["id"], media_body=media,
                                   fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
            accion = "reemplazado"
        else:
            f = svc.files().create(body={"name": nombre, "parents": [destino]}, media_body=media,
                                   fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
            accion = "subido"
        ok = destino in (f.get("parents") or [])
        print(f"{'✓' if ok else '⚠️ FUERA DE LUGAR'} S{sem}/BW/{sub}/{nombre} — {accion} · md5 {f.get('md5Checksum')}")


if __name__ == "__main__":
    main()

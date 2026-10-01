#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — sube las 11 piezas a las carpetas de semana de Eli.

Eli (28-09-2026): «una vez listo déjalo en drive en la carpeta, créalas igual que
en dt, qb y bw». Misma estructura:

    S<n> HILTON OCT 2026 / PISO18 / {FEED, STS}

La semana es la de la GRILLA de Piso18 (fila 7 de FEED y STORIES). La animada va
con MP4 + GIF + portada (memoria `video-siempre-con-gif`). Las GUIAS de zona
segura NO se suben (R-32: la carpeta la ve el cliente).

Idempotente: PISO18/{FEED,STS} las crea esta app y las vuelve a encontrar; un archivo con el
mismo nombre se REEMPLAZA (conserva el enlace). ⚠️ Scope `drive.file`: verificar
después con el conector MCP.

Uso:  python scripts/p18-oct-subir-drive.py [--solo "23-10"] [--dry-run]
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
ENTREGA = RAIZ / "out/piso18/oct/entrega"

SEMANAS = {  # carpetas S<n> HILTON OCT 2026 que creó Eli
    1: "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN",
    2: "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh",
    3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz",
    4: "1QBaEKSMFFn9EefWZQRWilzXUl6gsTxh7",
    5: "1fEkiPToyFK3rVK3M4ynPMdnHm5R21qZZ",
}

# (semana, subcarpeta, archivo) — en el orden de la grilla
PIEZAS = [
    (2, "FEED", "P18 FEED 06-10 Arreglos florales.png"),
    (2, "FEED", "P18 FEED 09-10 Fechas 2027 1.png"),
    (2, "FEED", "P18 FEED 09-10 Fechas 2027 2.png"),
    (2, "STS", "P18 ST 05-10 Primavera en Piso18.mp4"),
    (2, "STS", "P18 ST 05-10 Primavera en Piso18.gif"),
    (2, "STS", "P18 ST 05-10 Primavera en Piso18 portada.png"),
    (2, "STS", "P18 ST 07-10 Estacion favorita.png"),
    (2, "STS", "P18 ST 09-10 Recuerdos de matrimonio.png"),
    (3, "FEED", "P18 FEED 13-10 Atardecer 1.png"),
    (3, "FEED", "P18 FEED 13-10 Atardecer 2.png"),
] + [(3, "FEED", f"P18 FEED 16-10 Tu proxima celebracion {n}.png") for n in range(1, 6)] + [
    (4, "FEED", f"P18 FEED 23-10 Estacion Tex Mex {n}.png") for n in range(1, 5)] + [
    (3, "STS", "P18 ST 15-10 Cumpleanos sonado.png"),  # aprobada 29-09
    # 01-10: ST 13 y 19-10 con el comentario del cliente, ST 21-10, FEED 20-10 animado y las
    # dos historias animadas con video real (MP4 + GIF + portada)
    (3, "STS", "P18 ST 13-10 Cuenta regresiva al 2027.png"),
    (3, "STS", "P18 ST 16-10 Equipo Piso18.mp4"),
    (3, "STS", "P18 ST 16-10 Equipo Piso18.gif"),
    (3, "STS", "P18 ST 16-10 Equipo Piso18 portada.png"),
    (4, "FEED", "P18 FEED 20-10 Cumpleanos en Piso18.mp4"),
    (4, "FEED", "P18 FEED 20-10 Cumpleanos en Piso18.gif"),
    (4, "FEED", "P18 FEED 20-10 Cumpleanos en Piso18 portada.png"),
    (4, "STS", "P18 ST 19-10 Fiesta de empresa fin de ano.png"),
    (4, "STS", "P18 ST 21-10 Estaciones de comida.png"),
    (5, "STS", "P18 ST 30-10 Broche perfecto.mp4"),
    (5, "STS", "P18 ST 30-10 Broche perfecto.gif"),
    (5, "STS", "P18 ST 30-10 Broche perfecto portada.png"),
    (4, "STS", "P18 ST 23-10 Evento corporativo.png"),
    (5, "FEED", "P18 FEED 27-10 Wedding planner.png"),
    (5, "STS", "P18 ST 27-10 Visita virtual.png"),
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
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    svc = None if a.dry_run else servicio()
    cache = {}
    for sem, sub, nombre in PIEZAS:
        if a.solo and a.solo not in nombre:
            continue
        ruta = ENTREGA / f"S{sem}" / sub / nombre
        if not ruta.is_file():
            sys.exit(f"x falta {ruta}")
        if a.dry_run:
            print(f"· S{sem}/PISO18/{sub}/{nombre} ({ruta.stat().st_size // 1024} KB)")
            continue
        if (sem, sub) not in cache:
            bw = cache.get((sem, "PISO18")) or carpeta(svc, "PISO18", SEMANAS[sem])
            cache[(sem, "PISO18")] = bw
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
        print(f"{'✓' if ok else '⚠️ FUERA DE LUGAR'} S{sem}/PISO18/{sub}/{nombre} — {accion} · md5 {f.get('md5Checksum')}")


if __name__ == "__main__":
    main()

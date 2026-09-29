#!/usr/bin/env python3
"""⛔ 29-09-2026: NO volver a correr. La grilla corrió las fechas y las historias se
RENUMERARON en Drive (`qb-oct-renumerar.py`): estos nombres son los viejos y
subirían duplicados. Para subir, `scripts/qb-oct-subir.py <semana> <ruta> <archivo>`.

QB · OCTUBRE 2026 — sube lo nuevo de la grilla (rondas 9–12, aprobado por Eli el
28-09) a las carpetas de semana:

    S<n> HILTON OCT 2026 / QB / STS            ← historias
    S<n> HILTON OCT 2026 / QB / FEED           ← post suelto
    S<n> HILTON OCT 2026 / QB / FEED / C1 S<n> <TEMA>   ← cada carrusel en su carpeta
                                                 (así nombra Eli: el tema va en la carpeta)

Mismo mecanismo que `qb-oct-subir-drive.py`: idempotente, un archivo con el mismo
nombre se REEMPLAZA (conserva el enlace). ⚠️ Scope `drive.file`: verificar después
con el conector de Drive.

Uso:  python scripts/qb-oct-r9-subir-drive.py [--solo "ST n°3"]
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
ENTREGA = RAIZ / "out/qb/oct/r9"

SEMANAS = {  # carpetas S<n> HILTON OCT 2026 que creó Eli
    1: "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN",
    2: "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh",
    3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz",
    4: "1QBaEKSMFFn9EefWZQRWilzXUl6gsTxh7",
    5: "1fEkiPToyFK3rVK3M4ynPMdnHm5R21qZZ",
}

# (semana, ruta de carpetas bajo QB, archivo)
PIEZAS = [
    (1, ["STS"], "ST n°3 S1 QB OCT 26.png"),                       # 07-10 cumpleaños
    (2, ["STS"], "ST n°1 S2 QB OCT 26.png"),                       # 12-10 pulpo
    (2, ["STS"], "ST n°5 S2 QB OCT 26.png"),                       # 16-10 primavera
    (4, ["STS"], "ST n°3 S4 QB OCT 26.png"),                       # 28-10 ¿este o este?
    (1, ["FEED", "C1 S1 AYCD"], "C1 S1 N°1 QB OCT 26.png"),        # 07-10 AYCD G1
    (1, ["FEED", "C1 S1 AYCD"], "C1 S1 N°2 QB OCT 26.png"),        # 07-10 AYCD G2
    (2, ["FEED", "C1 S2 SUNSET"], "C1 S2 N°1 QB OCT 26.png"),      # 12-10 Sunset G1
    (2, ["FEED", "C1 S2 SUNSET"], "C1 S2 N°2 QB OCT 26.png"),      # 12-10 Sunset G2
    (2, ["FEED"], "Post n°1 S2 QB OCT 26.png"),                    # 16-10 Afrodita
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
    for sem, ruta_c, nombre in PIEZAS:
        if a.solo and a.solo not in nombre:
            continue
        ruta = ENTREGA / nombre
        if not ruta.is_file():
            sys.exit(f"x falta {ruta}")
        padre = cache.get((sem, "QB")) or carpeta(svc, "QB", SEMANAS[sem])
        cache[(sem, "QB")] = padre
        clave = (sem, "QB")
        for sub in ruta_c:
            clave = clave + (sub,)
            if clave not in cache:
                cache[clave] = carpeta(svc, sub, padre)
            padre = cache[clave]
        q = f"name = '{nombre}' and '{padre}' in parents and trashed = false"
        prev = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                                includeItemsFromAllDrives=True).execute().get("files", [])
        media = MediaFileUpload(str(ruta), mimetype="image/png", resumable=True)
        if prev:
            f = svc.files().update(fileId=prev[0]["id"], media_body=media,
                                   fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
            accion = "reemplazado"
        else:
            f = svc.files().create(body={"name": nombre, "parents": [padre]}, media_body=media,
                                   fields="id,md5Checksum,parents", supportsAllDrives=True).execute()
            accion = "subido"
        ok = padre in (f.get("parents") or [])
        print(f"{'✓' if ok else '⚠️ FUERA DE LUGAR'} S{sem}/QB/{'/'.join(ruta_c)}/{nombre} — {accion} · md5 {f.get('md5Checksum')}")


if __name__ == "__main__":
    main()

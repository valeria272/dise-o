#!/usr/bin/env python3
"""QB · OCTUBRE 2026 · RONDA 19 (29-09 noche) — sube, reemplaza y renumera en Drive.

La ronda de Scarlette / Nicolás / Eli cambió formatos y fechas en la S1:
  · FEED 05-10 cumpleaños: de post estático a CARRUSEL de 4 → `C1 S1 CUMPLEAÑOS`.
    El post viejo se renombra «ANTES r18 - …» (no se borra).
  · FEED 06-10 AYCD: la carpeta `C1 S1 AYCD` pasa a `C2 S1 AYCD` (R-67, orden de la
    grilla) y sus archivos a `C2 S1 N°…`; la N°1 se reemplaza (botella de espumante).
  · FEED 09-10 CMR: carrusel nuevo → `C3 S1 CMR` (3 láminas).
  · STS S1: n°1 Banco, n°2 AYCD, n°4 (ahora CMR 40 % sábados) y n°5 Sunset se
    reemplazan; n°3 cumpleaños pasa a animada (mp4 + gif + estática) y el png viejo
    se renombra «ANTES r18 - …».
  · STS S2: la CMR «todos los días» que era la n°4 S1 quedó en el 15-10 → entra como
    n°5 S2; primavera, Sunset y CMR 17 se corren un número (n°7→8, 6→7, 5→6).
Renombrar conserva ID y enlace. Todo se verifica por md5.

    python scripts/qb-oct-r19-drive.py            # sólo lista lo que ve
    python scripts/qb-oct-r19-drive.py --hacer
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

S1, S2 = "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN", "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh"
R = pathlib.Path("out/qb/oct/r19")
HACER = "--hacer" in sys.argv
K = dict(supportsAllDrives=True, includeItemsFromAllDrives=True)


def servicio():
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


svc = servicio()


def hijos(padre, carpetas=None):
    q = f"'{padre}' in parents and trashed = false"
    if carpetas is True:
        q += " and mimeType = 'application/vnd.google-apps.folder'"
    return svc.files().list(q=q, fields="files(id,name,mimeType)", pageSize=200, **K).execute().get("files", [])


def carpeta(nombre, padre, crear=True):
    for f in hijos(padre, True):
        if f["name"] == nombre:
            return f["id"]
    if not crear or not HACER:
        return None
    return svc.files().create(body={"name": nombre, "parents": [padre],
                                    "mimeType": "application/vnd.google-apps.folder"},
                              fields="id", supportsAllDrives=True).execute()["id"]


def renombrar(padre, viejo, nuevo, prefijo=False):
    """prefijo=True: renombra todo archivo cuyo nombre EMPIEZA por `viejo`."""
    n = 0
    for f in hijos(padre):
        if (f["name"].startswith(viejo) if prefijo else f["name"] == viejo):
            dest = nuevo + f["name"][len(viejo):] if prefijo else nuevo
            print(f"  ↺ {f['name']}  →  {dest}")
            if HACER:
                svc.files().update(fileId=f["id"], body={"name": dest}, supportsAllDrives=True).execute()
            n += 1
    if not n:
        print(f"  · (no está) {viejo}")


def subir(padre, local, nombre=None, ruta=""):
    local = pathlib.Path(local)
    nombre = nombre or local.name
    if not HACER:
        print(f"  ↑ {ruta}/{nombre}")
        return
    prev = [f for f in hijos(padre) if f["name"] == nombre]
    tipo = mimetypes.guess_type(nombre)[0] or "application/octet-stream"
    media = MediaFileUpload(str(local), mimetype=tipo, resumable=True)
    if prev:
        f = svc.files().update(fileId=prev[0]["id"], media_body=media, fields="id,md5Checksum",
                               supportsAllDrives=True).execute()
        acc = "reemplazado"
    else:
        f = svc.files().create(body={"name": nombre, "parents": [padre]}, media_body=media,
                               fields="id,md5Checksum", supportsAllDrives=True).execute()
        acc = "subido"
    ok = f.get("md5Checksum") == hashlib.md5(local.read_bytes()).hexdigest()
    print(f"  {'✓' if ok else '⚠️ md5 DISTINTO'} {ruta}/{nombre} — {acc} · https://drive.google.com/file/d/{f['id']}/view")


def main():
    qb1, qb2 = carpeta("QB", S1, False), carpeta("QB", S2, False)
    feed1, sts1, sts2 = carpeta("FEED", qb1, False), carpeta("STS", qb1, False), carpeta("STS", qb2, False)
    print("S1/QB/FEED:", sorted(f["name"] for f in hijos(feed1)))
    print("S1/QB/STS:", sorted(f["name"] for f in hijos(sts1)))
    print("S2/QB/STS:", sorted(f["name"] for f in hijos(sts2)))
    print("\n— FEED S1")
    renombrar(feed1, "Post n°1 S1 QB OCT 26.png", "ANTES r18 - Post n°1 S1 QB OCT 26.png")
    cumple = carpeta("C1 S1 CUMPLEAÑOS", feed1)
    for i in range(1, 5):
        subir(cumple, R / f"C1 S1 N°{i} QB OCT 26.png", ruta="S1/FEED/C1 S1 CUMPLEAÑOS")
    aycd = carpeta("C1 S1 AYCD", feed1, False)
    if aycd:
        renombrar(aycd, "C1 S1 N°", "C2 S1 N°", prefijo=True)
        print("  ↺ carpeta C1 S1 AYCD → C2 S1 AYCD")
        if HACER:
            svc.files().update(fileId=aycd, body={"name": "C2 S1 AYCD"}, supportsAllDrives=True).execute()
    else:
        aycd = carpeta("C2 S1 AYCD", feed1)
    subir(aycd, R / "C2 S1 N°1 QB OCT 26.png", ruta="S1/FEED/C2 S1 AYCD")
    cmr = carpeta("C3 S1 CMR", feed1)
    for i in range(1, 4):
        subir(cmr, R / f"C3 S1 N°{i} QB OCT 26.png", ruta="S1/FEED/C3 S1 CMR")

    print("\n— STS S2 (entra la CMR «todos los días» el 15-10)")
    for a, b in ((7, 8), (6, 7), (5, 6)):
        renombrar(sts2, f"ST n°{a} S2 QB OCT 26", f"ST n°{b} S2 QB OCT 26", prefijo=True)
    subir(sts2, R / "_antes/ST n°4 S1 QB OCT 26.png", "ST n°5 S2 QB OCT 26.png", ruta="S2/STS")

    print("\n— STS S1")
    for n in (1, 2, 4, 5):
        subir(sts1, R / f"ST n°{n} S1 QB OCT 26.png", ruta="S1/STS")
    renombrar(sts1, "ST n°3 S1 QB OCT 26.png", "ANTES r18 - ST n°3 S1 QB OCT 26.png")
    for suf in (".mp4", ".gif", " (estática).png"):
        subir(sts1, R / f"ST n°3 S1 QB OCT 26{suf}", ruta="S1/STS")


if __name__ == "__main__":
    main()

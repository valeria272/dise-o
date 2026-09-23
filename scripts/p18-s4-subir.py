#!/usr/bin/env python3
"""Sube la S4 de PISO18 a su carpeta del Drive, con la estructura que pidió Eli.

    python scripts/p18-s4-subir.py --dry-run
    python scripts/p18-s4-subir.py

Encargo textual del 15-09-2026: «una vez terminados debes dejarlo en drive en la
S4, lo que es historias dejalos en carpeta llamada STS y para carruseles igual
crea una según C1 S4 PISO18».

Estructura que deja:

    S4 HILTON SEP 2026 / PISO18 /
        ├── C1 S4 PISO18/   C1 S4 N°1..4.png      (carrusel 22-09, 2250×2813)
        ├── STS/            ST N°2 S4.png          (historia 22-09)
        │                   ST N°3 S4.mp4          (historia animada 23-09)
        │                   ST N°4 S4.png          (historia 25-09)
        └── Post S4 PISO18 25-09.png               (post estático de feed 25-09)

⚠️ El post del 25-09 **no es historia ni carrusel**, así que no cabe en ninguna de
las dos carpetas que pidió Eli y queda en la raíz de PISO18. Si prefiere otra
ubicación, se mueve: es un `files().update` con `addParents`.

Nomenclatura: la de Eli, medida sobre su propio Drive en `docs/COMO-DISENA-EL-EQUIPO.md`
(`C<n> S<n> N°<n>` para slide de carrusel, `ST N°<n> S<n>` para historia). Y la
numeración de las historias es LA SUYA, la de las referencias que dejó: ST 2 es la
del 22-09, ST 3 la del 23-09 y ST 4 la del 25-09 — la ST 1 (21-09) queda fuera de
esta entrega por decisión suya, porque su celda no trae brief de diseño.

⚠️ El token tiene scope `drive.file`: puede CREAR archivos y carpetas, y
actualizar los que creó esta misma app. Si un archivo ya está con ese nombre y lo
subimos nosotros, se reemplaza para no romper el enlace que el cliente ya tenga.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google  # noqa: E402

from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

# ⚠️ Windows: la consola escribe en cp1252 y los ✓ revientan DESPUÉS de haber
# subido. Mismo arreglo que en magnific.py, qa/motor.py y llavero.py.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

# S4 HILTON SEP 2026 › PISO18
PISO18_S4 = "1xHin8e7Iw4gdGR5x-Z_akFCokOzy4wE3"
ENTREGA = pathlib.Path(str(_RAIZ / "out/piso18/s4/entrega"))

MIME = {".png": "image/png", ".jpg": "image/jpeg", ".mp4": "video/mp4",
        # ⚠️ Sin esto el GIF sube como `application/octet-stream` y Drive no
        # lo previsualiza: se ve como un archivo suelto para descargar.
        ".gif": "image/gif"}


def credenciales():
    tok = pathlib.Path(str(_token_google()))
    cred = Credentials.from_authorized_user_file(str(tok), SCOPES)
    if cred.expired and cred.refresh_token:
        cred.refresh(Request())
        # ⛔ No se vuelve a escribir el token acá: si Google devolviera menos
        # scopes, guardarlo degradaría los permisos de todo el monorepo. Pasó el
        # 29-07-2026 y mató Sheets en todos los proyectos.
    return cred


def carpeta(svc, nombre, padre, seco):
    q = (f"name = '{nombre}' and '{padre}' in parents and "
         f"mimeType = 'application/vnd.google-apps.folder' and trashed = false")
    hay = svc.files().list(q=q, fields="files(id,name)", pageSize=5).execute().get("files", [])
    if hay:
        print(f"  · carpeta «{nombre}» ya existe")
        return hay[0]["id"]
    if seco:
        print(f"  + CREARÍA carpeta «{nombre}»")
        return f"(nueva:{nombre})"
    meta = {"name": nombre, "mimeType": "application/vnd.google-apps.folder", "parents": [padre]}
    cid = svc.files().create(body=meta, fields="id").execute()["id"]
    print(f"  + carpeta «{nombre}» creada")
    return cid


def sube(svc, ruta: pathlib.Path, padre, seco):
    mime = MIME.get(ruta.suffix.lower(), "application/octet-stream")
    kb = ruta.stat().st_size // 1024
    if seco or str(padre).startswith("(nueva:"):
        print(f"    + SUBIRÍA {ruta.name}  ({kb} KB)")
        return
    q = f"name = '{ruta.name}' and '{padre}' in parents and trashed = false"
    hay = svc.files().list(q=q, fields="files(id)", pageSize=5).execute().get("files", [])
    media = MediaFileUpload(str(ruta), mimetype=mime, resumable=True)
    if hay:
        # Reemplaza el contenido conservando el ID — así el enlace que el cliente
        # ya tenga sigue funcionando. Es la regla de la cuenta.
        f = svc.files().update(fileId=hay[0]["id"], media_body=media,
                               fields="id,webViewLink").execute()
        print(f"    ↻ {ruta.name}  ({kb} KB)  {f['webViewLink']}")
    else:
        meta = {"name": ruta.name, "parents": [padre]}
        f = svc.files().create(body=meta, media_body=media,
                               fields="id,webViewLink").execute()
        print(f"    ✓ {ruta.name}  ({kb} KB)  {f['webViewLink']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="dice qué haría, sin tocar Drive")
    # ⭐ En una RONDA sólo cambian una o dos piezas. Subir las ocho igual funciona
    # —el contenido es idéntico— pero le mueve el `modifiedTime` a todas y quien
    # mire el Drive no distingue qué se corrigió. Con `--solo` se sube lo que
    # cambió y el resto queda con su fecha real.
    ap.add_argument("--solo", nargs="*", metavar="ARCHIVO",
                    help="sube sólo estos archivos (por nombre, con extensión)")
    a = ap.parse_args()
    filtro = set(a.solo) if a.solo else None

    if not ENTREGA.exists():
        sys.exit(f"✗ No está {ENTREGA}. Rinde la S4 antes de subir.")

    svc = build("drive", "v3", credentials=credenciales(), cache_discovery=False)
    print(f"PISO18 · S4 → carpeta {PISO18_S4}"
          + ("   [ENSAYO, no sube nada]" if a.dry_run else ""))

    # Las dos subcarpetas que pidió Eli, con su nombre textual.
    for sub in ("C1 S4 PISO18", "STS"):
        origen = ENTREGA / sub
        if not origen.is_dir():
            print(f"  ⚠ falta {origen}")
            continue
        cid = carpeta(svc, sub, PISO18_S4, a.dry_run)
        for f in sorted(origen.iterdir()):
            if f.is_file() and (filtro is None or f.name in filtro):
                sube(svc, f, cid, a.dry_run)

    # Lo que no es historia ni carrusel queda en la raíz de PISO18.
    for f in sorted(ENTREGA.iterdir()):
        if f.is_file() and (filtro is None or f.name in filtro):
            print("  · raíz de PISO18")
            sube(svc, f, PISO18_S4, a.dry_run)

    print("\nListo." if not a.dry_run else "\nEnsayo terminado — nada se subió.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

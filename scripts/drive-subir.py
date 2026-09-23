#!/usr/bin/env python3
"""Sube un archivo cualquiera a Drive y devuelve el enlace para verlo.

    python3 scripts/drive-subir.py <archivo> [--carpeta <ID>] [--nombre "..."] [--enlace]

POR QUÉ EXISTE. El repo tenía un `*-subir-drive.py` por cliente (between, revex,
casablanca, cava, rentas…) y todos hacen lo mismo. Éste es el genérico: sube UN
archivo, reemplaza si ya existe uno con el mismo nombre en esa carpeta —no
duplica— y te devuelve el enlace.

⚠️ **El conector MCP de Drive no sirve para esto.** Habría que mandar el archivo
en base64 dentro de la llamada: un mp4 de 13 MB son ~17 MB de texto por el chat.
Acá se sube desde el disco con `MediaFileUpload`, que además reintenta solo.

⚠️ **Los 6 scopes van completos, SIEMPRE.** Es el único token OAuth del monorepo
(Tasks Pega, ASISTENTE PERSONAL, SEO EXPERT, AGENTE VENTAS). Si se pide un
subconjunto y el token se refresca, Google emite uno recortado y se degradan los
permisos de todos los demás proyectos. Pasó el 29-07-2026.

⚠️ El scope es `drive.file`: la app sólo ve lo que ella misma creó. Por eso, si
la carpeta de destino no la creó esta app, Google responde 404 y el archivo cae
en «Mi unidad». No es un error del script — se avisa y se sigue.
"""
import argparse
import os
import pathlib
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402

from google.auth.transport.requests import Request           # noqa: E402
from google.oauth2.credentials import Credentials            # noqa: E402
from googleapiclient.discovery import build                  # noqa: E402
from googleapiclient.errors import HttpError                 # noqa: E402
from googleapiclient.http import MediaFileUpload             # noqa: E402

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

TIPOS = {
    ".mp4": "video/mp4", ".mov": "video/quicktime", ".png": "image/png",
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".pdf": "application/pdf",
    ".wav": "audio/wav", ".mp3": "audio/mpeg", ".zip": "application/zip",
    # ⚠️ Drive NO renderiza el .html: lo ofrece para descargar. Se declara el
    # tipo igual para que el archivo baje con la extensión correcta y abra en
    # el navegador con doble clic.
    ".html": "text/html", ".csv": "text/csv", ".txt": "text/plain",
    ".svg": "image/svg+xml", ".webp": "image/webp",
    # ⚠️ Sin esta línea el GIF sube como `application/octet-stream` y Drive no
    # lo previsualiza — el mismo tropiezo que tuvo `p18-s4-subir.py`.
    ".gif": "image/gif",
}


def servicio():
    ruta = pathlib.Path(str(token_google()))
    if not ruta.exists():
        sys.exit(f"✗ No encuentro el token de Google en {ruta}.\n"
                 f"  Corre:  python3 scripts/llavero.py abrir")
    cred = Credentials.from_authorized_user_file(str(ruta), SCOPES)
    if not cred.valid and cred.refresh_token:
        cred.refresh(Request())
        # Se reescribe con los 6 scopes o no se reescribe.
        if set(SCOPES).issubset(set(cred.scopes or [])):
            ruta.write_text(cred.to_json())
        else:
            print("  ⚠️ El refresco devolvió menos scopes de los 6 — NO se guarda "
                  "el token para no degradar a los otros proyectos.")
    return build("drive", "v3", credentials=cred, cache_discovery=False)


def existente(drive, nombre, carpeta):
    """Si ya hay uno con ese nombre, se REEMPLAZA. Una revisión con dos archivos
    que se llaman igual es cómo se aprueba el corte equivocado."""
    q = f"name = '{nombre}' and trashed = false"
    if carpeta:
        q += f" and '{carpeta}' in parents"
    try:
        r = drive.files().list(q=q, fields="files(id,name)", pageSize=5).execute()
        return (r.get("files") or [{}])[0].get("id")
    except HttpError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivo")
    ap.add_argument("--carpeta", help="ID de la carpeta de destino")
    ap.add_argument("--nombre", help="nombre en Drive (por defecto, el del archivo)")
    ap.add_argument("--enlace", action="store_true",
                    help="deja el archivo visible para cualquiera CON EL ENLACE")
    a = ap.parse_args()

    ruta = pathlib.Path(a.archivo)
    if not ruta.is_file():
        sys.exit(f"✗ No encuentro el archivo: {ruta}")
    nombre = a.nombre or ruta.name
    mime = TIPOS.get(ruta.suffix.lower(), "application/octet-stream")
    mb = ruta.stat().st_size / 1e6

    drive = servicio()
    medio = MediaFileUpload(str(ruta), mimetype=mime, resumable=True, chunksize=8 << 20)
    print(f"→ {nombre}  ({mb:.1f} MB · {mime})")

    viejo = existente(drive, nombre, a.carpeta)
    try:
        if viejo:
            print(f"  … ya existía, se reemplaza ({viejo})")
            f = drive.files().update(fileId=viejo, media_body=medio,
                                     fields="id,webViewLink").execute()
        else:
            cuerpo = {"name": nombre}
            if a.carpeta:
                cuerpo["parents"] = [a.carpeta]
            f = drive.files().create(body=cuerpo, media_body=medio,
                                     fields="id,webViewLink").execute()
    except HttpError as e:
        if a.carpeta and e.resp.status == 404:
            print("  ⚠️ Drive no deja escribir en esa carpeta con el scope "
                  "`drive.file`. Va a «Mi unidad».")
            f = drive.files().create(body={"name": nombre}, media_body=medio,
                                     fields="id,webViewLink").execute()
        else:
            raise

    if a.enlace:
        drive.permissions().create(
            fileId=f["id"], body={"type": "anyone", "role": "reader"}).execute()
        print("  ✓ visible para cualquiera con el enlace (sólo lectura)")

    print(f"\n  {f['webViewLink']}")


if __name__ == "__main__":
    sys.exit(main())

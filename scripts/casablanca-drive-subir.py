"""Sube la entrega de septiembre de Pisos Casablanca a su carpeta de Drive.

Solo AGREGA: nunca manda nada a la papelera. Si se corre dos veces, reemplaza el
contenido de los archivos que subió esta misma app en vez de duplicarlos.

Estructura que deja dentro de "8. Septiembre":

    Diseño Casablanca Septiembre 2026/
        C1 - Carrusel productos/   (4 slides x feed + story)
        C2 - Showroom Vitacura/    (3 slides x feed + story)

OJO con los scopes: siempre los 6 completos, nunca un subconjunto — un refresco
parcial deja el token recortado y rompe Sheets/Gmail para todo el monorepo.
"""
import json
import os
import sys
from pathlib import Path

import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
TOKEN = str(_token_google())

# PISOS CASABLANCA / 2026 / 8. Septiembre
SEPTIEMBRE = "1jUG18Hjnifb-1-XZaugZWTt13SxH-jLs"
RAIZ_NOMBRE = "Diseño Casablanca Septiembre 2026"
# Cada vuelta entra en su propia carpeta: la V1 queda intacta para poder comparar.
VERSION = "V2"

ENTREGA = Path(
    str(_RAIZ / "out/casablanca/septiembre")
)
GRUPOS = {
    "C1 - Carrusel productos": "cb_sep_c1-",
    "C2 - Showroom Vitacura": "cb_sep_c2-",
}


def svc():
    c = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not c.valid:
        c.refresh(Request())
        if set(SCOPES) - set(c.scopes or []):
            sys.exit("ABORTA: el refresco perdió scopes")
        json.dump(json.loads(c.to_json()), open(TOKEN, "w"), indent=2)
    return build("drive", "v3", credentials=c, cache_discovery=False)


def hijos(d, padre):
    return (
        d.files()
        .list(
            q=f"'{padre}' in parents and trashed=false",
            fields="files(id,name,mimeType)",
            pageSize=400,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        )
        .execute()
        .get("files", [])
    )


def carpeta(d, nombre, padre):
    """Devuelve la carpeta `nombre` bajo `padre`, creándola si no existe.

    Drive no siempre respeta el `parents` del create (pasó el 19-08-2026 con
    Tierra Calma: las carpetas se crearon colgando de otro nodo). Por eso
    después del create se verifica el padre real y, si hace falta, se mueve.
    """
    for f in hijos(d, padre):
        if f["name"] == nombre and f["mimeType"] == "application/vnd.google-apps.folder":
            print(f"  = carpeta ya existía: {nombre}")
            return f["id"]

    m = (
        d.files()
        .create(
            body={
                "name": nombre,
                "mimeType": "application/vnd.google-apps.folder",
                "parents": [padre],
            },
            fields="id,parents",
            supportsAllDrives=True,
        )
        .execute()
    )
    if padre not in (m.get("parents") or []):
        previos = ",".join(m.get("parents") or [])
        d.files().update(
            fileId=m["id"],
            addParents=padre,
            removeParents=previos,
            fields="id,parents",
            supportsAllDrives=True,
        ).execute()
        print(f"  ! {nombre}: Drive la colgó mal, se movió a su lugar")
    print(f"  + carpeta: {nombre}")
    return m["id"]


def sube(d, ruta, padre):
    tipo = "text/markdown" if ruta.suffix == ".md" else "image/png"
    media = MediaFileUpload(str(ruta), mimetype=tipo, resumable=True)
    existentes = {f["name"]: f["id"] for f in hijos(d, padre)}
    if ruta.name in existentes:
        d.files().update(
            fileId=existentes[ruta.name], media_body=media, supportsAllDrives=True
        ).execute()
        print(f"    ~ actualizado  {ruta.name}")
        return
    d.files().create(
        body={"name": ruta.name, "parents": [padre]},
        media_body=media,
        fields="id",
        supportsAllDrives=True,
    ).execute()
    print(f"    + subido       {ruta.name}")


def main():
    if not ENTREGA.is_dir():
        sys.exit(f"No existe la carpeta de entrega: {ENTREGA}")
    d = svc()

    raiz = carpeta(d, RAIZ_NOMBRE, SEPTIEMBRE)
    raiz = carpeta(d, VERSION, raiz)
    total = 0
    for nombre, prefijo in GRUPOS.items():
        sub = carpeta(d, nombre, raiz)
        archivos = sorted(ENTREGA.glob(f"{prefijo}*.png"))
        if not archivos:
            print(f"    (sin archivos para {prefijo}*)")
            continue
        for ruta in archivos:
            sube(d, ruta, sub)
            total += 1

    for extra in ("ENTREGA.md",):
        r = ENTREGA / extra
        if r.exists():
            sube(d, r, raiz)
            total += 1
    print(f"\nListo: {total} archivos en «{RAIZ_NOMBRE} / {VERSION}»")
    print(f"https://drive.google.com/drive/folders/{raiz}")


if __name__ == "__main__":
    main()

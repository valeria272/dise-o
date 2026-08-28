"""Sube los mailings de septiembre de CAVA Morandé a su carpeta de Drive.

Solo AGREGA: nunca manda nada a la papelera. Si se corre dos veces, reemplaza el
contenido de los archivos que subió esta misma app en vez de duplicarlos.

Destino — la carpeta que el propio brief declara en la fila 8
("SEPTIEMBRE: CARPETA DE DISEÑOS"), donde ya viven el Sheet de briefs y el KV:

    SEPTIEMBRE: CARPETA DE DISEÑOS/
        MAILS MAILCHIMP/
            CAVA_SEP_KV.png · CAVA_SEP_BRIEF4..9.png
            _LEEME-pendientes.md

⛔ NO se sube ninguna pieza que no haya pasado `qa/motor.py --marca cava`. La
franja del Ministerio de Salud es obligatoria por ley (Ley 19.925) y el QA es lo
único que garantiza que está: por eso acá se vuelve a correr antes de subir.

OJO con los scopes: siempre los 6 completos, nunca un subconjunto — un refresco
parcial deja el token recortado y rompe Sheets/Gmail para todo el monorepo.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
TOKEN = str(_token_google())

# CAVA / SEPTIEMBRE: CARPETA DE DISEÑOS  (fila 8 del brief mensual)
DESTINO = "1WwwVgNaoJzkIBbiia38YbAUxaqo73526"
SUBCARPETA = "MAILS MAILCHIMP"

ENTREGA = Path(str(_RAIZ / "out/cava/septiembre-2026"))
PIEZAS = ["CAVA_SEP_KV", "CAVA_SEP_BRIEF4", "CAVA_SEP_BRIEF5", "CAVA_SEP_BRIEF6",
          "CAVA_SEP_BRIEF7", "CAVA_SEP_BRIEF8", "CAVA_SEP_BRIEF9"]


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
    Tierra Calma: las carpetas quedaron colgando de otro nodo). Por eso después
    del create se verifica el padre real y, si hace falta, se mueve.
    """
    for f in hijos(d, padre):
        if f["name"] == nombre and f["mimeType"] == "application/vnd.google-apps.folder":
            print(f"  = carpeta ya existía: {nombre}")
            return f["id"]

    m = (
        d.files()
        .create(
            body={"name": nombre, "mimeType": "application/vnd.google-apps.folder",
                  "parents": [padre]},
            fields="id,parents",
            supportsAllDrives=True,
        )
        .execute()
    )
    if padre not in (m.get("parents") or []):
        previos = ",".join(m.get("parents") or [])
        d.files().update(fileId=m["id"], addParents=padre, removeParents=previos,
                         fields="id,parents", supportsAllDrives=True).execute()
        print(f"  ! {nombre}: Drive la colgó mal, se movió a su lugar")
    print(f"  + carpeta: {nombre}")
    return m["id"]


def sube(d, ruta, padre):
    tipo = "text/markdown" if ruta.suffix == ".md" else "image/png"
    media = MediaFileUpload(str(ruta), mimetype=tipo, resumable=True)
    existentes = {f["name"]: f["id"] for f in hijos(d, padre)}
    if ruta.name in existentes:
        d.files().update(fileId=existentes[ruta.name], media_body=media,
                         supportsAllDrives=True).execute()
        print(f"    ~ actualizado  {ruta.name}")
        return
    d.files().create(body={"name": ruta.name, "parents": [padre]},
                     media_body=media, fields="id", supportsAllDrives=True).execute()
    print(f"    + subido       {ruta.name}")


def qa_en_verde():
    """La compuerta: sin QA en verde no se sube nada."""
    r = subprocess.run(
        [sys.executable, str(_RAIZ / "qa/motor.py"), "--marca", "cava",
         "--textos", str(_RAIZ / "datos/cava-sep2026-textos.json"),
         *[str(ENTREGA / f"{p}.png") for p in PIEZAS]],
        capture_output=True, text=True, cwd=str(_RAIZ),
    )
    print(r.stdout[-400:] if r.stdout else r.stderr[-400:])
    return r.returncode == 0


def main():
    faltan = [p for p in PIEZAS if not (ENTREGA / f"{p}.png").exists()]
    if faltan:
        sys.exit(f"ABORTA: faltan piezas por generar: {', '.join(faltan)}")

    print("QA antes de subir…")
    if not qa_en_verde():
        sys.exit("ABORTA: el QA de cava no está en verde. No se sube nada.")

    d = svc()
    destino = carpeta(d, SUBCARPETA, DESTINO)
    for p in PIEZAS:
        sube(d, ENTREGA / f"{p}.png", destino)
    leeme = ENTREGA / "_LEEME-pendientes.md"
    if leeme.exists():
        sube(d, leeme, destino)
    print(f"\nListo → https://drive.google.com/drive/folders/{destino}")


if __name__ == "__main__":
    main()

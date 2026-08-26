#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Actualiza el reel de EBEMA CLICK en Drive con el render corregido.

Reemplaza el CONTENIDO de los mp4 que ya están en Drive (mismo fileId, mismo
link, nueva versión), en:
    EBEMA / ... / "graficas septiembre 26" / "reels"

Corregido el 24-08-2026: la píldora "✓ Agregado" del carrito se salía de su caja
en el formato feed. Ahora la UI del teléfono escala con el ancho de la pantalla.

Correr:  ~/copylab-venv/bin/python3 scripts/ebema-click-drive-actualizar.py

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

CARPETA_REELS = "1BZDFXHHNPmguARi7TB0FI27D4m4DuJiF"  # "reels" dentro de "graficas septiembre 26"
OUT = Path(str(_RAIZ / "out/ebema"))
PIEZAS = {
    "ebema_reel_click_feed.mp4": "1pgQ76HDvnuTwcH-jCfBj0pleu7waiE8J",
    "ebema_reel_click_story.mp4": "1feuLwy8PR9AmV0zIP9k5Pztf_SKHUXzj",
}


def svc():
    c = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not c.valid:
        c.refresh(Request())
        if set(SCOPES) - set(c.scopes or []):
            sys.exit("ABORTA: el refresco perdió scopes")
        json.dump(json.loads(c.to_json()), open(TOKEN, "w"), indent=2)
    return build("drive", "v3", credentials=c, cache_discovery=False)


def main():
    d = svc()
    for nombre, fid in PIEZAS.items():
        ruta = OUT / nombre
        if not ruta.is_file() or ruta.stat().st_size < 1_000_000:
            sys.exit(f"ABORTA: falta o está vacío el render {ruta}")
        media = MediaFileUpload(str(ruta), mimetype="video/mp4", resumable=True)
        try:
            d.files().update(
                fileId=fid, media_body=media, supportsAllDrives=True
            ).execute()
            print(f"  ~ actualizado (mismo link)  {nombre}")
        except Exception as e:
            # si el archivo no lo creó esta app, se sube uno nuevo a la misma carpeta
            print(f"  ! no se pudo reemplazar {nombre}: {e}\n    subiendo copia nueva…")
            d.files().create(
                body={"name": nombre, "parents": [CARPETA_REELS]},
                media_body=MediaFileUpload(str(ruta), mimetype="video/mp4", resumable=True),
                fields="id",
                supportsAllDrives=True,
            ).execute()
            print(f"  + subido  {nombre}")
    print("Listo: https://drive.google.com/drive/folders/" + CARPETA_REELS)


if __name__ == "__main__":
    main()

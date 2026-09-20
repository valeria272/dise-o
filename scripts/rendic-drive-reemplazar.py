#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reemplaza EN SITIO la entrega de Rendic octubre 2026 en Drive.

Sube la ronda 2 (correcciones de Diego del 08-09-2026: logo con fondo de color y
fotos subidas) sobre los MISMOS archivos que ya están en Drive:
mismo fileId, mismo link, y —lo importante— **los comentarios de Diego siguen
anclados**, así los puede cerrar sobre la versión corregida.

No borra nada: usa files().update(media_body=...), que crea una versión nueva y
deja la anterior en el historial de Drive.

Carpeta: ADS Rendic octubre / RENDIC - Octubre 2026
    https://drive.google.com/drive/folders/16iX-ydCrG_g9l-Wi5yFWlc3Y3cbP2bkk

Correr:  ~/copylab-venv/bin/python3 scripts/rendic-drive-reemplazar.py

Requiere el token de Google, que al 13-09-2026 NO está en esta máquina
(`python3 scripts/_entorno.py` → "token Google ✗"). Con el token puesto, corre solo.

OJO con los scopes: siempre los 6 completos, nunca un subconjunto — un refresco
parcial deja el token recortado y rompe Sheets/Gmail para todo el monorepo.
"""
import os, sys
from pathlib import Path
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
sys.path.insert(0, "scripts")
from _entorno import RAIZ, token_google
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/calendar",
          "https://www.googleapis.com/auth/gmail.send",
          "https://www.googleapis.com/auth/gmail.modify",
          "https://www.googleapis.com/auth/gmail.labels",
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file"]

ORIGEN = Path(str(RAIZ / "out/rendic/octubre-2026"))

# fileId de cada pieza ya subida (leídos del Drive el 08-09-2026)
PIEZAS = [
 ("RENDIC_P01_Feed_1080x1080.jpg",  "1n8Ze6GLGylneifAMQHJmmSaqElc3H3Vz", "image/jpeg"),
 ("RENDIC_P03_Feed_1080x1080.jpg",  "1Wj4K33nv22sA_T0ZULm9NpTgWWNOysje", "image/jpeg"),
 ("RENDIC_P04_Feed_1080x1080.jpg",  "17uM6GdTRFhNEMU40DM--xMz9BjOr5xPe", "image/jpeg"),
 ("RENDIC_P06_Feed_1080x1080.jpg",  "1j0-qycHxkrIowh7XG9QErGGSyOtCY9i_", "image/jpeg"),
 ("RENDIC_P07_Feed_1080x1080.jpg",  "1TPE9xGY8YJNy8uSpq1U-_UsVPPohJWkU", "image/jpeg"),
 ("RENDIC_P01_Story_1080x1920.jpg", "1cO88cTcXo_r_C49Vh1sfy03PKGaxOwFY", "image/jpeg"),
 ("RENDIC_P03_Story_1080x1920.jpg", "1rPf1CiQtapWHjGYa-RokRrpAnq1lcS1P", "image/jpeg"),
 ("RENDIC_P04_Story_1080x1920.jpg", "126Cdey2OLHAFOhm3QZcxo8imUBePYIzS", "image/jpeg"),
 ("RENDIC_P06_Story_1080x1920.jpg", "1CCvxEfG0t0sOcQbnqoljsaDtKnUd7RDa", "image/jpeg"),
 ("RENDIC_P07_Story_1080x1920.jpg", "1j3kGMqDMMFuk7eBrC78hvc8ehmNKw_XA", "image/jpeg"),
 ("RENDIC_P02_Reel_1080x1920.mp4",  "1FWLislB8ZP1wgvqnYXkh4jsZta5CmyCH", "video/mp4"),
 ("RENDIC_P05_Reel_1080x1920.mp4",  "1IPq23E4hNQ_mCAmzrrcbLaNWkrDlap5x", "video/mp4"),
 ("RENDIC_P08_Reel_1080x1920.mp4",  "1bL--SGmg9qSILhcs5oa8cRTgdzHbPUPO", "video/mp4"),
 ("_CONTACTO-entrega.png",          "1CQqK2fxmeSxhhbI-zI_q3ZBRwtr6o84r", "image/png"),
]

def servicio():
    ruta = token_google()
    if not ruta:
        sys.exit("✗ No hay token de Google en esta máquina.\n"
                 "  Ponlo en credentials/token.json o exporta COPYLAB_TOKEN.\n"
                 "  Verifica con: python3 scripts/_entorno.py")
    cred = Credentials.from_authorized_user_file(str(ruta), SCOPES)
    if cred.expired and cred.refresh_token:
        cred.refresh(Request())
        Path(str(ruta)).write_text(cred.to_json())
    return build("drive", "v3", credentials=cred)

def main():
    d = servicio()
    faltan = [n for n, _, _ in PIEZAS if not (ORIGEN / n).exists()]
    if faltan:
        sys.exit(f"✗ No están en {ORIGEN}: {faltan}")
    for nombre, fid, mime in PIEZAS:
        ruta = ORIGEN / nombre
        media = MediaFileUpload(str(ruta), mimetype=mime, resumable=True)
        d.files().update(fileId=fid, media_body=media, supportsAllDrives=True).execute()
        print(f"  ✓ {nombre}  ({ruta.stat().st_size/1024:.0f} KB)")
    print(f"\n{len(PIEZAS)} archivos reemplazados. Mismos links, comentarios intactos.")

if __name__ == "__main__":
    main()

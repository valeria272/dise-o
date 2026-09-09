#!/usr/bin/env python3
"""Sube el PPTX del moodboard a Drive CONVERTIDO a Google Slides y lo comparte.

    python scripts/dt-moodboard-subir.py [--archivo x.pptx] [--con correo@...]

⚠️ POR QUE EXISTE, y no se edita el moodboard de Eli directamente: NO hay conector
de Google Slides. El de Drive solo lee, crea archivos, renombra y comparte. Asi que
no se puede insertar una lamina dentro de su presentacion.

El camino que si funciona: subir el .pptx pidiendo mimeType de Slides, con lo que
Drive lo CONVIERTE, y en Slides se copian diapositivas entre presentaciones
conservando las imagenes. Eli pega las laminas que quiera en su moodboard.

⚠️ El scope del token es drive.file: la app solo ve lo que ella creo. El archivo
cae en «Mi unidad» de la cuenta del token y por eso hay que COMPARTIRLO.
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

from google.auth.transport.requests import Request        # noqa: E402
from google.oauth2.credentials import Credentials         # noqa: E402
from googleapiclient.discovery import build               # noqa: E402
from googleapiclient.http import MediaFileUpload          # noqa: E402

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
PPTX = ("application/vnd.openxmlformats-officedocument."
        "presentationml.presentation")
SLIDES = "application/vnd.google-apps.presentation"


def servicio():
    ruta = pathlib.Path(str(token_google()))
    cred = Credentials.from_authorized_user_file(str(ruta), SCOPES)
    if not cred.valid and cred.expired and cred.refresh_token:
        cred.refresh(Request())
        ruta.write_text(cred.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=cred)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archivo", default="out/hilton/dt/MoodBoard-DT-espacios.pptx")
    ap.add_argument("--nombre", default="MoodBoard DT — referencias por espacio")
    ap.add_argument("--con", default="elisabet.soto@copywriters.cl")
    # ⭐ Actualizar EN SITIO conserva el enlace que ya tiene la diseñadora.
    ap.add_argument("--actualizar", default=None, help="ID de la presentacion a reemplazar")
    a = ap.parse_args()

    if not os.path.exists(a.archivo):
        sys.exit("no existe: " + a.archivo)

    sv = servicio()
    media = MediaFileUpload(a.archivo, mimetype=PPTX, resumable=True)
    if a.actualizar:
        f = sv.files().update(
            fileId=a.actualizar, body={"name": a.nombre},
            media_body=media, fields="id,name,mimeType,webViewLink",
        ).execute()
        print("ACTUALIZADO en sitio (mismo enlace):", f["name"])
    else:
        f = sv.files().create(
            body={"name": a.nombre, "mimeType": SLIDES},   # <- la conversion
            media_body=media, fields="id,name,mimeType,webViewLink",
        ).execute()
        print("subido y convertido:", f["name"])
    print("  tipo:", f["mimeType"])
    print("  ver :", f.get("webViewLink"))

    if a.con and not a.actualizar:
        sv.permissions().create(
            fileId=f["id"], sendNotificationEmail=False,
            body={"type": "user", "role": "writer", "emailAddress": a.con},
        ).execute()
        print("  compartido con", a.con, "(editor)")
    return f


if __name__ == "__main__":
    main()

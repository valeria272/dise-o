#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sube las piezas del Cyber Wine Week de octubre a las carpetas de Coni.

Destino — las carpetas que ella misma pidió, dentro de CAVA / DISEÑO ia:

    OCTUBRE/
        CYBER CAVA VIP/        mails verticales de la previa (briefs 1–3)
        CYBER CAVA GENERAL/    mails verticales del cyber público (briefs 4–6)
        CYBER CAVA WHATSAPP/   las cuadradas 1:1 de las plantillas de ManyChat

Solo AGREGA: nunca manda nada a la papelera. Si se corre dos veces, reemplaza el
contenido de los archivos que subió esta misma app en vez de duplicarlos.

⛔ La compuerta: sin `qa/motor.py --marca cava` en verde no sube nada. La franja
del Ministerio de Salud es obligatoria por ley (Ley 19.925) y el QA es lo único
que garantiza que está — de hecho cazó que la cuantización a paleta con la que
se bajaba el peso dejaba el azul de la bandera en (53,84,107).
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from google.auth.transport.requests import Request          # noqa: E402
from google.oauth2.credentials import Credentials           # noqa: E402
from googleapiclient.discovery import build                 # noqa: E402
from googleapiclient.http import MediaFileUpload            # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google   # noqa: E402

# Siempre los 6 scopes completos, nunca un subconjunto: un refresco parcial deja
# el token recortado y rompe Sheets/Gmail para todo el monorepo.
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
TOKEN = str(_token_google())
RAIZ = Path(str(_RAIZ))
ENTREGA = RAIZ / "out/cava/cyber-octubre"
TEXTOS = RAIZ / "clients/cava/entregas/textos-cyber-octubre.json"

DESTINOS = {                      # carpeta local → id de Drive
    "vip": "1A5VvD9qtg3JfeXw1IXRxYpOlqzvOTpyb",       # CYBER CAVA VIP
    "general": "1Rra3kVfqApwQHV7MEp7SQib_8jKs2Cmr",   # CYBER CAVA GENERAL
    "whatsapp": "12ea2FidTYrzo44zw1PvWACWaxMVdDFp7",  # CYBER CAVA WHATSAPP
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
    return (d.files().list(q=f"'{padre}' in parents and trashed=false",
                           fields="files(id,name)", pageSize=400,
                           supportsAllDrives=True, includeItemsFromAllDrives=True)
            .execute().get("files", []))


def sube(d, ruta, padre):
    media = MediaFileUpload(str(ruta), mimetype="image/png", resumable=True)
    existentes = {f["name"]: f["id"] for f in hijos(d, padre)}
    if ruta.name in existentes:
        d.files().update(fileId=existentes[ruta.name], media_body=media,
                         supportsAllDrives=True).execute()
        print(f"    ~ actualizado  {ruta.name}")
    else:
        d.files().create(body={"name": ruta.name, "parents": [padre]},
                         media_body=media, fields="id",
                         supportsAllDrives=True).execute()
        print(f"    + subido       {ruta.name}")


def qa_en_verde(piezas):
    print("  QA de marca…")
    r = subprocess.run([sys.executable, str(RAIZ / "qa/motor.py"),
                        "--marca", "cava", "--textos", str(TEXTOS),
                        *[str(p) for p in piezas]],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout)
        sys.exit("ABORTA: el QA de cava no está en verde. No se sube nada.")
    print("  ✓ QA en verde")


def banner_hermano(piezas):
    """Ningún `_PACK` viaja huérfano.

    Los banners de pack están EXENTOS de la regla de la franja del Ministerio
    (`clients/cava/reglas.yaml`) porque son trozos de un mail cuya cabecera sí
    la lleva. Esa exención sólo es legítima si la cabecera existe y se sube con
    ellos: si alguien manda un `_PACK` solo, el correo saldría sin advertencia.
    """
    nombres = {p.name for p in piezas}
    for p in piezas:
        if "_PACK" not in p.name:
            continue
        banner = p.name.split("_PACK")[0] + ".png"
        if banner not in nombres:
            sys.exit(f"ABORTA: {p.name} va sin su banner principal ({banner}). "
                     "Un banner de pack no lleva la franja del Ministerio: la "
                     "lleva la cabecera, y tiene que viajar con él.")
    print("  ✓ cada banner de pack viaja con su banner principal")


def main():
    # Sin argumentos sube todo; con argumentos, sólo esas carpetas. Sirve para
    # dejar una en pausa —WhatsApp quedó en stand-by el 30-09— sin tener que
    # tocar el script.
    pedidas = [a for a in sys.argv[1:] if a in DESTINOS] or list(DESTINOS)
    piezas = sorted(p for c in pedidas for p in (ENTREGA / c).glob("*.png"))
    if not piezas:
        sys.exit("No hay piezas que subir en out/cava/cyber-octubre/")
    banner_hermano(piezas)
    qa_en_verde(piezas)
    d = svc()
    for carpeta in pedidas:
        destino = DESTINOS[carpeta]
        lote = sorted((ENTREGA / carpeta).glob("*.png"))
        if not lote:
            continue
        print(f"  {carpeta.upper()}  ({len(lote)})")
        for p in lote:
            sube(d, p, destino)
    print("\nListo.")


if __name__ == "__main__":
    main()

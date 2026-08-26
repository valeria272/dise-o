"""Rehace desde cero la carpeta de septiembre de Tierra Calma en Drive.

Manda a la papelera TODO lo que la agencia había subido a esa carpeta y vuelve
a subir la entrega nueva desde out/tierracalma/ENTREGA-SEPTIEMBRE-2026/, con la
misma estructura de julio y agosto (FEED/ y ST/).

El token OAuth es el compartido del monorepo y tiene scope `drive.file`: la app
solo ve y toca los archivos que ella misma creó, así que el borrado no puede
alcanzar material del cliente subido por otra persona.

OJO con los scopes: siempre los 6 completos, nunca un subconjunto — un refresco
parcial deja el token recortado y rompe Sheets/Gmail para todo el monorepo
(ver CLAUDE.md raíz).
"""
import json
import mimetypes
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
SEPTIEMBRE = "1EwX10zMm2f36SlyxPSd-rVpuK73MI7kn"
# 21-08-2026: septiembre se publica con las piezas de Carlos Figueroa. Las
# nuestras quedan como aprendizaje y viven en ESTA subcarpeta, no en la raíz del
# mes, para que el equipo no las confunda con la entrega real.
RAIZ_NOMBRE = "APRENDIZAJE IA — NO PUBLICAR"
ENTREGA = Path(
    str(_RAIZ / "out/tierracalma/ENTREGA-SEPTIEMBRE-2026")
)


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


def vaciar(d, padre):
    for f in hijos(d, padre):
        d.files().update(fileId=f["id"], body={"trashed": True}, supportsAllDrives=True).execute()
        print(f"  papelera  {f['name']}")


def carpeta(d, nombre, padre):
    """Crea la carpeta y la deja SÍ o SÍ colgando de `padre`.

    Drive no siempre respeta el `parents` del create: el 19-08-2026 las carpetas
    FEED y ST se crearon con parent = la carpeta de septiembre y aparecieron
    colgando de otra (Drive resolvió el padre a otro nodo del árbol). Los
    archivos quedaron bien subidos pero fuera de la URL que tiene el equipo. Por
    eso después del create se verifica y, si hace falta, se mueve.
    """
    m = (
        d.files()
        .create(
            body={"name": nombre, "mimeType": "application/vnd.google-apps.folder", "parents": [padre]},
            fields="id,parents",
            supportsAllDrives=True,
        )
        .execute()
    )
    if padre not in (m.get("parents") or []):
        actual = ",".join(m.get("parents") or [])
        m = (
            d.files()
            .update(fileId=m["id"], addParents=padre, removeParents=actual,
                    fields="id,parents", supportsAllDrives=True)
            .execute()
        )
        print(f"  (se movió {nombre} al padre correcto)")
    return m["id"]


def raiz_aprendizaje(d):
    """Devuelve (creándola si hace falta) la subcarpeta donde va lo nuestro."""
    for f in hijos(d, SEPTIEMBRE):
        if f["name"] == RAIZ_NOMBRE and f["mimeType"] == "application/vnd.google-apps.folder":
            return f["id"]
    return carpeta(d, RAIZ_NOMBRE, SEPTIEMBRE)


def subir(d, ruta: Path, padre):
    mt = mimetypes.guess_type(ruta.name)[0] or "application/octet-stream"
    m = (
        d.files()
        .create(
            body={"name": ruta.name, "parents": [padre]},
            media_body=MediaFileUpload(str(ruta), mimetype=mt, resumable=True),
            fields="id,size",
            supportsAllDrives=True,
        )
        .execute()
    )
    print(f"  {ruta.name:<26} {int(m.get('size', 0)) / 1e6:6.1f} MB")


def main():
    if not ENTREGA.exists():
        sys.exit(f"No existe {ENTREGA} — corre antes scripts/tc-entrega.sh")
    d = svc()
    RAIZ = raiz_aprendizaje(d)

    print(f"Vaciando «{RAIZ_NOMBRE}»…")
    vaciar(d, RAIZ)

    print("\nSubiendo FEED…")
    feed = carpeta(d, "FEED", RAIZ)
    for f in sorted((ENTREGA / "FEED").iterdir()):
        if f.is_file() and not f.name.startswith("."):
            subir(d, f, feed)

    print("\nSubiendo ST…")
    st = carpeta(d, "ST", RAIZ)
    for carp in ("ST", "ST-ANIMADAS"):
        p = ENTREGA / carp
        if p.exists():
            for f in sorted(p.iterdir()):
                if f.is_file() and not f.name.startswith("."):
                    subir(d, f, st)

    print("\nSuelto en la raíz del mes…")
    for f in sorted(ENTREGA.iterdir()):
        if f.is_file() and not f.name.startswith("."):
            subir(d, f, RAIZ)

    nota = Path(
        "/private/tmp/claude-502/-Users-Vale-Desktop-COPYLAB-PROJECTS-EDITOR-VIDEOS/"
        "80210faa-da68-475c-a8fa-6d323c817476/scratchpad/nota-entrega.md"
    )
    if nota.exists():
        print("\nNota de entrega…")
        # Drive convierte el markdown a Documento de Google si se le pide el
        # mimeType de destino en el body. Así el equipo puede comentar encima.
        m = (
            d.files()
            .create(
                body={
                    "name": "Tierra Calma | Nota de entrega - Septiembre 2026",
                    "parents": [RAIZ],
                    "mimeType": "application/vnd.google-apps.document",
                },
                media_body=MediaFileUpload(str(nota), mimetype="text/markdown", resumable=True),
                fields="id",
                supportsAllDrives=True,
            )
            .execute()
        )
        print(f"  https://docs.google.com/document/d/{m['id']}/edit")

    print(f"\nLISTO — https://drive.google.com/drive/folders/{RAIZ}")


if __name__ == "__main__":
    main()

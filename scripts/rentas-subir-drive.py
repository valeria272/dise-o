#!/usr/bin/env python3
"""
Sube la grilla de octubre de Rentas Nueva Urbe a Drive, junto al brief.

Crea (o reutiliza) una carpeta `DISEÑOS` DENTRO de `10. OCTUBRE`, que es donde
vive `RENTAS_NUEVA_URBE_GRILLA_OCTUBRE_2026_1.pptx`. Así la CM abre la carpeta
del mes y encuentra el brief y las piezas en el mismo sitio.

Idempotente: si un archivo con el mismo nombre ya está en la carpeta, lo
ACTUALIZA en vez de duplicarlo — así conserva su ID, su enlace y los comentarios
que la CM haya dejado anclados.

Usa el token OAuth compartido del monorepo con los 6 scopes completos.
NUNCA pedirle un subconjunto: degrada el token de todos los proyectos.

Uso:  ~/copylab-venv/bin/python3 scripts/rentas-subir-drive.py [--dry-run]
"""
import argparse, mimetypes, pathlib, sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ, token_google

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

# `10. OCTUBRE`, dentro de RENTAS NUEVA URBE / … / GRILLAS / 2026
CARPETA_MES = "1uqBQPK06qH-_5AOuR9aey05aT7zNPuE6"
NOMBRE_SUB = "DISEÑOS"

ENTREGA = RAIZ / "out/rentas/20261000_grilla_octubre"
# (ruta local, nombre en Drive) — el nombre lleva la fecha adelante para que la
# carpeta se ordene sola en el orden en que se publica el mes.
PIEZAS = [
    (ENTREGA / "reel/rentas_reel-octubre-06-10.mp4", "06-10 REEL Nuevas condiciones.mp4"),
    (ENTREGA / "story/rentas_st-proyecto-02-10.png", "02-10 ST Proyecto Valle Altiplanico.png"),
    (ENTREGA / "feed/rentas_estatico-sin-comision-13-10.png", "13-10 ESTATICO Sin comision.png"),
    (ENTREGA / "feed/rentas_c-halloween1.png", "27-10 CARRUSEL Halloween 1 portada.png"),
    (ENTREGA / "feed/rentas_c-halloween2.png", "27-10 CARRUSEL Halloween 2 tip 1.png"),
    (ENTREGA / "feed/rentas_c-halloween3.png", "27-10 CARRUSEL Halloween 3 tip 2.png"),
    (ENTREGA / "feed/rentas_c-halloween4.png", "27-10 CARRUSEL Halloween 4 tip 3.png"),
    (ENTREGA / "feed/rentas_c-halloween5.png", "27-10 CARRUSEL Halloween 5 cierre.png"),
    (ENTREGA / "story/rentas_st-halloween-29-10.png", "29-10 ST Halloween.png"),
    (ENTREGA / "NOTAS-PARA-LA-CM.md", "LEEME - notas para la CM.md"),
]


def credenciales():
    tok = pathlib.Path(str(token_google()))
    c = Credentials.from_authorized_user_file(str(tok), SCOPES)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        faltan = set(SCOPES) - set(c.scopes or [])
        if faltan:
            sys.exit(f"ABORTA: el refresco perdería los scopes {faltan}. No se guarda el token.")
        tok.write_text(c.to_json())
    return c


def carpeta_destino(d, dry):
    q = (f"'{CARPETA_MES}' in parents and name = '{NOMBRE_SUB}' "
         "and mimeType = 'application/vnd.google-apps.folder' and trashed = false")
    hay = d.files().list(q=q, fields="files(id,name)", pageSize=5).execute().get("files", [])
    if hay:
        print(f"  carpeta DISEÑOS ya existe · {hay[0]['id']}")
        return hay[0]["id"]
    if dry:
        print("  [dry-run] crearía la carpeta DISEÑOS")
        return None
    f = d.files().create(body={"name": NOMBRE_SUB, "mimeType": "application/vnd.google-apps.folder",
                               "parents": [CARPETA_MES]}, fields="id").execute()
    print(f"  carpeta DISEÑOS creada · {f['id']}")
    return f["id"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    d = build("drive", "v3", credentials=credenciales())
    destino = carpeta_destino(d, a.dry_run)

    for local, nombre in PIEZAS:
        if not local.exists():
            print(f"  ⚠ falta {local}")
            continue
        mb = local.stat().st_size / 1e6
        if a.dry_run:
            print(f"  [dry-run] {nombre:46s} {mb:6.1f} MB")
            continue
        tipo = mimetypes.guess_type(str(local))[0] or "application/octet-stream"
        medio = MediaFileUpload(str(local), mimetype=tipo, resumable=True)
        q = f"'{destino}' in parents and name = '{nombre}' and trashed = false"
        ya = d.files().list(q=q, fields="files(id)", pageSize=2).execute().get("files", [])
        if ya:
            d.files().update(fileId=ya[0]["id"], media_body=medio).execute()
            print(f"  actualizado  {nombre:46s} {mb:6.1f} MB")
        else:
            d.files().create(body={"name": nombre, "parents": [destino]},
                             media_body=medio, fields="id").execute()
            print(f"  subido       {nombre:46s} {mb:6.1f} MB")

    if destino:
        print(f"\n  https://drive.google.com/drive/folders/{destino}")


if __name__ == "__main__":
    main()

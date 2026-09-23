#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RONDA 11 de BETWEEN: arma la entrega y la sube REEMPLAZANDO en el Drive.

Las tres piezas EN CAMBIOS de la grilla de septiembre, cada una en su carpeta:

    S1  ·  1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq  ->  subcarpeta «C2 CUMPLEAÑOS BW»
    S2  ·  1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1
    S3  ·  1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ

⭐ Se ACTUALIZA el archivo por su ID, no se sube uno nuevo. Dos razones:
  1. el enlace se conserva, así que quien ya lo tenía —el portal de validaciones
     incluido— ve la versión nueva sin que nadie reenvíe nada;
  2. subir con el mismo nombre NO reemplaza en Drive: deja una segunda copia
     homónima. Ya pasó con «…Promos To Go 4 trio.png» y el duplicado sigue vivo.

⚠️ Los nombres se dejan COMO ESTÁN, con las fechas viejas, y es a propósito.
   La grilla se re-fechó entera el 04-09 (el cumpleaños pasó del 3 al 9, «Primero
   la foto» del 9 al 14, «Ella habló» del 11 al 16 y las Promos To Go del 14 al
   22), pero el portal levanta las piezas POR NOMBRE: renombrarlas crearía
   duplicados y dejaría la pieza vieja publicada. Renombrar es una decisión que
   hay que tomar junto con borrar la copia anterior.

Y la entrega va a 150 ppp RGB, que es lo que pide el manual: es metadato `pHYs`
del PNG, no un reescalado — la pieza sigue midiendo 2250 px de ancho.

Uso:
    python scripts/between-r11-entrega-subir.py --listar   # qué haría, sin tocar
    python scripts/between-r11-entrega-subir.py            # arma y sube
    python scripts/between-r11-entrega-subir.py --solo-entrega
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ, token_google  # noqa: E402

from PIL import Image  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PPP = 150
RENDERS = RAIZ / "out/hilton-between-r11"
ENTREGA = RAIZ / "out/entrega-r11"

#: composición -> (nombre en el Drive, id del archivo a reemplazar, carpeta)
PIEZAS = [
    ("BW-F-Cumple-1",  "BW FEED 03-09 Cumpleanos 1.png",
     "1Qhv23-XsdqmLg4VGnvouZykbaOeP9t6q", "S1"),
    ("BW-F-Cumple-2",  "BW FEED 03-09 Cumpleanos 2 detalles.png",
     "1fP0_FaMG7Yw0rvA-RrtmdcuvpqxG39fr", "S1"),
    ("BW-F-EllaHablo", "BW FEED 11-09 Ella hablo Ella escucho.png",
     "1IMVs8xky6CVK0YhXpX0wzI6eumXAWgg1", "S2"),
    ("BW-F-ToGo-1",    "BW FEED 14-09 Promos To Go 1 portada.png",
     "1lhUHAgIi_6mXPEpe_Yqxg5eaxyvqxjgG", "S3"),
    ("BW-F-ToGo-2",    "BW FEED 14-09 Promos To Go 2 sandwich.png",
     "1GBfHpTI0inaLbRZNxfTPzPuWNMjIghio", "S3"),
    ("BW-F-ToGo-3",    "BW FEED 14-09 Promos To Go 3 dulce.png",
     "1WfCfhTYBTl8knO_U5bAyDE8IXQZ5B5oP", "S3"),
    ("BW-F-ToGo-4",    "BW FEED 14-09 Promos To Go 4 los tres.png",
     "19iZbK2U7pOiHDENOk4Z6DWO3GOzt08EQ", "S3"),
]


def arma():
    """Copia los renders a la carpeta de entrega con el nombre del portal y
    150 ppp declarados."""
    hechas = []
    for comp, nombre, _id, semana in PIEZAS:
        origen = RENDERS / f"{comp}.png"
        if not origen.exists():
            print(f"  FALTA el render {origen.name}")
            continue
        destino = ENTREGA / semana / nombre
        destino.parent.mkdir(parents=True, exist_ok=True)
        im = Image.open(origen)
        im.save(destino, "PNG", dpi=(PPP, PPP))
        kb = destino.stat().st_size / 1024
        print(f"  {semana}  {nombre:44s} {im.size[0]}x{im.size[1]}  {kb:,.0f} KB")
        hechas.append((destino, _id, nombre, semana))
    return hechas


def sube(hechas):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    ruta = token_google()
    if not ruta:
        sys.exit("no hay token de Google; ver credentials/LEEME.md")
    cred = Credentials.from_authorized_user_file(str(ruta))
    if not cred.valid:
        cred.refresh(Request())
    drive = build("drive", "v3", credentials=cred, cache_discovery=False)

    for destino, _id, nombre, semana in hechas:
        # se comprueba primero que el archivo sea alcanzable: con scope
        # `drive.file` sólo lo son los que subió esta misma aplicación
        try:
            meta = drive.files().get(fileId=_id, fields="id,name,size").execute()
        except Exception as e:
            print(f"  {semana} {nombre}: NO alcanzable ({e.__class__.__name__}) "
                  f"— hay que reemplazarlo a mano")
            continue
        antes = int(meta.get("size", 0))
        media = MediaFileUpload(str(destino), mimetype="image/png", resumable=True)
        pet = drive.files().update(fileId=_id, media_body=media, fields="id,size")
        resp = None
        while resp is None:
            _, resp = pet.next_chunk()
        print(f"  {semana} {nombre:44s} {antes:,} -> {int(resp['size']):,} bytes  OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--solo-entrega", action="store_true")
    a = ap.parse_args()

    if a.listar:
        for comp, nombre, _id, semana in PIEZAS:
            existe = "si" if (RENDERS / f"{comp}.png").exists() else "NO"
            print(f"  {semana}  {comp:16s} render:{existe:3s} -> {nombre}  ({_id})")
        return

    print("\n1 - entrega (150 ppp, nombre del portal)")
    hechas = arma()
    if a.solo_entrega:
        print(f"\nlisto: {ENTREGA}")
        return
    print("\n2 - Drive: se REEMPLAZA cada archivo por su id")
    sube(hechas)
    print(f"\nlisto. Copias locales en {ENTREGA}")


if __name__ == "__main__":
    main()

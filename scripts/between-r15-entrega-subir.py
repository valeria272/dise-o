#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RONDA 15 de BETWEEN: arma la entrega y la sube REEMPLAZANDO en el Drive.

Eli devolvió la ronda 14 entera:

    «se ve extraño, lo dorado se ve quemado. La sts de emergencia se ve el vaso
     to go pegoteado y el carrusel de s3 la portada el logo del vaso sigue igual
     + slide 4 sigue oscuro y logo extraños. Utiliza magnific y mejóralos. Ya
     que es muy reiterativo los cambios y debes mejorar.»

Y las cuatro tenían causa técnica, no de criterio:

    S1  Cumpleaños 1 y 2   el «quemado» era un HALO NEGRO: se desenfocaba el RGB
                           y el alfa por separado, y `rotate(expand=True)` rellena
                           con negro transparente. Ahora el filtrado va con alfa
                           PREMULTIPLICADO y la pieza pasa por el hombro de altas.
    S2  ST Emergencia      el «pegoteado» era el RECORTE: `vaso-248` tiene el canto
                           mordido por grabCut. Se cambia por `togo-vaso-real-nobg`,
                           que ya estaba en el repo con el canto entero, y se le
                           lleva la temperatura a la de la vitrina.
    S3  To Go 1 (portada)  el logo «sigue igual» porque NO CABÍA: la banda de
                           cartón limpia medía 25 px y el lockup pide 56. Se
                           regeneró la escena con Nano Banana Pro —misma mujer,
                           mismo local, misma luz— pidiendo que tome el vaso más
                           abajo. Ahora hay 83 px y el logotipo entra entero.
    S3  To Go 4 (los tres) «sigue oscuro» no era la mediana —ya calzaba— sino las
                           SOMBRAS: fondo casi negro contra dos bodegones de luz
                           de día. Se abren las sombras sin tocar el punto negro.
                           Y los «logos extraños» eran vectores sin desenfoque ni
                           grano sobre una fotografía: ahora el sello se funde a
                           la nitidez local y recibe el grano del papel.

⛔ NO entran: To Go 2 y 3 («no las toques») ni «Ella hablo Ella escucho».

⭐ Se ACTUALIZA cada archivo por su ID: el enlace se conserva y subir con el
mismo nombre NO reemplaza en Drive, deja una segunda copia homónima.
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
RENDERS = RAIZ / "out/hilton-between-r15"
ENTREGA = RAIZ / "out/entrega-r15"

PIEZAS = [
    ("BW-F-Cumple-1",   "BW FEED 03-09 Cumpleanos 1.png",
     "1Qhv23-XsdqmLg4VGnvouZykbaOeP9t6q", "S1"),
    ("BW-F-Cumple-2",   "BW FEED 03-09 Cumpleanos 2 detalles.png",
     "1fP0_FaMG7Yw0rvA-RrtmdcuvpqxG39fr", "S1"),
    ("BW-S-Emergencia", "BW ST 09-09 Emergencia Between.png",
     "1GJrYQZk4VPiWKlw4i9zu1rKaFdNbFJjd", "S2"),
    ("BW-F-ToGo-1",     "BW FEED 14-09 Promos To Go 1 portada.png",
     "1lhUHAgIi_6mXPEpe_Yqxg5eaxyvqxjgG", "S3"),
    ("BW-F-ToGo-4",     "BW FEED 14-09 Promos To Go 4 los tres.png",
     "19iZbK2U7pOiHDENOk4Z6DWO3GOzt08EQ", "S3"),
]


def arma():
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
        print(f"  {semana}  {nombre:44s} {im.size[0]}x{im.size[1]}  "
              f"{destino.stat().st_size / 1024:,.0f} KB")
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
        try:
            meta = drive.files().get(fileId=_id, fields="id,name,size").execute()
        except Exception as e:
            print(f"  {semana} {nombre}: NO alcanzable ({e.__class__.__name__}) "
                  f"— reemplazar a mano")
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

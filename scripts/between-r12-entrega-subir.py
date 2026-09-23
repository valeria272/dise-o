#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RONDA 12 de BETWEEN: arma la entrega y la sube REEMPLAZANDO en el Drive.

Qué entra en esta ronda y por qué:

    S1  Cumpleaños 1 y 2   serpentinas DORADAS en vez de papelitos de colores,
                           y el vaso deja de verse blanquecino (la exposición se
                           fija por el producto, no por el cuadro). En la G2,
                           además, el avatar del mock pasa a fondo café + logo
                           beige, que son los colores de la marca.
    S2  ST Emergencia      el salado pasa a croissant de jamón queso y el dulce
                           a muffin. ⚠️ El cambio se hizo en la ronda 10 pero la
                           pieza NUNCA se subió: la del Drive era del 02-09.
    S3  To Go 1 (portada)  la escena se genera completa, sin recortes.
    S3  To Go 4 (los tres) escena nueva en formato To Go, con mano, y los dos
                           logotipos estampados con el vector real.

⛔ NO entran, a propósito:
    · `BW FEED 11-09 Ella hablo Ella escucho.png` — Eli la dio por APROBADA.
    · To Go 2 (sándwich) y 3 (dulce) — no se objetaron; la versión de la ronda
      11, ya revelada, sigue siendo la buena. Re-subir una pieza que nadie
      objetó sólo mueve la fecha y hace dudar al cliente.

⭐ Se ACTUALIZA cada archivo por su ID, no se sube uno nuevo: el enlace se
conserva y subir con el mismo nombre NO reemplaza en Drive, deja una segunda
copia homónima.

⚠️ Los nombres siguen con las fechas VIEJAS (la grilla se re-fechó el 04-09).
   El portal levanta las piezas POR NOMBRE: renombrar crearía duplicados y
   dejaría la versión anterior publicada. Es una decisión que va junto con
   borrar la copia vieja.

Uso:
    python scripts/between-r12-entrega-subir.py --listar
    python scripts/between-r12-entrega-subir.py --solo-entrega
    python scripts/between-r12-entrega-subir.py
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
RENDERS = RAIZ / "out/hilton-between-r12"
ENTREGA = RAIZ / "out/entrega-r12"

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

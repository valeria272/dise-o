#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RONDA 13 de BETWEEN: arma la entrega y la sube REEMPLAZANDO en el Drive.

Qué entra, y son las cinco piezas que Eli pidió corregir:

    S1  Cumpleaños 1 y 2   los adornos salen de la FOTO y pasan a ILUSTRACIÓN
                           —los trazos de pincel de Eli—, que es lo que pidió:
                           «que sean ilustradas, con el trazado que ya se sabe y
                           se conoce, punto». La foto vuelve a ser sólo foto.
    S2  ST Emergencia      vitrina rehecha: se genera VACÍA y los tres productos
                           reales (vaso aprobado, croissant jamón queso, muffin
                           de chocolate) se apoyan en una línea de base común,
                           con sombra de contacto y el reflejo del vidrio encima.
    S3  To Go 1 (portada)  el logotipo del vaso, re-centrado y re-medido sobre la
                           CARA VISIBLE del cartón.
    S3  To Go 4 (los tres) tono igualado al de las slides 2 y 3: la calidez
                           bajaba de 55 a 29 y la saturación de 58 a 44.

⛔ NO entran, y es pedido expreso de Eli («modifica solo la portada y la slide
   cuatro. No toques la dos y la tres»): To Go 2 (sándwich) y To Go 3 (dulce).
   Tampoco «Ella hablo Ella escucho», que quedó aprobada en la ronda 12.

⭐ Se ACTUALIZA cada archivo por su ID: el enlace se conserva y subir con el
mismo nombre NO reemplaza en Drive, deja una segunda copia homónima.

⚠️ Los nombres siguen con las fechas viejas (la grilla se re-fechó el 04-09). El
   portal levanta las piezas POR NOMBRE: renombrar crearía duplicados.

Uso:
    python scripts/between-r13-entrega-subir.py --listar
    python scripts/between-r13-entrega-subir.py --solo-entrega
    python scripts/between-r13-entrega-subir.py
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
RENDERS = RAIZ / "out/hilton-between-r13"
ENTREGA = RAIZ / "out/entrega-r13"

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

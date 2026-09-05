#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RONDA 14 de BETWEEN: arma la entrega y la sube REEMPLAZANDO en el Drive.

Las cinco piezas que Eli pidió corregir el 05-09-2026:

    S1  Cumpleaños 1 y 2   fuera los «plátanos dorados» —que seguían vivos en la
                           ventana del mock de la slide 2, apuntando a la foto de
                           la ronda 12— y entra confeti dorado REAL, del vector
                           que eligió Eli, sembrado sobre la mesa con la receta
                           de montaje (DOF, iluminante y sombra de contacto).
                           La foto del vaso y la medialuna NO se toca.
    S2  ST Emergencia      los tres productos —café To Go, croissant jamón queso
                           y muffin de chocolate— revelados con `apetitoso()`,
                           un 25 % más grandes, y por fin APOYADOS: el piso de la
                           vitrina estaba mal medido (1230 contra 1272 real) y
                           los tres colgaban 36 px sobre él. Más la sombra
                           proyectada en la pared del fondo y el recorte del vaso
                           limpio del trozo de mesa que arrastraba.
    S3  To Go 1 (portada)  el logotipo del vaso al tamaño de marca (0,86) y
                           centrado en el EJE del vaso. La causa de tres rondas
                           era una medición: el cuerpo del vaso mide 199 px, no
                           los 240 que decía la constante.
    S3  To Go 4 (los tres) se le quita la igualación de tono que la dejó lechosa
                           y se rehace con punto negro antes del gamma. Queda en
                           100 · 27,3 · 40,0 contra 99/23,7/40,9 y 102/34,2/43,6
                           de sus hermanas: dentro de la familia.

⛔ NO entran, y sigue siendo pedido expreso de Eli: To Go 2 (sándwich) y To Go 3
   (dulce) —«no las toques»— ni «Ella hablo Ella escucho», aprobada en la r12 y
   que la grilla ya marcó CORREGIDO.

⭐ Se ACTUALIZA cada archivo por su ID: el enlace se conserva y subir con el
mismo nombre NO reemplaza en Drive, deja una segunda copia homónima.

⚠️ Los nombres siguen con las fechas viejas (la grilla se re-fechó el 04-09). El
   portal levanta las piezas POR NOMBRE: renombrar crearía duplicados.

Uso:
    python scripts/between-r14-entrega-subir.py --listar
    python scripts/between-r14-entrega-subir.py --solo-entrega
    python scripts/between-r14-entrega-subir.py
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
RENDERS = RAIZ / "out/hilton-between-r14"
ENTREGA = RAIZ / "out/entrega-r14"

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

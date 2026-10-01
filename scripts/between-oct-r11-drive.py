#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 11 (01-10) — ordena Drive según la grilla viva.

1. Carrusel To Go (S1/BW/FEED/C1 togo S1): entra una lámina de INTRODUCCIÓN en el lugar 1. Las
   cuatro que ya estaban se RENOMBRAN un número hacia arriba (mismo id y enlace, md5 verificado
   contra el local de la ronda anterior) y recién después se les reemplaza el contenido; la
   introducción sube como archivo nuevo. Nunca «reemplazar por nombre» (memoria insertar-lamina-renumera).
2. Historias con la fecha corrida por la grilla: se renombran, no se re-suben.
3. «Reúnete en Between»: sube la OPCIÓN con foto real junto a la pieza vigente, sin pisarla.

Uso:  python scripts/between-oct-r11-drive.py --ensayo     (imprime y no toca nada)
      python scripts/between-oct-r11-drive.py [--solo carrusel|fechas|opcion]
"""
import argparse
import hashlib
import os
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parent.parent
B = RAIZ / "out/hilton/between"
RONDA = next((x.split("=")[1] for x in sys.argv if x.startswith("--ronda=")), "oct-r11")  # oct-r12: ronda de Eli
sys.argv = [x for x in sys.argv if not x.startswith("--ronda=")]
NUEVO, ANTES = B / RONDA, B / RONDA / "antes"
SEMANAS = {1: "1jb-vwQrLnrl8Sxve4vR3EbG6LegOQoUN", 3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz",
           4: "1QBaEKSMFFn9EefWZQRWilzXUl6gsTxh7"}
C1 = "1ExY-2WHkqduzgAdi2Eo7nARAFIbucPIM"  # S1/BW/FEED/C1 togo S1
FECHAS = [  # (semana, nombre en Drive, nombre según la grilla del 01-10)
    (3, "BW ST 19-10 Cowork.png", "BW ST 12-10 Cowork.png"),
    (3, "BW ST 20-10 Lo dicen ustedes.png", "BW ST 13-10 Lo dicen ustedes.png"),
    (4, "BW ST 27-10 Espacio para tu evento.png", "BW ST 22-10 Espacio para tu evento.png"),
]
OPCION = "BW FEED 07-10 Reunete en Between - OPCION foto real.png"
K = dict(supportsAllDrives=True)
md5 = lambda p: hashlib.md5(pathlib.Path(p).read_bytes()).hexdigest()  # noqa: E731

ap = argparse.ArgumentParser()
ap.add_argument("--ensayo", action="store_true")
ap.add_argument("--solo", default="")
a = ap.parse_args()

c = Credentials.from_authorized_user_file(str(token_google()))
if not c.valid:
    c.refresh(Request())
svc = build("drive", "v3", credentials=c, cache_discovery=False)


def hijos(padre, nombre=None, carpeta=False):
    q = f"'{padre}' in parents and trashed = false"
    if nombre:
        q += f" and name = '{nombre}'"
    if carpeta:
        q += " and mimeType = 'application/vnd.google-apps.folder'"
    return svc.files().list(q=q, fields="files(id,name,md5Checksum)", includeItemsFromAllDrives=True, **K).execute()["files"]


def sub(semana, *ruta):
    padre = SEMANAS[semana]
    for parte in ruta:
        padre = hijos(padre, parte, carpeta=True)[0]["id"]
    return padre


def unico(padre, nombre):
    r = hijos(padre, nombre)
    if len(r) != 1:
        sys.exit(f"x «{nombre}»: se esperaba 1 archivo y hay {len(r)}")
    return r[0]


def renombrar(f, nuevo):
    print(f"  renombrar  {f['name']}  →  {nuevo}")
    if not a.ensayo:
        svc.files().update(fileId=f["id"], body={"name": nuevo}, **K).execute()


def contenido(fid, ruta, etiqueta):
    print(f"  reemplazar {etiqueta}  ←  {ruta.relative_to(RAIZ)}")
    if not a.ensayo:
        f = svc.files().update(fileId=fid, media_body=MediaFileUpload(str(ruta), resumable=True),
                               fields="md5Checksum", **K).execute()
        print(f"             md5 {f['md5Checksum']} {'= local' if f['md5Checksum'] == md5(ruta) else '≠ LOCAL ⚠️'}")


def crear(padre, ruta, nombre):
    print(f"  subir      {nombre}")
    if a.ensayo:
        return
    if hijos(padre, nombre):
        return contenido(unico(padre, nombre)["id"], ruta, nombre)
    f = svc.files().create(body={"name": nombre, "parents": [padre]}, media_body=MediaFileUpload(str(ruta), resumable=True),
                           fields="md5Checksum,parents", **K).execute()
    print(f"             md5 {f['md5Checksum']} {'= local' if f['md5Checksum'] == md5(ruta) else '≠ LOCAL ⚠️'}"
          f"{'' if padre in f['parents'] else ' · ⚠️ FUERA DE LUGAR'}")


if a.solo in ("", "carrusel"):
    print("CARRUSEL To Go — S1/BW/FEED/C1 togo S1")
    nombres = {f["name"] for f in hijos(C1)}
    if "C1 n°5 togo S1.png" in nombres:
        print("  ya renumerado (existe la n°5): sólo se reemplaza el contenido")
        viejos = None
    else:
        viejos = {k: unico(C1, f"C1 n°{k} togo S1.png") for k in range(1, 5)}
        for k, f in viejos.items():  # el que se va a correr tiene que ser el que creemos
            if f["md5Checksum"] != md5(ANTES / f"C1 n°{k} togo S1.png"):
                sys.exit(f"x la n°{k} de Drive no es la del local anterior: no se toca nada")
        for k in (4, 3, 2, 1):
            renombrar(viejos[k], f"C1 n°{k + 1} togo S1.png")
    for k in range(2, 6):
        fid = viejos[k - 1]["id"] if viejos else unico(C1, f"C1 n°{k} togo S1.png")["id"]
        contenido(fid, NUEVO / f"C1 n°{k} togo S1.png", f"C1 n°{k}")
    crear(C1, NUEVO / "C1 n°1 togo S1.png", "C1 n°1 togo S1.png")

if a.solo in ("", "fechas"):
    print("FECHAS corridas por la grilla")
    for sem, viejo, nuevo in FECHAS:
        sts = sub(sem, "BW", "STS")
        if hijos(sts, nuevo):
            print(f"  ya está    {nuevo}")
            continue
        renombrar(unico(sts, viejo), nuevo)

if a.solo in ("", "opcion"):
    print("REÚNETE — opción con foto real, junto a la vigente (S1/BW/FEED)")
    crear(sub(1, "BW", "FEED"), NUEVO / OPCION, OPCION)

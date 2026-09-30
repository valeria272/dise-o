#!/usr/bin/env python3
"""BETWEEN · OCTUBRE 2026 — ronda 8 (30-09): reglas nuevas desde la S3 y orden por semana.

Eli, 30-09: «aplica las reglas nuevas en historias y feed, sólo de la S3 en adelante
(S1 y S2 ya están en revisión, no se tocan), y verifica que esté bien guardado según
semanas: el reel "Por qué vienes" ahora es de la S3».

La grilla viva (hoja FEED) pone en el bloque SEMANA 3 el reel 12-10 y el feed 14-10,
que el 24-09 y el 29-09 se subieron a S4/BW/FEED. Se MUEVEN (cambio de carpeta padre:
conserva id y enlace) y después se reemplaza el contenido de las piezas corregidas.

Uso:  python scripts/between-oct-r8.py --listar     # árbol BW de S1–S5, sin tocar nada
      python scripts/between-oct-r8.py              # mueve + reemplaza + verifica md5
"""
import argparse
import hashlib
import importlib.util
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("subir", RAIZ / "scripts/between-oct-subir-drive.py")
subir = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subir)

R8 = RAIZ / "out/hilton/between/oct-r8"

# (semana vieja, semana nueva, archivo) — sólo cambia la carpeta
MOVER = [
    (4, 3, "BW FEED 12-10 Por que vienes por que te quedas.mp4"),
    (4, 3, "BW FEED 12-10 Por que vienes por que te quedas.gif"),
    (4, 3, "BW FEED 12-10 Por que vienes por que te quedas - PORTADA.png"),
    (4, 3, "BW FEED 14-10 Espacios Between.png"),
]

# (semana, subcarpeta, archivo) — contenido nuevo, mismo nombre
REEMPLAZAR = [
    (3, "STS", "BW ST 20-10 Lo dicen ustedes.png"),
    (3, "FEED", "BW FEED 14-10 Espacios Between.png"),
    (4, "STS", "BW ST 27-10 Espacio para tu evento.png"),
    (5, "STS", "BW ST 28-10 Desayuno Bonjour.png"),
]


def hijos(svc, padre):
    q = f"'{padre}' in parents and trashed = false"
    return svc.files().list(q=q, fields="files(id,name,mimeType,md5Checksum,modifiedTime)",
                            supportsAllDrives=True, includeItemsFromAllDrives=True,
                            pageSize=200).execute().get("files", [])


def listar(svc):
    for sem, sid in subir.SEMANAS.items():
        bw = [f for f in hijos(svc, sid) if f["name"] == "BW"]
        if not bw:
            print(f"S{sem}: sin carpeta BW")
            continue
        for sub in hijos(svc, bw[0]["id"]):
            for f in sorted(hijos(svc, sub["id"]), key=lambda x: x["name"]):
                print(f"S{sem}/BW/{sub['name']}/{f['name']}  ({f.get('modifiedTime', '')[:16]})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()
    svc = subir.servicio()
    if a.listar:
        listar(svc)
        return
    feed = {s: subir.carpeta(svc, "FEED", subir.carpeta(svc, "BW", subir.SEMANAS[s])) for s in (3, 4)}
    for sv, sn, nombre in MOVER:
        q = f"name = '{nombre}' and '{feed[sv]}' in parents and trashed = false"
        prev = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                                includeItemsFromAllDrives=True).execute().get("files", [])
        if not prev:
            print(f"· {nombre}: no está en S{sv}/BW/FEED (¿ya movido?)")
            continue
        svc.files().update(fileId=prev[0]["id"], addParents=feed[sn], removeParents=feed[sv],
                           fields="id,parents", supportsAllDrives=True).execute()
        print(f"✓ movido S{sv} → S{sn}/BW/FEED/{nombre}")
    for sem, sub, nombre in REEMPLAZAR:
        ruta = R8 / nombre
        destino = subir.carpeta(svc, sub, subir.carpeta(svc, "BW", subir.SEMANAS[sem]))
        q = f"name = '{nombre}' and '{destino}' in parents and trashed = false"
        prev = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                                includeItemsFromAllDrives=True).execute().get("files", [])
        media = subir.MediaFileUpload(str(ruta), resumable=True)
        if prev:
            f = svc.files().update(fileId=prev[0]["id"], media_body=media,
                                   fields="id,md5Checksum", supportsAllDrives=True).execute()
        else:
            f = svc.files().create(body={"name": nombre, "parents": [destino]}, media_body=media,
                                   fields="id,md5Checksum", supportsAllDrives=True).execute()
        igual = f.get("md5Checksum") == hashlib.md5(ruta.read_bytes()).hexdigest()
        print(f"✓ S{sem}/BW/{sub}/{nombre} — {'reemplazado' if prev else 'subido'} · md5 "
              f"{'= local' if igual else '≠ LOCAL ⚠️'}")


if __name__ == "__main__":
    main()

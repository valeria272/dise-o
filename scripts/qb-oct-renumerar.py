#!/usr/bin/env python3
"""QB · OCTUBRE 2026 — renumera las historias ya subidas según el orden ACTUAL de la
grilla (29-09-2026). Eli: «actualízalo según la fecha y las semanas».

La grilla corrió las fechas (R-44) y aparecieron las «ST APROBADA» entre medio, así
que el n° dentro de cada semana ya no seguía el orden de publicación. Renombrar
conserva el ID y el enlace de cada archivo. Se hace en un orden que no pisa nombres
(primero se libera el número de destino).

    S2: n°3 (14-10 Mejores amigos) → n°4 · n°2 (Adivina) → n°3
    S3: n°1 (20-10 AYCD llamada) → n°2 · n°4 (19-10 Ensalada, mp4/png/gif) → n°1 ·
        n°5 (22-10 Close friends) → n°4

⚠️ Scope `drive.file`: sólo ve lo que subió el estudio. Lo que no encuentra lo avisa.
Uso:  python scripts/qb-oct-renumerar.py [--hacer]     (sin --hacer, sólo muestra)
"""
import os
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402

SEMANAS = {2: "1JqUCA7x-Am1upxivw3cJ1yWzwYUz-HNh", 3: "1reZbVKdH31wurEWJqrToVqrdLefb9YBz"}
# (semana, número viejo, número nuevo) — en este orden
CAMBIOS = [(2, 3, 4), (2, 2, 3), (3, 1, 2), (3, 4, 1), (3, 5, 4)]


def servicio():
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def hijos(svc, padre, nombre=None):
    q = f"'{padre}' in parents and trashed = false"
    if nombre:
        q += f" and name = '{nombre}'"
    return svc.files().list(q=q, fields="files(id,name,mimeType)", supportsAllDrives=True,
                            includeItemsFromAllDrives=True, pageSize=200).execute().get("files", [])


def main():
    hacer = "--hacer" in sys.argv
    svc = servicio()
    for sem, viejo, nuevo in CAMBIOS:
        qb = hijos(svc, SEMANAS[sem], "QB")
        sts = hijos(svc, qb[0]["id"], "STS") if qb else []
        if not sts:
            print(f"⚠️ S{sem}: no encuentro QB/STS"); continue
        prefijo = f"ST n°{viejo} S{sem} QB OCT 26"
        archivos = [f for f in hijos(svc, sts[0]["id"]) if f["name"].startswith(prefijo)]
        if not archivos:
            print(f"⚠️ S{sem}: no hay «{prefijo}*» visible para el estudio"); continue
        for f in archivos:
            nombre = f["name"].replace(f"ST n°{viejo} S{sem}", f"ST n°{nuevo} S{sem}", 1)
            if hacer:
                svc.files().update(fileId=f["id"], body={"name": nombre}, supportsAllDrives=True).execute()
            print(f"{'✓' if hacer else '·'} S{sem}/QB/STS  {f['name']}  →  {nombre}  ({f['id']})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Sube el banco de la FAMILIA DT (25-09-2026) a la carpeta que pasó Eli, ordenado por formato.

    python scripts/dt-familia-subir-drive.py [--probar]

Destino: 1P0w__CrAANzx20N1FL9CQ0FFvnA8is7G («acá en orden»). Adentro:
    01 POST 4x5 · 02 STORY 9x16 · 03 HORIZONTAL 16x9 · 04 PERSONAJES
Reemplaza por nombre (no duplica). Usa `servicio()` y `existente()` de drive-subir.py.
"""
import importlib.util, pathlib, sys
from googleapiclient.http import MediaFileUpload

AQUI = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("drive_subir", AQUI / "drive-subir.py")
ds = importlib.util.module_from_spec(spec); spec.loader.exec_module(ds)

RAIZ = "1P0w__CrAANzx20N1FL9CQ0FFvnA8is7G"
REPO = AQUI.parent
ENTREGA = REPO / "out/hilton/dt/familia/entrega"
PERFILES = REPO / "raw/hilton/dt/familia/r1"
CARPETAS = {"post": "01 POST 4x5", "story": "02 STORY 9x16", "16x9": "03 HORIZONTAL 16x9", "perfil": "04 PERSONAJES"}
PERSONAJES = {"mama-D": "DT-familia-personaje-mama.png", "papa-A": "DT-familia-personaje-papa.png",
              "nina-B": "DT-familia-personaje-hija.png", "nino-A": "DT-familia-personaje-hijo.png"}


def carpeta(drive, nombre, padre):
    q = (f"name = '{nombre}' and '{padre}' in parents and trashed = false "
         "and mimeType = 'application/vnd.google-apps.folder'")
    r = drive.files().list(q=q, fields="files(id)").execute().get("files")
    if r:
        return r[0]["id"]
    return drive.files().create(body={"name": nombre, "parents": [padre],
                                      "mimeType": "application/vnd.google-apps.folder"},
                                fields="id").execute()["id"]


def subir(drive, ruta, nombre, padre):
    mime = ds.TIPOS.get(ruta.suffix.lower(), "application/octet-stream")
    medio = MediaFileUpload(str(ruta), mimetype=mime, resumable=True, chunksize=8 << 20)
    viejo = ds.existente(drive, nombre, padre)
    if viejo:
        drive.files().update(fileId=viejo, media_body=medio).execute(); return "reemplazado"
    drive.files().create(body={"name": nombre, "parents": [padre]}, media_body=medio, fields="id").execute()
    return "subido"


def main():
    drive = ds.servicio()
    ids = {k: carpeta(drive, v, RAIZ) for k, v in CARPETAS.items()}
    print("carpetas OK:", ", ".join(CARPETAS.values()))
    if "--probar" in sys.argv:
        return
    n = 0
    for f in sorted(ENTREGA.glob("DT-familia-*.jpg")):
        fmt = "16x9" if "-16x9-" in f.name else "story" if "-story-" in f.name else "post"
        print(f"  {CARPETAS[fmt]} / {f.name} → {subir(drive, f, f.name, ids[fmt])}"); n += 1
    for k, nombre in PERSONAJES.items():
        print(f"  {CARPETAS['perfil']} / {nombre} → {subir(drive, PERFILES / f'{k}.png', nombre, ids['perfil'])}"); n += 1
    print(f"✓ {n} archivos · https://drive.google.com/drive/folders/{RAIZ}")


if __name__ == "__main__":
    main()

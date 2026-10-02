#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sube la OPCIÓN 2 de la campaña ARMY de DOUBLETREE a Drive, ordenada en dos carpetas.

Eli, 02-10-2026: «en la misma carpeta deja todo de op 2, ajusta que crea carpetas para paid y contenido
normal. Con los formatos de paid de 150 ppp como máximo, no puede pesar más».

    GRÁFICAS DT ARMY/
      CONTENIDO/   post 4:5 (2250 × 2813) · historia (2250 × 4000)
      PAID/        post 1:1 (1080 × 1080) · historia (1080 × 1920)

Las de PAID van además en JPG (Eli: «y para paid en JPG igual»), calidad 95, junto al PNG.

Todas las piezas salen marcadas a 150 ppp (los píxeles no cambian: es el dato de resolución del PNG, que
Remotion deja vacío). Si la pieza ya estaba suelta en la carpeta madre, se MUEVE a su subcarpeta en vez
de duplicarse.

    python scripts/dt-army-subir.py
"""
import importlib.util
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("drive_subir", RAIZ / "scripts/drive-subir.py")
ds = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ds)

MADRE = "1fu6GlR9uEydLdieUtnIrOrgovibyUOMf"           # GRÁFICAS DT ARMY
SALIDA = RAIZ / "out/hilton/dt/army"
OP = "PREVENTA - Opción 2 Hotel al atardecer.png"
ENTREGA = {
    "CONTENIDO": [SALIDA / f"DT ARMY KV Post {OP}", SALIDA / "adaptaciones" / f"DT ARMY ST {OP}"],
    "PAID": [SALIDA / "adaptaciones" / f"DT ARMY Post Paid {OP}", SALIDA / "adaptaciones" / f"DT ARMY ST Paid {OP}"],
}
PPP = 150


def carpeta(drive, nombre: str) -> str:
    q = (f"name = '{nombre}' and '{MADRE}' in parents and trashed = false "
         "and mimeType = 'application/vnd.google-apps.folder'")
    r = drive.files().list(q=q, fields="files(id)").execute().get("files") or []
    if r:
        return r[0]["id"]
    f = drive.files().create(body={"name": nombre, "parents": [MADRE],
                                   "mimeType": "application/vnd.google-apps.folder"}, fields="id").execute()
    print(f"carpeta nueva: {nombre}")
    return f["id"]


def main() -> int:
    drive = ds.servicio()
    for nombre_carpeta, piezas in ENTREGA.items():
        cid = carpeta(drive, nombre_carpeta)
        piezas = list(piezas)
        for ruta in list(piezas):
            im = Image.open(ruta)
            if tuple(round(v) for v in im.info.get("dpi", (0, 0))) != (PPP, PPP):
                im.save(ruta, dpi=(PPP, PPP), optimize=True)
            if nombre_carpeta == "PAID":
                jpg = ruta.with_suffix(".jpg")
                im.convert("RGB").save(jpg, quality=95, subsampling=0, dpi=(PPP, PPP))
                piezas.append(jpg)
        for ruta in piezas:
            im = Image.open(ruta)
            mime = "image/jpeg" if ruta.suffix == ".jpg" else "image/png"
            medio = ds.MediaFileUpload(str(ruta), mimetype=mime, resumable=True, chunksize=8 << 20)
            en_carpeta = ds.existente(drive, ruta.name, cid)
            suelta = ds.existente(drive, ruta.name, MADRE)
            if en_carpeta:
                f = drive.files().update(fileId=en_carpeta, media_body=medio, fields="id,size,md5Checksum").execute()
            elif suelta:      # estaba en la carpeta madre: se mueve y se reemplaza
                f = drive.files().update(fileId=suelta, media_body=medio, addParents=cid, removeParents=MADRE,
                                         fields="id,size,md5Checksum").execute()
            else:
                f = drive.files().create(body={"name": ruta.name, "parents": [cid]}, media_body=medio,
                                         fields="id,size,md5Checksum").execute()
            import hashlib
            igual = hashlib.md5(ruta.read_bytes()).hexdigest() == f.get("md5Checksum")
            print(f"{'ok   ' if igual else 'DISTINTO'} {nombre_carpeta}/{ruta.name} · {im.size[0]}×{im.size[1]} · {PPP} ppp · "
                  f"{int(f['size']) / 1e6:.1f} MB · md5 {'igual' if igual else 'NO coincide'}")
        print(f"  https://drive.google.com/drive/folders/{cid}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

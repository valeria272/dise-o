#!/usr/bin/env python3
"""BETWEEN · OCTUBRE — reemplaza UNA imagen flotante de la grilla (.xlsx en Drive) por el render nuevo.

La grilla de Between es un .xlsx de verdad: las piezas que Eli pega sobre las celdas viven en
`xl/media/imageN.png`. Se cambia sólo ese archivo dentro del zip (mismo tamaño en px que el que
dejó Eli, así el ancla y la medida no se mueven) y todo lo demás viaja byte a byte: brief, estados,
hilos y enlaces. Antes de subir se comprueba que Drive siga en la misma versión que se bajó; si
alguien editó entremedio, se detiene. La versión anterior queda en el historial de Drive.

⛔ 01-10-2026: el armado funciona, pero `--subir` da 403 (`appNotAuthorizedToFile`): el token del
estudio es `drive.file` + `drive.readonly` y la grilla es de Scarlette. Hasta que Valeria no amplíe el
permiso, la imagen la pega Eli a mano.

Uso:  python scripts/between-oct-grilla-reemplazar-imagen.py <grilla.xlsx bajada> <imageN.png> <render.png> [--subir]
"""
import hashlib
import io
import os
import pathlib
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image  # noqa: E402

GRILLA = "1EnZOwUptY6SftX-CF9ZFwXUuzPCGZ76L"
src, medio, render = pathlib.Path(sys.argv[1]), "xl/media/" + sys.argv[2], sys.argv[3]
dst = src.with_name(src.stem + "-nueva.xlsx")
md5 = lambda p: hashlib.md5(pathlib.Path(p).read_bytes()).hexdigest()  # noqa: E731

zin = zipfile.ZipFile(src)
crc = {i.filename: i.CRC for i in zin.infolist()}  # antes de escribir: writestr muta el ZipInfo que recibe
vieja = Image.open(io.BytesIO(zin.read(medio)))
buf = io.BytesIO()
Image.open(render).convert(vieja.mode).resize(vieja.size, Image.LANCZOS).save(buf, "PNG", optimize=True)
with zipfile.ZipFile(dst, "w") as zout:
    for it in zin.infolist():
        zout.writestr(it, buf.getvalue() if it.filename == medio else zin.read(it.filename),
                      compress_type=it.compress_type)
znew = zipfile.ZipFile(dst)
assert znew.testzip() is None and znew.namelist() == zin.namelist()
distintos = [b.filename for b in znew.infolist() if crc[b.filename] != b.CRC]
assert distintos == [medio], distintos
print(f"ok {dst.name}: sólo cambia {medio} ({vieja.size[0]}×{vieja.size[1]}, {len(buf.getvalue()) // 1024} KB)")

if "--subir" in sys.argv:
    from _entorno import token_google
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    c = Credentials.from_authorized_user_file(str(token_google()))
    if not c.valid:
        c.refresh(Request())
    svc = build("drive", "v3", credentials=c, cache_discovery=False)
    vivo = svc.files().get(fileId=GRILLA, fields="md5Checksum,modifiedTime", supportsAllDrives=True).execute()
    if vivo["md5Checksum"] != md5(src):
        sys.exit(f"x la grilla cambió en Drive ({vivo['modifiedTime']}): bájala de nuevo antes de subir")
    f = svc.files().update(
        fileId=GRILLA, supportsAllDrives=True, fields="md5Checksum,modifiedTime,headRevisionId",
        media_body=MediaFileUpload(str(dst), resumable=True, chunksize=16 * 1024 * 1024,
                                   mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
    ).execute()
    print(f"✓ grilla reemplazada · {f['modifiedTime']} · md5 {f['md5Checksum']} "
          f"{'= local' if f['md5Checksum'] == md5(dst) else '≠ LOCAL ⚠️'}")

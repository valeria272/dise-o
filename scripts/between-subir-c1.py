#!/usr/bin/env python3
"""Sube la PORTADA del carrusel Cowork (C1) a la carpeta que abrió Eli en Drive.

⭐ RONDA 8 — 02-09-2026. Eli pidió la corrección de la portada y dio la carpeta
de destino en el mismo mensaje:

    https://drive.google.com/drive/u/0/folders/1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332

Es **`C1 COWORK`**, suya, creada el 01-09 y vacía hasta ahora, colgando de la
carpeta `BW` de `S1 HILTON SEP 2026` (`1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq`).

⚠️ El token del estudio tiene alcance `drive.file`: **no puede LEER** una carpeta
que no creó —`files.get` sobre ella devuelve 404— pero **sí puede ESCRIBIR**
dentro pasándola como `parents`. Por eso acá no se lista antes de subir; el
contenido se comprobó con el conector de Drive de claude.ai, que sí ve todo.

El nombre del archivo NO es decorativo: **el portal de validaciones levanta las
piezas por nombre**, así que se conserva exactamente el de la entrega anterior
(`BW FEED 01-09 Cowork 1 portada.png`). Renombrar DUPLICA en vez de reemplazar.

Uso:
    python scripts/between-subir-c1.py             # sube (o reemplaza si ya está)
    python scripts/between-subir-c1.py --listar    # qué subió este token acá
"""
import argparse
import json
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import token_google  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ⚠️ La lista completa, igual que en `between-subir-r7.py`: pedir menos scopes de
# los que el token ya tiene lo DEGRADA para todo el monorepo en el refresco.
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.labels',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
]

CARPETA = '1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332'          # C1 COWORK
ORIGEN = RAIZ / 'out/hilton-between-r8/BW-F-Cowork-1.png'
NOMBRE = 'BW FEED 01-09 Cowork 1 portada.png'
MANIFIESTO = RAIZ / 'out/hilton-between-r8/_subidas.json'


def servicio():
    tok = Path(str(token_google()))
    c = Credentials.from_authorized_user_file(str(tok), SCOPES)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        faltan = set(SCOPES) - set(c.scopes or [])
        if faltan:
            sys.exit(f'ABORTA: el refresco perdió scopes {faltan}. No se guarda el token.')
        tok.write_text(c.to_json())
    return build('drive', 'v3', credentials=c)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--listar', action='store_true',
                    help='muestra lo que ESTE token tiene subido en la carpeta')
    a = ap.parse_args()
    s = servicio()

    if a.listar:
        r = s.files().list(q=f"'{CARPETA}' in parents and trashed=false",
                           fields='files(id,name,size,modifiedTime)').execute()
        for f in r.get('files', []):
            print(f"  {int(f.get('size', 0))/1e6:6.2f} MB  {f['name']}  ({f['id']})")
        if not r.get('files'):
            print('  (el token no ve nada acá — con `drive.file` sólo ve lo que él subió)')
        return

    if not ORIGEN.is_file():
        sys.exit(f'✗ No existe {ORIGEN}\n  Rinde antes:  '
                 f'python scripts/between-rendir.py BW-F-Cowork-1 --salida out/hilton-between-r8')

    # ¿ya lo subimos antes? Entonces se REEMPLAZA el contenido para conservar el
    # enlace y los comentarios, en vez de dejar dos archivos con el mismo nombre.
    previo = s.files().list(
        q=f"'{CARPETA}' in parents and name = '{NOMBRE}' and trashed=false",
        fields='files(id,name)').execute().get('files', [])

    medio = MediaFileUpload(str(ORIGEN), mimetype='image/png', resumable=True)
    if previo:
        fid = previo[0]['id']
        s.files().update(fileId=fid, media_body=medio).execute()
        print(f'↻ REEMPLAZADA (mismo enlace): {NOMBRE}')
    else:
        fid = s.files().create(
            body={'name': NOMBRE, 'parents': [CARPETA]},
            media_body=medio, fields='id').execute()['id']
        print(f'↑ SUBIDA: {NOMBRE}')

    # verificación byte a byte: que lo que quedó arriba pese lo mismo que el local
    meta = s.files().get(fileId=fid, fields='id,name,size').execute()
    local = ORIGEN.stat().st_size
    ok = int(meta.get('size', -1)) == local
    print(f'   {local/1e6:.2f} MB local · {int(meta.get("size",0))/1e6:.2f} MB en Drive'
          f'  {"✓ coinciden" if ok else "✗ NO COINCIDEN"}')
    print(f'   https://drive.google.com/file/d/{fid}/view')
    if not ok:
        sys.exit(1)

    MANIFIESTO.parent.mkdir(parents=True, exist_ok=True)
    MANIFIESTO.write_text(json.dumps({NOMBRE: {'id': fid, 'bytes': local}},
                                     ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'   manifiesto → {MANIFIESTO.relative_to(RAIZ)}')


if __name__ == '__main__':
    main()

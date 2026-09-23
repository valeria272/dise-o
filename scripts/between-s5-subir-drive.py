#!/usr/bin/env python3
"""
Sube las DOS historias de la S5 de Between a la carpeta `STS` de la S5 del Drive.

Por qué no sirve `between-subir-drive.py`: ese sólo mira `*.png`, y acá una de
las dos piezas es un **MP4** (la col U de la grilla pide historia ANIMADA).

Idempotencia: el token del estudio tiene scope `drive.file`, así que puede crear
pero **no listar** lo que subió otra persona. El registro de lo ya subido vive en
un manifiesto local (`_subidas.json` junto a las piezas); correr el script dos
veces no duplica. Para reemplazar el contenido de un archivo ya subido —mismo
enlace para la diseñadora— se usa `--actualizar`.

⚠️ Se piden SIEMPRE los 6 scopes compartidos. Pedir un subconjunto y dejar que el
token se refresque lo degrada para todo el monorepo (pasó el 29-07-2026).

Uso:
    python scripts/between-s5-subir-drive.py --listar
    python scripts/between-s5-subir-drive.py
    python scripts/between-s5-subir-drive.py --actualizar BW-S5-Plateada
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ, token_google  # noqa: E402

from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

SCOPES_COMPARTIDOS = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.labels',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
]

# Carpeta `STS` de la S5 de BW — la abrió Eli el 11-09-2026 y la pasó en el encargo
CARPETA_STS = '1r_spPoBx-vR63J8GTRVCUkbZGGyNLnJg'
PIEZAS = RAIZ / 'out/hilton-between-s5'

# ⛔ Las copias `GUIA CM` NO se suben: son para el community manager, no para el
#    cliente. Por eso el mapa es explícito y no un glob.
ENTREGA = {
    'BW-S5-HumorToGo.png':  ('BW ST 28-09 Humor cafe gigante.png',       'image/png'),
    'BW-S5-Plateada.mp4':   ('BW ST 30-09 Plateada al Carmenere.mp4',    'video/mp4'),
}


def servicio():
    ruta = token_google()
    if not ruta or not Path(ruta).exists():
        sys.exit('No encontré el token de Google. Revisa scripts/_entorno.py')
    cred = Credentials.from_authorized_user_file(str(ruta), SCOPES_COMPARTIDOS)
    if cred.expired and cred.refresh_token:
        cred.refresh(Request())
        faltan = set(SCOPES_COMPARTIDOS) - set(cred.scopes or [])
        if faltan:
            sys.exit(f'⛔ El refresco devolvió un token RECORTADO (faltan {faltan}). '
                     f'NO se guarda: degradaría el token de todo el monorepo.')
        Path(ruta).write_text(cred.to_json())
    return build('drive', 'v3', credentials=cred, cache_discovery=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--carpeta', default=CARPETA_STS)
    ap.add_argument('--piezas', default=str(PIEZAS))
    ap.add_argument('--listar', action='store_true')
    ap.add_argument('--actualizar', nargs='+', default=[], metavar='CLAVE')
    a = ap.parse_args()

    origen = Path(a.piezas)
    manifiesto = origen / '_subidas.json'
    ya = json.loads(manifiesto.read_text(encoding='utf-8')) if manifiesto.exists() else {}

    faltan_en_disco = [n for n in ENTREGA if not (origen / n).exists()]
    if faltan_en_disco:
        sys.exit(f'⛔ No están rendidas: {faltan_en_disco}')

    if a.listar:
        for archivo, (nombre, _) in ENTREGA.items():
            peso = (origen / archivo).stat().st_size / 1048576
            estado = 'YA SUBIDA' if Path(archivo).stem in ya else 'por subir'
            print(f'  {archivo:26s} -> {nombre:42s} {peso:5.1f} MB  [{estado}]')
        print(f'\nhttps://drive.google.com/drive/folders/{a.carpeta}')
        return

    svc = servicio()
    fallos = []
    for archivo, (nombre, tipo) in ENTREGA.items():
        clave = Path(archivo).stem
        ruta = origen / archivo
        media = MediaFileUpload(str(ruta), mimetype=tipo, resumable=True,
                                chunksize=8 * 1024 * 1024)
        try:
            if clave in ya and clave in a.actualizar:
                pedido = svc.files().update(fileId=ya[clave]['id'], media_body=media,
                                            fields='id,name', supportsAllDrives=True)
                marca = '🔁'
            elif clave in ya:
                print(f'  ⏭  {nombre} (ya estaba; usa --actualizar para reemplazarla)')
                continue
            else:
                pedido = svc.files().create(
                    body={'name': nombre, 'parents': [a.carpeta]},
                    media_body=media, fields='id,name,webViewLink',
                    supportsAllDrives=True)
                marca = '✅'
            resp = None
            while resp is None:
                _, resp = pedido.next_chunk()
            ya[clave] = {'id': resp['id'], 'nombre': resp['name'],
                         'bytes': ruta.stat().st_size}
            manifiesto.write_text(json.dumps(ya, indent=2, ensure_ascii=False),
                                  encoding='utf-8')
            print(f'  {marca} {nombre}  ({ruta.stat().st_size / 1048576:.1f} MB)')
        except Exception as e:
            fallos.append((clave, str(e)[:200]))
            print(f'  ⛔ {nombre}: {str(e)[:200]}')

    print(f'\nhttps://drive.google.com/drive/folders/{a.carpeta}')
    if fallos:
        sys.exit(1)


if __name__ == '__main__':
    main()

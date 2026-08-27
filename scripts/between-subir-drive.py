#!/usr/bin/env python3
"""
Sube las piezas de BETWEEN a la carpeta de entrega del Drive de la agencia.

Por defecto sube `out/hilton-between-sept-v3/` a la carpeta `BW` de
`S1 HILTON SEP 2026` (la que abrió Elisabet).

Notas de implementación:
  · El token del monorepo tiene scope `drive.file`, que **sí permite crear**
    archivos nuevos, pero **no permite listar** los que subió otra persona. Por eso
    la idempotencia se lleva en un manifiesto local (`_subidas.json` junto a las
    piezas): si el script se corre dos veces, no duplica.
  · Se usa **subida reanudable**: las piezas pesan ~7 MB cada una y una subida
    simple se corta.
  · ⚠️ Se piden SIEMPRE los 6 scopes compartidos. Pedir un subconjunto y dejar que
    el token se refresque lo degrada para todo el monorepo (pasó el 29-07-2026).

Uso:
    python3 scripts/between-subir-drive.py                    # sube lo que falte
    python3 scripts/between-subir-drive.py --listar           # solo muestra qué haría
    python3 scripts/between-subir-drive.py --carpeta <id>
"""
import argparse
import json
import mimetypes
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ, token_google  # noqa: E402

from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

# ⚠️ Los 6 de siempre. No recortar. Ver CLAUDE.md del monorepo.
SCOPES_COMPARTIDOS = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.labels',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
]

# Carpeta BW dentro de «S1 HILTON SEP 2026»
CARPETA_BW = '1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq'
PIEZAS = RAIZ / 'out/hilton-between-sept-v3'

# id de composición → nombre de entrega. La fecha adelante para que la carpeta
# quede ordenada como el calendario, que es como lo revisa la diseñadora.
NOMBRES = {
    'BW-F-Cowork-1':      'BW FEED 01-09 Cowork 1 portada',
    'BW-F-Cowork-2':      'BW FEED 01-09 Cowork 2 winter garden',
    'BW-F-Cowork-3':      'BW FEED 01-09 Cowork 3 segundo nivel',
    'BW-F-Cowork-4':      'BW FEED 01-09 Cowork 4 servicio',
    'BW-F-Cumple-1':      'BW FEED 03-09 Cumpleanos 1',
    'BW-F-Cumple-2':      'BW FEED 03-09 Cumpleanos 2 detalles',
    'BW-F-HumorCafecito': 'BW FEED 07-09 Humor cafecito',
    'BW-F-Foto-1':        'BW FEED 09-09 Primero la foto 1',
    'BW-F-Foto-2':        'BW FEED 09-09 Primero la foto 2',
    'BW-F-Foto-3':        'BW FEED 09-09 Primero la foto 3',
    'BW-F-Foto-4':        'BW FEED 09-09 Primero la foto 4',
    'BW-F-EllaHablo':     'BW FEED 11-09 Ella hablo ella escucho',
    'BW-F-ToGo-1':        'BW FEED 14-09 Promos To Go 1 portada',
    'BW-F-ToGo-2':        'BW FEED 14-09 Promos To Go 2 sandwich',
    'BW-F-ToGo-3':        'BW FEED 14-09 Promos To Go 3 dulce',
    'BW-F-ToGo-4':        'BW FEED 14-09 Promos To Go 4 trio',
    'BW-S-ToGoDulce':     'BW ST 01-09 Promo To Go cafe y dulce',
    'BW-S-Cumple':        'BW ST 03-09 Cafe de regalo cumpleanos',
    'BW-S-Calculos':      'BW ST 04-09 Segun mis calculos',
    'BW-S-Emergencia':    'BW ST 09-09 Romper en caso de antojo',
    'BW-S-HoraCafe':      'BW ST 14-09 Cuando es hora de cafe',
    'BW-S-Cowork':        'BW ST 16-09 Cowork te esperamos',
    'BW-S-Dieciocho':     'BW ST 18-09 Saludo Fiestas Patrias',
    'BW-S-Strudel':       'BW ST 21-09 Strudel de manzana',
    'BW-S-Primavera':     'BW ST 22-09 Primavera milkshake',
    'BW-S-HumorToGo':     'BW ST 28-09 Humor cafe gigante',
    'BW-S-Plateada':      'BW ST 30-09 Plateada al Carmenere',
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
    ap.add_argument('--carpeta', default=CARPETA_BW)
    ap.add_argument('--piezas', default=str(PIEZAS))
    ap.add_argument('--listar', action='store_true', help='no sube, solo informa')
    args = ap.parse_args()

    origen = Path(args.piezas)
    archivos = sorted(p for p in origen.glob('*.png') if not p.name.startswith('_'))
    if not archivos:
        sys.exit(f'No hay piezas en {origen}')

    manifiesto = origen / '_subidas.json'
    ya = json.loads(manifiesto.read_text()) if manifiesto.exists() else {}

    pendientes = [p for p in archivos if p.stem not in ya]
    peso = sum(p.stat().st_size for p in pendientes) / 1048576
    print(f'{len(archivos)} piezas · {len(pendientes)} por subir · {peso:.0f} MB')
    if args.listar:
        for p in pendientes:
            print(f'   {p.stem}  ->  {NOMBRES.get(p.stem, p.stem)}.png')
        return

    svc = servicio()
    subidas, fallos = 0, []
    for p in pendientes:
        nombre = f'{NOMBRES.get(p.stem, p.stem)}.png'
        tipo = mimetypes.guess_type(p.name)[0] or 'image/png'
        try:
            media = MediaFileUpload(str(p), mimetype=tipo, resumable=True, chunksize=8 * 1024 * 1024)
            pedido = svc.files().create(
                body={'name': nombre, 'parents': [args.carpeta]},
                media_body=media,
                fields='id,name,webViewLink',
                supportsAllDrives=True,
            )
            resp = None
            while resp is None:
                _, resp = pedido.next_chunk()
            ya[p.stem] = {'id': resp['id'], 'nombre': resp['name']}
            manifiesto.write_text(json.dumps(ya, indent=2, ensure_ascii=False))
            subidas += 1
            print(f'  ✅ {nombre}')
        except Exception as e:
            fallos.append((p.stem, str(e)[:160]))
            print(f'  ⛔ {nombre}: {str(e)[:160]}')

    print(f'\n{subidas} subidas · {len(fallos)} fallos')
    print(f'https://drive.google.com/drive/folders/{args.carpeta}')
    if fallos:
        sys.exit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Sube los carruseles de la S1 de Between a las carpetas por carrusel de Eli.

⭐ RONDA 8 — 02-09-2026. Eli pidió la corrección de la portada y dio la carpeta
de destino en el mismo mensaje:

    https://drive.google.com/drive/u/0/folders/1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332

Es **`C1 COWORK`**, suya, creada el 01-09 y vacía hasta ahora, colgando de la
carpeta `BW` de `S1 HILTON SEP 2026` (`1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq`).

⭐ Y después la segunda: «Sigamos a corregir esta …/1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw»,
que es **`C2 CUMPLEAÑOS BW`**. Eli está ordenando la S1 **por carrusel**, una
carpeta cada uno, así que el script recibe cuál subir.

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

MANIFIESTO = RAIZ / 'out/hilton-between-r8/_subidas.json'
RENDER = RAIZ / 'out/hilton-between-r8'

# ⭐ Las carpetas POR CARRUSEL que abrió Eli el 01-09 dentro de `BW` de
# `S1 HILTON SEP 2026` (`1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq`). Hay una tercera,
# `STS` (`14Z4XnkM9sepmdPV0XjKzoqb1HXMbvIzO`), para las historias.
CARPETAS = {
    'cowork': '1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332',   # C1 COWORK
    'cumple': '1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw',   # C2 CUMPLEAÑOS BW
    # ⭐ La S2 va en OTRA carpeta, que Eli abrió el 02-09: `BW` dentro de la
    # semana 2 (`1MSF7sQYNowbU8GlkDn6_HoR8-bqCDeYn`). No cuelga de `BW` de la
    # S1, así que no se puede deducir: la dio ella por chat.
    's2': '1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1',      # S2 · BW
}

# ⭐ EL CARRUSEL COMPLETO, decisión de Eli el 02-09: «súbelas a ese drive, mejor
# así tenemos todo». `C1` y `C2` son CARRUSELES, no slides —la carpeta hermana
# es `C2 CUMPLEAÑOS BW`—, así que `C1 COWORK` es la carpeta del carrusel Cowork
# entero y tiene que traer las cuatro. El cliente revisa el carrusel completo,
# que es como se publica.
#
# Las CUATRO salen de la ronda 8: en la 2.ª pasada Eli pidió emparejar los
# títulos («se ven poco alineados y desordenados»), así que las tres interiores
# también se re-rindieron. Ya no se toma nada de `out/entrega-r7/S1`.
PIEZAS = {
    'cowork': [
        ('BW FEED 01-09 Cowork 1 portada.png', 'BW-F-Cowork-1.png'),
        ('BW FEED 01-09 Cowork 2 winter garden.png', 'BW-F-Cowork-2.png'),
        ('BW FEED 01-09 Cowork 3 segundo nivel.png', 'BW-F-Cowork-3.png'),
        ('BW FEED 01-09 Cowork 4 servicio.png', 'BW-F-Cowork-4.png'),
    ],
    'cumple': [
        ('BW FEED 03-09 Cumpleanos 1.png', 'BW-F-Cumple-1.png'),
        ('BW FEED 03-09 Cumpleanos 2 detalles.png', 'BW-F-Cumple-2.png'),
    ],
    's2': [
        ('BW ST 09-09 Emergencia Between.png', 'BW-S-Emergencia.png'),
    ],
}


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
    ap.add_argument('carrusel', nargs='*', choices=[*PIEZAS], default=[],
                    help='cowork · cumple. Sin argumentos, los dos.')
    ap.add_argument('--listar', action='store_true',
                    help='muestra lo que ESTE token tiene subido en las carpetas')
    a = ap.parse_args()
    s = servicio()
    cuales = a.carrusel or list(PIEZAS)

    if a.listar:
        for c in cuales:
            print(f'— {c}')
            r = s.files().list(q=f"'{CARPETAS[c]}' in parents and trashed=false",
                               fields='files(id,name,size,modifiedTime)').execute()
            for f in r.get('files', []):
                print(f"  {int(f.get('size', 0))/1e6:6.2f} MB  {f['name']}  ({f['id']})")
            if not r.get('files'):
                print('  (el token no ve nada acá — con `drive.file` sólo ve lo que él subió)')
        return

    tareas = [(CARPETAS[c], nom, RENDER / arch)
              for c in cuales for nom, arch in PIEZAS[c]]
    faltan = [str(o) for _, _, o in tareas]
    faltan = [f for f in faltan if not Path(f).is_file()]
    if faltan:
        sys.exit('✗ Faltan piezas rendidas:\n  ' + '\n  '.join(faltan) +
                 '\n\nRinde con:  python scripts/between-rendir.py BW-F-Cowork'
                 ' --salida out/hilton-between-r8')

    manifiesto, malas = {}, []
    for CARPETA, nombre, origen in tareas:
        # ¿ya está? Entonces se REEMPLAZA el contenido, para conservar el enlace
        # y los comentarios en vez de dejar dos archivos con el mismo nombre.
        previo = s.files().list(
            q=f"'{CARPETA}' in parents and name = '{nombre}' and trashed=false",
            fields='files(id,name)').execute().get('files', [])

        medio = MediaFileUpload(str(origen), mimetype='image/png', resumable=True)
        if previo:
            fid = previo[0]['id']
            s.files().update(fileId=fid, media_body=medio).execute()
            verbo = '↻ REEMPLAZADA'
        else:
            fid = s.files().create(
                body={'name': nombre, 'parents': [CARPETA]},
                media_body=medio, fields='id').execute()['id']
            verbo = '↑ SUBIDA    '

        # verificación byte a byte: lo de arriba tiene que pesar lo mismo
        meta = s.files().get(fileId=fid, fields='id,name,size').execute()
        local = origen.stat().st_size
        ok = int(meta.get('size', -1)) == local
        if not ok:
            malas.append(nombre)
        print(f'{verbo}  {nombre}')
        print(f'              {local/1e6:6.2f} MB  {"✓" if ok else "✗ NO COINCIDE"}'
              f'   https://drive.google.com/file/d/{fid}/view')
        manifiesto[nombre] = {'id': fid, 'bytes': local}

    MANIFIESTO.parent.mkdir(parents=True, exist_ok=True)
    MANIFIESTO.write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2),
                          encoding='utf-8')
    print(f'\n{len(tareas)} piezas · manifiesto → {MANIFIESTO.relative_to(RAIZ)}')
    if malas:
        sys.exit(f'✗ NO coinciden los bytes en: {", ".join(malas)}')


if __name__ == '__main__':
    main()

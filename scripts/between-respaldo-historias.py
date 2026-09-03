#!/usr/bin/env python3
"""Deja en Drive las historias de Between que YA NO SE PUEDEN REHACER.

⭐ 03-09-2026. Auditoría de `BetweenSeptiembre.tsx`: de las 27 composiciones
registradas, 8 no rinden porque sus imágenes de origen no existen en ningún
disco ni en el historial de git. Son todas historias. Su PNG final es la única
copia viva de ese trabajo, y hasta hoy vivía sólo en el disco externo `F:`.

Eli: «Deja esas fotos en drive en la S3, que se llame respaldo. No interfiere.»
→ subcarpeta `respaldo` DENTRO de `S3 · BW`, sin tocar la entrega.

El origen es la copia verificada con SHA256 contra `F:` (27 de 27 idénticas),
no el disco externo: así el script corre aunque `F:` esté desconectado.

⚠️ El token del estudio tiene alcance `drive.file`: no puede LEER la carpeta
ajena, pero sí crear dentro pasándola como `parents`. Por eso la subcarpeta se
busca entre lo que este token ya subió, y si no está, se crea.

    python scripts/between-respaldo-historias.py
    python scripts/between-respaldo-historias.py --listar
"""
import argparse
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

# ⚠️ La lista completa: pedir menos scopes de los que el token ya tiene lo
# DEGRADA para todo el monorepo en el refresco.
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.labels',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
]

S3 = '1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ'   # S3 · BW
SUBCARPETA = 'respaldo'
ORIGEN = RAIZ / 'out/_respaldo-F-between-sept/31-08_set-completo-27'

# Las 8 que `BetweenSeptiembre.tsx` ya no puede rendir, con la composición que
# quedó huérfana al lado.
HISTORIAS = [
    ('BW ST 04-09 Segun mis calculos.png',      'BW-S-Calculos'),
    ('BW ST 14-09 Cuando es hora de cafe.png',  'BW-S-HoraCafe'),
    ('BW ST 16-09 Cowork te esperamos.png',     'BW-S-Cowork'),
    ('BW ST 18-09 Saludo Fiestas Patrias.png',  'BW-S-Dieciocho'),
    ('BW ST 21-09 Strudel de manzana.png',      'BW-S-Strudel'),
    ('BW ST 22-09 Primavera milkshake.png',     'BW-S-Primavera'),
    ('BW ST 28-09 Humor cafe gigante.png',      'BW-S-HumorToGo'),
    ('BW ST 30-09 Plateada al Carmenere.png',   'BW-S-Plateada'),
]


def servicio():
    tok = Path(str(token_google()))
    c = Credentials.from_authorized_user_file(str(tok), SCOPES)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        faltan = set(SCOPES) - set(c.scopes or [])
        if faltan:
            sys.exit(f'ABORTA: el refresco perdió scopes {faltan}. No se guarda el token.')
        tok.write_text(c.to_json(), encoding='utf-8')
    return build('drive', 'v3', credentials=c)


def carpeta_respaldo(s, crear=True):
    """El id de `respaldo` dentro de S3 — la busca entre lo que subió el token."""
    q = (f"'{S3}' in parents and name='{SUBCARPETA}' and trashed=false "
         "and mimeType='application/vnd.google-apps.folder'")
    hay = s.files().list(q=q, fields='files(id,name)').execute().get('files', [])
    if hay:
        return hay[0]['id'], False
    if not crear:
        return None, False
    fid = s.files().create(
        body={'name': SUBCARPETA, 'parents': [S3],
              'mimeType': 'application/vnd.google-apps.folder'},
        fields='id').execute()['id']
    return fid, True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--listar', action='store_true',
                    help='sólo muestra lo que este token tiene subido en `respaldo`')
    args = ap.parse_args()

    s = servicio()

    if args.listar:
        fid, _ = carpeta_respaldo(s, crear=False)
        if not fid:
            print(f'  todavía no existe `{SUBCARPETA}` en S3')
            return
        for f in s.files().list(q=f"'{fid}' in parents and trashed=false",
                                fields='files(name,size)',
                                orderBy='name').execute().get('files', []):
            mb = int(f.get('size', 0)) / 1048576
            print(f"  {mb:6.1f} MB  {f['name']}")
        print(f"\n  https://drive.google.com/drive/folders/{fid}")
        return

    faltan = [n for n, _ in HISTORIAS if not (ORIGEN / n).is_file()]
    if faltan:
        sys.exit('ABORTA, no están en disco:\n  ' + '\n  '.join(faltan))

    fid, nueva = carpeta_respaldo(s)
    print(f"carpeta `{SUBCARPETA}` {'creada' if nueva else 'ya existía'} en S3 · BW\n")

    for nombre, comp in HISTORIAS:
        previo = s.files().list(
            q=f"'{fid}' in parents and name='{nombre}' and trashed=false",
            fields='files(id)').execute().get('files', [])
        medio = MediaFileUpload(str(ORIGEN / nombre), mimetype='image/png',
                                resumable=True)
        if previo:
            s.files().update(fileId=previo[0]['id'], media_body=medio).execute()
            verbo = '↻ REEMPLAZADA'
        else:
            s.files().create(body={'name': nombre, 'parents': [fid]},
                             media_body=medio, fields='id').execute()
            verbo = '↑ SUBIDA    '
        print(f'  {verbo}  {nombre}   ({comp})')

    print(f'\n  https://drive.google.com/drive/folders/{fid}')


if __name__ == '__main__':
    main()

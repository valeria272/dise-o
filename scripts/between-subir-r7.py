#!/usr/bin/env python3
"""
Sube la RONDA 7 de Between al Drive, a la carpeta fechada de los cambios del día.

Por qué existe además de `between-subir-drive.py`
-------------------------------------------------
El otro script sube el render CRUDO y renombra por `NOMBRES` a partir del id de
composición, siempre a una carpeta fija. Acá hacen falta dos cosas que no da:

  1. **Destino por pieza.** Empezó porque las piezas de la S1 viven en tres
     subcarpetas distintas (`C1 COWORK`, `C2 CUMPLEAÑOS BW`, `STS`) y las de la
     S3 en otra semana. Hoy las 12 apuntan a la misma carpeta fechada, pero el
     mapa por pieza se queda: es lo que permite moverlas a su sitio después.
  2. Se sube lo que salió de `between-entrega.py` —los PNG a **150 ppp** con el
     nombre final—, no el render crudo. El manual pide 150 ppp RGB en digital y
     es lo que se entregó las veces anteriores.

⚠️ Lo que este script NO puede hacer, y hay que saberlo
------------------------------------------------------
El token del estudio tiene alcance **`drive.file`**: crea archivos y puede
actualizar **los que él mismo subió**, pero no ve ni toca los que subió otra
persona. Las piezas de la S1 las subió Eli A MANO el 01-09, así que **no se
pueden reemplazar en su sitio** — y el conector de Drive tampoco pudo moverlas
(«The caller does not have permission»: su cuenta puede crear en la carpeta,
pero no editar archivos ajenos). Por eso las versiones nuevas van a una carpeta
aparte y las viejas quedan intactas hasta que Eli las borre.

⭐ De acá en adelante sí se puede reemplazar en su sitio: estas subidas quedan en
`_subidas.json` y el token es dueño de los archivos nuevos, así que la próxima
ronda usa `--actualizar` y **conserva el enlace y los comentarios** que el
cliente ya tenga. Es la primera vez que la cuenta queda en ese estado.

Uso:
    python scripts/between-subir-r7.py --listar   # no sube, informa
    python scripts/between-subir-r7.py            # sube lo que falte
    python scripts/between-subir-r7.py --actualizar "BW FEED 01-09 Cowork 1 portada.png"
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

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ⚠️ Los 6 de siempre. No recortar: pedir un subconjunto y dejar que el token se
# refresque lo degrada para todo el monorepo (pasó el 29-07-2026).
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.labels',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
]

ENTREGA = RAIZ / 'out/entrega-r7'


def ruta(nombre):
    """`between-entrega.py` agrupa por semana (`out/entrega-r7/S1/…`), así que el
    archivo NO está en la raíz. Se busca recursivamente para no tener que
    duplicar acá el mapa de semanas."""
    hallados = list(ENTREGA.rglob(nombre))
    return hallados[0] if hallados else None

# ⭐⭐ DÓNDE QUEDÓ LA ENTREGA, decisión de Eli el 02-09: «solo deja una carpeta
# con cambios de fecha de 2 de sep». Las 12 piezas viven en UNA sola carpeta
# fechada, hermana de las semanas dentro de `9. SEPTIEMBRE`:
#
#     9. SEPTIEMBRE / CAMBIOS 02-09 BETWEEN
#     └── 1TL4At7--ZSl3jrgJFQ5bbmbOku6LU5Ci
#
# Así la diseñadora revisa el día completo de una mirada, en vez de ir a buscar
# los cambios repartidos en S1 y S3. Y las carpetas de semana quedan TAL CUAL
# las dejó ella: `S1/BW` con sus tres subcarpetas (`C1 COWORK`, `C2 CUMPLEAÑOS
# BW`, `STS`) y `S3/BW` vacía.
CAMBIOS_02_09 = '1TL4At7--ZSl3jrgJFQ5bbmbOku6LU5Ci'

# Los ids de abajo son las subcarpetas ORIGINALES de la S1, donde siguen las
# versiones anteriores (las que Eli subió a mano el 01-09). Se dejan escritos
# porque son el destino final cuando ella borre las viejas y haya que mover las
# nuevas a su sitio: `files().update(addParents=…, removeParents=…)`.
# Leídas del Drive el 02-09-2026. `BW` de la S1 es 1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq.
C1_COWORK = '1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332'
C2_CUMPLE = '1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw'
STS       = '14Z4XnkM9sepmdPV0XjKzoqb1HXMbvIzO'
# «S3 HILTON SEP 2026 / BW» es 1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ (la abrió Eli el
# 02-09 a las 18:27) y quedó VACÍA: sus piezas están en la carpeta única.
S3_BW = '1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ'

# nombre del archivo (tal como lo dejó between-entrega.py) → carpeta destino
DESTINOS = {
    'BW FEED 01-09 Cowork 1 portada.png':        CAMBIOS_02_09,
    'BW FEED 01-09 Cowork 2 winter garden.png':  CAMBIOS_02_09,
    'BW FEED 01-09 Cowork 3 segundo nivel.png':  CAMBIOS_02_09,
    'BW FEED 01-09 Cowork 4 servicio.png':       CAMBIOS_02_09,
    'BW FEED 03-09 Cumpleanos 1.png':            CAMBIOS_02_09,
    'BW FEED 03-09 Cumpleanos 2 detalles.png':   CAMBIOS_02_09,
    'BW ST 01-09 Promo To Go cafe y dulce.png':  CAMBIOS_02_09,
    'BW ST 03-09 Cafe de regalo cumpleanos.png': CAMBIOS_02_09,

    # ⭐ El carrusel PROMOS TO GO (14-sep, S3), completo por primera vez. Se subió
    # primero a una subcarpeta dentro de `S3/BW` y se consolidó acá por decisión
    # de Eli; esa subcarpeta quedó a la basura.
    'BW FEED 14-09 Promos To Go 1 portada.png':  CAMBIOS_02_09,
    'BW FEED 14-09 Promos To Go 2 sandwich.png': CAMBIOS_02_09,
    'BW FEED 14-09 Promos To Go 3 dulce.png':    CAMBIOS_02_09,
    'BW FEED 14-09 Promos To Go 4 trio.png':     CAMBIOS_02_09,
}

# ⛔ NO se sube «BW ST 04-09 Segun mis calculos.png»: está APROBADA en la grilla
#    y no cambió en esta ronda. Subir una pieza que nadie tocó sólo confunde al
#    cliente sobre qué tiene que revisar.


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
    ap.add_argument('--listar', action='store_true')
    ap.add_argument('--actualizar', nargs='+', default=[], metavar='NOMBRE',
                    help='reemplaza en su sitio piezas que ESTE token ya subió '
                         '(conserva enlace y comentarios)')
    a = ap.parse_args()

    manifiesto = ENTREGA / '_subidas.json'
    ya = json.loads(manifiesto.read_text(encoding='utf-8')) if manifiesto.is_file() else {}

    faltan_local = [n for n in DESTINOS if ruta(n) is None]
    if faltan_local:
        sys.exit('✗ No están en out/entrega-r7:\n  ' + '\n  '.join(faltan_local) +
                 '\n\nCórrelo primero:\n  python scripts/between-entrega.py '
                 '--origen out/hilton-between-r7 --salida out/entrega-r7')

    nuevas = [n for n in DESTINOS if n not in ya and n not in a.actualizar]
    updates = [n for n in a.actualizar if n in ya]
    huerfanos = [n for n in a.actualizar if n not in ya]

    if a.listar:
        for n in nuevas:
            print(f'  SUBIR      {n}  -> {DESTINOS[n]}')
        for n in updates:
            print(f'  ACTUALIZAR {n}  (id {ya[n]["id"]})')
        for n in sorted(set(DESTINOS) - set(nuevas) - set(updates)):
            print(f'  ya está    {n}')
        if huerfanos:
            print('\n⚠️ Estas no las subió este token, no se pueden actualizar en su '
                  'sitio:\n  ' + '\n  '.join(huerfanos))
        return

    if huerfanos:
        sys.exit('✗ Este token no subió estas piezas, así que no puede reemplazarlas:\n  '
                 + '\n  '.join(huerfanos) +
                 '\n\nSe suben como nuevas y la vieja se aparta a mano o con el '
                 'conector de Drive.')

    svc = servicio()

    for n in nuevas:
        # Subida REANUDABLE: las piezas pesan hasta 11 MB y la simple se corta.
        media = MediaFileUpload(str(ruta(n)), mimetype='image/png', resumable=True)
        pedido = svc.files().create(
            body={'name': n, 'parents': [DESTINOS[n]]},
            media_body=media, fields='id,name,size')
        resp = None
        while resp is None:
            _, resp = pedido.next_chunk()
        ya[n] = {'id': resp['id'], 'carpeta': DESTINOS[n]}
        print(f'  ✓ subida     {n}  ({int(resp.get("size", 0))/1048576:.1f} MB)  id={resp["id"]}')
        manifiesto.write_text(json.dumps(ya, ensure_ascii=False, indent=2), encoding='utf-8')

    for n in updates:
        media = MediaFileUpload(str(ruta(n)), mimetype='image/png', resumable=True)
        pedido = svc.files().update(fileId=ya[n]['id'], media_body=media, fields='id,name,size')
        resp = None
        while resp is None:
            _, resp = pedido.next_chunk()
        print(f'  ✓ actualizada {n}  (mismo enlace, id={resp["id"]})')

    print(f'\n{len(nuevas)} subidas · {len(updates)} actualizadas')
    print(f'manifiesto: {manifiesto}')
    print('\n⚠️ Las 12 piezas quedan en UNA sola carpeta: '
          '`9. SEPTIEMBRE / CAMBIOS 02-09 BETWEEN`.\n'
          '   Las versiones anteriores siguen INTACTAS en las subcarpetas de la '
          'S1, con sus\n   comentarios y sus enlaces: este token tiene alcance '
          '`drive.file` y no puede\n   tocar lo que Eli subió a mano el 01-09. '
          'Cuando ella borre las viejas, las nuevas\n   se mueven a su sitio con '
          'addParents/removeParents — de ellas sí es dueño.')


if __name__ == '__main__':
    main()

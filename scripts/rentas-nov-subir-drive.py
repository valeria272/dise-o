#!/usr/bin/env python3
"""
Sube la grilla de NOVIEMBRE 2026 de Rentas Nueva Urbe a Drive (copia de rentas-subir-drive.py, que es la de octubre).

Crea (o reutiliza) una carpeta `DISEÑOS` DENTRO de `10. OCTUBRE`, que es donde
vive `RENTAS_NUEVA_URBE_GRILLA_OCTUBRE_2026_1.pptx`. Así la CM abre la carpeta
del mes y encuentra el brief y las piezas en el mismo sitio.

Idempotente: si un archivo con el mismo nombre ya está en la carpeta, lo
ACTUALIZA en vez de duplicarlo — así conserva su ID, su enlace y los comentarios
que la CM haya dejado anclados.

Usa el token OAuth compartido del monorepo con los 6 scopes completos.
NUNCA pedirle un subconjunto: degrada el token de todos los proyectos.

Uso:  ~/copylab-venv/bin/python3 scripts/rentas-subir-drive.py [--dry-run]
"""
import argparse, mimetypes, pathlib, sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import RAIZ, token_google

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

# Destino pedido por Diego el 30-09-2026: la carpeta `10. OCTUBRE` de grillas
# (la que tiene el brief de octubre). Las piezas van en una subcarpeta propia para
# no mezclarse con el PPT de octubre.
CARPETA_MES = "1uqBQPK06qH-_5AOuR9aey05aT7zNPuE6"
NOMBRE_SUB = "NOVIEMBRE 2026 - DISEÑOS"

ENTREGA = RAIZ / "out/rentas/20261100_grilla_noviembre"
PIEZAS = [
    (ENTREGA / "reel/rentas_reel-noviembre-03-11.mp4", "03-11 REEL Recorrido de amenidades.mp4"),
    (ENTREGA / "story/rentas_st-proyecto-04-11.png", "04-11 ST Proyecto Valle Altiplanico.png"),
    (ENTREGA / "feed/rentas_estatico-sin-comision-10-11.png", "10-11 ESTATICO Sin comision.png"),
    (ENTREGA / "feed/rentas_c-paid1.png", "17-11 PAID Arrienda facil 1 portada.png"),
    (ENTREGA / "feed/rentas_c-paid2.png", "17-11 PAID Arrienda facil 2 visita.png"),
    (ENTREGA / "feed/rentas_c-paid3.png", "17-11 PAID Arrienda facil 3 comision.png"),
    (ENTREGA / "feed/rentas_c-paid4.png", "17-11 PAID Arrienda facil 4 ejecutivo.png"),
    (ENTREGA / "feed/rentas_c-paid5.png", "17-11 PAID Arrienda facil 5 cierre.png"),
    (ENTREGA / "feed/rentas_c-airelibre1.png", "24-11 CARRUSEL Aire libre 1 portada.png"),
    (ENTREGA / "feed/rentas_c-airelibre2.png", "24-11 CARRUSEL Aire libre 2 tip 1.png"),
    (ENTREGA / "feed/rentas_c-airelibre3.png", "24-11 CARRUSEL Aire libre 3 tip 2.png"),
    (ENTREGA / "feed/rentas_c-airelibre4.png", "24-11 CARRUSEL Aire libre 4 tip 3.png"),
    (ENTREGA / "feed/rentas_c-airelibre5.png", "24-11 CARRUSEL Aire libre 5 cierre.png"),
    (ENTREGA / "story/rentas_st-encuesta-25-11.png", "25-11 ST Encuesta vida al aire libre.png"),
    (ENTREGA / "NOTAS-PARA-LA-CM.md", "LEEME - notas para la CM.md"),
]

# Mailings: van a la carpeta `MAIL` que Diego creó dentro de NOVIEMBRE 2026 - DISEÑOS.
# Se suben con --mail (subida aparte: otra carpeta de destino).
CARPETA_MAIL = "1DMbH3WWg46dxXavck0saGdIOnSiHs68C"
MAIL = [(ENTREGA / f"mail/rentas_mail{n}-{k}.png", f"MAIL {f} bloque {k.replace('_', ' ')}.png")
        for n, f in ((1, "03-11"), (2, "24-11"))
        for k in ("1_banner", "2_atencion", "3_ficha", "4_cierre")]
MAIL.append((ENTREGA / "NOTAS-MAILING.md", "LEEME - como armar los mailings.md"))


def credenciales():
    tok = pathlib.Path(str(token_google()))
    c = Credentials.from_authorized_user_file(str(tok), SCOPES)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        faltan = set(SCOPES) - set(c.scopes or [])
        if faltan:
            sys.exit(f"ABORTA: el refresco perdería los scopes {faltan}. No se guarda el token.")
        tok.write_text(c.to_json())
    return c


def carpeta_destino(d, dry):
    q = (f"'{CARPETA_MES}' in parents and name = '{NOMBRE_SUB}' "
         "and mimeType = 'application/vnd.google-apps.folder' and trashed = false")
    hay = d.files().list(q=q, fields="files(id,name)", pageSize=5).execute().get("files", [])
    if hay:
        print(f"  carpeta {NOMBRE_SUB} ya existe · {hay[0]['id']}")
        return hay[0]["id"]
    if dry:
        print(f"  [dry-run] crearía la carpeta {NOMBRE_SUB}")
        return None
    f = d.files().create(body={"name": NOMBRE_SUB, "mimeType": "application/vnd.google-apps.folder",
                               "parents": [CARPETA_MES]}, fields="id").execute()
    print(f"  carpeta {NOMBRE_SUB} creada · {f['id']}")
    return f["id"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    # En una ronda de correcciones cambian 5 o 6 piezas, no las 23. Re-subir las
    # otras 17 no rompe nada (actualiza por nombre y conserva los comentarios),
    # pero deja una versión nueva en el historial de Drive de archivos idénticos
    # —y arrastra el reel de 36 MB— así que se puede acotar.
    ap.add_argument("--solo", nargs="+", metavar="PATRON",
                    help="sube sólo las piezas cuyo nombre local o de Drive "
                         "contenga alguno de estos textos")
    ap.add_argument("--mail", action="store_true", help="sube los mailings a la carpeta MAIL")
    a = ap.parse_args()

    piezas = MAIL if a.mail else PIEZAS
    if a.solo:
        piezas = [(l, n) for l, n in PIEZAS
                  if any(t.lower() in l.name.lower() or t.lower() in n.lower()
                         for t in a.solo)]
        if not piezas:
            sys.exit(f"ABORTA: ningún nombre calza con {a.solo}. No se sube nada.")
        print(f"  acotado a {len(piezas)} de {len(PIEZAS)} piezas")

    d = build("drive", "v3", credentials=credenciales())
    destino = CARPETA_MAIL if a.mail else carpeta_destino(d, a.dry_run)

    for local, nombre in piezas:
        if not local.exists():
            print(f"  ⚠ falta {local}")
            continue
        mb = local.stat().st_size / 1e6
        if a.dry_run:
            print(f"  [dry-run] {nombre:46s} {mb:6.1f} MB")
            continue
        tipo = mimetypes.guess_type(str(local))[0] or "application/octet-stream"
        medio = MediaFileUpload(str(local), mimetype=tipo, resumable=True)
        q = f"'{destino}' in parents and name = '{nombre}' and trashed = false"
        ya = d.files().list(q=q, fields="files(id)", pageSize=2).execute().get("files", [])
        if ya:
            d.files().update(fileId=ya[0]["id"], media_body=medio).execute()
            print(f"  actualizado  {nombre:46s} {mb:6.1f} MB")
        else:
            d.files().create(body={"name": nombre, "parents": [destino]},
                             media_body=medio, fields="id").execute()
            print(f"  subido       {nombre:46s} {mb:6.1f} MB")

    if destino:
        print(f"\n  https://drive.google.com/drive/folders/{destino}")


if __name__ == "__main__":
    main()

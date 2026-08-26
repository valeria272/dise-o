#!/usr/bin/env python3
"""Baja material de una carpeta de Drive y VERIFICA que haya llegado bien.

    python3 scripts/bajar-de-drive.py <id-carpeta> <destino> [--recursivo] [--solo imagen|video|editable|fuente]
    python3 scripts/bajar-de-drive.py --listar <id-carpeta>

Por qué existe: el 25-08-2026 se diseñaron 8 piezas de Revex con referencias que
en realidad eran la página de login de Google guardada con extensión .jpg — 905 KB
cada una, todas parecidas a una foto. Nadie las abrió. El conector MCP falla en
silencio con archivos >10 MB y con la carpeta que no creó la app.

Este script hace tres cosas que el conector no hace:
  1. usa el token OAuth completo (ve todo lo que ve la cuenta, no sólo `drive.file`)
  2. **verifica cada archivo por su cabecera** y borra el que llegó mal
  3. reintenta, y al final dice exactamente qué falta

⚠️ LOS DOS CAMINOS, y cuál usar cuando:

  · **Conector MCP de Drive** (desde el chat) — es el que SÍ ve las carpetas de los
    clientes y de las diseñadoras. Úsalo para listar y para bajar lo normal.
    Su límite: archivos grandes (>10 MB) fallan o llegan truncados.

  · **Este script** — el token OAuth local tiene scope `drive.file`, o sea **sólo ve
    los archivos que creó la propia app**. Para una carpeta de cliente va a devolver
    0 archivos, y eso NO es un error tuyo. Sirve para dos cosas:
      --publico  : bajar por ID cualquier archivo con enlace compartido, sin límite
                   de tamaño. Es el camino para los editables .ai y los videos.
      verificar  : da igual cómo bajaste, corre la verificación al final.

Las Google Docs/Sheets se exportan (a .xlsx / .docx / .pdf) en vez de descargarse.
"""
import argparse
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402

FIRMAS = {
    b"\x89PNG\r\n\x1a\n": "png", b"\xff\xd8\xff": "jpg", b"GIF8": "gif",
    b"%PDF": "pdf", b"PK\x03\x04": "zip/ai/docx/xlsx", b"OTTO": "otf",
    b"\x00\x01\x00\x00": "ttf", b"wOFF": "woff", b"wOF2": "woff2",
}
GRUPOS = {
    "imagen":   (".png", ".jpg", ".jpeg", ".webp", ".gif", ".tif", ".tiff"),
    "video":    (".mp4", ".mov", ".m4v", ".webm"),
    "editable": (".ai", ".psd", ".indd", ".zip", ".pdf", ".sketch", ".fig"),
    "fuente":   (".otf", ".ttf", ".woff", ".woff2"),
}
EXPORTA = {
    "application/vnd.google-apps.spreadsheet":
        ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", ".xlsx"),
    "application/vnd.google-apps.document":
        ("application/vnd.openxmlformats-officedocument.wordprocessingml.document", ".docx"),
    "application/vnd.google-apps.presentation": ("application/pdf", ".pdf"),
}
CARPETA = "application/vnd.google-apps.folder"


def servicio():
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    ruta = token_google()
    if not ruta or not os.path.exists(ruta):
        sys.exit("✗ No encuentro el token de Google.\n"
                 "  Corre  python3 scripts/_entorno.py  para ver dónde lo busca.\n"
                 "  Si no lo tienes, usa el conector MCP de Drive desde el chat.")
    # ⚠️ Sin lista de scopes: pedir un subconjunto degrada el token compartido
    # de todo el monorepo al refrescarlo. Ver CLAUDE.md de la raíz.
    return build("drive", "v3", credentials=Credentials.from_authorized_user_file(ruta),
                 cache_discovery=False)


def listar(srv, carpeta, recursivo=False, _prefijo=""):
    salida, page = [], None
    while True:
        r = srv.files().list(
            q=f"'{carpeta}' in parents and trashed = false",
            fields="nextPageToken, files(id,name,mimeType,size,md5Checksum)",
            pageSize=1000, pageToken=page,
            supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
        for f in r.get("files", []):
            f["_ruta"] = _prefijo + f["name"]
            if f["mimeType"] == CARPETA:
                if recursivo:
                    salida += listar(srv, f["id"], True, f["_ruta"] + "/")
            else:
                salida.append(f)
        page = r.get("nextPageToken")
        if not page:
            break
    return salida


def tipo_real(ruta):
    with open(ruta, "rb") as fh:
        cab = fh.read(16)
    for firma, nombre in FIRMAS.items():
        if cab.startswith(firma):
            return nombre
    if cab[:4] == b"RIFF":
        return "riff/webp"
    if cab[4:8] in (b"ftyp",):
        return "mp4/mov"
    if cab[:1] in (b"<", b"{") or cab[:5].lower() == b"<!doc":
        return "HTML/texto"
    return "desconocido"


def baja_uno(srv, f, destino):
    from googleapiclient.http import MediaIoBaseDownload
    nombre = f["_ruta"]
    exp = EXPORTA.get(f["mimeType"])
    if exp:
        mime, ext = exp
        if not nombre.lower().endswith(ext):
            nombre += ext
        pedido = srv.files().export_media(fileId=f["id"], mimeType=mime)
    else:
        pedido = srv.files().get_media(fileId=f["id"], supportsAllDrives=True)

    ruta = os.path.join(destino, nombre)
    os.makedirs(os.path.dirname(ruta) or ".", exist_ok=True)
    buf = io.BytesIO()
    bajador = MediaIoBaseDownload(buf, pedido, chunksize=8 * 1024 * 1024)
    hecho = False
    while not hecho:
        _, hecho = bajador.next_chunk()
    datos = buf.getvalue()
    if not datos:
        return None, "llegó vacío"
    with open(ruta, "wb") as fh:
        fh.write(datos)

    # Verificación: ¿es lo que dice ser?
    ext = os.path.splitext(ruta)[1].lower()
    esperado = None
    for grupo, exts in GRUPOS.items():
        if ext in exts:
            esperado = grupo
    t = tipo_real(ruta)
    if t in ("HTML/texto", "desconocido") and esperado in ("imagen", "video", "fuente"):
        os.remove(ruta)
        return None, f"llegó como {t}, no como {esperado} — descarga fallida"
    return ruta, None


def baja_publicos(ids, destino):
    """Baja por enlace compartido. Sin OAuth y sin el techo de 10 MB del MCP."""
    import subprocess
    if os.path.isfile(ids):
        lista = [l.strip() for l in open(ids) if l.strip() and not l.startswith("#")]
    else:
        lista = [x.strip() for x in ids.split(",") if x.strip()]
    os.makedirs(destino, exist_ok=True)
    ok, fallidos = [], []
    for i, fid in enumerate(lista, 1):
        # El ID puede venir pegado como "nombre=ID" para conservar el nombre
        nombre, _, solo_id = fid.rpartition("=")
        solo_id = solo_id or fid
        ruta = os.path.join(destino, nombre or solo_id)
        url = f"https://drive.google.com/uc?export=download&id={solo_id}"
        subprocess.run(["curl", "-sL", "-o", ruta, url], check=False)
        if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
            fallidos.append((solo_id, "vacío")); print(f"  [{i}] ✗ {solo_id} — vacío")
            continue
        t = tipo_real(ruta)
        if t in ("HTML/texto", "desconocido"):
            os.remove(ruta)
            fallidos.append((solo_id, f"llegó como {t} — ¿el enlace no es público?"))
            print(f"  [{i}] ✗ {solo_id} — llegó como {t}")
        else:
            ok.append(ruta); print(f"  [{i}] ✓ {os.path.basename(ruta)}  ({t})")
    print(f"\n── {len(ok)} bajados · {len(fallidos)} fallidos ──")
    if fallidos:
        print("\n⛔ Los que llegaron como HTML casi siempre significan que el archivo\n"
              "   NO está compartido por enlace. Pídele a quien lo tiene que lo\n"
              "   comparta, o bájalo con el conector MCP si pesa menos de 10 MB.")
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("carpeta", help="ID de la carpeta de Drive")
    ap.add_argument("destino", nargs="?", help="carpeta local de destino")
    ap.add_argument("--recursivo", action="store_true")
    ap.add_argument("--listar", action="store_true", help="sólo mostrar qué hay")
    ap.add_argument("--solo", choices=list(GRUPOS), help="filtrar por tipo")
    ap.add_argument("--reintentos", type=int, default=2)
    ap.add_argument("--publico", action="store_true",
                    help="bajar por enlace compartido, sin OAuth y sin límite de "
                         "tamaño. `carpeta` pasa a ser una lista de IDs separada "
                         "por comas, o un archivo .txt con un ID por línea.")
    a = ap.parse_args()

    if a.publico:
        return baja_publicos(a.carpeta, a.destino)

    srv = servicio()
    archivos = listar(srv, a.carpeta, a.recursivo or a.listar)
    if not archivos:
        print("\n0 archivos. Ojo: el token local tiene scope `drive.file`, así que\n"
              "sólo ve lo que creó esta app. Si es una carpeta de cliente, es lo\n"
              "esperado — NO es que la carpeta esté vacía.\n\n"
              "  → Lístala con el conector MCP desde el chat, y para los archivos\n"
              "    pesados usa:  --publico <id1,id2,...> <destino>")
        return 1
    if a.solo:
        exts = GRUPOS[a.solo]
        archivos = [f for f in archivos
                    if os.path.splitext(f["name"])[1].lower() in exts]

    if a.listar or not a.destino:
        print(f"\n{len(archivos)} archivo(s):\n")
        for f in archivos:
            mb = int(f.get("size", 0)) / 1048576 if f.get("size") else 0
            print(f"  {f['_ruta'][:70]:70} {mb:7.1f} MB  {f['mimeType'].split('.')[-1]}")
        return 0

    os.makedirs(a.destino, exist_ok=True)
    ok, fallidos = [], []
    for i, f in enumerate(archivos, 1):
        for intento in range(a.reintentos + 1):
            try:
                ruta, error = baja_uno(srv, f, a.destino)
            except Exception as e:
                ruta, error = None, str(e)[:120]
            if ruta:
                ok.append(ruta)
                print(f"  [{i}/{len(archivos)}] ✓ {f['_ruta']}")
                break
            if intento == a.reintentos:
                fallidos.append((f["_ruta"], error))
                print(f"  [{i}/{len(archivos)}] ✗ {f['_ruta']} — {error}")

    print(f"\n── {len(ok)} bajados · {len(fallidos)} fallidos ──")
    if fallidos:
        print("\n⛔ NO SE DISEÑA con material incompleto. Fallaron:")
        for n, e in fallidos:
            print(f"   ✗ {n} — {e}")
        print("\n   Prueba de nuevo, o pide el archivo por otra vía.")
        return 1
    print(f"\n✅ Todo verificado en {a.destino}")
    print(f"   Siguiente paso — MIRA lo que bajaste antes de diseñar:")
    print(f"   python3 scripts/hoja-contacto.py {a.destino} out/_verificacion/material.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())

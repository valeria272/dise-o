#!/usr/bin/env python3
"""
Lista los comentarios de todos los archivos de una carpeta de Drive (y sus subcarpetas).

Los archivos tienen que haberlos subido este mismo token: el token compartido sólo
tiene `drive.file`, así que comments.list responde para lo que subimos nosotros.

Uso:
    ~/copylab-venv/bin/python3 scripts/drive-comentarios.py <folderId> [--json salida.json]
"""
import json, os, pathlib, sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google as _token_google

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
CAMPOS = ("comments(id,author(displayName),content,resolved,createdTime,modifiedTime,anchor,"
          "quotedFileContent(value),replies(author(displayName),content,createdTime))")


def creds():
    tok = pathlib.Path(str(_token_google()))
    c = Credentials.from_authorized_user_file(str(tok), SCOPES)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        faltan = set(SCOPES) - set(c.scopes or [])
        if faltan:
            sys.exit(f"ABORTA: el refresco perdió scopes {faltan}. No se guarda el token.")
        tok.write_text(c.to_json())
    return c


def recorrer(d, fid, ruta=""):
    """Devuelve [(ruta_legible, archivo)] de la carpeta y sus subcarpetas."""
    salida, tok = [], None
    while True:
        r = d.files().list(q=f"'{fid}' in parents and trashed=false",
                           fields="nextPageToken,files(id,name,mimeType,modifiedTime)",
                           pageSize=200, pageToken=tok, supportsAllDrives=True).execute()
        for f in r.get("files", []):
            if f["mimeType"] == "application/vnd.google-apps.folder":
                salida += recorrer(d, f["id"], f"{ruta}{f['name']}/")
            else:
                salida.append((ruta, f))
        tok = r.get("nextPageToken")
        if not tok:
            break
    return salida


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    fid = args[0]
    destino = None
    if "--json" in sys.argv:
        destino = sys.argv[sys.argv.index("--json") + 1]

    d = build("drive", "v3", credentials=creds())
    archivos = sorted(recorrer(d, fid), key=lambda x: (x[0], x[1]["name"]))
    print(f"{len(archivos)} archivos bajo {fid}\n")

    todo, total = {}, 0
    for ruta, f in archivos:
        try:
            cs = d.comments().list(fileId=f["id"], fields=CAMPOS, pageSize=100,
                                   includeDeleted=False).execute().get("comments", [])
        except Exception as e:
            print(f"!! {ruta}{f['name']}: {e}")
            continue
        if not cs:
            continue
        total += len(cs)
        print(f"=== {ruta}{f['name']}  ({f['id']}) ===")
        for c in cs:
            marca = " [RESUELTO]" if c.get("resolved") else ""
            print(f"  · ({c['author']['displayName']} · {c['createdTime']}){marca}")
            print(f"    {c['content'].strip()}")
            for rp in c.get("replies", []):
                print(f"      ↳ ({rp['author']['displayName']}): {rp['content'].strip()}")
        print()
        todo[f"{ruta}{f['name']}"] = cs

    print(f"total: {total} comentarios en {len(todo)} archivos")
    if destino:
        json.dump(todo, open(destino, "w"), ensure_ascii=False, indent=1)
        print(f"→ {destino}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Sube las piezas de REVEX septiembre a una carpeta de DISEÑO PAID en Drive.

Generaliza a `revex-sep-subir-v2.py`, que tenía la carpeta «v2» quemada.

    ~/copylab-venv/bin/python3 scripts/revex-sep-subir.py "Versión 4" [--dry-run]

Autenticación, en este orden:
  1. El token compartido del monorepo, si está (`_entorno.token_google()`).
  2. Si no está, flujo local de OAuth pidiendo **sólo `drive.file`** y guardando
     en `~/.copylab-drive-token.json`, FUERA del repo.

`drive.file` alcanza para crear y subir, y no da acceso al resto del Drive. El token
va a un archivo propio a propósito: pedirle un subconjunto de scopes al token
compartido lo degradaría para todos los demás proyectos.
"""
import os, pathlib, sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google

SCOPES_SUBIR = ["https://www.googleapis.com/auth/drive.file"]
CLIENTE = pathlib.Path("/Users/sere/Documents/SERE PROJECTS CLAUDE/GA4-GTM-EXPERTO/"
                       "client_secret_829570758817-uh6b0snf032t85me0rrqbe8iuaqkdliq"
                       ".apps.googleusercontent.com.json")
TOKEN_PROPIO = pathlib.Path.home() / ".copylab-drive-token.json"
CARPETA_LOCAL = pathlib.Path(str(_RAIZ / "out/revex/sep2026"))
DISENO_PAID = "1uMPBBoOpspRKBEqtiZOElJuMEDuaisl2"


def credenciales():
    # OJO: `token_google()` devuelve None si no hay token. Convertirlo a Path("")
    # da Path("."), que **existe** porque es un directorio: hay que preguntar por
    # is_file(), no por exists(), o se intenta abrir el directorio actual.
    ruta = _token_google()
    compartido = pathlib.Path(str(ruta)) if ruta else None
    if compartido and compartido.is_file():
        print(f"  usando el token compartido: {compartido}")
        c = Credentials.from_authorized_user_file(str(compartido))
        if c.expired and c.refresh_token:
            c.refresh(Request())
        return c
    if TOKEN_PROPIO.exists():
        print(f"  usando el token propio: {TOKEN_PROPIO}")
        c = Credentials.from_authorized_user_file(str(TOKEN_PROPIO), SCOPES_SUBIR)
        if c.expired and c.refresh_token:
            c.refresh(Request()); TOKEN_PROPIO.write_text(c.to_json())
        return c
    if not CLIENTE.exists():
        sys.exit(f"ABORTA: no hay token ni client secret en {CLIENTE}")
    from google_auth_oauthlib.flow import InstalledAppFlow
    print("  no hay token. Abriendo el navegador para autorizar (sólo drive.file)…")
    flujo = InstalledAppFlow.from_client_secrets_file(str(CLIENTE), SCOPES_SUBIR)
    c = flujo.run_local_server(port=0, prompt="consent",
                               authorization_prompt_message="Autoriza en el navegador: {url}",
                               success_message="Listo, ya puedes cerrar esta pestaña.")
    TOKEN_PROPIO.write_text(c.to_json())
    os.chmod(TOKEN_PROPIO, 0o600)
    print(f"  token guardado en {TOKEN_PROPIO} (permisos 600)")
    return c


def main():
    nombre = next((a for a in sys.argv[1:] if not a.startswith("--")), None)
    if not nombre:
        sys.exit('Falta el nombre de la carpeta. Ej: scripts/revex-sep-subir.py "Versión 4"')
    seco = "--dry-run" in sys.argv

    archivos = sorted(CARPETA_LOCAL.glob("*.png"))
    if not archivos:
        sys.exit(f"ABORTA: no hay PNG en {CARPETA_LOCAL}")
    print(f"  {len(archivos)} piezas en {CARPETA_LOCAL}")
    if seco:
        for a in archivos:
            print(f"    (seco) {a.name}  {a.stat().st_size/1048576:.2f} MB")
        return

    svc = build("drive", "v3", credentials=credenciales(), cache_discovery=False)

    r = svc.files().list(q=f"'{DISENO_PAID}' in parents and name = '{nombre}' "
                           f"and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
                         fields="files(id,name)").execute()
    if r.get("files"):
        carpeta = r["files"][0]["id"]
        print(f"  carpeta «{nombre}» ya existe: {carpeta}")
    else:
        carpeta = svc.files().create(
            body={"name": nombre, "mimeType": "application/vnd.google-apps.folder",
                  "parents": [DISENO_PAID]}, fields="id").execute()["id"]
        print(f"  carpeta «{nombre}» creada: {carpeta}")

    previos = {f["name"]: f["id"] for f in svc.files().list(
        q=f"'{carpeta}' in parents and trashed = false",
        fields="files(id,name)").execute().get("files", [])}

    for a in archivos:
        medio = MediaFileUpload(str(a), mimetype="image/png", resumable=True)
        if a.name in previos:
            f = svc.files().update(fileId=previos[a.name], media_body=medio,
                                   fields="id,name,size").execute()
            print(f"    ↻ {f['name']}  {int(f.get('size',0))/1048576:.2f} MB (reemplazado)")
        else:
            f = svc.files().create(body={"name": a.name, "parents": [carpeta]},
                                   media_body=medio, fields="id,name,size").execute()
            print(f"    ✓ {f['name']}  {int(f.get('size',0))/1048576:.2f} MB")

    print(f"\n  https://drive.google.com/drive/folders/{carpeta}")


if __name__ == "__main__":
    main()

"""Reemplaza la entrega de Casablanca en su carpeta de Drive.

⚠️ Este script BORRA: manda a la papelera TODO lo que haya en la carpeta antes de
subir. La papelera de Drive es recuperable, pero no se corre sin que alguien lo
pida explícitamente. Se usó el 25-08-2026 para reemplazar la v2 rechazada por la
v3 editorial.

A diferencia de `casablanca-drive-subir.py` —que sólo agrega— este deja la
carpeta exactamente con las 14 piezas de `out/casablanca/editorial/` numeradas en
orden de carrusel, más las notas de revisión.
"""
import json, os, sys
from pathlib import Path
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where(); os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
sys.path.insert(0, "scripts")
from _entorno import RAIZ, token_google
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/calendar",
          "https://www.googleapis.com/auth/gmail.send",
          "https://www.googleapis.com/auth/gmail.modify",
          "https://www.googleapis.com/auth/gmail.labels",
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file"]
TOKEN = str(token_google())
CARPETA = "13pOfaekruRWq8PEHrG0be20Bq6eG4yCB"   # Diseño Casablanca Septiembre 2026
ORIGEN = Path(str(RAIZ / "out/casablanca/sep"))
NOTAS = Path(str(RAIZ / "out/casablanca/editorial/LEEME - notas de revision.txt"))

# El orden es el del brief, tarjeta por tarjeta.
NOMBRES = {
    "c1a": "cb_sep_c1-1-roble-natural-uv-190x1900",
    "c1b": "cb_sep_c1-2-roble-natural-uv-167x1200",
    "c1c": "cb_sep_c1-3-roble-aserrado",
    "c1d": "cb_sep_c1-4-cumaru",
    "c2a": "cb_sep_c2-1-ven-a-ver-tu-piso",
    "c2b": "cb_sep_c2-2-compara-texturas",
    "c2c": "cb_sep_c2-3-te-esperamos",
}

c = Credentials.from_authorized_user_file(TOKEN, SCOPES)
if not c.valid:
    c.refresh(Request())
    if set(SCOPES) - set(c.scopes or []):
        sys.exit("ABORTA: el refresco perdió scopes")
    json.dump(json.loads(c.to_json()), open(TOKEN, "w"), indent=2)
d = build("drive", "v3", credentials=c, cache_discovery=False)

def hijos():
    return d.files().list(q=f"'{CARPETA}' in parents and trashed=false",
        fields="files(id,name,mimeType)", pageSize=400,
        supportsAllDrives=True, includeItemsFromAllDrives=True).execute().get("files", [])

previos = hijos()
print(f"Había {len(previos)} archivos en la carpeta.\n")

print("→ A la papelera (recuperables desde Drive):")
for f in previos:
    d.files().update(fileId=f["id"], body={"trashed": True}, supportsAllDrives=True).execute()
    print(f"    – {f['name']}")

print("\n→ Subiendo la v3:")
subidos = 0
for pieza, base in NOMBRES.items():
    for fmt in ("feed", "story"):
        ruta = ORIGEN / f"{pieza}_{fmt}.png"
        if not ruta.exists():
            print(f"    ! FALTA {ruta.name}"); continue
        d.files().create(
            body={"name": f"{base}_{fmt}.png", "parents": [CARPETA]},
            media_body=MediaFileUpload(str(ruta), mimetype="image/png", resumable=True),
            fields="id", supportsAllDrives=True).execute()
        print(f"    + {base}_{fmt}.png")
        subidos += 1

d.files().create(
    body={"name": "LEEME - notas de revision.txt", "parents": [CARPETA]},
    media_body=MediaFileUpload(str(NOTAS), mimetype="text/plain", resumable=True),
    fields="id", supportsAllDrives=True).execute()
print("    + LEEME - notas de revision.txt")

print(f"\nListo: {len(previos)} a la papelera, {subidos} piezas + notas arriba.")
final = hijos()
print(f"La carpeta queda con {len(final)} archivos.")

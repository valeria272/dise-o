# -*- coding: utf-8 -*-
"""Vuelca todas las celdas de texto de un Google Sheet nativo, por hoja."""
import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "scripts"))
from _entorno import token_google as _token_google
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
ruta = _token_google()
creds = Credentials.from_authorized_user_file(str(ruta), SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())
svc = build("sheets", "v4", credentials=creds)

sid = sys.argv[1]
meta = svc.spreadsheets().get(spreadsheetId=sid, fields="properties.title,sheets.properties").execute()
print("== " + meta["properties"]["title"])
hojas = [s["properties"]["title"] for s in meta["sheets"]]
print("hojas:", hojas)
out = {}
for h in hojas:
    try:
        r = svc.spreadsheets().values().get(spreadsheetId=sid, range=f"'{h}'").execute()
    except Exception as e:
        print(f"  !! {h}: {e}"); continue
    out[h] = r.get("values", [])
    print(f"  {h}: {len(out[h])} filas")
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)

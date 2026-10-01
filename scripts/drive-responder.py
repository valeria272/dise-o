#!/usr/bin/env python3
"""Responde un comentario de Drive y lo deja RESUELTO.

    python scripts/drive-responder.py <fileId> <commentId> "Aplicado: …"

Cierra el ciclo de `drive-comentarios.py` (leer → aplicar → responder y resolver):
un comentario aplicado que queda abierto hace creer al que retoma que falta
hacerlo (manual de Tierra Calma § 4 sexies · 6). Sólo funciona sobre archivos que
subió este mismo token (`drive.file`).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import credenciales_google
from googleapiclient.discovery import build

def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    fid, cid, texto = sys.argv[1], sys.argv[2], sys.argv[3]
    svc = build("drive", "v3", credentials=credenciales_google(), cache_discovery=False)
    r = svc.replies().create(fileId=fid, commentId=cid, fields="id,action,content",
                             body={"content": texto, "action": "resolve"}).execute()
    print("✓ respondido y resuelto:", r.get("id"), r.get("action"))

if __name__ == "__main__":
    main()

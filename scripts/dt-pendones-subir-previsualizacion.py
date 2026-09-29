#!/usr/bin/env python3
"""DT · pendones 0,8×3 — sube los PNG de PREVISUALIZACIÓN (150 ppp) a la carpeta de Eli
«PENDONES 2026 ACTUALIZADOS» (1ksPasLUqIT2Gj574nIqh6ydiB5biUb8R). Pedido de Eli 29-09:
«una vez corregido sube acá la imagen png en 150ppp solo para previsualizar».

Los PNG salen del .ai (`Pendones DT 2026 0,8x3m.ai`, export PNG24 al 208,33 %) y viven en F:
junto al editable. Si ya existe uno con el mismo nombre se REEMPLAZA su contenido (conserva el
enlace); después se compara el md5 de Drive con el local.

    py -3 scripts/dt-pendones-subir-previsualizacion.py "CHICA ENTRADA" COOKIE
"""
import hashlib, os, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

CARPETA = "1ksPasLUqIT2Gj574nIqh6ydiB5biUb8R"
F = pathlib.Path("F:/SOLICITUDES 2026 HILTON/Pendon editable 2026 0,8x3m/Pendones 2026 caras nuevas")
# ⚠️ Los PNG que subió Eli (dueña: ella) NO se pueden reemplazar ni mandar a la papelera: el token
# es drive.file (404) y el conector MCP no tiene permiso. La ronda 8 (29-09) subió los suyos como
# «… CORREGIDO.png» y, a pedido de Eli, se renombraron al nombre original; los suyos quedaron
# como «ANTERIOR - …» (el conector SÍ renombra, pero no mueve ni borra). Desde ahora se reemplazan por ID.
IDS = {"CHICA ENTRADA": "1CcGr4rX9LGT0CzzZx9YkiT4iROQzmC44",   # nombre original, subido por el estudio
       "COOKIE": "1xqBQL_pX0gfgrJzl8bgYXYTKI_TU22xx",          # nombre original, subido por el estudio
       "CHICA BOTELLA": "1inkly_ua7bjfYv7q3LaNIK9joQxcSsQw"}   # de Eli: no se puede reemplazar


def servicio():
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    d = servicio()
    for n in sys.argv[1:]:
        p = F / f"Pendones DT 2026 0,8x3m {n}.png"
        media = MediaFileUpload(str(p), mimetype="image/png", resumable=True, chunksize=16 << 20)
        try:
            r = d.files().update(fileId=IDS[n], media_body=media, fields="id,md5Checksum",
                                 supportsAllDrives=True).execute()
            accion = "reemplazado"
        except Exception as e:  # el token (drive.file) puede no ver un archivo que subió Eli
            print(f"  ! no se pudo reemplazar {n} por ID ({str(e)[:120]}) → se sube nuevo")
            r = d.files().create(body={"name": p.name, "parents": [CARPETA]}, media_body=media,
                                 fields="id,md5Checksum", supportsAllDrives=True).execute()
            accion = "subido NUEVO (queda el viejo: hay que mandarlo a la papelera)"
        ok = "✓ md5 igual" if r.get("md5Checksum") == md5(p) else "✗ md5 DISTINTO"
        print(f"  ↑ {p.name} · {accion} · id {r['id']} · {ok}")


if __name__ == "__main__":
    main()

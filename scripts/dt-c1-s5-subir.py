#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — sube la entrega al Drive, con la RENUMERACIÓN.

    python scripts/dt-c1-s5-subir.py --ensayo    # dice qué haría, no toca nada
    python scripts/dt-c1-s5-subir.py             # lo hace
    python scripts/dt-c1-s5-subir.py --gif       # además, los GIF a su carpeta

⛔⛔ POR QUÉ ESTE SCRIPT NO ES UN «SUBE LOS ARCHIVOS DE ESTA CARPETA».

El 21-09 entró el slide del GYM en el lugar 4 del brief, así que **el carrusel
se renumeró**: lo que en el Drive se llama `C1 S5 DT n°5.mp4` es el CIERRE, y lo
que ahora va en el lugar 5 es el GYM. Un «reemplazar por nombre» a ciegas pisa
el cierre con el gym y deja el carrusel con cinco láminas y un hueco.

⭐ **La salida correcta NO es re-subir el cierre: es RENOMBRARLO.** El archivo
del cierre ya está arriba con su `fileId`; se le cambia el nombre a `n°6` y
conserva su enlace, su historial y sus 22 MB sin volver a viajar. Después el gym
sube como archivo NUEVO en el `n°5` que quedó libre. Quien tenga el enlace viejo
del `n°5` sigue viendo el cierre, que es lo que ese enlace siempre mostró.

⚠️ Antes de mover nada, el script **verifica por md5** que el archivo que va a
renombrar sea de verdad el cierre. Si el Drive trae otra cosa, se planta.

⚠️ El token es scope `drive.file`: sólo ve lo que subió él. Por eso puede listar
y tocar estos seis mp4 —los subió él— pero `files.get` sobre la CARPETA da 404.
No es un error: es el modo normal de esta cuenta.
"""
import argparse
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import token_google                              # noqa: E402

from google.auth.transport.requests import Request             # noqa: E402
from google.oauth2.credentials import Credentials              # noqa: E402
from googleapiclient.discovery import build                    # noqa: E402
from googleapiclient.http import MediaFileUpload               # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                              # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ENTREGA = RAIZ / "out/hilton/dt/c1-s5/entrega"
ENTREGA_GIF = RAIZ / "out/hilton/dt/c1-s5/entrega-gif"

# ⭐ RONDA 9 (23-09): Eli movió el carrusel a `S5 HILTON SEP 2026 › DT › C2-28SEP`
# (el Turismo pasó a ser el C1 de la semana). Los archivos conservan el nombre
# `C1 S5 DT n°…` que ella dejó.
CARPETA = "1WXTx7b62fI5-heMZ0PDu85zCJWBxq1y3"
CARPETA_GIF = "C1 S5 DT - GIF"

# El archivo que hay que RENOMBRAR, y con qué md5 se reconoce.
# ⭐ RONDA 8-9: entra QB en el lugar 6 y el cierre pasa de n°6 a n°7. El md5 se
# compara contra la entrega de la ronda 7, que es lo que hay arriba.
CIERRE_EN_DRIVE = "C1 S5 DT n°6.mp4"
CIERRE_NUEVO = "C1 S5 DT n°7.mp4"
CIERRE_ARRIBA = RAIZ / "out/hilton/dt/c1-s5/entrega-r7/C1 S5 DT n°6.mp4"


def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def servicio():
    cr = Credentials.from_authorized_user_file(str(token_google()))
    if not cr.valid and cr.refresh_token:
        cr.refresh(Request())
    return build("drive", "v3", credentials=cr)


def listar(sv, carpeta: str) -> dict:
    r = sv.files().list(q=f"'{carpeta}' in parents and trashed=false",
                        fields="files(id,name,md5Checksum,size)",
                        pageSize=200).execute()
    return {f["name"]: f for f in r["files"]}


def sube(sv, ruta: Path, carpeta: str, existente: dict, ensayo: bool) -> str:
    tipo = "image/gif" if ruta.suffix == ".gif" else "video/mp4"
    viejo = existente.get(ruta.name)
    if viejo and viejo.get("md5Checksum") == md5(ruta):
        print(f"  = {ruta.name} ya está arriba e idéntico — no se toca")
        return viejo["id"]
    if ensayo:
        print(f"  {'↻ reemplazaría' if viejo else '+ subiría'} {ruta.name}")
        return viejo["id"] if viejo else "—"
    media = MediaFileUpload(str(ruta), mimetype=tipo, resumable=True)
    if viejo:
        f = sv.files().update(fileId=viejo["id"], media_body=media,
                              fields="id").execute()
        print(f"  ↻ {ruta.name} reemplazado (mismo enlace)")
    else:
        f = sv.files().create(body={"name": ruta.name, "parents": [carpeta]},
                              media_body=media, fields="id").execute()
        print(f"  + {ruta.name} subido")
    return f["id"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ensayo", action="store_true")
    ap.add_argument("--gif", action="store_true")
    a = ap.parse_args()
    sv = servicio()
    arriba = listar(sv, CARPETA)

    # ── 1 · la renumeración, y su verificación ────────────────────────────
    cierre_local = CIERRE_ARRIBA
    en_drive = arriba.get(CIERRE_EN_DRIVE)
    if arriba.get(CIERRE_NUEVO):
        print(f"✅ {CIERRE_NUEVO} ya existe en Drive — la renumeración ya se hizo")
    elif not en_drive:
        print(f"⛔ no encuentro {CIERRE_EN_DRIVE} en la carpeta. Reviso a mano.")
        return 1
    else:
        esperado = md5(cierre_local)
        if en_drive.get("md5Checksum") != esperado:
            print(f"⛔ EL {CIERRE_EN_DRIVE} DE DRIVE NO ES EL CIERRE.")
            print(f"   drive {en_drive.get('md5Checksum')} · local {esperado}")
            print("   No renombro nada: hay que mirarlo.")
            return 1
        print(f"✅ verificado por md5: {CIERRE_EN_DRIVE} ES el cierre")
        if a.ensayo:
            print(f"  → renombraría a {CIERRE_NUEVO} (mismo fileId, mismo enlace)")
        else:
            sv.files().update(fileId=en_drive["id"],
                              body={"name": CIERRE_NUEVO}).execute()
            print(f"  ✅ renombrado a {CIERRE_NUEVO} — {en_drive['id']}")
        arriba = listar(sv, CARPETA) if not a.ensayo else arriba

    # ── 2 · las seis láminas ──────────────────────────────────────────────
    print("\nLáminas:")
    for src in sorted(ENTREGA.glob("C1 S5 DT n°*.mp4")):
        sube(sv, src, CARPETA, arriba, a.ensayo)

    # ── 3 · los GIF, en su propia carpeta ─────────────────────────────────
    if a.gif:
        print(f"\nGIF — carpeta «{CARPETA_GIF}»:")
        r = sv.files().list(
            q=(f"'{CARPETA}' in parents and name='{CARPETA_GIF}' and "
               "mimeType='application/vnd.google-apps.folder' and trashed=false"),
            fields="files(id,name)").execute()
        if r["files"]:
            cid = r["files"][0]["id"]
            print(f"  la carpeta ya existe — {cid}")
        elif a.ensayo:
            print(f"  crearía la carpeta «{CARPETA_GIF}»")
            cid = None
        else:
            cid = sv.files().create(
                body={"name": CARPETA_GIF, "parents": [CARPETA],
                      "mimeType": "application/vnd.google-apps.folder"},
                fields="id").execute()["id"]
            print(f"  ✅ carpeta creada — {cid}")
        gifs = listar(sv, cid) if cid else {}
        # La misma renumeración en los GIF: el del cierre se RENOMBRA.
        g_viejo, g_nuevo = (CIERRE_EN_DRIVE.replace(".mp4", ".gif"),
                            CIERRE_NUEVO.replace(".mp4", ".gif"))
        if cid and g_viejo in gifs and g_nuevo not in gifs:
            if a.ensayo:
                print(f"  → renombraría {g_viejo} a {g_nuevo}")
            else:
                sv.files().update(fileId=gifs[g_viejo]["id"],
                                  body={"name": g_nuevo}).execute()
                print(f"  ✅ {g_viejo} renombrado a {g_nuevo}")
                gifs = listar(sv, cid)
        for src in sorted(ENTREGA_GIF.glob("C1 S5 DT n°*.gif")):
            sube(sv, src, cid, gifs, a.ensayo or not cid)

    print("\n✅ listo" if not a.ensayo else "\n(ensayo — no se tocó nada)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

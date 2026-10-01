#!/usr/bin/env python3
"""⛔ 01-10-2026: YA SE CORRIÓ. NO volver a correr — movería todo una semana más.
Antes y después en out/qb/oct/reorden-semanas/ (drive-antes.json · drive-despues.json).
Los 4 KV de Eli no los mueve este token (`appNotAuthorizedToFile`): dos se renombraron
con el conector de Drive y de los otros dos se dejó una copia idéntica en su semana.

QB · OCTUBRE 2026 — reordena los diseños de Drive por la SEMANA actual de la grilla
(01-10-2026, tarde). Eli: «ordena las gráficas de QB nuevamente según semana, ya que hubo
cambios» · «me refiero a los diseños, no edites nada de grilla».

Contenido partió la semana 1 en dos y corrió todo lo demás una semana:

    antes  S1 = 1–9 oct · S2 = 12–17 · S3 = 19–25 · S4 = 26–31
    ahora  S1 = 1–2 oct · S2 = 5–9 · S3 = 12–17 · S4 = 19–25 · S5 = 26–31

Sólo se MUEVE y se RENOMBRA (R-67): el ID y el enlace de cada archivo no cambian. La
grilla no se toca. Deja un registro antes → después en out/qb/oct/reorden-semanas/.

Uso:  python scripts/qb-oct-reordenar-semanas.py [--hacer]     (sin --hacer, sólo muestra)
"""
import json
import os
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import token_google  # noqa: E402
from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REGISTRO = RAIZ / "out/qb/oct/reorden-semanas/registro.json"
CARPETA = "application/vnd.google-apps.folder"

QB = {1: "1jjzSls7cN0j_aHL9te3Wu7yxBWO1n-Ab", 2: "12RkF3pdEOBv51vYYhe1PRVZVB9_hMM6Y",
      3: "1ApkHDRpSPdhOv47dlTvF_K6jS8gpHR9Z", 4: "1dQ1LShqIOKDci1v-0qGEna4K52QUUqhV",
      5: "1YrwyQ_6tbuDIrP4I9IgMh24on5NtstVu"}

HACER = "--hacer" in sys.argv
registro = []


def servicio():
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


svc = servicio()


def hijos(padre):
    r = svc.files().list(q=f"'{padre}' in parents and trashed = false",
                         fields="files(id,name,mimeType,md5Checksum)", supportsAllDrives=True,
                         includeItemsFromAllDrives=True, pageSize=200).execute().get("files", [])
    return sorted(r, key=lambda f: f["name"])


def sub(padre, nombre, crear=False):
    for f in hijos(padre):
        if f["name"] == nombre and f["mimeType"] == CARPETA:
            return f["id"]
    if not crear:
        return None
    if not HACER:
        print(f"· crear carpeta «{nombre}»")
        return f"(nueva:{nombre})"
    return svc.files().create(body={"name": nombre, "parents": [padre], "mimeType": CARPETA},
                              fields="id", supportsAllDrives=True).execute()["id"]


def mover(f, origen, destino, nombre, de, a):
    """Renombra y, si cambia de carpeta, mueve. `de` y `a` son rutas legibles para el registro."""
    registro.append({"id": f["id"], "antes": f"{de}/{f['name']}", "despues": f"{a}/{nombre}",
                     "padre_antes": origen, "padre_despues": destino})
    if HACER:
        kw = {"fileId": f["id"], "body": {"name": nombre}, "supportsAllDrives": True, "fields": "id"}
        if destino != origen:
            kw.update(addParents=destino, removeParents=origen)
        svc.files().update(**kw).execute()
    print(f"{'✓' if HACER else '·'} {de}/{f['name']}  →  {a}/{nombre}")


def copiar(f, destino, nombre, de, a):
    registro.append({"copia_de": f["id"], "antes": f"{de}/{f['name']}", "despues": f"{a}/{nombre}"})
    if HACER:
        nuevo = svc.files().copy(fileId=f["id"], body={"name": nombre, "parents": [destino]},
                                 supportsAllDrives=True, fields="id").execute()
        registro[-1]["id"] = nuevo["id"]
    print(f"{'✓' if HACER else '·'} COPIA {de}/{f['name']}  →  {a}/{nombre}")


def main():
    sts = {n: sub(QB[n], "STS", crear=(n == 5)) for n in QB}
    feed = {n: sub(QB[n], "FEED", crear=(n in (2, 3))) for n in (1, 2, 3)}

    # ── HISTORIAS: de atrás hacia adelante, para no pisar nombres ──────────────────
    for n in (4, 3, 2):                         # S4→S5 · S3→S4 · S2→S3, mismo n° (el orden no cambió)
        for f in hijos(sts[n]):
            if f["mimeType"] == CARPETA or f" S{n} QB OCT 26" not in f["name"]:
                continue
            nombre = f["name"].replace(f" S{n} QB OCT 26", f" S{n + 1} QB OCT 26", 1)
            mover(f, sts[n], sts[n + 1], nombre, f"S{n}/QB/STS", f"S{n + 1}/QB/STS")

    s1 = {f["name"]: f for f in hijos(sts[1])}
    # S2 nueva (5–9 oct): 06 AYCD · 07 cumpleaños · 08 CMR 40 % · 09 Sunset
    mover(s1["ST n°2 S1 QB OCT 26.png"], sts[1], sts[2], "ST n°1 S2 QB OCT 26.png", "S1/QB/STS", "S2/QB/STS")
    for ext in ("mp4", "gif"):
        mover(s1[f"ST n°3 S1 QB OCT 26.{ext}"], sts[1], sts[2], f"ST n°2 S2 QB OCT 26.{ext}",
              "S1/QB/STS", "S2/QB/STS")
    mover(s1["KV_ST CMR.png"], sts[1], sts[2], "ST n°3 S2 QB OCT 26 - KV CMR.png", "S1/QB/STS", "S2/QB/STS")
    # el KV de Sunset sale el 02-10 (S1) y otra vez el 09-10 (S2): un archivo por semana
    copiar(s1["KV_SUNSET QB ST.png"], sts[2], "ST n°4 S2 QB OCT 26 - KV SUNSET.png", "S1/QB/STS", "S2/QB/STS")
    # S1 nueva (1–2 oct): 02 Sunset (12:00) · 02 Banco de Chile (17:00)
    mover(s1["ST n°1 S1 QB OCT 26.png"], sts[1], sts[1], "ST n°2 S1 QB OCT 26.png", "S1/QB/STS", "S1/QB/STS")
    mover(s1["KV_SUNSET QB ST.png"], sts[1], sts[1], "ST n°1 S1 QB OCT 26 - KV SUNSET.png",
          "S1/QB/STS", "S1/QB/STS")

    # ── FEED ───────────────────────────────────────────────────────────────────────
    f1 = {f["name"]: f for f in hijos(feed[1])}
    f2 = {f["name"]: f for f in hijos(feed[2])}
    # 16-10 trago de autor: S2 → S3
    mover(f2["Post n°1 S2 QB OCT 26.png"], feed[2], feed[3], "Post n°1 S3 QB OCT 26.png",
          "S2/QB/FEED", "S3/QB/FEED")
    # carrusel Sunset viejo: lo reemplazó el KV de Eli (01-10) → queda como ANTES junto al KV
    car = f2["C1 S2 SUNSET"]
    for f in hijos(car["id"]):
        mover(f, car["id"], car["id"], "ANTES - " + f["name"], "S2/QB/FEED/C1 S2 SUNSET", "S1/QB/FEED/ANTES - C1 SUNSET")
    mover(car, feed[2], feed[1], "ANTES - C1 SUNSET carrusel (reemplazado por Post n°1 S1)", "S2/QB/FEED", "S1/QB/FEED")
    # carrusel CMR viejo: lo reemplazó el KV de Eli (02-10, «sólo 1G»)
    car = f1["C3 S1 CMR"]
    for f in hijos(car["id"]):
        mover(f, car["id"], car["id"], "ANTES - " + f["name"], "S1/QB/FEED/C3 S1 CMR", "S1/QB/FEED/ANTES - C3 CMR")
    mover(car, feed[1], feed[1], "ANTES - C3 CMR carrusel (reemplazado por Post n°2 S1)", "S1/QB/FEED", "S1/QB/FEED")
    # carruseles de cumpleaños y AYCD: S1 → S2
    for viejo, nuevo, c in (("C1 S1 CUMPLEAÑOS", "C1 S2 CUMPLEAÑOS", "C1"), ("C2 S1 AYCD", "C2 S2 AYCD", "C2")):
        car = f1[viejo]
        for f in hijos(car["id"]):
            mover(f, car["id"], car["id"], f["name"].replace(f"{c} S1 ", f"{c} S2 ", 1),
                  f"S1/QB/FEED/{viejo}", f"S2/QB/FEED/{nuevo}")
        mover(car, feed[1], feed[2], nuevo, "S1/QB/FEED", "S2/QB/FEED")
    # KV de Eli: 01-10 Sunset · 02-10 CMR
    mover(f2["KV_SUNSET QB POST.png"], feed[2], feed[1], "Post n°1 S1 QB OCT 26 - KV SUNSET.png",
          "S2/QB/FEED", "S1/QB/FEED")
    mover(f1["KV_POST 1 CMR.png"], feed[1], feed[1], "Post n°2 S1 QB OCT 26 - KV CMR.png",
          "S1/QB/FEED", "S1/QB/FEED")

    if HACER:
        REGISTRO.parent.mkdir(parents=True, exist_ok=True)
        REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\nregistro → {REGISTRO}")
    else:
        print(f"\n{len(registro)} cambios (simulación). Con --hacer se aplican.")


if __name__ == "__main__":
    main()

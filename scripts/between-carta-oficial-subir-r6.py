#!/usr/bin/env python3
"""BETWEEN · carta oficial R6 (30-09-2026) — carpeta de MUESTRA en Drive: PDF + mockup por opción, md5.

Pedido de Eli: «prepara el Drive para presentar los PDF como muestra y su mockup de cómo se vería la
portada y la contraportada en físico, de manera que se puedan visualizar las tres opciones».

Destino: carpeta de Eli de la carta (la misma de la R5, `sub.PADRE`)
  └ CARTA BETWEEN · R6 30-09 · MUESTRA
      ├ OPCION A · MOCKUP.jpg · OPCION A · CARTA.pdf (17 × 30 cm + 3 mm de sangrado)
      ├ OPCION B …   └ OPCION D …
      └ (cuando estén) BW-CARTA-BETWEEN-OPCION-X-R6.ai desde r6/editable/maestro/
Si un archivo ya existe con el mismo nombre, se REEMPLAZA (mismo id, no duplica).

    python scripts/between-carta-oficial-subir-r6.py
"""
import hashlib
import importlib.util
import pathlib
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
_s = importlib.util.spec_from_file_location("sub", pathlib.Path(__file__).with_name("between-carta-oficial-subir.py"))
sub = importlib.util.module_from_spec(_s)
_s.loader.exec_module(sub)
sub.TIPOS[".jpg"] = "image/jpeg"

R6 = sub.RAIZ / "out/hilton/between/carta-oficial/r6"
NOMBRE = "CARTA BETWEEN · R6 30-09 · MUESTRA"


def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()


def main():
    d = sub.servicio()
    raiz = sub.carpeta(d, NOMBRE, sub.PADRE)
    # Eli 30-09: «necesito más ordenada, que los mockups estén en una subcarpeta»
    sc = {"mock": sub.carpeta(d, "01 · MOCKUPS", raiz), "pdf": sub.carpeta(d, "02 · PDF", raiz)}
    lista = []
    for op in "ABD":
        # mockup en funda: escena de Magnific con hojas en blanco + la carta exacta calzada encima
        # (between-carta-r6-funda.py): portada a la izquierda, contraportada a la derecha
        lista.append(("mock", R6 / "mockup" / f"BW-CARTA-BETWEEN-OPCION-{op}-FUNDA-MAGNIFIC.jpg",
                      f"OPCION {op} · MOCKUP en funda (portada y contraportada).jpg"))
        lista.append(("pdf", R6 / "pdf-sangrado" / f"BW-CARTA-BETWEEN-OPCION-{op}-R6.pdf", f"OPCION {op} · CARTA COMPLETA.pdf"))
        ai = R6 / "editable/maestro" / f"BW-CARTA-BETWEEN-OPCION-{op}.ai"
        if ai.exists():
            sc.setdefault("ai", sub.carpeta(d, "03 · EDITABLES", raiz))
            lista.append(("ai", ai, f"BW-CARTA-BETWEEN-OPCION-{op}-R6.ai"))
    # lo que quedó suelto en la raíz de la primera subida: los PDF se MUEVEN (conservan id y enlace),
    # los mockups de mesa (reemplazados por la funda) van a la papelera
    sueltos = d.files().list(q=f"'{raiz}' in parents and trashed=false and mimeType!='application/vnd.google-apps.folder'",
                             fields="files(id,name)", supportsAllDrives=True, includeItemsFromAllDrives=True).execute()["files"]
    for f in sueltos:
        if f["name"].endswith(".pdf"):
            d.files().update(fileId=f["id"], addParents=sc["pdf"], removeParents=raiz, supportsAllDrives=True).execute()
            print("→ 02 · PDF:", f["name"])
        else:
            d.files().update(fileId=f["id"], body={"trashed": True}, supportsAllDrives=True).execute()
            print("papelera:", f["name"])
    # en MOCKUPS queda sólo lo vigente: la versión anterior en ángulo va a la papelera
    vigentes = {n for k, _, n in lista if k == "mock"}
    for f in d.files().list(q=f"'{sc['mock']}' in parents and trashed=false", fields="files(id,name)",
                            supportsAllDrives=True, includeItemsFromAllDrives=True).execute()["files"]:
        if f["name"] not in vigentes:
            d.files().update(fileId=f["id"], body={"trashed": True}, supportsAllDrives=True).execute()
            print("papelera:", f["name"])
    malos = 0
    ent = R6 / "entrega"                     # copia local idéntica a lo que queda en Drive
    ent.mkdir(exist_ok=True)
    for k, src, nombre in lista:
        tmp = ent / nombre
        tmp.write_bytes(src.read_bytes())
        sub.subir(d, tmp, sc[k])
        fid = sub.buscar(d, nombre, sc[k])
        rem = d.files().get(fileId=fid, fields="md5Checksum", supportsAllDrives=True).execute().get("md5Checksum")
        ok = rem == md5(src)
        malos += not ok
        print(("✓" if ok else "✗ md5 distinto"), nombre)
    print()
    print(f"https://drive.google.com/drive/folders/{raiz}")
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    main()

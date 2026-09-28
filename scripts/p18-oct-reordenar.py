#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — la grilla se reordenó DESPUÉS de la entrega del 28-09.

Instantánea `clients/hilton/grillas/api/p18-oct-20260928b.json` contra la de la mañana:
el contenido de cada celda es idéntico, sólo cambió la fecha.

    Fechas 2027 (carrusel)      09-10 → 06-10   (S2 → S2)
    Arreglos florales (post)    06-10 → 09-10   (S2 → S2)
    Tu próxima celebración (5)  16-10 → 30-10   (S3 → S5)

El portal levanta por NOMBRE, así que se RENOMBRA en Drive (conserva el enlace) y la
celebración se MUEVE de S3/PISO18/FEED a S5/PISO18/FEED. Lo mismo en la carpeta local
`out/piso18/oct/entrega/`. Memoria `insertar-lamina-renumera`.

Uso:  python scripts/p18-oct-reordenar.py [--dry-run]
"""
import argparse
import importlib.util
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("subir", RAIZ / "scripts/p18-oct-subir-drive.py")
subir = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subir)

# (semana vieja, nombre viejo, semana nueva, nombre nuevo)
CAMBIOS = [
    (2, "P18 FEED 06-10 Arreglos florales.png", 2, "P18 FEED 09-10 Arreglos florales.png"),
    (2, "P18 FEED 09-10 Fechas 2027 1.png", 2, "P18 FEED 06-10 Fechas 2027 1.png"),
    (2, "P18 FEED 09-10 Fechas 2027 2.png", 2, "P18 FEED 06-10 Fechas 2027 2.png"),
] + [(3, f"P18 FEED 16-10 Tu proxima celebracion {n}.png",
      5, f"P18 FEED 30-10 Tu proxima celebracion {n}.png") for n in range(1, 6)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    svc = None if a.dry_run else subir.servicio()
    feed = {}

    def carpeta_feed(sem):
        if sem not in feed:
            p18 = subir.carpeta(svc, "PISO18", subir.SEMANAS[sem])
            feed[sem] = subir.carpeta(svc, "FEED", p18)
        return feed[sem]

    for sv, viejo, sn, nuevo in CAMBIOS:
        # local
        src = subir.ENTREGA / f"S{sv}" / "FEED" / viejo
        dst = subir.ENTREGA / f"S{sn}" / "FEED" / nuevo
        if a.dry_run:
            print(f"· S{sv}/{viejo}  →  S{sn}/{nuevo}  (local {'ok' if src.is_file() or dst.is_file() else 'FALTA'})")
            continue
        if src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
        # Drive
        origen = carpeta_feed(sv)
        destino = carpeta_feed(sn)
        q = f"name = '{viejo}' and '{origen}' in parents and trashed = false"
        r = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                             includeItemsFromAllDrives=True).execute().get("files", [])
        if not r:
            q = f"name = '{nuevo}' and '{destino}' in parents and trashed = false"
            ya = svc.files().list(q=q, fields="files(id)", supportsAllDrives=True,
                                  includeItemsFromAllDrives=True).execute().get("files", [])
            print(("= ya estaba " if ya else "x NO ENCONTRADO ") + f"S{sn}/{nuevo}")
            continue
        kw = {}
        if origen != destino:
            kw = {"addParents": destino, "removeParents": origen}
        f = svc.files().update(fileId=r[0]["id"], body={"name": nuevo}, fields="id,name,parents",
                               supportsAllDrives=True, **kw).execute()
        ok = f["name"] == nuevo and destino in f.get("parents", [])
        print(f"{'✓' if ok else '⚠️'} S{sv}/{viejo}  →  S{sn}/{f['name']}  · {f['id']}")


if __name__ == "__main__":
    main()

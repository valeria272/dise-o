#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rinde las piezas de DOUBLETREE al máster con el que entrega la diseñadora.

⭐ `--scale 2.0833`: la mesa es de 1080 px de ancho y Eli ENTREGA a 2250 —
2250/1080 = 2,0833. Las 66 historias ya entregadas de esta cuenta están a
**2250×4000**; rendir a 1080 sería entregar la mitad de resolución.

Los nombres de archivo llevan espacios (así entrega el equipo y así los levanta
el portal), y en Windows eso rompe el shell: por eso se invoca por lista de
argumentos y no por línea de comandos armada a mano.

Uso:
    python scripts/dt-rendir.py                     # todas
    python scripts/dt-rendir.py DT-S-DiaTurismo     # sólo una
    python scripts/dt-rendir.py --guias             # incluye las guías de QA
    python scripts/dt-rendir.py --listar
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "src/DtEntry.tsx"
ESCALA = "2.0833"
# ⭐ El FEED va con OTRA escala, y no es un capricho: el máster 4:5 de esta
# cuenta es **2250×2813** (las tres piezas aprobadas y la plantilla
# `logo-post.png`), y 2813 no es 4:5 exacto — 4:5 de 2250 da 2812,5 y el equipo
# redondeó hacia arriba. Con la escala de historia (2,0833) la mesa de 1080×1350
# sale 2250×**2812** y queda 1 px corta respecto de lo que entrega Eli.
# Con 2,0837 sale 2250×2813 clavado. Verificado rindiendo las dos.
ESCALA_FEED = "2.0837"

# id de composición → nombre del archivo de entrega
NOMBRES = {
    "DT-S-DiaTurismo": "DT ST 27-09 Dia del Turismo.png",
    "DT-S-DiaTurismo-Guia": "GUIAS QA/DT ST 27-09 Dia del Turismo - GUIA.png",
    # STORIES col H · 18-09 · saludo Fiestas Patrias (collage, ronda 2).
    "DT-S-FiestasPatrias": "DT ST 18-09 Felices Fiestas Patrias.png",
    "DT-S-FiestasPatrias-Guia": "GUIAS QA/DT ST 18-09 Felices Fiestas Patrias - GUIA.png",
    # FEED col K · 23-09 · estático Hilton Honors.
    # ⚠️ El nombre lo fija cómo entrega Eli, no nosotros: su post de la S3 subió
    # como «Post n°1 S3 DT.png» (14-09), así que éste es el n°1 de la S4 — es el
    # único post de feed de esa semana. El portal levanta por nombre.
    "DT-F-HiltonHonors": "Post n°1 S4 DT.png",
    "DT-F-HiltonHonors-Guia": "GUIAS QA/Post n°1 S4 DT - GUIA.png",
}


def npx() -> str:
    return "npx.cmd" if sys.platform == "win32" else "npx"


def composiciones() -> list[str]:
    # ⚠️ Windows: Remotion escribe UTF-8 y Python decodifica en cp1252 por
    # defecto, lo que revienta el hilo lector. Se fuerza el encoding.
    r = subprocess.run([npx(), "remotion", "compositions", str(ENTRADA)],
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return re.findall(r"^(DT-[FSP]-[A-Za-z0-9-]+)", r.stdout, re.M)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--salida", default=str(RAIZ / "out/hilton/dt/st-turismo"))
    ap.add_argument("--escala", default=None,
                    help="por defecto 2,0833 en historia y 2,0837 en feed (DT-F-*)")
    ap.add_argument("--guias", action="store_true",
                    help="rinde también las composiciones -Guia (QA, no se entregan)")
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()

    todas = composiciones()
    if a.listar:
        print("\n".join(todas) or "no encontré composiciones")
        return 0

    ids = a.ids or [c for c in todas if a.guias or not c.endswith("-Guia")]
    if not ids:
        return print("No encontré composiciones. ¿Está bien src/DtEntry.tsx?") or 1

    salida = Path(a.salida)
    fallos = []
    for i, cid in enumerate(ids, 1):
        destino = salida / NOMBRES.get(cid, f"{cid}.png")
        destino.parent.mkdir(parents=True, exist_ok=True)
        print(f"[{i}/{len(ids)}] {cid} → {destino.name} ... ", end="", flush=True)
        # La escala la decide el FORMATO de la pieza, no la línea de comandos:
        # el feed 4:5 necesita 2,0837 para dar 2250×2813 (ver ESCALA_FEED).
        escala = a.escala or (ESCALA_FEED if cid.startswith("DT-F-") else ESCALA)
        r = subprocess.run(
            [npx(), "remotion", "still", str(ENTRADA), cid, str(destino),
             f"--scale={escala}"],
            cwd=RAIZ, capture_output=True, text=True,
            encoding="utf-8", errors="replace")
        if r.returncode == 0 and destino.exists():
            try:
                from PIL import Image
                tam = "×".join(map(str, Image.open(destino).size))
            except Exception:                                      # noqa: BLE001
                tam = f"{destino.stat().st_size // 1024} KB"
            print(f"ok  {tam}  ({destino.stat().st_size // 1024} KB)")
        else:
            print("FALLÓ")
            for linea in (r.stderr or r.stdout).strip().splitlines()[-6:]:
                print(f"      {linea}")
            fallos.append(cid)

    print(f"\n{len(ids) - len(fallos)}/{len(ids)} rendidas en {salida}")
    if fallos:
        print("fallaron:", ", ".join(fallos))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

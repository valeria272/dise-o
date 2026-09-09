#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Empaqueta y sube la historia del DÍA DEL TURISMO (DT · STORIES col K · 27-09).

Hace tres cosas, y sólo tres:

  1. Copia el render con el nombre que espera el portal de validaciones
     —`<SIGLA> <TIPO> <DD-MM> <Descripción>.png`, ver
     `docs/PORTAL-VALIDACIONES.html`— y le escribe **150 ppp** en el `pHYs`.
     No reescala nada: la pieza sigue midiendo 2250×4000, sólo se declara la
     densidad que pide el manual para todo lo digital.
  2. Deja la copia `GUIA` (zonas seguras dibujadas) en una subcarpeta aparte.
     **Ésa no se sube ni se le manda al cliente**: es para revisar.
  3. Con `--subir`, sube SÓLO la pieza del cliente a la carpeta `STS` que indicó
     Eli el 09-09 — `1dB-uwVA2Xdhxl0olsc2SMn6KMZ4J_h8E`, dentro de
     `S4 HILTON SEP 2026 › DT`.

⚠️ Idempotente por nombre: `scripts/drive-subir.py` reemplaza el archivo si ya
existe uno igual en la carpeta, así que correrlo dos veces no duplica.

⚠️ El token del estudio tiene scope `drive.file`: puede CREAR en una carpeta
ajena pero no puede LISTARLA. Si Google responde 404 por la carpeta, el archivo
cae en «Mi unidad» y el uploader lo avisa — **hay que mirar su salida, no darla
por buena.** Por eso este script imprime el enlace.

Antes de subir corre el QA (`scripts/dt-qa.py`) y se planta si algo falla.

Uso:
    python scripts/dt-st-turismo-entrega.py            # sólo empaqueta
    python scripts/dt-st-turismo-entrega.py --subir    # empaqueta y sube
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
RENDERS = RAIZ / "out/hilton/dt/st-turismo"
ENTREGA = RAIZ / "out/hilton/dt/entrega-st-s4-turismo"
CARPETA_STS = "1dB-uwVA2Xdhxl0olsc2SMn6KMZ4J_h8E"
PPP = 150

PIEZA = "DT ST 27-09 Dia del Turismo.png"
GUIA = "GUIAS QA/DT ST 27-09 Dia del Turismo - GUIA.png"


def copia_con_ppp(origen: Path, destino: Path) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(origen)
    im.save(destino, dpi=(PPP, PPP))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subir", action="store_true")
    a = ap.parse_args()

    origen = RENDERS / PIEZA
    if not origen.exists():
        print(f"⛔ Falta el render: {origen}")
        print("   Córrelo con: python scripts/dt-rendir.py --guias")
        return 1

    print("QA antes de empaquetar")
    q = subprocess.run([sys.executable, str(RAIZ / "scripts/dt-qa.py")],
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    for linea in q.stdout.strip().splitlines():
        print(f"   {linea}")
    if q.returncode != 0:
        print("⛔ El QA no pasó. No se empaqueta ni se sube.")
        return 1

    destino = ENTREGA / PIEZA
    copia_con_ppp(origen, destino)
    im = Image.open(destino)
    print(f"\n→ {destino.relative_to(RAIZ)}  {im.width}×{im.height}  "
          f"{PPP} ppp  ({destino.stat().st_size // 1024} KB)")

    guia_o = RENDERS / GUIA
    if guia_o.exists():
        guia_d = ENTREGA / "GUIA QA (no se sube)" / guia_o.name
        guia_d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(guia_o, guia_d)
        print(f"→ {guia_d.relative_to(RAIZ)}   ⚠️ NO se sube")

    if not a.subir:
        print("\n(no se subió nada — usa --subir)")
        return 0

    print(f"\nSubiendo a STS ({CARPETA_STS})")
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts/drive-subir.py"), str(destino),
         "--carpeta", CARPETA_STS],
        cwd=RAIZ, capture_output=True, text=True,
        encoding="utf-8", errors="replace")
    for linea in (r.stdout + r.stderr).strip().splitlines():
        print(f"   {linea}")
    if r.returncode != 0:
        print("✗ falló la subida")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

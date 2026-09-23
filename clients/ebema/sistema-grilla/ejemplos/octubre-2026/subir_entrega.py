#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA grilla octubre 2026 — arma la entrega y la sube a Drive.

Renombra los PNG del render a **la nomenclatura de Paulina** y los sube a
`MATERIAL DISEÑO PAULINA / EBEMA / 4-entregado / 2026-10 grilla octubre`.

Nomenclatura (docs/COMO-DISENA-EL-EQUIPO.md §3 — la de ella, medida sobre el Drive):
    <marca>_c_<tema><n>.png     ebema_c_masisa1.png
    `c_` = carrusel · el número final es la lámina · todo en minúscula, sin tildes
Estructura: una carpeta `c_<tema>/` por carrusel, como en `9. SEPTIEMBRE/feed/`.

⚠️ El conector MCP de Drive NO sirve para subir binarios (habría que mandarlos en
base64 dentro de la llamada). Se sube desde el disco con `scripts/drive-subir.py`,
que además reemplaza si el archivo ya existe y no duplica.

Uso:  python subir_entrega.py [--solo masisa] [--sin-subir]
"""
import argparse, os, shutil, subprocess, sys

for _f in (sys.stdout, sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
SUBIR = os.path.join(RAIZ, "scripts", "drive-subir.py")
SALIDA = os.path.join(AQUI, "editables", "salida")
ENTREGA = os.path.join(AQUI, "entrega")

# Carpetas creadas el 23-09-2026 dentro de «2026-10 grilla octubre — carruseles»
# (1Z7YxRwu_elAvb_dFpqSlHKKAFUKFVl0t), que cuelga de EBEMA / 4-entregado.
CARPETAS = {
    "masisa":    "1JebxFFux-yPFE3lcl-V6_RZVbCyWtvF5",
    "etersol":   "1-JvDyXissve0cARwAQToov1vai28Rhqy",
    "cbb":       "1CBzMIxLsQZ6rx35L8D6wxsnb1GpNZqX2",
    "volcanita": "1UMDlEi5odYJ1TiEZvbsoFUNQMmFbyYrv",
    "sanjuan":   "1WK2US9SYo6qdCHj1LofPM72NoFv12zMM",
    "pointfix":  "1esqYpWNTBqxlcd8K3EGYeVqXwP_AZs0U",
}
LAMINAS = {"masisa": 4, "etersol": 5, "cbb": 5, "volcanita": 5,
           "sanjuan": 5, "pointfix": 5}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo")
    ap.add_argument("--sin-subir", action="store_true")
    a = ap.parse_args()

    temas = [a.solo] if a.solo else list(CARPETAS)
    subidos = faltan = 0

    for tema in temas:
        dest = os.path.join(ENTREGA, f"c_{tema}")
        os.makedirs(dest, exist_ok=True)
        print(f"\n── c_{tema} ──")
        for i in range(1, LAMINAS[tema] + 1):
            src = os.path.join(SALIDA, f"{tema}{i}_feed.png")
            if not os.path.exists(src):
                print(f"    ✗ falta el render {tema}{i}_feed.png")
                faltan += 1
                continue
            nombre = f"ebema_c_{tema}{i}.png"
            fin = os.path.join(dest, nombre)
            shutil.copy2(src, fin)
            if a.sin_subir:
                print(f"    · {nombre}")
                continue
            r = subprocess.run(
                [sys.executable, SUBIR, fin, "--carpeta", CARPETAS[tema]],
                capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.returncode == 0:
                print(f"    ✓ {nombre}")
                subidos += 1
            else:
                print(f"    ✗ {nombre} — no subió")
                print("      " + (r.stdout or r.stderr or "").strip()[-300:])
                faltan += 1

    print(f"\n{'='*46}\n{subidos} subidas · {faltan} pendientes")
    print("https://drive.google.com/drive/folders/1Z7YxRwu_elAvb_dFpqSlHKKAFUKFVl0t")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Rinde la grilla de BETWEEN a la resolución con la que entrega la diseñadora.

Versión portable de `between-rendir.sh`, que era de Mac: tenía quemada la ruta
`/Applications/Google Chrome.app`, el venv `/Users/Vale/copylab-venv` y un
sandbox en `~/copylab-work` que existía sólo para esquivar iCloud. En Windows
nada de eso aplica y se rinde directo desde el repo.

⭐ `--scale 2.0833`: la mesa de trabajo del .ai de Eli es de 1080 px de ancho,
pero ella ENTREGA a 2250 — 2250/1080 = 2,0833. Nuestras entregas de la ronda 1
salieron a 1080 y eran la mitad de resolución.

Uso:
    python scripts/between-rendir.py                    # todas
    python scripts/between-rendir.py BW-S-Cumple        # sólo algunas
    python scripts/between-rendir.py --salida out/mi-carpeta
    python scripts/between-rendir.py --listar
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "src/BetweenEntry.tsx"
ESCALA = "2.0833"


def npx():
    """En Windows el ejecutable es npx.cmd; con shell=True da igual, pero así
    se evita depender del shell para citar rutas con espacios."""
    return "npx.cmd" if sys.platform == "win32" else "npx"


def composiciones():
    # ⚠️ Windows: Remotion escribe UTF-8 y Python decodifica en cp1252 por
    # defecto, lo que revienta el hilo lector. Se fuerza el encoding.
    r = subprocess.run([npx(), "remotion", "compositions", str(ENTRADA)],
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return re.findall(r"^(BW-[FSP]-[A-Za-z0-9-]+)", r.stdout, re.M)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", help="ids a rendir; vacío = todas")
    ap.add_argument("--salida", default=str(RAIZ / "out/hilton-between-sept"))
    ap.add_argument("--escala", default=ESCALA)
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()

    todas = composiciones()
    if a.listar:
        print("\n".join(todas) or "no encontré composiciones")
        return

    ids = a.ids or todas
    if not ids:
        sys.exit("No encontré composiciones. ¿Está bien src/BetweenEntry.tsx?")

    salida = Path(a.salida); salida.mkdir(parents=True, exist_ok=True)
    fallos = []
    for i, cid in enumerate(ids, 1):
        destino = salida / f"{cid}.png"
        print(f"[{i}/{len(ids)}] {cid} ... ", end="", flush=True)
        r = subprocess.run(
            [npx(), "remotion", "still", str(ENTRADA), cid, str(destino),
             f"--scale={a.escala}"],
            cwd=RAIZ, capture_output=True, text=True,
            encoding="utf-8", errors="replace")
        if r.returncode == 0 and destino.exists():
            try:
                from PIL import Image
                tam = "x".join(map(str, Image.open(destino).size))
            except Exception:                                  # noqa: BLE001
                tam = f"{destino.stat().st_size // 1024} KB"
            print(f"ok  {tam}")
        else:
            print("FALLÓ")
            for linea in (r.stderr or r.stdout).strip().splitlines()[-4:]:
                print(f"      {linea}")
            fallos.append(cid)

    print(f"\n{len(ids) - len(fallos)}/{len(ids)} rendidas en {salida}")
    if fallos:
        print("fallaron:", ", ".join(fallos))
        sys.exit(1)


if __name__ == "__main__":
    main()

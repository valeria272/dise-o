#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rinde la campaña ARMY de DOUBLETREE (02-10-2026): el KV de post 4:5 en 2 propuestas × 2 líneas.

Máster como entrega Eli: feed 2250×2813 (escala 2,0837).

⚠️ `public/` pesa 4,3 GB y `remotion still` lo copia entero en cada pieza (el primer intento tardó
más de 10 min y se colgó). Acá se arma UN paquete con un public mínimo —fuentes, logo y la foto— y
todas las piezas salen de ese paquete.

    python scripts/dt-army-rendir.py                 # las 4 del KV, a máster
    python scripts/dt-army-rendir.py --borrador      # a 1080, para mirar rápido
    python scripts/dt-army-rendir.py KV-A            # sólo las que calcen
    python scripts/dt-army-rendir.py --sin-paquete   # reusa el paquete (si sólo cambió la foto NO sirve)
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

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "src/DtArmyEntry.tsx"
SALIDA = RAIZ / "out/hilton/dt/army"
TMP = RAIZ / "raw/_army-paquete"
PUBLICO = ["assets/hilton/dt/fonts", "assets/hilton/dt/logo-dt-blanco.png", "assets/hilton/dt/army",
           "assets/hilton/between/fonts/KallimataScript.ttf"]

# id de composición → (nombre de archivo, escala del máster)
PIEZAS = {
    f"DT-Army-KV-{p}-{linea}": (f"DT ARMY KV Post {linea.upper()} - {nombre}.png", "2.0837")
    # ronda 14: la opción 2 es la foto de la clienta con filtro morado; la habitación con globos (ronda 11) y
    # la fachada del Día del Turismo (rondas 12 y 13) se retiraron — sus composiciones siguen registradas
    for p, nombre in (("Ciudad", "Opción 1 Ciudad"), ("Clienta", "Opción 2 Hotel al atardecer"),
                      ("CiudadLogo", "Opción 3 Ciudad logo morado"))
    for linea in ("Preventa",)          # Eli, 02-10: «omite por ahora venta» (las composiciones siguen registradas)
}
# Las adaptaciones de las opciones 1 y 2 (Eli, 02-10: «ten las adaptaciones listas para todas cuando te diga cuál
# quede»): historia a máster 2250 × 4000; el paid va a 1080, sin ampliar (Hilton: paid a 150 ppp como máximo).
PIEZAS.update({
    f"DT-Army-{fid}-{p}-Preventa": (f"adaptaciones/DT ARMY {formato} PREVENTA - {nombre}.png", escala)
    for fid, formato, escala in (("ST", "ST", "2.0833"), ("STPaid", "ST Paid", "1"), ("PostPaid", "Post Paid", "1"))
    for p, nombre in (("Ciudad", "Opción 1 Ciudad"), ("Clienta", "Opción 2 Hotel al atardecer"))
})


def npx() -> str:
    return "npx.cmd" if sys.platform == "win32" else "npx"


def corre(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("filtros", nargs="*")
    ap.add_argument("--borrador", action="store_true")
    ap.add_argument("--sin-paquete", action="store_true")
    a = ap.parse_args()

    pub, paquete = TMP / "public", TMP / "bundle"
    if not a.sin_paquete:
        shutil.rmtree(TMP, ignore_errors=True)
        for r in PUBLICO:
            src, dst = RAIZ / "public" / r, pub / r
            dst.parent.mkdir(parents=True, exist_ok=True)
            (shutil.copytree if src.is_dir() else shutil.copy2)(src, dst)
        r = corre([npx(), "remotion", "bundle", str(ENTRADA), f"--public-dir={pub}", f"--out-dir={paquete}"])
        if r.returncode:
            print((r.stderr or r.stdout)[-1500:])
            return 1
        print("paquete armado")

    fallos = 0
    for cid, (nombre, escala) in PIEZAS.items():
        if a.filtros and not any(f.lower() in cid.lower() for f in a.filtros):
            continue
        destino = (SALIDA / "borrador" / nombre) if a.borrador else (SALIDA / nombre)
        destino.parent.mkdir(parents=True, exist_ok=True)
        r = corre([npx(), "remotion", "still", str(paquete), cid, str(destino), f"--scale={'1' if a.borrador else escala}"])
        ok = r.returncode == 0 and destino.exists()
        print(f"{'ok   ' if ok else 'FALLÓ'} {cid} → {destino.name}", flush=True)
        if not ok:
            fallos += 1
            print("\n".join((r.stderr or r.stdout).strip().splitlines()[-6:]))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())

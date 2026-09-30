#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETWEEN · carta oficial R6 (copia de la R5) — arma el .ai de una opción HOJA POR HOJA.

Pedido de Eli (29-09-2026): «de a uno, que el Illustrator no se vaya a pegar, ve mostrándome
uno por uno». Cada llamada hace UNA hoja (≈20–40 s): abre el .ai de la opción, le agrega o
rehace esa hoja, guarda, exporta la vista previa de esa mesa y cierra sólo lo suyo.

⛔ Este script NO abre Illustrator. Si no está abierto (o está en la pantalla de carga), se
detiene y lo dice: el 29-09 lanzarlo por COM lo dejó pegado en el splash.

Uso:
    python scripts/between-carta-r5-por-hoja.py --estado
    python scripts/between-carta-r5-por-hoja.py A 1        # opción A, hoja 1 (crea el .ai)
    python scripts/between-carta-r5-por-hoja.py A 2        # agrega / rehace la hoja 2
Salida: out/hilton/between/carta-oficial/r6/editable/maestro/
        BW-CARTA-BETWEEN-OPCION-<X>.ai  ·  vista/BW-CARTA-BETWEEN-OPCION-<X>-HOJA-<n>.png
"""
import subprocess
import sys
import time
from pathlib import Path

import pythoncom
import win32com.client

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
BASE = RAIZ / "out/hilton/between/carta-oficial/r6/editable"
JSX = RAIZ / "scripts/between-carta-oficial-ai-r6-hoja.jsx"
OCUPADO = (-2147418111, -2147417846, -2147417851)


def illustrator_abierto():
    """Engancha el Illustrator YA abierto. Nunca lo lanza."""
    r = subprocess.run(["powershell", "-NoProfile", "-Command",
                        "Get-Process Illustrator -ErrorAction SilentlyContinue | "
                        "ForEach-Object { \"$($_.Id) $($_.Responding) $($_.MainWindowTitle)\" }"],
                       capture_output=True, text=True)
    if not r.stdout.strip():
        sys.exit("⛔ Illustrator no está abierto. Ábrelo tú (sin documento o con lo tuyo) y vuelvo a correr.")
    pythoncom.CoInitialize()
    try:
        ai = win32com.client.GetActiveObject("Illustrator.Application")
    except pythoncom.com_error:
        sys.exit("⛔ Illustrator está abriendo todavía (no contesta). Espera a que se vea la pantalla de inicio.")
    for _ in range(20):
        try:
            n = ai.DoJavaScript("app.documents.length")
            return ai, n
        except pythoncom.com_error as e:
            if e.hresult not in OCUPADO:
                raise
            time.sleep(3)
    sys.exit("⛔ Illustrator está ocupado (¿un diálogo abierto?). Ciérralo y vuelvo a correr.")


def main():
    args = sys.argv[1:]
    ai, n = illustrator_abierto()
    if not args or args[0] == "--estado":
        print(f"Illustrator responde · {n} documento(s) abierto(s)")
        return
    opcion, hoja = args[0].upper(), int(args[1])
    (BASE / "maestro").mkdir(parents=True, exist_ok=True)
    (BASE / "maestro/_param.jsxinc").write_text(f'var OPCION = "{opcion}";\nvar HOJA = {hoja};\n', encoding="utf-8")
    t0 = time.time()
    # sólo se reintenta si Illustrator RECHAZA la llamada (el script no llegó a correr);
    # un error del script no se reintenta: duplicaría documentos
    for _ in range(20):
        try:
            res = ai.DoJavaScriptFile(str(JSX))
            break
        except pythoncom.com_error as e:
            if e.hresult not in OCUPADO:
                raise
            time.sleep(3)
    else:
        sys.exit("⛔ Illustrator no aceptó el script (ocupado).")
    print(res)
    print(f"({time.time() - t0:.0f} s)")
    png = BASE / f"maestro/vista/BW-CARTA-BETWEEN-OPCION-{opcion}-HOJA-{hoja}.png"
    if png.exists():
        print("vista:", png)
    if not str(res).startswith("OK"):
        log = BASE / f"maestro/_avance-{opcion}.txt"
        if log.exists():
            print("── avance:\n" + log.read_text(encoding="utf-8")[-1500:])
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""HTML -> PNG con Chrome headless (versión Windows de render.sh).
Rutas ABSOLUTAS estilo Windows en --screenshot: con una relativa Chrome no escribe nada.
Uso: python render.py [patron]"""
import subprocess, sys, shutil
from pathlib import Path
AQUI = Path(__file__).resolve().parent
CHROME = next(c for c in [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"] if Path(c).exists())
patron = sys.argv[1] if len(sys.argv) > 1 else ""
for f in sorted(AQUI.glob("*.html")):
    if patron not in f.name: continue
    if "_mail" in f.name:
        H = next(h for k, h in [("banner", 750), ("atencion", 240), ("ficha", 1501), ("cierre", 551)] if k in f.name)
        W, dest = 1201, "mail"
    else:
        W, H, dest = (4500, 8000, "story") if "_st-" in f.name else (4500, 5625, "feed")
    out = AQUI.parent / dest / (f.stem + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--virtual-time-budget=25000", f"--window-size={W},{H}",
        f"--screenshot={out.as_posix()}", f.as_uri()], capture_output=True)
    print("[ok]" if out.exists() else "[FALLÓ]", out.relative_to(AQUI.parent))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta el vaso To Go con el matting de Magnific, no con grabCut.

⭐ RONDA 15 (05-09-2026) — Eli, sobre la ST de Emergencia:

    «se ve el vaso to go **pegoteado**»

⛔ Y el «pegoteado» es el RECORTE, no el montaje. Mirado al 300 %, el
   `vaso-248.png` que venía usándose desde la ronda 13 tiene el canto mordido:
   le faltan trozos del canto de la tapa arriba a izquierda y derecha, y el
   anillo blanco de la base está cortado en plano con una muesca. Eso es lo que
   deja `grabCut` cuando el objeto y su fondo comparten tono — y el kraft del
   vaso contra la mesa de madera de Between comparten tono casi exacto.

   La ronda 14 le quitó a ese recorte el trozo de mesa que arrastraba
   (`between-recortes-limpiar.py`), que era un defecto distinto y real, pero
   **no podía inventar el canto que grabCut ya se había comido**.

⭐ La salida es usar el matting que ya pagamos: `/v1/ai/beta/image-remove-background`
   de Magnific. Es un modelo de segmentación entrenado, no un algoritmo de
   contraste, y resuelve justamente el caso «objeto y fondo del mismo tono».

⚠️ Esto NO es generar el producto. El vaso sigue siendo la fotografía real del
   cliente (sesión 25-jul-2025, cuadro 248, el vaso vigente con su logotipo
   impreso): lo único que hace Magnific es decidir qué píxel es vaso y cuál es
   mesa. La jerarquía de imagen del manual se respeta — la IA no dibuja el
   producto ni la marca.

Uso:
    python scripts/between-vaso-matte.py
"""
import base64
import json
import mimetypes
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import clave_freepik  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-248.jpg"
DESTINO = RAIZ / "public/assets/hilton/between/recortes/vaso-248-matte.png"
#: el vaso en la toma original de 5.760×3.840, con aire para que el modelo vea
#: el objeto entero (un recorte pegado al borde le corta el canto).
CAJA = (3060, 700, 4560, 2520)
BASE = "https://api.freepik.com"
RUTA = "/v1/ai/beta/image-remove-background"


def pide(ruta, cuerpo=None):
    req = urllib.request.Request(
        BASE + ruta,
        data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
        headers={"x-freepik-api-key": clave_freepik(),
                 "Content-Type": "application/json"},
        method="POST" if cuerpo is not None else "GET")
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:500]}")


def main():
    if not ORIGEN.exists():
        sys.exit(f"falta la toma original: {ORIGEN}")
    im = Image.open(ORIGEN).convert("RGB").crop(CAJA)
    print(f"recorte de la toma original: {im.width}x{im.height}")
    tmp = RAIZ / "out/hilton-between-r15/pasos/vaso-248-crudo.png"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    im.save(tmp)

    b64 = base64.b64encode(tmp.read_bytes()).decode()
    mime = mimetypes.guess_type(tmp.name)[0] or "image/png"
    print("→ Magnific remove-background")
    r = pide(RUTA, {"image": b64, "mime_type": mime})
    d = r.get("data", r)

    #: la beta responde de dos formas según la carga: o el PNG ya resuelto en
    #: `url`/`high_resolution`, o un task_id que hay que consultar. Se cubren las
    #: dos para que el script no dependa del día.
    url = d.get("high_resolution") or d.get("url") or d.get("original")
    if not url and d.get("task_id"):
        for _ in range(60):
            time.sleep(5)
            e = pide(f"{RUTA}/{d['task_id']}").get("data", {})
            if e.get("status") in ("COMPLETED", "SUCCESS"):
                url = (e.get("generated") or [None])[0] or e.get("url")
                break
        else:
            sys.exit("la tarea no terminó")
    if not url:
        sys.exit(f"respuesta inesperada: {json.dumps(r)[:400]}")

    with urllib.request.urlopen(url, context=CTX, timeout=300) as f:
        DESTINO.write_bytes(f.read())
    png = Image.open(DESTINO).convert("RGBA")
    caja = png.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    png = png.crop(caja)
    png.save(DESTINO)

    a = np.asarray(png)
    al = a[..., 3]
    print(f"-> {DESTINO.relative_to(RAIZ)}  {png.size}")
    print(f"   alfa: {100 * (al > 128).mean():.1f} % opaco · "
          f"borde suave (0<α<255): {100 * ((al > 8) & (al < 248)).mean():.2f} %")


if __name__ == "__main__":
    main()

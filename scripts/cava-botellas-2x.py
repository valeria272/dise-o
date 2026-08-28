#!/usr/bin/env python3
"""CAVA — sube los bottle shots a 2× con el upscaler DE PRECISIÓN de Magnific.

POR QUÉ
-------
Los bottle shots del e-commerce traen la botella a ~763 px de alto, y el KV la
necesita a **1459** (52 % de 2813, manual §11). Eso es ampliar ×1,91: con LANCZOS
la etiqueta se ablanda y el producto queda menos nítido que el fondo — que es
justo lo que hace que una pieza se lea como collage.

⚠️ Va el **upscaler de PRECISIÓN**, no el creativo. El creativo *inventa* detalle:
sobre una etiqueta te redibuja las letras y sobre un sello de puntaje te cambia el
número. Precision solo resuelve píxeles. Regla del estudio: creativo para fondos,
precision para cualquier cosa con marca encima
(`docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`).

El alfa NO sobrevive al viaje (la API devuelve JPG/PNG sin transparencia), así que
se rescata el alfa original escalado y se vuelve a pegar. Sin eso, las botellas
salen con un fondo blanco pegado.

Uso:
    python3 scripts/cava-botellas-2x.py [--solo nombre] [--forzar]
"""
import argparse
import base64
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request

import certifi
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOT = os.path.join(RAIZ, "public", "assets", "cava", "bottles")
DEST = os.path.join(BOT, "2x")
CTX = ssl.create_default_context(cafile=certifi.where())
RUTA = "/v1/ai/image-upscaler-precision"
BASE = "https://api.freepik.com"

# Las del KV de Fiestas Patrias. Se amplía solo lo que se usa: cada llamada cuesta.
DEFECTO = ["edicion-limitada-carmenere", "7colores-limited-carmenere",
           "vitis-unica-cabernet", "seleccion-vinedos-gr-cabernet"]


def clave():
    f = os.path.join(os.path.expanduser("~"), ".magnific_key")
    if os.path.isfile(f):
        k = open(f).read().strip()
        if k:
            return k
    env = os.path.join(os.path.dirname(RAIZ), "ASISTENTE PERSONAL", ".env")
    for l in open(env, encoding="utf-8").read().splitlines():
        m = re.match(r"\s*FREEPIK_API_KEY\s*=\s*(.+)", l)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    sys.exit("✗ No encuentro la clave")


K = clave()


def pedir(ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo else None
    req = urllib.request.Request(BASE + ruta, data=datos,
                                 method="POST" if datos else "GET",
                                 headers={"x-freepik-api-key": K,
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
        return json.load(r)


def espera(task_id, limite=300):
    for i in range(limite):
        req = urllib.request.Request(f"{BASE}{RUTA}/{task_id}",
                                     headers={"x-freepik-api-key": K})
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            d = json.load(r)["data"]
        if d.get("status") == "COMPLETED":
            g = d.get("generated") or []
            if g:
                return g[0]
            # La API marca COMPLETED unos instantes ANTES de publicar la URL.
            # Abortar acá hacía fallar 3 de cada 4 escalados con «terminó sin
            # imagen» sobre tareas que en realidad habían salido bien.
            if i % 15 == 0:
                print("     … COMPLETED, esperando la URL")
            time.sleep(2)
            continue
        if d.get("status") in ("FAILED", "ERROR"):
            raise RuntimeError(json.dumps(d)[:200])
        if i % 15 == 0:
            print(f"     … {d.get('status')} ({i}s)")
        time.sleep(2)
    raise RuntimeError("se agotó la espera")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo")
    ap.add_argument("--forzar", action="store_true", help="rehacer si ya existe")
    a = ap.parse_args()
    os.makedirs(DEST, exist_ok=True)
    nombres = [a.solo] if a.solo else DEFECTO

    for n in nombres:
        destino = os.path.join(DEST, n + ".png")
        if os.path.isfile(destino) and not a.forzar:
            print(f"  · {n} — ya estaba, se salta (--forzar para rehacer)")
            continue
        origen = os.path.join(BOT, n + ".png")
        if not os.path.isfile(origen):
            print(f"  ✗ no existe {origen}")
            continue

        orig = Image.open(origen).convert("RGBA")
        alfa = orig.split()[3]
        # se manda sobre BLANCO: el fondo transparente llega como negro y le deja
        # un halo oscuro al vidrio, que después no hay cómo sacar
        plano = Image.new("RGB", orig.size, (255, 255, 255))
        plano.paste(orig.convert("RGB"), (0, 0), alfa)
        buf = io.BytesIO()
        plano.save(buf, "PNG")

        print(f"  → {n} ({orig.width}×{orig.height})…")
        try:
            r = pedir(RUTA, {"image": base64.b64encode(buf.getvalue()).decode()})
            url = espera(r["data"]["task_id"])
            with urllib.request.urlopen(url, context=CTX, timeout=180) as resp:
                grande = Image.open(io.BytesIO(resp.read())).convert("RGB")
        except (urllib.error.HTTPError, RuntimeError) as e:
            print(f"     ✗ falló: {e}")
            continue

        # el alfa original, escalado al tamaño nuevo
        af = alfa.resize(grande.size, Image.LANCZOS)
        salida = Image.new("RGBA", grande.size, (0, 0, 0, 0))
        salida.paste(grande, (0, 0), af)
        salida.save(destino)
        bb = af.getbbox()
        print(f"     ✓ {grande.width}×{grande.height} · botella {bb[3]-bb[1]} px de alto"
              f"  → {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

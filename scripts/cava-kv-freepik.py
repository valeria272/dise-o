#!/usr/bin/env python3
"""
CAVA MORANDÉ — genera los fondos del KV de septiembre 2026 (Fiestas Patrias).

El KV del mes es UNO solo y de él salen todos los mailings (ver
clients/cava/CLAUDE.md §1). Acá se generan SOLO los fondos: viñedo otoñal,
barrica de roble y el adorno dieciochero. Las botellas NUNCA se generan —
son bottle shots oficiales y se componen aparte (§2, regla dura).

El brief de septiembre pide cambiar la cinta tricolor de atrás por otro
adorno ornamental dieciochero: van copihues y espigas de trigo.

Uso:
    python3 scripts/cava-kv-freepik.py [--solo NOMBRE] [--reintentos N]
"""
import argparse
import base64
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

import certifi

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "public", "assets", "cava", "kv")
CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com/v1/ai/mystic"

# Lenguaje visual común, tomado del brief KV_FiestasPatrias_Septiembre2026:
# viñedo otoñal dorado, luz de atardecer, nunca frío ni azulado, aire premium.
COMUN = (
    "professional advertising photography, Chilean vineyard in autumn at golden hour, "
    "warm golden bokeh background, soft rim light, premium wine brand aesthetic, "
    "rich warm color grading, deep shadows, no people, no text, no logos, no letters, "
    "no bottles, no glasses, photorealistic, high end commercial photography"
)

ESCENAS = {
    # El barril tiene que verse LIGERAMENTE DESDE ARRIBA, con la tapa elíptica
    # ancha y despejada: es la superficie donde después se apoyan las botellas.
    # Con el barril de frente la tapa casi no se ve y las botellas compuestas
    # encima quedan flotando delante del cuerpo — el error de la v2.
    "kv-fiestas": (
        "an old oak wine barrel standing upright, seen from the front and SLIGHTLY "
        "FROM ABOVE so its round top surface reads as a wide clear ellipse of bare "
        "wood, empty and unobstructed, the barrel fills the lower half of the frame "
        "and is cropped by the bottom edge, dark iron hoops, "
        "a garland of small red berries and dry branches resting around the front rim "
        "of the barrel top, draping over the edge, "
        "behind it a deeply blurred warm autumn vineyard at golden hour, creamy bokeh, "
        "soft top light falling on the barrel top, " + COMUN
    ),
    "kv-primavera": (
        "an old light oak wine barrel standing upright, seen from the front and "
        "SLIGHTLY FROM ABOVE so its round top surface reads as a wide clear ellipse of "
        "bare wood, empty and unobstructed, the barrel fills the lower half of the "
        "frame and is cropped by the bottom edge, "
        "a small garland of green foliage and white blossoms resting ONLY on the LEFT "
        "front rim of the barrel, draping down the left side, "
        "the top surface of the barrel COMPLETELY EMPTY, CLEAR AND UNCOVERED, nothing "
        "on top of it, no foliage covering the wood, "
        "behind it a deeply blurred fresh spring vineyard, bright airy warm light, "
        "no autumn leaves, no red berries, no flags, no patriotic ornaments, " + COMUN
    ),
}


def clave():
    """La key sale del entorno o del archivo del estudio."""
    k = os.environ.get("FREEPIK_API_KEY") or os.environ.get("MAGNIFIC_API_KEY")
    if k:
        return k.strip()
    ruta = os.path.expanduser("~/.magnific_key")
    with open(ruta) as fh:
        return fh.read().strip()


def pedir(prompt, key, aspect="social_post_4_5"):
    cuerpo = json.dumps({
        "prompt": prompt,
        "aspect_ratio": aspect,
        "resolution": "2k",
        "realism": True,
        "creative_detailing": 33,
    }).encode()
    req = urllib.request.Request(
        BASE, data=cuerpo,
        headers={"Content-Type": "application/json", "x-freepik-api-key": key},
    )
    with urllib.request.urlopen(req, context=CTX, timeout=90) as r:
        return json.load(r)["data"]["task_id"]


def esperar(task_id, key, limite=300):
    req = urllib.request.Request(
        f"{BASE}/{task_id}", headers={"x-freepik-api-key": key}
    )
    t0 = time.time()
    while time.time() - t0 < limite:
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            d = json.load(r)["data"]
        if d["status"] == "COMPLETED":
            return d["generated"]
        if d["status"] == "FAILED":
            raise RuntimeError(f"la generación falló: {d}")
        time.sleep(6)
    raise TimeoutError(f"{task_id} no terminó en {limite}s")


def bajar(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
        datos = r.read()
    with open(destino, "wb") as fh:
        fh.write(datos)
    return len(datos)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="genera solo esta escena")
    ap.add_argument("--reintentos", type=int, default=2)
    args = ap.parse_args()

    os.makedirs(SALIDA, exist_ok=True)
    key = clave()
    escenas = {args.solo: ESCENAS[args.solo]} if args.solo else ESCENAS

    for nombre, prompt in escenas.items():
        for intento in range(1, args.reintentos + 1):
            try:
                print(f"[{nombre}] generando (intento {intento})…", flush=True)
                tid = pedir(prompt, key)
                urls = esperar(tid, key)
                for i, u in enumerate(urls, 1):
                    destino = os.path.join(SALIDA, f"{nombre}-{i:02d}.png")
                    n = bajar(u, destino)
                    print(f"  ✓ {os.path.basename(destino)}  ({n/1e6:.1f} MB)")
                break
            except Exception as e:
                print(f"  ✗ {type(e).__name__}: {e}")
                if intento == args.reintentos:
                    print(f"  [{nombre}] se agotaron los intentos")
                time.sleep(4)


if __name__ == "__main__":
    main()

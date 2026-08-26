"""Casablanca C1 (ronda 2) — genera EL ambiente base único de las 4 tarjetas.

Regla nº1 del brief: «UN MISMO AMBIENTE EN LAS 4 TARJETAS. Entre una y otra
cambia solo la tabla del piso.» Por eso acá se genera UNA sola escena, con el
piso deliberadamente VACÍO en primer plano: la madera de cada producto se
compone después con la foto real del cliente
(`scripts/casablanca-pisos-compositor.py`), no la inventa la IA.

Uso:  FREEPIK_API_KEY=... python3 scripts/casablanca-ambiente-base.py
"""
import json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

DEST = pathlib.Path(str(_RAIZ / "public/assets/casablanca"))
KEY = os.environ.get("FREEPIK_API_KEY", "")
if not KEY:
    sys.exit("Falta FREEPIK_API_KEY")
H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}

# Referencia de encuadre del brief: «interior luminoso, piso protagonista,
# ladrillo a la vista y vigas de madera» (foto de Jenny del 20 de agosto).
PROMPT = (
    "Wide interior photograph of a bright, airy contemporary living-dining room, "
    "shot from standing eye height looking slightly down, so the wooden floor "
    "fills the entire lower half of the frame in strong perspective and is the "
    "clear protagonist. THE FOREGROUND FLOOR IS COMPLETELY EMPTY AND "
    "UNOBSTRUCTED: no furniture, no rug, no objects and no shadows of objects in "
    "the front half of the room, just clean bare floor running away from the "
    "camera. Far in the background, against the back wall: an exposed red brick "
    "wall on the left, a light wooden dining table with two chairs, and a single "
    "potted plant in a woven basket. Warm wooden ceiling beams above. A tall "
    "window on the right letting in soft natural daylight. Plain pale plaster "
    "wall across the upper half of the frame, clean and free of decoration, "
    "leaving generous empty space. Neutral warm palette, beige and cream, "
    "natural daylight, calm and editorial. Everything sharp, deep depth of "
    "field. Architectural Digest interior photography, photorealistic. "
    "No people, no text, no logos, no watermark."
)


def http(url, method="GET", body=None, timeout=180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=H, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw.decode(errors="ignore")


def dig(obj):
    if isinstance(obj, str):
        return obj if obj.startswith("http") else None
    if isinstance(obj, dict):
        for v in obj.values():
            f = dig(v)
            if f:
                return f
    if isinstance(obj, list):
        for v in obj:
            f = dig(v)
            if f:
                return f
    return None


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    base = "https://api.freepik.com/v1/ai/mystic"
    # 4:5 para el feed nuevo; el story se recorta desde el mismo master.
    st, data = http(base, "POST", {
        "prompt": PROMPT, "aspect_ratio": "traditional_3_4", "resolution": "2k",
        "realism": True, "engine": "automatic",
    })
    print(f"mystic -> HTTP {st}")
    if st not in (200, 201):
        sys.exit(json.dumps(data)[:500])
    task = data.get("data", {}).get("task_id")
    for _ in range(90):
        s2, d2 = http(f"{base}/{task}")
        status = (d2.get("data") or {}).get("status")
        if status in ("COMPLETED", "SUCCESS"):
            url = dig(d2)
            with urllib.request.urlopen(url, timeout=180, context=SSL_CTX) as r:
                out = DEST / "amb_base_vacio.jpg"
                out.write_bytes(r.read())
            print(f"guardado {out} ({out.stat().st_size // 1024} KB)")
            return
        if status == "FAILED":
            sys.exit(json.dumps(d2)[:400])
        time.sleep(5)
    sys.exit("timeout")


if __name__ == "__main__":
    main()

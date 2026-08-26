"""Revex R1 (ronda 2) — fondo nuevo para la pieza del concurso.

La ronda 1 usó un render oscuro y moody, que ya estaba anotado como error en el
manual y que Paulina volvió a marcar: «la imagen de fondo debe ser de showroom
con muestras de producto, elegante, sofisticado, iluminacion clara y ambiente
minimalista».

Genera el fondo en 4:5 (feed) y 9:16 (story), con una zona limpia al centro
donde después cae el bloque de texto.

Uso:  FREEPIK_API_KEY=... python3 scripts/revex-fondo-concurso.py
"""
import json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

DEST = pathlib.Path(str(_RAIZ / "public/assets/revex/sep"))
KEY = os.environ.get("FREEPIK_API_KEY", "")
if not KEY:
    sys.exit("Falta FREEPIK_API_KEY")
H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}

PROMPT = (
    "Interior photograph of an elegant, sophisticated and minimalist flooring and "
    "wall-covering showroom. Bright clean daylight, pale walls, polished neutral "
    "floor. Along the walls, tidy vertical display panels and racks of flooring "
    "and stone samples in warm wood and neutral stone tones, plus a few large "
    "format porcelain slabs standing on a rack, all neatly aligned. A soft area "
    "rug on the floor in the middle distance. Uncluttered, calm, upmarket retail "
    "design, generous empty space in the centre of the frame. Warm neutral "
    "palette, beige, greige and light wood. Everything sharp, deep depth of "
    "field, no blur. Architectural interior photography, photorealistic. "
    "No people, no text, no signage, no logos, no watermark."
)

FORMATOS = [("concurso_feed", "traditional_3_4"), ("concurso_story", "social_story_9_16")]


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


def dig(o):
    if isinstance(o, str):
        return o if o.startswith("http") else None
    if isinstance(o, dict):
        for v in o.values():
            f = dig(v)
            if f:
                return f
    if isinstance(o, list):
        for v in o:
            f = dig(v)
            if f:
                return f
    return None


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    base = "https://api.freepik.com/v1/ai/mystic"
    for nombre, aspect in FORMATOS:
        st, data = http(base, "POST", {
            "prompt": PROMPT, "aspect_ratio": aspect, "resolution": "2k",
            "realism": True, "engine": "automatic",
        })
        print(f"[{nombre}] mystic -> HTTP {st}")
        if st not in (200, 201):
            print(json.dumps(data)[:400])
            continue
        task = data.get("data", {}).get("task_id")
        for _ in range(90):
            s2, d2 = http(f"{base}/{task}")
            status = (d2.get("data") or {}).get("status")
            if status in ("COMPLETED", "SUCCESS"):
                url = dig(d2)
                out = DEST / f"{nombre}.png"
                with urllib.request.urlopen(url, timeout=180, context=SSL_CTX) as r:
                    out.write_bytes(r.read())
                print(f"  guardado {out.name} ({out.stat().st_size // 1024} KB)")
                break
            if status == "FAILED":
                print("  falló:", json.dumps(d2)[:300])
                break
            time.sleep(5)


if __name__ == "__main__":
    main()

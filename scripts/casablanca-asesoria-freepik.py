"""C2B — escena de asesoría: cliente conversando con asesor en tienda de pisos.

Pedido de Valeria (24-08): reemplazar la foto del equipo posando por una escena
genérica de tienda de porcelanatos/pisos, con una persona conversando con alguien.
Genera 2 variantes (feed cuadrada y story vertical) con zona limpia arriba para
la tarjeta del logo y abajo para el titular.

Uso: ~/copylab-venv/bin/python3 scripts/casablanca-asesoria-freepik.py
"""
import base64, json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

import certifi

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


SSL_CTX = ssl.create_default_context(cafile=certifi.where())
DEST = pathlib.Path(__file__).parent.parent / "public/assets/casablanca"

KEY = os.environ.get("FREEPIK_API_KEY", "")
if not KEY:
    for line in pathlib.Path(
        str(_env_compartido())
    ).read_text().splitlines():
        if line.startswith("FREEPIK_API_KEY="):
            KEY = line.split("=", 1)[1].strip()
            break
if not KEY:
    sys.exit("Falta FREEPIK_API_KEY")

H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}

PROMPT = (
    "Photorealistic interior photograph inside a bright, elegant flooring and "
    "porcelain tile showroom. In the middle distance, slightly right of center, a "
    "store advisor and a customer stand together in relaxed conversation: the "
    "advisor, seen mostly in profile, gestures toward a large upright display "
    "panel of flooring samples while the customer, seen from behind at three "
    "quarters, listens attentively. Natural candid moment, faces partially "
    "turned away, not posing, not looking at camera. Around them, tall display "
    "racks with large-format porcelain tile and wood flooring samples in warm "
    "neutral tones, clean white walls, warm neutral lighting, polished light "
    "floor. Wide shot with generous clean space in the upper third of the frame "
    "and a clean floor area in the lower third. Editorial retail photography, "
    "soft daylight, realistic. No text, no logos, no watermark."
)


def http(url, method="GET", body=None):
    req = urllib.request.Request(
        url, method=method,
        data=json.dumps(body).encode() if body else None, headers=H,
    )
    try:
        with urllib.request.urlopen(req, timeout=300, context=SSL_CTX) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def poll(base, task_id, label):
    for _ in range(90):
        time.sleep(6)
        st, data = http(f"{base}/{task_id}")
        d = data.get("data", {})
        status = d.get("status")
        if status in ("COMPLETED", "SUCCESS"):
            gen = d.get("generated") or []
            return gen[0] if gen else None
        if status in ("FAILED", "ERROR"):
            print(f"  [{label}] FALLÓ: {json.dumps(data)[:300]}")
            return None
    print(f"  [{label}] timeout")
    return None


def text2image(prompt, aspect, label):
    base = "https://api.freepik.com/v1/ai/mystic"
    st, data = http(base, "POST", {
        "prompt": prompt, "aspect_ratio": aspect, "resolution": "2k",
        "realism": True, "engine": "automatic",
    })
    print(f"  [{label}] mystic -> HTTP {st}")
    if st not in (200, 201):
        print(f"  {json.dumps(data)[:400]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), label)


def save(result, path):
    if not result:
        return False
    if str(result).startswith("http"):
        with urllib.request.urlopen(result, timeout=180, context=SSL_CTX) as r:
            path.write_bytes(r.read())
    else:
        path.write_bytes(base64.b64decode(result))
    print(f"    guardado {path.name} ({path.stat().st_size // 1024} KB)")
    return True


def main():
    for aspect, name in [
        ("square_1_1", "asesoria_tienda_feed"),
        ("social_story_9_16", "asesoria_tienda_story"),
    ]:
        print(f"— {name} ({aspect})")
        save(text2image(PROMPT, aspect, name), DEST / f"{name}.jpg")


if __name__ == "__main__":
    main()

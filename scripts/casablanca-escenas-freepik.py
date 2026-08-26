"""Casablanca C1 — escenas de interior con el piso instalado (sistema gráfico de agosto).

El lenguaje de la marca NO son ambientes ni personas: son bodegones cenitales de
las tablas reales, dispuestas como composición geométrica sobre hormigón greige,
con luz cálida direccional y props matéricos mínimos (piedra, taza cerámica).

Genera UNA composición base y luego 3 ediciones img-to-img cambiando únicamente
la especie/terminación de la madera, para que las 4 tarjetas sean la misma
composición (regla nº1 del brief) y se lean como comparación de looks.

Uso:  FREEPIK_API_KEY=... python3 scripts/casablanca-bodegones-freepik.py
"""
import base64, json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


try:
    import certifi

    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

DEST = pathlib.Path(
    str(_RAIZ / "public/assets/casablanca")
)

KEY = os.environ.get("FREEPIK_API_KEY", "")
if not KEY:
    cfg = pathlib.Path(__file__).parent.parent / ".freepik.json"
    for c in (cfg, pathlib.Path("/private/tmp/claude-502/-Users-Vale-Desktop-COPYLAB-PROJECTS-EDITOR-VIDEOS/569aaaf7-0ae6-4d58-a492-2566e22bfa29/scratchpad/cfg.json")):
        if c.exists():
            KEY = json.loads(c.read_text()).get("key", "")
            break
if not KEY:
    sys.exit("Falta FREEPIK_API_KEY")

H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}

BASE_PROMPT = (
    "Interior photograph of a warm sophisticated contemporary living room, shot "
    "from standing eye height looking down at about 35 degrees, so the installed "
    "wood floor fills the entire lower half of the frame in perspective and is "
    "the clear protagonist. Wide oak planks laid lengthwise running away from the "
    "camera, their grain and joints clearly visible and perfectly sharp. Behind "
    "the floor, tasteful furniture in neutral tones: a pale boucle sofa, a light "
    "oak sideboard, a marble coffee table and a soft beige wool rug. Warm ambient "
    "light, rich medium-dark warm tonality, cosy and editorial rather than bright "
    "and airy. Everything in sharp focus, deep depth of field, no blur anywhere. "
    "Architectural digest interior photography, photorealistic. No people, "
    "no text, no logos, no watermark."
)

EDIT_PREFIX = (
    "Keep the room pixel-identical: exactly the same furniture, the same rug, "
    "the same walls, the same light and shadows, the same camera angle and "
    "framing. Do not move anything. Change ONLY the wood species and colour of "
    "the floor planks to: "
)

BASE_NAME = "escena_natural_uv_grande"
VARIANTS = [
    (
        "escena_natural_uv_chico",
        EDIT_PREFIX
        + "the same honey oak colour and finish, but every plank is clearly "
        "narrower and shorter, so the fan is made of many more, smaller pieces "
        "with more visible seams.",
    ),
    (
        "escena_aserrado",
        EDIT_PREFIX
        + "rustic sawn-cut oak, visibly rougher than before: pronounced parallel "
        "saw marks across every surface, deep open grain, several dark knots, and "
        "a dry matte finish with no sheen.",
    ),
    (
        "escena_cumaru",
        EDIT_PREFIX
        + "cumaru tropical hardwood: a rich reddish-brown chocolate tone, clearly "
        "much warmer, darker and redder than oak, with tight straight grain and a "
        "satin sheen. The colour change must be obvious.",
    ),
]


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


def dig(obj, want_url=True):
    if isinstance(obj, str):
        if want_url and obj.startswith("http"):
            return obj
        if not want_url and len(obj) > 5000 and not obj.startswith("http"):
            return obj
        return None
    if isinstance(obj, dict):
        for v in obj.values():
            f = dig(v, want_url)
            if f:
                return f
    if isinstance(obj, list):
        for v in obj:
            f = dig(v, want_url)
            if f:
                return f
    return None


def poll(base, task_id, label):
    for _ in range(90):
        st, data = http(f"{base}/{task_id}")
        d = data.get("data", {}) if isinstance(data, dict) else {}
        if d.get("status") in ("COMPLETED", "SUCCESS"):
            return dig(data, True) or dig(data, False)
        if d.get("status") in ("FAILED",):
            print(f"  [{label}] falló: {json.dumps(data)[:300]}")
            return None
        time.sleep(5)
    print(f"  [{label}] timeout")
    return None


def text2image(prompt, label):
    base = "https://api.freepik.com/v1/ai/mystic"
    st, data = http(
        base, "POST",
        {"prompt": prompt, "aspect_ratio": "square_1_1", "resolution": "2k",
         "realism": True, "engine": "automatic"},
    )
    print(f"  [{label}] mystic -> HTTP {st}")
    if st not in (200, 201):
        print(f"  {json.dumps(data)[:400]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), label)


def edit(prompt, ref_b64, label):
    base = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    st, data = http(base, "POST", {"prompt": prompt, "reference_images": [ref_b64]})
    print(f"  [{label}] nano-banana -> HTTP {st}")
    if st not in (200, 201):
        print(f"  {json.dumps(data)[:400]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), label)


def save(result, path):
    if not result:
        return False
    if result.startswith("http"):
        with urllib.request.urlopen(result, timeout=180, context=SSL_CTX) as r:
            path.write_bytes(r.read())
    else:
        path.write_bytes(base64.b64decode(result))
    print(f"    guardado {path.name} ({path.stat().st_size // 1024} KB)")
    return True


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    print("1/4 — escena base (Roble Natural UV 14/3)")
    base_path = DEST / f"{BASE_NAME}.jpg"
    res = text2image(BASE_PROMPT, BASE_NAME)
    if not save(res, base_path):
        sys.exit("No se generó la base")

    ref = base64.b64encode(base_path.read_bytes()).decode()
    for i, (name, prompt) in enumerate(VARIANTS, start=2):
        print(f"\n{i}/4 — {name}")
        r = edit(prompt, ref, name)
        if not save(r, DEST / f"{name}.jpg"):
            print(f"  ⚠️  {name} no salió; reintentar solo esta")

    print(f"\nListo en {DEST}")


if __name__ == "__main__":
    main()

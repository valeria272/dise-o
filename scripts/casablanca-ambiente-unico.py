"""Casablanca septiembre — UN ambiente, cuatro pisos (brief de Serena).

Lineamiento nº1 del brief, textual: *"UN MISMO AMBIENTE EN LAS 4 TARJETAS. Entre
una y otra cambia solo la tabla del piso. Así el carrusel se lee como una
comparación de looks y no como cuatro avisos sueltos. Es la regla más importante
de la pieza."*

Por eso: se genera **una** fotografía base por formato y las otras tres tarjetas
salen de ella con `structure_reference` de Mystic — misma sala, misma cámara,
misma luz, cambia sólo la madera del piso. No es lo mismo que generar cuatro
ambientes distintos (eso fue el intento anterior y contradice el brief).

Lo demás sale también del brief:
  · nº2 plano amplio, el piso ocupa al menos la mitad del cuadro.
  · nº3 ambiente habitado pero despejado: dos o tres elementos, no un render vacío.
        La referencia de Jenny (20 de agosto) tiene ladrillo a la vista y vigas.
  · nº4 luz natural, muros claros, misma temperatura de color en las cuatro.
  · nº5 el texto nunca va sobre la madera → el tercio superior tiene que ser
        MURO LIMPIO, sin muebles ni objetos, para que ahí caiga el bloque de texto.

Uso:
    python3 scripts/casablanca-ambiente-unico.py            # base + 3 variantes, ambos formatos
    python3 scripts/casablanca-ambiente-unico.py --fmt feed
"""
import base64
import json
import os
import pathlib
import ssl
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, env_compartido as _env_compartido

try:
    import certifi

    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

DEST = pathlib.Path(str(_RAIZ / "public/assets/casablanca/sep"))
PRODUCTOS = pathlib.Path(str(_RAIZ / "raw/casablanca/productos"))


def _key():
    k = os.environ.get("FREEPIK_API_KEY", "")
    if k:
        return k
    env = _env_compartido()
    if env and pathlib.Path(env).exists():
        for line in pathlib.Path(env).read_text(errors="ignore").splitlines():
            if line.startswith("FREEPIK_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("Falta FREEPIK_API_KEY")


H = {"x-freepik-api-key": _key(), "Content-Type": "application/json"}

# ── El ambiente. Uno solo, y con el muro de arriba despejado a propósito.
SALA = (
    "Wide interior photograph of a serene, luminous contemporary dining area in a "
    "high-end Chilean home. Composition: the upper third of the frame is a clean, "
    "empty pale plaster wall with warm wooden ceiling beams above it — no "
    "furniture, no artwork, no objects in that upper band. In the middle distance, "
    "just three elements and nothing more: a light oak dining table with four "
    "upholstered linen chairs, one large potted plant in a woven basket, and a "
    "single exposed brick accent wall on the far side. The lower half of the frame "
    "is the engineered wood floor, completely clear of furniture and rugs, running "
    "toward the camera."
)

CAMARA = (
    "Shot from standing eye height with a 35 mm lens tilted down about 30 degrees, "
    "so the wood floor fills the entire lower half of the picture and is the "
    "protagonist. One-point perspective, the planks running lengthwise away from "
    "the camera. Abundant natural daylight from a window out of frame on the left, "
    "soft warm shadows, neutral white balance, pale walls. Deep depth of field, "
    "everything tack sharp. Architectural digest editorial interior photography, "
    "photorealistic, calm and uncluttered."
)

PROHIBIDO = (
    "The floor must read as a real photograph of a real installed floor, never as a "
    "digital texture pasted on a surface. No herringbone, no chevron, no parquet, "
    "no short strips, no tiles. No repeating or cloned grain, no harsh colour jumps "
    "between boards, no orange or yellow cast, no plastic gloss, no warped "
    "perspective. No people, no text, no letters, no logos, no watermark. Nothing "
    "placed on the empty upper wall."
)

BASE_SKU = "natural_uv_grande"

MADERAS = {
    "natural_uv_grande": (
        "Extra-wide engineered oak planks, 19 cm across and nearly 1.9 metres long, "
        "so a single board runs most of the depth of the room and end joints are "
        "rare and widely staggered. Light-to-medium natural oak with a soft matte "
        "UV finish: calm long straight grain, a few small tight knots, warm "
        "beige-honey tone that stays muted and never turns orange."
    ),
    "natural_uv_chico": (
        "Engineered oak planks in a contained format, 16.7 cm across and only 1.2 "
        "metres long: because the boards are short, staggered butt joints appear "
        "regularly across the floor in a calm brick pattern, clearly more end "
        "joints than a long-plank floor. Golden honey oak with a satin UV finish, "
        "open grain with visible cathedral figure and occasional small dark knots."
    ),
    "aserrado": (
        "Extra-wide engineered oak planks, 19 cm across and nearly 1.9 metres long. "
        "Pale rustic sawn-cut oak, light sandy blond, NOT brown and NOT dark: every "
        "board carries fine short pale saw marks running across the grain, a "
        "texture of tiny light scratches that is unmistakable in the foreground, "
        "plus several large dark natural knots with filled cracks. Deep open grain, "
        "dry matte finish with no sheen at all."
    ),
    "cumaru": (
        "Narrow and very long hardwood planks: only 12 cm across but 2.13 metres "
        "long, so ten to twelve slender parallel boards are visible across the "
        "width of the frame — the floor reads as many fine long lines running away "
        "from the camera, clearly different from a wide-plank floor. Cumaru "
        "tropical hardwood: rich reddish-brown chocolate tone, clearly warmer, "
        "deeper and redder than oak, tight straight fine grain, satin sheen."
    ),
}

FMT = {"feed": "square_1_1", "story": "social_story_9_16"}


def http(url, method="GET", body=None, timeout=300):
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


def dig(obj, url=True):
    if isinstance(obj, str):
        if url and obj.startswith("http"):
            return obj
        if not url and len(obj) > 5000 and not obj.startswith("http"):
            return obj
        return None
    if isinstance(obj, dict):
        for v in obj.values():
            f = dig(v, url)
            if f:
                return f
    if isinstance(obj, list):
        for v in obj:
            f = dig(v, url)
            if f:
                return f
    return None


def poll(base, task_id, label):
    for _ in range(120):
        st, data = http(f"{base}/{task_id}")
        d = data.get("data", {}) if isinstance(data, dict) else {}
        if d.get("status") in ("COMPLETED", "SUCCESS"):
            return dig(data, True) or dig(data, False)
        if d.get("status") == "FAILED":
            print(f"  [{label}] falló: {json.dumps(data)[:300]}")
            return None
        time.sleep(5)
    print(f"  [{label}] timeout")
    return None


def mystic(prompt, aspect, label, structure=None, fuerza=80):
    base = "https://api.freepik.com/v1/ai/mystic"
    cuerpo = {
        "prompt": prompt,
        "aspect_ratio": aspect,
        "resolution": "2k",
        "realism": True,
        "engine": "automatic",
        "creative_detailing": 20,
    }
    if structure:
        cuerpo["structure_reference"] = structure
        cuerpo["structure_strength"] = fuerza
    st, data = http(base, "POST", cuerpo)
    print(f"  [{label}] mystic {aspect}{' + estructura' if structure else ''} -> HTTP {st}")
    if st not in (200, 201):
        print(f"  {json.dumps(data)[:500]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), label)


def guardar(res, path):
    if not res:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    if res.startswith("http"):
        with urllib.request.urlopen(res, timeout=300, context=SSL_CTX) as r:
            path.write_bytes(r.read())
    else:
        path.write_bytes(base64.b64decode(res))
    print(f"    ✓ {path.name} ({path.stat().st_size // 1024} KB)")
    return True


def prompt_de(sku):
    return f"{SALA} The floor: {MADERAS[sku]} {CAMARA} {PROHIBIDO}"


def main():
    fmts = ["feed", "story"]
    for a in sys.argv[1:]:
        if a.startswith("--fmt"):
            fmts = [a.split("=", 1)[1]] if "=" in a else fmts

    for fmt in fmts:
        print(f"\n═══ {fmt.upper()} ═══")
        base_path = DEST / f"amb_{BASE_SKU}_{fmt}.jpg"
        if not base_path.exists():
            print(f"▸ base ({BASE_SKU})")
            if not guardar(mystic(prompt_de(BASE_SKU), FMT[fmt], f"base_{fmt}"), base_path):
                print("  no salió la base; se salta el formato")
                continue
        else:
            print(f"▸ base ya existe: {base_path.name}")

        ref = base64.b64encode(base_path.read_bytes()).decode()
        for sku in MADERAS:
            if sku == BASE_SKU:
                continue
            print(f"▸ {sku}")
            r = mystic(prompt_de(sku), FMT[fmt], f"{sku}_{fmt}", structure=ref)
            guardar(r, DEST / f"amb_{sku}_{fmt}.jpg")

    print(f"\nListo en {DEST}")


if __name__ == "__main__":
    main()

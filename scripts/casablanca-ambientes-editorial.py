"""Casablanca — ambientes editoriales, uno por SKU (replanteo 25-08-2026).

Reemplaza a `casablanca-ambiente-base.py` + `casablanca-pisos-compositor.py`.

**Por qué se rehace.** El pipeline anterior generaba UN ambiente vacío y le pegaba
encima la textura del piso en perspectiva. El resultado se leía como textura digital
aplicada: tablas cortas, juntas repetidas, veta clonada. Feedback de Valeria
(25-08): *"El piso tiene que parecer FOTOGRAFÍA DE ARQUITECTURA REAL, no un render
evidente ni una textura superpuesta"*.

**Cómo se hace ahora.** Cada SKU se genera como una fotografía de interiorismo
completa, con:
  1. **La escala física de la tabla escrita en el prompt** — 190 × 1900 mm es una
     tabla de casi dos metros, y tiene que verse así: pocas juntas de tope, tablas
     que cruzan el encuadre. Cumaru es angosta (120) y de LARGO VARIABLE y corto.
  2. **Un ambiente distinto por producto** — living, comedor, dormitorio, estar.
     Nada de repetir la misma sala con otro color (regla vieja del brief, muerta
     tras el replanteo: el carrusel ya no compara looks en una misma pieza).
  3. **La madera real como referencia** — la foto oficial del producto va como
     `reference_images` en el pase de Nano Banana, así el tono no lo inventa el
     modelo.

Uso:
    FREEPIK_API_KEY=... python3 scripts/casablanca-ambientes-editorial.py [sku...] [--fmt feed|story|ambos]

Sin argumentos genera los 4 SKU en feed (4:5).
"""
import base64, json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, env_compartido as _env_compartido

try:
    import certifi

    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

DEST = pathlib.Path(str(_RAIZ / "public/assets/casablanca/editorial"))
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

# ── La cámara y la luz son las mismas en las 4: es lo que hace que el feed se lea
#    como una sola campaña aunque los ambientes cambien.
CAMARA = (
    "Editorial interior photograph for an architecture magazine. Full-frame camera "
    "at standing eye height, 35 mm lens, tilted down about 30 degrees so the wood "
    "floor occupies the lower 55 percent of the frame and is unmistakably the "
    "protagonist of the picture. One-point perspective: the planks run lengthwise "
    "away from the camera. Deep depth of field, everything tack sharp from the "
    "floor in the foreground to the far wall. Large window out of frame casting "
    "soft directional daylight across the floor, gentle natural shadows, no "
    "artificial flash. Restrained editorial colour grading, neutral white balance."
)

# ── Lo que arruinó la ronda anterior, dicho explícitamente.
PROHIBIDO = (
    "The floor must read as real photography of a real installed floor, never as a "
    "digital texture pasted onto a surface. Absolutely no herringbone, no chevron, "
    "no parquet, no short strips, no mosaic, no tile. No repeating grain: every "
    "plank has its own distinct figure, and no two boards look cloned. No harsh "
    "colour jumps between neighbouring boards, no orange or yellow cast, no plastic "
    "sheen, no warped perspective, no visible tiling seams. No people, no text, no "
    "letters, no logos, no watermark, no furniture blocking the foreground floor."
)

# ── Un ambiente por SKU. Paleta común: beige, greige, piedra, madera, negro suave.
SKUS = {
    "natural_uv_grande": {
        "producto": "roble-natural-143x190x1900.jpg",
        "medida": "190 mm wide and 1900 mm long",
        "escala": (
            "Extra-wide engineered oak planks, each board 19 cm across and nearly "
            "1.9 metres long, so a single board runs most of the depth of the room "
            "and end joints are rare and widely staggered."
        ),
        "madera": (
            "Light-to-medium natural oak with a soft matte UV finish: calm, long, "
            "straight grain, a few small tight knots, warm beige-honey tone that "
            "stays muted and never turns orange."
        ),
        "ambiente": (
            "A serene contemporary living room in a high-end residence. Low bouclé "
            "sofa in warm off-white, a stone coffee table, a soft greige wool rug "
            "pushed back from the camera, tall sheer curtains, one sculptural floor "
            "lamp and a large olive tree in a matte ceramic pot. Walls in warm "
            "white plaster. European contemporary interior design, calm and airy."
        ),
    },
    "natural_uv_chico": {
        "producto": "roble-natural-uv-formato-chico.jpg",
        "medida": "167 mm wide and 1200 mm long",
        "escala": (
            "Engineered oak planks in a contained format, 16.7 cm across and only "
            "1.2 metres long. Because the boards are short, butt joints appear "
            "regularly across the floor in a calm staggered brick pattern — "
            "clearly more end joints than a long-plank floor, and that rhythm is "
            "visible in the foreground. Never short strips or parquet blocks."
        ),
        "madera": (
            "Natural oak with a satin UV finish in a clearly GOLDEN HONEY tone — "
            "warmer and more saturated than a pale blond oak, closer to amber than "
            "to cream. Open grain with strong visible figure, cathedral patterns, "
            "and occasional small dark knots."
        ),
        "ambiente": (
            "A contemporary dining room in a warm minimalist apartment. Solid oak "
            "dining table with slim sculptural chairs upholstered in stone linen, a "
            "low sideboard in pale wood, a linear pendant light above the table, "
            "and a doorway opening to a bright corridor. Walls in warm greige."
        ),
    },
    "aserrado": {
        "producto": "roble-aserrado.jpg",
        "medida": "190 mm wide and 1900 mm long",
        "escala": (
            "Extra-wide engineered oak planks, 19 cm across and nearly 1.9 metres "
            "long, running the depth of the room with rare, widely staggered end "
            "joints."
        ),
        "madera": (
            "Pale rustic sawn-cut oak, light sandy blond in colour, NOT brown and "
            "NOT dark. Every single board is covered in fine short pale saw marks "
            "running across the grain, clearly visible as a texture of tiny light "
            "scratches — this is the defining feature of the product and must be "
            "unmistakable in the foreground. Several large dark natural knots with "
            "filled cracks scattered across the floor. Deep open grain, dry matte "
            "finish with absolutely no sheen or gloss."
        ),
        "ambiente": (
            "A premium primary bedroom at dusk in a contemporary residence. "
            "Upholstered low bed in stone linen with layered bedding, slatted warm "
            "wood panelling behind the headboard with concealed warm lighting, a "
            "backlit built-in display niche, a lounge chair with an ottoman, and a "
            "soft wool rug set back from the camera. Bright soft morning daylight "
            "pouring in from a large window, so the pale floor reads clearly."
        ),
    },
    "cumaru": {
        "producto": "cumaru.jpg",
        # «2.130 LV» en la ficha del cliente = largo VARIABLE con tope 2130, no
        # tablas de 2,13 m. La clienta lo corrigió el 16-09-2026.
        "medida": "120 mm wide, of VARIABLE and short length (mostly under 1.3 m)",
        "escala": (
            "Narrow and very long hardwood planks: only 12 cm across but 2.13 "
            "metres long. Because the boards are narrow, at least ten to twelve "
            "separate parallel boards are visible across the width of the frame — "
            "the floor reads as many fine long parallel lines running away from the "
            "camera, quite different from a wide-plank floor. Very few end joints. "
            "Never short pieces, never a patchwork of small blocks."
        ),
        "madera": (
            "Cumaru tropical hardwood: rich reddish-brown chocolate tone, clearly "
            "warmer, deeper and redder than oak, tight straight fine grain with "
            "subtle tone variation from board to board, elegant satin sheen."
        ),
        "ambiente": (
            "A sophisticated contemporary living area in a dark elegant palette: "
            "deep charcoal built-in shelving with warm brass detailing, a low sofa "
            "in taupe, a black marble coffee table, heavy stone-coloured drapes and "
            "a tall potted plant. The room is bright, not gloomy: generous daylight "
            "from a tall window falls across the floor so the reddish-brown wood "
            "reads clearly. Stone, taupe and soft-black palette."
        ),
    },
}

FMT = {"feed": "social_post_4_5", "story": "social_story_9_16"}


def http(url, method="GET", body=None, timeout=240):
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
    for _ in range(90):
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


def mystic(prompt, aspect, label):
    base = "https://api.freepik.com/v1/ai/mystic"
    st, data = http(
        base,
        "POST",
        {
            "prompt": prompt,
            "aspect_ratio": aspect,
            "resolution": "2k",
            "realism": True,
            "engine": "automatic",
            "creative_detailing": 25,
        },
    )
    print(f"  [{label}] mystic {aspect} -> HTTP {st}")
    if st not in (200, 201):
        print(f"  {json.dumps(data)[:400]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), label)


def guardar(res, path):
    if not res:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    if res.startswith("http"):
        with urllib.request.urlopen(res, timeout=240, context=SSL_CTX) as r:
            path.write_bytes(r.read())
    else:
        path.write_bytes(base64.b64decode(res))
    print(f"    ✓ {path.name} ({path.stat().st_size // 1024} KB)")
    return True


def prompt_de(sku):
    d = SKUS[sku]
    return (
        f"{d['ambiente']} The floor is an engineered wood floor, boards {d['medida']}. "
        f"{d['escala']} {d['madera']} {CAMARA} {PROHIBIDO}"
    )


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fmt = "feed"
    for a in sys.argv[1:]:
        if a.startswith("--fmt"):
            fmt = a.split("=", 1)[1] if "=" in a else "feed"
    skus = args or list(SKUS)
    formatos = ["feed", "story"] if fmt == "ambos" else [fmt]

    for sku in skus:
        if sku not in SKUS:
            print(f"⚠️  SKU desconocido: {sku}")
            continue
        for f in formatos:
            label = f"{sku}_{f}"
            print(f"\n▸ {label}")
            res = mystic(prompt_de(sku), FMT[f], label)
            guardar(res, DEST / f"amb_{sku}_{f}.jpg")

    print(f"\nListo en {DEST}")


if __name__ == "__main__":
    main()


# ─────────────────────────────────────────────────────────────────────────────
# Pase 2 — CALZAR EL TONO con la foto oficial del producto.
#
# Mystic da la fotografía, pero inventa el color de la madera: el primer render
# de Roble Natural UV salió con ΔE 18 contra la foto real (más gris, menos miel).
# Acá se le pasan las DOS imágenes a Nano Banana —el ambiente y la tabla real— y
# se le pide cambiar únicamente el color/veta del piso. Después se vuelve a medir.
# ─────────────────────────────────────────────────────────────────────────────

MATCH_PROMPT = (
    "The first image is an interior photograph. The second image is a photograph "
    "of the actual wood flooring product. Recolour the wood floor in the first "
    "image so that its colour, tone, warmth and grain character match the second "
    "image exactly, as if that exact product had been installed in that room. "
    "Keep everything else in the first image pixel-identical: same room, same "
    "furniture, same walls, same curtains, same light, same shadows, same camera "
    "angle, same plank widths, same plank lengths, same joint positions. Do not "
    "move, add or remove anything. Photorealistic result, no text, no watermark."
)


def b64(path):
    return base64.b64encode(pathlib.Path(path).read_bytes()).decode()


def match_tono(escena, producto, label):
    base = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    st, data = http(
        base, "POST",
        {"prompt": MATCH_PROMPT, "reference_images": [b64(escena), b64(producto)]},
    )
    print(f"  [{label}] nano-banana match -> HTTP {st}")
    if st not in (200, 201):
        print(f"  {json.dumps(data)[:400]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), label)

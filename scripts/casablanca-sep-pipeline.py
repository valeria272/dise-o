"""Casablanca septiembre — las 4 fotos del carrusel, misma sala, distinta tabla.

Lineamiento nº1 del brief (el que manda): *"UN MISMO AMBIENTE EN LAS 4 TARJETAS.
Entre una y otra cambia solo la tabla del piso."*

Se probaron dos caminos para cumplirlo y quedó documentado cuál gana:

  · **Mystic + structure_reference** (fuerza 80 y 95): mantiene el encuadre pero
    **redibuja la sala** — cambian las sillas, el muro, la ventana. A fuerza 95
    quedó peor que a 80. No sirve para "sólo cambia la tabla".
  · **Nano Banana con dos referencias** (la foto base + la foto oficial del
    producto): deja la sala prácticamente pixel a pixel y cambia sólo el piso.
    Gana. Su límite es que devuelve 1024×1024, así que después se sube de
    resolución.

Pipeline:
  1. base 1:1 en 2K — la genera `casablanca-ambiente-unico.py`.
  2. 3 variantes con Nano Banana (sala idéntica, cambia la madera).
  3. upscaler ×2 para recuperar nitidez (queda ~2048).
  4. `image-expand/flux-pro` lleva cada cuadrada a 9:16 para la story, así la
     story es la MISMA sala con el MISMO piso y no otra generación.

Uso:
    python3 scripts/casablanca-sep-pipeline.py            # todo
    python3 scripts/casablanca-sep-pipeline.py --paso 3   # sólo un paso
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
BASE = "natural_uv_grande"

SKUS = {
    "natural_uv_grande": ("roble-natural-143x190x1900.jpg", None),
    "natural_uv_chico": (
        "roble-natural-uv-formato-chico.jpg",
        "engineered oak planks in a contained format, only 16.7 cm wide and 1.2 metres "
        "long, so staggered butt joints appear regularly across the floor in a calm "
        "brick pattern — clearly more end joints than a long-plank floor; golden honey "
        "oak with a satin UV finish and visible cathedral grain",
    ),
    "aserrado": (
        "roble-aserrado.jpg",
        "extra-wide pale rustic sawn-cut oak planks, 19 cm wide and 1.9 metres long, "
        "light sandy blond and never brown: every board carries fine short pale saw "
        "marks running across the grain, plus several large dark natural knots with "
        "filled cracks; deep open grain, dry matte finish with no sheen",
    ),
    "cumaru": (
        "cumaru.jpg",
        "narrow and very long cumaru tropical hardwood planks, only 12 cm wide and "
        "2.13 metres long, so ten to twelve slender parallel boards are visible across "
        "the width of the frame; rich reddish-brown chocolate tone, tight straight fine "
        "grain, satin sheen",
    ),
}

IDENTICO = (
    "Everything else must stay pixel-identical: the same room, the same table and "
    "chairs in the same positions, the same plants, the same brick wall, the same "
    "ceiling beams, the same window and curtain, the same daylight and shadows, the "
    "same camera angle and framing. Do not move, add or remove anything. Keep the "
    "upper wall empty. Photorealistic, no text, no watermark."
)


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


def dig(o, url=True):
    if isinstance(o, str):
        if url and o.startswith("http"):
            return o
        if not url and len(o) > 5000 and not o.startswith("http"):
            return o
        return None
    if isinstance(o, dict):
        for v in o.values():
            f = dig(v, url)
            if f:
                return f
    if isinstance(o, list):
        for v in o:
            f = dig(v, url)
            if f:
                return f
    return None


def poll(base, tid, label):
    for _ in range(120):
        st, d = http(f"{base}/{tid}")
        e = d.get("data", {}) if isinstance(d, dict) else {}
        if e.get("status") in ("COMPLETED", "SUCCESS"):
            return dig(d, True) or dig(d, False)
        if e.get("status") == "FAILED":
            print(f"    ! {label} falló: {json.dumps(d)[:240]}")
            return None
        time.sleep(5)
    print(f"    ! {label} timeout")
    return None


def guardar(res, path):
    if not res:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    if res.startswith("http"):
        with urllib.request.urlopen(res, timeout=300, context=SSL_CTX) as r:
            path.write_bytes(r.read())
    else:
        path.write_bytes(base64.b64decode(res))
    from PIL import Image

    print(f"    ✓ {path.name}  {Image.open(path).size}")
    return True


def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()


def paso2_variantes():
    print("\n▸ Paso 2 — variantes de piso (sala idéntica)")
    base_img = DEST / f"amb_{BASE}_feed.jpg"
    if not base_img.exists():
        sys.exit(f"Falta la base {base_img}; correr casablanca-ambiente-unico.py")
    ref = b64(base_img)
    ep = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    for sku, (prod, madera) in SKUS.items():
        if madera is None:
            continue
        destino = DEST / f"nb_{sku}.jpg"
        if destino.exists():
            print(f"    = ya existe {destino.name}")
            continue
        prompt = (
            "The first image is an interior photograph. The second image shows the "
            f"actual wood flooring product. Replace ONLY the wood floor in the first "
            f"image with this product: {madera}. {IDENTICO}"
        )
        st, d = http(ep, "POST", {"prompt": prompt, "reference_images": [ref, b64(PRODUCTOS / prod)]})
        print(f"  [{sku}] nano-banana -> HTTP {st}")
        if st not in (200, 201):
            print(f"    {json.dumps(d)[:300]}")
            continue
        guardar(poll(ep, d.get("data", {}).get("task_id"), sku), destino)


def paso3_upscale():
    print("\n▸ Paso 3 — subir resolución de las variantes")
    ep = "https://api.freepik.com/v1/ai/image-upscaler"
    for sku, (_, madera) in SKUS.items():
        if madera is None:
            continue
        src = DEST / f"nb_{sku}.jpg"
        destino = DEST / f"amb_{sku}_feed.jpg"
        if not src.exists() or destino.exists():
            print(f"    = se salta {sku}")
            continue
        st, d = http(ep, "POST", {"image": b64(src), "scale_factor": "2x"})
        print(f"  [{sku}] upscaler -> HTTP {st}")
        if st not in (200, 201):
            print(f"    {json.dumps(d)[:300]}")
            continue
        if not guardar(poll(ep, d.get("data", {}).get("task_id"), sku), destino):
            # Sin upscaler, la variante igual sirve: 1024 sobre un lienzo de 1080.
            destino.write_bytes(src.read_bytes())
            print(f"    ~ {destino.name} sin upscale (se usa el 1024)")


def paso4_story():
    """No genera nada: la story usa LA MISMA foto del feed.

    Se probaron los dos caminos para tener un 9:16 propio y ninguno sirve:
      · `image-expand/flux-pro` ignora el tamaño pedido — devuelve ~1344×1184
        con cualquier `aspect_ratio`, `top` o `bottom`.
      · Mystic con `structure_reference` **fuerza la proporción de la referencia**:
        pidiendo social_story_9_16 sobre una base cuadrada devuelve 2944×2944.

    Así que la story monta la foto cuadrada en encuadre vertical (objectFit
    cover). Es la misma sala y la misma tabla por construcción, que es lo que
    pide el lineamiento nº1, en vez de una generación distinta que se parezca.
    """
    print("\n▸ Paso 4 — la story reusa la foto del feed (ver el docstring)")


def main():
    pasos = [a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--paso")]
    todo = not pasos
    if todo or "2" in pasos:
        paso2_variantes()
    if todo or "3" in pasos:
        paso3_upscale()
    if todo or "4" in pasos:
        paso4_story()
    print(f"\nListo en {DEST}")


if __name__ == "__main__":
    main()

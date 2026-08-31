#!/usr/bin/env python3
"""Casablanca C1 — CUATRO ambientes distintos, uno por producto (Jenny, 28-08-2026).

    python3 scripts/casablanca-ambientes-jenny.py natural_uv_grande
    python3 scripts/casablanca-ambientes-jenny.py --todos
    python3 scripts/casablanca-ambientes-jenny.py natural_uv_grande --medir

Por qué existe, y por qué NO se reusa `casablanca-ambiente-unico.py`:

  · La clienta pidió por WhatsApp el 28-08: *«por favor usar ambiente distintos en
    cada foto no el mismo»*. Eso DEROGA el lineamiento nº1 del brief —«UN MISMO
    AMBIENTE EN LAS 4 TARJETAS»—, que era la regla sobre la que estaba construido
    el script anterior. Ver `feedback/2026-08-28-ronda4-cliente.md`.

  · El método viejo era una base + 3 ediciones img-to-img. Su prompt base decía
    «engineered oak plank flooring in **warm honey tone**», así que las cuatro
    tarjetas arrastraban el miel — incluido el Cumarú, que es café rojizo. Medido:
    el piso del ambiente daba ΔE 17,6 a 31,6 contra la foto oficial del producto.
    Jenny lo vio a simple vista: *«este piso no se parece al producto real»*.

  · Acá cada ambiente se genera SOLO, con su propia sala, y el piso se describe
    desde la foto oficial del SKU y desde la referencia que mandó Jenny.

⚠️ Las referencias de Jenny (`raw/casablanca/ref-jenny-28ago/`) son REFERENCIA, no
material: *«yo las tengo para mis post, por favor usar otras ustedes»*. No se
publican ni se recortan; sirven para fijar tono, veta y formato de tabla.

La verificación NO es opcional, y el juez es la REFERENCIA DE JENNY, no la foto
oficial del producto. Medido el 28-08: la oficial es plana de estudio y tiene croma
29,8; el mismo piso en una sala con luz, en la propia referencia de la clienta, da
croma 14-15. La oficial no es un objetivo alcanzable en un ambiente. Se comparan
TONO y CROMA, no la luminosidad — el L* depende de cuánta luz tenga la sala, que es
decisión de composición y no de fidelidad de producto. Ver `mide()`.
"""
import argparse
import base64
import json
import os
import pathlib
import ssl
import sys
import time
import urllib.request

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

RAIZ = pathlib.Path(str(_RAIZ))
ASSETS = RAIZ / "public/assets/casablanca"
DEST = ASSETS / "sep"
SSL_CTX = ssl.create_default_context()
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    pass

BASE = "https://api.freepik.com/v1/ai/mystic"
ASPECTO = {"feed": "square_1_1", "feed45": "social_post_4_5"}

# ── La madera, dicha desde la foto oficial y desde la referencia de Jenny ────────
# Ojo: los tres robles comparten tono (72,5° · 76,3° · 78,1° en Lab; sólo el Cumarú
# se separa, 59,3°). O sea que el color NO distingue tres de los cuatro: lo que los
# separa es la TEXTURA y el FORMATO de tabla. Por eso cada prompt insiste en las
# dimensiones reales en mm y en el acabado, no sólo en el color.
MADERA = {
    "natural_uv_grande": (
        "natural light oak flooring of MEDIUM tone — clearly warm, the colour of "
        "raw untreated oak, with only a light greige cast. Not orange, not golden, "
        "not honey, and NOT grey, NOT beige-white, NOT bleached. Subtle fine grain, "
        "no knots, matte UV finish. Wide long planks, 190 mm wide and 1900 mm long, "
        "laid lengthwise with few seams."
    ),
    "natural_uv_chico": (
        "light greige oak flooring, desaturated and natural — NOT orange, NOT "
        "golden, NOT bleached white — a soft muted greyish-beige oak of medium-light "
        "tone with subtle fine grain and no knots, matte UV finish. Narrower shorter "
        "planks, 167 mm wide and 1200 mm long, so the seams across the floor are "
        "noticeably more frequent."
    ),
    "aserrado": (
        "warm honey oak flooring with pronounced saw-cut texture, open grain and "
        "visible dark knots, rustic character, matte finish. Wide long planks, "
        "190 mm wide and 1900 mm long."
    ),
    "cumaru": (
        "cumaru tropical hardwood flooring in a deep reddish-brown mahogany tone, "
        "tight straight fine grain with almost no knots, warm satin sheen. Narrow "
        "very long planks, 120 mm wide and 2130 mm long, laid lengthwise."
    ),
}

# ── La sala. UNA DISTINTA POR PRODUCTO — es el pedido de Jenny ───────────────────
# Todas comparten lo que el brief sí sigue pidiendo y ella no tocó:
#   nº2 plano amplio, el piso ocupa al menos la mitad del cuadro
#   nº3 habitado pero despejado, dos o tres elementos
#   nº4 luz natural y muros claros
#   nº5 el tercio superior tiene que ser muro limpio: ahí cae el bloque de texto
SALA = {
    "natural_uv_grande":
        "a double-height living room with a tall window on the left, a pale plaster "
        "wall, one low linen sofa set far back on the left and a single olive tree "
        "in a stone planter",
    "natural_uv_chico":
        "a serene open dining room with a tall window wall on the right, a slim oak "
        "table with four chairs set back on the left and a single ceramic vase",
    "aserrado":
        "a warm rustic-modern living room with a white brick chimney breast on the "
        "right, slim wooden ceiling beams, one linen armchair and a woven basket "
        "with a green plant",
    "cumaru":
        "a calm contemporary lounge with a full-height glass wall opening to a "
        "garden on the right, one low dark-green sofa set back and a round stone "
        "coffee table",
}

COMUN = (
    "Interior architectural photograph, camera at waist height angled slightly "
    "downward so the wood floor fills the entire bottom 55 percent of the frame and "
    "recedes in perspective toward the viewer. The upper third of the image must be "
    "CLEAN EMPTY WALL, with no furniture, no art and no objects. Wide empty floor "
    "area in the foreground with nothing on it. Soft natural daylight, warm neutral "
    "white balance, calm and uncluttered. Architectural Digest style, "
    "photorealistic, sharp. No people, no text, no logos, no watermark."
)


def clave():
    p = pathlib.Path.home() / ".magnific_key"
    k = os.environ.get("FREEPIK_API_KEY") or (p.read_text().strip() if p.exists() else "")
    if not k:
        sys.exit("Falta la clave: ~/.magnific_key o FREEPIK_API_KEY")
    return k


def http(url, metodo="GET", cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(url, data=datos, method=metodo, headers={
        "x-freepik-api-key": clave(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180, context=SSL_CTX) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")


def espera(task_id, etiqueta, minutos=8):
    hasta = time.time() + minutos * 60
    while time.time() < hasta:
        st, data = http(f"{BASE}/{task_id}")
        d = data.get("data", {}) if isinstance(data, dict) else {}
        estado = d.get("status")
        if estado in ("COMPLETED", "SUCCESS"):
            g = d.get("generated") or []
            if g:
                return g[0]
            return None
        if estado == "FAILED":
            print(f"  [{etiqueta}] FALLÓ: {json.dumps(data)[:300]}")
            return None
        time.sleep(5)
    print(f"  [{etiqueta}] timeout")
    return None


def genera(sku, fmt):
    prompt = f"{COMUN} The room is {SALA[sku]}. The floor is {MADERA[sku]}"
    cuerpo = {"prompt": prompt, "aspect_ratio": ASPECTO[fmt], "resolution": "2k",
              "realism": True, "engine": "automatic", "creative_detailing": 20}
    st, data = http(BASE, "POST", cuerpo)
    print(f"  [{sku} {fmt}] POST -> HTTP {st}")
    if st not in (200, 201):
        print(f"    {json.dumps(data)[:400]}")
        return None
    return espera(data.get("data", {}).get("task_id"), f"{sku} {fmt}")


def guarda(url, destino):
    if not url:
        return False
    destino.parent.mkdir(parents=True, exist_ok=True)
    if url.startswith("http"):
        with urllib.request.urlopen(url, timeout=300, context=SSL_CTX) as r:
            destino.write_bytes(r.read())
    else:
        destino.write_bytes(base64.b64decode(url))
    print(f"    ✓ {destino.name} ({destino.stat().st_size // 1024} KB)")
    return True


# ── la verificación ─────────────────────────────────────────────────────────────
def _lab(rgb):
    c = np.asarray(rgb, float) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[.4124, .3576, .1805], [.2126, .7152, .0722], [.0193, .1192, .9505]])
    xyz = c @ M.T / np.array([.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), xyz * 7.787 + 16 / 116)
    return np.array([116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])])


def _medio(p, z):
    a = np.asarray(Image.open(p).convert("RGB"), float)
    H, W = a.shape[:2]
    return a[int(z[1] * H):int(z[3] * H), int(z[0] * W):int(z[2] * W)].reshape(-1, 3).mean(axis=0)


REF_JENNY = RAIZ / "raw/casablanca/ref-jenny-28ago"
REF_ARCHIVO = {"natural_uv_grande": "natural-uv-grande.jpg",
               "natural_uv_chico": "natural-uv-chico.jpg",
               "aserrado": "aserrado.jpg", "cumaru": "cumaru.jpg"}


def _tono_croma(rgb):
    import math
    L, A, B = _lab(rgb)
    return L, math.degrees(math.atan2(B, A)) % 360, math.hypot(A, B)


def mide(sku, ruta):
    """El juez es la REFERENCIA DE JENNY, no la foto oficial del producto.

    Medido el 28-08: la foto oficial es plana de estudio y tiene croma 29,8; el
    mismo piso fotografiado en una sala con luz, en la referencia de la propia
    clienta, da croma 14-15. O sea que la oficial NO es un objetivo alcanzable en un
    ambiente — la referencia de Jenny está a ΔE 17 de ella y aun así ES el producto,
    según quien lo fabrica.

    Se comparan TONO y CROMA, no la luminosidad: el L* depende de cuánta luz tenga
    la sala y eso es decisión de composición, no de fidelidad de producto.
    Así se caza el error real: el ambiente anterior tenía el tono correcto (68,8°
    contra 73,1°) pero croma 32,4 contra 15,4 — el doble de saturado. Se leía miel.
    """
    ref = _medio(REF_JENNY / REF_ARCHIVO[sku], (0.30, 0.60, 0.75, 0.80))
    piso = _medio(ruta, (0.25, 0.72, 0.85, 0.96))
    Lr, hr, cr = _tono_croma(ref)
    Lp, hp, cp = _tono_croma(piso)
    d_tono = abs((hp - hr + 180) % 360 - 180)
    d_croma = abs(cp - cr)
    ok = d_tono <= 8.0 and d_croma <= 8.0
    print(f"      referencia Jenny  L*{Lr:5.1f}  tono {hr:5.1f}°  croma {cr:5.1f}")
    print(f"      piso generado     L*{Lp:5.1f}  tono {hp:5.1f}°  croma {cp:5.1f}")
    print(f"    Δtono {d_tono:4.1f}° (tope 8)   Δcroma {d_croma:4.1f} (tope 8)   "
          f"{'✓ pasa' if ok else '⚠ NO PASA'}")
    return d_tono, d_croma


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sku", nargs="?", choices=list(MADERA))
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--fmt", default="feed45", choices=list(ASPECTO))
    ap.add_argument("--medir", action="store_true",
                    help="sólo medir lo que ya está, sin generar")
    a = ap.parse_args()
    skus = list(MADERA) if a.todos else ([a.sku] if a.sku else [])
    if not skus:
        ap.error("dime un sku o pasa --todos")

    for sku in skus:
        destino = DEST / f"amb_{sku}_{a.fmt}.jpg"
        print(f"── {sku} · {a.fmt}")
        if a.medir:
            if destino.exists():
                mide(sku, destino)
            else:
                print("    no existe todavía")
            continue
        nuevo = DEST / f"amb_{sku}_{a.fmt}.nuevo.jpg"
        if guarda(genera(sku, a.fmt), nuevo):
            mide(sku, nuevo)
            print(f"    queda en {nuevo.name} — revísala y renómbrala a mano si sirve")


if __name__ == "__main__":
    main()

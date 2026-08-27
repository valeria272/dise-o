#!/usr/bin/env python3
"""
BETWEEN · montajes que el banco de fotos del cliente NO tiene (septiembre 2026).

⭐ Punto 6 del feedback del 27-08-2026, literal:
   «Mejorar el prompt para las imágenes que hagas montaje, ya que el cliente busca
    "realismo y naturalidad", quiere que la terraza y sus vasos TO GO sean los
    actuales, para que mantenga coherencia.»

Por eso NINGÚN montaje se genera de texto puro cuando aparece un vaso To Go o el
local: se genera con **Nano Banana pasándole una foto REAL de Between como
referencia**, así el vaso de cartón con tapa negra es el de verdad en forma,
proporción y material — pero SIN logo impreso (ver la nota de VASO). Solo lo que no existe en ninguna foto (un bodegón de
ingredientes, la caja de emergencia) sale de Mystic.

Uso:
    python3 scripts/between-montajes-sept.py            # genera lo que falte
    python3 scripts/between-montajes-sept.py --forzar   # regenera todo
    python3 scripts/between-montajes-sept.py --solo cafe-gigante
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
from pathlib import Path

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:                                    # el fix SSL de macOS
    SSL_CTX = ssl.create_default_context()

RAIZ = Path(__file__).resolve().parent.parent
FOTOS = RAIZ / "public/assets/hilton/between/fotos-gradadas"
DEST = RAIZ / "public/assets/hilton/between/ia-sept"


def clave() -> str:
    if os.environ.get("FREEPIK_API_KEY"):
        return os.environ["FREEPIK_API_KEY"]
    env = RAIZ.parent / "ASISTENTE PERSONAL/.env"
    if env.exists():
        for ln in env.read_text(errors="ignore").splitlines():
            if ln.startswith("FREEPIK_API_KEY="):
                return ln.split("=", 1)[1].strip().strip('"')
    sys.exit("No encontré FREEPIK_API_KEY (ni en el entorno ni en ASISTENTE PERSONAL/.env)")


H = {"x-freepik-api-key": clave(), "Content-Type": "application/json"}

# ── El ADN visual que toda imagen de Between tiene que respetar ──────────────
# Sale de clients/hilton/CLAUDE.md y de las reglas escritas de la diseñadora.
ESTILO = (
    "Photorealistic lifestyle photography for a specialty coffee shop in Santiago, "
    "Chile. Warm natural daylight, soft directional window light, no flash, no "
    "blown-out highlights, no harsh reflections on the table. Warm neutral palette: "
    "wood, cream, deep green plants, taupe. Shallow depth of field, natural skin "
    "tones, candid and unposed. Editorial food-photography quality. "
    "Absolutely no text, no lettering, no watermarks and no logos anywhere in the "
    "image. Any ceramic cup must be plain white with no printed brand."
)

# ⚠️ La taza va SIN logo impreso, a propósito. Nano Banana intenta reproducir el
# logo de la foto de referencia y lo saca DEFORME («B3TWEEIN», letras rotas), que
# es peor que no ponerlo: es la misma regla por la que a la taza blanca hay que
# borrarle el KIMBO. La marca la pone el logo vectorial de la pieza, no la foto.
VASO = (
    "The takeaway cup is a tall kraft brown paper cup with a matte BLACK plastic "
    "dome lid and no cardboard sleeve — the same format Between actually uses. "
    "CRITICAL: the cup must be completely PLAIN — absolutely no printed logo, no "
    "brand name, no letters, no symbols and no pattern anywhere on it. A blank "
    "kraft cup. Do not attempt to draw any logo."
)

# ── Los montajes. `ref` = foto real de Between que fija el vaso o el local. ──
MONTAJES = [
    dict(
        nombre="togo-salida",
        ref=None,
        ratio="social_post_4_5",
        prompt=(
            f"{ESTILO} A young woman in her late twenties stepping out of a modern "
            "coffee shop doorway onto a sunny city sidewalk, seen from the front at "
            "a slight angle, mid-stride, relaxed and in a hurry in a good way. She "
            "holds the takeaway coffee cup in one hand and a plain kraft paper "
            "takeaway bag in the other. Morning light, urban but calm background "
            f"softly out of focus. Vertical 4:5 framing with clear empty space in "
            f"the upper third for a headline. {VASO}"
        ),
    ),
    dict(
        nombre="cumple-manos",
        ref=None,
        ratio="social_post_4_5",
        prompt=(
            f"{ESTILO} Extreme close-up of two pairs of hands at the counter of a "
            "coffee shop: one hand of a barista handing over the takeaway coffee "
            "cup, the other hand of a customer receiving it. The cup sits exactly "
            "in the centre of the frame and is the meeting point between both "
            "hands. Background is the warm, softly blurred interior of the café "
            "with plants. Spontaneous, like the real moment someone gets their "
            f"coffee. Vertical 4:5 framing, empty space in the lower third. {VASO}"
        ),
    ),
    dict(
        nombre="cumple-vela",
        ref=None,
        ratio="social_story_9_16",
        prompt=(
            f"{ESTILO} The takeaway coffee cup standing on a warm wooden café table, "
            "photographed in close-up at a 45-degree angle, with one single slim lit "
            "birthday candle standing right next to it, as if the coffee were a tiny "
            "birthday cake. Small warm flame, gentle glow. Background is the blurred "
            "café interior with green plants. Vertical 9:16 framing with generous "
            f"empty space in the upper half for a headline. {VASO}"
        ),
    ),
    dict(
        nombre="cafe-gigante",
        ref=None,
        ratio="social_story_9_16",
        prompt=(
            f"{ESTILO} Surreal but photorealistic scale illusion, like an "
            "oversized-object art installation. A young woman walks along a sunlit "
            "sidewalk carrying an ENORMOUS takeaway coffee cup about the size of "
            "her torso, hugging it with both arms and leaning back under the "
            "weight. Kraft paper cup with its matte black dome lid clearly on top. "
            "COMPOSITION, CRITICAL: she stands in the LOWER TWO THIRDS — the top of "
            "the cup she carries reaches no higher than 45%% down the frame. The "
            "ENTIRE UPPER THIRD of the image is a plain, empty, sunlit plaster "
            "wall: no plants, no roof, no awning, no windows, no branches, nothing "
            "at all, left deliberately blank for a headline. Full body down to her "
            f"shoes. Strong side sun, one long shadow on the pavement. {VASO}"
        ),
    ),
    dict(
        nombre="calculadora-mesa",
        ratio="social_story_9_16",
        ref=None,
        prompt=(
            f"{ESTILO} Straight overhead flat-lay of a café table, shot from directly "
            "above: a pocket calculator in the very centre, an open notebook with "
            "blank pages, a pen, a closed laptop at the edge of the frame, and a "
            "white ceramic coffee cup that is almost empty. The scene should feel "
            "like someone trying to get through the day and clearly running out of "
            "fuel. Warm wooden table, natural side light, soft shadows. Vertical "
            "9:16 framing with empty table surface in the upper third for a headline."
        ),
    ),
    dict(
        nombre="emergencia-caja",
        ref=None,
        ratio="social_story_9_16",
        prompt=(
            f"{ESTILO} A wall-mounted emergency cabinet of the classic kind used for "
            "fire extinguishers: a single rectangular case with a clear GLASS front "
            "panel, a slim cream metal frame and a small emergency hammer hanging "
            "beside it on a thin chain. Mounted at eye level on a warm taupe "
            "plastered wall. Behind the glass, instead of a fire extinguisher, "
            "there are TWO shelves displaying exactly three café items like "
            "museum exhibits, ALL fully visible, none cropped or hidden: a kraft "
            "brown takeaway coffee cup with a black lid, one golden croissant and "
            "one sandwich. Warm light inside the case. "
            "COMPOSITION, CRITICAL: the cabinet sits in the exact VERTICAL CENTRE "
            "of the frame — the top quarter of the image is empty plaster wall and "
            "the bottom quarter is empty wall too, both deliberately blank for "
            "text. No plants in front of the cabinet. Vertical 9:16 framing."
        ),
    ),
    dict(
        # el togo-trio anterior traía un logo INVENTADO y deforme en el vaso
        nombre="togo-trio",
        ref=None,
        ratio="social_post_4_5",
        prompt=(
            f"{ESTILO} A wooden café table by a sunlit window: one takeaway coffee "
            "cup standing tall, and next to it a small wooden board with a golden "
            "croissant and a fresh sandwich wrapped in kraft paper, both looking "
            "irresistible. Green foliage softly blurred behind. The three items "
            "read clearly as a set of three. Vertical 4:5 framing with empty space "
            f"in the upper third for a headline. {VASO}"
        ),
    ),
    dict(
        nombre="strudel-entero",
        ref=None,
        prompt=(
            f"{ESTILO} A single generous slice of apple strudel on a small ceramic "
            "plate, photographed close up at a 45-degree angle. Golden flaky layered "
            "pastry with visible crisp sheets, warm baked apple filling with cinnamon "
            "spilling slightly at the cut, a scatter of chopped walnuts and a light "
            "dusting of icing sugar. Extremely appetising, glossy and fresh out of "
            "the oven. Square framing, the dessert fills the frame."
        ),
        ratio="square_1_1",
    ),
]


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


def dig(obj, want_url=True):
    """Las respuestas cambian de forma entre modelos: se busca la imagen a fondo."""
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


def poll(base, task_id, etiqueta):
    for _ in range(90):
        st, data = http(f"{base}/{task_id}")
        d = data.get("data", {}) if isinstance(data, dict) else {}
        if d.get("status") in ("COMPLETED", "SUCCESS"):
            return dig(data, True) or dig(data, False)
        if d.get("status") == "FAILED":
            print(f"    ⛔ falló: {json.dumps(data)[:300]}")
            return None
        time.sleep(5)
    print("    ⛔ timeout")
    return None


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def con_referencia(prompt, ref: Path, ratio, etiqueta):
    base = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    # sin `aspect_ratio` el modelo devuelve TODO en 1248×832 apaisado, y recortar
    # eso a 9:16 se come la mitad de la escena
    st, data = http(base, "POST", {
        "prompt": prompt, "reference_images": [b64(ref)], "aspect_ratio": ratio,
    })
    print(f"    nano-banana (ref {ref.name}) -> HTTP {st}")
    if st not in (200, 201):
        print(f"    {json.dumps(data)[:300]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), etiqueta)


def sin_referencia(prompt, ratio, etiqueta):
    base = "https://api.freepik.com/v1/ai/mystic"
    st, data = http(base, "POST", {
        "prompt": prompt, "aspect_ratio": ratio, "resolution": "2k",
        "realism": True, "engine": "automatic",
    })
    print(f"    mystic ({ratio}) -> HTTP {st}")
    if st not in (200, 201):
        print(f"    {json.dumps(data)[:300]}")
        return None
    return poll(base, data.get("data", {}).get("task_id"), etiqueta)


def guardar(resultado, destino: Path) -> bool:
    if not resultado:
        return False
    if resultado.startswith("http"):
        with urllib.request.urlopen(resultado, timeout=240, context=SSL_CTX) as r:
            destino.write_bytes(r.read())
    else:
        destino.write_bytes(base64.b64decode(resultado))
    kb = destino.stat().st_size // 1024
    if kb < 20:                       # una respuesta de error disfrazada de imagen
        print(f"    ⛔ {destino.name} pesa {kb} KB — sospechoso, se descarta")
        destino.unlink()
        return False
    print(f"    ✅ {destino.name} ({kb} KB)")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--forzar", action="store_true", help="regenera aunque ya exista")
    ap.add_argument("--solo", help="genera solo este montaje")
    args = ap.parse_args()

    DEST.mkdir(parents=True, exist_ok=True)
    hechos, saltados, fallidos = 0, 0, []

    for m in MONTAJES:
        if args.solo and m["nombre"] != args.solo:
            continue
        destino = DEST / f"{m['nombre']}.png"
        if destino.exists() and not args.forzar:
            print(f"[{m['nombre']}] ya existe, se salta")
            saltados += 1
            continue
        print(f"[{m['nombre']}]")
        if m.get("ref"):
            ref = FOTOS / m["ref"]
            if not ref.exists():
                print(f"    ⛔ falta la foto de referencia {ref}")
                fallidos.append(m["nombre"])
                continue
            res = con_referencia(m["prompt"], ref, m.get("ratio", "square_1_1"), m["nombre"])
        else:
            res = sin_referencia(m["prompt"], m.get("ratio", "square_1_1"), m["nombre"])
        if guardar(res, destino):
            hechos += 1
        else:
            fallidos.append(m["nombre"])

    print(f"\n{hechos} generados · {saltados} ya estaban · {len(fallidos)} fallaron")
    if fallidos:
        print("  fallaron:", ", ".join(fallidos))
        sys.exit(1)


if __name__ == "__main__":
    main()

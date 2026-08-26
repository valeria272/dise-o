#!/usr/bin/env python3
"""
REVEX R1 — ambiente del concurso de la alfombra (brief septiembre 2026).

El brief pide: "Ambiente de living con la alfombra de protagonista, ocupando buena
parte del piso. Estilo sobrio y oscuro, como la referencia de la clienta. La
alfombra tiene que verse: es el premio."

Genera el fondo en los dos formatos que pide el brief (cuadrado + story).
"""
import base64, json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, env_compartido as _env_compartido

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

DEST = pathlib.Path(str(_RAIZ / "public/assets/revex/sep"))

KEY = os.environ.get("FREEPIK_API_KEY", "")
if not KEY:
    envp = _env_compartido()
    if envp and pathlib.Path(envp).exists():
        for ln in pathlib.Path(envp).read_text().splitlines():
            if ln.startswith("FREEPIK_API_KEY="):
                KEY = ln.split("=", 1)[1].strip().strip('"').strip("'")
if not KEY:
    sys.exit("Falta FREEPIK_API_KEY")

FP_H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}

# La alfombra es el premio: tiene que ocupar el cuadro y leerse la trama.
PROMPT = (
    "Interior photograph of an elegant contemporary living room in a sober, dark, "
    "moody palette. A large custom-cut area rug is the clear protagonist and covers "
    "most of the floor, filling the lower two thirds of the frame, its woven texture "
    "and cut pile clearly visible with grazing light across it. Around it very few "
    "pieces of furniture, set back and partially cropped: a low sofa upholstered in "
    "dark charcoal fabric, a round white marble coffee table with two art books, a "
    "tall ceramic vase. Deep charcoal, espresso brown and warm taupe tones, low warm "
    "ambient lighting with soft pools of light and long soft shadows, dark walls. "
    "A wide clean uncluttered area of rug in the middle left of the frame with no "
    "objects on it. Architectural digest interior photography, photorealistic, sharp "
    "detail, natural perspective at seated eye height, no people, no text, no logos, "
    "no watermark, no signage."
)

def http(url, headers, method="GET", body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
            raw = r.read()
            try: return r.status, json.loads(raw)
            except Exception: return r.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read()
        try: return e.code, json.loads(raw)
        except Exception: return e.code, raw.decode(errors="ignore")

def dig_url(o):
    if isinstance(o, str):
        return o if o.startswith("http") and any(e in o.lower() for e in (".png",".jpg",".jpeg",".webp")) else None
    if isinstance(o, dict):
        for k in ("raw","url","image_url","output","result"):
            if k in o and (f:=dig_url(o[k])): return f
        for v in o.values():
            if (f:=dig_url(v)): return f
    if isinstance(o, list):
        for v in o:
            if (f:=dig_url(v)): return f
    return None

def dig_b64(o):
    if isinstance(o, str) and len(o) > 5000 and not o.startswith("http"): return o
    if isinstance(o, dict):
        for v in o.values():
            if (f:=dig_b64(v)): return f
    if isinstance(o, list):
        for v in o:
            if (f:=dig_b64(v)): return f
    return None

def generar(aspect, nombre, seed):
    base = "https://api.freepik.com/v1/ai/mystic"
    st, data = http(base, FP_H, "POST", {
        "prompt": PROMPT, "aspect_ratio": aspect, "resolution": "2k",
        "realism": True, "engine": "automatic", "seed": seed,
    })
    print(f"  [{nombre}] POST mystic -> HTTP {st}")
    if st not in (200, 201):
        print("  ", json.dumps(data)[:400]); return False
    tid = data.get("data", {}).get("task_id")
    for _ in range(90):
        st, d = http(f"{base}/{tid}", FP_H)
        dd = d.get("data", d) if isinstance(d, dict) else {}
        s = dd.get("status")
        if s in ("COMPLETED","SUCCESS","completed"):
            res = dig_url(d) or dig_b64(d)
            p = DEST / f"{nombre}.jpg"
            if res.startswith("http"):
                with urllib.request.urlopen(res, timeout=180, context=SSL_CTX) as r:
                    p.write_bytes(r.read())
            else:
                p.write_bytes(base64.b64decode(res))
            print(f"  [{nombre}] guardado {p.name} ({p.stat().st_size//1024} KB)")
            return True
        if s in ("FAILED","failed"):
            print(f"  [{nombre}] fallo: {json.dumps(d)[:300]}"); return False
        time.sleep(5)
    print(f"  [{nombre}] timeout"); return False

if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    ok = 0
    for aspect, nombre, seed in [("square_1_1","concurso_amb_feed",41207),
                                 ("social_story_9_16","concurso_amb_story",41207)]:
        if generar(aspect, nombre, seed): ok += 1
    print(f"\nlisto: {ok}/2")

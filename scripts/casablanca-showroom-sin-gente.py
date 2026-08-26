"""Casablanca C2 (ronda 2) — el interior REAL del showroom, sin el equipo.

De las 24 fotos del showroom de Vitacura, 20 son la fachada desde afuera y las
4 del interior tienen al equipo posando. No tenemos derechos de imagen del
equipo, y dirección vetó (con razón) inventar un local con IA: la pieza invita
a Vitacura, así que tiene que mostrar Vitacura.

La salida correcta es la foto real del local con las personas borradas: no se
inventa el showroom, se quita a la gente. Además se saca el extintor, que
Paulina marcó como el tipo de detalle que ensucia la imagen.

Uso:  FREEPIK_API_KEY=... python3 scripts/casablanca-showroom-sin-gente.py
"""
import base64, json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

RAIZ = pathlib.Path(str(_RAIZ))
ORIGEN = RAIZ / "raw/casablanca/showroom/_JCW0017.jpg"
DEST = RAIZ / "public/assets/casablanca"
KEY = os.environ.get("FREEPIK_API_KEY", "")
if not KEY:
    sys.exit("Falta FREEPIK_API_KEY")
H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}

PROMPT = (
    "Remove the three people from this flooring showroom photograph completely. "
    "Reconstruct what is behind them: continue the vertical wood sample panels in "
    "their black display frames across the back wall, and continue the oak plank "
    "floor in correct perspective. Also remove the red fire extinguisher on the "
    "right wall. Keep absolutely everything else pixel-identical: the same "
    "panels, the same frames, the same floor, the same walls, the same lighting "
    "and the same camera angle. The result must be the same empty showroom "
    "interior, clean and photorealistic. No people, no text, no logos."
)


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


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    # La API pide un archivo manejable: se reduce el master de 5603 px.
    tmp = DEST / "_tmp_showroom_in.jpg"
    im = Image.open(ORIGEN).convert("RGB")
    im.thumbnail((1600, 1600))
    im.save(tmp, quality=92)
    ref = base64.b64encode(tmp.read_bytes()).decode()

    base = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    st, data = http(base, "POST", {"prompt": PROMPT, "reference_images": [ref]})
    print(f"nano-banana -> HTTP {st}")
    if st not in (200, 201):
        sys.exit(json.dumps(data)[:500])
    task = data.get("data", {}).get("task_id")
    for _ in range(90):
        s2, d2 = http(f"{base}/{task}")
        status = (d2.get("data") or {}).get("status")
        if status in ("COMPLETED", "SUCCESS"):
            res = dig(d2, True) or dig(d2, False)
            out = DEST / "sr_interior_limpio.jpg"
            if res.startswith("http"):
                with urllib.request.urlopen(res, timeout=240, context=SSL_CTX) as r:
                    out.write_bytes(r.read())
            else:
                out.write_bytes(base64.b64decode(res))
            tmp.unlink(missing_ok=True)
            print(f"guardado {out} ({out.stat().st_size // 1024} KB)")
            return
        if status == "FAILED":
            sys.exit(json.dumps(d2)[:400])
        time.sleep(5)
    sys.exit("timeout")


if __name__ == "__main__":
    main()

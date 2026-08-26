"""Revex Temuco (ronda 2) — saca el fondo real del local desde el video oficial.

La pieza de Temuco venía sin foto: `temuco_fachada.jpg` es un placeholder y el
reemplazo de la ronda 1 era un collage de dos fotos que Paulina rechazó.

Pero el material SÍ existía: `raw/revex/ref-drive/videos/rvx_storie_temuco.mp4` es
el video oficial del showroom de Temuco, en 2160 × 3840, y dice en pantalla
«Visítanos en Reyes Católicos 1550, Temuco» — es el local actual, no el viejo de
Hochstetter 220 que sale en las gráficas de 2024.

Este script toma el frame más limpio y le borra el bloque rojo del logo y el texto
sobreimpreso, para poder usarlo como fondo de la pieza nueva.

Uso:  FREEPIK_API_KEY=... python3 scripts/revex-temuco-limpiar.py
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
DEST = RAIZ / "public/assets/revex/sep"
KEY = os.environ.get("FREEPIK_API_KEY", "")
if not KEY:
    sys.exit("Falta FREEPIK_API_KEY")
H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}

TOMAS = [
    ("frame_4.2.png", "temuco_reparado_salon",
     "Remove the red square logo badge at the top left corner and any overlaid "
     "text or graphics. Reconstruct the ceiling and wall behind them. Keep the "
     "showroom itself pixel-identical: the same display panels, the same tile and "
     "flooring samples, the same GRUPOREVEX sign painted on the back wall, the "
     "same floor, the same lighting and the same camera angle. Photorealistic "
     "interior of a flooring showroom. No people, no overlaid text, no watermark."),
    ("frame_9.0.png", "temuco_reparado_piedras",
     "Remove the red square logo badge at the top left corner and the red text "
     "banner in the middle. Reconstruct what is behind them: continue the natural "
     "stone display panels, the 'PIEDRAS NATURALES' sign and the floor in correct "
     "perspective. Keep everything else pixel-identical: the same samples, the "
     "same lighting, the same camera angle. Photorealistic flooring showroom "
     "interior. No people, no overlaid text, no watermark."),
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


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    origen = RAIZ / "raw/revex/temuco-video"
    base = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    for archivo, salida, prompt in TOMAS:
        src = origen / archivo
        if not src.exists():
            print(f"  falta {src}")
            continue
        tmp = DEST / "_tmp_in.jpg"
        im = Image.open(src).convert("RGB")
        im.thumbnail((1600, 1600))
        im.save(tmp, quality=92)
        ref = base64.b64encode(tmp.read_bytes()).decode()
        st, data = http(base, "POST", {"prompt": prompt, "reference_images": [ref]})
        print(f"[{salida}] nano-banana -> HTTP {st}")
        if st not in (200, 201):
            print(json.dumps(data)[:400])
            continue
        task = data.get("data", {}).get("task_id")
        for _ in range(90):
            s2, d2 = http(f"{base}/{task}")
            status = (d2.get("data") or {}).get("status")
            if status in ("COMPLETED", "SUCCESS"):
                res = dig(d2, True) or dig(d2, False)
                out = DEST / f"{salida}.jpg"
                if res.startswith("http"):
                    with urllib.request.urlopen(res, timeout=240, context=SSL_CTX) as r:
                        out.write_bytes(r.read())
                else:
                    out.write_bytes(base64.b64decode(res))
                print(f"  guardado {out.name} ({out.stat().st_size // 1024} KB)")
                break
            if status == "FAILED":
                print("  falló:", json.dumps(d2)[:300])
                break
            time.sleep(5)
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()

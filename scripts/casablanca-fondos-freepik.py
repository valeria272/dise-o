#!/usr/bin/env python3
"""
Casablanca C1 — genera los 4 fondos de ambiente.

Detecta solo si la credencial es de Higgsfield o de Freepik/Magnific y usa la
que responda. Crea UNA imagen base y luego 3 ediciones img-to-img cambiando
únicamente el piso (regla nº1 del brief: mismo ambiente en las 4 tarjetas).

Uso:
    python3 genera_fondos.py

Lee la credencial de cfg.json (mismo directorio) o de las variables de entorno
HF_API_KEY / HF_SECRET / FREEPIK_API_KEY.
"""
import base64, json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


try:
    import certifi

    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:  # este Python trae el bundle de CA incompleto
    SSL_CTX = ssl.create_default_context()

HERE = pathlib.Path(__file__).parent
DEST = pathlib.Path(
    str(_RAIZ / "public/assets/casablanca")
)

# ---------------------------------------------------------------- credencial
KEY = os.environ.get("HF_API_KEY") or os.environ.get("FREEPIK_API_KEY") or ""
SECRET = os.environ.get("HF_SECRET") or ""
if not KEY:
    cfg_path = HERE / "cfg.json"
    if cfg_path.exists():
        cfg = json.loads(cfg_path.read_text())
        KEY, SECRET = cfg.get("key", ""), cfg.get("secret", "")
if not KEY:
    sys.exit("No hay credencial: define HF_API_KEY/FREEPIK_API_KEY o crea cfg.json")

# ---------------------------------------------------------------- prompts
BASE_PROMPT = (
    "Interior photograph of a bright airy living-dining room, camera at waist "
    "height angled slightly downward so the engineered wood floor fills the entire "
    "bottom 55 percent of the frame and recedes in perspective toward the viewer. "
    "Above the floor, a plain light plaster wall with a section of exposed brick "
    "and slim wooden ceiling beams. Only two or three furniture pieces, placed to "
    "the left and set back: a simple light-wood dining table with chairs and a "
    "woven basket with a green plant. Large window on the right with soft natural "
    "daylight, warm neutral white balance. Very clean and uncluttered, with a wide "
    "empty floor area in the foreground and no objects on it. Engineered oak plank "
    "flooring in warm honey tone, wide long planks laid lengthwise. Architectural "
    "digest style, photorealistic, sharp, no people, no text, no logos, "
    "no watermark."
)

EDIT_PREFIX = (
    "Keep the entire scene absolutely identical - same walls, same brick, same "
    "beams, same furniture, same plant, same window, same daylight, same white "
    "balance, same camera angle and framing. Change ONLY the wood floor planks to: "
)

VARIANTS = [
    (
        "amb_natural_uv_chico",
        EDIT_PREFIX
        + "the same honey oak tone and finish, but noticeably narrower and shorter "
        "planks, more visible seams across the floor.",
    ),
    (
        "amb_aserrado",
        EDIT_PREFIX
        + "rustic sawn-cut oak with pronounced saw marks, open grain, visible knots "
        "and strong texture, slightly cooler and more matte than before.",
    ),
    (
        "amb_cumaru",
        EDIT_PREFIX
        + "narrow long cumaru planks in a warm reddish-brown tropical hardwood tone, "
        "tight straight grain, satin sheen.",
    ),
]

BASE_NAME = "amb_natural_uv_grande"


# ---------------------------------------------------------------- http utils
def http(url, headers, method="GET", body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
            raw = r.read()
            try:
                return r.status, json.loads(raw)
            except Exception:
                return r.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw.decode(errors="ignore")


def download(url, path):
    with urllib.request.urlopen(url, timeout=180, context=SSL_CTX) as r:
        path.write_bytes(r.read())
    print(f"  guardado: {path.name} ({path.stat().st_size // 1024} KB)")


def dig_url(obj):
    """Busca recursivamente la primera URL de imagen en la respuesta."""
    if isinstance(obj, str):
        if obj.startswith("http") and any(
            e in obj.lower() for e in (".png", ".jpg", ".jpeg", ".webp")
        ):
            return obj
        return None
    if isinstance(obj, dict):
        for k in ("raw", "url", "image_url", "output", "result"):
            if k in obj:
                found = dig_url(obj[k])
                if found:
                    return found
        for v in obj.values():
            found = dig_url(v)
            if found:
                return found
    if isinstance(obj, list):
        for v in obj:
            found = dig_url(v)
            if found:
                return found
    return None


def dig_b64(obj):
    """Busca base64 de imagen en la respuesta (Freepik lo devuelve así a veces)."""
    if isinstance(obj, str) and len(obj) > 5000 and not obj.startswith("http"):
        return obj
    if isinstance(obj, dict):
        for v in obj.values():
            found = dig_b64(v)
            if found:
                return found
    if isinstance(obj, list):
        for v in obj:
            found = dig_b64(v)
            if found:
                return found
    return None


# ---------------------------------------------------------------- detección
HF_H = {"hf-api-key": KEY, "hf-secret": SECRET, "Content-Type": "application/json"}
FP_H = {"x-freepik-api-key": KEY, "Content-Type": "application/json"}


def detect():
    """401/403 = la credencial no es de ese servicio. Cualquier otra cosa = sí lo es."""
    st, body = http("https://api.freepik.com/v1/ai/mystic", FP_H, "POST", {})
    print(f"  Freepik  /v1/ai/mystic  -> HTTP {st}")
    if st not in (401, 403):
        return "freepik"

    st, body = http(
        "https://platform.higgsfield.ai/v1/text2image/soul", HF_H, "POST", {}
    )
    print(f"  Higgsfield /v1/text2image/soul -> HTTP {st}")
    if st not in (401, 403):
        return "higgsfield"

    print(f"  última respuesta: {json.dumps(body)[:300]}")
    return None


# ---------------------------------------------------------------- Higgsfield
def hf_poll(job_set_id, label):
    for _ in range(90):
        st, data = http(
            f"https://platform.higgsfield.ai/v1/job-sets/{job_set_id}", HF_H
        )
        jobs = data.get("jobs", []) if isinstance(data, dict) else []
        statuses = [j.get("status") for j in jobs]
        if statuses and all(s in ("completed", "failed") for s in statuses):
            if "failed" in statuses:
                print(f"  [{label}] job falló: {json.dumps(data)[:400]}")
                return None
            return dig_url(data)
        time.sleep(5)
    print(f"  [{label}] timeout esperando el job")
    return None


def hf_text2image(prompt, label):
    st, data = http(
        "https://platform.higgsfield.ai/v1/text2image/soul",
        HF_H,
        "POST",
        {
            "params": {
                "prompt": prompt,
                "width_and_height": "2048x2048",
                "enhance_prompt": False,
                "quality": "1080p",
                "batch_size": 1,
                "seed": 77021,
            }
        },
    )
    print(f"  [{label}] soul POST -> HTTP {st}")
    if st not in (200, 201):
        print(f"  respuesta: {json.dumps(data)[:500]}")
        return None
    return hf_poll(data.get("id"), label)


def hf_edit(prompt, ref_url, label):
    for endpoint, body in (
        (
            "https://platform.higgsfield.ai/v1/image2image/nano-banana",
            {"params": {"prompt": prompt, "input_images": [{"type": "image_url", "image_url": ref_url}]}},
        ),
        (
            "https://platform.higgsfield.ai/v1/image2image",
            {"params": {"prompt": prompt, "input_images": [{"type": "image_url", "image_url": ref_url}], "model": "nano-banana"}},
        ),
    ):
        st, data = http(endpoint, HF_H, "POST", body)
        print(f"  [{label}] {endpoint.rsplit('/', 1)[-1]} -> HTTP {st}")
        if st in (200, 201):
            return hf_poll(data.get("id"), label)
        print(f"  respuesta: {json.dumps(data)[:300]}")
    return None


# ---------------------------------------------------------------- Freepik
def fp_poll(base, task_id, label):
    for _ in range(90):
        st, data = http(f"{base}/{task_id}", FP_H)
        d = data.get("data", data) if isinstance(data, dict) else {}
        status = d.get("status")
        if status in ("COMPLETED", "SUCCESS", "completed"):
            return dig_url(data) or dig_b64(data)
        if status in ("FAILED", "failed"):
            print(f"  [{label}] falló: {json.dumps(data)[:300]}")
            return None
        time.sleep(5)
    print(f"  [{label}] timeout")
    return None


def fp_text2image(prompt, label):
    base = "https://api.freepik.com/v1/ai/mystic"
    st, data = http(
        base, FP_H, "POST",
        {"prompt": prompt, "aspect_ratio": "square_1_1", "resolution": "2k",
         "realism": True, "engine": "automatic"},
    )
    print(f"  [{label}] mystic POST -> HTTP {st}")
    if st not in (200, 201):
        print(f"  respuesta: {json.dumps(data)[:500]}")
        return None
    return fp_poll(base, data.get("data", {}).get("task_id"), label)


def fp_edit(prompt, ref_b64, label):
    base = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    st, data = http(
        base, FP_H, "POST",
        {"prompt": prompt, "reference_images": [ref_b64]},
    )
    print(f"  [{label}] nano-banana POST -> HTTP {st}")
    if st not in (200, 201):
        print(f"  respuesta: {json.dumps(data)[:500]}")
        return None
    return fp_poll(base, data.get("data", {}).get("task_id"), label)


def save_result(result, path):
    """result puede ser URL o base64."""
    if not result:
        return False
    if result.startswith("http"):
        download(result, path)
    else:
        path.write_bytes(base64.b64decode(result))
        print(f"  guardado: {path.name} ({path.stat().st_size // 1024} KB)")
    return True


# ---------------------------------------------------------------- main
def main():
    DEST.mkdir(parents=True, exist_ok=True)
    print("Detectando API...")
    api = detect()
    if not api:
        sys.exit("La credencial no autenticó ni en Higgsfield ni en Freepik.")
    print(f"API detectada: {api}\n")

    print("1/4 — generando ambiente base (Roble Natural UV 14/3)...")
    base_path = DEST / f"{BASE_NAME}.jpg"
    if api == "higgsfield":
        base_res = hf_text2image(BASE_PROMPT, BASE_NAME)
    else:
        base_res = fp_text2image(BASE_PROMPT, BASE_NAME)
    if not save_result(base_res, base_path):
        sys.exit("No se pudo generar la imagen base; revisa el log de arriba.")

    ref_b64 = base64.b64encode(base_path.read_bytes()).decode()

    for i, (name, prompt) in enumerate(VARIANTS, start=2):
        print(f"\n{i}/4 — {name} (cambiando solo el piso)...")
        if api == "higgsfield":
            res = hf_edit(prompt, base_res, name)
        else:
            res = fp_edit(prompt, ref_b64, name)
        if not save_result(res, DEST / f"{name}.jpg"):
            print(f"  ⚠️  {name} no se generó — se puede reintentar solo esta.")

    print("\nListo. Archivos en:")
    print(f"  {DEST}")
    print("\nSiguiente paso: cambiar los 4 campos bg de C1_CARDS en")
    print("  src/compositions/CasablancaSeptiembre.tsx")
    print("y re-rendir CBSep-C1-1..4 en Feed y Story.")


if __name__ == "__main__":
    main()

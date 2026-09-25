#!/usr/bin/env python3
"""COPYWRITERS · «LA GOMA» — retoque del hero v4 con Nano Banana Pro.

v4 fue la única variante con la idea correcta (goma gastada borrando, no lápiz),
pero Mystic le pintó las uñas de rosa — el rosa se escapaba de la goma — y dejó
una mancha negra junto al dedo medio izquierdo. Se corrige editando, no
regenerando: la escena ya está resuelta.
"""
import base64, io, json, ssl, sys, time, pathlib, urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _entorno import clave_freepik, OUT, FALTA_CLAVE  # noqa: E402

import certifi
from PIL import Image

CTX = ssl.create_default_context(cafile=certifi.where())
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) copylab-estudio/1.0"
API = "https://api.freepik.com/v1/ai/text-to-image/nano-banana-pro"
DIR = OUT / "copylab/goma/hero"

PROMPT = (
    "Edit this exact photograph, keeping everything identical: same woman, same face, same pose, same framing, "
    "same light, same pink eraser, same pink eraser crumbs, same paper, same desk, same film grain. "
    "Only two changes: 1) her fingernails are short, natural and unpolished, bare nail color with no nail polish "
    "at all — the only pink in the whole image must be the eraser and its crumbs; "
    "2) remove the small black object on the paper next to her left hand's middle finger. "
    "Keep the upper-left area of the frame empty and dark. No text, no letters."
)


def pedir(url, clave, cuerpo=None):
    req = urllib.request.Request(
        url, data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
        headers={"x-freepik-api-key": clave, "Content-Type": "application/json", "User-Agent": UA},
        method="POST" if cuerpo is not None else "GET")
    with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
        return json.loads(r.read())


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    clave = clave_freepik()
    if not clave:
        sys.exit(FALTA_CLAVE)
    im = Image.open(DIR / "goma-v4.jpg").convert("RGB")
    im.thumbnail((1400, 1400), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=92)
    cuerpo = {"prompt": PROMPT, "aspect_ratio": "4:5", "resolution": "2K",
              "reference_images": [{"image": base64.b64encode(buf.getvalue()).decode(),
                                    "mime_type": "image/jpeg",
                                    "text": "The photograph to edit — keep it identical except the requested fixes"}]}
    tareas = [pedir(API, clave, cuerpo)["data"]["task_id"] for _ in range(n)]
    pend = dict(enumerate(tareas, 1))
    while pend:
        time.sleep(8)
        for i, t in list(pend.items()):
            d = pedir(f"{API}/{t}", clave)["data"]
            if d["status"] == "COMPLETED":
                req = urllib.request.Request(d["generated"][0], headers={"User-Agent": UA})
                with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
                    (DIR / f"goma-v4-retoque{i}.png").write_bytes(r.read())
                print(f"listo retoque {i}", flush=True); del pend[i]
            elif d["status"] == "FAILED":
                print(f"falló {i}", flush=True); del pend[i]


if __name__ == "__main__":
    main()

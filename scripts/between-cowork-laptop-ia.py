#!/usr/bin/env python3
"""Agrega una LAPTOP ABIERTA a la mesa real del cowork de Between (ST col N, 16-09).

Por que
-------
Ronda 10: el cliente pidio foto real («podemos cambiar la imagen a una real de
cowork?») y el brief pide «notebook abierto + cafe Between + libreta». El
material real del cliente NO tiene ningun notebook fotografiado en el cowork:
los unicos fotogramas con notebook son del lounge del hotel, con caras
reconocibles. Eli resolvio antes ese mismo hueco con Magnific, y su edicion es
la referencia:

    raw/hilton/between/ediciones-ia-eli/magnific_agrega-una-laptop-en-la-m_*.png

Ahi hay una mesa de madera con un MacBook, el vaso Between REAL con arte latte
y comida, con follaje detras. Ese es el tratamiento que se calca.

⛔ EL ORDEN IMPORTA, y es la regla de la casa (memoria
`between-cumple-tecnica-eli`: «packshot real + fondo IA»):

    1. la IA trabaja sobre la base LIMPIA, sin el vaso;
    2. el vaso REAL se monta DESPUES con `between-montar-vaso.py`.

Asi el logotipo impreso del vaso no lo toca nunca el modelo. Mandar la pieza ya
compuesta es como el relight sobre el producto: preciosa la escena y destruido
el producto (ver `docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`, regla dura 1).

Se prueban los DOS caminos porque hacen cosas distintas:
  · `gemini-2-5-flash-image-preview` (Nano Banana) es imagen -> imagen: EDITA y
    respeta el encuadre. Es el que corresponde a «agrega X y no toques nada mas».
  · `text-to-image/nano-banana-pro` acepta hasta 14 referencias y es el que la
    tabla de decision manda cuando «la escena tiene que parecerse a una foto real
    del cliente». Se le pasan las DOS: la base y la edicion de Eli.

Uso:
    python scripts/between-cowork-laptop-ia.py
    python scripts/between-cowork-laptop-ia.py --solo edit
    python scripts/between-cowork-laptop-ia.py --solo pro
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import clave_freepik  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
BASE_LIMPIA = RAIZ / "public/assets/hilton/between/st-s3/st-16-09-cowork-real.jpg"
REF_ELI = (RAIZ / "raw/hilton/between/ediciones-ia-eli"
           / "magnific_agrega-una-laptop-en-la-m_iAi90W63uK.png")
SALIDA = RAIZ / "out/hilton/between/ia-cowork-laptop"

K = clave_freepik() or sys.exit("x falta la clave de Freepik — corre llavero.py abrir")
H = {"x-freepik-api-key": K, "Content-Type": "application/json"}

# El fix de certifi de la memoria `freepik-api-generacion-imagenes`.
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    SSL_CTX = ssl.create_default_context()

# ── EL PROMPT ──────────────────────────────────────────────────────────────
# Escrito en ingles porque los modelos de Freepik obedecen mejor, y con la lista
# de lo que NO se toca por delante: es lo que la tabla de decision exige para que
# la escena siga siendo la foto real del cliente.
NO_TOCAR = (
    "CRITICAL: keep the photograph exactly as it is. Do not change the framing, "
    "the camera angle, the perspective, the focal length or the crop. Do not "
    "change or redraw the architecture, the suspended ceiling, the recessed "
    "downlights, the arched floor lamp with its woven shade, the framed black "
    "and white city photographs, the dark vertical slat wall, the armchairs, the "
    "banquette, the side console, the carpet or the wooden table itself. Keep the "
    "exact wood grain, colour and knots of the table. Keep the existing lighting, "
    "white balance, contrast and the shallow depth of field of the background. "
    "Add no text, no logos, no brand names and no watermarks."
)

PROMPT_LAPTOP = (
    "Add ONE open laptop standing on the wooden table in the foreground, on the "
    "LEFT side of the table, and a small closed notebook with a pen next to it. "
    "The laptop is a modern thin aluminium laptop in dark space grey, matte "
    "finish, lid open at a natural working angle, seen from a rear three-quarter "
    "view so the back of the screen faces the camera; the screen glow is subtle "
    "and no interface or text is visible. It sits flat on the table, in the same "
    "perspective as the table surface, with a soft realistic contact shadow. "
    "The laptop must be lit by the SAME light as the room: the warm highlight "
    "comes from the RIGHT, so its right edge is brighter and its shadow falls to "
    "the left. Match the sharpness of the table: the laptop is close to the "
    "camera so it is in focus, but it must not look sharper or more contrasted "
    "than the wood it rests on. Leave the RIGHT HALF of the table empty. "
    "Leave the whole upper half of the image untouched and free of new objects. "
    + NO_TOCAR
)


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
    if not task_id:
        return None
    for _ in range(90):
        st, data = http(f"{base}/{task_id}")
        d = data.get("data", {}) if isinstance(data, dict) else {}
        if d.get("status") in ("COMPLETED", "SUCCESS"):
            return dig(data, True) or dig(data, False)
        if d.get("status") == "FAILED":
            print("    x fallo: " + json.dumps(data)[:300])
            return None
        time.sleep(5)
    print("    x timeout de " + etiqueta)
    return None


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def mime(p: Path) -> str:
    return "image/png" if p.suffix.lower() == ".png" else "image/jpeg"


def guardar(resultado, destino: Path) -> bool:
    if not resultado:
        return False
    destino.parent.mkdir(parents=True, exist_ok=True)
    if resultado.startswith("http"):
        with urllib.request.urlopen(resultado, timeout=300, context=SSL_CTX) as r:
            destino.write_bytes(r.read())
    else:
        destino.write_bytes(base64.b64decode(resultado))
    kb = destino.stat().st_size // 1024
    if kb < 20:
        print("    x " + destino.name + " pesa %d KB — sospechoso, se descarta" % kb)
        destino.unlink()
        return False
    print("    OK " + destino.name + " (%d KB)" % kb)
    return True


def via_edicion():
    """Nano Banana imagen -> imagen. El que respeta el encuadre."""
    base = "https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
    st, data = http(base, "POST", {
        "prompt": PROMPT_LAPTOP,
        "reference_images": [b64(BASE_LIMPIA)],
        "aspect_ratio": "social_story_9_16",
    })
    print("  nano-banana (edicion, 1 ref) -> HTTP %s" % st)
    if st not in (200, 201):
        print("  " + json.dumps(data)[:400])
        return None
    return poll(base, data.get("data", {}).get("task_id"), "edicion")


def via_pro():
    """Nano Banana Pro con la base Y la edicion de Eli como referencias."""
    base = "https://api.freepik.com/v1/ai/text-to-image/nano-banana-pro"
    refs = [BASE_LIMPIA]
    if REF_ELI.exists():
        refs.append(REF_ELI)
    else:
        print("  ! no encuentro la referencia de Eli: " + REF_ELI.name)
    prompt = PROMPT_LAPTOP + (
        " The FIRST reference image is the photograph to keep. The SECOND "
        "reference image shows how this brand photographs a laptop on a wooden "
        "cafe table: copy that laptop's material, colour, scale relative to the "
        "table and its warm natural-light treatment, but nothing else from it — "
        "do not copy its background, its foliage, its food, its plates, its "
        "phone or its sunglasses."
    ) if len(refs) == 2 else PROMPT_LAPTOP
    st, data = http(base, "POST", {
        "prompt": prompt,
        "aspect_ratio": "9:16",
        "resolution": "4K",
        "reference_images": [{"image": b64(r), "mime_type": mime(r)} for r in refs],
    })
    print("  nano-banana-pro (%d refs, 4K) -> HTTP %s" % (len(refs), st))
    if st not in (200, 201):
        print("  " + json.dumps(data)[:400])
        return None
    return poll(base, data.get("data", {}).get("task_id"), "pro")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", choices=["edit", "pro"], help="correr solo un camino")
    a = ap.parse_args()

    if not BASE_LIMPIA.exists():
        sys.exit("x no encuentro la base limpia: " + str(BASE_LIMPIA))
    print("base    : %s" % BASE_LIMPIA.name)
    print("refEli  : %s" % (REF_ELI.name if REF_ELI.exists() else "(falta)"))
    print("salida  : %s" % SALIDA)
    print()

    if a.solo != "pro":
        guardar(via_edicion(), SALIDA / "laptop-edicion.png")
    if a.solo != "edit":
        guardar(via_pro(), SALIDA / "laptop-pro.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())

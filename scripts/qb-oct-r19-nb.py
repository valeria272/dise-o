# -*- coding: utf-8 -*-
"""QB · octubre r19 — edición puntual de una foto con Nano Banana Pro (Freepik).

Uso:
    python scripts/qb-oct-r19-nb.py <entrada> <salida-base> <aspecto> "<prompt>" [n] [ref2 ref3 ...]

Genera n variantes (<salida-base>-v1.jpg, -v2…) a 4K con la entrada como primera
referencia. Después el cambio se INJERTA sobre la foto original (sólo la zona
pedida), para que el resto de la foto aprobada no se mueva ([[foto-aprobada-no-se-retoca]]).
"""
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
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    SSL_CTX = ssl.create_default_context()

K = clave_freepik() or sys.exit("x falta la clave de Freepik — corre llavero.py abrir")
H = {"x-freepik-api-key": K, "Content-Type": "application/json"}
BASE = "https://api.freepik.com/v1/ai/text-to-image/nano-banana-pro"


def http(url, method="GET", body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=H, method=method)
    try:
        with urllib.request.urlopen(req, timeout=300, context=SSL_CTX) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw.decode(errors="ignore")


def url_de(obj):
    if isinstance(obj, str):
        return obj if obj.startswith("http") else None
    for v in (obj.values() if isinstance(obj, dict) else obj if isinstance(obj, list) else []):
        u = url_de(v)
        if u:
            return u
    return None


def ref(p):
    p = Path(p)
    return {"image": base64.b64encode(p.read_bytes()).decode(),
            "mime_type": "image/png" if p.suffix.lower() == ".png" else "image/jpeg"}


def main():
    ent, sal, asp, prompt = sys.argv[1:5]
    n = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    extra = sys.argv[6:]
    assert len(prompt) <= 3000
    tareas = []
    for i in range(n):
        st, d = http(BASE, "POST", {"prompt": prompt, "aspect_ratio": asp, "resolution": "4K",
                                    "reference_images": [ref(ent)] + [ref(x) for x in extra]})
        print("v%d -> HTTP %s" % (i + 1, st))
        if st not in (200, 201):
            print(json.dumps(d)[:400])
            continue
        tareas.append((i + 1, d["data"]["task_id"]))
    for i, t in tareas:
        for _ in range(120):
            st, d = http("%s/%s" % (BASE, t))
            s = (d.get("data") or {}).get("status") if isinstance(d, dict) else None
            if s in ("COMPLETED", "SUCCESS"):
                u = url_de(d.get("data", {}).get("generated", d))
                dest = Path("%s-v%d.jpg" % (sal, i))
                dest.parent.mkdir(parents=True, exist_ok=True)
                with urllib.request.urlopen(u, timeout=300, context=SSL_CTX) as r:
                    dest.write_bytes(r.read())
                print("OK", dest)
                break
            if s == "FAILED":
                print("x v%d falló" % i)
                break
            time.sleep(5)


if __name__ == "__main__":
    main()

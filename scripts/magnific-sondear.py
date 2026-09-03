#!/usr/bin/env python3
"""¿Qué modelos de Magnific/Freepik tiene realmente nuestra cuenta? — SIN gastar créditos.

Correr esto cuando cambie el plan, o antes de decirle a alguien «no se puede».
Lo que reporta queda documentado en `docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md`.

CÓMO SONDEA (dos trampas, las dos pisadas el 28-08-2026)
--------------------------------------------------------
Se manda un **POST con cuerpo vacío**: si el endpoint existe, la API contesta
`400 Validation error` quejándose del campo que falta; si no existe, `404`.
No genera nada, así que no cuesta créditos.

1. ⛔ **GET no sirve.** Parece la vía limpia, pero esta API devuelve `404` (no
   `405`) en las rutas que solo aceptan POST — así que marcaba como ausentes
   `image-upscaler` y Nano Banana, que usamos todos los días.
2. ⛔ **`mystic` no se sondea.** Con cuerpo vacío devuelve `200`: acepta la tarea
   y **consume un crédito**. Se descubrió gastando uno. Va en la lista de saltados.

Uso:
    python3 scripts/magnific-sondear.py
"""
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

import certifi

BASE = "https://api.freepik.com"      # api.magnific.com responde igual
CTX = ssl.create_default_context(cafile=certifi.where())
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Lo que usamos hoy + lo que ofrece el catálogo público de Magnific.
MODELOS = [
    # ── VIDEO (agregado 03-09-2026: el sondeo anterior no miraba video) ────────
    ("image-to-video/pixverse-v5-transition", "VIDEO · PRIMER Y ÚLTIMO FOTOGRAMA ⭐"),
    ("image-to-video/pixverse-v5",            "VIDEO · Pixverse v5"),
    ("image-to-video/kling-v2-1-pro",         "VIDEO · Kling 2.1 pro"),
    ("image-to-video/kling-v2-1-master",      "VIDEO · Kling 2.1 master"),
    ("image-to-video/kling-v2-5-pro",         "VIDEO · Kling 2.5 pro"),
    ("image-to-video/minimax-hailuo-02-1080p","VIDEO · Hailuo 02 1080p"),
    ("image-to-video/wan-v2-2-720p",          "VIDEO · Wan 2.2 720p"),
    ("text-to-image/seedream-v4",             "IMAGEN · Seedream 4"),
    ("text-to-image/seedream-v4-edit",        "IMAGEN · Seedream 4 edit"),
    ("text-to-image/flux-dev",                "IMAGEN · Flux dev"),
    ("text-to-image/hyperflux",               "IMAGEN · HyperFlux"),
    ("image-expand/flux-pro",                 "EDICIÓN · outpaint"),

    ("mystic",                          "texto→imagen 2K"),
    ("gemini-2-5-flash-image-preview",  "Nano Banana · imagen→imagen"),
    ("image-upscaler",                  "escalado creativo"),
    ("image-upscaler-precision",        "escalado sin reinventar detalle"),
    ("image-relight",                   "reiluminar escena"),
    ("image-style-transfer",            "copiar look de una referencia"),
    ("text-to-image/nano-banana-pro",   "Gemini 3 Pro · texto legible + 4K"),
    ("seedream-v4-5",                   "Seedream 4.5"),
    ("flux-2-pro",                      "Flux 2 Pro"),
    ("flux-2-turbo",                    "Flux 2 Turbo"),
    ("flux-dev",                        "Flux Dev"),
    ("hyperflux",                       "Hyperflux"),
    ("remove-background",               "recorte automático"),
]


def clave():
    f = os.path.join(os.path.expanduser("~"), ".magnific_key")
    if os.path.isfile(f):
        k = open(f).read().strip()
        if k:
            return k
    env = os.path.join(os.path.dirname(RAIZ), "ASISTENTE PERSONAL", ".env")
    if os.path.isfile(env):
        for l in open(env, encoding="utf-8").read().splitlines():
            m = re.match(r"\s*FREEPIK_API_KEY\s*=\s*(.+)", l)
            if m:
                return m.group(1).strip().strip('"').strip("'")
    sys.exit("✗ No encuentro la clave (~/.magnific_key o FREEPIK_API_KEY en el .env)")


# Sondearlos cuesta un crédito (ver arriba). Los usamos a diario: existen.
SALTAR = {"mystic"}
# Endpoints que son GET por naturaleza: con POST devuelven 404 y parecen ausentes.
SOLO_GET = {"loras": "estilos entrenados de la cuenta"}


def main():
    k = clave()
    tengo, no_tengo = [], []
    print(f"{'modelo':<34} {'':4} qué es")
    print("-" * 78)
    for ruta, desc in list(SOLO_GET.items()) + MODELOS:
        if ruta in SOLO_GET:
            req = urllib.request.Request(f"{BASE}/v1/ai/{ruta}", method="GET",
                                         headers={"x-freepik-api-key": k})
            try:
                urllib.request.urlopen(req, context=CTX, timeout=25)
                ok = True
            except urllib.error.HTTPError as e:
                ok = e.code != 404   # 502/503 = la ruta EXISTE y el proveedor está ocupado
            (tengo if ok else no_tengo).append(ruta)
            print(f"{ruta:<34} {'✅' if ok else '❌':4} {desc}  (se consulta con GET)")
            continue
        if ruta in SALTAR:
            tengo.append(ruta)
            print(f"{ruta:<34} {'✅':4} {desc}  (en uso; no se sondea)")
            continue
        req = urllib.request.Request(f"{BASE}/v1/ai/{ruta}", data=b"{}", method="POST",
                                     headers={"x-freepik-api-key": k,
                                              "Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req, context=CTX, timeout=30)
            ok = True                      # 200: aceptó — ojo, pudo encolar
            desc += "  ⚠️ aceptó el POST: pudo consumir un crédito"
        except urllib.error.HTTPError as e:
            ok = e.code != 404   # 502/503 = la ruta EXISTE y el proveedor está ocupado             # 400/401/403 → el endpoint existe
        except Exception as e:
            print(f"{ruta:<34} {'—':4} red: {type(e).__name__}")
            continue
        (tengo if ok else no_tengo).append(ruta)
        print(f"{ruta:<34} {'✅' if ok else '❌':4} {desc}")

    print(f"\nDisponibles: {len(tengo)} · Fuera del plan: {len(no_tengo)}")
    if no_tengo:
        print("Fuera del plan → " + ", ".join(no_tengo))
        print("(el acceso por API a esos modelos está en el plan Pro de Magnific)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

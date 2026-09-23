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
import time

BASE = "https://api.freepik.com"      # api.magnific.com responde igual

# ⛔ El WAF de Freepik BLOQUEA el User-Agent por defecto de urllib
# ("Python-urllib/3.10"): devuelve 403 "Penalty Box for WAF" a todos los POST,
# mientras el mismo request con un UA normal pasa. Verificado el 08-09-2026.
# Y como el sondeo trata 403 como "existe", sin esto marcaría TODO como disponible.
UA = "copylab-estudio/1.0 (+https://copywriters.cl)"
CTX = ssl.create_default_context(cafile=certifi.where())
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Catálogo completo de docs.magnific.com/llms.txt (traído el 08-09-2026) + las rutas
# viejas que usan los scripts del estudio. Magnific RENOMBRÓ endpoints: se sondean las
# dos formas para saber cuál sigue viva antes de tocar un script de producción.
MODELOS = [
    # ── TEXTO → IMAGEN ────────────────────────────────────────────────────────
    ("text-to-image/nano-banana-pro",        "IMAGEN · Gemini 3 Pro · texto legible + 4K ⭐"),
    ("gemini-2-5-flash-image-preview",       "IMAGEN · Nano Banana · imagen→imagen"),
    ("text-to-image/seedream-v5-pro",        "IMAGEN · Seedream 5 Pro ⭐ (generador por defecto)"),
    ("text-to-image/seedream-v5-pro-edit",   "EDICIÓN · Seedream 5 Pro edit (con referencias) ⭐"),
    ("text-to-image/seedream-v5-lite",       "IMAGEN · Seedream 5 Lite"),
    ("text-to-image/seedream-4",             "IMAGEN · Seedream 4"),
    ("text-to-image/seedream-4-5",           "IMAGEN · Seedream 4.5"),
    ("text-to-image/seedream-v4",            "IMAGEN · Seedream 4 (ruta vieja)"),
    ("text-to-image/z-image-turbo",          "IMAGEN · Z-Image Turbo"),
    ("text-to-image/flux-2-pro",             "IMAGEN · Flux 2 Pro"),
    ("text-to-image/flux-2-turbo",           "IMAGEN · Flux 2 Turbo"),
    ("text-to-image/flux-2-klein",           "IMAGEN · Flux 2 Klein"),
    ("text-to-image/flux-kontext-pro",       "IMAGEN · Flux Kontext Pro"),
    ("text-to-image/flux-pro-v1-1",          "IMAGEN · Flux Pro 1.1"),
    ("text-to-image/flux-dev",               "IMAGEN · Flux Dev"),
    ("text-to-image/hyperflux",              "IMAGEN · HyperFlux"),
    ("text-to-image/runway",                 "IMAGEN · Runway texto→imagen"),
    ("text-to-icon",                         "IMAGEN · iconos"),

    # ── EDICIÓN DE IMAGEN ─────────────────────────────────────────────────────
    ("image-editing/seedream-4-5-edit",      "EDICIÓN · Seedream 4.5 edit (por instrucción)"),
    ("text-to-image/seedream-v4-edit",       "EDICIÓN · Seedream 4 edit (ruta vieja)"),
    ("image-upscaler/creative",              "EDICIÓN · escalado creativo"),
    ("image-upscaler/precision",             "EDICIÓN · escalado que NO reinventa detalle ⭐"),
    ("image-upscaler",                       "EDICIÓN · escalado (ruta vieja, en uso)"),
    ("image-upscaler-precision",             "EDICIÓN · precision (ruta vieja, en uso)"),
    ("relight",                              "EDICIÓN · reiluminar escena"),
    ("image-relight",                        "EDICIÓN · relight (ruta vieja, en uso)"),
    ("style-transfer",                       "EDICIÓN · copiar el look de una referencia"),
    ("image-style-transfer",                 "EDICIÓN · style transfer (ruta vieja, en uso)"),
    ("remove-background",                    "EDICIÓN · recorte automático"),
    ("beta/image-remove-background",         "EDICIÓN · recorte (ruta vieja, en uso)"),
    ("image-expand",                         "EDICIÓN · outpaint / ampliar encuadre"),
    ("image-expand/flux-pro",                "EDICIÓN · outpaint (ruta vieja)"),

    # ── IMAGEN → VIDEO ────────────────────────────────────────────────────────
    ("image-to-video/kling-2-6-pro",         "VIDEO · Kling 2.6 Pro"),
    ("image-to-video/kling-2-5-pro",         "VIDEO · Kling 2.5 Pro"),
    ("image-to-video/kling-2-1-pro",         "VIDEO · Kling 2.1 Pro"),
    ("image-to-video/kling-motion",          "VIDEO · Kling 2.6 control de movimiento ⭐"),
    ("image-to-video/kling-o1-pro",          "VIDEO · Kling O1 Pro"),
    ("image-to-video/kling-v2-1-pro",        "VIDEO · Kling 2.1 pro (ruta vieja, en uso)"),
    ("image-to-video/kling-v2-1-master",     "VIDEO · Kling 2.1 master (ruta vieja)"),
    ("image-to-video/kling-v2-5-pro",        "VIDEO · Kling 2.5 pro (ruta vieja)"),
    ("image-to-video/seedance-pro-1080p",    "VIDEO · Seedance Pro 1080p"),
    ("image-to-video/wan-2-6-1080p",         "VIDEO · WAN 2.6 1080p"),
    ("image-to-video/wan-2-5-i2v-1080p",     "VIDEO · WAN 2.5 imagen→video"),
    ("image-to-video/wan-v2-2-720p",         "VIDEO · Wan 2.2 720p (ruta vieja)"),
    ("image-to-video/minimax-hailuo-2-3-1080p", "VIDEO · Hailuo 2.3 1080p"),
    ("image-to-video/minimax-hailuo-02-1080p",  "VIDEO · Hailuo 02 1080p"),
    ("image-to-video/minimax-video-01-live", "VIDEO · Video-01-Live (anima ilustración)"),
    ("image-to-video/runway-gen4-turbo",     "VIDEO · Runway Gen-4 Turbo"),
    ("image-to-video/runway-act-two",        "VIDEO · Runway Act-Two (actuación) ⭐"),
    ("image-to-video/pixverse",              "VIDEO · PixVerse V5"),
    ("image-to-video/pixverse-v5",           "VIDEO · PixVerse V5 (ruta vieja)"),
    ("image-to-video/pixverse-v5-transition","VIDEO · PRIMER Y ÚLTIMO FOTOGRAMA ⭐"),
    ("video/omni-human-1-5",                 "VIDEO · OmniHuman 1.5 (avatar que habla) ⭐"),
    ("video/vfx",                            "VIDEO · efectos VFX sobre un clip"),

    # ── TEXTO → VIDEO ─────────────────────────────────────────────────────────
    ("text-to-video/ltx-2-pro",              "VIDEO · LTX 2.0 Pro (texto→video)"),
    ("text-to-video/wan-2-5-t2v-1080p",      "VIDEO · WAN 2.5 (texto→video)"),

    # ── AUDIO ─────────────────────────────────────────────────────────────────
    ("music-generation",                     "AUDIO · música original ⭐"),
    ("sound-effects",                        "AUDIO · efectos de sonido ⭐"),
    ("audio-isolation",                      "AUDIO · aislar voz del ruido"),
    ("text-to-speech",                       "AUDIO · voz (ruta estable)"),
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


# Sondearlos CUESTA UN CRÉDITO: con cuerpo vacío devuelven 200 (aceptan la tarea)
# en vez de 400. Los cinco de abajo se descubrieron a la mala en el sondeo del
# 08-09-2026 — existen, están confirmados, y no se vuelven a golpear.
SALTAR = {
    "mystic",
    "text-to-image/seedream-v4",
    "text-to-image/seedream-v4-edit",
    "text-to-image/flux-pro-v1-1",
    "text-to-image/hyperflux",
    "image-to-video/kling-v2-5-pro",
}
# Endpoints que son GET por naturaleza: con POST devuelven 404 y parecen ausentes.
SOLO_GET = {"loras": "estilos entrenados de la cuenta"}


def main():
    k = clave()
    tengo, no_tengo = [], []
    print(f"{'modelo':<42} {'':4} qué es")
    print("-" * 78)
    for ruta, desc in list(SOLO_GET.items()) + MODELOS:
        if ruta in SOLO_GET:
            req = urllib.request.Request(f"{BASE}/v1/ai/{ruta}", method="GET",
                                         headers={"x-freepik-api-key": k, "User-Agent": UA})
            try:
                urllib.request.urlopen(req, context=CTX, timeout=25)
                ok = True
            except urllib.error.HTTPError as e:
                ok = e.code != 404   # 502/503 = la ruta EXISTE y el proveedor está ocupado
            (tengo if ok else no_tengo).append(ruta)
            print(f"{ruta:<42} {'✅' if ok else '❌':4} {desc}  (se consulta con GET)")
            continue
        if ruta in SALTAR:
            tengo.append(ruta)
            print(f"{ruta:<42} {'✅':4} {desc}  (en uso; no se sondea)")
            continue
        req = urllib.request.Request(f"{BASE}/v1/ai/{ruta}", data=b"{}", method="POST",
                                     headers={"x-freepik-api-key": k,
                                              "Content-Type": "application/json",
                                              "User-Agent": UA})
        try:
            urllib.request.urlopen(req, context=CTX, timeout=30)
            ok = True                      # 200: aceptó — ojo, pudo encolar
            desc += "  ⚠️ aceptó el POST: pudo consumir un crédito"
        except urllib.error.HTTPError as e:
            if e.code == 403 and "Penalty Box" in e.read()[:400].decode("utf-8", "replace"):
                sys.exit("\n⛔ WAF: 403 penalty box. Dos causas, en este orden:\n"
                         "   1. falta el User-Agent (urllib por defecto está vetado) — ver UA arriba;\n"
                         "   2. se mandó un cuerpo mal formado y la IP quedó castigada ~10 min.\n"
                         "   Sondea SIEMPRE con b'{}' y con UA propio.")
            ok = e.code != 404   # 502/503 = la ruta EXISTE y el proveedor está ocupado
                                 # 400/401/403 → el endpoint existe
        except Exception as e:
            print(f"{ruta:<42} {'—':4} red: {type(e).__name__}")
            continue
        (tengo if ok else no_tengo).append(ruta)
        print(f"{ruta:<42} {'✅' if ok else '❌':4} {desc}", flush=True)
        time.sleep(0.7)   # el WAF se despierta con ráfagas

    print(f"\nDisponibles: {len(tengo)} · Fuera del plan: {len(no_tengo)}")
    if no_tengo:
        print("Fuera del plan → " + ", ".join(no_tengo))
        print("(el acceso por API a esos modelos está en el plan Pro de Magnific)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

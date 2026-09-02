#!/usr/bin/env python3
"""Magnific / Freepik — image-to-video. El motor de animación del estudio.

    python3 scripts/magnific-video.py <imagen.jpg> --out clip.mp4 \
        --prompt "<qué pasa en el plano>" [--dur 5] [--modelo kling-v2-1-pro]

POR QUÉ EXISTE (02-09-2026): el pipeline de video de G.CL se dio por bloqueado
meses porque Higgsfield quedó en 0,43 créditos. **La misma clave de Magnific
hace video** — sólo image-to-video, que es justo lo que pide el protocolo de
consistencia del personaje (candado 4: nunca text-to-video, siempre desde un
keyframe aprobado).

Modelos que tiene el plan (sondeados con POST vacío):
  kling-v2-1-pro · kling-v2-1-master · kling-v2 · minimax-hailuo-02-768p/1080p
  wan-v2-2-720p · pixverse-v5 · pixverse-v5-transition
No hay text-to-video ni Veo3 en el plan.

REGLA DEL PLANO (aprendida en el R01): un movimiento de cámara y un microgesto
por clip, nada más. Y **vigilar que el personaje no gire y pierda el visor** —
Kling lo hizo girar de espaldas a partir del segundo 2,2 y hubo que ralentizar
el plano entero para salvarlo.
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

import certifi

BASE = "https://api.freepik.com/v1/ai"
CTX = ssl.create_default_context(cafile=certifi.where())

# ⚠️ Kling en Freepik NO acepta `negative_prompt`: mandarlo devuelve 404 «Not
# found», que parece un problema de ruta y no lo es. Lo que se quiere evitar va
# redactado en positivo dentro del propio prompt.
NEGATIVO_EN_EL_PROMPT = (
    "minimal controlled motion, no camera shake, the character stays facing "
    "camera the whole time and never turns away, consistent shape, no morphing"
)


def clave():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _entorno import clave_freepik
    return clave_freepik()


def pedir(ruta, cuerpo=None, metodo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(
        BASE + ruta, data=datos, method=metodo or ("POST" if datos else "GET"),
        headers={"x-freepik-api-key": clave(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"✗ HTTP {e.code}: {e.read().decode()[:600]}")


def ruta_consulta(modelo):
    """⚠️ La trampa de esta API: se ENVÍA a `kling-v2-1-pro` pero se CONSULTA en
    `kling-v2-1` — la familia, sin el nivel. Preguntar por la misma ruta del POST
    devuelve 404 «Not found», que parece que el modelo no existe y no es eso.
    Descubierto el 02-09-2026 probando rutas a mano."""
    for nivel in ("-pro", "-master", "-std"):
        if modelo.endswith(nivel):
            return f"/image-to-video/{modelo[: -len(nivel)]}"
    return f"/image-to-video/{modelo}"


def espera(ruta, task_id, minutos=15):
    """Kling se demora bastante más que una imagen: 3–8 minutos por clip."""
    limite = time.time() + minutos * 60
    ultimo = ""
    while time.time() < limite:
        r = pedir(f"{ruta}/{task_id}")["data"]
        estado = r.get("status")
        if estado != ultimo:
            print(f"  … {estado}")
            ultimo = estado
        if estado == "COMPLETED":
            return r.get("generated") or []
        if estado in ("FAILED", "ERROR"):
            sys.exit(f"✗ la tarea terminó en {estado}: {json.dumps(r)[:400]}")
        time.sleep(15)
    sys.exit("✗ se acabó el tiempo de espera")


def guarda(urls, destino):
    if not urls:
        sys.exit("✗ la tarea no devolvió ningún video")
    os.makedirs(os.path.dirname(os.path.abspath(destino)) or ".", exist_ok=True)
    with urllib.request.urlopen(urls[0], context=CTX, timeout=300) as r:
        open(destino, "wb").write(r.read())
    print(f"  ✓ {destino}  ({os.path.getsize(destino)//1024} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("imagen")
    ap.add_argument("--out", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--dur", default="5", choices=["5", "10"])
    ap.add_argument("--modelo", default="kling-v2-1-pro")
    a = ap.parse_args()

    if not os.path.isfile(a.imagen):
        sys.exit(f"✗ No encuentro la imagen: {a.imagen}")
    # La imagen se manda reducida: el keyframe de 1536×2752 son 471 KB en base64
    # y no hace falta — Kling entrega 1080p igual. Payload chico = menos fallas.
    from PIL import Image
    import io
    im = Image.open(a.imagen).convert("RGB")
    im.thumbnail((720, 1280))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    ruta = f"/image-to-video/{a.modelo}"
    cuerpo = {
        "image": base64.b64encode(buf.getvalue()).decode(),
        "prompt": a.prompt + ". " + NEGATIVO_EN_EL_PROMPT,
        "duration": a.dur,
    }
    print(f"→ {a.modelo} · {a.dur}s · {os.path.basename(a.imagen)}")
    r = pedir(ruta, cuerpo)
    guarda(espera(ruta_consulta(a.modelo), r["data"]["task_id"]), a.out)


if __name__ == "__main__":
    sys.exit(main())

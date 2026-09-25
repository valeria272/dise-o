#!/usr/bin/env python3
"""Magnific / Freepik — image-to-video. El motor de animación del estudio.

    python3 scripts/magnific-video.py <imagen.jpg> --out clip.mp4 \
        --prompt "<qué pasa en el plano>" [--dur 5] [--modelo kling-v2-1-pro]

POR QUÉ EXISTE (02-09-2026): el pipeline de video de G.CL se dio por bloqueado
meses porque Higgsfield quedó en 0,43 créditos. **La misma clave de Magnific
hace video** — sólo image-to-video, que es justo lo que pide el protocolo de
consistencia del personaje (candado 4: nunca text-to-video, siempre desde un
keyframe aprobado).

Modelos que tiene el plan (sondeados con POST vacío el 04-09-2026):
  kling-v2-1-pro ⭐ · kling-v2-5-pro · kling-v2-1-master · kling-v2 · kling-std
  kling-elements-pro · minimax-hailuo-02-768p/1080p · wan-v2-2-720p
  pixverse-v5 · pixverse-v5-transition
NO existen: minimax-h3, seedance-pro-1080p, vidu-q1 (404).

⭐ EL FRAME FINAL — lo que desbloqueó el Cap. 02 (04-09-2026)
`--fin` manda `image_tail`: el plano TERMINA en el keyframe que tú elijas, no
donde el modelo quiera. Es la diferencia entre 8 clips sueltos y una escena.

⚠️ **Quién lo acepta de verdad** (probado a mano, no deducido): el validador de
Freepik acepta el CAMPO en toda la familia kling y después el modelo lo rechaza.

  kling-v2-1-pro           ✅  ← el que se usa. base64, sin hosting
  kling-v2                 ✅
  minimax-hailuo-02-1080p  ✅  pero se llama `last_frame_image` y sólo hace 6 s
  kling-v2-5-pro           ❌  «Image tail is not allowed» — el modelo nuevo lo perdió
  kling-v2-1-master        ❌  «not supported yet»
  pixverse-v5-transition   ✅  pero exige URLs PÚBLICAS, no base64

Por eso el default de este script es `kling-v2-1-pro` y no el modelo más nuevo:
el frame final vale más que la mejora de motor.

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

# ⚠️ Windows: la consola escribe en cp1252 y el «→» del primer print reventaba con
# UnicodeEncodeError ANTES de llamar a la API (24-09-2026, story animada de EBEMA).
# Mismo arreglo que magnific.py.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = "https://api.freepik.com/v1/ai"
CTX = ssl.create_default_context(cafile=certifi.where())

# ⚠️ Kling en Freepik NO acepta `negative_prompt`: mandarlo devuelve 404 «Not
# found», que parece un problema de ruta y no lo es. Lo que se quiere evitar va
# redactado en positivo dentro del propio prompt.
NEGATIVO_EN_EL_PROMPT = (
    "minimal controlled motion, no camera shake, the character stays facing "
    "camera the whole time and never turns away, consistent shape, no morphing"
)

# ⚠️ Esa coda es la del plano quieto. En un plano donde el personaje SÍ tiene que
# salir de cuadro (el rewind del Cap. 02) se contradice con el prompt y el modelo
# resuelve el conflicto por su cuenta. Por eso se puede reemplazar con `--coda`.
CODA_FISICA = (
    "real physics with natural weight and inertia, locked-off camera unless the "
    "prompt asks for a move, consistent character shape, no morphing, no flickering"
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


# ⚠️ Y la trampa NO es uniforme: `kling-v2-5-pro` se consulta en su ruta COMPLETA.
# Si se le quita el `-pro` como a la v2.1, devuelve 404 y parece que el modelo no
# existe. Verificado a mano el 04-09-2026.
CONSULTA_RUTA_ENTERA = {"kling-v2-5-pro"}


def ruta_consulta(modelo):
    """⚠️ La trampa de esta API: se ENVÍA a `kling-v2-1-pro` pero se CONSULTA en
    `kling-v2-1` — la familia, sin el nivel. Preguntar por la misma ruta del POST
    devuelve 404 «Not found», que parece que el modelo no existe y no es eso.
    Descubierto el 02-09-2026 probando rutas a mano."""
    if modelo in CONSULTA_RUTA_ENTERA:
        return f"/image-to-video/{modelo}"
    for nivel in ("-pro", "-master", "-std"):
        if modelo.endswith(nivel):
            return f"/image-to-video/{modelo[: -len(nivel)]}"
    return f"/image-to-video/{modelo}"


def a_base64(ruta):
    """La imagen se manda reducida: el keyframe de 1536×2752 son 471 KB en base64
    y no hace falta — Kling entrega 1080p igual. Payload chico = menos fallas."""
    import io
    from PIL import Image
    im = Image.open(ruta).convert("RGB")
    im.thumbnail((720, 1280))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    return base64.b64encode(buf.getvalue()).decode()


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
    ap.add_argument("--fin", help="keyframe FINAL del plano (image_tail). El plano "
                                  "termina exactamente ahí — sólo kling")
    ap.add_argument("--coda", default=NEGATIVO_EN_EL_PROMPT,
                    help="coda de control. 'fisica' para planos con movimiento real")
    ap.add_argument("--dur", default="5", choices=["5", "10"])
    ap.add_argument("--modelo", default="kling-v2-1-pro")
    ap.add_argument("--tarea", help="task_id de un trabajo ya lanzado: no manda nada "
                                    "nuevo, sólo espera y baja el video (24-09: Kling "
                                    "tardó más de 15 min y el trabajo quedó huérfano)")
    ap.add_argument("--minutos", type=int, default=15)
    a = ap.parse_args()

    if a.tarea:
        guarda(espera(ruta_consulta(a.modelo), a.tarea, a.minutos), a.out)
        return

    if not os.path.isfile(a.imagen):
        sys.exit(f"✗ No encuentro la imagen: {a.imagen}")
    ruta = f"/image-to-video/{a.modelo}"
    cuerpo = {
        "image": a_base64(a.imagen),
        "prompt": a.prompt + ". " + (CODA_FISICA if a.coda == "fisica" else a.coda),
        "duration": a.dur,
    }
    if a.fin:
        if not a.modelo.startswith("kling"):
            sys.exit(f"✗ --fin (image_tail) sólo lo aceptan los modelos kling; "
                     f"{a.modelo} no. Usa kling-v2-5-pro.")
        if not os.path.isfile(a.fin):
            sys.exit(f"✗ No encuentro el keyframe final: {a.fin}")
        cuerpo["image_tail"] = a_base64(a.fin)
    fin = f" → {os.path.basename(a.fin)}" if a.fin else ""
    print(f"→ {a.modelo} · {a.dur}s · {os.path.basename(a.imagen)}{fin}")
    r = pedir(ruta, cuerpo)
    tid = r["data"]["task_id"]
    print(f"  tarea {tid}  (si se corta la espera: --tarea {tid})", flush=True)
    guarda(espera(ruta_consulta(a.modelo), tid, a.minutos), a.out)


if __name__ == "__main__":
    sys.exit(main())

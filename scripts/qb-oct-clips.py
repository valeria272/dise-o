#!/usr/bin/env python3
"""
QB · GRILLA OCTUBRE 2026 — clips de video (image-to-video) para las ST animadas.

Mismo aparato que `scripts/gcl-r02-clips.py` (Kling 2.1 Pro por la API de
Freepik): se mandan todos los clips de una y después se consulta, porque Kling
tarda 3–8 minutos por clip y en serie el lote se hace eterno.

⚠️ Se ENVÍA a `kling-v2-1-pro` y se CONSULTA en `kling-v2-1`: preguntar por la
ruta del POST devuelve 404 y parece que la tarea no existiera.
⚠️ `negative_prompt` NO existe en este endpoint (404): lo que se quiere evitar
va redactado en positivo dentro del prompt.

LA REGLA DEL PLANO: un movimiento de cámara y una acción por clip. Si el prompt
pide dos, Kling hace las dos a medias.

Todo lo que sale de acá es material NO real → la pieza lleva «Imagen
referencial» (pedido del cliente en la grilla de octubre, 22-10).

Uso:
    python scripts/qb-oct-clips.py                 # los que falten
    python scripts/qb-oct-clips.py --solo s22_e2
    python scripts/qb-oct-clips.py --rehacer
"""
import argparse
import base64
import io
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

import certifi

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRADA = os.path.join(RAIZ, "raw", "hilton", "qb", "oct-ia")
SALIDA = os.path.join(ENTRADA, "clips")
BASE = "https://api.freepik.com/v1/ai"
MODELO = "kling-v2-1-pro"
CTX = ssl.create_default_context(cafile=certifi.where())
UA = "copylab-estudio/1.0"   # el WAF de Freepik castiga el User-Agent de urllib

CONTROL = (
    " Realistic natural motion, cinematic, steady camera, the plate and the food "
    "keep exactly the same shape and ingredients, no morphing, no extra objects "
    "appearing, no text, no faces, only a hand and cutlery."
)

# clave → (imagen de arranque, prompt)
CLIPS = {
    # ST 22-10 · ENSALADA DE CAMARÓN PANKO — 4 escenas del brief
    "s22_e1": ("22-ensalada-A.png",
               "Very slow cinematic push-in towards the salad plate on the table, "
               "candle light flickering softly in the background."),
    "s22_e2": ("22-ensalada-A.png",
               "A woman's hand holding a silver fork enters the frame from the right "
               "and gently tosses the salad leaves on the plate. Static camera."),
    "s22_e3": ("22-ensalada-detalle.png",
               "Macro close-up: a fork slowly moves through the green leaves, crispy "
               "panko shrimp and mozzarella, the ingredients shift naturally. Static camera."),
    "s22_e4": ("22-ensalada-A.png",
               "A hand with a silver fork picks up a bite with green leaves, one crispy "
               "panko shrimp and a piece of mozzarella, and lifts it slowly out of the "
               "plate towards the camera. Static camera."),
}


def clave():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from _entorno import clave_freepik
    return clave_freepik()


def api(ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(
        BASE + ruta, data=datos, method="POST" if datos else "GET",
        headers={"x-freepik-api-key": clave(), "Content-Type": "application/json",
                 "User-Agent": UA})
    with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
        return json.loads(r.read())


def imagen_b64(ruta):
    """Reducida a 720 px de ancho: Kling entrega 1080p igual y el payload chico
    falla menos."""
    from PIL import Image
    im = Image.open(ruta).convert("RGB")
    im.thumbnail((720, 1280))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=92)
    return base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", nargs="*")
    ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--modelo", default=MODELO)
    a = ap.parse_args()
    os.makedirs(SALIDA, exist_ok=True)
    modelo = a.modelo

    tareas = {}
    for n in (a.solo or list(CLIPS)):
        img, prompt = CLIPS[n]
        destino = os.path.join(SALIDA, n + ".mp4")
        if os.path.exists(destino) and not a.rehacer:
            print(f"·  {n} ya está")
            continue
        ruta = os.path.join(ENTRADA, img)
        if not os.path.isfile(ruta):
            print(f"✗  {n}: falta {img}")
            continue
        cuerpo = {"image": imagen_b64(ruta), "prompt": prompt + CONTROL, "duration": "5"}
        try:
            r = api(f"/image-to-video/{modelo}", cuerpo)
            tareas[n] = r["data"]["task_id"]
            print(f"→  {n}  {tareas[n][:8]}")
        except urllib.error.HTTPError as e:
            print(f"✗  {n}: HTTP {e.code} {e.read().decode()[:200]}")

    # La ruta de consulta no siempre es la del POST: se prueban las dos.
    consultas = [f"/image-to-video/{modelo.rsplit('-', 1)[0]}", f"/image-to-video/{modelo}"]
    limite = time.time() + 40 * 60
    while tareas and time.time() < limite:
        time.sleep(20)
        for n in list(tareas):
            d = None
            for c in consultas:
                try:
                    d = api(f"{c}/{tareas[n]}")["data"]
                    break
                except Exception:
                    continue
            if d is None:
                continue
            if d["status"] == "COMPLETED" and d.get("generated"):
                destino = os.path.join(SALIDA, n + ".mp4")
                with urllib.request.urlopen(urllib.request.Request(
                        d["generated"][0], headers={"User-Agent": UA}),
                        context=CTX, timeout=300) as r:
                    open(destino, "wb").write(r.read())
                print(f"✓  {n}  ({os.path.getsize(destino)//1024} KB)")
                del tareas[n]
            elif d["status"] in ("FAILED", "ERROR"):
                print(f"✗  {n}: {d['status']} — {json.dumps(d)[:200]}")
                del tareas[n]
    if tareas:
        print(f"⏳ quedaron sin terminar: {', '.join(tareas)}")


if __name__ == "__main__":
    main()

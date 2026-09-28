#!/usr/bin/env python3
"""
DOUBLETREE · ST 01-10 FAMILY TIME (S1 octubre), ronda con la familia fija — clips.
Eli 28-09: «utiliza los nuevos personajes… las imágenes ya realizadas… vuélvelas
video para que se vea más realista, más bonito, más sutil».

Las fotos de arranque son las story 9:16 del banco aprobado el 25-09 (familia IA
sobre fotos REALES de DT, `out/hilton/dt/familia/entrega/`). Kling 2.1 Pro por la
API de Freepik, mismo aparato que `p18-oct-clips.py`.

REGLA DEL PLANO: un movimiento de cámara lento y un microgesto por clip. Nadie mira
a cámara y las caras no cambian (R-68/R-69 y checklist de realismo).

Uso:
    python scripts/dt-oct-ft-clips.py                 # los que falten
    python scripts/dt-oct-ft-clips.py --solo vista --rehacer
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
ENTRADA = os.path.join(RAIZ, "out", "hilton", "dt", "familia", "entrega")
SALIDA = os.path.join(RAIZ, "raw", "hilton", "dt", "oct-ft-video")
BASE = "https://api.freepik.com/v1/ai"
MODELO = "kling-v2-5-pro"   # 28-09: 2.1 Pro devolvía FAILED sin error; 2.5 Pro sí
CTX = ssl.create_default_context(cafile=certifi.where())
UA = "copylab-estudio/1.0"   # el WAF de Freepik castiga el User-Agent de urllib

CONTROL = (
    " Photorealistic, gentle natural movement at real speed, cinematic hotel commercial. The "
    "family keeps exactly the same faces, hair, clothes and body proportions; nobody looks at the "
    "camera; hands keep five fingers; the hotel room, furniture and windows stay exactly the same "
    "shape and position, no morphing, no new people, no text, no logos."
)

# clave → (imagen de arranque, prompt)
CLIPS = {
    "vista": ("DT-familia-vista-story-2160x3840.jpg",
              "Very slow cinematic push-in. Warm spring afternoon daylight comes through the big "
              "window. The father and the boy stand looking out at the city; the mother and the girl "
              "on the sofa turn a page of the book and smile softly at each other."),
    "lobby": ("DT-familia-lobby-story-2160x3840.jpg",
              "Slow backward dolly as the family walks calmly toward the camera through the lobby, "
              "the father pulling the suitcase, the kids holding hands with the mother, relaxed "
              "natural steps. Plants of the green wall move slightly."),
    "almohadas": ("DT-familia-almohadas-story-2160x3840.jpg",
                  "Static camera with a very slight drift. The two kids play a soft, gentle pillow "
                  "fight on the bed, the pillow moves in slow arcs, the mother laughs softly sitting "
                  "on the edge of the bed. Warm lamp light."),
    "restaurante": ("DT-familia-restaurante-story-2160x3840.jpg",
                    "Slow lateral dolly along the breakfast table. The father pours orange juice into "
                    "a glass, the mother and the kids smile and reach for their food. Morning light."),
    "cookie": ("DT-familia-cookie-hab-story-2160x3840.jpg",
               "Very slow push-in. The mother and the boy take a bite of their warm cookies, the "
               "father sips his cup, relaxed smiles, soft daylight from the window."),
    "hab": ("DT-familia-hab-2camas-story-2160x3840.jpg",
            "Very slow push-in. The family relaxes on the bed looking at a tablet together, the "
            "girl points at the screen and they smile softly. Calm, cozy, still."),
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
    ap.add_argument("--dur", default="5", choices=["5", "10"])
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
        cuerpo = {"image": imagen_b64(ruta), "prompt": prompt + CONTROL, "duration": a.dur}
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

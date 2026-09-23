#!/usr/bin/env python3
"""
R02 «Turno de noche» — anima los keyframes del episodio (image-to-video).

Storyboard: gcl-agent/R02_STORYBOARD.md. Cada clave es el nombre del plano ahí.
Entrada: public/assets/gcl/r02/<plano>.jpg   Salida: .../clips/<plano>.mp4

POR QUÉ TODOS LOS ENVÍOS VAN JUNTOS
Kling tarda 3–8 minutos por clip. En serie, 14 clips son dos horas. La API es
asíncrona: se mandan los 14 de una y después se consulta. Así el lote entero
tarda lo que tarda el más lento.

LA REGLA DEL PLANO (biblia de G.CL): **un movimiento de cámara y un microgesto
por clip.** Si el prompt pide dos acciones, Kling hace las dos a medias.

DOS VIGILANCIAS
 1. Que el personaje NO gire y pierda el visor — pasó en el R01 a partir del
    segundo 2,2. Por eso el montaje usa sólo el primer tramo de cada clip.
 2. `negative_prompt` NO existe en este endpoint: mandarlo devuelve 404. Lo que
    se quiere evitar va redactado en positivo dentro del prompt.

Uso:
    python3 scripts/gcl-r02-clips.py            # los que falten
    python3 scripts/gcl-r02-clips.py --solo c05_portal
    python3 scripts/gcl-r02-clips.py --rehacer
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

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANOS_DIR = os.path.join(RAIZ, "public", "assets", "gcl", "r02")
SALIDA = os.path.join(PLANOS_DIR, "clips")
BASE = "https://api.freepik.com/v1/ai"
MODELO = "kling-v2-1-pro"
CTX = ssl.create_default_context(cafile=certifi.where())

# Coletilla de control. Reemplaza al negative_prompt, que este endpoint rechaza.
CONTROL = (
    " Minimal controlled motion, cinematic, no camera shake, the subject stays "
    "facing camera the whole time and never turns away, shape and proportions "
    "stay exactly the same, no morphing, no extra objects appearing."
)

CLIPS = {
    # ---------- ACTO 1 ----------
    "c01_se_van": "The two coworkers keep walking away towards the office door, "
        "still chatting; the camera drifts slowly after them.",
    "c02_interruptor": "A hand presses the light switch down, the office behind "
        "falls into darkness, and the hand withdraws out of frame. Static camera.",
    # Hay que VER que quedó apagado: el plano es la consecuencia, no la acción.
    "c02b_apagado": "Nothing moves. Only a very slow camera drift closer to the "
        "switch, and the faint light from the far windows shifting almost "
        "imperceptibly. The room stays dark.",
    # ---------- ACTO 2 · la llegada ----------
    "c05_grieta": "The vertical crack of pink light crackles and widens a little, "
        "and the two black gloved hands tighten their grip on its two edges.",
    "c06_abre": "He pulls the rip of pink light WIDE OPEN with both arms, one to "
        "each side, and leans further out into the dark room. Sparks fly.",
    "c07_salta": "He lands on the meeting table from the leap, knees bending to "
        "absorb it, arms coming down to his sides. The portal closes behind him.",
    "c08_guino": "He holds the wink for a beat and then the closed eye opens back "
        "into the letter G, and he lowers his raised arm.",
    # ---------- ACTO 3 · a trabajar ----------
    "c09_chasquea": "The ring of glowing panels finishes igniting around him one "
        "after another while he lowers his arm. Slow camera arc to the right.",
    "c11_enfocado": "Slow push in on the black visor; the two narrow pink eyes "
        "narrow a little further.",
    "c12_manotea": "He completes the swipe: the panel flies off to the left and the "
        "next one slides in from the right.",
    "c13_sorpresa": "He leans back a little further with both arms still up while "
        "the bright panel in front of him pulses twice.",
    "c14_patron": "He lands from the small hop and points once more at the three "
        "identical panels, which pulse brighter together.",
    "c15_alerta": "The two loose panels fall and he catches them, leaning back away "
        "from the coral panel.",
    # v2: la primera versión despegaba la zapatilla del portal y le apagaba la
    # suela coral. Ese plano salió del capítulo entero: ahora él abre el portal.
    "c16_teclea": "His short arms move as he types in the air in front of him, "
        "and the glowing panel he is writing on brightens. He stays sitting.",
    "c17_corrige": "He pushes the crooked bar in the panel back into line with the "
        "others and lowers his arms; the check mark on the visor brightens.",
    # ---------- ACTO 4 · amanece y llega el equipo ----------
    "c19_amanece": "The last floating panels fade out around him one by one while "
        "the warm golden light shifts slowly across the table. He stands still.",
    "c20_llegan": "The people keep walking in towards the table, one of them "
        "raising a hand in greeting, and he waves back with his short arm.",
    "c21_highfive": "The human hand and the small gloved robot hand meet in the "
        "high five and bounce slightly apart. Close, warm, one single clean beat.",
    "c22_equipo": "The people around the table lean in slightly, smiling, and the "
        "glowing panel above the table brightens.",
}


def clave():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from _entorno import clave_freepik
    return clave_freepik()


def api(ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(
        BASE + ruta, data=datos, method="POST" if datos else "GET",
        headers={"x-freepik-api-key": clave(), "Content-Type": "application/json"})
    with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
        return json.loads(r.read())


def imagen_b64(ruta):
    """Reducida a 720 px: el keyframe de 1536×2752 son 471 KB en base64 y no hace
    falta — Kling entrega 1080p igual, y el payload chico falla menos."""
    from PIL import Image
    im = Image.open(ruta).convert("RGB")
    im.thumbnail((720, 1280))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    return base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", nargs="*")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()
    os.makedirs(SALIDA, exist_ok=True)

    nombres = a.solo or list(CLIPS)
    pendientes = {}
    for n in nombres:
        if n not in CLIPS:
            print(f"✗ No existe el clip «{n}»")
            continue
        destino = os.path.join(SALIDA, n + ".mp4")
        if os.path.exists(destino) and not a.rehacer:
            print(f"·  {n} ya está")
            continue
        kf = os.path.join(PLANOS_DIR, n + ".jpg")
        if not os.path.isfile(kf):
            print(f"✗  {n}: falta el keyframe {os.path.basename(kf)}")
            continue
        pendientes[n] = kf

    # 1) mandar todos de una
    tareas = {}
    for n, kf in pendientes.items():
        cuerpo = {"image": imagen_b64(kf),
                  "prompt": CLIPS[n] + CONTROL,
                  "duration": "5"}
        try:
            r = api(f"/image-to-video/{MODELO}", cuerpo)
            tareas[n] = r["data"]["task_id"]
            print(f"→  {n}  {tareas[n][:8]}")
        except urllib.error.HTTPError as e:
            print(f"✗  {n}: HTTP {e.code} {e.read().decode()[:200]}")

    # 2) consultar. ⚠️ Se ENVÍA a kling-v2-1-pro y se CONSULTA en kling-v2-1:
    #    preguntar por la ruta del POST devuelve 404 y parece que no existiera.
    consulta = f"/image-to-video/{MODELO.rsplit('-', 1)[0]}"
    limite = time.time() + 40 * 60
    while tareas and time.time() < limite:
        time.sleep(20)
        for n in list(tareas):
            try:
                d = api(f"{consulta}/{tareas[n]}")["data"]
            except Exception:
                continue
            if d["status"] == "COMPLETED" and d.get("generated"):
                destino = os.path.join(SALIDA, n + ".mp4")
                with urllib.request.urlopen(d["generated"][0], context=CTX,
                                            timeout=300) as r:
                    open(destino, "wb").write(r.read())
                print(f"✓  {n}  ({os.path.getsize(destino)//1024} KB)")
                del tareas[n]
            elif d["status"] in ("FAILED", "ERROR"):
                print(f"✗  {n}: {d['status']} — {json.dumps(d)[:200]}")
                del tareas[n]
    if tareas:
        print(f"⏳ quedaron sin terminar: {', '.join(tareas)}")

    # Los clips de Kling vienen pesados y ningún plano del reel usa más allá del
    # segundo 3,3. Se recortan a 3,5 s y se recomprimen: 16 clips pasan de 98 MB
    # a ~9 MB y así SÍ pueden viajar en el repo. Sin ellos versionados, otro
    # diseñador no reproduce el reel: Kling no es determinista y volver a
    # generarlos da otro movimiento. Además recortar elimina de raíz el riesgo
    # de que el personaje se gire pasados los 2 s.
    comp = os.path.join(RAIZ, "node_modules", "@remotion",
                        "compositor-darwin-arm64")
    entorno = dict(os.environ, DYLD_LIBRARY_PATH=comp)
    import subprocess
    for f in sorted(os.listdir(SALIDA)):
        if not f.endswith(".mp4"):
            continue
        ruta = os.path.join(SALIDA, f)
        if os.path.getsize(ruta) < 1_500_000:
            continue                      # ya está recortado
        tmp = ruta + ".tmp.mp4"
        subprocess.run([os.path.join(comp, "ffmpeg"), "-y", "-v", "error",
                        "-i", ruta, "-t", "3.5", "-c:v", "libx264",
                        "-crf", "26", "-preset", "medium", "-an", tmp],
                       env=entorno, check=False)
        if os.path.exists(tmp) and os.path.getsize(tmp) > 50_000:
            os.replace(tmp, ruta)
            print(f"   {f} → {os.path.getsize(ruta)//1024} KB")
        elif os.path.exists(tmp):
            os.remove(tmp)

    print(f"\nEn {os.path.relpath(SALIDA, RAIZ)}:")
    for f in sorted(os.listdir(SALIDA)):
        print("   ", f, os.path.getsize(os.path.join(SALIDA, f)) // 1024, "KB")


if __name__ == "__main__":
    sys.exit(main())

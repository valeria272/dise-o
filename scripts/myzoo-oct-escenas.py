#!/usr/bin/env python3
"""MyZoo · octubre 2026 — escenas IA de los 4 estáticos «Por diseñar».

La IA hace AMBIENTE y ESCENA. Nunca el producto, el logo ni un texto: donde va
un envase MyZoo se pide un MANIQUÍ liso (spray blanco sin etiqueta) y encima se
compone el packshot real (`myzoo-oct-armar.py`). Mismo flujo que CAVA
(`cava-escena-nanobanana.py`, ESCENA_MANIQUI).

Criterio del cliente que entra a los prompts (raw/myzoo/feedback-cliente.md):
  · «nada que se vea falso» (rechazó mascotas bailando con IA) → animales
    fotorrealistas, quietos, sin antropomorfizar más de lo que pide el brief
  · Exequiel es «muy picky»: limpio, sin barro, sin desorden
  · «no un fondo de color plano» → escena con profundidad, no cartulina

Uso:
    python3 scripts/myzoo-oct-escenas.py            # las 4
    python3 scripts/myzoo-oct-escenas.py kit meli   # sólo esas
"""
import base64
import json
import os
import ssl
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import certifi

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import clave_freepik  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAL = os.path.join(RAIZ, "raw", "myzoo", "oct", "escenas")
CTX = ssl.create_default_context(cafile=certifi.where())
RUTA = "/v1/ai/text-to-image/nano-banana-pro"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) copylab-estudio"  # el WAF bloquea el UA de urllib

LIMPIO = ("Clean, bright, premium pet-care advertising photograph, photorealistic, "
          "natural soft light, tidy and spotless, no mud, no mess. ")
SIN_TEXTO = (" Absolutely NO text, NO letters, NO logos, NO brand marks anywhere in "
             "the image.")

ESCENAS = {
    # 01-10 · Post · «ROMPER EN CASO DE PASEO» (ref: pins break-glass)
    "kit": dict(aspect="4:5", refs=[], prompt=LIMPIO + (
        "A wall-mounted emergency cabinet painted glossy coral red (#FF6969) with a "
        "clear glass door, hanging on a smooth soft sky-blue painted wall (#8FCBE0). "
        "The cabinet is seen straight-on, perfectly frontal and level, centered "
        "horizontally, its top edge at about 42% of the image height and its bottom "
        "at about 80%. At the TOP of the cabinet, above the glass, there is a BLANK "
        "plain white rectangular plate, completely empty. Inside the cabinet, on a "
        "small shelf, stands ONE single plain white spray bottle with a black trigger "
        "pump, completely blank with NO label, centered, occupying about 70% of the "
        "cabinet interior height. A small red emergency hammer hangs on a chain on the "
        "right side of the cabinet. A tan leather dog leash hangs from a hook on the "
        "wall to the left. In the lower left foreground, a fluffy golden cocker spaniel "
        "sits seen from behind in three-quarter view, looking up curiously at the "
        "cabinet. The upper 38% of the image is calm empty blue wall. Floor: light "
        "wooden floor. Soft shadow of the cabinet on the wall." + SIN_TEXTO)),

    # 02-10 · Story · PREGUNTAZOO (ref: vet con mascota, caja de preguntas)
    "preguntazoo": dict(aspect="9:16", refs=[], prompt=LIMPIO + (
        "A friendly young Chilean female veterinarian with a warm genuine smile, "
        "wearing a clean light-blue medical scrub top, holding a happy fluffy "
        "golden retriever puppy in her arms, while a gray tabby cat sits on the "
        "table beside her. They occupy ONLY the bottom 42% of the vertical frame, "
        "cropped at her waist by the bottom edge. Background: a seamless soft "
        "sky-blue studio backdrop (#8FCBE0) with a gentle gradient, completely empty "
        "and clean in the upper 58% of the image. A few very subtle, soft, out of "
        "focus coral pink question-mark shaped paper cutouts float near the edges, "
        "small and discreet." + SIN_TEXTO)),

    # 05-10 · Post · MyZoo llega a todo Chile con Mercado Libre (ref: mapa + scooter)
    "meli": dict(aspect="4:5", refs=[os.path.join(RAIZ, "raw/myzoo/oct/chile-silueta.png")], prompt=(
        "Cheerful stylized 3D illustrated scene, soft clay/toy-like render, bright and "
        "clean, like a premium Pixar-style advertising illustration. A 3D "
        "illustrated MAP OF CHILE lies on a soft sky-blue ground. The map occupies ONLY "
        "the lower 62% of the image: its northern tip starts at 40% of the image height, seen in gentle "
        "perspective from above: the country shape MUST follow EXACTLY the long thin "
        "silhouette of the reference image (north at the top, southern end near the bottom "
        "edge, the far south bending to the east), with little mountains of the Andes along its east "
        "side, tiny trees, the Atacama desert in warm sand tones in the north, green "
        "center and lakes and forests in the south, blue Pacific ocean to the west. "
        "A bright yellow dotted delivery route runs along the whole country from north "
        "to south with small location pins. On the route, in the center of the image "
        "and large in the foreground, a cute yellow pickup delivery truck WITHOUT any "
        "logo, seen in three-quarter view, drives, driven by a happy smiling french bulldog with its head out of "
        "the window. In the open cargo bed, a gray tabby cat "
        "sits next to an open EMPTY cardboard box; the cargo bed floor is clearly "
        "visible and empty in front of the box. The truck sits in the lower-center "
        "of the image, between 50% and 85% of the height. The upper 38% of the image "
        "is calm empty sky-blue with only two or three small soft clouds near the "
        "side edges." + SIN_TEXTO)),

    # 08-10 · Post · Cruelty Free Te Protejo (ref: choque de mano y pata, amarillo)
    "cruelty": dict(aspect="4:5", refs=[], prompt=LIMPIO + (
        "Emotional, luminous close-up: a human hand and a dog's paw meeting gently "
        "palm to paw in a soft high five, entering from the left (the dog: a "
        "friendly brown mixed-breed dog, head and paw visible in profile) and from the "
        "right (the human hand, forearm only). Behind the touching point, a soft glow "
        "of warm sunlight. Background: a warm, radiant sunny yellow gradient "
        "(#FFD94A to #FFB930) with soft light rays, clean and uplifting. The subjects "
        "are small-to-medium in frame and sit LOW, in the band between 42% and 78% of "
        "the image height; the dog's head is at about 50% of the height. The top 40% "
        "and the bottom 20% are calm, empty warm yellow, full bleed, no borders, no "
        "bands, one continuous background." + SIN_TEXTO)),
}


def b64(ruta):
    return base64.b64encode(open(ruta, "rb").read()).decode()


def pedir(ruta, cuerpo=None):
    req = urllib.request.Request(
        "https://api.freepik.com" + ruta,
        data=json.dumps(cuerpo).encode() if cuerpo else None,
        headers={"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json",
                 "User-Agent": UA},
        method="POST" if cuerpo else "GET")
    with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
        return json.load(r)


def generar(nombre, n):
    e = ESCENAS[nombre]
    cuerpo = {"prompt": e["prompt"], "aspect_ratio": e["aspect"], "resolution": "4K"}
    if e["refs"]:
        cuerpo["reference_images"] = [{"image": b64(r), "mime_type": "image/png"} for r in e["refs"]]
    try:
        tid = pedir(RUTA, cuerpo)["data"]["task_id"]
    except urllib.error.HTTPError as err:
        return f"{nombre}-{n}: HTTP {err.code} {err.read()[:300]}"
    for _ in range(80):
        time.sleep(8)
        d = pedir(f"{RUTA}/{tid}")["data"]
        if d["status"] == "COMPLETED":
            dst = os.path.join(SAL, f"{nombre}-{n}.png")
            req = urllib.request.Request(d["generated"][0], headers={"User-Agent": UA})
            open(dst, "wb").write(urllib.request.urlopen(req, context=CTX).read())
            return f"{nombre}-{n}: ✓ {dst}"
        if d["status"] == "FAILED":
            return f"{nombre}-{n}: ✗ FAILED"
    return f"{nombre}-{n}: ✗ timeout"


if __name__ == "__main__":
    os.makedirs(SAL, exist_ok=True)
    nombres = sys.argv[1:] or list(ESCENAS)
    trabajos = [(n, i) for n in nombres for i in (1, 2)]   # 2 tomas por escena para elegir
    with ThreadPoolExecutor(8) as ex:
        for r in ex.map(lambda t: generar(*t), trabajos):
            print(r)


# ── Reencuadre: la escena elegida trae el sujeto muy arriba y choca con el titular.
# NO se estira (rayas verticales) ni se usa image-expand (ignora el tamaño pedido,
# ver casablanca-sep-pipeline.py paso 4). Se le pasa la MISMA imagen a Nano Banana
# Pro y se le pide alejar la cámara, dejando fondo continuo arriba.
REENCUADRE = {
    "kit-1": ("Recreate this exact image, identical coral red emergency cabinet, blank white "
              "plate, plain white unlabeled spray bottle, hammer, leash, dog, blue wall and "
              "wood floor, same light and style, but the camera is CLOSER and the scene sits "
              "LOWER: the cabinet is larger, centered horizontally, its top edge (the blank "
              "white plate) at 46% of the image height and its bottom edge at 86%. The dog "
              "sits in the lower left corner, partially cropped by the left and bottom edges, "
              "looking up at the cabinet. The top 44% of the image is the same calm, empty, "
              "smooth sky-blue wall. The plate stays completely blank and the bottle stays "
              "completely unlabeled."),
    "preguntazoo-1": ("Recreate this exact image, identical veterinarian, golden retriever puppy, "
                      "tabby cat, blue scrub, sky-blue studio backdrop and light, but zoomed OUT: "
                      "the group is smaller and occupies ONLY the bottom 30% of the vertical frame, "
                      "the veterinarian's head at about 74% of the image height, cropped at her "
                      "waist by the bottom edge. The top 70% is the same calm, clean, empty "
                      "sky-blue backdrop with only two or three small soft coral question-mark "
                      "cutouts near the side edges."),
    "cruelty-3": ("Recreate this exact image, identical subjects, colors, light and style, "
                  "but zoomed out: the dog and the hand are smaller and placed LOWER, with the "
                  "dog's head at about 55% of the image height and the high-five point at "
                  "about 58%. The top 45% of the image is the same warm radiant yellow "
                  "background with soft light rays, continuous and clean, no borders, no bands."),
    "meli-4": ("Recreate this exact image, identical map of Chile, truck, dog, cat, colors and "
               "style, but zoomed out a little and shifted DOWN: the northern tip of the map "
               "starts at 42% of the image height and the southern end touches the bottom "
               "edge. The top 40% is the same calm light sky-blue background with two or "
               "three small soft clouds near the side edges, continuous and clean."),
}


def reencuadrar(nombre, n):
    fuente = os.path.join(SAL, nombre + ".png")
    from PIL import Image
    import io
    im = Image.open(fuente).convert("RGB"); im.thumbnail((1600, 1600))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=92)
    cuerpo = {"prompt": REENCUADRE[nombre] + SIN_TEXTO, "aspect_ratio": ("9:16" if nombre.startswith("pregunta") else "4:5"), "resolution": "4K",
              "reference_images": [{"image": base64.b64encode(buf.getvalue()).decode(),
                                    "mime_type": "image/jpeg"}]}
    tid = pedir(RUTA, cuerpo)["data"]["task_id"]
    for _ in range(80):
        time.sleep(8)
        d = pedir(f"{RUTA}/{tid}")["data"]
        if d["status"] == "COMPLETED":
            dst = os.path.join(SAL, f"{nombre}-bajo{n}.png")
            req = urllib.request.Request(d["generated"][0], headers={"User-Agent": UA})
            open(dst, "wb").write(urllib.request.urlopen(req, context=CTX).read())
            return f"{nombre}-bajo{n}: ✓"
        if d["status"] == "FAILED":
            return f"{nombre}-bajo{n}: ✗ FAILED"
    return "timeout"


# ── Diagramación por BOCETO. Nano Banana Pro no respeta porcentajes escritos en el
# prompt (dos reencuadres del 22-09 dejaron el gabinete al 32 % pidiendo 46 %), pero
# sí copia la diagramación de una imagen de referencia. Se le pasa un boceto de
# bloques de color con la escena ya ubicada donde deja aire al titular.
BOCETO = {
    "kit": ("raw/myzoo/oct/boceto-kit.png", "4:5", ESCENAS["kit"]["prompt"]),
    "preguntazoo": ("raw/myzoo/oct/boceto-story.png", "9:16", ESCENAS["preguntazoo"]["prompt"]),
}


def con_boceto(nombre, n):
    ruta, aspecto, prompt = BOCETO[nombre]
    prompt = ("Use the attached flat color-block sketch ONLY as the LAYOUT guide: place every "
              "element exactly where its block is, same size and position, and keep the empty "
              "areas of the sketch empty. Do not copy the sketch's flat style. " + prompt)
    cuerpo = {"prompt": prompt, "aspect_ratio": aspecto, "resolution": "4K",
              "reference_images": [{"image": b64(os.path.join(RAIZ, ruta)), "mime_type": "image/png"}]}
    tid = pedir(RUTA, cuerpo)["data"]["task_id"]
    for _ in range(80):
        time.sleep(8)
        d = pedir(f"{RUTA}/{tid}")["data"]
        if d["status"] == "COMPLETED":
            dst = os.path.join(SAL, f"{nombre}-boceto{n}.png")
            req = urllib.request.Request(d["generated"][0], headers={"User-Agent": UA})
            open(dst, "wb").write(urllib.request.urlopen(req, context=CTX).read())
            return f"{nombre}-boceto{n}: ✓"
        if d["status"] == "FAILED":
            return f"{nombre}-boceto{n}: ✗"
    return "timeout"


# ── Outpaint dirigido. Ni el prompt ni el boceto hicieron bajar los sujetos, así que
# la posición la decide el estudio: la escena buena se pone MÁS CHICA y apoyada abajo
# en un lienzo del tamaño final, con márgenes gris plano, y Nano Banana Pro sólo
# rellena esos márgenes continuando muro, piso y fondo (lienzo-*.png).
def outpaint(lienzo, aspecto, dst, n):
    prompt = ("Complete this image: fill ONLY the flat solid gray (#808080) areas at the top "
              "and sides, seamlessly continuing the existing wall, backdrop, floor and table "
              "with the same color, gradient, light and texture, so the whole image reads as "
              "one continuous photograph with no seams, borders or frames. Keep everything "
              "that is already in the photo exactly as it is, in the same position and size. "
              "Do not add any new objects." + SIN_TEXTO)
    cuerpo = {"prompt": prompt, "aspect_ratio": aspecto, "resolution": "4K",
              "reference_images": [{"image": b64(os.path.join(RAIZ, lienzo)), "mime_type": "image/png"}]}
    tid = pedir(RUTA, cuerpo)["data"]["task_id"]
    for _ in range(80):
        time.sleep(8)
        d = pedir(f"{RUTA}/{tid}")["data"]
        if d["status"] == "COMPLETED":
            out = os.path.join(SAL, f"{dst}{n}.png")
            req = urllib.request.Request(d["generated"][0], headers={"User-Agent": UA})
            open(out, "wb").write(urllib.request.urlopen(req, context=CTX).read())
            return f"{dst}{n}: ✓"
        if d["status"] == "FAILED":
            return f"{dst}{n}: ✗"
    return "timeout"

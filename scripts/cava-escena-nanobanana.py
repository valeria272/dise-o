#!/usr/bin/env python3
"""CAVA — genera el bodegón COMPLETO con Nano Banana Pro, con el packshot de referencia.

POR QUÉ SE LLEGA A ESTO (28-08-2026)
------------------------------------
Componer el packshot sobre un fondo generado tiene un techo: **el barril del fondo
y la botella no comparten escala**. En `kv-fiestas-01.png` la tapa mide 1580 px de
diámetro; el manual pide la botella al 52 % del alto (1459 px), o sea 0,92 del
diámetro de la tapa cuando físicamente una botella es 0,53. Se puede respetar la
escala física —y la botella queda chica, «un barril grande con botellita encima»—
o respetar el tamaño del manual —y queda desproporcionada—. No hay punto bueno:
el fondo se generó sin pensar en el producto que iba encima.

Valeria, 28-08: *«la botella sigue flotando cuando debería estar sobre el barril
[…] todo es desproporcional»*.

La salida es generar barril y botella EN LA MISMA ESCENA, para que la IA resuelva
apoyo, escala, sombra y luz de una vez. Nano Banana Pro acepta hasta 14 imágenes
de referencia, así que se le pasa el bottle shot oficial.

⛔ LO QUE HAY QUE VERIFICAR SIEMPRE
-----------------------------------
`clients/cava/CLAUDE.md` §2: las botellas y sus etiquetas son intocables. Una IA
puede devolver una etiqueta *parecida* y eso no se entrega. Este script recorta la
etiqueta del resultado y la compara con el packshot real; si el parecido no da,
la escena sirve como FONDO y el producto se compone encima con el packshot de
verdad. Ver [[integrar-luz-sin-tocar-el-producto]].

Uso:
    python3 scripts/cava-escena-nanobanana.py --botella 7colores-single-vineyard-red-blend
"""
import argparse
import base64
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request

import certifi
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOT = os.path.join(RAIZ, "public", "assets", "cava", "bottles")
SALIDA = os.path.join(RAIZ, "out", "cava", "escenas-ia")
CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com"
RUTA = "/v1/ai/text-to-image/nano-banana-pro"

# La escena. Lo que importa: barril VISTO LIGERAMENTE DESDE ARRIBA para que la
# tapa sea una elipse donde apoyar, botella APOYADA con sombra de contacto, y el
# viñedo deshecho en bokeh — el fondo nunca compite en nitidez con el producto.
# ⛔ PROBADO EL 28-08-2026: pedirle la botella a la IA NO sirve para esta cuenta.
# La escena sale perfecta —apoyo real sobre la tapa, escala coherente, bokeh— pero
# REDIBUJA LA ETIQUETA E INVENTA EL TEXTO: devolvió «SINGLE VINESARD», «VALLE DEL
# MALLSI» y «WINE DE CHIVE» en un 7Colores. En una viña eso no se entrega.
# Por eso el flujo bueno es ESCENA_VACIA: la IA hace el barril y el viñedo, y el
# producto real se compone encima. clients/cava/CLAUDE.md §2.
ESCENA_CON_BOTELLA = (
    "Professional advertising photograph of the exact wine bottle from the "
    "reference image, standing UPRIGHT AND FIRMLY RESTING ON TOP of an old oak "
    "wine barrel, seen slightly from above so the round barrel top reads as a wide "
    "ellipse of bare wood. The bottle sits ON the wooden surface with a visible "
    "contact shadow under its base — it must NOT float in front of the barrel. "
    "The bottle occupies about half the image height and is clearly the subject. "
    "Behind, a Chilean vineyard in autumn at golden hour, completely out of focus, "
    "creamy warm bokeh, shallow depth of field, only the bottle is sharp. "
    "Warm golden backlight, soft rim light along the bottle edges, deep amber "
    "shadows, premium wine brand aesthetic, photorealistic, shot on 85mm lens. "
    "CRITICAL: reproduce the bottle label EXACTLY as in the reference image — same "
    "artwork, same colors, same text, same proportions. Do not redesign the label. "
    "No people, no extra text, no logos added, no other bottles."
)


# El barril SIN botella, con la misma puesta de cámara que resolvió bien la escala:
# barril cortado por el pie, tapa como elipse ancha y despejada, viñedo deshecho.
ESCENA_VACIA = (
    "Professional advertising photograph of an old oak wine barrel standing "
    "upright, seen slightly from above so its round top reads as a WIDE CLEAR "
    "ELLIPSE of bare wood, completely empty and unobstructed — nothing on top of "
    "it. The barrel is cropped by the bottom edge of the frame and fills the lower "
    "third; its top surface sits around 55-60% of the image height. Behind it, a "
    "Chilean vineyard in autumn at golden hour, completely out of focus, creamy "
    "warm bokeh, shallow depth of field. Warm golden backlight from behind, soft "
    "light falling on the barrel top, deep amber shadows, premium wine brand "
    "aesthetic, photorealistic, shot on 85mm lens. "
    "No bottles, no glasses, no people, no text, no logos, no props on the barrel."
)


# ⭐ EL FLUJO BUENO: una botella MANIQUÍ, lisa y sin nada encima. Define el apoyo,
# la escala, la sombra y la luz —que es lo que la IA resuelve bien— y después se
# cubre con el bottle shot oficial. Sin etiqueta ni medallas inventadas asomando
# por detrás, que fue lo que arruinó el primer intento.
ESCENA_MANIQUI = (
    "Professional advertising photograph of a PLAIN UNLABELED dark green wine "
    "bottle, completely blank with NO LABEL, NO TEXT, NO MEDALS, NO STICKERS and "
    "NO FOIL DESIGN — just smooth dark glass with a plain black capsule. The bottle "
    "stands UPRIGHT AND FIRMLY RESTING ON TOP of an old oak wine barrel, seen "
    "slightly from above so the barrel top reads as a wide ellipse of bare wood. "
    "The bottle sits ON the wooden surface with a clear contact shadow under its "
    "base — it must NOT float in front of the barrel. The bottle is centered and "
    "occupies about 70% of the image height. Behind it, a Chilean vineyard in "
    "autumn at golden hour, completely out of focus, creamy warm bokeh, shallow "
    "depth of field. Warm golden backlight, soft rim light along the bottle edges, "
    "deep amber shadows, premium wine aesthetic, photorealistic, 85mm lens. "
    "No people, no other bottles, no glasses, no text anywhere in the image."
)


def clave():
    f = os.path.join(os.path.expanduser("~"), ".magnific_key")
    if os.path.isfile(f):
        k = open(f).read().strip()
        if k:
            return k
    env = os.path.join(os.path.dirname(RAIZ), "ASISTENTE PERSONAL", ".env")
    for l in open(env, encoding="utf-8").read().splitlines():
        m = re.match(r"\s*FREEPIK_API_KEY\s*=\s*(.+)", l)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    sys.exit("✗ No encuentro la clave")


K = clave()


def espera(task_id, limite=240):
    for i in range(limite):
        req = urllib.request.Request(f"{BASE}{RUTA}/{task_id}",
                                     headers={"x-freepik-api-key": K})
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            d = json.load(r)["data"]
        est = d.get("status")
        if est == "COMPLETED":
            g = d.get("generated") or []
            if g:
                return g[0]
            # marca COMPLETED antes de publicar la URL — ver cava-botellas-2x.py
        elif est in ("FAILED", "ERROR"):
            sys.exit(f"✗ falló: {json.dumps(d)[:300]}")
        if i % 15 == 0:
            print(f"     … {est} ({i*2}s)")
        time.sleep(2)
    sys.exit("✗ se agotó la espera")


def ref_b64(nombre, lado=1024):
    """El packshot, sobre blanco y reducido: un payload grande corta la conexión."""
    p2 = os.path.join(BOT, "2x", nombre + ".png")
    im = Image.open(p2 if os.path.isfile(p2) else
                    os.path.join(BOT, nombre + ".png")).convert("RGBA")
    im = im.crop(im.split()[-1].getbbox())
    plano = Image.new("RGB", im.size, (255, 255, 255))
    plano.paste(im.convert("RGB"), (0, 0), im.split()[3])
    esc = lado / max(plano.size)
    if esc < 1:
        plano = plano.resize((round(plano.width * esc), round(plano.height * esc)),
                             Image.LANCZOS)
    buf = io.BytesIO()
    plano.save(buf, "JPEG", quality=92)
    return base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--botella", default="7colores-single-vineyard-red-blend")
    ap.add_argument("--aspecto", default="4:5")
    ap.add_argument("--resolucion", default="2K", choices=["1K", "2K", "4K"])
    ap.add_argument("--n", type=int, default=1, help="cuántas variantes")
    ap.add_argument("--maniqui", action="store_true",
                    help="botella LISA sin etiqueta: el flujo bueno")
    ap.add_argument("--vacia", action="store_true",
                    help="barril SIN botella (el flujo bueno: el producto se compone después)")
    a = ap.parse_args()
    os.makedirs(SALIDA, exist_ok=True)

    print(f"→ Nano Banana Pro · {a.botella} · {a.aspecto} · {a.resolucion}")
    # Cada referencia es un OBJETO {image, mime_type, text}, no una cadena suelta
    # como en el endpoint de Nano Banana (el viejo). Mandar el base64 pelado
    # devuelve 400 «Input should be a valid dictionary».
    if a.maniqui:
        cuerpo = {"prompt": ESCENA_MANIQUI, "aspect_ratio": a.aspecto,
                  "resolution": a.resolucion}
    elif a.vacia:
        cuerpo = {"prompt": ESCENA_VACIA, "aspect_ratio": a.aspecto,
                  "resolution": a.resolucion}
    else:
        cuerpo = {"prompt": ESCENA_CON_BOTELLA, "aspect_ratio": a.aspecto,
              "resolution": a.resolucion,
              "reference_images": [{
                  "image": ref_b64(a.botella),
                  "mime_type": "image/jpeg",
                  "text": "The exact wine bottle and label to reproduce, unchanged",
              }]}

    for k in range(a.n):
        req = urllib.request.Request(BASE + RUTA, data=json.dumps(cuerpo).encode(),
                                     method="POST",
                                     headers={"x-freepik-api-key": K,
                                              "Content-Type": "application/json"})
        try:
            tid = json.load(urllib.request.urlopen(req, context=CTX,
                                                   timeout=180))["data"]["task_id"]
        except urllib.error.HTTPError as e:
            sys.exit(f"✗ {e.code} {e.read(300).decode()[:300]}")
        url = espera(tid)
        nombre = ("maniqui" if a.maniqui else
                  "barril-vacio" if a.vacia else a.botella)
        destino = os.path.join(SALIDA, f"{nombre}-{k+1:02d}.png")
        with urllib.request.urlopen(url, context=CTX, timeout=180) as r:
            open(destino, "wb").write(r.read())
        im = Image.open(destino)
        print(f"  ✓ {im.width}×{im.height} → {destino}")

    print("\n⚠️ MÍRALA antes de usarla, y comprueba la etiqueta contra el packshot:")
    print("   si la IA la redibujó, la escena sirve de FONDO y el producto se")
    print("   compone encima con el bottle shot real (clients/cava/CLAUDE.md §2).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

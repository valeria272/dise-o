#!/usr/bin/env python3
"""RONDA 11 — la escena de la ST de Cowork (col N, 16-09) se PRODUCE entera con IA.

Que cambia respecto de la ronda 10
----------------------------------
Eli, 10-09: «Me parece que el montaje esta mal logrado, la foto de fondo original
debes anadir un vaso togo, un notebook con logo apple, da lo mismo si aparece que
sea sutil. Un desayuno de sandwich. como se ven en las fotos. Hazlo nuevamente y
recuerda hacer un buen prompt, en magnific.»

Tres correcciones, y ninguna es de gusto:

  1. ⛔ SE ACABA EL MONTAJE A MANO. En la ronda 10 el vaso real se pegaba con
     `between-montar-vaso.py` DESPUES del paso de IA. Eli lo rechazo: «el montaje
     esta mal logrado». Ahora el vaso lo pinta el modelo, dentro de la escena,
     con la luz y la profundidad de campo de la mesa.
  2. ✅ EL LOGO DE APPLE SE QUEDA. En la ronda 10 se lo saque por prudencia («una
     marca ajena no va en una pieza de cliente») y ella lo devolvio: «un notebook
     con logo apple, da lo mismo si aparece que sea sutil». Es criterio de la
     disenadora y manda.
  3. ➕ ENTRA EL DESAYUNO DE SANDWICH, «como se ven en las fotos» — o sea el de
     la sesion real del cliente, no uno inventado.

Las cuatro referencias, y para que va cada una
----------------------------------------------
  1. la foto REAL del cowork reencuadrada  -> la escena que hay que conservar
  2. la edicion de Magnific de Eli          -> el tratamiento: como esta cuenta
     pone un portatil y una taza sobre una mesa de madera
  3. el vaso To Go real recortado           -> el logotipo, para que el modelo lo
     escriba bien en vez de inventar letras
  4. un desayuno real de la sesion          -> el plato, el pan y el montaje del
     desayuno tal como los sirve Between

⚠️ Nano Banana Pro pide las referencias como objetos {"image", "mime_type"}, no
strings sueltos, y acepta hasta 14.

Uso:
    python scripts/between-cowork-escena-ia.py            # 3 variantes
    python scripts/between-cowork-escena-ia.py --n 1
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import clave_freepik  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "out/hilton/between/ia-cowork-taza2"

REFS = [
    RAIZ / "public/assets/hilton/between/st-s3/st-16-09-cowork-real.jpg",
    RAIZ / "public/assets/hilton/between/taza-cappuccino-nobg.png",
    # ⭐ RONDA 13: la tercera referencia es LA PROPIA VERSION APROBADA. Eli: «me
    # cambiaste el sandwich y ese estaba correcto, vuelve al sandwich anterior de
    # jamon y queso». Cuando lo aprobado es un resultado del modelo, la referencia
    # mas fiel es ese resultado — y de paso trae la laptop y el tratamiento, asi
    # que la edicion de Magnific de Eli deja de hacer falta como referencia.
    RAIZ / "out/hilton/between/ia-cowork-escena/escena-v3.png",
]

K = clave_freepik() or sys.exit("x falta la clave de Freepik — corre llavero.py abrir")
H = {"x-freepik-api-key": K, "Content-Type": "application/json"}

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    SSL_CTX = ssl.create_default_context()


# ── EL PROMPT ──────────────────────────────────────────────────────────────
# Estructura: que es cada referencia, lo que NO se toca, lo que se agrega objeto
# por objeto, la luz medida, la composicion (con la restriccion del cartel) y al
# final las negaciones. Lo que no se toca va ANTES de lo que se agrega: si se
# pone al final, el modelo ya reescribio la escena.

REFERENCIAS = (
    "Three references. REF1 is the photograph to keep: the real second-floor lounge "
    "of the Between coffee bar, shot from a seat at a wooden table. REF2 is the "
    "brand's cappuccino: a plain white ceramic cup on a matching white saucer, "
    "latte art on the crema, a spoon on the saucer. REF3 is the APPROVED version of "
    "this same picture: copy its laptop and its breakfast exactly. "
)

CONSERVAR = (
    "KEEP REF1 EXACTLY. Do not change framing, crop, camera angle, perspective or "
    "focal length. Do not redraw or move the ceiling, the downlights, the arched "
    "floor lamp with its woven shade, the framed city photographs, the dark slat "
    "wall, the grey armchairs, the tan banquette, the console, the carpet or the "
    "table. Keep the exact wood grain, colour, knots and sheen of the table top, "
    "and the existing lighting, white balance, contrast and background blur. It "
    "must read as the same photograph. "
)

AGREGAR = (
    "ADD THREE OBJECTS resting on the wooden table in the foreground, each with a "
    "realistic contact shadow. "
    "(a) THE OPEN LAPTOP FROM REF3, slightly left of centre and set back: thin "
    "space-grey aluminium, lid open, rear three-quarter view so the back of the lid "
    "faces the camera, with the same small subtle dark apple logo on the lid. No "
    "screen interface, no text. "
    "(b) THE BREAKFAST PLATE FROM REF3, in front of the laptop and slightly left: "
    "the round white plate with the toasted ham and cheese sandwich cut into two "
    "halves, the melted cheese and the ham visible at the cut, exactly as in REF3. "
    "(c) THE WHITE CAPPUCCINO from REF2, on its saucer, to the RIGHT of the plate, "
    "near it but NOT touching: leave a narrow strip of bare wood between the saucer "
    "and the plate, about a third of the saucer's width. Same low table-level "
    "angle, latte art visible on the crema. "
)

LUZ = (
    "LIGHT: the warm interior light comes from the RIGHT - measured on the table, "
    "the right side is brighter. Light every added object from the right, brighter "
    "edge on the right, soft contact shadow falling LEFT and slightly toward the "
    "camera. Match the room's white balance and the grain of the photograph: "
    "nothing may look sharper than the wood. "
)

COMPOSICION = (
    "COMPOSITION: all three objects sit in the LOWER HALF of the vertical frame, "
    "below the middle line. The plate and the cup read as one breakfast served "
    "together, side by side but separated by a narrow strip of wood; the laptop "
    "sits behind them with more wood between. The UPPER HALF stays completely "
    "untouched and free of new objects - graphic text goes there. Keep the near "
    "table edge mostly empty. "
)

NEGATIVO = (
    "No people, hands, phones, sunglasses, cables, plants, takeaway cups or a "
    "second cup. No brand name, sign, logo or watermark except the small apple on "
    "the laptop lid. No captions. Take ONLY the laptop and the plate from REF3 - "
    "ignore its takeaway cup, which must not appear. Photorealistic, one coherent "
    "photo."
)

PROMPT = REFERENCIAS + CONSERVAR + AGREGAR + LUZ + COMPOSICION + NEGATIVO

# ⚠️ La API topa el prompt en 3000 caracteres y devuelve HTTP 400 si se pasa.
assert len(PROMPT) <= 3000, "el prompt mide %d y el tope son 3000" % len(PROMPT)


def http(url, method="GET", body=None, timeout=300):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=H, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw.decode(errors="ignore")


def dig(obj, want_url=True):
    if isinstance(obj, str):
        if want_url and obj.startswith("http"):
            return obj
        if not want_url and len(obj) > 5000 and not obj.startswith("http"):
            return obj
        return None
    if isinstance(obj, dict):
        for v in obj.values():
            f = dig(v, want_url)
            if f:
                return f
    if isinstance(obj, list):
        for v in obj:
            f = dig(v, want_url)
            if f:
                return f
    return None


def poll(base, task_id, etiqueta):
    if not task_id:
        return None
    for _ in range(100):
        st, data = http("%s/%s" % (base, task_id))
        d = data.get("data", {}) if isinstance(data, dict) else {}
        if d.get("status") in ("COMPLETED", "SUCCESS"):
            return dig(data, True) or dig(data, False)
        if d.get("status") == "FAILED":
            print("    x fallo: " + json.dumps(data)[:300])
            return None
        time.sleep(5)
    print("    x timeout de " + etiqueta)
    return None


def b64(p):
    return base64.b64encode(p.read_bytes()).decode()


def mime(p):
    return "image/png" if p.suffix.lower() == ".png" else "image/jpeg"


def guardar(resultado, destino):
    if not resultado:
        return False
    destino.parent.mkdir(parents=True, exist_ok=True)
    if resultado.startswith("http"):
        with urllib.request.urlopen(resultado, timeout=300, context=SSL_CTX) as r:
            destino.write_bytes(r.read())
    else:
        destino.write_bytes(base64.b64decode(resultado))
    kb = destino.stat().st_size // 1024
    if kb < 20:
        print("    x %s pesa %d KB — sospechoso, se descarta" % (destino.name, kb))
        destino.unlink()
        return False
    print("    OK %s (%d KB)" % (destino.name, kb))
    return True


def generar(i):
    base = "https://api.freepik.com/v1/ai/text-to-image/nano-banana-pro"
    st, data = http(base, "POST", {
        "prompt": PROMPT,
        "aspect_ratio": "9:16",
        "resolution": "4K",
        "reference_images": [{"image": b64(r), "mime_type": mime(r)} for r in REFS],
    })
    print("  variante %d · nano-banana-pro (%d refs, 4K) -> HTTP %s"
          % (i, len(REFS), st))
    if st not in (200, 201):
        print("  " + json.dumps(data)[:400])
        return None
    return poll(base, data.get("data", {}).get("task_id"), "v%d" % i)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=3, help="cuantas variantes")
    a = ap.parse_args()

    faltan = [r for r in REFS if not r.exists()]
    if faltan:
        sys.exit("x faltan referencias:\n  " + "\n  ".join(str(f) for f in faltan))
    print("referencias:")
    for r in REFS:
        print("  · " + r.name)
    print("prompt: %d caracteres" % len(PROMPT))
    print()
    for i in range(1, a.n + 1):
        guardar(generar(i), SALIDA / ("escena-v%d.png" % i))
    return 0


if __name__ == "__main__":
    sys.exit(main())

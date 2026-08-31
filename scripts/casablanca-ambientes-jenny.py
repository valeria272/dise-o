#!/usr/bin/env python3
"""Casablanca C1 — CUATRO ambientes distintos, uno por producto (Jenny, 28-08-2026).

    python3 scripts/casablanca-ambientes-jenny.py natural_uv_grande
    python3 scripts/casablanca-ambientes-jenny.py --todos
    python3 scripts/casablanca-ambientes-jenny.py natural_uv_grande --medir

Por qué existe, y por qué NO se reusa `casablanca-ambiente-unico.py`:

  · La clienta pidió por WhatsApp el 28-08: *«por favor usar ambiente distintos en
    cada foto no el mismo»*. Eso DEROGA el lineamiento nº1 del brief —«UN MISMO
    AMBIENTE EN LAS 4 TARJETAS»—, que era la regla sobre la que estaba construido
    el script anterior. Ver `feedback/2026-08-28-ronda4-cliente.md`.

  · El método viejo era una base + 3 ediciones img-to-img. Su prompt base decía
    «engineered oak plank flooring in **warm honey tone**», así que las cuatro
    tarjetas arrastraban el miel — incluido el Cumarú, que es café rojizo. Medido:
    el piso del ambiente daba ΔE 17,6 a 31,6 contra la foto oficial del producto.
    Jenny lo vio a simple vista: *«este piso no se parece al producto real»*.

  · Acá cada ambiente se genera SOLO, con su propia sala, y el piso se describe
    desde la foto oficial del SKU y desde la referencia que mandó Jenny.

⛔ INTENTO DESCARTADO — no volver a hacerlo. El generador tiene un sesgo fijo de
13° a 20° hacia el amarillo que ningún prompt movió (se probaron cuatro
redacciones). Se implementó una rotación determinista del tono sobre los píxeles de
madera y **los números pasaron**: Δtono bajó a 3,1° y 1,9°. Pero los pisos quedaron
ROSADOS: no parecían madera. Es optimizar la métrica en vez del resultado.

La causa: el tono objetivo sale de fotos de la clienta que tienen su propia
dominante de luz. La SATURACIÓN sí se transfiere entre fotos con luz distinta —es
independiente de la exposición— pero el TONO no. Por eso el tope de tono queda como
aviso y manda el ojo; el de saturación sí es exigible.

⚠️ Las referencias de Jenny (`raw/casablanca/ref-jenny-28ago/`) son REFERENCIA, no
material: *«yo las tengo para mis post, por favor usar otras ustedes»*. No se
publican ni se recortan; sirven para fijar tono, veta y formato de tabla.

La verificación NO es opcional, y el juez es la REFERENCIA DE JENNY, no la foto
oficial del producto. Medido el 28-08: la oficial es plana de estudio y tiene croma
29,8; el mismo piso en una sala con luz, en la propia referencia de la clienta, da
croma 14-15. La oficial no es un objetivo alcanzable en un ambiente. Se comparan
TONO y CROMA, no la luminosidad — el L* depende de cuánta luz tenga la sala, que es
decisión de composición y no de fidelidad de producto. Ver `mide()`.
"""
import argparse
import base64
import json
import os
import pathlib
import ssl
import sys
import time
import urllib.request

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

RAIZ = pathlib.Path(str(_RAIZ))
ASSETS = RAIZ / "public/assets/casablanca"
DEST = ASSETS / "sep"
SSL_CTX = ssl.create_default_context()
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    pass

BASE = "https://api.freepik.com/v1/ai/mystic"
REF_JENNY = RAIZ / "raw/casablanca/ref-jenny-28ago"
# Qué foto MIDE cada SKU: la suya, la que Jenny mandó para ese producto.
REF_ARCHIVO = {"natural_uv_grande": "natural-uv-grande.jpg",
               "natural_uv_chico": "natural-uv-chico.jpg",
               "aserrado": "aserrado.jpg", "cumaru": "cumaru.jpg"}

# Qué foto GUÍA el estilo. Casi siempre la misma, con UNA excepción deliberada:
# los dos Roble Natural UV son el MISMO producto en dos formatos de tabla, así que
# tienen que salir de una sola referencia. Con una cada uno salían distintos —Serena,
# 31-08: «los dos roble natural se ven como diferentes, se supone que son los
# mismos»—: medido, mismo tono (Δ0,6°) y misma luminosidad (Δ0,1) pero satHSV 0,151
# contra 0,211, y esa diferencia se ve. Las dos fotos que ella mandó son del mismo
# piso con luz distinta, y esa diferencia de luz se estaba trasladando al producto.
# Manda la del 10, que es la que dio el resultado más cercano a las dos referencias.
REF_ESTILO = dict(REF_ARCHIVO, natural_uv_grande="natural-uv-chico.jpg")
ASPECTO = {"feed": "square_1_1", "feed45": "social_post_4_5"}

# ── La madera, dicha desde la foto oficial y desde la referencia de Jenny ────────
# Ojo: los tres robles comparten tono (72,5° · 76,3° · 78,1° en Lab; sólo el Cumarú
# se separa, 59,3°). O sea que el color NO distingue tres de los cuatro: lo que los
# separa es la TEXTURA y el FORMATO de tabla. Por eso cada prompt insiste en las
# dimensiones reales en mm y en el acabado, no sólo en el color.
TABLA = {
    "natural_uv_grande": "Wide long planks, 190 mm wide and 1900 mm long, laid "
                         "lengthwise with few seams.",
    "natural_uv_chico":  "Narrower shorter planks, 167 mm wide and 1200 mm long, so "
                         "the seams across the floor are noticeably more frequent.",
    "aserrado":          "Very wide long planks, 190 mm wide and 1900 mm long, only "
                         "three or four planks across the whole width of the frame.",
    # El Cumarú necesita decir lo que la referencia no logra imponer sola: es
    # madera TROPICAL, de veta lisa y pareja, no un roble teñido de rojo. Sin esto
    # sale un roble con figura de catedral y color terracota.
    "cumaru":            "Narrow very long planks, 120 mm wide and 2130 mm long, "
                         "laid lengthwise. It is a DARK tropical hardwood with a "
                         "deep mahogany red-brown colour, smooth uniform fine "
                         "straight grain and no knots — no oak cathedral figure, "
                         "no light streaks, not terracotta and not orange.",
}

# Se conserva sólo como registro de lo que NO funcionó: describir la madera con
# palabras. Ver el docstring de `genera()`.
MADERA = {
    "natural_uv_grande": (
        "natural oak flooring in a soft warm tan tone with clearly visible wood "
        "colour — the colour of raw untreated oak, warm but never orange and never "
        "golden-honey. It must read as real wood, NOT as grey, NOT as washed-out "
        "beige, NOT bleached or painted. Fine straight grain clearly visible, no "
        "knots at all — a clean uniform floor with absolutely no dark knots — matte UV "
        "finish. Wide long planks, 190 mm wide and 1900 mm long, laid lengthwise."
    ),
    "natural_uv_chico": (
        "natural oak flooring in a warm tan tone with a soft CARAMEL undertone, "
        "clearly warm rather than yellow — the colour of raw untreated oak. NOT "
        "grey, NOT washed-out beige, NOT bleached, NOT lemon-yellow. Fine straight "
        "grain clearly visible, no knots, matte UV finish. IDENTICAL colour and "
        "finish to the wider version of "
        "this same floor. Narrower shorter planks, 167 mm wide and 1200 mm long, so "
        "the seams across the floor are noticeably more frequent."
    ),
    "aserrado": (
        # ⚠️ Tercera redacción, 31-08. La 1ª («amber, orange-brown caramel, rustic,
        # visible dark knots») dio un pino barnizado amarillo. La 2ª («greige-taupe,
        # neither yellow nor golden») lo blanqueó: L* 66,9 contra 50,2 de la
        # referencia. Medido en la foto de la clienta, este piso es un café MEDIO y
        # bastante saturado — RGB (146,111,89), tono 58°, satHSV 0,387 — con tabla
        # muy ancha y casi sin nudos. Ni pálido ni dorado: café de madera.
        "wide-plank oak flooring in a warm MID-BROWN tone with a soft taupe cast, "
        "the colour of natural walnut-brown oak. Medium depth — NOT pale, NOT "
        "bleached, NOT whitewashed, NOT grey, and NOT yellow or golden. Completely "
        "MATTE with no sheen, no gloss and no specular reflections. Fine even grain "
        "with a soft cathedral figure and almost no knots — at most one or two very "
        "small ones. NOT knotty pine. Extremely wide long planks: only three or four "
        "planks visible across the whole width of the frame."
    ),
    "cumaru": (
        "cumaru Brazilian teak flooring in a deep RED-brown mahogany tone with a "
        "distinctly reddish undertone — clearly red-brown, not orange, not golden, "
        "not yellow-brown. Rich saturated tropical hardwood colour. Tight straight "
        "fine grain with almost no knots, warm satin sheen. Narrow very long planks, "
        "120 mm wide and 2130 mm long, laid lengthwise."
    ),
}

# ── La sala. UNA DISTINTA POR PRODUCTO — es el pedido de Jenny ───────────────────
# Todas comparten lo que el brief sí sigue pidiendo y ella no tocó:
#   nº2 plano amplio, el piso ocupa al menos la mitad del cuadro
#   nº3 habitado pero despejado, dos o tres elementos
#   nº4 luz natural y muros claros
#   nº5 el tercio superior tiene que ser muro limpio: ahí cae el bloque de texto
SALA = {
    "natural_uv_grande":
        "a double-height living room with a tall window on the left, a pale plaster "
        "wall, one low linen sofa set far back on the left and a single olive tree "
        "in a stone planter",
    "natural_uv_chico":
        "a serene open room with one tall plain wall, a slim bench set far back on "
        "the left and a single tall ceramic vase",
    "aserrado":
        "a calm minimal room with one tall plain wall and a single low linen bench "
        "set far back on the right, lit by soft even overcast daylight with NO "
        "direct sun patches falling on the floor",
    "cumaru":
        "a calm contemporary lounge with a full-height glass wall opening to a "
        "garden on the right, one low dark-green sofa set back and a round stone "
        "coffee table",
}

COMUN = (
    "Interior architectural photograph, camera at waist height angled slightly "
    "downward so the wood floor fills the entire bottom 55 percent of the frame and "
    "recedes in perspective toward the viewer. The upper third of the image must be "
    "CLEAN EMPTY WALL, with no furniture, no art and no objects. Wide empty floor "
    "area in the foreground with nothing on it. Soft natural daylight, warm neutral "
    "white balance, calm and uncluttered. Architectural Digest style, "
    "photorealistic, sharp. No people, no text, no logos, no watermark."
)


def clave():
    p = pathlib.Path.home() / ".magnific_key"
    k = os.environ.get("FREEPIK_API_KEY") or (p.read_text().strip() if p.exists() else "")
    if not k:
        sys.exit("Falta la clave: ~/.magnific_key o FREEPIK_API_KEY")
    return k


def http(url, metodo="GET", cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(url, data=datos, method=metodo, headers={
        "x-freepik-api-key": clave(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180, context=SSL_CTX) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")


def espera(task_id, etiqueta, minutos=8):
    hasta = time.time() + minutos * 60
    while time.time() < hasta:
        st, data = http(f"{BASE}/{task_id}")
        d = data.get("data", {}) if isinstance(data, dict) else {}
        estado = d.get("status")
        if estado in ("COMPLETED", "SUCCESS"):
            g = d.get("generated") or []
            if g:
                return g[0]
            return None
        if estado == "FAILED":
            print(f"  [{etiqueta}] FALLÓ: {json.dumps(data)[:300]}")
            return None
        time.sleep(5)
    print(f"  [{etiqueta}] timeout")
    return None


def genera(sku, fmt):
    """El piso se transfiere con `style_reference`, no se describe con palabras.

    Por qué: describir la madera en el prompt no funcionó. En el Aserrado se
    escribieron TRES redacciones distintas y las tres dieron un pino nórdico pálido
    con reflejos de sol — el modelo tiene un sesgo fuerte hacia ese piso y no lo
    suelta por más adjetivos que se le pongan («amber caramel» salió amarillo,
    «greige-taupe» salió blanqueado, «mid-brown walnut» volvió al pálido).

    Pasando la foto de la clienta como `style_reference` de Mystic, el material se
    transfiere de una: tono 63,6° contra 58,4° y satHSV 0,438 contra 0,387, con la
    veta fina, el mate y el ancho de tabla correctos. El prompt queda sólo para la
    SALA, que tiene que ser distinta en cada tarjeta.

    ⚠️ Esto NO publica la foto de la clienta: es referencia de estilo, la imagen
    final es otra. Es justo lo que ella pidió — «usen estas imágenes de referencia
    […] por favor usar otras ustedes».
    """
    ref = base64.b64encode((REF_JENNY / REF_ESTILO[sku]).read_bytes()).decode()
    # El prompt NO describe la madera: sólo la sala. Describirla peleaba con la
    # referencia — en el Cumarú, decirle «deep red-brown mahogany, not orange»
    # sobre una referencia caoba lo sacaba HACIA el naranjo. La imagen manda; el
    # texto sólo dice qué tabla es, que es lo único que la referencia no puede
    # transmitir (el ancho y el largo reales en mm).
    prompt = (f"{COMUN} The room is {SALA[sku]}. The floor is exactly the same wood "
              f"as the reference image — same colour, same tone, same grain, same "
              f"matte finish. {TABLA[sku]}")
    cuerpo = {"prompt": prompt, "aspect_ratio": ASPECTO[fmt], "resolution": "2k",
              "realism": True, "engine": "automatic", "creative_detailing": 20,
              "style_reference": ref}
    st, data = http(BASE, "POST", cuerpo)
    print(f"  [{sku} {fmt}] POST -> HTTP {st}")
    if st not in (200, 201):
        print(f"    {json.dumps(data)[:400]}")
        return None
    return espera(data.get("data", {}).get("task_id"), f"{sku} {fmt}")


def guarda(url, destino):
    if not url:
        return False
    destino.parent.mkdir(parents=True, exist_ok=True)
    if url.startswith("http"):
        with urllib.request.urlopen(url, timeout=300, context=SSL_CTX) as r:
            destino.write_bytes(r.read())
    else:
        destino.write_bytes(base64.b64decode(url))
    print(f"    ✓ {destino.name} ({destino.stat().st_size // 1024} KB)")
    return True


# ── la verificación ─────────────────────────────────────────────────────────────
def _lab(rgb):
    c = np.asarray(rgb, float) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[.4124, .3576, .1805], [.2126, .7152, .0722], [.0193, .1192, .9505]])
    xyz = c @ M.T / np.array([.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), xyz * 7.787 + 16 / 116)
    return np.array([116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])])


def _medio(p, z):
    a = np.asarray(Image.open(p).convert("RGB"), float)
    H, W = a.shape[:2]
    return a[int(z[1] * H):int(z[3] * H), int(z[0] * W):int(z[2] * W)].reshape(-1, 3).mean(axis=0)


def _tono_sat(rgb):
    """Tono en Lab + saturación en HSV.

    La saturación va en HSV y NO el croma de Lab, porque el croma de Lab depende de
    la luminosidad: oscurecer un color le baja el croma aunque no lo desature ni un
    poco. Medido el 28-08 — el velo multiplica el piso por 0,641 y le baja el croma
    de 15,4 a 10,7, pero su saturación HSV queda idéntica en 0,304. Con el croma yo
    había acusado al velo de despintar el producto, y el velo no tiene nada que ver:
    la madera generada ya salía con la mitad de saturación que la real.
    """
    import math, colorsys
    L, A, B = _lab(rgb)
    r, g, b = [v / 255.0 for v in rgb]
    return L, math.degrees(math.atan2(B, A)) % 360, colorsys.rgb_to_hsv(r, g, b)[1]


def mide(sku, ruta):
    """El juez es la REFERENCIA DE JENNY, no la foto oficial del producto.

    Medido el 28-08: la foto oficial es plana de estudio y tiene croma 29,8; el
    mismo piso fotografiado en una sala con luz, en la referencia de la propia
    clienta, da croma 14-15. O sea que la oficial NO es un objetivo alcanzable en un
    ambiente — la referencia de Jenny está a ΔE 17 de ella y aun así ES el producto,
    según quien lo fabrica.

    Se comparan TONO y CROMA, no la luminosidad: el L* depende de cuánta luz tenga
    la sala y eso es decisión de composición, no de fidelidad de producto.
    Así se caza el error real: el ambiente anterior tenía el tono correcto (68,8°
    contra 73,1°) pero croma 32,4 contra 15,4 — el doble de saturado. Se leía miel.
    """
    # Franja INFERIOR: es piso en cualquier composición. La zona media anterior
    # (0.30, 0.60, 0.75, 0.78) funcionaba en unas y en otras caía sobre un vano
    # oscuro o un muro — en el cuadrado del Cumarú dio satHSV 0,208 contra 0,532 y
    # el piso era rojo intenso. Un recorte fijo a media altura no sirve cuando la
    # composición cambia, y con ambientes distintos por producto cambia siempre.
    Z = (0.25, 0.80, 0.90, 0.97)
    ref = _medio(REF_JENNY / REF_ARCHIVO[sku], Z)
    piso = _medio(ruta, Z)
    Lr, hr, sr = _tono_sat(ref)
    Lp, hp, sp = _tono_sat(piso)
    d_tono = abs((hp - hr + 180) % 360 - 180)
    d_sat = abs(sp - sr)
    # El tono es AVISO, no bloqueo: las fotos de la clienta traen su propia dominante
    # de luz y el tono no se transfiere entre iluminaciones distintas (la saturación
    # sí). Dos fotos del MISMO producto, las que mandó de Natural UV, difieren 7,5°
    # entre ellas: por debajo de eso el número es ruido de la referencia.
    ok = d_tono <= 12.0 and d_sat <= 0.06
    print(f"      referencia Jenny  L*{Lr:5.1f}  tono {hr:5.1f}°  satHSV {sr:5.3f}")
    print(f"      piso generado     L*{Lp:5.1f}  tono {hp:5.1f}°  satHSV {sp:5.3f}")
    print(f"    Δtono {d_tono:4.1f}° (tope 8)   Δsat {d_sat:5.3f} (tope 0,06)   "
          f"{'✓ pasa' if ok else '⚠ NO PASA'}")
    return d_tono, d_sat


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sku", nargs="?", choices=list(MADERA))
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--fmt", default="feed45", choices=list(ASPECTO))
    ap.add_argument("--medir", action="store_true",
                    help="sólo medir lo que ya está, sin generar")
    a = ap.parse_args()
    skus = list(MADERA) if a.todos else ([a.sku] if a.sku else [])
    if not skus:
        ap.error("dime un sku o pasa --todos")

    for sku in skus:
        destino = DEST / f"amb_{sku}_{a.fmt}.jpg"
        print(f"── {sku} · {a.fmt}")
        if a.medir:
            if destino.exists():
                mide(sku, destino)
            else:
                print("    no existe todavía")
            continue
        nuevo = DEST / f"amb_{sku}_{a.fmt}.nuevo.jpg"
        if guarda(genera(sku, a.fmt), nuevo):
            mide(sku, nuevo)
            print(f"    queda en {nuevo.name} — revísala y renómbrala a mano si sirve")


if __name__ == "__main__":
    main()

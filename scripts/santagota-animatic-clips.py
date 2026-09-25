"""SANTA GOTA · animatic — placas en MOVIMIENTO (Kling 2.1 Pro vía Freepik, 5 s, en paralelo).

Sólo se animan placas SIN packaging (cocina, gota, impacto, pizza, sartén, pasta). El packshot oficial
nunca pasa por un modelo de video: entra en Remotion encima, en 2D. La única excepción es el ensayo
«mano»: se anima el envase GENÉRICO generado (v3_mano_v6_up) para estudiar el gesto; si sirve, el packshot
oficial se vuelve a pegar cuadro a cuadro con santagota-spot-mano.py. Si no sirve, el reveal va en 2D.

Uso: python3 scripts/santagota-animatic-clips.py [ids...]
Salida: public/assets/santagota/spot/clips/<id>.mp4
"""
import base64, io, json, os, ssl, sys, time, urllib.error, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik
import certifi
from PIL import Image

CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com/v1/ai"
PL = RAIZ / "public/assets/santagota/spot/plates"
OUT = RAIZ / "public/assets/santagota/spot/clips"
OUT.mkdir(parents=True, exist_ok=True)
H = {"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 CopylabStudio/1.0"}
MODELO = os.environ.get("SG_MODELO", "kling-v2-5-pro")   # 15-09 noche: kling-v2-1-pro FALLA en Freepik (error null); la 2.5 sí anda, pero sin image_tail

FISICA = ("Real physics with natural weight and inertia, locked-off camera, photographic and restrained, "
          "no morphing, no flickering, no added objects, no text, no bottle appears")

CLIPS = {
    # 01 · NORMALIDAD: casi nada pasa. Eso es el punto.
    "cliche": dict(img="01_gota_sola_v2.png", prompt=(
        "Extremely calm classic Mediterranean food scene, almost nothing moves: a faint drift of steam, the basil "
        "leaf barely trembles, the tiny drop of oil at the top falls in extreme slow motion. Nothing dramatic.")),
    # 02 · LA GOTA: descenso escultórico en cámara lentísima
    "gota": dict(img="v2_gota_descenso_v2.png", prompt=(
        "Macro: the sculptural golden olive oil drop stretches and descends in extreme slow motion toward the "
        "burrata below, the thread above it thins, light refracts inside the drop. Time almost stops.")),
    # 03 · PLOP: el impacto en el charco
    "plop": dict(img="v2_plop_v1.png", prompt=(
        "Macro slow motion: the single drop of olive oil hits the pool of oil on the white plate, a small crown "
        "splash rises and a perfect ring of ripples expands outward. Elegant, restrained.")),
    # 03→04 · PLOP → BIG BANG en un solo plano (frame final = el KV)
    "plop_bigbang": dict(img="v2_plop_v1.png", fin="v2_bigbang_b_v1.png", prompt=(
        "The drop of olive oil hits the pool and the ring of ripples expands outward as a shockwave; as the wave "
        "travels, the world around it ignites: warm fire rises at the edges, the light turns dramatic and dark, "
        "the plate becomes black wet stone. One continuous slow-motion transformation.")),
    # 04 · BIG BANG solo: la onda y el fuego viven
    "bigbang": dict(img="v2_bigbang_b_v1.png", prompt=(
        "Slow motion: the ring of ripples keeps expanding from the drop impact, the column of oil settles, the "
        "flames at the edges pulse and lick upward, embers drift slowly. The camera does not move.")),
    # 05 · PIZZA: el queso reacciona al aceite que cae en diagonal
    "pizza": dict(img="v2_pizza_limpia_v2.png", prompt=(
        "Slow motion close-up: a thin thread of olive oil falls diagonally from the top right onto the melted "
        "mozzarella, the cheese glistens, bubbles and stretches slightly where the oil lands, basil leaves settle. "
        "Very slow push-in.")),
    # 06 · SARTÉN: el flare corto y elegante
    "sarten": dict(img="v3_sarten_flare_v1.png", prompt=(
        "A short elegant tongue of orange flame rises from the far edge of the hot pan for a fraction of a second, "
        "flares once, and dies down to almost nothing; the oil shimmers and sizzles, a few tiny embers. Mostly "
        "black frame, controlled, no big fire.")),
    # 07 · PASTA: el giro y el hilo real
    "pasta": dict(img="v3_pasta_real_v3.png", prompt=(
        "Slow motion: the fork twirls the tagliatelle slowly, the thin thread of real olive oil keeps falling from "
        "above and wraps around the twirl, translucent and viscous with tiny highlights, small droplets land on the "
        "black stone. Photographic.")),
    # 11 · FIRMA: la gota final cae (sobre negro, se mezcla en screen)
    "gota_firma": dict(img="v2_gota_firma_v1_limpio.png", prompt=(
        "Macro on black: the golden olive oil drop hangs, stretches and finally detaches and falls straight down out "
        "of frame in slow motion. Pure black background stays black.")),
    # ENSAYO · la mano (envase genérico, sólo para estudiar el gesto)
    "mano_gesto": dict(img="v3_mano_v6_up.png", prompt=(
        "A real hand holds the squeeze bottle horizontally and squeezes it gently: micro tilt of the wrist, the "
        "fingers press the soft plastic, a thin thread of golden oil falls from the nozzle and thickens slightly. "
        "The bottle keeps exactly the same shape, size, label and position; camera locked; black background.")),
    "mano_entra": dict(img="__mano_fuera__", fin="v3_mano_v6_up.png", prompt=(
        "A real hand and forearm enter from the right edge of the frame holding the squeeze bottle horizontally, "
        "settle naturally with a micro tilt of the wrist, then squeeze gently and a thin thread of golden oil falls "
        "from the nozzle. The bottle keeps its exact shape and label; camera locked; black background.")),
    # ── V4 (animatic V2): MENOS ACEITE, MÁS IMPACTO ──
    "gota4": dict(img="v4_gota_v1.png", prompt=(
        "Extreme macro, extreme slow motion: the single small delicate drop of olive oil at the end of the thin thread "
        "stretches and descends slowly toward the plate below, real surface tension, slightly irregular, light "
        "refracting inside it. Only one drop, tiny, no stream. The background stays out of focus and still.")),
    "plop4": dict(img="v4_plop_v3.png", prompt=(
        "Extreme macro, high-speed slow motion: the tiny column of oil from the drop impact collapses back and a "
        "single delicate ring of ripples expands outward across the thin film of oil, physically real, restrained, "
        "no big splash, no droplets flying. Camera locked.")),
    "universo4": dict(img="v4_universo_v2.png", prompt=(
        "Slow motion on wet black stone: the glowing ring of oil ripples expands outward from the centre, the warm "
        "golden light travels along the ripple, the tiny embers drift very slowly, the light breathes. No new flames, "
        "no explosion, no smoke cloud. Camera locked, dark and premium.")),
    "pizza4": dict(img="v4_pizza_v1.png", prompt=(
        "Slow motion close-up: a VERY THIN thread of olive oil keeps falling from the top onto the mozzarella, leaving "
        "a few small glistening drops, the cheese stays matte and creamy, basil leaves settle, a very slow push-in. "
        "Only a fine line of oil, never a pool, never soaked.")),
    # ── V5 (animatic V3) ──
    "pasta5": dict(img="v3_pasta_real_v3.png", prompt=(
        "Slow motion: the fork twirls the tagliatelle slowly and ONLY a single very thin thread of olive oil keeps "
        "falling from above onto the twirl, translucent and viscous. Absolutely NO droplets flying, NO splash, NO "
        "spray, nothing in the air except the one thin thread. The surface stays as it is. Photographic, calm.")),
    "gota5": dict(img="v4_gota_libre_v1.png", prompt=(
        "Extreme macro, extreme slow motion: the single detached drop of olive oil falls slowly straight down through "
        "the frame toward the plate, keeping its delicate teardrop shape with real surface tension, nothing above it, "
        "no thread, no stream. The background stays out of focus and still.")),
    "sarten5": dict(img="v4_sarten_food_v1.png", prompt=(
        "Slow motion: the garlic, tomatoes and shrimp sizzle in the olive oil with tiny bubbles, the oil glistens, "
        "and ONE short thin tongue of flame at the far edge of the pan rises for an instant and dies down to nothing. "
        "Mostly black frame, controlled, no big fire, almost no particles.")),
    "gota5b": dict(img="v4_gota_libre_v1.png", prompt=(
        "Extreme macro, extreme slow motion, high-speed camera: a single ALREADY DETACHED drop of olive oil falls "
        "straight down through the frame. There is NOTHING above the drop: no thread, no string, no stream, no "
        "second drop, empty air above it at all times. The drop keeps a compact teardrop shape with real surface "
        "tension and lands softly on the burrata at the end. Background out of focus and perfectly still.")),
    # ── V6 (animatic V4): la persona que le echa Santa Gota a la ensalada con amigos ──
    "ensalada": dict(img="v6_ensalada_v3_up.png", prompt=(
        "Candid dinner with friends at golden hour: the woman's hand gently squeezes the bottle and a single thin "
        "thread of olive oil keeps falling onto the salad; the hand and bottle move very little, the bottle keeps "
        "exactly the same shape, size, label and position; in the background the friends laugh softly and a glass "
        "is lifted, natural small movements, candle flames flicker. Locked camera, shallow depth of field, warm.")),
    "universo_comida": dict(img="v4_universo_comida_v1.png", prompt=(
        "Slow motion: a single ring of ripples expands outward across the pool of olive oil on the plate from the "
        "centre, the hard golden side light breathes very slightly, a basil leaf trembles. Nothing else moves; the "
        "food stays exactly as it is. Locked camera, dramatic, premium, appetizing.")),
    "ensalada_b": dict(img="v6_ensalada_v3_up.png", prompt=(
        "Keep this exact composition and framing, locked camera, nothing is re-arranged: the woman's hand holding the "
        "bottle stays exactly where it is with the bottle in the exact same size, orientation and place, only a tiny "
        "natural tremor; the thin thread of oil keeps falling from the nozzle onto the salad; in the background the "
        "friends laugh softly and sip wine, candle flames flicker. Subtle, candid, photographic. No zoom, no reframing.")),
    "ensalada_c": dict(img="v7_ensalada_v1.png", prompt=(
        "Keep this exact composition and framing, locked camera, nothing is re-arranged: the woman's hand holding the "
        "bottle upside down stays exactly where it is, the bottle keeps the exact same size, orientation and place with "
        "only a tiny natural tremor; the thin thread of oil keeps falling from the yellow nozzle onto the salad; in the "
        "background the friends laugh softly, candle flames flicker. Subtle, candid, photographic. No zoom, no reframing.")),
}


def b64(ruta):
    if ruta == "__mano_fuera__":
        im = Image.open(PL / "v3_mano_v6_up.png").convert("RGB")
        fuera = Image.new("RGB", im.size, (0, 0, 0)); fuera.paste(im, (int(im.width * 0.42), 0)); im = fuera
    else:
        im = Image.open(PL / ruta).convert("RGB")
    im.thumbnail((1280, 1280))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=90)
    return base64.b64encode(buf.getvalue()).decode()


def pedir(ruta, cuerpo=None, intentos=4):
    for i in range(intentos):
        datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
        req = urllib.request.Request(BASE + ruta, data=datos, method="POST" if datos else "GET", headers=H)
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=180) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            cuerpo_e = e.read().decode(errors="ignore")[:300]
            if e.code >= 500 and i < intentos - 1:
                print(f"  HTTP {e.code} {ruta}; reintento {i + 2}"); time.sleep(10 * (i + 1)); continue
            raise SystemExit(f"✗ HTTP {e.code} {ruta}: {cuerpo_e}")


def main():
    ids = sys.argv[1:] or list(CLIPS)
    tareas = {}
    for cid in ids:
        dst = OUT / f"{cid}.mp4"
        if dst.exists():
            print(f"  ya existe {cid}"); continue
        c = CLIPS[cid]
        cuerpo = {"image": b64(c["img"]), "prompt": c["prompt"] + ". " + FISICA, "duration": "5"}
        if c.get("fin"):
            if MODELO != "kling-v2-1-pro":
                print(f"  {cid}: salta (image_tail sólo en 2.1)"); continue
            cuerpo["image_tail"] = b64(c["fin"])
        r = pedir(f"/image-to-video/{MODELO}", cuerpo)
        tareas[cid] = r["data"]["task_id"]; print(f"  enviada {cid} → {tareas[cid]}")
        time.sleep(2)
    t0 = time.time()
    while tareas and time.time() - t0 < 25 * 60:
        time.sleep(20)
        for cid, tid in list(tareas.items()):
            try:
                d = pedir(f"/image-to-video/{'kling-v2-5-pro' if MODELO == 'kling-v2-5-pro' else 'kling-v2-1'}/{tid}")["data"]
            except SystemExit as e:
                print(f"  {cid}: {e}"); continue
            st = d.get("status")
            if st == "COMPLETED":
                url = (d.get("generated") or [None])[0]
                with urllib.request.urlopen(url, context=CTX, timeout=300) as r, open(OUT / f"{cid}.mp4", "wb") as f:
                    f.write(r.read())
                print(f"  ✔ {cid} ({time.time() - t0:.0f}s)"); del tareas[cid]
            elif st in ("FAILED", "ERROR"):
                print(f"  ✘ {cid}: {json.dumps(d)[:300]}"); del tareas[cid]
    if tareas:
        print("SIN TERMINAR:", tareas)
    print("listo")


if __name__ == "__main__":
    main()

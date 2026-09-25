"""SANTA GOTA · animatic V2 — placas V4: MENOS ACEITE, MÁS IMPACTO (feedback consolidado 15-09-2026, noche).

  gota      UNA sola gota delicada y real (tensión superficial, irregular), no miel, no gel, no esfera 3D.
  plop      impacto de una gota chica en una película fina de aceite: corona pequeña, real.
  universo  el mundo DESPUÉS del cambio: piedra negra húmeda, anillo de ondas con luz dorada, apenas brasas.
            Sin explosión literal, casi sin fuego: el cambio es de luz, color y espacio.
  pizza     squeeze fino y apetitoso: hilo delgado, queso mate, sin bañar la comida.

Salida: public/assets/santagota/spot/plates/v4_<id>_vN.png   ·   Uso: python3 <script> [ids...]
"""
import json, os, ssl, sys, time, urllib.error, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik
import certifi

SSL_CTX = ssl.create_default_context(cafile=certifi.where())
DEST = RAIZ / "public/assets/santagota/spot/plates"
H = {"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 CopylabStudio/1.0"}

FOTO = ("Hyper-real television commercial food photography, Phase One medium format, {lente}, physically accurate "
        "liquids and optics, restrained and photographic, no fantasy glow, no floating sparkles, no CGI look, no "
        "illustration, no people, no hands, no text, no logos, no labels, no watermark, no bottle, 16:9 television frame.")
MACRO = FOTO.format(lente="100mm macro lens at f/4")
MEDIO = FOTO.format(lente="50mm lens at f/2")
NEGRO_ = "Absolute black background, dark brushed steel, deep contrast, contemporary, nothing rustic."

PLACAS = {
    "gota": dict(n=3, prompt=(
        "Extreme macro of ONE single small drop of extra virgin olive oil hanging and about to fall, seen against a "
        "sunlit Mediterranean kitchen far out of focus: the drop is tiny and delicate, translucent pale gold, "
        "slightly irregular, real surface tension, a thin thread above it thinning to nothing, real refraction with "
        "the window inside it. NOT honey, NOT gel, NOT a perfect sphere, NOT huge. Below and out of focus, a white "
        "plate with burrata. Sophisticated, almost excessively gourmet, warm morning light. " + MACRO)),
    "plop": dict(n=3, prompt=(
        "Extreme macro, high-speed photography: one small drop of olive oil has just touched a very thin film of olive "
        "oil on a white ceramic plate: a tiny, delicate crown splash only a few millimetres high and a single ring of "
        "ripples, physically real, translucent gold, restrained. Warm Mediterranean kitchen far out of focus. Not a big "
        "splash, not a pool, not exaggerated. " + MACRO)),
    "universo": dict(n=3, prompt=(
        "The same impact point one instant later, but the world has changed: the plate has become wet black stone, "
        "the light is dark and dramatic, a single expanding ring of oil ripples catches a thin line of warm golden-orange "
        "light, tiny embers glow at the far edges of the frame and a faint acid lime green rim light touches the left "
        "edge. Almost no fire, no explosion, no flames in the foreground, no smoke cloud. Contemporary, premium, mostly "
        "black frame with enormous contrast. " + MEDIO)),
    "pizza": dict(n=3, prompt=(
        "Close-up of a Neapolitan margherita pizza on dark slate, fresh out of the oven: a VERY THIN thread of extra "
        "virgin olive oil falls diagonally from the top right onto the mozzarella, just a fine translucent line, "
        "leaving only a few small glistening drops on the cheese. The cheese is matte and creamy, not soaked, not "
        "shiny, no pool of oil. Basil leaves, charred crust. Black background, appetizing, real. " + MEDIO)),
    # ── V5 (animatic V3): gota libre sin hilo · sartén con comida ──
    "gota_libre": dict(n=3, prompt=(
        "Extreme macro, high-speed photography: ONE single small drop of extra virgin olive oil in free fall in "
        "mid-air, already detached, no thread above it, no stream, nothing connected to it: a delicate, slightly "
        "irregular teardrop with real surface tension and the sunlit window refracted inside. Below and out of "
        "focus, a white plate with burrata in a warm Mediterranean kitchen. Sophisticated, gourmet, real. " + MACRO)),
    "sarten_food": dict(n=3, prompt=(
        "Close-up of a black carbon-steel pan on a dark stove with real food cooking in olive oil: sliced garlic, "
        "halved cherry tomatoes, a sprig of rosemary and a few shrimp sizzling and glistening, tiny bubbles in the "
        "oil around them; at the far edge of the pan ONE short thin tongue of orange flame rises for an instant, "
        "small and controlled. Most of the frame stays black, restrained, no big fire, almost no particles, no "
        "smoke cloud. Appetizing and premium. " + NEGRO_ + " " + MEDIO)),
    # ── V6 (animatic V4): el universo del cambio es COMIDA, no lava ──
    "universo_comida": dict(n=3, prompt=(
        "The same Mediterranean dish one instant after the drop of olive oil hit it, but the whole world has changed "
        "its light: the white plate with burrata, sliced tomatoes and basil now sits on wet black stone against an "
        "absolutely black background, lit by one dramatic hard golden side light with deep shadows; a single ring of "
        "ripples in the pool of olive oil catches a thin line of warm gold light; a faint acid lime green rim light "
        "touches the edge of the plate. It is clearly delicious FOOD, appetizing and premium: no fire, no lava, no "
        "embers, no smoke, no glow effects. Cinematic contrast, contemporary, restaurant-editorial. " + MEDIO)),
}


def post(ruta, cuerpo, intentos=4):
    for i in range(intentos):
        req = urllib.request.Request(f"https://api.freepik.com/v1/ai/{ruta}", data=json.dumps(cuerpo).encode(), headers=H, method="POST")
        try:
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=90) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code >= 500 and i < intentos - 1:
                print(f"  HTTP {e.code}; reintento {i + 2}/{intentos}"); time.sleep(8 * (i + 1)); continue
            print("  cuerpo:", e.read().decode(errors="ignore")[:300]); raise


def get(ruta):
    req = urllib.request.Request(f"https://api.freepik.com/v1/ai/{ruta}", headers=H)
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as r:
        return json.loads(r.read())


def main():
    pedidos = sys.argv[1:] or list(PLACAS)
    tareas = {}
    for pid in pedidos:
        p = PLACAS[pid]
        for v in range(p["n"]):
            nombre = f"v4_{pid}_v{v + 1}"
            if (DEST / f"{nombre}.png").exists():
                print(f"  ya existe {nombre}"); continue
            r = post("mystic", {"prompt": p["prompt"], "aspect_ratio": "widescreen_16_9", "resolution": "2k", "realism": True, "creative_detailing": 22})
            tareas[nombre] = r["data"]["task_id"]; print(f"  enviada {nombre}"); time.sleep(1.5)
    t0 = time.time()
    while tareas and time.time() - t0 < 15 * 60:
        time.sleep(12)
        for nombre, tid in list(tareas.items()):
            try:
                d = get(f"mystic/{tid}")["data"]
            except urllib.error.HTTPError as e:
                print(f"  {nombre}: HTTP {e.code}"); continue
            if d["status"] == "COMPLETED":
                req = urllib.request.Request(d["generated"][0], headers={"User-Agent": H["User-Agent"]})
                with urllib.request.urlopen(req, context=SSL_CTX, timeout=120) as r, open(DEST / f"{nombre}.png", "wb") as f:
                    f.write(r.read())
                print(f"  ✔ {nombre} ({time.time() - t0:.0f}s)"); del tareas[nombre]
            elif d["status"] in ("FAILED", "ERROR"):
                print(f"  ✘ {nombre}"); del tareas[nombre]
    print("listo")


if __name__ == "__main__":
    main()

"""SANTA GOTA · spot TV «UNA GOTA. CAMBIA TODO.» — placas de fondo para los 10 keyframes.

Genera con Mystic (Freepik) SOLO lo que la regla del cliente permite generar: cocina,
comida, aceite, fuego, luz, atmósfera. NUNCA el packaging: las botellas y latas entran
después como packshot oficial (public/assets/santagota/producto/) en la composición.

Dos universos con dirección de arte opuesta (Production Bible V2):
  ANTES  (01–02): mediterráneo, cálido, luminoso, predecible, bonito.
  DESPUÉS (03–10): negro, acero, fuego, aceite dorado, verde ácido, naranja. Food real.

Salida: public/assets/santagota/spot/plates/<id>[_v].png  (2k, 16:9)

Uso:  /Users/Vale/copylab-venv/bin/python3 scripts/santagota-spot-plates-freepik.py [ids...]
"""
import json, os, pathlib, ssl, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik

import certifi
SSL_CTX = ssl.create_default_context(cafile=certifi.where())

DEST = RAIZ / "public/assets/santagota/spot/plates"
DEST.mkdir(parents=True, exist_ok=True)

KEY = clave_freepik()
if not KEY:
    sys.exit("Falta la clave de Freepik (llavero / credentials/.env)")
H = {"x-freepik-api-key": KEY, "Content-Type": "application/json",
     "User-Agent": "Mozilla/5.0 CopylabStudio/1.0"}  # el WAF bloquea el UA de urllib

# Guardas de calidad comunes a todas las placas: foto publicitaria, no IA, no texto, no marca.
FOTO = ("Ultra-realistic commercial food advertising photography for television, shot on a "
        "Phase One medium format camera, {lente}, cinematic lighting, extremely shallow depth of "
        "field, physically accurate liquids and reflections, natural micro-textures, no CGI look, "
        "no illustration, no people, no faces, no hands, no text, no letters, no logos, no labels, "
        "no watermark, no bottle, 16:9 television frame.")
MACRO = FOTO.format(lente="100mm macro lens at f/4")
MEDIO = FOTO.format(lente="50mm lens at f/2.8")
TELE = FOTO.format(lente="85mm lens at f/2.8")

# Universo ANTES: el cliché que la gota viene a romper (deliberadamente bonito y tradicional).
ANTES = ("Warm golden Mediterranean daylight from a window, rustic white ceramic plate on a light "
         "linen tablecloth, soft creamy bokeh of an old-world Italian kitchen behind, calm, "
         "traditional, predictable, elegant.")
# Universo DESPUÉS: Santa Gota.
DESPUES = ("Deep black background, brushed black steel and dark stone surfaces, hard dramatic rim "
           "light from behind, high contrast, wet golden olive oil highlights, accents of acid "
           "lime green and vivid orange in the ingredients and the light, contemporary, intense, "
           "bold, irreverent, nothing rustic, nothing beige, nothing wooden.")

PLACAS = {
    # 01 EL CLICHÉ · 00:00–02.5 · gota suspendida sobre plato mediterráneo
    "01_cliche": dict(n=3, prompt=(
        "Extreme close-up of a beautiful classic Mediterranean dish: a whole creamy burrata over "
        "sliced heirloom tomatoes with fresh basil leaves and flaky sea salt, everything perfectly "
        "still. From the very top edge of the frame ONE single large drop of golden olive oil hangs "
        "suspended in mid-air above the burrata, sharply in focus, catching the light, not yet "
        "fallen; only one drop, no bubbles, no splashes, no second drop, no glass bottle anywhere. " + ANTES + " " + MACRO)),
    # 02 LA GOTA · 02.5–04.0 · la gota cae, slow motion, a punto de tocar
    "02_gota": dict(n=1, prompt=(
        "Extreme macro of one single perfect drop of golden extra virgin olive oil falling in "
        "mid-air, elongated by gravity, one millimetre above the glossy surface of a creamy "
        "burrata, frozen at 1/8000 s, the drop razor sharp and the food a warm soft blur. " +
        ANTES + " " + MACRO)),
    # 03 CAMBIA TODO · 04.0–05.0 · el impacto: corona líquida, y la luz ya cambió
    "03_impacto": dict(n=2, prompt=(
        "Extreme macro of the exact instant a single drop of golden olive oil impacts a thin film "
        "of oil: a small perfect liquid crown splash with a circular ripple wave expanding, "
        "physically real, wet and glossy, frozen at 1/8000 s. The light has changed: " + DESPUES +
        " The splash is lit from behind so the gold glows against pure black, with a subtle "
        "acid-green and orange colour split in the reflections. " + MACRO)),
    # 04 NUEVO UNIVERSO · 05.0–06.5 · sartén negra, verduras, fuego real
    "04_universo": dict(n=1, prompt=(
        "Medium shot of a black carbon-steel skillet on a professional gas burner, vegetables "
        "(green chilli, orange bell pepper, cherry tomatoes, spring onion) being tossed mid-air "
        "with a violent real flame flare bursting up from the pan, oil droplets sparkling, "
        "steam, motion. " + DESPUES + " " + MEDIO)),
    # 05 FOOD 1 · 06.5–08.0 · chorro sobre pizza (la boquilla queda fuera de cuadro)
    "05_pizza": dict(n=1, prompt=(
        "Close-up of a thin golden stream of extra virgin olive oil pouring from the top edge of "
        "the frame onto a hot artisan pizza margherita, blistered crust, melted mozzarella, torn "
        "basil, the oil pooling and glistening on the cheese, the source of the stream out of "
        "frame above. " + DESPUES + " " + TELE)),
    # 06 FOOD 2 · 08.0–09.5 · aceite sobre carne a la parrilla, fuego
    "06_carne": dict(n=1, prompt=(
        "Close-up of a thin golden stream of olive oil hitting a thick seared ribeye steak on a "
        "black cast-iron grill, coarse salt crystals, the oil flashing into sizzling smoke and "
        "small flames licking up from the grates, the source of the stream out of frame above. " +
        DESPUES + " " + TELE)),
    # 07 FOOD 3 · 09.5–10.5 · aceite recorre la pasta
    "07_pasta": dict(n=1, prompt=(
        "Close-up of golden olive oil flowing over a nest of fresh tagliatelle pasta with shaved "
        "parmesan and cracked black pepper, the oil running along the ribbons and catching a "
        "spectacular backlight, glossy, appetising, the source of the stream out of frame above. " +
        DESPUES + " " + TELE)),
    # 08 EL ORIGEN · 10.5–12.5 · fondo del reveal (la botella oficial se compone encima)
    "08_origen_fondo": dict(n=1, prompt=(
        "Dark contemporary kitchen background, softly out of focus, a black steel pan with "
        "sautéed vegetables at the bottom of the frame catching golden light, the upper two "
        "thirds of the frame empty deep black space with a faint warm haze, dramatic backlight, "
        "surfaces only of black stone and dark steel, absolutely no wood, no cutting board, no herbs. " +
        DESPUES + " " + MEDIO)),
    # 08b · el chorro solo, sobre negro puro, para componerlo desde la boquilla oficial
    "08_chorro_negro": dict(n=1, prompt=(
        "A single thin continuous stream of golden extra virgin olive oil pouring diagonally "
        "from the upper right towards the lower left, isolated on a pure black background, "
        "backlit so the liquid glows amber gold with bright specular highlights, physically "
        "accurate, glossy, slightly twisting, nothing else in the frame. " + MACRO)),
    # 09/10 HERO + FIRMA · 12.5–20.0 · set de producto vacío (los packshots oficiales van encima)
    "09_estudio": dict(n=2, prompt=(
        "Empty premium product photography set for a television commercial: a glossy black "
        "reflective surface like polished black glass, deep black background, a soft golden "
        "backlight glow low on the horizon at the centre, thin acid lime green light accent "
        "on the left edge and vivid orange light accent on the right edge, subtle warm haze, "
        "a few tiny golden oil droplets on the surface in the foreground, absolutely nothing "
        "standing on the surface, centre empty. " + MEDIO)),
    # ── Regeneraciones 15-09 (tarde): UNA sola gota, de verdad ──────────────────
    "01_gota_sola": dict(n=2, prompt=(
        "Extreme close-up of a beautiful classic Mediterranean dish: a whole creamy burrata over "
        "sliced heirloom tomatoes with fresh basil and flaky sea salt, everything perfectly still, "
        "nothing pouring. Above the burrata, in the upper centre of the frame, hangs ONE isolated "
        "spherical drop of golden olive oil suspended in mid-air, razor sharp, catching a highlight, "
        "with clear empty space around it. Exactly one drop: no stream, no thread, no pour, no "
        "bubbles, no second drop, no bottle, no spoon, no hand. " + ANTES + " " + MACRO)),
    "02_gota_sola": dict(n=2, prompt=(
        "Extreme macro, 1/8000 s freeze: ONE isolated teardrop-shaped drop of golden extra virgin "
        "olive oil falling in mid-air, two centimetres above the glossy white surface of a creamy "
        "burrata, the drop perfectly sharp and glowing, the food a warm soft blur below. Exactly one "
        "drop: no stream, no thread, no pour, no bubbles, no bottle, no spoon, no hand. " +
        ANTES + " " + MACRO)),
    "05_pizza_b": dict(n=2, prompt=(
        "Close-up of a thin golden stream of extra virgin olive oil falling from above the top "
        "edge of the frame onto a hot artisan pizza margherita, blistered leopard-spotted crust, "
        "melted mozzarella, torn basil, the oil pooling and glistening on the cheese. The stream "
        "enters from outside the frame: no bottle, no nozzle, no spout, no neck, no hand visible. " +
        DESPUES + " " + TELE)),
}


def post(ruta, cuerpo):
    req = urllib.request.Request(f"https://api.freepik.com/v1/ai/{ruta}", data=json.dumps(cuerpo).encode(),
                                 headers=H, method="POST")
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as r:
        return json.loads(r.read())


def get(ruta):
    req = urllib.request.Request(f"https://api.freepik.com/v1/ai/{ruta}", headers=H)
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as r:
        return json.loads(r.read())


def descarga(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": H["User-Agent"]})
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=120) as r, open(destino, "wb") as f:
        f.write(r.read())


def main():
    pedidos = sys.argv[1:] or list(PLACAS)
    tareas = []  # (nombre_archivo, task_id)
    for pid in pedidos:
        p = PLACAS[pid]
        for v in range(p["n"]):
            nombre = f"{pid}_v{v + 1}" if p["n"] > 1 else pid
            if (DEST / f"{nombre}.png").exists():
                print(f"  ya existe {nombre}.png — salto")
                continue
            r = post("mystic", {"prompt": p["prompt"], "aspect_ratio": "widescreen_16_9",
                                "resolution": "2k", "realism": True, "creative_detailing": 33})
            tid = r["data"]["task_id"]
            tareas.append((nombre, tid))
            print(f"  enviada {nombre} → {tid}")
            time.sleep(1.5)

    pendientes = dict(tareas)
    t0 = time.time()
    while pendientes and time.time() - t0 < 15 * 60:
        time.sleep(12)
        for nombre, tid in list(pendientes.items()):
            try:
                r = get(f"mystic/{tid}")
            except urllib.error.HTTPError as e:
                print(f"  {nombre}: HTTP {e.code}")
                continue
            st = r["data"]["status"]
            if st == "COMPLETED":
                url = r["data"]["generated"][0]
                out = DEST / f"{nombre}.png"
                descarga(url, out)
                print(f"  ✔ {nombre} ({time.time() - t0:.0f}s) → {out.relative_to(RAIZ)}")
                del pendientes[nombre]
            elif st in ("FAILED", "ERROR"):
                print(f"  ✘ {nombre}: {st} {r}")
                del pendientes[nombre]
    if pendientes:
        print("SIN TERMINAR:", list(pendientes))
    print("listo")


if __name__ == "__main__":
    main()

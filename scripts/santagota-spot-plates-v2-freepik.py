"""SANTA GOTA · spot TV «UNA GOTA. CAMBIA TODO.» — placas V2 (segunda dirección creativa, 15-09-2026).

Qué cambió respecto a la V1 (feedback de Valeria):
  - El impacto de la gota es EL PLANO de la campaña: un big bang gastronómico en macro. La onda avanza
    y por donde pasa el mundo mediterráneo se apaga, la superficie se vuelve negra, se enciende fuego,
    vuelan microgotas, cambia la luz. Tiene que funcionar congelado como KV.
  - Tres acciones distintas en el food (nada de «chorro vertical sobre X»): squeeze DIAGONAL sobre
    pizza y el queso reacciona · aceite entra a la sartén y FLASH de fuego · tenedor gira la pasta y un
    hilo de aceite envuelve el giro y sale de cuadro.
  - Códigos de marca antes del reveal: verde ácido en una luz, naranja en el fuego.
  - La gota es un gesto propietario: escultórica, reconocible, abre y cierra el spot.
  - Hero carísimo: negro absoluto, superficie húmeda, halo naranja detrás de la naranja, halo verde detrás
    de la verde, aceite dorado muy desenfocado en primer plano.
  - Menos «golden fantasy», menos partículas decorativas, física impecable.

Sigue sin generar packaging: el producto entra después como packshot oficial.
Salida: public/assets/santagota/spot/plates/v2_<id>[_vN].png · Uso: python3 <script> [ids...]
"""
import json, os, ssl, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik
import certifi

SSL_CTX = ssl.create_default_context(cafile=certifi.where())
DEST = RAIZ / "public/assets/santagota/spot/plates"
DEST.mkdir(parents=True, exist_ok=True)
KEY = clave_freepik() or sys.exit("Falta la clave de Freepik")
H = {"x-freepik-api-key": KEY, "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 CopylabStudio/1.0"}

FOTO = ("Hyper-real television commercial food photography, shot on a Phase One medium format camera with a "
        "{lente}, physically accurate liquids, real optics, extremely shallow depth of field, natural "
        "micro-textures, restrained and photographic, no fantasy glow, no floating sparkles, no CGI look, no "
        "illustration, no people, no faces, no hands, no text, no letters, no logos, no labels, no watermark, "
        "no bottle, 16:9 television frame.")
MACRO = FOTO.format(lente="100mm macro lens at f/4")
MEDIO = FOTO.format(lente="50mm lens at f/2")
TELE = FOTO.format(lente="85mm lens at f/2.8")

ANTES = ("Warm soft Mediterranean window daylight, rustic white ceramic plate on natural linen, creamy bokeh "
         "of an old Italian kitchen behind, calm, classic, predictable, elegant.")
DESPUES = ("Absolute black background, wet black stone and dark brushed steel, hard rim light from behind, "
           "deep contrast, golden olive oil highlights, one accent of acid lime green light and one accent "
           "of vivid orange light, contemporary, intense, nothing rustic, nothing beige, nothing wooden.")

PLACAS = {
    # 02 · LA GOTA — macro imposible: una gota escultórica descendiendo, el tiempo detenido
    "gota_descenso": dict(n=2, prompt=(
        "Extreme macro, time frozen: ONE large sculptural teardrop of golden extra virgin olive oil "
        "falling through the air, filling almost half the height of the frame, glass-like, perfectly "
        "smooth, catching one crisp window highlight, razor sharp; far below and completely out of focus "
        "a creamy burrata on a white plate. Exactly one drop: no stream, no thread, no bubbles, no second "
        "drop, no bottle, no spoon. " + ANTES + " " + MACRO)),
    # gesto propietario · la gota sola sobre negro (para componerla al inicio y al cierre)
    "gota_firma": dict(n=2, prompt=(
        "Extreme macro of ONE perfect sculptural teardrop of golden olive oil suspended in mid-air, "
        "isolated on a pure black background, backlit so the gold glows from inside with one crisp "
        "specular highlight, glass-like surface, physically accurate refraction, nothing else in the "
        "frame, no reflections on the ground, no surface. " + MACRO)),
    # 03 · PLOP — el instante del impacto: corona líquida, la onda recién nace, el mundo aún cálido
    "plop": dict(n=2, prompt=(
        "Extreme macro, 1/8000 s: the exact instant a single drop of golden olive oil hits a thin film "
        "of oil on a white ceramic plate: a small perfect liquid crown rising, a first tight circular "
        "ripple just born around it. The world around is still the warm classic Mediterranean table, "
        "soft and calm. " + ANTES + " " + MACRO)),
    # 04 · BIG BANG — EL PLANO. La onda avanza y por donde pasa el mundo cambia físicamente
    "bigbang": dict(n=3, prompt=(
        "Extreme macro of a gastronomic big bang: from the point where a single drop of golden olive oil "
        "has just hit, a circular shockwave ripple of oil expands outward and physically transforms the "
        "world as it passes. INSIDE the ring the surface has become wet black stone, real orange fire is "
        "igniting along the wave front, tiny oil droplets are thrown into the air, and the light is hard, "
        "dark and contemporary with an acid lime green rim light on one side and vivid orange fire light "
        "on the other. OUTSIDE the ring, at the edges of the frame, the old world still survives: a warm "
        "classic Mediterranean plate with tomatoes and burrata on linen, soft window light, dimming as the "
        "wave reaches it. A liquid crown still rises at the centre. Physically real, wet, glossy, "
        "photographic; not a sci-fi explosion. " + MACRO)),
    # 05 · PIZZA — el squeeze cruza en diagonal y el queso reacciona
    "pizza_diag": dict(n=2, prompt=(
        "Close-up of a hot artisan pizza margherita with leopard-spotted crust: a thin stream of golden "
        "olive oil crosses the frame DIAGONALLY from the lower left to the upper right, entering from "
        "outside the frame, and where it lands the melted mozzarella reacts, bubbling and glistening, with "
        "a strand of cheese lifting. Strong side light, dark background. The source of the stream is "
        "outside the frame: no bottle, no nozzle, no spout, no hand. " + DESPUES + " " + TELE)),
    # 06 · SARTÉN — el aceite entra y FLASH de fuego (naranja = código de marca)
    "sarten_flash": dict(n=2, prompt=(
        "Close-up, the exact instant a splash of olive oil hits a screaming hot black carbon-steel pan: "
        "a violent orange flash of real flame bursts up and fills the upper half of the frame, oil "
        "droplets sparkling in the heat, black steel, black background, the flame light painting "
        "everything vivid orange. Physically real fire, not CGI. " + DESPUES + " " + MEDIO)),
    # 07 · PASTA — el tenedor gira, el hilo de aceite envuelve el giro (verde ácido = código de marca)
    "pasta_giro": dict(n=2, prompt=(
        "Close-up of a steel fork twirling a nest of fresh tagliatelle in mid-air, motion in the pasta, "
        "and a single thin thread of golden olive oil spiralling around the twirl and leaving the frame "
        "towards the upper right. Black background, acid lime green rim light from the left edge, warm "
        "key light. Only the fork and the pasta: no hand, no plate, no bottle. " + DESPUES + " " + TELE)),
    # 08 · REVEAL — el vacío negro donde aparece la boquilla y luego la botella
    "reveal_vacio": dict(n=1, prompt=(
        "Almost pure black frame: a dark professional kitchen far out of focus, only a faint warm haze and "
        "one thin acid lime green light accent low on the left, nothing recognisable, no objects in focus, "
        "empty centre. " + DESPUES + " " + MEDIO)),
    # 08 · el hilo de aceite subiendo hacia su origen, sobre negro (se compone desde la boquilla)
    "hilo_negro": dict(n=1, prompt=(
        "A single thin continuous thread of golden olive oil rising vertically from the bottom edge of "
        "the frame to the exact top centre, isolated on a pure black background, backlit amber gold with "
        "crisp specular highlights, slightly twisting, physically accurate, nothing else. " + MACRO)),
    # 09/10 · HERO — negro absoluto, superficie húmeda, halo naranja izquierda / halo verde derecha
    "hero_set": dict(n=2, prompt=(
        "Empty cinematic product set: an absolute black background and a wet black glossy floor with "
        "partial reflections and a few water droplets, a soft vivid ORANGE halo of light low on the LEFT "
        "half and a soft ACID LIME GREEN halo of light low on the RIGHT half, both behind the floor line "
        "at the horizon, dark centre, nothing standing on the floor, no props, no smoke. " + MEDIO)),
    # primer plano de aceite muy desenfocado para cruzar delante del hero
    "hero_fg_aceite": dict(n=1, prompt=(
        "A thick stream of golden olive oil crossing the frame diagonally, extremely out of focus, as a "
        "soft amber bokeh smear, isolated on a pure black background, no sharp edges anywhere. " + MACRO)),
    # ── Regeneraciones (tarde) ──────────────────────────────────────────────
    "bigbang_b": dict(n=2, prompt=(
        "Extreme macro, 1/8000 s, of a gastronomic big bang: a single drop of golden olive oil has just hit "
        "the centre and a perfect liquid crown rises there; a circular shockwave ripple expands from it. The "
        "frame is split by that ring: INSIDE the ring the surface is now wet black stone with small real "
        "orange flames igniting along the wave front and tiny oil droplets thrown into the air, hard dark "
        "contemporary light with an acid lime green rim on the left and vivid orange fire light on the right. "
        "OUTSIDE the ring, filling the four corners of the frame, the old world is still there and clearly "
        "visible: a warm classic Mediterranean table with a white ceramic plate, sliced tomatoes, burrata and "
        "basil on natural linen in soft window light, just starting to dim. Photographic, wet, glossy, "
        "physically real; not a sci-fi explosion. " + MACRO)),
    "pizza_diag_b": dict(n=2, prompt=(
        "Close-up of a hot artisan pizza margherita with a leopard-spotted crust, dark background, strong "
        "side light. A single thin stream of golden olive oil enters from the UPPER RIGHT corner of the frame "
        "and travels in a straight DIAGONAL line down to the lower left, landing on the melted mozzarella, "
        "which bubbles and lifts a strand of cheese where the oil hits. The stream comes from outside the "
        "frame: no bottle, no nozzle, no spout, no neck, no glass, no hand. " + DESPUES + " " + TELE)),
    # pizza SIN chorro: la diagonal se compone en Remotion (chorro sobre negro + boquilla oficial)
    "pizza_limpia": dict(n=2, prompt=(
        "Close-up of a hot artisan pizza margherita with a leopard-spotted crust seen from a low angle, "
        "melted mozzarella glistening, a few basil leaves, dark black slate background, strong hard side "
        "light from the right, the upper left third of the frame is empty deep black space. Absolutely no "
        "oil being poured, no stream, no drops in the air, no bottle, no hand. " + DESPUES + " " + TELE)),
}


def post(ruta, cuerpo, intentos=4):
    """POST con reintento: Freepik devuelve 500 esporádicos al encolar (15-09-2026)."""
    for i in range(intentos):
        req = urllib.request.Request(f"https://api.freepik.com/v1/ai/{ruta}", data=json.dumps(cuerpo).encode(), headers=H, method="POST")
        try:
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code >= 500 and i < intentos - 1:
                print(f"  HTTP {e.code} al enviar; reintento {i + 2}/{intentos}"); time.sleep(8 * (i + 1)); continue
            raise


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
    tareas = []
    for pid in pedidos:
        p = PLACAS[pid]
        for v in range(p["n"]):
            nombre = f"v2_{pid}_v{v + 1}" if p["n"] > 1 else f"v2_{pid}"
            if (DEST / f"{nombre}.png").exists():
                print(f"  ya existe {nombre}.png — salto"); continue
            r = post("mystic", {"prompt": p["prompt"], "aspect_ratio": "widescreen_16_9", "resolution": "2k",
                                "realism": True, "creative_detailing": 28})
            tareas.append((nombre, r["data"]["task_id"])); print(f"  enviada {nombre}")
            time.sleep(1.5)
    pendientes = dict(tareas); t0 = time.time()
    while pendientes and time.time() - t0 < 15 * 60:
        time.sleep(12)
        for nombre, tid in list(pendientes.items()):
            try:
                r = get(f"mystic/{tid}")
            except urllib.error.HTTPError as e:
                print(f"  {nombre}: HTTP {e.code}"); continue
            st = r["data"]["status"]
            if st == "COMPLETED":
                descarga(r["data"]["generated"][0], DEST / f"{nombre}.png")
                print(f"  ✔ {nombre} ({time.time() - t0:.0f}s)"); del pendientes[nombre]
            elif st in ("FAILED", "ERROR"):
                print(f"  ✘ {nombre}: {st}"); del pendientes[nombre]
    if pendientes:
        print("SIN TERMINAR:", list(pendientes))
    print("listo")


if __name__ == "__main__":
    main()

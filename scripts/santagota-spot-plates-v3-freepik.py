"""SANTA GOTA · spot TV — placas V3: sólo los 4 cuadros críticos (06 sartén · 07 pasta · 08 reveal · 09 hero).

Regla global de Valeria (15-09-2026): «menos efectos = más premium; nada debe parecer generado por IA».
  06  flare breve, lateral, elegante; fuego −60 %, casi sin partículas. No «sartén incendiándose».
  07  aceite REAL: translúcido, viscoso, irregular, con refracción y highlights. Nada de «golden CGI ribbon».
  08  PROHIBIDO producto flotando: una mano real sostiene el squeeze horizontal desde fuera de cuadro.
      → se genera la mano con un squeeze GENÉRICO oscuro (Nano Banana con el packshot oficial de referencia
        para que la pose y la escala calcen) y en composición el packshot oficial va encima del envase
        generado, con los dedos recuperados delante por máscara de piel. El packaging final sigue siendo el original.
  09  set negro casi absoluto, superficie húmeda apenas visible, SIN nubes de color (el rim va en el packshot).

Salida: public/assets/santagota/spot/plates/v3_<id>[_vN].png
Uso: python3 <script> [ids...]     (ids de PLACAS = Mystic · «mano» = Nano Banana)
"""
import base64, json, os, ssl, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik
import certifi

SSL_CTX = ssl.create_default_context(cafile=certifi.where())
DEST = RAIZ / "public/assets/santagota/spot/plates"
KEY = clave_freepik() or sys.exit("Falta la clave de Freepik")
H = {"x-freepik-api-key": KEY, "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 CopylabStudio/1.0"}

FOTO = ("Hyper-real television commercial food photography, Phase One medium format, {lente}, physically "
        "accurate liquids and optics, extremely shallow depth of field, restrained and photographic, no fantasy "
        "glow, no floating sparkles, no CGI look, no illustration, no people, no faces, no text, no logos, no "
        "labels, no watermark, no bottle, 16:9 television frame.")
MACRO = FOTO.format(lente="100mm macro lens at f/4")
MEDIO = FOTO.format(lente="50mm lens at f/2")
TELE = FOTO.format(lente="85mm lens at f/2.8")
NEGRO = ("Absolute black background, wet black stone and dark brushed steel, deep contrast, contemporary, "
         "nothing rustic, nothing beige, nothing wooden.")

PLACAS = {
    # 06 · SARTÉN — flare breve y hermoso, no incendio
    "sarten_flare": dict(n=3, prompt=(
        "Close-up of a black carbon-steel pan on a dark stove, the instant a splash of olive oil touches the "
        "hot steel: ONE short, thin, elegant tongue of orange flame rises sideways from the far edge of the pan, "
        "small and controlled, lasting a fraction of a second, lighting the rim of the pan and the oil with a "
        "warm orange glow. Most of the frame stays black. Very few sparks, almost no particles, no smoke cloud, "
        "no big fire, no inferno. " + NEGRO + " " + MEDIO)),
    # 07 · PASTA — el hilo de aceite REAL envolviendo el giro
    "pasta_real": dict(n=3, prompt=(
        "Close-up of a steel fork twirling a nest of fresh tagliatelle in mid-air. A single thin thread of real "
        "extra virgin olive oil falls onto the twirl and wraps around it: the oil is translucent, viscous, "
        "slightly irregular, with true refraction, tiny highlights and a few micro droplets, exactly like real "
        "olive oil filmed at high speed — NOT a solid golden ribbon, NOT CGI. Black background, a thin acid lime "
        "green rim light from the left edge, warm key light. Only the fork and the pasta: no hand, no plate, "
        "no bottle. " + NEGRO + " " + TELE)),
    # 09 · HERO — negro casi absoluto, superficie húmeda apenas visible, sin color
    "hero_negro": dict(n=2, prompt=(
        "Empty premium beauty-product set for a television commercial: an almost absolutely black frame, a wet "
        "black glossy floor barely visible with a faint horizon line and one or two tiny water droplets, a very "
        "subtle neutral warm haze far behind, no coloured lights, no glow, no props, nothing standing on the "
        "floor, enormous negative space. " + MEDIO)),
}

MANO_PROMPT = (
    "Photorealistic television commercial frame, 16:9, absolute black background. A real human hand and "
    "forearm enter from the RIGHT edge of the frame holding THIS EXACT squeeze bottle horizontally in the same position and size as in the reference, the nozzle "
    "pointing to the LEFT, squeezing it gently; the composition is a 16:9 wide frame like the reference; a single thin thread of golden olive oil falls straight down "
    "from the nozzle tip. Keep the bottle exactly as in the reference: same proportions, same label, same colours, "
    "same yellow nozzle. Dramatic thin rim light on the hand and the bottle, deep black shadows, shallow depth of "
    "field, Phase One medium format, 85mm, physically real skin, no face, no second hand, no text."
)


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


def descarga(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": H["User-Agent"]})
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=120) as r, open(destino, "wb") as f:
        f.write(r.read())


def espera(tareas, t0):
    pendientes = dict(tareas)
    while pendientes and time.time() - t0 < 15 * 60:
        time.sleep(12)
        for nombre, (ruta, tid) in list(pendientes.items()):
            try:
                r = get(f"{ruta}/{tid}")
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


def main():
    pedidos = sys.argv[1:] or (list(PLACAS) + ["mano"])
    tareas = []
    for pid in pedidos:
        if pid == "mano":
            # referencia: el packshot oficial del 750 aplanado sobre negro, a ~1024 px (payload chico)
            from PIL import Image
            # referencia 16:9 con el packshot YA horizontal (boquilla a la izquierda): el modelo copia el aspecto de la referencia
            tmp = "/tmp/sg_ref_750_h.png"
            b64 = base64.b64encode(open(tmp, "rb").read()).decode()
            for v in range(3, 6):
                nombre = f"v3_mano_v{v + 1}"
                if (DEST / f"{nombre}.png").exists():
                    print(f"  ya existe {nombre}"); continue
                r = post("gemini-2-5-flash-image-preview", {"prompt": MANO_PROMPT, "reference_images": [b64]})
                tareas.append((nombre, ("gemini-2-5-flash-image-preview", r["data"]["task_id"]))); print(f"  enviada {nombre}")
                time.sleep(1.5)
            continue
        p = PLACAS[pid]
        for v in range(p["n"]):
            nombre = f"v3_{pid}_v{v + 1}" if p["n"] > 1 else f"v3_{pid}"
            if (DEST / f"{nombre}.png").exists():
                print(f"  ya existe {nombre}"); continue
            r = post("mystic", {"prompt": p["prompt"], "aspect_ratio": "widescreen_16_9", "resolution": "2k",
                                "realism": True, "creative_detailing": 22})
            tareas.append((nombre, ("mystic", r["data"]["task_id"]))); print(f"  enviada {nombre}")
            time.sleep(1.5)
    espera(tareas, time.time())
    print("listo")


if __name__ == "__main__":
    main()

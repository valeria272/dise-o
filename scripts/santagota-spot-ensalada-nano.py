"""SANTA GOTA · animatic V4 · reveal «con amigos»: una persona le echa Santa Gota a una ensalada en una mesa con amigos.

Nano Banana con REFERENCIA del packshot oficial ya en pose de vertido (16:9): la pose, la escala y la luz vienen de
ahí, pero ESE envase no se entrega. Después Kling anima la escena y el packshot oficial se pega cuadro a cuadro
(santagota-spot-mano-video.py, modo lifestyle). El packaging nunca lo dibuja ni lo anima un modelo.

Uso: python3 scripts/santagota-spot-ensalada-nano.py   → plates/v6_ensalada_vN.png (3 variantes)
"""
import base64, io, json, os, ssl, sys, time, urllib.error, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ, clave_freepik
import certifi
from PIL import Image

CTX = ssl.create_default_context(cafile=certifi.where())
DEST = RAIZ / "public/assets/santagota/spot/plates"
H = {"x-freepik-api-key": clave_freepik(), "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 CopylabStudio/1.0"}

PROMPT_ABIERTO = (
    "Photorealistic television commercial frame, 16:9, wide shot of a long dinner table on a terrace at golden hour, "
    "five or six friends around it laughing and talking, candid documentary feel. In the middle distance on the right "
    "side of the table, one woman standing slightly, seen from the chest up, holds THIS EXACT squeeze bottle upside "
    "down with the YELLOW NOZZLE pointing DOWN and pours a single thin thread of olive oil onto a big fresh salad in "
    "a ceramic bowl in front of her; the bottle is small in frame (about one sixth of the frame height), exactly as "
    "in the reference in size, orientation and position. Keep the bottle exactly as in the reference: same proportions, "
    "same label, same colours, same yellow nozzle. Natural warm light, shallow depth of field on the table, bread, "
    "wine, tomatoes, no text, no logos elsewhere."
)
PROMPT = (
    "Photorealistic television commercial frame, 16:9, warm golden-hour dinner on a terrace with friends. In the "
    "upper right, a real woman's hand and forearm hold THIS EXACT squeeze bottle by its body, upside down and tilted "
    "exactly as in the reference: the YELLOW NOZZLE points DOWN toward the salad and a single thin thread of golden "
    "olive oil falls straight down FROM THE YELLOW NOZZLE TIP onto a big fresh Mediterranean salad (tomatoes, burrata, "
    "basil, arugula) in a ceramic bowl in the lower centre. The bottle's base is up, held in the hand; the nozzle is "
    "the lowest point of the bottle. Two or three friends laughing softly out "
    "of focus in the background, wine glasses, bread, candles, bokeh. Keep the bottle exactly as in the reference: same "
    "proportions, same label, same colours, same yellow nozzle, same size and position. Shallow depth of field, Phase One, "
    "50mm, physically real skin, natural, candid, no faces in focus, no text."
)


ABIERTO = "--abierto" in sys.argv


def referencia():
    """Packshot oficial en pose de vertido sobre negro, 1344×768 (el modelo copia el aspecto de la referencia)."""
    pk = Image.open(RAIZ / "public/assets/santagota/spot/producto/hero4-750.png").convert("RGBA")
    h = 300 if ABIERTO else 620; pk = pk.resize((int(pk.width * h / pk.height), h), Image.LANCZOS)
    pk = pk.rotate(150, expand=True, resample=Image.BICUBIC)    # boquilla ABAJO (un poco a la izquierda): vertiendo sobre la ensalada
    ref = Image.new("RGB", (1344, 768), (0, 0, 0)); ref.paste(pk, (1344 - pk.width - 180, 20) if not ABIERTO else (860, 150), pk)
    tmp = "/tmp/sg_ref_750_vertido.png"; ref.save(tmp); return tmp


def post(ruta, cuerpo, intentos=4):
    for i in range(intentos):
        req = urllib.request.Request(f"https://api.freepik.com/v1/ai/{ruta}", data=json.dumps(cuerpo).encode(), headers=H, method="POST")
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=90) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code >= 500 and i < intentos - 1:
                print(f"  HTTP {e.code}; reintento"); time.sleep(8 * (i + 1)); continue
            raise SystemExit(f"✗ HTTP {e.code}: {e.read().decode(errors='ignore')[:300]}")


def main():
    b64 = base64.b64encode(open(referencia(), "rb").read()).decode()
    tareas = {}
    for v in range(1, 4):
        nombre = f"v8_mesa_v{v}" if ABIERTO else f"v7_ensalada_v{v}"
        if (DEST / f"{nombre}.png").exists():
            print("  ya existe", nombre); continue
        r = post("gemini-2-5-flash-image-preview", {"prompt": PROMPT_ABIERTO if ABIERTO else PROMPT, "reference_images": [b64]})
        tareas[nombre] = r["data"]["task_id"]; print("  enviada", nombre); time.sleep(1.5)
    t0 = time.time()
    while tareas and time.time() - t0 < 10 * 60:
        time.sleep(10)
        for nombre, tid in list(tareas.items()):
            req = urllib.request.Request(f"https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview/{tid}", headers=H)
            with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
                d = json.loads(r.read())["data"]
            if d["status"] == "COMPLETED":
                req = urllib.request.Request(d["generated"][0], headers={"User-Agent": H["User-Agent"]})
                with urllib.request.urlopen(req, context=CTX, timeout=120) as r, open(DEST / f"{nombre}.png", "wb") as f:
                    f.write(r.read())
                print(f"  ✔ {nombre} ({time.time() - t0:.0f}s)"); del tareas[nombre]
            elif d["status"] in ("FAILED", "ERROR"):
                print("  ✘", nombre); del tareas[nombre]
    print("listo")


if __name__ == "__main__":
    main()

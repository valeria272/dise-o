# -*- coding: utf-8 -*-
"""MyZoo · Paid Fase 3 — FONDOS de los 6 estáticos, sin producto.

Decisión de Paulina (02-10-2026): se dejan de pelear los envases y se generan
primero TODAS las escenas de fondo, con el animal cerca, en primer plano y con
conexión (mirando a cámara). El producto entra después, sobre la superficie
que cada escena deja vacía.

Cada escena se pide desde cero y sólo con texto (APRENDIZAJES R-44, R-51): foto
de cámara real, pelaje mate y desordenado, living moderno (R-35), todo limpio
(R-21), un cuarto del alto libre arriba para el titular (R-43).

Uso:
    python scripts/myzoo-f3-fondos.py                 # todas las piezas
    python scripts/myzoo-f3-fondos.py p07 p08         # sólo ésas
    python scripts/myzoo-f3-fondos.py p01 --tanda b   # otra tanda, sin pisar la anterior

Deja las tomas en raw/myzoo/fase3/fondos/ (borradores, no viajan en git).
"""
import subprocess, sys, pathlib, concurrent.futures as cf

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "raw" / "myzoo" / "fase3" / "fondos"

CAMARA = ("Candid lifestyle photograph taken in a real home, shot on a Canon EOS R5, {lente}, ISO 400, "
          "natural late-afternoon window light. Unretouched editorial photo, square frame. ")

REAL = (" Real photograph look: true-to-life colours, neutral white balance with gentle warm sunlight, "
        "soft realistic shadows, no HDR, no retouching, no glow. Natural matte fur with fine individual "
        "hairs, slightly uneven and a little messy, real fabric and wood textures, subtle sensor grain. "
        "The home is modern, tidy and spotless. No people's faces, no text, no logos, no packaging, "
        "no bottles, no extra objects.")

ESCENAS = {
    # P01 · Pet Wipes desde $2.990 — tres envases acostados, cada uno con su precio.
    "p01": ("50mm lens at f/4",
            "High-angle view, camera looking down at about 60 degrees. Golden late-afternoon sun, warm honey "
            "and cream tones throughout, long soft warm shadows. The top quarter of the frame is only "
            "soft out-of-focus cream wool rug, calm and empty. A modern light oak coffee table with a smooth "
            "matte top and fine straight grain fills the lower left: its surface is completely bare and empty "
            "and occupies the left 45 percent of the frame from the middle down to the bottom edge. On the "
            "right, an adult golden retriever sits on the rug very close to the camera, large in the frame, "
            "its chin resting on the right edge of the table, eyes looking straight up into the lens with a "
            "soft, loving expression. The whole head and shoulders are inside the frame. Sunlight comes from "
            "the upper right."),
    # P02 · 3 productos por $24.990 — eliminador de olores + shampoo de avena + espuma repelente.
    # (tanda b: la tanda a salió fría, con el perro lejos y «sonriendo»; se pide cálida,
    #  el perro más cerca y con el hocico cerrado.)
    "p02": ("50mm lens at f/2.8",
            "Eye-level view in a warm living room, golden late-afternoon sun, cream and beige palette, a "
            "pale linen sofa softly out of focus behind. The top quarter of the frame is a plain warm cream "
            "wall, calm and empty. A modern light oak coffee table with a smooth matte oak top crosses the "
            "bottom of the frame: its top is completely bare and empty and takes the left 55 percent of the "
            "frame width. On the right, very close to the camera and filling the right 45 percent of the "
            "frame, a medium mixed-breed dog with floppy ears and a medium-length honey-coloured coat rests "
            "its chin on the edge of the table, mouth closed, looking straight into the lens with soft, "
            "attentive eyes. Its whole head is inside the frame. Sunlight from the left."),
    # (tanda c, 02-10: P01 más cálida; P07 manta color caramelo, el perro blanco se perdía sobre
    #  la manta blanca; P08 sofá color caramelo, la escena se veía muy blanca.)
    # P07 · ¿Cómo limpiar a una mascota con piel sensible? — tip, pregunta protagonista.
    "p07": ("35mm lens at f/2.8",
            "First-person point of view of the owner sitting on a warm beige linen sofa, camera looking down at "
            "their lap. A small white Maltese-mix dog lies relaxed on a caramel-brown knitted wool blanket, very close to "
            "the camera and large in the frame, looking up straight into the lens with calm, trusting eyes. "
            "One adult hand enters from the bottom right and gently wipes the dog's front paw with a plain "
            "white soft cloth wipe. Only the hand and forearm are visible. The top quarter of the frame is "
            "soft out-of-focus sofa fabric, calm and empty. Golden late-afternoon sunlight from the upper left, warm tones."),
    # P08 · Higiene sin estrés para tu gato — calma, sin agua; misma paleta de la 07.
    # (tanda b: en la tanda a el gato salió dormido y chico; sin mirada no hay conexión.)
    "p08": ("85mm lens at f/2.8",
            "Eye-level close-up in a warm living room, golden late-afternoon sun, cream and beige palette. "
            "An adult grey tabby cat lies relaxed on a cream cotton blanket on a caramel-brown fabric sofa, very close "
            "to the camera: its head and front paws fill the lower right half of the frame, chin resting on "
            "its paws, eyes fully open looking straight into the lens with a calm, content expression. The "
            "top quarter of the frame is a plain warm cream wall softly out of focus, calm and empty. The "
            "left third of the blanket in the foreground is flat, smooth and empty. Soft warm window light "
            "from the left."),
    # P09 · Pet Wipes en dos tamaños — el de 110 y el de 15, diferencia de tamaño clara.
    "p09": ("50mm lens at f/4",
            "High-angle view, camera looking down at about 55 degrees, in a bright entrance hall with pale "
            "walls. A modern light oak bench with a smooth matte top runs across the lower part of the "
            "frame: its surface is completely bare and empty and fills the left 55 percent of the frame. "
            "The top quarter of the frame is a plain pale wall, calm and empty. On the right, a beagle sits "
            "on a light wooden floor right beside the bench, close to the camera and large in the frame, a "
            "leash hanging loosely from its collar, head tilted, looking up straight into the lens with "
            "bright eager eyes, as if just back from a walk. Sunlight from the upper right."),
    # P10 · Todo para su higiene, en un solo lugar — bodegón de la línea completa.
    "p10": ("35mm lens at f/4",
            "Eye-level view of a bright, modern laundry and bathroom corner with pale walls. A long light "
            "oak shelf with a smooth matte top crosses the frame at mid height from the left edge to "
            "70 percent of the width: the shelf is completely bare and empty. The top quarter of the frame "
            "is a plain pale wall, calm and empty. In the lower right foreground, close to the camera, a "
            "border collie and a ginger cat sit side by side on a light floor, both looking straight into "
            "the lens with gentle expressions, the dog slightly taller. A folded cream towel rests on the "
            "floor behind them. Soft warm window light from the right."),
}

# Dos tomas de Seedream 5 Pro y una de Nano Banana Pro por pieza: los dos dieron
# foto creíble el 01-10 cuando se les pidió desde cero.
TOMAS = [("seedream", "s1"), ("seedream", "s2"), ("pro", "n1")]


def genera(pieza, motor, toma, tanda):
    lente, escena = ESCENAS[pieza]
    prompt = CAMARA.format(lente=lente) + escena + REAL
    destino = OUT / f"{pieza}_{tanda}_{toma}.png"
    r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "magnific.py"), motor, prompt,
                        "--aspecto", "feed", "--out", str(destino)],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    ok = r.returncode == 0 and any(OUT.glob(destino.stem + "*"))
    cola = (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]
    return f"{'✓' if ok else '✗'} {destino.name} · {cola[0][:160]}"


def main():
    args = sys.argv[1:]
    tanda = "a"
    if "--tanda" in args:
        i = args.index("--tanda")
        tanda = args[i + 1]
        del args[i:i + 2]
    piezas = args or list(ESCENAS)
    OUT.mkdir(parents=True, exist_ok=True)
    trabajos = [(p, m, t, tanda) for p in piezas for m, t in TOMAS]
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for linea in ex.map(lambda x: genera(*x), trabajos):
            print(linea, flush=True)


if __name__ == "__main__":
    main()

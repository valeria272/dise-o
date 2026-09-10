#!/usr/bin/env python3
"""
TRAVERSO × COPYLAB — «Los de siempre»: casting, sets y keyframes del reel.

Biblia: clients/traverso/reel-los-de-siempre/BIBLIA.md. Cada clave de PLANOS es
un keyframe; se puede regenerar uno solo con --solo.

Todo con Nano Banana Pro y REFERENCIAS: los packshots reales de la línea 350 g
(nunca un personaje text-only) y, a partir del segundo paso, el HERO TRIO
MASTER aprobado, que fija proporción, vestuario y set.

    python3 scripts/traverso-lds-keyframes.py --solo master_trio
    python3 scripts/traverso-lds-keyframes.py                 # todo lo que falte
    python3 scripts/traverso-lds-keyframes.py --rehacer --solo k07b
"""
import argparse, os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(RAIZ, "public", "assets", "traverso", "lds")
PACK = os.path.join(RAIZ, "raw", "traverso", "packshots")
MAGNIFIC = os.path.join(RAIZ, "scripts", "magnific.py")
PY = sys.executable

REF_AJI = os.path.join(PACK, "aji-crema-350g.png")
REF_MOS = os.path.join(PACK, "mostaza-350g.png")
REF_KET = os.path.join(PACK, "ketchup-350g.png")
PACKS = [REF_AJI, REF_MOS, REF_KET]

MASTER = os.path.join(A, "casting", "master_trio.png")          # smokings cerrados
MASTER_V1 = os.path.join(A, "casting", "master_trio_v1.png")    # v1: pose y set buenos, smoking abierto y piernas negras
MASTER_OPEN = os.path.join(A, "casting", "master_trio_open.png")  # smokings abiertos
CORREDOR = os.path.join(A, "sets", "corredor.png")
BOARD = os.path.join(A, "sets", "boardroom.png")

# --- TRAVERSO_CHARACTER_BIBLE (verbatim en cada prompt) ---------------------
BIBLE = (
    "CHARACTER BIBLE: three anthropomorphic characters whose TORSO IS THE REAL Traverso "
    "350 g squeeze bottle from the reference photos, standing exactly as sold: blue cap at "
    "the base at hip level like a belt, rounded bottle top as the head. NO human head, NO "
    "face, NO eyes, NO mouth. Slim humanoid arms from the bottle shoulders ending in white "
    "gloves; slim legs below the blue cap and glossy leather shoes, both in the product "
    "colour. Perfectly tailored black tuxedo jacket, white dress shirt, black bow tie at the "
    "bottle neck. AJI CREMA orange on the LEFT, MOSTAZA mustard-yellow in the CENTRE one step "
    "ahead, KETCHUP red on the RIGHT. Total height about 5.5 heads, identical proportions and "
    "identical bottle size for the three. Label geometry, text and colours exactly as the "
    "reference, never rewritten. "
)
NEG = (
    "Strictly: no cartoon, no Pixar, no mascot look, no human face, no eyes, no mouth, no "
    "floating limbs, no extra fingers, no altered packaging, no rewritten label, no morphing, "
    "no hats, no extra accessories, no exaggerated gestures, no dancing, no comedy acting, no "
    "neon, no cyberpunk, no camera shake, no watermark, no text overlays."
)
SET1 = (
    "SET: infinite pitch-black studio, wet glossy black floor with controlled reflections, "
    "three warm tungsten (3200K) theatrical spotlights from above, one per character, very "
    "subtle volumetric haze, deep blacks, no visible walls, nothing recognisable. Colour "
    "appears only through the characters and their individual lights; no golden backdrop. "
)
LOOK = (
    "Photoreal premium product-film / fashion-film look, Saint Laurent - Tom Ford campaign "
    "mood, 85mm lens, low camera, moderate depth of field, deadpan and dignified, they "
    "genuinely believe they are stars. "
)
SAME = ("Preserve EXACTLY the character design, bottle size, wardrobe, gloves, shoes and the "
        "set lighting of the master reference image. ")

# (aspecto, prompt, refs)
PLANOS = {
    # ---------- CASTING ----------
    "casting/master_trio": ("reel",
        "HERO TRIO MASTER, full body, frontal, the three characters standing still facing "
        "camera side by side, arms relaxed at their sides, Mostaza one step ahead in the "
        "centre. Same pose, same set, same camera and same character design as the first "
        "reference image, with TWO corrections: (1) the tuxedo jackets are BUTTONED CLOSED "
        "and completely cover the label, only a narrow strip of white shirt and the black bow "
        "tie show at the bottle neck, and the bottle top above the jacket keeps the product "
        "colour; (2) the legs below the blue cap are the PRODUCT COLOUR (orange, mustard "
        "yellow, red), matte like the bottle plastic, not black trousers. "
        + BIBLE + SET1 + LOOK + NEG,
        [MASTER_V1, *PACKS]),

    # ---------- CHARACTER LOCK (una ficha por personaje) ----------
    "casting/ficha_aji": ("wide",
        "CHARACTER SHEET of AJI CREMA only (the orange one), four full-body views side by side "
        "on the same black studio floor under one warm spotlight: FRONT, THREE-QUARTER, PROFILE "
        "and BACK, arms relaxed, jacket buttoned. The other two characters do not appear. "
        + SAME + BIBLE + LOOK + NEG, [None, REF_AJI]),
    "casting/ficha_mostaza": ("wide",
        "CHARACTER SHEET of MOSTAZA only (the mustard-yellow one), four full-body views side by "
        "side on the same black studio floor under one warm spotlight: FRONT, THREE-QUARTER, "
        "PROFILE and BACK, arms relaxed, jacket buttoned. The other two characters do not appear. "
        + SAME + BIBLE + LOOK + NEG, [None, REF_MOS]),
    "casting/ficha_ketchup": ("wide",
        "CHARACTER SHEET of KETCHUP only (the red one), four full-body views side by side on the "
        "same black studio floor under one warm spotlight: FRONT, THREE-QUARTER, PROFILE and "
        "BACK, arms relaxed, jacket buttoned. The other two characters do not appear. "
        + SAME + BIBLE + LOOK + NEG, [None, REF_KET]),

    # ---------- KEYFRAMES · ACTO I ----------
    "keyframes/k01a": ("reel",
        "SHOT 01 START: extreme low locked camera 15 cm above the wet black floor, 85mm. Frame "
        "shows ONLY the lower legs and the glossy leather shoes of the three characters, far "
        "from camera (shoes small in frame, about one third up), mid-stride walking towards the "
        "lens: orange legs and shoes on the left, mustard-yellow in the centre slightly ahead, "
        "red on the right. Reflections on the wet floor, one warm spotlight pool from above, "
        "darkness beyond. No bottles or jackets visible, no faces. " + SAME + BIBLE + SET1 + LOOK + NEG,
        [None]),
    "keyframes/k01b": ("reel",
        "SHOT 01 END: EXACTLY the same low camera, lens and lighting as the reference image, "
        "but the three pairs of legs and shoes are now CLOSE to the lens filling the lower "
        "half of the frame, the yellow right shoe landing flat on the wet floor in the centre "
        "foreground, orange legs left, red legs right, mid-stride. Only legs and shoes, "
        "reflections on the wet floor. " + SAME + BIBLE + SET1 + LOOK + NEG,
        ["@keyframes/k01a", None]),
    "keyframes/k02a": ("reel",
        "SHOT 02 START: frontal low camera at knee height, 85mm. The three characters are FAR "
        "from camera as pure BLACK SILHOUETTES walking towards the lens, backlit by one strong "
        "warm tungsten spotlight behind them at floor level that blooms through subtle haze; "
        "their shapes (bottle top, jacket shoulders, legs) readable but no colour or detail "
        "yet, only faint rim light on the edges; long reflections on the wet floor. Mostaza in "
        "the centre one step ahead. " + SAME + BIBLE + SET1 + LOOK + NEG, [None]),
    "keyframes/k02b": ("reel",
        "SHOT 02 END: EXACTLY the same camera, lens and backlight as the reference image, but "
        "the three silhouettes have walked CLOSER, now filling most of the frame height, still "
        "mostly silhouetted with warm rim light revealing a hint of orange (left), yellow "
        "(centre, ahead) and red (right) on the bottle edges. " + SAME + BIBLE + SET1 + LOOK + NEG,
        ["@keyframes/k02a", None]),

    # ---------- KEYFRAMES · ACTO II (inserts) ----------
    "keyframes/k03": ("reel",
        "SHOT 03: medium close-up, three-quarter view of AJI CREMA alone (the orange one) as his "
        "own warm spotlight switches on above him, the other two out of frame in darkness. He "
        "has just stopped and is adjusting the left cuff of his tuxedo with his right white "
        "glove, effortless and relaxed, shoulders a little soft. 85mm, moderate depth of field, "
        "no face. " + "CONTINUITY: his tuxedo jacket is BUTTONED CLOSED exactly as in the master reference, the label is NOT visible, only the white shirt strip and bow tie show at the bottle neck; the bottle keeps EXACTLY the rounded top shape of the master, no nozzle, no cap on top. FRAMING: medium shot from the blue cap at the bottom edge up to the bottle top near the upper edge, character centred. " + SAME + BIBLE + SET1 + LOOK + NEG,
        [None]),
    "keyframes/k04": ("reel",
        "SHOT 04: medium close-up, frontal, of MOSTAZA alone (the mustard-yellow one) under his "
        "own warm spotlight, the others out of frame in darkness. Both white gloves are up at "
        "the bow tie, straightening it, calm and sure, the leader. 85mm, moderate depth of "
        "field, no face. " + "CONTINUITY: his tuxedo jacket is BUTTONED CLOSED exactly as in the master reference, the label is NOT visible, only the white shirt strip and bow tie show at the bottle neck; the bottle keeps EXACTLY the rounded top shape of the master, no nozzle, no cap on top. FRAMING: medium shot from the blue cap at the bottom edge up to the bottle top near the upper edge, character centred. " + SAME + BIBLE + SET1 + LOOK + NEG,
        [None]),
    "keyframes/k05": ("reel",
        "SHOT 05: medium close-up, three-quarter view of KETCHUP alone (the red one) under his "
        "own warm spotlight, the others out of frame in darkness. He is smoothing the right "
        "lapel of his tuxedo with one white glove in a dry, precise movement, posture very "
        "straight, bodyguard energy. 85mm, moderate depth of field, no face. " + "CONTINUITY: his tuxedo jacket is BUTTONED CLOSED exactly as in the master reference, the label is NOT visible, only the white shirt strip and bow tie show at the bottle neck; the bottle keeps EXACTLY the rounded top shape of the master, no nozzle, no cap on top. FRAMING: medium shot from the blue cap at the bottom edge up to the bottle top near the upper edge, character centred. " 
        + SAME + BIBLE + SET1 + LOOK + NEG, [None]),

    # ---------- KEYFRAMES · ACTO III ----------
    "keyframes/k07b": ("reel",
        "SHOT 07 END - THE REVEAL: EXACTLY the same frontal full-body framing, camera, pose and "
        "set as the reference master image, but the three characters now hold their tuxedo "
        "jackets WIDE OPEN with both white gloves gripping the lapels, revealing the REAL "
        "Traverso 350 g bottle and its full label exactly as in the product reference photos "
        "(AJI CREMA orange left, MOSTAZA yellow centre, KETCHUP red right), white shirt fronts "
        "pushed aside, each lit by his own spotlight, the labels clean and legible. "
        + SAME + BIBLE + SET1 + LOOK + NEG, [None, *PACKS]),

    # ---------- KEYFRAMES · ACTO IV y V ----------
    "keyframes/k09a": ("reel",
        "SHOT 09 START: camera BEHIND the three characters at hip height, 85mm. We see their "
        "BACKS full body (black tuxedo backs, product-colour legs and shoes, blue caps at hip "
        "level, rounded bottle tops) walking away from camera down the dark corridor towards "
        "the black door with the warm light at its edges and the brass 'GRUPO COPYLAB' plaque "
        "of the reference set image, still some distance away. Orange on the left, yellow "
        "centre one step ahead, red on the right. Wet floor reflections, subtle haze. "
        + SAME + BIBLE + LOOK + NEG, [None, "@sets/puerta_copylab"]),
    "keyframes/k09b": ("reel",
        "SHOT 09 END: EXACTLY the same camera, corridor and door as the reference images, but "
        "the three characters seen from behind have now ARRIVED at the door, which is opening "
        "and spilling warm daylight over them and the wet floor; Mostaza in the centre is one "
        "step ahead with a white glove on the door, the brass 'GRUPO COPYLAB' plaque readable "
        "on the right. " + SAME + BIBLE + LOOK + NEG, ["@keyframes/k09a", None, "@sets/puerta_copylab"]),
    "keyframes/k11": ("reel",
        "SHOT 11 - THE PUNCHLINE: EXACTLY the same meeting room, camera, framing and warm "
        "natural light as the reference room image, but now the three characters are SEATED "
        "in the three black leather chairs on the far side of the table facing camera, jackets "
        "buttoned, perfectly still and serious as if waiting for a strategy meeting to start: "
        "AJI CREMA (orange) on the left, MOSTAZA (yellow) in the centre with both white gloves "
        "resting flat on the table, KETCHUP (red) on the right very upright. Laptop, notebooks, "
        "coffee cups and documents on the table as in the reference; a small folded white "
        "table card in front of Mostaza reads exactly 'NUEVO CLIENTE'. No humans. No comedy "
        "acting. " + SAME + BIBLE + LOOK + NEG, [None, "@sets/boardroom", *PACKS]),

    # Alternativa IA al composite (los packshots reales son de 400 px). Sin personajes.
    "keyframes/k08_ia": ("reel",
        "PRODUCT HERO: the three REAL Traverso 350 g squeeze bottles from the reference photos "
        "standing upright side by side on the wet glossy black floor of the reference set, "
        "exactly as sold (blue cap at the base), AJI CREMA orange on the left, MOSTAZA yellow in "
        "the centre slightly ahead, KETCHUP red on the right, each under its own warm tungsten "
        "spotlight from above, reflections on the wet floor, subtle haze, deep blacks. The "
        "labels are reproduced EXACTLY as in the reference photos, same layout, same words, "
        "same colours, nothing rewritten, crisp and legible. Bottles about one third of the "
        "frame height. Frontal camera at bottle height, 85mm, premium product film. No "
        "characters, no arms, no legs, no tuxedos, no extra text. " + NEG,
        ["@sets/corredor", *PACKS]),
    # ---------- SETS (vacíos) ----------
    "sets/corredor": ("reel",
        "EXACTLY the same set, camera height and framing as the reference image but "
        "COMPLETELY EMPTY: no characters, no bottles, nobody. Just the infinite black studio, "
        "the wet glossy black floor with the reflections of the three warm tungsten "
        "spotlights above, very subtle volumetric haze, deep blacks, no walls. Photoreal, "
        "85mm, low camera. No text, no watermark.",
        [MASTER_V1]),
    "sets/boardroom": ("reel",
        "Empty meeting room of a contemporary creative advertising agency in Santiago, seen "
        "frontally from the head of a long dark walnut table at seated eye level: THREE empty "
        "black leather chairs on the far side of the table facing camera, a laptop, two "
        "notebooks, three ceramic coffee cups and a few printed documents on the table, glass "
        "partition behind with a small discreet frosted 'GRUPO COPYLAB' logo on the glass, "
        "warm natural window light from the side, a plant, very subtle peach-pink accents "
        "(a chair cushion, a notebook cover). Premium, real, cool agency; not corporate grey, "
        "not futuristic. Photoreal, 50mm, moderate depth of field, vertical 9:16. No people. "
        "No other text.",
        []),
    "sets/puerta_copylab": ("reel",
        "Contemporary minimalist entrance seen frontally from a low camera at hip height in a "
        "dark corridor: a tall black door with a warm light glowing at its edges, a small "
        "brushed-brass plaque on the wall to its right that reads exactly 'GRUPO COPYLAB' in "
        "clean sans-serif capitals, wet glossy black floor reflecting a warm tungsten "
        "spotlight from above, subtle haze, deep blacks. Same black-studio universe as the "
        "reference image. Photoreal, 85mm, vertical 9:16. No people, no other text.",
        [MASTER_V1]),
    "casting/master_trio_open": ("reel",
        "HERO TRIO, full body, frontal, the three characters standing still facing camera, "
        "each one holding his tuxedo jacket wide OPEN with both white-gloved hands on the "
        "lapels, revealing the real bottle and its full label exactly as in the reference "
        "photos, white shirt panels pushed to the sides. " + SAME + BIBLE + SET1 + LOOK + NEG,
        [None, *PACKS]),  # None → MASTER
}


def ruta(k):
    return os.path.join(A, k + ".png")


def generar(k, aspecto, prompt, refs):
    out = ruta(k)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    refs = [MASTER if r is None else (ruta(r[1:]) if r.startswith("@") else r) for r in refs]
    for r in refs:
        if not os.path.isfile(r):
            sys.exit(f"✗ falta la referencia {r} para {k}")
    if len(prompt) > 3000:
        sys.exit(f"✗ {k}: prompt de {len(prompt)} caracteres (máx 3000)")
    cmd = [PY, MAGNIFIC, "pro", prompt, "--out", out, "--aspecto", aspecto,
           "--resolucion", "2K", "--refs", *refs]
    print(f"\n=== {k} ({len(prompt)} chars, {len(refs)} refs)")
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", nargs="*")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()
    claves = a.solo or list(PLANOS)
    for k in claves:
        if k not in PLANOS:
            sys.exit(f"✗ no existe el plano {k}")
        if os.path.isfile(ruta(k)) and not a.rehacer:
            print(f"· {k} ya existe"); continue
        generar(k, *PLANOS[k])


if __name__ == "__main__":
    main()

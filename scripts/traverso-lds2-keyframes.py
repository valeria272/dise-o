#!/usr/bin/env python3
"""
TRAVERSO × COPYLAB — «Los de siempre» v2 (brief final 09-09-2026).

Canon nuevo: línea 450 g con boquilla (Mostaza Suave amarilla · Mostaza Tradicional
dorada · Ketchup rojo) y anatomía de CORPÓREO (brazos cortos, piernas muy cortas,
pies grandes). Fases con compuerta: no se avanza sin aprobación de los masters.

    python3 scripts/traverso-lds2-keyframes.py --solo casting/trio_master
Salida: public/assets/traverso/lds2/
"""
import argparse, os, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(RAIZ, "public", "assets", "traverso", "lds2")
MAGNIFIC = os.path.join(RAIZ, "scripts", "magnific.py")
P = os.path.join(A, "packshots")
REF_SUAVE = os.path.join(P, "mostaza-suave-450g.png")
REF_TRAD = os.path.join(P, "mostaza-tradicional-450g.png")
REF_KET = os.path.join(P, "ketchup-450g.png")
PACKS = [REF_SUAVE, REF_TRAD, REF_KET]
FICHAS = [os.path.join(A, "casting", f"master_{n}.png") for n in ("mostaza_suave", "mostaza_tradicional", "ketchup")]
MASTER = os.path.join(A, "casting", "trio_master.png")
MASTER_V1 = os.path.join(A, "casting", "trio_master_v1.png")  # diseño aprobado; el del centro salió más grande

BIBLE = (
    "CHARACTER BIBLE: three advertising-costume (Chilean 'corporeo') characters whose whole "
    "body IS the real Traverso 450 g squeeze bottle from the reference photos, upright "
    "exactly as sold, the conical nozzle cap on top acting as the head. NO added head, NO "
    "face, NO eyes, NO mouth, NO hair, NO hat. SHORT THICK simplified arms grow directly from "
    "the sides of the bottle and end in round white mascot gloves. VERY SHORT thick "
    "cylindrical legs come out directly under the bottle base (no thighs, no knees, no "
    "ankles, nothing human) and end in BIG rounded mascot feet in the product colour. Premium "
    "black tuxedo jacket tailored to the bottle: long, black satin lapels, white shirt front "
    "and black bow tie just under the nozzle ring; the bottle geometry stays readable through "
    "the clothes. LEFT: MOSTAZA SUAVE, bright yellow bottle and yellow feet. CENTRE, one step "
    "ahead: MOSTAZA TRADICIONAL, metallic gold bottle and gold feet, the leader. RIGHT: "
    "KETCHUP, red bottle and red feet. The three bottles have identical size and proportions. "
    "WARDROBE (final rule): the tuxedo shoulders start IMMEDIATELY under the cap's neck ring, using the bottle's natural upper widening as the shoulder line; the arms are born there and hang down (same length as before). A WHITE SHIRT FRONT with buttons and a BLACK BOW TIE are visible right under the neck ring, in every view. The jacket is LONG like a real man's tuxedo: it covers the WHOLE label, including the product-name line at the bottom, and its hem ends just above the bottle base where the legs start; only a thin strip of bottle colour shows above the legs. Lapels run from the neck down over the covered label. "
    "Labels, caps and colours exactly as the photos, never rewritten. "
)
NEG = ("No face, no eyes, no mouth, no human legs, no knees, no morphing, no altered packaging, "
       "no rewritten label, no neon, no watermark.")
SET1 = ("SET: infinite pitch-black studio, wet glossy black floor with controlled reflections, "
        "warm tungsten (3200K) theatrical spotlights from above, one per character, minimal "
        "volumetric haze, deep blacks, nothing recognisable. ")
LOOK = ("Photoreal premium fashion-film look, 85mm, low camera, deadpan. ")
SAME = ("Preserve EXACTLY the character design, bottle size, limb lengths, feet, gloves, tuxedo "
        "and lighting of the master reference image. ")

def ficha_a(nombre, color, ref):
    return ("wide",
        f"CHARACTER MASTER SHEET of {nombre} only ({color}), THREE full-body views side by side "
        "on a black studio floor under one warm spotlight: FRONT, THREE-QUARTER and PROFILE, arms "
        "relaxed. The bottle is the product in the reference photo with its vintage label. The "
        "tuxedo jacket is LONG like a real man's tuxedo: from the shoulders right under the neck "
        "ring down to just above the legs, covering the ENTIRE label including the product-name "
        "line; only a thin strip of bottle colour shows above the legs. White shirt front with "
        "buttons and black bow tie visible under the neck ring in every view. "
        + BIBLE + LOOK + NEG, [ref])

def ficha_b(nombre, color, ref):
    return ("wide",
        f"Same character sheet as the reference (same {color} bottle, label, cap, legs, feet, "
        "gloves, shoulders, shirt and bow tie, same three views FRONT / THREE-QUARTER / PROFILE) "
        "with ONE change only: the tuxedo jacket is about 30% LONGER, its hem now reaching just "
        "above the legs so that the label is COMPLETELY hidden, including the bottom line with "
        "the product name and '450g'; only a thin strip of bottle colour remains above the legs. "
        "Nothing else changes. " + BIBLE + LOOK + NEG,
        [os.path.join(A, "casting", "ronda3", f"master_{nombre.lower().replace(' ', '_')}.png"), ref])

def ficha(nombre, color, ref):
    return ("wide",
        f"CHARACTER MASTER SHEET of {nombre} only ({color}, feet in the SAME colour as the bottle, "
        f"label reading exactly '{nombre}' as in the product photo), THREE full-body views side by "
        "side on the same black studio floor under one warm spotlight: FRONT, THREE-QUARTER and "
        "PROFILE, arms relaxed, tuxedo buttoned. Use the FIRST reference image (the yellow "
        "character sheet) ONLY as the rule for WHERE the wardrobe sits: shoulders starting right "
        "under the cap's neck ring, arms born there, bow tie in the top third of the bottle, "
        "jacket hem at 60-65% of the bottle body. The bottle itself is the product in the SECOND "
        "reference photo, with its complete vintage label printed on it: the lower part of the "
        "label (product name, 'MÁS DE 125 AÑOS', '450g') stays VISIBLE below the jacket hem, and "
        "the upper part shows between the lapels; the black 'ALTO EN' warning seals stay at the "
        "TOP of the bottle next to the shoulder, exactly where the photo has them, never lower. Legs, feet and gloves as in the yellow sheet. "
        "The other two characters do not appear. " + BIBLE + LOOK + NEG,
        [os.path.join(A, "casting", "ronda2", f"master_{nombre.lower().replace(' ', '_')}.png"), ref])

PLANOS = {
    "casting/trio_master": ("reel",
        "TRIO MASTER, full body, frontal, perfectly symmetric: the three characters standing "
        "still facing camera side by side, arms relaxed, tuxedo jackets buttoned and covering "
        "the middle of the label, Mostaza Tradicional one step ahead in the centre, each under "
        "his own spotlight. Same character design, set and camera as the first reference "
        "image, with ONE correction: the THREE bottles are EXACTLY THE SAME HEIGHT and width; "
        "Mostaza Tradicional is only a small step ahead so it appears barely larger, not a "
        "bigger bottle. " + "LABELS ARE SACRED: each bottle carries its real VINTAGE ornamental label copied exactly from the product photo references: decorative framed border, small 'desde 1896', the banner 'TRADICIÓN FAMILIAR', the big 'TRAVERSO' wordmark, then the product name ('MOSTAZA SUAVE' / 'MOSTAZA TRADICIONAL' / 'KETCHUP'), 'MÁS DE 125 AÑOS' and '450g'. Do NOT simplify or modernise the label, do NOT invent a new label, do NOT add a bow tie above the label: the bow tie sits at the jacket collar over the lower part of the label. " + BIBLE + SET1 + LOOK + NEG, [MASTER_V1, *PACKS]),
    "casting/trio_master_b": ("reel",
        "TRIO MASTER, full body, frontal, perfectly symmetric: the three characters standing "
        "still facing camera side by side, arms relaxed, tuxedo jackets buttoned over the lower "
        "half of the label, Mostaza Tradicional a small step ahead in the centre, each under his "
        "own spotlight. The THREE bottles are EXACTLY the same height and width. Same character "
        "design as the reference image. " + "LABELS ARE SACRED: each bottle carries its real VINTAGE ornamental label copied exactly from the product photo references: decorative framed border, small 'desde 1896', the banner 'TRADICIÓN FAMILIAR', the big 'TRAVERSO' wordmark, then the product name ('MOSTAZA SUAVE' / 'MOSTAZA TRADICIONAL' / 'KETCHUP'), 'MÁS DE 125 AÑOS' and '450g'. Do NOT simplify or modernise the label, do NOT invent a new label, do NOT add a bow tie above the label: the bow tie sits at the jacket collar over the lower part of the label. " + BIBLE + SET1 + LOOK + NEG, [MASTER_V1, *PACKS]),
    "casting/trio_master_r5a": ("reel",
        "TRIO MASTER, full body, frontal, symmetric: the three characters from the three "
        "character-sheet references standing still side by side on the wet black studio floor, "
        "each under his own warm spotlight, arms relaxed. MOSTAZA SUAVE (yellow) LEFT, MOSTAZA "
        "TRADICIONAL (gold) CENTRE half a step ahead, KETCHUP (red) RIGHT, identical bottle "
        "height. Each wears EXACTLY the wardrobe of his sheet: long black tuxedo jacket "
        "BUTTONED CLOSED so the label is completely hidden, white shirt front and black bow tie "
        "under the neck ring, very short thick legs and big rounded feet in the product colour. "
        + BIBLE + SET1 + LOOK + NEG, FICHAS),
    "casting/trio_master_r5b": ("reel",
        "Group portrait, full body, frontal, of the three character-sheet characters shoulder to "
        "shoulder on the wet black floor under three warm spotlights, jackets BUTTONED CLOSED "
        "exactly as in the sheets (no label visible), white shirt and black bow tie on each, "
        "yellow MOSTAZA SUAVE left, gold MOSTAZA TRADICIONAL centre slightly ahead, red KETCHUP "
        "right, same bottle height, short thick legs and big mascot feet. " + BIBLE + SET1 + LOOK + NEG, FICHAS),
    "casting/trio_master_r4a": ("reel",
        "TRIO MASTER, full body, frontal, symmetric: the three approved characters from the "
        "three character-sheet references side by side on the wet black studio floor, each "
        "under his own warm spotlight, arms relaxed, tuxedos buttoned. MOSTAZA SUAVE (yellow) "
        "LEFT, MOSTAZA TRADICIONAL (gold) CENTRE half a step ahead, KETCHUP (red) RIGHT. ALL "
        "THREE wear the SAME wardrobe: black tuxedo with satin lapels starting right under the "
        "cap's neck ring, WHITE SHIRT FRONT and BLACK BOW TIE visible on each of the three in the "
        "top third of the bottle, LONG jacket covering the whole label down to just above the legs. ALL THREE have the same VERY "
        "SHORT thick corporeo legs and big rounded feet in the product colour (no trousers, no "
        "human legs). Identical bottle height. Vintage labels exactly as the sheets and photos. "
        + BIBLE + SET1 + LOOK + NEG, [*FICHAS, *PACKS]),
    "casting/trio_master_r4b": ("reel",
        "Group portrait, full body, frontal, of the three characters from the character-sheet "
        "references, shoulder to shoulder on the wet black floor under three warm spotlights: "
        "yellow MOSTAZA SUAVE left, gold MOSTAZA TRADICIONAL centre slightly ahead, red KETCHUP "
        "right, same bottle height. Each of the THREE shows a white shirt front and a black bow "
        "tie just under the neck ring, LONG tuxedo jacket hiding the whole label down to just above "
        "the legs, very short thick legs and big rounded mascot feet in the product colour. "
        "Vintage labels exactly as the sheets and photos. " + BIBLE + SET1 + LOOK + NEG, [*FICHAS, *PACKS]),
    "casting/trio_master_r2a": ("reel",
        "TRIO MASTER, full body, frontal, perfectly symmetric: compose the THREE approved "
        "characters from the three character-sheet references standing still side by side on "
        "the same wet black studio floor, each under his own warm spotlight, arms relaxed, "
        "tuxedos buttoned: MOSTAZA SUAVE (yellow, from sheet 1) on the LEFT, MOSTAZA "
        "TRADICIONAL (gold, from sheet 2) in the CENTRE a small step ahead, KETCHUP (red, from "
        "sheet 3) on the RIGHT. All three bottles EXACTLY the same height and width, same feet "
        "size, same arm length. Copy each character's vintage label exactly from its sheet and "
        "from the product photos. " + BIBLE + SET1 + LOOK + NEG, [*FICHAS, *PACKS]),
    "casting/trio_master_r2b": ("reel",
        "Full-body frontal group portrait of the three approved character-sheet characters, "
        "shoulder to shoulder facing camera on the wet black studio floor under three warm "
        "spotlights, tuxedos buttoned, arms relaxed, identical bottle height for the three, the "
        "gold MOSTAZA TRADICIONAL in the centre half a step ahead, yellow MOSTAZA SUAVE left, red "
        "KETCHUP right, vintage labels exactly as in the sheets and product photos. "
        + BIBLE + SET1 + LOOK + NEG, [*FICHAS, *PACKS]),
    "casting/master_mostaza_suave_a": ficha_a("MOSTAZA SUAVE", "the yellow one", REF_SUAVE),
    "casting/master_mostaza_tradicional_a": ficha_a("MOSTAZA TRADICIONAL", "the gold one", REF_TRAD),
    "casting/master_ketchup_a": ficha_a("KETCHUP", "the red one", REF_KET),
    "casting/master_mostaza_suave_b": ficha_b("MOSTAZA SUAVE", "yellow", REF_SUAVE),
    "casting/master_mostaza_tradicional_b": ficha_b("MOSTAZA TRADICIONAL", "gold", REF_TRAD),
    "casting/master_ketchup_b": ficha_b("KETCHUP", "red", REF_KET),
    "casting/master_mostaza_suave": ficha("MOSTAZA SUAVE", "the yellow one", REF_SUAVE),
    "casting/master_mostaza_tradicional": ficha("MOSTAZA TRADICIONAL", "the gold one", REF_TRAD),
    "casting/master_ketchup": ficha("KETCHUP", "the red one", REF_KET),
}

def ruta(k): return os.path.join(A, k + ".png")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--solo", nargs="*"); ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()
    for k in (a.solo or PLANOS):
        asp, prompt, refs = PLANOS[k]; out = ruta(k)
        if os.path.isfile(out) and not a.rehacer: print(f"· {k} ya existe"); continue
        refs = [MASTER if r is None else (ruta(r[1:]) if r.startswith("@") else r) for r in refs]
        for r in refs:
            if not os.path.isfile(r): sys.exit(f"✗ falta {r}")
        if len(prompt) > 3000: sys.exit(f"✗ {k}: {len(prompt)} chars")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        print(f"\n=== {k} ({len(prompt)} chars, {len(refs)} refs)")
        subprocess.run([sys.executable, MAGNIFIC, "pro", prompt, "--out", out, "--aspecto", asp,
                        "--resolucion", "2K", "--refs", *refs], check=True)


# =====================================================================
# FASE 3 (sets) + FASE 4 (11 keyframes) — CHARACTER LOCK FINAL 09-09-2026
# Fuente visual obligatoria: casting/LOCKED/*. Cerrado → refs fichas/trío;
# reveal → trío + packshots.
# =====================================================================
LOCK_TRIO = os.path.join(A, "casting", "LOCKED", "TRIO_MASTER_FINAL.png")
LOCK_SUAVE = os.path.join(A, "casting", "LOCKED", "CHARACTER_MASTER_mostaza_suave.png")
LOCK_TRAD = os.path.join(A, "casting", "LOCKED", "CHARACTER_MASTER_mostaza_tradicional.png")
LOCK_KET = os.path.join(A, "casting", "LOCKED", "CHARACTER_MASTER_ketchup.png")
CORREDOR = os.path.join(A, "sets", "corredor.png")
BOARD = os.path.join(A, "sets", "boardroom.png")
ENTRADA = os.path.join(A, "sets", "entrada_copylab.png")

LOCKED = ("CHARACTER LOCK: reproduce the LOCKED characters of the reference images EXACTLY — same "
          "bottle, cap, proportions, very short legs, big feet, arm roots at the shoulders, white "
          "gloves, long black tuxedo BUTTONED CLOSED hiding the label, white shirt and bow tie. No "
          "redesign. MOSTAZA SUAVE yellow LEFT, MOSTAZA TRADICIONAL gold CENTRE slightly ahead, "
          "KETCHUP red RIGHT. ")
CAM = "Vertical 9:16, cinematic, 50-85mm, stable camera, no shake. "

PLANOS.update({
    "sets/entrada_copylab": ("reel",
        "SET: contemporary entrance of a creative agency seen frontally from a low camera in a "
        "dark corridor with a wet glossy black floor: a wide glass and dark-wood doorway, warm "
        "light glowing from inside, and above the door clean white sans-serif lettering that "
        "reads exactly 'GRUPO COPYLAB'. Same black-studio universe as the reference set image, "
        "subtle haze, deep blacks. Photoreal, 85mm, vertical 9:16. No people, no other text.",
        [CORREDOR]),

    # ---- ACTO I ----
    "keyframes/k01_siluetas": ("reel",
        "SHOT 01 'ALGO VIENE': the three LOCKED characters far from a low frontal fixed camera, "
        "walking towards it, seen ONLY as PURE BLACK SILHOUETTES against a single strong warm "
        "backlight at floor level behind them that blooms through haze: 100% black shapes, ZERO "
        "colour, no yellow/gold/red visible, no label, no detail, only their outlines (cap, "
        "shoulders, long jacket, very short legs, big feet) and long reflections on the wet "
        "black floor. Centre one slightly ahead. " + LOCKED + SET1 + CAM + NEG, [LOCK_TRIO, CORREDOR]),
    "keyframes/k02_pies": ("reel",
        "SHOT 02 'LOS PASOS': EXTREME LOW-ANGLE MACRO. The camera lies ON the wet black floor, "
        "85mm. The frame is CROPPED so that ONLY the BIG rounded mascot feet and the very short "
        "thick legs of the three LOCKED characters are visible, filling the lower two thirds of "
        "the frame, mid-step walking towards the lens: yellow feet left, gold feet centre and "
        "closest, red feet right; the black hem of the long tuxedos cuts the top of the frame. "
        "NO caps, NO bottles, NO upper body in frame. Reflections on the floor. " + LOCKED + SET1 + CAM + NEG, [LOCK_TRIO, CORREDOR]),
    "keyframes/k03_entrada": ("reel",
        "SHOT 03 'LA ENTRADA': full-body frontal, the three LOCKED characters walking towards "
        "the camera in sync under their three warm spotlights, tuxedos buttoned, arms swinging "
        "slightly, gold MOSTAZA TRADICIONAL centre one step ahead, yellow left, red right. Low "
        "camera, slight push-in feel. " + LOCKED + SET1 + CAM + NEG, [LOCK_TRIO, CORREDOR]),

    # ---- ACTO II inserts (cerrado → sólo la ficha) ----
    "keyframes/k04_suave": ("reel",
        "SHOT 04: medium close-up, frontal, of MOSTAZA SUAVE alone (the yellow LOCKED character "
        "of the reference sheet) under one warm spotlight, the others out of frame. He calmly "
        "adjusts ONE cuff of his tuxedo with the other white glove; relaxed, cool. Framed from "
        "the cap to the jacket hem. Tuxedo buttoned, label hidden. " + LOCKED + SET1 + CAM + NEG, [LOCK_SUAVE]),
    "keyframes/k05_tradicional": ("reel",
        "SHOT 05: medium close-up, frontal, of MOSTAZA TRADICIONAL alone (the gold LOCKED "
        "character of the reference sheet) under one warm spotlight. Both white gloves up at the "
        "black bow tie, adjusting it slowly; the leader, calm. Framed from the cap to the jacket "
        "hem. Tuxedo buttoned, label hidden. " + LOCKED + SET1 + CAM + NEG, [LOCK_TRAD]),
    "keyframes/k06_ketchup": ("reel",
        "SHOT 06: medium close-up, three-quarter, of KETCHUP alone (the red LOCKED character of "
        "the reference sheet) under one warm spotlight. One white glove smoothing a lapel of the "
        "tuxedo, posture very straight, serious. Framed from the cap to the jacket hem. Tuxedo "
        "buttoned, label hidden. " + LOCKED + SET1 + CAM + NEG, [LOCK_KET]),

    # ---- ACTO III reveal (trío + packshots) ----
    "keyframes/k07_reveal": ("reel",
        "SHOT 07 'HERO REVEAL': EXACTLY the same frontal symmetric full-body framing, set and "
        "characters as the reference trio image, but now each of the three holds his long tuxedo "
        "jacket WIDE OPEN with both white gloves on the lapels, revealing the REAL bottle and its "
        "complete vintage label EXACTLY as in the product photos (MOSTAZA SUAVE yellow left, "
        "MOSTAZA TRADICIONAL gold centre, KETCHUP red right), white shirt fronts pushed aside. No "
        "transformation: the same bottle that was under the jacket. Each under his spotlight. "
        + LOCKED.replace("BUTTONED CLOSED hiding the label", "now OPEN") + SET1 + CAM + NEG,
        [LOCK_TRIO, *PACKS]),

    # ---- ACTO IV / V ----
    "keyframes/k08_hacia_copylab": ("reel",
        "SHOT 08 'A DONDE VAN': camera BEHIND the three LOCKED characters at hip height. We see "
        "their BACKS (black tuxedo backs, caps, short legs and big feet: yellow left, gold centre "
        "ahead, red right) walking away down the dark corridor towards the glowing entrance of "
        "the reference set with the 'GRUPO COPYLAB' lettering above the door, the door opening "
        "and spilling warm light on the wet floor. " + LOCKED + CAM + NEG, [LOCK_TRIO, ENTRADA]),
    "keyframes/k09_nueva_casa": ("reel",
        "SHOT 09 'NUEVA CASA': inside the meeting room of the reference room image, seen from "
        "the head of the table: the three LOCKED characters have just walked in through the "
        "glass door at the back and stand side by side next to the table, still, tuxedos "
        "buttoned, yellow left, gold centre, red right; warm natural window light, wood, glass, "
        "the frosted 'Grupo CopyLab' logo on the glass as in the reference. Not seated yet. "
        + LOCKED + CAM + NEG, [LOCK_TRIO, BOARD]),
    "keyframes/k10_reunion": ("reel",
        "SHOT 10 'LA REUNION': EXACTLY the same meeting room, camera and warm light as the "
        "reference room image; the three LOCKED characters are now SEATED in the three black "
        "chairs on the far side of the table facing camera, perfectly serious: yellow MOSTAZA "
        "SUAVE left, gold MOSTAZA TRADICIONAL centre with both white gloves on a printed document "
        "that reads exactly 'PLAN 2026', red KETCHUP right very upright. Laptop, notebooks, coffee "
        "cups on the table. No humans, no comedy. " + LOCKED + CAM + NEG, [LOCK_TRIO, BOARD]),
})


# =====================================================================
# NUEVA DIRECCIÓN «THE ENTRANCE» (09-09-2026, noche) — keyframes extra
# =====================================================================
PACK_MACRO = ("Extreme macro product photograph of the REAL Traverso 450 g bottle from the "
              "reference photo, exact packaging, on the wet black studio set, one warm tungsten "
              "spotlight sweeping across the glossy plastic, deep blacks, shallow depth of field, "
              "100mm macro, vertical 9:16, no characters, no text overlays, no watermark. ")
PLANOS.update({
    "keyframes/e01_macro_boquilla": ("reel",
        "COLD OPEN macro: extreme close-up of the GOLD conical nozzle cap of MOSTAZA TRADICIONAL "
        "(the LOCKED character's cap, exactly as the reference), a theatrical spotlight just "
        "switched on above it, the rest of the frame pitch black, haze, rim light on the ridges "
        "of the cap. " + CAM + NEG, [LOCK_TRAD, REF_TRAD]),
    "keyframes/e02_macro_guante": ("reel",
        "COLD OPEN macro: extreme close-up of a round WHITE MASCOT GLOVE of the LOCKED character "
        "pinching and adjusting the black satin lapel of his tuxedo, white shirt and bow tie "
        "partly in frame, warm spotlight, pitch black around, shallow depth of field. No face. "
        + CAM + NEG, [LOCK_KET]),
    "keyframes/e07a_falso_reveal": ("reel",
        "FALSE REVEAL: WORM'S-EYE VIEW, the camera lies ON THE FLOOR between their feet pointing "
        "straight UP, wide 24mm, strong perspective: the big feet and legs huge in the foreground, "
        "the bottles converging towards the spotlights above. The three LOCKED characters have "
        "just STOPPED, towering over the lens, tuxedos buttoned, label "
        "hidden; MOSTAZA TRADICIONAL (gold, centre, slightly ahead) raises both white gloves to "
        "his lapels as if about to open the jacket; yellow left, red right, still. Three warm "
        "spotlights above them against black, haze. Tension. " + LOCKED + SET1 + CAM + NEG,
        [LOCK_TRIO, CORREDOR]),
    "keyframes/e07b_falso_reveal_cenital": ("reel",
        "FALSE REVEAL, TOP-DOWN: the camera is directly ABOVE the three LOCKED characters, "
        "looking straight DOWN (bird's-eye view), so we see the tops of the three nozzle caps "
        "(yellow left, gold centre slightly ahead, red right), the black tuxedo shoulders, the "
        "white gloves of the gold one rising to his lapels, and their big feet foreshortened on "
        "the wet black floor with three spotlight pools around them. They have just stopped. "
        + LOCKED + SET1 + CAM + NEG, [LOCK_TRIO, CORREDOR]),
    "keyframes/e12a_macro_amarillo": ("reel",
        PACK_MACRO + "Subject: the YELLOW nozzle cap and shoulder of MOSTAZA SUAVE, light "
        "gliding along the cone. ", [REF_SUAVE, CORREDOR]),
    "keyframes/e12b_macro_dorado": ("reel",
        PACK_MACRO + "Subject: the vintage label of MOSTAZA TRADICIONAL on the gold bottle, "
        "'TRAVERSO' and 'MOSTAZA TRADICIONAL' crisp and legible, exactly as the photo, light "
        "sweeping across the gold plastic. ", [REF_TRAD, CORREDOR]),
    "keyframes/e12c_macro_rojo": ("reel",
        PACK_MACRO + "Subject: the red KETCHUP bottle, its nozzle cap and the top of the vintage "
        "label 'TRAVERSO' exactly as the photo, glossy red plastic with a warm highlight. ",
        [REF_KET, CORREDOR]),
    "keyframes/e10_reunion": ("reel",
        "THE GAG: EXACTLY the same meeting room, camera and warm light as the reference room "
        "image; the three LOCKED characters are ALREADY SEATED in the three black chairs on the "
        "far side of the table facing camera, dead serious: yellow MOSTAZA SUAVE left holding a "
        "white ceramic coffee cup with one white glove, gold MOSTAZA TRADICIONAL centre opening a "
        "black folder with both gloves, red KETCHUP right with an open laptop in front of him. "
        "Notebooks and documents on the table. No humans, no comedy. " + LOCKED + CAM + NEG,
        [LOCK_TRIO, BOARD]),
})

if __name__ == "__main__": main()

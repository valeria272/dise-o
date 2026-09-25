#!/usr/bin/env python3
"""G.CL CAP.02 «TURNO DE NOCHE» — storyboard visual: el cuadro de inicio de cada plano.

Storyboard: gcl-agent/universo/06_VIDEO_REELS/CAP_02_TURNO_DE_NOCHE/STORYBOARD_V3_DEFINITIVO.md
Canon:      G MASTER REFERENCE VFinal + ESTACIÓN DE G canon (lock 19) y los 4
            keyframes maestros aprobados (out/gcl/cap02-v3/keyframes-r2/elegidos/).

Cada plano parte SIEMPRE de: G maestro → estación canon → el keyframe maestro
más cercano. Así G no cambia de cabeza en P12 ni de altura en P16.

Reutilizados sin generar (van copiados a out/gcl/cap02-v3/planos/):
  · P13 = K2 (el trío en el piso)      · P18 = K4 (apagado + NO MOLESTAR)
  · P15 = P09 (mismo encuadre; sólo cambia la notificación, que va en post)

    python3 scripts/gcl-cap02-planos.py            # tanda 1 (todo menos P17)
    python3 scripts/gcl-cap02-planos.py P17        # tanda 2 (usa P02 como ref)
    python3 scripts/gcl-cap02-planos.py P05 P12    # regenerar sólo esos

⛔ Todo texto va en post: post-its en blanco, paneles sin letras, carpeta sin rótulo.
"""
import importlib.util, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("kf", RAIZ / "scripts/gcl-cap02-keyframes.py")
kf = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(kf)

REFS = kf.REFS
OUT = RAIZ / "out/gcl/cap02-v3/planos"
ELEGIDOS = RAIZ / "out/gcl/cap02-v3/keyframes-r2/elegidos"

# Los keyframes aprobados se usan como referencia con nombre propio.
for k in ("K1", "K2", "K3", "K4"):
    destino = REFS / f"kf_{k.lower()}.png"
    if not destino.exists() and (ELEGIDOS / f"{k}.png").exists():
        shutil.copy(ELEGIDOS / f"{k}.png", destino)
# La oficina de Pancho de la ronda 1 (Nano Banana Pro) da la locación de arriba.
_of = RAIZ / "out/gcl/cap02-v3/keyframes/k1-pancho-oficina-noche-pro.png"
if _of.exists() and not (REFS / "oficina_pancho.png").exists():
    shutil.copy(_of, REFS / "oficina_pancho.png")

E, N1, G, VG, HALO = kf.ESTILO, kf.NIVEL_MENOS_1, kf.G, kf.VISOR_G, kf.HALO
MARTA, ROLO, EST = kf.MARTA, kf.ROLO, kf.ESTACION
SIN_HALO = "G has NO halo in this shot. "
REF_G = ["g_master_cap02.png", "g_master_cap02_full.png"]
REF_EST = ["estacion_g_canon.png"]
REF_MARTA = ["marta_turn.png", "marta_hero.png"]
REF_ROLO = ["rolo_turn.png", "rolo_hero.png"]
REF_PANCHO = ["pancho_retrato.png", "pancho_equipo.png", "oficina_pancho.png"]
OFICINA = (
    "Setting: the Copylab agency office (Level 0), warm and real: pendant lamps, plants, wooden "
    "desks, exposed concrete ceiling, large windows with city lights at dusk. "
)
PANCHO = (
    "PANCHO: the young man from the reference photos — same face, short brown hair, round friendly "
    "face, clean-shaven — wearing a cream crewneck sweatshirt. "
)
# Valeria 25-09: «Pancho se ve muy falso». Pistas de foto real, no de render.
FOTO_REAL = (
    "This must look like a REAL candid photograph of a real person, not a 3D render and not an AI "
    "portrait: natural skin with pores, slight blemishes and uneven tone, real hair strands, a little "
    "asymmetry in the face, natural imperfect posture, real fabric wrinkles on the sweatshirt, "
    "documentary photojournalism style, available light, subtle motion, unposed. "
)
PANEL = "Translucent pink holographic panels with abstract bars and boxes only, absolutely no letters or numbers. "

PLANOS = {
    "P01": (REF_PANCHO + ["set_oficina_noche.png"], E + OFICINA + FOTO_REAL + (
        "Close-up of the TOP RIGHT CORNER of a black computer monitor on a wooden desk, seen slightly "
        "from the side and a little above. A single square yellow sticky note, completely BLANK, is "
        "stuck FLAT against the front of the monitor's black bezel at that corner, its adhesive top "
        "edge pressed on, the paper lying flush on the plastic with only its bottom corner curling a "
        "couple of millimetres: it is clearly glued onto the screen frame, not floating. The note "
        "fills about half the frame width. Background: the warm office at 7 pm, out of focus, soft "
        "bokeh of pendant lamps. No people in focus.")),
    "P02": (REF_PANCHO + ["P01"], E + OFICINA + PANCHO + FOTO_REAL + (
        "Medium shot, frontal, eye level, static, 50mm. Pancho sits at his desk at 7 pm, relaxed and a "
        "bit slouched, half smile, zero guilt, looking to his side at the yellow sticky note stuck on "
        "the corner of the monitor next to him (the same note as the P01 reference, blank), NOT at the "
        "camera. Both hands resting on the lid of his open laptop, about to close it. An olive jacket "
        "hangs on his chair. Empty desks behind him, city lights at dusk in the windows.")),
    "P03": (["oficina_pancho.png"], E + OFICINA + (
        "NO robots, NO characters, NO people in this shot. Very wide static shot of the whole open-plan office at night, seen from the front towards "
        "the back, city lights in the windows. Nobody left. The lights near the camera are already "
        "OFF, the middle zone is still lit, the far zone lit: the moment the lights switch off zone "
        "by zone: the foreground is clearly DARK, the background still warm.")),
    "P04": (REF_MARTA + ["set_archivo.png"], E + N1 + MARTA + (
        "Marta ALONE in frame: no G, no Rolo, no other characters. Medium shot, frontal, at Marta's height, warm amber light, archive shelves behind. Marta is "
        "printing on her own: a sheet of continuous paper (blank, no writing) is coming out of her "
        "top. Her heavy eyelids are half closed: bored veteran, 'again'.")),
    "P05": (REF_ROLO + ["rolo_bandera.png", "set_archivo.png"], E + N1 + ROLO + (
        "Rolo has a thin mast on his back with a small plain pink flag, as in the flag reference "
        "(no letters on the flag, no lettering on his chest). Close shot from a low angle at his "
        "height, handheld feel. Rolo is SCARED and ANXIOUS — not angry, not determined: he is "
        "BACKING AWAY, leaning backwards, knees bent, clutching the blank sheet of paper against his "
        "chest with both arms, helmet pulled in, glancing sideways as if looking for an escape. His "
        "two pink rectangular LED eyes have shrunk into small, uneven, wobbly vertical bars, worried "
        "(NOT slanted, NOT angry brows). His whole body is shaking: slight motion blur on his edges, "
        "the mast and flag vibrating and blurred. Faint cold bluish-white flicker across his black "
        "face screen. Robot anxiety, not human: no sweat, no drops, no tears, no mouth.")),
    "P06": (REF_G + REF_EST + ["kf_k1.png"], E + N1 + G + VG + SIN_HALO + EST + (
        "Medium shot, G in 3/4 front view standing on the clear area of his workbench, night. He "
        "is working, visor tilted slightly down towards one small dim holographic panel. The halo "
        "is OFF (not there yet). " + PANEL)),
    "P07": (REF_G + ["kf_k4.png"] + REF_ROLO + REF_EST, E + N1 + G + VG + HALO + ROLO + EST + (
        "G keeps EXACTLY the compact proportions of the G master and of the K4 reference: short stubby body, very short legs, the helmet as tall as the whole body. Same G-to-Rolo scale as in K4. "
        
        "Close two-shot at Rolo's height on the workbench. G places one hand gently on top of "
        "Rolo's helmet; Rolo, still slightly tense, is calming down, his LED eyes returning to their "
        "normal shape. With his other hand G takes the blank sheet of paper from Rolo. Brief, almost "
        "paternal gesture.")),
    "P08a": (REF_G + REF_EST + ["kf_k1.png"], E + N1 + G + VG + HALO + EST + (
        "BEAT 1 — COPY. Close side shot, camera low and near. G leans FORWARD in total focus, both "
        "small gloved hands typing fast on a flat translucent pink holographic keyboard floating "
        "over the workbench; in front of him ONE tall narrow vertical panel filled with many rows of "
        "abstract text lines (no real letters), like a document being written. Tight, intimate, "
        "concentrated. " + PANEL)),
    "P08b": (REF_G + REF_EST + ["kf_k1.png"], E + N1 + G + VG + HALO + EST + (
        "BEAT 2 — DESIGN. Wide low-angle shot, the camera pulled far back. G steps BACK on the "
        "workbench with both arms spread wide, like an art director framing a layout; in front of "
        "him a LARGE horizontal grid of many image tiles, colour swatches and shapes (no letters) "
        "spreads out in the air — a visual, colourful composition, very different from a text "
        "document. Expansive, creative energy. " + PANEL)),
    "P08c": (REF_G + REF_EST + ["kf_k1.png"], E + N1 + G + VG + HALO + EST + (
        "BEAT 3 — DONE. Frontal medium shot, G facing the camera, standing upright and still on "
        "the workbench, one small hand raised giving a short, satisfied tap in the air. All the "
        "panels have collapsed into ONE single small square pink panel floating at his side, "
        "showing only a large clean check-mark symbol. Calm, complete, a tiny pause of pride. "
        "The pink holographic panel has no letters or numbers.")),
    "P09": (REF_G + REF_EST + ["kf_k1.png"], E + N1 + HALO + EST + (
        "Over-the-shoulder shot from behind G (G's glossy black helmet, pink headphone pod and thin "
        "halo in the foreground, out of focus), looking at a pink holographic panel in sharp focus. "
        "On the panel, a large EMPTY rounded rectangle notification card slides in (no text, it is "
        "added later). G's gloved hand is frozen in mid-air. " + PANEL)),
    "P10": (REF_G + REF_MARTA + ["kf_k2.png", "set_archivo.png"], E + N1 + G + VG + HALO + MARTA + (
        "Medium side shot, static. Marta in the foreground on the left, G on the right a bit further "
        "back. Without turning or looking at him, Marta has slid open a drawer of an old metal filing "
        "cabinet next to her and is holding out a worn, dusty manila folder towards G (the folder "
        "label is blank). Her eyelids half closed, zero surprise.")),
    "P11a": (REF_G + ["set_archivo.png"], E + N1 + (
        "Tight insert: G's small dark gloved hands (from the G master) hold an old, worn, dusty manila "
        "folder with coffee rings and bent corners. On its front, a plain white paper label, EMPTY "
        "(the title is added later). Shallow depth of field, warm lamp light.")),
    "P11b": (REF_G + REF_EST + ["kf_k1.png"], E + N1 + G + VG + HALO + EST + (
        "Close shot, frontal, static, G on his workbench holding the old manila folder in both hands "
        "at chest height. His visor is raised, looking straight ahead off-screen to the left (at "
        "Marta), a long deadpan beat. Minimal expression: only the tilt of the helmet. The dot-matrix "
        "G on the visor unchanged.")),
    "P12": (REF_G + ["kf_k3.png"], E + N1 + G + HALO + (
        "Extreme close-up of G's visor, slightly low angle. The pink dot-matrix letter G is DIMMED, "
        "low brightness. Under it, a thin horizontal battery bar almost empty, dull coral. In the "
        "glossy visor, a faint reflection of pink holographic panels. The thin halo at the top edge "
        "of frame, dim.")),
    "P14": (REF_ROLO + ["kf_k2.png", "set_archivo.png"], E + N1 + ROLO + (
        "Shot at floor level at Rolo's height on the concrete floor between archive shelves. Rolo has "
        "just collapsed: sitting down hard, legs splayed, leaning to one side, arms loose. His LED eyes "
        "are two thin flat horizontal lines, half-closed, exhausted. Robot fatigue, not human.")),
    "P16": (REF_G + REF_EST + ["kf_k3.png", "kf_k4.png"], E + N1 + G + EST + (
        "Close shot, frontal, static, G on his workbench. The moment of shutdown: on the visor the "
        "dot-matrix pixels are scrambled and glitching, breaking up into a faint pink 'X X' mark. The "
        "thin halo is flickering and half gone. Head starting to tilt down. Headphone pods fading.")),
    "P17": (["P02"] + REF_PANCHO[:2], E + OFICINA + PANCHO + FOTO_REAL + (
        "Recreate the P02 reference image as its MIRROR shot: IDENTICAL camera position, lens, "
        "angle and framing, same desk, same chair, same monitor on the same side, same window "
        "behind, Pancho in exactly the same place in the frame. Only these things change: it is 9 am, "
        "bright soft morning daylight through the windows and the office is ALIVE: several colleagues "
        "out of focus in the background, walking with coffee, chatting at desks, someone at the "
        "window; the sticky note is gone from the monitor; Pancho holds a takeaway coffee in one hand "
        "and has just opened the laptop with the other; his eyes are DOWN on the laptop screen (not at "
        "the camera), a satisfied casual half smile.")),
    # ── GUION V2 «volvamos a la primera versión» (25-09-2026) ──
    "P19": (REF_MARTA + ["P10", "P04", "set_archivo.png"], E + N1 + MARTA + (
        "Medium shot, static, at Marta's height, next to her old metal filing cabinet (the same one as "
        "in the P10 reference). A single freshly printed sheet has just come out of Marta and is sliding "
        "down, neatly, into the open top drawer of the filing cabinet beside her, to be archived. Her "
        "heavy eyelids half closed, completely calm, routine. The sheet is blank (text is added later).")),
    "P20": (REF_ROLO + ["rolo_bandera.png", "P05", "set_archivo.png"], E + N1 + ROLO + (
        "Rolo has a thin mast on his back with a small plain pink flag. Medium shot, low angle, on the "
        "concrete floor between the archive shelves, late at night. Rolo is running badly, exhausted "
        "and overloaded: he carries a tall, wobbling tower of paper sheets in both arms that is taller "
        "than him, leaning dangerously, a few sheets slipping and flying off; more piles of papers are "
        "scattered on the floor around him. His pink LED eyes squeezed tired and stressed. Chaos is "
        "getting out of control. No text on papers.")),
    "P21": (REF_MARTA + ["P10", "set_archivo.png"], E + N1 + MARTA + (
        "Close shot, static, of Marta and the old metal filing cabinet beside her (same as the P10 "
        "reference). Without turning or looking, completely deadpan with half-closed eyelids, Marta has "
        "pushed open the drawer and a single CLEAN, crisp, thin manila folder rises neatly out of it "
        "towards the right edge of frame, offered to someone off-screen. Its label is plain white and "
        "blank (the text is added later). Calm, veteran, 'I knew this would happen'.")),
    "P22": (REF_G + REF_ROLO + REF_MARTA + REF_EST + ["kf_k2.png"], E + N1 + G + SIN_HALO + ROLO + MARTA + EST + (
        "It is MORNING: there is absolutely NO halo ring above G's helmet, nothing floating over his head. "
        
        "Early morning, wide static shot of Level -1 after an all-nighter. The three are wrecked: G sits "
        "slumped on the edge of his workbench, legs hanging, arms loose, helmet tilted down, the dot-"
        "matrix G on his visor very dim, NO halo. Rolo lies flat face-down on the floor among scattered "
        "papers, pink flag drooping. In the background Marta keeps calmly printing, paper feeding out, "
        "as if nothing happened. Warm tired light, quiet.")),
    # ── GUION V3 «MAÑANA LO VEO» (25-09-2026): el tubo, la revelación, la explosión ──
    # Tanda 1 (sin dependencias)
    "N01": (["P01"] + REF_PANCHO[:2], E + OFICINA + (
        "EXTREME MACRO close-up: the square yellow sticky note fills about 70 percent of the frame "
        "width, stuck on the black monitor bezel, sharp focus, the office behind reduced to soft warm "
        "bokeh. The sticky note is completely BLANK (text is added later). A man's hand in a cream "
        "sweatshirt cuff enters from the lower right holding a cheap blue ballpoint pen, the pen tip "
        "touching the note near its BOTTOM edge, casually writing. The hand and pen stay in the lower "
        "right corner and never cover the upper two thirds of the note.")),
    "N02": (["set_archivo.png"], E + (
        "Inside the building's hidden service shaft, raw concrete, warm dim light. A vertical vintage "
        "pneumatic tube (old bank tube-mail system): a thick transparent glass tube with polished brass "
        "rings and brass joints runs straight down through several raw concrete floor slabs, with a small "
        "pink indicator lamp glowing at each floor. Steep high angle looking DOWN along the tube, the "
        "floors receding below into warm darkness, strong depth. Halfway down, a clear acrylic capsule "
        "with brass end caps, a rolled yellow note visible inside, rushes downward, slight motion blur. "
        "Real, tactile, backstage, not sci-fi, very little neon. No text.")),
    "N04": (REF_G + REF_EST + ["kf_k1.png", "P11b"], E + N1 + G + VG + HALO + EST + (
        "Medium shot, static, eye level. G sits on an overturned wooden crate next to his workbench, the "
        "old dusty manila folder open on his lap, one small gloved hand touching the chin of his helmet "
        "in a classic thinking pose, helmet tilted a little. Deadpan, pondering hard. The folder label "
        "is plain white and blank.")),
    "N06": (["g_master_cap02.png"], E + (
        "A comedic celestial vision, like a Baroque church ceiling painting: a COLOSSAL ancient retro "
        "robot deity head floating among glowing golden clouds and god rays. Vintage 1950s tin-toy robot "
        "style: rounded cream enamel and chrome, rivets, a small antenna crowned by a thin pink halo "
        "ring, two huge round glowing pink LED eyes emitting beams of pink light downward. Majestic, "
        "solemn and absurd at the same time. Warm gold and pink light. Vertical composition, the head "
        "fills the upper two thirds. No text.")),
    "N08": (REF_G + REF_EST + ["kf_k1.png"], E + N1 + G + VG + HALO + EST + (
        "Medium close shot, slightly low angle, dynamic. G sits at his workbench in front of a chunky old "
        "beige CRT computer and a modern open laptop side by side, typing furiously with both small "
        "gloved hands, fingers blurred with speed, halo glowing bright, visor bright. Papers flying off "
        "the bench, cables, coffee mug. The screens show abstract pink shapes and bars only, absolutely "
        "no letters or numbers. Full-power energy.")),
    "N09": (REF_ROLO + ["rolo_bandera.png", "P05", "set_archivo.png"], E + N1 + ROLO + (
        "Rolo has a thin mast on his back with a small plain pink flag. High angle, almost top-down, on "
        "the concrete floor between the archive shelves. Rolo runs in a tight circle, arms flailing, "
        "loose paper sheets swirling around him in a vortex, the flag flapping, motion blur on his feet. "
        "Pure panic chaos, comedic. No text on papers.")),
    "N14": (REF_G + REF_ROLO + REF_MARTA + ["kf_k2.png"], E + N1 + G + VG + ROLO + MARTA + (
        "Exactly the framing and poses of the kf_k2 reference (Marta left, G center, Rolo right, standing "
        "on the concrete floor), one second AFTER a comedic cartoon explosion. EDIT THE REFERENCE: all three "
        "are HEAVILY BLACKENED with thick black soot like in a Looney Tunes gag: Marta's cream metal body "
        "is charred grey-black, Rolo's white shell is smudged dark grey almost everywhere, G's suit and "
        "helmet dusty with ash, only their eyes and G's visor still glowing through the soot. They are frozen stiff in the same poses, thin smoke wisps rising from them. G's thin halo "
        "ring is bent and tilted, crackling with a tiny spark. Rolo's pink flag is burnt down to a "
        "charred little stub. A burnt strip of paper hangs from Marta's slot, smoking. Singed paper "
        "sheets float down through the air all around; a black blast mark on the floor. Deadpan, "
        "blinking, cartoon logic but photoreal materials.")),
    # Tanda 2 (usan el tubo N02 o el G sentado N04 como referencia)
    "N03": (["N02", "P04"] + REF_MARTA + ["set_archivo.png"], E + N1 + MARTA + (
        "Level -1 archive, warm amber light. The same vertical glass-and-brass pneumatic tube as the N02 "
        "reference comes down from the concrete ceiling and ends in a brass receiving hatch with a small "
        "wire basket, right beside Marta the printer, who is in the left half of the frame with "
        "half-closed eyelids. A clear acrylic capsule with brass end caps and a rolled yellow note "
        "inside has just dropped into the basket. Medium shot, static. No text.")),
    "N05": (["N04"] + REF_G + REF_EST, E + N1 + G + VG + HALO + EST + (
        "Same room as the N04 reference, closer: G sits on the wooden crate with the folder on his lap, "
        "his big glossy helmet TILTED BACK, visor facing UP towards the ceiling. G is fully INSIDE a single "
        "vertical column of intense white-pink light that falls from a small open hatch in the concrete "
        "ceiling straight down onto his helmet: the beam hits him directly and lights his helmet and "
        "shoulders brightly, glowing dust particles inside the beam, the rest of the room goes dark "
        "around him. Religious-painting moment, comedic and solemn.")),
    "N07": (["N05"] + REF_G, E + N1 + G + VG + HALO + (
        "Close-up from a low three-quarter angle of G's glossy black helmet, looking up into a beam of "
        "white-pink light. Streams of glowing pink and white light filaments made of tiny abstract dots "
        "and dashes (absolutely no readable letters or numbers) pour down from above into the top of "
        "his helmet like data rain; his dot-matrix visor G blazing bright; the thin halo ring glowing "
        "intensely. Revelation.")),
    "N10": (["N03"] + REF_G + REF_EST, E + N1 + G + VG + HALO + (
        "Medium shot, static, at the pneumatic tube of the N03 reference (glass and brass, coming down "
        "from the ceiling into a brass hatch). G stands on tiptoe, pushing a clear capsule with a rolled "
        "paper into the tube's open brass hatch with both small gloved hands, determined, in a hurry. "
        "Papers scattered on the floor around him after a long night. No text.")),
    "N11": (["oficina_pancho.png", "P01", "N02"], E + OFICINA + (
        "Pancho's empty desk at DAWN (6:45 am): pale pink-blue sunrise light through the big windows, "
        "pendant lamps off, quiet. On the desk: the closed laptop and the black monitor with the yellow "
        "sticky note still on its bezel (blank). Next to the desk, the same glass-and-brass pneumatic "
        "tube as the N02 reference rises out of the floor and ends in a brass receiving hatch; a clear "
        "capsule with a rolled paper has just popped out and lies on the desk. Nobody there. No text.")),

    # ── CORTE 4 (Valeria 25-09, feedback del corte 3) ──
    "N15": (REF_G + REF_ROLO + REF_EST + ["P07", "kf_k4.png"], E + N1 + G + VG + HALO + ROLO + EST + (
        "Two-shot, static, eye level, at G's workbench at night: G (halo on) on the left and Rolo (with "
        "his thin mast and small pink flag) on the right, both standing on the bench, both FROZEN in "
        "the middle of working, turned to look straight at EACH OTHER, deadpan, a silent 'here we go "
        "again' exchanged between them. Papers and the holographic panel around them. Rolo's LED eyes "
        "wide.")),
    "N16": (["P17"] + REF_PANCHO[:2], E + OFICINA + PANCHO + FOTO_REAL + (
        "Same camera, framing and morning office as the P17 reference (colleagues out of focus behind, "
        "walking and chatting). Pancho sits at the desk looking at the laptop screen, caught mid "
        "SHRUG: both shoulders raised, elbows bent, palms turned up beside the laptop, eyebrows raised, "
        "mouth pulled into a small 'oh well, whatever' grimace. Genuinely indifferent, a little amused. "
        "Not looking at the camera. The monitor beside him is a plain black screen: absolutely NO pink "
        "or magenta light, no glowing ring, no reflections of any robot; only warm morning daylight.")),
    # ── CORTE 5 (Valeria 25-09): gags entre G y su equipo mientras trabajan + botón final ──
    "N17": (REF_G + REF_ROLO + REF_EST + ["N15", "kf_k4.png"], E + N1 + G + VG + HALO + ROLO + EST + (
        "Two-shot at G's workbench at night, static, eye level. Rolo (thin mast, small pink flag) proudly "
        "holds up towards G a completely WRONG object: a dusty old rolled-up poster tube, way too big for "
        "him, beaming with his LED eyes. G, standing beside him, has one small gloved hand pressed flat "
        "against the front of his own visor in a classic facepalm, helmet tilted down. Deadpan comedy.")),
    "N18": (REF_G + REF_ROLO + REF_EST + ["N15", "kf_k1.png"], E + N1 + G + VG + HALO + ROLO + EST + (
        "Two-shot at G's workbench at night, static. G and Rolo ARGUE in front of the tall translucent pink "
        "holographic panel: G points firmly at the panel with one hand, the other hand on his hip; Rolo, "
        "facing him, has both arms thrown up in the air, LED eyes squeezed, the pink flag on his mast "
        "bristling. Both leaning slightly towards each other. Comedic disagreement, cartoon body language.")),
    "N19": (REF_MARTA + REF_ROLO + ["P04", "set_archivo.png"], E + N1 + MARTA + ROLO + (
        "Wide static shot in the archive at night. Marta is printing an ABSURDLY long strip of continuous "
        "paper that has piled up in huge loose loops on the concrete floor, filling the lower half of the "
        "frame, and keeps coming. Rolo (thin mast, small pink flag) stands buried up to his chest in the "
        "paper loops, arms up, LED eyes wide, holding one end of the strip. Marta's eyelids half closed, "
        "unbothered. Paper is blank, no text.")),
    "N20": (REF_G + REF_ROLO + REF_EST + ["N15", "kf_k4.png"], E + N1 + G + VG + HALO + ROLO + EST + (
        "Two-shot at G's workbench at night, static, low angle. G and Rolo do a tiny FIST BUMP: G's small "
        "gloved fist meets Rolo's little white fist in the middle of the frame, both looking at the fists; "
        "G's visor bright, Rolo's LED eyes as two happy arcs, his pink flag straight up. A small win. "
        "Holographic panel glowing behind them.")),
    "N21": (["N14", "P18"] + REF_G + REF_ROLO, E + N1 + (
        "Close two-shot, static, right after the explosion: G stands powered OFF, covered in black soot, his "
        "visor showing only two dim 'X X' marks, no halo, helmet tilted slightly down. Rolo, also sooty and "
        "smudged grey, his pink flag burnt to a stub, stands on tiptoe beside him pressing a square yellow "
        "sticky note (completely BLANK) flat onto G's visor with one hand, the other hand holding a cheap "
        "blue ballpoint pen. Thin smoke wisps still rising. Deadpan.")),
    # ── CORTE 6 (Valeria 25-09): descansan y celebran con café ──
    "N22": (REF_G + REF_ROLO + REF_MARTA + REF_EST + ["kf_k2.png", "P22"], E + N1 + G + VG + SIN_HALO + ROLO + MARTA + EST + (
        "It is DAWN after an all-nighter: absolutely NO halo above G's helmet. Medium three-shot, static, "
        "eye level, warm early light from a high window plus the desk lamp. G, Rolo (thin mast, small pink "
        "flag drooping) and Marta are together at G's workbench, exhausted and happy, TOASTING with coffee: "
        "G holds a big ceramic mug up in one gloved hand, Rolo holds a tiny espresso cup with both hands, "
        "and a third mug rests on Marta's top next to her paper slot, her eyelids half closed but content. "
        "The mugs clink in the middle. Papers everywhere, the holographic panel dimmed. Tired, cozy, proud.")),
    # ── CORTE 7 (Valeria 25-09, últimos cambios): Pancho más real + 5 s de trabajo tipo Pixar ──
    "P02b": (REF_PANCHO + ["P01", "P02"], E + OFICINA + PANCHO + FOTO_REAL + (
        "Candid over-the-shoulder shot from BEHIND and slightly to the side of Pancho, 35mm, handheld "
        "feel: we see the back of his head and his shoulder in the near foreground, slightly out of "
        "focus, and past him the black monitor with the yellow sticky note stuck on its top corner (the "
        "same note as the P01 reference, blank) in focus. His face is mostly hidden: only a sliver of his "
        "cheek as he turns toward the note. Both hands resting on the lid of the open laptop. Cream "
        "sweatshirt, olive jacket on the chair. 6:30 pm, warm pendant lamps, dusk in the windows, empty "
        "desks. Real photograph, unposed, natural.")),
    "N23": (REF_G + REF_ROLO + REF_MARTA + REF_EST + ["kf_k1.png", "N15"], E + N1 + G + VG + HALO + ROLO + MARTA + EST + (
        "Wide static shot at night, the big cork pinboard behind G's workbench now covered in dozens of "
        "small pinned sketches and torn paper notes (drawings only, NO letters). G stands on the bench "
        "pinning one more sheet with a pushpin, halo bright; Rolo (thin mast, pink flag) stands beside him "
        "holding up a tiny box of pushpins with both arms like an assistant; Marta on the floor at the "
        "side printing a long strip of small sketches that curls toward G. Creative brainstorm energy.")),
    "N24": (REF_G + REF_ROLO + REF_MARTA + REF_EST + ["N15", "N18"], E + N1 + G + VG + HALO + ROLO + MARTA + EST + (
        "Two-shot at G's workbench at night, static, eye level: G and Rolo in a comedic TUG-OF-WAR over a "
        "single large sheet of paper (blank), each gripping one end with both hands, leaning back hard in "
        "opposite directions, feet planted, the paper stretched tight between them. Rolo's LED eyes "
        "squeezed, pink flag whipping; G's helmet tilted back with effort. Marta visible behind on the "
        "floor, eyelids half closed, unbothered. Cartoon body language, photoreal materials.")),
    "N25": (REF_G + REF_ROLO + REF_EST + ["N15", "P08b"], E + N1 + G + VG + HALO + ROLO + EST + (
        "Two-shot at G's workbench at night, static. Rolo (thin mast, pink flag) stands on tiptoe "
        "painting a huge messy PINK brushstroke across the tall translucent holographic panel with an "
        "oversized paintbrush, paint splashing, thrilled; right beside him G, very precise, holds a "
        "wooden ruler against the panel and squints at it, measuring, helmet tilted. Two ways of "
        "working. No letters anywhere.")),
}
REUSO = {"P13": ELEGIDOS / "K2.png", "P18": ELEGIDOS / "K4.png"}


MOTOR = "seedream"


def correr(p):
    refs_n, prompt = PLANOS[p]
    refs = [str(OUT / f"{r}.png") if r[0] in "PN" and r[1].isdigit() else str(REFS / r) for r in refs_n]
    faltan = [r for r in refs if not Path(r).exists()]
    if faltan:
        return f"✗ {p}: faltan referencias {faltan}"
    destino = OUT / (f"{p}.png" if MOTOR == "seedream" else f"{p}-{MOTOR}.png")
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), MOTOR, prompt,
           "--out", str(destino), "--aspecto", "reel", "--refs", *refs[:10]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = r.returncode == 0 and destino.exists()
    return f"{'✓' if ok else '✗'} {p}" + ("" if ok else "\n" + (r.stdout + r.stderr)[-400:])


def main():
    global MOTOR
    OUT.mkdir(parents=True, exist_ok=True)
    args = sys.argv[1:]
    if "--motor" in args:
        i = args.index("--motor"); MOTOR = args[i + 1]; del args[i:i + 2]
    pedidos = args or [p for p in PLANOS if p != "P17"]
    if not args:
        for p, src in REUSO.items():
            shutil.copy(src, OUT / f"{p}.png"); print(f"= {p} ← {src.name}")
    with ThreadPoolExecutor(max_workers=5) as ex:
        for linea in ex.map(correr, pedidos):
            print(linea, flush=True)
    if (OUT / "P09.png").exists() and not (OUT / "P15.png").exists():
        shutil.copy(OUT / "P09.png", OUT / "P15.png"); print("= P15 ← P09")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""G.CL CAP.02 «TURNO DE NOCHE» — cada cuadro del storyboard visual pasa a video.

Entrada: out/gcl/cap02-v3/planos/<P>.png (storyboard visual aprobado 24-09-2026)
Salida:  out/gcl/cap02-v3/video/<P>.mp4 (clips de 5 s; el montaje los recorta
         a la duración del storyboard)

Regla del plano (R01): UN movimiento de cámara y UN gesto por clip.
Siempre image-to-video desde el cuadro aprobado, nunca texto→video.

Modelo:
  · con `fin` (el plano debe TERMINAR en un keyframe) → kling-v2-1-pro, que es
    el único que acepta image_tail.
  · el resto → kling-v2-5-pro, el mejor motor que tenemos.
  · si la 2.1 falla en silencio (pasó el 15-09) se reintenta con la 2.5 sin fin.

    python3 scripts/gcl-cap02-video.py P05 P07 P11a P11b P16   # piloto de riesgo
    python3 scripts/gcl-cap02-video.py                 # todos los que falten
"""
import subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANOS = RAIZ / "out/gcl/cap02-v3/planos"
OUT = RAIZ / "out/gcl/cap02-v3/video"
REFS = RAIZ / "raw/gcl/cap02-v3/refs"

G_FIJO = ("The small robot G keeps EXACTLY his design the whole time: same compact proportions, "
          "big glossy black helmet, short body, short legs, same visor geometry, the thin halo "
          "(if present) stays the same ring. His helmet keeps facing the same way, no turning "
          "around, no morphing. ")

# Reglas duras de Valeria (24-09-2026) — van al final de TODOS los prompts.
REGLAS = (
    "HARD RULES: keep exactly the design, scale and proportions of the input frame. Do not "
    "reinterpret faces, bodies, joints, visor, halo, clothing or props. Short, controlled, "
    "physically coherent motion. Do not add objects, characters or text. Do not deform screens, "
    "furniture or hands. No camera movement unless stated above. Body acting of the character "
    "matters more than camera movement. "
)

# Duración del plano en el storyboard: la acción tiene que caber ahí y después
# quedarse casi quieta, para que el montaje recorte sin cortar el gesto.
DUR = {"P01": 1.5, "P02": 4.5, "P03": 0.8, "P04": 1.0, "P05": 1.2, "P06": 1.5, "P07": 1.5,
       "P08a": 0.7, "P08b": 0.7, "P08c": 0.7, "P09": 1.5, "P10": 1.5, "P11a": 0.6, "P11b": 2.2,
       "P12": 1.5, "P13": 2.0, "P14": 1.5, "P16": 2.0, "P17": 2.3, "P18": 1.7, "P19": 1.0, "P20": 1.2, "P21": 1.2, "P22": 1.5,
       "N01": 1.5, "N02": 1.0, "N03": 1.0, "N04": 1.5, "N05": 1.5, "N06": 1.5, "N07": 1.5, "N08": 2.0,
       "N09": 2.0, "N10": 1.5, "N11": 1.5, "N13": 1.2, "N14": 2.0, "N15": 1.5, "N16": 2.0, "N17": 1.5, "N18": 2.0, "N19": 2.0, "N20": 1.2, "N21": 2.0, "N22": 2.0, "P02b": 3.0, "N23": 2.0, "N24": 2.0, "N25": 2.0}

# plano: (prompt de movimiento, keyframe final o None, coda)
MOV = {
    "P01": ("Very slow push-in towards the blank yellow sticky note, about 5 percent. Nothing else "
            "moves except a faint flicker of the background bokeh.", None, None),
    "P02": ("Static camera. The man glances at the sticky note, closes the laptop lid slowly and "
            "casually with both hands, leans back, stretches a little, then stands up at a relaxed "
            "natural human pace, picks the jacket off the chair and turns to leave. Half smile, zero "
            "guilt. Natural human weight and timing, no rush, no jerky movement.", None, "fisica"),
    "P03": ("Locked-off camera. The office lights switch off zone by zone, from the camera towards "
            "the back, in three quick steps, until only the far zone and the city lights remain. "
            "No people.", None, "fisica"),
    "P04": ("Static camera. Continuous paper slowly feeds out of the printer character. Her heavy "
            "eyelids lower slowly to half closed: bored, 'here we go again'. Nothing else moves.",
            None, None),
    "P05": ("Slight handheld shake. The small white robot trembles fast all over, backs away two "
            "tiny nervous steps clutching the paper, the pink flag on his mast vibrating, his LED "
            "eyes flickering small and worried. Panic, not anger.", None, "fisica"),
    "P06": (G_FIJO + "Static camera, very slight dolly-in. G lifts his helmet from the panel and "
            "turns it slightly towards the right, noticing someone off-screen who needs him; at that "
            "moment a thin pink halo ring switches on above his helmet, tracing itself around the "
            "circle, and he takes one small step forward.", "kf_k1.png", None),
    "P07": (G_FIJO + "Static camera. G's hand rests gently on the small white robot's helmet; the "
            "robot's trembling slowly stops and his eyes relax; G takes the paper with his other "
            "hand. Calm and brief.", None, "fisica"),
    "P08a": (G_FIJO + "Static camera. G types very fast on the holographic keyboard; blocks of "
             "abstract lines fill the tall panel from top to bottom.", None, None),
    "P08b": (G_FIJO + "Static camera. Image tiles fly in and snap into the large floating grid as "
             "G spreads his arms wider, like an art director framing a layout.", None, None),
    "P08c": (G_FIJO + "Static camera. The last panels fold away into the single small panel with "
             "the check mark; G gives one short satisfied tap in the air and stays still.",
             None, None),
    "P09": (G_FIJO + "Static over-the-shoulder camera. G's raised hand freezes in mid-air; an "
            "empty notification card slides into the holographic panel and stops.", None, None),
    "P10": ("Static camera. The printer character slides the drawer of the filing cabinet open and "
            "holds the old folder out towards G without turning to look at him. G stays still, "
            "waiting.", None, "fisica"),
    "P11a": ("Static insert. The small gloved hands hold the dusty folder; a tiny tilt as if "
             "reading its label. Nothing else moves.", None, None),
    "P11b": (G_FIJO + "Static camera. G tilts his helmet down to look at the folder in his hands, "
             "then turns his helmet only about 30 degrees to his left, towards someone standing "
             "off-screen left, keeping his glowing visor clearly visible in three-quarter view, and "
             "holds that look completely still for a long deadpan beat. His body does not turn. He "
             "never shows the back of his helmet and never looks at the camera.", None, None),
    "P12": (G_FIJO + "Very slow push-in on the visor. The dot-matrix G slowly dims and the thin "
            "battery bar under it shrinks towards empty.", None, None),
    "P13": ("Locked-off camera, almost a still: the paper stops coming out of the printer, the "
            "halo above G dims slightly, nobody moves. Quiet relief.", None, None),
    "P14": ("Static camera at floor level. The small white robot collapses: sits down hard, "
            "legs splay, tips slowly to one side, his LED eyes fading to two flat lines.",
            None, "fisica"),
    "P16": (G_FIJO + "Static camera. On G's visor the pink dot-matrix pixels glitch and scramble "
            "into a dim 'X X'; the halo flickers and switches off; the headphone lights fade out; "
            "his helmet tilts slightly down and he goes completely still.", None, None),
    "P17": ("Static camera. Morning. The man settles into his chair with his coffee, opens the "
            "laptop fully, looks at the screen and smiles to himself, satisfied. He does not look "
            "at the camera.", None, "fisica"),
    "P18": (G_FIJO + "Static camera. G stays completely still and powered off. The small white "
            "robot presses the yellow sticky note flat onto G's visor, smooths it once with one "
            "finger, then lets go and steps back. The sticky note STAYS STUCK on G's visor for the "
            "rest of the shot; nobody removes it. In the background the printer keeps printing.",
            None, "fisica"),
    # ── GUION V2 (25-09-2026) ──
    "P19": ("Static camera. The freshly printed sheet slides neatly down into the open drawer of the "
            "filing cabinet, and the drawer slides shut with one dry push. The printer character stays "
            "calm, eyelids half closed. Routine, precise.", None, "fisica"),
    "P20": ("Slight handheld follow. The small white robot runs badly across the floor carrying the tall "
            "wobbling tower of paper; the tower leans, several sheets slip off and flutter to the floor, "
            "he stumbles but keeps going. Getting out of control.", None, "fisica"),
    "P21": ("Static camera. The clean manila folder rises smoothly out of the open drawer and is offered "
            "towards the right edge of frame. The printer character does not turn or react at all, "
            "eyelids half closed, perfectly deadpan.", None, "fisica"),
    "P22": ("Locked-off camera, almost still. The robot sitting on the bench sighs, his helmet sinking a "
            "little lower; the small robot on the floor twitches once; in the background the printer "
            "keeps printing, paper slowly feeding out. Exhausted morning calm.", None, "fisica"),
    # ── GUION V3 «MAÑANA LO VEO» (25-09-2026) ──
    "N01": ("Static macro camera. The hand quickly writes one short line with the blue pen along the "
            "bottom of the yellow sticky note, left to right, then lifts the pen away and leaves frame. "
            "The sticky note does not move.", None, "fisica"),
    "N02": ("The camera plunges fast straight DOWN the shaft following the capsule as it rushes down "
            "inside the glass tube; the pink floor lamps flash past one after another; strong speed.",
            None, None),
    "N03": ("Static camera. The capsule drops into the wire basket with a small bounce and settles. "
            "The printer character beside it lifts her heavy eyelids a tiny bit, then lowers them.",
            None, "fisica"),
    "N04": (G_FIJO + "Static camera. G taps the chin of his helmet twice with one finger, tilts his "
            "helmet slowly to one side and then the other, pondering, looking down at the folder.",
            None, None),
    "N05": (G_FIJO + "Static camera. The column of light from the ceiling hatch intensifies and "
            "pulses; glowing dust particles swirl down inside the beam; G stays seated, helmet raised "
            "to the light, completely still, his visor glowing brighter.", None, None),
    "N06": ("Slow dramatic push-in towards the colossal robot deity. Its huge pink eyes pulse "
            "brighter and the beams from them intensify; golden clouds drift; the head nods very "
            "slightly downward, solemn.", None, None),
    "N07": (G_FIJO + "Static camera. The streams of glowing light filaments pour faster and faster "
            "into the top of his helmet; the visor flashes brighter in pulses; the halo ring glows "
            "intensely. G does not move.", None, None),
    "N08": (G_FIJO + "Static camera with a slight shake. G types furiously fast on the keyboard with "
            "both hands; papers fly off the bench; the screens flicker with abstract pink shapes.",
            None, "fisica"),
    "N09": ("Static high-angle camera. The small white robot runs fast in a tight circle, arms "
            "flailing; paper sheets swirl around him in a vortex; the pink flag flaps. Comedic "
            "panic.", None, "fisica"),
    "N10": (G_FIJO + "Static camera. G shoves the capsule into the brass hatch, slams the little "
            "hatch lid shut with his palm, and the capsule is sucked away upward inside the glass "
            "tube out of frame.", None, "fisica"),
    "N11": ("Static camera. The capsule pops out of the brass hatch, lands on the desk and rolls a "
            "little, then stops. Dawn light slowly brightens through the windows. Nobody there.",
            None, "fisica"),
    "N13": ("Static camera. After half a second, a sudden comedic cartoon explosion bursts from the "
            "middle of the group: a bright flash, a big puff of grey smoke and papers blasting "
            "outward. When the smoke thins the three are still standing in the same place, blackened "
            "with soot. Cartoon logic, not scary, nobody is hurt.", None, None),
    "N14": ("Static camera. Thin smoke wisps rise from the three soot-covered characters; singed "
            "papers float slowly down; G's bent halo crackles with a tiny spark; they blink once, "
            "deadpan. Nothing else moves.", None, None),
    # ── CORTE 4 ──
    "N15": (G_FIJO + "Static camera. G and the small white robot hold their look at each other, "
            "completely still for a beat; then both snap their heads back to their work at the same "
            "instant and their hands start moving fast.", None, None),
    "N16": ("Static camera. The man looks at the laptop screen, raises both shoulders in a slow "
            "indifferent shrug with palms up, tilts his head, lets the shoulders drop, then reaches to "
            "the trackpad and clicks once. Colleagues keep moving out of focus behind him. Natural "
            "human pace.", None, "fisica"),
    # ── CORTE 5 ──
    "N17": (G_FIJO + "Static camera. The small white robot lifts the big poster tube higher, proud, "
            "wobbling under its weight; G slowly drags his hand down his visor and shakes his helmet "
            "once, slowly. Nothing else moves.", None, "fisica"),
    "N18": (G_FIJO + "Static camera. G jabs his finger at the panel twice; the small white robot waves "
            "both arms up and down, stamps one foot, his flag whipping; they lean closer to each other. "
            "Fast, comedic, cartoon energy, but both stay in place.", None, "fisica"),
    "N19": ("Static camera. The paper keeps pouring out of the printer in loops, piling higher; the "
            "small white robot struggles in the paper, flailing, sinking a little deeper, flag flapping. "
            "The printer does not react.", None, "fisica"),
    "N20": (G_FIJO + "Static camera. The two small fists bump once with a tiny bounce, then both "
            "characters snap back to their work at the same instant, fast.", None, None),
    "N21": (G_FIJO + "Static camera. The small white robot presses the sticky note flat onto the visor, "
            "smooths it once with one finger, steps back and looks at it, satisfied. The big robot stays "
            "completely still and powered off. Smoke wisps drift. The sticky note STAYS on the visor.",
            None, "fisica"),
    # ── CORTE 6 ──
    "N22": (G_FIJO + "Static camera. The three mugs clink together once with a small bounce; G leans back "
            "slowly and relaxed; the small white robot takes a sip from his tiny cup and his LED eyes turn "
            "into two happy arcs; the printer's eyelids droop a little further. Slow, warm, tired. No halo "
            "appears at any point.", None, "fisica"),
    # ── CORTE 7 ──
    "P02b": ("Handheld camera with a slight natural sway. Seen from behind, the man looks at the sticky "
             "note for a moment, closes the laptop lid slowly with both hands, then pushes his chair "
             "back and stands up at a natural unhurried human pace, his back and shoulder filling more "
             "of the frame as he rises. Real human weight and timing, no jerky movement, nothing else "
             "changes.", None, "fisica"),
    "N23": (G_FIJO + "Static camera. G presses the pushpin in and immediately grabs the next sketch "
            "from the strip coming out of the printer; the small white robot bounces on his feet "
            "holding the pin box up; sketches flutter on the board. Busy, creative, fast.", None, "fisica"),
    "N24": (G_FIJO + "Static camera. Both pull harder, leaning further back, the paper stretching; "
            "then the sheet TEARS in the middle and both fall backwards onto their bottoms in opposite "
            "directions, each holding half a sheet. The printer in the back does not react.",
            None, "fisica"),
    "N25": (G_FIJO + "Static camera. The small white robot drags the giant brush across the panel in "
            "one big wild stroke, paint splattering; G, unbothered, slides the ruler along the panel and "
            "taps it twice with one finger, precise. Nothing else moves.", None, "fisica"),
}
# P15 reutiliza el clip de P09 (mismo encuadre; la notificación va en post).


def correr(p):
    prompt, fin, coda = MOV[p]
    prompt = (prompt + f" The whole action happens within the first {DUR[p]:.1f} seconds; "
              "afterwards everything holds almost still. " + REGLAS)
    destino = OUT / f"{p}.mp4"
    if destino.exists():
        return f"= {p} ya existe"
    fuente = {"N13": "P13"}.get(p, p)
    base = [sys.executable, str(RAIZ / "scripts/magnific-video.py"), str(PLANOS / f"{fuente}.png"),
            "--out", str(destino), "--prompt", prompt, "--dur", "5"]
    if coda:
        base += ["--coda", coda]
    # 24-09-2026: Kling 2.5 falló 7 de 8 tareas tras una hora en cola; Hailuo 02
    # entregó P07 en 2 min, vertical y con G intacto. Hailuo va primero; Kling
    # queda de respaldo. Hailuo sólo hace 6 s.
    base = [x if x != "5" else "6" for x in base]
    intentos = [base + ["--modelo", "minimax-hailuo-02-1080p"]] \
        + ([[x if x != "6" else "5" for x in base] + ["--modelo", "kling-v2-1-pro", "--fin", str(REFS / fin)]] if fin else [])
    log = ""
    for cmd in intentos:
        r = subprocess.run(cmd, capture_output=True, text=True)
        log = (r.stdout + r.stderr)[-300:]
        if r.returncode == 0 and destino.exists():
            modelo = cmd[cmd.index("--modelo") + 1]
            return f"✓ {p} ({modelo}{', con frame final' if '--fin' in cmd else ''})"
    return f"✗ {p}\n{log}"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pedidos = sys.argv[1:] or list(MOV)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for linea in ex.map(correr, pedidos):
            print(linea, flush=True)
    p09, p15 = OUT / "P09.mp4", OUT / "P15.mp4"
    if p09.exists() and not p15.exists():
        p15.write_bytes(p09.read_bytes()); print("= P15 ← P09")


if __name__ == "__main__":
    main()

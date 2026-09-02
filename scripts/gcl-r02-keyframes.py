#!/usr/bin/env python3
"""
R02 «Turno de noche» — genera los keyframes del capítulo 2 de G.CL.

Storyboard: gcl-agent/R02_STORYBOARD.md. Cada clave de PLANOS es el nombre del
plano ahí (p01, p02, …), así que se puede regenerar uno solo sin tocar el resto.

DOS FAMILIAS, DOS MODELOS
  · Planos de OFICINA sin personaje → Mystic (`generar`): ambiente y fondo.
  · Planos con G.CL → Nano Banana Pro (`pro`) **con el master como referencia**.
    Es el candado 1 del protocolo de consistencia (GCL_CHARACTER_BIBLE): ninguna
    imagen del personaje se genera text-only.

POR QUÉ LOS PLANOS QUEDAN EN JPEG
Nano Banana Pro devuelve PNG de 1536×2752: los 13 planos pesan 49 MB y no pueden
viajar así en el repo. Convertidos a JPEG 93 sin submuestreo de croma pesan
7,9 MB y son indistinguibles en pantalla — además el montaje les pasa grano,
gradación y desenfoque encima. La composición lee los `.jpg`.

LO QUE ARREGLAN ESTOS PROMPTS (feedback del director, cap. 1: «el personaje se
ve muy sobrepuesto»): todos los planos con G.CL exigen explícitamente **sombra
de contacto** en la superficie donde se apoya y **derrame de luz del visor**
sobre lo que tiene al lado. Sin eso el render se ve pegado encima aunque el
pipeline sea correcto.

Uso:
    python3 scripts/gcl-r02-keyframes.py             # todos los que falten
    python3 scripts/gcl-r02-keyframes.py --solo p05  # uno
    python3 scripts/gcl-r02-keyframes.py --rehacer   # regenera aunque exista
"""
import argparse
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "public", "assets", "gcl", "r02")
MASTER = os.path.join(RAIZ, "gcl-agent", "character-master", "gcl_master_frontal_logo.png")
MAGNIFIC = os.path.join(RAIZ, "scripts", "magnific.py")

# Bloque canónico del personaje — copiado VERBATIM de GCL_PROMPT_LIBRARY.md.
# No parafrasear: es lo que mantiene al personaje igual entre capítulos.
CANONICO = (
    "G.CL, a premium collectible chibi robot mascot, high-end vinyl designer-toy 3D "
    "render. CRITICAL PROPORTIONS: an oversized glossy piano-black spherical "
    "astronaut-helmet HEAD taking up almost half of the total body height, on a small "
    "compact rounded body. Seamless reflective black dome visor displaying a glowing "
    "electric-pink dot-matrix letter \"G\", black over-ear headphone pods with a thin "
    "glowing coral-orange light ring on each side of the helmet, matte black techwear "
    "suit with a tiny electric-pink \"G.CL\" wordmark on the chest, short rounded arms "
    "with black rounded glove hands, short stubby legs, chunky black sneakers with "
    "glowing coral-pink soles. "
)

# Integración: lo que evita el «personaje sobrepuesto».
INTEGRA = (
    "CRITICAL INTEGRATION: the character casts a soft dark CONTACT SHADOW on the "
    "surface it rests on, directly under its body, and the pink glow of its visor "
    "SPILLS onto the nearby surfaces and edges, tinting them faintly pink. The "
    "character is lit by the same light as the room. Shallow depth of field with the "
    "character in focus and the background softer than the character. "
    "Cinematic anamorphic look, 4K, no text, no letters, no watermark. "
)

NEG = (
    "no cheap toy look, no childish primary colors, no generic cute robot, no human "
    "body proportions, no slim human legs, no deformed hands, no extra limbs, no "
    "changing helmet shape, no green neon, no blue AI aesthetic, no random holograms, "
    "no cyberpunk cliche, no text, no letters, no watermark."
)

# Ambiente común de la oficina: es la MISMA oficina en todo el capítulo.
OFICINA = (
    "interior of a modern minimal advertising agency office in Santiago de Chile at "
    "night, empty, lights off, only the cold blue glow of sleeping monitors and warm "
    "amber city light coming through big windows, dark grey and black surfaces, light "
    "wood table, glass partitions, cinematic anamorphic photography, shallow depth of "
    "field, deep shadows, film grain, no people, no text, no letters, no logos, "
    "no watermark, photorealistic"
)

# ---------------------------------------------------------------------------
# EL SET. Todo el episodio pasa en LA MISMA sala de reuniones — no en un vacío
# negro abstracto, que es lo que hacía que la v2 se viera como láminas sueltas.
# Por eso casi todos los planos llevan `p05_el_noche.jpg` como referencia además
# del master del personaje: fija el mueble, la ventana, la altura de cámara y la
# escala del personaje sobre la mesa. Un set, muchos planos.
# ---------------------------------------------------------------------------
SET = os.path.join(SALIDA, "p05_el_noche.jpg")

MISMO_SET = (
    "Same meeting room, same camera position and same framing as the reference "
    "image: seen from the far end of a long light-wood meeting table at table "
    "height, big window with the city on the right, glass partitions on the left. "
)

# (modelo, prompt, aspecto, referencias extra)
#   "mystic" → ambiente sin personaje · "pro" → con referencias
# ---------------------------------------------------------------------------
PLANOS = {
    # ---------- ACTO 1 · se van ----------
    "c01_se_van": ("mystic",
        "Two coworkers seen from behind walking away towards the office door at "
        "night, putting on their jackets, mid-conversation, one of them laughing, "
        "faces not visible, back view only, natural motion blur, handheld camera "
        "feel, " + OFICINA, []),

    "c02_interruptor": ("mystic",
        "Extreme close-up of a hand pressing a black light switch on a dark office "
        "wall, the room behind falling into darkness, only rim light on the "
        "fingers, very shallow depth of field, " + OFICINA, []),

    # c03_puerta salió del capítulo — ver la nota en gcl-r02-clips.py.

    # Hay que VER que quedó apagado, no sólo la mano bajándolo.
    # v2: la primera salió con un piloto encendido en el propio interruptor, que
    # dice justo lo contrario de lo que tiene que decir el plano.
    "c02b_apagado": ("mystic",
        "Extreme close-up of a plain black light switch on a dark office wall, now "
        "in the DOWN / OFF position, nobody touching it. The switch is COMPLETELY "
        "DARK: no indicator light, no LED, no glow of any kind on it. The room "
        "behind is dark with only a faint cold glow from far windows, very shallow "
        "depth of field, " + OFICINA, []),

    "c04_mesa_vacia": ("pro",
        "EXACTLY the same shot as the reference image — same camera, same framing, "
        "same furniture, same night lighting — but the table is COMPLETELY EMPTY: "
        "there is no character and no robot anywhere in the frame. Just the empty "
        "meeting table in the dark office at night, lit only by the blue city "
        "outside. " + NEG,
        [SET]),

    # ---------- ACTO 2 · LA LLEGADA (v4) ----------
    # El portal ya no escupe una zapatilla: **él lo abre con las manos**. La
    # versión anterior se leía rara —«sale una zapatilla» no dice nada del
    # personaje— y encima Kling le apagaba la suela coral. Ahora la entrada
    # cuenta algo: rompe el aire, se abre paso y aterriza como quien llega a
    # trabajar sabiendo que lo esperan.
    "c05_grieta": ("pro",
        MISMO_SET +
        "A narrow VERTICAL CRACK of blinding electric-pink light has torn open in "
        "mid-air just above the centre of the empty meeting table, like a rip in "
        "the room. TWO SMALL ROUNDED BLACK GLOVED ROBOT HANDS have come through it "
        "and are gripping its two edges from inside, about to pull it apart. "
        "Nothing else of the body is visible yet. The pink light spills across the "
        "wood. " + INTEGRA + NEG,
        [os.path.join(SALIDA, "c04_mesa_vacia.jpg"), MASTER]),

    "c06_abre": ("pro",
        CANONICO + MISMO_SET +
        "He is PULLING THE RIP OF PINK LIGHT WIDE OPEN with both short arms, one to "
        "each side, like opening a pair of curtains, and his big glossy black "
        "helmet with the pink G is already through, leaning out into the dark "
        "office. Sparks fly from the edges he is holding. " + INTEGRA + NEG,
        [os.path.join(SALIDA, "c05_grieta.jpg"), MASTER]),

    "c07_salta": ("pro",
        CANONICO + MISMO_SET +
        "He has just LEAPT OUT of the closing portal and is caught MID-AIR above "
        "the meeting table, both short arms thrown up and out in triumph, legs "
        "tucked, about to land. The portal is a shrinking pink ring behind him. "
        "Low heroic angle. " + INTEGRA + NEG,
        [os.path.join(SALIDA, "c05_grieta.jpg"), MASTER]),

    "c08_guino": ("pro",
        CANONICO +
        "CLOSE-UP of him standing on the meeting table, leaning slightly towards "
        "camera, one arm raised in a small salute. The visor shows a WINK: the "
        "left eye is a short curved pink dot-matrix arc, closed, and the right eye "
        "is one round pink dot, open. Behind him the dark office. " + INTEGRA + NEG,
        [SET, MASTER]),

    # ---------- ACTO 3 · a trabajar ----------
    "c09_chasquea": ("pro",
        CANONICO + MISMO_SET +
        "He stands on the meeting table with one arm extended, having just snapped "
        "his fingers, and a RING of floating translucent glowing panels is igniting "
        "in the air all around him above the table — abstract pink charts and grids, "
        "no readable text. Their light fills the dark room. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c11_enfocado": ("pro",
        CANONICO +
        "MEDIUM CLOSE-UP of him facing camera, head slightly tilted, the visor "
        "showing a FOCUSED expression: two narrow horizontal pink dot-matrix eyes "
        "instead of the G. Behind him, out of focus, floating glowing panels and "
        "the dark office. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c12_manotea": ("pro",
        CANONICO + MISMO_SET +
        "Seen closer, he swipes one floating translucent glowing panel away to the "
        "left with his short rounded arm, motion blur on the panel he is pushing, "
        "the next panel already sliding in from the right, standing on the meeting "
        "table. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c14_patron": ("pro",
        CANONICO + MISMO_SET +
        "THREE IDENTICAL glowing pink panels have lined up in a neat row floating "
        "in front of him — the same little bar-chart shape repeated three times — "
        "and he is pointing at them with one arm, caught mid-air in a small happy "
        "hop, both feet slightly off the table. The visor shows an EXCITED "
        "expression: two big round pink dot-matrix eyes. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c15_alerta": ("pro",
        CANONICO + MISMO_SET +
        "One floating panel has turned CORAL ORANGE and he is startled by it: he "
        "leans back, and TWO other panels have slipped out of his hands and are "
        "tumbling down through the air, which he is trying to catch. The visor "
        "shows an ALERT expression: a coral dot-matrix exclamation mark. The coral "
        "light washes over his black helmet. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c16_teclea": ("pro",
        CANONICO + MISMO_SET +
        "He sits cross-legged on the meeting table typing in the air with both "
        "short rounded arms, and ONE large translucent glowing panel floats "
        "upright in front of him filling the left half of the frame — abstract "
        "glowing lines, no readable text. He is small and sits on the right side "
        "of the frame. The panel lights his helmet from the side. " + INTEGRA + NEG,
        [SET, MASTER]),

    # Más intención y emoción en el análisis: que encuentre, que se sorprenda y
    # que corrija — no que sólo mire paneles.
    "c13_sorpresa": ("pro",
        CANONICO + MISMO_SET +
        "He has just found something: he recoils half a step back with both short "
        "arms flung up, and ONE floating panel in front of him is glowing much "
        "brighter than the rest. The visor shows SURPRISE: two big wide round pink "
        "dot-matrix eyes. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c17_corrige": ("pro",
        CANONICO + MISMO_SET +
        "He is FIXING something: he reaches both short arms into a floating panel "
        "and pushes one of its bars back into line with the others, which are now "
        "even. The visor shows a small pink dot-matrix CHECK MARK instead of the G. "
        + INTEGRA + NEG,
        [SET, MASTER]),

    # ---------- ACTO 4 · amanece y LLEGA EL EQUIPO (v4) ----------
    # Se cayó el remate del sueño: **G.CL no duerme**, y que se durmiera lo
    # contradecía. Ahora el capítulo cierra con el traspaso: llega el equipo,
    # lo saludan, y él choca los cinco. La noche se entrega en la mano.
    "c19_amanece": ("pro",
        "EXACTLY the same shot, same framing and same camera position as the "
        "reference image, and the same character standing awake on the same table "
        "— change only the light: it is now 7:40 in the morning and warm golden "
        "sunrise light floods in through the big window from the right, long soft "
        "shadows across the table. The last floating panels are fading out around "
        "him. He is awake, standing, the pink G bright on the visor. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c20_llegan": ("pro",
        CANONICO +
        "Morning in the same meeting room, warm golden light. THREE PEOPLE are "
        "arriving around the long meeting table with coffee cups and laptops, "
        "smiling and greeting, seen from behind and in three-quarter view, faces "
        "soft-focus and partly out of frame. He stands small on the table in the "
        "middle facing them, arm raised in greeting. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c21_highfive": ("pro",
        CANONICO +
        "CLOSE-UP, warm morning light: a human hand reaching in from the right and "
        "the small rounded BLACK GLOVED HAND of the chibi robot reaching up from "
        "the left, meeting in a HIGH FIVE right in the middle of the frame, palms "
        "together, a soft coral glow where they touch. His helmet with the pink G "
        "is visible below the hand, slightly out of focus. " + INTEGRA + NEG,
        [SET, MASTER]),

    "c22_equipo": ("pro",
        CANONICO +
        "Wide morning shot of the same meeting room: FOUR PEOPLE now sit and stand "
        "around the long table with coffee and laptops, all turned towards him and "
        "smiling, faces soft and partly out of frame. He stands on the middle of "
        "the table facing them with both arms slightly open, the pink G bright. "
        "One large translucent pink panel floats above the table between them. "
        "Warm golden light. " + INTEGRA + NEG,
        [SET, MASTER]),

    # c21_mesa (la mano tomando la tablet) salió del capítulo: el cierre ya no
    # es un objeto, es el traspaso al equipo — ver c21_highfive.
}


def a_jpeg(png):
    """PNG de 3,8 MB -> JPEG de 0,6 MB. Es lo que permite versionar los planos."""
    try:
        from PIL import Image
    except ImportError:
        print("   (sin PIL: el plano queda en PNG y NO va a entrar al repo)")
        return png
    jpg = png[:-4] + ".jpg"
    Image.open(png).convert("RGB").save(
        jpg, "JPEG", quality=93, subsampling=0, optimize=True)
    os.remove(png)
    return jpg


def genera(nombre, rehacer=False):
    modelo, prompt, refs = PLANOS[nombre]
    destino = os.path.join(SALIDA, nombre + ".png")
    if os.path.exists(destino[:-4] + ".jpg") and not rehacer:
        print(f"·  {nombre} ya está — salto")
        return True
    faltan = [r for r in refs if not os.path.exists(r)]
    if faltan:
        print(f"✗  {nombre}: falta la referencia {os.path.basename(faltan[0])}")
        return False
    cmd = [sys.executable, MAGNIFIC, "pro" if modelo == "pro" else "generar",
           prompt, "--out", destino, "--aspecto", "reel"]
    if modelo == "pro":
        cmd += ["--resolucion", "2K", "--refs"] + refs
    print(f"→  {nombre} · {modelo}")
    r = subprocess.run(cmd, cwd=RAIZ)
    ok = r.returncode == 0 and os.path.exists(destino)
    if ok:
        a_jpeg(destino)
    print(("✓  " if ok else "✗  ") + nombre)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", nargs="*", help="nombres de plano (p05_el_noche…)")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()
    os.makedirs(SALIDA, exist_ok=True)
    # p17 depende de p05: el orden del diccionario ya lo respeta.
    nombres = a.solo if a.solo else list(PLANOS)
    for n in nombres:
        if n not in PLANOS:
            print(f"✗  No existe el plano «{n}». Hay: {', '.join(PLANOS)}")
            continue
        genera(n, a.rehacer)
    print(f"\nEn {os.path.relpath(SALIDA, RAIZ)}:")
    for f in sorted(os.listdir(SALIDA)):
        print("   ", f)


if __name__ == "__main__":
    sys.exit(main())

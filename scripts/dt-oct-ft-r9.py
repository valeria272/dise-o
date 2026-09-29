"""DT ST 01-10 Family Time, RONDA 9 — la familia aprobada (25-09) en las tres escenas de la story.

Eli 29-09: «hay fotos… desapariciones de rostro, de narices… recuerda que ya tenemos nuestro
personaje para Family Time». En la r8 el papá y el niño del desayuno NO eran papa-A / nino-A,
y la r7 (la de Drive) traía la foto de las almohadas con caras tapadas y el papá cortado.

Técnica (memoria foto-por-partes-se-regenera-entera): Nano Banana Pro 4K en 9:16 con la escena
de la r8 como imagen 1 (fondo real de DT ya expandido, composición resuelta) + las 4 hojas y
las 4 caras aprobadas. Se re-rinde la foto ENTERA con las identidades correctas.

Uso:  py scripts/dt-oct-ft-r9.py [escena ...]      (VAR=b para la segunda variante)
"""
import os, subprocess, sys, concurrent.futures as cf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, "scripts/dt-familia")
from ronda3 import ANAT, NAT  # noqa: E402  (checklist de anatomía de Eli 25-09)

P = "clients/hilton/dt-familia/personajes/"
REFS = [P + "mama-D.png", P + "papa-A.png", P + "nina-B.png", P + "nino-A.png",
        P + "cara-mama-D.png", P + "cara-papa-A.png", P + "cara-nina-B.png", P + "cara-nino-A.png"]
OSC = "public/assets/hilton/dt/oct/"
R = "raw/hilton/dt/oct/r9/"

KEEP = ("Image 1 is the layout of a REAL photograph of the DoubleTree hotel in Santiago, vertical 9:16 story. "
        "Re-render it as one single clean, coherent, sharp professional photograph: keep exactly the same room, "
        "architecture, furniture, materials, colors, lamps, light and camera position and framing, and keep the "
        "family in the same places, poses and scale. What changes is WHO the people are: replace the four people "
        "with exactly the four approved persons below, with their faces fully visible and in sharp focus — every "
        "face complete with both eyes, nose and mouth clearly drawn, nothing covering or blurring any face, no "
        "face turned fully away. Nobody is cut by the edges of the frame. No other people in the image.")
WHO = ("IDENTITY IS CRITICAL. MOTHER = images 2 and 6 (38, dark chestnut long wavy hair — DARK brown, NOT red, NOT "
       "auburn —, warm brown eyes, olive-golden skin, full cheeks); FATHER = images 3 and 7 (38, short DARK brown hair "
       "with NO grey, short dark stubble beard, dark brown eyes); DAUGHTER = images 4 and 8 (about 9, shoulder-length "
       "MEDIUM-BROWN hair with soft waves — NOT red, NOT ginger, NOT curly; brown eyes); SON = images 5 and 9 (about 7, "
       "short messy DARK brown hair, brown eyes). All four share the same warm olive-golden Chilean skin tone. Same "
       "faces, hair and ages as the references.")

ESCENAS = {
    "lobby": (OSC + "ft-f-lobby.jpg",
        "Scene: the family arrives walking together through the lobby towards the camera, relaxed and happy; the "
        "father pulls a rolling suitcase, the mother holds the son's hand, the daughter walks at the left with a small "
        "backpack. They look at each other, not at the camera. Show all four from head to at least the knees."),
    # ⚠️ Con las caras de la r8 visibles, NB copió al papá y al niño de la r8 (no papa-A / nino-A):
    # la imagen 1 va con las cabezas BORRONEADAS y la identidad sale sólo de las hojas.
    "desayuno": (R + "desayuno-sin-caras.jpg",
        "The heads in image 1 are blurred placeholders only: draw every head, face and hair EXCLUSIVELY from the "
        "reference persons, never from image 1. Scene: family breakfast at the one table closest to the camera. Each "
        "person sits on their OWN chair. The father pours orange juice into the daughter's glass, smiling at her; the "
        "daughter watches the juice; the mother holds a coffee cup smiling at the son; the son holds a croissant in "
        "his hand at chest height and smiles at his mother — his mouth and whole face uncovered. The rest of the "
        "restaurant stays empty."),
    "hab": (OSC + "ft-r8-hab.jpg",
        "Scene: the four sit together on the bed against the headboard looking at a tablet the daughter holds. Each "
        "person's legs and feet belong clearly to them: the mother's two feet together at the end of her legs, the "
        "kids' legs side by side, the father's legs on the right. Pajamas and soft loungewear."),
}


def generar(k):
    foto, escena = ESCENAS[k]
    suf = os.environ.get("VAR", "a")
    out = R + f"nb-{k}-{suf}.png"
    prompt = f"{KEEP} {WHO} {escena} {ANAT} {NAT}"
    r = subprocess.run(["py", "scripts/magnific.py", "pro", prompt, "--refs", foto, *REFS,
                        "--aspecto", "story", "--resolucion", "4K", "--out", out],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return k, "ok " + out if os.path.exists(out) else (r.stdout + r.stderr)[-400:]


if __name__ == "__main__":
    os.makedirs(R, exist_ok=True)
    ks = sys.argv[1:] or list(ESCENAS)
    with cf.ThreadPoolExecutor(3) as ex:
        for k, msg in ex.map(generar, ks):
            print(k, "→", msg)

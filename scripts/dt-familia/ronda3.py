"""Ronda 3 — más situaciones de la familia DT sobre fotos REALES del hotel.
Uso:  py scripts/dt-familia/ronda3.py generar|componer|escalar|formatos [escena ...]
Criterio de Eli (25-09): fondo real siempre; que pase por foto de sesión. Regla DT §A:
a un trabajador NO se le ve la cara en imagen (sólo torso y manos)."""
import sys, os, subprocess, concurrent.futures as cf
import numpy as np, cv2
from PIL import Image

A = "raw/hilton/dt/sesion-real/alta/"; M2 = "raw/hilton/dt/sesion-real/muestra2/"
R = "raw/hilton/dt/familia/r3/"; P1 = P2 = "clients/hilton/dt-familia/personajes/"
OUT = "out/hilton/dt/familia/entrega/"

COOKIE = ("the DoubleTree signature welcome cookie: a large warm chunky chocolate chip cookie with walnut pieces, "
          "golden-brown, irregular homemade edges, REAL-LIFE SIZE about 7 cm across — smaller than a child's palm; no packaging, no logos, no text")

# escena: (foto real, desplazamiento del cuadro 4:5, qué pasa)
ESCENAS = {
    "checkin": (M2 + "_MG_9219.jpg", 160,
        "Scene: check-in at the wooden reception desk. The parents stand at the counter, the father signing, the mother "
        "smiling down at the kids. A receptionist behind the counter is visible ONLY as hands and torso in a dark suit, "
        "face out of frame, handing two warm cookies to the kids; " + COOKIE + ". The daughter reaches up for hers, the "
        "son already holds his and looks at it delighted. A rolling suitcase beside them. No other people anywhere in the "
        "background: remove any standing staff or guests behind them."),
    "cookie-hab": (A + "HDT_65-hab.jpg", 1600,
        "Scene: afternoon in the room. ALL FOUR family members are in the picture. BOTH kids — the daughter AND the son — "
        "sit cross-legged side by side on the bed near the bathrobes, each biting into "
        + COOKIE + ", crumbs on their hands, sharing a glance and giggling. The mother sits at the edge of the bed with a "
        "cup of tea smiling at them; the father sits in the armchair by the window. Remove the champagne bottle and ice "
        "bucket from the bed. Soft daylight from the window."),
    "almohadas": (A + "HDT_57.jpg", 2900,
        "Keep the exact room of image 1 — same two beds, headboards, wall lamps, painting and carpet, same camera. "
        "Scene: playful pillow fight. The two kids stand on the nearer bed swinging hotel pillows at each other, laughing, "
        "hair messy, mid-motion; the father kneels on the other bed holding a pillow up as a shield, laughing; the mother "
        "sits at the foot of the bed laughing and watching. Pajamas. Duvet slightly rumpled where they stand. Natural "
        "motion, slight motion blur on the swinging pillows."),
    "lobby-cartas": (A + "HDT_37.jpg", 1800,
        "Scene: relaxed afternoon in the lobby lounge. The family sits around the low coffee table on the sofa and "
        "armchairs playing a card game: the son shows his cards to his father proudly, the daughter covers her mouth "
        "laughing, the mother leans in. Casual weekend clothes. Keep the exact same camera position, lens and framing of "
        "image 1 — same armchairs, bar and windows in the same places; the family sits in the existing armchairs in the "
        "foreground and the rest of the lobby stays unchanged and empty."),
    "restaurante": (A + "HDT_76.jpg", 1568,
        "Scene: family breakfast. ALL FOUR sit together at the SAME single square table — the table closest to the camera "
        "in the foreground, nobody at any other table. Each person sits on their OWN chair, "
        "clearly seated with the chair visible under them: father and daughter side by side on one side, mother and son "
        "on the other side facing them. The father pours orange juice into the daughter's glass; the son takes a bite of "
        "a croissant; the mother holds a coffee cup smiling at the son. Plates with fruit, bread and eggs. The rest of the "
        "restaurant stays empty and unchanged."),
    "vista": (A + "HDT_67-hab-vista.jpg", 600,
        "Scene: quiet moment in the room with the city view. The mother and the daughter sit together on the sofa "
        "reading a book, the daughter leaning on her mother's shoulder; the father stands by the big window with the son, "
        "pointing at the city skyline, the son on tiptoe looking out. Soft daylight."),
}

KEEP = ("Image 1 is a REAL photograph of the DoubleTree hotel: keep it exactly as it is — same architecture, furniture, "
        "materials, colors, lamps, window, light and camera framing. Do not add light patches, reflections, signs, logos, "
        "text or objects beyond what the scene needs. Only add the people (and the props in their hands) into this exact "
        "scene, with soft contact shadows matching the photo's light direction.")
WHO = ("IDENTITY IS CRITICAL. The four guests must be exactly these persons: MOTHER = images 2 and 6 (dark chestnut long "
       "wavy hair — DARK brown, NOT red, NOT auburn, NOT copper —, warm brown eyes, olive-golden skin, 38); FATHER = images 3 and 7 (short DARK brown hair with NO grey, "
       "short dark stubble beard, dark brown eyes, youthful 38); DAUGHTER = images 4 and 8 (about 9, shoulder-length "
       "MEDIUM-BROWN hair with soft waves — NOT red, NOT ginger, NOT auburn, NOT curly; brown eyes; olive-golden skin like "
       "her mother); SON = images 5 and 9 (about 7, short messy DARK brown hair, brown eyes). All four share the same warm "
       "olive-golden Chilean skin tone. Same faces, hair and ages as the references.")
# ⚠️ «freckles» en la niña la volvía pelirroja (3 de 5 escenas, 25-09): no se nombra.
NAT = ("It must pass as a real photo from a professional hotel photo session: candid documentary moment, nobody looks at "
       "the camera, natural relaxed expressions and eyes, soft genuine smiles and real laughter without exaggeration, "
       "natural catchlights. Real skin texture, natural hair flyaways, correct hands with five fingers, natural anatomy. "
       "Casual clothes in soft neutral and warm tones. Same exposure, white balance, lens and grain as the original photo.")
# ⭐ Eli 25-09: las correcciones que SIEMPRE vuelven — se previenen en el prompt, no se arreglan después.
ANAT = ("ANATOMY AND PLACEMENT CHECKLIST, mandatory: every person is physically supported — sitting on their own "
        "chair, sofa or bed, or standing on the floor — never floating or sitting on nothing; each person has exactly two "
        "arms, two legs and two feet, all visible limbs complete and connected, no missing or extra legs or feet, no "
        "limbs merging into furniture or into another person; every visible hand has five fingers with natural joints "
        "and correct grip on what it holds; eyes are alive and natural — both eyes looking at the same point, real iris "
        "texture, moist catchlights, relaxed lids, no glassy or doll-like stare; objects at real-life scale.")
REFS = [P1 + "mama-D.png", P1 + "papa-A.png", P1 + "nina-B.png", P1 + "nino-A.png",
        P2 + "cara-mama-D.png", P2 + "cara-papa-A.png", P2 + "cara-nina-B.png", P2 + "cara-nino-A.png"]


def cuadro(k):
    foto, off, _ = ESCENAS[k]
    O = Image.open(foto).convert("RGB"); W, H = O.size
    if H > W:  # vertical: 4:5 a ancho completo
        ch = int(W * 5 / 4); y0 = min(off, H - ch)
        return O, (0, y0, W, y0 + ch)
    cw = int(H * 4 / 5); x0 = min(off, W - cw)
    return O, (x0, 0, x0 + cw, H)


SUF = os.environ.get("VAR", "")
# SOLO_CARAS=1: sólo las 4 caras de frente (menos referencias = el modelo se confunde menos de persona)
if os.environ.get("SOLO_CARAS"):
    REFS = REFS[4:]
    WHO = WHO.replace("images 2 and 6", "image 2").replace("images 3 and 7", "image 3").replace("images 4 and 8", "image 4").replace("images 5 and 9", "image 5")


def generar(k):
    O, box = cuadro(k); os.makedirs(R + "fondos", exist_ok=True)
    O.crop(box).resize((1600, 2000), Image.LANCZOS).save(R + f"fondos/{k}.jpg", quality=93)
    prompt = f"{KEEP} {WHO} {ESCENAS[k][2]} {ANAT} {NAT} Hair colors are critical: mother DARK brown, father DARK brown, daughter medium brown, son DARK brown — nobody blond, nobody red-haired."
    r = subprocess.run(["py", "scripts/magnific.py", "pro", prompt, "--refs", R + f"fondos/{k}.jpg", *REFS,
                        "--aspecto", "carrusel", "--resolucion", "2K", "--out", R + f"nb-{k}{SUF}.png"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return k, "ok" if os.path.exists(R + f"nb-{k}{SUF}.png") else (r.stdout + r.stderr)[-300:]


def componer(k, umbral=30):
    gen = np.asarray(Image.open(R + f"nb-{k}.png").convert("RGB")); H, W = gen.shape[:2]
    real = np.asarray(Image.open(R + f"fondos/{k}.jpg").convert("RGB").resize((W, H), Image.LANCZOS))
    lab = lambda x: cv2.GaussianBlur(cv2.cvtColor(x, cv2.COLOR_RGB2LAB).astype(float), (0, 0), 3)
    d = np.sqrt(((lab(gen) - lab(real)) ** 2).sum(2))
    m = cv2.morphologyEx((d > umbral).astype(np.uint8), cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((41, 41), np.uint8))
    n, labm, st, _ = cv2.connectedComponentsWithStats(m); keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 0.004 * H * W: keep[labm == i] = 1
    keep = cv2.dilate(keep, np.ones((31, 31), np.uint8))
    cnts, _ = cv2.findContours(keep, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(keep, cnts, -1, 1, -1)
    a = cv2.GaussianBlur(keep.astype(float), (0, 0), 14)
    Image.fromarray((a * 255).astype(np.uint8)).save(R + f"mascara-{k}.png")
    return k, f"máscara {a.mean() * 100:.1f} % · diferencia arriba {d[:H // 4].mean():.1f}"


def escalar(k):
    Image.open(R + f"nb-{k}.png").convert("RGB").save(R + f"nb-{k}-q.jpg", quality=95)
    for _ in range(3):
        subprocess.run(["py", "scripts/magnific.py", "escalar", R + f"nb-{k}-q.jpg", "--precision",
                        "--out", R + f"x2-{k}.png"], capture_output=True)
        if os.path.exists(R + f"x2-{k}.png"): return k, "ok"
    return k, "FALLÓ el escalado (se usa la generada sin escalar)"


def formatos(k):
    O, (x0, y0, x1, y1) = cuadro(k); W, H = O.size; cw, ch = x1 - x0, y1 - y0
    src = R + f"x2-{k}.png" if os.path.exists(R + f"x2-{k}.png") else R + f"nb-{k}.png"
    gen = np.asarray(Image.open(src).convert("RGB").resize((cw, ch), Image.LANCZOS)).astype(float)
    a = np.asarray(Image.open(R + f"mascara-{k}.png").convert("L").resize((cw, ch), Image.LANCZOS)).astype(float)[..., None] / 255
    Mx = np.asarray(O).astype(float); Mx[y0:y1, x0:x1] = gen * a + Mx[y0:y1, x0:x1] * (1 - a)
    Mi = Image.fromarray(Mx.clip(0, 255).astype(np.uint8)); Mi.save(R + f"maestro-{k}.jpg", quality=93)
    ys, xs = np.where(a[..., 0] > 0.5); cx = int(xs.mean()) + x0; by1 = ys.max() + y0
    alta = W > 3000; os.makedirs(OUT, exist_ok=True); hechos = []
    post = (2250, 2813) if alta else (1080, 1350)
    Mi.crop((x0, y0, x1, y1)).resize(post, Image.LANCZOS).save(OUT + f"DT-familia-{k}-post-{post[0]}x{post[1]}.jpg", quality=93)
    hechos.append("post")
    sw, sh = (int(H * 9 / 16), H) if W / H > 9 / 16 else (W, int(W * 16 / 9))
    sx = int(np.clip(cx - sw / 2, 0, W - sw)); sy = int(np.clip((y0 + y1) / 2 - sh / 2, 0, H - sh))
    story = (2160, 3840) if alta else (1080, 1920)
    Mi.crop((sx, sy, sx + sw, sy + sh)).resize(story, Image.LANCZOS).save(OUT + f"DT-familia-{k}-story-{story[0]}x{story[1]}.jpg", quality=93)
    hechos.append("story")
    if W > H:
        hh = int(W * 9 / 16); wy = int(np.clip(by1 + 0.12 * hh - hh, 0, H - hh))
        Mi.crop((0, wy, W, wy + hh)).resize((3840, 2160), Image.LANCZOS).save(OUT + f"DT-familia-{k}-16x9-3840x2160.jpg", quality=93)
        hechos.append("16x9")
    return k, " + ".join(hechos)


if __name__ == "__main__":
    os.makedirs(R, exist_ok=True)
    paso = sys.argv[1]; ks = sys.argv[2:] or list(ESCENAS)
    f = {"generar": generar, "componer": componer, "escalar": escalar, "formatos": formatos}[paso]
    with cf.ThreadPoolExecutor(5) as ex:
        for k, msg in ex.map(f, ks): print(k, "→", msg)

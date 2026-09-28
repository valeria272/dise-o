"""Pulido de la familia DT (feedback de Eli 25-09): piernas, cookie a tamaño real, naipes reales,
borrar personas/reflejos, y que cada personaje se vea como su hoja.
Uso: py scripts/dt-familia/pulir.py editar|pegar|formatos [escena ...]

Método: Nano Banana retoca el cuadro 4:5 actual con una lista de arreglos + las 8 referencias; sólo las
zonas que CAMBIARON (diferencia contra el cuadro de partida) se pegan sobre el maestro en alta. Así el
resto de la foto —y el fondo real de DT— queda intacto."""
import sys, os, shutil, subprocess, concurrent.futures as cf
import numpy as np, cv2
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ronda3 as r3

R = r3.R; OUT = r3.OUT
IDENT = ("Make every family member look EXACTLY like their reference: " + r3.WHO)
BASE = ("Image 1 is a finished photo that needs retouching. Keep EVERYTHING identical — framing, background, "
        "architecture, furniture, light, colors, poses, clothing and composition — and change ONLY what is listed. "
        "The result must look like an untouched real photograph from a professional hotel photo session.")
FIX = {
    "checkin": "Fixes: (1) the two cookies must be a realistic real-life size, about 7 cm across — clearly smaller than "
               "a child's palm, not bigger than the hand; (2) completely remove the man in a suit standing in the "
               "background near the elevator and fill that area with the surrounding wall; (3) the MOTHER must have "
               "exactly the face, skin and long DARK CHESTNUT hair of her reference, not lighter or blonder.",
    "cookie-hab": "Fixes: (1) the MOTHER must have exactly the face of her reference and DARK CHESTNUT brown hair — "
                  "NOT red, NOT auburn; (2) the cookies must be a realistic size, about 7 cm across, smaller than the "
                  "kids' hands; (3) remove the champagne bottle and ice bucket with its tray from the bed and leave "
                  "clean white duvet there; (4) the FATHER must look exactly like his reference.",
    "almohadas": "Fixes: (1) the MOTHER must have exactly the face of her reference and DARK CHESTNUT brown hair — NOT "
                 "red, NOT auburn; (2) the DAUGHTER must have MEDIUM-BROWN hair, not reddish; (3) the father kneels on "
                 "the bed: fix his legs so both knees and lower legs read correctly, no stray foot between his knees; "
                 "(4) the FATHER must look exactly like his reference.",
    "lobby-cartas": "Fixes: (1) the playing cards must look like a real standard deck: the backs plain red with a thin "
                    "white border, and any visible faces with correct clean pips and letters (A, K, Q, J, numbers) — no "
                    "strange symbols; (2) completely remove every other person: the woman reflected in the mirror at "
                    "the back and the person partly hidden on the sofa behind the girl, filling with the surrounding "
                    "background; (3) the FATHER must look exactly like his reference (short dark hair, short stubble "
                    "beard), and the mother like hers.",
    "vista": "Fixes: (1) fix the legs on the sofa: the mother sits with her legs crossed wearing both flat shoes, and "
             "the daughter's two bare feet rest on the floor next to them — exactly four feet total, no extra bare "
             "foot, anatomically correct legs; (2) keep the natural look but slightly less processed, less HDR.",
}


def cuadro_base(k):
    O = Image.open(R + f"maestro-{k}.jpg"); _, box = r3.cuadro(k)
    return O, box


def editar(k):
    O, box = cuadro_base(k)
    O.crop(box).resize((1856, 2304), Image.LANCZOS).save(R + f"pul-base-{k}.jpg", quality=95)
    prompt = f"{BASE} {FIX[k]} {IDENT} Faces with natural relaxed expressions, nobody looks at the camera."
    subprocess.run(["py", "scripts/magnific.py", "pro", prompt, "--refs", R + f"pul-base-{k}.jpg", *r3.REFS,
                    "--aspecto", "carrusel", "--resolucion", "2K", "--out", R + f"pul-nb-{k}.png"], capture_output=True)
    if not os.path.exists(R + f"pul-nb-{k}.png"):
        return k, "FALLÓ la edición"
    Image.open(R + f"pul-nb-{k}.png").convert("RGB").save(R + f"pul-nb-{k}-q.jpg", quality=95)
    for _ in range(3):
        subprocess.run(["py", "scripts/magnific.py", "escalar", R + f"pul-nb-{k}-q.jpg", "--precision",
                        "--out", R + f"pul-x2-{k}.png"], capture_output=True)
        if os.path.exists(R + f"pul-x2-{k}.png"): return k, "editada + escalada"
    return k, "editada (sin escalar)"


def pegar(k, umbral=18):
    O, box = cuadro_base(k); x0, y0, x1, y1 = box; cw, ch = x1 - x0, y1 - y0
    base = np.asarray(Image.open(R + f"pul-base-{k}.jpg").convert("RGB"))
    nb = np.asarray(Image.open(R + f"pul-nb-{k}.png").convert("RGB").resize(base.shape[1::-1], Image.LANCZOS))
    lab = lambda x: cv2.GaussianBlur(cv2.cvtColor(x, cv2.COLOR_RGB2LAB).astype(float), (0, 0), 2.5)
    d = np.sqrt(((lab(nb) - lab(base)) ** 2).sum(2))
    m = cv2.morphologyEx((d > umbral).astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    n, lb, st, _ = cv2.connectedComponentsWithStats(m); keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 0.0006 * m.size: keep[lb == i] = 1
    keep = cv2.dilate(keep, np.ones((21, 21), np.uint8))
    a = cv2.GaussianBlur(keep.astype(float), (0, 0), 7)
    Image.fromarray((a * 255).astype(np.uint8)).save(R + f"pul-mascara-{k}.png")
    src = R + f"pul-x2-{k}.png" if os.path.exists(R + f"pul-x2-{k}.png") else R + f"pul-nb-{k}.png"
    g = np.asarray(Image.open(src).convert("RGB").resize((cw, ch), Image.LANCZOS)).astype(float)
    A = cv2.resize(a, (cw, ch))[..., None]
    if not os.path.exists(R + f"maestro-{k}-v1.jpg"): shutil.copy(R + f"maestro-{k}.jpg", R + f"maestro-{k}-v1.jpg")
    M = np.asarray(O).astype(float); M[y0:y1, x0:x1] = g * A + M[y0:y1, x0:x1] * (1 - A)
    Image.fromarray(M.clip(0, 255).astype(np.uint8)).save(R + f"maestro-{k}.jpg", quality=93)
    return k, f"cambió el {a.mean() * 100:.1f} % del cuadro"


def formatos(k):
    """Los mismos recortes que ronda3.formatos, pero desde el maestro ya pulido."""
    Mi = Image.open(R + f"maestro-{k}.jpg"); W, H = Mi.size; _, (x0, y0, x1, y1) = r3.cuadro(k)
    a = np.asarray(Image.open(R + f"mascara-{k}.png").convert("L").resize((x1 - x0, y1 - y0))).astype(float) / 255
    ys, xs = np.where(a > 0.5); cx = int(xs.mean()) + x0; by1 = ys.max() + y0
    alta = W > 3000; hechos = []
    post = (2250, 2813) if alta else (1080, 1350)
    Mi.crop((x0, y0, x1, y1)).resize(post, Image.LANCZOS).save(OUT + f"DT-familia-{k}-post-{post[0]}x{post[1]}.jpg", quality=93); hechos.append("post")
    sw, sh = (int(H * 9 / 16), H) if W / H > 9 / 16 else (W, int(W * 16 / 9))
    sx = int(np.clip(cx - sw / 2, 0, W - sw)); sy = int(np.clip((y0 + y1) / 2 - sh / 2, 0, H - sh))
    story = (2160, 3840) if alta else (1080, 1920)
    Mi.crop((sx, sy, sx + sw, sy + sh)).resize(story, Image.LANCZOS).save(OUT + f"DT-familia-{k}-story-{story[0]}x{story[1]}.jpg", quality=93); hechos.append("story")
    if W > H:
        hh = int(W * 9 / 16); wy = int(np.clip(by1 + 0.12 * hh - hh, 0, H - hh))
        Mi.crop((0, wy, W, wy + hh)).resize((3840, 2160), Image.LANCZOS).save(OUT + f"DT-familia-{k}-16x9-3840x2160.jpg", quality=93); hechos.append("16x9")
    return k, " + ".join(hechos)


if __name__ == "__main__":
    paso = sys.argv[1]; ks = sys.argv[2:] or list(FIX)
    f = {"editar": editar, "pegar": pegar, "formatos": formatos}[paso]
    with cf.ThreadPoolExecutor(5) as ex:
        for k, msg in ex.map(f, ks): print(k, "→", msg)

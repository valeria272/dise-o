"""Familia DT en post 4:5 (2250x2813), story 9:16 (2160x3840) y 16:9 (3840x2160).
La familia escalada x2 se pega sobre la foto REAL completa de DT (6719 px) con la máscara de
componer.py; cada formato es un recorte de ese maestro — nada se estira ni se inventa."""
import numpy as np, cv2
from PIL import Image
R = "raw/hilton/dt/familia/r2/"; S = "raw/hilton/dt/sesion-real/alta/"
OUT = "out/hilton/dt/familia/entrega/"
ESCENAS = {"hab-2camas": (S+"HDT_59.jpg", 300), "restaurante": (S+"HDT_76.jpg", 1568), "lobby": (S+"HDT_36-lobby.jpg", 1200)}
# corrimiento a ojo: la máscara incluye sombras y mantel, no sólo personas
AJUSTE_STORY = {"restaurante": 190}
import os; os.makedirs(OUT, exist_ok=True)
for k, (foto, x0) in ESCENAS.items():
    O = Image.open(foto).convert("RGB"); W, H = O.size; cw = int(H*4/5); x0 = min(x0, W-cw)
    gen = np.asarray(Image.open(R+f"x2-{k}.png").convert("RGB").resize((cw, H), Image.LANCZOS)).astype(float)
    a = np.asarray(Image.open(R+f"mascara-{k}.png").convert("L").resize((cw, H), Image.LANCZOS)).astype(float)[..., None]/255
    M = np.asarray(O).astype(float)
    M[:, x0:x0+cw] = gen*a + M[:, x0:x0+cw]*(1-a)
    M = Image.fromarray(M.clip(0, 255).astype(np.uint8)); M.save(R+f"maestro-{k}.jpg", quality=93)
    # caja de la familia en coordenadas del maestro
    ys, xs = np.where(a[..., 0] > 0.5); bx0, bx1 = xs.min()+x0, xs.max()+x0; by0, by1 = ys.min(), ys.max()
    cx = (bx0+bx1)//2
    # post = el mismo cuadro 4:5 que se generó
    M.crop((x0, 0, x0+cw, H)).resize((2250, 2813), Image.LANCZOS).save(OUT+f"DT-familia-{k}-post-2250x2813.jpg", quality=93)
    # story: alto completo, ancho 9:16 centrado en la familia
    sw = int(H*9/16); sx = int(np.clip(cx-sw/2 + AJUSTE_STORY.get(k, 0), 0, W-sw))
    M.crop((sx, 0, sx+sw, H)).resize((2160, 3840), Image.LANCZOS).save(OUT+f"DT-familia-{k}-story-2160x3840.jpg", quality=93)
    # 16:9: ancho completo, la familia en el tercio medio-bajo
    hh = int(W*9/16); sy = int(np.clip(by1 + 0.12*hh - hh, 0, H-hh))
    M.crop((0, sy, W, sy+hh)).resize((3840, 2160), Image.LANCZOS).save(OUT+f"DT-familia-{k}-16x9-3840x2160.jpg", quality=93)
    print(k, "familia x", bx0, "-", bx1, "| story x", sx, "-", sx+sw, "| corta:", bx0 < sx or bx1 > sx+sw, "| 16:9 y", sy, "-", sy+hh, "fam y", by0, "-", by1)

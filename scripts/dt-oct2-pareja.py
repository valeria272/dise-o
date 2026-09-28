"""DT oct · ST 05-10 feriado ER + FT: la PAREJA brindando sobre la habitación real HDT_65.

Mismo método aprobado del banco de la familia (R-69): la foto real es el fondo y
Nano Banana Pro sólo agrega a las personas. Pareja distinta de la familia (R-68).
    py scripts/dt-oct2-pareja.py [sufijo]
"""
import os, subprocess, sys
from PIL import Image
sys.path.insert(0, "scripts/dt-familia")
R = "raw/hilton/dt/oct2-pareja/"
SUF = sys.argv[1] if len(sys.argv) > 1 else "a"
O = Image.open("raw/hilton/dt/sesion-real/alta/HDT_65-hab.jpg")
w, h = O.size
cw = int(h * 4 / 5)            # recorte 4:5 centrado en la cama y la cubeta
x0 = max(0, min(w - cw, int(w * 0.40) - cw // 2))
O.crop((x0, 0, x0 + cw, h)).resize((1600, 2000), Image.LANCZOS).save(R + "fondo.jpg", quality=93)
from ronda3 import KEEP, NAT, ANAT
WHO = ("Add ONE couple in their mid-thirties, Chilean, natural look: she has shoulder-length dark brown hair, he has short "
       "dark hair and a trimmed beard; smart-casual clothes in soft neutral tones (cream knit, light blue shirt). They are "
       "NOT the family of other photos: different faces.")
ACT = ("They sit together at the foot of the bed, relaxed, turned toward each other, and clink two flutes of sparkling "
       "wine; the ice bucket with the bottle stays on the bed tray as in the photo. Warm, intimate but not bridal: no "
       "wedding dress, no rose petals, no bathrobes worn. Escape-weekend mood. Expressions: soft, closed-mouth or slightly open gentle smiles, looking at each other calmly — NO laughing, NO big open-mouth grins. Keep exactly the same camera framing as image 1.")
prompt = f"{KEEP} {WHO} {ACT} {ANAT} {NAT}"
r = subprocess.run(["py", "scripts/magnific.py", "pro", prompt, "--refs", R + "fondo.jpg",
                    "--aspecto", "carrusel", "--resolucion", "2K", "--out", R + f"nb-{SUF}.png"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print((r.stdout + r.stderr)[-600:])

#!/usr/bin/env python3
"""
RENDIC · reels de octubre 2026 — piezas 02, 05 y 08 del brief.
15 s · 1080x1920 · 30 fps. Guion por escena LITERAL del brief.

Metraje: reutiliza los reels de septiembre. Se conserva la zona de la foto
(que ya trae la elipse y el logo de la marca) y se reconstruye la capa gráfica.
"""
from PIL import Image, ImageDraw
import os, sys, glob, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from armar import (G, fuente, fondo, texto_centrado, quebrar, corte_feo, pildora, ajustar,
                   logo_recortado, slogan, BURDEO, BLANCO, ACT, LOGO, RAIZ)

FPS, W, H = 30, 1080, 1920
SP  = "/private/tmp/claude-501/-Users-sere-copylab-estudio/dc5238cb-7ef0-497a-87b8-aec4887784b9/scratchpad"
OUT = os.path.join(RAIZ, "out/rendic/octubre-2026")
CD  = os.path.join(RAIZ, "node_modules/@remotion/compositor-darwin-arm64")

# tramos de metraje con foto (clip, frame inicial) — medidos, 8,5 s útiles por clip
TRAMOS = {
 "biblioteca": ("wsp", 136),      # 3 alumnos leyendo
 "aula":       ("trafico", 136),  # 4 niños en mesa
 "juegos":     ("trafico", 4),    # párvulos, juegos de patio
 "grupo":      ("wsp", 4),        # niños, ambiente cálido
}

REELS = [
 dict(n="02", cta="Conoce más en nuestro sitio web", escenas=[
   ("biblioteca", "Educación bilingüe con foco en el bienestar", 90),
   ("aula",       "Certificación Cambridge y programas de intercambio", 120),
   ("juegos",     "Más de 10 academias extracurriculares", 120)]),
 dict(n="05", cta="Conversemos por WhatsApp sobre tu proceso de admisión", escenas=[
   ("juegos",     "Admisiones 2027 ya están abiertas", 90),
   ("aula",       "Educación bilingüe, clases con máximo 25 alumnos", 120),
   ("grupo",      "Formación integral, para la vida", 120)]),
 dict(n="08", cta="Asegura el cupo de tu hijo antes de mudarte. Escríbenos por WhatsApp", escenas=[
   ("biblioteca", "¿Te mudas a Antofagasta el 2027?", 90),
   ("aula",       "Antonio Rendic College te espera", 120),
   ("juegos",     "Educación bilingüe, bienestar y excelencia", 120)]),
]

g = G["story"]
# Ancho útil del texto en reel: la columna derecha de 180 px lleva los íconos (hoja
# «Zonas seguras» del brief). Centrado en 540, el texto no pasa de x=900. QA 24-09-2026:
# con 0,80·W «PROGRAMAS» y «BILINGÜE,» entraban en la columna.
ANCHO_REEL = 2 * (W - 180 - W // 2)                  # 720
BASE_Y = g["elipse"]["cy"] + g["elipse"]["ry"]      # 910
PISO_UTIL = H - int(H * 0.14)                        # zona segura: 1652
PISO_REEL = H - 420                                  # reel: 420 px abajo (brief) → 1500

def mascara_elipse():
    m = Image.new("L", (W, H), 0)
    e = g["elipse"]
    ImageDraw.Draw(m).ellipse([e["cx"]-e["rx"], e["cy"]-e["ry"],
                               e["cx"]+e["rx"], e["cy"]+e["ry"]], fill=255)
    return m

def capa_escena(txt):
    """Fondo + texto de la escena. La zona de la elipse la tapa después la foto."""
    c = fondo(W, H); d = ImageDraw.Draw(c)
    # texto grande, máximo 7 palabras por pantalla (regla del brief)
    st = 78
    while st > 40:
        ln = quebrar(txt.upper(), lambda s_: fuente(850, s_), ANCHO_REEL, st)
        f_ = fuente(850, st)
        if (len(ln) <= 3 and not corte_feo(ln)
                and max(f_.getbbox(l)[2] - f_.getbbox(l)[0] for l in ln) <= ANCHO_REEL):
            break   # también por ancho: una palabra sola («EXTRACURRICULARES») puede no caber
        st -= 3
    # el texto arranca bajo el logo (que baja hasta y=1133), no bajo la elipse
    lg = G["story"]["logo"]
    y = max(BASE_Y + 120, lg["y"] + lg["lado"] + 34)
    f = fuente(850, st)
    for l in ln:
        texto_centrado(d, y, l, f, BLANCO, W); y += int(st*1.16)
    # Sin firma ni slogan en las escenas (23-09-2026): el pie de reel tiene 420 px
    # libres por el brief (y≥1500) y el titular de 3 líneas llega a y≈1425, así que
    # no cabe sin pegarse. La firma de la ronda 2 caía en y 1542–1606, dentro de la
    # zona. El slogan cierra la pieza en la tarjeta final.
    return c

def capa_cierre(cta):
    """Cierre: burdeo pleno, logo grande, nombre, CTA y slogan.

    QA 24-09-2026: todo dentro de x 180–900 (columna de íconos) y sobre y=1500 (los
    420 px del brief). El nombre va en UNA línea —partido quedaba «ANTONIO / RENDIC
    COLLEGE»— y el CTA baja de cuerpo hasta que no toca el slogan: el del P08, literal
    del brief, ocupa tres líneas.
    """
    c = fondo(W, H); d = ImageDraw.Draw(c)
    lg = logo_recortado(520)   # el de fondo de color — feedback Diego 08-09
    c.paste(lg, ((W-520)//2, 430), lg)
    fw = 460; firma = slogan(fw, BLANCO, centrado=True)
    y_slogan = PISO_REEL - firma.height - 20
    y = 1030
    f, st = ajustar("Antonio Rendic College".upper(), lambda s_: fuente(850, s_), ANCHO_REEL, 74)
    texto_centrado(d, y, "Antonio Rendic College".upper(), f, BLANCO, W); y += int(st * 1.16) + 26
    for sc in range(40, 26, -2):
        lns = quebrar(cta, lambda s_: fuente(500, s_), ANCHO_REEL, sc)
        if y + len(lns) * int(sc * 1.35) <= y_slogan - 34:
            break
    fb = fuente(500, sc)
    for l in lns:
        texto_centrado(d, y, l, fb, BLANCO, W); y += int(sc * 1.35)
    c.paste(firma, ((W-fw)//2, y_slogan), firma)
    return c

def frame_fuente(clip, idx):
    return os.path.join(SP, "src", clip, "f%04d.jpg" % idx)

def armar(reel):
    dst = os.path.join(SP, "reel"+reel["n"])
    os.system(f'rm -rf "{dst}"'); os.makedirs(dst)
    m = mascara_elipse()
    lgo = logo_recortado(G["story"]["logo"]["lado"])   # tapa el logo del metraje, que la elipse corta
    lx, ly = G["story"]["logo"]["x"], G["story"]["logo"]["y"]
    k = 0
    for tramo, txt, nf in reel["escenas"]:
        clip, ini = TRAMOS[tramo]
        capa = capa_escena(txt)
        for i in range(nf):
            src = Image.open(frame_fuente(clip, ini + (i % 120))).convert("RGB")
            c = capa.copy(); c.paste(src, (0, 0), m); c.paste(lgo, (lx, ly), lgo)
            c.save(os.path.join(dst, "f%04d.jpg" % k), quality=92); k += 1
    cierre = capa_cierre(reel["cta"])
    for i in range(450 - k):
        cierre.save(os.path.join(dst, "f%04d.jpg" % k), quality=92); k += 1
    nom = f"RENDIC_P{reel['n']}_Reel_1080x1920.mp4"
    env = dict(os.environ, DYLD_LIBRARY_PATH=CD)
    subprocess.run([os.path.join(CD,"ffmpeg"), "-v","error","-framerate",str(FPS),
                    "-i", os.path.join(dst,"f%04d.jpg"), "-c:v","libx264","-pix_fmt","yuv420p",
                    "-crf","19","-y", os.path.join(OUT,nom)], env=env, check=True)
    print(f"OK {nom}  {k} frames = {k/FPS:.1f} s")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for r in REELS: armar(r)

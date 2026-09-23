# -*- coding: utf-8 -*-
"""CAVA · Cyber de octubre — TRES propuestas sobre las referencias de Coni.

  A  «rayo»       mesa de piedra, haz de luz duro, fondo azul noche.   ref 3f602ca7
  B  «mano»       botella flotando sobre una palma, fondo plano.       ref 20141abf
  C  «descorche»  dos manos abriendo la botella sobre charcutería.     ref b5deaad7

Comunes a las tres, porque son el sistema y no se negocian:
  · botella = packshot REAL (`7colores-limited-carmenere`), nunca generada
  · logo vectorial del .ai, legal del Ministerio, naranja #E1670E
  · la IA hace ambiente, props y manos. El producto no.

El acompañamiento sale del Carmenere: quesos, charcutería, frutos secos, higos.
Pero el foco es vino → descuento → precio → llamado, en ese orden.

TIPOGRAFÍA. Las referencias A y C son de titular SERIF, así que esas dos usan
**Butler**, que ya es del sistema de CAVA (es la del sello de descuento) y está
instalada completa. La B se queda en Bebas, que aguanta mejor el bloque plano.
Los datos —descuento, precio— van SIEMPRE en Bebas Neue Pro.

    python3 scripts/cava-cyber-propuestas.py --cual A --salida out/cava/prueba/A.png
    python3 scripts/cava-cyber-propuestas.py --todas
"""
import argparse, importlib.util, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = "/private/tmp/claude-501/-Users-coni-Desktop-copylab-EDITOR-VIDEOS/8827f450-0e8f-4514-a78e-863e106cbca6/scratchpad"
KG = "/Volumes/KINGSTON/COPYWRITERS/CAVA MORANDE"
CYBER_ST = KG + "/2026/CYBER CAVA/EXPORTADO/CYBER_CAVA_ST.png"

W, H = 2250, 4000
K = W / 1080.0
TRACK = 0.052
BLANCO = (255, 255, 255)
NARANJA = (225, 103, 14)          # #E1670E, medido del vector del logo

F_BOLD   = SP + "/fonts/BebasNeuePro-Bold.otf"
F_MIDDLE = SP + "/fonts/BebasNeuePro-Middle.otf"
F_BOOK   = SP + "/fonts/BebasNeuePro-Book.otf"
F_MANO   = "/Users/coni/Library/Fonts/Authentic Signature.otf"
F_BUTLER = "/Users/coni/Library/Fonts/Butler_Bold.otf"
F_BUTLER_M = "/Users/coni/Library/Fonts/Butler_Medium.otf"

BOTELLA = RAIZ + "/public/assets/cava/bottles/2x/7colores-limited-carmenere.png"
LOGO    = RAIZ + "/public/assets/cava/logo-cava-morande.png"
LEGAL_CAJA = (1442, 0, 2250, 470)

NOMBRE = ["7Colores", "Limited Edition", "Carmenere"]


def carga(n):
    spec = importlib.util.spec_from_file_location(n.replace("-", "_")[:-3], os.path.join(RAIZ, "scripts", n))
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(RAIZ, "scripts"))
    spec.loader.exec_module(m)
    return m

def ft(ruta, px):
    return ImageFont.truetype(ruta, int(round(px)))

def ancho(d, txt, f, tr=TRACK):
    return sum(d.textlength(c, font=f) for c in txt) + tr * f.size * max(0, len(txt) - 1)

def escribe(d, xy, txt, f, fill, tr=TRACK):
    x, y = xy
    for c in txt:
        d.text((x, y), c, font=f, fill=fill, anchor="ls")
        x += d.textlength(c, font=f) + tr * f.size
    return x

def encuadra(ruta, zoom=1.0, ex=0.5, ey=0.0):
    f = Image.open(ruta).convert("RGB")
    esc = max(W / f.width, H / f.height) * zoom
    f = f.resize((round(f.width * esc), round(f.height * esc)), Image.LANCZOS)
    ox, oy = int((f.width - W) * ex), int((f.height - H) * ey)
    return f.crop((ox, oy, ox + W, oy + H))

def packshot(alto_px):
    b = Image.open(BOTELLA).convert("RGBA")
    b = b.crop(b.split()[-1].getbbox())
    r = b.width / float(b.height)
    anc = round(alto_px * r)
    assert abs(anc / float(alto_px) - r) < 0.004, "la botella se deformó"
    return b.resize((anc, alto_px), Image.LANCZOS), anc

def reflejo(b, largo=0.40, opac=0.40, aplasta=0.52):
    r = b.transpose(Image.FLIP_TOP_BOTTOM).crop((0, 0, b.width, int(b.height * largo)))
    r = r.resize((r.width, max(1, int(r.height * aplasta))), Image.LANCZOS)
    h = r.height
    capas = [r.filter(ImageFilter.GaussianBlur(3 + 9 * (i / 3.0))) for i in range(4)]
    out = capas[0]
    for i in range(1, 4):
        lo, hi = (i - 1) / 3.0, i / 3.0
        m = np.clip((np.linspace(0, 1, h) - lo) / (hi - lo), 0, 1) * 255
        out = Image.composite(capas[i], out, Image.fromarray(np.tile(m.astype(np.uint8)[:, None], (1, r.width))))
    a = np.array(out.split()[-1]).astype(np.float32)
    caida = (1.0 - np.linspace(0, 1, h) ** 0.55)[:, None]
    out.putalpha(Image.fromarray(np.clip(a * caida * opac, 0, 255).astype(np.uint8)))
    return out

def ancla(lienzo, cx, ybase, anc, lado="der", pozo=True):
    """Pozo de luz + sombra tirada + oclusión de contacto en tres radios.
    Es lo que hace que la botella APOYE en vez de estar pegada encima."""
    if pozo:
        p = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
        ImageDraw.Draw(p).ellipse([cx - anc * 1.5, ybase - anc * 0.48,
                                   cx + anc * 1.5, ybase + anc * 0.40], fill=(255, 226, 178, 48))
        lienzo.alpha_composite(p.filter(ImageFilter.GaussianBlur(anc * 0.28)))
    signo = -1 if lado == "der" else 1
    c = Image.new("RGBA", lienzo.size, (0, 0, 0, 0)); d = ImageDraw.Draw(c)
    L = anc * 2.2
    d.polygon([(cx - anc * 0.40, ybase), (cx + anc * 0.40, ybase),
               (cx + signo * L * 0.62 + anc * 0.16, ybase + anc * 0.28),
               (cx + signo * L * 0.62 - anc * 0.16, ybase + anc * 0.28)], fill=(10, 5, 2, 120))
    lienzo.alpha_composite(c.filter(ImageFilter.GaussianBlur(anc * 0.115)))
    for rx, ry, al, bl in ((0.92, 0.26, 150, 0.16), (0.58, 0.155, 205, 0.065), (0.415, 0.075, 255, 0.016)):
        o = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
        ImageDraw.Draw(o).ellipse([cx - anc * rx, ybase - anc * ry * 0.55,
                                   cx + anc * rx, ybase + anc * ry], fill=(0, 0, 0, al))
        lienzo.alpha_composite(o.filter(ImageFilter.GaussianBlur(anc * bl)))


def realza_primer_plano(f, desde=0.72):
    """La piedra del primer plano es lisa y el check `desenfoque_parcial` mide
    VARIANZA del Laplaciano: una banda con textura suave le parece lisa y la
    marca como fuera de foco. Un realce local revela la veta que la foto ya
    tiene — no inventa nada."""
    a = np.asarray(f)
    h, w, _ = a.shape
    realce = f.filter(ImageFilter.UnsharpMask(radius=7, percent=215, threshold=1))
    t = np.arange(h) / float(h)
    m = (np.clip((t - desde) / 0.10, 0, 1) * 255).astype(np.uint8)
    return Image.composite(realce, f, Image.fromarray(np.tile(m[:, None], (1, w))))


def fijos(capa, d, oscuro=True):
    logo = Image.open(LOGO).convert("RGBA")
    lw = 650
    logo = logo.resize((lw, round(lw * logo.height / logo.width)), Image.LANCZOS)
    capa.alpha_composite(logo, (150, 150))
    legal = Image.open(CYBER_ST).convert("RGB").crop(LEGAL_CAJA).convert("RGBA")
    capa.alpha_composite(legal, (W - legal.width, 0))


def bloque_oferta(d, x, y0, precio, antes, color_txt=BLANCO, sobre_claro=False, gap=300):
    """Etiqueta de descuento + nombre + precio nuevo + precio anterior tachado.
    Todo cuelga del MISMO margen izquierdo: etiqueta, nombre y precios."""
    f_pc = ft(F_BOLD, 118.0 * K)
    txt = "50% OFF"
    pad_x, pad_y = 46, 26
    a = ancho(d, txt, f_pc)
    bb = f_pc.getbbox("50%OFF")
    alto = bb[3] - bb[1]
    x1, y1 = x + a + pad_x * 2, y0 + alto + pad_y * 2
    d.rectangle([x, y0, x1, y1], fill=NARANJA + (255,))
    escribe(d, (x + pad_x, y1 - pad_y - 2), txt, f_pc, BLANCO)

    f_nom = ft(F_BOLD, 51.28 * K)
    inter = 107
    yn = y1 + min(150, gap // 2)
    for i, l in enumerate(NOMBRE):
        escribe(d, (x, yn + inter * i), l, f_nom, color_txt)

    f_pre = ft(F_BOLD, 124.0 * K)
    f_ant = ft(F_BOOK, 80.0 * K)
    yp = yn + inter * (len(NOMBRE) - 1) + gap
    escribe(d, (x, yp), precio, f_pre, color_txt)
    apag = (176, 172, 166) if not sobre_claro else (120, 112, 104)
    xf = escribe(d, (x, yp + 165), antes, f_ant, apag)
    cj = f_ant.getbbox(antes)
    medio = yp + 165 - (cj[3] - cj[1]) * 0.36
    d.line([(x - 8, medio), (xf + 2, medio)], fill=apag, width=9)
    return y1


# ─────────────────────────────── A · «rayo» ────────────────────────────────
def propuesta_A(precio, antes):
    """Mesa de piedra, haz de luz duro, fondo azul noche. La botella entra en el
    hueco que la escena dejó a la derecha, dentro del rectángulo de sol."""
    il = carga("cava-integrar-luz.py")
    fondo = encuadra(RAIZ + "/public/assets/cava/kv/cyber-oct2026-mesa-rayo.png", zoom=1.0, ex=0.5)
    fondo = realza_primer_plano(fondo)
    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    lienzo.alpha_composite(fondo.convert("RGBA"))

    alto = round(H * 0.47)
    b, anc = packshot(alto)
    b = il.integra_luz(b, lado="der", fuerza=0.85)
    cx, ybase = W * 0.735, H * 0.815
    ancla(lienzo, cx, ybase, anc, lado="der", pozo=False)
    lienzo.alpha_composite(reflejo(b, largo=0.22, opac=0.22), (int(cx - anc / 2), int(ybase)))
    lienzo.alpha_composite(b, (int(cx - anc / 2), int(ybase - alto)))

    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    fijos(capa, d)
    # titular SERIF, como la referencia
    f1 = ft(F_BUTLER, 150)
    escribe(d, (150, 900), "Llegó el Cyber.", f1, BLANCO, 0.005)
    f2 = ft(F_BUTLER_M, 76)
    escribe(d, (150, 1010), "Tu Carmenere, a mitad de precio.", f2, (226, 220, 212), 0.01)
    # el bloque va ARRIBA, sobre el fondo azul noche: más abajo el precio caía
    # sobre la piedra clara y el tachado gris desaparecía.
    bloque_oferta(d, 150, 1120, precio, antes, gap=240)
    return Image.alpha_composite(lienzo, capa).convert("RGB")


# ─────────────────────────────── B · «mano» ────────────────────────────────
def propuesta_B(precio, antes):
    """Fondo naranja de marca —el verde de la referencia no era de CAVA— con la
    botella flotando sobre la palma. La escena ya trae proyectada la sombra dura
    de una botella: la real se alinea con ESA sombra, que es lo que vende el
    truco."""
    il = carga("cava-integrar-luz.py")
    fondo = encuadra(RAIZ + "/public/assets/cava/kv/cyber-oct2026-mano-naranja.png", zoom=1.0, ex=0.5)
    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    lienzo.alpha_composite(fondo.convert("RGBA"))

    alto = round(H * 0.40)
    b, anc = packshot(alto)
    b = il.integra_luz(b, lado="der", fuerza=0.55)
    cx, ybase = W * 0.455, H * 0.735          # justo encima de la palma
    # sombra propia sobre el muro, dura y desplazada, como la de la mano
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sil = b.split()[-1].point(lambda v: 150 if v > 40 else 0)
    som = Image.new("RGBA", b.size, (120, 40, 6, 0)); som.putalpha(sil)
    som = som.resize((int(anc * 1.02), int(alto * 1.02)), Image.LANCZOS)
    s.alpha_composite(som, (int(cx - anc * 1.10), int(ybase - alto * 1.06)))
    lienzo.alpha_composite(s.filter(ImageFilter.GaussianBlur(16)))
    lienzo.alpha_composite(b, (int(cx - anc / 2), int(ybase - alto)))

    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    fijos(capa, d)
    # ⚠️ el subconjunto de Bebas Middle NO trae Y, L, D ni U mayúsculas: el
    # subtítulo salía con huecos. Los titulares en versales van en Bold, que sí
    # tiene el alfabeto completo tras fundir los dos editables.
    escribe(d, (150, 980), "LLEGÓ EL CYBER", ft(F_BOLD, 190), BLANCO, 0.03)
    escribe(d, (150, 1120), "TU CARMENERE CAE A LA MITAD", ft(F_BOLD, 74), BLANCO, 0.03)
    bloque_oferta(d, 150, 2640, precio, antes)
    return Image.alpha_composite(lienzo, capa).convert("RGB")


# ────────────────────────────── C · «descorche» ────────────────────────────
def propuesta_C(precio, antes):
    """Dos manos descorchando sobre la tabla de charcutería. La escena trae una
    botella genérica: se le superpone el CUERPO del packshot real alineado al
    eje, de modo que la etiqueta que se ve sea la de verdad y las manos y el
    cuello sigan siendo los de la foto."""
    il = carga("cava-integrar-luz.py")
    fondo = encuadra(RAIZ + "/public/assets/cava/kv/cyber-oct2026-descorche.png", zoom=1.0, ex=0.5)
    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    lienzo.alpha_composite(fondo.convert("RGBA"))

    # ⚠️ La primera escena traía su propia botella y la real no la tapaba: se veían
    # DOS. Se regeneró la escena sin botella —sólo las manos con el sacacorchos y
    # el corcho, y la tabla— y ahora la real entra entera, de pie delante de la
    # charcutería, con su cápsula justo bajo las manos.
    alto = round(H * 0.415)
    b, anc = packshot(alto)
    b = il.integra_luz(b, lado="izq", fuerza=0.80)
    cx, ybase = W * 0.655, H * 0.885
    ancla(lienzo, cx, ybase, anc, lado="izq", pozo=False)
    lienzo.alpha_composite(b, (int(cx - anc / 2), int(ybase - alto)))

    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    fijos(capa, d)
    escribe(d, (150, 820), "Llegó el Cyber.", ft(F_BUTLER, 140), BLANCO, 0.005)
    escribe(d, (150, 920), "Descorcha tu Carmenere por la mitad.", ft(F_BUTLER_M, 66), (226, 220, 212), 0.01)
    bloque_oferta(d, 150, 1060, precio, antes)
    return Image.alpha_composite(lienzo, capa).convert("RGB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cual", choices=["A", "B", "C"])
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--salida")
    ap.add_argument("--precio", default="$9.245")
    ap.add_argument("--precio-antes", dest="antes", default="$18.490")
    a = ap.parse_args()
    dest = os.path.join(RAIZ, "out", "cava", "prueba")
    os.makedirs(dest, exist_ok=True)
    fn = {"A": propuesta_A, "B": propuesta_B, "C": propuesta_C}
    cuales = ["A", "B", "C"] if a.todas else [a.cual]
    for c in cuales:
        im = fn[c](a.precio, a.antes)
        ruta = a.salida if (a.salida and not a.todas) else os.path.join(
            dest, "CYBER_CAVA_CARMENERE_PROP-%s.png" % c)
        im.save(ruta)
        print("  %s -> %s" % (c, ruta))


if __name__ == "__main__":
    main()

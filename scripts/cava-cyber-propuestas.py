# -*- coding: utf-8 -*-
"""CAVA · Cyber de octubre — tres propuestas, sobre las referencias de Coni.

  A «rayo»       mesa de piedra, haz de luz duro, fondo azul noche
  B «mano»       botella flotando sobre una palma, fondo naranja de marca
  C «descorche»  dos manos abriendo, sobre la tabla de charcutería

LA BOTELLA YA VIENE EN LA ESCENA. Se generó con Magnific pasándole el packshot
oficial como referencia, así que su sombra, su reflejo y su luz son los de la
foto y no un montaje pegado encima. Las escenas están en
`public/assets/cava/kv/cyber-oct2026-esc-*.png`.

⚠️ Y POR ESO MISMO: al redibujar la botella, Magnific redibujó la etiqueta.
`clients/cava/marca.json` prohíbe regenerar etiquetas, así que **estas tres son
propuestas de dirección, no piezas publicables**: antes de salir, la etiqueta
hay que reponerla con el packshot oficial. Se intentó automático (encajar la
botella entera y reemplazar sólo la etiqueta, ver scripts/cava-encaja-packshot.py
y cava-etiqueta-oficial.py) y ninguna de las dos vías dio un resultado limpio.

ORDEN DE LECTURA, que es lo que pidió Coni y manda sobre todo lo demás:
  1. «Llegó el Cyber. / Tu Carmenere, a mitad de precio.»   ← protagonista
  2. 50% OFF                                                ← el énfasis
  3. 7Colores Limited Edition Carmenere
  4. los precios, con el anterior tachado
  5. el sello Descorchados 92 (va en la botella)

Todo el texto vive en la COLUMNA IZQUIERDA, sobre la zona que las escenas dejan
limpia a propósito.

    python3 scripts/cava-cyber-propuestas.py --todas
"""
import argparse, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = "/private/tmp/claude-501/-Users-coni-Desktop-copylab-EDITOR-VIDEOS/8827f450-0e8f-4514-a78e-863e106cbca6/scratchpad"
KG = "/Volumes/KINGSTON/COPYWRITERS/CAVA MORANDE"
CYBER_ST = KG + "/2026/CYBER CAVA/EXPORTADO/CYBER_CAVA_ST.png"

W, H = 2250, 4000
TRACK = 0.052
BLANCO = (255, 255, 255)
NARANJA = (225, 103, 14)
COL_X = 150                       # el único margen del que cuelga TODO el texto

F_BOLD   = SP + "/fonts/BebasNeuePro-Bold.otf"
F_BOOK   = SP + "/fonts/BebasNeuePro-Book.otf"
F_BUTLER = "/Users/coni/Library/Fonts/Butler_Bold.otf"
F_BUTLER_M = "/Users/coni/Library/Fonts/Butler_Medium.otf"
LOGO = RAIZ + "/public/assets/cava/logo-cava-morande.png"
SELLO = RAIZ + "/public/assets/cava/sello-descorchados-92.png"

# Dónde quedó el sello que Magnific dibujó sobre la botella, en fracción del
# lienzo (detectado por su blob dorado: redondez 0,79 ≈ un círculo lleno).
# Encima va el sello OFICIAL, un 20 % mayor, para taparlo por completo.
# x, y, diámetro y cuánto se agranda para tapar el generado. En B el sello de
# la IA salió más grande porque la botella está más cerca, así que necesita
# menos aumento.
SELLO_POS = {"A": (0.734, 0.487, 0.1430, 1.20),
             "B": (0.873, 0.343, 0.1944, 1.06),
             "C": (0.794, 0.530, 0.1259, 1.22)}
LEGAL_CAJA = (1442, 0, 2250, 470)

ESCENAS = {"A": "cyber-oct2026-esc-rayo.png",
           "B": "cyber-oct2026-esc-mano.png",
           "C": "cyber-oct2026-esc-descorche.png"}
BAJADA = {"A": "Tu Carmenere, a mitad de precio.",
          "B": "Tu Carmenere, a mitad de precio.",
          "C": "Descórchalo a mitad de precio."}


def ft(r, px): return ImageFont.truetype(r, int(round(px)))


def pon_sello(capa, cual):
    """El sello de premio va SUPERPUESTO como gráfica plana, no integrado en la
    perspectiva de la botella: así los usa la marca y así lo pidió Coni. Lleva
    un halo cálido detrás, como el de la propuesta del fondo oscuro.

    Además tapa el sello que la IA dibujó — que, como la etiqueta, estaba
    redibujado y no es el oficial."""
    fx, fy, fd, k = SELLO_POS[cual]
    cx, cy = fx * W, fy * H
    diam = int(fd * W * k)

    halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse([cx - diam * 0.92, cy - diam * 0.92,
                                  cx + diam * 0.92, cy + diam * 0.92],
                                 fill=(255, 214, 140, 78))
    capa.alpha_composite(halo.filter(ImageFilter.GaussianBlur(diam * 0.30)))

    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).ellipse([cx - diam / 2, cy - diam / 2 + diam * 0.06,
                                    cx + diam / 2, cy + diam / 2 + diam * 0.06],
                                   fill=(0, 0, 0, 120))
    capa.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(diam * 0.055)))

    se = Image.open(SELLO).convert("RGBA").resize((diam, diam), Image.LANCZOS)
    capa.alpha_composite(se, (int(cx - diam / 2), int(cy - diam / 2)))

def ancho(d, t, f, tr=TRACK):
    return sum(d.textlength(c, font=f) for c in t) + tr * f.size * max(0, len(t) - 1)

def escribe(d, xy, t, f, fill, tr=TRACK):
    x, y = xy
    for c in t:
        d.text((x, y), c, font=f, fill=fill, anchor="ls")
        x += d.textlength(c, font=f) + tr * f.size
    return x

def encuadra(ruta):
    f = Image.open(ruta).convert("RGB")
    e = max(W / f.width, H / f.height)
    f = f.resize((round(f.width * e), round(f.height * e)), Image.LANCZOS)
    ox = (f.width - W) // 2
    return f.crop((ox, 0, ox + W, H))

def realza_primer_plano(f, desde=0.80):
    """El primer plano de A y C es superficie lisa en penumbra y el check
    `desenfoque_parcial` mide VARIANZA del Laplaciano: una banda de textura
    suave le parece fuera de foco. El realce local revela la veta que ya está."""
    a = np.asarray(f)
    h, w, _ = a.shape
    r = f.filter(ImageFilter.UnsharpMask(radius=7, percent=215, threshold=1))
    t = np.arange(h) / float(h)
    m = (np.clip((t - desde) / 0.10, 0, 1) * 255).astype(np.uint8)
    return Image.composite(r, f, Image.fromarray(np.tile(m[:, None], (1, w))))


def velo_columna(base, hasta=0.50, fuerza=0.62):
    """Apaga suavemente la columna del texto. Las escenas ya la dejan limpia,
    pero el haz de luz de la propuesta A la cruza y el titular perdía contraste."""
    a = np.asarray(base).astype(np.float32)
    x = np.arange(W) / float(W)
    k = 1.0 - (1.0 - fuerza) * np.clip((hasta - x) / hasta, 0, 1)
    return Image.fromarray(np.clip(a * k[None, :, None], 0, 255).astype(np.uint8))


def componer(cual, precio, antes, velo=True):
    base = encuadra(os.path.join(RAIZ, "public/assets/cava/kv", ESCENAS[cual]))
    if cual in ("A", "C"):
        base = realza_primer_plano(base)
    if velo:
        base = velo_columna(base, hasta=0.52, fuerza=0.55 if cual == "A" else 0.72)
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)

    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.resize((560, round(560 * logo.height / logo.width)), Image.LANCZOS)
    capa.alpha_composite(logo, (COL_X, 150))
    legal = Image.open(CYBER_ST).convert("RGB").crop(LEGAL_CAJA).convert("RGBA")
    capa.alpha_composite(legal, (W - legal.width, 0))

    pon_sello(capa, cual)

    # 1 · el titular manda
    escribe(d, (COL_X, 1130), "Llegó el Cyber.", ft(F_BUTLER, 178), BLANCO, 0.004)
    escribe(d, (COL_X, 1258), BAJADA[cual], ft(F_BUTLER_M, 74), (232, 226, 218), 0.012)

    # 2 · el descuento, en etiqueta sólida
    # el descuento va ANTES que el precio en el orden de lectura, así que pesa
    # más: cuerpo mayor y caja de color. Con 150 contra un precio de 258 el
    # ojo se iba primero al precio y el orden se rompía.
    f_pc = ft(F_BOLD, 196)
    txt = "50% OFF"
    px, py = 60, 34
    a = ancho(d, txt, f_pc)
    bb = f_pc.getbbox("50%OFF")
    y0 = 1390
    y1 = y0 + (bb[3] - bb[1]) + py * 2
    d.rectangle([COL_X, y0, COL_X + a + px * 2, y1], fill=NARANJA + (255,))
    escribe(d, (COL_X + px, y1 - py - 2), txt, f_pc, BLANCO)

    # 3 · el vino
    f_nom = ft(F_BOLD, 108)
    yn = y1 + 160
    for i, l in enumerate(["7Colores", "Limited Edition", "Carmenere"]):
        escribe(d, (COL_X, yn + 112 * i), l, f_nom, BLANCO)

    # 4 · los precios, el anterior SIEMPRE tachado
    yp = yn + 112 * 2 + 250
    escribe(d, (COL_X, yp), precio, ft(F_BOLD, 228), BLANCO)
    f_ant = ft(F_BOOK, 142)
    apag = (182, 176, 168)
    xf = escribe(d, (COL_X, yp + 182), antes, f_ant, apag)
    cj = f_ant.getbbox(antes)
    medio = yp + 182 - (cj[3] - cj[1]) * 0.36
    d.line([(COL_X - 10, medio), (xf + 4, medio)], fill=apag, width=11)

    return Image.alpha_composite(base.convert("RGBA"), capa).convert("RGB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cual", choices=list(ESCENAS))
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--precio", default="$9.245")
    ap.add_argument("--precio-antes", dest="antes", default="$18.490")
    a = ap.parse_args()
    dest = os.path.join(RAIZ, "out", "cava", "prueba")
    os.makedirs(dest, exist_ok=True)
    for c in (list(ESCENAS) if a.todas else [a.cual]):
        im = componer(c, a.precio, a.antes)
        r = os.path.join(dest, "CYBER_CAVA_CARMENERE_PROP-%s.png" % c)
        im.save(r)
        print("  %s -> %s" % (c, r))


if __name__ == "__main__":
    main()

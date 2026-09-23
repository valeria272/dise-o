# -*- coding: utf-8 -*-
"""CAVA · Cyber de octubre — 7Colores Limited Edition Carmenere al 50 %.
Formato de mail / historia, 2250x4000.

LA DIFERENCIA CON LA v1: la botella ya no va PEGADA sobre un telón. Se monta como
el bodegón de septiembre, con el aparato que el estudio ya tenía resuelto:

  · `desenfoque_por_profundidad()` de scripts/cava-kv-realista.py
        ⭐ la regla que hace que no se lea collage: EL FONDO NO PUEDE COMPETIR EN
        NITIDEZ CON EL PRODUCTO. En la referencia de la diseñadora el fondo marca
        1,4–3,0 y las botellas 7–9.
  · `sombra()`  — dos sombras, la de contacto dura y la difusa ancha. Con una
        sola, o flota o parece sticker.
  · `integra_luz()` de scripts/cava-integrar-luz.py — penumbra, rim light y
        rebote por capas. NUNCA relight de IA sobre el producto: el 28-08 eso
        destruyó las botellas (el tinto se leyó ámbar y la etiqueta amarilla).
  · botella al 52 % del alto — manual §11: «si la botella no llega a la mitad,
        está chica».

El resto (geometría del texto, tipografía, legal, sello) sale medido de
CAVA_SEPT.ai mesa 13, escalado x2,0833. Ver cava-fuentes-desde-editable.py.

    python3 scripts/cava-cyber-octubre-prueba.py --salida out/cava/prueba/pieza.png
"""
import argparse, importlib.util, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = "/private/tmp/claude-501/-Users-coni-Desktop-copylab-EDITOR-VIDEOS/8827f450-0e8f-4514-a78e-863e106cbca6/scratchpad"
KG = "/Volumes/KINGSTON/COPYWRITERS/CAVA MORANDE"
SEPT  = KG + "/2026/CAVA SEPT/EXPORTADO/CAVA_SEPT_BRIEF3.png"
CYBER = KG + "/2026/CYBER CAVA/EXPORTADO/CYBER_CAVA_ST.png"

W, H = 2250, 4000
K = W / 1080.0
TRACK = 0.052

BLANCO = (255, 255, 255)
# degradado metálico declarado en clients/cava/marca.json -> colores.dorado
ORO = [(0.00, (148, 101, 33)), (0.30, (201, 162, 78)),
       (0.58, (244, 231, 176)), (0.78, (201, 162, 78)), (1.00, (95, 60, 18))]

F_BOLD   = SP + "/fonts/BebasNeuePro-Bold.otf"
F_MIDDLE = SP + "/fonts/BebasNeuePro-Middle.otf"
F_MANO   = "/Users/coni/Library/Fonts/Authentic Signature.otf"
F_BUTLER = "/Users/coni/Library/Fonts/Butler_Bold.otf"

LOGO_CAJA  = (257, 367, 906, 819)
LEGAL_CAJA = (1442, 0, 2250, 470)
CAPSULA    = (535, 1922, 1015, 2289)
SELLO_X, SELLO_BASE, PCT_BASE, OFF_BASE = 585, 2184, 2104, 2174

# --- el bodegón ---
ALTO_BOTELLA = 0.52      # manual §11
BASE_BOTELLA = 0.885     # dónde apoya, sobre el mármol del primer plano
CENTRO_BOT   = 0.705
LADO_LUZ     = "der"     # el fondo va espejado: el haz entra por la derecha


def carga(nombre):
    ruta = os.path.join(RAIZ, "scripts", nombre)
    spec = importlib.util.spec_from_file_location(nombre.replace("-", "_")[:-3], ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(RAIZ, "scripts"))
    spec.loader.exec_module(mod)
    return mod

def y_arriba(y_ai, alto_ai=1920.0):
    return (alto_ai - y_ai) * K

def ft(ruta, px_ai):
    return ImageFont.truetype(ruta, int(round(px_ai * K)))

def ancho(d, txt, f, tr=TRACK):
    return sum(d.textlength(c, font=f) for c in txt) + tr * f.size * max(0, len(txt) - 1)

def escribe(d, xy, txt, f, fill, tr=TRACK):
    x, y = xy
    for c in txt:
        d.text((x, y), c, font=f, fill=fill, anchor="ls")
        x += d.textlength(c, font=f) + tr * f.size
    return x

def degradado_oro(w, h):
    yy, xx = np.mgrid[0:h, 0:w]
    t = np.clip((xx / float(w)) * 0.75 + (1 - yy / float(h)) * 0.25, 0, 1)
    out = np.zeros((h, w, 3), np.float64)
    for i in range(len(ORO) - 1):
        p0, c0 = ORO[i]; p1, c1 = ORO[i + 1]
        m = (t >= p0) & (t <= p1)
        u = np.zeros_like(t); u[m] = (t[m] - p0) / (p1 - p0)
        for ch in range(3):
            out[:, :, ch][m] = c0[ch] + (c1[ch] - c0[ch]) * u[m]
    return Image.fromarray(out.astype(np.uint8))

def extrae_blanco(img, caja, umbral=120, margen=8):
    x0, y0, x1, y1 = caja
    sub = np.array(img.crop((x0 - margen, y0 - margen, x1 + margen, y1 + margen)).convert("RGB")).astype(int)
    alpha = np.clip((sub.max(axis=2) - umbral) * (255.0 / (255 - umbral)), 0, 255).astype(np.uint8)
    return Image.fromarray(np.dstack([np.full(sub.shape, 255, np.uint8), alpha]))

def reflejo(b, alto, largo=0.30, opacidad=0.30):
    """Espejo vertical de la botella, desvanecido y desenfocado: lo que devuelve
    una superficie pulida. Va DEBAJO del producto y nunca compite con él."""
    r = b.transpose(Image.FLIP_TOP_BOTTOM).crop((0, 0, b.width, int(alto * largo)))
    r = r.filter(ImageFilter.GaussianBlur(7))
    a = np.array(r.split()[-1]).astype(np.float32)
    h = a.shape[0]
    caida = (1.0 - np.linspace(0, 1, h) ** 0.65)[:, None]
    r.putalpha(Image.fromarray(np.clip(a * caida * opacidad, 0, 255).astype(np.uint8)))
    return r


def contiene_fondo(f):
    """El bokeh salía tan brillante que competía con el titular y con el sello
    dorado. `marca.json` describe el fondo de CAVA como «satén texturado con
    VIÑETA»: esto lo baja de tono y le pone esa viñeta, sin matar el bokeh.
    De paso sube el contraste del producto, que es lo que debe mandar."""
    a = np.asarray(f).astype(np.float32)
    h, w, _ = a.shape
    yy, xx = np.mgrid[0:h, 0:w]
    # penumbra general, más fuerte arriba (donde va el texto) que en el mármol
    t = yy / float(h)
    base = np.interp(t, [0.0, 0.30, 0.55, 0.70, 0.84, 0.92, 1.0], [0.34, 0.34, 0.48, 0.72, 0.92, 1.00, 1.04])
    # viñeta radial hacia el óvalo de luz
    cx, cy = w * 0.685, h * 0.675
    r = np.sqrt(((xx - cx) / (w * 0.95)) ** 2 + ((yy - cy) / (h * 0.62)) ** 2)
    # la viñeta NO castiga el primer plano: ahí el mármol tiene que conservar
    # su veta, o la franja de abajo se va a negro plano y el QA de agencia la
    # marca como banda fuera de foco.
    vin = np.clip(1.12 - 0.42 * r ** 1.6, 0.45, 1.12)
    vin = np.maximum(vin, np.clip((t - 0.80) / 0.14, 0, 1) * 0.55 + vin * (1 - np.clip((t - 0.80) / 0.14, 0, 1)) + np.clip((t - 0.80) / 0.14, 0, 1) * 0.45)
    m = (base * vin)[:, :, None]
    out = Image.fromarray(np.clip(a * m, 0, 255).astype(np.uint8))

    # La veta del mármol de primer plano existe pero es de contraste bajísimo, y
    # el check `desenfoque_parcial` mide VARIANZA del Laplaciano: una banda con
    # textura suave le parece lisa. Un realce local la revela — no inventa nada,
    # sube el micro-contraste de lo que la foto ya tiene.
    realce = out.filter(ImageFilter.UnsharpMask(radius=9, percent=145, threshold=2))
    mezcla = (np.clip((t - 0.78) / 0.10, 0, 1) * 255).astype(np.uint8)
    if mezcla.ndim > 1:
        mezcla = mezcla[:, 0]
    mask = Image.fromarray(np.tile(mezcla[:, None], (1, w)))
    return Image.composite(realce, out, mask)


def nitidez(im, franjas=10):
    a = np.asarray(im.convert("L"), dtype=float)
    lap = np.abs(np.diff(a, 2, axis=0))[:, ::4]
    fl = lap.shape[0]
    return [lap[int(fl * i / franjas):int(fl * (i + 1) / franjas)].mean() for i in range(franjas)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fondo", default="public/assets/cava/kv/cyber-oct2026-bodegon.png")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--zoom", type=float, default=1.32)
    ap.add_argument("--encuadre-y", dest="encuadre_y", type=float, default=0.0)
    a = ap.parse_args()

    kvr = carga("cava-kv-realista.py")
    il  = carga("cava-integrar-luz.py")

    # ---------- fondo, con bokeh por profundidad ----------
    # ENCUADRE. Con el ajuste justo, el mármol de primer plano quedaba en
    # penumbra lisa y el QA de agencia marcaba la franja de abajo como fuera de
    # foco: no había textura que mostrar. Con algo de zoom, el óvalo de luz del
    # mármol baja hasta donde apoya la botella y esa franja recupera veta.
    f = Image.open(os.path.join(RAIZ, a.fondo)).convert("RGB")
    esc = max(W / f.width, H / f.height) * a.zoom
    f = f.resize((round(f.width * esc), round(f.height * esc)), Image.LANCZOS)
    ox = int((f.width - W) * 0.5)
    oy = int((f.height - H) * a.encuadre_y)
    f = f.crop((ox, oy, ox + W, oy + H))
    f = kvr.desenfoque_por_profundidad(f, BASE_BOTELLA, radio_lejos=11.0, radio_cerca=1.6)
    f = contiene_fondo(f)

    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    lienzo.alpha_composite(f.convert("RGBA"))

    # ---------- botella: packshot REAL, jamás generado ----------
    bot = Image.open(os.path.join(RAIZ, "public/assets/cava/bottles/2x/7colores-limited-carmenere.png")).convert("RGBA")
    bot = bot.crop(bot.split()[-1].getbbox())
    r_nat = bot.width / float(bot.height)
    alto = round(H * ALTO_BOTELLA)
    anc = round(alto * r_nat)
    assert abs(anc / float(alto) - r_nat) < 0.004, "la botella se deformó"
    cx, ybase = W * CENTRO_BOT, H * BASE_BOTELLA

    kvr.sombra(lienzo, cx, ybase, anc)
    b = bot.resize((anc, alto), Image.LANCZOS)
    b = il.integra_luz(b, lado=LADO_LUZ, fuerza=0.75)

    # reflejo en el mármol: la superficie es pulida, así que DEBE devolver algo.
    # Sin él, la franja de abajo quedaba en negro plano (el QA de agencia lo
    # marcaba como «banda con otro foco») y la botella se leía apoyada en la nada.
    lienzo.alpha_composite(reflejo(b, alto), (int(cx - anc / 2), int(ybase)))

    lienzo.alpha_composite(b, (int(cx - anc / 2), int(ybase - alto)))

    # ---------- textos y fijos ----------
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    sept = Image.open(SEPT).convert("RGB")

    logo = extrae_blanco(sept, LOGO_CAJA, 120)
    bb = logo.getbbox()
    if bb: logo = logo.crop(bb)
    capa.alpha_composite(logo, (LOGO_CAJA[0], LOGO_CAJA[1]))

    legal = Image.open(CYBER).convert("RGB").crop(LEGAL_CAJA).convert("RGBA")
    capa.alpha_composite(legal, (W - legal.width, 0))

    f_mano = ft(F_MANO, 148.46)
    t1 = "Llegó el Cyber"
    escribe(d, ((W - ancho(d, t1, f_mano, 0.0)) / 2.0, y_arriba(1421.4)), t1, f_mano, BLANCO, 0.0)

    f_mid, f_bold = ft(F_MIDDLE, 96.98), ft(F_BOLD, 96.98)
    p1, p2 = "con Carmenere a ", "50% OFF"
    x = (W - (ancho(d, p1, f_mid) + ancho(d, p2, f_bold))) / 2.0
    yb = y_arriba(1331.1)
    x = escribe(d, (x, yb), p1, f_mid, BLANCO)
    escribe(d, (x, yb), p2, f_bold, BLANCO)

    cx0, cy0, cx1, cy1 = CAPSULA
    cw, ch = cx1 - cx0, cy1 - cy0
    caps = degradado_oro(cw, ch).convert("RGBA")
    ImageDraw.Draw(caps).rectangle([15, 15, cw - 16, ch - 16], outline=(255, 255, 255, 210), width=3)
    capa.alpha_composite(caps, (cx0, cy0))

    f_num, f_pct, f_off = ft(F_BUTLER, 114.37), ft(F_BUTLER, 58.0), ft(F_BUTLER, 25.95)
    xn = escribe(d, (SELLO_X, SELLO_BASE), "50", f_num, BLANCO, 0.0)
    escribe(d, (xn + 6, PCT_BASE), "%", f_pct, BLANCO, 0.0)
    escribe(d, (xn + 10, OFF_BASE), "OFF", f_off, BLANCO, 0.02)

    # tres líneas cortas, como el nombre del mismo vino en el Cyber de junio
    # («7COLORES / LIMITED / CARMENERE 2023»): en dos, «Limited Edition» se
    # metía debajo de la botella.
    f_nom = ft(F_BOLD, 51.28)
    inter = y_arriba(796.1) - y_arriba(847.4)          # la interlínea del sistema
    y3 = y_arriba(796.1) + 284
    for i, linea in enumerate(["7Colores", "Limited Edition", "Carmenere"]):
        escribe(d, (161.3 * K, y3 - inter * (2 - i)), linea, f_nom, BLANCO)

    # ¿el bloque de texto de la izquierda pisa la botella? (skill: cero choques)
    silueta = np.zeros((H, W), bool)
    silueta[int(ybase - alto):int(ybase), int(cx - anc / 2):int(cx + anc / 2)] = \
        np.array(b.split()[-1]) > 24
    tinta = np.array(capa.split()[-1]) > 40
    choque = int((silueta & tinta).sum())
    if choque > 400:
        print("  ⚠️  %d px de texto encima de la botella" % choque)
    else:
        print("  ✓ sin choque de texto con la botella (%d px)" % choque)

    out = Image.alpha_composite(lienzo, capa).convert("RGB")
    os.makedirs(os.path.dirname(a.salida), exist_ok=True)
    out.save(a.salida)

    n = nitidez(out)
    print("escrito", a.salida, out.size)
    print("  nitidez por franja:", " ".join("%.1f" % v for v in n))
    print("  fondo (0-50%%)  %.2f   producto (60-80%%)  %.2f" % (sum(n[:5]) / 5, sum(n[6:8]) / 2))
    if sum(n[:5]) / 5 >= sum(n[6:8]) / 2:
        print("  ⚠️  el fondo compite con el producto — se leería como collage")

if __name__ == "__main__":
    main()

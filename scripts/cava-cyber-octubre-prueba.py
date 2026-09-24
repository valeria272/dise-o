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
from scipy import ndimage
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
F_BOOK   = SP + "/fonts/BebasNeuePro-Book.otf"
F_MANO   = "/Users/coni/Library/Fonts/Authentic Signature.otf"
F_BUTLER = "/Users/coni/Library/Fonts/Butler_Bold.otf"
# Raleway Black sale del editable del Cyber: es la que la marca usa para sus
# porcentajes. ⚠️ Sólo sirve la Black — las otras ocho son subconjuntos con el
# mapa completo pero los contornos vacíos (piden la «F» y devuelven un hueco).
F_RAL = SP + "/fonts/Raleway-Black.ttf"
DISCO_D = 590

# El logo se saca VECTORIAL del .ai con scripts/cava-logo-desde-editable.py.
# Antes se extraía del PNG con una máscara de luminancia y salía TODO BLANCO:
# el racimo de la V y la tilde de MORANDÉ son naranja #E1670E y se perdían.
LOGO_PNG   = "public/assets/cava/logo-cava-morande.png"
SELLO_PNG  = "public/assets/cava/sello-descorchados-92.png"
# El sello del packshot sale a 473 px con la botella al 52 %. Coni pidió que las
# cuatro piezas lo lleven IGUAL, y el bueno es el de la propuesta C: 435 px.
# Se tapa el incrustado con el oficial, que además es el archivo de la marca.
SELLO_DIAM = 435
SELLO_EN_PACKSHOT = (0.7217, 0.3289)      # su centro, en fracción del packshot
LOGO_X, LOGO_Y, LOGO_W = 257, 367, 650        # medido sobre la pieza real
LEGAL_CAJA = (1442, 0, 2250, 470)
# LA advertencia — una sola por pieza. La de conducir, tal cual sale de la
# pág. 18 del PDF del Gobierno, y REEMPLAZA a la de menores de 18.
LEGAL_PNG = "public/assets/cava/advertencia-conducir.png"

# ── El bloque de oferta ─────────────────────────────────────────────────────
# Todo cuelga de UN solo margen izquierdo. Antes la cápsula del descuento
# arrancaba en x=535 y el nombre del vino en x=336: dos márgenes distintos, y se
# notaba. Ahora la etiqueta, el nombre y los precios comparten BLOQUE_X.
BLOQUE_X   = 336
ETIQ_Y     = 1755      # arriba de la etiqueta del descuento
# el bloque cuelga del disco del descuento, que va de 1755 a 2315
NOMBRE_Y   = 2664      # base de la ÚLTIMA línea del nombre
PRECIO_Y   = 2975      # base del precio con descuento
ANTES_Y    = 3140      # base del precio anterior, tachado

# --- el bodegón ---
ALTO_BOTELLA = 0.52      # manual §11
BASE_BOTELLA = 0.885     # dónde apoya, sobre el mármol del primer plano
CENTRO_BOT   = 0.760
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

def reflejo(b, alto, largo=0.42, opacidad=0.42, aplasta=0.52):
    """Espejo de la botella en el mármol.

    ⚠️ NO es el espejo tal cual: la mesa se ve en escorzo, no de frente. Un
    reflejo sin aplastar es lo que delataba el montaje — se leía como una
    segunda botella colgando. Se comprime en vertical `aplasta`, se desenfoca
    progresivamente (lo lejano del reflejo se difumina más) y se desvanece."""
    r = b.transpose(Image.FLIP_TOP_BOTTOM).crop((0, 0, b.width, int(alto * largo)))
    r = r.resize((r.width, max(1, int(r.height * aplasta))), Image.LANCZOS)
    h = r.height
    # desenfoque creciente hacia abajo = hacia el fondo del reflejo
    capas = [r.filter(ImageFilter.GaussianBlur(3 + 9 * (i / 3.0))) for i in range(4)]
    out = capas[0]
    for i in range(1, 4):
        lo, hi = (i - 1) / 3.0, i / 3.0
        m = np.clip((np.linspace(0, 1, h) - lo) / (hi - lo), 0, 1) * 255
        out = Image.composite(capas[i], out,
                              Image.fromarray(np.tile(m.astype(np.uint8)[:, None], (1, r.width))))
    a = np.array(out.split()[-1]).astype(np.float32)
    caida = (1.0 - np.linspace(0, 1, h) ** 0.55)[:, None]
    out.putalpha(Image.fromarray(np.clip(a * caida * opacidad, 0, 255).astype(np.uint8)))
    return out


def sombra_direccional(lienzo, silueta, cx, ybase, anc, lado="der"):
    """La sombra sale de la SILUETA de la botella, no de elipses.

    ⛔ POR QUÉ SE REHIZO (Coni la marcó tres veces). Estaba armada con elipses
    superpuestas y, por muy chicas que se hicieran, la suma de sus bordes
    difuminados dejaba una mancha que no correspondía a ninguna forma real y se
    leía como un borrón al costado. Se comprobó apagándolas: sin ellas la mancha
    desaparecía, así que era mía y no del fondo.

    Lo que hace una botella de verdad: proyecta SU PROPIA FORMA, aplastada
    contra la mesa por el escorzo, corta si la luz es alta, y desplazada al lado
    contrario del haz. Eso es lo que se dibuja ahora.
    """
    signo = -1 if lado == "der" else 1
    alfa = silueta.split()[-1]
    w, h = alfa.size

    # sólo el tercio inferior: es lo que apoya y proyecta
    base = alfa.crop((0, int(h * 0.68), w, h))
    # aplastada contra la mesa
    prj = base.resize((w, max(6, int(h * 0.075))), Image.LANCZOS)

    capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    tinta = Image.new("RGBA", prj.size, (5, 3, 1, 255))
    tinta.putalpha(prj.point(lambda v: int(v * 0.62)))
    x = int(cx - w / 2 + signo * anc * 0.10)
    y = int(ybase - prj.height * 0.42)
    capa.alpha_composite(tinta, (x, y))
    lienzo.alpha_composite(capa.filter(ImageFilter.GaussianBlur(anc * 0.055)))

    # contacto: la línea oscura justo donde el vidrio toca la piedra
    oc = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    tinta2 = Image.new("RGBA", prj.size, (0, 0, 0, 255))
    tinta2.putalpha(prj.point(lambda v: int(v * 0.80)))
    oc.alpha_composite(tinta2.resize((int(w * 0.94), max(4, int(prj.height * 0.42))), Image.LANCZOS),
                       (int(cx - w * 0.47), int(ybase - prj.height * 0.16)))
    lienzo.alpha_composite(oc.filter(ImageFilter.GaussianBlur(anc * 0.013)))

def aplana_mesa(f, desde=0.66, fuerza=0.95):
    """Iguala la luz de la mesa de lado a lado.

    ⛔ EL BUG QUE COSTÓ DOS RONDAS. La escena generada trae el mármol más oscuro
    de un lado, y esa penumbra se lee como una sombra suelta «volando» al costado
    de la botella — Coni la marcó dos veces creyendo que era la sombra que yo
    dibujaba. No lo era: la sombra estaba bien puesta y era el FONDO.

    Se corrige aplanando el perfil horizontal de esa franja: se divide por su
    propia media por columna, muy suavizada, así que desaparecen las manchas
    grandes y la veta fina del mármol se queda."""
    a = np.asarray(f).astype(np.float32)
    h, w, _ = a.shape
    y0 = int(h * desde)
    zona = a[y0:]
    lum = zona.mean(axis=2)
    perfil = ndimage.gaussian_filter1d(lum.mean(axis=0), w * 0.055)
    corr = np.clip(perfil.mean() / np.maximum(perfil, 1.0), 0.30, 4.50)
    corr = 1.0 + (corr - 1.0) * fuerza
    rampa = np.clip((np.arange(h - y0) / float(max(1, (h - y0) * 0.25))), 0, 1)[:, None]
    a[y0:] = np.clip(zona * (1.0 + (corr[None, :] - 1.0) * rampa)[:, :, None], 0, 255)
    return Image.fromarray(a.astype(np.uint8))


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
    out = aplana_mesa(out)

    # La veta del mármol de primer plano existe pero es de contraste bajísimo, y
    # el check `desenfoque_parcial` mide VARIANZA del Laplaciano: una banda con
    # textura suave le parece lisa. Un realce local la revela — no inventa nada,
    # sube el micro-contraste de lo que la foto ya tiene.
    realce = out.filter(ImageFilter.UnsharpMask(radius=7, percent=215, threshold=1))
    mezcla = (np.clip((t - 0.72) / 0.10, 0, 1) * 255).astype(np.uint8)
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
    ap.add_argument("--encuadre-x", dest="encuadre_x", type=float, default=0.0)
    # ⚠️ DE MUESTRA. No hay precio del 7Colores Limited Edition Carmenere ni en
    # los editables ni en los briefs de CAVA: hay que pedírselo a la ejecutiva.
    ap.add_argument("--precio", default="$9.245")
    ap.add_argument("--precio-antes", dest="precio_antes", default="$18.490")
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
    # el óvalo de luz del mármol tiene que caer BAJO la botella, no al lado:
    # si no, la botella queda en penumbra sobre una mesa iluminada aparte.
    ox = int((f.width - W) * a.encuadre_x)
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

    b = bot.resize((anc, alto), Image.LANCZOS)
    b = il.integra_luz(b, lado=LADO_LUZ, fuerza=0.75)

    # POZO DE LUZ propio: el óvalo iluminado del fondo no llega hasta donde
    # terminó la botella, y sin luz alrededor el producto queda flotando en
    # penumbra. Es el foco que pondría un fotógrafo, y va ANTES de la sombra
    # para que la oclusión lo recorte y ancle la base.
    pozo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(pozo).ellipse([cx - anc * 1.05, ybase - anc * 0.34,
                                  cx + anc * 1.05, ybase + anc * 0.28],
                                 fill=(255, 226, 178, 44))
    lienzo.alpha_composite(pozo.filter(ImageFilter.GaussianBlur(anc * 0.28)))

    sombra_direccional(lienzo, b, cx, ybase, anc, lado=LADO_LUZ)

    # reflejo en el mármol: la superficie es pulida, así que DEBE devolver algo.
    # Sin él, la franja de abajo quedaba en negro plano (el QA de agencia lo
    # marcaba como «banda con otro foco») y la botella se leía apoyada en la nada.
    lienzo.alpha_composite(reflejo(b, alto), (int(cx - anc / 2), int(ybase)))

    lienzo.alpha_composite(b, (int(cx - anc / 2), int(ybase - alto)))

    # sello oficial, plano y superpuesto, tapando el que trae el packshot
    fx, fy = SELLO_EN_PACKSHOT
    sx = cx - anc / 2 + fx * anc
    sy = ybase - alto + fy * alto
    som = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(som).ellipse([sx - SELLO_DIAM / 2, sy - SELLO_DIAM / 2 + SELLO_DIAM * 0.035,
                                 sx + SELLO_DIAM / 2, sy + SELLO_DIAM / 2 + SELLO_DIAM * 0.035],
                                fill=(0, 0, 0, 96))
    lienzo.alpha_composite(som.filter(ImageFilter.GaussianBlur(SELLO_DIAM * 0.030)))
    se = Image.open(os.path.join(RAIZ, SELLO_PNG)).convert("RGBA").resize(
        (SELLO_DIAM, SELLO_DIAM), Image.LANCZOS)
    lienzo.alpha_composite(se, (int(sx - SELLO_DIAM / 2), int(sy - SELLO_DIAM / 2)))

    # ---------- textos y fijos ----------
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    sept = Image.open(SEPT).convert("RGB")

    logo = Image.open(os.path.join(RAIZ, LOGO_PNG)).convert("RGBA")
    logo = logo.resize((LOGO_W, round(LOGO_W * logo.height / logo.width)), Image.LANCZOS)
    capa.alpha_composite(logo, (LOGO_X, LOGO_Y))

    # UNA SOLA advertencia por pieza. La de conducir REEMPLAZA a la de menores
    # de 18 — no se suma. Sale tal cual de la pág. 18 del PDF del Gobierno.
    legal = Image.open(os.path.join(RAIZ, LEGAL_PNG)).convert("RGBA")
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

    # ── el disco del descuento ─────────────────────────────────────────────
    # Coni, 24-09: el recuadro no la convencía y pidió probarlo en círculo, como
    # un sello de rebaja. En Raleway Black, la del propio editable del Cyber.
    cxd, cyd = BLOQUE_X + DISCO_D // 2, ETIQ_Y + DISCO_D // 2
    disco = Image.new("RGBA", (DISCO_D * 3, DISCO_D * 3), (0, 0, 0, 0))
    ImageDraw.Draw(disco).ellipse([0, 0, DISCO_D * 3 - 1, DISCO_D * 3 - 1],
                                  fill=(225, 103, 14, 255))
    disco = disco.resize((DISCO_D, DISCO_D), Image.LANCZOS)
    capa.alpha_composite(disco, (cxd - DISCO_D // 2, cyd - DISCO_D // 2))

    # Dentro del disco: el «50» manda, y a su derecha una columna con el «%»
    # arriba y el «OFF» debajo. Coni, 24-09: «el 50 debe ser más grande, el OFF
    # al costado en pequeño y sobre el OFF el símbolo de descuento».
    f_num = ImageFont.truetype(F_RAL, 218)
    f_pct = ImageFont.truetype(F_RAL, 84)
    f_off = ImageFont.truetype(F_RAL, 58)
    a_num = d.textlength("50", font=f_num)
    tr = 0.16 * f_off.size
    a_off = sum(d.textlength(c, font=f_off) for c in "OFF") + tr * 2
    a_pct = d.textlength("%", font=f_pct)
    col = max(a_off, a_pct)
    hueco = 218 * 0.12
    total = a_num + hueco + col
    x0 = cxd - total / 2
    # el «50», centrado en vertical
    d.text((x0, cyd + 218 * 0.32), "50", font=f_num, fill=BLANCO, anchor="ls")
    # el «%» arriba de la columna, alineado con el tope del «50»
    d.text((x0 + a_num + hueco + (col - a_pct) / 2, cyd - 218 * 0.12),
           "%", font=f_pct, fill=BLANCO, anchor="ls")
    # y el «OFF» debajo del «%»
    x = x0 + a_num + hueco + (col - a_off) / 2
    for c in "OFF":
        d.text((x, cyd + 218 * 0.32), c, font=f_off, fill=BLANCO, anchor="ls")
        x += d.textlength(c, font=f_off) + tr



    # ── nombre del vino, tres líneas ───────────────────────────────────────
    f_nom = ft(F_BOLD, 51.28)
    inter = y_arriba(796.1) - y_arriba(847.4)
    for i, linea in enumerate(["7Colores", "Limited Edition", "Carmenere"]):
        escribe(d, (BLOQUE_X, NOMBRE_Y - inter * (2 - i)), linea, f_nom, BLANCO)

    # ── precios: el de ahora manda, el de antes va SIEMPRE tachado ─────────
    # el sistema los tiene en 163,74 y 105,95 sobre la mesa de 1080, pero ahí el
    # bloque no llevaba etiqueta de descuento encima. Se bajan para que el
    # precio no invada la botella — comprobado por el test de choque de abajo.
    f_pre = ft(F_BOLD, 124.0)
    f_ant = ft(F_BOOK, 80.0)
    escribe(d, (BLOQUE_X, PRECIO_Y), a.precio, f_pre, BLANCO)
    xf = escribe(d, (BLOQUE_X, ANTES_Y), a.precio_antes, f_ant, (176, 172, 166))
    caja = f_ant.getbbox(a.precio_antes)
    medio = ANTES_Y - (caja[3] - caja[1]) * 0.36
    d.line([(BLOQUE_X - 8, medio), (xf + 2, medio)], fill=(176, 172, 166), width=9)

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

#!/usr/bin/env python3
"""
REVEX octubre 2026 — las 23 tarjetas del brief, en 1:1 y story.

Brief: «Revex brief octubre 2026.xlsx» (Drive 1rnAxEwixHZ5MLybEcg7SkI36FiljlBLa),
de Sebastián Córdova. Los textos de TEXTOS van LITERALES de la columna
«TEXTO SOBRE LA IMAGEN»; no se inventa ninguno.

Decisiones de Serena (29-09-2026), que mandan sobre el brief o sobre el manual:
  · Formato 1:1 como pide el brief, pero a la resolución de Paulina:
    2250 × 2250 y story 2250 × 4000.
  · «Cotiza por WhatsApp» SÍ va dibujado, como en los carruseles Austral de Paulina
    (cápsula gris #868686). Esto se aparta de R-17, que era de la pauta de sucursales.
  · Texto BLANCO con velo (sistema de Paulina), no el «texto oscuro» del look del brief.
  · Los 4 SKU sin foto: se hacen con IA. Estudio: la IA hace AMBIENTE; la muestra sale
    de la foto real del mismo producto (ver revex-oct2026-ambientes.py · derivados()).
    Caucho no tiene foto de nada → tarjeta sin muestra, fondo PROVISORIO.

Gramática: la tarjeta de producto de Paulina (rvx_porcelanatos_2, rvx_austral_2), MEDIDA
a 1080 el 29-09: muestra 530 de ancho con borde blanco · banderola #D92028 251 × 130 con
pliegue #AD1C27 · cápsula del CTA #868686 alto 42 · bloque de logo a la izquierda
(cx 199,9, E-04 del cerebro).
"""
import os, sys, argparse
import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revex_sistema import Lienzo, TAG_RED, BLANCO, BLOCK_RED  # noqa

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AMB = os.path.join(RAIZ, "public/assets/revex/oct")
PROD = os.path.join(RAIZ, "public/assets/revex/oct/productos")
OUT = os.path.join(RAIZ, "out/revex/oct2026")

FEED = (2250, 2250)
STORY = (2250, 4000)

AJUSTE_Y = {(k, st): d for k in ("03A", "03B", "03C") for st, d in ((False, 50), (True, 180))}  # Urban: nombres de color sobre muro claro (30-09) · (pieza, story) → desplazamiento vertical del bloque, medido sobre SU foto
PLIEGUE = (0xAD, 0x1C, 0x27)
CTA_GRIS = (0x86, 0x86, 0x86)
PIE = "Pisos SPC, laminados, porcelanatos, pisos de ingeniería y mucho más"
CTA = "Cotiza por WhatsApp"

# pieza: amb, [muestras], categoría (banderola, sup), TÍTULO, BAJADA, APOYO, sello
# categoría: SÓLO si el brief la trae (en 04/05/06/07 viene como BAJADA). En 01/02 la
# primera versión ponía «CERÁMICA DE MURO», sacado del sitio: no está en el brief → fuera (QA 29-09, R-23).
# ⭐ RONDA 3 — 30-09-2026. Jenny Campos (la clienta), por WhatsApp a Serena:
#   «las fotos ambientadas están todas malas» · «si no encuentras fotos de algún producto se
#   saca de la lista y solo se deja lo que está en el link» · «en keraz te solicité 5 productos y
#   solo te adjunté de 3… se dejan solo esos 3» · «de las alfombras sacar los 2 post y dejar solo
#   de alfombras dimensionadas en general, te adjunté 3 imágenes» · cerámicas blancas: «estoy
#   esperando validación».
# Los fondos IA quedan DESCARTADOS: cada tarjeta usa la foto de la clienta (carpeta «AGENCIA »,
# 1RfSf8kOi5f9hLmL2TJQAWssQGqqIB4JB → public/assets/revex/oct/cliente/, con PROCEDENCIA.tsv).
# foto = archivo de la clienta · foco = posición vertical del recorte (feed, story).
CLI = os.path.join(RAIZ, "public/assets/revex/oct/cliente")
T = {
 # 01A Blanco Brillante y 01B Blanco Mate: EN ESPERA, Jenny está validando esas fotos (30-09).
 "01C": dict(foto="BISELADO BLANCO BRILLO.png", foco=(0.30, 0.5), m=["6351001020_0.jpg"], cat=None,
             tit="Biselado Blanco Brillo", baj="Formato 10×20", apo="Un borde biselado que suma relieve al muro"),
 "01D": dict(foto="2x/BLANCO BRILLO 15X15 CR.jpg", foco=(0.35, 0.5), m=["muestra_cliente_01D.png"], cat=None,
             tit="Blanco Brillo", baj="Formato 15×15", apo="El formato clásico para muros"),
 "01E": dict(foto="2x/BRICK BLANCO MT 7,5x25 CR.jpg", foco=(0.30, 0.5), m=["muestra_cliente_01E.png"], cat=None,
             tit="Brick Blanco", baj="Formato 7,5×25 · en brillo o mate", apo=CTA),
 "02A": dict(foto="KERAZ ANTIQUE GREY.png", foco=(0.5, 0.5), m=["6954003060_0.jpg"], cat=None,
             tit="Keraz Antique Grey", baj="Formato 30×60", apo="Consulta la oferta por WhatsApp", sello="EN OFERTA"),
 "02B": dict(foto="KERAZ MARMO OCEAN VEIN.png", foco=(0.5, 0.5), m=["6962003060_0.jpg"], cat=None,
             tit="Keraz Marmo Ocean Vein", baj="Efecto mármol · 30×60", apo=None),
 "02C": dict(foto="2x/KERAZ MARMO GREY.jpg", foco=(0.5, 0.5), m=["6957003060_0.jpg"], cat=None,
             tit="Keraz Marmo Grey", baj="Efecto mármol · 30×60", apo=CTA),
 # 02D Marmo Rombo y 02E Calacatta Gold: FUERA, la clienta no mandó foto («se dejan solo esos 3»).
 "03A": dict(foto="URBAN LIGHT GREY NAT 30x60 VT.png", foco=(0.55, 0.5), urban=(30, 60), cat=None,
             tit="Porcelanato Urban", baj="Formato 30×60", apo="Disponible en 3 colores"),
 "03B": dict(foto="Urban Light Grey Nat 60x60.png", foco=(0.55, 0.5), urban=(60, 60), cat=None,
             tit="Porcelanato Urban", baj="Formato 60×60", apo="Disponible en 3 colores"),
 "03C": dict(foto="URBAN PEARL NAT 60x120.png", foco=(0.55, 0.5), urban=(60, 120), cat=None,
             tit="Porcelanato Urban", baj="Gran formato 60×120", apo=CTA),
 # 04 (muro a muro) y los modelos de 05: FUERA. Queda UN carrusel de alfombras dimensionadas
 # «en general» con las 3 fotos de la clienta. ⚠️ El brief no trae texto para esto: se usan
 # SÓLO líneas literales del brief de 05 + la etiqueta de cada foto de la clienta
 # («EN STOCK», «A PEDIDO»). Confirmar con Sebastián.
 "05A": dict(foto="ALFOMBRA DIMENSIONADA EN STOCK.webp", foco=(0.62, 0.5), m=["muestra_cliente_05A.png"],
             cat="En stock", tit="Alfombras dimensionadas", baj=None,
             apo="Terminación con cinta en los bordes", cuadrada=True),
 "05B": dict(foto="ALFOMBRA DIMENSIONADAS A PEDIDO.jpg", foco=(0.62, 0.5), m=["muestra_cliente_05B.png"],
             cat="A pedido", tit="Alfombras dimensionadas", baj=None,
             apo="Alfombra dimensionada a tu medida", cuadrada=True),
 "05C": dict(foto="ALFOMBRA DIMENSIONADAS A PEDIDO 2.jpg", foco=(0.6, 0.5), m=["muestra_cliente_05C.png"],
             cat="A pedido", tit="Alfombras dimensionadas", baj=None, apo=CTA, cuadrada=True),
 "06":  dict(foto="Adoquines.png", foco=(0.55, 0.5), m=["muestra_cliente_06.png"],
             cat="Color negro · espesores de 25 y 45 mm", tit="Adoquines de caucho", baj=None, apo=CTA),
 "07A": dict(foto="SPC GRAVITY ARENA.png", foco=(0.6, 0.5), m=["5903607305_0.jpg"], cat="Piso SPC",
             tit="SPC Gravity · Roble Arena", baj=None, apo=None),
 "07B": dict(foto="SPC GRAVITY TITANIO.png", foco=(0.6, 0.5), m=["5903607308_0.jpg"], cat="Piso SPC",
             tit="SPC Gravity · Roble Titanio", baj=None, apo=None),
 "07C": dict(foto="SPC GRAVITY NATURAL.png", foco=(0.6, 0.5), m=["5903607311_0.jpg"], cat="Piso SPC",
             tit="SPC Gravity · Roble Natural", baj=None, apo=CTA),
}
for _k, _t in T.items():
    _t["amb"] = _k.lower()        # sólo para los ajustes por pieza de abajo

# Muestras que salen de la PROPIA foto de la clienta (no hay packshot en el sitio de esos productos):
# recorte (x0, y0, x1, y1) en fracción de la foto.
MUESTRA_DE_FOTO = {
    # 01D y 01E: la muestra deja de ser DERIVADA — sale del muro real de la foto de la clienta
    "01D": ("BLANCO BRILLO 15X15 CR.png", (0.52, 0.10, 0.665, 0.55)),
    "01E": ("BRICK BLANCO MT 7,5x25 CR.png", (0.45, 0.02, 0.95, 0.28)),
    "05A": ("ALFOMBRA DIMENSIONADA EN STOCK.webp", (0.30, 0.62, 0.62, 0.78)),
    "05B": ("ALFOMBRA DIMENSIONADAS A PEDIDO.jpg", (0.30, 0.76, 0.62, 0.90)),
    "05C": ("ALFOMBRA DIMENSIONADAS A PEDIDO 2.jpg", (0.40, 0.80, 0.60, 0.97)),
    "06":  ("Adoquines.png", (0.25, 0.70, 0.75, 0.90)),
}


# BAJADA de 04/05/06/07: el brief la da como bajada («Alfombra muro a muro», «Piso SPC»…);
# en la gramática de Paulina ese dato es la categoría de la banderola, así que va ahí, literal.
# Stories que NO usan la expansión sino el cuadrado recortado en vertical (cover):
# en las alfombras muro a muro, image-expand inventó piso de madera bajo la alfombra
# dos veces seguidas, con y sin instrucción (29-09). Recorte = la misma foto aprobada.
DESDE_CUADRADO = set()   # ronda 3: ya no hay ambientes IA ni expansiones
URBAN = [("Pearl", "7411"), ("Light Grey", "7412"), ("Anthracite", "7413")]


# ─────────────────────────────── piezas del sistema ───────────────────────────────
def velo_abajo(L, desde, hasta, alpha, luma_obj=None, suelta=None):
    """Si se da luma_obj, alpha se calcula para que la meseta quede en esa luma media:
    sobre un baño blanco el 34 % deja el fondo en ~155 y el texto blanco no se lee.
    La portada «muros» aprobada tenía 167,7 bajo el titular (bold grande); acá el texto
    es más chico, así que se pide menos.
    """
    if luma_obj is not None:
        g = np.asarray(L.im.convert("L")).astype(np.float64)
        fin = int(L.P(suelta[0])) if suelta else None
        med = g[int(L.P(hasta)):fin].mean()
        # tope 0,36: con 0,62 el velo cambiaba el COLOR del producto (el Roble Arena se leía
        # Titanio, el baño blanco gris). QA 29-09. Paulina tiene 2,0–4,0:1 en el cuerpo de Austral.
        alpha = float(np.clip(1 - luma_obj / max(med, 1), 0.18, 0.36))
    """Banda oscura bajo el bloque de texto (misma lógica que el velo medido,
    que es banda y no degradado de página), con rampa suave de entrada."""
    a = np.asarray(L.im).astype(np.float64)
    for y in range(L.Hpx):
        yn = y / L.S
        if yn < desde: k = 0
        elif yn < hasta: k = alpha * ((yn - desde) / (hasta - desde)) ** 1.4
        elif suelta and yn > suelta[0]:   # story: la banda se suelta bajo el texto
            k = alpha * max(0.0, 1 - (yn - suelta[0]) / (suelta[1] - suelta[0]))
        else: k = alpha
        if k: a[y] *= 1 - k
    L.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); L.d = ImageDraw.Draw(L.im, "RGBA")


def muestra(L, archivo, x0, y0, w, h, recorte=None):
    """Muestra real con borde blanco y sombra suave, como la de Paulina."""
    im = Image.open(os.path.join(PROD, archivo)).convert("RGB")
    iw, ih = im.size
    r = w / h
    # recorte centrado a la proporción de la muestra (las fotos del sitio son cuadradas,
    # con la palmeta sobre blanco en las _1: se usan las _0, que son textura a sangre)
    if iw / ih > r: nw = ih * r; box = ((iw - nw) / 2, 0, (iw + nw) / 2, ih)
    else: nh = iw / r; box = (0, (ih - nh) / 2, iw, (ih + nh) / 2)
    im = im.crop(tuple(map(round, box))).resize((round(L.P(w)), round(L.P(h))), Image.LANCZOS)
    # sombra
    sh = Image.new("RGBA", L.im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([L.P(x0 + 2), L.P(y0 + 6), L.P(x0 + w + 2), L.P(y0 + h + 8)],
                                          radius=L.P(12), fill=(0, 0, 0, 70))
    from PIL import ImageFilter
    sh = sh.filter(ImageFilter.GaussianBlur(L.P(9)))
    L.im = Image.alpha_composite(L.im.convert("RGBA"), sh).convert("RGB")
    L.d = ImageDraw.Draw(L.im, "RGBA")
    b = 4  # borde blanco medido ≈ 3,5 a 1080
    L.d.rounded_rectangle([L.P(x0 - b), L.P(y0 - b), L.P(x0 + w + b), L.P(y0 + h + b)],
                          radius=L.P(12), fill=BLANCO)
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], radius=L.P(9), fill=255)
    L.im.paste(im, (round(L.P(x0)), round(L.P(y0))), m)
    L.d = ImageDraw.Draw(L.im, "RGBA")


def aparejo(src, pw, ph, destino, n=(3, 5), junta=(212, 214, 216)):
    """Muestra de cerámica lisa: la foto del sitio es blanco puro y se lee como una
    tarjeta vacía (primera 01A, 29-09). Se arma la palmeta REAL en su aparejo, con
    junta, a partir del mismo esmalte fotografiado. Es la foto del producto; no es IA."""
    if os.path.exists(destino): return
    base = Image.open(os.path.join(PROD, src)).convert("RGB")
    cols, filas = n
    W = 1200; esc = W / (cols * pw); H = round(filas * ph * esc)
    tex = base.resize((W, max(H, W)), Image.LANCZOS).crop((0, 0, W, H))
    d = ImageDraw.Draw(tex)
    for i in range(1, cols): x = round(i * pw * esc); d.line([(x, 0), (x, H)], fill=junta, width=6)
    for j in range(1, filas): y = round(j * ph * esc); d.line([(0, y), (W, y)], fill=junta, width=6)
    tex.save(destino)


def flecha_medida(L, txt, y, cx, cap):
    """⟵ medida ⟶ de la banderola, como «60 x 120 cm.» de Paulina: la flecha va encima."""
    cuerpo = L.cuerpo_para_cap(cap, 500)
    w = L.ancho(txt, cuerpo, 500)
    fy = y - cap * 0.95
    L.d.line([L.P(cx - w / 2), L.P(fy), L.P(cx + w / 2), L.P(fy)], fill=BLANCO, width=max(1, round(L.P(1.3))))
    for s in (-1, 1):
        xe = cx + s * w / 2
        L.d.polygon([(L.P(xe), L.P(fy)), (L.P(xe - s * 7), L.P(fy - 3.5)), (L.P(xe - s * 7), L.P(fy + 3.5))], fill=BLANCO)
    L.texto(txt, y, cuerpo, 500, BLANCO, cx)


def banderola(L, cat, nombre, medida, x_der, y0, escala=1.0):
    """Banderola #D92028 con pliegue #AD1C27. Ancho al texto (mín. el medido, 251).
    Categoría en regular versalita con tracking · nombre en bold · medida con flechas."""
    e = escala
    c_cat, c_nom, c_med = 9.5 * e, 13 * e, 12 * e        # rvx_porcelanatos_2 @1080
    f_cat = L.cuerpo_para_cap(c_cat, 400); f_nom = L.cuerpo_para_cap(c_nom, 700)
    tr = 0.06
    cat_txt = (cat or "").upper()
    w_txt = max(L.ancho(cat_txt, f_cat, 400, tr), L.ancho(nombre.upper(), f_nom, 700, 0.01),
                L.ancho(medida, L.cuerpo_para_cap(c_med, 500), 500) if medida else 0)
    w = max(251 * e, w_txt + 2 * 24 * e)
    flecha = bool(medida) and "·" not in medida       # la flecha es de UNA medida, no de una lista
    h_cat = (c_cat + 14 * e) if cat_txt else 0
    h = 26 * e + h_cat + c_nom + ((14 + (11 if flecha else 0)) * e + c_med if medida else 0) + 26 * e
    x0 = x_der - w
    L.d.rectangle([L.P(x0), L.P(y0), L.P(x_der), L.P(y0 + h)], fill=TAG_RED)
    # SIN pliegue: Paulina 29-09 en P01A, «eliminar triangulo. esto va para todas las otras
    # graficas que lo tengan» (también en P06 y P07A). Deroga el pliegue #AD1C27 para este lote.
    cx = x0 + w / 2
    y = y0 + 26 * e
    if cat_txt:
        L.texto(cat_txt, y, f_cat, 400, BLANCO, cx, tr); y += c_cat + 14 * e
    L.texto(nombre.upper(), y, f_nom, 700, BLANCO, cx, 0.01); y += c_nom
    if medida and flecha:
        y += (14 + 11) * e
        flecha_medida(L, medida, y, cx, c_med)
    elif medida:
        y += 14 * e
        L.texto(medida, y, L.cuerpo_para_cap(c_med, 500), 500, BLANCO, cx)
    return x0, y0 + h


def cta(L, y, cx=540, cap=15.5, e=1.0):
    """Cápsula gris del CTA (#868686), MEDIDA en rvx_austral_2: alto 42, radio ~8."""
    cuerpo = L.cuerpo_para_cap(cap, 500)
    w = L.ancho(CTA, cuerpo, 500, 0.02) + 2 * 30 * e
    h = 42 * e
    L.d.rounded_rectangle([L.P(cx - w / 2), L.P(y), L.P(cx + w / 2), L.P(y + h)], radius=L.P(9 * e), fill=CTA_GRIS)   # opaco: #868686 exacto, como el medido
    L.texto(CTA, y + (h - cap) / 2, cuerpo, 500, BLANCO, cx, 0.02)
    return y + h


def banda(L, y0, y1, alpha, rampa):
    """Velo en banda entre y0 e y1 (norm), con rampas suaves hacia afuera."""
    a = np.asarray(L.im).astype(np.float64)
    for yy in range(max(0, int(L.P(y0 - rampa))), min(L.Hpx, int(L.P(y1 + rampa)))):
        yn = yy / L.S
        k = alpha if y0 <= yn <= y1 else alpha * (1 - min(abs(yn - y0), abs(yn - y1)) / rampa)
        a[yy] *= 1 - max(0.0, k)
    L.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); L.d = ImageDraw.Draw(L.im, "RGBA")


def banda_pie(L, y, alto=46, alpha=0.40, rampa=34):
    """Velo en BANDA detrás del pie (el velo medido de Paulina es banda, no degradado).
    Separa la legibilidad del texto más chico del color del producto: con un solo velo
    fuerte el piso cambiaba de tono; con uno suave el pie bajaba de 3:1 (QA 29-09)."""
    a = np.asarray(L.im).astype(np.float64)
    y0, y1 = y - alto / 2 + 6, y + alto / 2 + 6
    for yy in range(max(0, int(L.P(y0 - rampa))), min(L.Hpx, int(L.P(y1 + rampa)))):
        yn = yy / L.S
        k = alpha if y0 <= yn <= y1 else alpha * (1 - min(abs(yn - y0), abs(yn - y1)) / rampa)
        a[yy] *= 1 - max(0.0, k)
    L.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); L.d = ImageDraw.Draw(L.im, "RGBA")


def degradado(L, y0, y1, alpha, y2=None, y3=None):
    """Degradado MUY suave detrás del texto (Paulina 29-09: «siempre debe ir un degradado muy
    suave detras del texto para que destaque pero nunca ese tipo de cuadro cortado»).
    Sube de 0 en y0 a alpha en y1 con curva suave; en story vuelve a 0 entre y2 e y3.
    Reemplaza las bandas de velo (banda/banda_pie) que ella rechazó."""
    a = np.asarray(L.im).astype(np.float64)
    def ss(t): t = min(max(t, 0.0), 1.0); return t * t * (3 - 2 * t)
    for yy in range(L.Hpx):
        yn = yy / L.S
        k = alpha * ss((yn - y0) / (y1 - y0))
        if y2 is not None and yn > y2: k = alpha * (1 - ss((yn - y2) / (y3 - y2)))
        if k > 0.001: a[yy] *= 1 - k
    L.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); L.d = ImageDraw.Draw(L.im, "RGBA")


PIE_2 = ("Pisos SPC, laminados, porcelanatos,", "pisos de ingeniería y mucho más")


def pie2(L, y, cap, peso=600):
    """Pie de la story en DOS líneas y más grande (Paulina 29-09, P01A story: «texto demasiado
    pequeño aumenta los pt de texto y dejalo en 2 lineas… no deben quedar una palabra sola
    en la segunda linea»). Corte en la coma: 4 palabras abajo."""
    cuerpo = L.cuerpo_para_cap(cap, peso)
    w = max(L.ancho(x, cuerpo, peso, 0.01) for x in PIE_2)
    L.filete(y - 22, ancho=w + 50, grosor=1.4, color=(255, 255, 255, 170))
    L.texto(PIE_2[0], y, cuerpo, peso, BLANCO, 540, 0.01)
    L.texto(PIE_2[1], y + cap * 1.75, cuerpo, peso, BLANCO, 540, 0.01)
    return y + cap * 1.75 + cap


def pie(L, y, cap=12, peso=600):
    """PIE (franja fija) del brief. Se traduce a un elemento que el sistema ya tiene:
    línea regular entre filetes finos, como la bajada de Paulina. No es una barra nueva."""
    cuerpo = L.cuerpo_para_cap(cap, peso)
    w = L.ancho(PIE, cuerpo, peso, 0.01)
    L.filete(y - 16, ancho=w + 40, grosor=1.2, color=(255, 255, 255, 170))
    L.texto(PIE, y, cuerpo, peso, BLANCO, 540, 0.01)


def apoyo(L, txt, y, cap=17):
    cuerpo = L.cuerpo_para_cap(cap, 600)
    L.texto(txt, y, cuerpo, 600, BLANCO, 540)
    return y + cap


# ─────────────────────────────── armado ───────────────────────────────
def muestras_de_foto():
    for k, (f, (x0, y0, x1, y1)) in MUESTRA_DE_FOTO.items():
        im = Image.open(os.path.join(CLI, f)).convert("RGB"); W, H = im.size
        im.crop((round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H))).save(
            os.path.join(PROD, f"muestra_cliente_{k}.png"))


def pieza(k, story=False):
    t = T[k]
    aparejo("6910003060_0.jpg", 60, 30, os.path.join(PROD, "aparejo_6910003060.png"), n=(3, 3))
    aparejo("6910102540_0.jpg", 25, 40, os.path.join(PROD, "aparejo_6910102540.png"), n=(5, 2))
    L = Lienzo(*(STORY if story else FEED))
    L.fondo(os.path.join(CLI, t["foto"]), foco=t["foco"][1 if story else 0])
    # La story tiene su PROPIA escala: copiar el cuadrado «se ve muy pequeño» (Paulina 29-09,
    # P03A story: «toda esta estructura debe adaptarse al tamaño de la storie»).
    e = 1.35 if story else 1.0
    y_m = 640 if story else 560
    # Ajustes por pieza, medidos sobre su foto (QA ronda 2, 29-09):
    #  · 06: el apilado de adoquines de la escena quedaba bajo la muestra y asomaba por el marco;
    #    el bloque sube a piso liso (feed) y el pie de la story ya no pisa el apilado.
    #  · 03 story: los nombres de color caían sobre la ventana (casi blanca) y no se leían.
    y_m += AJUSTE_Y.get((k, story), 0)
    # degradado muy suave detrás del bloque de texto; la muestra se dibuja encima y no se toca
    if story:
        degradado(L, 820, 1060, 0.42, 1330, 1640)
    else:
        degradado(L, 600, 930, 0.42)
    if story:
        L.bloque_logo(story=True)
    else:
        L.bloque_logo(cx=199.9)

    y = y_m
    if t.get("sello"):
        # separada ≥ 90 de la banderola: dos cuadros rojos pegados rompen la regla R-05 de Paulina
        L.barra(t["sello"], y - 150 * e, 20 * e, peso=775, tracking=0.04, padx=20 * e, padv=12 * e)

    if t.get("urban"):
        a, b = t["urban"]
        eu = min(e, 1.2)                         # 3 × 60×120 a ×1,35 no caben en 1080
        k_cm = 2.05 * eu  # misma escala en las 3 tarjetas: se ve crecer el formato
        w, h = b * k_cm, a * k_cm
        gap = 22 * eu
        tot = 3 * w + 2 * gap
        x = 540 - tot / 2
        fila = 123 * eu
        yb = y + fila - h  # alineadas abajo, así se nota el cambio de alto
        for nombre, pre in URBAN:
            f = f"derivado_{pre}003060.png" if (a, b) == (30, 60) else \
                f"{pre}006060_0.jpg" if (a, b) == (60, 60) else f"{pre}0060120_0.jpg"
            muestra(L, f, x, yb, w, h)
            # el nombre cabe en su muestra + medio hueco a cada lado: en la story 30×60 los tres
            # se pisaban («PEARL LIGHT GREY ANTHRACITE» en una línea, QA 29-09)
            capn = min(L.cap_que_cabe(n2.upper(), 12.5 * e, 600, w + gap - 14, 0.06)
                       for n2, _ in URBAN)
            c = L.cuerpo_para_cap(capn, 600)
            L.texto(nombre.upper(), y + fila + 20 * e, c, 600, BLANCO, x + w / 2, 0.06)
            x += w + gap
        # banderola centrada sobre la fila, con aire: no pisa ninguna muestra
        bw = max(251 * e, L.ancho(t["tit"].upper(), L.cuerpo_para_cap(13 * e, 700), 700, 0.01) + 48 * e)
        banderola(L, t["cat"], t["tit"], t["baj"], 540 + bw / 2, y - (26 + 90) * e, e)
        y = y + fila + (20 + 12.5) * e
    elif t.get("cuadrada"):
        mw = mh = 250 * e
        mx = 540 - mw / 2 - 120 * e
        muestra(L, t["m"][0], mx, y - 40 * e, mw, mh)
        banderola(L, t["cat"], t["tit"], None, mx + mw + 250 * e, y + 60 * e, e)
        y = y - 40 * e + mh
    else:
        # 06 no tiene foto de producto: la muestra es un recorte PROVISORIO del ambiente
        # generado (los adoquines apilados, que muestran los dos espesores). Paulina 29-09:
        # «faltó la muestra del producto».
        archivo = t["m"][0]
        mw, mh = ((440, 220) if archivo.startswith("PROVISORIO") else (530, 190))
        mw, mh = mw * e, mh * e
        mx = 540 - mw / 2
        muestra(L, archivo, mx, y, mw, mh)
        banderola(L, t["cat"], t["tit"], t["baj"], mx + mw - 23 * e, y - 14 * e, e)
        y = y + mh

    y += 42 * e
    if t["apo"] and t["apo"] != CTA:
        L.filete(y, ancho=560 * e, grosor=1.3 * e)
        y = apoyo(L, t["apo"], y + 24 * e, cap=17 * e) + 24 * e
        L.filete(y, ancho=560 * e, grosor=1.3 * e)
        y += 26 * e
    y = cta(L, y, cap=15.5 * e, e=e)
    if story:
        pie2(L, y + 80, cap=17)
    else:
        pie(L, 1010)   # 1040 dejaba 28 de respiro al borde; el QA pide 60 px (29-09)
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("que", nargs="*", default=[])
    ap.add_argument("--solo-feed", action="store_true")
    a = ap.parse_args()
    muestras_de_foto()
    ks = [k for k in T if not a.que or any(k.startswith(q.upper()) for q in a.que)]
    for k in ks:
        for story in ([False] if a.solo_feed else [False, True]):
            amb = os.path.join(CLI, T[k]["foto"])
            if not os.path.exists(amb):
                print(f"· {k} {'story' if story else 'feed'}: falta {T[k]['foto']}"); continue
            L = pieza(k, story)
            nombre = f"REVEX_P{k}_{'Story_2250x4000' if story else 'Feed_2250x2250'}.png"
            print("✓", L.guardar(os.path.join(OUT, nombre)))


if __name__ == "__main__":
    main()

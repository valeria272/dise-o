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

PLIEGUE = (0xAD, 0x1C, 0x27)
CTA_GRIS = (0x86, 0x86, 0x86)
PIE = "Pisos SPC, laminados, porcelanatos, pisos de ingeniería y mucho más"
CTA = "Cotiza por WhatsApp"

# pieza: amb, [muestras], categoría (banderola, sup), TÍTULO, BAJADA, APOYO, sello
# categoría: SÓLO si el brief la trae (en 04/05/06/07 viene como BAJADA). En 01/02 la
# primera versión ponía «CERÁMICA DE MURO», sacado del sitio: no está en el brief → fuera (QA 29-09, R-23).
T = {
 "01A": dict(amb="01a", m=["aparejo_6910003060.png"], cat=None, tit="Blanco Brillante",
             baj="Formatos 20×30 · 25×40 · 30×60", apo="Luz y amplitud para baños y cocinas"),
 "01B": dict(amb="01b", m=["aparejo_6910102540.png"], cat=None, tit="Blanco Mate",
             baj="Formatos 25×40 · 30×60", apo="El blanco de siempre, sin brillo"),
 "01C": dict(amb="01c", m=["6351001020_0.jpg"], cat=None, tit="Biselado Blanco Brillo",
             baj="Formato 10×20", apo="Un borde biselado que suma relieve al muro"),
 "01D": dict(amb="01d", m=["derivado_6353001515.png"], cat=None, tit="Blanco Brillo",
             baj="Formato 15×15", apo="El formato clásico para muros"),
 "01E": dict(amb="01e", m=["6355175250_0.jpg"], cat=None, tit="Brick Blanco",
             baj="Formato 7,5×25 · en brillo o mate", apo=CTA),
 "02A": dict(amb="02a", m=["6954003060_0.jpg"], cat=None, tit="Keraz Antique Grey",
             baj="Formato 30×60", apo="Consulta la oferta por WhatsApp", sello="EN OFERTA"),
 "02B": dict(amb="02b", m=["6962003060_0.jpg"], cat=None, tit="Keraz Marmo Ocean Vein",
             baj="Efecto mármol · 30×60", apo=None),
 "02C": dict(amb="02c", m=["6957003060_0.jpg"], cat=None, tit="Keraz Marmo Grey",
             baj="Efecto mármol · 30×60", apo=None),
 "02D": dict(amb="02d", m=["6958003060_0.jpg"], cat=None, tit="Keraz Marmo Rombo",
             baj="Efecto mármol · 30×60", apo=None),
 "02E": dict(amb="02e", m=["6963003060_0.jpg"], cat=None, tit="Keraz Calacatta Gold",
             baj="Efecto mármol · 30×60", apo=CTA),
 "03A": dict(amb="03", urban=(30, 60), cat=None, tit="Porcelanato Urban",
             baj="Formato 30×60", apo="Disponible en 3 colores"),
 "03B": dict(amb="03", urban=(60, 60), cat=None, tit="Porcelanato Urban",
             baj="Formato 60×60", apo="Disponible en 3 colores"),
 "03C": dict(amb="03", urban=(60, 120), cat=None, tit="Porcelanato Urban",
             baj="Gran formato 60×120", apo=CTA),
 "04A": dict(amb="04a", m=["5690020092_0.jpg"], cat="Alfombra muro a muro", tit="Santana · Gris Perla",
             baj=None, apo="Rollo de 4 m de ancho", cuadrada=True),
 "04B": dict(amb="04b", m=["5690040063_0.jpg"], cat="Alfombra muro a muro", tit="Salamanca · Arena",
             baj=None, apo="Rollo de 4 m de ancho", cuadrada=True),
 "04C": dict(amb="04c", m=["5690066600_0.jpg"], cat="Alfombra muro a muro", tit="Bruselas · Lino",
             baj=None, apo="Rollo de 4 m de ancho", cuadrada=True),
 "04D": dict(amb="04d", m=["5690067000_0.jpg"], cat="Alfombra muro a muro", tit="Bruselas · Castaña",
             baj=None, apo=CTA, cuadrada=True),
 "05A": dict(amb="05a", m=["5698209037_0.jpg"], cat="Alfombra dimensionada a tu medida",
             tit="Nature Rainbow · Tivoli", baj=None, apo="Terminación con cinta en los bordes", cuadrada=True),
 "05B": dict(amb="05b", m=["5698209073_0.jpg"], cat="Alfombra dimensionada a tu medida",
             tit="Nature Rainbow · Trieste", baj=None, apo="Terminación con cinta en los bordes", cuadrada=True),
 "05C": dict(amb="05c", m=["5698209084_0.jpg"], cat="Alfombra dimensionada a tu medida",
             tit="Nature Rainbow · Treviso", baj=None, apo=CTA, cuadrada=True),
 "06":  dict(amb="06", m=["PROVISORIO_IA_caucho_detalle.png"], cat="Color negro · espesores de 25 y 45 mm", tit="Adoquines de caucho",
             baj=None, apo=CTA),
 "07A": dict(amb="07a", m=["5903607305_0.jpg"], cat="PISO SPC", tit="SPC Gravity · Roble Arena",
             baj=None, apo=None),
 "07B": dict(amb="07b", m=["5903607308_0.jpg"], cat="PISO SPC", tit="SPC Gravity · Roble Titanio",
             baj=None, apo=None),
 "07C": dict(amb="07c", m=["5903607311_0.jpg"], cat="PISO SPC", tit="SPC Gravity · Roble Natural",
             baj=None, apo=CTA),
}
# BAJADA de 04/05/06/07: el brief la da como bajada («Alfombra muro a muro», «Piso SPC»…);
# en la gramática de Paulina ese dato es la categoría de la banderola, así que va ahí, literal.
T["07A"]["cat"] = T["07B"]["cat"] = T["07C"]["cat"] = "Piso SPC"
# Stories que NO usan la expansión sino el cuadrado recortado en vertical (cover):
# en las alfombras muro a muro, image-expand inventó piso de madera bajo la alfombra
# dos veces seguidas, con y sin instrucción (29-09). Recorte = la misma foto aprobada.
DESDE_CUADRADO = {"04a", "04b", "04c", "04d"}
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
def pieza(k, story=False):
    t = T[k]
    aparejo("6910003060_0.jpg", 60, 30, os.path.join(PROD, "aparejo_6910003060.png"), n=(3, 3))
    aparejo("6910102540_0.jpg", 25, 40, os.path.join(PROD, "aparejo_6910102540.png"), n=(5, 2))
    L = Lienzo(*(STORY if story else FEED))
    amb = os.path.join(AMB, f"amb_{t['amb']}{'_story' if story and t['amb'] not in DESDE_CUADRADO else ''}.png")
    L.fondo(amb)
    # La story tiene su PROPIA escala: copiar el cuadrado «se ve muy pequeño» (Paulina 29-09,
    # P03A story: «toda esta estructura debe adaptarse al tamaño de la storie»).
    e = 1.35 if story else 1.0
    y_m = 640 if story else 560
    # Ajustes por pieza, medidos sobre su foto (QA ronda 2, 29-09):
    #  · 06: el apilado de adoquines de la escena quedaba bajo la muestra y asomaba por el marco;
    #    el bloque sube a piso liso (feed) y el pie de la story ya no pisa el apilado.
    #  · 03 story: los nombres de color caían sobre la ventana (casi blanca) y no se leían.
    y_m += {("06", False): -280, ("06", True): -80, ("03", True): 180}.get((t["amb"][:2], story), 0)
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
    ks = [k for k in T if not a.que or any(k.startswith(q.upper()) for q in a.que)]
    for k in ks:
        for story in ([False] if a.solo_feed else [False, True]):
            amb = os.path.join(AMB, f"amb_{T[k]['amb']}{'_story' if story and T[k]['amb'] not in DESDE_CUADRADO else ''}.png")
            if not os.path.exists(amb):
                print(f"· {k} {'story' if story else 'feed'}: falta {os.path.basename(amb)}"); continue
            L = pieza(k, story)
            nombre = f"REVEX_P{k}_{'Story_2250x4000' if story else 'Feed_2250x2250'}.png"
            print("✓", L.guardar(os.path.join(OUT, nombre)))


if __name__ == "__main__":
    main()

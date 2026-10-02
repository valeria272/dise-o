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
from revex_sistema import Lienzo, TAG_RED, BLANCO, BLOCK_RED, BAR_RED  # noqa

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AMB = os.path.join(RAIZ, "public/assets/revex/oct")
PROD = os.path.join(RAIZ, "public/assets/revex/oct/productos")
OUT = os.path.join(RAIZ, "out/revex/oct2026")

FEED = (2250, 2250)
STORY = (2250, 4000)

AJUSTE_Y = {(k, False): 50 for k in ("03A", "03B", "03C")}  # Urban: nombres de color sobre muro claro (30-09) · (pieza, story) → desplazamiento vertical del bloque, medido sobre SU foto
PLIEGUE = (0xAD, 0x1C, 0x27)
CTA_GRIS = (0x86, 0x86, 0x86)
PIE = "Pisos SPC, laminados, porcelanatos, pisos de ingeniería y mucho más"
CTA = "Cotiza por WhatsApp"

# pieza: amb, [muestras], categoría (banderola, sup), TÍTULO, BAJADA, APOYO, sello
# categoría: SÓLO si el brief la trae (en 04/05/06/07 viene como BAJADA). En 01/02 la
# primera versión ponía «CERÁMICA DE MURO», sacado del sitio: no está en el brief → fuera (QA 29-09, R-23).
# ⭐ RONDA 4 — 01-10-2026. Lista de cambios de Serena con lo que marcó la clienta
#   («Solo cambia lo que está en esta lista. No muevas nada más de las piezas»):
#   1 stories: logo centrado (YA lo estaba: x 432–647, medido) · bloque centrado · muestra más chica
#     y con «solo un trozo del producto» para que se vea el ambiente · 2 feed: SÓLO centrar el logo ·
#   3 SPC Gravity: una sola línea en el marco (la 2ª era la franja blanca entre tablas de la foto del
#     sitio → se recorta UNA tabla) + «EN OFERTA» + «Dale un nuevo aire a tu HOGAR» ·
#   4 caucho: «EN OFERTA» + «Pisos seguros y resistentes para tus espacios exteriores» ·
#   5 alfombras: fuera «a pedido» y «stock»; «Alfombras personalizadas · Tú eliges la medida, el
#     diseño y la cinta» (la lista nombra 04 y Nature Rainbow, que ya no existen: se aplica a P05A–C).
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
 "02C": dict(foto="2x/KERAZ MARMO GREY (sin logo de app).png", foco=(0.5, 0.5), m=["6957003060_0.jpg"], cat=None,
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
             cat=None, tit="Alfombras personalizadas", baj=None,
             apo="Tú eliges la medida, el diseño y la cinta", cuadrada=True),
 "05B": dict(foto="ALFOMBRA DIMENSIONADAS A PEDIDO.jpg", foco=(0.62, 0.5), m=["muestra_cliente_05B.png"],
             cat=None, tit="Alfombras personalizadas", baj=None,
             apo="Tú eliges la medida, el diseño y la cinta", cuadrada=True),
 "05C": dict(foto="ALFOMBRA DIMENSIONADAS A PEDIDO 2.jpg", foco=(0.6, 0.5), m=["muestra_cliente_05C.png"],
             cat=None, tit="Alfombras personalizadas", baj=None,
             apo="Tú eliges la medida, el diseño y la cinta", cuadrada=True),
 "06":  dict(foto="Adoquines.png", foco=(0.55, 0.5), m=["muestra_cliente_06.png"],
             cat="Color negro · espesores de 25 y 45 mm", tit="Adoquines de caucho", baj=None, apo=CTA, sello="EN OFERTA", frase=("Pisos seguros y resistentes", "para tus espacios exteriores")),
 "07A": dict(foto="SPC GRAVITY ARENA.png", foco=(0.6, 0.5), m=["5903607305_0.jpg"], cat="Piso SPC",
             tit="SPC Gravity · Roble Arena", baj=None, apo=None, sello="EN OFERTA", frase=("Dale un nuevo aire a tu HOGAR",)),
 "07B": dict(foto="SPC GRAVITY TITANIO.png", foco=(0.6, 0.5), m=["tabla_5903607308.png"], cat="Piso SPC",
             tit="SPC Gravity · Roble Titanio", baj=None, apo=None, sello="EN OFERTA", frase=("Dale un nuevo aire a tu HOGAR",)),
 "07C": dict(foto="SPC GRAVITY NATURAL.png", foco=(0.6, 0.5), m=["tabla_5903607311.png"], cat="Piso SPC",
             tit="SPC Gravity · Roble Natural", baj=None, apo=CTA, sello="EN OFERTA", frase=("Dale un nuevo aire a tu HOGAR",)),
}
for _k, _t in T.items():
    _t["amb"] = _k.lower()        # sólo para los ajustes por pieza de abajo

# ⭐ RONDA 5 — 02-10-2026. Paulina, 2 comentarios en P01C story («ADS Revex octubre»):
#   1 «esta zona del cuadro es demasiado larga hacia abajo, ajustar para que tenga solo un poco de
#     aire abajo del logo. esto es para todas las stories» → bloque de logo de story con el mismo
#     aire abajo que arriba (ALTO_BLOQUE_STORY), no los 275 del manual.
#   2 «en esta zona no se aprecia el zoom del producto. ajustar para que se vea a detalle el
#     producto. esto para todas las graficas» → la muestra es un ZOOM: el producto se ve más cerca
#     que en el ambiente, con su relieve, junta, veta o trama a la vista. DETALLE = recorte de la
#     foto del sitio (fracción del lado, centro x, centro y) en (feed, story); el centro se elige
#     para que el detalle caiga en la zona que la banderola deja libre (izquierda y abajo).
#     Tope de ampliación ×2,5 sobre el píxel de origen (R-42).
# ⭐ RONDA 6 — 02-10-2026. Paulina, 9 comentarios sobre la ronda 5 + lo que dijo en la sesión:
#   1 SOMBRAS: «evitar sombras localizadas» · «sombra muy oscura y marcada» · «sombra dura». La
#     clienta odia la sombra sólo donde está la huincha de texto. La sombra SALE DE UN BORDE (abajo),
#     llega sin cortarse hasta el borde, es suave y parte donde empieza el TEXTO BLANCO: no sube
#     detrás de los cuadros que se leen solos (banderola, muestra, botón). Si el fondo ya es oscuro,
#     no hay sombra. Ejemplo que dio: P07C feed («no se ve cortada, se ve constante»).
#   2 BOTÓN del CTA ROJO con letra blanca; gris SÓLO si queda justo bajo un cuadro rojo.
#   3 PIE: «subirlo que no quede tan separado del boton de cta» → el pie sigue al botón.
#   4 STORY con mucho espacio: el bloque «un poco más abajo… así no queda texto sobre el objeto
#     en el fondo» (P07A story) → AJUSTE_STORY.
#   5 «logos de app eliminar» (P02C feed): la foto de la clienta trae el destello de la app.
#   6 MUESTRA: la junta de las baldosas no puede caer en el borde del marco → los recortes se
#     eligen con los bordes a MEDIA palmeta (juntas medidas en la foto, en px).
# ronda 7: «en stories este texto debe ser un 15% mas grande sin llegar a los bordes» (pie, P01D story)
CAP_PIE_STORY = 17 * 1.15
SOMBRA_TOPE, SOMBRA_LUMA = 0.36, 145      # opacidad máxima · luma que se busca bajo el texto blanco
# el bloque baja del sofá, la cama o la mesa al piso o a la alfombra
AJUSTE_STORY = {"07A": 220, "07B": 220, "07C": 220, "05A": 240, "05B": 240, "05C": 240}
LOGO_ASPECTO = 2129 / 2489                      # alto / ancho de logo_blanco.png
ALTO_BLOQUE_STORY = 37.8 + 162.7 * LOGO_ASPECTO + 37.8   # = 214,8: mismo aire arriba y abajo del logo
DETALLE = {
 # ⭐ RONDA 7 — 02-10-2026. Paulina: «esta muestra tiene mucho zoom no se nota el modelo de la baldosa»
 # (P01C feed) · «muestra con mucho zoom» (P02A feed, P02C story). El zoom es MODERADO: se tiene que
 # reconocer el modelo (palmetas o motivos enteros), no un trozo irreconocible. Juntas fuera del borde.
 # 01C: juntas horizontales cada 200 px y verticales en 67/500/931 y 278/724 (aparejo trabado).
 # Recorte x 100–900, y 257–543: dos palmetas casi enteras arriba y una entera abajo; la junta
 # horizontal al medio y las verticales al 50 %, 22 % y 78 %.
 "01C": ((0.80, 0.50, 0.40), (0.80, 0.50, 0.40)),
 # 02A: motivos de ~350 px, juntas verticales en 167/520/876 y horizontales en 326/674.
 # Recorte x 0–837, y 350–650: una fila de motivos casi entera, sin junta horizontal a la vista.
 "02A": ((0.837, 0.4185, 0.50), (0.837, 0.4185, 0.50)),
 # mármoles: paño amplio, con la veta de color a la izquierda y abajo, donde no tapa la banderola
 "02B": ((0.85, 0.45, 0.62), (0.85, 0.45, 0.62)),
 "02C": ((0.85, 0.45, 0.55), (0.85, 0.45, 0.55)),
 "07A": ((0.60, 0.50, 0.50), (0.50, 0.50, 0.50)),
 "07B": ((0.60, 0.50, 0.50), (0.58, 0.50, 0.50)),   # tabla de 1000 px: 0,5 la dejaba en ×2,9
 "07C": ((0.60, 0.50, 0.50), (0.58, 0.50, 0.50)),
}

# Muestras que salen de la PROPIA foto de la clienta (no hay packshot en el sitio de esos productos):
# recorte (x0, y0, x1, y1) en fracción de la foto.
MUESTRA_DE_FOTO = {
    # 01D y 01E: la muestra deja de ser DERIVADA — sale del muro real de la foto de la clienta
    # ronda 5 (zoom): ~3,5 palmetas de 15×15 y ~6 de 7,5×25, de la versión ×2; ampliación ≤ ×2,5
    # sobre el píxel original de la clienta
    # ronda 6: bordes a MEDIA palmeta. 01D: juntas verticales en 970/1212/1456/1700/1942 y horizontal
    # en 2610 (px de la ×2) → 4 palmetas de ancho, la junta horizontal al medio. 01E: verticales cada
    # ~163 desde 2660, horizontal en 824 → 6 palmetas de ancho, la junta horizontal al 62 %.
    "01D": ("2x/BLANCO BRILLO 15X15 CR.jpg", (1091 / 4672, 2440 / 3488, 2063 / 4672, 2788 / 3488)),
    "01E": ("2x/BRICK BLANCO MT 7,5x25 CR.jpg", (2743 / 4672, 607 / 3488, 3721 / 4672, 957 / 3488)),
    "05A": ("ALFOMBRA DIMENSIONADA EN STOCK.webp", (0.30, 0.62, 0.62, 0.78)),
    "05B": ("ALFOMBRA DIMENSIONADAS A PEDIDO.jpg", (0.30, 0.76, 0.62, 0.90)),
    "05C": ("ALFOMBRA DIMENSIONADAS A PEDIDO 2.jpg", (0.40, 0.80, 0.60, 0.97)),
    "06":  ("Adoquines.png", (0.25, 0.80, 0.58, 0.867)),   # ronda 5: ~2 adoquines de ancho
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


def muestra(L, archivo, x0, y0, w, h, recorte=None, zoom=1.0, centro=None):
    """Muestra real con borde blanco y sombra suave, como la de Paulina."""
    im = Image.open(os.path.join(PROD, archivo)).convert("RGB")
    iw, ih = im.size
    r = w / h
    # recorte centrado a la proporción de la muestra (las fotos del sitio son cuadradas,
    # con la palmeta sobre blanco en las _1: se usan las _0, que son textura a sangre)
    if iw / ih > r: nw = ih * r; box = ((iw - nw) / 2, 0, (iw + nw) / 2, ih)
    else: nh = iw / r; box = (0, (ih - nh) / 2, iw, (ih + nh) / 2)
    if zoom < 1:   # «solo un trozo del producto» (story, ronda 4): recorte centrado más cerrado
        cx, cy, bw, bh = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2, (box[2] - box[0]) * zoom, (box[3] - box[1]) * zoom
        if centro:   # ronda 5: el detalle se elige, no cae donde caiga el centro de la foto
            cx = min(max(centro[0] * iw, box[0] + bw / 2), box[2] - bw / 2)
            cy = min(max(centro[1] * ih, bh / 2), ih - bh / 2)
        box = (cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2)
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


def cta(L, y, cx=540, cap=15.5, e=1.0, gris=False):
    """Botón del CTA. ROJO de marca con letra blanca (Paulina 02-10: «boton debe ser rojo»… «para que
    llame mucho la atención»); gris #868686 sólo si queda justo bajo un cuadro rojo. Alto 42, radio ~8."""
    cuerpo = L.cuerpo_para_cap(cap, 500)
    w = L.ancho(CTA, cuerpo, 500, 0.02) + 2 * 30 * e
    h = 42 * e
    L.d.rounded_rectangle([L.P(cx - w / 2), L.P(y), L.P(cx + w / 2), L.P(y + h)], radius=L.P(9 * e), fill=CTA_GRIS if gris else BAR_RED)
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


def sombra_desde_abajo(L, y_txt, y_fin, rampa):
    """Sombra de la ronda 6: sale del borde inferior y llega, constante, hasta donde empieza el texto
    blanco (y_txt), donde se apaga con una rampa larga. Nunca una banda sólo detrás del texto.
    La opacidad se calcula para dejar el fondo del texto en SOMBRA_LUMA, con tope SOMBRA_TOPE:
    sobre un fondo que ya es oscuro no se pone nada."""
    g = np.asarray(L.im.convert("L")).astype(np.float64)
    x0, x1 = int(L.W * 0.15), int(L.W * 0.85)
    # se mide la zona MÁS CLARA bajo el texto (percentil 85 de la luma suavizada), no el promedio:
    # con el promedio, los muebles oscuros de abajo dejaban sin sombra el texto que cae sobre el muro blanco
    zona = Image.fromarray(g[int(L.P(y_txt)):int(L.P(y_fin)), x0:x1].astype(np.uint8))
    zona = zona.resize((max(1, zona.size[0] // 24), max(1, zona.size[1] // 24)), Image.BOX)
    med = float(np.percentile(np.asarray(zona), 85))
    alpha = float(np.clip(1 - SOMBRA_LUMA / max(med, 1), 0.0, SOMBRA_TOPE))
    if alpha < 0.03: return 0.0
    a = np.asarray(L.im).astype(np.float64)
    def ss(t): t = min(max(t, 0.0), 1.0); return t * t * (3 - 2 * t)
    y0 = y_txt - 12 - rampa
    for yy in range(max(0, int(L.P(y0))), L.Hpx):
        k = alpha * ss((yy / L.S - y0) / rampa)
        if k > 0.001: a[yy] *= 1 - k
    L.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); L.d = ImageDraw.Draw(L.im, "RGBA")
    return alpha


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


def frase(L, lineas, y, cap, e):
    """Frase de titular (ronda 4: SPC y caucho «se ven vacías»). Montserrat 750, blanca, centrada,
    máximo 2 líneas y sin palabra sola. Va SIN barra: la barra roja de «EN OFERTA» ya está arriba
    y dos cuadros rojos pegados rompen R-05."""
    for i, ln in enumerate(lineas):
        L.texto(ln, y + i * cap * 1.55, L.cuerpo_para_cap(cap, 750), 750, BLANCO, 540, -0.02)
    return y + (len(lineas) - 1) * cap * 1.55 + cap


def apoyo(L, txt, y, cap=17):
    cuerpo = L.cuerpo_para_cap(cap, 600)
    L.texto(txt, y, cuerpo, 600, BLANCO, 540)
    return y + cap


# ─────────────────────────────── armado ───────────────────────────────
# Sólo para la STORY (QA ronda 4): el recorte del 15×15 caía sobre el vidrio de la ducha y, con
# el zoom de «un trozo», quedaba ×7,5 y sin ninguna palmeta visible. Se recorta el muro bajo el
# lavamanos, de la versión ×2. El feed NO cambia: la clienta lo aprobó.
MUESTRA_STORY = {}   # ronda 5: feed y story usan el mismo zoom (MUESTRA_DE_FOTO)


SIN_LOGO = "2x/KERAZ MARMO GREY (sin logo de app).png"


def quitar_logo_de_app():
    """La foto «KERAZ MARMO GREY» de la clienta trae el destello de la app con que se generó, abajo a
    la derecha (x 1760–1856, y 1965–2076 en la ×2). Paulina 02-10: «logos de app eliminar». Se rellena
    con el mismo mueble blanco de alrededor; el original de la clienta no se toca."""
    destino = os.path.join(CLI, SIN_LOGO)
    if os.path.exists(destino): return
    import cv2
    im = np.asarray(Image.open(os.path.join(CLI, "2x/KERAZ MARMO GREY.jpg")).convert("RGB")).copy()
    x0, y0, x1, y1 = 1740, 1945, 1876, 2096
    zona = im[y0:y1, x0:x1].astype(np.float64).mean(axis=2)
    m = np.zeros(im.shape[:2], np.uint8)
    m[y0:y1, x0:x1] = (zona > np.median(zona) + 2.5).astype(np.uint8) * 255
    m = cv2.dilate(cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)), np.ones((9, 9), np.uint8))
    Image.fromarray(cv2.inpaint(im, m, 7, cv2.INPAINT_TELEA)).save(destino)


def muestras_de_foto():
    for k, (f, (x0, y0, x1, y1)) in MUESTRA_STORY.items():
        im = Image.open(os.path.join(CLI, f)).convert("RGB"); W, H = im.size
        im.crop((round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H))).save(
            os.path.join(PROD, f"muestra_cliente_{k}_story.png"))
    for k, (f, (x0, y0, x1, y1)) in MUESTRA_DE_FOTO.items():
        im = Image.open(os.path.join(CLI, f)).convert("RGB"); W, H = im.size
        im.crop((round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H))).save(
            os.path.join(PROD, f"muestra_cliente_{k}.png"))


def pieza(k, story=False, sombra=None):
    """sombra = (y del primer texto blanco, y del último): se mide en una primera pasada sin sombra."""
    t = T[k]
    blancos = []
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
    # Ronda 4: en la story la muestra va al tamaño del feed (×1,0) y con «solo un trozo» del
    # producto (zoom 0,5), para que se vea el ambiente; textos y banderola siguen a ×1,35 (R-35).
    em = 1.15 if story else e   # 1,0 dejaba la muestra tapada por la banderola (texto a ×1,35)
    zoom = 0.5 if story else 1.0
    m0 = t.get("m", [None])[0] if t.get("m") else None
    if story and k in MUESTRA_STORY: m0 = f"muestra_cliente_{k}_story.png"
    # una muestra recortada de la foto de la clienta YA es un trozo: sin zoom extra (QA ronda 4:
    # con zoom quedaban ×3–7,5 y se pixelaban)
    if m0 and m0.startswith("muestra_cliente_"): zoom = 1.0
    centro = None
    if k in DETALLE:
        zoom, *centro = DETALLE[k][1 if story else 0]
    fr = t.get("frase")
    cap_fr = 26 * e
    h_fr = (cap_fr + (len(fr) - 1) * cap_fr * 1.55) if fr else 0
    # extensión vertical del bloque, relativa a y_m (para centrarlo en la story)
    if t.get("urban"):
        top, fondo_m = -116 * e, 123 * (1.2 if story else e) + 32.5 * e
    elif t.get("cuadrada"):
        top, fondo_m = -40 * em, -40 * em + 250 * em
    else:
        top, fondo_m = -14 * e, 190 * em
        if fr: top = -14 * e - 34 * e - h_fr - 50 * e - 20 * e - 12 * e
        elif t.get("sello"): top = -150 * e - 12 * e
    abajo = fondo_m + 42 * e + (91 * e if (t["apo"] and t["apo"] != CTA) else 0) + 42 * e
    if story:
        abajo += 80 + CAP_PIE_STORY * 1.75 + CAP_PIE_STORY
        # Ronda 4: «centra el bloque de contenido» → el centro del bloque cae en el centro del cuadro
        y_m = 960 - (top + abajo) / 2 + AJUSTE_STORY.get(k, 0)
    # degradado muy suave detrás del bloque de texto; la muestra se dibuja encima y no se toca
    if sombra:
        sombra_desde_abajo(L, sombra[0], sombra[1], 260 if story else 170)
    if story:
        L.bloque_logo(story=True, h=ALTO_BLOQUE_STORY)
    else:
        L.bloque_logo(cx=540)                # ronda 4, punto 2: «solo centra el logo»

    y = y_m
    if fr:
        # «EN OFERTA» arriba, la frase al medio y la banderola abajo: la frase separa los dos rojos (R-05)
        y_fr = y - 14 * e - 34 * e - h_fr
        blancos.append(y_fr)
        frase(L, fr, y_fr, cap_fr, e)
        L.barra(t["sello"], y_fr - 50 * e - 20 * e, 20 * e, peso=775, tracking=0.04, padx=20 * e, padv=12 * e)
    elif t.get("sello"):
        # separada ≥ 90 de la banderola: dos cuadros rojos pegados rompen la regla R-05 de Paulina
        L.barra(t["sello"], y - 150 * e, 20 * e, peso=775, tracking=0.04, padx=20 * e, padv=12 * e)

    if t.get("urban"):
        a, b = t["urban"]
        eu = 1.2 if story else e                 # Urban: escala de la ronda 3; con 1,0 los nombres de color no se leían
        k_cm = 2.05 * eu  # misma escala en las 3 tarjetas: se ve crecer el formato
        w, h = b * k_cm, a * k_cm
        gap = 22 * eu
        tot = 3 * w + 2 * gap
        x = 540 - tot / 2
        fila = 123 * eu
        # nota: los nombres de color y la banderola siguen a escala e (texto de story, R-35)
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
            blancos.append(y + fila + 20 * e)
            x += w + gap
        # banderola centrada sobre la fila, con aire: no pisa ninguna muestra
        bw = max(251 * e, L.ancho(t["tit"].upper(), L.cuerpo_para_cap(13 * e, 700), 700, 0.01) + 48 * e)
        banderola(L, t["cat"], t["tit"], t["baj"], 540 + bw / 2, y - (26 + 90) * e, e)
        y = y + fila + (20 + 12.5) * e
        rojo_fin = -1e9
    elif t.get("cuadrada"):
        mw = mh = 250 * em
        mx = 540 - mw / 2 - 120 * e
        muestra(L, m0, mx, y - 40 * em, mw, mh, zoom=zoom)
        _, rojo_fin = banderola(L, t["cat"], t["tit"], None, mx + mw + 250 * e, y + 60 * em, e)
        y = y - 40 * em + mh
    else:
        # 06 no tiene foto de producto: la muestra es un recorte PROVISORIO del ambiente
        # generado (los adoquines apilados, que muestran los dos espesores). Paulina 29-09:
        # «faltó la muestra del producto».
        archivo = m0
        mw, mh = ((440, 220) if archivo.startswith("PROVISORIO") else (530, 190))
        mw, mh = mw * em, mh * em
        mx = 540 - mw / 2
        muestra(L, archivo, mx, y, mw, mh, zoom=zoom, centro=centro)
        _, rojo_fin = banderola(L, t["cat"], t["tit"], t["baj"], mx + mw - 23 * e, y - 14 * e, e)
        y = y + mh

    y += 42 * e
    if t["apo"] and t["apo"] != CTA:
        blancos.append(y)
        L.filete(y, ancho=560 * e, grosor=1.3 * e)
        y = apoyo(L, t["apo"], y + 24 * e, cap=17 * e) + 24 * e
        L.filete(y, ancho=560 * e, grosor=1.3 * e)
        y += 26 * e
    y = cta(L, y, cap=15.5 * e, e=e, gris=(y - rojo_fin) < 40 * e)
    if story:
        blancos += [y + 80 - 22, pie2(L, y + 80, cap=CAP_PIE_STORY)]
    else:
        # ronda 6: el pie sigue al botón (antes fijo en 1010 y quedaba suelto); tope 1010 por el respiro al borde
        yp = min(1010, y + 70)
        pie(L, yp)
        blancos += [yp - 16, yp + 12]
    L.sombra = (min(blancos), max(blancos))
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("que", nargs="*", default=[])
    ap.add_argument("--solo-feed", action="store_true")
    a = ap.parse_args()
    quitar_logo_de_app()
    muestras_de_foto()
    ks = [k for k in T if not a.que or any(k.startswith(q.upper()) for q in a.que)]
    for k in ks:
        for story in ([False] if a.solo_feed else [False, True]):
            amb = os.path.join(CLI, T[k]["foto"])
            if not os.path.exists(amb):
                print(f"· {k} {'story' if story else 'feed'}: falta {T[k]['foto']}"); continue
            L = pieza(k, story, sombra=pieza(k, story).sombra)   # 1ª pasada: mide dónde está el texto blanco
            nombre = f"REVEX_P{k}_{'Story_2250x4000' if story else 'Feed_2250x2250'}.png"
            print("✓", L.guardar(os.path.join(OUT, nombre)))


if __name__ == "__main__":
    main()

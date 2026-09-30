#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAVA · Cyber Wine Week octubre 2026 — las 12 piezas.

6 mails verticales (tamaño historia) + 6 cuadradas para las plantillas de
WhatsApp/ManyChat. Los textos salen LITERALES del brief
«CAVA _ Briefs Cyber octubre 2026.xlsx» (pestañas MAILS MAILCHIMP | OCTUBRE y
WHATSAPP | OCTUBRE): no se inventa un CTA ni un claim.

    python3 scripts/cava-cyber-oct-piezas.py            # todo
    python3 scripts/cava-cyber-oct-piezas.py wsp1       # una

Los briefs 1–3 son PREVIA VIP (cupón CYBERVIP, 45 % OFF) y salen del KV VIP.
Los briefs 4–6 son CYBER PÚBLICO (hasta 50 % OFF, sin cupón) y salen del KV
público. El brief lo dice y el KV manda.

La maqueta está calcada del editable del Cyber pasado (CYBER_CAVA.ai): la
vertical de la mesa 21/26 y la cuadrada de la mesa 24 — botella a un lado,
columna de mensaje al otro.
"""
import sys
import pathlib

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cava_cyber_oct import (  # noqa: E402
    ESC, ESCRITORIO, LOCKUP, u, fondo, escena_montada, viñeta, marco, advertencia,
    logo, lockup, losa,
    banda_gancho, cupon, botella, sello, guarda, fuente, mide,
    texto_oro, texto_plano, _cuerpo_para_cap, _cuerpo_para_ancho, BLANCO,
)

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "out/cava/cyber-octubre"
GRIS = (206, 200, 192)

# ── Los packshots oficiales que Coni dejó en BRIEF/KV ───────────────────────
# Viven versionados en el repo: hoy sólo existían en su escritorio y sin ellos
# otro diseñador no reproduce la entrega — se cae al packshot chico del
# e-commerce (800–1000 px) y la etiqueta deja de leerse.
BT = RAIZ / "public/assets/cava/bottles/oficiales"
BOTELLAS = {
    "ranquil": BT / "BottleShot_Morande_CabernetRanquil (Cap 42).png",
    "house": BT / "MOR_HOUSE_.png",
    "enologica_ca": BT / "BottleShot_Morande_SeleccionEnologica_CA.png",
    "enologica_cs": BT / "BottleShot_Morande_SeleccionEnologica_CS.png",
    "7c_gran_reserva": BT / "BTT_7_COLORES_GRAN_RVA CA_VI_VINTAGE.png",
    "vitis_carmenere": BT / "BottleShot Vitis Unica CR (Maipo).png",
    "charmat": BT / "BottleShot_Morande_ExtraBrut Charmat SINGOTAS.png",
    # Estas tres no estaban en BRIEF/KV. Salen de los packshots del catálogo que
    # ya vivían en el repo, en su versión 1x.
    #
    # ⛔ NO se usa la carpeta `2x/`: esas son upscales de precisión y el modelo
    #    REESCRIBIÓ las etiquetas. En el 7Colores dejó «SINGLE VIN5CI80»,
    #    «WIRE06 CHILE» y el sello como «IAMESSOCKLIHG.COM». Las 1x traen el
    #    texto real y, al tamaño al que se entregan (la botella mide ~450 px en
    #    el PNG final), sobra resolución.
    "7c_single": RAIZ / "public/assets/cava/bottles/7colores-single-vineyard-red-blend.png",
    "vitis_cabernet": RAIZ / "public/assets/cava/bottles/vitis-unica-cabernet.png",
    "vinedos_carmenere": RAIZ / "public/assets/cava/bottles/seleccion-vinedos-gr-carmenere.png",
}

# ── Los 6 envíos, textuales del brief ───────────────────────────────────────
PIEZAS = [
    # El brief dice «ACCESO VIP AL CYBER», pero el gancho entra directo al logo
    # CYBERWINE week: dejarlo completo repetía «CYBER» dos veces seguidas. Coni
    # quitó la palabra el 30-09 y la frase sigue cerrando contra el logo.
    dict(n=1, escena="vip", fin=0.850, tope=790, borde=0.889, vert=0.14, zoom=1.16, gancho="ACCESO VIP AL",
         titular="45% OFF", bajada="ANTES QUE NADIE", cupon="CYBERVIP",
         producto=["MORANDÉ EL CABERNET", "DE RANQUIL 2021"],
         botella="ranquil", oferta="$34.970", normal="$59.990",
         sellos=["descorchados-98-2021", "james-suckling-98"],
         # Dónde caen los sellos ahora que la botella viene en el montaje: se
         # ubican a mano sobre el hombro, del lado libre. Antes colgaban del
         # bbox del packshot, que ya no se pega.
         # Sobre el CUELLO, sin bajar a la etiqueta: la etiqueta del Ranquil
         # arranca al 42 % del alto del montaje.
         sellos_en=(0.822, 0.322), sellos_diam=152, sellos_paso=0.049,
         legal="Cupón CYBERVIP válido del 1 al 4 de octubre de 2026. "
               "No acumulable con otras promociones. Hasta agotar stock."),
    # Sin bajada: el brief dice «HOUSE OF MORANDÉ A $46.630», pero el nombre del
    # vino y su precio ya van más abajo en la pieza. Coni la quitó el 30-09.
    dict(n=2, escena="vip", fin=0.735, tope=790, borde=0.889, vert=0.0, zoom=1.16,
         alto_img=0.87, baja=12,
         gancho="TU CUPÓN VIP SIGUE ACTIVO",
         titular="45% OFF", bajada=None, cupon="CYBERVIP",
         producto=["HOUSE OF MORANDÉ", "MEZCLAS TINTAS 2021"],
         botella="house", oferta="$46.630", normal="$84.790", sellos=[],
         legal="Cupón CYBERVIP válido del 1 al 4 de octubre de 2026. "
               "No acumulable con otras promociones. Hasta agotar stock."),
    dict(n=3, escena="vip", fin=0.88, tope=545, gancho="ÚLTIMO DÍA VIP",
         titular="45% OFF", bajada="SE DESACTIVA MAÑANA", cupon="CYBERVIP",
         producto=["MORANDÉ SELECCIÓN ENOLÓGICA", "CARMENERE Y CABERNET SAUVIGNON"],
         botella="enologica_ca", botella2="enologica_cs",
         oferta="$9.340", normal="$16.990", sellos=[],
         legal="Cupón CYBERVIP válido del 1 al 4 de octubre de 2026. "
               "No acumulable con otras promociones. Hasta agotar stock."),
    dict(n=4, escena="pub", fin=0.88, tope=385, gancho=None,   # el KV público no lleva bajada sobre el lockup
         titular="HASTA 50% OFF", bajada="EN TUS FAVORITOS", cupon=None,
         producto=["PACK X6 7COLORES GRAN RESERVA", "CARMENERE / VIOGNIER 2023"],
         botella="7c_gran_reserva", botella2="vitis_carmenere",
         oferta="$4.290 c/u", normal="$47.340", sellos=[],
         legal="Válido del 5 al 7 de octubre de 2026 o hasta agotar stock. "
               "No acumulable con otras promociones."),
    dict(n=5, escena="pub", fin=0.9, tope=520, gancho="SE ESTÁN AGOTANDO",
         titular="50% OFF", bajada="SOLO HASTA MAÑANA", cupon=None,
         producto=["PACK X6 7COLORES SINGLE", "VINEYARD RED BLEND 2022"],
         botella="7c_single", botella2="vitis_cabernet",
         oferta="$5.490 c/u", normal="$71.940",
         # Sin discos: el packshot oficial YA trae quemados los dos sellos del
         # brief —Descorchados 92 y James Suckling 91—. Superponer los míos
         # sería duplicar el mismo premio dos veces en la misma botella.
         sellos=[],
         legal="Válido del 5 al 7 de octubre de 2026 o hasta agotar stock. "
               "No acumulable con otras promociones."),
    dict(n=6, escena="pub", fin=0.92, tope=640, gancho="ÚLTIMAS HORAS DEL CYBER",
         titular="50% OFF", bajada="HOY CIERRA", cupon=None,
         producto=["PACK X6 SELECCIÓN DE VIÑEDOS", "GRAN RESERVA CARMENERE 2024"],
         botella="vinedos_carmenere", botella2="charmat",
         oferta="$4.490 c/u", normal="$53.940", sellos=[],
         legal="Válido del 5 al 7 de octubre de 2026 o hasta agotar stock. "
               "No acumulable con otras promociones."),
]


# ── Cuadrada 1:1 para la plantilla de WhatsApp ──────────────────────────────
def cuadrada(p):
    im = viñeta(fondo(p["escena"], "wsp"), 0.40)
    marco(im)
    advertencia(im)                       # ocupa x 671..1080, y 0..204

    # El logo se centra en el aire que deja la advertencia, nunca debajo de ella.
    logo(im, u(500), 44, ancho=196)
    columna_botella(im, p, cx=u(248), base_y=1002, alto=770, sellos_a="izq")

    COL = u(730)
    TOPE = 1000         # hasta dónde puede bajar el cupón, sobre el legal

    y = 214
    if p["gancho"]:
        y = banda_gancho(im, COL, y, p["gancho"], cap=27, holgura=24) / ESC + 10
    y = lockup(im, COL, y, ancho=550) / ESC + 18

    ft = fuente("xbold", _cuerpo_para_ancho("xbold", p["titular"], u(390), -0.02))
    c = texto_oro(im, (COL, u(y)), p["titular"], ft, -0.02, ancla="centro")
    if p["bajada"]:
        ftb = fuente("light", _cuerpo_para_ancho("light", p["bajada"], u(430), 0.06))
        b = texto_plano(im, (COL, c[3] + u(12)), p["bajada"], ftb, BLANCO, 0.06,
                        ancla="centro")
        y = b[3] / ESC + 22
    else:
        y = c[3] / ESC + 22

    # Mismo orden que en la vertical: oferta, nombre del vino con su precio y el
    # cupón al final.
    alto_pr = alto_bloque_producto(p, 23, 520)
    bloque_producto(im, COL, y_base=y + alto_pr, p=p, cap=23, ancho_max=520)
    if p["cupon"]:
        cupon_al_hueco(im, COL, y + alto_pr + 24, TOPE, p["cupon"], ancho_max=500)
    pie_legal(im, p, y=1030, ancho_max=980)
    return im


# ── Vertical tamaño historia ────────────────────────────────────────────────
# ── La maqueta del mail, según la ronda 2 de Coni (30-09) ───────────────────
#
#   ADVERTENCIA arriba a la derecha (ley, pegada al borde)
#   logo CAVA centrado
#   gancho + logo CYBERWINE week, centrados
#   la OFERTA y su bajada, centradas, justo debajo del logo
#   banda: la botella con sus sellos a la DERECHA
#          el nombre del vino y el precio a la izquierda, ALINEADOS A LA DERECHA
#          para que cierren contra la botella
#   el cupón al pie
#   la letra legal, en dos líneas
#
# El alto no está fijado: sale de sumar los bloques. Por eso primero se mide
# todo y después se crea el lienzo.

CAP_OFERTA, CAP_BAJADA = 126, 31
CAP_NOMBRE, CAP_PRECIO = 32, 48
CAP_LEGAL = 17               # Coni pidió agrandar la letra chica
TOPE_TRACK = 0.22            # cuánto se puede abrir una línea antes de desarmarse
ALTO_BOTELLA = 1130          # la botella manda: es la protagonista de la pieza
COL_TEXTO = 548              # dónde cierra por la derecha la columna de texto
CX_BOTELLA = 782
# Cuánto baja el bloque de texto respecto al tope de la botella. Coni: «la
# información del 45% off, la frase, el nombre y los precios, un poquito más
# abajo… a ras de la tapa de la botella». Es una fracción del alto de la
# botella, medida sobre el packshot: ahí termina la cápsula y arranca el cuello.
TEXTO_BAJO_TAPA = 0.12
# Los sellos ocupaban el 64 % del ancho de la botella y la tapaban. «Si bien es
# importante el sello porque son los premios que ha ganado el vino, es mucho más
# importante que se vea el vino».
SELLO_POR_BOTELLA = 0.138
# Dónde cae el CENTRO del primer sello, en fracción del alto de la botella.
# El tope es la etiqueta: medida sobre los siete packshots oficiales, la más
# alta —la Selección Enológica— arranca al 40 % del alto. Con este valor el
# segundo sello cierra en el 38 % y ninguno la toca.
SELLO_PRIMERO = 0.15
Y_LOGO, Y_GANCHO = 152, 330  # la cabecera sube: el ángulo superior izquierdo
                             # quedaba vacío con el logo centrado y más abajo
MARGEN_PIE = 92              # aire entre la letra legal y el filete dorado


def parte_oferta(titular):
    """«45% OFF» → dos líneas: la cifra arriba y OFF abajo.

    Coni el 30-09: «cuarenta por ciento arriba en una línea y abajo off. Y
    debajo de eso, antes que nadie». Sirve igual para «HASTA 50% OFF».
    """
    t = titular.strip()
    return ([t[:-3].strip(), "OFF"] if t.upper().endswith("OFF") and len(t) > 3
            else [t])


def lineas_a_plomo(im, x, y_pen, lineas, ft, paso, color=None, track=0.0, ancla="izq",
                   tracks=None):
    """Escribe varias líneas con el interlineado PAREJO.

    ⚠️ Las funciones de pintado pegan la mancha, no la caja tipográfica, así que
    repartir con un paso fijo sobre el tope de la mancha rompe el interlineado:
    «MORANDÉ EL» lleva la tilde de la É y su tinta empieza 26 px más arriba que
    «CABERNET DE», y la cola de la Q de «RANQUIL 2021» la estira 4 px por abajo.
    El bloque se veía desalineado sin que ninguna línea estuviera mal.

    Acá se reparte sobre el ORIGEN DE ESCRITURA —la línea base— y se compensa,
    línea a línea, cuánto se despega su mancha de ese origen.
    """
    y = y_pen
    for i, linea in enumerate(lineas):
        tr = tracks[i] if tracks else track
        b = mide(linea, ft, tr)
        destino = u(y) + b[1]
        if color is None:
            texto_oro(im, (x, destino), linea, ft, tr, ancla=ancla)
        else:
            texto_plano(im, (x, destino), linea, ft, color, tr, ancla=ancla)
        y += paso
    return y


def _alto_lockup(ancho):
    lg = Image.open(LOCKUP)
    return ancho * lg.height / lg.width


# El bloque de descuento se alinea con la «C» de CYBERWINE, que es el canto
# izquierdo del logo. Coni: «ubícala más hacia la izquierda, justificado ojalá
# alineado a la C». Centrado dejaba un vacío grande a su izquierda.
def x_de_la_C(cx, ancho_lockup):
    return cx - u(ancho_lockup) / 2


def _nombre_en_lineas(p, cap, ancho_max, maximo=4):
    """Parte el nombre del vino en hasta `maximo` líneas que quepan en el ancho.

    Coni: «quizás en tres líneas, no necesariamente dos, en tres líneas para que
    alcance al lado de la botella». Se busca el menor número de líneas con el
    cuerpo pedido; si no cabe, se agrega una más.

    Se admiten hasta CUATRO antes de tocar el cuerpo. Con tres, un nombre largo
    como «HOUSE OF MORANDÉ MEZCLAS TINTAS 2021» obligaba a achicar la letra y esa
    pieza quedaba con otra tipografía que el resto de la campaña.
    """
    palabras = " ".join(p["producto"]).split()
    ft = fuente("bold", _cuerpo_para_cap("bold", u(cap)))
    for n in range(1, maximo + 1):
        corte, lineas, por = [], [], len(palabras) / n
        for i in range(n):
            lineas.append(" ".join(palabras[int(round(i * por)):int(round((i + 1) * por))]))
        if all((mide(l, ft, 0.01)[2] - mide(l, ft, 0.01)[0]) <= u(ancho_max)
               for l in lineas if l):
            return [l for l in lineas if l], ft
    # no cabe ni en `maximo`: se achica el cuerpo hasta que entre
    ft = min((fuente("bold", _cuerpo_para_ancho("bold", l, u(ancho_max), 0.01))
              for l in lineas), key=lambda f: f.size)
    return [l for l in lineas if l], ft


def vertical(p):
    dobles = bool(p.get("botella2"))
    ANCHO_LOCKUP = 840

    # ── 1. medir ────────────────────────────────────────────────────────────
    # El gancho mide lo mismo que el logo: arranca en la «C» de CYBERWINE y
    # cierra al final de la «E». Coni lo pidió para el brief 2 y vale para
    # todas: dos líneas del mismo ancho leen como un bloque.
    ft_g = (fuente("light", _cuerpo_para_ancho("light", p["gancho"],
                                               u(ANCHO_LOCKUP), 0.075))
            if p["gancho"] else None)
    alto_g = (mide(p["gancho"], ft_g, 0.075)[3] - mide(p["gancho"], ft_g, 0.075)[1]) / ESC \
        if ft_g else 0
    # El descuento va apilado: la cifra arriba, OFF debajo y la bajada abajo.
    lin_of = parte_oferta(p["titular"])
    # El ancho de la columna lo dicta el MONTAJE: no puede invadir la zona donde
    # arrancan las botellas. `tope` es esa vertical, en unidades de mesa, medida
    # sobre CADA pieza ya compuesta. Se dejó como número por pieza y no como
    # fórmula: al correr el encuadre para que la botella entre entera, la escala
    # y el desplazamiento cambian de una pieza a otra y una fórmula única erraba.
    ancho_of = max(230, p["tope"] - x_de_la_C(u(540), ANCHO_LOCKUP) / ESC)
    ft_t = fuente("xbold", _cuerpo_para_cap("xbold", u(CAP_OFERTA)))
    for l in lin_of:
        ft_t = min(ft_t, fuente("xbold", _cuerpo_para_ancho("xbold", l, u(ancho_of), -0.02)),
                   key=lambda f: f.size)
    # El paso se fija por ALTURA DE MAYÚSCULA, no por cuerpo: el cuerpo arrastra
    # ascendentes y descendentes que acá no existen —son cifras y versales— y
    # dejaba las dos líneas demasiado separadas.
    paso_of = CAP_OFERTA * 1.12
    # LA CAJA INVISIBLE. Coni: «que el ancho de antes que nadie quede alineado
    # desde el 4 hasta el %, lo mismo con la palabra OFF; se debe formar como
    # una caja visualmente para que no se vea tan desordenado».
    #
    # El ancho lo pone la primera línea —la cifra— y las demás se ajustan a él:
    # las que están en el mismo cuerpo se abren con TRACKING (OFF pasa de 325 a
    # 382 ud repartiendo la diferencia entre sus dos huecos) y la frase, que es
    # de otro cuerpo, se ajusta cambiando el CUERPO. Estirar los glifos no es
    # opción: deformaría la tipografía.
    b0 = mide(lin_of[0], ft_t, -0.02)
    W_CAJA = b0[2] - b0[0]
    # ⛔ El OFF NO se estira para llenar la caja. Se probó el 30-09 —abrirlo con
    # tracking hasta el ancho de la cifra— y Coni lo bajó: la palabra se lee
    # «O F F», desarmada. Conserva su espaciado y arranca donde arranca la
    # cifra. Quien sí se ajusta al ancho de la caja es la FRASE, que al ser de
    # otro cuerpo se acomoda sin abrir las letras.
    tracks_of = [-0.02] * len(lin_of)
    sangria_of = [0.0] * len(lin_of)
    if p["bajada"]:
        ft_b = fuente("light", _cuerpo_para_ancho("light", p["bajada"], W_CAJA, 0.055))
        cb = mide(p["bajada"], ft_b, 0.055)
    else:
        ft_b, cb = None, (0, 0, 0, 0)
    # Todo el bloque del descuento se mide en el espacio del ORIGEN DE
    # ESCRITURA, que es donde se dibuja. Medir la mancha y dibujar por línea
    # base son dos rejillas distintas: mezclarlas hacía que la bajada se
    # montara encima del OFF.
    b_prim = b0
    b_ult = mide(lin_of[-1], ft_t, tracks_of[-1])
    # La bajada arranca donde TERMINA LA MANCHA de la última línea, más aire. Si
    # se reserva un hueco a ojo, «ANTES QUE NADIE» se monta sobre el OFF.
    if ft_b:
        salto_bajada = ((len(lin_of) - 1) * paso_of
                        + (b_ult[3] - cb[1]) / ESC + CAP_BAJADA * 0.75)
        alto_desc = salto_bajada + (cb[3] - b_prim[1]) / ESC
    else:
        salto_bajada = 0.0
        alto_desc = (len(lin_of) - 1) * paso_of + (b_ult[3] - b_prim[1]) / ESC

    # Todas las piezas comparten la misma maqueta: la columna de texto a la
    # izquierda y las botellas —que ya vienen en el montaje— a la derecha. Antes
    # las de dos botellas iban centradas, pero con el montaje de fondo el texto
    # les caía encima.
    ancho_texto = W_CAJA / ESC
    lineas, ft_n = _nombre_en_lineas(p, CAP_NOMBRE, ancho_texto)
    paso_n = ft_n.size / ESC * 1.34
    ft_o = fuente("xbold", _cuerpo_para_cap("xbold", u(CAP_PRECIO)))
    ft_v = fuente("light", _cuerpo_para_cap("light", u(CAP_PRECIO * 0.56)))
    co, cv = mide(p["oferta"], ft_o), mide(p["normal"], ft_v)
    alto_texto = (len(lineas) * paso_n + CAP_NOMBRE * 0.9
                  + (co[3] - co[1]) / ESC + CAP_PRECIO * 0.34 + (cv[3] - cv[1]) / ESC)

    y_gancho = Y_GANCHO
    y_lockup = y_gancho + alto_g + (16 if ft_g else 0)
    y_banda = y_lockup + _alto_lockup(ANCHO_LOCKUP) + 52
    y_oferta = y_banda + ALTO_BOTELLA * TEXTO_BAJO_TAPA
    alto_banda = max(ALTO_BOTELLA, (y_oferta - y_banda) + alto_desc + 58 + alto_texto)
    y_cupon = y_banda + alto_banda + 54
    alto_cupon = (cupon_alto(620) if p["cupon"] else 0)
    y_legal = y_cupon + alto_cupon + (58 if p["cupon"] else 10)
    ALTO = y_legal + CAP_LEGAL * 1.55 + MARGEN_PIE

    # ── 2. lienzo y fondo ───────────────────────────────────────────────────
    # El fondo es el MONTAJE: la botella ya viene parada sobre la plataforma del
    # KV. Se recorta el sobrante por la derecha para que la botella se corra a
    # ese costado y el texto tenga el suyo.
    base, k_img, x_img, y_img = escena_montada(p["n"], "mail", ALTO, fin=p["fin"],
                                    borde=p.get("borde", 0.955),
                                    vert=p.get("vert", 0.5),
                                    zoom=p.get("zoom", 1.0),
                                    alto_img=p.get("alto_img", 1.0),
                                    baja=p.get("baja", 0.0))
    im = viñeta(base, 0.22)
    marco(im)
    advertencia(im)
    CX = u(540)
    logo(im, x_de_la_C(CX, ANCHO_LOCKUP), Y_LOGO, ancho=217.4, ancla="izq")

    # ── 3. dibujar ──────────────────────────────────────────────────────────
    if ft_g:
        texto_oro(im, (CX, u(y_gancho)), p["gancho"], ft_g, 0.075, ancla="centro")
    lockup(im, CX, y_lockup, ancho=ANCHO_LOCKUP)

    # Toda la columna izquierda cierra en la MISMA vertical —descuento, bajada,
    # nombre y precios—, contra la botella. Coni: «que quede alineado a nombre
    # del vino y los precios, para que se vea mucho más armónico».
    if dobles:
        x_desc, ancla_desc = CX, "centro"
    else:
        # Toda la columna arranca en el MISMO canto izquierdo que el logo CAVA
        # MORANDÉ y que la «C» de CYBERWINE. Coni: «para que no queden los
        # elementos tan desarticulados».
        x_desc, ancla_desc = x_de_la_C(CX, ANCHO_LOCKUP), "izq"
    # El pen se retrasa lo que la mancha se despega de él, para que el bloque
    # ARRANQUE visualmente en y_oferta.
    pen = y_oferta - b_prim[1] / ESC
    for i, l in enumerate(lin_of):
        tr = tracks_of[i]
        b = mide(l, ft_t, tr)
        x = x_desc + (sangria_of[i] if ancla_desc == "izq" else 0)
        texto_oro(im, (x, u(pen + i * paso_of) + b[1]), l, ft_t, tr, ancla=ancla_desc)
    if ft_b:
        texto_plano(im, (x_desc, u(pen + salto_bajada) + cb[1]),
                    p["bajada"], ft_b, BLANCO, 0.055, ancla=ancla_desc)

    # Cierran contra la «E» de ANTES QUE NADIE, que es el canto derecho de la
    # caja. Coni: «justifícalo a la derecha».
    x_texto, ancla = x_de_la_C(CX, ANCHO_LOCKUP) + W_CAJA, "der"
    yy = y_oferta + alto_desc + 58

    yy = lineas_a_plomo(im, x_texto, yy, lineas, ft_n, paso_n, BLANCO, 0.01, ancla)
    yy += CAP_NOMBRE * 0.9
    texto_oro(im, (x_texto, u(yy)), p["oferta"], ft_o, ancla=ancla)
    yy += (co[3] - co[1]) / ESC + CAP_PRECIO * 0.34
    bv = texto_plano(im, (x_texto, u(yy)), p["normal"], ft_v, GRIS, ancla=ancla)


    ImageDraw.Draw(im).line([bv[0] - u(5), (bv[1] + bv[3]) / 2,
                             bv[2] + u(5), (bv[1] + bv[3]) / 2],
                            fill=GRIS, width=max(1, int(u(2.6))))

    if p["cupon"]:
        cupon(im, CX, y_cupon, p["cupon"], ancho=620, alto=620 / PROP_CUPON)
    # Los sellos van sobre la BOTELLA, y la botella vive en el montaje: su sitio
    # se declara en fracciones de la escena y se transforma con el mismo
    # encuadre. Así no se despegan cuando la imagen se corre.
    for i, nombre in enumerate(p.get("sellos", [])):
        px, py = p["sellos_en"]
        esc = Image.open(LOCKUP)  # sólo para tener PIL a mano
        anc_img = k_img * 1536
        sello(im, px * anc_img - x_img,
              (py + i * p["sellos_paso"]) * k_img * 2752
              - max(0, k_img * 2752 - im.height) * p.get("vert", 0.5) + y_img,
              nombre, diam=p["sellos_diam"])

    pie_legal(im, p, y=y_legal + CAP_LEGAL * 1.55, ancho_max=940, cap=CAP_LEGAL)
    return im


# ── Piezas compartidas ──────────────────────────────────────────────────────
PROP_CUPON = 675 / 345.0        # la del cupón que diseñó Coni — no se altera
GIRO_CUPON = -7.0


def cupon_alto(ancho, giro=GIRO_CUPON):
    """Alto que ocupa el troquel YA GIRADO, para poder reservarle el sitio."""
    import math
    alto = ancho / PROP_CUPON
    return alto * math.cos(math.radians(abs(giro))) + ancho * math.sin(math.radians(abs(giro)))


def cupon_al_hueco(im, cx, y, tope, codigo, ancho_max=500, giro=GIRO_CUPON):
    """Mete el cupón en el aire que queda, sin deformarlo.

    Al girarlo −7° la caja crece, así que el alto útil hay que despejarlo de
    `alto·cosθ + ancho·senθ`. Con un alto fijo el troquel se comía el nombre del
    vino en cuanto el lockup crecía.
    """
    import math
    hueco = max(0.0, tope - y - 12)
    k = math.cos(math.radians(abs(giro))) + PROP_CUPON * math.sin(math.radians(abs(giro)))
    alto = min(ancho_max / PROP_CUPON, hueco / k)
    if alto < 110:                                   # no cabe: mejor no ponerlo
        return y
    ancho = alto * PROP_CUPON
    sobra = hueco - alto * k
    return cupon(im, cx, y + sobra / 2, codigo, ancho=ancho, alto=alto, giro=giro) / ESC


SECUNDARIO = 0.88       # el brief distingue «PRODUCTO ESTRELLA» de «SECUNDARIO»


def _ancho_colocado(ruta, alto):
    """Ancho que va a ocupar ese packshot a esa altura, sin dibujarlo."""
    im = Image.open(ruta)
    b = im.convert("RGBA").split()[3].getbbox()
    return u(alto) * (b[2] - b[0]) / (b[3] - b[1])


def columna_botella(im, p, cx, base_y, alto, sellos_a="izq", hueco=16, sobre_losa=True):
    """Coloca una botella, o dos repartidas por sus anchos REALES.

    Separarlas por una fracción de la altura las montaba una encima de otra en
    cuanto una era más ancha que la otra, y los sellos que el packshot trae
    quemados quedaban tapados. Acá se miden los dos anchos y se reparte el
    conjunto; la estrella va más grande y se dibuja ÚLTIMA, así queda delante.
    """
    if not p.get("botella"):
        return
    if sobre_losa:
        # La losa va PRIMERO: la botella se para encima, no al revés.
        # El ancho se calibra contra la BOTELLA, no contra el lienzo: en el KV
        # la botella mide unas tres veces el alto de la losa. Con la losa más
        # grande el canto de piedra pesaba más que el vino.
        losa(im, cx, base_y, ancho=alto * (0.86 if p.get("botella2") else 0.65))
    if p.get("botella2"):
        a1, a2 = alto, alto * SECUNDARIO
        w1 = _ancho_colocado(BOTELLAS[p["botella"]], a1)
        w2 = _ancho_colocado(BOTELLAS[p["botella2"]], a2)
        total = w1 + w2 + u(hueco)
        botella(im, BOTELLAS[p["botella2"]], cx + total / 2 - w2 / 2, base_y, a2)
        ancla = botella(im, BOTELLAS[p["botella"]], cx - total / 2 + w1 / 2, base_y, a1)
    else:
        ancla = botella(im, BOTELLAS[p["botella"]], cx, base_y, alto)
    d = alto * SELLO_POR_BOTELLA
    for i, nombre in enumerate(p.get("sellos", [])):
        x = ancla[0] + u(d * 0.16) if sellos_a == "izq" else ancla[2] - u(d * 0.16)
        sello(im, x, ancla[1] + u(alto * SELLO_PRIMERO + i * d * 1.12), nombre, diam=d)


def _tipografia_producto(p, cap, ancho_max):
    ft = fuente("bold", _cuerpo_para_cap("bold", u(cap)))
    for linea in p["producto"]:                      # que nunca se salga del ancho
        ft = min(ft, fuente("bold", _cuerpo_para_ancho("bold", linea, u(ancho_max), 0.01)),
                 key=lambda f: f.size)
    return ft, ft.size / ESC * 1.40


def alto_bloque_producto(p, cap=30, ancho_max=600):
    """Lo que mide el bloque nombre+precio, para poder repartir el aire antes
    de dibujar nada."""
    _, paso = _tipografia_producto(p, cap, ancho_max)
    fto = fuente("xbold", _cuerpo_para_cap("xbold", u(cap * 1.7)))
    ao = mide(p["oferta"], fto)
    return len(p["producto"]) * paso + cap * 0.75 + (ao[3] - ao[1]) / ESC


def bloque_producto(im, cx, y_base, p, cap=30, ancho_max=600):
    """Nombre del vino y precio, anclados POR ABAJO.

    Anclarlo por arriba dejaba el precio encima del legal cuando el cupón crecía:
    el pie legal es la última línea de la pieza y no se puede pisar.
    """
    ft, paso = _tipografia_producto(p, cap, ancho_max)
    alto_nombre = len(p["producto"]) * paso

    fto = fuente("xbold", _cuerpo_para_cap("xbold", u(cap * 1.7)))
    ftn = fuente("light", _cuerpo_para_cap("light", u(cap * 0.9)))
    ao = mide(p["oferta"], fto); an = mide(p["normal"], ftn)
    alto_precio = (ao[3] - ao[1]) / ESC

    y = y_base - alto_precio - cap * 0.75 - alto_nombre
    for i, linea in enumerate(p["producto"]):
        texto_plano(im, (cx, u(y) + i * u(paso)), linea, ft, BLANCO, 0.01, ancla="centro")

    y += alto_nombre + cap * 0.75
    sep = u(cap * 0.55)
    x0 = cx - ((ao[2] - ao[0]) + sep + (an[2] - an[0])) / 2
    co = texto_oro(im, (x0, u(y)), p["oferta"], fto)
    cn = texto_plano(im, (co[2] + sep, co[3] - (an[3] - an[1]) - u(cap * 0.10)),
                     p["normal"], ftn, GRIS)
    ImageDraw.Draw(im).line(
        [cn[0] - u(5), (cn[1] + cn[3]) / 2, cn[2] + u(5), (cn[1] + cn[3]) / 2],
        fill=GRIS, width=max(1, int(u(2.2))))
    return y_base - alto_precio - cap * 0.75 - alto_nombre


def parte_en_dos(texto):
    """Reparte el texto en dos líneas lo más parejas posible.

    Se prueban todos los cortes y gana el que deja las dos líneas de ancho
    parecido, penalizando que la segunda quede muy corta: una línea con dos
    palabras sueltas debajo se lee como un error, no como una bajada.
    """
    palabras = texto.split()
    if len(palabras) < 4:
        return [texto]
    mejor, puntaje = None, None
    for i in range(1, len(palabras)):
        a, b = " ".join(palabras[:i]), " ".join(palabras[i:])
        desnivel = abs(len(a) - len(b))
        viuda = max(0, 3 - len(b.split())) * 22      # castigo por cola corta
        pt = desnivel + viuda
        if puntaje is None or pt < puntaje:
            mejor, puntaje = (a, b), pt
    return list(mejor)


def pie_legal(im, p, y, ancho_max=940, cap=12.5, interlinea=1.55):
    """La letra chica, SIEMPRE en dos líneas.

    En una sola línea el cuerpo se achica hasta ser ilegible en tamaño mail: es
    texto legal y tiene que poder leerse.
    """
    lineas = parte_en_dos(p["legal"])
    ft = fuente("light", _cuerpo_para_cap("light", u(cap)))
    for linea in lineas:                             # que ninguna se pase de ancho
        ft = min(ft, fuente("light", _cuerpo_para_ancho("light", linea, u(ancho_max), 0.01)),
                 key=lambda f: f.size)
    paso = ft.size / ESC * interlinea
    y0 = y - (len(lineas) - 1) * paso                # crece hacia arriba
    for i, linea in enumerate(lineas):
        texto_plano(im, (im.width / 2, u(y0 + i * paso)), linea, ft, (188, 180, 172),
                    0.01, ancla="centro")


# ── CLI ─────────────────────────────────────────────────────────────────────
def construye(clave):
    tipo, n = ("wsp", int(clave[3:])) if clave.startswith("wsp") else ("mail", int(clave[4:]))
    p = PIEZAS[n - 1]
    if not p.get("botella"):
        print(f"  ⏭  {clave}: falta el bottle shot de «{p['falta']}» — se pide, no se genera")
        return None
    im = cuadrada(p) if tipo == "wsp" else vertical(p)
    carpeta = "VIP" if p["escena"] == "vip" else "GENERAL"
    nombre = f"CYBER_CAVA_OCT_{'WSP' if tipo == 'wsp' else 'MAIL'}{p['n']}_{carpeta}.png"
    destino = SALIDA / ("whatsapp" if tipo == "wsp" else carpeta.lower()) / nombre
    kb = guarda(im, destino, tipo)
    print(f"  ✓ {destino.relative_to(RAIZ)}  ({kb:.0f} KB)")
    return destino


if __name__ == "__main__":
    claves = sys.argv[1:] or [f"wsp{i}" for i in range(1, 7)] + [f"mail{i}" for i in range(1, 7)]
    for c in claves:
        construye(c)

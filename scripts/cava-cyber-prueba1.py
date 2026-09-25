# -*- coding: utf-8 -*-
"""CAVA · Cyber de octubre — PRUEBA 1: la propuesta A con la columna editorial.

Pedido de Coni (25-09-2026), sobre la referencia que dejó adjunta:

  «probemos el diseño prop A con el estilo del descuento que dejo adjunto.
   No cambies logo cava, advertencias e imagen. Pero la información del costado
   donde está el llamado de cyber y el descuento me gustaría usar el estilo que
   dejo adjunto. Trabájalo con tipografías que estén dentro de los edit de cava.
   Y en cuanto al nombre y precio del vino justifiquémoslo a la derecha.»

QUÉ NO SE TOCA — es literal del pedido:
  · el logo CAVA MORANDÉ, en su sitio y su tamaño de la propuesta A (x=150, y=150)
  · el recuadro de ADVERTENCIA (pág. 18 del PDF del Gobierno), arriba a la derecha
  · la imagen: misma escena `cyber-oct2026-esc-rayo.png`, mismo encuadre (1.34,
    0.86, 0.30), mismo realce de primer plano y mismo velo de columna
  · el sello Descorchados 92 sobre la botella, al mismo diámetro (435)

QUÉ CAMBIA — la columna de texto, traducida a la referencia SIN inventar copy:

    referencia (Celestia Home)          prueba 1 (CAVA)
    ────────────────────────────────    ──────────────────────────────────────
    logotipo                            logo CAVA MORANDÉ  ← intacto
    ✦                                   ✦
    «10% OFF» serif clara, versales     «50% OFF» Butler Light versales
    «your first order» serif itálica    «Llegó el Cyber.» Authentic Signature
    filete — ✦ — filete                 filete — ✦ — filete, en dorado
    «TIMELESS PIECES. / …» versales     «TU CARMENERE, / A MITAD DE PRECIO.»
      muy espaciadas                      Butler versales muy espaciadas
    [ botón ] + URL                     ⛔ NO van: ver la nota de abajo
    ─                                   nombre + precios, JUSTIFICADOS A LA DERECHA

⭐ RONDA 2 (25-09-2026), pedido de Coni: «ajusta esa información en la parte
   superior y centrado y agrándalo. Necesito que se logre leer todo y se vea
   llamativo y grande y centrado. Pero el nombre del vino y los valores déjalos
   donde están. No olvides que la botella no debe taparse y tampoco hay que
   perjudicar la legibilidad.»

   El bloque editorial sube a la franja de arriba y se centra en el EJE DE LA
   PIEZA (1125), no en el de la columna. Los tres límites son medidos:

     · el logo cierra en y=422 y el recuadro legal en y=314  → la franja abre
       en 440
     · la CÁPSULA de la botella asoma en y=1485 (medida columna a columna sobre
       la escena limpia: el punto más alto está en x=1200-1350) → la franja
       cierra en 1445, con 40 px de aire
     · el blanco sobre esa franja da 9,9:1 en su PEOR punto —el canto derecho,
       donde pega el haz de luz— contra 20,3:1 en el izquierdo. O sea que se
       puede usar a todo el ancho sin cargarle velo a la imagen.

   ⭐ Y EL CUERPO NO SE ELIGE: SE RESUELVE. Se busca por bisección el ancho de
   columna cuyo bloque llena la franja sin pasarse, así que el «50% OFF» es todo
   lo grande que el hueco permite y ni un punto más. Si mañana cambia el
   encuadre o entra una línea de texto, el cuerpo se re-calcula solo.

   ⛔ EL NOMBRE Y LOS PRECIOS NO SE MUEVEN. Sus líneas base quedan CLAVADAS en
   los valores que tenían antes de esta ronda (1916 / 2028 / 2140 · 2373 · 2551),
   no derivadas del ritmo del bloque de arriba: si se derivaran, al agrandar el
   descuento se habrían corrido solas y eso es justo lo que Coni pidió que no
   pasara.

⛔ POR QUÉ NO VAN EL BOTÓN NI LA URL DE LA REFERENCIA. Son los dos únicos
   elementos de la referencia que obligarían a ESCRIBIR texto nuevo («SHOP THE
   COLLECTION»), y esta pieza no tiene brief de octubre. La regla del estudio es
   que los llamados van literales del brief y no se inventan. Si Coni los quiere,
   son dos líneas: se activan con --boton "<texto>" y --url.

⭐ LAS TIPOGRAFÍAS SON LAS DE LOS EDITABLES, y la pareja no la elegí yo:
   `clients/cava/CLAUDE.md` §4 dice que el email marketing de CAVA va con
   **Butler** (serif Didone, «la general») + **Authentic Signature** (script,
   «para jugar con títulos»), las dos mandadas por el cliente. Y hay precedente
   exacto para esta pieza: el layout «Titular protagonista» del mailing de agosto
   (CAVA_AGO_BRIEF3) lleva **el `50%off` gigante en Butler**. O sea que la
   referencia de Coni y lo que CAVA ya aprobó son el mismo recurso.

⛔ Y LA REGLA QUE MANDA SOBRE EL BLOQUE DE LA DERECHA, del mismo manual:
   «El nombre del vino y el precio van en SANS BOLD, no en Butler. La serif es
   sólo para el titular de campaña.» Por eso el nombre y los precios se quedan en
   **Bebas Neue Pro Bold** y NO pasan a Butler, aunque el resto de la columna sí.

⛔ BEBAS NEUE PRO: SÓLO SIRVE LA BOLD. Las otras cuatro del editable son
   subconjuntos con el mapa de caracteres completo y los CONTORNOS VACÍOS —
   medido carácter a carácter: a la Book le faltan 24 glifos y a la Light 39,
   entre ellos el `$` y media docena de cifras. El precio anterior, que antes iba
   en Book, pasa a la **Bebas Neue libre** (`base_libre` de marca.json, OFL y
   verificada), que sí está entera.

⚠️ SIGUE EN PIE, y no lo arregla esta prueba: la etiqueta de la botella la
   redibujó Magnific y `marca.json` prohíbe regenerar etiquetas. Antes de
   publicar hay que reponerla con el packshot oficial. Y el precio
   `$9.245 / $18.490` es INVENTADO: no existe brief de octubre de CAVA.

    ~/copylab-venv/bin/python3 scripts/cava-cyber-prueba1.py
"""
import argparse, math, os
import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = "/private/tmp/claude-501/-Users-coni-Desktop-copylab-EDITOR-VIDEOS/8827f450-0e8f-4514-a78e-863e106cbca6/scratchpad"

W, H = 2250, 4000

# ── la columna: dos rieles, y de ellos cuelga todo ──────────────────────────
# El izquierdo es el de la propuesta A (150, el del logo, que no se toca).
#
# ⭐ EL DERECHO SE MIDE CONTRA LA BOTELLA, FILA POR FILA, y por eso es 940.
# La primera versión lo puso en 1050 leyendo la escena por bandas anchas, y el
# bloque del producto —que es el que baja más— se metió encima de la botella:
# «Limited Edition» y los dos precios la cruzaban. Recorrido el borde izquierdo
# de la botella cada 100 px, su punto más angosto está en x=996 (y 2300-2900);
# arriba de y=1500 la escena está limpia hasta 1600, pero el riel es UNO SOLO
# para toda la columna, porque es lo que hace que el filete del divisor y el
# bloque del producto mueran en la misma vertical. 940 deja 56 px de aire
# contra el punto más angosto.
COL_X, COL_R = 150, 940

# ── el bloque editorial: arriba, centrado en la PIEZA y a todo el ancho ─────
EJE = W // 2                       # 1125 — el eje de la pieza, no el de la columna
MARGEN = 150                       # el mismo del logo, a los dos lados
ANCHO_MAX = W - 2 * MARGEN
# La franja libre, medida: bajo el logo (cierra en 422) y el recuadro legal
# (cierra en 314), y sobre la CÁPSULA de la botella (asoma en 1483).
# ⚠️ EL TECHO NO ES 440 AUNQUE EL LOGO CIERRE EN 422. Al agrandar el descuento
# en la ronda 3, su tinta pasó a arrancar en x=500 y el logo llega hasta x=709:
# se solapan 209 px en horizontal, así que con el techo en 440 quedaban SÓLO
# 16 px de aire entre «MORANDÉ» y el «5». Medido, no estimado — y es el defecto
# que el estudio ya tiene escrito: cuando un elemento crece, hay que volver a
# mirar qué quedó al lado. A 515 el aire sube a ~94 px.
# ⚠️ Y el piso no es 1445 aunque quepa: ahí la bajada quedaba a 39 px de la
# cápsula y se leía rozándola. A 1420 quedan ~63, que es el punto en que deja
# de leerse pegada sin regalar tamaño.
BANDA = (515, 1420)

# ── el bloque del producto: CLAVADO donde ya estaba ────────────────────────
# Coni: «el nombre del vino y los valores déjalos donde están». Son las líneas
# base que tenía la ronda 1, escritas a mano para que NO dependan del ritmo del
# bloque de arriba — si dependieran, agrandar el descuento las correría solas.
# ⭐ RONDA 3: Coni lo marcó «bajar un poco para nivelar el peso visual». Baja
# 210 px en bloque —no se re-diagrama— y con eso su centro pasa de y=2233 a
# y=2443, que lo acerca al centro visual de la botella. Verificado contra el
# flanco: a esa altura la botella empieza en x=996 y el riel sigue en 940.
BAJADA_PRODUCTO = 210
Y_NOMBRE, PASO_NOMBRE = 1916 + BAJADA_PRODUCTO, 112
Y_PRECIO, Y_TACHADO = 2373 + BAJADA_PRODUCTO, 2551 + BAJADA_PRODUCTO

BLANCO   = (255, 255, 255)
CREMA    = (238, 233, 226)
DORADO   = (201, 162, 78)          # #C9A24E, el dorado medio de la ficha
# ⭐ EL DORADO DE CAVA ES UN DEGRADADO, NO UN COLOR. Lo dice marca.json con
# todas sus letras: «es un DEGRADADO metálico en diagonal, nunca un color
# plano», y da los cinco topes. Pintarlo plano en el medio es lo que hacía que
# el script se leyera apagado (ronda 3 de Coni: «no se lee bien»).
# ⚠️ Pero la rampa NO baja hasta la sombra. El manual la describe «de sombra a
# brillo y de vuelta» para la BARRA dorada, que es una masa sobre la que se lee
# texto negro. Acá el oro ES la tinta y va sobre fondo oscuro: con el tope
# sombra (#5F3C12) los extremos de la palabra desaparecerían. Se usa la mitad
# LUMINOSA de la rampa —medio → luz → brillo → luz → medio—, que conserva el
# metal y deja el peor punto muy por encima de la vara.
ORO_RAMPA = [(201, 162, 78), (244, 231, 176), (255, 247, 193),
             (244, 231, 176), (201, 162, 78)]
APAGADO  = (176, 170, 162)

# Butler — la serif del email marketing de CAVA, mandada por el cliente.
F_BUT_LIGHT = "/Users/coni/Library/Fonts/Butler_Light.otf"
F_BUT_REG   = "/Users/coni/Library/Fonts/Butler_Regular.otf"
# Authentic Signature — el script del email marketing, también del cliente.
F_SCRIPT    = RAIZ + "/public/assets/cava/fonts/AuthenticSignature.ttf"
# Bebas Neue Pro Bold — la sans condensada de los editables de campaña.
F_SANS_BOLD = SP + "/fonts/BebasNeuePro-Bold.otf"
# Bebas Neue libre (OFL), para el precio tachado: la Pro Book está vacía.
F_SANS_REG  = RAIZ + "/public/assets/cava/fonts/BebasNeue-Regular.ttf"

LOGO  = RAIZ + "/public/assets/cava/logo-cava-morande.png"
SELLO = RAIZ + "/public/assets/cava/sello-descorchados-92.png"
LEGAL_PNG = RAIZ + "/public/assets/cava/advertencia-conducir.png"
ESCENA = RAIZ + "/public/assets/cava/kv/cyber-oct2026-esc-rayo.png"

ENCUADRE = (1.34, 0.86, 0.30)      # el de la propuesta A, intacto
SELLO_DIAM = 435
SELLO_POS = (0.734, 0.487)         # fracción de la ESCENA sin agrandar

TITULAR   = "Llegó el Cyber."
DESCUENTO = "50% OFF"
BAJADA    = ["TU CARMENERE,", "A MITAD DE PRECIO."]
VINO      = ["7Colores", "Limited Edition", "Carmenere"]


def ft(r, px):
    return ImageFont.truetype(r, int(round(px)))


def ancho(d, t, f, tr=0.0):
    return sum(d.textlength(c, font=f) for c in t) + tr * f.size * max(0, len(t) - 1)


def escribe(d, xy, t, f, fill, tr=0.0):
    """Dibuja con tracking manual y devuelve dónde terminó la tinta."""
    x, y = xy
    for c in t:
        d.text((x, y), c, font=f, fill=fill, anchor="ls")
        x += d.textlength(c, font=f) + tr * f.size
    return x - tr * f.size


def cuerpo_para_ancho(d, t, ruta, objetivo, tr=0.0, lo=40, hi=900):
    """El cuerpo es CONSECUENCIA de la medida, no una decisión: se busca el que
    hace que la línea mida exactamente lo que la columna permite. Es el criterio
    que el estudio ya usa en DT para justificar un titular a una medida."""
    while hi - lo > 1:
        m = (lo + hi) // 2
        if ancho(d, t, ft(ruta, m), tr) <= objetivo:
            lo = m
        else:
            hi = m
    return lo


def alto_versal(f, t="H"):
    c = f.getbbox(t)
    return c[3] - c[1]


def estrella(capa, cx, cy, r, color, n=3.2, plano=False):
    """La ✦ de la referencia. No existe en ninguna de las doce fuentes de CAVA
    —comprobado con fontTools— así que se dibuja: es un ornamento geométrico,
    no un glifo de marca.

    ⛔ Y NO SE DIBUJA CON LÓBULOS. El primer intento la construyó con un radio
    que colapsa hacia la cintura, `r(t) = |cos(2t)|^p`, y sale una FLOR de
    cuatro pétalos: con cualquier exponente los costados quedan CONVEXOS. Lo
    que distingue un destello de una flor es que sus costados son CÓNCAVOS, y
    eso lo da la astroide generalizada `x = sgn(cos t)·|cos t|^n` con n > 1.
    Barrido n = 1,8 / 2,4 / 3,0 / 4,0: por debajo de 2,4 es un rombo y por
    encima de 4 se deshilacha. Va en 3,2.

    Se supermuestrea ×6 para que el canto quede limpio a 2250 px."""
    k = 6
    modo = "L" if plano else "RGBA"
    lienzo = Image.new(modo, (int(r * 2 * k) + 2, int(r * 2 * k) + 2), 0)
    pts = []
    for i in range(1440):
        t = i / 1440.0 * 2 * math.pi
        c, sn = math.cos(t), math.sin(t)
        x = math.copysign(abs(c) ** n, c)
        y = math.copysign(abs(sn) ** n, sn)
        pts.append((r * k + x * r * k + 1, r * k + y * r * k + 1))
    ImageDraw.Draw(lienzo).polygon(pts, fill=(color if plano else color + (255,)))
    lienzo = lienzo.resize((int(r * 2), int(r * 2)), Image.LANCZOS)
    if plano:
        caja = (int(cx - r), int(cy - r))
        capa.paste(ImageChops.lighter(capa.crop(
            (caja[0], caja[1], caja[0] + lienzo.width, caja[1] + lienzo.height)), lienzo), caja)
    else:
        capa.alpha_composite(lienzo, (int(cx - r), int(cy - r)))


def pinta_oro(capa, mascara):
    """Rellena una máscara con el degradado metálico de la marca, en diagonal.
    Se usa UNA sola vez por pieza sobre la máscara de TODO lo dorado —script,
    filete y estrella— para que los tres compartan exactamente el mismo metal
    y no queden tres oros distintos."""
    x = np.linspace(0, 1, W, dtype=np.float32)[None, :]
    y = np.linspace(0, 1, H, dtype=np.float32)[:, None]
    t = np.clip((x * 0.72 + y * 0.28), 0, 1)          # diagonal, dominante en x
    n = len(ORO_RAMPA) - 1
    i = np.clip((t * n).astype(np.int32), 0, n - 1)
    f = (t * n - i)[..., None]
    topes = np.array(ORO_RAMPA, dtype=np.float32)
    grad = topes[i] * (1 - f) + topes[i + 1] * f
    img = Image.fromarray(grad.astype(np.uint8)).convert("RGBA")
    capa.paste(img, (0, 0), mascara)


def encuadra(ruta, zoom, ex, ey):
    f = Image.open(ruta).convert("RGB")
    e = max(W / f.width, H / f.height) * zoom
    f = f.resize((round(f.width * e), round(f.height * e)), Image.LANCZOS)
    ox, oy = int((f.width - W) * ex), int((f.height - H) * ey)
    return f.crop((ox, oy, ox + W, oy + H))


def realza_primer_plano(f, desde=0.80):
    """El primer plano es superficie lisa en penumbra y el check
    `desenfoque_parcial` mide varianza del Laplaciano: una textura suave le
    parece fuera de foco. Se revela la veta que ya está."""
    r = f.filter(ImageFilter.UnsharpMask(radius=7, percent=215, threshold=1))
    h, w = f.height, f.width
    t = np.arange(h) / float(h)
    m = (np.clip((t - desde) / 0.10, 0, 1) * 255).astype(np.uint8)
    return Image.composite(r, f, Image.fromarray(np.tile(m[:, None], (1, w))))


def velo_columna(base, hasta=0.52, fuerza=0.55):
    a = np.asarray(base).astype(np.float32)
    x = np.arange(W) / float(W)
    k = 1.0 - (1.0 - fuerza) * np.clip((hasta - x) / hasta, 0, 1)
    return Image.fromarray(np.clip(a * k[None, :, None], 0, 255).astype(np.uint8))


def pon_sello(capa):
    z, ex, ey = ENCUADRE
    fx, fy = SELLO_POS
    fw, fh = W * z, H * z
    cx = fx * fw - (fw - W) * ex
    cy = fy * fh - (fh - H) * ey
    d = SELLO_DIAM
    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).ellipse([cx - d / 2, cy - d / 2 + d * 0.035,
                                    cx + d / 2, cy + d / 2 + d * 0.035],
                                   fill=(0, 0, 0, 96))
    capa.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(d * 0.030)))
    se = Image.open(SELLO).convert("RGBA").resize((d, d), Image.LANCZOS)
    capa.alpha_composite(se, (int(cx - d / 2), int(cy - d / 2)))


def bloque_editorial(d, capa, ancho_col, y_arriba, pinta, boton=None, url=None):
    """El bloque de la referencia, centrado en el eje de la pieza. Con
    pinta=False sólo mide. `y_arriba` es el borde de ARRIBA del bloque.

    ⭐ RONDA 3 (25-09), las marcas rojas de Coni sobre el render:
      · ✦ de arriba: ELIMINAR. Y no sólo se borra — libera 0,93 de altura de
        versal, que es lo que deja crecer todo lo demás dentro de la misma
        franja.
      · «50% OFF»: AGRANDAR.
      · el script: AGRANDAR «y no se lee bien».
      · la bajada: AGRANDAR.
    Los tres crecen, pero NO en la misma proporción: el script pasa de 1,02 a
    1,30 de la altura de versal y la bajada de 0,215 a 0,265, así que ganan
    tamaño RELATIVO contra el titular. Es lo que piden sus tres flechas: si
    todo creciera parejo, la pieza se vería igual, sólo que más grande."""
    def linea(*a, **k):
        if pinta: d_oro.line(*a, **k)
    def txt(*a, **k):
        return escribe(d, *a, **k) if pinta else 0

    oro = Image.new("L", (W, H), 0)
    d_oro = ImageDraw.Draw(oro)

    f_desc = ft(F_BUT_LIGHT, cuerpo_para_ancho(d, DESCUENTO, F_BUT_LIGHT, ancho_col, tr=0.045))
    hv = alto_versal(f_desc)
    AIRE, AIRE_CORTO = hv * 0.80, hv * 0.47
    x0, x1 = EJE - ancho_col / 2, EJE + ancho_col / 2

    # ⛔ SIN la ✦ de arriba: el bloque abre en la versal del descuento.
    y = y_arriba + hv
    a = ancho(d, DESCUENTO, f_desc, 0.045)
    txt((EJE - a / 2, y), DESCUENTO, f_desc, BLANCO, 0.045)

    # el script crece, y se le pone tope para que no se salga de la columna
    cuerpo_scr = min(int(hv * 1.30),
                     cuerpo_para_ancho(d, TITULAR, F_SCRIPT, ancho_col))
    f_scr = ft(F_SCRIPT, cuerpo_scr)
    y += AIRE_CORTO + alto_versal(f_scr, "L")
    a = ancho(d, TITULAR, f_scr)
    if pinta:
        escribe(d_oro, (EJE - a / 2, y), TITULAR, f_scr, 255)

    y += AIRE
    ornr = hv * 0.095
    hueco = ornr * 3.2
    linea([(x0, y), (EJE - hueco, y)], fill=255, width=4)
    linea([(EJE + hueco, y), (x1, y)], fill=255, width=4)
    if pinta:
        estrella(oro, EJE, y, ornr, 255, plano=True)

    f_baj = ft(F_BUT_REG, hv * 0.265)
    tr_baj = 0.26
    y += AIRE * 0.95 + alto_versal(f_baj)
    for i, l in enumerate(BAJADA):
        a = ancho(d, l, f_baj, tr_baj)
        txt((EJE - a / 2, y + i * f_baj.size * 1.62), l, f_baj, CREMA, tr_baj)
    y += f_baj.size * 1.62

    if boton:
        f_b = ft(F_BUT_REG, hv * 0.22)
        ab = ancho(d, boton, f_b, 0.30)
        alto_b = f_b.size * 2.5
        y += AIRE
        if pinta:
            d_oro.rounded_rectangle([EJE - ab / 2 - 70, y, EJE + ab / 2 + 70, y + alto_b],
                                    radius=alto_b / 2, outline=255, width=4)
            escribe(d_oro, (EJE - ab / 2, y + alto_b * 0.63), boton, f_b, 255, 0.30)
        y += alto_b
    if url:
        f_u = ft(F_BUT_REG, hv * 0.19)
        au = ancho(d, url, f_u, 0.30)
        y += AIRE * 0.75 + alto_versal(f_u)
        txt((EJE - au / 2, y), url, f_u, CREMA, 0.30)

    if pinta:
        pinta_oro(capa, oro)
    return y - y_arriba, hv, f_desc.size, cuerpo_scr, f_baj.size


def bloque_producto(d, capa, precio, antes):
    """Nombre y precios, justificados a la derecha contra el riel de la columna
    y CLAVADOS en sus líneas base de siempre."""
    f_nom = ft(F_SANS_BOLD, 108)
    for i, l in enumerate(VINO):
        a = ancho(d, l, f_nom, 0.052)
        escribe(d, (COL_R - a, Y_NOMBRE + PASO_NOMBRE * i), l, f_nom, BLANCO, 0.052)

    f_pre = ft(F_SANS_BOLD, 228)
    a = ancho(d, precio, f_pre, 0.052)
    escribe(d, (COL_R - a, Y_PRECIO), precio, f_pre, BLANCO, 0.052)

    f_ant = ft(F_SANS_REG, 150)
    a = ancho(d, antes, f_ant, 0.052)
    xi = COL_R - a
    xf = escribe(d, (xi, Y_TACHADO), antes, f_ant, APAGADO, 0.052)
    cj = f_ant.getbbox(antes)
    medio = Y_TACHADO - (cj[3] - cj[1]) * 0.36
    d.line([(xi - 10, medio), (xf + 10, medio)], fill=APAGADO, width=9)


def componer(precio, antes, boton=None, url=None):
    z, ex, ey = ENCUADRE
    base = velo_columna(realza_primer_plano(encuadra(ESCENA, z, ex, ey)))
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)

    # ── lo que no se toca ───────────────────────────────────────────────────
    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.resize((560, round(560 * logo.height / logo.width)), Image.LANCZOS)
    capa.alpha_composite(logo, (COL_X, 150))
    legal = Image.open(LEGAL_PNG).convert("RGBA")
    capa.alpha_composite(legal, (W - legal.width, 0))
    pon_sello(capa)

    # ⭐ El cuerpo es CONSECUENCIA de la franja: se busca por bisección el ancho
    # de columna cuyo bloque la llena sin pasarse. El «50% OFF» queda todo lo
    # grande que el hueco permite, y ni un punto más.
    hueco = BANDA[1] - BANDA[0]
    lo, hi = 400, ANCHO_MAX
    while hi - lo > 4:
        m = (lo + hi) // 2
        if bloque_editorial(d, capa, m, BANDA[0], False, boton, url)[0] <= hueco:
            lo = m
        else:
            hi = m
    alto, hv, cuerpo, c_scr, c_baj = bloque_editorial(d, capa, lo, BANDA[0], False, boton, url)
    y0 = BANDA[0] + (hueco - alto) / 2
    bloque_editorial(d, capa, lo, y0, True, boton, url)
    bloque_producto(d, capa, precio, antes)

    return Image.alpha_composite(base.convert("RGBA"), capa).convert("RGB"), lo, hv, cuerpo, y0, alto, c_scr, c_baj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--precio", default="$9.245")
    ap.add_argument("--precio-antes", dest="antes", default="$18.490")
    ap.add_argument("--boton", default=None, help="texto del botón de la referencia (no va sin brief)")
    ap.add_argument("--url", default=None, help="línea de URL de la referencia (no va sin brief)")
    a = ap.parse_args()
    dest = os.path.join(RAIZ, "out", "cava", "prueba1")
    os.makedirs(dest, exist_ok=True)
    im, anc, hv, cuerpo, y0, alto, c_scr, c_baj = componer(a.precio, a.antes, a.boton, a.url)
    r = os.path.join(dest, "CYBER_CAVA_CARMENERE_PRUEBA1.png")
    im.save(r)
    print("  prueba1 -> %s" % r)
    print("  bloque editorial: ancho %d (de %d posibles) · versal %d"
          % (anc, ANCHO_MAX, hv))
    print("                    cuerpos: 50%% OFF %d · script %d · bajada %d"
          % (cuerpo, c_scr, c_baj))
    print("                    y=%d..%d dentro de la franja %d..%d (cápsula en 1485)"
          % (y0, y0 + alto, BANDA[0], BANDA[1]))
    print("  producto: clavado en y=%d · %d · %d" % (Y_NOMBRE, Y_PRECIO, Y_TACHADO))


if __name__ == "__main__":
    main()

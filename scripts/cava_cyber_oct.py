# -*- coding: utf-8 -*-
"""CAVA · Cyber Wine Week octubre 2026 — el motor de las piezas derivadas.

LA PIEZA MADRE ES EL KV. Coni entregó dos KV apaisados (VIP y PÚBLICO) hechos en
Illustrator sobre dos fotos de set. Todo lo que este módulo dibuja sale medido de
ahí — no de un criterio propio:

    escala .......... la mesa de trabajo es de 1080 px y se exporta a 2,0833×.
                      Es lo que explica que el logo mida 453×217 px TANTO en el
                      KV de 4040 px de ancho COMO en el cupón de 2250: Coni
                      trabaja a tamaños absolutos constantes, no a porcentajes.
    fondo ........... recorte del MISMO archivo fotográfico que enlaza su .ai
                      (7678×4771 el VIP, 8372×4631 el público). Se recorta la
                      zona limpia —cortina y mármol, sin botellas— porque las
                      botellas del set vienen quemadas en la foto y acá van los
                      packshots oficiales de cada vino.
    advertencia ..... se LEVANTA de su KV en píxeles, no se recompone. Es
                      exigencia legal y Coni pidió expresamente respetarla.
    dorado .......... degradado HORIZONTAL medido sobre su lockup: bronce a la
                      izquierda, pico champán al 18 %, y se asienta en #D69C47.
    cupón ........... calcado del que ella misma diseñó para el Black Wine
                      (KV_BLACKWINE_MAILS_kv1mail_cupon.png): 675×345 ud,
                      girado −7°, troquel dentado en los cantos cortos.
    maquetación ..... de su editable del Cyber del año pasado (CYBER_CAVA.ai,
                      32 mesas). Ella pidió guiarse por ubicación de elementos.

⛔ Las botellas y sus etiquetas no se tocan: se escalan proporcionalmente y nada
más. Si falta un bottle shot SE PIDE, no se genera.
"""
import os
import pathlib

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

Image.MAX_IMAGE_PIXELS = None

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "public/assets/fonts"
CAVA = RAIZ / "public/assets/cava"
ESCRITORIO = pathlib.Path.home() / "Desktop/CAVA OCT-CYBER"

# ── La escala del estudio ────────────────────────────────────────────────────
# Medida sobre dos piezas suyas: el logo mide 453 px de ancho en el KV exportado
# a 4040 y también en el cupón exportado a 2250. 453 / 217,4 = 2,0833.
ESC = 2.08333


def u(v):
    """Unidades de mesa (1080) → píxeles de exportación."""
    return v * ESC


# ── Lienzos ──────────────────────────────────────────────────────────────────
# El mail es vertical tamaño historia; el de WhatsApp es cuadrado, como exige la
# pestaña WHATSAPP del brief («Gráfica: CUADRADA (1:1) para cada pieza»).
# El ANCHO manda; el alto lo pone el contenido. Coni el 30-09: «tiene que
# mantenerse en 1080 de ancho y de alto puede ir variando, depende de la
# información». Un mail no se lee de un vistazo como una historia: puede correr.
ANCHO = {"mail": 2250, "wsp": 2250}
LIENZOS = {"wsp": (2250, 2250)}          # la de WhatsApp sí es 1:1 fija
# Lo que se entrega: nítido pero liviano, porque sube a plataforma.
# Tamaño de historia exacto. Se subió a 1350/1440 creyendo que la cursiva Amalfi
# Coast se perdía a 1080, pero el garabato venía de un recorte de la máscara, no
# de la resolución: arreglado eso, a 1080 lee perfecta y el archivo pesa un
# tercio menos. Entre dos entregas que se ven igual, gana la liviana.
ENTREGA = {"mail": 1080, "wsp": 1080}    # ancho de entrega; el alto sale de él

# ── Fondos: los archivos que enlaza su .ai ───────────────────────────────────
SET = {
    "vip": ESCRITORIO / "BRIEF/KV/REFERENCIA FOTO VIP/SyWcSOtUb8.jpg",
    "pub": ESCRITORIO / "BRIEF/KV/REFERENCIA FOTO PUBLICO/ks3R7kV16B.jpg",
}
# Dónde se recorta la foto ORIGINAL. Se elige la zona limpia —cortina y mármol,
# a la izquierda del set— porque las botellas del bodegón vienen quemadas en la
# foto y acá van los packshots oficiales encima.
#   eje    = centro horizontal del recorte, en px de la foto
#   franja = (y0, y1) de la foto que se usa
RECORTE = {
    ("vip", "mail"): {"eje": 1902, "franja": (0, 4771)},
    ("vip", "wsp"): {"eje": 1760, "franja": (900, 4300)},
    ("pub", "mail"): {"eje": 2102, "franja": (0, 4631)},
    ("pub", "wsp"): {"eje": 2050, "franja": (800, 4200)},
}

ADVERTENCIA = CAVA / "cyber-oct/advertencia-kv-oct.png"
LOGO = CAVA / "logo-cava-morande.png"

# ── El dorado, medido sobre el lockup del KV ─────────────────────────────────
# Es un degradado HORIZONTAL. La regla dura de la marca dice «el dorado es
# degradado metálico, no color plano»: pintarlo plano fue el error del 25-09 que
# dejó la cursiva ilegible.
ORO = [
    (0.00, (176, 131, 52)),
    (0.06, (224, 201, 138)),
    (0.18, (255, 247, 195)),
    (0.30, (255, 243, 181)),
    (0.42, (255, 234, 154)),
    (0.52, (253, 218, 106)),
    (0.62, (240, 198, 95)),
    (0.72, (224, 172, 80)),
    (0.80, (214, 156, 71)),
    (1.00, (214, 156, 71)),
]
BLANCO = (255, 255, 255)
TINTA = (12, 10, 10)          # el negro del texto sobre dorado, del cupón

F = {
    "light": FUENTES / "Poppins-Light.ttf",
    "reg": FUENTES / "Poppins-Regular.ttf",
    "med": FUENTES / "Poppins-Medium.ttf",
    "semi": FUENTES / "Poppins-SemiBold.ttf",
    "bold": FUENTES / "Poppins-Bold.ttf",
    "xbold": FUENTES / "Poppins-ExtraBold.ttf",
    "script": ESCRITORIO / "CYBER_CAVA_OCT_Carpeta/Fonts/Amalfi Coast.ttf",
}


def fuente(peso, cuerpo):
    return ImageFont.truetype(str(F[peso]), int(round(cuerpo)))


# ── Medición real de la tinta ────────────────────────────────────────────────
# getbbox() de PIL devuelve la caja tipográfica, no la mancha. Para cuadrar un
# titular con el de otra persona hay que RENDERIZAR y umbralizar: fue lo que el
# 25-09 hizo cuadrar la cursiva de Coni al píxel.
def _lienzo_texto(texto, ft, track=0.0):
    """Lienzo con margen sobrado a los cuatro lados, y dónde quedó el origen.

    Un solo sitio decide el margen. Cuando `mide()` y la máscara del pintado lo
    calculaban por su cuenta, terminaron discrepando: la medición recortaba la
    cola de la cursiva 53 px y devolvía una mancha más baja que la que después
    se pintaba.
    """
    m = int(ft.size * 2.5) + 200
    w = int(_ancho(texto, ft, track)) + m * 2
    h = int(ft.size * 4.5) + m * 2
    im = Image.new("L", (w, h), 0)
    _escribe(ImageDraw.Draw(im), (m, m), texto, ft, 255, track)
    return im, m


def mide(texto, ft, track=0.0):
    """Mancha real del texto, en coordenadas relativas al origen de escritura.

    Puede devolver x0 o y0 NEGATIVOS: Amalfi Coast entra con salida negativa y
    su mancha empieza a la izquierda del origen. Quien pinte tiene que contar
    con eso o le corta el arranque a la letra.
    """
    im, m = _lienzo_texto(texto, ft, track)
    b = im.getbbox()
    return (0, 0, 0, 0) if b is None else (b[0] - m, b[1] - m, b[2] - m, b[3] - m)


def _escribe(dr, xy, texto, ft, fill, track=0.0):
    """Dibuja con tracking en em. PIL no lo trae: se avanza glifo a glifo."""
    if not track:
        dr.text(xy, texto, font=ft, fill=fill)
        return
    x, y = xy
    paso = track * ft.size
    for ch in texto:
        dr.text((x, y), ch, font=ft, fill=fill)
        x += dr.textlength(ch, font=ft) + paso


def _ancho(texto, ft, track=0.0):
    im = Image.new("L", (10, 10))
    dr = ImageDraw.Draw(im)
    w = dr.textlength(texto, font=ft)
    return w + track * ft.size * max(0, len(texto) - 1)


# ── Dorado ───────────────────────────────────────────────────────────────────
def rampa_oro(w, h):
    """Degradado metálico horizontal, del ancho que se le pida."""
    w = max(1, int(w))
    xs = np.linspace(0, 1, w)
    col = np.zeros((w, 3))
    ps = [p for p, _ in ORO]
    for c in range(3):
        col[:, c] = np.interp(xs, ps, [rgb[c] for _, rgb in ORO])
    return Image.fromarray(np.tile(col.astype(np.uint8), (max(1, int(h)), 1, 1)))


def _mascara(texto, ft, track=0.0):
    """Máscara del texto recortada a su mancha, sin cortarlo por ningún lado.

    ⚠️ Se dibuja con MARGEN a los cuatro lados y recién después se recorta. La
    «w» de Amalfi Coast entra con salida negativa —su mancha empieza 21 px a la
    IZQUIERDA del origen a cuerpo 300—, así que dibujarla pegada a x=0 le comía
    el arranque y «week» salía cortada. Lo mismo vale para cualquier cursiva o
    itálica que se use más adelante.
    """
    mask, _ = _lienzo_texto(texto, ft, track)
    b = mask.getbbox()
    return None if b is None else mask.crop(b)


def texto_oro(lienzo, xy, texto, ft, track=0.0, ancla="izq"):
    """Escribe con el degradado metálico. Devuelve la caja de tinta."""
    mask = _mascara(texto, ft, track)
    if mask is None:
        return None
    oro = rampa_oro(mask.width, mask.height)
    x, y = _ancla(xy, mask.size, ancla)
    lienzo.paste(oro, (int(x), int(y)), mask)
    return (int(x), int(y), int(x) + mask.width, int(y) + mask.height)


def texto_plano(lienzo, xy, texto, ft, color, track=0.0, ancla="izq"):
    mask = _mascara(texto, ft, track)
    if mask is None:
        return None
    x, y = _ancla(xy, mask.size, ancla)
    lienzo.paste(Image.new("RGB", mask.size, color), (int(x), int(y)), mask)
    return (int(x), int(y), int(x) + mask.width, int(y) + mask.height)


def _ancla(xy, tam, ancla):
    x, y = xy
    w, h = tam
    if ancla == "centro":
        x -= w / 2
    elif ancla == "der":
        x -= w
    return x, y


# ── Fondo ────────────────────────────────────────────────────────────────────
def fondo(escena, formato, alto_ud=None):
    """Recorta el set a la proporción que pida la pieza.

    Como el alto es variable, la ventana no puede estar escrita a mano: se fija
    el eje y la franja de la foto y el ANCHO del recorte se despeja de la
    proporción pedida. Así el encuadre del set es el mismo en todas las piezas,
    corran lo que corran.
    """
    W = ANCHO[formato]
    H = LIENZOS[formato][1] if formato in LIENZOS else int(round(u(alto_ud)))
    r = RECORTE[(escena, formato)]
    fy0, fy1 = r["franja"]
    foto = Image.open(SET[escena]).convert("RGB")
    ancho_rec = (fy1 - fy0) * W / H
    x0 = r["eje"] - ancho_rec / 2
    x0 = max(0, min(x0, foto.width - ancho_rec))     # sin salirse de la foto
    im = foto.crop((int(x0), fy0, int(x0 + ancho_rec), fy1))
    return im.resize((W, H), Image.LANCZOS)


def viñeta(im, fuerza=0.35):
    """Oscurece los bordes para que la tipografía respire, como en el KV."""
    W, H = im.size
    yy, xx = np.mgrid[0:H, 0:W]
    cx, cy = W / 2, H / 2
    r = np.sqrt(((xx - cx) / cx) ** 2 + ((yy - cy) / cy) ** 2) / np.sqrt(2)
    k = np.clip(1 - fuerza * np.clip(r - 0.35, 0, None) / 0.65, 0, 1)
    a = np.asarray(im).astype(float) * k[..., None]
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))


# ── Piezas fijas ─────────────────────────────────────────────────────────────
def marco(im, inset=16, grosor=3):
    """El filete dorado. inset y grosor en unidades de mesa."""
    W, H = im.size
    i, g = int(u(inset)), max(1, int(u(grosor)))
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dr = ImageDraw.Draw(capa)
    dr.rectangle([i, i, W - 1 - i, H - 1 - i], outline=(198, 156, 82, 150), width=g)
    im.paste(Image.alpha_composite(im.convert("RGBA"), capa).convert("RGB"), (0, 0))
    return im


def advertencia(im, ancho=408.5):
    """Se pega tal cual salió de su KV: la ley no se recompone.

    Una sola por pieza — las cuatro advertencias de la Ley 19.925 son
    alternativas y no se suman.
    """
    adv = Image.open(ADVERTENCIA).convert("RGB")
    w = int(u(ancho))
    h = int(round(w * adv.height / adv.width))   # proporción intacta
    im.paste(adv.resize((w, h), Image.LANCZOS), (im.width - w, 0))
    return (im.width - w, 0, im.width, h)


def logo(im, cy_x, y, ancho=217.4):
    lg = Image.open(LOGO).convert("RGBA")
    w = int(u(ancho))
    h = int(round(w * lg.height / lg.width))
    lg = lg.resize((w, h), Image.LANCZOS)
    im.paste(lg, (int(cy_x - w / 2), int(u(y))), lg)
    return (int(cy_x - w / 2), int(u(y)), int(cy_x + w / 2), int(u(y)) + h)


# ── El lockup CYBERWINE week ─────────────────────────────────────────────────
LOCKUP = CAVA / "cyber-oct/lockup-cyberwine-week.png"


def lockup(im, cx, y_top, ancho, margen=26):
    """El logo CYBERWINE week: se COPIA del editable, no se recompone.

    Lo tenía reconstruido con las fuentes y salía distinto —Coni lo escribió en
    Poppins **Bold**, no ExtraBold, y con un tracking cerrado que yo no tenía—,
    así que cada pieza llevaba una versión ligeramente propia de su logo. Ahora
    es el dibujo de ella, levantado del .ai con scripts/cava-cyber-oct-extraer.py
    (y sin el filete: pidió que no vaya en ninguna pieza).

    Devuelve la y de la base.
    """
    lg = Image.open(LOCKUP).convert("RGBA")
    w = int(min(u(ancho), im.width - u(margen) * 2))
    h = int(round(w * lg.height / lg.width))      # proporción intacta
    x, y = int(cx - w / 2), int(u(y_top))
    x = max(int(u(margen)), min(x, im.width - int(u(margen)) - w))
    im.paste(_reescala_rgba(lg, w, h), (x, y), _reescala_rgba(lg, w, h))
    return y + h


def _cuerpo_para_ancho(peso, texto, ancho_px, track=0.0):
    """El cuerpo que hace que la MANCHA mida ese ancho."""
    lo, hi = 8.0, 1600.0
    for _ in range(40):
        mid = (lo + hi) / 2
        ft = ImageFont.truetype(str(F[peso]), int(round(mid)))
        b = mide(texto, ft, track)
        if (b[2] - b[0]) < ancho_px:
            lo = mid
        else:
            hi = mid
    return max(8, int(round((lo + hi) / 2)))


def _cuerpo_para_cap(peso, cap_px, ref="H"):
    """Busca el cuerpo que da exactamente esa altura de mancha.

    Resolver sólo por ancho fue el error del 25-09: la cursiva salió 298 px de
    alto donde Coni la había dejado en 230. Se resuelve por ALTO.
    """
    lo, hi = 8.0, 1200.0
    for _ in range(40):
        mid = (lo + hi) / 2
        ft = ImageFont.truetype(str(F[peso]), int(round(mid)))
        b = mide(ref, ft)
        h = b[3] - b[1]
        if h < cap_px:
            lo = mid
        else:
            hi = mid
    return int(round((lo + hi) / 2))


# ⛔ El filete bajo el lockup se eliminó el 30-09 a pedido de Coni: «elimina la
# línea y eso aplica para todo. No es necesaria la línea que está debajo del
# logo Cyber Wine Week». También se borra al extraer el logo del editable.
# ── Banda dorada del gancho ──────────────────────────────────────────────────
def banda_gancho(im, cx, y, texto, cap=34, alto=None, holgura=30):
    """Pastilla dorada con el gancho en negro. Es el recurso del editable 2025."""
    ft = fuente("bold", _cuerpo_para_cap("bold", u(cap)))
    caja = mide(texto, ft, 0.01)
    tw, th = caja[2] - caja[0], caja[3] - caja[1]
    bw = int(tw + u(holgura) * 2)
    bh = int(u(alto) if alto else th + u(20) * 2)
    banda = rampa_oro(bw, bh)
    x = int(cx - bw / 2)
    yy = int(u(y))
    sombra = Image.new("RGBA", (bw + 40, bh + 40), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rectangle([20, 20, bw + 19, bh + 19], fill=(0, 0, 0, 120))
    sombra = sombra.filter(ImageFilter.GaussianBlur(14))
    im.paste(Image.alpha_composite(
        im.crop((x - 20, yy - 20, x + bw + 20, yy + bh + 20)).convert("RGBA"), sombra
    ).convert("RGB"), (x - 20, yy - 20))
    im.paste(banda, (x, yy))
    texto_plano(im, (cx, yy + (bh - th) / 2), texto, ft, TINTA, 0.01, ancla="centro")
    return yy + bh


# ── El cupón ─────────────────────────────────────────────────────────────────
def cupon(im, cx, y, codigo, encabezado="CUPÓN EXCLUSIVO:", pie=None,
          ancho=675, alto=345, giro=-7.0, dientes=16):
    """El cupón que diseñó Coni, adaptado al KV de octubre.

    Medido sobre KV_BLACKWINE_MAILS_kv1mail_cupon.png: 675×345 ud, girado −7°,
    cantos cortos dentados, filete interior negro y el código en caja alta.
    """
    S = 3  # se dibuja a 3× y se reduce: el troquel queda limpio
    W, H = int(u(ancho)) * S, int(u(alto)) * S
    diente = H / dientes / 2
    puntos = []
    puntos.append((0, 0))
    puntos.append((W, 0))
    # canto derecho dentado
    n = dientes
    for i in range(n):
        yy = H * (i + 0.5) / n
        puntos.append((W - diente, yy))
        puntos.append((W, H * (i + 1) / n))
    puntos.append((0, H))
    for i in range(n):
        yy = H * (1 - (i + 0.5) / n)
        puntos.append((diente, yy))
        puntos.append((0, H * (1 - (i + 1) / n)))

    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(puntos, fill=255)
    tk = rampa_oro(W, H).convert("RGBA")
    tk.putalpha(mask)

    # filete interior negro
    dr = ImageDraw.Draw(tk)
    m = int(u(18) * S)
    dr.rectangle([m, m, W - 1 - m, H - 1 - m], outline=TINTA + (255,), width=int(u(3) * S))

    tk = tk.resize((int(W / S), int(H / S)), Image.LANCZOS)
    dr = ImageDraw.Draw(tk)
    w, h = tk.size

    # El texto se ajusta AL TROQUEL. Escribirlo a cuerpo fijo lo desborda en
    # cuanto el cupón se achica para el formato cuadrado.
    # El contenido se arma como UN BLOQUE y se centra en el troquel. Antes cada
    # línea iba a una fracción fija del alto y entre «CUPÓN EXCLUSIVO:» y el
    # código quedaba un hueco grande: Coni pidió cerrar ese aire.
    util = w - u(18) * 2 - u(22) * 2       # dentro del filete interior
    ft_h = fuente("light", _cuerpo_para_ancho("light", encabezado, util * 0.74, 0.06))
    ft_c = fuente("xbold", _cuerpo_para_ancho("xbold", codigo, util, -0.015))
    ch, cc = mide(encabezado, ft_h, 0.06), mide(codigo, ft_c, -0.015)
    alto_h, alto_c = ch[3] - ch[1], cc[3] - cc[1]
    aire = alto_h * 0.34                   # aire entre las dos líneas, cerrado
    piezas = [(encabezado, ft_h, 0.06, ch, alto_h), (codigo, ft_c, -0.015, cc, alto_c)]
    if pie:
        ft_p = fuente("med", _cuerpo_para_ancho("med", pie, util * 0.92))
        cp = mide(pie, ft_p)
        piezas.append((pie, ft_p, 0.0, cp, cp[3] - cp[1]))

    total = sum(x[4] for x in piezas) + aire * (len(piezas) - 1)
    cursor = (h - total) / 2      # ojo: NO llamarlo `y`, que es el parámetro de
    for texto, ft, tr, caja, alto_l in piezas:   # colocación de la pieza entera
        _escribe(dr, ((w - (caja[2] - caja[0])) / 2 - caja[0], cursor - caja[1]),
                 texto, ft, TINTA + (255,), tr)
        cursor += alto_l + aire

    tk = tk.rotate(giro, Image.BICUBIC, expand=True)
    sombra = Image.new("RGBA", tk.size, (0, 0, 0, 0))
    sombra.paste((0, 0, 0, 150), (0, 0), tk.split()[3])
    sombra = sombra.filter(ImageFilter.GaussianBlur(int(u(9))))
    px, py = int(cx - tk.width / 2), int(u(y))
    base = im.crop((px, py, px + tk.width, py + tk.height)).convert("RGBA")
    base = Image.alpha_composite(base, sombra.transform(
        sombra.size, Image.AFFINE, (1, 0, -int(u(5)), 0, 1, -int(u(7)))))
    im.paste(Image.alpha_composite(base, tk).convert("RGB"), (px, py))
    return py + tk.height


# ── Botella ──────────────────────────────────────────────────────────────────
def botella(im, ruta, cx, base_y, alto, reflejo=0.30):
    """Coloca un packshot oficial.

    ⛔ Se escala PROPORCIONALMENTE y nada más: el ancho/alto final tiene que dar
    el mismo ratio que el archivo nativo. Nunca se estira, se espeja ni se
    redibuja la etiqueta.
    """
    bt = Image.open(ruta).convert("RGBA")
    bt = bt.crop(bt.split()[3].getbbox())      # recorta el aire transparente
    h = int(u(alto))
    w = int(round(h * bt.width / bt.height))   # ← la proporción nativa manda
    bt = _reescala_rgba(bt, w, h)
    x, y = int(cx - w / 2), int(u(base_y)) - h

    # Halo cálido detrás. En el set del KV la botella recibe una luz de contra
    # que la despega de la cortina; sin ella, una botella negra como la del
    # House desaparece sobre el fondo oscuro. Es ajuste de luz, no de etiqueta.
    #
    # ⚠️ La capa lleva MARGEN de tres radios de desenfoque a los cuatro lados y
    # la elipse va metida dentro de ese margen. Sin eso el desenfoque se corta
    # contra el borde de su propia capa y el halo se ve como un RECTÁNGULO
    # alrededor de la botella — que es justo lo que se coló en la primera vuelta.
    # Coni el 30-09: «no quiero que ninguna de las botellas tenga un destello o
    # halo dorado detrás porque se ve extraño, se ve un poco falso… o que sea
    # más sutil». Queda un lavado de luz ambiente, apenas: gris cálido en vez de
    # dorado, la mitad de opaco y mucho más abierto, para que la botella negra
    # siga despegando de la cortina sin que se vea un resplandor.
    _halo(im, cx, y + h * 0.52, w * 2.0, h * 1.02, radio=u(105), alfa=46,
          color=(122, 100, 88))

    # sombra de contacto — misma cocina que el halo, con su margen
    _halo(im, cx, u(base_y) - u(4), w + u(50), u(40), radio=u(15), alfa=170,
          color=(0, 0, 0))

    # reflejo sobre el mármol
    if reflejo > 0:
        rf = bt.transpose(Image.FLIP_TOP_BOTTOM)
        alto_rf = int(h * reflejo)
        rf = rf.crop((0, 0, w, alto_rf))
        a = np.asarray(rf.split()[3]).astype(float)
        fade = np.linspace(0.42, 0.0, alto_rf)[:, None]
        rf.putalpha(Image.fromarray((a * fade).clip(0, 255).astype(np.uint8)))
        rf = rf.filter(ImageFilter.GaussianBlur(int(u(2.5))))
        ry = int(u(base_y))
        reg = im.crop((x, ry, x + w, ry + alto_rf)).convert("RGBA")
        im.paste(Image.alpha_composite(reg, rf).convert("RGB"), (x, ry))

    im.paste(bt, (x, y), bt)
    return (x, y, x + w, y + h)


def _reescala_rgba(im, w, h):
    """Reescala respetando el alfa PREMULTIPLICADO.

    Varios packshots del e-commerce vienen recortados sobre BLANCO: el alfa es
    0 pero el RGB de fuera de la botella sigue siendo blanco. Si se reescala el
    RGB y el alfa por separado —que es lo que hace PIL— los píxeles del canto
    mezclan ese blanco y la botella queda con un filo claro alrededor sobre el
    fondo oscuro del KV. Premultiplicando, el canto mezcla transparencia en vez
    de blanco.
    """
    a = np.asarray(im).astype(np.float32)
    al = a[..., 3:4] / 255.0
    pre = np.concatenate([a[..., :3] * al, a[..., 3:4]], axis=2)
    pre = Image.fromarray(pre.clip(0, 255).astype(np.uint8)).resize((w, h), Image.LANCZOS)
    b = np.asarray(pre).astype(np.float32)
    al2 = np.maximum(b[..., 3:4] / 255.0, 1e-4)
    rgb = (b[..., :3] / al2).clip(0, 255)
    return Image.fromarray(np.concatenate([rgb, b[..., 3:4]], axis=2).astype(np.uint8), "RGBA")


def _halo(im, cx, cy, ancho, alto, radio, alfa=110, color=(158, 96, 44)):
    """Mancha de luz elíptica y de verdad blanda, centrada en (cx, cy).

    El margen de 3·radio es lo que evita que el desenfoque tope el borde de la
    capa: un blur truncado deja un canto recto y el halo se lee cuadrado.
    """
    r = max(1, int(radio))
    pad = r * 3
    aw, ah = int(ancho) + pad * 2, int(alto) + pad * 2
    capa = Image.new("RGBA", (aw, ah), (0, 0, 0, 0))
    ImageDraw.Draw(capa).ellipse([pad, pad, aw - 1 - pad, ah - 1 - pad],
                                 fill=color + (int(alfa),))
    capa = capa.filter(ImageFilter.GaussianBlur(r))

    hx, hy = int(cx - aw / 2), int(cy - ah / 2)
    # Recortar contra el lienzo: pedirle a PIL una región fuera de borde
    # devuelve negro y eso pintaría un bloque oscuro junto a la botella.
    x0, y0 = max(0, hx), max(0, hy)
    x1, y1 = min(im.width, hx + aw), min(im.height, hy + ah)
    if x1 <= x0 or y1 <= y0:
        return
    capa = capa.crop((x0 - hx, y0 - hy, x1 - hx, y1 - hy))
    reg = im.crop((x0, y0, x1, y1)).convert("RGBA")
    im.paste(Image.alpha_composite(reg, capa).convert("RGB"), (x0, y0))


SELLOS = {
    "descorchados-98-2021": CAVA / "sellos/descorchados-98-2021.png",
    "james-suckling-98": CAVA / "sellos/james-suckling-98.png",
}


def sello(im, cx, cy, nombre, diam=126):
    """Sello de premio: el archivo OFICIAL, colocado como gráfica plana.

    Los dibujaba yo con el puntaje que decía el brief y salían mal —Coni mandó
    los buenos, que son 98 y 98—. Un sello es una marca registrada: se pega, no
    se redibuja. Van superpuestos, sin resplandor y sin seguir la perspectiva de
    la botella.
    """
    sl = Image.open(SELLOS[nombre]).convert("RGBA")
    d = int(u(diam))
    h = int(round(d * sl.height / sl.width))
    sl = _reescala_rgba(sl, d, h)
    im.paste(sl, (int(cx - d / 2), int(cy - h / 2)), sl)


# ── Entrega ──────────────────────────────────────────────────────────────────
def guarda(im, destino, formato):
    """PNG nítido pero liviano: se baja al tamaño de entrega y se cuantiza."""
    destino = pathlib.Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    W = ENTREGA[formato]
    H = int(round(im.height * W / im.width))     # el alto sigue al ancho
    fin = im.resize((W, H), Image.LANCZOS)
    fin.save(destino, "PNG", optimize=True)

    # ⛔ NO se cuantiza a paleta para bajar el peso. Se probó el 30-09 y el motor
    # de QA lo cazó: el dithering sobre la banda tricolor del Ministerio —que son
    # 17 px de azul y rojo saturados contra una pieza oscura y dorada— la dejaba
    # en (53,84,107) y (154,49,43) en vez de #0063AF y #E73439. La franja legal
    # es lo único de la pieza que es ilegal tocar. El peso se controla con la
    # resolución de entrega, nunca con la profundidad de color.
    return os.path.getsize(destino) / 1024

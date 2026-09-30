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
LIENZOS = {
    "mail": (2250, 4000),      # 1080×1920 ud — 9:16
    "wsp": (2250, 2250),       # 1080×1080 ud — 1:1
}
# Lo que se entrega: nítido pero liviano, porque sube a plataforma.
# Tamaño de historia exacto. Se subió a 1350/1440 creyendo que la cursiva Amalfi
# Coast se perdía a 1080, pero el garabato venía de un recorte de la máscara, no
# de la resolución: arreglado eso, a 1080 lee perfecta y el archivo pesa un
# tercio menos. Entre dos entregas que se ven igual, gana la liviana.
ENTREGA = {"mail": (1080, 1920), "wsp": (1080, 1080)}

# ── Fondos: los archivos que enlaza su .ai ───────────────────────────────────
SET = {
    "vip": ESCRITORIO / "BRIEF/KV/REFERENCIA FOTO VIP/SyWcSOtUb8.jpg",
    "pub": ESCRITORIO / "BRIEF/KV/REFERENCIA FOTO PUBLICO/ks3R7kV16B.jpg",
}
# Ventanas elegidas sobre la foto ORIGINAL. Se quedan a la izquierda del set: ahí
# está la cortina y el mármol y NO hay botellas quemadas en la foto.
VENTANA = {
    ("vip", "mail"): (560, 0, 3244, 4771),
    ("vip", "wsp"): (60, 900, 3460, 4300),
    ("pub", "mail"): (800, 0, 3405, 4631),
    ("pub", "wsp"): (350, 800, 3750, 4200),
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
def mide(texto, ft, track=0.0):
    """Mancha real del texto. El lienzo se dimensiona con el CUERPO, no fijo:
    Amalfi Coast dibuja hasta 1,8 veces el cuerpo por debajo del origen y con un
    lienzo corto la cursiva se cortaba por abajo — por eso «week» salía partida
    en trazos sueltos."""
    m = int(ft.size * 2.5) + 200
    im = Image.new("L", (int(_ancho(texto, ft, track)) + int(ft.size * 3) + 400,
                         int(ft.size * 4.0) + 400), 0)
    dr = ImageDraw.Draw(im)
    _escribe(dr, (m, m), texto, ft, 255, track)
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


def texto_oro(lienzo, xy, texto, ft, track=0.0, ancla="izq"):
    """Escribe con el degradado metálico. Devuelve la caja de tinta."""
    w = int(_ancho(texto, ft, track)) + int(ft.size * 3)
    h = int(ft.size * 4.0)
    mask = Image.new("L", (w, h), 0)
    _escribe(ImageDraw.Draw(mask), (0, int(ft.size * 0.9)), texto, ft, 255, track)
    b = mask.getbbox()
    if b is None:
        return None
    mask = mask.crop(b)
    oro = rampa_oro(mask.width, mask.height)
    x, y = _ancla(xy, mask.size, ancla)
    lienzo.paste(oro, (int(x), int(y)), mask)
    return (int(x), int(y), int(x) + mask.width, int(y) + mask.height)


def texto_plano(lienzo, xy, texto, ft, color, track=0.0, ancla="izq"):
    w = int(_ancho(texto, ft, track)) + int(ft.size * 3)
    h = int(ft.size * 4.0)
    mask = Image.new("L", (w, h), 0)
    _escribe(ImageDraw.Draw(mask), (0, int(ft.size * 0.9)), texto, ft, 255, track)
    b = mask.getbbox()
    if b is None:
        return None
    mask = mask.crop(b)
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
def fondo(escena, formato):
    x0, y0, x1, y1 = VENTANA[(escena, formato)]
    W, H = LIENZOS[formato]
    im = Image.open(SET[escena]).convert("RGB").crop((x0, y0, x1, y1))
    im = im.resize((W, H), Image.LANCZOS)
    return im


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
# Relaciones medidas sobre el lockup del KV VIP: CYBERWINE mide 1519×250 px
# (x 400..1918, y 760..1009) y la cursiva «week» arranca en x 1356, y 906, con
# los ojos de las letras en 193 px de alto.
#
# ⚠️ La cursiva NO se puede dimensionar por el ancho de su mancha: el rasgo
# ascendente de la «k» se dispara y domina la caja, así que ajustar por ancho la
# deja a dos tercios del tamaño y el conjunto se vuelve un garabato. Se ancla
# por ALTURA DE OJO —la mancha de «wee»— que es lo que el ojo compara.
WEEK_OJO = 193 / 250.0      # alto de «wee» respecto a la mayúscula de CYBERWINE
WEEK_IZQ = (1356 - 400) / 1519.0    # dónde entra, sobre el ancho del titular
WEEK_TOP = (906 - 760) / 250.0      # cuánto baja, sobre la mayúscula


def lockup(im, cx, y_top, ancho):
    """CYBERWINE en Poppins ExtraBold con el degradado, y «week» en Amalfi Coast.

    Se resuelve por ANCHO, no por altura de mayúscula: en una pieza vertical la
    columna tiene un ancho dado y el titular tiene que caber en él. Devuelve la
    y de la base del conjunto.
    """
    track = -0.022
    cuerpo = _cuerpo_para_ancho("xbold", "CYBERWINE", u(ancho), track)
    ft = fuente("xbold", cuerpo)
    caja = mide("CYBERWINE", ft, track)
    b = texto_oro(im, (cx - (caja[2] - caja[0]) / 2, u(y_top)), "CYBERWINE", ft, track)
    cw, cap = b[2] - b[0], b[3] - b[1]

    fts = fuente("script", _cuerpo_para_cap("script", cap * WEEK_OJO, ref="wee"))
    xs = b[0] + cw * WEEK_IZQ
    ys = b[1] + cap * WEEK_TOP
    # La cursiva monta sobre el dorado de WINE: blanco sobre dorado no contrasta.
    # Una sombra suave la despega sin cambiar el dibujo del KV.
    _sombra_texto(im, (xs, ys), "week", fts, radio=cw * 0.012)
    bs = texto_plano(im, (xs, ys), "week", fts, BLANCO)
    return max(b[3], bs[3] if bs else b[3])


def _sombra_texto(im, xy, texto, ft, radio, alfa=190):
    w = int(_ancho(texto, ft)) + int(ft.size * 3)
    h = int(ft.size * 4.0)
    mask = Image.new("L", (w, h), 0)
    _escribe(ImageDraw.Draw(mask), (0, int(ft.size * 0.9)), texto, ft, 255)
    b = mask.getbbox()
    if b is None:
        return
    mask = mask.crop(b)
    r = max(1, int(radio))
    capa = Image.new("RGBA", (mask.width + r * 6, mask.height + r * 6), (0, 0, 0, 0))
    capa.paste((0, 0, 0, alfa), (r * 3, r * 3), mask)
    capa = capa.filter(ImageFilter.GaussianBlur(r * 1.6))
    x, y = int(xy[0]) - r * 3, int(xy[1]) - r * 3
    reg = im.crop((x, y, x + capa.width, y + capa.height)).convert("RGBA")
    im.paste(Image.alpha_composite(reg, capa).convert("RGB"), (x, y))


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


def hairline(im, cx, y, ancho, grosor=1.6):
    w = int(u(ancho))
    h = max(1, int(u(grosor)))
    im.paste(rampa_oro(w, h), (int(cx - w / 2), int(u(y))))


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
    util = w - u(18) * 2 - u(26) * 2       # dentro del filete interior, con aire
    ft_h = fuente("light", _cuerpo_para_ancho("light", encabezado, util * 0.80, 0.06))
    ch = mide(encabezado, ft_h, 0.06)
    _escribe(dr, ((w - (ch[2] - ch[0])) / 2 - ch[0], h * 0.135 - ch[1]),
             encabezado, ft_h, TINTA + (255,), 0.06)

    ft_c = fuente("xbold", _cuerpo_para_ancho("xbold", codigo, util, -0.015))
    cc = mide(codigo, ft_c, -0.015)
    _escribe(dr, ((w - (cc[2] - cc[0])) / 2 - cc[0],
                  h * (0.62 if pie else 0.70) - (cc[3] - cc[1]) / 2 - cc[1]),
             codigo, ft_c, TINTA + (255,), -0.015)

    if pie:
        ft_p = fuente("med", _cuerpo_para_ancho("med", pie, util * 0.92))
        cp = mide(pie, ft_p)
        _escribe(dr, ((w - (cp[2] - cp[0])) / 2 - cp[0], h * 0.845 - cp[1]),
                 pie, ft_p, TINTA + (255,))

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
    bt = bt.resize((w, h), Image.LANCZOS)
    x, y = int(cx - w / 2), int(u(base_y)) - h

    # Halo cálido detrás. En el set del KV la botella recibe una luz de contra
    # que la despega de la cortina; sin ella, una botella negra como la del
    # House desaparece sobre el fondo oscuro. Es ajuste de luz, no de etiqueta.
    hw, hh = int(w * 2.1), int(h * 1.18)
    halo = Image.new("RGBA", (hw, hh), (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse([0, 0, hw - 1, hh - 1], fill=(158, 96, 44, 120))
    halo = halo.filter(ImageFilter.GaussianBlur(int(u(60))))
    hx, hy = int(cx - hw / 2), int(y + h * 0.5 - hh / 2)
    reg = im.crop((hx, hy, hx + hw, hy + hh)).convert("RGBA")
    im.paste(Image.alpha_composite(reg, halo).convert("RGB"), (hx, hy))

    # sombra de contacto
    som = Image.new("RGBA", (w + int(u(60)), int(u(46))), (0, 0, 0, 0))
    ImageDraw.Draw(som).ellipse([0, 0, som.width - 1, som.height - 1], fill=(0, 0, 0, 165))
    som = som.filter(ImageFilter.GaussianBlur(int(u(14))))
    sx, sy = int(cx - som.width / 2), int(u(base_y) - u(20))
    reg = im.crop((sx, sy, sx + som.width, sy + som.height)).convert("RGBA")
    im.paste(Image.alpha_composite(reg, som).convert("RGB"), (sx, sy))

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


def sello(im, cx, cy, cifra, casa, diam=126):
    """Disco de premio, con la gramática del editable 2025: casa arriba, cifra
    grande y PUNTOS abajo, los tres DENTRO del disco.

    Va como gráfica plana, sin resplandor y sin seguir la perspectiva de la
    botella. El puntaje y la casa son los de ESE vino y ESA cosecha.
    """
    S = 3
    d = int(u(diam))
    capa = Image.new("RGBA", (d * S, d * S), (0, 0, 0, 0))
    dr = ImageDraw.Draw(capa)
    dr.ellipse([0, 0, d * S - 1, d * S - 1], fill=(16, 14, 14, 240))
    g = int(u(2.6) * S)
    dr.ellipse([int(u(7) * S)] * 2 + [d * S - 1 - int(u(7) * S)] * 2,
               outline=(214, 156, 71, 255), width=g)
    capa = capa.resize((d, d), Image.LANCZOS)

    util = d * 0.70
    ftc = fuente("semi", _cuerpo_para_ancho("semi", casa, util, 0.04))
    ftn = fuente("xbold", _cuerpo_para_cap("xbold", d * 0.30))
    ftp = fuente("semi", _cuerpo_para_ancho("semi", "PUNTOS", util * 0.62, 0.06))
    bc, bn, bp = mide(casa, ftc, 0.04), mide(cifra, ftn), mide("PUNTOS", ftp, 0.06)
    hc, hn, hp = bc[3] - bc[1], bn[3] - bn[1], bp[3] - bp[1]
    aire = d * 0.055
    total = hc + aire + hn + aire + hp
    y = cy - total / 2

    im.paste(capa, (int(cx - d / 2), int(cy - d / 2)), capa)
    texto_plano(im, (cx, y), casa, ftc, BLANCO, 0.04, ancla="centro")
    texto_oro(im, (cx, y + hc + aire), cifra, ftn, ancla="centro")
    texto_plano(im, (cx, y + hc + aire + hn + aire), "PUNTOS", ftp, BLANCO, 0.06,
                ancla="centro")


# ── Entrega ──────────────────────────────────────────────────────────────────
def guarda(im, destino, formato):
    """PNG nítido pero liviano: se baja al tamaño de entrega y se cuantiza."""
    destino = pathlib.Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    W, H = ENTREGA[formato]
    fin = im.resize((W, H), Image.LANCZOS)
    fin.save(destino, "PNG", optimize=True)

    # ⛔ NO se cuantiza a paleta para bajar el peso. Se probó el 30-09 y el motor
    # de QA lo cazó: el dithering sobre la banda tricolor del Ministerio —que son
    # 17 px de azul y rojo saturados contra una pieza oscura y dorada— la dejaba
    # en (53,84,107) y (154,49,43) en vez de #0063AF y #E73439. La franja legal
    # es lo único de la pieza que es ilegal tocar. El peso se controla con la
    # resolución de entrega, nunca con la profundidad de color.
    return os.path.getsize(destino) / 1024

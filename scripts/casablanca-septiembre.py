#!/usr/bin/env python3
"""PISOS CASABLANCA · Septiembre 2026 — las 14 gráficas del brief.

    python3 scripts/casablanca-septiembre.py            # todo
    python3 scripts/casablanca-septiembre.py c1 feed    # sólo una tanda

Brief: «Brief Diseño Septiembre 2026 - CASABLANCA» (Serena, 24-08-2026).
  C1 · carrusel de 4 tarjetas de producto  ×  feed 1:1 + story 9:16
  C2 · carrusel de 3 tarjetas del showroom ×  feed 1:1 + story 9:16

TODA la geometría sale de medir las piezas aprobadas de Paulina
(`clients/casablanca/medidas.json`), normalizada a 1080 y escalada al master de
2250 px que ella entrega. Acá no hay una sola cifra inventada: si un número no
está medido, está marcado como derivado y se dice de dónde sale.
"""
import os
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont
from fontTools.ttLib import TTCollection

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

RAIZ = pathlib.Path(str(_RAIZ))
ASSETS = RAIZ / "public/assets/casablanca"
FUENTES = RAIZ / "public/assets/fonts"
SALIDA = RAIZ / "out/casablanca/septiembre"
CACHE = pathlib.Path("/tmp/cb-fuentes")

# ─────────────────────────────────────────────────────────── marca
GRIS = (0x62, 0x62, 0x60)
BLANCO = (255, 255, 255)
MASTER = 2250                      # ancho de entrega (el de Paulina)
R = MASTER / 1080                  # todo se escribe en px sobre 1080
P = lambda v: int(round(v * R))


def futura():
    """Futura Medium — identificada por glifos (IoU 89,2%). Vive en el .ttc del sistema."""
    CACHE.mkdir(exist_ok=True)
    d = CACHE / "Futura_Medium.ttf"
    if not d.exists():
        for f in TTCollection("/System/Library/Fonts/Supplemental/Futura.ttc", lazy=True).fonts:
            if (f["name"].getDebugName(4) or "") == "Futura Medium":
                f.save(str(d))
    if not d.exists():
        raise SystemExit("No encuentro Futura Medium en el sistema")
    return str(d)


FT_VERSALES = None                 # se resuelve en main()
FT_SERIF = str(FUENTES / "BodoniModa-Italic.ttf")
FT_CAJA = str(FUENTES / "Montserrat.ttf")

CAP_FUTURA = 0.700                 # altura de mayúscula / cuerpo, medido


def _f(path, cuerpo, ejes=None):
    f = ImageFont.truetype(path, int(round(cuerpo)))
    if ejes:
        try:
            f.set_variation_by_axes(ejes)
        except Exception:
            pass
    return f


def _cap(path, ejes=None, letra="H"):
    f = _f(path, 400, ejes)
    bb = f.getbbox(letra)
    return (bb[3] - bb[1]) / 400


def versales(cap_1080):
    return _f(FT_VERSALES, cap_1080 * R / CAP_FUTURA)


def serif(cap_1080):
    """Bodoni Moda Italic wght 800 / opsz 18 — el mejor calce medido (77,1%)."""
    ejes = [800, 18]
    return _f(FT_SERIF, cap_1080 * R / _cap(FT_SERIF, ejes, "R"), ejes), ejes


def caja(cap_1080, peso=400):
    ejes = [peso]
    return _f(FT_CAJA, cap_1080 * R / _cap(FT_CAJA, ejes), ejes)


# ─────────────────────────────────────────────────────────── dibujo
def _ancho(d, txt, f, tr):
    return sum(d.textlength(c, font=f) for c in txt) + tr * (len(txt) - 1)


def escribe(d, txt, f, fill, cx=None, x=None, ink_top=0, tr=0.0, sombra=None):
    """Escribe alineando por el TOPE DE TINTA (no por el ascendente del cuerpo)."""
    bb = f.getbbox(txt)
    w = _ancho(d, txt, f, tr)
    x0 = (cx - w / 2) if cx is not None else x
    y0 = ink_top - bb[1]
    if sombra:
        cur = x0
        for c in txt:
            d.text((cur + sombra[0], y0 + sombra[1]), c, sombra[2], font=f)
            cur += d.textlength(c, font=f) + tr
    cur = x0
    for c in txt:
        d.text((cur, y0), c, fill, font=f)
        cur += d.textlength(c, font=f) + tr
    return w


def ajusta_tr(d, txt, f, objetivo):
    """Tracking necesario para que la línea mida `objetivo` px (sobre 1080)."""
    if len(txt) < 2:
        return 0.0
    return (P(objetivo) - sum(d.textlength(c, font=f) for c in txt)) / (len(txt) - 1)


def cover(im, w, h, foco_x=0.5, foco_y=0.5, zoom=1.0):
    """Recorte tipo object-fit: cover. `foco_x`/`foco_y` mueven el encuadre.

    `zoom` acerca antes de recortar: cuando la foto ya viene del ancho exacto del
    lienzo no queda margen para mover el encuadre, y sin él `foco_x` no hace nada.

    0.5 es centrado. Al pasar una foto horizontal a 4:5 se recorta ~20 % del ancho,
    y qué 20 % se pierde no da lo mismo: en el local de Vitacura, centrado corta el
    letrero «Pisos de Madera» y descentrado deja fuera la placa del 6359.
    """
    iw, ih = im.size
    e = max(w / iw, h / ih) * zoom
    im = im.resize((int(round(iw * e)), int(round(ih * e))), Image.LANCZOS)
    iw, ih = im.size
    x = int(round((iw - w) * min(max(foco_x, 0.0), 1.0)))
    y = int(round((ih - h) * min(max(foco_y, 0.0), 1.0)))
    return im.crop((x, y, x + w, y + h))


def velo(im, desde, hasta, alfa_max):
    """Velo NEGRO con opacidad, en degradado hacia el pie (Paulina, 25-08-2026)."""
    W, H = im.size
    capa = Image.new("L", (1, H), 0)
    px = capa.load()
    y0, y1 = int(H * desde), int(H * hasta)
    for y in range(H):
        if y <= y0:
            v = 0
        elif y >= y1:
            v = alfa_max
        else:
            v = int(alfa_max * (y - y0) / (y1 - y0))
        px[0, y] = v
    capa = capa.resize((W, H))
    im.paste(Image.new("RGB", (W, H), (0, 0, 0)), (0, 0), capa)
    return im


def _lum_rel(rgb):
    """Luminancia relativa WCAG de un color sRGB 0-255."""
    import numpy as _np
    c = _np.asarray(rgb, dtype=_np.float64) / 255.0
    c = _np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def velo_medido(im, y_top, y_bot, objetivo=5.0, tope=190, cx_libre=(0.06, 0.94)):
    """Velo cuyo alfa se MIDE para que el texto blanco alcance `objetivo`:1.

    Por qué existe: el lineamiento 5 del brief dice que el texto nunca va sobre la
    madera. Medido, el problema real no es la madera sino el CONTRASTE — con el velo
    fijo anterior la etiqueta del look daba 3,54:1, ilegible. Y un alfa fijo tampoco
    sirve, porque las cuatro maderas del carrusel son distintas: el mismo velo que
    deja bien al Roble Natural UV lleva al Cumarú a 9:1 y lo enloda.

    Así que se mide el fondo en la banda donde va el texto y se calcula el alfa justo.
    La meseta arranca antes del bloque y llega al borde inferior: contraste uniforme
    en todo el texto y ningún apagado que se vea cortado.

    Devuelve (im, alfa, contraste_logrado) para poder dejarlo en el QA.
    """
    import numpy as _np
    W, H = im.size
    a = _np.asarray(im).astype(_np.float64)
    y0, y1 = int(P(y_top)), min(H, int(P(y_bot)))
    x0, x1 = int(W * cx_libre[0]), int(W * cx_libre[1])
    fondo = a[y0:y1, x0:x1].reshape(-1, 3).mean(axis=0)
    L = float(_lum_rel(fondo))
    L_obj = 1.05 / objetivo - 0.05
    if L <= L_obj:                                  # ya es suficientemente oscuro
        alfa = 0
    else:
        f = (L_obj / L) ** (1 / 2.2)                # el velo multiplica en sRGB
        alfa = int(round(min(tope, 255 * (1 - f))))
    if alfa:
        # `velo` toma FRACCIONES del alto: sube de 0 en `desde` a `alfa` en `hasta`,
        # y de ahí al pie se mantiene. La meseta empieza 8 u sobre el bloque, con una
        # rampa de 300 u para que la entrada no se vea como una banda.
        H1080 = H / R
        hasta = (y_top - 8.0) / H1080
        desde = max(0.0, (y_top - 8.0 - 300.0) / H1080)
        im = velo(im, desde, hasta, alfa)
    fondo2 = _np.asarray(im).astype(_np.float64)[y0:y1, x0:x1].reshape(-1, 3).mean(axis=0)
    return im, alfa, float(1.05 / (_lum_rel(fondo2) + 0.05))


def tarjeta_logo(im, x, y, w, h):
    """Caja BLANCA colgando del borde superior. Medido: cx 540 · y 0 en feed y story."""
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([P(x), P(y) - P(20), P(x + w), P(y + h)],
                        radius=P(6), fill=BLANCO)
    logo = Image.open(ASSETS / "logo_gris.png").convert("RGBA")
    logo = logo.crop(logo.getbbox())
    lw = P(w * 0.72)
    lh = int(lw * logo.height / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    im.paste(logo, (P(x + w / 2) - lw // 2, P(y + h / 2) - lh // 2), logo)


def muestra_tabla(im, sku, x, y, w, h):
    """Muestra vertical del producto. Medido en las fichas de Paulina:
    139,7 × 470 sobre 1080 — el 43,5 % del alto de la pieza. Esquinas r 13."""
    tab = Image.open(ASSETS / f"muestra_{sku}.png").convert("RGB")
    tab = cover(tab, P(w), P(h))
    tab = _luz_del_ambiente(im, tab, x, y, w, h)
    mask = Image.new("L", tab.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, tab.size[0] - 1, tab.size[1] - 1],
                                           radius=P(13), fill=255)
    sombra = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rounded_rectangle(
        [P(x) + P(4), P(y) + P(7), P(x + w) + P(4), P(y + h) + P(7)],
        radius=P(13), fill=(0, 0, 0, 105))
    im.paste(Image.alpha_composite(im.convert("RGBA"), sombra.filter(
        ImageFilter.GaussianBlur(P(9)))).convert("RGB"), (0, 0))
    im.paste(tab, (P(x), P(y)), mask)


def _luz_del_ambiente(im, tab, x, y, w, h, fuerza=0.90):
    """La muestra está DENTRO de la escena: tiene que recibir su luz.

    Si se pega la foto de estudio tal cual, queda más saturada y más clara que el
    suelo y se lee como otro producto — el error más caro de esta marca. Se mide
    el piso a los dos costados de la muestra y se lleva la muestra hacia esa luz,
    conservando su textura y su color relativo.
    """
    import numpy as np
    # se mide el PISO, que está DEBAJO de la muestra. A los costados, a esa
    # altura, hay ventana y muro: medir ahí dejaba la muestra dorada.
    a = np.asarray(im).astype(float)
    cx0, cx1 = P(max(0, x - w * 0.2)), P(min(1080, x + w * 2.6))
    ent = a[P(y + h * 1.06):P(y + h * 1.46), cx0:cx1].reshape(-1, 3).mean(axis=0)
    t = np.asarray(tab).astype(float)
    med = t.reshape(-1, 3).mean(axis=0)
    f = np.clip(ent / np.maximum(med, 1.0), 0.45, 1.55)
    f = 1.0 + (f - 1.0) * fuerza
    return Image.fromarray(np.clip(t * f, 0, 255).astype("uint8"))


def etiqueta_gris(im, x, y, w, h, l1, l2):
    """Caja gris #626260 DELANTE de la muestra, texto CENTRADO, y un triángulo
    abajo a la derecha que simula SOMBRA (Paulina, 25-08-2026)."""
    d = ImageDraw.Draw(im)
    tri = P(h * 0.30)
    d.polygon([(P(x + w), P(y + h)), (P(x + w), P(y + h) + tri), (P(x + w) - tri, P(y + h))],
              fill=(0x4C, 0x4C, 0x4A))
    d.rectangle([P(x), P(y), P(x + w), P(y + h)], fill=GRIS)
    cx = P(x + w / 2)
    escribe(d, l1, caja(h * 0.245, 400), BLANCO, cx=cx, ink_top=P(y + h * 0.20))
    escribe(d, l2, caja(h * 0.245, 700), BLANCO, cx=cx, ink_top=P(y + h * 0.585))


def _flecha(d, x, y, largo):
    """Futura no trae el glifo «→»: la flecha se dibuja."""
    gr = max(2, int(round(2.2 * R)))
    p = max(3, int(round(5.5 * R)))
    d.line([(x, y), (x + largo, y)], fill=BLANCO, width=gr)
    d.line([(x + largo - p, y - p), (x + largo, y), (x + largo - p, y + p)],
           fill=BLANCO, width=gr, joint="curve")


def bloque_texto(im, cx, y_filete, antetitulo, titular, bajada, ancho_filete, x_filete, esc=1.0):
    """Antetítulo (brief nº6) → titular serif → filete → bajada → filete.
    Posiciones medidas en las fichas de Paulina: filete y 901, titular ink-top 817,
    bajada ink-top 920,6, filete inferior 965,8 (una línea) / 1000,3 (dos)."""
    d = ImageDraw.Draw(im)
    SOM = (P(2), P(3), (0, 0, 0))

    escribe(d, antetitulo, versales(17.0 * esc), BLANCO, cx=P(cx),
            ink_top=P(y_filete - 139.0 * esc), tr=P(17.0 * esc) * 0.19, sombra=SOM)

    fs = _serif_que_quepa(d, titular, ancho_filete - 20.0, 56.6 * esc)
    escribe(d, titular, fs, BLANCO, cx=P(cx), ink_top=P(y_filete - 84.0 * esc),
            tr=ajusta_tr(d, titular, fs, _ancho_serif(d, titular, fs)), sombra=SOM)

    d.rectangle([P(x_filete), P(y_filete), P(x_filete + ancho_filete), P(y_filete) + max(1, int(R))],
                fill=BLANCO)

    cap = 24.5 * esc
    tope = ancho_filete - 52.0
    while cap > 15.0:
        fv = versales(cap)
        if max(_ancho(d, l, fv, 0) for l in bajada) <= P(tope):
            break
        cap -= 0.5
    fv = versales(cap)
    y = y_filete + 19.6 * esc
    for linea in bajada:
        escribe(d, linea, fv, BLANCO, cx=P(cx), ink_top=P(y), sombra=SOM)
        y += cap * 1.706
    y_inf = y_filete + 64.8 * esc + (cap * 1.706 * (len(bajada) - 1))
    d.rectangle([P(x_filete), P(y_inf), P(x_filete + ancho_filete), P(y_inf) + max(1, int(R))],
                fill=BLANCO)
    return y_inf


def _serif_que_quepa(d, txt, tope_1080, cap=56.6):
    cap = float(cap)
    """El titular nunca se sale del ancho del filete. Paulina no lo hace nunca."""
    while cap > 26.0:
        f, _ = serif(cap)
        if _ancho_serif(d, txt, f) <= tope_1080:
            return f
        cap -= 0.5
    return serif(26.0)[0]


def _ancho_serif(d, txt, f):
    """El titular real de Paulina es un 6,7 % más ancho que Bodoni Moda a igual
    altura de mayúscula: se compensa con tracking hasta cerrar la fuente real."""
    return sum(d.textlength(c, font=f) for c in txt) * 1.067 / R


# ─────────────────────────────────────────────────────────── contenido del brief
C1 = [
    dict(sku="natural_uv_grande", n=1,
         look="LOOK NATURAL UV", titulo="Roble Natural UV",
         medida="14/3 · 190 × 1900 mm",
         bajada=["LA CALIDEZ DEL ROBLE CON PROTECCIÓN UV,", "EN FORMATO AMPLIO"]),
    dict(sku="natural_uv_chico", n=2,
         look="LOOK NATURAL UV", titulo="Roble Natural UV",
         medida="10/1.2 · 167 × 1200 mm",
         bajada=["EL MISMO ACABADO,", "EN UNA PROPORCIÓN MÁS CONTENIDA"]),
    dict(sku="aserrado", n=3,
         look="LOOK RÚSTICO", titulo="Roble Aserrado",
         medida="14/3 · 190 × 1900 mm",
         bajada=["TEXTURA ASERRADA Y VETA A LA VISTA:", "CARÁCTER EN CADA TABLA"]),
    dict(sku="cumaru", n=4,
         look="LOOK TRADICIONAL", titulo="Cumarú",
         medida="12/2 · 120 × 2130 mm",
         bajada=["TABLA LARGA Y ANGOSTA, DEL FORMATO", "CLÁSICO QUE NO SE PASA DE MODA"]),
]

C2 = [
    # `logo=False` donde el letrero del local ya dice Casablanca: la ronda 2 marcó
    # el logo duplicado en la tarjeta de la fachada.
    dict(n=1, logo=False, franja=False, foto=3, foco_y=0.30, etiqueta="SHOWROOM CASABLANCA · VITACURA",
         titulo="Ven a ver tu piso en persona", bajada=[]),
    dict(n=2, logo=True, franja=False, etiqueta="",
         titulo="Compara texturas, tonos y formatos",
         bajada=["CON ASESORÍA DE NUESTRO EQUIPO"]),
    # La foto del 6359 no tiene zona despejada donde cae el texto y el titular
    # chocaba con el número y con el letrero. El brief lo resuelve: «si la foto no
    # tiene espacio limpio, usar una franja de color sólido en el borde antes que
    # poner el texto encima del detalle» (C2, lineamiento nº3).
    # ⚠️ c2-3 SIN RESOLVER. Serena, 28-08: «se ve fea la foto donde sale el 6359
    # grande, me gusta que se vea la fachada pero que no se vea eso». Se probaron
    # tres encuadres: correr a la derecha corta la «C» de Casablanca, acercar y subir
    # deja puro cielo, centrado deja la placa abajo a la izquierda. La placa, el
    # letrero y el edificio están dispuestos de modo que NINGÚN recorte 4:5 los separa.
    # No es un problema de encuadre: falta la foto. El brief pide para esta tarjeta
    # «un piso instalado o una vista acogedora del local» y de las 36 fotos de la
    # clienta 32 son fachada. Queda en el menos malo hasta que llegue material.
    dict(n=3, logo=False, franja=True, foco_y=0.30, etiqueta="",
         titulo="Te esperamos",
         bajada=["JUAN XXIII 6359, VITACURA",
                 "AGENDA TU VISITA POR WHATSAPP  ·  +56 9 6653 5124"]),
]

# Geometría por formato. feed y story están MEDIDAS en las piezas de Paulina.
QA = []   # (pieza, alfa del velo, contraste logrado)

FORMATOS = {
    "feed": dict(w=1080, h=1080, esc=1.0,
                 logo=(440.6, 0.0, 198.7, 199.2),
                 muestra=(124.8, 258.0, 139.7, 470.0),
                 etiq=(69.1, 355.7, 252.0, 65.3),
                 filete_y=901.0, filete_x=163.2, filete_w=753.1,
                 velo=(0.42, 1.0, 96)),
    "story": dict(w=1080, h=1920,
                  logo=(421.4, 0.0, 237.1, 305.8),
                  muestra=(161.6, 418.6, 155.0, 522.0),
                  etiq=(99.8, 527.0, 279.8, 72.0),
                  filete_y=1292.0, filete_x=116.2, filete_w=847.2,
                  esc=1.25,          # «aumentar el bloque de texto un 20-30 %» (Paulina, 25-08)
                  velo=(0.40, 1.0, 104)),
    # ── 4:5 (Serena, 27-08-2026) ───────────────────────────────────────────
    # MEDIDO sobre las 6 piezas 4:5 de Paulina (raw/casablanca/ref/2026-08_carrusel_*.png,
    # 2250x2813 -> 1080x1350): el logo va en 440,6 / 0 / 198,7 / 221,3 en las seis, y el
    # bloque de texto del registro ANUNCIO lleva sus filetes en y 699 y 814 (esc 1,08).
    # DERIVADO: esas seis son registro anuncio y no traen muestra de tabla ni etiqueta,
    # así que para la FICHA se conserva la geometría 1:1 en la misma fracción de alto
    # (muestra y filete al 23,9 % y 83,4 %). No mezclar registros: si aparece una ficha
    # 4:5 aprobada, se mide y esto se reemplaza.
    "feed45": dict(w=1080, h=1350,
                   logo=(440.6, 0.0, 198.7, 221.3),          # medido
                   muestra=(124.8, 322.5, 139.7, 470.0),     # x/w/h del 1:1; y derivado
                   etiq=(69.1, 420.2, 252.0, 65.3),          # acompaña a la muestra
                   filete_y=1126.3, filete_x=163.2, filete_w=753.1,
                   esc=1.08,                                  # medido en el anuncio 4:5
                   velo=(0.42, 1.0, 96)),
}

# Qué foto usa cada formato. El 4:5 tiene ambiente propio (amb_*_feed45, 2432x2944
# nativo) porque recortar el cuadrado obligaba a ampliarlo un 37 %; el showroom sale
# del _story (2250x4000), que recorta a 4:5 sin ampliar nada.
AMB = {"feed": "feed", "story": "feed", "feed45": "feed45"}
SR2 = {"feed": "feed", "story": "story", "feed45": "story"}


def pieza_c1(t, fmt):
    g = FORMATOS[fmt]
    foto = Image.open(ASSETS / f"sep/amb_{t['sku']}_{AMB[fmt]}.jpg").convert("RGB")
    im = cover(foto, P(g["w"]), P(g["h"]))
    y_top = g["filete_y"] - 139.0 * g["esc"]
    y_bot = g["filete_y"] + 90.0 * g["esc"]
    im, _alfa, _c = velo_medido(im, y_top, y_bot)
    QA.append((f"c1-{t['n']} {fmt}", _alfa, _c))
    tarjeta_logo(im, *g["logo"])
    muestra_tabla(im, t["sku"], *g["muestra"])
    etiqueta_gris(im, *g["etiq"], "Piso de Ingeniería", t["medida"])
    y_inf = bloque_texto(im, g["w"] / 2, g["filete_y"], t["look"], t["titulo"],
                         t["bajada"], g["filete_w"], g["filete_x"], g["esc"])
    if t["n"] == 1 and fmt in ("feed", "feed45"):   # brief nº7 — sólo en feed
        d = ImageDraw.Draw(im)
        fv = versales(17.0)
        tr = P(17.0) * 0.19
        w = _ancho(d, "DESLIZA", fv, tr) + P(46)
        x0 = P(g["w"] / 2) - w / 2
        escribe(d, "DESLIZA", fv, BLANCO, x=x0, ink_top=P(y_inf + 26.0), tr=tr,
                sombra=(P(2), P(3), (0, 0, 0)))
        _flecha(d, x0 + w - P(30), P(y_inf + 34.5), P(26))
    return im


def pieza_c2(t, fmt):
    g = FORMATOS[fmt]
    # Serena, 28-08: «mover la foto para que no corte lo que dice pisos de madera».
    # El corte no es de la foto: el archivo _story ya trae el letrero al filo. El
    # _feed (2250x2250) sí lo muestra entero, y aunque para 4:5 haya que ampliarlo un
    # 25 %, está medido que a la medida de entrega (1080x1350) eso es invisible —
    # ambos caminos terminan reduciendo desde la misma fuente. Manda el encuadre.
    _src = SR2[fmt]
    _n = t.get("foto", t["n"])          # c2-1 usa la toma amplia (archivo 3)
    im = Image.open(ASSETS / f"sep/sr2_{_n}_{_src}.jpg").convert("RGB")
    # El 4:5 reusa la foto de story (2250x4000) y hay que recortarla. En feed y
    # story el archivo ya viene al tamaño exacto: no se toca, para no alterar por
    # un resample lo que el cliente ya aprobó.
    if im.size != (P(g["w"]), P(g["h"])):
        im = cover(im, P(g["w"]), P(g["h"]),
                   foco_x=t.get("foco_x", 0.5), foco_y=t.get("foco_y", 0.5),
                   zoom=t.get("zoom", 1.0))
    im = velo(im, g["velo"][0] - 0.06, 1.0, g["velo"][2] + 22)

    # Serena, 28-08: «el texto no se visualiza bien» (c2-1, c2-2) y «abajo el
    # rectángulo gris no me gusta, rompe la imagen» (c2-3). Las dos cosas a la vez:
    # el texto necesita algo detrás, pero no una banda con borde visible.
    #
    # Ojo con lo aprendido: medido, esas piezas daban 4,98 y 5,00:1, o sea pasaban el
    # umbral de contraste. El contraste mide LUMINOSIDAD, no lo movido que está el
    # fondo — sobre adoquines o paneles de madera el texto compite con el detalle
    # aunque el brillo dé. Por eso la métrica sola no alcanzaba.
    #
    # Se probaron tres salidas (ver _revisión/7): un panel claro translúcido BAJA el
    # contraste del texto blanco, al revés de lo buscado; el gris atenuado sigue
    # dejando el borde a la vista. Gana el degradado: continuo hasta el filo, sin
    # ninguna línea donde empiece.
    _grad_y0 = P(g["filete_y"] - 160.0 * g["esc"])
    _cap = Image.new("L", (1, im.size[1]), 0)
    _px = _cap.load()
    for _y in range(im.size[1]):
        _px[0, _y] = 0 if _y < _grad_y0 else int(
            150 * min(1.0, (_y - _grad_y0) / max(1, im.size[1] - _grad_y0) * 1.6))
    im.paste(Image.new("RGB", im.size, (28, 24, 20)), (0, 0), _cap.resize(im.size))

    if False:  # la franja gris queda derogada por el degradado de arriba
        # En story la franja NO llega al borde: si el texto cae bajo los 340 px
        # inferiores, Meta lo tapa con su interfaz. Es una banda a sangre lateral.
        # 1:1 medido (822 -> 1080). En 4:5 se mantiene la misma fracción de alto
        # (76,1 % -> borde). En story la franja NO llega al borde: bajo los 340 px
        # inferiores Meta tapa el texto con su interfaz.
        y0, y1 = {"feed": (822.0, 1080.0),
                  "feed45": (1027.5, 1350.0),
                  "story": (1152.0, 1562.0)}[fmt]
        ImageDraw.Draw(im).rectangle([0, P(y0), P(g["w"]), P(y1)], fill=GRIS)
        g = dict(g, filete_y={"feed": 950.0, "feed45": 1187.5, "story": 1320.0}[fmt])
    if t["logo"]:
        # Serena, 28-08: «que el logo no se vea tan al límite». En C1 cuelga del borde
        # a propósito (es la firma de marca); en C2 cae sobre foto de local y ahí se
        # lee como que se cae. Baja 26 u, sólo en C2.
        _lx, _ly, _lw, _lh = g["logo"]
        tarjeta_logo(im, _lx, _ly + 26.0, _lw, _lh)
    d = ImageDraw.Draw(im)
    SOM = (P(2), P(3), (0, 0, 0))
    y_f = g["filete_y"]
    e = g["esc"]
    if t["etiqueta"]:
        escribe(d, t["etiqueta"], versales(17.0 * e), BLANCO, cx=P(g["w"] / 2),
                ink_top=P(y_f - 139.0 * e), tr=P(17.0 * e) * 0.19, sombra=SOM)
    fs = _serif_que_quepa(d, t["titulo"], g["filete_w"] - 20.0, 56.6 * e)
    escribe(d, t["titulo"], fs, BLANCO, cx=P(g["w"] / 2), ink_top=P(y_f - 84.0 * e),
            tr=ajusta_tr(d, t["titulo"], fs, _ancho_serif(d, t["titulo"], fs)), sombra=SOM)
    if t["bajada"]:
        d.rectangle([P(g["filete_x"]), P(y_f), P(g["filete_x"] + g["filete_w"]), P(y_f) + max(1, int(R))],
                    fill=BLANCO)
        y = y_f + 19.6 * e
        for linea in t["bajada"]:
            escribe(d, linea, versales(21.0 * e), BLANCO, cx=P(g["w"] / 2), ink_top=P(y), sombra=SOM)
            y += 38.0 * e
        y_inf = y_f + 61.0 * e + 38.0 * e * (len(t["bajada"]) - 1)
        d.rectangle([P(g["filete_x"]), P(y_inf), P(g["filete_x"] + g["filete_w"]), P(y_inf) + max(1, int(R))],
                    fill=BLANCO)
    return im


def main():
    global FT_VERSALES
    FT_VERSALES = futura()
    quiere = [a.lower() for a in sys.argv[1:]]
    SALIDA.mkdir(parents=True, exist_ok=True)
    hechas = []
    for fmt in ("feed", "story", "feed45"):
        if quiere and fmt not in quiere and not any(q in ("c1", "c2") for q in quiere):
            continue
        for t in C1:
            if quiere and "c2" in quiere and "c1" not in quiere:
                break
            if quiere and fmt not in quiere and any(q in ("feed", "story") for q in quiere):
                break
            f = SALIDA / f"cb_sep_c1-{t['n']}-{t['sku'].replace('_','-')}_{fmt}.png"
            pieza_c1(t, fmt).save(f); hechas.append(f)
        for t in C2:
            if quiere and "c1" in quiere and "c2" not in quiere:
                break
            if quiere and fmt not in quiere and any(q in ("feed", "story") for q in quiere):
                break
            f = SALIDA / f"cb_sep_c2-{t['n']}_{fmt}.png"
            pieza_c2(t, fmt).save(f); hechas.append(f)
    for f in hechas:
        print(f"  ✓ {f.name}  {Image.open(f).size}")
    print(f"\n{len(hechas)} piezas en {SALIDA}")


if __name__ == "__main__":
    main()

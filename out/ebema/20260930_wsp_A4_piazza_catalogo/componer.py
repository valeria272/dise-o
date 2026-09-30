# -*- coding: utf-8 -*-
"""
EBEMA CLICK — campaña WhatsApp ARIEL A4 (septiembre 2026)
GRIFERÍA PIAZZA — CATÁLOGO +50 PRODUCTOS — FERRETERO — Santiago

Lenguaje: el de la madre de Paulina `A1_portezuelo_sept2026.png` (2500x4510):
cabezal rojo EBEMA CLICK (píxel original), título blanco sobre caja roja que
muerde la mitad de la 1.ª línea, píldora blanca con la bajada, mármol gris claro.

Textos: SÓLO los de la celda «Brief / Nota / imagen» de Carlos, verbatim.
Productos: los 7 packshots reales de la carpeta del brief (recortar.py). La IA
sólo hizo el set vacío (fondo_v3, Seedream); ninguna grifería pasa por IA.
Las 4 de muro van en el muro; las 3 de cubierta, paradas sobre los pedestales.

Uso:  python componer.py            → A4_piazza_catalogo_ferretero.png
"""
from pathlib import Path
import re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
FONTS = RAIZ / "clients/ebema/sistema/fonts"
MADRE = RAIZ / "public/assets/ebema/wsp-ariel/A1_portezuelo_sept2026.png"
W, H = 2500, 4510
ROJO = (236, 28, 35)          # #EC1C23
GRIS_PILDORA = (109, 111, 114)  # #6D6F72 (enunciado de la madre)
GRIS_TXT = (51, 51, 51)
# ronda 1: Paulina decide después si etiquetas y legal van en blanco o en negro
COLOR_ETIQUETA = (38, 38, 40)


def raleway(size, wght):
    f = ImageFont.truetype(str(FONTS / "Raleway-Variable.ttf"), size)
    f.set_variation_by_axes([wght])
    return f


def helv(size):
    return ImageFont.truetype(str(FONTS / "Helvetica-Bold.ttf"), size)


# ---------------------------------------------------------------- texto mixto
# R-02: toda cifra en Helvetica Bold. Se parte el texto en tramos cifra / letra.
CIFRA = re.compile(r"([+$]?\d[\d.]*)")


def tramos(txt, f_txt, f_num):
    out = []
    for i, t in enumerate(CIFRA.split(txt)):
        if t:
            out.append((t, f_num if i % 2 else f_txt))
    return out


def ancho(txt, f_txt, f_num, track=0):
    return sum(f.getlength(t) + track * len(t) for t, f in tramos(txt, f_txt, f_num))


def escribir(d, x, base, txt, f_txt, f_num, fill, track=0):
    """Dibuja en la línea base `base` (las dos fuentes comparten baseline)."""
    for t, f in tramos(txt, f_txt, f_num):
        for ch in t:
            d.text((x, base), ch, font=f, fill=fill, anchor="ls")
            x += f.getlength(ch) + track
    return x


def centrado(d, cx, base, txt, f_txt, f_num, fill, track=0):
    escribir(d, cx - ancho(txt, f_txt, f_num, track) / 2, base, txt, f_txt, f_num, fill, track)


# ---------------------------------------------------------------- fondo
def fondo():
    src = AQUI / "fondos/fondo_v4_x2.png"   # ronda 3: sin pedestales
    im = Image.open(src).convert("RGB")
    s = H / im.height
    im = im.resize((round(im.width * s), H), Image.LANCZOS)
    x0 = (im.width - W) // 2
    return im.crop((x0, 0, x0 + W, H)), s, x0


CUBIERTA_BORDE = 3246   # arista frontal de la cubierta en el lienzo


def zona_plana(im):
    """Ronda 4: «sigue viéndose cortada; más que un mesón, dale más iluminación».
    La cubierta se funde, sin arista, en una superficie de mármol clara: misma
    piedra del muro, más luz, y un fundido largo desde la cubierta."""
    a = np.array(im).astype(float)
    y0, fundido = 2990, 240      # termina antes de la arista frontal (3246): no queda línea
    alto = H - y0
    tex = a[700:700 + alto].copy()
    tex = (tex - tex.mean()) * 0.7 + 222
    t = np.clip(np.arange(alto) / fundido, 0, 1)[:, None, None]
    t = t * t * (3 - 2 * t)
    a[y0:] = a[y0:] * (1 - t) + tex * t
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def muro_oscuro(im):
    """Ronda 11 (Paulina): «oscurece la zona de arriba como está a la derecha, para
    que no se pierda GRIFERÍA». La luz de baja frecuencia del muro se lleva al nivel
    del lado derecho (~135) sin tocar la veta; se funde antes de la repisa."""
    a = np.array(im).astype(float)
    y1, y2 = 1000, 1400
    zona = Image.fromarray(a[:y2].mean(2).astype(np.uint8)).filter(ImageFilter.GaussianBlur(120))
    L = np.maximum(np.array(zona).astype(float), 1)
    gan = np.clip(135 / L, 0.55, 1.0)
    w = np.ones(y2)
    t = np.clip((np.arange(y2) - y1) / (y2 - y1), 0, 1)
    w -= t * t * (3 - 2 * t)
    g = 1 - (1 - gan) * w[:, None]
    a[:y2] *= g[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


REPISA_Y, REPISA_X0, REPISA_X1 = 1470, 0, 2500   # ronda 4: de muro a muro
REPISA_FONDO, REPISA_CANTO = 100, 44   # ronda 6: canto delgado                # cara superior en perspectiva + canto


def repisa(lienzo, fuente):
    """Ronda 4: la repisa corre de borde a borde, empotrada en el muro, con su cara
    superior en perspectiva y canto: se lee como una cubierta más, no flota.
    Piedra y luz sacadas de la cubierta del set."""
    f = np.array(fuente).astype(float)
    sup = Image.fromarray(f[2880:3230, 0:2500].astype(np.uint8)).resize((W, REPISA_FONDO), Image.LANCZOS)
    canto = Image.fromarray(f[3250:3560, 0:2500].astype(np.uint8)).resize((W, REPISA_CANTO), Image.LANCZOS)
    canto = Image.fromarray(np.clip(np.array(canto).astype(float) * 1.25, 0, 255).astype(np.uint8))
    y_canto = REPISA_Y + REPISA_FONDO
    sh = Image.new("L", lienzo.size, 0)
    ImageDraw.Draw(sh).rectangle([0, y_canto + REPISA_CANTO - 6, W, y_canto + REPISA_CANTO + 30], fill=70)
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    capa = Image.new("RGBA", lienzo.size, (30, 32, 38, 0)); capa.putalpha(sh); lienzo.alpha_composite(capa)
    # sombra de contacto contra el muro, al fondo de la cara superior
    sh = Image.new("L", lienzo.size, 0)
    ImageDraw.Draw(sh).rectangle([0, REPISA_Y - 6, W, REPISA_Y + 4], fill=120)
    sh = sh.filter(ImageFilter.GaussianBlur(5))
    lienzo.paste(sup, (0, REPISA_Y))
    capa = Image.new("RGBA", lienzo.size, (30, 32, 38, 0)); capa.putalpha(sh); lienzo.alpha_composite(capa)
    lienzo.paste(canto, (0, y_canto))
    ImageDraw.Draw(lienzo).line([(0, y_canto), (W, y_canto)], fill=(238, 239, 240), width=3)


# ---------------------------------------------------------------- productos
# Ronda 1 (Paulina): «todas las piezas mirando hacia un solo lado». Manda la
# derecha (4 de 7 ya miraban así); se espejan las 3 que miraban a la izquierda.
# Ronda 3: la ducha PZ6012 también se da vuelta; como su indicador rojo/azul
# quedaría invertido, se le intercambian los colores (rojo sigue a la izquierda).
ESPEJO = {"PZ6002", "GR317", "PZ6009", "PZ6012"}
INDICADOR = {"PZ6012"}


def corregir_indicador(p):
    a = np.array(p).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    rojo = (r > g + 60) & (r > b + 60)
    azul = (b > r + 50) & (b > g + 15)
    ys, xs = np.where(rojo)
    if len(ys):
        # sólo alrededor del botón indicador (evita tocar reflejos del cromo)
        cy, cx = int(np.median(ys)), int(np.median(xs))
        rad = int(max(ys.max() - ys.min(), xs.max() - xs.min()) * 1.6) + 10
        zona = np.zeros_like(rojo)
        zona[max(0, cy - rad):cy + rad, max(0, cx - rad):cx + rad] = True
        mr, mb = rojo & zona, azul & zona
        R, G, B = a[..., 0].copy(), a[..., 1].copy(), a[..., 2].copy()
        # rojo -> azul (220,40,50 -> 50,80,220) y azul -> rojo (50,90,220 -> 220,30,30)
        a[mr, 0], a[mr, 1], a[mr, 2] = B[mr], np.minimum(G[mr] * 2, 255), R[mr]
        a[mb, 0], a[mb, 1], a[mb, 2] = B[mb], R[mb] * 0.6, R[mb] * 0.6
    return Image.fromarray(a.astype(np.uint8))


# Ronda 4: proporciones reales. Una sola escala para las 7 piezas, desde las
# medidas de las fichas (GR317 13 cm y lavaplato 29,8 cm vienen acotados; el
# resto, de los planos y del estándar de cada tipo).
PX_CM = 24
MEDIDA = {  # (dimensión, cm)
    "PZ6002": ("ancho", 27),   # monomando tina ducha
    "PZ6012": ("ancho", 22),   # monomando ducha
    "PZ6000": ("alto", 15),    # monomando lavatorio
    "GR317": ("ancho", 13),    # llave individual (ficha: 13 cm)
    "AZ3214": ("ancho", 28),   # combinación lavaplato de 2 llaves
    "PZ6009": ("alto", 29.8),  # lavaplato vertical (ficha: 298 mm)
    "PZ20000NE": ("alto", 15), # Calyx negro
}


def a_escala(k):
    dim, cm = MEDIDA[k]
    return {"ancho_px": cm * PX_CM} if dim == "ancho" else {"alto_px": cm * PX_CM}


def con_roseta(p):
    """Ronda 6 (Paulina): la llave individual GR317 no trae base y se veía «pegada al
    suelo». Se le pone una roseta cromada redonda bajo el cuerpo, del mismo aire que
    la base de la llave vecina. El producto no se toca: sólo se levanta sobre ella."""
    a = np.array(p.getchannel("A"))
    h, w = a.shape
    filas = np.where(a.max(1) > 128)[0]
    # columnas del cuerpo = las de la manilla (tercio superior de la pieza)
    arriba = a[filas.min():filas.min() + (filas.max() - filas.min()) // 3]
    cols = np.where(arriba.max(0) > 128)[0]
    c0, c1 = cols.min(), cols.max()
    cuerpo = a[:, c0:c1 + 1]
    pie_y = int(np.where(cuerpo.max(1) > 128)[0].max())   # donde termina el cuerpo
    # ronda 7: la pestaña del Portezuelo «quedó rara». Ahora es una roseta baja
    # que sigue la forma de la propia llave: del ancho de su cuerpo, cilíndrica,
    # hecha con el cromo facetado de SU manilla (mismos reflejos, misma luz).
    alto_m = filas.max() - filas.min()
    banda = p.crop((c0, filas.min() + int(alto_m * 0.16), c1 + 1, filas.min() + int(alto_m * 0.24)))
    rw = int((c1 - c0) * 0.58)            # ronda 8: base angosta, no ancha
    cara = max(8, int(rw * 0.22))        # alto de la elipse superior (perspectiva)
    rh = max(10, int(rw * 0.16))          # alto del canto
    S = 4
    canto = banda.resize((rw * S, (rh + cara) * S), Image.LANCZOS).convert("RGB")
    m = Image.new("L", canto.size, 0)
    gm = ImageDraw.Draw(m)
    gm.rectangle([0, cara * S / 2, rw * S, (rh + cara / 2) * S], fill=255)
    gm.ellipse([0, rh * S, rw * S - 1, (rh + cara) * S - 1], fill=255)
    ro = Image.new("RGBA", canto.size, (0, 0, 0, 0))
    ro.paste(canto, (0, 0), m)
    g = ImageDraw.Draw(ro)
    g.ellipse([0, 0, rw * S - 1, cara * S - 1], fill=(214, 216, 220, 255))
    g.ellipse([rw * S * 0.12, cara * S * 0.18, rw * S * 0.55, cara * S * 0.58], fill=(242, 243, 245, 255))
    ro = ro.resize((rw, rh + cara), Image.LANCZOS)
    cx = (c0 + c1) / 2
    solape = cara // 2                    # el cuerpo asienta dentro de la cara superior
    alto_extra = ro.height - solape
    out = Image.new("RGBA", (max(w, int(cx + rw / 2) + 2), h + alto_extra), (0, 0, 0, 0))
    out.alpha_composite(ro, (int(cx - rw / 2), pie_y - solape))
    out.alpha_composite(p, (0, 0))
    return out


ROSETA = {"GR317"}


def cargar(k, ancho_px=None, alto_px=None):
    p = Image.open(AQUI / f"recortes/{k}.png").convert("RGBA")
    if k in ESPEJO:
        p = p.transpose(Image.FLIP_LEFT_RIGHT)
        if k in INDICADOR:
            p = corregir_indicador(p)
    if k in ROSETA:
        p = con_roseta(p)
    s = (ancho_px / p.width) if ancho_px else (alto_px / p.height)
    p = p.resize((round(p.width * s), round(p.height * s)), Image.LANCZOS)
    a = np.array(p).astype(float)
    # integración de color: el cromo de la ficha está sobre blanco puro; en el set
    # la luz es gris fría. Se bajan un poco las luces y se enfría apenas.
    rgb = a[..., :3]
    rgb = rgb * 0.92 + np.array([6, 8, 12])
    rgb = np.clip(rgb, 0, 246)
    # borde: 1 px hacia adentro y suavizado, para que no quede el filo del recorte
    al = Image.fromarray(a[..., 3].astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    out = np.dstack([rgb, np.array(al)]).astype(np.uint8)
    return Image.fromarray(out)


def sombra(lienzo, alfa, pos, dx, dy, blur, opac):
    sh = Image.new("L", lienzo.size, 0)
    sh.paste(alfa, (pos[0] + dx, pos[1] + dy))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * opac))
    capa = Image.new("RGBA", lienzo.size, (40, 42, 48, 0))
    capa.putalpha(sh)
    lienzo.alpha_composite(capa)


def de_muro(lienzo, k, cx, top, ancho_px):
    """Grifería de muro: sombra proyectada sobre el mármol (luz de arriba a la izquierda)."""
    p = cargar(k, ancho_px=ancho_px)
    pos = (round(cx - p.width / 2), top)
    a = p.getchannel("A")
    sombra(lienzo, a, pos, 10, 14, 6, 0.30)     # contacto, cerca
    sombra(lienzo, a, pos, 38, 52, 26, 0.22)    # proyectada, lejos
    lienzo.alpha_composite(p, pos)
    return pos, p.size


def de_cubierta(lienzo, k, cx, base_y, alto_px, reflejo=True, ancho_max=None, centrar_caja=False, escala=1.0):
    """Grifería apoyada en la cubierta o la repisa: sombra de contacto + reflejo leve."""
    p = cargar(k, **{d: v * escala for d, v in a_escala(k).items()}) if alto_px is None else cargar(k, alto_px=alto_px)
    a = np.array(p.getchannel("A"))
    filas = np.where(a.max(1) > 128)[0]
    fondo_y = filas.max()
    base_cols = np.where(a[max(0, fondo_y - 25):fondo_y + 1].max(0) > 128)[0]
    bx = (base_cols.min() + base_cols.max()) / 2
    bw = base_cols.max() - base_cols.min()
    if centrar_caja:          # en la repisa: la pieza se centra en su casillero
        bx = p.width / 2
    pos = (round(cx - bx), round(base_y - fondo_y))
    # sombra de contacto: elipse oscura bajo la base
    # ronda 4: la sombra sigue los puntos que de verdad tocan la superficie
    # (las 2 llaves de la Azteca, el pie del lavaplato), no una elipse al centro
    pie = p.getchannel("A").crop((0, max(0, fondo_y - 30), p.width, fondo_y + 1)).resize((p.width, 16))
    sh = Image.new("L", lienzo.size, 0)
    sh.paste(pie, (pos[0] + 8, round(base_y - 6)))
    sh = sh.filter(ImageFilter.GaussianBlur(9)).point(lambda v: int(min(255, v * 1.3) * 0.6))
    capa = Image.new("RGBA", lienzo.size, (35, 37, 42, 0)); capa.putalpha(sh); lienzo.alpha_composite(capa)
    # sombra proyectada hacia la derecha-atrás, aplastada sobre la cara superior
    alfa = p.getchannel("A")
    plano = alfa.resize((alfa.width, max(1, alfa.height // 6)))
    sh2 = Image.new("L", lienzo.size, 0)
    sh2.paste(plano, (pos[0] + 40, round(base_y - plano.height + 4)))
    sh2 = sh2.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.25))
    capa = Image.new("RGBA", lienzo.size, (35, 37, 42, 0)); capa.putalpha(sh2); lienzo.alpha_composite(capa)
    # reflejo en el mármol pulido del pedestal (muy leve, se desvanece)
    if not reflejo:
        lienzo.alpha_composite(p, pos)
        return pos, p.size
    ref = p.transpose(Image.FLIP_TOP_BOTTOM)
    ra = np.array(ref).astype(float)
    grad = np.clip(1 - np.arange(ref.height) / 90, 0, 1)[:, None] * 0.13
    ra[..., 3] *= grad
    lienzo.alpha_composite(Image.fromarray(ra.astype(np.uint8)), (pos[0], round(base_y + (p.height - fondo_y) - 1)))
    lienzo.alpha_composite(p, pos)
    return pos, p.size


# ---------------------------------------------------------------- íconos
def icono(tipo, d=190):
    S = 4
    D = d * S
    im = Image.new("RGBA", (D, D), (0, 0, 0, 0))
    g = ImageDraw.Draw(im)
    g.ellipse([0, 0, D - 1, D - 1], fill=(255, 255, 255))
    c = D / 2
    if tipo == "bandera":
        r = D * 0.40
        disco = Image.new("L", (D, D), 0)
        ImageDraw.Draw(disco).ellipse([c - r, c - r, c + r, c + r], fill=255)
        fl = Image.new("RGBA", (D, D), (255, 255, 255, 255))
        fg = ImageDraw.Draw(fl)
        celeste = (116, 172, 223)
        fg.rectangle([0, 0, D, c - r / 3], fill=celeste)
        fg.rectangle([0, c + r / 3, D, D], fill=celeste)
        sol = r * 0.17
        fg.ellipse([c - sol, c - sol, c + sol, c + sol], fill=(246, 180, 14))
        im.paste(fl, (0, 0), disco)
        g.ellipse([c - r, c - r, c + r, c + r], outline=(215, 215, 218), width=S * 2)
    elif tipo == "escudo":
        # escudo clásico: hombros rectos, costados rectos hasta la mitad y curvas
        # limpias hasta la punta (ronda 1: «el contorno se ve raro»)
        w, h = D * 0.52, D * 0.60
        x0, y0 = c - w / 2, c - h / 2 - D * 0.01
        curva = []
        for t in np.linspace(0, 1, 40):     # bézier cuadrática: costado izq. -> punta
            p0, p1, p2 = (x0, y0 + h * 0.48), (x0 + w * 0.02, y0 + h * 0.86), (c, y0 + h)
            curva.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
                          (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]))
        der = [(2 * c - x, y) for x, y in curva]          # costado der. -> punta
        pts = [(x0, y0 + h * 0.10), (c, y0), (x0 + w, y0 + h * 0.10)] + der + list(reversed(curva))
        g.polygon(pts, fill=ROJO)
        f5 = helv(int(D * 0.32))
        g.text((c, c - D * 0.005), "5", font=f5, fill=(255, 255, 255), anchor="mm")
    elif tipo == "camion":
        u = D / 100
        g.rounded_rectangle([18 * u, 33 * u, 60 * u, 64 * u], radius=2 * u, fill=ROJO)          # carga
        g.polygon([(62 * u, 42 * u), (74 * u, 42 * u), (83 * u, 53 * u), (83 * u, 64 * u), (62 * u, 64 * u)], fill=ROJO)  # cabina
        g.polygon([(66 * u, 45 * u), (73 * u, 45 * u), (78 * u, 52 * u), (66 * u, 52 * u)], fill=(255, 255, 255))      # ventana
        for x in (32, 71):
            g.ellipse([(x - 7) * u, 59 * u, (x + 7) * u, 73 * u], fill=ROJO)
            g.ellipse([(x - 3) * u, 63 * u, (x + 3) * u, 69 * u], fill=(255, 255, 255))
    return im.resize((d, d), Image.LANCZOS)


# ---------------------------------------------------------------- pieza
def componer(salida, linea2="PARA TU FERRETERÍA", exhibidor=True):
    lienzo, s, x0 = fondo()
    lienzo = lienzo.convert("RGBA")

    # 1. zona inferior plana y repisa (ronda 1)
    lienzo = muro_oscuro(zona_plana(lienzo.convert("RGB"))).convert("RGBA")
    repisa(lienzo, fondo()[0])

    # 2. cabezal: píxel original de la madre (EBEMA CLICK · Materiales y beneficios)
    madre = Image.open(MADRE).convert("RGBA")
    lienzo.alpha_composite(madre.crop((0, 0, W, 293)), (0, 0))
    sh = Image.new("L", (W, 40), 0)
    for i in range(40):
        ImageDraw.Draw(sh).line([(0, i), (W, i)], fill=int(70 * (1 - i / 40) ** 2))
    capa = Image.new("RGBA", (W, 40), (0, 0, 0, 0)); capa.putalpha(sh); lienzo.alpha_composite(capa, (0, 293))

    # 3. productos (ronda 6, orden de Paulina), todos mirando a la derecha:
    #    arriba · repisa con los 3 de lavamanos: Calyx negra · llave individual · Portezuelo
    #    medio  · las 2 de ducha instaladas en el muro
    #    abajo  · en la cubierta, más grandes y más abajo: lavaplato · Azteca
    base_rep = REPISA_Y + 58
    for k, cx, h_ in [("PZ20000NE", 560, 420), ("GR317", 1250, 350), ("PZ6000", 1940, 420)]:
        de_cubierta(lienzo, k, cx, base_rep, h_, centrar_caja=True)
    de_muro(lienzo, "PZ6002", 700, 1790, 690)       # tina ducha
    de_muro(lienzo, "PZ6012", 1820, 1745, 600)      # ducha
    de_cubierta(lienzo, "PZ6009", 760, 3170, 860, centrar_caja=True)   # lavaplato vertical
    de_cubierta(lienzo, "AZ3214", 1720, 3170, 800, centrar_caja=True)  # combinación Azteca

    d = ImageDraw.Draw(lienzo)

    # 4. título en 2 líneas (ronda 1): «GRIFERÍA PIAZZA: +50 PRODUCTOS» / «PARA TU FERRETERÍA»
    lineas = ["GRIFERÍA PIAZZA: +50 PRODUCTOS", linea2]
    # el cuerpo se mide SIEMPRE sobre la A4 aprobada: en la A5 «PARA TU OBRA» va
    # del mismo tamaño que «PARA TU FERRETERÍA» (Paulina, 30-09)
    MEDIR = ["GRIFERÍA PIAZZA: +50 PRODUCTOS", "PARA TU FERRETERÍA"]
    ANCHO_T, CAP_MAX = 2150, 165
    medidas = []
    for t, tm in zip(lineas, MEDIR):
        size = 400
        while True:
            ft, fn = raleway(size, 800), helv(round(size * 0.96))
            cap = ft.getbbox("E")[3] - ft.getbbox("E")[1]
            if ancho(tm, ft, fn, -2) <= ANCHO_T and cap <= CAP_MAX:
                break
            size -= 2
        medidas.append((t, ft, fn, cap))
    y = 430
    bases = []
    for t, ft, fn, cap in medidas:
        y += cap
        bases.append(y)
        y += 68       # ronda 9: el tilde de la 2.ª línea queda ~26 px bajo la 1.ª (con 40 chocaba, con 88 sobraba)
    # ronda 10: el rojo arranca a la mitad de la barra horizontal de la «A» de la 1.ª línea
    ft0 = medidas[0][1]
    am = Image.new("L", (ft0.size * 2, ft0.size * 2), 0)
    base_a = int(ft0.size * 1.5)
    ImageDraw.Draw(am).text((10, base_a), "A", font=ft0, fill=255, anchor="ls")
    aa = np.array(am) > 128
    filas_a = np.where(aa.any(1))[0]
    # la barra: filas donde la tinta es continua entre las dos patas (un solo tramo)
    def tramos_fila(r):
        x = np.where(r)[0]
        return 1 + int((np.diff(x) > 1).sum()) if len(x) else 0
    barra = [y for y in filas_a if tramos_fila(aa[y]) == 1 and y > filas_a.min() + (filas_a.max() - filas_a.min()) * 0.35]
    medio_barra = (min(barra) + max(barra)) / 2
    caja_y0 = bases[0] - (base_a - medio_barra)
    caja_y1 = bases[-1] + 115          # ronda 1: el rojo baja más y la píldora se despega del texto
    anchos = [ancho(t, ft, fn, -2) for t, ft, fn, _ in medidas]
    caja_x0, caja_x1 = W / 2 - max(anchos) / 2 - 55, W / 2 + max(anchos) / 2 + 55
    sc = Image.new("L", lienzo.size, 0)
    ImageDraw.Draw(sc).rectangle([caja_x0 + 8, caja_y0 + 10, caja_x1 + 8, caja_y1 + 10], fill=110)
    capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0)); capa.putalpha(sc.filter(ImageFilter.GaussianBlur(10))); lienzo.alpha_composite(capa)
    d.rectangle([caja_x0, caja_y0, caja_x1, caja_y1], fill=ROJO)
    capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for (t, ft, fn, _), b in zip(medidas, bases):
        centrado(dc, W / 2 + 5, b + 6, t, ft, fn, (0, 0, 0, 120), -2)
    lienzo.alpha_composite(capa.filter(ImageFilter.GaussianBlur(6)))
    d = ImageDraw.Draw(lienzo)
    for (t, ft, fn, _), b in zip(medidas, bases):
        centrado(d, W / 2, b, t, ft, fn, (255, 255, 255), -2)

    # 5. píldora blanca con la bajada — ronda 1: más grande y en mayúsculas
    bajada = "Calidad argentina con 5 años de garantía".upper()
    fp, fpn = raleway(76, 600), helv(74)
    aw = ancho(bajada, fp, fpn, 0)
    py0 = caja_y1 - 62   # ronda 10: la píldora sube
    d.rectangle([W / 2 - aw / 2 - 90, py0, W / 2 + aw / 2 + 90, py0 + 142], fill=(255, 255, 255))
    centrado(d, W / 2, py0 + 99, bajada, fp, fpn, GRIS_PILDORA, 0)
    # logo Piazza: fuera en la ronda 1 («se llena la imagen»); se decide después dónde va

    # 6. íconos: bandera · escudo · camión — ronda 1: textos más grandes
    ICO_Y, DI = 3330, 200
    items = [("bandera", ["Origen", "Argentina"]),
             ("escudo", ["Garantía", "5 años"]),
             ("camion", ["Despacho directo", "del proveedor"])]
    fl, fln = raleway(62, 700), helv(60)
    for i, (tipo, lab) in enumerate(items):
        cx = W / 2 + (i - 1) * 740
        ic = icono(tipo, DI)
        sa = Image.new("L", lienzo.size, 0)
        ImageDraw.Draw(sa).ellipse([cx - DI / 2 + 4, ICO_Y + 10, cx + DI / 2 + 4, ICO_Y + DI + 10], fill=120)
        capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0)); capa.putalpha(sa.filter(ImageFilter.GaussianBlur(12))); lienzo.alpha_composite(capa)
        lienzo.alpha_composite(ic, (round(cx - DI / 2), ICO_Y))
        d = ImageDraw.Draw(lienzo)
        for j, l in enumerate(lab):
            centrado(d, cx, ICO_Y + DI + 86 + j * 74, l, fl, fln, COLOR_ETIQUETA)

    # 7. caja roja: sello del exhibidor
    e1, e2 = "EXHIBIDOR CON MUESTRAS GRATIS", "por compras sobre $300.000 + IVA"
    fe1, fe1n = raleway(84, 800), helv(80)
    fe2, fe2n = raleway(64, 500), helv(64)
    ew = max(ancho(e1, fe1, fe1n), ancho(e2, fe2, fe2n)) + 2 * 110
    EY0 = 3800
    if exhibidor:
        d.rounded_rectangle([W / 2 - ew / 2, EY0, W / 2 + ew / 2, EY0 + 270], radius=34, fill=ROJO)
        centrado(d, W / 2, EY0 + 118, e1, fe1, fe1n, (255, 255, 255))
        centrado(d, W / 2, EY0 + 212, e2, fe2, fe2n, (255, 255, 255))

    # 8. CTA: cápsula roja con filete blanco
    cta = "VER CATÁLOGO EN EBEMACLICK.CL"
    fc = raleway(70, 800)
    cw = fc.getlength(cta) + 2 * 90
    # A5 (contratista): sin exhibidor ni legal; el botón sube a donde iba el exhibidor
    # ronda A5-2: el botón queda centrado entre el pie de las etiquetas (3702) y el
    # borde inferior (4180): 164 px de aire arriba y abajo
    CY0 = EY0 + 270 + 60 if exhibidor else 3866
    d.rounded_rectangle([W / 2 - cw / 2, CY0, W / 2 + cw / 2, CY0 + 150], radius=75, fill=ROJO,
                        outline=(255, 255, 255), width=6)
    d.text((W / 2, CY0 + 77), cta, font=fc, fill=(255, 255, 255), anchor="mm")

    # 9. nota legal — ronda 1: más grande
    leg = "Beneficio exclusivo para ferreteros. Las muestras del exhibidor no se cobran."
    if exhibidor:
        d.text((W / 2, CY0 + 150 + 88), leg, font=raleway(54, 600), fill=COLOR_ETIQUETA, anchor="mm")
    else:
        # la pieza se acorta: bajo el botón queda el mismo aire que la A4 deja bajo el legal
        lienzo = lienzo.crop((0, 0, W, 4180))

    lienzo.convert("RGB").save(salida, optimize=True)
    print("->", salida)


if __name__ == "__main__":
    componer(AQUI / "A4_piazza_catalogo_ferretero.png")
    # A5 — contratista: idéntica a la A4 aprobada, sólo cambia la 2.ª línea del título
    componer(AQUI / "A5_piazza_catalogo_contratista.png", linea2="PARA TU OBRA", exhibidor=False)

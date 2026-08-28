#!/usr/bin/env python3
"""
CAVA MORANDÉ — piezas del sistema de marca para los mailings.

Todo lo que se dibuja acá sale medido de las piezas reales de la diseñadora
(ver clients/cava/CLAUDE.md). Las reglas duras que este módulo hace cumplir:

  · La ADVERTENCIA es obligatoria en toda pieza (§3). No hay forma de armar
    un lienzo sin ella: `lienzo_mailing()` la pega siempre.
  · Las botellas no se deforman (§2). `pegar_botella()` escala con un solo
    factor y verifica el ratio contra el archivo original.
  · El logo es el PNG oficial, nunca recreado (§4).
  · El dorado es un degradado metálico, nunca un color plano (§4).
"""
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(RAIZ, "public", "assets", "cava")
FUENTES = os.path.join(ASSETS, "fonts")

# ── Paleta medida sobre las piezas reales ────────────────────────────────
DORADO_SOMBRA = (95, 60, 18)      # #5F3C12
DORADO_MEDIO = (201, 162, 78)     # #C9A24E
DORADO_LUZ = (244, 231, 176)      # #F4E7B0
DORADO_BRILLO = (255, 247, 193)   # #FFF7C1
NARANJO = (221, 102, 14)          # #DD660E — el isotipo
AZUL_BANDERA = (0, 99, 175)       # #0063AF — medido en la banda tricolor
ROJO_BANDERA = (231, 52, 57)      # #E73439 — idem
FONDO = (14, 26, 43)              # azul marino casi negro del mailing de sept.
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"


SANS = os.path.join(RAIZ, "public", "assets", "fonts", "Montserrat.ttf")


def sans(tam, peso=700):
    """Montserrat es variable: el nombre del vino y el precio van en sans bold,
    no en Butler. En el mailing de agosto se ve clarísimo — la serif es sólo
    para el titular de campaña."""
    f = ImageFont.truetype(SANS, tam)
    f.set_variation_by_axes([peso])
    return f


def fuente(nombre, tam):
    """Butler para el titular, Authentic Signature para la línea en script."""
    rutas = {
        "titulo": "Butler-Bold.ttf",        # la Bold que mandó el cliente
        "cuerpo": "ButlerFree-Lgt.ttf",     # la "thin" general
        "medio": "ButlerFree-Med.ttf",
        "libro": "ButlerFree-Rmn.ttf",
        "script": "AuthenticSignature.ttf",
        "condensada": "BebasNeue-Regular.ttf",
    }
    if nombre in ("arial", "legal"):
        return ImageFont.truetype(ARIAL_BOLD, tam)
    return ImageFont.truetype(os.path.join(FUENTES, rutas[nombre]), tam)


def ancho_texto(dib, txt, f, tracking=0):
    if not tracking:
        return dib.textlength(txt, font=f)
    return sum(dib.textlength(c, font=f) for c in txt) + tracking * (len(txt) - 1)


def texto(dib, xy, txt, f, fill, tracking=0, anclaje="la"):
    """Dibuja texto con tracking opcional. anclaje: la (izq) | ma (centro) | ra (der)."""
    x, y = xy
    if tracking:
        w = ancho_texto(dib, txt, f, tracking)
        if anclaje[0] == "m":
            x -= w / 2
        elif anclaje[0] == "r":
            x -= w
        for c in txt:
            dib.text((x, y), c, font=f, fill=fill, anchor="l" + anclaje[1])
            x += dib.textlength(c, font=f) + tracking
        return w
    dib.text((x, y), txt, font=f, fill=fill, anchor=anclaje)
    return dib.textlength(txt, font=f)


# ── Dorado metálico ──────────────────────────────────────────────────────
def degradado_dorado(tam, diagonal=True, oscuro=False):
    """
    El dorado de CAVA es un degradado metálico que va de sombra a brillo y de
    vuelta, en diagonal — nunca un color plano (clients/cava/CLAUDE.md §4).

    `oscuro` baja el rango para que el texto BLANCO encima se lea. Se usa en
    los badges de descuento: sobre el dorado con brillo, el blanco desaparece.
    """
    w, h = tam
    if oscuro:
        paradas = [
            (0.00, (74, 46, 13)), (0.20, (120, 82, 27)), (0.42, (156, 112, 42)),
            (0.52, (174, 128, 54)), (0.66, (150, 106, 39)), (0.85, (108, 73, 24)),
            (1.00, (74, 46, 13)),
        ]
    else:
        paradas = [
            (0.00, DORADO_SOMBRA), (0.14, (148, 101, 33)), (0.30, DORADO_MEDIO),
            (0.44, DORADO_LUZ), (0.52, DORADO_BRILLO), (0.62, DORADO_LUZ),
            (0.78, DORADO_MEDIO), (0.90, (175, 125, 55)), (1.00, DORADO_SOMBRA),
        ]
    largo = w + h if diagonal else w
    linea = Image.new("RGB", (largo, 1))
    px = linea.load()
    for x in range(largo):
        t = x / max(largo - 1, 1)
        for i in range(len(paradas) - 1):
            t0, c0 = paradas[i]
            t1, c1 = paradas[i + 1]
            if t0 <= t <= t1:
                k = (t - t0) / (t1 - t0)
                px[x, 0] = tuple(int(c0[j] + (c1[j] - c0[j]) * k) for j in range(3))
                break
    if not diagonal:
        return linea.resize((w, h), Image.BILINEAR)
    # proyecta la línea en diagonal
    banda = linea.resize((largo, largo), Image.BILINEAR)
    return banda.transform(
        (w, h), Image.AFFINE, (1, 1, 0, 0, 1, 0), resample=Image.BILINEAR
    )


def pintar_dorado(mascara, oscuro=False):
    """Devuelve una capa RGBA con el degradado dorado recortado por la máscara."""
    capa = degradado_dorado(mascara.size, oscuro=oscuro).convert("RGBA")
    capa.putalpha(mascara)
    return capa


# ── La advertencia — OBLIGATORIA ─────────────────────────────────────────
# El cliente usa hoy la variante del embarazo (verificado en el mailing de
# agosto 2026 y en el brief 1 de septiembre). La de "menores de 18" es la
# otra variante legal; se elige con `variante`.
LEYENDAS = {
    "embarazo": ("ADVERTENCIA", ["TODO CONSUMO", "DE ALCOHOL ES DAÑINO",
                                 "DURANTE EL EMBARAZO"]),
    "menores": ("ADVERTENCIA", ["EL CONSUMO DE ALCOHOL", "EN MENORES DE 18 AÑOS",
                                "SE ENCUENTRA PROHIBIDO"]),
}


def advertencia(ancho_pieza=2250, variante="embarazo"):
    """
    Caja negra + banda de color, medida sobre el KV_FIESTAS PATRIAS_2025 de la
    diseñadora: caja 992×462 sobre lienzo de 2250, banda 525×30 centrada al pie.
    (La del Cyber es 839×425; la de los mailings de este mes es la grande.)

    La banda lleva SÓLO azul y rojo, sin blanco entre medio: se verificó fila a
    fila en las dos piezas oficiales.
    """
    k = ancho_pieza / 2250
    w, h = int(992 * k), int(462 * k)
    caja = Image.new("RGBA", (w, h), NEGRO + (255,))
    d = ImageDraw.Draw(caja)

    titulo, lineas = LEYENDAS[variante]
    f_tit = fuente("legal", int(72 * k))
    f_lin = fuente("legal", int(52 * k))
    f_min = fuente("legal", int(46 * k))

    y = int(30 * k)
    texto(d, (w / 2, y), titulo, f_tit, BLANCO, tracking=int(2 * k), anclaje="ma")
    y += int(94 * k)
    for ln in lineas:
        texto(d, (w / 2, y), ln, f_lin, BLANCO, anclaje="ma")
        y += int(62 * k)
    y += int(12 * k)
    texto(d, (w / 2, y), "Ministerio de Salud", f_min, BLANCO, anclaje="ma")

    # banda al pie: 525×30 centrada (medido)
    bw, bh = int(525 * k), int(30 * k)
    bx, by = (w - bw) // 2, h - bh - int(14 * k)
    d.rectangle([bx, by, bx + bw // 2, by + bh], fill=AZUL_BANDERA)
    d.rectangle([bx + bw // 2, by, bx + bw, by + bh], fill=ROJO_BANDERA)
    return caja


# ── Logo oficial ─────────────────────────────────────────────────────────
def logo(alto):
    """El PNG oficial escalado proporcionalmente. Nunca se recrea (§4)."""
    lg = Image.open(os.path.join(ASSETS, "logo", "cava-morande-blanco.png")).convert("RGBA")
    w = round(lg.width * alto / lg.height)
    return lg.resize((w, alto), Image.LANCZOS)


# ── Botellas — sin deformar, con verificación ────────────────────────────
def pegar_botella(lienzo, ruta, centro_x, base_y, alto_destino, sombra=True):
    """
    Coloca un bottle shot oficial escalando con UN factor y verificando que el
    ratio final sea el del archivo original (clients/cava/CLAUDE.md §2).
    """
    # Si existe la versión 2× del upscaler de precisión, se usa esa: la botella
    # se reduce para llegar a su tamaño final en vez de ampliarse, y la etiqueta
    # llega nítida. Ver scripts/cava-botellas-2x.py.
    dosx = os.path.join(os.path.dirname(ruta), "2x", os.path.basename(ruta))
    im = Image.open(dosx if os.path.isfile(dosx) else ruta).convert("RGBA")
    bb = im.split()[-1].getbbox()
    im = im.crop(bb)
    ratio_original = im.width / im.height

    escala = alto_destino / im.height
    w = round(im.width * escala)
    im = im.resize((w, alto_destino), Image.LANCZOS)

    ratio_final = im.width / im.height
    if abs(ratio_final - ratio_original) > 0.005:
        raise ValueError(
            f"{os.path.basename(ruta)} quedó deformada: "
            f"{ratio_original:.4f} -> {ratio_final:.4f}"
        )

    x, y = int(centro_x - im.width / 2), int(base_y - im.height)
    if sombra:
        s = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
        elipse = ImageDraw.Draw(s)
        rx, ry = int(im.width * 0.46), max(int(im.width * 0.10), 8)
        elipse.ellipse(
            [centro_x - rx, base_y - ry, centro_x + rx, base_y + ry],
            fill=(0, 0, 0, 130),
        )
        lienzo.alpha_composite(s.filter(ImageFilter.GaussianBlur(int(im.width * 0.07))))
    lienzo.alpha_composite(im, (x, y))
    return ratio_original, ratio_final


# ── Barra dorada del llamado comercial ───────────────────────────────────
def barra_llamado(ancho, texto_llamado, alto=None, tam=None):
    """
    Lo único que cambia entre piezas del mes (§1). Texto negro sobre el
    degradado dorado, versales, condensada.
    """
    alto = alto or int(ancho * 0.075)
    tam = tam or int(alto * 0.62)
    barra = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    mask = Image.new("L", (ancho, alto), 255)
    barra.alpha_composite(pintar_dorado(mask))
    d = ImageDraw.Draw(barra)
    f = fuente("condensada", tam)
    texto(d, (ancho / 2, alto / 2), texto_llamado.upper(), f, NEGRO,
          tracking=int(tam * 0.045), anclaje="mm")
    return barra


# ── Cupón troquelado ─────────────────────────────────────────────────────
def cupon(ancho, codigo, rotulo="CUPÓN:", alto=None):
    """
    El ticket dorado con borde dentado y el código en negro, calcado de las
    dos referencias que dejó la ejecutiva en el brief (REF CUPÓN 1 y 2).
    """
    alto = alto or int(ancho * 0.42)
    diente = max(int(alto * 0.045), 10)

    # silueta con dientes arriba y abajo
    mask = Image.new("L", (ancho, alto), 0)
    md = ImageDraw.Draw(mask)
    md.rectangle([0, diente, ancho, alto - diente], fill=255)
    n = max(int(ancho / (diente * 2.4)), 6)
    paso = ancho / n
    for i in range(n + 1):
        cx = i * paso
        md.ellipse([cx - diente, 0, cx + diente, diente * 2], fill=255)
        md.ellipse([cx - diente, alto - diente * 2, cx + diente, alto], fill=255)

    ticket = pintar_dorado(mask)
    d = ImageDraw.Draw(ticket)

    # filete interior fino, como en la referencia
    m = int(alto * 0.11)
    d.rounded_rectangle([m, m, ancho - m, alto - m], radius=int(alto * 0.05),
                        outline=(70, 45, 14, 210), width=max(int(alto * 0.012), 3))

    f_rot = fuente("condensada", int(alto * 0.17))
    f_cod = fuente("condensada", int(alto * 0.42))
    texto(d, (ancho / 2, alto * 0.30), rotulo.upper(), f_rot, NEGRO,
          tracking=int(alto * 0.02), anclaje="mm")
    texto(d, (ancho / 2, alto * 0.60), codigo.upper(), f_cod, NEGRO,
          tracking=int(alto * 0.012), anclaje="mm")
    return ticket


# ── Badge de descuento ───────────────────────────────────────────────────
def badge(diam, pct):
    """Badge dorado con el % — el 'sticker' de descuento de las tarjetas."""
    b = Image.new("RGBA", (diam, diam), (0, 0, 0, 0))
    mask = Image.new("L", (diam, diam), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, diam - 1, diam - 1], radius=int(diam * 0.16), fill=255
    )
    # dorado oscuro: sobre el dorado con brillo el texto blanco se pierde
    b.alpha_composite(pintar_dorado(mask, oscuro=True))
    d = ImageDraw.Draw(b)
    f_n = fuente("condensada", int(diam * 0.46))
    f_o = fuente("condensada", int(diam * 0.19))
    texto(d, (diam / 2, diam * 0.44), f"{pct}%", f_n, BLANCO, anclaje="mm")
    texto(d, (diam / 2, diam * 0.73), "OFF", f_o, BLANCO,
          tracking=int(diam * 0.02), anclaje="mm")
    return b


def clp(valor):
    """Formato chileno: separador de miles con punto, sin decimales."""
    return "$" + f"{int(valor):,}".replace(",", ".")


# ── Tarjeta de producto ──────────────────────────────────────────────────
def tarjeta_producto(ancho, alto, nombre, precio, precio_antes, pct, ruta_img):
    """
    La tarjeta blanca del mailing: badge dorado, nombre, precio grande y el
    precio anterior tachado, con el packshot a la derecha.
    """
    t = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    mask = Image.new("L", (ancho, alto), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, ancho - 1, alto - 1], radius=int(alto * 0.10), fill=255
    )
    blanca = Image.new("RGBA", (ancho, alto), BLANCO + (255,))
    blanca.putalpha(mask)
    t.alpha_composite(blanca)
    d = ImageDraw.Draw(t)

    pad = int(alto * 0.11)
    col_txt = int(ancho * 0.66)

    # badge arriba a la izquierda
    dbadge = int(alto * 0.28)
    t.alpha_composite(badge(dbadge, pct), (pad, pad))

    # nombre del producto, en dos o tres líneas
    f_nom = fuente("titulo", int(alto * 0.094))
    y = pad + dbadge + int(alto * 0.05)
    palabras, linea, lineas = nombre.split(), "", []
    for p in palabras:
        prueba = (linea + " " + p).strip()
        if d.textlength(prueba, font=f_nom) > col_txt - pad * 2 and linea:
            lineas.append(linea)
            linea = p
        else:
            linea = prueba
    lineas.append(linea)
    for ln in lineas[:3]:
        d.text((pad, y), ln, font=f_nom, fill=(26, 26, 26))
        y += int(alto * 0.112)

    # precio de oferta y, a su lado, el precio anterior tachado por el medio:
    # en columna se salía de la tarjeta cuando el nombre ocupaba dos líneas.
    y += int(alto * 0.03)
    f_pre = fuente("titulo", int(alto * 0.21))
    txt_pre = clp(precio)
    d.text((pad, y), txt_pre, font=f_pre, fill=(10, 10, 10))
    caja_pre = d.textbbox((pad, y), txt_pre, font=f_pre)

    f_ant = fuente("libro", int(alto * 0.105))
    txt_ant = clp(precio_antes)
    x_ant = caja_pre[2] + int(alto * 0.06)
    # se alinea por la base del precio grande
    caja_ant = d.textbbox((x_ant, 0), txt_ant, font=f_ant)
    y_ant = caja_pre[3] - (caja_ant[3] - caja_ant[1]) - int(alto * 0.012)
    d.text((x_ant, y_ant), txt_ant, font=f_ant, fill=(150, 150, 150))
    cb = d.textbbox((x_ant, y_ant), txt_ant, font=f_ant)
    ty = (cb[1] + cb[3]) / 2
    d.line([x_ant - 4, ty, cb[2] + 4, ty], fill=(150, 150, 150),
           width=max(int(alto * 0.009), 2))

    # filete divisorio y packshot a la derecha
    d.line([col_txt, pad, col_txt, alto - pad], fill=(225, 225, 225), width=2)
    if ruta_img and os.path.exists(ruta_img):
        im = Image.open(ruta_img).convert("RGBA")
        im = im.crop(im.split()[-1].getbbox())
        h = int(alto * 0.90)
        w = round(im.width * h / im.height)
        maxw = ancho - col_txt - int(pad * 1.2)
        if w > maxw:
            w, h = maxw, round(im.height * maxw / im.width)
        im = im.resize((w, h), Image.LANCZOS)
        t.alpha_composite(im, (col_txt + (ancho - col_txt - w) // 2, (alto - h) // 2))
    return t


# ── El lienzo del mailing ────────────────────────────────────────────────
def lienzo_mailing(alto, ancho=2250, variante_legal="embarazo"):
    """
    Crea el lienzo y pega la ADVERTENCIA arriba a la derecha, pegada al borde.
    Es el único constructor de piezas: así ninguna sale sin el legal (§3).
    """
    im = Image.new("RGBA", (ancho, alto), FONDO + (255,))
    adv = advertencia(ancho, variante_legal)
    im.alpha_composite(adv, (ancho - adv.width, 0))
    return im


def pegar_advertencia_encima(im, variante_legal="embarazo"):
    """Vuelve a pegar el legal al final, para que nada lo tape."""
    adv = advertencia(im.width, variante_legal)
    im.alpha_composite(adv, (im.width - adv.width, 0))
    return im


# ── Bodegón realista ─────────────────────────────────────────────────────
# Medido el 28-08-2026 contra el KV real de la diseñadora
# (`raw/cava/ref-sept2026/KV_FIESTAS_PATRIAS_2025.png`, 2250×2813). El KV que se
# había entregado se leía como collage y la causa NO era la geometría —esa ya
# estaba corregida— sino la PROFUNDIDAD DE CAMPO:
#
#   nitidez del fondo    ella 1,4–3,0   ·   nosotros 8,8   ← el barril competía
#   nitidez del producto ella 7,0–9,2   ·   nosotros 5,9   ← y le ganaba
#
# En un bodegón fotografiado de verdad el fondo se deshace y lo único enfocado es
# el producto. Mientras el fondo tenga tanto detalle como la botella, el ojo lee
# dos fotos pegadas y no hay sombra que lo arregle.
#
# Ver `docs/MAGNIFIC-LO-QUE-YA-PAGAMOS.md` y `scripts/cava-kv-realista.py`.

FR_ALTO_BOTELLA = 0.519    # 1459/2813 — manual §11: si no llega a la mitad, está chica
FR_ALTO_HEROE   = 0.620    # una botella SOLA tiene que subir, o el barril se queda
                           # de protagonista y vuelve el error del «barril grande
                           # con botellita encima» que advierte el manual §11
FR_BASE_GRUPO   = 0.880    # dónde apoyan
FR_ANCHO_GRUPO  = 0.800    # ella usa 0,723 con botellas limpias; las nuestras traen
                           # el sello de puntaje incrustado y a 0,723 se pisan
FR_CENTRO_GRUPO = 0.532    # 1198/2250 — no es el centro exacto de la pieza
FR_CURVA_APOYO  = 0.018    # la tapa es una elipse: la del centro apoya más abajo


def desenfoque_por_profundidad(fondo, y_apoyo, radio_lejos=13.0, radio_cerca=2.0):
    """Bokeh progresivo según la distancia, como una lente abierta.

    Un blur uniforme se ve a plástico. Se interpola entre varias versiones
    borrosas según la altura: el horizonte al radio máximo, el plano donde apoyan
    las botellas casi nítido, y hacia el pie vuelve a subir — el borde delantero
    del barril también está fuera de foco.
    """
    import numpy as np

    w, h = fondo.size
    niveles = 5
    capas = [fondo.filter(ImageFilter.GaussianBlur(
        radio_cerca + (radio_lejos - radio_cerca) * (i / (niveles - 1)) ** 1.15))
        for i in range(niveles)]
    ys = np.arange(h) / h
    d = np.abs(ys - y_apoyo)
    perfil = np.clip(d / max(y_apoyo, 1e-6), 0, 1) ** 0.75
    perfil = np.where(ys > y_apoyo, np.clip(d / 0.30, 0, 1) ** 1.1 * 0.75, perfil)
    salida = capas[0].copy()
    for i in range(1, niveles):
        lo, hi = (i - 1) / (niveles - 1), i / (niveles - 1)
        m = np.clip((perfil - lo) / (hi - lo), 0, 1) * 255
        mask = Image.fromarray(m.astype("uint8")[:, None].repeat(w, axis=1), "L")
        salida = Image.composite(capas[i], salida, mask)
    return salida


def sombra_apoyo(lienzo, cx, y, ancho, fuerza=1.0):
    """Dos sombras: contacto (dura y chica) + proyectada (ancha y difusa).
    Con una sola, o flota —si es suave— o parece sticker —si es dura—."""
    for rx_f, ry_f, alfa, blur_f in ((0.46, 0.100, 185, 0.055),
                                     (0.95, 0.200, 85, 0.230)):
        capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
        rx, ry = ancho * rx_f, max(ancho * ry_f, 8)
        ImageDraw.Draw(capa).ellipse([cx - rx, y - ry, cx + rx, y + ry],
                                     fill=(26, 13, 5, int(alfa * fuerza)))
        lienzo.alpha_composite(capa.filter(
            ImageFilter.GaussianBlur(max(ancho * blur_f, 3))))


def shot(nombre):
    """El bottle shot, prefiriendo la versión 2× del upscaler DE PRECISIÓN.

    Con la 2× la botella se REDUCE para llegar a su tamaño final en vez de
    ampliarse; ampliar ×1,9 con LANCZOS ablanda la etiqueta y deja el producto
    menos nítido que el fondo. Se generan con `scripts/cava-botellas-2x.py`.
    """
    dosx = os.path.join(ASSETS, "bottles", "2x", nombre + ".png")
    base = dosx if os.path.isfile(dosx) else os.path.join(
        ASSETS, "bottles", nombre + ".png")
    im = Image.open(base).convert("RGBA")
    return im.crop(im.split()[-1].getbbox())


def bodegon(fondo_png, botellas, W, H, con_luz=True):
    """Fondo desenfocado por profundidad + botellas apoyadas e integradas.

    Devuelve el lienzo RGBA sin tipografía: el texto lo pone quien llame.
    """
    f = Image.open(os.path.join(ASSETS, "kv", fondo_png)).convert("RGB")
    esc = max(W / f.width, H / f.height)
    f = f.resize((round(f.width * esc), round(f.height * esc)), Image.LANCZOS)
    f = f.crop(((f.width - W) // 2, 0, (f.width - W) // 2 + W, H))
    f = desenfoque_por_profundidad(f, FR_BASE_GRUPO)

    kv = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    kv.alpha_composite(f.convert("RGBA"))
    if not botellas:
        return kv

    alto_bot = round(H * (FR_ALTO_HEROE if len(botellas) == 1 else FR_ALTO_BOTELLA))
    y_base = H * FR_BASE_GRUPO
    n = len(botellas)
    x0 = W * FR_CENTRO_GRUPO - W * FR_ANCHO_GRUPO / 2
    x1 = W * FR_CENTRO_GRUPO + W * FR_ANCHO_GRUPO / 2

    puestas = []
    for i, nombre in enumerate(botellas):
        im = shot(nombre)
        cx = x0 + (x1 - x0) * ((i + 0.5) / n) if n > 1 else W * FR_CENTRO_GRUPO
        anc = round(alto_bot * im.width / im.height)
        dx = (cx - W * FR_CENTRO_GRUPO) / max(W * FR_ANCHO_GRUPO / 2, 1)
        y = y_base + H * FR_CURVA_APOYO * (1 - min(abs(dx), 1.0) ** 2)
        puestas.append((im, cx, y, alto_bot, anc))

    for im, cx, y, alto, anc in puestas:
        sombra_apoyo(kv, cx, y, anc)
    # De DERECHA A IZQUIERDA. Los bottle shots del e-commerce traen el sello de
    # puntaje incrustado y sobresaliendo hacia la derecha del hombro; si se apila
    # al revés, la botella siguiente le corta el sello a la anterior — se veía un
    # «91 PTS» partido en el KV del 28-08.
    for im, cx, y, alto, anc in sorted(puestas, key=lambda p: -p[1]):
        b = im.resize((anc, alto), Image.LANCZOS)
        if con_luz:
            b = _integra_luz(b, fuerza=0.75)
        kv.alpha_composite(b, (int(cx - anc / 2), int(y - alto)))
    return kv


def _integra_luz(im, fuerza=1.0):
    """Carga perezosa de scripts/cava-integrar-luz.py (tiene guiones en el nombre)."""
    global _IL
    try:
        _IL
    except NameError:
        import importlib.util
        import sys as _sys
        r = os.path.join(RAIZ, "scripts", "cava-integrar-luz.py")
        sp = importlib.util.spec_from_file_location("cava_integrar_luz", r)
        m = importlib.util.module_from_spec(sp)
        _sys.modules["cava_integrar_luz"] = m
        sp.loader.exec_module(m)
        _IL = m
    return _IL.integra_luz(im, fuerza=fuerza)

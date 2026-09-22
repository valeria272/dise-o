#!/usr/bin/env python3
"""MyZoo · octubre 2026 — arma los 4 estáticos «Por diseñar» de la grilla.

Grilla: «MyZoo | Grilla Octubre 2026» (1cYmSebFK-MMVECzL2I6Nc5jWwk7Y4PNx9-71rCePMcI),
hoja «Grilla Octubre » (con espacio), columnas C, D, G e I — las únicas con estado
«Por diseñar» y «ok» del cliente en COMENTARIOS CLIENTE TEXTO al 22-09-2026.

GRAMÁTICA — medida sobre 23 piezas publicadas jul–sep 2026 (casi todas de Paulina,
`raw/myzoo/ref-digital/`), NO inventada:
  · Exporta a 2250 px de ancho: feed 2250×2813, story 2250×4000.
  · Logo `logo.png` centrado arriba: 353 px de ancho en feed (círculo negro de
    y=145 a y=399), 418 px en story (círculo desde y=410).
  · Titular Neutraface Text Bold, MAYÚSCULAS, centrado. En feed la línea sin caja
    va a 171 px (alto de H = 116) y la línea en caja a 188 px (H = 128), o sea la
    línea destacada es ~10 % más grande. En story todas las líneas a 213 px (H = 145).
  · La caja destacada es coral #FF6969 (medido: 255,105,105), esquinas apenas
    redondeadas, texto blanco; 35 px sobre la H y 29 bajo la base, ~130 px a los lados.
  · Bajadas en Neutraface Text itálica. Cajas de producto verde #6BBC4F con texto
    blanco en itálica (carrusel «paseo», sept).
  · Sin punto final en los textos de pieza — lo pidió el cliente (27-08, Xtreme-Vet
    WTF: «para que todas las slides sean sin punto»).

LO QUE EL CLIENTE CORRIGIÓ Y ENTRA ACÁ (raw/myzoo/feedback-cliente.md):
  · «Bajar el logo y agregarle el claim "amor que se siente" [...] que no quede
    enano» (01-08). Los 4 briefs de octubre piden «Logo MyZoo + Amor que se siente».
    → el claim oficial (`myzoo_claim_amor.png`, la O es una huella) va BAJO el logo,
    a 620 px de ancho (alto de H ≈ 32 px en 2250 → ~16 px en pantalla de 1080).
  · El producto es el packshot REAL, nunca generado.

Uso:  python3 scripts/myzoo-oct-armar.py   → out/myzoo/octubre-2026/
"""
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(RAIZ, "public/assets/fonts/myzoo/NeutrafaceText-")
ESC = os.path.join(RAIZ, "public/assets/myzoo/oct/escenas/")   # las 4 elegidas, en JPG 93: viajan en git
LOG = os.path.join(RAIZ, "public/assets/myzoo/marca/")
PROD = os.path.join(RAIZ, "public/assets/myzoo/producto/")
OUT = os.path.join(RAIZ, "out/myzoo/octubre-2026")

CORAL = (255, 105, 105)
VERDE = (107, 188, 79)
AMARILLO = (255, 230, 0)
BLANCO = (255, 255, 255)
TINTA = (17, 17, 17)

FEED = (2250, 2813)
STORY = (2250, 4000)


def azul_marca(im, objetivo=(141, 196, 212)):
    """Lleva los celestes claros del fondo generado al celeste de MyZoo (#8DC4D4,
    medido en «detective», sept). Nano Banana los devuelve casi blancos (189,211,234)
    y el titular blanco pierde contraste. Máscara por TONO y saturación: sólo toca
    muro/cielo/telón celeste — nunca el perro, el gabinete ni un envase."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    hsv = np.asarray(im.convert("HSV")).astype(np.float32)
    h, sat, v = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255, hsv[..., 2] / 255
    m = np.clip(1 - np.abs(h - 205) / 25, 0, 1) * np.clip((sat - .08) / .1, 0, 1) * np.clip((v - .55) / .15, 0, 1)
    m = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))) / 255
    # color medio actual del fondo (los píxeles más «fondo»)
    sel = m > .9
    actual = a[sel].mean(0) if sel.any() else np.array(objetivo, np.float32)
    k = np.array(objetivo, np.float32) / actual
    b = a * (1 + (k - 1) * m[..., None])
    return Image.fromarray(np.clip(b, 0, 255).astype(np.uint8))


def fuente(peso, px):
    return ImageFont.truetype(F + peso + ".otf", px)


def cubrir(ruta, tam, zoom=1.0, cx=0.5, cy=0.5):
    """object-fit: cover, con zoom y centro opcional. Nunca estira."""
    im = Image.open(ruta).convert("RGB")
    W, H = tam
    s = max(W / im.width, H / im.height) * zoom
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = min(max(round(im.width * cx - W / 2), 0), im.width - W)
    y = min(max(round(im.height * cy - H / 2), 0), im.height - H)
    return im.crop((x, y, x + W, y + H)), s, (x, y)


def recortar_alfa(im):
    return im.crop(im.getbbox())


def pegar_logo(lienzo, ancho, top, claim_color=BLANCO, claim_ancho=620):
    """Logo oficial + claim «AMOR QUE SE SIENTE» debajo. Devuelve el y final."""
    logo = recortar_alfa(Image.open(LOG + "logo.png").convert("RGBA"))
    logo = logo.resize((ancho, round(logo.height * ancho / logo.width)), Image.LANCZOS)
    W = lienzo.width
    lienzo.alpha_composite(logo, ((W - ancho) // 2, top))
    claim = recortar_alfa(Image.open(LOG + "myzoo_claim_amor.png").convert("RGBA"))
    claim = claim.resize((claim_ancho, round(claim.height * claim_ancho / claim.width)), Image.LANCZOS)
    if claim_color != BLANCO:
        capa = Image.new("RGBA", claim.size, claim_color + (255,))
        capa.putalpha(claim.getchannel("A"))
        claim = capa
    y = top + logo.height + 34
    sombra_suave(lienzo, claim, ((W - claim_ancho) // 2, y), claim_color)
    lienzo.alpha_composite(claim, ((W - claim_ancho) // 2, y))
    return y + claim.height


def sombra_suave(lienzo, capa, pos, color, radio=14, opac=70):
    """Sombra difusa bajo texto blanco sobre foto — sólo si el texto es claro."""
    if sum(color) < 400:
        return
    a = capa.getchannel("A").filter(ImageFilter.GaussianBlur(radio))
    a = a.point(lambda v: v * opac // 255)
    s = Image.new("RGBA", capa.size, (0, 0, 0, 0))
    s.putalpha(a)
    lienzo.alpha_composite(s, (pos[0], pos[1] + 6))


def texto_capa(txt, f, color):
    bb = f.getbbox(txt)
    capa = Image.new("RGBA", (bb[2] - bb[0] + 4, bb[3] + 8), (0, 0, 0, 0))
    ImageDraw.Draw(capa).text((-bb[0] + 2, 0), txt, font=f, fill=color + (255,))
    return capa, bb


def titular(lienzo, lineas, top, story=False, color=BLANCO, escala=1.0):
    """lineas = [(texto, destacada)]. Devuelve el y final (base de la última línea)."""
    W = lienzo.width
    d = ImageDraw.Draw(lienzo)
    y = top
    # Cuerpo: primero se resuelve la línea en caja (la más importante) ajustada al
    # ancho útil, y la línea sin caja queda en 1/1,10 de ella — la proporción medida
    # (171 vs 188 en feed). En story todas iguales. `escala` achica el bloque entero.
    base_caja = round((213 if story else 188) * escala)
    for txt, caja in lineas:
        if caja:
            while fuente("Bold", base_caja).getlength(txt) > W - 340 - 260:
                base_caja -= 4
    for i, (txt, caja) in enumerate(lineas):
        px = base_caja if (caja or story) else round(base_caja / 1.10)
        f = fuente("Bold", px)
        while f.getlength(txt) > W - 340:
            px -= 4
            f = fuente("Bold", px)
        cap = f.getbbox("H")          # (x0, top_de_H, x1, base)
        alto_h = cap[3] - cap[1]
        ancho = f.getlength(txt)
        x = (W - ancho) / 2
        if caja:
            pad_t, pad_b, pad_x = round(alto_h * .27), round(alto_h * .23), 130
            y += pad_t + 6
            d.rounded_rectangle((x - pad_x, y - pad_t, x + ancho + pad_x, y + alto_h + pad_b),
                                radius=20, fill=CORAL)
            d.text((x, y - cap[1]), txt, font=f, fill=BLANCO)
            y += alto_h + pad_b
        else:
            capa, bb = texto_capa(txt, f, color)
            pos = (round(x + bb[0] - 2), round(y - cap[1]))
            sombra_suave(lienzo, capa, pos, color)
            lienzo.alpha_composite(capa, pos)
            y += alto_h
        y += round(alto_h * .42)      # interlínea medida: H de 116 → 181 de paso
    return y


def parrafo(lienzo, lineas, top, px, color=BLANCO, peso="DemiItalic", paso=1.32):
    W = lienzo.width
    f = fuente(peso, px)
    y = top
    for l in lineas:
        capa, bb = texto_capa(l, f, color)
        pos = (round((W - f.getlength(l)) / 2 + bb[0] - 2), y)
        sombra_suave(lienzo, capa, pos, color, radio=10, opac=60)
        lienzo.alpha_composite(capa, pos)
        y += round(px * paso)
    return y


def caja_etiqueta(lienzo, lineas, centro, px, fondo=VERDE, color=BLANCO, peso="DemiItalic", pad=(48, 30)):
    f = fuente(peso, px)
    ancho = max(f.getlength(l) for l in lineas)
    alto = round(px * 1.25) * len(lineas)
    x0 = round(centro[0] - ancho / 2 - pad[0]); y0 = round(centro[1] - alto / 2 - pad[1])
    d = ImageDraw.Draw(lienzo)
    d.rounded_rectangle((x0, y0, x0 + ancho + 2 * pad[0], y0 + alto + 2 * pad[1]), radius=22, fill=fondo)
    y = y0 + pad[1]
    for l in lineas:
        d.text((centro[0] - f.getlength(l) / 2, y), l, font=f, fill=color)
        y += round(px * 1.25)
    return (x0, y0, x0 + ancho + 2 * pad[0], y0 + alto + 2 * pad[1])


def huella(alto):
    """La huella de la O del claim oficial — es el 🐾 de la marca, no un emoji."""
    c = Image.open(LOG + "myzoo_claim_amor.png").convert("RGBA")
    a = np.asarray(c.getchannel("A"))
    cols = np.where(a.max(0) > 10)[0]
    grupos = np.split(cols, np.where(np.diff(cols) > 6)[0] + 1)   # A, M, huella, R, ...
    g = grupos[2]
    h = recortar_alfa(c.crop((g[0], 0, g[-1] + 1, c.height)))
    return h.resize((round(h.width * alto / h.height), alto), Image.LANCZOS)


def packshot(ruta, alto):
    p = recortar_alfa(Image.open(ruta).convert("RGBA"))
    return p.resize((round(p.width * alto / p.height), alto), Image.LANCZOS)


def sombra_contacto(lienzo, cx, base, ancho, opac=110):
    s = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    ImageDraw.Draw(s).ellipse((cx - ancho / 2, base - ancho * .09, cx + ancho / 2, base + ancho * .09),
                              fill=(0, 0, 0, opac))
    lienzo.alpha_composite(s.filter(ImageFilter.GaussianBlur(ancho * .08)))


# ───────────────────────────────────────────────────────────────────────────────
def p01_kit():
    """01-10 · Post estático · Espuma Repelente — «ROMPER EN CASO DE PASEO»."""
    from scipy import ndimage
    ruta = ESC + "kit-out2.jpg"
    fondo, s, (ox, oy) = cubrir(ruta, FEED)
    L = azul_marca(fondo).convert("RGBA")
    esc = lambda x, y: (x * s - ox, y * s - oy)       # coords de la escena → lienzo
    # placa y maniquí se ubican por máscara (las dos manchas blancas más grandes)
    k = np.asarray(Image.open(ruta).convert("RGB")).min(-1) > 220
    lab, n = ndimage.label(k)
    tam = ndimage.sum(k, lab, range(1, n + 1))
    orden = np.argsort(-tam)[:2]
    cajas = sorted([ndimage.find_objects(lab)[i] for i in orden], key=lambda sl: sl[0].start)
    placa, cuerpo_m = cajas            # la de arriba es la placa, la de abajo el envase
    (px0, py0), (px1, py1) = esc(placa[1].start, placa[0].start), esc(placa[1].stop, placa[0].stop)
    d = ImageDraw.Draw(L)
    f = fuente("Bold", round((py1 - py0) * .34))
    while f.getlength("ROMPER EN CASO") > (px1 - px0) * .86:
        f = fuente("Bold", f.size - 1)
    l1, l2 = "ROMPER EN CASO", "DE PASEO"
    cy = (py0 + py1) / 2
    hp = huella(round((py1 - py0) * .28))
    ancho2 = f.getlength(l2) + 14 + hp.width
    d.text(((px0 + px1) / 2 - f.getlength(l1) / 2, cy - (py1 - py0) * .38), l1, font=f, fill=TINTA)
    x2 = (px0 + px1) / 2 - ancho2 / 2
    d.text((x2, cy + 2), l2, font=f, fill=CORAL)
    tinta = Image.new("RGBA", hp.size, CORAL + (255,)); tinta.putalpha(hp.getchannel("A"))
    L.alpha_composite(tinta, (round(x2 + f.getlength(l2) + 14), round(cy + 4)))

    # packshot real sobre el maniquí (cuerpo blanco detectado arriba)
    (bx0, _), (bx1, bbase) = esc(cuerpo_m[1].start, 0), esc(cuerpo_m[1].stop, cuerpo_m[0].stop)
    # 1º se BORRA el maniquí: si no, su gatillo negro y su canto blanco asoman detrás
    # del envase real (primer armado del 22-09: se veían dos gatillos). Cada fila de
    # la zona se rellena interpolando entre el fondo coral a cada lado.
    arr = np.asarray(L).astype(np.float32)
    ancho_m = bx1 - bx0
    zx0, zx1 = int(bx0 - ancho_m * 1.05), int(bx1 + ancho_m * .5)
    zy0, zy1 = int(bbase - ancho_m * 5.9), int(bbase - 2)
    for yy in range(zy0, zy1):
        izq, der = arr[yy, zx0 - 3:zx0].mean(0), arr[yy, zx1:zx1 + 3].mean(0)
        t = np.linspace(0, 1, zx1 - zx0)[:, None]
        arr[yy, zx0:zx1] = izq * (1 - t) + der * t
    parche = Image.fromarray(arr.astype(np.uint8), "RGBA").crop((zx0, zy0, zx1, zy1))
    parche = parche.filter(ImageFilter.GaussianBlur(2))
    L.paste(parche, (zx0, zy0))
    pk = packshot(PROD + "REPELENTE_psd_compuesto.png", 10)
    a = np.asarray(pk.getchannel("A"))                  # ancho del cuerpo a 80 % del alto
    ref = Image.open(PROD + "REPELENTE_psd_compuesto.png").convert("RGBA")
    ref = recortar_alfa(ref); ra = np.asarray(ref.getchannel("A"))
    fila = ra[int(ra.shape[0] * .8)]; cuerpo = np.where(fila > 128)[0]
    k = (bx1 - bx0) * 1.32 / (cuerpo[-1] - cuerpo[0])   # 25 % más que el maniquí: el brief lo pide protagonista
    pk = ref.resize((round(ref.width * k), round(ref.height * k)), Image.LANCZOS)
    cx = (bx0 + bx1) / 2
    sombra_contacto(L, cx, bbase, pk.width * 1.1, opac=90)
    L.alpha_composite(pk, (round(cx - pk.width / 2), round(bbase - pk.height)))
    # reflejo del vidrio de la puerta encima del envase (el envase está DETRÁS del vidrio)
    brillo = Image.new("RGBA", L.size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(brillo)
    gx0, gy0 = bx0 - 60, bbase - (bx1 - bx0) * 5.2; gx1, gy1 = bx1 + 60, bbase + 10
    dd.polygon([(gx0 + 60, gy0), (gx0 + 180, gy0), (gx0 + 20, gy1), (gx0 - 100, gy1)], fill=(255, 255, 255, 38))
    L.alpha_composite(brillo.filter(ImageFilter.GaussianBlur(6)))

    y = pegar_logo(L, 353, 115)
    y = titular(L, [("ANTES DE SALIR,", False), ("PROTÉGELO", True)], y + 70)
    parrafo(L, ["Haz de la prevención parte de cada paseo"], y + 10, 66, color=TINTA)
    # etiqueta de producto — verde del repelente y de las cajas del carrusel «paseo»,
    # colgando bajo el gabinete, del lado contrario al perro
    caja_etiqueta(L, ["Espuma Repelente de Insectos", "para Perros MyZoo"],
                  ((bx0 + bx1) / 2 + 120, bbase + 410), 54)
    return L.convert("RGB")


def p02_preguntazoo(guia=False):
    """02-10 · Story estática · PREGUNTAZOO — deja el hueco para la caja de preguntas.

    La caja de preguntas la pone el CM en Instagram, NO va dibujada. Por eso el
    bloque de texto se compacta al cuerpo de la story de preguntas de sept
    (`storie_08.09`: caja de 132 px de alto → H ≈ 90) y no al de la story de evento
    (H 145): con H 145 el texto llegaba a la cara de la veterinaria y no quedaba
    aire para el sticker. `guia=True` dibuja dónde cae el sticker (sólo revisión).
    """
    fondo, s, _ = cubrir(ESC + "story-out1.jpg", STORY)
    L = azul_marca(fondo).convert("RGBA")
    y = pegar_logo(L, 380, 300, claim_ancho=660)

    # sello PREGUNTAZOO — NO EXISTE un logo de la sección (buscado en Drive el 22-09).
    # Propuesta armada con piezas del sistema: pastilla negra como el círculo del logo,
    # «PREGUNTA» blanco + «ZOO» amarillo #FFE600 como el «zoo» del logo, y la huella.
    f = fuente("Bold", 104)
    t1, t2 = "PREGUNTA", "ZOO"
    cap = f.getbbox("H"); alto_h = cap[3] - cap[1]
    hp = huella(round(alto_h * 1.15))
    w = f.getlength(t1) + f.getlength(t2) + 24 + hp.width
    x0 = (L.width - w) / 2; top = y + 80; alto_p = alto_h + 96
    d = ImageDraw.Draw(L)
    d.rounded_rectangle((x0 - 64, top, x0 + w + 64, top + alto_p), radius=alto_p // 2, fill=(0, 0, 0))
    ty = top + 48 - cap[1]
    d.text((x0, ty), t1, font=f, fill=BLANCO)
    d.text((x0 + f.getlength(t1), ty), t2, font=f, fill=AMARILLO)
    am = Image.new("RGBA", hp.size, AMARILLO + (255,)); am.putalpha(hp.getchannel("A"))
    L.alpha_composite(am, (round(x0 + f.getlength(t1) + f.getlength(t2) + 24),
                           round(top + 48 + alto_h - hp.height + 4)))
    y = top + alto_p

    y = titular(L, [("¿QUÉ TE GUSTARÍA", False), ("PREGUNTARLE A", False), ("NUESTRA EXPERTA?", True)],
                y + 90, story=True, escala=0.72)
    y = parrafo(L, ["Baño, pelaje, frecuencia de lavado,", "productos, rutinas de cuidado…",
                    "Déjanos tu duda y podría ser respondida", "en nuestro próximo Reel"],
                y + 4, 58, color=TINTA, peso="DemiItalic", paso=1.34)
    if guia:   # dónde cae el sticker de preguntas (≈ 1380×560 en 2250 de ancho)
        g = ImageDraw.Draw(L)
        gx0, gy0 = (L.width - 1380) // 2, y + 60
        g.rounded_rectangle((gx0, gy0, gx0 + 1380, gy0 + 560), radius=60, fill=(255, 255, 255, 235))
        fg = fuente("Book", 64)
        msg = "ESCRIBE TU PREGUNTA AQUÍ"
        g.text(((L.width - fg.getlength(msg)) / 2, gy0 + 240), msg, font=fg, fill=(150, 150, 150))
    return L.convert("RGB")


def p05_meli():
    """05-10 · Post estático · ¡MYZOO LLEGA A TODO CHILE! — Mercado Libre."""
    # meli-out1 = meli-4-bajo1 reducida a 0,84 y apoyada abajo en un lienzo 1600×2000,
    # con el cielo de arriba rellenado por outpaint (la punta norte chocaba con la bajada)
    fondo, s, (ox, oy) = cubrir(ESC + "meli-out1.jpg", FEED, zoom=1.0, cx=0.5, cy=0.5)
    L = azul_marca(fondo).convert("RGBA")
    k0 = 1600 / 3712 * 0.84                      # escena vieja → lienzo 1600
    k1 = 3712 / 1600                             # lienzo 1600 → salida 3712
    ajuste = lambda x, y: ((x * k0 + (1600 - 3712 * k0) / 2) * k1, (y * k0 + 2000 - 4608 * k0) * k1)
    esc = lambda x, y: tuple(v * s - o for v, o in zip(ajuste(x, y), (ox, oy)))
    # 3 favoritos REALES parados en la caja de la camioneta, a la derecha del gato.
    # Piso de la caja medido sobre la escena: bases entre y 3130 y 3240.
    for ruta, (x, base), alto in [
        (PROD + "MyZoo_Shampoo_neutro_coco_Perro.png", (2995, 3120), 250),
        (PROD + "REPELENTE_psd_compuesto.png", (2880, 3175), 285),
        (PROD + "MyZoo_Shampoo_neutro_avena_Perro.png", (2760, 3235), 275),
    ]:
        cx, cb = esc(x, base)
        pk = packshot(ruta, round(alto * s * k0 * k1))
        sombra_contacto(L, cx, cb, pk.width * 1.25, opac=120)
        L.alpha_composite(pk, (round(cx - pk.width / 2), round(cb - pk.height)))

    y = pegar_logo(L, 353, 115)
    y = titular(L, [("¡MYZOO LLEGA", False), ("A TODO CHILE!", True)], y + 70)
    parrafo(L, ["De norte a sur,", "tus favoritos MyZoo más cerca de ti"], y + 10, 66, color=TINTA)
    # llamado: «ENCUÉNTRANOS EN / MERCADO LIBRE» — pastilla amarilla abajo al centro
    f1, f2 = fuente("Demi", 58), fuente("Bold", 96)
    a1, a2 = "ENCUÉNTRANOS EN", "MERCADO LIBRE"
    w = max(f1.getlength(a1), f2.getlength(a2)) + 150
    x0 = (L.width - w) / 2; y0 = 2440
    d = ImageDraw.Draw(L)
    d.rounded_rectangle((x0, y0, x0 + w, y0 + 250), radius=28, fill=AMARILLO)
    d.text(((L.width - f1.getlength(a1)) / 2, y0 + 36), a1, font=f1, fill=TINTA)
    d.text(((L.width - f2.getlength(a2)) / 2, y0 + 110), a2, font=f2, fill=TINTA)
    return L.convert("RGB")


def p08_cruelty():
    """08-10 · Post estático · Cruelty Free — certificación ONG Te Protejo."""
    fondo, s, _ = cubrir(ESC + "cruelty-3-bajo1.jpg", FEED, zoom=1.0, cx=0.5, cy=0.5)
    L = fondo.convert("RGBA")
    # fondo amarillo claro → titular en TINTA (el blanco no se lee), caja coral igual
    y = pegar_logo(L, 353, 115, claim_color=TINTA)
    titular(L, [("CUIDARLOS TAMBIÉN ES", False), ("ELEGIR RESPONSABLEMENTE", True)], y + 70, color=TINTA)
    # bloque de certificación abajo a la derecha: sello Te Protejo + textos
    sello = recortar_alfa(Image.open(LOG + "sello_te_protejo_sobre_2cm.png").convert("RGBA"))
    sello = sello.resize((300, round(sello.height * 300 / sello.width)), Image.LANCZOS)
    circ = Image.new("RGBA", (380, 380), (0, 0, 0, 0))
    ImageDraw.Draw(circ).ellipse((0, 0, 379, 379), fill=BLANCO)
    circ.alpha_composite(sello, ((380 - sello.width) // 2, (380 - sello.height) // 2))
    x_s, y_s = 1640, 2290
    sombra_contacto(L, x_s + 190, y_s + 370, 330, opac=60)
    L.alpha_composite(circ, (x_s, y_s))
    d = ImageDraw.Draw(L)
    fb, fi = fuente("Bold", 76), fuente("DemiItalic", 58)
    tx = x_s - 50
    d.text((tx - fb.getlength("MyZoo es Cruelty Free"), y_s + 100), "MyZoo es Cruelty Free", font=fb, fill=TINTA)
    d.text((tx - fi.getlength("Certificados por ONG Te Protejo"), y_s + 200),
           "Certificados por ONG Te Protejo", font=fi, fill=TINTA)
    return L.convert("RGB")


PIEZAS = {
    # Nomenclatura de Paulina: fecha de publicación primero, minúscula y guion bajo
    # (docs/COMO-DISENA-EL-EQUIPO.md §3). El portal levanta por nombre.
    "01.10_post_repelente.png": p01_kit,
    "02.10_storie_preguntazoo.png": p02_preguntazoo,
    "05.10_post_mercadolibre.png": p05_meli,
    "08.10_post_crueltyfree.png": p08_cruelty,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, "_revision"), exist_ok=True)
    p02_preguntazoo(guia=True).save(os.path.join(OUT, "_revision", "02.10_storie_preguntazoo_CON-STICKER.png"))
    for nombre, fn in PIEZAS.items():
        im = fn()
        im.save(os.path.join(OUT, nombre), optimize=True)
        print("✓", nombre, im.size)

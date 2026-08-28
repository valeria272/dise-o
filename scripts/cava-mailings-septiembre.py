#!/usr/bin/env python3
"""
CAVA MORANDÉ — mailings de septiembre 2026 (Mailchimp).

Arma las 7 piezas que pidió la ejecutiva en el Sheet "CAVA | Briefs septiembre
2026", hoja MAILS MAILCHIMP | SEPTIEMBRE: el KV (f23-24) y los briefs 4 a 9.
De cada brief se toman SÓLO las celdas "Banner principal" y "Texto en imagen".

⭐ TODO ESTO ESTÁ CALCADO de las piezas reales de la diseñadora, no inventado:

    raw/cava/ref-sept2026/KV_FIESTAS_PATRIAS_2025.png   ← el KV que manda copiar
                                                          la celda de la fila 23
    raw/cava/ref-sept2026/CAVA_AGO_BRIEF1.png           ← bloque de oferta
    raw/cava/ref-sept2026/CAVA_AGO_BRIEF3.png           ← titular tipográfico
    raw/cava/ref-sept2026/mailing-agosto-orden.png      ← tarjetas de packs

Lo que se midió sobre el KV de referencia (2250×2813) y se respeta acá:

    caja del legal      992×462, pegada arriba a la derecha
    bloque logo+titular centrado en x≈670, NO en el centro de la pieza:
                        la derecha se la come el legal
    logo                alto 221, arriba
    titular             DOS registros — la primera línea en Butler y la
                        segunda en Authentic Signature, más grande
    botellas            base y=2602 sobre 2813 y alto 1459 = **52 % del alto
                        de la pieza**. Son las protagonistas; la barrica es
                        una base cortada por el pie del cuadro, no el sujeto.
    adorno              cruza en diagonal POR DETRÁS de las botellas

Uso:
    python3 scripts/cava-mailings-septiembre.py [--solo kv|b4|b5|b6|b7|b8|b9]
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cava_sistema as cs  # noqa: E402

RAIZ = cs.RAIZ
BOT = os.path.join(cs.ASSETS, "bottles")
KVS = os.path.join(cs.ASSETS, "kv")
SALIDA = os.path.join(RAIZ, "out", "cava", "septiembre-2026")

W = 2250
# El fondo escalado a 2250 mide 2793 de alto. Se le suma BAJADA arriba —
# estirando el cielo— para que quepan el logo y las dos líneas del titular sin
# que las botellas se les metan encima. La tapa baja lo mismo, en bloque.
BAJADA = 380
# y se recorta por abajo: bajo la tapa sobra barril y en la referencia el
# bloque de oferta arranca poco después del segundo aro.
RECORTE_PIE = 420
ALTO_KV = 2793 + BAJADA - RECORTE_PIE

# ── Proporciones sacadas del KV de referencia, en fracción del alto del KV ──
FR_LOGO_Y = 0.131       # 369/2813
FR_LOGO_ALTO = 0.0900   # el logo también iba corto contra la referencia
FR_TIT1_Y = 0.240       # 675/2813
FR_TIT2_Y = 0.293       # 801/2813
FR_BOTELLA = 0.519      # 1459/2813 — el 52 % del alto: son las protagonistas
# Con 4 botellas hay que bajar un punto la escala: los bottle shots del
# e-commerce traen el sello de puntaje incrustado sobre el hombro, y a tamaño
# completo los sellos de botellas contiguas se pisan entre sí. El KV de la
# diseñadora usa botellas limpias del SharePoint de la viña, que no tenemos.
FR_BOTELLA_GRUPO = 0.455
CENTRO_TEXTO = 670      # el bloque logo+titular no va al centro: el legal ocupa
                        # la derecha, así que se centra en x≈670

# La tapa del barril de cada fondo, medida con scripts/cava-calibrar-tapa.py.
# Las botellas se apoyan SOBRE esa elipse — no en una `y` puesta a mano, que es
# como en la v2 terminaron flotando delante del cuerpo del barril.
TAPAS = json.load(open(os.path.join(KVS, "tapas.json")))

# Alto de la botella respecto al DIÁMETRO de la tapa. Físicamente una botella
# (30 cm) es 0,53 del diámetro de un barril de 225 L (57 cm); en la perspectiva
# ligeramente elevada del KV se lee un poco más alta.
BOTELLA_POR_DIAMETRO = 0.63
# Un vino solo sobre la tapa se ve chico: cuatro botellas llenan el ancho y
# dominan, una sola deja el barril de protagonista. Sube hasta lo que permite
# el carril del titular.
BOTELLA_HEROE = 0.70

# Dónde apoyan dentro de la elipse: 0 = borde del fondo, 1 = borde delantero.
# Van en la mitad trasera para que la guirnalda pase por delante, como en la
# referencia.
APOYO_EN_TAPA = 0.42


def apoyo_en_elipse(t, x, k=APOYO_EN_TAPA):
    """`y` de contacto sobre la tapa para una botella puesta en la columna `x`.

    La superficie no es una recta: es una elipse en perspectiva, así que la
    botella del centro apoya más abajo que la del costado. Sin esto las bases
    quedan alineadas en horizontal y el grupo se ve pegoteado sobre el barril.
    """
    dx = (x - t["cx"]) / max(t["rx"], 1)
    dx = max(-0.995, min(0.995, dx))
    return t["cy"] + t["ry"] * k * (1 - dx ** 2) ** 0.5


def sombra_contacto(lienzo, cx, y, ancho):
    """La mancha de contacto en la madera. Sin ella la botella no se apoya: se posa."""
    capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    rx, ry = ancho * 0.52, max(ancho * 0.12, 10)
    d.ellipse([cx - rx, y - ry, cx + rx, y + ry], fill=(24, 12, 4, 165))
    lienzo.alpha_composite(capa.filter(ImageFilter.GaussianBlur(ancho * 0.085)))


FONDO_OFERTA = (14, 26, 43)     # azul marino del mailing de septiembre
CAFE = (74, 44, 26)


def b(nombre):
    return os.path.join(BOT, nombre + ".png")


# ── El key visual, calcado ───────────────────────────────────────────────
def bloque_kv(fondo, titular_serif, titular_script, botellas):
    # El bodegón (fondo desenfocado por profundidad + botellas apoyadas e
    # integradas) lo arma cs.bodegon(), medido contra el KV real de la diseñadora.
    # Acá sólo va el velo y la tipografía. Ver cava_sistema.py §bodegón.
    kv = cs.bodegon(fondo, botellas, W, ALTO_KV)

    # velo superior: el logo y el titular van en blanco sobre el viñedo claro
    velo = Image.new("RGBA", (W, ALTO_KV), (0, 0, 0, 0))
    dv = ImageDraw.Draw(velo)
    tope = int(ALTO_KV * 0.40)
    for y in range(tope):
        dv.line([0, y, W, y], fill=(8, 14, 24, int(150 * (1 - y / tope) ** 1.35)))
    kv.alpha_composite(velo)

    d = ImageDraw.Draw(kv)

    lg = cs.logo(round(ALTO_KV * FR_LOGO_ALTO))
    kv.alpha_composite(lg, (CENTRO_TEXTO - lg.width // 2, round(ALTO_KV * FR_LOGO_Y)))

    def escribe(txt, y, f_txt):
        capa = Image.new("RGBA", kv.size, (0, 0, 0, 0))
        ImageDraw.Draw(capa).text((CENTRO_TEXTO, y), txt, font=f_txt,
                                  fill=(0, 0, 0, 175), anchor="ma")
        kv.alpha_composite(capa.filter(ImageFilter.GaussianBlur(16)))
        d.text((CENTRO_TEXTO, y), txt, font=f_txt, fill=cs.BLANCO, anchor="ma")

    # Medido contra el KV real: el titular ocupa mucho más ancho del que le
    # estábamos dando. Valeria 28-08: «los textos quedan chicos».
    # El ancho útil se mide contra el KV real: el titular ocupa ~1240 px de los
    # 2250, centrado en x≈670. Darle 1560 lo hacía desbordar por la izquierda —
    # el bloque va centrado en 670, no en el centro de la pieza, porque arriba a
    # la derecha manda el legal. El cuerpo arranca grande y baja hasta caber.
    util_txt = 1235
    cuerpo = 122
    while cuerpo > 44 and d.textlength(titular_serif,
                                       font=cs.fuente("libro", cuerpo)) > util_txt:
        cuerpo -= 3
    escribe(titular_serif, round(ALTO_KV * FR_TIT1_Y), cs.fuente("libro", cuerpo))

    cuerpo2 = 215   # en el KV real la línea en script es la GRANDE de las dos
    while cuerpo2 > 60 and d.textlength(titular_script,
                                        font=cs.fuente("script", cuerpo2)) > util_txt:
        cuerpo2 -= 4
    escribe(titular_script, round(ALTO_KV * FR_TIT2_Y), cs.fuente("script", cuerpo2))
    return kv


def montar(kv, bloques, cola=110):
    alto = kv.height + sum(h for _, h in bloques) + cola
    im = cs.lienzo_mailing(alto, W)
    im.alpha_composite(kv, (0, 0))
    y = kv.height
    for dibuja, h in bloques:
        dibuja(im, y)
        y += h
    return cs.pegar_advertencia_encima(im)


def guardar(im, nombre):
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, nombre + ".png")
    im.convert("RGB").save(ruta)
    print(f"  ✓ {nombre}.png  {im.width}×{im.height}")


# ── Bloques de oferta, calcados del mailing de agosto ────────────────────
def bloque_oferta(producto, alto_bloque=None):
    """
    El bloque del mailing de agosto: badge dorado, nombre del vino en SANS bold,
    precio grande en sans y el precio anterior tachado debajo. Todo alineado a
    la izquierda, con el packshot a la derecha.

    El alto se DERIVA del contenido — con un alto fijo, el precio tachado se
    salía por el pie de la pieza en cuanto el nombre ocupaba tres líneas.
    """
    nonlocal_alto = (70 + 215 + 56              # margen + badge + aire
                     + 92 * len(producto["nombre_lineas"])
                     + 26 + 200                 # aire + precio
                     + 22 + 96                  # tachado
                     + 90)                      # margen inferior
    alto = alto_bloque or nonlocal_alto

    def dibuja(im, y):
        d = ImageDraw.Draw(im)
        x = 190
        im.alpha_composite(cs.badge(215, producto["pct"]), (x, y + 70))

        yy = y + 70 + 215 + 56
        f_nom = cs.sans(76, 700)
        for ln in producto["nombre_lineas"]:
            f_ln, cuerpo = f_nom, 76
            while cuerpo > 40 and d.textlength(ln, font=f_ln) > 1080:
                cuerpo -= 3
                f_ln = cs.sans(cuerpo, 700)
            d.text((x, yy), ln, font=f_ln, fill=cs.BLANCO)
            yy += 92

        yy += 26
        f_pre = cs.sans(178, 800)
        txt = cs.clp(producto["precio"])
        d.text((x, yy), txt, font=f_pre, fill=cs.BLANCO)
        caja = d.textbbox((x, yy), txt, font=f_pre)

        f_ant = cs.sans(86, 500)
        ant = cs.clp(producto["antes"])
        ya = caja[3] + 22
        d.text((x, ya), ant, font=f_ant, fill=(168, 172, 182))
        cb = d.textbbox((x, ya), ant, font=f_ant)
        ty = (cb[1] + cb[3]) / 2
        d.line([x - 6, ty, cb[2] + 6, ty], fill=(168, 172, 182), width=6)

        # La botella NO se repite acá: ya es la protagonista del KV, y en el
        # mailing de agosto aparece una sola vez en toda la pieza. Repetirla
        # dejaba el mismo bottle shot dos veces, una grande y una chica.
    return dibuja, alto


def bloque_tarjetas(productos, alto_tarjeta=520, sep=40, margen=175):
    n = len(productos)
    alto_bloque = n * alto_tarjeta + (n - 1) * sep + 90

    def dibuja(im, y):
        yy = y + 40
        for p in productos:
            t = tarjeta(W - margen * 2, alto_tarjeta, p)
            im.alpha_composite(t, (margen, yy))
            yy += alto_tarjeta + sep
    return dibuja, alto_bloque


def tarjeta(ancho, alto, p):
    """Tarjeta oscura con filete dorado — la del mailing del dúo 7Colores."""
    t = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    mask = Image.new("L", (ancho, alto), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, ancho - 1, alto - 1],
                                           radius=int(alto * 0.09), fill=255)
    base = Image.new("RGBA", (ancho, alto), (9, 17, 30, 255))
    base.putalpha(mask)
    t.alpha_composite(base)
    d = ImageDraw.Draw(t)
    d.rounded_rectangle([2, 2, ancho - 3, alto - 3], radius=int(alto * 0.09),
                        outline=cs.DORADO_MEDIO + (170,), width=3)

    pad = int(alto * 0.13)
    col = int(ancho * 0.62)
    t.alpha_composite(cs.badge(int(alto * 0.27), p["pct"]), (pad, pad))

    yy = pad + int(alto * 0.27) + int(alto * 0.06)
    f_nom = cs.sans(int(alto * 0.077), 700)
    palabras, linea, lineas = p["nombre"].split(), "", []
    for w in palabras:
        prueba = (linea + " " + w).strip()
        if d.textlength(prueba, font=f_nom) > col - pad * 2 and linea:
            lineas.append(linea)
            linea = w
        else:
            linea = prueba
    lineas.append(linea)
    for ln in lineas[:2]:
        d.text((pad, yy), ln, font=f_nom, fill=cs.BLANCO)
        yy += int(alto * 0.088)

    yy += int(alto * 0.02)
    f_pre = cs.sans(int(alto * 0.175), 800)
    txt = cs.clp(p["precio"])
    d.text((pad, yy), txt, font=f_pre, fill=cs.BLANCO)
    caja = d.textbbox((pad, yy), txt, font=f_pre)
    f_ant = cs.sans(int(alto * 0.088), 500)
    ant = cs.clp(p["antes"])
    xa = caja[2] + int(alto * 0.05)
    ca = d.textbbox((xa, 0), ant, font=f_ant)
    ya = caja[3] - (ca[3] - ca[1]) - int(alto * 0.012)
    d.text((xa, ya), ant, font=f_ant, fill=(168, 172, 182))
    cb = d.textbbox((xa, ya), ant, font=f_ant)
    ty = (cb[1] + cb[3]) / 2
    d.line([xa - 4, ty, cb[2] + 4, ty], fill=(168, 172, 182), width=4)

    im = Image.open(b(p["img"])).convert("RGBA")
    im = im.crop(im.split()[-1].getbbox())
    h = int(alto * 0.88)
    w = round(im.width * h / im.height)
    maxw = ancho - col - pad
    if w > maxw:
        w, h = maxw, round(im.height * maxw / im.width)
    t.alpha_composite(im.resize((w, h), Image.LANCZOS),
                      (col + (ancho - col - w) // 2, (alto - h) // 2))
    return t


def bloque_cupon(codigo, vigencia=None, alto_bloque=780):
    def dibuja(im, y):
        cp = cs.cupon(1460, codigo)
        im.alpha_composite(cp, ((W - cp.width) // 2, y + 50))
        if vigencia:
            d = ImageDraw.Draw(im)
            d.text((W / 2, y + 70 + cp.height + 34), vigencia,
                   font=cs.sans(50, 500), fill=(198, 202, 212), anchor="ma")
    return dibuja, alto_bloque


# ══════════════════════════════════════════════════════════════════════════
def pieza_kv():
    """KV SEPTIEMBRE · f23-24."""
    kv = bloque_kv("kv-fiestas-01.png",
                   "Que no falte vino en tu mesa", "estas Fiestas Patrias",
                   ["seleccion-vinedos-gr-cabernet", "vitis-unica-carmenere",
                    "edicion-limitada-carmenere", "7colores-limited-carmenere"])
    return montar(kv, [])


def pieza_b4():
    """BRIEF 4 · f125-126 · Día del Vino Chileno, cupón VINOCAVA."""
    kv = bloque_kv("kv-fiestas-01.png",
                   "Este Día del Vino celebra con", "40% off en tus favoritos",
                   ["seleccion-vinedos-gr-carmenere", "edicion-limitada-carmenere",
                    "vitis-unica-cabernet"])
    return montar(kv, [bloque_cupon(
        "VINOCAVA", "Válido solo el 04 de septiembre · stock limitado")])


def pieza_b5():
    """BRIEF 5 · f146-147 · Bombazo, Edición Limitada Carmenere 50 % OFF."""
    kv = bloque_kv("kv-fiestas-01.png",
                   "Vuelve Bombazo Cava", "50% off solo por hoy",
                   ["edicion-limitada-carmenere"])
    return montar(kv, [bloque_oferta({
        "img": "edicion-limitada-carmenere",
        "nombre_lineas": ["Morandé Edición Limitada", "Carmenere 2023",
                          "93 pts. Descorchados"],
        "precio": 9245, "antes": 18490, "pct": 50})])


def pieza_b6():
    """BRIEF 6 · f167-168 · Arma tu Fonda, cupón CAVA18, foco Carmenere."""
    kv = bloque_kv("kv-fiestas-01.png",
                   "Las fiestas son mejor con Cava", "lleva tus infaltables",
                   ["vitis-unica-carmenere", "edicion-limitada-carmenere",
                    "7colores-limited-carmenere", "seleccion-vinedos-gr-carmenere"])
    return montar(kv, [
        bloque_cupon("CAVA18", "45% OFF · vigencia 08 al 13 de septiembre"),
        bloque_tarjetas([
            {"nombre": "Morandé Vitis Única Carmenere 2023", "precio": 8245,
             "antes": 14990, "pct": 45, "img": "vitis-unica-carmenere"},
            {"nombre": "Morandé Edición Limitada Carmenere 2023", "precio": 10170,
             "antes": 18490, "pct": 45, "img": "edicion-limitada-carmenere"},
            {"nombre": "7Colores Limited Carmenere 2023", "precio": 10445,
             "antes": 18990, "pct": 45, "img": "7colores-limited-carmenere"},
            {"nombre": "Selección de Viñedos Gran Reserva Carmenere 2024",
             "precio": 4945, "antes": 8990, "pct": 45,
             "img": "seleccion-vinedos-gr-carmenere"},
        ])])


def pieza_b7():
    """BRIEF 7 · f188-189 · 7Colores Single Vineyard 50 % OFF."""
    kv = bloque_kv("kv-fiestas-01.png",
                   "Tu favorito", "a mitad de precio",
                   ["7colores-single-vineyard-red-blend"])
    return montar(kv, [bloque_oferta({
        "img": "7colores-single-vineyard-red-blend",
        "nombre_lineas": ["7Colores Single Vineyard", "Red Blend 2022",
                          "92 pts. Descorchados · 91 pts. James Suckling"],
        "precio": 5990, "antes": 11990, "pct": 50})])


def pieza_b8():
    """BRIEF 8 · f208-209 · Día de la Garnacha, Antiguas Raíces 40 % OFF."""
    kv = bloque_kv("kv-fiestas-01.png",
                   "Vuelve a las raíces", "con 40% off",
                   ["adventure-antiguas-raices"])
    return montar(kv, [bloque_oferta({
        "img": "adventure-antiguas-raices",
        "nombre_lineas": ["Morandé Adventure", "Antiguas Raíces 2020",
                          "93 pts. Robert Parker"],
        "precio": 11754, "antes": 19590, "pct": 40})])


def pieza_b9():
    """
    BRIEF 9 · f228-229 · Pionero Rosé pack x6, 40 % OFF.
    La celda dice «REFERENCIA KV SEPTIEMBRE PERO SIN DETALLES PATRIOS»: desde
    acá la estética deja de ser dieciochera y pasa a primaveral.
    """
    kv = bloque_kv("kv-primavera-01.png",
                   "Recibe la primavera", "con rosé a 40% off",
                   ["pionero-rose-packx6"])
    return montar(kv, [bloque_tarjetas([
        {"nombre": "Morandé Tributo Pionero Rosé · Pack x6", "precio": 21564,
         "antes": 35940, "pct": 40, "img": "pionero-rose-packx6"}])])


PIEZAS = {
    "kv": ("CAVA_SEP_KV", pieza_kv), "b4": ("CAVA_SEP_BRIEF4", pieza_b4),
    "b5": ("CAVA_SEP_BRIEF5", pieza_b5), "b6": ("CAVA_SEP_BRIEF6", pieza_b6),
    "b7": ("CAVA_SEP_BRIEF7", pieza_b7), "b8": ("CAVA_SEP_BRIEF8", pieza_b8),
    "b9": ("CAVA_SEP_BRIEF9", pieza_b9),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", choices=list(PIEZAS))
    args = ap.parse_args()
    objetivo = {args.solo: PIEZAS[args.solo]} if args.solo else PIEZAS
    print(f"CAVA MORANDÉ · mailings septiembre 2026 → {SALIDA}")
    for _, (nombre, fn) in objetivo.items():
        guardar(fn(), nombre)


if __name__ == "__main__":
    main()

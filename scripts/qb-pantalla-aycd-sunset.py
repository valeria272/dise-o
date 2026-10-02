# -*- coding: utf-8 -*-
"""Pantalla digital QB «All You Can Drink + Sunset QB» (02-10-2026).

Parte de los editables de Eli (disco F:, no viajan):
  · PANTALLA SUNSET QB+AYCD.ai  → mesa 12 (1080×1920) y mesa 11 (1230×720, ascensor)
  · SUNSET QB PROMO 2026.ai     → KV de Sunset aprobado el 01-10 (mesas 4 y 5)

La mitad de AYCD queda EXACTA al editable (se toma del render de la mesa). La mitad
de Sunset se rehace con el KV nuevo: foto de la terraza, logo Sunset QB, franja
«DESDE $3.990» y la misma estructura de recuadro + pastilla «TODOS LOS VIERNES».

Uso:
    python scripts/qb-pantalla-aycd-sunset.py capas     # separa capas de los .ai (una vez)
    python scripts/qb-pantalla-aycd-sunset.py armar r1  # arma las dos medidas en out/…/r1
"""
import io
import pathlib
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = pathlib.Path(__file__).resolve().parent.parent
EDIT = pathlib.Path("F:/SOLICITUDES 2026 HILTON/PROMOS QB 2026 Editable/SUNSET QB (PROMO OCT 2026)")
CAPAS = RAIZ / "raw/hilton/qb/pantallas-02-10/capas"
OUT = RAIZ / "out/qb/oct/pantalla-aycd-sunset"
Z = 150 / 72          # se trabaja a 150 ppp; la de 72 ppp sale reduciendo
FUENTES = RAIZ / "public/assets/hilton/qb/fonts"


def fuente(peso):
    """Raleway con los números de caja alta (`lnum`), como los deja Illustrator en el editable.
    PIL no aplica rasgos OpenType sin raqm, así que se remapean los dígitos en una copia."""
    destino = CAPAS / f"Raleway-{peso}-lnum.ttf"
    if not destino.exists():
        from fontTools.ttLib import TTFont
        f = TTFont(str(FUENTES / f"Raleway-{peso}.ttf"))
        gsub = f["GSUB"].table
        idx = [i for fr in gsub.FeatureList.FeatureRecord if fr.FeatureTag == "lnum" for i in fr.Feature.LookupListIndex]
        mapa = {}
        for i in idx:
            for st in gsub.LookupList.Lookup[i].SubTable:
                st = getattr(st, "ExtSubTable", st)
                mapa.update(getattr(st, "mapping", {}))
        for tabla in f["cmap"].tables:
            for cod, glifo in list(tabla.cmap.items()):
                if glifo in mapa:
                    tabla.cmap[cod] = mapa[glifo]
        destino.parent.mkdir(parents=True, exist_ok=True)
        f.save(str(destino))
        print("fuente", destino.name, "dígitos remapeados:", len(mapa))
    return str(destino)


def px(v):
    return int(round(v * Z))


def capas():
    import pymupdf
    CAPAS.mkdir(parents=True, exist_ok=True)
    m = pymupdf.Matrix(Z, Z)
    doc = pymupdf.open(str(EDIT / "PANTALLA SUNSET QB+AYCD.ai"), filetype="pdf")
    for i in (10, 11):
        doc[i].get_pixmap(matrix=m).save(str(CAPAS / f"pantalla-m{i+1}-full.png"))
    doc = pymupdf.open(str(EDIT / "PANTALLA SUNSET QB+AYCD.ai"), filetype="pdf")
    for i in (10, 11):
        p = doc[i]
        for x in sorted({im["xref"] for im in p.get_image_info(xrefs=True) if im["xref"]}):
            p.delete_image(x)
        p.get_pixmap(matrix=m, alpha=True).save(str(CAPAS / f"pantalla-m{i+1}-vect.png"))
    # la misma mesa SIN el listado de tragos de AYCD (texto vivo): se vuelve a escribir más abajo
    doc = pymupdf.open(str(EDIT / "PANTALLA SUNSET QB+AYCD.ai"), filetype="pdf")
    for i in (10, 11):
        p = doc[i]
        for b in p.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                t = "".join(sp["text"] for sp in ln["spans"])
                if t.startswith(("Schop Heineken - Piscola", "Sangría - Copa")):
                    p.add_redact_annot(pymupdf.Rect(ln["bbox"]), fill=False)
        p.apply_redactions(images=0, graphics=0)
        p.get_pixmap(matrix=m).save(str(CAPAS / f"pantalla-m{i+1}-base.png"))
    doc = pymupdf.open(str(EDIT / "SUNSET QB PROMO 2026.ai"), filetype="pdf")
    d = doc.extract_image(109)                      # foto horizontal de la terraza
    Image.open(io.BytesIO(d["image"])).convert("RGB").save(CAPAS / "foto-109.png")
    p = doc[3]
    p.delete_image(93)                              # sin la foto: logo, franja y textos con alfa
    p.get_pixmap(matrix=m, alpha=True).save(str(CAPAS / "sunset-m4-vect.png"))
    print("capas listas en", CAPAS)


def blanco_desde_negro(im):
    """Trazo o texto blanco sobre negro → capa blanca con alfa = luminancia."""
    lum = im.convert("L")
    capa = Image.new("RGBA", im.size, (255, 255, 255, 0))
    capa.putalpha(lum)
    return capa


def logo_sunset(alto_tinta):
    """Logo «Sunset QB» del KV: blanco puro, sin el degradado que trae detrás."""
    v = Image.open(CAPAS / "sunset-m4-vect.png").convert("RGBA")
    c = np.array(v.crop((px(190), px(235), px(905), px(530)))).astype(float)
    alfa = (c[:, :, 0] * c[:, :, 3] / 255.0)        # cobertura de blanco (el fondo es negro)
    alfa[alfa < 40] = 0                              # fuera la sombra y el degradado
    ys, xs = np.where(alfa > 128)
    alfa = alfa[ys.min() - 4:ys.max() + 5, xs.min() - 4:xs.max() + 5]
    capa = Image.new("RGBA", (alfa.shape[1], alfa.shape[0]), (255, 255, 255, 0))
    capa.putalpha(Image.fromarray(alfa.clip(0, 255).astype("uint8")))
    k = px(alto_tinta) / capa.height
    return capa.resize((int(capa.width * k), int(capa.height * k)), Image.LANCZOS)


def franja_precio(alto):
    """Franja verde «DESDE $3.990» tal como está en el KV."""
    v = Image.open(CAPAS / "sunset-m4-vect.png").convert("RGBA")
    c = v.crop((px(290), px(1397), px(790), px(1475)))
    k = px(alto) / c.height
    return c.resize((int(c.width * k), int(c.height * k)), Image.LANCZOS)


def degradado(tam, puntos, eje):
    """Negro con alfa por tramos. puntos = [(pos_pt, alfa 0–1), …] en el eje dado."""
    w, h = tam
    n = h if eje == "y" else w
    pos = np.arange(n) / Z
    a = np.interp(pos, [p for p, _ in puntos], [v for _, v in puntos])
    a = a * a * (3 - 2 * a) if False else a
    arr = np.zeros((h, w, 4), dtype="uint8")
    arr[:, :, 3] = (a[:, None] if eje == "y" else a[None, :]) * 255
    return Image.fromarray(arr, "RGBA")


def sombra(capa, radio, fuerza):
    s = Image.new("RGBA", capa.size, (0, 0, 0, 0))
    s.putalpha(capa.getchannel("A").point(lambda v: int(v * fuerza)))
    return s.filter(ImageFilter.GaussianBlur(px(radio)))


def pastilla(vect, zona, ancho_min):
    """Recorta la pastilla blanca «TODOS LOS VIERNES» del editable (zona y ancho mínimo en pt)."""
    x0, y0, x1, y1 = [px(v) for v in zona]
    a = np.array(vect.convert("RGB").crop((x0, y0, x1, y1))).min(2) > 235

    def tramo(fila):
        cols = np.where(fila)[0]
        if not len(cols):
            return cols
        return max(np.split(cols, np.where(np.diff(cols) > 1)[0] + 1), key=len)

    filas = [i for i, f in enumerate(a) if len(tramo(f)) > px(ancho_min)]
    f0, f1 = filas[0], filas[-1]
    t = tramo(a[f0 + 2])
    caja = (x0 + t[0], y0 + f0, x0 + t[-1] + 1, y0 + f1 + 1)
    return vect.convert("RGBA").crop(caja), caja


def texto_centrado(lienzo, lineas, cx, y_centros, cuerpo, peso="Bold", tracking=0.0):
    """Líneas centradas en cx (pt). tracking en em (0,06 = 60 de Illustrator)."""
    f = ImageFont.truetype(fuente(peso), px(cuerpo))
    d = ImageDraw.Draw(lienzo)
    for t, y in zip(lineas, y_centros):
        if not tracking:
            d.text((px(cx), px(y)), t, font=f, fill=(255, 255, 255, 255), anchor="mm")
            continue
        esp = tracking * px(cuerpo)
        anchos = [f.getlength(c) for c in t]
        x = px(cx) - (sum(anchos) + esp * (len(t) - 1)) / 2
        for c, w in zip(t, anchos):
            d.text((x, px(y)), c, font=f, fill=(255, 255, 255, 255), anchor="lm")
            x += w + esp


def marco(lienzo, caja, trazo, radio, relleno):
    x0, y0, x1, y1 = [px(v) for v in caja]
    capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    d.rounded_rectangle((x0, y0, x1, y1), radius=px(radio), fill=(0, 0, 0, int(255 * relleno)),
                        outline=(255, 255, 255, 255), width=max(2, px(trazo)))
    lienzo.alpha_composite(capa)


def pegar_foto(lienzo, escala, cx_foto, cx, y_foto, y):
    """La foto de la terraza a `escala` pt/px, con (cx_foto, y_foto) px sobre (cx, y) pt."""
    foto = Image.open(CAPAS / "foto-109.png").convert("RGBA")
    k = escala * Z
    f = foto.resize((int(foto.width * k), int(foto.height * k)), Image.LANCZOS)
    lienzo.alpha_composite(f, (px(cx) - int(cx_foto * k), px(y) - int(y_foto * k))) if True else None


def vertical():
    base = Image.open(CAPAS / "pantalla-m12-base.png").convert("RGBA")
    vect = Image.open(CAPAS / "pantalla-m12-vect.png")
    W, H = base.size
    L = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    foto = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    # foto: copas arriba del recuadro, centradas
    f = Image.open(CAPAS / "foto-109.png").convert("RGBA")
    s = P["v_escala"] * Z
    f = f.resize((int(f.width * s), int(f.height * s)), Image.LANCZOS)
    foto.paste(f, (px(540) - int(P["v_cx"] * s), px(P["v_y"]) - int(P["v_fy"] * s)))
    foto.alpha_composite(degradado((W, H), [(0, 1), (960, 1), (1055, 0), (1300, 0), (1400, .35), (1600, .82), (1760, 1), (1920, 1)], "y"))
    L.alpha_composite(foto)
    # recuadro al alto del de AYCD (203 pt), franja en la misma línea que tenía
    marco(L, (168, 1376, 911.5, 1579.4), 2.9, 9, FONDO_MARCO)
    tab, caja = pastilla(vect, (300, 1235, 780, 1305), 250)
    L.alpha_composite(tab, (caja[0], caja[1] + px(107)))
    lg = logo_sunset(100)
    L.alpha_composite(sombra(lg, 5, .55), (px(540) - lg.width // 2, px(1474) - lg.height // 2 + px(2)))
    L.alpha_composite(lg, (px(540) - lg.width // 2, px(1474) - lg.height // 2))
    fr = franja_precio(58.5)
    L.alpha_composite(fr, (px(540) - fr.width // 2, px(1545.4)))
    texto_centrado(L, [HORA_SUNSET], 540, [1634], 27, "Medium", .06)
    texto_centrado(L, COCTELES, 540, [1674, 1705], 22.7)
    legal = blanco_desde_negro(vect.convert("RGB").crop((px(230), px(1768), px(850), px(1838))))
    L.alpha_composite(legal, (px(230), px(1768)))
    # mitad de AYCD: intacta del editable
    L.paste(base.crop((0, 0, W, px(960))), (0, 0))
    texto_centrado(L, [HORA_AYCD], 540, [842], 27, "Medium", .06)
    texto_centrado(L, AYCD, 540, [882, 913], 22.7)
    return L.convert("RGB")


def horizontal():
    base = Image.open(CAPAS / "pantalla-m11-base.png").convert("RGBA")
    vect = Image.open(CAPAS / "pantalla-m11-vect.png")
    W, H = base.size
    L = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    f = Image.open(CAPAS / "foto-109.png").convert("RGBA")
    s = P["h_escala"] * Z
    f = f.resize((int(f.width * s), int(f.height * s)), Image.LANCZOS)
    L.paste(f, (px(893.5) - int(P["h_cx"] * s), px(P["h_y"]) - int(P["h_fy"] * s)))
    L.alpha_composite(degradado((W, H), [(0, 1), (615, 1), (700, 0), (1230, 0)], "x"))
    L.alpha_composite(degradado((W, H), [(0, 0), (400, 0), (470, .4), (590, .85), (660, 1), (720, 1)], "y"))
    marco(L, (681, 444, 1106, 561), 1.7, 5, FONDO_MARCO)
    tab, caja = pastilla(vect, (700, 425, 1090, 470), 150)
    L.alpha_composite(tab, (caja[0], caja[1]))
    lg = logo_sunset(62)
    L.alpha_composite(sombra(lg, 3, .55), (px(893.5) - lg.width // 2, px(501) - lg.height // 2 + px(1)))
    L.alpha_composite(lg, (px(893.5) - lg.width // 2, px(501) - lg.height // 2))
    fr = franja_precio(34)
    L.alpha_composite(fr, (px(893.5) - fr.width // 2, px(542)))
    texto_centrado(L, [HORA_SUNSET], 893.5, [593], 16, "Medium", .06)
    texto_centrado(L, COCTELES, 893.5, [617.5, 635.5], 13)
    # mitad de AYCD intacta + legal común sobre las dos mitades
    L.paste(base.crop((0, 0, px(615), H)), (0, 0))
    texto_centrado(L, [HORA_AYCD], 305.5, [593], 16, "Medium", .06)
    texto_centrado(L, AYCD, 305.5, [617.5, 635.5], 13)
    legal = blanco_desde_negro(vect.convert("RGB").crop((px(270), px(662), px(960), px(692))))
    franja_negra = Image.new("RGBA", legal.size, (0, 0, 0, 255))
    L.paste(franja_negra, (px(270), px(662)))
    L.alpha_composite(legal, (px(270), px(662)))
    return L.convert("RGB")


# Los cócteles del Sunset, en el orden de la mesa 3 de «SUNSET QB PROMO 2026.ai» y con la
# misma forma del listado de AYCD (nombres separados por guion, dos líneas centradas)
AYCD = ["Schop Heineken - Piscola 35° (Mistral o Alto del Carmen) - Ramazzotti",
        "Sangría - Copa de espumante (opción de la casa)"]
HORA_AYCD = "18:00 a 21:00 hrs"      # como en la pantalla sola de AYCD del editable
HORA_SUNSET = "16:00 a 21:00 hrs"
COCTELES = ["Aperol - Ramazzotti - Sangría - Margarita - Mojito",
            "Espumante - Schop - Piscola - Gin"]

FONDO_MARCO = .40      # velo del recuadro de Sunset, parejo con el de AYCD (Eli, r3)

# Encuadre de la foto (px de la foto 2560×1440): centro de las tres copas y altura de sus bocas
P = dict(v_escala=.60, v_cx=1325, v_fy=250, v_y=1040,
         h_escala=.50, h_cx=1325, h_fy=250, h_y=95)


def armar(ronda):
    d = OUT / ronda
    d.mkdir(parents=True, exist_ok=True)
    for nombre, im, chico in (("PANTALLA AYCD+SUNSET", vertical(), (1080, 1920)),
                              ("ASCENSOR AYCD+SUNSET", horizontal(), (1230, 720))):
        im.save(d / f"150ppp_{nombre}.png", dpi=(150, 150))
        im.save(d / f"150ppp_{nombre}.jpg", quality=95, subsampling=0, dpi=(150, 150))
        c = im.resize(chico, Image.LANCZOS)
        c.save(d / f"72ppp_{nombre}.png", dpi=(72, 72))
        c.save(d / f"72ppp_{nombre}.jpg", quality=95, subsampling=0, dpi=(72, 72))
        print(nombre, im.size, "→", chico)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "capas":
        capas()
    else:
        armar(sys.argv[2] if len(sys.argv) > 2 else "r1")

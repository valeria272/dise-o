#!/usr/bin/env python3
"""
PETRA — Propuesta de mensajes comerciales para Meta Ads (septiembre 2026)

Arma las 4 piezas de la propuesta en los dos formatos de Meta.
NO es la entrega final: la ejecución la hace el equipo de diseño de Petra.
Esto es la referencia de mensaje y de armado.

Gramática replicada de las piezas que Petra ya tiene corriendo:
campo de color plano · titular en versales · foto en óvalo · logotipo abajo.
El logotipo es el SVG oficial de Petra, no una aproximación tipográfica.
Es la estructura de "Anuncio 5 | vertical", la que mejor rinde de la cuenta.

Paleta MEDIDA con PIL sobre las creatividades bajadas de la cuenta
(no estimada): oliva #525834, celeste #AAB9BE.

Reglas duras aplicadas (docs/SISTEMA-DE-MARCAS.md + skill direccion-de-arte):
  - Ningún botón dibujado dentro de la gráfica: Meta ya pone el suyo.
  - Zonas seguras de Meta en 9:16: 250 px arriba, 340 px abajo.
  - La foto se recorta a "cover", nunca se estira.
  - Máximo 3 bloques apilados: titular, dato, logotipo.
  - El logotipo va sobre el campo plano, nunca sobre la foto: encima
    del satín claro o del telón no se lee.
  - Sin palabras solas en la última línea del titular.

Uso:  python3 clients/petra/armar-propuesta-sep2026.py
"""

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

RAIZ = Path(__file__).resolve().parents[2]
FUENTES = RAIZ / "public" / "assets" / "fonts"
FOTOS = Path(__file__).parent / "material"
SALIDA = RAIZ / "out" / "petra" / "20260910_propuesta-mensajes"

DISPLAY = FUENTES / "BodoniModa.ttf"
UTIL = FUENTES / "Montserrat.ttf"
# logotipo real de Petra, rasterizado del logo.svg de su sitio.
# Se usa el alfa y se rellena con la tinta de la pieza.
LOGO = FOTOS / "logo-negro.png"

OLIVA = (0x52, 0x58, 0x34)
CELESTE = (0xAA, 0xB9, 0xBE)
HUESO = (0xF2, 0xF0, 0xE4)
TINTA = (0x1C, 0x20, 0x13)

# ---------------------------------------------------------------- las 4 piezas

PIEZAS = [
    dict(
        id="P1-precio",
        nombre="El precio, dicho",
        fondo=OLIVA,
        tinta=HUESO,
        titular="UN FUNERAL COMPLETO, DESDE 52 UF",
        dato="URNA · FLORES · CARROZA · TRÁMITES · REGISTRO CIVIL",
        foto="italiana1.jpg",
        # Ópalo 1 en petrafuneraria.com/planes-de-servicios-funebres
    ),
    dict(
        id="P2-urgencia",
        nombre="Cuando ya pasó",
        fondo=OLIVA,
        tinta=HUESO,
        titular="RETIRO, VELORIO, TRÁMITES Y CEREMONIA",
        # la dirección completa se va al copy de Meta: en la gráfica no cabe
        # en una línea y partida en dos choca con el óvalo.
        dato="NOSOTROS COORDINAMOS TODO · PROVIDENCIA",
        foto="somos.jpg",
        foco=0.48,  # centra la puerta y saca la viga oscura del cielo
    ),
    dict(
        id="P3-valor",
        nombre="El valor no depende del ataúd",
        fondo=CELESTE,
        tinta=TINTA,
        titular="EL VALOR NO DEPENDE DEL ATAÚD",
        dato="ELIGES CADA COMPONENTE POR SEPARADO",
        # Canciller lenga, no el detalle de mimbre: si el titular habla del
        # ataúd, en la foto tiene que verse un ataúd. El detalle en primer
        # plano leía como una forma blanca abstracta.
        foto="cancillerlenga1.jpg",
        # frase textual de la página de planes de Petra
    ),
    dict(
        id="P4-anticipada",
        nombre="Así quiero el funeral",
        fondo=OLIVA,
        tinta=HUESO,
        titular="DEJA TU FUNERAL DECIDIDO EN TRES SESIONES",
        dato="SÍMBOLOS · MÚSICA · FLORES · EL TONO DE LA CEREMONIA",
        foto="cat-flores.jpg",
    ),
]

# ------------------------------------------------------------------- formatos
# ovalo = (x0, y0, x1, y1) de la caja del óvalo
FORMATOS = {
    "4x5": dict(
        w=1080, h=1350,
        titular_y=170, titular_px=78, titular_max_lineas=3,
        dato_px=25,
        ovalo=(190, 500, 890, 1120),
        logo_ancho=156, logo_base=1215,
        margen_x=110,
        seguro_arriba=0, seguro_abajo=135,   # feed: tercio inferior con respiro
    ),
    "9x16": dict(
        w=1080, h=1920,
        titular_y=320, titular_px=84, titular_max_lineas=4,
        dato_px=27,
        ovalo=(150, 690, 930, 1420),
        logo_ancho=168, logo_base=1530,
        margen_x=110,
        seguro_arriba=250, seguro_abajo=340,  # zonas seguras Reels/Stories
    ),
}


# ------------------------------------------------------------------ utilidades

def cargar(ruta, px):
    if not ruta.exists():
        sys.exit(f"✗ falta la tipografía {ruta}")
    return ImageFont.truetype(str(ruta), px)


def ancho(draw, texto, fuente, track=0.0):
    """Ancho real de una línea, con tracking en em."""
    if not track:
        return draw.textlength(texto, font=fuente)
    esp = track * fuente.size
    return sum(draw.textlength(c, font=fuente) for c in texto) + esp * (len(texto) - 1)


def escribir(draw, xy, texto, fuente, fill, track=0.0, centro_x=None):
    """Escribe con tracking. Si centro_x, centra la línea en ese eje."""
    x, y = xy
    if centro_x is not None:
        x = centro_x - ancho(draw, texto, fuente, track) / 2
    if not track:
        draw.text((x, y), texto, font=fuente, fill=fill)
        return
    esp = track * fuente.size
    for c in texto:
        draw.text((x, y), c, font=fuente, fill=fill)
        x += draw.textlength(c, font=fuente) + esp


def partir(draw, texto, fuente, ancho_max, track=0.0):
    """Corta en líneas y evita dejar una palabra sola al final."""
    palabras = texto.split()
    lineas, actual = [], ""
    for p in palabras:
        prueba = f"{actual} {p}".strip()
        if ancho(draw, prueba, fuente, track) <= ancho_max or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)

    # sin palabras solas en la última línea: baja una de la anterior
    if len(lineas) >= 2 and len(lineas[-1].split()) == 1:
        prev = lineas[-2].split()
        if len(prev) >= 3:
            baja = prev.pop()
            candidata = f"{baja} {lineas[-1]}"
            if ancho(draw, candidata, fuente, track) <= ancho_max:
                lineas[-2] = " ".join(prev)
                lineas[-1] = candidata
    return lineas


def ajustar(draw, texto, ruta_fuente, px, ancho_max, max_lineas, track=0.0):
    """Baja el cuerpo hasta que el titular quepa en max_lineas."""
    while px > 26:
        fuente = cargar(ruta_fuente, px)
        lineas = partir(draw, texto, fuente, ancho_max, track)
        if len(lineas) <= max_lineas:
            return fuente, lineas
        px -= 2
    return cargar(ruta_fuente, px), partir(draw, texto, cargar(ruta_fuente, px), ancho_max, track)


def foto_en_ovalo(base, ruta_foto, caja, foco=0.32):
    """Pega la foto recortada a 'cover' con viñeta ovalada. Nunca estira."""
    x0, y0, x1, y1 = caja
    cw, ch = x1 - x0, y1 - y0

    im = Image.open(ruta_foto).convert("RGB")
    w, h = im.size
    objetivo = cw / ch
    if w / h > objetivo:                      # sobra ancho: recorta a los lados
        nw = int(round(h * objetivo))
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:                                     # sobra alto: recorta arriba/abajo
        nh = int(round(w / objetivo))
        top = int((h - nh) * foco)            # foco vertical del recorte
        im = im.crop((0, top, w, top + nh))
    im = im.resize((cw, ch), Image.LANCZOS)

    # viñeta: sólida hasta el 56% del radio, desvanece hasta el borde
    yy, xx = np.mgrid[0:ch, 0:cw]
    dx = (xx - (cw - 1) / 2) / ((cw - 1) / 2)
    dy = (yy - (ch - 1) / 2) / ((ch - 1) / 2)
    d = np.sqrt(dx ** 2 + dy ** 2)
    a = np.clip((1.0 - d) / (1.0 - 0.66), 0.0, 1.0)
    a = a ** 1.15
    mascara = Image.fromarray((a * 255).astype("uint8"), "L")

    base.paste(im, (x0, y0), mascara)


def poner_logo(base, tinta, ancho_px, base_y, centro_x):
    """Pega el logotipo real de Petra teñido con la tinta de la pieza.

    Geometría medida sobre "Anuncio 9" de la propia cuenta: el logotipo va
    centrado, con 14,4 % del ancho de la pieza, y la punta del descendente
    de la p al 92,6 % de la altura.
    """
    logo = Image.open(LOGO).convert("RGBA")
    prop = logo.height / logo.width
    alto = int(round(ancho_px * prop))
    logo = logo.resize((ancho_px, alto), Image.LANCZOS)
    alfa = logo.split()[-1]
    tinte = Image.new("RGB", logo.size, tinta)
    base.paste(tinte, (int(centro_x - ancho_px / 2), base_y - alto), alfa)


# -------------------------------------------------------------------- armado

def armar(pieza, clave_formato):
    f = FORMATOS[clave_formato]
    lienzo = Image.new("RGB", (f["w"], f["h"]), pieza["fondo"])
    draw = ImageDraw.Draw(lienzo)
    centro = f["w"] / 2
    ancho_max = f["w"] - 2 * f["margen_x"]

    # 1 · titular
    fuente_tit, lineas = ajustar(
        draw, pieza["titular"], DISPLAY, f["titular_px"],
        ancho_max, f["titular_max_lineas"], track=0.005,
    )
    interlinea = fuente_tit.size * 1.14
    y = f["titular_y"]
    for linea in lineas:
        escribir(draw, (0, y), linea, fuente_tit, pieza["tinta"],
                 track=0.005, centro_x=centro)
        y += interlinea

    # 2 · dato duro (uno, y sólo uno)
    fuente_dato = cargar(UTIL, f["dato_px"])
    y += fuente_tit.size * 0.58
    for linea in partir(draw, pieza["dato"], fuente_dato, ancho_max, track=0.11):
        escribir(draw, (0, y), linea, fuente_dato, pieza["tinta"],
                 track=0.11, centro_x=centro)
        y += fuente_dato.size * 1.55

    # 3 · foto en óvalo
    caja = list(f["ovalo"])
    minimo = int(y + 40)
    if caja[1] < minimo:                      # el titular creció: baja el óvalo
        caja[1] = minimo
    foto_en_ovalo(lienzo, FOTOS / pieza["foto"], tuple(caja),
                  foco=pieza.get("foco", 0.32))

    # 4 · logotipo real de Petra
    poner_logo(lienzo, pieza["tinta"], f["logo_ancho"], f["logo_base"], centro)

    return lienzo


def con_zonas_seguras(im, clave_formato):
    """Copia de QA con las zonas seguras de Meta dibujadas encima."""
    f = FORMATOS[clave_formato]
    qa = im.convert("RGB").copy()
    capa = Image.new("RGBA", qa.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    rojo = (220, 60, 60, 70)
    if f["seguro_arriba"]:
        d.rectangle([0, 0, f["w"], f["seguro_arriba"]], fill=rojo)
    if f["seguro_abajo"]:
        d.rectangle([0, f["h"] - f["seguro_abajo"], f["w"], f["h"]], fill=rojo)
    qa = Image.alpha_composite(qa.convert("RGBA"), capa).convert("RGB")
    return qa


def main():
    if not FOTOS.exists():
        sys.exit(f"✗ falta la carpeta de material: {FOTOS}")

    hechas = []
    for clave in FORMATOS:
        (SALIDA / clave).mkdir(parents=True, exist_ok=True)
    (SALIDA / "_qa-zonas-seguras").mkdir(parents=True, exist_ok=True)

    for pieza in PIEZAS:
        for clave, f in FORMATOS.items():
            im = armar(pieza, clave)
            nombre = f"{pieza['id']}_{f['w']}x{f['h']}.jpg"
            destino = SALIDA / clave / nombre
            im.save(destino, quality=92, subsampling=0)
            hechas.append(destino)
            print(f"  ✓ {clave}/{nombre}")

            if f["seguro_arriba"] or f["seguro_abajo"]:
                qa = con_zonas_seguras(im, clave)
                qa.save(SALIDA / "_qa-zonas-seguras" / f"{pieza['id']}_{clave}_QA.jpg",
                        quality=86)

    # hoja de contacto para mirarlas todas juntas antes de mostrar
    th = []
    for p in PIEZAS:
        im = Image.open(SALIDA / "4x5" / f"{p['id']}_1080x1350.jpg")
        im.thumbnail((420, 420))
        th.append(im)
    W = sum(i.width for i in th) + 16 * (len(th) + 1)
    H = max(i.height for i in th) + 32
    hoja = Image.new("RGB", (W, H), (250, 249, 245))
    x = 16
    for i in th:
        hoja.paste(i, (x, 16))
        x += i.width + 16
    hoja.save(SALIDA / "_hoja-de-contacto.jpg", quality=90)

    print(f"\n{len(hechas)} piezas en {SALIDA}")


if __name__ == "__main__":
    main()

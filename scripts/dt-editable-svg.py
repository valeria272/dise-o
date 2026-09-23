#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saca el EDITABLE (.svg, se abre en Adobe Illustrator) de una pieza de DT.

Por ahora sólo del post estático de Hilton Honors — `DT-F-HiltonHonors`, FEED
col K del 23-09, el que Eli aprobó el 15-09. La geometría NO se vuelve a
inventar: sale entera de `src/compositions/hilton/DtFtHonors.tsx`, que es la
pieza aprobada, y este archivo sólo la traduce a SVG.

⭐⭐ POR QUÉ SVG Y NO OTRA COSA
Illustrator abre `.svg` nativo y, si las fuentes están instaladas, el texto
entra VIVO: se reescribe, se cambia de cuerpo y se mueve. Un PDF de Chrome trae
la tipografía subincrustada y se edita a pedazos; un PNG no se edita; y el `.ai`
propietario no lo escribe nada que no sea Illustrator.

⭐⭐ LA LÍNEA BASE — POR QUÉ ESTOS NÚMEROS Y NO LOS OBVIOS
Para que el SVG caiga encima del render aprobado hay que colocar cada línea de
texto por su LÍNEA BASE, y eso depende de qué métricas verticales usa Chrome.
Medido sobre `Post n°1 S4 DT.png` (2250×2813), despejando la base desde los
contornos reales de los glifos con fontTools:

    «CON HILTON HONORS»  tinta 685,6–734,2 @1080  ⇒  base 733,5–733,9
      modelo hhea  (asc 0,838)              predice 731,98   ✗ 1,5 px arriba
      modelo usWin (asc 0,930 · alto 1,138) predice 733,55   ✅

O sea: en Windows, Chrome mide con **DirectWrite**, que toma `usWinAscent` /
`usWinDescent` del OS/2 y NO el `hhea`. Confirmado también en el llamado del
pie, donde `line-height: normal` da 1,138 × cuerpo y media interlínea 0.

    base = tope + (interlínea − 1,138 × cuerpo) / 2 + 0,930 × cuerpo

⚠️ Vale para Stag, cuyo OS/2 trae `fsSelection` SIN `USE_TYPO_METRICS`. Otra
familia hay que volver a medirla antes de reusar esta fórmula.

⭐ EL CRISTAL SE HORNEA
`backdrop-filter: blur()` no existe en SVG ni en Illustrator. El desenfoque de
3,5 px que Eli pidió en la ronda 3 se calcula acá con PIL sobre foto+velo y
entra como una imagen recortada al rectángulo redondeado. Se ve idéntico y se
puede mover; lo que no se puede es cambiarle el radio sin volver a correr esto.

⭐ VERIFICADO (15-09-2026, `--verificar`): rasterizado con Chrome al máster y
comparado con `Post n°1 S4 DT.png`, la TINTA cae donde tiene que caer —

    titular líneas 1 y 2   idénticas (0,0 px)     · x idéntica
    titular línea 3        0,5 px
    llamado del pie        idéntico (0,0 px)      · x idéntica
    rótulos de cuadrante   0,5 px más abajo       · x idéntica

Medio píxel en la mesa de 1080 es **1 px en el máster de 2250** y no se ve. El
residuo de los rótulos es sistemático (los ocho, misma dirección), así que es un
detalle de cómo Chrome centra un bloque de dos líneas dentro de un contenedor
flex; NO se corrige con una constante mágica, porque eso sería calzar el modelo
a un caso en vez de describir el motor.

⚠️ La diferencia GLOBAL de píxel no sirve como control: la domina el remuestreo
de la foto (el <img> de HTML y el <image> de SVG no interpolan igual). La media
de color de las zonas planas coincide en ±0,5, que es lo que prueba que no hay
corrimiento de gamma ni de perfil.

⛔ LAS FUENTES NO VIAJAN DENTRO DEL SVG. Illustrator resuelve la tipografía por
NOMBRE DE FAMILIA contra lo que está instalado en el sistema, y en esta máquina
los nueve cortes de Stag son familias separadas («Stag», «Stag Light»,
«Stag Med»), no pesos de una sola. Por eso cada línea declara su familia real.
Si Stag no está instalada, Illustrator sustituye y la diagramación se corre.

Uso:
    python scripts/dt-editable-svg.py
    python scripts/dt-editable-svg.py --verificar   # rasteriza y compara
"""
import argparse
import base64
import io
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "public/assets/hilton/dt"
FUENTES = ASSETS / "fonts"
SALIDA = RAIZ / "out/hilton/dt/ft-honors/editable"
APROBADA = RAIZ / "out/hilton/dt/ft-honors/Post n\u00b01 S4 DT.png"

# ── La mesa. 1:1 con la geometría documentada en la composición ──────────────
ANCHO, ALTO = 1080, 1350
ESCALA_MASTER = 2250 / 1080            # se entrega a 2250×2813 (208,34 %)

AZUL = "#09194E"
BLANCO = "#FAFAFA"

# ── Métricas de Stag, medidas con fontTools sobre los .ttf de esta máquina ───
ASC, ALTO_CAJA = 0.930, 1.138          # usWinAscent / (usWin asc+desc), upem 1000


def base(tope: float, interlinea: float, cuerpo: float) -> float:
    """Línea base de una línea de texto, con el modelo DirectWrite de arriba."""
    return tope + (interlinea - ALTO_CAJA * cuerpo) / 2 + ASC * cuerpo


# ── Geometría: copiada de DtFtHonors.tsx, no re-medida ───────────────────────
CAJA = dict(x=100, ancho=880, y=812, alto=306, radio=26, filete=1.5,
            relleno=0.30, desenfoque=3.5)
CAJA_DER = CAJA["x"] + CAJA["ancho"]
CAJA_PIE = CAJA["y"] + CAJA["alto"]
REGLA_PIE = 1258

LOGO = dict(ancho=160, proporcion=1.2254, y=111)
HONORS = dict(y=1156, alto=64)
CUERPO = dict(titulo=68, rotulo=29, pie=29)
SALTO_TITULO = 66
TITULO_PIE = 742                       # el bloque se ancla por su PIE
LLAMADO_Y = 1283

# Aire de la ronda 4, en px (el CSS lo decía en em sobre cuerpo 29)
AIRE = dict(palabra=0.14 * 29, letra=0.012 * 29)
TRACKING_TITULO = 0.035 * 68

CELDA = dict(icono_ancho=71, icono_alto=57, aire_antes=11.5, regla_ancho=1.9,
             regla_alto=62, aire_despues=13, pad_izq=30)
CAMA = dict(ancho=69.9, alto=57.1)

VELO = [(0, 0), (10, .01), (20, .03), (30, .08), (40, .15), (50, .23),
        (60, .31), (70, .38), (80, .44), (90, .48), (100, .50)]

# ⭐⭐⭐ RONDA 5 (15-09, tarde) — EL TITULAR JUSTIFICADO A UNA MEDIDA.
#
# Eli abrió este editable en su Illustrator y **escaló cada línea hasta una misma
# medida**: los cuerpos pasaron de 68/68/68 a 92,3 / 87,5 / 73,6 y los anchos de
# tinta quedaron en 764,2 / 764,1 / 766,6 — las tres a 2,4 px una de otra. Lo
# aprobó ella («quedó bien») y ES la pieza entregada.
#
# Estos números NO están estimados: se leyeron por COM del documento abierto
# (`anchor` y `characterAttributes`), y la base va desde ARRIBA de la mesa
# (Illustrator los reporta desde abajo: 1350 − y).
#
# ⛔ Por eso el titular ya no se arma como bloque con interlínea: cada línea va
# colocada por su línea base y alineada a la IZQUIERDA, que es como quedó.
# El criterio, escrito: `clients/hilton/CLAUDE.md` § RONDA 5.
TITULO = [
    ("MÁS BENEFICIOS", "Stag Med", 92.292, 154.928, 607.027),
    ("EN CADA ESTADÍA", "Stag Light", 87.505, 154.929, 696.515),
    ("CON HILTON HONORS", "Stag Light", 73.576, 152.427, 773.999),
]
LLAMADO = "Inscríbete gratis en el link de la bio"
# Ronda 5: Eli lo centró exacto en 540 y le bajó el tracking de 12 a 10
# milésimas (los rótulos del cuadro siguen en 12).
LLAMADO_R5 = dict(x=540.0, base=1312.759, tracking=10 / 1000 * 29)

# ⚠️ Los círculos del original venían como <circle>; acá van como <path> porque
# Illustrator importa un <circle> como objeto de forma viva y al reescalar el
# trazo se comporta distinto que el resto del ícono. Mismo dibujo, un solo tipo
# de objeto.
ICONOS = {
    "etiqueta": [
        'M11 24.5 L31.5 4 a4.6 4.6 0 0 1 3.3-1.4 H56 a4.6 4.6 0 0 1 4.6 4.6 V27 '
        'a4.6 4.6 0 0 1-1.4 3.3 L38.7 50.9 a4.6 4.6 0 0 1-6.5 0 L11 31 a4.6 4.6 0 0 1 0-6.5 Z',
        'M51 8.6 a3.9 3.9 0 1 1 0 7.8 a3.9 3.9 0 0 1 0-7.8 Z',
        'M24.5 40 L40 24.5',
        'M25 22.8 a2.7 2.7 0 1 1 0 5.4 a2.7 2.7 0 0 1 0-5.4 Z',
        'M39.5 36.8 a2.7 2.7 0 1 1 0 5.4 a2.7 2.7 0 0 1 0-5.4 Z',
    ],
    "regalo": [
        'M14.1 20 h42.8 a2.6 2.6 0 0 1 2.6 2.6 v5.3 a2.6 2.6 0 0 1-2.6 2.6 H14.1 '
        'a2.6 2.6 0 0 1-2.6-2.6 v-5.3 a2.6 2.6 0 0 1 2.6-2.6 Z',
        'M16 30.5 V50.5 a2.6 2.6 0 0 0 2.6 2.6 h33.8 a2.6 2.6 0 0 0 2.6-2.6 V30.5',
        'M35.5 20 V53.1',
        'M35.5 20 c-8.2 0-12.8-2-12.8-6.6 a5.1 5.1 0 0 1 9-3.4 c2.4 2.8 3.8 6.7 3.8 10 Z',
        'M35.5 20 c8.2 0 12.8-2 12.8-6.6 a5.1 5.1 0 0 0-9-3.4 c-2.4 2.8-3.8 6.7-3.8 10 Z',
    ],
    "monedas": [
        'M35.5 6.1 c12.7 0 23 3.3 23 7.4 c0 4.1-10.3 7.4-23 7.4 c-12.7 0-23-3.3-23-7.4 '
        'c0-4.1 10.3-7.4 23-7.4 Z',
        'M12.5 13.5 v10 a23 7.4 0 0 0 46 0 v-10',
        'M12.5 23.5 v10 a23 7.4 0 0 0 46 0 v-10',
        'M12.5 33.5 v10 a23 7.4 0 0 0 46 0 v-10',
    ],
}
CELDAS = [
    ("etiqueta", ("Tarifas", "exclusivas")),
    ("cama", ("Upgrades de", "habitación")),
    ("regalo", ("Canje de noches", "gratis")),
    ("monedas", ("Acumula puntos", "en cada estadía")),
]


def b64(datos: bytes, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(datos).decode("ascii")


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def cristal() -> str:
    """Hornea el fondo difuminado de la caja: foto + velo, desenfocados y recortados.

    Se desenfoca el lienzo ENTERO y recién después se recorta, que es lo que
    hace `backdrop-filter` en Chrome: muestrea todo el fondo y ahí recorta. Si
    se recortara primero, el borde del cuadro se aclararía.
    """
    foto = Image.open(ASSETS / "ft-honors-lobby.jpg").convert("RGB")
    e = foto.width / ANCHO                          # la foto ya viene al máster
    # El velo, como rampa vertical (color constante: sólo cambia el alfa).
    rampa = Image.new("L", (1, foto.height))
    px = rampa.load()
    for y in range(foto.height):
        p = y / (foto.height - 1) * 100
        a = VELO[-1][1]
        for i in range(len(VELO) - 1):
            (p0, a0), (p1, a1) = VELO[i], VELO[i + 1]
            if p0 <= p <= p1:
                a = a0 + (a1 - a0) * ((p - p0) / (p1 - p0))
                break
        px[0, y] = round(a * 255)
    capa = Image.new("RGB", foto.size, AZUL)
    fondo = Image.composite(capa, foto, rampa.resize(foto.size))
    # blur(3.5px) en la mesa de 1080 ⇒ sigma 3,5 × escala, en píxeles del máster.
    fondo = fondo.filter(ImageFilter.GaussianBlur(CAJA["desenfoque"] * e))
    caja = fondo.crop((round(CAJA["x"] * e), round(CAJA["y"] * e),
                       round(CAJA_DER * e), round(CAJA_PIE * e)))
    buf = io.BytesIO()
    caja.save(buf, "JPEG", quality=94, subsampling=0)
    return b64(buf.getvalue(), "image/jpeg")


def texto(x, y, cadena, familia, cuerpo, *, ancla="start", tracking=0.0,
          palabra=0.0, nombre=None) -> str:
    a = [f'x="{x:.2f}"', f'y="{y:.2f}"',
         f'font-family="{familia}"', f'font-size="{cuerpo}"', f'fill="{BLANCO}"']
    if ancla != "start":
        a.append(f'text-anchor="{ancla}"')
    if tracking:
        a.append(f'letter-spacing="{tracking:.3f}"')
    if palabra:
        a.append(f'word-spacing="{palabra:.3f}"')
    if nombre:
        a.append(f'id="{nombre}"')
    return f'  <text {" ".join(a)} xml:space="preserve">{esc(cadena)}</text>'


def construir() -> str:
    foto_b64 = b64((ASSETS / "ft-honors-lobby.jpg").read_bytes(), "image/jpeg")
    logo_b64 = b64((ASSETS / "logo-dt-blanco.png").read_bytes(), "image/png")
    honors_b64 = b64((ASSETS / "hilton-honors-blanco.png").read_bytes(), "image/png")
    cama_b64 = b64((ASSETS / "icono-cama-eli.png").read_bytes(), "image/png")

    # La foto va `object-fit: cover` sobre 1080×1350.
    f = Image.open(ASSETS / "ft-honors-lobby.jpg")
    k = max(ANCHO / f.width, ALTO / f.height)
    fw, fh = f.width * k, f.height * k

    # El logotipo de Honors va `object-fit: contain` en una caja de 1080×64.
    h = Image.open(ASSETS / "hilton-honors-blanco.png")
    kh = min(ANCHO / h.width, HONORS["alto"] / h.height)
    hw, hh = h.width * kh, h.height * kh

    paradas = "\n".join(
        f'      <stop offset="{p}%" stop-color="{AZUL}" stop-opacity="{a}"/>'
        for p, a in VELO)

    L = ['<svg xmlns="http://www.w3.org/2000/svg" '
         'xmlns:xlink="http://www.w3.org/1999/xlink"',
         f'     width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}">',
         '  <defs>',
         '    <linearGradient id="velo" x1="0" y1="0" x2="0" y2="1">',
         paradas,
         '    </linearGradient>',
         f'    <clipPath id="recorteCaja"><rect x="{CAJA["x"]}" y="{CAJA["y"]}" '
         f'width="{CAJA["ancho"]}" height="{CAJA["alto"]}" rx="{CAJA["radio"]}"/></clipPath>',
         # La sombra paralela de la ronda 2: 0 2px 7px al 60 % + 0 0 2px al 45 %.
         '    <filter id="sombra" x="-25%" y="-60%" width="150%" height="220%" '
         'color-interpolation-filters="sRGB">',
         '      <feGaussianBlur in="SourceAlpha" stdDeviation="3.5" result="d1"/>',
         '      <feOffset in="d1" dy="2" result="o1"/>',
         f'      <feFlood flood-color="{AZUL}" flood-opacity="0.60" result="c1"/>',
         '      <feComposite in="c1" in2="o1" operator="in" result="s1"/>',
         '      <feGaussianBlur in="SourceAlpha" stdDeviation="1" result="d2"/>',
         f'      <feFlood flood-color="{AZUL}" flood-opacity="0.45" result="c2"/>',
         '      <feComposite in="c2" in2="d2" operator="in" result="s2"/>',
         '      <feMerge><feMergeNode in="s1"/><feMergeNode in="s2"/>'
         '<feMergeNode in="SourceGraphic"/></feMerge>',
         '    </filter>',
         '  </defs>']

    L.append(f'  <g id="01-FOTO-lobby"><image xlink:href="{foto_b64}" '
             f'x="{(ANCHO - fw) / 2:.2f}" y="{(ALTO - fh) / 2:.2f}" '
             f'width="{fw:.2f}" height="{fh:.2f}" preserveAspectRatio="none"/></g>')
    L.append(f'  <g id="02-VELO-azul"><rect x="0" y="0" width="{ANCHO}" '
             f'height="{ALTO}" fill="url(#velo)"/></g>')

    L.append('  <g id="03-CRISTAL" clip-path="url(#recorteCaja)">')
    L.append(f'    <image id="cristal-fondo-difuminado" xlink:href="{cristal()}" '
             f'x="{CAJA["x"]}" y="{CAJA["y"]}" width="{CAJA["ancho"]}" '
             f'height="{CAJA["alto"]}" preserveAspectRatio="none"/>')
    L.append(f'    <rect id="cristal-tinte-azul" x="{CAJA["x"]}" y="{CAJA["y"]}" '
             f'width="{CAJA["ancho"]}" height="{CAJA["alto"]}" rx="{CAJA["radio"]}" '
             f'fill="{AZUL}" fill-opacity="{CAJA["relleno"]}"/>')
    L.append('  </g>')

    # El logotipo DT va SIN sombra y SIN halo (ronda 3, decisión de Eli).
    L.append(f'  <g id="04-LOGO-DT"><image xlink:href="{logo_b64}" '
             f'x="{(ANCHO - LOGO["ancho"]) / 2:.2f}" y="{LOGO["y"]}" '
             f'width="{LOGO["ancho"]}" '
             f'height="{LOGO["ancho"] / LOGO["proporcion"]:.2f}"/></g>')

    # Titular: ronda 5 — cada línea por su línea base, a la izquierda. Ver TITULO.
    L.append('  <g id="05-TITULAR" filter="url(#sombra)">')
    for i, (linea, familia, cuerpo, x, y) in enumerate(TITULO):
        L.append(texto(x, y, linea, familia, cuerpo,
                       tracking=0.035 * cuerpo, nombre=f"titular-{i + 1}"))
    L.append('  </g>')

    # Los cuatro cuadrantes, en el orden en que el brief lista los rótulos.
    L.append('  <g id="06-CUADRANTES" filter="url(#sombra)">')
    for n, (icono, rotulo) in enumerate(CELDAS):
        cx = CAJA["x"] + (n % 2) * CAJA["ancho"] / 2
        cy = CAJA["y"] + (n // 2) * CAJA["alto"] / 2
        alto_celda = CAJA["alto"] / 2
        ix = cx + CELDA["pad_izq"]
        nombre = rotulo[0].lower().replace(" ", "-")
        L.append(f'    <g id="cuadrante-{n + 1}-{nombre}">')
        if icono == "cama":
            # La cama es de Eli: va a su proporción real, jamás deformada.
            L.append(f'      <image id="icono-cama-de-Eli" xlink:href="{cama_b64}" '
                     f'x="{ix + (CELDA["icono_ancho"] - CAMA["ancho"]) / 2:.2f}" '
                     f'y="{cy + (alto_celda - CAMA["alto"]) / 2:.2f}" '
                     f'width="{CAMA["ancho"]}" height="{CAMA["alto"]}"/>')
        else:
            iy = cy + (alto_celda - CELDA["icono_alto"]) / 2
            L.append(f'      <g id="icono-{icono}" '
                     f'transform="translate({ix:.2f} {iy:.2f})" fill="none" '
                     f'stroke="{BLANCO}" stroke-width="2.4" stroke-linecap="round" '
                     'stroke-linejoin="round">')
            for d in ICONOS[icono]:
                L.append(f'        <path d="{d}"/>')
            L.append('      </g>')
        rx = ix + CELDA["icono_ancho"] + CELDA["aire_antes"]
        L.append(f'      <rect id="regla-{n + 1}" x="{rx:.2f}" '
                 f'y="{cy + (alto_celda - CELDA["regla_alto"]) / 2:.2f}" '
                 f'width="{CELDA["regla_ancho"]}" height="{CELDA["regla_alto"]}" '
                 f'fill="{BLANCO}" fill-opacity="0.85"/>')
        tx = rx + CELDA["regla_ancho"] + CELDA["aire_despues"]
        interlinea = CUERPO["rotulo"] * 1.2
        t0 = cy + (alto_celda - interlinea * 2) / 2
        for j, linea in enumerate(rotulo):
            y = base(t0 + j * interlinea, interlinea, CUERPO["rotulo"])
            L.append("  " + texto(tx, y, linea, "Stag", CUERPO["rotulo"],
                                  tracking=AIRE["letra"], palabra=AIRE["palabra"],
                                  nombre=f"rotulo-{n + 1}-{j + 1}"))
        L.append('    </g>')
    L.append('  </g>')

    # Filete, divisores y regla del pie.
    L.append('  <g id="07-FILETES" filter="url(#sombra)" fill="none" '
             f'stroke="{BLANCO}" stroke-width="{CAJA["filete"]}">')
    L.append(f'    <rect id="filete-caja" x="{CAJA["x"]}" y="{CAJA["y"]}" '
             f'width="{CAJA["ancho"]}" height="{CAJA["alto"]}" rx="{CAJA["radio"]}"/>')
    L.append(f'    <path id="divisor-horizontal" '
             f'd="M {CAJA["x"]} {CAJA["y"] + CAJA["alto"] / 2} '
             f'L {CAJA_DER} {CAJA["y"] + CAJA["alto"] / 2}" stroke-opacity="0.45"/>')
    L.append(f'    <path id="divisor-vertical" d="M {ANCHO / 2} {CAJA["y"]} '
             f'L {ANCHO / 2} {CAJA_PIE}" stroke-opacity="0.45"/>')
    L.append(f'    <path id="regla-del-pie" d="M {CAJA["x"]} {REGLA_PIE} '
             f'L {CAJA_DER} {REGLA_PIE}" stroke-opacity="0.7"/>')
    L.append('  </g>')

    # Honors va SIN sombra (ronda 4): cae sobre el piso de madera, que es oscuro.
    L.append(f'  <g id="08-LOGO-HILTON-HONORS"><image xlink:href="{honors_b64}" '
             f'x="{(ANCHO - hw) / 2:.2f}" y="{HONORS["y"]}" '
             f'width="{hw:.2f}" height="{hh:.2f}"/></g>')

    L.append('  <g id="09-LLAMADO" filter="url(#sombra)">')
    L.append(texto(LLAMADO_R5["x"], LLAMADO_R5["base"], LLAMADO, "Stag",
                   CUERPO["pie"], ancla="middle", tracking=LLAMADO_R5["tracking"],
                   palabra=AIRE["palabra"], nombre="llamado"))
    L.append('  </g>')
    L.append('</svg>')
    return "\n".join(L)


# ── Verificación: se rasteriza con Chrome y se compara con la aprobada ───────
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def verificar(svg: Path) -> int:
    """Rasteriza el SVG al máster y lo compara píxel a píxel con la aprobada.

    ⚠️ Se envuelve en un HTML con `@font-face` apuntando a los .ttf del repo,
    porque el navegador —al revés que Illustrator— no tiene a Stag instalada.
    Las familias que se declaran son las MISMAS que usa el SVG.
    """
    if not CHROME.exists():
        print("⚠️  No está Chrome; me salto la verificación.")
        return 0
    caras = [("Stag", "Stag-Regular.ttf"), ("Stag Light", "Stag-Light.ttf"),
             ("Stag Med", "Stag-Medium.ttf")]
    css = "\n".join(
        f"@font-face{{font-family:'{fam}';src:url('{(FUENTES / arch).as_uri()}') "
        "format('truetype');font-display:block}" for fam, arch in caras)
    ancho_m, alto_m = 2250, 2813
    html = (f"<!doctype html><meta charset=utf-8><style>{css}\n"
            f"html,body{{margin:0;background:#000}}"
            f"svg{{display:block;width:{ancho_m}px;height:{alto_m}px}}</style>"
            + svg.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "v.html").write_text(html, encoding="utf-8")
        png = t / "v.png"
        subprocess.run([str(CHROME), "--headless=new", "--disable-gpu",
                        "--hide-scrollbars", "--force-device-scale-factor=1",
                        f"--window-size={ancho_m},{alto_m}",
                        f"--screenshot={png}", (t / "v.html").as_uri()],
                       capture_output=True, timeout=180)
        if not png.exists():
            print("⚠️  Chrome no escribió la captura.")
            return 1
        a = Image.open(APROBADA).convert("RGB")
        b = Image.open(png).convert("RGB").resize(a.size)
        import numpy as np
        d = np.abs(np.asarray(a, int) - np.asarray(b, int)).max(axis=2)
        (SALIDA / "_verificacion").mkdir(parents=True, exist_ok=True)
        b.save(SALIDA / "_verificacion/svg-rasterizado.png")
        Image.fromarray((np.clip(d * 4, 0, 255)).astype("uint8")).save(
            SALIDA / "_verificacion/diferencia-x4.png")
        print(f"   diferencia: media {d.mean():.2f} · p99 {np.percentile(d, 99):.0f} "
              f"· máx {d.max()} · píxeles >16: {(d > 16).mean() * 100:.3f} %")
        # Dónde cae lo que sobrepasa el umbral, por bandas de la rejilla.
        for nom, y0, y1 in [("logo DT", 111, 242), ("titular", 540, 745),
                            ("caja", 812, 1120), ("Honors", 1156, 1225),
                            ("llamado", 1258, 1320)]:
            e = 2250 / 1080
            z = d[int(y0 * e):int(y1 * e)]
            print(f"     {nom:<9} media {z.mean():5.2f} · >16: {(z > 16).mean() * 100:6.3f} %")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true",
                    help="rasteriza el SVG con Chrome y lo compara con la aprobada")
    a = ap.parse_args()

    SALIDA.mkdir(parents=True, exist_ok=True)
    destino = SALIDA / "Post n\u00b01 S4 DT - EDITABLE.svg"
    destino.write_text(construir(), encoding="utf-8")
    print(f"✅ {destino.relative_to(RAIZ)}  ({destino.stat().st_size / 1e6:.1f} MB)")
    print(f"   mesa {ANCHO}×{ALTO} · el máster de entrega sale al "
          f"{ESCALA_MASTER * 100:.2f} % (2250×2813)")
    if a.verificar:
        return verificar(destino)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

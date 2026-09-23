#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ST EMERGENCIA BETWEEN (S2) — ronda 18: los tres al mismo tamaño, dentro del
vidrio, y sitio para la caja de preguntas.

Eli, 07-09-2026 (y esta pieza la necesita HOY):

    «tienes que hacer que el café togo, el muffin y el croissant tengan medidas
     similares. Además que tienen que estar dentro del vidrio, porque es romper
     en caso de emergencia. Seguido, necesito que dejes espacio para que
     contenido pueda colocar una caja de preguntas.»

Tres correcciones, y las tres son de geometría:

**1. MEDIDAS SIMILARES.** La ronda 17 escalonaba los tres en profundidad con el
vaso de protagonista: 730 px de ancho contra 620 y 430. Eso era «jerarquía» leída
como tamaño, y no es lo que la pieza necesita — acá los tres son las tres
OPCIONES de una encuesta, así que tienen que pesar lo mismo. Ahora se dimensionan
por su lado mayor a ~280 px cada uno:

    vaso       alto 280 → ancho 203   (proporción 1,380)
    croissant  ancho 280 → alto 158   (proporción 0,565)
    muffin     ancho 280 → alto 236   (proporción 0,842)

**2. DENTRO DEL VIDRIO.** En la r17 el croissant iba adelantado 60 px y su canto
bajaba del borde del estante: se leía por delante del cristal, y en una caja de
«romper el vidrio» eso rompe el concepto. Ahora los tres van sobre una sola línea
de base dentro del nicho (x 746..1566 · y 810..2158) y nada sale de ahí.

**3. SITIO PARA LA CAJA DE PREGUNTAS.** La caja se compone al 51 % en vez del
96,5 %, así que el marco cierra en y=2531 y quedan **365 px lógicos de muro
limpio** (y 1215..1580) para que la CM ponga el sticker de preguntas sin taparla
— que es el reclamo original de esta pieza, de la ronda 4.

Historial de la ronda 17, que sigue valiendo:



Eli, 07-09-2026:

    «Para la historia de emergencia se ve pegoteada el togo, se ve de mala
     calidad el muffin, al igual que el croissant de queso y jamón. Tiene que
     verse atractivo visualmente, con una mejor jerarquía y hacerlo de manera
     atractivo, ya que son alimentos, son productos.»

Y antes, la frase que ordena todo el arreglo: **el concepto sirve, el problema es
la ejecución** — «se ve armada, no diseñada».

⛔⛔ 1. LA CAJA LA DIBUJÉ YO, Y POR ESO PARECÍA DIBUJADA

La ronda 16 construyó el contenedor con `ImageDraw` y degradados: polígonos para
el bisel, un `linspace` para el fondo del nicho, una tira plana de «piso». Mirado
al 300 % eso da exactamente lo que Eli vio:

  · la esquina del marco es un **degradado borroso**, no una arista biselada;
  · el «piso» es una **tira plana con canto recto**, así que los productos no
    apoyan en ninguna superficie — vuelve el defecto de la ronda 13 con otra cara;
  · el reflejo del vidrio deja una arista que se lee como un pliegue de papel.

⭐ Y el manual ya decía qué hacer, en la receta de vitrina de la ronda 13: **«el
contenedor se genera VACÍO»**. Yo me salté ese paso y lo dibujé. Generado con
Nano Banana Pro, el contenedor trae lo que no se puede pintar: marco macizo con
aristas de verdad y bisel que toma la luz, nicho con paredes que se van en
profundidad, **un estante de madera real donde apoyar**, vidrio con su reflejo, y
la barra inferior en blanco para el llamado.

    `ia-sept/emergencia-caja-r17.png`  (3072×5504, vacía, sin texto)

⭐⭐ 2. JERARQUÍA: LOS TRES YA NO VAN EN FILA

Eli pidió «mejor jerarquía». La ronda 16 los ponía en fila sobre una línea de
base, los tres al mismo plano: eso es un inventario, no una composición. El nicho
generado es vertical, así que ahora se usa la PROFUNDIDAD:

    el VASO al centro y al fondo — es el que lleva la marca, es el protagonista
    el CROISSANT delante a la izquierda, apoyado y adelantado
    el MUFFIN delante a la derecha, un poco más atrás que el croissant

Tres planos, tres tamaños, un solo estante. El vaso manda.

⭐⭐ 3. «MALA CALIDAD» DEL CROISSANT: HABÍA MATERIAL MEJOR EN LA CASA

El croissant salía de la sesión del 25-jul: tendido, con un blob de queso
desbordando que a 360 px se lee como un bulto pálido. Se cambia por el de la
sesión PROFESIONAL de platos (`croissant-h3-nobg.png`, recortado por
`between-croissant-recortar-r17.py`): partido, jamón y queso a la vista, luz de
estudio, de frente. Ver ese script para la medición.

⭐⭐ 4. «MALA CALIDAD» DEL MUFFIN: no hay otra toma, así que se REVELA de verdad

Medido, no hay muffin en ninguna otra sesión del cliente (`desayunos-ago2026` son
28 tomas de omelettes y tostadas; `platos-ene` no tiene ninguno). Así que hay que
trabajar el que hay, y venía muy corto:

    recorte crudo ......... mediana 74,8 · p95 129,1 · laplaciano 796
    montado en la r16 ..... mediana 92,5 · p95 167,2 · laplaciano **513**

O sea que mi propio montaje le **bajaba** el contraste local un 36 %. Y la
cápsula de papel es una mancha negra sin detalle. Acá el muffin pasa por
`abre_sombras()` —para que el papel deje de ser un agujero— y por `apetitoso()`
con mano larga, y **el remate de nitidez va DESPUÉS de escalar**, que es lo que
faltaba: afilar antes de reducir es tirar el trabajo.

⭐⭐ 5. «PEGOTEADO» EL VASO: el vidrio va DELANTE

El reflejo del vidrio viene pintado en la generación, así que al pegar los
productos encima quedaban **delante del cristal** — y un objeto que tapa el
vidrio de su propia vitrina se lee pegado, siempre. Se aísla el reflejo del
propio archivo (el EXCESO de luz respecto de la mediana de cada fila, la técnica
que ya está en el manual) y se vuelve a poner ENCIMA de los productos.

Más la receta completa de montaje, que ésa no cambia: apoyo medido por percentil
del contorno, sombra de contacto sobre la madera, sombra en la pared del fondo,
campo de luz del nicho y luz envolvente en el canto.

Salida: public/assets/hilton/between/ia-sept/emergencia-fondo-r18.png (2250×4000)
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from between_retoque import (apetitoso, hombro, luz_envolvente,  # noqa: E402
                             nitidez, revela, vivo)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = RAIZ / "public/assets/hilton/between"
CAJA = BASE / "ia-sept/emergencia-caja-r17.png"
SALIDA = BASE / "ia-sept/emergencia-fondo-r18.png"
PASOS = RAIZ / "out/hilton-between-r17/pasos"

W, H = 2250, 4000
ESC = 2250 / 1080          # el lienzo lógico de Remotion

# ── la caja generada, medida con cuadrícula sobre sus 3072×5504 ──────────────
# ⚠️ NO se usa la generación como lienzo completo. A escala 1:1 de ancho
# (factor 0,7324) el canto inferior del marco caía en y=3324 y `between-qa.py`
# marcaba **16 px dentro de la zona segura inferior de Meta** (que empieza en
# 3292). Se compone al 96,5 % sobre un muro del mismo crema, con sesgo hacia
# arriba: así la caja entra completa en la zona útil y queda además más aire
# abajo para el sticker de encuesta que pone la CM.
# ⭐ RONDA 18 — la escala sale de la CAJA DE PREGUNTAS, no del gusto.
# El marco de la generación mide 3780 px de alto. Para dejar 365 px lógicos de
# muro limpio abajo (y 1215..1580 del lienzo lógico) el marco tiene que cerrar en
# y=2531 del lienzo y abrir en y=604, o sea 1927 px:
#     FACTOR = 1927 / 3780 = 0,50979
# y de ahí los dos desplazamientos, para centrarlo en x:
#     360 · F + DESPL_X = 555   →  DESPL_X = 371
#     780 · F + DESPL_Y = 604   →  DESPL_Y = 206
FACTOR = 1927 / 3780
# ⚠️ Los desplazamientos se refieren al RECORTE de la caja, que arranca en
# (300, 720) de la generación — no a la generación completa. Con el marco en
# gen y 780..4560 y gen x 360..2600, y queriéndolo en el lienzo en y 604..2531 y
# x 555..1696:
#     (780 − 720) · F + DESPL_Y = 604   →  DESPL_Y = 573
#     (360 − 300) · F + DESPL_X = 555   →  DESPL_X = 524
DESPL_Y = 573
DESPL_X = 524


def g(v):
    """Pasa una medida de la generación al lienzo de salida.
    ⚠️ El recorte de la caja arranca en GEN_CAJA_CON_SOMBRA, así que se descuenta
    su origen: las cifras del nicho y del estante están medidas sobre la
    generación COMPLETA."""
    return int(round((v - 720) * FACTOR)) + DESPL_Y


def gx(v):
    return int(round((v - 300) * FACTOR)) + DESPL_X


#: leído sobre la generación
GEN_NICHO = (735, 1185, 2345, 3830)       # el hueco tras el vidrio
GEN_ESTANTE = (750, 3572, 2331, 3830)     # la madera donde se apoya
GEN_BARRA = (735, 3860, 2345, 4150)       # la banda en blanco del marco

NICHO = (gx(GEN_NICHO[0]), g(GEN_NICHO[1]), gx(GEN_NICHO[2]), g(GEN_NICHO[3]))
ESTANTE = (gx(GEN_ESTANTE[0]), g(GEN_ESTANTE[1]), gx(GEN_ESTANTE[2]), g(GEN_ESTANTE[3]))
BARRA = (gx(GEN_BARRA[0]), g(GEN_BARRA[1]), gx(GEN_BARRA[2]), g(GEN_BARRA[3]))

#: la línea de base va a MEDIA PROFUNDIDAD del estante, no en su canto de atrás
#: (lección de la r16: apoyado atrás se lee flotando sobre la tira clara)
# ⚠️ CORREGIDO tras la primera pasada: a +30 los productos SE SALÍAN del nicho —
# el croissant y el muffin bajaban del canto del estante (y=2789) y se metían en
# la barra del marco. Un producto que se sale de su vitrina no es un montaje, es
# un error. La base va dentro del estante y con margen para lo que cuelga por
# debajo del apoyo.
# ⚠️ Y se CALCULA desde el estante, no se escribe a mano: la primera vez quedó
# clavado en 2680 y al recomponer la caja al 96,5 % el estante se movió a
# 2450..2633 — el número viejo dejaba a los productos colgando por debajo del
# canto otra vez. Una cifra que depende de otra no se copia, se deriva.
PISO = int(ESTANTE[1] + (ESTANTE[3] - ESTANTE[1]) * 0.62)

# ── los tres productos: (archivo, ancho, centro x, adelanto de la base) ─────
# El VASO manda: al centro, al fondo y el más alto. Los dos alimentos delante,
# a distinta profundidad, solapándole la base.
# ⚠️ Anchos BAJADOS respecto de la primera pasada (700/660/430): el vaso ocupaba
# el 60 % del ancho del nicho y el croissant el 56 %, así que entre los dos no
# cabían y el croissant le tapaba «COFFEE & BAR» al vaso — que es justo el que
# lleva la marca y es el protagonista de la jerarquía.
# Los ADELANTOS escalonan la profundidad: el vaso al fondo, el muffin medio paso
# adelante y el croissant el más cerca de cámara.
# ⚠️ SEGUNDA CORRECCIÓN DE ESCALA: a 560/500/330 el grupo ocupaba sólo el 42 %
# del alto del nicho y volvía el defecto de la ronda 13 —«chicos y perdidos en un
# hueco alto»—. A 730/650/430 el grupo llena el estante de lado a lado (545..1695
# de un nicho de 538..1718) y sube al 55 % del alto, dejando arriba los 798 px que
# el titular necesita.
# ⚠️ TERCERA CORRECCIÓN: el vaso se va MÁS AL FONDO del estante (adelanto −60) y
# el croissant más adelante (+60). El motivo es de marca, no de gusto: con los dos
# a la misma profundidad el croissant le tapaba «COFFEE & BAR» al vaso, y el vaso
# es el que firma la pieza. Separados en profundidad, el logotipo entero queda por
# encima del canto del croissant.
# ⭐ RONDA 18: los tres al MISMO PESO, dimensionados por su lado mayor (~280 px),
# sobre UNA línea de base y los tres enteros dentro del nicho. Son las tres
# opciones de una encuesta: ninguno manda.
#   croissant  x  756..1036      vaso  x 1054..1257      muffin  x 1281..1561
#   el nicho va de 746 a 1566, así que nadie toca los cantos.
# ⚠️ Se igualan por ANCHO (265 px cada uno) y no por lado mayor. Igualando el
# ALTO el vaso quedaba en 203 px de ancho y **su logotipo impreso dejaba de
# leerse** — y el logotipo del vaso es lo que firma la pieza. Con el ancho igual
# los tres pesan lo mismo en la fila y el vaso conserva su marca legible.
#   croissant  750..1015      vaso  1023..1288      muffin  1296..1561
#   el nicho va de 746 a 1566: nadie toca los cantos, todos DENTRO del vidrio.
PRODUCTOS = [
    ("recortes/croissant-h3-nobg.png",       265,  882,  14),
    ("togo-vaso-real-nobg.png",              265, 1155,   0),
    ("recortes/muffin-chocolate-limpio.png", 265, 1428,   8),
]


def apoyo(fig, pct=72.0):
    """La fila del recorte que cae sobre la línea de base — su apoyo REAL.
    Ver `between-emergencia-r16.py` para la medición que lo justifica: en el
    croissant el `bbox` inferior y el apoyo se separaban 85 px."""
    a = np.asarray(fig.getchannel("A"))
    al, an = a.shape
    op = a > 40
    cols = np.where(op.any(axis=0))[0]
    if len(cols) < 24:
        return al - 1
    x0, x1 = int(cols[0]), int(cols[-1])
    m0, m1 = int(x0 + (x1 - x0) * 0.15), int(x0 + (x1 - x0) * 0.85)
    idx = np.arange(al)
    bajos = [int(idx[op[:, x]][-1]) for x in range(m0, max(m1, m0 + 1))
             if op[:, x].any()]
    return int(np.percentile(np.array(bajos), pct)) if len(bajos) >= 16 else al - 1


def abre_sombras(im, fuerza=0.34, corte=0.46):
    """Levanta los medios bajos y deja quietos el negro puro y las altas.
    Es la del carrusel To Go; acá sirve para que la cápsula de papel del muffin
    deje de ser un agujero negro sin detalle."""
    a = np.asarray(im.convert("RGB")).astype(np.float32) / 255.0
    lum = a.mean(axis=2, keepdims=True)
    peso = np.clip(1.0 - lum / corte, 0.0, 1.0) * np.clip(lum / 0.05, 0.0, 1.0)
    a = np.clip(a + fuerza * peso * (corte - lum) * 1.5, 0.0, 1.0)
    return Image.fromarray((a * 255).astype(np.uint8))


#: la caja con su sombra, dentro de la generación
GEN_CAJA_CON_SOMBRA = (300, 720, 2820, 4780)


def fondo():
    """El muro sale de la PROPIA generación, y la caja se pega encima con el
    canto difuminado.

    ⛔⛔ La primera pasada rellenaba el lienzo con el color medio de la pared y
    pegaba la generación entera encima. Eso dejaba un **RECTÁNGULO VISIBLE**: un
    color plano no reproduce el degradado suave que tiene la pared de la
    generación, así que el empalme se veía como un parche — el peor delator
    posible, y justo el defecto que esta pieza venía arrastrando.

    Ahora el muro se construye escalando la MISMA generación para que cubra el
    lienzo (su pared, con su degradado y su grano) y la caja se recorta de una
    segunda copia a la escala que toca, con un alfa difuminado en el canto. Los
    dos tonos coinciden por construcción, porque salen del mismo archivo.
    """
    im = Image.open(CAJA).convert("RGB")

    # 1. el MURO: la generación escalada a cubrir, y desenfocada para que no
    #    aparezca una segunda caja de fondo.
    fac_muro = max(W / im.width, H / im.height)
    muro = im.resize((int(im.width * fac_muro) + 1, int(im.height * fac_muro) + 1),
                     Image.LANCZOS)
    # se toma una banda de pared LIMPIA (el flanco izquierdo) y se estira: así no
    # queda el marco fantasma del propio archivo detrás de la caja.
    banda = muro.crop((0, 0, int(muro.width * 0.09), muro.height)).resize(
        (W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(60))
    lienzo = banda

    # 2. la CAJA con su sombra, a la escala de esta ronda
    cx0, cy0, cx1, cy1 = GEN_CAJA_CON_SOMBRA
    caja = im.crop((cx0, cy0, cx1, cy1))
    an = int(round(caja.width * FACTOR))
    al = int(round(caja.height * FACTOR))
    caja = caja.resize((an, al), Image.LANCZOS)

    # alfa con el canto difuminado: sin esto el recorte deja borde recto
    m = Image.new("L", (an, al), 0)
    d = ImageDraw.Draw(m)
    b = 26
    d.rectangle([b, b, an - b, al - b], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(b * 0.55))

    lienzo.paste(caja, (DESPL_X, DESPL_Y), m)
    print(f"   muro desde la propia generación · caja {an}×{al} en "
          f"({DESPL_X},{DESPL_Y}) con canto difuminado {b} px")
    return lienzo


def campo_de_luz(al, an, y0):
    """El gradiente de luz del nicho, medido sobre la propia generación: de
    arriba (en penumbra) al estante (iluminado). Suelo en 0,82 — por debajo el
    chocolate del muffin se convierte en mancha, y eso ya pasó en la ronda 13."""
    a0 = (y0 - NICHO[1]) / max(NICHO[3] - NICHO[1], 1)
    a1 = (y0 + al - NICHO[1]) / max(NICHO[3] - NICHO[1], 1)
    g0 = 0.82 + 0.30 * np.clip(a0, 0, 1)
    g1 = 0.82 + 0.30 * np.clip(a1, 0, 1)
    v = np.linspace(g0, g1, al)[:, None]
    lat = np.linspace(0.97, 1.05, an)[None, :]     # la luz entra por la derecha
    return np.clip(v * lat, 0.75, 1.14)[..., None]


def reflejo_del_vidrio(im):
    """Aísla el reflejo del cristal del PROPIO archivo: el exceso de luz
    respecto de la mediana de cada fila dentro del nicho. Se vuelve a poner
    ENCIMA de los productos, porque lo que está delante va delante — y un
    producto que tapa el vidrio de su vitrina se lee pegado."""
    x0, y0, x1, y1 = NICHO
    z = np.asarray(im.crop((x0, y0, x1, y1)).convert("L")).astype(np.float32)
    med = np.median(z, axis=1, keepdims=True)
    exceso = np.clip(z - med, 0, None)
    exceso = cv2.GaussianBlur(exceso, (0, 0), 9)
    cap = np.clip(exceso / max(exceso.max(), 1.0) * 210, 0, 255).astype(np.uint8)
    print(f"   reflejo del vidrio aislado: máximo {exceso.max():.0f} de luz sobre "
          f"la mediana de fila")
    return Image.fromarray(cap)


def pon_producto(lienzo, ruta, ancho, cx, adelanto):
    fig = Image.open(BASE / ruta).convert("RGBA")
    fig = fig.crop(fig.getchannel("A").getbbox())
    es_vaso = "vaso" in ruta
    es_muffin = "muffin" in ruta

    # ── el producto se REVELA antes de montarlo, y el envase NO se toca
    rgb = fig.convert("RGB")
    if es_vaso:
        rgb = revela(rgb, medios=None, negros=0.006, contraste=1.03, calidez_max=6.0)
    else:
        if es_muffin:
            # ⚠️ La cápsula de papel es un agujero negro y hay que abrirla, pero
            # a fuerza 0,34 + claridad 0,62 el muffin salió GRIS: `apetitoso()`
            # con la claridad alta desatura, y sobre un objeto que ya es marrón
            # oscuro eso lo convierte en un bulto de plomo. Se abre menos, se le
            # da CUERPO (contraste) en vez de claridad, y se le devuelve el color
            # con `vivo()`, que es lo que hace que el chocolate se lea chocolate.
            rgb = abre_sombras(rgb, fuerza=0.18)
            rgb = apetitoso(rgb, claridad=0.34, cuerpo=1.20, calor=6.0)
            rgb = vivo(rgb, vibrancia=0.32)
        else:
            rgb = apetitoso(rgb, claridad=0.52, cuerpo=1.12, calor=5.0)
            rgb = vivo(rgb, vibrancia=0.16)
    fig = Image.merge("RGBA", (*rgb.split(), fig.getchannel("A")))

    an = ancho
    al = int(round(an * fig.height / fig.width))
    # ⚠️ alfa PREMULTIPLICADO antes de escalar: sin esto el color de los píxeles
    # invisibles entra en la mezcla y deja halo en el contorno (ronda 14).
    a4 = np.asarray(fig).astype(np.float32)
    alf = a4[..., 3:4] / 255.0
    a4[..., :3] *= alf
    fig = Image.fromarray(np.clip(a4, 0, 255).astype(np.uint8), "RGBA").resize(
        (an, al), Image.LANCZOS)
    b4 = np.asarray(fig).astype(np.float32)
    alf2 = np.clip(b4[..., 3:4] / 255.0, 1e-4, 1.0)
    b4[..., :3] /= alf2
    fig = Image.fromarray(np.clip(b4, 0, 255).astype(np.uint8), "RGBA")

    ap = apoyo(fig)
    base_y = PISO + adelanto
    x = cx - an // 2
    y = base_y - ap
    print(f"  · {Path(ruta).name:34s} {an}×{al} · apoyo fila {ap} · "
          f"y {y}..{y + al}")

    # ── ⭐ el remate de nitidez va DESPUÉS de escalar, no antes
    if not es_vaso:
        rgb2 = nitidez(fig.convert("RGB"), cantidad=0.50, radio=1.2)
        fig = Image.merge("RGBA", (*rgb2.split(), fig.getchannel("A")))

    # ── campo de luz del nicho sobre el propio recorte
    a = np.asarray(fig).astype(np.float32)
    a[..., :3] *= campo_de_luz(al, an, y)
    fig = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
    alfa = fig.getchannel("A")

    # ── 1. sombra en la PARED del fondo: en un nicho frontal es la que cuenta
    #    la profundidad. Corta, difusa, corrida a la izquierda (la luz entra
    #    por la derecha en esta generación).
    par = Image.new("L", (W, H), 0)
    par.paste(alfa, (x - int(an * 0.05), y - int(al * 0.02)))
    par = par.filter(ImageFilter.GaussianBlur(26))
    lienzo.paste(Image.new("RGB", (W, H), (40, 30, 22)), (0, 0),
                 par.point(lambda v: int(v * 0.30)))

    # ── 2. sombra de CONTACTO sobre la madera: elipse corta y densa, más ancha
    #    que la huella (si mide lo mismo, el objeto la tapa y no se ve).
    con = Image.new("L", (W, H), 0)
    dc = ImageDraw.Draw(con)
    # ⚠️ La elipse se CORRE HACIA EL ESPECTADOR (base_y + 10) y se achata: con el
    # centro justo en la línea de base el objeto la tapa casi entera y no se ve
    # ninguna sombra — que es el «flotan» que esta pieza arrastra desde la r13.
    # Corrida, asoma un reborde por delante del apoyo y ahí sí se lee el contacto.
    rx, ry = int(an * 0.60), 20
    dc.ellipse([x + an // 2 - rx, base_y + 10 - ry, x + an // 2 + rx, base_y + 10 + ry],
               fill=228)
    con = con.filter(ImageFilter.GaussianBlur(14))
    lienzo.paste(Image.new("RGB", (W, H), (34, 24, 16)), (0, 0), con)

    lienzo.paste(fig, (x, y), fig)

    # ── 3. luz envolvente en el canto: lo que impide que se lea como sticker
    trozo = lienzo.crop((x, y, x + an, y + al))
    lienzo.paste(luz_envolvente(trozo, fig, radio=24, fuerza=0.52), (x, y))
    return lienzo


def main():
    if not CAJA.exists():
        sys.exit(f"falta la caja generada: {CAJA}")
    lienzo = fondo()
    print(f"caja generada -> lienzo {lienzo.size}")
    print(f"  nicho   x {NICHO[0]}..{NICHO[2]}   y {NICHO[1]}..{NICHO[3]}")
    print(f"  estante y {ESTANTE[1]}..{ESTANTE[3]}   ·  línea de base y {PISO}")
    print(f"  barra   y {BARRA[1]}..{BARRA[3]}")
    print("  en el lienzo LÓGICO de 1080×1920:")
    print(f"    nicho x {NICHO[0]/ESC:.0f}..{NICHO[2]/ESC:.0f} "
          f"y {NICHO[1]/ESC:.0f}..{NICHO[3]/ESC:.0f}")
    print(f"    barra y {BARRA[1]/ESC:.0f}..{BARRA[3]/ESC:.0f}")

    cap_reflejo = reflejo_del_vidrio(lienzo)

    for ruta, anc, cx, ade in PRODUCTOS:
        lienzo = pon_producto(lienzo, ruta, anc, cx, ade)

    # ── el vidrio, ENCIMA de todo
    x0, y0, x1, y1 = NICHO
    lienzo.paste(Image.new("RGB", (x1 - x0, y1 - y0), (255, 252, 246)),
                 (x0, y0), cap_reflejo.point(lambda v: int(v * 0.42)))

    lienzo = Image.fromarray(np.clip(
        hombro(np.asarray(lienzo).astype(np.float32) / 255.0) * 255, 0, 255
    ).astype(np.uint8))

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(SALIDA)
    PASOS.mkdir(parents=True, exist_ok=True)
    lienzo.resize((W // 3, H // 3), Image.LANCZOS).save(
        PASOS / "emergencia-r18.jpg", quality=90)
    print(f"✓ {SALIDA.relative_to(RAIZ)}  {lienzo.size}")


if __name__ == "__main__":
    main()

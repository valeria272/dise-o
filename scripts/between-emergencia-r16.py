#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ST EMERGENCIA BETWEEN (S2) — ronda 16: la caja de «romper el vidrio», calcada
a la referencia que eligió Eli.

Eli, 07-09-2026, con la referencia en la mano
(https://cl.pinterest.com/pin/1040683426409551586/):

    «necesito que sean café TOGO, croissant jamón queso y muffin de chocolate,
     debe ser igual a la referencia con los textos del brief»

⛔ POR QUÉ NO SE AJUSTA LA ANTERIOR, SE REHACE LA GEOMETRÍA

La ronda 15 dejó `emergencia-fondo-r13.png`: una vitrina **horizontal y chata**
de tres compartimentos, con la caja ocupando 675 px de alto en un lienzo de
1.920 y los productos perdidos dentro de huecos altos. Medido sobre esa pieza:

    caja                      810 × 675 px  (proporción 1,20 : 1, apaisada)
    productos / alto del hueco       ~46 %
    vacío arriba de la caja          292 px sin nada
    vacío abajo de la caja           465 px

La referencia es lo contrario y por eso funciona: **una caja VERTICAL que manda
en el cuadro**, con el producto grande dentro y **el texto sobre el vidrio**, no
flotando en la pared. Sus proporciones, medidas sobre el pin (736 × 976):

    caja / ancho de la pieza         0,65
    caja                             1 : 1,37  (vertical)
    marco                            0,065 del ancho de la caja
    barra inferior / alto de caja    0,085
    titular                          sobre el vidrio, arriba, 2 líneas
    llamado                          en la BARRA del marco, no en la pared

Y ésta es la regla de proceso de la ronda 15 aplicada: el comentario se repitió
cuatro rondas, así que **no se toca un parámetro — se cambia el planteamiento**.

⭐ CÓMO SE ARMA (el recetario de vitrina del manual, en orden)

  1. la pared, plana y cálida, con viñeta muy suave;
  2. la caja: marco macizo en el café de marca con bisel real (canto claro
     arriba-izquierda, oscuro abajo-derecha), sombra proyectada blanda;
  3. el nicho **hundido**: fondo con gradiente —oscuro arriba para que el
     titular beige se lea, y CLARO hacia el piso para que el muffin de chocolate
     no se vaya a negro, que es el defecto que mató la ronda 13—;
  4. los tres productos son FOTOGRAFÍA REAL del cliente, agrupados en
     naturaleza muerta sobre UNA línea de base, no uno por compartimento:
     el vaso a la izquierda, el muffin a la derecha y el croissant tendido
     delante, que es como se apoya de verdad;
     ⚠️ el vaso es `togo-vaso-real-nobg.png`, NO `vaso-248*`: medido, el real
     tiene 2,50 % de canto suave contra 1,26 %, o sea el doble de transición y
     sin mordiscos (lección de la ronda 15);
  5. sombra de contacto por objeto + sombra en la PARED del fondo, que en un
     nicho frontal es la que cuenta la profundidad;
  6. campo de luz del nicho, con suelo en 0,80 — nunca 0,55;
  7. luz envolvente en el canto, que es lo que impide que se lea como sticker;
  8. y el vidrio ENCIMA: reflejo diagonal, canto brillante y dos destellos.

La barra inferior va **vacía** acá: el «¿CUÁL TOMARÍAS?» lo escribe Remotion con
la Raleway de la marca, igual que el titular. Este script entrega el escenario.

Salida: public/assets/hilton/between/ia-sept/emergencia-fondo-r16.png (2250×4000)
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from between_retoque import apetitoso, hombro, luz_envolvente, revela  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = RAIZ / "public/assets/hilton/between"
SALIDA = BASE / "ia-sept/emergencia-fondo-r16.png"

# ── lienzo ────────────────────────────────────────────────────────────────────
# Se compone en el espacio LÓGICO de Remotion (1080×1920) y se escribe a 2250×4000,
# que es el master 2× de la marca. Así las cifras de este archivo son las mismas
# que usa `StEmergencia` para poner el texto.
LOGICO = (1080, 1920)
ESC = 2250 / 1080          # 2,08333…
W, H = 2250, 4000

def e(v):
    """Pasa una medida del espacio lógico al lienzo de salida."""
    return int(round(v * ESC))

# ── la caja, en espacio lógico ────────────────────────────────────────────────
# ⚠️ LA PROPORCIÓN NO SE COPIA TAL CUAL, Y ESTÁ RAZONADO.
# La caja de la referencia mide 0,65 del ancho y 1 : 1,37, porque dentro lleva UN
# solo producto centrado. Acá el brief pide TRES —café, salado y dulce— y encima
# la encuesta le pide al seguidor que elija uno, así que los tres tienen que
# reconocerse. Con el ancho de la referencia el nicho queda en 608 px y los tres
# productos entran a 205 px cada uno: chicos y apretados, que es justo el defecto
# de la ronda 13. Se ensancha la caja a 0,759 del lienzo y se baja el alto, y con
# eso el nicho pasa a 728 px y el vaso entra a 250.
# ⚠️ SEGUNDA CORRECCIÓN, y salió del lado a lado con la referencia — el control
# que el método pide y que ninguna ronda anterior de esta pieza hizo.
# Con la caja en 820×1010 arrancando en y=276, quedaban **634 px de pared muerta
# abajo** (el 33 % del lienzo) y la caja se leía chica y desplazada hacia arriba,
# mientras en la referencia la caja MANDA en el cuadro y está centrada. Ahora la
# caja se centra en la zona útil de Meta (268..1580, eje 924) y crece:
#   ancho  868 → 0,804 del lienzo (la ref: 0,72; acá va más porque son 3 productos)
#   alto  1110 → 1 : 1,279
CAJA_X0, CAJA_X1 = 106, 974            # 868 de ancho, centrada
CAJA_Y0, CAJA_Y1 = 320, 1430           # 1110 de alto, centrada en la zona útil
MARCO = 46                             # 0,053 del ancho de la caja
BARRA = 114                            # la barra del llamado
LABIO = 16                             # el canto del marco que queda bajo la barra

# el nicho: lo que queda dentro del marco, por encima de la barra
NICHO_X0, NICHO_X1 = CAJA_X0 + MARCO, CAJA_X1 - MARCO          # 176 .. 904  (728)
NICHO_Y0 = CAJA_Y0 + MARCO                                     # 322
NICHO_Y1 = CAJA_Y1 - LABIO - BARRA                             # 1172  (850 de alto)
PISO_ALTO = 54                         # la tira de piso visible del nicho
# ⚠️ La línea de base va a MEDIA PROFUNDIDAD del piso, no en su canto de atrás.
# Con la base en el fondo del piso los tres quedan detrás de la tira clara y se
# leen flotando sobre ella — es el mismo defecto de la ronda 13 con otra cara.
PISO = NICHO_Y1 - 22                   # la línea de base de los tres productos

# la barra del marco donde va «¿CUÁL TOMARÍAS?»
BARRA_Y0, BARRA_Y1 = NICHO_Y1, NICHO_Y1 + BARRA                # 1172 .. 1272

# ── paleta ───────────────────────────────────────────────────────────────────
PARED = (238, 226, 208)                # crema cálido de la marca
MARCO_C = (103, 91, 73)                # #675b49, el café de BETWEEN
MARCO_LUZ = (129, 116, 96)             # bisel iluminado
MARCO_SOMBRA = (76, 66, 52)            # bisel en sombra
# ⚠️ El interior del nicho iba en (92,80,65) → (168,150,126): un pardo OLIVA y
# desaturado, del mismo valor que el marco. En el lado a lado con la referencia
# la caja se leía como una sola masa café y los productos salían apagados —el
# muffin de chocolate se fundía con el fondo—. La referencia funciona porque el
# interior es un color RICO y el marco CONTRASTA con él.
# Con la paleta de BETWEEN (beige + café) el contraste no puede ser de matiz, así
# que se hace de VALOR y de TEMPERATURA: espresso profundo arriba (donde va el
# titular beige) y caramelo cálido abajo (donde apoyan los tres productos).
NICHO_ALTO = (74, 57, 43)              # espresso: el titular beige se lee limpio
NICHO_BAJO = (178, 150, 116)           # caramelo cálido: el chocolate no se va a negro
PISO_C = (156, 125, 88)                # el piso del nicho, madera cálida


def rect(dib, caja, color, radio=0):
    if radio:
        dib.rounded_rectangle(caja, radius=radio, fill=color)
    else:
        dib.rectangle(caja, fill=color)


def pared():
    """Pared plana con viñeta muy suave: plana no es lo mismo que muerta."""
    im = Image.new("RGB", (W, H), PARED)
    a = np.asarray(im).astype(np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    cx, cy = W / 2, H * 0.42
    r = np.sqrt(((xx - cx) / (W * 0.78)) ** 2 + ((yy - cy) / (H * 0.72)) ** 2)
    # 1,0 en el centro → 0,90 en los cantos. Apenas se ve, y quita el aire de PNG plano.
    k = np.clip(1.0 - 0.10 * np.clip(r, 0, 1.6) ** 1.6, 0.86, 1.0)[..., None]
    return Image.fromarray(np.clip(a * k, 0, 255).astype(np.uint8))


def sombra_de_la_caja(lienzo):
    """Sombra proyectada de la caja sobre la pared. Luz desde arriba-izquierda,
    así que cae hacia abajo-derecha. Blanda y corta: la caja está pegada al muro."""
    cap = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(cap)
    dx, dy = e(14), e(20)
    d.rounded_rectangle(
        [e(CAJA_X0) + dx, e(CAJA_Y0) + dy, e(CAJA_X1) + dx, e(CAJA_Y1) + dy],
        radius=e(8), fill=150,
    )
    cap = cap.filter(ImageFilter.GaussianBlur(e(26)))
    tinta = Image.new("RGB", (W, H), (96, 82, 66))
    return Image.composite(tinta, lienzo, cap.point(lambda v: int(v * 0.55)))


def marco_con_bisel(lienzo):
    """El marco: no es un rectángulo de color, es un sólido con canto.
    El bisel se dibuja como cuatro trapecios — arriba/izquierda iluminados,
    abajo/derecha en sombra— y eso es lo que le da cuerpo."""
    d = ImageDraw.Draw(lienzo)
    X0, Y0, X1, Y1 = e(CAJA_X0), e(CAJA_Y0), e(CAJA_X1), e(CAJA_Y1)
    d.rounded_rectangle([X0, Y0, X1, Y1], radius=e(8), fill=MARCO_C)

    # el chaflán exterior, 6 px lógicos: claro arriba e izquierda
    ch = e(6)
    d.polygon([(X0, Y0), (X1, Y0), (X1 - ch, Y0 + ch), (X0 + ch, Y0 + ch)], fill=MARCO_LUZ)
    d.polygon([(X0, Y0), (X0 + ch, Y0 + ch), (X0 + ch, Y1 - ch), (X0, Y1)], fill=MARCO_LUZ)
    d.polygon([(X1, Y0), (X1, Y1), (X1 - ch, Y1 - ch), (X1 - ch, Y0 + ch)], fill=MARCO_SOMBRA)
    d.polygon([(X0, Y1), (X1, Y1), (X1 - ch, Y1 - ch), (X0 + ch, Y1 - ch)], fill=MARCO_SOMBRA)
    return lienzo


def nicho(lienzo):
    """El hueco hundido: gradiente vertical + piso de madera + el chaflán interior
    invertido (oscuro arriba, claro abajo) que es lo que lo hunde de verdad."""
    x0, y0, x1, y1 = e(NICHO_X0), e(NICHO_Y0), e(NICHO_X1), e(NICHO_Y1)
    an, al = x1 - x0, y1 - y0

    # el fondo del nicho: oscuro arriba (para el titular beige), claro abajo
    # (para que el chocolate del muffin no se vaya a negro — lección de la r13)
    g = np.linspace(0.0, 1.0, al)[:, None] ** 0.78
    alto = np.array(NICHO_ALTO, np.float32)
    bajo = np.array(NICHO_BAJO, np.float32)
    fondo = alto[None, None, :] * (1 - g[..., None]) + bajo[None, None, :] * g[..., None]
    fondo = np.repeat(fondo, an, axis=1)

    # el piso, una tira de madera al pie
    hp = e(PISO_ALTO)
    piso = np.array(PISO_C, np.float32)[None, None, :] * np.ones((hp, an, 1), np.float32)
    # el piso se aclara hacia el frente
    gp = np.linspace(0.86, 1.06, hp)[:, None, None]
    fondo[al - hp:al] = np.clip(piso * gp, 0, 255)

    lienzo.paste(Image.fromarray(np.clip(fondo, 0, 255).astype(np.uint8)), (x0, y0))

    # chaflán interior: sombra arriba/izquierda, luz abajo/derecha → hunde
    cap = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(cap)
    ci = e(9)
    d.polygon([(x0, y0), (x1, y0), (x1 - ci, y0 + ci), (x0 + ci, y0 + ci)], fill=190)
    d.polygon([(x0, y0), (x0 + ci, y0 + ci), (x0 + ci, y1 - ci), (x0, y1)], fill=140)
    cap = cap.filter(ImageFilter.GaussianBlur(e(3)))
    lienzo.paste(Image.new("RGB", (W, H), (44, 37, 29)), (0, 0), cap)

    cap2 = Image.new("L", (W, H), 0)
    d2 = ImageDraw.Draw(cap2)
    d2.polygon([(x1, y0), (x1, y1), (x1 - ci, y1 - ci), (x1 - ci, y0 + ci)], fill=70)
    cap2 = cap2.filter(ImageFilter.GaussianBlur(e(3)))
    lienzo.paste(Image.new("RGB", (W, H), (206, 188, 160)), (0, 0), cap2)
    return lienzo


def barra(lienzo):
    """La barra del marco donde Remotion escribirá el llamado. Va VACÍA:
    el texto lo pone la tipografía de la marca, no este script."""
    d = ImageDraw.Draw(lienzo)
    x0, x1 = e(NICHO_X0), e(NICHO_X1)
    y0, y1 = e(BARRA_Y0), e(BARRA_Y1)
    d.rectangle([x0, y0, x1, y1], fill=MARCO_C)
    # un filete claro arriba, que la separa del nicho como en la referencia
    d.rectangle([x0, y0, x1, y0 + e(3)], fill=MARCO_LUZ)
    return lienzo


# ── los productos ────────────────────────────────────────────────────────────
# ancho lógico de cada uno; el alto sale del ratio real del recorte, nunca a ojo
# Naturaleza muerta triangular sobre UNA línea de base: el vaso —el más alto—
# ancla a la izquierda, el muffin cierra a la derecha y el croissant va TENDIDO
# delante, que es como se apoya de verdad, con la base 28 px adelantada para que
# se lea en primer plano. Los solapes son simétricos (65 y 60 px) para que el
# grupo se lea como un grupo y no como tres objetos en fila.
PRODUCTOS = [
    # (archivo, ancho lógico, centro x lógico, adelanto de la base en px lógicos)
    ("togo-vaso-real-nobg.png",                  290, 330,  0),
    ("recortes/muffin-chocolate-limpio.png",     280, 782,  0),
    ("recortes/croissant-jamon-queso-limpio.png", 320, 545, 30),
]
# ⚠️ Los anchos subieron un 20 % respecto de la primera pasada de esta ronda
# (250/240/320): con los de antes el grupo ocupaba el 45 % del alto del nicho y
# quedaba una banda vacía en el medio del vidrio.
# ⚠️ Y el croissant BAJÓ de 384 a 320 después de mirar el lado a lado: a 384 su
# punta cruzaba por delante del muffin y le tapaba media cápsula de papel, así
# que el dulce dejaba de reconocerse — y en esta pieza los tres productos son las
# tres opciones de la encuesta, o sea que tienen que reconocerse los tres.
# Solapes medidos ahora: 90 px con el vaso y 63 px con el muffin. El croissant se
# lee DELANTE del grupo, no apoyado encima de él.


def apoyo(fig, pct=72.0):
    """⭐ Devuelve la fila del recorte que tiene que caer sobre la línea de base
    — su APOYO real, medido, no el canto de su caja.

    El croissant de jamón queso es el caso que lo obliga: su píxel más bajo es el
    queso derretido del extremo izquierdo. Alinear el `bbox` inferior a la línea
    de base apoya sólo el queso y deja la masa en el aire, y eso se lee igual que
    el defecto «los productos flotan» de la ronda 13 con otra cara.

    Medido en este recorte:

        contorno inferior · máximo (el queso) ...... fila 1155
        contorno inferior · percentil 72 (la masa) . fila ~1070

    o sea **85 px de diferencia**: es exactamente lo que colgaba.

    Se toma un percentil alto del contorno inferior sobre el 70 % central de las
    columnas —los extremos son donde el objeto se adelgaza y mienten—. Así la
    masa apoya y el queso queda un poco por delante y por debajo del canto del
    piso, que es como se derrama de verdad.

    ⛔ Y por qué NO se gira: la primera versión ajustaba una recta al contorno y
    rotaba por su pendiente. El vaso salió a −14° y el croissant también, los dos
    tocando el tope — señal de ajuste malo. La base de un vaso es una ELIPSE, y
    ajustarle una recta a una curva da una pendiente inventada. Los tres
    productos se fotografiaron apoyados en una mesa: ya vienen derechos. Lo que
    estaba mal era el ancla, no el ángulo.
    """
    a = np.asarray(fig.getchannel("A"))
    al, an = a.shape
    op = a > 40
    cols = np.where(op.any(axis=0))[0]
    if len(cols) < 24:
        return al - 1
    x0, x1 = int(cols[0]), int(cols[-1])
    m0, m1 = int(x0 + (x1 - x0) * 0.15), int(x0 + (x1 - x0) * 0.85)
    idx = np.arange(al)
    bajos = []
    for x in range(m0, max(m1, m0 + 1)):
        v = idx[op[:, x]]
        if len(v):
            bajos.append(int(v[-1]))
    if len(bajos) < 16:
        return al - 1
    return int(np.percentile(np.array(bajos), pct))


def campo_de_luz(al, an):
    """Gradiente de luz del nicho. Suelo en 0,80: por debajo de eso el chocolate
    del muffin se convierte en una mancha negra (medido en la ronda 13)."""
    g = np.linspace(1.06, 0.80, al)[:, None]
    lat = np.linspace(1.04, 0.94, an)[None, :]      # luz desde la izquierda
    return np.clip(g * lat, 0.72, 1.10)[..., None]


def pon_producto(lienzo, ruta, ancho_l, cx_l, adelanto):
    fig = Image.open(BASE / ruta).convert("RGBA")
    fig = fig.crop(fig.getchannel("A").getbbox())

    # el producto se REVELA antes de montarlo. El vaso NO: subirle la claridad
    # le ensucia el kraft y le mueve el logotipo impreso.
    es_envase = "vaso" in ruta
    rgb = fig.convert("RGB")
    if not es_envase:
        rgb = apetitoso(rgb, claridad=0.50, cuerpo=1.08, calor=4.0)
    else:
        rgb = revela(rgb, medios=None, negros=0.006, contraste=1.03, calidez_max=6.0)
    fig = Image.merge("RGBA", (*rgb.split(), fig.getchannel("A")))

    an = e(ancho_l)
    al = int(round(an * fig.height / fig.width))
    fig = fig.resize((an, al), Image.LANCZOS)

    # ⭐ el ancla es el APOYO MEDIDO, no el canto de la caja del recorte
    ap = apoyo(fig)
    base_y = e(PISO + adelanto)
    x = e(cx_l) - an // 2
    y = base_y - ap
    print(f"  · {Path(ruta).name:44s} {an}×{al} px · apoyo en la fila {ap} "
          f"de {al} ({al - ap} px por debajo)")

    # campo de luz del nicho sobre el propio recorte
    a = np.asarray(fig).astype(np.float32)
    a[..., :3] *= campo_de_luz(al, an)
    fig = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")

    alfa = fig.getchannel("A")

    # 1. sombra en la PARED del fondo: en un nicho frontal es la que cuenta la
    #    profundidad. Corrida a la derecha y arriba, corta y difusa, al 30 %.
    par = Image.new("L", (W, H), 0)
    par.paste(alfa, (x + e(16), y - e(10)))
    par = par.filter(ImageFilter.GaussianBlur(e(13)))
    lienzo.paste(Image.new("RGB", (W, H), (58, 48, 37)), (0, 0),
                 par.point(lambda v: int(v * 0.30)))

    # 2. sombra de CONTACTO: elipse corta y densa bajo la base. Larga y suave
    #    levanta el objeto del piso.
    # ⚠️ la elipse va un poco MÁS ANCHA que la huella: si mide lo mismo, el
    # objeto la tapa entera y la sombra no se ve — parecía que no había.
    con = Image.new("L", (W, H), 0)
    dc = ImageDraw.Draw(con)
    rx, ry = int(an * 0.56), e(13)
    dc.ellipse([x + an // 2 - rx, base_y - ry, x + an // 2 + rx, base_y + ry], fill=215)
    con = con.filter(ImageFilter.GaussianBlur(e(8)))
    lienzo.paste(Image.new("RGB", (W, H), (46, 37, 28)), (0, 0), con)

    # 3. el producto
    lienzo.paste(fig, (x, y), fig)

    # 4. luz envolvente en el canto: sin esto se lee como sticker
    trozo = lienzo.crop((x, y, x + an, y + al))
    lienzo.paste(luz_envolvente(trozo, fig, radio=e(11), fuerza=0.50), (x, y))
    return lienzo


def vidrio(lienzo):
    """El vidrio va ENCIMA de los productos: lo que está delante, delante.
    Reflejo diagonal + canto brillante + dos destellos, como en la referencia."""
    x0, y0, x1, y1 = e(NICHO_X0), e(NICHO_Y0), e(NICHO_X1), e(NICHO_Y1)
    an, al = x1 - x0, y1 - y0

    # Reflejo diagonal. ⚠️ En la primera pasada iba a 52 con 9 px de desenfoque y
    # el canto de la banda se leía como un PLIEGUE, no como un reflejo: sobre el
    # gradiente oscuro del nicho una arista recta parece un doblez de papel.
    # Un reflejo de cristal no tiene canto — se baja la opacidad a la mitad y se
    # desenfoca cuatro veces más.
    cap = Image.new("L", (an, al), 0)
    d = ImageDraw.Draw(cap)
    d.polygon([(0, int(al * 0.16)), (int(an * 0.52), 0),
               (int(an * 0.80), 0), (0, int(al * 0.62))], fill=26)
    d.polygon([(0, int(al * 0.66)), (int(an * 0.20), int(al * 0.44)),
               (int(an * 0.30), int(al * 0.50)), (0, int(al * 0.80))], fill=13)
    cap = cap.filter(ImageFilter.GaussianBlur(e(36)))
    # ⚠️ la tinta tiene que medir lo MISMO que la máscara: pegar un lienzo
    # completo con una máscara del tamaño del nicho revienta con
    # «images do not match».
    lienzo.paste(Image.new("RGB", (an, al), (255, 252, 244)), (x0, y0), cap)

    # un velo general muy leve: es un cristal, no aire
    velo = Image.new("L", (an, al), 12)
    lienzo.paste(Image.new("RGB", (an, al), (240, 244, 250)), (x0, y0), velo)

    # canto brillante del vidrio contra el marco
    cap2 = Image.new("L", (W, H), 0)
    d2 = ImageDraw.Draw(cap2)
    d2.rectangle([x0, y0, x1, y1], outline=120, width=e(2))
    cap2 = cap2.filter(ImageFilter.GaussianBlur(e(1)))
    lienzo.paste(Image.new("RGB", (W, H), (255, 253, 247)), (0, 0), cap2)

    # Los dos destellos de la referencia. ⚠️ Dibujados con dos líneas de grosor
    # constante salían como signos «+» de tipografía. Un destello de vidrio es un
    # núcleo brillante con cuatro puntas que se AFINAN: se dibuja por tramos
    # decrecientes y se desenfoca, y entonces se lee como brillo y no como signo.
    for (px, py, r) in ((0.11, 0.28, 22), (0.85, 0.55, 15)):
        cap3 = Image.new("L", (W, H), 0)
        d3 = ImageDraw.Draw(cap3)
        cxp, cyp, rr = x0 + int(an * px), y0 + int(al * py), e(r)
        pasos = 7
        for i in range(pasos):
            f = 1.0 - i / pasos                    # 1 → 0 desde el centro
            largo = int(rr * f)
            grosor = max(1, int(e(3) * f))
            v = int(150 * (1 - f) + 60)
            d3.line([cxp - largo, cyp, cxp + largo, cyp], fill=v, width=grosor)
            d3.line([cxp, cyp - largo, cxp, cyp + largo], fill=v, width=grosor)
        d3.ellipse([cxp - e(2), cyp - e(2), cxp + e(2), cyp + e(2)], fill=210)
        cap3 = cap3.filter(ImageFilter.GaussianBlur(e(4)))
        lienzo.paste(Image.new("RGB", (W, H), (255, 255, 252)), (0, 0), cap3)
    return lienzo


def main():
    lienzo = pared()
    lienzo = sombra_de_la_caja(lienzo)
    lienzo = marco_con_bisel(lienzo)
    lienzo = nicho(lienzo)
    for ruta, anc, cx, ade in PRODUCTOS:
        lienzo = pon_producto(lienzo, ruta, anc, cx, ade)
    lienzo = vidrio(lienzo)
    lienzo = barra(lienzo)

    lienzo = hombro(np.asarray(lienzo).astype(np.float32) / 255.0)
    lienzo = Image.fromarray(np.clip(lienzo * 255, 0, 255).astype(np.uint8))

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(SALIDA)
    print(f"✓ {SALIDA.relative_to(RAIZ)}  {lienzo.size}")
    print(f"  caja lógica      x {CAJA_X0}..{CAJA_X1}   y {CAJA_Y0}..{CAJA_Y1}")
    print(f"  nicho (vidrio)   x {NICHO_X0}..{NICHO_X1}   y {NICHO_Y0}..{NICHO_Y1}")
    print(f"  barra del marco  y {BARRA_Y0}..{BARRA_Y1}")
    print(f"  línea de base    y {PISO}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · ST 28-09 «HUMOR | CAFÉ TO GO» — el vaso gigante, con foto real
========================================================================

Encargo de Eli (14-09-2026): «utiliza este vaso y esta foto […] solo que haz
que él esté cargando con el vaso gigante, la idea es que no se le vea el
rostro», más «ten en cuenta la referencia de la misma carpeta drive».

El brief de la grilla (col T, hoja STORIES, `gid=1367300884`) dice:

    «Imagen intervenida de una chica caminando con un vaso de café Between
     exageradamente grande, incluso más grande que ella. La chica debe verse
     haciendo esfuerzo por cargarlo, como si literalmente estuviera llevando
     "el peso" de sus ganas de café.»

⚠️ El brief dice «una chica» y Eli mandó la foto de un hombre. El titular
—«POV: / YO CARGANDO EL PESO / DE MIS GANAS DE CAFÉ»— es de primera persona y
no tiene género, así que la pieza se sostiene igual. Queda informado, no
resuelto: el brief es del cliente.

⭐ REFERENCIA: `raw/hilton/between/refs-s5/st1-ref-s5.jpg` (la que el propio
   cliente dejó en la fila REF). Una persona caminando abrazada a un vaso
   gigantesco que le tapa la cabeza, titular arriba sobre el fondo. Eso es lo
   que se replica: el vaso ES lo que oculta el rostro.

═══════════════════════════════════════════════════════════════════════════
NADA DE ESTA PIEZA ESTÁ GENERADO
═══════════════════════════════════════════════════════════════════════════
La versión anterior (ronda 26) era una escena de Nano Banana con el logotipo
estampado encima. Ésta no genera un solo píxel de producto ni de persona:

  · **La persona y el lugar** son `IMG_4175.HEIC` — la foto que mandó Eli, de
    la sesión de Sebastián del 09-09 16:34 (iPhone 16 Pro). Sale del local con
    el vaso real en la mano y la chaqueta al hombro. **El encuadre ya empieza
    bajo el mentón**, y encima el vaso gigante le tapa lo que queda: el rostro
    no se ve por dos motivos independientes.
  · **El vaso gigante** es `IMG_4150.HEIC` de la misma sesión: el packshot
    frontal del vaso GRANDE, con el logotipo real impreso y en perspectiva.
    No se estampa nada — el logotipo que se ve es tinta sobre cartón.
  · **La mano** que lo agarra son los dedos de la propia foto, recortados y
    puestos DELANTE del vaso para que se lea que lo carga.

⭐⭐ LO ÚNICO CONSTRUIDO ES EL FONDO QUE FALTABA, Y ESTÁ MEDIDO.
La foto termina en el mentón: sobre él no hay ni un píxel, y la referencia
necesita aire arriba para el titular y para la tapa del vaso. Ese aire se
fabrica con el **fondo real de la propia foto** —sus franjas laterales, que sí
llegan de arriba abajo— en mosaico con espejo y solape, no estirando una banda
(estirar deja rayas horizontales; se probó y se descartó). La costura se iguala
COLUMNA POR COLUMNA contra las primeras filas de la foto, así que no hay salto
de tono. Es fachada fuera de foco: el mismo material que ya está detrás de él.

⭐ EL VASO SE RE-ILUMINA, NO SE RECOLOREA A OJO.
`IMG_4150` está con sol de tarde (cartón R/G 1,46 · sat 0,61 · L 114) y la
escena es nublado plano (R/G 1,29 · sat 0,36 · L 148). El objetivo NO se
inventa: es el vaso chico que él lleva en la mano, que está en la misma foto y
bajo el mismo iluminante. Se mide ahí y se lleva el grande a esos números.

⛔ EL VASO DE ESTA SESIÓN ES EL GRANDE, y eso importa: no lleva anillo blanco
   en la base (ése es el chico). Ver `clients/hilton/CLAUDE.md § EL VASO TO GO`.

═══════════════════════════════════════════════════════════════════════════
GEOMETRÍA — por qué el lienzo es más ancho que la foto
═══════════════════════════════════════════════════════════════════════════
La foto es 3024×4032 (3:4) y la historia es 9:16. Si se recorta a 9:16 el
mentón queda a 0 % de altura y no cabe ni el titular ni la tapa. Para que el
orden de la referencia se pueda armar —titular · tapa · mentón— el mentón tiene
que caer cerca del 40 % de la altura, y eso obliga a que la foto ocupe ~60 % del
alto, o sea a dejarle margen también a los lados. De ahí el lienzo de
4200×7467: la foto va abajo y centrada, con 588 px de fondo a cada lado y 3435
arriba. Los 588 laterales son fachada desenfocada arriba y piso liso abajo:
material que el espejo desenfocado resuelve sin inventar nada.

El orden vertical, en el lienzo de 7467 (entre paréntesis, sobre 1920):
    972 (250)   arranca el titular — es la zona segura de Instagram
   3050 (784)   termina el bloque de texto
   3300 (848)   la tapa del vaso
   3435 (883)   el mentón: entra 135 px POR DEBAJO del filo de la tapa
   7467         el vaso sale por abajo del cuadro, como en la pieza aprobada

Uso:
    python scripts/between-s5-vaso-gigante.py
    python scripts/between-s5-vaso-gigante.py --vaso-ancho 2640 --tapa-top 3300
"""
from __future__ import annotations

import argparse
import os
import pathlib
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

SESION = RAIZ / "raw/hilton/between/vasos-togo-sep2026/jpg"
DESTINO_RAW = RAIZ / "raw/hilton/between/s5"
ASSET = RAIZ / "public/assets/hilton/between/s5/st-28-09-togo.jpg"

# ── la foto base: IMG_4175, la que mandó Eli ───────────────────────────────
FOTO = SESION / "IMG_4175.jpg"
# ── el vaso grande: IMG_4150, el packshot más nítido de las 39 ─────────────
VASO = SESION / "IMG_4150.jpg"

# Contornos del CUERPO del vaso en IMG_4150, ajustados sobre 16 filas.
# Son rectas: el vaso es un tronco de cono y la cámara está casi a su altura.
CUERPO_IZQ = lambda y: 387 + 0.128 * (y - 700)          # noqa: E731
CUERPO_DER = lambda y: 2307 - 0.0932 * (y - 1100)       # noqa: E731
# La BASE es una elipse medida: centro (1418, 3690), semiejes 648 × 62.
# El punto más bajo del vaso queda en y=3752.
BASE_CX, BASE_CY, BASE_RX, BASE_RY = 1418.0, 3690.0, 618.0, 62.0

# Cúpula de la tapa, medida columna a columna. A la izquierda el fondo es
# follaje oscuro y la luminancia no sirve: ahí el borde se sacó por croma
# (G−R), que separa el verde desenfocado del plástico negro.
TAPA_CUPULA_X = [420, 470, 550, 700, 850, 1000, 1200, 1400, 1600, 1800, 2000, 2150, 2250, 2305]
TAPA_CUPULA_Y = [410, 330, 260, 220, 210, 180, 155, 160, 165, 200, 195, 200, 178, 182]
# La ORLA es un anillo aparte que sobresale de la cúpula, y modelarla como
# parte de ella dejaba una esquina cuadrada arriba a la derecha.
ORLA_I_X, ORLA_I_TOP, ORLA_I_BOT = [264, 300, 360, 420], [625, 455, 435, 425], [660, 685, 697, 705]
ORLA_D_X, ORLA_D_TOP, ORLA_D_BOT = [2305, 2360, 2410, 2445], [408, 410, 418, 470], [650, 632, 610, 500]

# ── La mano: el grupo de dedos que en la foto envuelve el vaso chico ───────
MANO_CAJA = (330, 1400, 760, 1920)      # x0,y0,x1,y1 en la foto base

# ══════════════════════════════════════════════════════════════════════════
# EL CAMPO DE LUZ — la causa real de que el vaso se viera pegado
# ══════════════════════════════════════════════════════════════════════════
# Eli, ronda 27: «se ve pegoteado». No era el filo ni el recorte: era que el
# vaso traía OTRA LUZ. Medidos los dos perfiles de izquierda a derecha sobre
# el cuerpo, normalizados a su media:
#
#   · el vaso REAL de la escena (nublado plano, en su mano, misma foto) sube a
#     1,09 en u=0,14 y baja suave hasta 0,72 en el canto derecho — casi plano.
#   · `IMG_4150` (sol de tarde) arranca en **1,62** en el canto izquierdo y se
#     desploma a 0,93 en u=0,25.
#
# Ese 1,62 es un filo de sol de 80 px que en una escena nublada no existe, y
# es lo que el ojo lee como calcomanía. Se divide uno por otro y se corrige.
PERFIL_REAL = [0.945, 0.958, 1.061, 1.088, 1.090, 1.087, 1.086, 1.075, 1.076, 1.090,
               1.072, 1.054, 1.052, 1.055, 1.045, 1.044, 1.051, 1.053, 1.044, 1.024,
               1.037, 1.037, 1.047, 1.039, 1.027, 1.026, 1.035, 1.045, 1.046, 1.046,
               1.046, 1.046, 1.035, 1.041, 1.050, 1.045, 1.041, 1.041, 1.031, 1.031,
               1.036, 1.042, 1.042, 1.031, 1.028, 1.024, 1.014, 1.009, 1.000, 0.995,
               0.962, 0.933, 0.929, 0.913, 0.897, 0.874, 0.848, 0.824, 0.794, 0.763,
               0.720, 0.727, 0.837, 0.916]
PERFIL_4150 = [1.619, 1.581, 1.541, 1.499, 1.491, 1.468, 1.457, 1.391, 1.376, 1.339,
               1.278, 1.223, 1.154, 1.088, 1.041, 0.978, 0.928, 0.923, 0.906, 0.913,
               0.907, 0.908, 0.917, 0.907, 0.915, 0.905, 0.909, 0.920, 0.924, 0.924,
               0.910, 0.932, 0.922, 0.932, 0.911, 0.923, 0.923, 0.930, 0.936, 0.926,
               0.929, 0.922, 0.933, 0.930, 0.922, 0.920, 0.901, 0.898, 0.904, 0.878,
               0.875, 0.866, 0.856, 0.857, 0.840, 0.822, 0.823, 0.806, 0.800, 0.789,
               0.768, 0.761, 0.730, 0.696]
# La tapa es plástico brillante y sí puede tener más variación que el cartón:
# se le aplica la misma corrección a media fuerza.
CORRECCION_TAPA = 0.55

# ── Muestras para medir la luz de la escena (en la foto base) ──────────────
# ⛔ La primera caja de cartón caía SOBRE LOS DEDOS y el objetivo salía
#    rosado y lavado: el vaso gigante quedaba de color piel. Ésta es cartón
#    limpio, la franja entre la tapa y el índice.
M_CARTON = (560, 1385, 770, 1462)     # B98 G132 R166 · L138 · R/G 1,264 · sat 0,41
M_TAPA = (470, 1270, 700, 1330)       # B64 G61 R58 · neutra y fría
# ⛔ Acá había un 1,09 «porque el vaso chico va pegado al cuerpo y recibe
#    menos luz». Era una suposición mía, no una medida, y Eli la cazó en la
#    ronda 28: «parece que tuviera luz de flash». Medido, el cartón montado
#    daba L=153 contra L=141 del vaso real de la MISMA foto. Vuelve a 1,00:
#    manda lo medido, no el razonamiento.
CARTON_LUZ = 1.00

# ══════════════════════════════════════════════════════════════════════════
# LA TEXTURA — la otra mitad de la «luz de flash»
# ══════════════════════════════════════════════════════════════════════════
# El sol rasante de `IMG_4150` convierte cada fibra del cartón en una
# microsombra. Comparadas a escala equivalente —el vaso real mide 360 px de
# ancho y el montado 1.144, así que los sigma se escalan— la amplitud de
# textura del montaje estaba en:
#
#     fino  3,35 ×   ·   medio  2,50 ×   ·   grueso  1,78 ×
#
# (medido sobre cartón LIMPIO; si la ventana pisa el logotipo la tinta se
# come la diferencia y el exceso parece la mitad de lo que es)
#
# ⭐ Y hay una razón física, no sólo estética: la fibra del cartón mide lo
# que mide —da igual el tamaño del vaso—, así que en pantalla tendría que
# verse igual de chica que en el vaso de su mano, ~1 px. El packshot la trae
# a 6,7 px porque el vaso llena el cuadro. Aplastarla no es suavizar: es
# devolverla a su tamaño aparente.
#
# Un cartón mate bajo nublado NO tiene ese relieve. Se comprime cada banda
# por el inverso de su exceso.
#
# ⚠️ Y se protege la TINTA. El logotipo son trazos de 12-18 px sobre el
#    original: comprimir esa banda sin máscara lo lavaría, y el logotipo de
#    este vaso es justo lo que el cliente reclamó tres veces.
ESCALA_VASO = 2200 / 360.0          # ancho del vaso origen / ancho del real
TEXTURA_SIGMAS = [3.0, 6.0, 12.0]   # en px del vaso REAL
# ⚠️ A 0,16 / 0,28 el cartón desaparecía y el vaso se leía de vinilo: aplastar
#    de más cuesta tan caro como no aplastar. Con éstos la fibra se ve y el
#    relieve de sol no.
TEXTURA_GANANCIAS = [0.38, 0.50, 0.72]
# Aplastada la fibra, el cartón queda demasiado limpio para una foto de
# iPhone: se le devuelve el grano del propio sensor, medido en la foto base
# (sigma 1,4 en el pantalón claro y 4,2 en la camisa gris).
GRANO = 1.8


def leer(p: pathlib.Path) -> np.ndarray:
    im = cv2.imread(str(p))
    if im is None:
        sys.exit(f"ABORTA: no se pudo leer {p}")
    return im.astype(np.float32)


def medias(a: np.ndarray, caja) -> np.ndarray:
    x0, y0, x1, y1 = caja
    return a[y0:y1, x0:x1].reshape(-1, 3).mean(0)


def saturacion(a: np.ndarray, caja) -> float:
    x0, y0, x1, y1 = caja
    f = a[y0:y1, x0:x1].reshape(-1, 3)
    return float((f.max(1) - f.min(1)).mean() / max(f.max(1).mean(), 1))


def mascara_vaso(h: int, w: int):
    """Silueta del vaso de IMG_4150: cuerpo (rectas) + cúpula + las dos orlas.

    Devuelve (silueta, tapa). La tapa se separa por GEOMETRÍA y no por
    luminancia: ⛔ con el umbral `lum < 95` el costado en sombra del cartón
    caía del lado de la tapa y se le aplicaba su corrección — quedaba un
    manchón verde oliva de 900 px en la mitad baja del vaso.
    """
    xs = np.arange(w, dtype=np.float32)
    ys = np.arange(h, dtype=np.float32)
    Y, X = ys[:, None], xs[None, :]
    m = np.zeros((h, w), np.uint8)

    m[(Y >= 700) & (Y <= BASE_CY) & (X > CUERPO_IZQ(Y)) & (X < CUERPO_DER(Y))] = 255
    # base: la mitad inferior de la elipse del culo del vaso
    d = np.clip(1 - ((X - BASE_CX) / BASE_RX) ** 2, 0, None)
    m[(Y > BASE_CY) & (Y <= BASE_CY + BASE_RY * np.sqrt(d))] = 255

    cup = np.interp(xs, TAPA_CUPULA_X, TAPA_CUPULA_Y)
    m[(X >= 420) & (X <= 2305) & (Y >= cup[None, :]) & (Y <= 760)] = 255

    for xr, tt, bb in ((ORLA_I_X, ORLA_I_TOP, ORLA_I_BOT), (ORLA_D_X, ORLA_D_TOP, ORLA_D_BOT)):
        t = np.interp(xs, xr, tt)
        b = np.interp(xs, xr, bb)
        m[(X >= xr[0]) & (X <= xr[-1]) & (Y >= t[None, :]) & (Y <= b[None, :])] = 255

    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (27, 27)))
    # el OPEN redondea las esquinas: con 19 px las dos puntas de la elipse de
    # la base quedaban como papel rasgado
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (49, 49)))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    if n > 1:
        m = np.where(lab == 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])), 255, 0).astype(np.uint8)
    tap = np.zeros_like(m)
    tap[(Y <= 745) & (m > 0)] = 255
    return m, tap


def afinar_contorno(im: np.ndarray, par: np.ndarray) -> np.ndarray:
    """Ajusta la silueta paramétrica al borde REAL del vaso.

    ⭐ Eli, ronda 27: «un recorte preciso del vaso, se ve pegoteado». Tenía
    razón y el defecto era de forma, no de filo: con rectas ajustadas el
    costado del vaso bajaba PERFECTAMENTE recto 3.000 px, y el extremo
    derecho de la tapa terminaba en un muro vertical con escalón. Un vaso
    real no tiene ninguna de las dos cosas.

    El paramétrico sigue mandando la envolvente —es lo que impide que el
    algoritmo se coma la cúpula contra el follaje oscuro— pero el borde lo
    decide la imagen dentro de una banda de ±100 px. Corre a media
    resolución porque a tamaño completo son cuatro minutos.
    """
    h, w = im.shape[:2]
    ch, cw = h // 2, w // 2
    small = cv2.resize(im, (cw, ch), interpolation=cv2.INTER_AREA)
    ps = cv2.resize(par, (cw, ch), interpolation=cv2.INTER_NEAREST)
    fg = cv2.erode(ps, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41)))
    bg = cv2.dilate(ps, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (61, 61)))
    m = np.full(ps.shape, cv2.GC_PR_BGD, np.uint8)
    m[bg > 0] = cv2.GC_PR_FGD
    m[fg > 0] = cv2.GC_FGD
    m[bg == 0] = cv2.GC_BGD
    cv2.grabCut(np.clip(small, 0, 255).astype(np.uint8), m, None,
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                4, cv2.GC_INIT_WITH_MASK)
    r = np.where((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    r = cv2.resize(r, (w, h), interpolation=cv2.INTER_LINEAR)
    # la envolvente paramétrica acota los dos errores del algoritmo: los
    # mordiscos cuadrados en la cúpula (contra el fondo oscuro) y la lengüeta
    # de mesa de teca que se traga en la base
    r = np.maximum(r, cv2.erode(par, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (37, 37))))
    r = np.minimum(r, cv2.dilate(par, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))))
    r = cv2.morphologyEx(r, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (39, 39)))
    r = cv2.morphologyEx(r, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21)))
    n, lab, st, _ = cv2.connectedComponentsWithStats(r, 8)
    if n > 1:
        r = np.where(lab == 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])), 255, 0).astype(np.uint8)
    # ⭐ Y se muerde 5 px hacia adentro. El vaso de IMG_4150 está contra una
    #    mesa de teca iluminada, así que sus píxeles de canto llevan mezclado
    #    el fondo claro de origen: recortado tal cual, ese medio píxel dibuja
    #    un reborde amarillento que sigue el contorno y se lee como el filo
    #    de una calcomanía. Descontaminar = no usarlos.
    r = cv2.erode(r, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    # y se alisa el contorno: desenfocar y volver a umbralizar en el 50 % se
    # come los dientes de sierra de menos de 20 px sin mover el borde
    return ((cv2.GaussianBlur(r.astype(np.float32), (0, 0), 11) > 127) * 255).astype(np.uint8)


def reiluminar(vaso: np.ndarray, m: np.ndarray, tap: np.ndarray, base: np.ndarray,
               crudo: bool = False) -> np.ndarray:
    """Lleva el vaso de IMG_4150 al iluminante de la escena de IMG_4175.

    El objetivo no se inventa: es el vaso CHICO que él lleva en la mano, que
    está en la foto base y bajo la misma luz. Cartón y tapa se tratan por
    separado porque son materiales distintos (difuso vs. plástico).
    """
    obj_carton = medias(base, M_CARTON) * (1.09 if crudo else CARTON_LUZ)
    obj_tapa = medias(base, M_TAPA)
    obj_sat = saturacion(base, M_CARTON)

    dentro = m > 127
    tapa = dentro & (tap > 127)
    carton = dentro & ~tapa

    # ── 1. SE LE CAMBIA LA LUZ, no sólo el color ─────────────────────────
    # u = posición horizontal dentro del vaso, fila por fila y sacada de la
    # propia silueta: así vale igual para la tapa (más ancha), el cuerpo y la
    # base. La ganancia es el perfil nublado dividido por el de sol.
    h, w = m.shape
    xs = np.arange(w, dtype=np.float32)[None, :]
    idx = np.where(dentro, xs, np.nan)
    with np.errstate(invalid='ignore'):
        li = np.nanmin(idx, axis=1)
        ld = np.nanmax(idx, axis=1)
    with np.errstate(invalid='ignore'):
        pass
    hay = ~np.isnan(li)
    li = np.nan_to_num(li)
    ld = np.nan_to_num(ld, nan=1.0)
    ancho = np.maximum(ld - li, 1.0)
    u = np.clip((xs - li[:, None]) / ancho[:, None], 0, 1)
    # ⭐ El perfil de ORIGEN no se da por sabido: se mide sobre este mismo
    # cartón, con la misma u, y así la ganancia lo deja exactamente en el
    # perfil nublado. La tabla PERFIL_4150 queda de referencia documental.
    lum0 = vaso @ np.array([0.114, 0.587, 0.299], np.float32)
    ub = np.clip((u * 64).astype(np.int32), 0, 63)
    suma = np.zeros(64, np.float64)
    cuenta = np.zeros(64, np.float64)
    np.add.at(suma, ub[carton], lum0[carton])
    np.add.at(cuenta, ub[carton], 1.0)
    p_src = suma / np.maximum(cuenta, 1.0)
    p_src = p_src / max(p_src.mean(), 1e-6)
    obj = np.array(PERFIL_REAL, np.float64)
    obj = obj / obj.mean()
    g = (obj / np.maximum(p_src, 1e-3)).astype(np.float32)
    g = cv2.GaussianBlur(g.reshape(1, -1), (0, 0), 2.2).ravel()
    g = np.clip(g, 0.45, 1.8)
    ganancia = np.interp(u, np.linspace(0, 1, len(g)), g).astype(np.float32)
    ganancia = cv2.GaussianBlur(ganancia, (0, 0), 25)          # sin escalones
    ganancia = np.where(hay[:, None], ganancia, 1.0)
    if not crudo:
        k = np.where(tapa, 1 + (ganancia - 1) * CORRECCION_TAPA, ganancia)
        vaso = np.where(dentro[..., None], vaso * k[..., None], vaso)

    # ── 2. SE LE BAJA EL RELIEVE DE LA FIBRA ─────────────────────────────
    lum = vaso @ np.array([0.114, 0.587, 0.299], np.float32)
    loc = cv2.GaussianBlur(lum, (0, 0), 60)
    # ⛔ La máscara de tinta hay que sacarla de la luminancia SUAVIZADA. Con
    #    la cruda, la propia fibra —que es lo que se quiere aplastar— dispara
    #    el umbral y el aplastado no se aplicaba en ninguna parte: la medición
    #    bajaba de 3,35× a 3,19× y nada más. Medido sobre IMG_4150: el cartón
    #    limpio llega a 6 y la tinta del logotipo a 58-72.
    suave = cv2.GaussianBlur(lum, (0, 0), 8)
    tinta = np.clip((loc - suave - 18) / 25.0, 0, 1)
    tinta = cv2.dilate(tinta, np.ones((9, 9), np.uint8))
    tinta = cv2.GaussianBlur(tinta, (0, 0), 5)
    libre = (carton.astype(np.float32) * (1 - tinta))[..., None]

    gan_tex = [1.0, 1.0, 1.0] if crudo else TEXTURA_GANANCIAS
    sig = [s * ESCALA_VASO for s in TEXTURA_SIGMAS]
    b = [cv2.GaussianBlur(vaso, (0, 0), s) for s in sig]
    bandas = [vaso - b[0], b[0] - b[1], b[1] - b[2]]
    plano = b[2].copy()
    for banda, g in zip(bandas, gan_tex):
        plano += banda * (1 - libre * (1 - g))
    vaso = np.where(carton[..., None], plano, vaso)

    # ── 3. el grano del sensor, que el aplastado se llevó ────────────────
    rng = np.random.default_rng(509)
    g0 = rng.normal(0, GRANO, vaso.shape[:2]).astype(np.float32)
    g0 = cv2.GaussianBlur(g0, (0, 0), 0.7)
    g0 *= GRANO / max(g0.std(), 1e-6)
    ruido = np.stack([g0, g0, g0], -1) + rng.normal(0, GRANO * 0.35, vaso.shape).astype(np.float32)
    vaso = np.where(dentro[..., None], vaso + ruido, vaso)

    out = vaso.copy()
    for reg, objetivo, sat_obj in ((carton, obj_carton, obj_sat), (tapa, obj_tapa, None)):
        if reg.sum() == 0:
            continue
        px = vaso[reg]
        if sat_obj is not None:
            s = float((px.max(1) - px.min(1)).mean() / max(px.max(1).mean(), 1))
            k = np.clip(sat_obj / max(s, 1e-3), 0.2, 1.0)
            l = px @ np.array([0.114, 0.587, 0.299], np.float32)
            px = l[:, None] + (px - l[:, None]) * k
        g = objetivo / np.maximum(px.mean(0), 1e-3)
        out[reg] = px * g[None, :]
    return np.clip(out, 0, 255)


def fondo_extendido(base: np.ndarray, alto: int, ancho: int, offx: int, semilla: int = 28) -> np.ndarray:
    """Mosaico de fondo REAL para el aire que la foto no tiene.

    Las franjas laterales de la foto (x 0..430 y x 2480..3024) son fondo puro
    de arriba abajo: son la fuente. Se teselan con espejo y solape de 150 px,
    se desenfocan a σ=26 —ya estaban fuera de foco— y se iguala la costura
    columna por columna contra las primeras filas de la foto.
    """
    rng = np.random.default_rng(semilla)
    # ⛔ Las columnas 0-430 NO son fondo limpio: medida la nitidez por
    #    franjas, su manga entra hasta x=330. Con 430 el mosaico repartía por
    #    el cielo un hombro suyo desenfocado. Los extremos limpios son x<300
    #    y x>2724.
    fuentes = [base[0:1900, 0:300], base[0:1900, 2724:3024],
               base[900:2600, 0:300], base[0:1500, 2760:3024]]
    lienzo = np.zeros((alto, ancho, 3), np.float32)
    peso = np.zeros((alto, ancho, 1), np.float32)
    BW, SOL = 560, 150
    x = 0
    while x < ancho:
        f = fuentes[rng.integers(len(fuentes))]
        fh, fw = f.shape[:2]
        w = min(BW + SOL, ancho - x)
        px = int(np.clip(rng.integers(0, max(fw - 1, 1)), 0, max(fw - w, 0)))
        blo = f[:, px:px + w]
        if blo.shape[1] < w:
            blo = cv2.resize(blo, (w, blo.shape[0]))
        t = np.zeros((alto, w, 3), np.float32)
        y, flip = 0, bool(rng.integers(2))
        while y < alto:
            b = cv2.flip(blo, 0) if flip else blo
            n = min(b.shape[0], alto - y)
            t[y:y + n] = b[:n]
            y += n
            flip = not flip
        if bool(rng.integers(2)):
            t = cv2.flip(t, 1)
        msk = np.ones((alto, w, 1), np.float32)
        s0 = min(SOL, w)
        if x > 0:
            msk[:, :s0] *= np.linspace(0, 1, s0)[None, :, None]
        if x + w < ancho:
            msk[:, -s0:] *= np.linspace(1, 0, s0)[None, :, None]
        lienzo[:, x:x + w] += t * msk
        peso[:, x:x + w] += msk
        x += BW
    lienzo /= np.maximum(peso, 1e-6)
    # ⭐ el desenfoque va EN RAMPA. Con un σ único la costura se ve igual
    # aunque el tono calce: abajo tiene que tener la misma blandura que el
    # fondo de la foto (σ≈9) y arriba puede irse a σ=34, que además calma el
    # dibujo para que el titular se lea encima.
    sub = np.zeros_like(lienzo)
    P = 12
    for i in range(P):
        a0, b0 = alto * i // P, alto * (i + 1) // P
        sig = 34 - 25 * (i / (P - 1))
        m0 = max(a0 - 120, 0)
        tr = cv2.GaussianBlur(lienzo[m0:b0 + 120], (0, 0), max(sig, 4))
        sub[a0:b0] = tr[a0 - m0:a0 - m0 + (b0 - a0)]
    lienzo = sub
    # y se aplana un poco: es profundidad fuera de foco, no un cuadro
    lienzo = lienzo * 0.55 + cv2.GaussianBlur(lienzo, (0, 0), 110) * 0.45

    # costura: las últimas filas del mosaico igualan a las primeras de la foto
    ref = cv2.GaussianBlur(base[0:90], (0, 0), 26).mean(0)              # (3024,3)
    ref_full = np.zeros((ancho, 3), np.float32)
    ref_full[offx:offx + base.shape[1]] = ref
    ref_full[:offx] = ref[0]
    ref_full[offx + base.shape[1]:] = ref[-1]
    delta = (ref_full - lienzo[-90:].mean(0))[None, :, :]
    lienzo += delta * (np.linspace(0, 1, alto)[:, None, None].astype(np.float32) ** 1.6)

    # ⭐⭐ LA COSTURA NO SE ARREGLA SÓLO CON TONO. Igualado el color por
    # columna seguía viéndose la línea, porque lo que se corta es la
    # ESTRUCTURA: el panel de madera y los montantes del vidrio terminan de
    # golpe. Lo que la cierra es un ESPEJO VERTICAL de las primeras filas de
    # la foto, que empalma exacto —la fila de arriba de la foto y la de abajo
    # del espejo son la misma— y continúa cada columna. Se funde con el
    # mosaico en 700 px. El mentón espejado cae detrás del vaso.
    # ⛔ Con 900 px de espejo aparecía ÉL boca abajo en el cielo: las filas
    #    200-900 de la foto son su hombro, su pecho y la mano de la chaqueta.
    #    Con 260 todo lo suyo que se espeja —mentón y nacimiento del hombro—
    #    cae DETRÁS del vaso, que a esa altura cruza de lado a lado.
    ESP = min(alto, 260)
    esp = cv2.flip(base[0:ESP], 0)
    banda = np.zeros((ESP, ancho, 3), np.float32)
    banda[:, offx:offx + base.shape[1]] = esp
    banda[:, :offx] = esp[:, :1]
    banda[:, offx + base.shape[1]:] = esp[:, -1:]
    # ⛔ Y el espejo NO puede ir desenfocado parejo: con σ=9 fijo, la última
    #    fila de la extensión quedaba borrosa contra la primera de la foto,
    #    que está nítida, y ese salto de NITIDEZ dibujaba la línea aunque el
    #    tono calzara. El desenfoque arranca en 0 justo en la costura.
    sb = np.zeros_like(banda)
    Q = 8
    for i in range(Q):
        a0, b0 = ESP * i // Q, ESP * (i + 1) // Q
        sig = 11 - 11 * (i / (Q - 1))
        if sig < 0.6:
            sb[a0:b0] = banda[a0:b0]
            continue
        m0 = max(a0 - 60, 0)
        tr = cv2.GaussianBlur(banda[m0:b0 + 60], (0, 0), sig)
        sb[a0:b0] = tr[a0 - m0:a0 - m0 + (b0 - a0)]
    w = (np.linspace(0, 1, ESP) ** 0.7)[:, None, None].astype(np.float32)
    lienzo[-ESP:] = lienzo[-ESP:] * (1 - w) + sb * w
    # arriba más oscuro y más plano: es el cielo raso del local, fuera de foco
    lienzo *= np.linspace(0.72, 1.0, alto)[:, None, None].astype(np.float32)
    return lienzo


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vaso-ancho", type=int, default=2130)
    ap.add_argument("--tapa-top", type=int, default=2400)
    ap.add_argument("--vaso-cx", type=int, default=1750, help="centro del vaso en el lienzo")
    ap.add_argument("--giro", type=float, default=-3.5, help="grados: el vaso se apoya en el cuerpo")
    ap.add_argument("--salida", default=None)
    ap.add_argument("--guardar-capas", default=None, metavar="DIR",
                    help="además del JPG, escribe la MÁSCARA del vaso en coordenadas "
                         "de la pieza (2250x4000). La usa between-s5-vaso-magnific.py "
                         "para devolver al montaje sólo los píxeles del vaso.")
    ap.add_argument("--crudo", action="store_true",
                    help="sin corregir la luz ni la textura del vaso: reproduce lo que "
                         "Eli vio en la ronda 27 y llamó «luz de flash». Sólo para comparar.")
    a = ap.parse_args()

    base = leer(FOTO)
    bh, bw = base.shape[:2]

    # ── lienzo 9:16 con la foto abajo y centrada ──────────────────────────
    # 4200 × 7466: la foto entra a 1:1, deja 588 px a cada lado y 3434 arriba.
    # ⭐ Los 178 laterales son la clave de que los lados NO se inventen: en la
    # foto las columnas x<178 y x>2846 son fondo puro a CUALQUIER altura
    # (fachada arriba, piso abajo), así que un espejo corto fila a fila
    # continúa lo que había. Con el lienzo anterior (588 px) el espejo se
    # comía su brazo y aparecía un segundo hombre borroso en el borde.
    # El alto lo fija el titular: para que el bloque de texto quepa entre la
    # zona segura de Instagram (250 sobre 1920) y el filo de la tapa, el
    # mentón tiene que caer en el 46 % de la altura.
    # ⭐⭐ Y el alto lo fija algo más, que Eli cazó en la ronda 27: «pareciera
    # que le falta la cabeza». Era cierto y es medible. Su hombro está 200 px
    # bajo el borde de la foto, y con 1.452 px de ancho de hombros la coronilla
    # le caería 636 px sobre el mentón. Con el lienzo anterior la tapa
    # terminaba POR DEBAJO de esa coronilla: quedaban 134 px de fondo justo
    # donde tendría que haber cabeza, y el ojo lee un decapitado. Ahora la
    # tapa pasa 103 px por ENCIMA de la línea de coronilla, y el vaso ocupa el
    # sitio de la cabeza en vez de dejarlo vacío.
    #
    # El orden vertical queda así, sobre 1920:
    #    250   arranca el titular — zona segura de Instagram
    #    576   termina el bloque de texto
    #    617   filo de la tapa · 41 px de holgura
    #    720   línea de coronilla — el vaso ya pasó por encima
    #    883   el mentón, 266 px dentro del vaso
    W, H = 4200, 7466
    OFFX, OFFY = (W - bw) // 2, H - bh
    DER = W - OFFX - bw
    lienzo = fondo_extendido(base, OFFY, W, OFFX)
    lienzo = np.concatenate([lienzo, np.zeros((bh, W, 3), np.float32)], 0)
    # ⛔ Los laterales NO se espejan con un trozo ancho de la foto: medida la
    #    nitidez por franjas, su silueta llega hasta x=330 por la izquierda y
    #    x=2650 por la derecha, así que un espejo de 458 px lo duplicaría
    #    borroso en el borde. Sólo son fondo limpio las 300 columnas de cada
    #    extremo, y se reflejan sobre sí mismas —fila por fila, para que
    #    arriba siga siendo fachada y abajo siga siendo piso—.
    LIM = 300
    lienzo[OFFY:, :OFFX] = cv2.copyMakeBorder(base[:, :LIM], 0, 0, OFFX, 0,
                                              cv2.BORDER_REFLECT_101)[:, :OFFX]
    lienzo[OFFY:, OFFX + bw:] = cv2.copyMakeBorder(base[:, -LIM:], 0, 0, 0, DER,
                                                   cv2.BORDER_REFLECT_101)[:, -DER:]
    lienzo[OFFY:, OFFX:OFFX + bw] = base
    # las dos costuras verticales se difuminan sobre 90 px
    for xc in (OFFX, OFFX + bw):
        a0, b0 = xc - 90, xc + 90
        franja = cv2.GaussianBlur(lienzo[OFFY:, a0 - 60:b0 + 60], (0, 0), 7)[:, 60:-60]
        w = np.abs(np.linspace(-1, 1, b0 - a0))[None, :, None].astype(np.float32)
        lienzo[OFFY:, a0:b0] = lienzo[OFFY:, a0:b0] * w + franja * (1 - w)

    # ── el vaso gigante ───────────────────────────────────────────────────
    vaso = leer(VASO)
    m, tap = mascara_vaso(*vaso.shape[:2])
    m = afinar_contorno(np.clip(vaso, 0, 255).astype(np.uint8), m)
    vaso = reiluminar(vaso, m, tap, base, crudo=a.crudo)

    # ⭐⭐ DESCONTAMINAR EL CANTO — esto es lo que dibujaba el reborde pálido.
    # El degradado de alpha (σ=2) se abre ±5 px a cada lado del borde, y del
    # lado de afuera lo que hay son píxeles de la MESA DE TECA iluminada de
    # IMG_4150. Mezclados al 50 % pintaban una línea crema que seguía todo el
    # contorno: el filo de calcomanía que marcó Eli. La cura no es afinar el
    # degradado —eso devuelve el filo de bisturí— sino EXTENDER el color del
    # vaso hacia afuera antes de difuminar, para que la rampa mezcle cartón
    # con cartón.
    dentro = (m > 127).astype(np.float32)
    num = cv2.GaussianBlur(vaso * dentro[..., None], (0, 0), 11)
    den = cv2.GaussianBlur(dentro, (0, 0), 11)[..., None]
    vaso = np.where(dentro[..., None] > 0.5, vaso, num / np.maximum(den, 1e-4))

    alpha = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 2.0) / 255.0

    ys, xs = np.nonzero(m)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    rec = vaso[y0:y1 + 1, x0:x1 + 1]
    rea = alpha[y0:y1 + 1, x0:x1 + 1]
    esc = a.vaso_ancho / rec.shape[1]
    nw, nh = a.vaso_ancho, int(round(rec.shape[0] * esc))
    rec = cv2.resize(rec, (nw, nh), interpolation=cv2.INTER_AREA)
    rea = cv2.resize(rea, (nw, nh), interpolation=cv2.INTER_AREA)

    # se inclina un poco: un vaso cargado con una mano no queda a plomo
    if abs(a.giro) > 0.01:
        pad = int(nw * 0.12)
        rec = cv2.copyMakeBorder(rec, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
        rea = cv2.copyMakeBorder(rea, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0)
        Mr = cv2.getRotationMatrix2D((rec.shape[1] / 2, rec.shape[0] / 2), a.giro, 1.0)
        rec = cv2.warpAffine(rec, Mr, (rec.shape[1], rec.shape[0]), flags=cv2.INTER_LINEAR)
        rea = cv2.warpAffine(rea, Mr, (rea.shape[1], rea.shape[0]), flags=cv2.INTER_LINEAR)
        nw, nh = rec.shape[1], rec.shape[0]

    # ⛔ Al girar se añade borde, y si se posiciona por la esquina del lienzo
    #    rotado la tapa baja `pad` píxeles — 228 en la primera prueba — y el
    #    mentón se asomaba por encima de la tapa, que era justo lo que no
    #    podía pasar. Se posiciona por la SILUETA, no por el lienzo.
    yy, xx = np.nonzero(rea > 0.5)
    py0 = int(a.tapa_top - yy.min())
    px0 = int(a.vaso_cx - (xx.min() + xx.max()) // 2)
    if os.environ.get("VASO_DEBUG"):
        print(f'   vaso: tapa en y={a.tapa_top} ({a.tapa_top/H*1920:.0f} sobre 1920) · '
          f'base en y={py0 + int(yy.max())} ({(py0 + yy.max())/H*1920:.0f}) · '
          f'ancho {int(xx.max()-xx.min())} ({(xx.max()-xx.min())/W*1080:.0f} sobre 1080)')
    # recorte contra los bordes del lienzo, en los dos ejes
    sx, sy = max(0, -px0), max(0, -py0)
    dx, dy = max(0, px0), max(0, py0)
    pw = min(nw - sx, W - dx)
    ph = min(nh - sy, H - dy)
    cap = rec[sy:sy + ph, sx:sx + pw]
    cal = rea[sy:sy + ph, sx:sx + pw][..., None]
    silueta = np.zeros((H, W), np.float32)
    silueta[dy:dy + ph, dx:dx + pw] = cal[..., 0]

    # ── LA SOMBRA VA ANTES DEL VASO, porque cae sobre el fondo ────────────
    # Dirección medida en la propia foto: la sombra del cuello sobre la
    # camisa y la del cinturón caen rectas y un punto a la derecha. Sin esto
    # el vaso no toca nada y se lee pegado — fue lo que Eli marcó con rojo
    # en la base y en el filo de la tapa.
    proy = cv2.warpAffine(silueta, np.float32([[1, 0, 30], [0, 1, 74]]), (W, H))
    lienzo *= (1 - 0.52 * np.clip(cv2.GaussianBlur(proy, (0, 0), 44) - silueta, 0, 1))[..., None]
    # y el contacto, más corto y más oscuro, pegado al canto
    ao = np.clip(cv2.GaussianBlur(silueta, (0, 0), 19) - silueta, 0, 1)
    lienzo *= (1 - 0.34 * ao)[..., None]

    # ── LUZ ENVOLVENTE ───────────────────────────────────────────────────
    # Lo que delata un montaje no es tanto el filo como que el objeto ignore
    # la escena. Acá el fondo es un vidrio claro y el vaso es opaco: en una
    # foto de verdad esa claridad se derrama unos píxeles sobre el canto. Se
    # toma el fondo YA ensombrecido, se desenfoca y se mezcla en una banda
    # estrecha por dentro del borde.
    # ⛔ A 0,42 sobre una banda de 26 px dejaba un reborde pálido continuo
    #    alrededor de TODO el vaso —abajo, contra el pantalón blanco, se leía
    #    como el halo de una calcomanía—. Un derrame real es sutil y no
    #    dibuja contorno: 0,18 sobre 15 px.
    roi = lienzo[dy:dy + ph, dx:dx + pw]
    halo = cv2.GaussianBlur(roi, (0, 0), 40)
    banda = cal[..., 0] - cv2.erode(cal[..., 0], np.ones((31, 31), np.uint8))
    banda = cv2.GaussianBlur(np.clip(banda, 0, 1), (0, 0), 7)[..., None] * 0.18
    cap = cap * (1 - banda) + halo * banda

    lienzo[dy:dy + ph, dx:dx + pw] = roi * (1 - cal) + cap * cal

    # ⛔ NO se pega ninguna mano recortada, y se probó.
    # La idea era poner los dedos de la propia foto delante del vaso para que
    # se leyera «lo carga». Pegados quedaban como una calcomanía: el vaso le
    # tapa el antebrazo, así que la mano aparecía flotando sin brazo que la
    # sostenga, y encima arrastraba un trozo de puño gris.
    # ⭐ No hace falta: **su mano derecha real, con la pulsera, cae justo en el
    # filo del vaso** a la altura de la tapa (la que en la foto sujeta la
    # chaqueta al hombro). Ahí sí hay brazo, hombro y cuerpo detrás, y se lee
    # que lo agarra. Es fotografía, no montaje.

    # ── el degradado del titular, y está MEDIDO ───────────────────────────
    # Sin él la mediana del fondo bajo el texto da 6,5-8,1:1, que basta, pero
    # el p98 —los brillos del vidrio y las luces fuera de foco— cae a 2,7:1 y
    # el beige se pierde justo donde hay un reflejo. La regla del estudio es
    # mirar el PEOR tercio, no el promedio. Un multiplicador de 0,68 que sube
    # a 1,0 en y=2300 deja el peor caso sobre 5:1 y no toca el vaso, que
    # empieza en 2120 y es oscuro de por sí.
    y = np.arange(H, dtype=np.float32)
    s = np.clip((y - 2280) / 800.0, 0, 1)
    k = 0.58 + 0.42 * (s * s * (3 - 2 * s))      # smoothstep, no una recta
    lienzo *= k[:, None, None].astype(np.float32)

    # ── salida ────────────────────────────────────────────────────────────
    out = np.clip(lienzo, 0, 255).astype(np.uint8)
    final = cv2.resize(out, (2250, 4000), interpolation=cv2.INTER_AREA)
    if a.guardar_capas:
        capas = pathlib.Path(a.guardar_capas)
        capas.mkdir(parents=True, exist_ok=True)
        masc = cv2.resize((np.clip(silueta, 0, 1) * 255).astype(np.uint8), (2250, 4000),
                          interpolation=cv2.INTER_AREA)
        cv2.imwrite(str(capas / "vaso-alpha.png"), masc)
        print(f"capa   {capas / 'vaso-alpha.png'}")

    destino = pathlib.Path(a.salida) if a.salida else (DESTINO_RAW / "st-28-09-togo-r27.jpg")
    destino.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(destino), final, [cv2.IMWRITE_JPEG_QUALITY, 96])
    print(f"listo  {destino}  {final.shape[1]}×{final.shape[0]}")


if __name__ == "__main__":
    main()

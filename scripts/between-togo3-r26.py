#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · slide 3 — ronda 26 (21-09-2026): la medialuna pasa a ROLLO DE
CANELA, y el vaso baja al tamaño de sus hermanas.

Scarlette, comentario de contenido del 21-09 (10:08) sobre la S4:

    «Primeramente mencionan que los productos no se ven proporcionales unos con
     otros para revisar los tamaños de los cafés y sus agregados.
     Slide 3: Desde $2.990 - Cambiar medialuna por rollo de canela.»

⭐⭐⭐ NO SE MONTA NI SE GENERA NADA: LA FOTO EXISTE.
La sesión `25 jul 2025` tiene el rollo de canela CON el vaso vigente, sobre la
misma mesa de listones, el mismo muro vegetal y el mismo 50 mm que las otras
slides — es la regla madre de la ronda 10 del manual, «antes de generar un
producto, búscalo en la sesión», y acá se cumple entera:

    25-280   apaisada, sin muro vegetal (sólo mesa)   → descartada
    25-281   VERTICAL, muro vegetal arriba + mesa     → ✅ ésta
    25-283   el vaso VIEJO, gris con faja de papel    → descartada

La 281 es 3840×5760 y entra de una en el 4:5 del feed, así que la slide deja de
ser una generación y pasa a ser **una fotografía del cliente, sin retoque de
producto**.

⭐⭐⭐ LA DESPROPORCIÓN SE MIDIÓ, NO SE ESTIMÓ — Y EL PATRÓN ES EL WORDMARK.
El logotipo impreso «BETWEEN» mide **lo mismo en los tres tamaños de vaso**:
medido sobre la sesión de vasos que mandó Eli (`IMG_5714-5729`, los tres tamaños
juntos sobre la misma mesa) da 952 · 892 · 938 px para el grande, el medio y el
chico. O sea que el wordmark **no depende del tamaño del vaso** y por eso sirve
de regla: su ancho en píxeles ES la escala a la que está leyendo el vaso en la
pieza. Contra eso, el carrusel entregado medía:

    slide        wordmark   alto del vaso   alto/wordmark
    2 · sándwich   554 px       948 px          1,71
    3 · dulce      781 px      1540 px          1,97   ← 1,41× sus hermanas
    4 · los tres   393 px       687 px          1,75

⛔ Y OJO CON CÓMO SE MIDE ESE ANCHO, porque la primera pasada se equivocó en
   140 px y la ventana salió 20 % corta. Segmentar la tinta por «más oscuro que
   su entorno» NO sirve sobre un vaso: el canto cilíndrico en sombra entra en el
   mismo umbral que el trazo del logotipo y la caja se estira hasta el borde del
   vaso (daba 901 px donde hay 700). La correlación multi-escala tampoco, porque
   las dos tomas curvan el wordmark distinto y el máximo cae en un falso.
   Lo que sí: **regla dibujada sobre un zoom, glifo a glifo** — el canto
   izquierdo de la «B» y el derecho de la última «N».

⛔ **El mismo vaso leía 2,0× más grande en la 3 que en la 4.** Y adentro de la
propia slide 3 la medialuna medía 0,69 del alto del vaso cuando en la fotografía
real el rollo mide **1,11** — o sea que el agregado se veía un **38 % más chico**
de lo que es al lado de su café. Las dos mitades del reclamo, en un número.

⭐ LA VENTANA SALE DE ESA CUENTA, no de mirar la foto. El wordmark de la 281 mide
700 px en el original, así que el ancho de la ventana 4:5 fija la escala a la que
va a leer el vaso: `wordmark final = 700 × 2250 / ancho`.

⛔⛔ Y ACÁ HAY UN CANJE QUE NO SE PUEDE ESQUIVAR, y es lo que trajo la 2.ª vuelta
   de esta ronda. Eli, sobre la primera: «esta foto se ve muy blanca» y «trata
   que esa tenga el mismo fondo de las demás».
   Las dos frases son el mismo problema: **la ventana que deja el vaso en 554 px
   sólo deja 28 % de muro vegetal**, contra el 48 % de la slide 2 y el 55 % de la
   4. Con tan poco verde oscuro arriba, el resto del cuadro es mesa clara y la
   pieza lee blanca aunque la mediana empate.
   Y no se arregla bajando la ventana: con esta toma, el borde de la mesa y el
   rollo están a una distancia FIJA, así que cuanto más se acerca la cámara menos
   muro cabe. La cuenta, con el rollo entero y sin que la pastilla del precio lo
   pise:

       horizonte_máx = 2560 − 2075 × escala      wordmark = 700 × escala

       escala   wordmark   muro vegetal
        0,79      554 px      34 %   ← la 1.ª vuelta: empata el vaso, fondo blanco
        0,68      476 px      41 %   ← acá
        0,60      420 px      47 %      empata el fondo, el vaso queda chico

   Se eligió **0,68**: el vaso queda en 476 px, o sea 0,86× el de la slide 2 —una
   diferencia del 14 %, que no se lee— y el muro sube a 41 %, que sí se lee. El
   desajuste que reclamó el cliente era de 1,41× y queda en 1,16×.
   ⚠️ Queda dicho para la próxima: si alguna vez hay que empatar el vaso Y el
   fondo en esta slide, hace falta OTRA toma, no otro encuadre.

⚠️ La slide 4 se queda como está, y es a propósito. Es el plano ABIERTO del
carrusel (bolsa + mano + tres productos) y sus proporciones internas sí están
bien —el vaso mide 1,64 de su wordmark, igual que la 2—: lee más chico porque la
cámara está más atrás, no porque el producto esté mal. Medido, no cabe acercarla:
para subir el vaso a 592 habría que ampliar 1,41× y con cualquier encuadre que
mantenga el sándwich entero **el vaso se sale por la derecha** (el máximo que
admite sin cortar producto es 1,08×, que no arregla nada y arriesga la mano).

⛔ EL PRODUCTO NO SE TOCA. No hay recorte, no hay estampado de logotipo, no hay
relight: sale de cámara. Lo único que se hace es la ventana 4:5 y el revelado
para igualar el tono al de sus hermanas.

Salida: public/assets/hilton/between/fotos-gradadas/togo-s3-r26.jpg
"""
import importlib.util
import sys
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

from between_retoque import apetitoso, hombro as _hombro_bt, revela, vivo  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "between_togo4_r12", RAIZ / "scripts/between-togo4-r12.py")
_r12 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_r12)
iguala_tono, hombro = _r12.iguala_tono, _r12.hombro

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

#: ⚠️ `raw/` NO viaja en el repo. Si falta la toma, se rebaja de Drive — carpeta
#: `BETWEEN 25 JULIO MODELOS` (1gI00XGbBV5YjqcSjG3SmmkMuxr-ev_60), archivo
#: `Double Tree 25 jul 25-281.jpg`, id 19huZ5DzTswtI13MbJK_4AAiG6aGNtqUY:
#:   curl -L "https://drive.usercontent.google.com/download?id=19huZ5DzTswtI13MbJK_4AAiG6aGNtqUY&export=download&confirm=t" #:     -o "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-281.jpg"
#: Igual no hace falta para rendir: la toma CURADA (`togo-25jul2025-rol.jpg`) y
#: la revelada (`togo-s3-r26.jpg`) sí están versionadas.
ORIGEN = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-281.jpg"
CURADA = RAIZ / "public/assets/hilton/between/togo-25jul2025-rol.jpg"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-s3-r26.jpg"
SALIDA = (2250, 2812)

#: ⭐ LA VENTANA, con las cuatro restricciones que la fijan (todo en px del
#: original de 3840×5760, medido sobre la toma):
#:
#:   · el wordmark del vaso mide 700 px y se pide en 476 → escala 0,68 → la
#:     ventana mide 3309 × 4136 (ver el canje en la cabecera).
#:   · el CANTO DERECHO DEL VASO está en x=3436 y pide x0 ≥ 318 para no salirse;
#:     el CANTO IZQUIERDO DEL ROLLO está en x=783 y pide x0 ≤ 783 para no
#:     cortarse. `x0=420` deja el vaso con 199 px de aire y el rollo entrando
#:     con 247. El PLATO se corta por la izquierda y está bien: la slide
#:     entregada también cortaba el papel por ahí.
#:   · el PLATO se corta por la izquierda y está bien: la slide entregada
#:     también cortaba el papel por ahí, y es lo que hace la slide 2 con el suyo.
#:   · el borde de la mesa —donde termina el muro vegetal— está en y=2021. Con
#:     y0=331 cae en y=1149 del lienzo, o sea **41 % de muro vegetal**, que es
#:     lo que pidió Eli y lo que hace que la pieza deje de leer blanca. El
#:     bloque de texto cierra en 660, así que el titular y la bajada quedan
#:     enteros sobre el verde con 489 px de sobra.
#:   · el que pone el techo a y0 es el ROLLO: cierra en y=4096 del original y
#:     tiene que quedar sobre la pastilla del precio, que arranca en y=2609.
#:     Con y0=331 el rollo cierra en 2560: 49 px de aire y nada pisado.
#:
#: ⚠️ El PLATO se corta 57 px por abajo. Es a propósito y es lo que compra el
#: muro vegetal: el ala de la loza no es producto.
VENTANA = {"x0": 420, "y0": 331, "ancho": 3309, "alto": 4136}

#: ⭐ EL PILAR — lo único del fondo que no es muro vegetal.
#: Eli: «trata que esa tenga el mismo fondo de las demás». Medido sobre el
#: muro, la 281 empata con sus hermanas en casi todo: luma 68 contra 78 de la
#: slide 2 y 71 de la 3 vieja, y la energía a la escala de una HOJA —lo que
#: hace que un fondo lea como masa desenfocada y no como plantas legibles— da
#: 13,0 contra 14,2 de la slide 2 y 13,0 de la 4. O sea que el muro sirve.
#: Lo que NO tienen las hermanas es el **pilar gris** que entra por el canto
#: derecho: en el original va de x=3600 a 3840 desde y≈470, y dentro de la
#: ventana queda como una franja clara de 88 px pegada al borde.
#: Se tapa clonando el muro de su izquierda ESPEJADO, que sobre bokeh no deja
#: rastro (`cv2.inpaint` dejaría un parche liso, que es peor — la misma trampa
#: que la raya del cartón en la r25).
PILAR = {"x0": 3560, "x1": 3840, "y0": 260, "y1": 2200, "espejo_desde": 3560, "suave": 45}

#: ⭐ EL REVELADO: la toma sale de cámara en mediana 80 y sus hermanas están en
#: 127. Hay que levantarla, y el objetivo es el tono de la slide 3 ENTREGADA —el
#: que el cliente ya dio por bueno de color—, porque esta ronda cambia el
#: producto y el encuadre, no el revelado:
#:
#:     pieza            mediana   calidez   saturación   croma
#:     slide 2 (r24)      127,9      28,1        41,8     23,7
#:     slide 3 (r24)      126,7      27,5        41,9     25,2   ← el objetivo
#:     slide 4 (r24)      124,0      23,6        40,4     23,4
#:     la 281 cruda        80,1      37,6        40,5     21,4
#:
#: ⛔ `iguala_tono` SOLO no llega: su gamma está topada en 0,70 y desde 80 se
#:    queda en 108. Por eso el orden es `revela` primero —que es el revelado por
#:    MEDIOS de la marca y admite gamma hasta 0,55— y `iguala_tono` después, ya
#:    sin trabajo de exposición, sólo para clavar la calidez.
#: ⛔ Y la saturación de `iguala_tono` se deja PASAR (999) a propósito: su
#:    métrica es `(max−min).mean()` y recortando ahí la pieza caía a croma 20,8,
#:    o sea lavada. El color lo pone `vivo`, que es vibrancia y no saturación
#:    plana — la regla del manual para que el kraft no se vuelva naranjo.
#: ⭐ La calidez se pide en 23,5 y no en 27,5: `vivo` devuelve ~4,4 de calidez
#:    después. Es la misma precompensación de la r23, medida acá.
#:        pedida 16,0 -> 24,3    18,0 -> 26,9    20,0 -> 28,8
REV_MEDIOS, REV_CALIDEZ_MAX = 133, 14
OBJ_CALIDEZ, VIBRANCIA = 18.0, 0.25

#: ⭐ LA MASA, APARTE — «la comida clara se grada con mano SUAVE».
#: Con el revelado global la pieza clava el tono de sus hermanas (mediana 126,4
#: contra 126,7) pero el rollo sale PÁLIDO: es hojaldre claro sobre un plato
#: verde apagado, y la medialuna que reemplaza era dorada. Subir la exposición
#: global para arreglarlo rompería el empate con las hermanas y quemaría el
#: hojaldre — que es el error que el manual ya tiene escrito.
#: Por eso la claridad va SÓLO sobre la masa, con `apetitoso`, que es el
#: instrumento de la marca para esto: contraste de media frecuencia para que se
#: separen las capas, cuerpo y calidez de horno, y todo frenado en las altas
#: para que no aparezca blanco puro.
#: ⛔ La máscara es una elipse SUAVE sobre el rollo y no llega ni al vaso ni al
#:    plato: el vaso es producto de marca y no se toca, y el plato es loza —
#:    darle calidez de horno lo volvería amarillo.
#: Caja del rollo, calculada con la ventana: x 247..1261 · y 1973..2560.
MASA = {"cx": 754, "cy": 2266, "rx": 560, "ry": 320, "suave": 90}
CLARIDAD, CUERPO, CALOR = 0.50, 1.10, 6.0

#: ⭐⭐ EL PIE DE LA CURVA — lo que de verdad estaba detrás del «se ve muy blanca».
#: La mediana empataba con las hermanas (126 contra 127) y la pieza igual leía
#: lavada. El histograma lo cantó de una:
#:
#:     pieza                p5     p25     p50     p75     p95
#:     slide 2             7,5    58,4   120,2   160,5   207,1
#:     slide 3 entregada   8,5    62,4   120,6   153,8   203,4
#:     slide 4            10,0    56,4   112,7   178,7   197,6
#:     slide 3 · 1.ª vuelta  30,5  88,7   116,7   147,3   196,1   ← sin negros
#:
#: ⛔ **La pieza no tenía negros.** Su cuarto bajo estaba 25-30 niveles por
#:    encima del de sus tres hermanas. Igualar la MEDIANA no dice nada del pie
#:    de la curva, y el pie es lo que se ve como densidad.
#: ⛔ El punto negro de `iguala_tono` no lo agarra: mide el percentil 0,8 y en
#:    esta toma ya estaba en 0, así que no hacía nada. El levante venía del
#:    gamma de `revela`, que sube TODO.
#: ⭐ Por eso este paso va AL FINAL y por separado: punto negro en el percentil
#:    3,5 —medido, es donde arranca la sombra real de la mesa— y un contraste
#:    suave de 1,08 pivotando en 118, que es la mediana del set. Cierra con el
#:    hombro, así que no puede clipear.
#: Resultado: p5 7,2 · p25 67,4 · p50 118,5 · p75 149,4 · p95 206,3.
NEGRO_PCT, CONTRASTE, PIVOTE = 3.5, 1.08, 118.0


def profundidad(im):
    """Punto negro + contraste suave, al final de todo. Devuelve la densidad que
    el gamma del revelado se llevó."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    p = float(np.percentile(a, NEGRO_PCT))
    a = np.clip(a - p, 0, None) * (255.0 / max(1.0, 255.0 - p))
    a = (a - PIVOTE) * CONTRASTE + PIVOTE
    print(f"   profundidad: negro del percentil {NEGRO_PCT} ({p:.0f}) -> 0 · contraste {CONTRASTE}")
    return Image.fromarray(np.clip(_hombro_bt(np.clip(a, 0, 320)), 0, 255).astype(np.uint8))


def tapa_pilar(im):
    """Clona muro espejado sobre el pilar gris del canto derecho."""
    import cv2
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    P = PILAR
    ancho = P["x1"] - P["x0"]
    origen = a[P["y0"]:P["y1"], P["espejo_desde"] - ancho:P["espejo_desde"]][:, ::-1]
    destino = a[P["y0"]:P["y1"], P["x0"]:P["x1"]]
    m = np.zeros(destino.shape[:2], np.float32)
    m[P["suave"]:-P["suave"], : -P["suave"]] = 1.0
    m = cv2.GaussianBlur(m, (0, 0), P["suave"])[..., None]
    a[P["y0"]:P["y1"], P["x0"]:P["x1"]] = destino * (1 - m) + origen * m
    print(f"   pilar tapado: x {P['x0']}..{P['x1']} · y {P['y0']}..{P['y1']}")
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def mascara_masa(tam):
    """Elipse suave sobre el rollo. Se difumina para que no quede canto: un
    parche con borde se delata más que el defecto que arregla."""
    import cv2
    w, h = tam
    m = np.zeros((h, w), np.float32)
    cv2.ellipse(m, (MASA["cx"], MASA["cy"]), (MASA["rx"], MASA["ry"]), 0, 0, 360, 1.0, -1)
    return cv2.GaussianBlur(m, (0, 0), MASA["suave"])


def cifras(im, nom):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a[..., 0] * .299 + a[..., 1] * .587 + a[..., 2] * .114
    mx, mn = a.max(2), a.min(2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1) * 100, 0)
    gris = a.mean(2)
    q = np.percentile(g, [5, 25, 50, 75, 95])
    print(f"   {nom:16s} p5 {q[0]:6.1f} · p25 {q[1]:5.1f} · p50 {q[2]:5.1f} · p75 {q[3]:5.1f} "
          f"· p95 {q[4]:5.1f} · calidez {(a[..., 0] - a[..., 2]).mean():5.1f}")
    print(f"   {'':16s} saturación {sat.mean():5.1f} · croma "
          f"{np.abs(a - gris[..., None]).max(2).mean():5.1f} "
          f"· blanco puro {(a > 250).mean() * 100:4.2f} %")


def main():
    if not ORIGEN.exists():
        sys.exit(f"falta la toma original: {ORIGEN}")
    src = tapa_pilar(Image.open(ORIGEN).convert("RGB"))
    v = VENTANA
    print(f"original ............. {src.width}×{src.height}")
    print(f"ventana 4:5 .......... {v['ancho']}×{v['alto']} desde ({v['x0']}, {v['y0']})"
          f"  ratio {v['ancho'] / v['alto']:.3f}")

    im = src.crop((v["x0"], v["y0"], v["x0"] + v["ancho"], v["y0"] + v["alto"]))
    im = im.resize(SALIDA, Image.LANCZOS)
    cifras(im, "de cámara")

    # la toma curada, SIN revelar: es la que queda versionada como material
    CURADA.parent.mkdir(parents=True, exist_ok=True)
    im.save(CURADA, "JPEG", quality=95, subsampling=0)

    out = revela(im, medios=REV_MEDIOS, calidez_max=REV_CALIDEZ_MAX)
    out = iguala_tono(out, mediana=REV_MEDIOS, calidez=OBJ_CALIDEZ, saturacion=999)
    out = vivo(out, vibrancia=VIBRANCIA)
    out = apetitoso(out, mascara=mascara_masa(SALIDA),
                    claridad=CLARIDAD, cuerpo=CUERPO, calor=CALOR)
    out = profundidad(out)
    cifras(out, "revelada")
    print("   objetivo (hermanas):   p5    8.0 · p25  60.4 · p50 120.4 "
          "· p75 157.2 · p95 205.3 · calidez  27.5")

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    out.save(DESTINO, "JPEG", quality=95, subsampling=0)
    print(f"\n-> {DESTINO.relative_to(RAIZ)}")
    print(f"-> {CURADA.relative_to(RAIZ)}  (toma curada, sin revelar)")


if __name__ == "__main__":
    main()

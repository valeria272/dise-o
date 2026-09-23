#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAFÉ DE CUMPLEAÑOS (FEED 03-sep, S1) — ronda 16: EL MURO, con globos reales.

Eli, 07-09-2026:

    «para la s1 de between debes volver a hacer el fondo, genera en magnific
     debes guiarte del comentario de Scarlett utilizando la foto [X] pero con el
     vaso actual de TOGO, debe ser continuo de slide 1 y 2, tiene que tener el
     prompt hablar de calidad, realisto y detalle de cumpleaños con elegancia de
     serpentina dorada o detalle de cumpleaños como globos de fondo sutil,
     recordando que se note que es between el fondo.»

⭐ LO QUE YA ESTABA RESUELTO Y NO SE TOCA

  · «utilizando la foto … pero con el vaso actual de TOGO» **ya se cumple**: el
    EXIF probó que el adjunto de Scarlette y `Double Tree 25 jul 25-257.jpg` son
    la MISMA mesa 63 segundos después, y la 257 es la que trae el vaso nuevo.
    Ver el manual § «LA FOTO QUE MANDÓ EL CLIENTE YA TENÍA EL VASO NUEVO».
  · «continuo de slide 1 y 2» ya se hace con **dos recortes 4:5 REALES** de esa
    toma (x 1830-4902 y x 2688-5760), no tejiendo ni espejando nada.
  · las serpentinas doradas sobre la mesa son la ilustración de Eli y la ronda 15
    ya les arregló el alfa. Están aprobadas: no se rehacen.

⛔ POR QUÉ ESTE PASO NO DIBUJA NADA, Y POR QUÉ TAMPOCO PARCHA EL MURO

Dos intentos anteriores de meter adorno de cumpleaños DENTRO de la foto se
rechazaron —los papelitos de color plano parecían «grageas de torta» (r11) y la
cinta dorada dibujada parecía «un plátano» (r12)— y de ahí salió la regla del
manual: *un adorno sobre una fotografía es ilustración, no fotografía*. Sigue
valiendo **para lo que se dibuja**. Acá el material es otro: una fotografía
generada con Nano Banana Pro, con globos champán fuera de foco sobre un muro
vegetal, o sea el mismo material que la toma que los recibe.

Y no se pega un PARCHE rectangular del muro generado, aunque sea lo más simple,
porque las dos superficies no coinciden — medido:

    zona                        varianza laplaciano   mediana
    muro real de la 257                  38,7            47
    muro generado (globos)                8,2           168

El generado es **3,5 veces más claro y 4,7 veces más blando**: un parche se
leería como un rectángulo pegado. Lo que sí se puede trasplantar es el GLOBO,
porque un globo fuera de foco no tiene detalle de alta frecuencia —sólo canto
blando, que es justo lo que hay que conservar— y su brillo se puede llevar al
del muro que lo recibe.

⭐ CÓMO SE COMPONE (y es la receta de «un elemento agregado necesita tres cosas»)

  1. se AÍSLA el globo por luminancia y temperatura (claro y cálido contra
     follaje verde oscuro), con el canto suavizado — nunca duro;
  2. se lleva su brillo al del MURO DESTINO por la mediana del follaje, no a ojo:
     el objetivo es quedar ~1,9× sobre la mediana del muro, que es visible sin
     ser un foco;
  3. se conserva el desenfoque: no se afila. Un globo más blando que el follaje
     se lee LEJOS, que es exactamente donde tiene que estar;
  4. y se REPARTEN A LO LARGO DEL PAR, no uno en cada slide: el par abre en el
     extremo izquierdo (sólo lo ve la slide 1) y uno solo cierra en el derecho
     (sólo lo ve la slide 2). Repetir el adorno en las dos rompe la continuidad
     y la pieza parece plantilla — está escrito en el manual.

Salida: raw/hilton/between/togo-25jul2025/base-r16-muro.jpg (5760×3840),
con la MISMA geometría que la 257, así que todos los recortes y todas las
mediciones del pipeline siguen valiendo tal cual.
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-257.jpg"
# ⚠️ Los globos NO se sacan de la generación de la escena (`cumple-fondo-r16.png`):
# ahí salen CORTADOS por el canto superior del cuadro y sin cuello ni hilo, así
# que recortados se leían como manchas pálidas — probado y descartado. Se generó
# material propio, con los tres globos enteros, separados entre sí y con espacio
# alrededor, justo para poder recortarlos.
GEN = RAIZ / "public/assets/hilton/between/ia-sept/cumple-globos-r16.png"
SALIDA = RAIZ / "raw/hilton/between/togo-25jul2025/base-r16-muro.jpg"
PASOS = RAIZ / "out/hilton-between-r16/pasos"

# ── el muro de la toma ───────────────────────────────────────────────────────
# El canto de la mesa está en y≈1834; el muro es todo lo de arriba. Y el vaso
# —el protagonista— ocupa x 3613..4712 desde y≈1204: ningún globo entra ahí.
MURO_Y1 = 1834
VASO_X0, VASO_X1, VASO_Y0 = 3613, 4712, 1204

# ── de dónde se sacan los globos en la generación ────────────────────────────
# Las cajas salen de `connectedComponentsWithStats` sobre la máscara de globo,
# no de mirar la imagen: el par de la izquierda y un solo globo del grupo derecho.
# Cajas leídas de `connectedComponentsWithStats` sobre la máscara de globo del
# material propio, con margen. El globo de la IZQUIERDA de esa generación no se
# usa: toca una franja de muro claro y la máscara se lo lleva entero.
RECORTES_GEN = {
    "grande": (2700, 580, 3890, 2600),     # el del medio: cuerpo + hilo largo
    "chico":  (3880, 470, 5040, 1980),     # el de la derecha, más lejano
}
# Una zona de FOLLAJE PURO de la misma generación —sin globo ni hilo—, que es la
# regla de medida para calibrar el desenfoque contra el muro de la toma real.
FOLLAJE_REF = (2100, 1900, 2700, 2500)

# ── dónde van sobre la toma real ─────────────────────────────────────────────
# slide 1 recorta x 1830..4902 · slide 2 recorta x 2688..5760
# La regla del manual: los adornos NO se repiten en las dos slides, se REPARTEN
# a lo largo del par — el par abre a la izquierda y uno solo cierra a la derecha.
#   · el PAR   en x 1880..2490 → x < 2688, así que lo ve SÓLO la slide 1
#   · el SOLO  en x 4990..5470 → x > 4902, así que lo ve SÓLO la slide 2
# Y ninguno pisa el vaso (x 3613..4712), que es el protagonista.
# ⚠️ El par BAJÓ 370 px respecto de la primera pasada (iba en y=60 y y=350).
# Arriba choca con el TITULAR: en la slide 1 «¿Estás de cumpleaños? / ESTE CAFÉ ES
# PARA TI» ocupa el borde superior de lado a lado, y el globo le quedaba detrás de
# la script. Y no se puede mover a la derecha: la franja exclusiva de la slide 1
# es sólo x 1830..2688 (de 2688 en adelante la ve también la slide 2 y el adorno
# se repetiría, que es justo lo que el manual prohíbe). Así que baja, al hueco
# entre el titular y los globos ilustrados de Eli.
# ⚠️ SEGUNDA CORRECCIÓN DE ALTURA (ronda 17). A y=430 el globo grande seguía
# CHOCANDO con el titular: medido sobre el render, su cuerpo caía en y 393..1083
# de la base, que en la pieza es y 290..798, y la script «¿Estás de cumpleaños?»
# ocupa y 345..508. Bajan al hueco real que hay entre el titular y el plato:
#   titular, canto inferior ....... pieza y ≈ 660  → base y ≈  900
#   plato, canto superior ......... pieza y ≈1550  → base y ≈2116
SIEMBRA = [
    # (recorte, x, y, ancho destino, espejar)
    ("grande", 1940,  980, 520, False),
    ("chico",  2160, 1180, 330, False),
    ("grande", 4990,   90, 480, True),
]

# ⚠️ Subió de 1,9 a 2,45 después de mirar la primera pasada: a 1,9 los globos
# quedaban al mismo valor que el follaje y se leían como manchas grises, no como
# globos champán. Un globo pálido ES lo más claro del muro; «sutil» es que sea
# pequeño y esté fuera de foco, no que esté apagado.
OBJETIVO = 2.45       # cuántas veces la mediana del muro tiene que dar el globo
# Y se le devuelve la calidez que el escalado plano le quita: el globo es champán,
# no gris. Factores sobre R y B, normalizados en verde.
CALIDEZ = (1.045, 1.0, 0.945)


def mascara_globo(a):
    """Aísla el globo: claro y cálido contra follaje verde oscuro.
    Devuelve alfa en 0..1 con el canto suavizado — un globo fuera de foco NUNCA
    tiene canto duro, y un alfa binario es lo que delata un recorte."""
    L = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114
    calido = a[..., 0] >= a[..., 1] - 4
    duro = ((L > 112) & calido).astype(np.float32)
    # se cierra para que no queden agujeros del follaje que cruza por delante
    duro = cv2.morphologyEx(duro, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    # y se queda sólo con la mancha grande: las motas sueltas son follaje claro
    n, et, est, _ = cv2.connectedComponentsWithStats((duro > 0.5).astype(np.uint8), 8)
    if n > 1:
        mayor = 1 + int(np.argmax(est[1:, 4]))
        duro = (et == mayor).astype(np.float32)
    alfa = cv2.GaussianBlur(duro, (0, 0), 9.0)

    # ⛔⛔ EL ALFA TIENE QUE MORIR EN EL BORDE DEL RECORTE, Y ESTO ERA UN BUG.
    # En la primera pasada el globo derecho tocaba el canto superior del recorte,
    # así que su alfa valía 1 justo en el borde y al componerlo dejaba un CANTO
    # RECTANGULAR perfectamente visible sobre el muro — un rectángulo pegado, que
    # es el peor delator posible de un montaje. Se fuerza una caída a 0 en un
    # margen del 4 % del lado, y así el parche no puede tener borde recto.
    al, an = alfa.shape
    m = max(8, int(min(al, an) * 0.04))
    caida = np.ones((al, an), np.float32)
    r = np.linspace(0.0, 1.0, m)
    caida[:m, :] *= r[:, None]
    caida[-m:, :] *= r[::-1][:, None]
    caida[:, :m] *= r[None, :]
    caida[:, -m:] *= r[::-1][None, :]
    return alfa * caida


def var_lap(im):
    g = np.asarray(im.convert("L")).astype(np.float64)
    return float(cv2.Laplacian(g, cv2.CV_64F).var()) if g.size else 0.0


def radio_por_follaje(gen, follaje_caja, escala, var_destino):
    """⭐ Cuánto hay que desenfocar el globo — calibrado FOLLAJE contra FOLLAJE.

    ⛔ El primer intento midió la varianza del laplaciano DENTRO del globo y la
    comparó con la del muro: dio 4,6 contra 34 y concluyó «no hace falta
    desenfocar». La medición estaba mal planteada, no el resultado. El interior
    de un globo **es** liso —no tiene detalle que medir—, así que compararlo con
    el detalle de unas hojas no dice nada. Lo que delata un montaje es el CANTO.

    La forma honesta es comparar lo comparable: el muro vegetal de la generación
    de donde sale el globo, contra el muro vegetal de la toma que lo recibe, **a
    la misma escala de píxel** (la que impone el resize del globo). Si el follaje
    de origen sigue siendo más nítido que el de destino, ese exceso es justo el
    desenfoque que le falta al globo.

    Los dos son follaje fuera de foco de un muro vegetal con la misma óptica, así
    que la comparación es legítima.
    """
    trozo = gen.crop(follaje_caja)
    nuevo = (max(8, int(trozo.width * escala)), max(8, int(trozo.height * escala)))
    trozo = trozo.resize(nuevo, Image.LANCZOS)
    v0 = var_lap(trozo)
    if v0 <= var_destino:
        print(f"    follaje origen {v0:.1f} ≤ destino {var_destino:.1f} → sin desenfoque extra")
        return 0.0
    for radio in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.5, 7.0, 9.0, 12.0):
        v = var_lap(trozo.filter(ImageFilter.GaussianBlur(radio)))
        if v <= var_destino:
            print(f"    follaje origen {v0:.1f} → {v:.1f} con {radio:.1f} px "
                  f"(destino {var_destino:.1f})")
            return radio
    print(f"    follaje origen {v0:.1f}: no baja de {var_destino:.1f} ni con 12 px")
    return 12.0


def mediana_follaje(a):
    """Mediana de luminancia del FOLLAJE (verde), que es la referencia honesta —
    la mediana del cuadro completo la mueven los globos o la mesa."""
    L = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114
    verde = a[..., 1] > a[..., 0]
    return float(np.median(L[verde])) if verde.any() else float(np.median(L))


def main():
    if not BASE.exists():
        sys.exit(f"falta la toma original: {BASE}")
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN} — corre magnific.py pro")

    base = Image.open(BASE).convert("RGB")
    gen = Image.open(GEN).convert("RGB")
    print(f"toma real   {base.size}   ·   generación {gen.size}")

    a = np.asarray(base).astype(np.float32)
    muro_ref = mediana_follaje(a[:MURO_Y1])
    print(f"mediana del follaje del muro real: {muro_ref:.1f}  "
          f"→ objetivo del globo: {muro_ref * OBJETIVO:.1f}")

    PASOS.mkdir(parents=True, exist_ok=True)

    for nombre, dx, dy, anc, espejo in SIEMBRA:
        caja = RECORTES_GEN[nombre]
        trozo = gen.crop(caja)
        if espejo:
            trozo = trozo.transpose(Image.FLIP_LEFT_RIGHT)
        t = np.asarray(trozo).astype(np.float32)
        alfa = mascara_globo(t)
        if alfa.max() < 0.2:
            sys.exit(f"no se aisló el globo «{nombre}»")

        # el brillo del globo, medido sobre sus propios píxeles
        L = t[..., 0] * 0.299 + t[..., 1] * 0.587 + t[..., 2] * 0.114
        dentro = alfa > 0.75
        brillo = float(np.median(L[dentro]))
        k = (muro_ref * OBJETIVO) / max(brillo, 1.0)
        print(f"\n· globo «{nombre}»: recorte {trozo.size} · alfa {alfa.mean():.3f} · "
              f"brillo {brillo:.1f} → ×{k:.3f}")

        # se escala el brillo ANTES de redimensionar, y con alfa premultiplicado
        # (girar/escalar sin premultiplicar arrastra el fondo al canto: es el
        # halo negro que el cliente leyó como «quemado» en la ronda 14)
        t2 = np.clip(t * k * np.array(CALIDEZ, np.float32)[None, None, :], 0, 255)
        pm = np.dstack([t2 * alfa[..., None], alfa[..., None] * 255.0])
        pmi = Image.fromarray(np.clip(pm, 0, 255).astype(np.uint8), "RGBA")
        alt = int(round(anc * pmi.height / pmi.width))
        pmi = pmi.resize((anc, alt), Image.LANCZOS)

        # ⭐ el desenfoque se calibra FOLLAJE contra FOLLAJE (ver la función).
        # Nunca se afila: si sobra desenfoque, el globo se lee más lejos, que es
        # justo donde tiene que estar.
        var_muro = var_lap(base.crop((dx, dy, min(dx + anc, base.width),
                                      min(dy + alt, MURO_Y1))))
        radio = radio_por_follaje(gen, FOLLAJE_REF, anc / (caja[2] - caja[0]), var_muro)
        if radio:
            pmi = pmi.filter(ImageFilter.GaussianBlur(radio))

        p = np.asarray(pmi).astype(np.float32)
        rgb_pm, al = p[..., :3], p[..., 3:4] / 255.0

        y0, x0 = dy, dx
        y1, x1 = min(y0 + alt, MURO_Y1), min(x0 + anc, a.shape[1])
        if y1 <= y0 or x1 <= x0:
            sys.exit(f"el globo «{nombre}» cae fuera del muro")
        # candado: nunca sobre el vaso, que es el protagonista
        if not (x1 <= VASO_X0 or x0 >= VASO_X1) and y1 > VASO_Y0:
            sys.exit(f"el globo «{nombre}» pisaría el vaso — mueve la siembra")

        zi, zj = slice(y0, y1), slice(x0, x1)
        za = al[: y1 - y0, : x1 - x0]
        zc = rgb_pm[: y1 - y0, : x1 - x0]
        a[zi, zj] = a[zi, zj] * (1.0 - za) + zc
        print(f"  puesto en x {x0}..{x1}  y {y0}..{y1}  ({anc}×{alt})")

    salida = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    b = np.asarray(salida).astype(np.float32)
    print(f"\nmuro final: mediana del follaje {mediana_follaje(b[:MURO_Y1]):.1f}")
    salida.save(SALIDA, quality=96, subsampling=0)
    salida.resize((salida.width // 4, salida.height // 4), Image.LANCZOS).save(
        PASOS / "muro-r16.jpg", quality=88)
    print(f"✓ {SALIDA.relative_to(RAIZ)}  {salida.size}")
    print(f"  vista: {(PASOS / 'muro-r16.jpg').relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

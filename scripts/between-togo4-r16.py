#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SLIDE 4 del carrusel PROMOS TO GO (S3) — ronda 16: la escena, al mundo de la marca.

Eli, 07-09-2026: «el 4 vuelve a hacer ese ya que se ve extraño la foto de fondo
y todo».

⭐⭐⭐ EL DEFECTO ERA DE COHERENCIA DE CARRUSEL, Y SE VE PONIENDO LAS TRES JUNTAS

Las slides 2 y 3 —las que Eli mandó no tocar— comparten un mundo: **mesa de
madera miel y muro vegetal verde fuera de foco**, que es el Between real. La
slide 4 tenía un **panel azul marino** con listones de madera cortados arriba y
una mesa muy barnizada con reflejos naranjas: un interior de bar. No es que
estuviera mal revelada — estaba en otro sitio.

Y de ahí viene toda la historia de esta pieza, que llevaba tres rondas de
revelado peleando contra el escenario:

    ronda 12   «se ve quemada»          → naranja saturado (calidez 55,3)
    ronda 13   «se ve extraño el color» → se pasó: saturación bajo las hermanas
    ronda 14   se calibra contra el render
    ronda 15   «sigue oscuro»           → se levantan las sombras (p10 30 → 46)

> **Cuando tres rondas de revelado no logran meter una pieza en su carrusel, el
> problema es la ESCENA, no el revelado.**

Así que la escena se regeneró con Nano Banana Pro pasándole la propia slide 4
como referencia y cambiando **sólo el fondo y la mesa**: muro vegetal verde muy
fuera de foco y mesa de madera miel mate, los de sus hermanas. Se conserva todo
lo demás —la bolsa atrás, la mano con el vaso, el sándwich sobre el papel y el
muffin de chocolate—, que era lo aprobado del contenido.

⚠️ Y con la escena nueva **la corrección de tono se invierte**. Medido:

    pieza                          mediana    p10   calidez   saturación
    slide 2 (intacta)                104,0   28,3      26,6        44,3
    slide 3 (intacta)                114,7   37,8      38,8        40,4
    slide 4 · ronda 15               109,1   49,2      28,7        34,2
    slide 4 · r16 generada cruda     151,5   70,8      76,6        50,7

La generación viene **clara y muy naranja**, al revés que la vieja. Así que se le
baja calidez y saturación y se le sube el punto negro — y ⛔ **NO se llama
`abre_sombras()`**: su p10 ya está en 70,8 contra los 28-38 de las hermanas, o
sea que las sombras están de sobra abiertas. Aplicarlo por costumbre, porque «la
ronda 15 lo necesitaba», es exactamente el error de arrastrar un parámetro a una
escena distinta.

⭐ LOS DOS LOGOTIPOS, RE-MEDIDOS con cuadrícula sobre la ventana nueva:

    cara frontal de la bolsa ....... x  760..1790 (1030)   y  580..2040 (1460)
    cuerpo del vaso ................ x  205.. 565 ( 360)   y 1205..2050 ( 845)
    la mano cubre el vaso .......... desde y=1370

⚠️ En esta toma la mano envuelve el vaso entero: por debajo de y=1370 sólo queda
un lienzo limpio de 95 px a la derecha. El logotipo del vaso va por eso en la
banda bajo la tapa — acá no se puede aplicar el truco de la portada («los dedos
lo tapan»), porque los dedos taparían el 80 % del lockup y eso no es una
oclusión, es un logotipo roto. La bolsa es la que firma grande en esta slide.

Y el ancho del vaso va a **0,80 de la cara visible**, no a 0,86: el vaso está
cerca y girado, y la lección de la ronda 9 vale igual — un logo CORTADO por la
silueta es peor que un logo un 7 % más chico.

Salida: public/assets/hilton/between/fotos-gradadas/togo-trio-r16.jpg
"""
import importlib.util
import sys
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from between_retoque import hombro, informe  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ⭐ Se REUSAN `estampa` e `iguala_tono` de la ronda 12 en vez de copiarlas: son
# las que ya pasaron por cuatro rondas de correcciones del cliente y cada línea
# suya está justificada en su propio archivo. El nombre del módulo lleva guiones,
# así que se carga por ruta.
_spec = importlib.util.spec_from_file_location(
    "between_togo4_r12", RAIZ / "scripts/between-togo4-r12.py")
_r12 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_r12)
estampa, iguala_tono = _r12.estampa, _r12.iguala_tono

GEN = RAIZ / "public/assets/hilton/between/ia-sept/togo-trio-gen-r16.png"
SALIDA = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-trio-r16.jpg"

RECORTE_ARRIBA = 160
SALIDA_PX = (2250, 2812)

# ── medido con cuadrícula sobre la ventana 4:5 de ESTA generación ────────────
# ⛔⛔ CORREGIDO EN LA RONDA 17, y era el reclamo de Eli «el logo se ve mal
# maqueteado con respecto a la posición en que está la bolsa».
# Medido con cuadrícula sobre la ventana de ESTA generación, la cara frontal va
# de x=760 a x=1920 (1160 px, centro 1340) y de y=640 a y=1950. Yo la tenía en
# (760, 580, 1790, 2040): centro 1275 y 1030 de ancho, o sea el logotipo quedaba
# **65 px descentrado a la izquierda** y un 11 % más chico de lo que corresponde.
# La cara de una bolsa girada no se estima: su canto derecho es donde cambia el
# tono al panel lateral, y eso se lee en la cuadrícula.
CARA_BOLSA = (760, 640, 1920, 1950)
# ⚠️ CORREGIDO: la primera pasada puso el cuerpo en x 205..565 leyendo la
# cuadrícula a ojo, y estaba MAL — el logotipo caía medio fuera del vaso y la
# máscara de cartón lo dejaba en fragmentos («cartón en la caja: 20 %»), que es
# justo el «logotipo roto» que la ronda 9 ya había diagnosticado.
# Medido bien: la TAPA NEGRA se aísla por componentes conexas (oscura y neutra)
# y da x 327..890 (563 px) · y 1028..1212. De ahí sale todo lo demás.
CUERPO_VASO = (340, 1212, 875, 2050)  # el cuerpo, ~95 % del ancho de la tapa
MANO_DESDE = 1387                     # por debajo de acá el vaso está tapado

RATIO_BOLSA = 0.50                    # del ancho de la cara (regla de la r15)
RATIO_VASO = 0.80                     # de la cara visible del cilindro

# objetivo = media de las slides 2 y 3, medidas sobre sus FOTOS
OBJ_MEDIANA, OBJ_CALIDEZ, OBJ_SATURACION = 109, 33.0, 42.0


def main():
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN}")
    im = Image.open(GEN).convert("RGB")
    print(f"generación {im.width}×{im.height}")
    alto = int(round(im.width / 0.8))
    y0 = min(RECORTE_ARRIBA, im.height - alto)
    im = im.crop((0, y0, im.width, y0 + alto)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"recorte 4:5 desde y={y0} ({im.width}×{im.height})")
    informe(im, "generada")

    bx0, by0, bx1, by1 = CARA_BOLSA
    print("   BOLSA:")
    # ⚠️ 0,50 del alto y no 0,544: con la cara re-medida, a 0,544 el sello caía
    # sobre el pliegue horizontal del papel (y≈1420). A 0,50 queda por encima.
    im = estampa(im, ((bx0 + bx1) // 2, int(by0 + 0.50 * (by1 - by0))),
                 int(round(RATIO_BOLSA * (bx1 - bx0))))

    vx0, vy0, vx1, vy1 = CUERPO_VASO
    anc_v = int(round(RATIO_VASO * (vx1 - vx0)))
    # el lockup mide 1/3,0273 de su ancho; se centra en la banda limpia que hay
    # entre el canto de la tapa y donde arranca la mano
    alt_v = int(round(anc_v / 3.0273))
    cy_v = vy0 + (MANO_DESDE - vy0) // 2
    print("   VASO:")
    print(f"      banda limpia y {vy0}..{MANO_DESDE} ({MANO_DESDE - vy0} px) · "
          f"lockup {anc_v}×{alt_v} centrado en y={cy_v}")
    # ⛔⛔ SIN `mascarar_carton`, y por dos razones — la primera pasada lo dejó en
    # True «por si acaso» y el logotipo salió ROTO: se leía «TWEEN / FEE & BAR».
    #
    # 1. La máscara separa cartón de piel por la razón **B/R < 0,62**, y en esta
    #    escena eso ya no vale: el flanco IZQUIERDO del vaso recibe rebote verde
    #    del muro vegetal y su B/R sube a 0,70. Medido por tramos dentro de la
    #    caja del logotipo:
    #        x 393..453 → 0,703   x 573..633 → 0,535
    #        x 453..513 → 0,667   x 693..753 → 0,429
    #    O sea que la máscara declaraba «no cartón» el tercio izquierdo del vaso
    #    y se comía la «B», la «E» y el «COF».
    #    ⚠️ Y subir el umbral no es la respuesta: en esta marca la PIEL da B/R
    #    ≈0,51, o sea MÁS BAJO que el cartón en sombra. B/R no separa piel de
    #    cartón acá; el que separa es G/R (cartón 0,74 · piel 0,58).
    # 2. Pero sobre todo: **no hay nada que enmascarar.** La caja del logotipo va
    #    de y=1229 a y=1370 y la mano empieza en y=1387. Y en x el logotipo
    #    (393..821) queda dentro de la silueta del vaso (340..875), así que
    #    tampoco se derrama sobre la bolsa de atrás.
    #
    # Regla: una máscara sólo se enciende si hay algo que tape, y su umbral se
    # re-mide en cada escena. Heredada de otra toma, resta en vez de proteger.
    im = estampa(im, ((vx0 + vx1) // 2, cy_v), anc_v, mascarar_carton=False)

    im = iguala_tono(im, mediana=OBJ_MEDIANA, calidez=OBJ_CALIDEZ,
                     saturacion=OBJ_SATURACION)
    # ⛔ sin `abre_sombras()`: ver la cabecera — el p10 de esta escena ya está en
    #    70,8 contra 28-38 de sus hermanas.
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    informe(im, "final")

    a = np.asarray(im).astype(np.float32)
    g = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114
    mx, mn = a.max(axis=2), a.min(axis=2)
    print(f"   control: mediana {np.median(g):.1f} · p10 {np.percentile(g, 10):.1f} · "
          f"calidez {(a[..., 0] - a[..., 2]).mean():.1f} · "
          f"saturación {np.where(mx > 0, (mx - mn) / np.maximum(mx, 1) * 100, 0).mean():.1f}")
    print("   (hermanas: mediana 104/115 · p10 28/38 · calidez 27/39 · sat 44/40)")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    im.save(SALIDA, quality=95, subsampling=0)
    print(f"-> {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

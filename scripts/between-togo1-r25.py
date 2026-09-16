#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO — ronda 25 (16-09-2026): la portada cambia de FOTO, no de diseño.

Lo que pide la ronda, literal de la grilla viva (`FEED!L15`, prepended arriba de
todo, o sea lo más nuevo):

    «Perdón, se puso mal el enlace: es esta en la G1
     https://drive.google.com/file/d/1ZUClVyKcfy_WNcXw8eKhSxe46H7Dpv3i/view»

O sea que el pedido de la ronda 23 —«armar una foto en la G1 con las fotos
sacadas por Seba»— seguía en pie, pero la foto elegida era otra. La ronda 23 usó
`togo-en-mano-entrada.jpg` (IMG_4170, la persona en la entrada del local); el
enlace corregido apunta a **IMG_4146**, que es el vaso sostenido sobre la mesa
de listones. Verificado por md5: el archivo que bajó del enlace es idéntico a
`raw/hilton/between/vasos-togo-sep2026/IMG_4146.HEIC`, ya curado en el repo como
`public/assets/hilton/between/togo-sep2026/togo-en-mano-mesa.jpg`.

⚠️ El enlace baja un **HEIC con extensión `.jpg`** — no está roto, es un iPhone
(memoria `heic-no-es-archivo-roto`). No hizo falta convertirlo: la foto ya
estaba en el repo.

⭐ EL DISEÑO NO SE TOCA. Eli cerró los textos de esta portada en la ronda 24
(«quiero los textos de la portada como estaban antes… si necesitas algo puedes
añadir una transparencia en opacidad o degradado») y el cliente marcó las otras
tres slides como OK. Acá cambia la placa de fondo y nada más.

⛔ EL RECORTE SE CORTA POR ABAJO, AL REVÉS QUE LA R23, Y ES POR EL LOGOTIPO.
La toma es 3:4 (3024×4032) y el feed es 4:5, así que sobran 252 filas. Cortando
por arriba —como la r23— el vaso queda BAJO y la script «¿Vas con poco tiempo?»
cae encima de su wordmark: medido sobre ese render, la tinta del logotipo
impreso cierra en y≈733 y la script entra en 745, o sea que se pisan. Romper el
logotipo del vaso es el peor error posible en una pieza cuyo héroe es ese vaso
(manual § «el garabato no toca el producto»).
Cortando por abajo el vaso sube 90 px en el lienzo de 1080 y el logotipo queda
entero, con aire, por encima del bloque de texto. Se pierden 252 filas de mesa
al pie, que es justo la franja que el degradado tapa de todas formas.

Salida: public/assets/hilton/between/fotos-gradadas/togo-portada-r25.jpg
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import revela, vivo  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = Path("public/assets/hilton/between/togo-sep2026/togo-en-mano-mesa.jpg")
DESTINO = Path("public/assets/hilton/between/fotos-gradadas/togo-portada-r25.jpg")

#: ⛔ NO SE COPIAN LOS PARÁMETROS DE LA R23, Y ESO SE MIDIÓ.
#: La r23 usa `CALOR=0,08` y `calidez_max=99` porque aquella toma era de
#: exterior, de luz fría, y venía en calidez 9,7: había que EMPUJARLA. Ésta es
#: otra foto: mesa de madera al sol, y ya viene en **38,5** de calidez, por
#: encima de los 25,9 del set. Aplicándole la receta de la r23 tal cual sube a
#: **66,3** — o sea, justo el «filtro de color cálido» que el cliente mandó
#: eliminar dos veces («Eliminar el filtro de color cálido que tiene el carrusel
#: completo», 01-09).
#: Acá el calor va en 0 y `calidez_max` en el valor del set, para que `revela`
#: ENFRÍE hasta ahí. La densidad sí se iguala igual: mediana objetivo 104.
#: La vibrancia también baja: esta toma ya tiene croma 21,7 (la de la entrada
#: tenía 9,7), así que 0,30 la manda a 35,6 y el carrusel se despareja.
#:
#: ⚠️ `calidez_max` NO es el objetivo: `revela` sólo quita el 55 % del exceso, y
#: después el contraste y la vibrancia devuelven algo. Medido, la ventana nueva
#: —casi todo madera al sol— entra en calidez 50,9, y el barrido da:
#:      max 22 → 40,1 · max 16 → 36,6 · max 10 → 33,1 · max 4 → 29,5
#: Se deja en 10 (→ 33,1). El set del carrusel está en 25,9 y la portada
#: APROBADA de la r23 cerró en 34,2 sobre un set de 29,2, o sea que una portada
#: ~5 puntos sobre su set ya es lo aceptado. Bajar a 4 la acerca más pero
#: empieza a apagar la madera, y el manual es explícito: «la calidez sólo se
#: corrige si SOBRA».
CALOR, MEDIOS, VIBRANCIA, CALIDEZ_MAX = 0.0, 104, 0.12, 10.0


def calienta(im, k):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    a[..., 0] = np.clip(a[..., 0] * (1 + k * 0.8), 0, 255)
    a[..., 2] = np.clip(a[..., 2] * (1 - k * 0.9), 0, 255)
    return Image.fromarray(a.astype(np.uint8))


#: ⭐ LA VENTANA 4:5, CALCULADA — no elegida a ojo.
#: Restricciones medidas sobre la toma (3024×4032):
#:   · la tapa negra del vaso va de la fila 1244 a la 1649;
#:   · la tinta del logotipo impreso cierra en la fila ≈2593;
#:   · el bloque de texto de la pieza —ya aprobado por Eli en la r24— ocupa de
#:     y=718 a y=1202 del lienzo de 1350, o sea desde el 53,2 % del alto.
#: O sea que el logotipo tiene que cerrar por encima del 52 % de la ventana y la
#: tapa tiene que entrar con algo de aire. Resolviendo las dos:
#:      alto 2930 · arranque en la fila 1070  →  logotipo al 52 %, tapa al 6 %
#: y la ventana cierra en la fila 4000, justo dentro de las 4032 de la toma.
#: ⚠️ No hay holgura: con la ventana a ancho completo (3024×3780) el logotipo
#: caía en el 60-66 % y el titular se le montaba encima.
VENTANA = {"x_centro": 1300, "ancho": 2344, "y0": 1070, "alto": 2930}


def corta_4_5(im):
    v = VENTANA
    x0 = max(0, v["x_centro"] - v["ancho"] // 2)
    x1 = min(im.width, x0 + v["ancho"])
    y1 = min(im.height, v["y0"] + v["alto"])
    return im.crop((x0, v["y0"], x1, y1))


def medir(im):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a.mean(2)
    return (float(np.median(a)), float(a[..., 0].mean() - a[..., 2].mean()),
            float(np.abs(a - g[..., None]).max(2).mean()), float((a > 250).mean() * 100))


def main():
    im = corta_4_5(Image.open(ORIGEN).convert("RGB"))
    antes = medir(im)
    base = calienta(im, CALOR) if CALOR else im
    out = vivo(revela(base, medios=MEDIOS, calidez_max=CALIDEZ_MAX),
               vibrancia=VIBRANCIA)
    desp = medir(out)
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    out.save(DESTINO, "JPEG", quality=95, subsampling=0)
    print(f"recorte 4:5 .......... {im.size[0]}×{im.size[1]}  ({im.size[0]/im.size[1]:.3f})")
    print(f"mediana .............. {antes[0]:6.1f} -> {desp[0]:6.1f}   (set: 101)")
    print(f"calidez .............. {antes[1]:6.1f} -> {desp[1]:6.1f}   (set: 25,9)")
    print(f"croma ................ {antes[2]:6.1f} -> {desp[2]:6.1f}   (set: 21,5)")
    print(f"% blanco puro ........ {desp[3]:6.2f}")
    print(f"\n-> {DESTINO}")


if __name__ == "__main__":
    main()

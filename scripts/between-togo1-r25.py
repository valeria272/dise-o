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

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = Path("public/assets/hilton/between/togo-sep2026/togo-en-mano-mesa.jpg")
DESTINO = Path("public/assets/hilton/between/fotos-gradadas/togo-portada-r25.jpg")

#: ⛔⛔ RONDA 2 (16-09) — ESTA FOTO NO SE GRADA. NADA.
#: Eli, sobre la primera pasada: «la última no se ve nada, el carrusel de la
#: portada muy oscura y quemada. NO EDITES LA FOTO ORIGINAL, déjala así tal cual
#: el link. Pero con textos y diseños de arriba y transparencia. Solo reemplaza
#: la foto.»
#:
#: La primera pasada sí la gradaba —mediana 116→102 para igualar al set, y la
#: calidez de 50,9 a 33,1— y entre eso y el degradado al pie la lámina se leía
#: apagada. El encargo ahora es explícito y es el contrario: **la foto entra tal
#: como viene del enlace**. Lo único que se hace es el recorte 4:5, que no es
#: opcional (la toma es 3:4 y el feed es 4:5).
#:
#: ⚠️ Queda anotado que el set del carrusel está en mediana 101 y esta toma en
#: 116: la portada va a leer más clara que las otras tres slides. Es decisión de
#: ella y está pedida por escrito.
#: ⭐ LA VENTANA 4:5, CALCULADA — no elegida a ojo.
#: Restricciones MEDIDAS sobre la toma (3024×4032):
#:   · la tapa negra del vaso va de la fila 1244 a la 1649;
#:   · el logotipo impreso son DOS bandas de tinta: el wordmark en 2239–2513 y
#:     «COFFEE & BAR» en 2617–2685. **Manda la segunda**, y ése fue el error de
#:     la pasada anterior: se calculó contra el wordmark (2593) y el script
#:     «¿Vas con poco tiempo?» terminaba rozando el «COFFEE & BAR».
#:   · el bloque de texto —el que Eli cerró en la r24— arranca en y=718 de 1350,
#:     o sea en el 53,2 % del alto.
#: Con el logotipo completo cerrando en la fila 2685 y la ventana obligada a
#: terminar dentro de las 4032 filas de la toma, la condición «logotipo por
#: encima del 50 %» deja **alto ≤ 2 × (4032 − 2685) = 2694**:
#:      alto 2694 · ancho 2155 · arranque en la fila 1338
#: → el logotipo queda en 33–50 % y el texto entra en 53,2 %: 43 px de aire.
#: ⚠️ EL PRECIO: la tapa se corta por el canto de arriba (la ventana entra en la
#: fila 1338 y la tapa empieza en la 1244). Es inevitable — con la tapa entera el
#: logotipo no puede quedar sobre el texto, y eso está demostrado: haría falta
#: alto ≥ 2882 y el máximo que cabe es 2788.
#: ⚠️ Y el otro precio: 2155 px de ancho contra los 2250 de la entrega, o sea un
#: 4,4 % de ampliación. Es lo mínimo que permite la toma.
VENTANA = {"x_centro": 1300, "ancho": 2155, "y0": 1338, "alto": 2694}


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
    out = im                       # ← sin revelado, sin vibrancia, sin calor
    desp = medir(out)
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    out.save(DESTINO, "JPEG", quality=95, subsampling=0)
    print(f"recorte 4:5 .......... {im.size[0]}×{im.size[1]}  ({im.size[0]/im.size[1]:.3f})")
    print(f"mediana .............. {desp[0]:6.1f}   (set: 101 — no se iguala, ver cabecera)")
    print(f"calidez .............. {desp[1]:6.1f}   (set: 25,9)")
    print(f"croma ................ {desp[2]:6.1f}   (set: 21,5)")
    print(f"sin gradar: antes == despues -> {antes == desp}")
    print(f"% blanco puro ........ {desp[3]:6.2f}")
    print(f"\n-> {DESTINO}")


if __name__ == "__main__":
    main()

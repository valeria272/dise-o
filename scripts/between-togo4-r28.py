#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · slide 4 — ronda 28 (21-09-2026): la foto aprobada, y el café
un poco más grande. Nada más.

Eli, mirando la generada de la ronda 27 al lado de la original:

    «la última slide, el sándwich no se parece al real. tiene que ser como el
     del slide. me gustaba más la foto de proporción de la primera, pero el
     café un poco más grande, sutil»

⭐ Las dos frases mandan lo mismo: **se vuelve a la fotografía aprobada**. El
   sándwich de la escena generada era otro —pan rectangular grueso, relleno
   distinto— y el de la marca es el de la slide 2: pan de molde blanco sin
   corteza, tostado por arriba, cortado en triángulo, con palta y pollo. Ese ya
   está fotografiado en esta pieza; el generador no tenía que inventarlo.
   La ronda 27 queda archivada en `raw/hilton/between/s4/gen-r27/`.

⛔⛔ Y ESTA VEZ EL RETOQUE ES UNO SOLO Y SE VERIFICA. La ronda 26 escaló tres
   objetos con parches dilatados y el resultado fue el que Eli rechazó: 888.000
   px tocados de borde a borde, **el logotipo del vaso duplicado** y un pedazo
   del pan borrado. Acá:

     · se toca SÓLO el vaso, y a 1,10 — «sutil»;
     · el mate NO se dilata a los lados (`lado=0`), que es lo que arrastraba la
       bolsa de atrás y le mordía el canto;
     · se dilata 40 px SÓLO hacia abajo, que es lo justo para tapar el filo del
       canto viejo — el apoyo del vaso es una curva, no una recta, y al escalar
       desde el punto más bajo se levanta;
     · el plato vuelve POR DELANTE, con mate de grabCut verificado (el de color
       perdía el ala derecha y dejaba al vaso pintado encima);
     · y al final el script **mide el área tocada y aborta si se sale del
       vaso**. Un retoque que no se verifica contra la pieza miente en silencio.

Salida: public/assets/hilton/between/fotos-gradadas/togo-s4-r28.jpg
"""
import sys
from pathlib import Path

import cv2
import numpy as np

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-s4-r24.jpg"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-s4-r28.jpg"

CAJA_VASO = (1560, 1590, 2180, 2360)     # medida: tapa en y=1622, base en y=2308
CAJA_PLATO = (820, 2120, 1800, 2520)

#: ⭐ 1,10. Eli pidió «sutil». A 1,26 —la ronda 26— el vaso se le montaba al
#: plato y había que correrlo, y correrlo es lo que destapaba el vaso viejo.
ESCALA = 1.10
DILATA_ABAJO = 95
#: ⛔⛔ Y A LOS LADOS, CERO. Ni siquiera 14 px.
#: La pasada anterior dilataba 14 px «porque son 14 px de bolsa desplazados
#: 1,4 px: invisible». No lo era. Eli: «mira la línea de la bolsa». El PLIEGUE
#: horizontal de la bolsa cruza justo por ahí, y al escalar el parche ese
#: tramo de pliegue se corre un par de px respecto del que queda afuera: donde
#: la línea entra y sale del parche quedan dos escalones.
#: ⭐ La lección: **no importa cuánto se desplaza el fondo, sino si el fondo
#:    tiene una LÍNEA que lo delate.** Sobre madera desenfocada 14 px no se
#:    ven; sobre un pliegue recto, 1 px sí.
#: Los 289 px del canto de la tapa se tapan de otra forma — ver `estira_tapa`.
DILATA_LADO = 0

#: El vaso no puede salirse
#: El vaso no puede salirse de su zona. Si el retoque toca fuera de esta caja,
#: algo se movió que no debía y el script aborta.
ZONA_PERMITIDA = (1540, 1300, 2250, 2400)   # el vaso crece HACIA ARRIBA: su tapa
#: sube de y=1622 a 1465, y el parche empieza en 1329. La zona lo contempla.


def _grabcut(im, caja, margen, cierra, abre):
    x0, y0, x1, y1 = caja
    sub = im[y0:y1, x0:x1].copy()
    mk = np.zeros(sub.shape[:2], np.uint8)
    mx, my = margen
    cv2.grabCut(sub, mk, (mx, my, (x1 - x0) - 2 * mx, (y1 - y0) - 2 * my),
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                6, cv2.GC_INIT_WITH_RECT)
    k = np.where((mk == cv2.GC_FGD) | (mk == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    k = cv2.morphologyEx(k, cv2.MORPH_CLOSE, np.ones((cierra, cierra), np.uint8))
    k = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((abre, abre), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(k, 8)
    i = max(range(1, n), key=lambda j: st[j][4])
    # ⭐ macizo por el CONTORNO EXTERNO: grabCut abre agujeros dentro del objeto
    #   —le pasó al pan— y un mate con agujeros escala el borde y deja el
    #   relleno quieto: el objeto se parte.
    cnt, _ = cv2.findContours((lab == i).astype(np.uint8) * 255,
                              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    k = np.zeros_like(k)
    cv2.drawContours(k, [max(cnt, key=cv2.contourArea)], -1, 255, cv2.FILLED)
    lleno = np.zeros(im.shape[:2], np.uint8)
    lleno[y0:y1, x0:x1] = k
    return lleno


#: Cuánto se corre la muestra para rellenar la astilla. Tiene que caer FUERA
#: del vaso viejo: su canto está en x=1607 y 2111, y la astilla mide 8 px.
CLON_LADO = 25


def tapa_astilla(salida, original, alf, mate_viejo, cx):
    """⭐ Tapa la astilla del canto de la TAPA con bolsa, clonada EN HORIZONTAL.

    Al escalar desde la base, la fila más ancha del vaso —el canto de la tapa—
    se mapea a una fila de más abajo, donde el vaso es más angosto, y no se
    tapa a sí misma: quedan ~289 px del vaso viejo asomando a los dos costados,
    en las filas 1759-1790. Lo que corresponde ahí es FONDO: bolsa.

    ⛔ Dilatar el mate para cubrirlos mete bolsa DENTRO del parche y la escala:
       el pliegue horizontal de la bolsa se corre un par de px y quedan dos
       escalones donde entra y sale del parche. Es lo que cazó Eli.
    ⛔ Estirar la tapa hacia afuera tampoco: en esas filas el canto del vaso ya
       no es negro sino kraft, y quedan dos protuberancias claras.
    ⭐ La muestra se toma de la foto ORIGINAL, en la MISMA FILA, corrida 25 px
       hacia afuera — o sea fuera del vaso viejo. Clonar en horizontal es lo
       único que **no mueve una línea horizontal**, y el pliegue de la bolsa lo
       es: queda exactamente donde estaba.
    """
    resto = ((mate_viejo > 127) & (alf < 0.5))
    n = int(resto.sum())
    if not n:
        return salida, 0
    ys, xs = np.nonzero(resto)
    d = np.where(xs < cx, -CLON_LADO, CLON_LADO)
    nx = np.clip(xs + d, 0, salida.shape[1] - 1)
    m = np.zeros(salida.shape[:2], np.float32)
    m[ys, xs] = 1.0
    m = cv2.GaussianBlur(cv2.dilate(m, np.ones((3, 3), np.uint8)), (0, 0), 1.6)
    relleno = salida.copy()
    relleno[ys, xs] = original[ys, nx]
    return salida * (1 - m[..., None]) + relleno * m[..., None], n


def main():
    im = cv2.imread(str(ORIGEN))
    if im is None:
        sys.exit(f"no pude abrir {ORIGEN}")
    H, W = im.shape[:2]
    capa = im.astype(np.float32)
    print(f"foto aprobada ....... {W}×{H}")

    vaso = _grabcut(im, CAJA_VASO, (35, 15), 9, 7)
    plato = _grabcut(im, CAJA_PLATO, (20, 20), 15, 11)
    for nom, m in (("vaso", vaso), ("plato", plato)):
        ys, xs = np.nonzero(m)
        print(f"  {nom:6s} x {xs.min()}..{xs.max()} · y {ys.min()}..{ys.max()}")

    ys, xs = np.nonzero(vaso)
    base_y = int(ys.max())
    cx = int((xs.min() + xs.max()) / 2)

    # el parche: el vaso, 95 px de mesa por ABAJO y 14 px de aire alrededor
    patron = cv2.dilate(vaso, np.ones((DILATA_ABAJO * 2 + 1, 1), np.uint8), anchor=(0, 0))
    if DILATA_LADO:
        patron = cv2.dilate(patron, np.ones((DILATA_LADO * 2 + 1, DILATA_LADO * 2 + 1), np.uint8))
    alfa = cv2.GaussianBlur(patron.astype(np.float32) / 255.0, (0, 0), 6)

    M = np.float32([[ESCALA, 0, cx * (1 - ESCALA)], [0, ESCALA, base_y * (1 - ESCALA)]])
    cap = cv2.warpAffine(capa, M, (W, H), flags=cv2.INTER_LANCZOS4,
                         borderMode=cv2.BORDER_REPLICATE)
    alf = cv2.warpAffine(alfa, M, (W, H), flags=cv2.INTER_LINEAR,
                         borderMode=cv2.BORDER_CONSTANT, borderValue=0)

    resto = int(((vaso > 127) & (alf < 0.5)).sum())
    ys2, xs2 = np.nonzero(alf > 0.5)
    print(f"\nvaso × {ESCALA} ......... x {xs2.min()}..{xs2.max()} · y {ys2.min()}..{ys2.max()}"
          f"  (margen derecho {W - xs2.max()} px)")
    print(f"del vaso viejo asoma  {resto} px")
    a = alf[..., None]
    salida = capa * (1 - a) + cap * a
    salida, n_ast = tapa_astilla(salida, capa, alf, vaso, cx)
    print(f"astilla del canto de la tapa, rellenada con bolsa: {n_ast} px")

    # el plato, por delante: está más cerca de la cámara
    pa = cv2.GaussianBlur(plato.astype(np.float32) / 255.0, (0, 0), 1.6)[..., None]
    tapado = int(((pa[..., 0] > 0.5) & (alf > 0.5)).sum())
    salida = salida * (1 - pa) + capa * pa
    print(f"plato por delante ... {tapado} px del vaso que le tocaban, devueltos")

    out = np.clip(salida, 0, 255).astype(np.uint8)

    # ⭐ LA COMPUERTA: qué se movió de verdad
    d = (np.abs(im.astype(np.int16) - out.astype(np.int16)).max(2) > 12)
    ys3, xs3 = np.nonzero(d)
    zx0, zy0, zx1, zy1 = ZONA_PERMITIDA
    print(f"\nárea tocada ......... {d.sum() / 1000:.0f} k px"
          f" · x {xs3.min()}..{xs3.max()} · y {ys3.min()}..{ys3.max()}")
    fuera = int((d & ~np.pad(np.ones((zy1 - zy0, zx1 - zx0), bool),
                             ((zy0, H - zy1), (zx0, W - zx1)))).sum())
    if fuera > 200:
        sys.exit(f"⛔ ABORTA: {fuera} px tocados FUERA de la zona del vaso "
                 f"{ZONA_PERMITIDA}. Algo se movió que no debía.")
    print(f"fuera de la zona .... {fuera} px  ✅")

    cv2.imwrite(str(DESTINO), out, [cv2.IMWRITE_JPEG_QUALITY, 95])
    print(f"-> {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

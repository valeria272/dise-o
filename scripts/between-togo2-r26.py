#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · slide 2 — ronda 26 (21-09-2026): el sándwich crece un poco.

Eli: «ajustes en todas, lo que es sándwich es más grande solo un poco».

Es el mismo criterio que en la slide 4 y la misma operación: el sándwich con su
papel se escala **1,10 desde el centro de su apoyo**, así no despega de la mesa
y, al crecer, CONTIENE a su propia silueta anterior — no queda nada que
rellenar detrás, que es donde estos montajes se delatan.

⛔ EL MATE SE RELLENA POR DENTRO ANTES DE USARLO. grabCut le abre agujeros al
   pan: la miga tostada y el papel de estraza tienen el mismo color, así que el
   algoritmo se come trozos del centro del sándwich. Un mate con agujeros
   escala el borde y deja el relleno quieto — el objeto se parte. Se cierra
   tomando sólo el CONTORNO EXTERNO y pintándolo macizo.

⛔ NO SE TOCA NADA MÁS: ni el vaso —que es el patrón de escala del carrusel—,
   ni el encuadre, ni el revelado, ni la diagramación.

Salida: public/assets/hilton/between/fotos-gradadas/togo-s2-r26.jpg
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

ORIGEN = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-s2-r24.jpg"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-s2-r26.jpg"

#: caja medida sobre el asset de 2250×2812: contiene el sándwich y su papel, y
#: nada del vaso (que empieza en x=1400).
CAJA = (80, 1380, 1330, 2400)
ESCALA = 1.10


def ancla(mate):
    """Centro de la huella (en x) y punto de apoyo (en y).
    ⛔ El ancla en x NO sale de la fila de la base: ahí el papel se va en una
       punta a la derecha y el centro daba x=1139, o sea 435 px corrido — al
       escalar, el sándwich se movía de lugar. Va el centro de la CAJA."""
    ys, xs = np.nonzero(mate)
    return int((xs.min() + xs.max()) / 2), int(ys.max())


def parche_con_suelo(mate, abajo=70, lado=20, suave=14):
    """⭐⭐⭐ UN OBJETO QUE CRECE SE ESCALA CON UN POCO DE SU SUELO, NO SOLO.

    El apoyo de un objeto no es una línea horizontal: es una curva. Escalando
    desde el punto más bajo, toda columna cuyo canto inferior esté más arriba
    se levanta (s−1)·(distancia) y por debajo asoma el canto del VIEJO — una
    raya que dibuja el contorno anterior. En el papel de la slide 2 eran
    32.441 px y se veía como un filo doble.

    ⛔ Probé dos parches y los dos fueron peores:
       · **rellenar con lo que hay más abajo**: ahí están la sombra de contacto
         y el canto oscuro de la mesa, y queda una franja café;
       · **estirar el canto del objeto hacia abajo**: queda peinado, con el
         grano del borde repetido en vertical.

    Lo que sí: el mate se **dilata hacia abajo y a los lados** antes de
    escalar, así el parche se lleva su propio pedazo de mesa. El contorno
    viejo queda debajo del suelo nuevo —no del objeto— y la costura cae sobre
    madera lisa, donde un degradado de 14 px no se ve. La mesa de adentro del
    parche también se estira un 10 %, y sobre madera desenfocada eso es
    invisible.

    `abajo` tiene que ser ≥ (s−1)·(alto de la curva del apoyo); 70 px cubre
    los 170 px de curva del papel a escala 1,10 con holgura.
    """
    k_ab = np.ones((abajo * 2 + 1, 1), np.uint8)
    m = cv2.dilate(mate, k_ab, anchor=(0, 0))          # sólo hacia abajo
    if lado:
        m = cv2.dilate(m, np.ones((1, lado * 2 + 1), np.uint8))
    return cv2.GaussianBlur(m.astype(np.float32) / 255.0, (0, 0), suave)


def mate(im):
    x0, y0, x1, y1 = CAJA
    sub = im[y0:y1, x0:x1].copy()
    mk = np.zeros(sub.shape[:2], np.uint8)
    cv2.grabCut(sub, mk, (25, 25, (x1 - x0) - 50, (y1 - y0) - 50),
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                6, cv2.GC_INIT_WITH_RECT)
    k = np.where((mk == cv2.GC_FGD) | (mk == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    k = cv2.morphologyEx(k, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    k = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((11, 11), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(k, 8)
    i = max(range(1, n), key=lambda j: st[j][4])
    k = (lab == i).astype(np.uint8) * 255
    # ⭐ macizo: sólo el contorno externo, relleno. Ver la cabecera.
    cnt, _ = cv2.findContours(k, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    k = np.zeros_like(k)
    cv2.drawContours(k, [max(cnt, key=cv2.contourArea)], -1, 255, cv2.FILLED)
    lleno = np.zeros(im.shape[:2], np.uint8)
    lleno[y0:y1, x0:x1] = k
    return lleno


def main():
    im = cv2.imread(str(ORIGEN))
    if im is None:
        sys.exit(f"no pude abrir {ORIGEN}")
    H, W = im.shape[:2]
    capa = im.astype(np.float32)

    m = mate(im)
    ys, xs = np.nonzero(m)
    #: ⛔ El ancla en x tampoco sale de la fila de la base: ahí el papel se va
    #: en una punta a la derecha y daba x=1139, 435 px corrido. Va el centro de
    #: la HUELLA completa.
    cx, by = ancla(m)
    print(f"sándwich+papel ... x {xs.min()}..{xs.max()} · y {ys.min()}..{ys.max()}"
          f" · apoyo en x={cx}, y={by}")

    alfa = parche_con_suelo(m, abajo=70, lado=20)
    M = np.float32([[ESCALA, 0, cx * (1 - ESCALA)], [0, ESCALA, by * (1 - ESCALA)]])
    cap = cv2.warpAffine(capa, M, (W, H), flags=cv2.INTER_LANCZOS4,
                         borderMode=cv2.BORDER_REPLICATE)
    alf = cv2.warpAffine(alfa, M, (W, H), flags=cv2.INTER_LINEAR,
                         borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    ys2, xs2 = np.nonzero(alf > 0.5)
    resto = int(((m > 127) & (alf < 0.5)).sum())
    print(f"× {ESCALA} .......... x {xs2.min()}..{xs2.max()} · y {ys2.min()}..{ys2.max()}"
          f"  (del viejo asoma {resto} px · al vaso le quedan {1400 - xs2.max()} px)")

    a = alf[..., None]
    out = np.clip(capa * (1 - a) + cap * a, 0, 255).astype(np.uint8)
    cv2.imwrite(str(DESTINO), out, [cv2.IMWRITE_JPEG_QUALITY, 95])
    print(f"-> {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

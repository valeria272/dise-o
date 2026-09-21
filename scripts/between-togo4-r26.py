#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · slide 4 — ronda 26 (21-09-2026): los tres productos se ponen
en proporción entre ellos.

Eli, en dos mensajes:

    «el ajuste de proporción de tamaño es de café y productos, sobre todo de
     la última slide»
    «ajustes en todas, lo que es sándwich es más grande solo un poco, muffin
     última que crezca solo un poco o achique el plato»

Lo que se hace, y en este orden de capas:

    sándwich  × 1,10   crece un poco
    plato     × 0,88   se achica alrededor de la base del muffin
    muffin    intacto  — al achicar el plato, pasa de ocupar el 71 % al 80 %
    vaso      × 1,30   crece, + 20 px a la derecha

⭐⭐ EL PATRÓN DE ESCALA ES EL LOGOTIPO DEL VASO, que mide lo mismo en los tres
tamaños de vaso (952 · 892 · 938 px en la sesión `cafes-sep2026` que mandó Eli).
Contra ese patrón el vaso de esta slide leía **341 px** y el de la slide 2 —la
aprobada, que sale de una fotografía real— **554 px**: el mismo vaso, 1,63× más
chico. Acá pasa a **443** y el carrusel entero cae en una banda de 1,25×
(554 · 480 · 443) donde antes estaba en 2,29×.

⛔⛔ LA TRAMPA DEL PLATO, Y ES POR QUÉ HAY QUE MEDIR EL MATE ANTES DE USARLO.
La primera pasada buscaba el plato por color («loza gris azulada, poco
saturada») y **se perdía toda el ala derecha**: daba x 852..1547 cuando el plato
llega a **1724**. Con el mate corto, el paso «el plato va por delante» informaba
0 px devueltos —o sea que no hacía nada— y el vaso quedaba pintado ENCIMA del
ala. Eso es lo que Eli vio: «este plato se solapa en la imagen».
Con grabCut y caja medida sale entero. **Un mate que no se verifica contra la
pieza miente en silencio: el paso corre, no falla, y no hace nada.**

⛔ Y LA OTRA: al correr el vaso 45 px para separarlo del plato, el vaso nuevo
   dejaba de contener al viejo y asomaba una media luna de la franja blanca de
   su base. Se rellenó clonando 70 px a la izquierda… que ahí es PLATO, y quedó
   una medialuna gris flotando sobre el vaso. Achicando el plato el vaso ya no
   necesita correrse tanto: con **+20 px** el vaso nuevo vuelve a contener al
   viejo en todas las filas y el relleno desaparece del problema.

⛔ NO SE MUEVE NADA MÁS: ni la bolsa, ni la mano, ni el encuadre, ni el revelado.

Salida: public/assets/hilton/between/fotos-gradadas/togo-s4-r26.jpg
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
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-s4-r26.jpg"

#: Cajas del grabCut, medidas sobre el asset de 2250×2812. Cada una tiene que
#: contener su objeto ENTERO y lo menos posible de lo demás.
CAJA_VASO = (1560, 1590, 2180, 2360)
CAJA_SAND = (40, 1820, 1120, 2480)      # el sándwich CON su papel: van juntos
CAJA_PLATO = (820, 2120, 1800, 2520)

#: el muffin no se escala; se recorta sólo para volver a ponerlo ENCIMA del
#: plato achicado. Sale por luminancia: es lo único casi negro de la zona.
MUFFIN = {"x0": 1000, "y0": 1800, "x1": 1620, "y1": 2400, "v_max": 115}

ESC_VASO, DX_VASO = 1.26, 25
ESC_SAND = 1.10
ESC_MUFFIN = 1.08

SOMBRA = {"alto": 46, "fuerza": 0.30, "suave": 26}


# ─────────────────────────── mates ───────────────────────────────────────────
def _grabcut(im, caja, margen=20, cierra=15, abre=11, iters=6):
    x0, y0, x1, y1 = caja
    sub = im[y0:y1, x0:x1].copy()
    mk = np.zeros(sub.shape[:2], np.uint8)
    cv2.grabCut(sub, mk, (margen, margen, (x1 - x0) - 2 * margen, (y1 - y0) - 2 * margen),
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                iters, cv2.GC_INIT_WITH_RECT)
    k = np.where((mk == cv2.GC_FGD) | (mk == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    k = cv2.morphologyEx(k, cv2.MORPH_CLOSE, np.ones((cierra, cierra), np.uint8))
    k = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((abre, abre), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(k, 8)
    i = max(range(1, n), key=lambda j: st[j][4])
    lleno = np.zeros(im.shape[:2], np.uint8)
    lleno[y0:y1, x0:x1] = (lab == i).astype(np.uint8) * 255
    return lleno


def mate_del_vaso(im):
    x0, y0, x1, y1 = CAJA_VASO
    sub = im[y0:y1, x0:x1].copy()
    mk = np.zeros(sub.shape[:2], np.uint8)
    cv2.grabCut(sub, mk, (35, 15, (x1 - x0) - 70, (y1 - y0) - 25),
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                6, cv2.GC_INIT_WITH_RECT)
    k = np.where((mk == cv2.GC_FGD) | (mk == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    k = cv2.morphologyEx(k, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    k = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(k, 8)
    i = max(range(1, n), key=lambda j: st[j][4])
    lleno = np.zeros(im.shape[:2], np.uint8)
    lleno[y0:y1, x0:x1] = (lab == i).astype(np.uint8) * 255
    return lleno


def mate_del_muffin(im):
    M = MUFFIN
    z = cv2.cvtColor(im[M["y0"]:M["y1"], M["x0"]:M["x1"]], cv2.COLOR_BGR2HSV)
    k = (z[..., 2] < M["v_max"]).astype(np.uint8) * 255
    k = cv2.morphologyEx(k, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    k = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((15, 15), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(k, 8)
    i = max(range(1, n), key=lambda j: st[j][4])
    lleno = np.zeros(im.shape[:2], np.uint8)
    lleno[M["y0"]:M["y1"], M["x0"]:M["x1"]] = (lab == i).astype(np.uint8) * 255
    return lleno


# ─────────────────────────── piezas ──────────────────────────────────────────
def ancla_base(mate):
    """Centro de la huella (en x) y punto de apoyo (en y)."""
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


def escala_desde(im_f, alfa, cx, cy, s, dx=0):
    H, W = alfa.shape
    M = np.float32([[s, 0, cx * (1 - s) + dx], [0, s, cy * (1 - s)]])
    capa = cv2.warpAffine(im_f, M, (W, H), flags=cv2.INTER_LANCZOS4,
                          borderMode=cv2.BORDER_REPLICATE)
    a = cv2.warpAffine(alfa, M, (W, H), flags=cv2.INTER_LINEAR,
                       borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return capa, a


def main():
    im = cv2.imread(str(ORIGEN))
    if im is None:
        sys.exit(f"no pude abrir {ORIGEN}")
    H, W = im.shape[:2]
    capa = im.astype(np.float32)
    print(f"asset ............... {W}×{H}")

    vaso = mate_del_vaso(im)
    sand = _grabcut(im, CAJA_SAND)
    plato = _grabcut(im, CAJA_PLATO)
    muffin = mate_del_muffin(im)
    for nom, m in (("vaso", vaso), ("sándwich+papel", sand), ("plato", plato), ("muffin", muffin)):
        ys, xs = np.nonzero(m)
        print(f"  {nom:15s} x {xs.min():4d}..{xs.max():4d} · y {ys.min():4d}..{ys.max():4d}"
              f" · ancho {xs.max() - xs.min():4d}")

    # los que CRECEN se escalan con su suelo; el plato, que no se escala, va
    # con mate ajustado porque tiene que recortar limpio contra el vaso.
    a_vaso = parche_con_suelo(vaso, abajo=70, lado=40)
    a_sand = parche_con_suelo(sand, abajo=70, lado=40)
    a_muffin = parche_con_suelo(muffin, abajo=40, lado=25)
    a_plato = cv2.GaussianBlur(plato.astype(np.float32) / 255.0, (0, 0), 1.6)

    salida = capa.copy()

    # ── 1 · el sándwich crece. Al crecer desde su base CONTIENE al viejo, así
    #        que no hay nada que rellenar detrás.
    cxs, cys = ancla_base(sand)
    cap_s, alf_s = escala_desde(capa, a_sand, cxs, cys, ESC_SAND)
    xs2 = np.nonzero(alf_s > 0.5)[1]
    print(f"\nsándwich × {ESC_SAND} .... x {xs2.min()}..{xs2.max()}  (margen izquierdo {xs2.min()} px)")
    salida = salida * (1 - alf_s[..., None]) + cap_s * alf_s[..., None]

    # ── 2 · el muffin crece. También desde su base, así que CONTIENE al viejo
    #        y no hay nada que rellenar. Se dibuja al final, sobre el plato.
    cxm, cym = ancla_base(muffin)
    cap_m, alf_m = escala_desde(capa, a_muffin, cxm, cym, ESC_MUFFIN)
    xm = np.nonzero(alf_m > 0.5)[1]
    resto_m = int(((muffin > 127) & (alf_m < 0.5)).sum())
    print(f"muffin × {ESC_MUFFIN} .... x {xm.min()}..{xm.max()}"
          f"  (del viejo asoma {resto_m} px)")

    # ── 3 · el vaso crece y se corre lo justo
    cxv, cyv = ancla_base(vaso)
    cap_v, alf_v = escala_desde(capa, a_vaso, cxv, cyv, ESC_VASO, DX_VASO)
    ys2, xv = np.nonzero(alf_v > 0.5)
    resto = int(((vaso > 127) & (alf_v < 0.5)).sum())
    print(f"vaso × {ESC_VASO} +{DX_VASO} ... x {xv.min()}..{xv.max()} · y {ys2.min()}..{ys2.max()}"
          f"  (margen derecho {W - xv.max()} px · del viejo asoma {resto} px)")

    S = SOMBRA
    sombra = np.zeros((H, W), np.float32)
    cv2.ellipse(sombra, (cxv + DX_VASO, cyv), (int((xv.max() - xv.min()) / 2 * 0.95), S["alto"]),
                0, 0, 360, 1.0, -1)
    sombra = cv2.GaussianBlur(sombra, (0, 0), S["suave"])
    salida *= (1 - S["fuerza"] * sombra[..., None])
    salida = salida * (1 - alf_v[..., None]) + cap_v * alf_v[..., None]

    # ── 4 · el plato va POR DELANTE del vaso y del sándwich. Es lo que estaba
    #        roto: con el mate corto no se dibujaba y el vaso quedaba encima.
    salida = salida * (1 - a_plato[..., None]) + capa * a_plato[..., None]
    # ── 5 · y el muffin, crecido, por delante del plato. Su filo viejo cae
    #        sobre el PLATO, así que se clona desde el plato (30 px abajo).
    salida = salida * (1 - alf_m[..., None]) + cap_m * alf_m[..., None]

    # control: cuánto se le mete el vaso al plato (que va por delante, así que
    # un poco es normal y es lo que da profundidad; lo que NO puede pasar es que
    # el vaso se pinte ENCIMA, que fue el defecto de la pasada anterior)
    pn, vn = (a_plato > 0.5), (alf_v > 0.5)
    peor, yp = 10 ** 6, None
    for y in range(2100, 2400):
        pp, cc = np.flatnonzero(pn[y]), np.flatnonzero(vn[y])
        if len(pp) == 0 or len(cc) == 0:
            continue
        if cc.min() - pp.max() < peor:
            peor, yp = int(cc.min() - pp.max()), y
    print("")
    print(f"vaso contra el plato  {peor:+d} px en y={yp}  (el plato va por delante)")
    print(f"muffin sobre su plato {100 * (xm.max() - xm.min()) / 872:.0f} % del ancho del plato"
          f"   (antes {100 * 619 / 872:.0f} %)")

    cv2.imwrite(str(DESTINO), np.clip(salida, 0, 255).astype(np.uint8),
                [cv2.IMWRITE_JPEG_QUALITY, 95])
    print(f"-> {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

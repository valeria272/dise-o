#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · ST 28-09 — acabado de la escena generada
==================================================

Lo que hay que arreglar DESPUÉS del generador, según
`clients/hilton/PROMPTS-DE-ELI.md` § «dos cosas que hay que arreglar SIEMPRE»:

  **El color de marca no llega exacto.** Se pidió una pared `#675B49` y llegó
  `#7B685B`: más roja y más clara. Se corrige con una **ganancia multiplicativa
  por canal** —multiplicar conserva el degradado de la pared y su luz; sumar un
  offset la aplana y se ve de cartulina— y la ganancia se calcula sobre el
  **medio tono**, no sobre el promedio: el promedio arrastra la sombra del
  rincón y llevar ESO al café de marca revienta los medios.

La máscara es la pared, o sea todo menos la persona y el vaso. Se saca con
grabCut a media resolución, que sobre un fondo liso es trivial, y se afloja en
los bordes para que no quede un halo alrededor del sujeto.

Uso:
    python scripts/between-st-s5-togo-acabado.py
    python scripts/between-st-s5-togo-acabado.py --entrada <png> --fuerza 0.8
"""
from __future__ import annotations

import argparse
import os
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

ENTRADA = RAIZ / "raw/hilton/between/s5/gen-r29/st-28-09-togo-gen-pared.png"
SALIDA = RAIZ / "raw/hilton/between/s5/st-28-09-togo-r29.jpg"
ASSET = RAIZ / "public/assets/hilton/between/s5/st-28-09-togo.jpg"

CAFE = np.array([0x49, 0x5B, 0x67], np.float32)     # #675B49 en BGR
# Rectángulo de MEDIO TONO de la pared: ni el lado iluminado ni el rincón.
MEDIO_TONO = (200, 1200, 1100, 2400)                # x0, y0, x1, y1


def mascara_pared(im: np.ndarray) -> np.ndarray:
    """1 en la pared, 0 en la persona y el vaso."""
    h, w = im.shape[:2]
    ch, cw = h // 4, w // 4
    ch_im = cv2.resize(im, (cw, ch), interpolation=cv2.INTER_AREA)
    m = np.full((ch, cw), cv2.GC_PR_BGD, np.uint8)
    # el sujeto vive en la columna central; la pared, en las dos franjas
    m[:, int(cw * 0.18):int(cw * 0.82)] = cv2.GC_PR_FGD
    m[int(ch * 0.30):int(ch * 0.62), int(cw * 0.30):int(cw * 0.70)] = cv2.GC_FGD
    m[:, :int(cw * 0.08)] = cv2.GC_BGD
    m[:, int(cw * 0.92):] = cv2.GC_BGD
    m[:int(ch * 0.12), :] = cv2.GC_BGD
    cv2.grabCut(ch_im, m, None, np.zeros((1, 65), np.float64),
                np.zeros((1, 65), np.float64), 4, cv2.GC_INIT_WITH_MASK)
    suj = np.where((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    suj = cv2.morphologyEx(suj, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(suj, 8)
    if n > 1:
        suj = np.where(lab == 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])), 255, 0).astype(np.uint8)
    suj = cv2.resize(suj, (w, h), interpolation=cv2.INTER_LINEAR)
    pared = 255 - cv2.dilate(suj, np.ones((25, 25), np.uint8))
    return cv2.GaussianBlur(pared.astype(np.float32), (0, 0), 18) / 255.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default=str(ENTRADA))
    ap.add_argument("--fuerza", type=float, default=1.0,
                    help="0 = deja el color del generador · 1 = lo lleva entero al de marca")
    ap.add_argument("--salida", default=str(SALIDA))
    ap.add_argument("--degradado", type=float, default=0.0, metavar="K",
                    help="oscurece el tercio de arriba a K (0 = no toca). Sobre el verde "
                         "del Winter Garden el beige da 3,1:1 y la marca trabaja mas "
                         "arriba; con 0,72 sube a ~5:1 sin apagar la escena.")
    ap.add_argument("--hasta", type=int, default=2400,
                    help="fila donde el degradado ya vale 1")
    ap.add_argument("--sin-filo", action="store_true",
                    help="borra el filo blanco que el generador le pone a la base del "
                         "vaso. Es el detalle del vaso CHICO —el grande es kraft hasta "
                         "abajo— y el manual lo tiene marcado como error desde la ronda 2. "
                         "Mide 10-15 filas: se tapa bajando el propio carton.")
    ap.add_argument("--bajar", type=int, default=0, metavar="PX",
                    help="baja la escena dentro del cuadro y rellena arriba con la propia "
                         "pared. Sirve cuando el generador deja el vaso muy alto y el "
                         "titular le pisa la tapa. La pared es plana, asi que continuarla "
                         "es invisible — nada que ver con reconstruir una fachada.")
    ap.add_argument("--filo-alto", type=int, default=22,
                    help="filas que se bajan sobre el arco de la base")
    ap.add_argument("--cafe-hasta", type=int, default=0, metavar="Y",
                    help="lleva al cafe de marca el muro que hay SOBRE las plantas, "
                         "hasta esta fila")
    ap.add_argument("--cafe-fundido", type=int, default=300,
                    help="px en los que se apaga esa correccion")
    ap.add_argument("--verde-a-cafe", action="store_true",
                    help="repinta la banda LISA de arriba con el cafe de marca. Eli, "
                         "ronda 31: «no tenemos ese color en Between, debe ser el cafe "
                         "de bw». El follaje del Winter Garden se deja verde —son plantas "
                         "de verdad— y solo cambia la superficie plana de arriba.")
    a = ap.parse_args()

    im = cv2.imread(a.entrada)
    if im is None:
        sys.exit(f"ABORTA: no se pudo leer {a.entrada}")
    im = im.astype(np.float32)

    if a.bajar > 0:
        n = a.bajar
        # la franja de arriba se estira: son filas de pared lisa, y se toma su
        # propio degradado para que no aparezca un escalon de tono
        banda = im[:120]
        top = cv2.resize(banda, (im.shape[1], n + 120), interpolation=cv2.INTER_LINEAR)[:n]
        im = np.concatenate([top, im], 0)[: im.shape[0]]
        print(f"escena bajada {n} px; arriba se continuo la pared")

    x0, y0, x1, y1 = MEDIO_TONO
    medio = np.percentile(im[y0:y1, x0:x1].reshape(-1, 3), 50, axis=0)
    g = np.clip(CAFE / np.maximum(medio, 1.0), 0.5, 1.6)
    g = 1 + (g - 1) * a.fuerza
    print(f"pared medida #{int(medio[2]):02X}{int(medio[1]):02X}{int(medio[0]):02X}"
          f"  ->  objetivo #675B49   ganancia B {g[0]:.3f} G {g[1]:.3f} R {g[2]:.3f}")

    if a.fuerza > 0:
        m = mascara_pared(np.clip(im, 0, 255).astype(np.uint8))[..., None]
        im = im * (1 + (g[None, None, :] - 1) * m)
    out = np.clip(im, 0, 255).astype(np.uint8)

    if a.sin_filo:
        # ⛔ Primer intento: columna por columna, bajando el cartón n filas según
        #    lo que midiera cada una. Salió un peinado de rayas verticales,
        #    porque el borde detectado salta de columna a columna y la mano lo
        #    interrumpe. ⭐ Lo que sirve: AJUSTAR la curva de la base —que es un
        #    arco suave— y bajar el cartón esa misma cantidad en todas.
        w = out.astype(np.float32)
        B, G, R = w[..., 0], w[..., 1], w[..., 2]
        kraft = ((R - B > 55) & (R > 110)).astype(np.uint8)
        kraft = cv2.morphologyEx(kraft, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
        hh, ww = out.shape[:2]
        borde = np.full(ww, -1.0, np.float32)
        for x in range(ww):
            c = np.nonzero(kraft[:, x])[0]
            if len(c) > 200:
                borde[x] = c.max()
        val = borde > 0
        if val.sum() > 50:
            xs = np.arange(ww)
            # la base es un arco: una parábola lo describe y mata los saltos
            co = np.polyfit(xs[val], borde[val], 2)
            arco = np.polyval(co, xs)
            dentro = (xs >= xs[val].min() + 6) & (xs <= xs[val].max() - 6)
            ALTO, SUBE = a.filo_alto, 10
            for x in np.nonzero(dentro)[0]:
                y = int(round(arco[x]))
                if y - SUBE < 0 or y + ALTO >= hh:
                    continue
                fuente = w[y - SUBE, x]
                for d in range(ALTO):
                    p_ = 1.0 if d < ALTO - 5 else (ALTO - d) / 5.0
                    w[y + d, x] = w[y + d, x] * (1 - p_) + fuente * p_
            out = np.clip(w, 0, 255).astype(np.uint8)
            print(f"filo blanco tapado sobre el arco de la base "
                  f"({int(dentro.sum())} columnas, {ALTO} filas)")

    if a.cafe_hasta > 0:
        # El muro que el generador pone SOBRE las plantas llega caliente
        # (#7E6C58) y la marca es #675B49. Es el mismo caso del sweater del
        # 14-09: ganancia multiplicativa por canal sobre el medio tono, que
        # conserva la luz del muro. Se aplica sólo hasta donde empieza el
        # follaje y se apaga en `--cafe-fundido` px, así las hojas no se tocan.
        base = out.astype(np.float32)
        med = np.percentile(base[80:int(a.cafe_hasta * 0.7)].reshape(-1, 3), 50, axis=0)
        gg = np.clip(CAFE / np.maximum(med, 1.0), 0.5, 1.6)
        ys = np.arange(base.shape[0], dtype=np.float32)
        wv = np.clip((a.cafe_hasta - ys) / max(a.cafe_fundido, 1), 0, 1)[:, None, None]
        out = np.clip(base * (1 + (gg[None, None, :] - 1) * wv), 0, 255).astype(np.uint8)
        q = np.percentile(out[80:int(a.cafe_hasta * 0.7)].reshape(-1, 3), 50, axis=0)
        print(f"muro de arriba #{int(med[2]):02X}{int(med[1]):02X}{int(med[0]):02X}"
              f"  ->  #{int(q[2]):02X}{int(q[1]):02X}{int(q[0]):02X}")

    if a.degradado > 0:
        h = out.shape[0]
        y = np.arange(h, dtype=np.float32)
        s = np.clip((y - a.hasta * 0.45) / (a.hasta * 0.55), 0, 1)
        k = a.degradado + (1 - a.degradado) * (s * s * (3 - 2 * s))
        out = np.clip(out.astype(np.float32) * k[:, None, None], 0, 255).astype(np.uint8)
        print(f"degradado del titular: {a.degradado:.2f} arriba -> 1,00 en y={a.hasta}")

    cv2.imwrite(a.salida, out, [cv2.IMWRITE_JPEG_QUALITY, 96])
    ASSET.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(ASSET), out, [cv2.IMWRITE_JPEG_QUALITY, 96])
    p = np.percentile(out[y0:y1, x0:x1].reshape(-1, 3), 50, axis=0)
    print(f"quedó #{int(p[2]):02X}{int(p[1]):02X}{int(p[0]):02X}")
    print(f"pieza  {a.salida}\nasset  {ASSET}")


if __name__ == "__main__":
    main()

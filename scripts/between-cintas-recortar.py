#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta las CINTAS DORADAS fotográficas de su generación sobre blanco.

⭐ RONDA 17 (07-09-2026) — Eli, sobre el cumpleaños:

    «el problema es la serpentina que se ve fea, se ve como si fuera dibujada a
     mano. No se ve realista, y se ve de un color dorado opaco. Tiene que verse
     mejor realizado, con un dorado brillante»

⛔⛔ LA CAUSA, Y ES UNA CORRECCIÓN QUE SE PASÓ DE LARGO

El adorno que había es el VECTOR de Eli (`recursos/confeti-oro/`), o sea una
ilustración — y por eso «se ve dibujada a mano»: lo es. Pero lo de «dorado
opaco» tiene una causa aparte y peor, y está en el propio historial:

    ronda 15 · Eli: «lo dorado se ve QUEMADO»
    → se bajó `ASIENTO` de 0,88 a 0,80 y se metió `hombro()`

Esa corrección apagó los brillos: medido sobre la entrega, el oro quedó con
**0,0 % de píxeles especulares** (L>200), contra **3,4 %** en la pieza que Eli
tiene aprobada. Un metal sin especular no es metal — es pintura mate. O sea que
arreglar «quemado» bajando todo produjo «opaco»: el problema nunca fue el brillo
máximo, fue que el vector no tiene RANGO.

    material              L p5-p95     especular (L>200)
    vector, como iba       77-180           0,0 %
    la pieza de Eli        89-197           3,4 %
    cinta fotográfica     47-219          11,8 %   ← generada acá

⭐ LA SALIDA: material FOTOGRÁFICO con rango propio. Cinta metálica que **gira**
sobre su eje, así que alterna sola entre especular casi blanco en las caras que
toman la luz y bronce oscuro en la sombra del giro. Ese contraste interno es lo
que la lee como metal, y no se puede pintar: hay que fotografiarlo.

Se generó con Nano Banana Pro sobre BLANCO —para poder recortarla limpia— y con
la pieza aprobada de Eli como referencia de estilo.

⚠️ Cómo se saca el alfa, y por qué no sirve lo obvio: un umbral de luminancia
recorta la cinta pero **se come sus propios brillos**, que son casi blancos como
el fondo. Así que la máscara es «saturado O no-tan-claro», se queda con las
componentes grandes (una por cinta), se le rellenan los huecos y se le suaviza
el canto. Los brillos quedan dentro porque están rodeados de cinta.

Salida: public/assets/hilton/between/recursos/cintas-oro/cinta-oro-NN.png
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

GEN = RAIZ / "public/assets/hilton/between/ia-sept/cumple-cintas-oro-r17.png"
DESTINO = RAIZ / "public/assets/hilton/between/recursos/cintas-oro"
MIN_AREA = 40_000          # una cinta de verdad; por debajo es mota o sombra


def main():
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN}")
    im = Image.open(GEN).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    print(f"generación {im.size}")

    mx, mn = a.max(axis=2), a.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1.0), 0.0)
    L = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114

    # «es cinta» = saturado (el oro) O no tan claro (el canto y la sombra del
    # giro). Los brillos casi blancos entran porque quedan rodeados y los rellena
    # el paso de huecos.
    bruto = ((sat > 0.14) | (L < 232)).astype(np.uint8)
    bruto = cv2.morphologyEx(bruto, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))

    n, et, est, _ = cv2.connectedComponentsWithStats(bruto, 8)
    piezas = sorted(
        [(est[i, 4], i) for i in range(1, n) if est[i, 4] >= MIN_AREA],
        reverse=True)
    print(f"componentes ≥ {MIN_AREA:,} px: {len(piezas)}")

    DESTINO.mkdir(parents=True, exist_ok=True)
    for k, (area, i) in enumerate(piezas, start=1):
        m = (et == i).astype(np.uint8)
        # rellenar huecos interiores (los brillos que el umbral dejó fuera)
        relleno = m.copy()
        h, w = m.shape
        mascara = np.zeros((h + 2, w + 2), np.uint8)
        cv2.floodFill(relleno, mascara, (0, 0), 1)
        huecos = (relleno == 0).astype(np.uint8)
        m = ((m | huecos) > 0).astype(np.uint8)

        x, y, ww, hh = cv2.boundingRect(m)
        pad = 12
        x0, y0 = max(0, x - pad), max(0, y - pad)
        x1, y1 = min(w, x + ww + pad), min(h, y + hh + pad)

        alfa = (m[y0:y1, x0:x1] * 255).astype(np.uint8)
        alfa = np.asarray(Image.fromarray(alfa).filter(
            ImageFilter.GaussianBlur(1.4)))
        rgb = a[y0:y1, x0:x1]

        z = rgb[alfa > 200]
        Lz = z[..., 0] * 0.299 + z[..., 1] * 0.587 + z[..., 2] * 0.114
        fig = Image.merge("RGBA", (
            *Image.fromarray(rgb.astype(np.uint8)).split(),
            Image.fromarray(alfa)))
        p = DESTINO / f"cinta-oro-{k:02d}.png"
        fig.save(p)
        print(f"  {p.name}  {fig.size}  área {area:,} px  ·  "
              f"L p5-p95 {np.percentile(Lz, 5):.0f}-{np.percentile(Lz, 95):.0f}  ·  "
              f"especular {100 * (Lz > 200).mean():.1f} %")
    print(f"\n-> {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

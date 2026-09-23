#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta una a una las serpentinas del vector de confeti dorado.

⭐ RONDA 14 (05-09-2026) — Eli: «debes quitar esos "plátanos dorados" del
   carrusel de cumpleaños, puedes añadir alguna de [este vector] sutiles en el
   slide 1 y 2. Hazlo realista.»

Van TRES intentos de adorno de cumpleaños en esta pieza:

| ronda | qué era | veredicto |
|---|---|---|
| 11 | papelitos de 5 colores planos | «se ve muy infantil y mal diseñado» |
| 12 | cintas de oro dibujadas píxel a píxel | «parece un plátano» |
| 13 | los trazos de pincel de Eli (doodle) | ✅ la slide 1 se aprobó |
| 14 | **serpentinas de un vector real** | ← esto |

Y el aprendizaje de la 12 sigue en pie: un adorno que quiere ser fotografía se
mide contra la fotografía que lo rodea. La diferencia ahora es el MATERIAL: no
es una forma que yo dibujo con `ImageDraw`, es una ilustración vectorial de
4.998×3.540 con degradados de cinta metálica, vuelta y veta especular reales —
la que eligió Eli. Eso sí aguanta la comparación; mi cinta de 40 px no.

El vector viene de la API que ya pagamos (Freepik/Magnific, recurso
**177837523** «golden confetti for decorations vector illustration», de xvector,
gratuito dentro del plan). Se baja con `/v1/resources/177837523/download`.

Qué hace este script
--------------------
1. Alfa por diferencia contra el gris de fondo del vector (no por umbral de
   luminancia: hay cintas oscuras que un umbral se come).
2. Componentes conexas → una pieza por serpentina.
3. Descarta las de menos de `MIN_PX` (motas sueltas que no aportan) y guarda
   cada una recortada a su tinta, con su alfa.
4. Ordena por tamaño y las nombra `confeti-oro-NN.png`, para poder elegirlas
   por número en el sembrador.

Salida: public/assets/hilton/between/recursos/confeti-oro/
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "public/assets/hilton/between/recursos/confeti-oro"
#: mínimo de píxeles de tinta para que una pieza valga la pena
MIN_PX = 4000


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: between-confeti-recortar.py <vector.jpg>")
    origen = Path(sys.argv[1])
    im = Image.open(origen).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    print(f"vector {im.width}x{im.height}")

    #: el fondo del vector es un gris parejo; se muestrea en las cuatro esquinas
    esquinas = np.array([a[5, 5], a[5, -5], a[-5, 5], a[-5, -5]])
    fondo = esquinas.mean(axis=0)
    print(f"gris de fondo: {fondo.round(1)}")

    dif = np.abs(a - fondo).sum(axis=2)
    tinta = (dif > 26).astype(np.uint8)
    tinta = cv2.morphologyEx(tinta, cv2.MORPH_CLOSE,
                             cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    n, etiq, stats, _ = cv2.connectedComponentsWithStats(tinta, connectivity=8)
    print(f"componentes: {n - 1}")

    piezas = []
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        if area < MIN_PX:
            continue
        piezas.append((area, i, x, y, w, h))
    piezas.sort(reverse=True)
    print(f"piezas con más de {MIN_PX:,} px de tinta: {len(piezas)}")

    DESTINO.mkdir(parents=True, exist_ok=True)
    for k, (area, i, x, y, w, h) in enumerate(piezas, 1):
        m = (etiq[y:y + h, x:x + w] == i).astype(np.uint8) * 255
        #: el alfa se suaviza 0,8 px: el vector viene rasterizado y el canto
        #: duro delata el recorte cuando la pieza se pega sobre una fotografía.
        m = cv2.GaussianBlur(m, (0, 0), 0.8)
        rgba = np.dstack([np.asarray(im)[y:y + h, x:x + w], m])
        Image.fromarray(rgba).save(DESTINO / f"confeti-oro-{k:02d}.png")
        print(f"  {k:02d}: {w}x{h}  tinta {area:,} px  ratio {w / h:.2f}")
    print(f"\n-> {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

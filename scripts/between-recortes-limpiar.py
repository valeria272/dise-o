#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le quita a los recortes de producto el trozo de MESA que arrastró el grabCut.

⭐ RONDA 14 (05-09-2026). Eli, sobre la ST de Emergencia: «vuelve a hacer lo de
   TOGO, MUFFIN CHOCOLATE + CROISANT QUESO JAMÓN, **para que se vea apetitoso en
   caso de romper**».

⛔⛔ Y revisando la vitrina al 300 % apareció un defecto que ninguna ronda había
   mirado: **`vaso-248.png` no es el vaso. Es el vaso MÁS un trozo de la mesa de
   madera** en la que estaba apoyado. El grabCut de `between-recortes-reales.py`
   se llevó la superficie de apoyo junto con el objeto, y esa media luna de
   madera —de 1.670 a 1.830 en el recorte, unos 160 px— venía pegándose debajo
   del vaso desde la ronda 13.

   En la pieza se leía como una base rota y sucia: un vaso dentro de una vitrina
   de vidrio, apoyado sobre un pedazo de OTRA mesa. Es el mismo delator que el
   manual ya tiene escrito para los montajes, sólo que metido dentro del propio
   recorte, que es donde no se estaba mirando.

   ⚠️ La lección: un recorte se revisa por su CANTO INFERIOR, con zoom, antes de
      montarlo. La zona de apoyo es justo donde el segmentador se confunde,
      porque el objeto y su sombra comparten borde.

Cómo se limpia, sin tocar el producto:

  1. se marca como **madera** todo píxel cálido y oscuro (R − B > `CALIDEZ` y
     luminancia < `LUZ_MAX`) dentro de la banda inferior del recorte;
  2. se le resta al alfa;
  3. y se conserva **la componente conexa más grande** de lo que queda, que es
     el producto: así no sobreviven islas sueltas de mesa lejos del objeto;
  4. el alfa se suaviza 1 px para que el canto no quede dentado.

Uso:
    python scripts/between-recortes-limpiar.py vaso-248.png
    python scripts/between-recortes-limpiar.py            # revisa los tres
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
RECORTES = RAIZ / "public/assets/hilton/between/recortes"

#: qué se considera madera de la mesa, y desde qué fracción del alto se busca.
#: Sólo se mira la banda de abajo: arriba está el producto y el croissant TAMBIÉN
#: es cálido y dorado — aplicar esto a toda la imagen se comería el hojaldre.
CALIDEZ, LUZ_MAX, DESDE = 22.0, 178.0, 0.86


def limpia(nombre, calidez=CALIDEZ, luz_max=LUZ_MAX, desde=DESDE):
    origen = RECORTES / nombre
    im = Image.open(origen).convert("RGBA")
    a = np.asarray(im).astype(np.float32)
    alfa = (a[..., 3] > 128).astype(np.uint8)
    antes = int(alfa.sum())

    y0 = int(im.height * desde)
    banda = np.zeros_like(alfa)
    banda[y0:] = 1
    lum = 0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]
    madera = ((a[..., 0] - a[..., 2]) > calidez) & (lum < luz_max) & (banda > 0) & (alfa > 0)
    alfa[madera] = 0

    n, etiq, stats, _ = cv2.connectedComponentsWithStats(alfa, connectivity=8)
    if n > 1:
        mayor = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        alfa = (etiq == mayor).astype(np.uint8)
    islas = n - 2

    m = cv2.GaussianBlur(alfa * 255.0, (0, 0), 1.0)
    salida = np.dstack([a[..., :3], m])
    destino = RECORTES / origen.name.replace(".png", "-limpio.png")
    Image.fromarray(np.clip(salida, 0, 255).astype(np.uint8), "RGBA").save(destino)

    ys = np.where(alfa.any(axis=1))[0]
    print(f"{nombre}: {antes:,} -> {int(alfa.sum()):,} px de alfa "
          f"(−{100 * (1 - alfa.sum() / max(antes, 1)):.1f} %) · "
          f"islas descartadas: {max(0, islas)} · "
          f"canto inferior {ys.max() if len(ys) else -1} (era {im.height - 1})")
    print(f"   -> {destino.name}")


if __name__ == "__main__":
    for n in (sys.argv[1:] or ["vaso-248.png", "croissant-jamon-queso.png",
                               "muffin-chocolate.png"]):
        limpia(n)

#!/usr/bin/env python3
"""C2 · fotos del showroom de Vitacura, listas para montar.

Reglas del brief (hoja «C2 · Post tienda»):
  nº1 fotos REALES del local, sin render ni banco de imágenes.
  nº2 MISMA temperatura de color en las tres — las fotos vienen con luces
      mezcladas y hay que corregirlas antes de montar.
  nº5 revisar qué pisos se ven: si aparece una línea no autorizada, se recorta.

Y la regla de Paulina (25-08-2026): *«editar las imágenes para que detalles como
el letrero de enfrente no se vean. las imágenes deben ser limpias, minimalistas
y comerciales»* → los recortes de acá sacan los autos y el estacionamiento.

Salida: public/assets/casablanca/sep/sr2_<n>_<formato>.jpg
"""
import os
import pathlib
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

RAIZ = pathlib.Path(str(_RAIZ))
SHOW = RAIZ / "raw/casablanca/showroom"
ASSETS = RAIZ / "public/assets/casablanca"
DEST = ASSETS / "sep"

# (archivo, recorte feed x0,y0,x1,y1 en fracción, recorte story)
# Recortes elegidos MIRANDO la foto, no a ojo de porcentaje: el letrero del local
# y el monolito «6359» tienen que entrar ENTEROS, y fuera los autos.
FOTOS = {
    1: ("_JCW9757.jpg", (0.06, 0.235, 0.99, 0.705), (0.055, 0.115, 0.985, 0.90)),
    2: (None,           (0.05, 0.02, 0.95, 0.98),   (0.20, 0.00, 0.80, 1.00)),
    3: ("_JCW9937.jpg", (0.19, 0.335, 0.82, 0.695), (0.19, 0.085, 0.85, 0.715)),
}
REFERENCIA = 1          # la tarjeta cuya luz mandan las otras dos


def recorta(im, caja, w, h):
    W, H = im.size
    x0, y0, x1, y1 = caja
    c = im.crop((int(W * x0), int(H * y0), int(W * x1), int(H * y1)))
    cw, ch = c.size
    e = max(w / cw, h / ch)
    c = c.resize((int(round(cw * e)), int(round(ch * e))), Image.LANCZOS)
    cw, ch = c.size
    return c.crop(((cw - w) // 2, (ch - h) // 2, (cw - w) // 2 + w, (ch - h) // 2 + h))


def iguala_luz(im, objetivo, fuerza=0.45):
    """Lleva la temperatura de color a la de la foto de referencia (brief nº2)."""
    a = np.asarray(im).astype(float)
    m = a.reshape(-1, 3).mean(axis=0)
    f = np.clip(objetivo / np.maximum(m, 1.0), 0.75, 1.35)
    f = 1.0 + (f - 1.0) * fuerza
    return Image.fromarray(np.clip(a * f, 0, 255).astype("uint8"))


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    # el interior venía a 1248×832 (borrado de personas sobre la foto real);
    # se subió a 2496×1664 con el upscaler antes de recortar
    interior = Image.open(ASSETS / "sr_interior_2k.jpg").convert("RGB")
    ref = None
    for fmt, (w, h) in (("feed", (2250, 2250)), ("story", (2250, 4000))):
        for n, (archivo, cf, cs) in FOTOS.items():
            src = interior if archivo is None else Image.open(SHOW / archivo).convert("RGB")
            out = recorta(src, cf if fmt == "feed" else cs, w, h)
            if n == REFERENCIA and fmt == "feed":
                ref = np.asarray(out).reshape(-1, 3).mean(axis=0)
            if n != REFERENCIA and ref is not None:
                out = iguala_luz(out, ref)
            d = DEST / f"sr2_{n}_{fmt}.jpg"
            out.save(d, quality=94)
            print(f"  ✓ {d.name}  {out.size}")


if __name__ == "__main__":
    main()

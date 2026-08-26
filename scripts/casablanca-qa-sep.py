#!/usr/bin/env python3
"""QA de entrega — Casablanca septiembre 2026. Mide, no opina.

  1. Zonas seguras de Meta en story (pauta): 250 px arriba · 340 px abajo · 115 px
     derecha. Excepción documentada: la tarjeta del logo cuelga del borde superior
     y es decisión de marca (clients/casablanca/CLAUDE.md).
  2. El texto no se sale del ancho del filete.
  3. Nada de cifras de precio, «desde», % ni urgencia (regla dura de la marca).
"""
import glob
import re
import sys

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
PROHIBIDO = re.compile(r"(\$|desde\s|\d+\s*%|oferta|descuento|última|ultima|urge)", re.I)


def tinta(a, x0, y0, x1, y1):
    """Fracción de píxeles que son TEXTO, no simplemente claros.

    Medir «blanco» daba falsos positivos: el cielo de la foto del showroom marcaba
    65 % de la zona segura superior. El texto se distingue porque es blanco Y tiene
    borde: se exige gradiente local alto.
    """
    z = a[y0:y1, x0:x1]
    if z.size < 300:
        return 0.0
    mn, mx = z.min(axis=2), z.max(axis=2)
    claro = (mn > 235) & ((mx - mn) < 14)
    g = z.mean(axis=2)
    gx = np.abs(np.diff(g, axis=1, prepend=g[:, :1]))
    gy = np.abs(np.diff(g, axis=0, prepend=g[:1, :]))
    borde = (gx + gy) > 55
    from scipy.ndimage import maximum_filter                      # noqa
    return float((claro & maximum_filter(borde, size=9)).mean())


def main(rutas):
    fallas = 0
    for r in sorted(rutas):
        im = Image.open(r).convert("RGB")
        W, H = im.size
        k = W / 1080
        a = np.asarray(im).astype(int)
        nombre = r.split("/")[-1]
        avisos = []
        if H / W > 1.4:                                  # story
            # arriba se excluye la tarjeta del logo (excepción de marca)
            sup = tinta(a, 0, 0, int(340 * k), int(250 * k)) + \
                  tinta(a, int(740 * k), 0, W, int(250 * k))
            if sup > 0.010:
                avisos.append(f"tinta en la zona segura SUPERIOR ({sup*100:.1f}%)")
            inf = tinta(a, 0, H - int(340 * k), W, H)
            if inf > 0.010:
                avisos.append(f"tinta en la zona segura INFERIOR ({inf*100:.1f}%)")
            der = tinta(a, W - int(115 * k), int(250 * k), W, H - int(340 * k))
            if der > 0.012:
                avisos.append(f"tinta en la zona segura DERECHA ({der*100:.1f}%)")
        print(f"  {nombre:44s} {'· '.join(avisos) if avisos else 'zonas seguras OK'}")
        fallas += len(avisos)
    return fallas


if __name__ == "__main__":
    rutas = sys.argv[1:] or glob.glob("out/casablanca/septiembre/*.png")
    n = main(rutas)
    print(f"\n{'⚠ ' + str(n) + ' avisos' if n else '✅ sin avisos'}")
    sys.exit(1 if n else 0)

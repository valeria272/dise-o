# -*- coding: utf-8 -*-
"""Logo Piazza en alta: se extrae de la cabecera de la ficha oficial PZ20000NE (3508 px).
Es el mismo lockup del link del brief (PIAZZA-NUEVO-small.png, 220 px), pero a ~780 px.
El beige de la ficha se quita desmezclando el color (no es un recorte con halo)."""
from pathlib import Path
import numpy as np
from PIL import Image
RAIZ = Path(__file__).resolve().parents[3]
im = np.array(Image.open(RAIZ / "raw/ebema/piazza-catalogo-a4a5/PZ20000NE.jpg").convert("RGB"))
c = im[60:410, 90:900].astype(float)
bg = np.array([229., 218., 200.])
L = c.mean(2); Lbg = bg.mean()
a_osc = np.clip((Lbg - L) / (Lbg - 15), 0, 1)                   # texto negro
dist = np.abs(c - bg).max(2)
a_col = np.clip((dist - 18) / 50, 0, 1)                          # bandera (verde, blanco, rojo)
sat = c.max(2) - c.min(2)
bandera = (sat > 60) | ((L > 236) & (dist > 12))
a = np.where(bandera, np.maximum(a_col, a_osc), a_osc)
a[a < 0.04] = 0
col = np.where(bandera[..., None], c, np.zeros_like(c) + 20)     # el negro del logo, parejo
rgba = np.dstack([col, a * 255]).astype(np.uint8)
ys, xs = np.where(a > 0.05)
rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
Image.fromarray(rgba).save(Path(__file__).parent / "recortes/logo_piazza.png")
print(rgba.shape)

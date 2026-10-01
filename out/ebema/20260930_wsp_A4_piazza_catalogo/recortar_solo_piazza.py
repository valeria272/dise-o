# -*- coding: utf-8 -*-
"""A4/A5 Piazza catálogo — productos ACTUALIZADOS (cliente, vía Carlos, 01-10-2026).

Carlos cambió el enlace PRODUCTOS del brief por la carpeta «SÓLO PIAZZA»
(Drive `1tmtgvsYbzr_1Y-OJ8QQBDK_0cjGP6Qz7`): 7 packshots de 640x905 sobre blanco.
Tres son los mismos productos que ya estaban (PZ20000NE, PZ6000, PZ6009) y siguen
con su recorte de la ficha en alta. Los otros cuatro son nuevos y se recortan acá.
Los códigos salen de cotejar cada imagen con piazzagriferia.cl/img/productos/<sku>.jpg
(mismo packshot, 650x927: el sitio no tiene más resolución que la carpeta).

rembg sólo da la máscara; el píxel del producto es el de la imagen de Carlos."""
from pathlib import Path
import numpy as np, cv2
from PIL import Image
from rembg import remove, new_session
RAIZ = Path(__file__).resolve().parents[3]
SRC = RAIZ / "raw/ebema/piazza-catalogo-a4a5/solo-piazza_01-10"
OUT = Path(__file__).parent / "recortes"
NUEVOS = {
    "PZ20009NE": "imagen_2026-10-01_140539231.png",   # monomando cocina Calyx negro
    "PZ43001": "imagen_2026-10-01_140555305.png",     # llave temporizada lavatorio
    "PZ20012NE": "imagen_2026-10-01_140801891.png",   # monomando ducha Calyx negro
    "PZ20002NE": "imagen_2026-10-01_141023197.png",   # monomando tina ducha Calyx negro
}
ses = new_session("isnet-general-use")
for k, nombre in NUEVOS.items():
    im = Image.open(SRC / nombre).convert("RGB")
    m = np.array(remove(im, session=ses, only_mask=True))
    # el fondo es blanco puro: lo que no es blanco es producto (rescata lo que rembg suelte)
    no_blanco = (np.array(im).min(2) < 236).astype(np.uint8) * 255
    n, lab, st, _ = cv2.connectedComponentsWithStats((np.maximum(m, no_blanco) > 40).astype(np.uint8), 8)
    grande = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    alpha = np.where(lab == grande, np.maximum(m, no_blanco), 0).astype(np.uint8)
    alpha = cv2.GaussianBlur(alpha, (0, 0), 0.6)
    rgba = np.dstack([np.array(im), alpha])
    ys, xs = np.where(alpha > 10)
    rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    Image.fromarray(rgba).save(OUT / f"{k}.png"); print(k, rgba.shape[1], rgba.shape[0])

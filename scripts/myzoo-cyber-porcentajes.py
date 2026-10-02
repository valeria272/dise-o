#!/usr/bin/env python3
"""MyZoo Cyber — cambia los globos «%» por «20%» (izquierda) y «30%» (derecha).

Paulina, 02-10-2026: los dos globos «corresponden a cada uno» de los descuentos del legal
(20 % en todos los productos, 30 % para usuarios Meli+). Vale para la story 1 y la story 2.

La pasada de Nano Banana Pro se hace sobre un RECORTE 16:9 de la franja de los globos
(más píxeles por globo, y el resto de la imagen no pasa por el generador). De la pasada
vuelve sólo lo que cambió: máscara por diferencia contra el recorte original, abierta
para botar el ruido, dilatada y difuminada. El perro queda el de la imagen original.

  recorte  <imagen> <y0> <prefijo>             → <prefijo>_rec.png / _rec.jpg (x 150–2922, 16:9)
  pegar    <imagen> <y0> <prefijo> <pasada> <salida>
Las imágenes son las de trabajo, 3072 × 5504.
"""
import sys

import cv2
import numpy as np
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

X0, X1 = 150, 2922
ALTO = round((X1 - X0) * 9 / 16)


def main():
    paso, imagen, y0, pref = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    caja = (X0, y0, X1, y0 + ALTO)
    im = Image.open(imagen).convert("RGB")
    if paso == "recorte":
        r = im.crop(caja)
        r.save(pref + "_rec.png")
        r.save(pref + "_rec.jpg", quality=95, subsampling=0)
        print("✓", pref + "_rec.png", r.size)
    elif paso == "pegar":
        orig = np.asarray(im.crop(caja)).astype(np.float32)
        nb = np.asarray(Image.open(sys.argv[5]).convert("RGB").resize((X1 - X0, ALTO), Image.LANCZOS)).astype(np.float32)
        # la pasada corre el tono general unos niveles: para comparar se iguala con UN
        # desplazamiento por canal (la mediana). Igualar con un desenfoque de toda la franja
        # mezclaba el amarillo del papel con el blanco de los globos y los dejaba crema.
        nb_c = nb + np.median((orig - nb).reshape(-1, 3), axis=0)
        dif = np.abs(nb_c - orig).max(axis=2)
        m = (cv2.GaussianBlur(dif, (0, 0), 2) > 22).astype(np.uint8)
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
        # sólo componentes grandes (globos y sus sombras), no motas en el pelo del perro
        n, lab, st, _ = cv2.connectedComponentsWithStats(m)
        keep = np.zeros_like(m)
        for i in range(1, n):
            if st[i, cv2.CC_STAT_AREA] > 4000:
                keep[lab == i] = 1
        keep = cv2.dilate(keep, np.ones((61, 61), np.uint8))
        # tono local: la diferencia original − pasada medida SÓLO donde no cambió nada, y
        # continuada hacia dentro de la zona de los globos (si no, queda una aureola)
        igual = 1 - cv2.dilate(keep, np.ones((41, 41), np.uint8)).astype(np.float32)
        d = cv2.GaussianBlur((orig - nb) * igual[..., None], (0, 0), 90) / np.maximum(cv2.GaussianBlur(igual, (0, 0), 90), 1e-3)[..., None]
        nb_c = nb + d
        k = cv2.GaussianBlur(keep.astype(np.float32), (0, 0), 14)[..., None]
        out = np.clip(nb_c * k + orig * (1 - k), 0, 255).astype(np.uint8)
        im.paste(Image.fromarray(out), caja[:2])
        im.save(sys.argv[6])
        Image.fromarray((keep * 255).astype(np.uint8)).save(pref + "_mascara.png")
        print("✓", sys.argv[6], "· zona cambiada:", f"{keep.mean() * 100:.0f} % del recorte")


if __name__ == "__main__":
    main()

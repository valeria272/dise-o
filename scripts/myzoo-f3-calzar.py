#!/usr/bin/env python3
"""MyZoo Fase 3 — calza el packshot REAL sobre el envase que la IA puso en la escena.

Por qué existe (Paulina, 30-09-2026): pegar el packshot con sombra por código «se ve
montado encima»; pedirle a la IA que ponga el envase lo integra bien a la escena, pero
Nano Banana Pro inventa la letra chica («Paso Moecotes», «Uto fracoonte»). Las
etiquetas no se tocan. Solución: la escena y la luz son de la IA; la etiqueta es la real.

  1. SIFT + homografía (RANSAC) entre el packshot real y la zona del envase generado.
  2. Se deforma el packshot real a esa posición y perspectiva.
  3. Se le traspasa la luz de la escena: razón de baja frecuencia, por canal, entre el
     envase generado y el real deformado (con desenfoque enmascarado para no traer halo
     del fondo). El detalle —el texto— es del real; la luz y el tono, de la escena.
  4. Orden: primero los de atrás, al final el de adelante (tapa lo que tiene que tapar).

Uso:  python scripts/myzoo-f3-calzar.py <escena> <salida> <json de calces>
      el json: [{"pack": "MyZoo_wipes_azul_110u.png", "roi": [x0,y0,x1,y1], "tapar": [[..]]}, …]
"""
import json
import os
import sys

import cv2
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROD = os.path.join(RAIZ, "public/assets/myzoo/producto/")


def blur_enmascarado(img, m, s):
    num = cv2.GaussianBlur(img * m[..., None], (0, 0), s)
    den = cv2.GaussianBlur(m, (0, 0), s)[..., None]
    return num / np.maximum(den, 1e-4)


def calzar(escena, pack_rgba, roi, tapar=()):
    H, W = escena.shape[:2]
    sift = cv2.SIFT_create(6000)
    gris_e = cv2.cvtColor(escena, cv2.COLOR_BGR2GRAY)
    mask = np.zeros((H, W), np.uint8)
    x0, y0, x1, y1 = roi
    mask[y0:y1, x0:x1] = 255
    for t in tapar:
        mask[t[1]:t[3], t[0]:t[2]] = 0
    # el packshot se reduce a la escala aproximada del ROI para que SIFT empareje mejor
    esc = (y1 - y0) / pack_rgba.shape[0]
    p = cv2.resize(pack_rgba, None, fx=esc, fy=esc, interpolation=cv2.INTER_AREA)
    gris_p = cv2.cvtColor(p[..., :3], cv2.COLOR_BGR2GRAY)
    kp1, d1 = sift.detectAndCompute(gris_p, (p[..., 3] > 128).astype(np.uint8) * 255)
    kp2, d2 = sift.detectAndCompute(gris_e, mask)
    pares = cv2.BFMatcher().knnMatch(d1, d2, k=2)
    buenos = [m for m, n in pares if m.distance < 0.78 * n.distance]
    src = np.float32([kp1[m.queryIdx].pt for m in buenos])
    dst = np.float32([kp2[m.trainIdx].pt for m in buenos])
    Hm, inl = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
    print(f"  {len(buenos)} pares, {int(inl.sum())} inliers")
    # también se deforma la versión a resolución completa, escalando la homografía
    S = np.diag([esc, esc, 1.0])
    Hfull = Hm @ S
    warp = cv2.warpPerspective(pack_rgba, Hfull, (W, H), flags=cv2.INTER_LANCZOS4)
    a = warp[..., 3].astype(np.float32) / 255
    a_duro = (a > 0.5).astype(np.float32)
    # luz de la escena: razón de baja frecuencia por canal (envase generado ÷ real deformado)
    E = escena.astype(np.float32)
    R = warp[..., :3].astype(np.float32)
    s = max(8, (y1 - y0) / 40)
    ratio = blur_enmascarado(E, a_duro, s) / np.maximum(blur_enmascarado(R, a_duro, s), 1)
    ratio = np.clip(ratio, 0.35, 1.5)
    R2 = np.clip(R * ratio, 0, 255)
    # borde: se come 1 px y se suaviza para que no quede recortado a tijera
    a2 = cv2.GaussianBlur(cv2.erode(a, np.ones((3, 3))), (0, 0), 0.9)[..., None]
    return (E * (1 - a2) + R2 * a2).astype(np.uint8)


if __name__ == "__main__":
    esc_path, out_path, cfg_path = sys.argv[1:4]
    escena = cv2.imread(esc_path)
    for c in json.load(open(cfg_path, encoding="utf-8")):
        print("→", c["pack"])
        pack = cv2.imread(PROD + c["pack"], cv2.IMREAD_UNCHANGED)
        escena = calzar(escena, pack, c["roi"], c.get("tapar", []))
    cv2.imwrite(out_path, escena)
    print("✓", out_path)

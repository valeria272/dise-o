#!/usr/bin/env python3
"""Mide el post-it amarillo en el primer frame de cada clip y escribe
src/compositions/gcl/track/postits.json, para pegarle el texto en perspectiva.

Por plano guarda dos cosas:
  · "quad": cuadrilátero TL, TR, BR, BL (rectángulo mínimo rotado) — perspectiva plana
  · "perfil": filas [y, x_izq, x_der] cada ~12 px de arriba abajo del papel — para seguir la
    CURVATURA (el papel se despega y se curva: el texto tiene que curvarse con él)

    python3 scripts/medir-postit.py P01 N01
"""
import json, sys
from pathlib import Path
import cv2, numpy as np

RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "src/compositions/gcl/track/postits.json"


def medir(clip):
    cap = cv2.VideoCapture(str(clip)); ok, f = cap.read()
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    m = ((hsv[..., 0] > 15) & (hsv[..., 0] < 40) & (hsv[..., 1] > 60) & (hsv[..., 2] > 140)).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cs, key=cv2.contourArea)
    mk = np.zeros(m.shape, np.uint8); cv2.drawContours(mk, [c], -1, 255, -1)
    q = cv2.boxPoints(cv2.minAreaRect(c))
    s = q.sum(1); d = np.diff(q, axis=1).ravel()
    tl, br = q[np.argmin(s)], q[np.argmax(s)]; tr, bl = q[np.argmin(d)], q[np.argmax(d)]
    quad = [[int(round(x)), int(round(y))] for x, y in (tl, tr, br, bl)]
    x, y, w, h = cv2.boundingRect(c)
    perfil = []
    for yy in range(y, y + h, 12):
        xs = np.where(mk[yy] > 0)[0]
        if len(xs) > 20:
            perfil.append([int(yy), int(xs.min()), int(xs.max())])
    return {"quad": quad, "perfil": perfil}, int(cv2.contourArea(c))


def main():
    datos = json.loads(OUT.read_text()) if OUT.exists() else {}
    for p in sys.argv[1:]:
        d, area = medir(RAIZ / f"public/assets/gcl/cap02-v3/video/{p}.mp4")
        datos[p] = d; print(f"{p}: quad {d['quad']} · {len(d['perfil'])} filas · área {area}")
    OUT.write_text(json.dumps(datos) + "\n")


if __name__ == "__main__":
    main()

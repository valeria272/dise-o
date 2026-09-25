#!/usr/bin/env python3
"""Sigue la punta del lápiz azul en un clip (frame a frame) y escribe
src/compositions/gcl/track/lapiz-<P>.json: [[frame, x, y], ...] en px del clip.

La punta es el extremo del blob azul más alejado de la mano (el punto más a la
izquierda y arriba). Sirve para que el texto «se escriba» siguiendo la mano.

    python3 scripts/seguir-lapiz.py N01
"""
import json, sys
from pathlib import Path
import cv2, numpy as np

RAIZ = Path(__file__).resolve().parent.parent


def main():
    p = sys.argv[1]
    cap = cv2.VideoCapture(str(RAIZ / f"public/assets/gcl/cap02-v3/video/{p}.mp4"))
    fps = cap.get(cv2.CAP_PROP_FPS); k = 0; out = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
        m = ((hsv[..., 0] > 100) & (hsv[..., 0] < 130) & (hsv[..., 1] > 90) & (hsv[..., 2] > 60)).astype(np.uint8) * 255
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        m[:900] = 0   # el lápiz vive abajo; arriba hay bokeh azul de la ciudad
        cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cs = [c for c in cs if cv2.contourArea(c) > 300]
        if cs:
            c = max(cs, key=cv2.contourArea).reshape(-1, 2)
            i = np.argmin(c[:, 0] * 1.0 + c[:, 1] * 0.6)   # extremo izquierdo-arriba = la punta
            out.append([k, int(c[i, 0]), int(c[i, 1])])
        k += 1
    dest = RAIZ / f"src/compositions/gcl/track/lapiz-{p}.json"
    dest.write_text(json.dumps({"fps": fps, "puntos": out}) + "\n")
    print(f"✓ {dest.name}: {len(out)}/{k} frames con lápiz; fps {fps}")
    for fr, x, y in out[::12]:
        print(f"  f{fr}: ({x},{y})")


if __name__ == "__main__":
    main()

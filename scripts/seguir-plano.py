#!/usr/bin/env python3
"""Tracking planar de una superficie en un clip → homografía por frame para Remotion.

Para pegar texto EN PERSPECTIVA sobre una superficie que se mueve (la carpeta
MÁS WOW, la tira de papel de Marta, el post-it): se siguen puntos con textura
dentro de un polígono (Lucas-Kanade) y se estima la homografía de la superficie
respecto del frame de referencia. En Remotion, `Superficie` (src/compositions/gcl/
superficie.ts) aplica H a las 4 esquinas del texto y arma un matrix3d.

⚠️ El polígono va sobre la SUPERFICIE con textura (manchas, cuadrícula), no sobre
el rótulo blanco liso: ahí no hay nada que seguir. Excluye manos y bordes.

    python3 scripts/seguir-plano.py public/assets/gcl/cap02-v3/video/P11a.mp4 \
        --ref 0 --poli 160,1100 420,1095 495,1385 255,1390 --out .../P11a.json

Salida: {"ref": r, "w": 1080, "h": 1944, "H": {"<frame>": [9 floats], ...}}
con H[k] que lleva coordenadas del frame r (en px del clip) al frame k.
"""
import argparse, json

import cv2
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("--ref", type=float, default=0, help="segundo de referencia")
    ap.add_argument("--hasta", type=float, default=None, help="segundo final (default: fin del clip)")
    ap.add_argument("--poli", nargs="+", required=True, help="vértices x,y del área a seguir (frame ref)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    cap = cv2.VideoCapture(a.clip)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frames = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        frames.append(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY))
    r = int(round(a.ref * fps))
    fin = len(frames) if a.hasta is None else min(len(frames), int(round(a.hasta * fps)) + 1)
    h, w = frames[0].shape

    poli = np.array([[float(v) for v in p.split(",")] for p in a.poli], np.int32)
    mask = np.zeros((h, w), np.uint8)
    cv2.fillPoly(mask, [poli], 255)

    base = cv2.goodFeaturesToTrack(frames[r], maxCorners=400, qualityLevel=0.005, minDistance=6, mask=mask)
    if base is None or len(base) < 8:
        raise SystemExit(f"✗ muy pocos puntos con textura en el polígono ({0 if base is None else len(base)})")
    lk = dict(winSize=(25, 25), maxLevel=4, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.01))

    salida = {str(r): np.eye(3).flatten().tolist()}
    # Se sigue frame a frame y se acumula contra la referencia; los puntos que se
    # pierden se descartan, y si quedan pocos se re-siembran dentro del polígono
    # proyectado.
    ref_pts = base.reshape(-1, 2)
    prev_pts = ref_pts.copy()
    Hk = np.eye(3)
    for k in range(r + 1, fin):
        nxt, st, _ = cv2.calcOpticalFlowPyrLK(frames[k - 1], frames[k], prev_pts.reshape(-1, 1, 2).astype(np.float32), None, **lk)
        back, st2, _ = cv2.calcOpticalFlowPyrLK(frames[k], frames[k - 1], nxt, None, **lk)
        err = np.linalg.norm(back.reshape(-1, 2) - prev_pts, axis=1)
        bueno = (st.ravel() == 1) & (st2.ravel() == 1) & (err < 1.0)
        ref_pts, nxt = ref_pts[bueno], nxt.reshape(-1, 2)[bueno]
        if len(ref_pts) >= 8:
            H, inl = cv2.findHomography(ref_pts, nxt, cv2.RANSAC, 2.0)
            if H is not None:
                Hk = H
                inl = inl.ravel() == 1
                ref_pts, nxt = ref_pts[inl], nxt[inl]
        salida[str(k)] = (Hk / Hk[2, 2]).flatten().tolist()
        if len(ref_pts) < 60:  # re-sembrar: puntos nuevos del frame k, llevados a coords de ref con H⁻¹
            pk = cv2.perspectiveTransform(poli.reshape(-1, 1, 2).astype(np.float32), Hk).reshape(-1, 2).astype(np.int32)
            mk = np.zeros((h, w), np.uint8); cv2.fillPoly(mk, [pk], 255)
            nuevos = cv2.goodFeaturesToTrack(frames[k], maxCorners=300, qualityLevel=0.005, minDistance=6, mask=mk)
            if nuevos is not None:
                nuevos = nuevos.reshape(-1, 2)
                en_ref = cv2.perspectiveTransform(nuevos.reshape(-1, 1, 2), np.linalg.inv(Hk)).reshape(-1, 2)
                ref_pts = np.vstack([ref_pts, en_ref]); nxt = np.vstack([nxt, nuevos])
        prev_pts = nxt
    json.dump({"ref": r, "w": w, "h": h, "fps": fps, "H": salida}, open(a.out, "w"))
    print(f"✓ {a.out}: frames {r}–{fin - 1}, {len(ref_pts)} puntos al final")


if __name__ == "__main__":
    main()

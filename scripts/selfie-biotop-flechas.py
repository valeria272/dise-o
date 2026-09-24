#!/usr/bin/env python3
"""Ancla las flechas de la prueba Biotop: de la FICHA al PRODUCTO, sin tocar nada.

    ~/copylab-venv/bin/python3 scripts/selfie-biotop-flechas.py

POR QUÉ EXISTE (24-09-2026). Coni: «las flechas deben dirigir desde el bullet hasta el
producto». Calcar la forma no basta: hay que ANCLARLA. Por formato:
  1. Rinde la pieza sin flechas y mide dónde quedaron las cajas de beneficio (blanco
     puro) y los frascos (alfa de las imágenes ya preparadas).
  2. Prueba salidas a lo largo del borde de la ficha que mira a su producto y, para
     cada una, tira la flecha hacia el frasco hasta justo antes de tocarlo (o su sombra).
  3. Calca el trazo de la historia entre esos dos puntos (girado y escalado) y descarta
     todo recorrido que roce algo: texto, caja, logo, frasco o sombra.
  4. Se queda con el que respeta mejor el largo del trazo original y apunta al cuerpo
     del frasco. Escribe start/tip en src/compositions/selfie/biotop-prueba.json.
Después: scripts/selfie-biotop-qa.py para el render y el control final.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _selfie_biotop import mascara_producto, obstaculos  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
JSON = RAIZ / "src/compositions/selfie/biotop-prueba.json"
PROD = RAIZ / "public/assets/selfie/2026-nuevo-estilo/biotop"
TMP = RAIZ / "out/selfie/prueba/_qa"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
COMP = {"post": "Post", "story": "Story", "mail": "Mail", "bannerDesk": "BannerDesk", "bannerMobile": "BannerMobile"}
MARGEN = 18  # px de salida libres alrededor del trazo (el QA exige 10 con filtro cuadrado)


def still(comp, destino, formato):
    props = '{"formato":"%s","capa":"sinFlechas"}' % formato
    r = subprocess.run([str(RAIZ / "node_modules/.bin/remotion"), "still", f"SelfiePruebaBiotop-{comp}", str(destino),
                        f"--props={props}", f"--browser-executable={CHROME}", "--log=error"],
                       cwd=RAIZ, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-2000:])


def puntos(d):
    n = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", d)]
    return np.array(list(zip(n[0::2], n[1::2])))


def calca(P, start, tip):
    s0, t0 = P[0], P[-1]
    v0, v1 = t0 - s0, tip - start
    k = np.hypot(*v1) / np.hypot(*v0)
    g = np.arctan2(v1[1], v1[0]) - np.arctan2(v0[1], v0[0])
    R = np.array([[np.cos(g), -np.sin(g)], [np.sin(g), np.cos(g)]]) * k
    return start + (P - s0) @ R.T


def muestrea(Q, n=60):
    out = [Q[0]]
    for i in range(1, len(Q), 3):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        for t in np.linspace(0, 1, n)[1:]:
            out.append((1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3)
    return np.array(out)


def cabeza(Q, L):
    tip, pen = Q[-1], Q[-2]
    ang = np.arctan2(*(tip - pen)[::-1])
    alas = []
    for a in (ang + np.radians(28), ang - np.radians(28)):
        ala = tip - L * np.array([np.cos(a), np.sin(a)])
        alas += list(np.linspace(tip, ala, 12))
    return np.array(alas)


def main():
    D = json.loads(JSON.read_text())
    TMP.mkdir(parents=True, exist_ok=True)
    trazos = {k: puntos(D["_trazo"][k]["d"]) for k in ("700", "911")}
    for fmt, comp in COMP.items():
        L = D[fmt]
        u = L["outW"] / L["mesaW"]
        t = L["t"]
        img = TMP / f"{comp}-anclas.png"
        still(comp, img, fmt)
        px = np.array(Image.open(img).convert("RGB")).astype(float)
        H, W = px.shape[:2]
        obst = obstaculos(px, fmt, L)
        libre = ndimage.distance_transform_edt(~obst)  # px hasta el obstáculo más cercano
        r = 2.4 * t * u / 2 + MARGEN

        # cajas de beneficio: blanco puro macizo (el titular y el logo son trazos finos)
        blanco = (px > 250).all(axis=2)
        blanco = ndimage.binary_opening(blanco, iterations=max(2, int(6 * t * u)))
        lab, n = ndimage.label(blanco)
        cajas = sorted(ndimage.find_objects(lab), key=lambda s: -(s[0].stop - s[0].start) * (s[1].stop - s[1].start))[:2]

        centros = {k: np.array([L[f"p{k}"]["cx"] * u, L[f"p{k}"]["cy"] * u]) for k in ("700", "911")}
        cen = lambda s: np.array([(s[1].start + s[1].stop) / 2, (s[0].start + s[0].stop) / 2])
        # cada caja blanca se empareja con la ficha que la dibujó (su x, y, w del JSON)
        def ancla(k):
            f = L[f"ficha{k}"]
            return np.array([(f["x"] + f["w"] / 2) * u, f["y"] * u + 110 * t * u])
        caja_de = {k: min(cajas, key=lambda s: np.hypot(*(cen(s) - ancla(k)))) for k in ("700", "911")}

        for k in ("700", "911"):
            p = L[f"p{k}"]
            c = centros[k]
            pm = mascara_producto(fmt, k, L, H, W)
            cerca_prod = ndimage.distance_transform_edt(~pm) < 90 * t * u  # frasco + su sombra
            caja = caja_de[k]
            bx0, bx1, by0, by1 = caja[1].start, caja[1].stop, caja[0].start, caja[0].stop
            fx0, fx1 = bx0 - 32 * t * u, bx1 + 32 * t * u   # la caja coral del nombre es más ancha
            fy0, fy1 = by0 - 80 * t * u, by1                 # y va encima de la blanca
            gap = r + 6

            # eje del frasco, para apuntar al cuerpo y no a la tapa
            ang = np.radians(p["rot"])
            eje = np.array([np.sin(ang), -np.cos(ang)])  # hacia la tapa
            h = p["h"] * u
            objetivos = [c + eje * h * f for f in (0.0, -0.15, 0.15, 0.3, -0.3)]

            P = trazos[k]
            L0 = np.hypot(*(P[-1] - P[0])) * t * u
            mejor = None
            borde = []
            for x in np.linspace(fx0, fx1, 24):
                borde += [(x, fy0 - gap), (x, fy1 + gap)]
            for y in np.linspace(fy0, fy1, 12):
                borde += [(fx0 - gap, y), (fx1 + gap, y)]
            for s in map(np.array, borde):
                if libre[int(np.clip(s[1], 0, H - 1)), int(np.clip(s[0], 0, W - 1))] <= r:
                    continue
                for oi, o in enumerate(objetivos):
                    v = o - s
                    dist = np.hypot(*v)
                    if dist < 1:
                        continue
                    u_ = v / dist
                    # avanza hasta justo antes del frasco o su sombra
                    tip = None
                    for step in np.arange(0, dist, 3):
                        q = s + u_ * step
                        yi, xi = int(q[1]), int(q[0])
                        if not (0 <= xi < W and 0 <= yi < H):
                            break
                        if libre[yi, xi] <= r:
                            if cerca_prod[yi, xi]:
                                tip = s + u_ * max(step - 3, 0)
                            break
                    if tip is None:
                        continue
                    largo = np.hypot(*(tip - s))
                    if not 0.6 * L0 <= largo <= 1.7 * L0:
                        continue
                    Q = calca(P * 1.0, s, tip)
                    muestras = np.vstack([muestrea(Q), cabeza(Q, 22 * t * u)])
                    xi, yi = muestras[:, 0].astype(int), muestras[:, 1].astype(int)
                    if (xi < 15).any() or (yi < 15).any() or (xi >= W - 15).any() or (yi >= H - 15).any():
                        continue
                    if (libre[yi, xi] <= r).any():
                        continue
                    nota = abs(largo / L0 - 1) + 0.15 * oi
                    if mejor is None or nota < mejor[0]:
                        mejor = (nota, s, tip, largo / L0)
            if mejor is None:
                print(f"✗ {fmt:12} {k}: ningún recorrido limpio de la ficha al frasco — hay que mover la ficha")
                continue
            _, s, tip, rel = mejor
            L[f"start{k}"] = {"x": round(float(s[0]) / u, 1), "y": round(float(s[1]) / u, 1)}
            L[f"tip{k}"] = {"x": round(float(tip[0]) / u, 1), "y": round(float(tip[1]) / u, 1)}
            print(f"✓ {fmt:12} {k}: sale de la ficha en {L[f'start{k}']} → llega al frasco en {L[f'tip{k}']}  (largo {rel:.2f}× el trazo)")
    JSON.write_text(json.dumps(D, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()

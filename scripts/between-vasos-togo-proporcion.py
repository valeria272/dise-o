#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BETWEEN · cuánto mide de verdad cada vaso To Go, uno respecto del otro.

En la foto los tres vasos NO están a la misma distancia de la cámara ni se ven
desde el mismo ángulo, así que sus altos en píxeles no son su proporción. Acá se
mide con DOS reglas independientes y se entrega el compromiso entre las dos,
porque ninguna foto puede satisfacer a las dos a la vez — para eso habría que
haberlos fotografiado a los tres desde el mismo punto.

REGLA 1 · EL HORIZONTE (sobre IMG_4153, mesa de listones)
    alto_real / altura_cámara = (y_base − y_tope) / (y_base − y_horizonte)
El horizonte sale de que los listones están IGUALMENTE ESPACIADOS: sus alturas
sobre una columna siguen y(k) = (A·k + B)/(C·k + 1) y el horizonte es A/C.
Ajuste conjunto de 5 columnas y 29 juntas → y = 1440 px, residuo 6,3 px.

⛔ En IMG_4153 los tres vasos SE TOCAN en la silueta (el mediano tapa al grande)
y el mate los une. El tope y la base de cada uno se miden en una VENTANA CENTRAL
que es suya y de nadie más, y se verifica que la caja no lo corte. La primera
versión de este script medía con cajas que sí cortaban.

REGLA 2 · LA TAPA (sobre IMG_5715, donde los tres están limpios y separados)
El mediano y el grande **comparten tapa**, así que en la entrega sus tapas tienen
que medir lo mismo. Eso fija la escala relativa entre esos dos sin depender de
ninguna otra foto. Para el chico, que tiene tapa propia y más chica, se usa la
razón estándar de la familia 8 oz / 12-16 oz.

Las dos reglas discrepan ~5 % en el mediano: es el ángulo distinto desde el que
se fotografió cada vaso. Se entrega la **media geométrica**, que reparte el error
en ±2,5 % en vez de cargárselo entero a una de las dos.
"""
import json
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw
from scipy.optimize import least_squares

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

TRABAJO = RAIZ / "out/hilton/between/vasos-togo/_trabajo"
SESION = RAIZ / "raw/hilton/between/vasos-togo-sep2026/jpg"
FOTO = "IMG_4153"
VASOS = ["chico", "mediano", "grande"]

# Caja generosa (que no corte) + ventana central que es sólo de ese vaso.
CFG = {
    "chico":   dict(caja=(0, 1900, 980, 3460), vent=(120, 700)),
    "mediano": dict(caja=(860, 1680, 1880, 3400), vent=(1020, 1680)),
    "grande":  dict(caja=(1760, 1380, 3024, 3400), vent=(2120, 2720)),
}
COLUMNAS = [150, 330, 520, 1120, 1700, 2990]
FRANJA = (3200, 4025)

# Tapa del chico contra la del grande. Los vasos son la familia estándar
# 8 oz / 12 oz / 16 oz: el chico lleva tapa de 80 mm y los otros dos de 90 mm.
TAPA_CHICO = 80.0 / 90.0


def juntas(img, x, y0, y1, ancho=26):
    tira = cv2.cvtColor(img[y0:y1, x - ancho // 2:x + ancho // 2], cv2.COLOR_BGR2GRAY)
    perfil = tira.mean(1).astype(np.float32)
    suave = cv2.GaussianBlur(perfil.reshape(-1, 1), (0, 0), 3).ravel()
    fondo = cv2.GaussianBlur(perfil.reshape(-1, 1), (0, 0), 40).ravel()
    hueco = fondo - suave
    umbral = max(6.0, 0.35 * hueco.max())
    ys, i = [], 0
    while i < len(hueco):
        if hueco[i] > umbral:
            j = i
            while j < len(hueco) and hueco[j] > umbral:
                j += 1
            if j - i >= 3:
                w = hueco[i:j]
                ys.append(y0 + i + float((w * np.arange(len(w))).sum() / w.sum()))
            i = j
        else:
            i += 1
    return np.array(ys)


def horizonte(img):
    datos = []
    for x in COLUMNAS:
        ys = juntas(img, x, *FRANJA)
        if len(ys) >= 4:
            datos.append((x, ys))
    assert len(datos) >= 2, "muy pocas columnas útiles"

    sueltos = []
    for x, ys in datos:
        k = np.arange(len(ys), dtype=float)
        s = least_squares(lambda p: (p[0] * k + p[1]) / (p[2] * k + 1.0) - ys,
                          [ys[-1] - ys[0], ys[0], 1e-3], loss="huber",
                          f_scale=2.0, max_nfev=20000)
        A, B, C = s.x
        if abs(C) > 1e-7:
            sueltos.append(A / C)

    def rj(p):
        out = []
        for i, (x, ys) in enumerate(datos):
            B, C = p[1 + 2 * i], p[2 + 2 * i]
            k = np.arange(len(ys), dtype=float)
            out.append(p[0] + (B - p[0]) / (C * k + 1.0) - ys)
        return np.concatenate(out)

    p0 = [float(np.nanmedian(sueltos))]
    for x, ys in datos:
        p0 += [float(ys[0]), 1e-3]
    s = least_squares(rj, p0, loss="huber", f_scale=2.0, max_nfev=60000)
    return float(s.x[0]), sueltos, float(np.sqrt(np.mean(s.fun ** 2)))


def _mate(ruta_png, ruta_out, recorte):
    if not ruta_out.exists():
        cv2.imwrite(str(ruta_png), recorte)
        subprocess.run(["npx", "tsx", str(RAIZ / "scripts/remove-bg.ts"),
                        str(ruta_png), str(ruta_out)],
                       cwd=str(RAIZ), check=True, shell=(os.name == "nt"),
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return np.array(Image.open(ruta_out).convert("RGBA"))[:, :, 3] > 128


# ⚠️ La regla de la tapa compara los tres vasos DENTRO de una misma foto, así que
# se mide siempre sobre IMG_5715 aunque el mediano se ENTREGUE desde IMG_5719
# (su vaso tiene un pliegue del cartón justo hacia la cámara en 5715). Por eso
# esta medición hace sus propios recortes y no usa los de la entrega.
CAJAS_5715 = {
    "grande": (340, 2660, 1780, 5100),
    "mediano": (1540, 2980, 2960, 5160),
    "chico": (2800, 3320, 4284, 5340),
}


def ancho_de_tapa(nombre):
    """Ancho máximo de la tapa y alto del vaso, medidos sobre IMG_5715."""
    q = TRABAJO / ("tapa5715-%s-nobg.png" % nombre)
    if not q.exists():
        img = cv2.imread(str(RAIZ / "raw/hilton/between/cafes-sep2026/IMG_5715.jpg"))
        x0, y0, x1, y1 = CAJAS_5715[nombre]
        _mate(TRABAJO / ("tapa5715-%s.png" % nombre), q, img[y0:y1, x0:x1])
    a = np.array(Image.open(q).convert("RGBA"))[:, :, 3] > 128
    f = np.nonzero(a.any(1))[0]
    y0, y1 = int(f.min()), int(f.max())
    alto = y1 - y0 + 1
    anchos = [int(np.ptp(np.nonzero(a[y])[0])) + 1 if a[y].any() else 0
              for y in range(y0, int(y0 + 0.35 * alto))]
    return float(max(anchos)), alto


def main():
    TRABAJO.mkdir(parents=True, exist_ok=True)
    img = cv2.imread(str(SESION / (FOTO + ".jpg")))
    assert img is not None, FOTO

    print("REGLA 1 — el horizonte sobre %s" % FOTO)
    yh, sueltos, rms = horizonte(img)
    print("   horizonte y = %.1f px · residuo %.2f px" % (yh, rms))

    alto_real = {}
    for n in VASOS:
        c = CFG[n]
        x0, y0, x1, y1 = c["caja"]
        m = _mate(TRABAJO / ("alt-%s.png" % n), TRABAJO / ("alt-%s-nobg.png" % n),
                  img[y0:y1, x0:x1])
        sub = m[:, c["vent"][0] - x0:c["vent"][1] - x0]
        fil = np.nonzero(sub.any(1))[0]
        assert fil.min() > 1 and fil.max() < m.shape[0] - 2, \
            "la caja de %s corta el vaso" % n
        yt, yb = int(fil.min()) + y0, int(fil.max()) + y0
        alto_real[n] = (yb - yt) / (yb - yh)
        print("   %-8s tope %5d · base %5d · alto %5d · alto real %.4f"
              % (n, yt, yb, yb - yt, alto_real[n]))
    H = {n: alto_real[n] / alto_real["grande"] for n in VASOS}
    print("   -> por el horizonte (grande = 1,000): chico %.4f · mediano %.4f"
          % (H["chico"], H["mediano"]))

    print("\nREGLA 2 — la tapa, sobre IMG_5715 (recortes limpios)")
    tapa, alto5715 = {}, {}
    for n in VASOS:
        tapa[n], alto5715[n] = ancho_de_tapa(n)
        print("   %-8s tapa %6.0f px · alto %5d px" % (n, tapa[n], alto5715[n]))
    D = {"grande": 1.0, "mediano": 1.0, "chico": TAPA_CHICO}
    # escala de cada vaso en IMG_5715 según su tapa, y el alto que implica
    s_tapa = {n: tapa[n] / D[n] for n in VASOS}
    T = {n: (alto5715[n] / s_tapa[n]) / (alto5715["grande"] / s_tapa["grande"])
         for n in VASOS}
    print("   -> por la tapa (grande = 1,000): chico %.4f · mediano %.4f"
          % (T["chico"], T["mediano"]))

    print("\nCOMPROMISO — media geométrica de las dos reglas")
    final = {n: float(np.sqrt(H[n] * T[n])) for n in VASOS}
    for n in VASOS:
        e = 100 * (max(H[n], T[n]) / final[n] - 1)
        print("   %-8s %.4f   (horizonte %.4f · tapa %.4f · error repartido ±%.1f %%)"
              % (n, final[n], H[n], T[n], e))

    json.dump(dict(foto=FOTO, horizonte=yh, por_horizonte=H, por_tapa=T,
                   proporcion=final, tapa_px_5715=tapa, alto_px_5715=alto5715),
              open(TRABAJO / "proporcion.json", "w"), indent=2)

    im = Image.open(SESION / (FOTO + ".jpg")).convert("RGB")
    d = ImageDraw.Draw(im)
    d.line([(0, yh), (im.width, yh)], fill=(255, 0, 255), width=9)
    d.text((40, yh + 18), "horizonte", fill=(255, 0, 255))
    for n in VASOS:
        c = CFG[n]
        x0, y0, x1, y1 = c["caja"]
        m = np.array(Image.open(TRABAJO / ("alt-%s-nobg.png" % n))
                     .convert("RGBA"))[:, :, 3] > 128
        sub = m[:, c["vent"][0] - x0:c["vent"][1] - x0]
        fil = np.nonzero(sub.any(1))[0]
        xm = (c["vent"][0] + c["vent"][1]) // 2
        d.line([(xm, fil.min() + y0), (xm, fil.max() + y0)], fill=(255, 240, 0), width=9)
        d.line([(xm - 70, fil.max() + y0), (xm + 70, fil.max() + y0)],
               fill=(0, 255, 255), width=9)
    im.thumbnail((1100, 1500))
    im.save(TRABAJO / "proporcion-verificacion.jpg", quality=90)
    print("\nverificación ->", TRABAJO / "proporcion-verificacion.jpg")


if __name__ == "__main__":
    main()

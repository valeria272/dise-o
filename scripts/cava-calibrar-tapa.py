#!/usr/bin/env python3
"""
CAVA MORANDÉ — encuentra la tapa del barril en cada fondo del KV.

POR QUÉ EXISTE ESTE ARCHIVO. La v2 de los mailings puso el punto de apoyo de
las botellas a ojo, con un número escrito a mano. Con el fondo regenerado ese
número quedó sobre el CUERPO cilíndrico del barril y las botellas salieron
flotando delante de él, apoyadas en el aire. Valeria lo cazó al primer vistazo:
«las botellas no están sobre el barril».

La superficie de apoyo de un barril no es una recta: es una ELIPSE en
perspectiva. Una botella al centro apoya más abajo que una del costado. Así que
acá se detecta la elipse de verdad y se guarda en un JSON, y el compositor
apoya cada botella en la curva según su x.

Salida: public/assets/cava/kv/tapas.json
    {archivo: {cx, cy, rx, ry, y_frente, y_fondo}}   en píxeles sobre 2250 de ancho

Uso:
    python3 scripts/cava-calibrar-tapa.py [--ver]
"""
import argparse
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KVS = os.path.join(RAIZ, "public", "assets", "cava", "kv")
W = 2250


def detecta_tapa(ruta):
    """
    La tapa es una mancha de madera clara ENCERRADA por el aro de hierro oscuro.
    El viñedo otoñal del fondo también es cálido y claro, así que filtrar por
    color no basta: hay que quedarse con la COMPONENTE CONEXA que se comporta
    como una tapa — ancha, achatada, centrada y sin tocar los bordes laterales.
    """
    from scipy import ndimage

    im = Image.open(ruta).convert("RGB")
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    a = np.array(im).astype(float)
    H = a.shape[0]

    r, bl = a[:, :, 0], a[:, :, 2]
    lum = a.mean(axis=2)
    # madera iluminada: cálida y por encima de la mediana de la mitad inferior
    madera = (r > bl + 14) & (lum > np.percentile(lum[H // 2:], 60))
    madera[: int(H * 0.35)] = False
    madera = ndimage.binary_opening(madera, np.ones((9, 9)))
    madera = ndimage.binary_closing(madera, np.ones((13, 13)))

    etiquetas, n = ndimage.label(madera)
    if not n:
        raise SystemExit(f"no se encontró madera en {os.path.basename(ruta)}")

    mejor, mejor_puntaje = None, -1e9
    for k in range(1, n + 1):
        ys, xs = np.where(etiquetas == k)
        if len(xs) < 4000:
            continue
        x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        ancho, alto = x1 - x0, y1 - y0
        if ancho < W * 0.20 or alto < 25:
            continue
        # una tapa en perspectiva es MUCHO más ancha que alta
        achatada = ancho / max(alto, 1)
        if achatada < 1.6:
            continue
        # y no se derrama hasta los bordes del cuadro: eso es el viñedo
        if x0 < W * 0.02 and x1 > W * 0.98:
            continue
        # se prefiere la que esté más centrada y más arriba (la tapa, no el suelo)
        centrado = 1 - abs((x0 + x1) / 2 - W / 2) / (W / 2)
        puntaje = len(xs) * (0.5 + centrado) * min(achatada / 3.0, 1.4) - y0 * 12
        if puntaje > mejor_puntaje:
            mejor_puntaje, mejor = puntaje, (xs, ys)

    if mejor is None:
        raise SystemExit(f"no se aisló la tapa en {os.path.basename(ruta)}")
    xs, ys = mejor
    cx = float((xs.min() + xs.max()) / 2)
    rx = float((xs.max() - xs.min()) / 2)
    y_fondo, y_frente = float(ys.min()), float(ys.max())
    return {"cx": cx, "cy": (y_fondo + y_frente) / 2, "rx": rx,
            "ry": (y_frente - y_fondo) / 2,
            "y_frente": y_frente, "y_fondo": y_fondo,
            "x0": float(xs.min()), "x1": float(xs.max()), "alto_img": H}


def apoyo(t, x, margen=0.80):
    """
    Dónde apoya una botella colocada en la columna `x`: sobre la elipse, no en
    el borde. `margen` la mete hacia adentro para que no quede al filo.
    """
    dx = (x - t["cx"]) / max(t["rx"], 1)
    dx = max(-0.99, min(0.99, dx))
    # y de la mitad delantera de la elipse, achatada por el margen
    return t["cy"] + t["ry"] * margen * (1 - dx ** 2) ** 0.5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ver", action="store_true", help="dibuja la elipse guardada")
    ap.add_argument("--grilla", action="store_true",
                    help="saca el fondo con una grilla de coordenadas, para medir a mano")
    args = ap.parse_args()

    if args.grilla:
        f = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 34)
        for n in sorted(os.listdir(KVS)):
            if not n.endswith(".png") or n.startswith("_"):
                continue
            im = Image.open(os.path.join(KVS, n)).convert("RGB")
            im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
            d = ImageDraw.Draw(im)
            for x in range(0, W, 150):
                d.line([x, 0, x, im.height], fill=(0, 255, 255), width=2)
                d.text((x + 6, 6), str(x), font=f, fill=(0, 255, 255))
            for y in range(0, im.height, 150):
                d.line([0, y, W, y], fill=(255, 255, 0), width=2)
                d.text((8, y + 6), str(y), font=f, fill=(255, 255, 0))
            im.resize((640, round(640 * im.height / W)), Image.LANCZOS).save(
                os.path.join(KVS, f"_grid_{n.replace('.png', '.jpg')}"), quality=92)
            print(f"grilla → _grid_{n.replace('.png', '.jpg')}")
        return

    if args.ver:
        # dibuja la elipse YA GUARDADA, para comprobar que sigue calzando
        tapas = json.load(open(os.path.join(KVS, "tapas.json")))
        for n, t in tapas.items():
            if n.startswith("_"):
                continue
            im = Image.open(os.path.join(KVS, n)).convert("RGB")
            im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
            d = ImageDraw.Draw(im)
            d.ellipse([t["cx"] - t["rx"], t["cy"] - t["ry"],
                       t["cx"] + t["rx"], t["cy"] + t["ry"]],
                      outline=(0, 255, 90), width=7)
            for k in range(5):
                x = t["x0"] + (t["x1"] - t["x0"]) * (k + 0.5) / 5
                y = apoyo(t, x)
                d.line([x, y - 260, x, y], fill=(255, 40, 40), width=6)
                d.ellipse([x - 14, y - 14, x + 14, y + 14], fill=(255, 40, 40))
            im.resize((560, round(560 * im.height / W)), Image.LANCZOS).save(
                os.path.join(KVS, f"_tapa_{n.replace('.png', '.jpg')}"), quality=90)
            print(f"comprobación → _tapa_{n.replace('.png', '.jpg')}")
        return

    tapas = {}
    for n in sorted(os.listdir(KVS)):
        if not n.endswith(".png") or n.startswith("_"):
            continue
        try:
            t = detecta_tapa(os.path.join(KVS, n))
        except SystemExit as e:
            print(f"{n}: {e}")
            continue
        tapas[n] = t
        print(f"{n}: tapa x {t['x0']:.0f}..{t['x1']:.0f}  "
              f"fondo y={t['y_fondo']:.0f}  frente y={t['y_frente']:.0f}  "
              f"(rx={t['rx']:.0f} ry={t['ry']:.0f})")
        if args.ver:
            im = Image.open(os.path.join(KVS, n)).convert("RGB")
            im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
            d = ImageDraw.Draw(im)
            d.ellipse([t["cx"] - t["rx"], t["cy"] - t["ry"],
                       t["cx"] + t["rx"], t["cy"] + t["ry"]],
                      outline=(0, 255, 90), width=7)
            for k in range(5):
                x = t["x0"] + (t["x1"] - t["x0"]) * (k + 0.5) / 5
                y = apoyo(t, x)
                d.line([x, y - 90, x, y], fill=(255, 40, 40), width=6)
                d.ellipse([x - 12, y - 12, x + 12, y + 12], fill=(255, 40, 40))
            im.resize((560, round(560 * im.height / W)), Image.LANCZOS).save(
                os.path.join(KVS, f"_tapa_{n.replace('.png', '.jpg')}"), quality=90)

    with open(os.path.join(KVS, "tapas.json"), "w") as fh:
        json.dump(tapas, fh, indent=1)
    print(f"\n→ {os.path.join(KVS, 'tapas.json')}")


if __name__ == "__main__":
    main()

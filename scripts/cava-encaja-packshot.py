# -*- coding: utf-8 -*-
"""Encaja el packshot OFICIAL sobre la botella de una escena generada.

POR QUÉ. Magnific integra la botella en la escena de forma impecable —sombra,
reflejo y luz reales— pero al hacerlo REDIBUJA la etiqueta, y
`clients/cava/marca.json` lo prohíbe expresamente:

    botellas.prohibido: "editar, reescribir o regenerar una etiqueta
                         (año, cepa, valle, tipografía)"

Así que la escena aporta la luz y la sombra, y encima va la etiqueta de verdad.

El ancla es la ETIQUETA BLANCA, que en el packshot ocupa una fracción fija del
alto de la botella (0,416–0,708). Detectándola en la escena sale la escala y la
posición de toda la botella.

    python3 scripts/cava-encaja-packshot.py escena.png salida.png [--ajuste-y 0]
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

PACK = "public/assets/cava/bottles/2x/7colores-limited-carmenere.png"
ET_Y0, ET_Y1 = 0.416, 0.708          # la etiqueta, en fracción del alto de botella
ET_X0, ET_X1 = 0.141, 0.625


def mancha_blanca(a, xmin=0.40):
    r, g, b = [a[:, :, i].astype(int) for i in range(3)]
    m = (r > 168) & (g > 152) & (b > 138) & (r - b < 70) & (r - b > -10)
    m[:, :int(a.shape[1] * xmin)] = False
    lab, k = ndimage.label(m)
    if not k:
        return None
    tam = ndimage.sum(m, lab, range(1, k + 1))
    i = int(np.argmax(tam)) + 1
    ys, xs = np.where(lab == i)
    return xs.min(), xs.max(), ys.min(), ys.max()


def encaja(escena, ajuste_y=0, ajuste_x=0, escala=1.0, xmin=0.40):
    a = np.array(escena.convert("RGB"))
    q = mancha_blanca(a, xmin)
    if q is None:
        raise SystemExit("no se encontró la etiqueta en la escena")
    x0, x1, y0, y1 = q
    alto_bot = (y1 - y0) / (ET_Y1 - ET_Y0) * escala
    tope = y0 - ET_Y0 * alto_bot + ajuste_y
    eje = (x0 + x1) / 2.0 + ajuste_x

    p = Image.open(PACK).convert("RGBA")
    p = p.crop(p.split()[-1].getbbox())
    anc = round(alto_bot * p.width / p.height)
    p = p.resize((anc, int(round(alto_bot))), Image.LANCZOS)

    out = escena.convert("RGBA").copy()
    out.alpha_composite(p, (int(eje - anc / 2), int(tope)))
    return out, dict(eje=eje, tope=tope, alto=alto_bot, anc=anc,
                     etiqueta=(x0, x1, y0, y1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("escena")
    ap.add_argument("salida")
    ap.add_argument("--ajuste-y", dest="ay", type=float, default=0)
    ap.add_argument("--ajuste-x", dest="ax", type=float, default=0)
    ap.add_argument("--escala", type=float, default=1.0)
    ap.add_argument("--xmin", type=float, default=0.40)
    a = ap.parse_args()
    im = Image.open(a.escena)
    out, info = encaja(im, a.ay, a.ax, a.escala, a.xmin)
    out.convert("RGB").save(a.salida)
    print("  %s  eje=%.0f tope=%.0f alto=%.0f ancho=%d  (etiqueta %s)" % (
        a.salida, info["eje"], info["tope"], info["alto"], info["anc"], info["etiqueta"]))


if __name__ == "__main__":
    main()

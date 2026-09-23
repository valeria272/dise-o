# -*- coding: utf-8 -*-
"""Saca el logotipo de CAVA MORANDÉ del .ai, VECTORIAL y con su color real.

POR QUÉ EXISTE. El 23-09-2026 la pieza del Cyber salió con el logo todo blanco:
se había extraído del PNG exportado con una máscara de luminancia, que pinta de
blanco cuanto toca. El logo de CAVA tiene DOS tintas y el isotipo NO es blanco.

Leído de `CAVA_SEPT.ai` con PyMuPDF, el logo son dos rellenos:

    #FFFFFF  el texto  CAVA MORANDÉ
    #E1670E  el isotipo

⚠️ `clients/cava/marca.json` declara `naranjoLogo: #DD660E`. El editable dice
**#E1670E**. Manda el editable — la ficha se anotó de una pieza, no del vector.

    python3 scripts/cava-logo-desde-editable.py <.ai> <salida.png> [--pagina 13] [--escala 6]
"""
import argparse
import fitz


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ai")
    ap.add_argument("salida")
    ap.add_argument("--pagina", type=int, default=13, help="mesa de trabajo (1-based)")
    ap.add_argument("--escala", type=float, default=6.0)
    ap.add_argument("--caja", nargs=4, type=float, default=[115, 165, 445, 400],
                    help="x0 y0 x1 y1 de la zona del logo, en unidades del .ai")
    a = ap.parse_args()

    doc = fitz.open(a.ai)
    pg = doc[a.pagina - 1]
    caja = fitz.Rect(*a.caja)

    dibujos = [d for d in pg.get_drawings() if d["rect"].intersects(caja)]
    if not dibujos:
        raise SystemExit("no hay vectores en esa caja")

    # lienzo nuevo, sólo con el logo
    w, h = caja.width, caja.height
    out = fitz.open()
    np_ = out.new_page(width=w, height=h)
    desp = fitz.Point(-caja.x0, -caja.y0)

    for d in dibujos:
        sh = np_.new_shape()
        for it in d["items"]:
            t = it[0]
            if t == "l":
                sh.draw_line(it[1] + desp, it[2] + desp)
            elif t == "c":
                sh.draw_bezier(it[1] + desp, it[2] + desp, it[3] + desp, it[4] + desp)
            elif t == "re":
                sh.draw_rect(it[1] + desp)
            elif t == "qu":
                sh.draw_quad(it[1] + desp)
        sh.finish(fill=d.get("fill"), color=d.get("color"),
                  width=d.get("width") or 0,
                  even_odd=d.get("even_odd", False),
                  closePath=d.get("closePath", True))
        sh.commit()

    pix = np_.get_pixmap(matrix=fitz.Matrix(a.escala, a.escala), alpha=True)
    pix.save(a.salida)
    print("escrito %s  %dx%d" % (a.salida, pix.width, pix.height))
    tintas = sorted({tuple(round(c, 3) for c in d["fill"]) for d in dibujos if d.get("fill")})
    for t in tintas:
        print("   tinta #%02X%02X%02X" % tuple(int(round(c * 255)) for c in t))


if __name__ == "__main__":
    main()

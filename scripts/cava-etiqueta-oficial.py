# -*- coding: utf-8 -*-
"""Devuelve la etiqueta OFICIAL a una botella que Magnific integró en la escena.

EL PROBLEMA. Magnific integra la botella de forma impecable —vidrio, sombra,
reflejo y luz de verdad— pero al redibujarla REDIBUJA LA ETIQUETA, y eso lo
prohíbe `clients/cava/marca.json`:

    botellas.prohibido: "editar, reescribir o regenerar una etiqueta
                         (año, cepa, valle, tipografía)"

Encajar el packshot entero encima no sirve: la botella generada asoma por detrás
porque nunca coincide del todo en ancho ni en inclinación (probado el 23-09).

LO QUE SÍ FUNCIONA es cambiar SOLO la etiqueta: se detecta la mancha clara de la
etiqueta generada, se recorta la etiqueta real del packshot, se rota al mismo
ángulo principal, se escala a esa mancha y se compone MULTIPLICANDO por el
sombreado local — así conserva la luz que la escena ya tenía y no queda como una
calcomanía plana.

    python3 scripts/cava-etiqueta-oficial.py escena.png salida.png
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

PACK = "public/assets/cava/bottles/2x/7colores-limited-carmenere.png"
ET = (0.141, 0.625, 0.416, 0.708)     # x0,x1,y0,y1 de la etiqueta en el packshot


def region_etiqueta(a, xmin=0.40):
    r, g, b = [a[:, :, i].astype(int) for i in range(3)]
    m = (r > 168) & (g > 152) & (b > 138) & (r - b < 70) & (r - b > -10)
    m[:, :int(a.shape[1] * xmin)] = False
    m = ndimage.binary_opening(m, np.ones((5, 5)))
    lab, k = ndimage.label(m)
    if not k:
        return None, None
    tam = ndimage.sum(m, lab, range(1, k + 1))
    i = int(np.argmax(tam)) + 1
    return (lab == i), tam[i - 1]


def angulo(mask):
    """Ángulo del eje mayor, para seguir la inclinación de la botella."""
    ys, xs = np.where(mask)
    ys = ys - ys.mean(); xs = xs - xs.mean()
    cov = np.cov(np.vstack([xs, ys]))
    w, v = np.linalg.eigh(cov)
    vy, vx = v[1, np.argmax(w)], v[0, np.argmax(w)]
    return np.degrees(np.arctan2(vx, vy))


def etiqueta_real():
    p = Image.open(PACK).convert("RGBA")
    p = p.crop(p.split()[-1].getbbox())
    W, H = p.size
    x0, x1, y0, y1 = ET
    return p.crop((int(W * x0), int(H * y0), int(W * x1), int(H * y1)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("escena"); ap.add_argument("salida")
    ap.add_argument("--xmin", type=float, default=0.40)
    ap.add_argument("--dilata", type=int, default=2)
    a = ap.parse_args()

    esc = Image.open(a.escena).convert("RGB")
    arr = np.array(esc)
    m, tam = region_etiqueta(arr, a.xmin)
    if m is None:
        raise SystemExit("no se encontró la etiqueta generada")
    ys, xs = np.where(m)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    ang = angulo(m)

    et = etiqueta_real()
    if abs(ang) > 1.5:
        et = et.rotate(-ang, expand=True, resample=Image.BICUBIC)
    et = et.resize((x1 - x0 + 1, y1 - y0 + 1), Image.LANCZOS)

    # el sombreado que la escena ya tenía sobre la etiqueta, normalizado
    gris = np.array(esc.convert("L")).astype(np.float32)
    zona = gris[y0:y1 + 1, x0:x1 + 1]
    suave = ndimage.gaussian_filter(zona, 9)
    mm = m[y0:y1 + 1, x0:x1 + 1]
    ref = np.median(suave[mm]) if mm.any() else suave.mean()
    sombreado = np.clip(suave / max(ref, 1e-3), 0.55, 1.35)[:, :, None]

    ea = np.array(et).astype(np.float32)
    ea[:, :, :3] = np.clip(ea[:, :, :3] * sombreado, 0, 255)

    # máscara: la región detectada, suavizada, para que el canto no se note
    mask = (mm * 255).astype(np.uint8)
    mask = np.array(Image.fromarray(mask).filter(ImageFilter.GaussianBlur(a.dilata)))
    alfa = (ea[:, :, 3] * (mask / 255.0)).astype(np.uint8)
    et2 = Image.fromarray(np.dstack([ea[:, :, :3].astype(np.uint8), alfa]))

    out = esc.convert("RGBA")
    out.alpha_composite(et2, (int(x0), int(y0)))
    out.convert("RGB").save(a.salida)
    print("  %s  etiqueta x=%d..%d y=%d..%d  ángulo %.1f°" % (a.salida, x0, x1, y0, y1, ang))


if __name__ == "__main__":
    main()

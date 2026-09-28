#!/usr/bin/env python3
"""MÁS CENTER — compara el render del sistema (pieza CTRL, textos de septiembre) contra el editable.

El .ai de septiembre se renderiza con PyMuPDF (trae la Gotham incrustada) y se mide, zona por zona,
la caja de la tinta del texto: blanco dentro de la pastilla, rojo de la bajada y blanco en la burbuja.
Tolerancia: ±3 px en vertical y ±1,5 % del ancho en horizontal (ver main()).

Uso: python scripts/mascenter-calibrar-gotham.py [carpeta_render]   (por defecto out/mascenter/2026-10/gotham)
Deja la comparación visual en out/_verificacion/mc/gotham-<formato>.png
"""
import sys
from pathlib import Path

import numpy as np
import pymupdf
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent
AI = Path("D:/DIEGO 2023/COPYWRITERS/MAS CENTER/SEPTIEMBRE IFB/PAID SEPT IFB/PAID SEPT IFB.ai")
REND = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "out/mascenter/2026-10/gotham"
VER = RAIZ / "out/_verificacion/mc"; VER.mkdir(parents=True, exist_ok=True)

# zonas (x0, y0, x1, y1) y qué tinta buscar en cada una
ZONAS = {
    "feed": {"mesa": 1, "png": "MASCENTER_CTRL_Feed_1080x1080.png",
             "titular": ((185, 572, 892, 685), "blanco"),
             "bajada": ((120, 705, 960, 800), "rojo"),
             "cta": ((172, 843, 646, 967), "blanco")},
    "story": {"mesa": 0, "png": "MASCENTER_CTRL_Story_1080x1920.png",
              "titular": ((172, 1003, 908, 1197), "blanco"),
              "bajada": ((100, 1240, 980, 1430), "rojo"),
              "cta": ((85, 1495, 615, 1632), "blanco")},
}


def caja(img, zona, tinta, radio=30):
    """Caja de la tinta. Los extremos en x se miden sólo en las filas centrales de la zona y los
    extremos en y sólo en las columnas centrales: así las esquinas redondeadas de la pastilla y la
    burbuja (donde asoma el fondo blanco) no cuentan como texto."""
    x0, y0, x1, y1 = zona
    a = np.asarray(img.convert("RGB"), dtype=int)[y0:y1, x0:x1]
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = (r > 200) & (g > 200) & (b > 200) if tinta == "blanco" else (r > 150) & (g < 90) & (b < 90)
    filas, cols = m[radio:-radio, :], m[:, radio:-radio]
    xs = np.where(filas.any(0))[0]; ys = np.where(cols.any(1))[0]
    if not len(xs) or not len(ys):
        return None
    return (x0 + xs.min(), y0 + ys.min(), x0 + xs.max(), y0 + ys.max()), int(m.sum())


def main():
    doc = pymupdf.open(AI)
    malo = 0
    for fmt, z in ZONAS.items():
        pg = doc[z["mesa"]]
        pix = pg.get_pixmap(matrix=pymupdf.Matrix(1, 1), alpha=False)
        ref = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        mia = Image.open(REND / z["png"]).convert("RGB")
        print(f"\n{fmt}  (editable {ref.size} · sistema {mia.size})")
        for nombre in ("titular", "bajada", "cta"):
            zona, tinta = z[nombre]
            cr, cm = caja(ref, zona, tinta), caja(mia, zona, tinta)
            if not cr or not cm:
                print(f"  {nombre:8s} sin tinta en alguna de las dos"); malo += 1; continue
            d = [int(cm[0][i] - cr[0][i]) for i in range(4)]
            # y: ±3 px (línea base y cuerpo). x: ±1,5 % del ancho de la línea (mín. 8 px), porque Diego
            # aprieta a mano algunas líneas en Illustrator (−10/1000 em: «TIENDAS Y BUENOS DATOS?»,
            # «aprovechar tu próxima visita.») y el sistema no copia tracking línea por línea.
            tol_x = max(8, 0.015 * (cr[0][2] - cr[0][0]))
            ok = abs(d[1]) <= 3 and abs(d[3]) <= 3 and abs(d[0]) <= tol_x and abs(d[2]) <= tol_x
            malo += not ok
            print(f"  {'✓' if ok else '✗'} {nombre:8s} editable {tuple(map(int, cr[0]))}  sistema {tuple(map(int, cm[0]))}  Δ(x0,y0,x1,y1)={d}  tinta {cm[1] / cr[1]:.2f}×")
        # comparación visual: editable arriba, sistema abajo, sólo la columna de texto
        y0 = ZONAS[fmt]["titular"][0][1] - 20; y1 = ZONAS[fmt]["cta"][0][3] + 20
        a, b = ref.crop((0, y0, ref.width, y1)), mia.crop((0, y0, mia.width, y1))
        lado = Image.new("RGB", (a.width, a.height * 2 + 10), "black")
        lado.paste(a, (0, 0)); lado.paste(b, (0, a.height + 10))
        lado.save(VER / f"gotham-{fmt}.png")
    print("\n" + ("✓ calibrado" if not malo else f"✗ {malo} zona(s) fuera de tolerancia"))
    sys.exit(1 if malo else 0)


if __name__ == "__main__":
    main()

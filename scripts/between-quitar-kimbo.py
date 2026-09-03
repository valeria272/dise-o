#!/usr/bin/env python3
"""Borra el logotipo KIMBO de las tazas de loza de Between.

⭐ 03-09-2026 · RONDA 9. El cliente lleva desde la ronda 4 repitiendo lo mismo:

    «Ese kimbo en la G1 hay que quitarlo, porque ya no servimos en esas tazas»
    «recordemos que la taza de Kimbo ya no se puede usar»   (Scarlette, 31-08)

El problema es de MATERIAL, no de diseño: **las tazas de la sesión de platos del
cliente traen el logotipo KIMBO impreso al costado** —wordmark rojo vertical más
una barra gris debajo—. Sale en toda toma lateral o en 45°.

Hay tres salidas y ésta es la tercera:

  1. **Elegir tomas CENITALES**, donde el logotipo queda en la pared exterior de
     la taza y la cámara no lo ve. Es la salida preferida y la que usan las
     slides 1 y 2 del carrusel FEED H. **Cuando exista una cenital, va esa.**
  2. Recortar la taza fuera del encuadre. Sirve, pero en 4:5 suele dejar el
     plato ahogado contra el borde: pasó en la slide 3, donde sin la taza el
     croissant quedaba pegado al canto superior.
  3. **Borrar la marca**, que es lo que hace este script — y sólo cuando 1 y 2
     no dan.

⭐ CÓMO se borra, y por qué NO se clona. El primer intento clonaba una franja de
esmalte vecina a la misma altura. Falla, y se ve: **la taza tiene un degradado
lateral**, así que la franja traída de 150 px a la derecha llega con otra
luminancia y deja un RECTÁNGULO visible — el parche se nota más que la marca.

Lo que sí funciona: **interpolar horizontalmente**. Para cada fila se toma el
color a la izquierda y a la derecha de la caja —promediando unas columnas
limpias a cada lado— y se rellena con la recta que los une. En estas tomas la
taza está fuera de foco y su superficie es un degradado suave, así que la recta
ES la superficie: no queda empalme porque no hay dos texturas que empalmar.
Después, un difuminado proporcional al ancho de la marca funde los cantos.

⛔ Lo que este script NO hace: inventar una taza, ni estampar el logotipo de
Between encima. La taza es real y de Between; lo único que sale es la marca del
proveedor de café que el cliente ya no usa.

Uso:
    python scripts/between-quitar-kimbo.py Between-42.jpg
    python scripts/between-quitar-kimbo.py --todas
    python scripts/between-quitar-kimbo.py Between-42.jpg --revisar   # sólo mide
"""
import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = RAIZ / "raw/hilton/between/platos-ene"

#: Caja del logotipo por foto (x0, y0, x1, y1), medida a mano sobre el original
#: con una rejilla. Generosa a propósito: mejor sobrar esmalte liso que dejar
#: asomando un trozo del wordmark rojo.
MARCAS = {
    "Between-42.jpg": {"caja": (286, 650, 362, 1005)},
}


def borrar(nombre, caja, apoyo=14, sufijo="-sinkimbo"):
    """Rellena la caja interpolando entre el esmalte limpio de sus dos costados.

    `apoyo` = cuántas columnas limpias se promedian a cada lado para tomar el
    color de referencia. Unas pocas bastan y absorben el ruido del sensor."""
    import numpy as np
    from PIL import Image, ImageFilter
    Image.MAX_IMAGE_PIXELS = None
    src = ORIGEN / nombre
    if not src.is_file():
        sys.exit(f"✗ Falta {src}")
    im = Image.open(src).convert("RGB")
    x0, y0, x1, y1 = caja
    if not (apoyo <= x0 and x1 + apoyo <= im.width and 0 <= y0 and y1 <= im.height):
        sys.exit(f"✗ {nombre}: la caja no deja {apoyo} px de apoyo a los lados.")

    a = np.asarray(im).astype(np.float32)
    izq = a[y0:y1, x0 - apoyo:x0].mean(axis=1)          # (alto, 3)
    der = a[y0:y1, x1:x1 + apoyo].mean(axis=1)
    ancho = x1 - x0
    t = np.linspace(0.0, 1.0, ancho, dtype=np.float32)[None, :, None]
    a[y0:y1, x0:x1] = izq[:, None, :] * (1 - t) + der[:, None, :] * t

    relleno = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

    # Los cantos: se funden con un difuminado proporcional al ancho de la marca.
    # ⚠️ Proporcional y NUNCA fijo — un inset fijo se come el borde cuando la
    # marca es chica; es la trampa que costó dos pasadas en
    # `between-relogo-ronda5.py`.
    m = max(6, int(0.30 * ancho))
    zx0, zy0 = max(0, x0 - m), max(0, y0 - m)
    zx1, zy1 = min(im.width, x1 + m), min(im.height, y1 + m)
    zona = relleno.crop((zx0, zy0, zx1, zy1))
    suave = zona.filter(ImageFilter.GaussianBlur(m / 3.0))
    from PIL import ImageDraw
    mask = Image.new("L", zona.size, 0)
    ImageDraw.Draw(mask).rectangle([m, m, mask.width - m, mask.height - m], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(m / 2.0))
    zona = Image.composite(suave, zona, mask)
    relleno.paste(zona, (zx0, zy0))

    dst = ORIGEN / (Path(nombre).stem + sufijo + ".jpg")
    relleno.save(dst, quality=97)
    print(f"· {nombre} → {dst.name}   caja {caja}  apoyo={apoyo}  difuminado={m}")
    return dst


def revisar(nombre, caja):
    """Recorta la zona a 3× para mirarla con zoom antes y después."""
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    x0, y0, x1, y1 = caja
    m = 160
    for etq, f in (("antes", ORIGEN / nombre),
                   ("despues", ORIGEN / (Path(nombre).stem + "-sinkimbo.jpg"))):
        if not f.is_file():
            continue
        z = Image.open(f).convert("RGB").crop((x0 - m, y0 - m, x1 + m, y1 + m))
        z = z.resize((z.width * 3, z.height * 3), Image.LANCZOS)
        out = ORIGEN / f"_qa-{Path(nombre).stem}-{etq}.jpg"
        z.save(out, quality=94)
        print(f"  {etq}: {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fotos", nargs="*", help="nombres de MARCAS")
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--revisar", action="store_true",
                    help="además guarda recortes a 3× para mirar el empalme")
    a = ap.parse_args()
    cuales = list(MARCAS) if a.todas else (a.fotos or sys.exit(ap.format_help()))
    for n in cuales:
        if n not in MARCAS:
            sys.exit(f"✗ {n} no está medido en MARCAS. Mídelo con una rejilla primero.")
        borrar(n, **MARCAS[n])
        if a.revisar:
            revisar(n, MARCAS[n]["caja"])


if __name__ == "__main__":
    main()

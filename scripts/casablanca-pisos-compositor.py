"""Casablanca C1 (ronda 2) — instala el piso REAL de cada producto en el ambiente base.

Por qué existe
--------------
En la ronda 1 el ambiente lo inventaba la IA y la muestra de la tarjeta venía de
otra parte: el recuadro mostraba un roble cálido y el suelo, otra madera (en
Cumarú, muestra café rojizo sobre piso miel). Para una marca de pisos ese es el
error más caro que hay — el cliente compra lo que ve.

Acá la madera NO se inventa. Sale de la foto oficial del producto en
pisoscasablanca.cl (`raw/casablanca/productos/`), se arma un plano de piso
cenital respetando el ancho y el largo reales de la tabla en mm, se proyecta en
perspectiva sobre el piso vacío de `amb_base_vacio.jpg` y se le devuelve la luz
y las sombras del ambiente original. La muestra vertical de la tarjeta se
recorta de la MISMA textura, así que muestra y suelo son el mismo piso por
construcción.

Además resuelve la regla nº1 del brief al derecho: el ambiente es idéntico en
las cuatro tarjetas y lo que cambia es la tabla — y cambia de verdad, porque
190 × 1900 y Cumaru (120 de ancho, largo variable y corto) dan densidades de
junta distintas y se ven distintas.

Salida:
  public/assets/casablanca/amb_<sku>.jpg    ambiente con el piso instalado
  public/assets/casablanca/tabla_<sku>.png  muestra vertical de la misma textura
"""
import os
import pathlib
import random
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ

RAIZ = pathlib.Path(str(_RAIZ))
FUENTE = RAIZ / "raw/casablanca/productos"
DEST = RAIZ / "public/assets/casablanca"
BASE = DEST / "amb_base_vacio.jpg"

# --- Geometría del ambiente base (medida sobre amb_base_vacio.jpg, 1792×2368) ---
Y_HORIZONTE = 1310       # donde el muro del fondo toca el piso
EXTENSION = 1600         # cuánto se abre el piso más allá del cuadro en primer plano
FEATHER = 46             # fundido en la unión con el fondo
# Lo que toca el suelo y no se puede pisar: macetero de mimbre de la derecha.
# La mesa y las sillas terminan en y≈1300, sobre Y_HORIZONTE, así que no estorban.
EXCLUIR = [(1462, 1300, 1728, 1392)]

ANCHO_AMBIENTE_MM = 5500
PROFUNDIDAD_MM = 7000
PX_POR_MM = 0.62

# --- Los cuatro SKU autorizados del brief de septiembre ---
PRODUCTOS = {
    "natural_uv_grande": {"foto": "roble-natural-143x190x1900.jpg", "ancho": 190, "largo": 1900},
    "natural_uv_chico":  {"foto": "roble-natural-uv-formato-chico.jpg", "ancho": 167, "largo": 1200},
    "aserrado":          {"foto": "roble-aserrado.jpg", "ancho": 190, "largo": 1900},
    # `largo` como (min, max) = LARGO VARIABLE: la ficha del cliente dice «2.130 LV»
    # y el LV es variable, con el 2130 de tope. La clienta precisó el 16-09-2026 que
    # en la práctica va bajo 1,30 m. `plano_cenital` sortea el largo tabla por tabla.
    "cumaru":            {"foto": "cumaru.jpg", "ancho": 120, "largo": (600, 1300)},
}


def coeffs(dst, src):
    """Coeficientes PERSPECTIVE de PIL: mapea los puntos de destino a los de origen."""
    import numpy as np

    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    A = np.matrix(m, dtype=float)
    B = np.array(src).reshape(8)
    return np.array(np.dot(np.linalg.inv(A.T * A) * A.T, B)).reshape(8)


def franjas(foto, n=6):
    """Saca n franjas horizontales de la foto de producto, para variar la veta.

    Las franjas se igualan en luminancia entre sí: la foto de producto tiene
    tablas más claras y más oscuras, y si se pegan tal cual el piso queda con
    parches de exposición que se leen como manchas y no como madera. La
    variación de VETA se conserva; la de LUZ la pone después el ambiente.
    """
    import numpy as np

    im = Image.open(FUENTE / foto).convert("RGB")
    w, h = im.size
    alto = h // (n + 1)
    crudas = [im.crop((0, i * alto, w, i * alto + alto)) for i in range(n)]
    medias = [float(np.asarray(c.convert("L"), dtype=float).mean()) for c in crudas]
    objetivo = sum(medias) / len(medias)
    out = []
    for c, m in zip(crudas, medias):
        a = np.asarray(c, dtype=float) * (objetivo / max(1.0, m))
        out.append(Image.fromarray(np.clip(a, 0, 255).astype("uint8")))
    return out


def plano_cenital(sku):
    """Arma el piso visto desde arriba, con el ancho y el largo reales de la tabla."""
    d = PRODUCTOS[sku]
    W = int(ANCHO_AMBIENTE_MM * PX_POR_MM)
    H = int(PROFUNDIDAD_MM * PX_POR_MM)
    tw = max(8, int(d["ancho"] * PX_POR_MM))
    # `largo` puede ser un número (tabla de largo fijo) o un par (min, max) = LARGO
    # VARIABLE, que es como viene el Cumaru. En ese caso el largo NO se sortea una vez
    # por piso sino una vez POR TABLA: un piso de largo variable se reconoce justamente
    # porque las juntas de tope caen a distinta altura y no forman un patrón.
    lv = isinstance(d["largo"], (tuple, list))
    th_max = max(8, int((d["largo"][1] if lv else d["largo"]) * PX_POR_MM))
    piezas = franjas(d["foto"])
    plano = Image.new("RGB", (W, H))
    rnd = random.Random(hash(sku) & 0xFFFF)
    for cx in range(0, W, tw):
        offset = rnd.randrange(0, th_max)  # traba entre columnas, como se instala de verdad
        y = -offset
        while y < H:
            th = max(8, int(rnd.uniform(*d["largo"]) * PX_POR_MM)) if lv else th_max
            src = rnd.choice(piezas)
            tabla = src.resize((tw, th))
            if rnd.random() < 0.5:
                tabla = tabla.transpose(Image.FLIP_TOP_BOTTOM)
            plano.paste(tabla, (cx, y))
            # junta entre tablas
            dr = ImageDraw.Draw(plano)
            dr.line([(cx, y), (cx, min(y + th, H))], fill=(120, 100, 78), width=1)
            dr.line([(cx, y), (min(cx + tw, W), y)], fill=(126, 106, 84), width=1)
            y += th
    return plano


def luz_del_ambiente(base, y0):
    """Extrae luces y sombras del piso original para devolvérselas al piso nuevo."""
    piso = base.crop((0, y0, base.width, base.height)).convert("L")
    piso = piso.filter(ImageFilter.GaussianBlur(26))
    import numpy as np

    a = np.asarray(piso, dtype=float)
    a = a / max(1.0, float(np.median(a)))
    a = np.clip(a, 0.62, 1.45)
    return Image.fromarray((np.clip(a * 128, 0, 255)).astype("uint8"))


def instala(sku, base, luz):
    W, H = base.size
    plano = plano_cenital(sku)
    dst = [(-EXTENSION, H), (W + EXTENSION, H), (W, Y_HORIZONTE), (0, Y_HORIZONTE)]
    src = [(0, plano.height), (plano.width, plano.height), (plano.width, 0), (0, 0)]
    proy = plano.transform((W, H), Image.PERSPECTIVE, coeffs(dst, src), Image.BICUBIC)

    import numpy as np

    trozo = np.asarray(proy.crop((0, Y_HORIZONTE, W, H)), dtype=float)
    factor = np.asarray(luz, dtype=float)[:, :, None] / 128.0
    trozo = np.clip(trozo * factor, 0, 255).astype("uint8")
    piso = Image.fromarray(trozo)

    mask = Image.new("L", piso.size, 255)
    dr = ImageDraw.Draw(mask)
    dr.rectangle([0, 0, piso.width, FEATHER], fill=0)  # se funde con el fondo
    for x0, y0, x1, y1 in EXCLUIR:
        dr.rectangle([x0, y0 - Y_HORIZONTE, x1, y1 - Y_HORIZONTE], fill=0)
    mask = mask.filter(ImageFilter.GaussianBlur(18))

    out = base.copy()
    out.paste(piso, (0, Y_HORIZONTE), mask)
    return out


def muestra(sku):
    """Muestra vertical de la tarjeta — de la MISMA foto que el piso instalado.

    Paulina la llama «el cuadro que muestra a detalle el producto», y ahí está la
    clave: es un DETALLE, no una miniatura del piso. En la ronda 1 la muestra
    salía a la misma escala que el suelo y se camuflaba — el recuadro se leía como
    un marco blanco vacío. Acá se amplía ~2,4× y se gira para que la veta corra
    vertical, que es como la muestra la diseñadora.
    """
    d = PRODUCTOS[sku]
    w, h = 460, 1450
    im = Image.open(FUENTE / d["foto"]).convert("RGB")
    # La veta de la foto de producto corre horizontal: se gira para la muestra.
    im = im.transpose(Image.ROTATE_90)
    zoom = 2.4
    escala = max(w / im.width, h / im.height) * zoom
    im = im.resize((int(im.width * escala), int(im.height * escala)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def main():
    if not BASE.exists():
        sys.exit(f"Falta {BASE} — corre antes scripts/casablanca-ambiente-base.py")
    base = Image.open(BASE).convert("RGB")
    luz = luz_del_ambiente(base, Y_HORIZONTE)
    for sku in PRODUCTOS:
        amb = instala(sku, base, luz)
        p = DEST / f"amb_{sku}.jpg"
        amb.save(p, quality=93)
        m = muestra(sku)
        q = DEST / f"tabla_{sku}.png"
        m.save(q)
        print(f"  {p.name} ({p.stat().st_size // 1024} KB) · {q.name}")
    print(f"\nListo en {DEST}")


if __name__ == "__main__":
    main()

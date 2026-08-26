"""Casablanca — QA de tono: ¿el piso del ambiente es el producto que decimos?

**El problema que resuelve.** Mystic entrega la fotografía de interiorismo, pero
inventa el color de la madera: el primer render de Roble Natural UV salió con
ΔE 18 contra la foto real (más gris, menos miel). Y el error más caro de esta
marca es justamente ese — *"el cliente compra lo que ve"*.

**Este script MIDE, no corrige.** Se probaron las dos correcciones automáticas y
las dos empeoraron la foto:
  · **Nano Banana** (recoloreo por IA) devuelve 1024×1024: aplasta el 4:5 y bota
    resolución.
  · **Gradación en Lab** contra la media de la foto de producto: deja el piso
    naranja —justo lo que el cliente vetó— y mancha las cortinas en el borde de
    la máscara. La foto de producto es un plano de estudio con luz plana; su
    media no es el objetivo correcto para un piso iluminado por ventana.

El color de la madera se controla **en el prompt** de
`casablanca-ambientes-editorial.py`. Acá sólo se verifica que el ambiente no
muestre un producto distinto del que dice la pieza (el error caro de la ronda 1:
muestra café rojizo sobre piso miel). Umbral: ΔE ≥ 20 es otro producto.

La corrección quedó disponible con `--corregir`, a media fuerza y con máscara
estricta, para casos puntuales — pero hay que mirar el resultado, no confiar en
el número.

Uso:
    python3 scripts/casablanca-tono.py --todos                # QA de los 4 SKU
    python3 scripts/casablanca-tono.py <escena> <producto>     # QA de una
    python3 scripts/casablanca-tono.py <escena> <producto> --corregir
"""
import pathlib
import sys

import numpy as np
from PIL import Image, ImageFilter

RAIZ = pathlib.Path(__file__).resolve().parent.parent
EDITORIAL = RAIZ / "public/assets/casablanca/editorial"
PRODUCTOS = RAIZ / "raw/casablanca/productos"

SKUS = {
    "natural_uv_grande": "roble-natural-143x190x1900.jpg",
    "natural_uv_chico": "roble-natural-uv-formato-chico.jpg",
    "aserrado": "roble-aserrado.jpg",
    "cumaru": "cumaru.jpg",
}


# ── Conversión RGB ↔ Lab (D65). Se hace a mano para no depender de skimage.
def _srgb_a_lin(a):
    return np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)


def _lin_a_srgb(a):
    return np.where(a <= 0.0031308, a * 12.92, 1.055 * np.clip(a, 0, None) ** (1 / 2.4) - 0.055)


M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
BLANCO = np.array([0.95047, 1.0, 1.08883])


def rgb2lab(rgb):
    # OJO: numpy 2.2 en macOS (Accelerate) revienta con matmul de un array 3D
    # contra una 3×3 — segfault, sin excepción. Se aplana a (N,3) siempre.
    forma = rgb.shape
    lin = _srgb_a_lin(rgb.astype(np.float64).reshape(-1, 3) / 255)
    xyz = (lin.dot(M.T) / BLANCO).reshape(forma)
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def lab2rgb(lab):
    fy = (lab[..., 0] + 16) / 116
    fx = fy + lab[..., 1] / 500
    fz = fy - lab[..., 2] / 200
    f = np.stack([fx, fy, fz], -1)
    xyz = np.where(f ** 3 > 0.008856, f ** 3, (f - 16 / 116) / 7.787) * BLANCO
    forma = xyz.shape
    lin = xyz.reshape(-1, 3).dot(np.linalg.inv(M).T).reshape(forma)
    return np.clip(_lin_a_srgb(lin) * 255, 0, 255).astype(np.uint8)


def mascara_piso(rgb, desde=0.55):
    """Píxeles de MADERA del piso, con máscara ESTRICTA.

    Excluye alfombras, muros y muebles por cromaticidad: la madera tiene b* alto
    (amarillo-rojo) y luminosidad media; un textil greige tiene b* bajo.

    ⚠️ La primera versión difuminaba la máscara con un gaussiano de 9 px y el
    desplazamiento se escapaba hacia las cortinas: quedaron manchones naranjos
    sobre la tela. Ahora el suavizado se multiplica por la máscara dura, así el
    ajuste NUNCA sale del piso.
    """
    h, w, _ = rgb.shape
    lab = rgb2lab(rgb)
    L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
    m = (b > 12) & (a > 0) & (L > 25) & (L < 88)
    zona = np.zeros((h, w), bool)
    zona[int(h * desde):, :] = True
    return m & zona


def calza(escena, producto, salida=None, verbose=True):
    im = Image.open(escena).convert("RGB")
    rgb = np.asarray(im)
    objetivo = rgb2lab(np.asarray(Image.open(producto).convert("RGB"))).reshape(-1, 3).mean(0)

    msk = mascara_piso(rgb)
    if msk.sum() < rgb.shape[0] * rgb.shape[1] * 0.02:
        print(f"  ⚠️  máscara de piso muy chica ({msk.mean()*100:.1f} %) — revisar a ojo")
    lab = rgb2lab(rgb)
    actual = lab[msk].mean(0)
    antes = float(np.linalg.norm(actual - objetivo))

    # Desplazamiento PARCIAL en Lab. La foto de producto es un plano de estudio
    # con luz plana; calzar su media al 100 % sobre un piso iluminado por ventana
    # deja la madera naranja fosforescente — que es justo lo que el cliente vetó.
    # Se corrige el 55 % del croma y el 25 % de la luminosidad, y se topa el b*
    # para que la madera nunca quede MÁS saturada que el producto real.
    delta = objetivo - actual
    peso = np.asarray(
        Image.fromarray((msk * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))
    ).astype(np.float64) / 255
    peso = peso * msk            # el suavizado nunca sale de la máscara dura
    lab_out = lab.copy()
    lab_out[..., 0] = lab[..., 0] + peso * delta[0] * 0.25
    lab_out[..., 1] = lab[..., 1] + peso * delta[1] * 0.55
    lab_out[..., 2] = lab[..., 2] + peso * delta[2] * 0.55
    tope = objetivo[2] + 4
    lab_out[..., 2] = np.where(msk, np.minimum(lab_out[..., 2], tope), lab_out[..., 2])

    out = lab2rgb(lab_out)
    despues = float(np.linalg.norm(rgb2lab(out)[msk].mean(0) - objetivo))
    salida = pathlib.Path(salida or escena)
    Image.fromarray(out).save(salida, quality=95)
    if verbose:
        print(f"  {pathlib.Path(escena).name}: ΔE {antes:.1f} → {despues:.1f}  "
              f"({'OK' if despues < 10 else 'sigue fuera'})  máscara {msk.mean()*100:.0f} %")
    return despues


UMBRAL = 20.0   # ΔE por encima de esto = el ambiente muestra OTRO producto


def mide(escena, producto):
    rgb = np.asarray(Image.open(escena).convert("RGB"))
    objetivo = rgb2lab(np.asarray(Image.open(producto).convert("RGB"))).reshape(-1, 3).mean(0)
    msk = mascara_piso(rgb)
    if msk.sum() < rgb.shape[0] * rgb.shape[1] * 0.02:
        print(f"  ⚠️  {pathlib.Path(escena).name}: máscara de piso muy chica "
              f"({msk.mean()*100:.1f} %) — revisar a ojo")
        return None
    d = float(np.linalg.norm(rgb2lab(rgb)[msk].mean(0) - objetivo))
    estado = "OK" if d < UMBRAL else "⛔ OTRO PRODUCTO"
    print(f"  {pathlib.Path(escena).name:44s} ΔE {d:5.1f}  {estado}")
    return d


def main():
    corregir = "--corregir" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--todos" in sys.argv:
        for sku, prod in SKUS.items():
            for fmt in ("feed", "story"):
                p = EDITORIAL / f"amb_{sku}_{fmt}.jpg"
                if p.exists():
                    (calza if corregir else mide)(p, PRODUCTOS / prod)
        return
    if len(args) < 2:
        sys.exit(__doc__)
    if corregir:
        calza(args[0], args[1], args[2] if len(args) > 2 else None)
    else:
        mide(args[0], args[1])


if __name__ == "__main__":
    main()

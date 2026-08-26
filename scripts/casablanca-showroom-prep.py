"""Casablanca C2 — deja las tres fotos del showroom con la MISMA luz.

Lineamiento nº2 del brief para la pieza del showroom, textual: *"MISMA
TEMPERATURA DE COLOR en las tres tarjetas. Las fotos de local suelen venir con
luces mezcladas (led frío, ampolleta cálida, luz de ventana): corregir a una luz
cálida neutra antes de montar."*

Qué hace: balance de blancos por mundo-gris sobre los píxeles claros y neutros
de cada foto —que es donde vive la dominante— y después un sesgo cálido común y
suave para las tres. Imprime el R/B de cada una antes y después, así el "misma
temperatura" es un número y no una impresión.
"""
import pathlib
import sys

import numpy as np
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "public/assets/casablanca"
DEST = RAIZ / "public/assets/casablanca/sep"

# Qué foto va en cada tarjeta, según lo que describe el brief.
FOTOS = {
    "sr_interior": "sr_interior_limpio.jpg",   # 1 · vista general del espacio
    "sr_muestras": "sr_exhibidores.jpg",       # 2 · la zona donde se compara
    "sr_local": "sr_fachada.jpg",              # 3 · cierre, vista del local (feed)
    # La fachada es apaisada (1,27): en 9:16 el letrero del local queda partido.
    # Para la story del cierre se usa la foto VERTICAL del acceso con el número.
    "sr_local_v": "sr_direccion.jpg",
}
# Sesgo cálido común: un pelo más de rojo que de azul. Neutro sería 1,00.
CALIDO = 1.045
# Luminancia media a la que se llevan las tres. Sin esto, la foto de los
# muestrarios (76/255) entra mucho más oscura que la de la fachada (164/255) y
# el carrusel se ve parchado al deslizar.
LUZ_OBJETIVO = 132.0


def rb(a):
    return float(a[..., 0].mean() / max(a[..., 2].mean(), 1e-6))


def corrige(a):
    """Mundo-gris sobre los claros neutros + sesgo cálido común."""
    f = a.astype(np.float64)
    lum = f.mean(axis=2)
    croma = f.max(axis=2) - f.min(axis=2)
    # Claros y poco saturados: muros, cielo, luz. Ahí se lee la dominante.
    m = (lum > np.percentile(lum, 70)) & (croma < 42)
    if m.sum() < lum.size * 0.01:
        m = lum > np.percentile(lum, 85)
    medio = f[m].mean(axis=0)
    gan = medio.mean() / np.maximum(medio, 1e-6)
    gan[0] *= CALIDO ** 0.5
    gan[2] /= CALIDO ** 0.5
    f = np.clip(f * gan, 0, 255)

    # Exposición pareja, por gamma: sube las medias sin quemar los blancos.
    media = f.mean()
    if media > 1:
        gamma = np.log(LUZ_OBJETIVO / 255) / np.log(max(media, 1) / 255)
        gamma = float(np.clip(gamma, 0.55, 1.8))
        f = 255 * (f / 255) ** gamma
    return np.clip(f, 0, 255).astype(np.uint8)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    print("foto                      R/B antes → después    ·    luz antes → después")
    for nombre, archivo in FOTOS.items():
        src = ORIGEN / archivo
        if not src.exists():
            print(f"  ! falta {archivo}")
            continue
        a = np.asarray(Image.open(src).convert("RGB"))
        out = corrige(a)
        Image.fromarray(out).save(DEST / f"{nombre}.jpg", quality=95)
        print(f"  {nombre:14s} ({archivo:22s})  {rb(a):.3f} → {rb(out):.3f}"
              f"    ·    {a.mean():.0f} → {out.mean():.0f}")
    print("\nSi los tres 'después' no quedan dentro de ±0,03, revisar a ojo.")


if __name__ == "__main__":
    main()

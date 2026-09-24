#!/usr/bin/env python3
"""Prepara los frascos de la prueba Biotop 700 + 911 de Selfie, uno por formato.

    ~/copylab-venv/bin/python3 scripts/selfie-biotop-productos.py

POR QUÉ EXISTE (24-09-2026). Coni: «el cliente siempre reclama que los productos se
ven pixelados». Tres causas, las tres corregidas acá:
  1. El recorte de remove-bg sale en PNG DE PALETA (256 colores). Se usa sólo su
     máscara; el color sale de la foto original del e-commerce, a 24 bits.
  2. Chrome estiraba y giraba el frasco con su propio remuestreo. Acá se deja al
     alto EXACTO en píxeles de cada formato (Lanczos, alfa premultiplicado para que
     no haya halo) y ya girado: la composición lo pone 1:1.
  3. ⛔ NO se usa el Upscaler Precision de Magnific: probado el 24-09 sobre estos dos
     packshots, reescribió la etiqueta («65 ml» → «66 ml», «HYDRATING» → «RYDRATING»).
     Un producto con la etiqueta inventada es peor que uno blando.

La fuente es de 1000 px (el máximo que publica selfie.cl y el que dejó Coni). En post
e historia el frasco queda ~1,5× sobre la fuente: si el cliente pide más nitidez, lo
que hace falta es un packshot más grande de Biotop, no más IA.
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "raw/selfie/prueba-biotop"
DEST = RAIZ / "public/assets/selfie/2026-nuevo-estilo/biotop"
LAYOUT = json.loads((RAIZ / "src/compositions/selfie/biotop-prueba.json").read_text())

PRODUCTOS = {
    "700": "BP_700_Keratin_Kale_Serum",
    "911": "BP_911Quinoa_Serum",
}


def recorte(base: str) -> Image.Image:
    """Color de la foto original + alfa del recorte, sin el reflejo bajo la base."""
    rgb = np.array(Image.open(FUENTE / f"{base}.webp").convert("RGB"))
    alfa = np.array(Image.open(FUENTE / f"{base}-nobg.png").convert("RGBA"))[:, :, 3].copy()
    anchos = (alfa > 200).sum(1)
    base_y = np.where(anchos > 0.6 * anchos.max())[0].max()
    alfa[base_y + 2:, :] = 0
    im = Image.fromarray(np.dstack([rgb, alfa]), "RGBA")
    caja = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    return im.crop(caja)


def prepara(im: Image.Image, alto_px: int, giro: float) -> Image.Image:
    escala = alto_px / im.height
    pm = im.convert("RGBa")  # premultiplicado: sin halo claro en el borde
    pm = pm.resize((round(im.width * escala), alto_px), Image.LANCZOS)
    rgb = pm.convert("RGBA")
    # enfoque suave, más fuerte cuando se agranda
    fuerza = 70 if escala > 1.05 else 35
    nitido = rgb.filter(ImageFilter.UnsharpMask(radius=1.4 if escala > 1.05 else 0.8, percent=fuerza, threshold=2))
    nitido.putalpha(rgb.getchannel("A"))
    # CSS rotate(+) es horario; PIL rotate(+) es antihorario
    girado = nitido.convert("RGBa").rotate(-giro, resample=Image.BICUBIC, expand=True)
    return girado.convert("RGBA")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    fuentes = {k: recorte(v) for k, v in PRODUCTOS.items()}
    for fmt, L in LAYOUT.items():
        if fmt.startswith("_"):
            continue
        u = L["outW"] / L["mesaW"]
        for k, im in fuentes.items():
            p = L[f"p{k}"]
            alto = round(p["h"] * u)
            out = prepara(im, alto, p["rot"])
            ruta = DEST / f"{fmt}-{k}.png"
            out.save(ruta, optimize=True)
            print(f"{fmt:12} {k}  frasco {alto:4d} px  ({alto / im.height:.2f}× la fuente)  → {ruta.name} {out.size}")


if __name__ == "__main__":
    main()

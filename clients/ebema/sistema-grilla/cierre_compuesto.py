#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · la lámina de cierre — bodega generada + packshot REAL encima.

⛔ POR QUÉ NO SE GENERA ENTERA CON IA. El lineamiento de Paulina (23-09-2026) para
toda lámina final es: «una bodega de materiales en el fondo y el producto original
en el centro, siempre la imagen total con desenfoque para que el texto destaque».
El **producto original** es un packshot de marca —el saco lleva la marca impresa—
y §5 del manual lo deja fuera de la IA: se falsificaría la etiqueta del proveedor.

Así que se hace en dos tiempos:
  1. `generar_fotos.py` produce SÓLO la bodega (`05_bodega`), con el centro libre.
  2. este script pega encima el PNG oficial del proveedor, con su sombra, y suaviza
     el conjunto. La etiqueta nunca pasa por el modelo.

Uso:  python cierre_compuesto.py sanjuan
"""
import os
import sys

from PIL import Image, ImageFilter

for _f in (sys.stdout, sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))
ANCHO, ALTO = 2400, 3000          # 4:5, el mismo lienzo de las otras fotos del lote

# ⭐ EL PRODUCTO SE ENCAJA EN UNA BANDA, no se escala por ancho.
# Escalar por ancho no sirve porque los packshots tienen proporciones muy distintas:
# el saco de San Juan es apaisado (1024×761) y el de CBB casi cuadrado (584×565).
# Con un ancho fijo, el cuadrado se iba de alto, se comía la bajada de arriba y el
# botón de abajo. Ahora se encaja en la banda libre que dejan los dos textos:
#   la bajada del cierre termina hacia el 33 % del alto
#   el botón de WhatsApp empieza en el 68 %
# El anillo EBEMA (303,7 de ancho, y 502-812 sobre 1080) queda encima de la zona
# media del producto, así que la banda se elige para que se vean su parte de arriba
# y la franja de la marca de abajo.
BANDA_Y   = (0.345, 0.655)        # arriba y abajo, en fracción del alto
ANCHO_MAX = 0.62                  # tope de ancho, en fracción del ancho

DESENFOQUE_FONDO    = 7.0         # la bodega ya viene suave; esto la asienta
DESENFOQUE_CONJUNTO = 1.6         # «la imagen total con desenfoque»


def componer(tema):
    fondo_p = os.path.join(AQUI, "fotos", tema, "05_bodega.jpg")
    pack_p = os.path.join(AQUI, "packshots", f"{tema}_saco.png")
    salida = os.path.join(AQUI, "fotos", tema, "05.jpg")
    for p in (fondo_p, pack_p):
        if not os.path.exists(p):
            sys.exit(f"falta {p}")

    fondo = Image.open(fondo_p).convert("RGB")
    # cubrir el lienzo sin deformar
    e = max(ANCHO / fondo.width, ALTO / fondo.height)
    fondo = fondo.resize((round(fondo.width * e), round(fondo.height * e)), Image.LANCZOS)
    x = (fondo.width - ANCHO) // 2
    y = (fondo.height - ALTO) // 2
    fondo = fondo.crop((x, y, x + ANCHO, y + ALTO))
    fondo = fondo.filter(ImageFilter.GaussianBlur(DESENFOQUE_FONDO))

    pack = Image.open(pack_p).convert("RGBA")
    alto_banda = round(ALTO * (BANDA_Y[1] - BANDA_Y[0]))
    e2 = min(alto_banda / pack.height, (ANCHO * ANCHO_MAX) / pack.width)
    w = round(pack.width * e2)
    h = round(pack.height * e2)
    pack = pack.resize((w, h), Image.LANCZOS)

    px = (ANCHO - w) // 2
    py = round(ALTO * BANDA_Y[0]) + (alto_banda - h) // 2

    # Sombra: la silueta del propio packshot, desplazada y muy difusa. Sin ella el
    # saco se ve pegado, que es justo lo que Paulina llama «se ve falsa».
    sombra = Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 0))
    silueta = Image.new("RGBA", pack.size, (0, 0, 0, 120))
    silueta.putalpha(pack.getchannel("A").point(lambda a: int(a * 0.47)))
    sombra.paste(silueta, (px + round(w * 0.035), py + round(h * 0.055)), silueta)
    sombra = sombra.filter(ImageFilter.GaussianBlur(38))

    lienzo = fondo.convert("RGBA")
    lienzo.alpha_composite(sombra)
    lienzo.alpha_composite(pack, (px, py))
    final = lienzo.convert("RGB").filter(ImageFilter.GaussianBlur(DESENFOQUE_CONJUNTO))
    final.save(salida, quality=92, subsampling=0, optimize=True)
    print(f"  ✓ {tema}/05.jpg  ·  saco {w}×{h} en ({px}, {py})")


if __name__ == "__main__":
    for t in (sys.argv[1:] or ["sanjuan"]):
        componer(t)

#!/usr/bin/env python3
"""Ronda 3 — reemplaza 4 fotos del carrusel de la landing de terrenos de Más Center.

Fuente: banco de imágenes de Más Center en el Drive de la agencia (marzo 2026),
copiado a raw/mascenter-terrenos/fotos-drive-2026-03/. Son las fotos con la marca
Aramco vigente, las que pidió el cliente en la ronda 3.

Cada tarjeta del carrusel es 3:2 · 1200×800.
"""
import sys
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parents[1]
ORIG = RAIZ / "raw/mascenter-terrenos/fotos-drive-2026-03"
DEST = RAIZ / "out/mascenter-terrenos/assets/img/centros"

# destino -> (archivo de origen, caja de recorte (izq, arriba, der, abajo), por qué)
RECORTES = {
    # "se ve fea": la publicada era un recorte cerrado con el muro gris.
    # Ésta muestra la tira completa: Express de Líder, Cruz Verde y los locales.
    "padre-hurtado.jpg": ("SC-PadreHurtado.jpg", (0, 229, 1000, 896)),
    # Ya no es Petrobras. Recorte que deja fuera el tótem de precios de la derecha.
    "osorno.jpg":        ("SC-Osorno.jpg",       (0, 150, 940, 777)),
    # Aramco vigente y más strip: el edificio de dos pisos con los locales queda a la izquierda.
    "copiapo.jpg":       ("SC-Copiapo.jpg",      (0, 296, 900, 896)),
    # Corrida para que entre el logo del Jumbo, como pidió el cliente.
    "chamisero-1.jpg":   ("SC-ChamiseroI.jpg",   (0, 0, 1150, 767)),
}

ANCHO, ALTO = 1200, 800


def main() -> int:
    for salida, (origen, caja) in RECORTES.items():
        src = ORIG / origen
        if not src.exists():
            print(f"FALTA {src}")
            return 1
        im = Image.open(src).convert("RGB").crop(caja)
        # asegura 3:2 exacto antes de escalar
        objetivo = ANCHO / ALTO
        if abs(im.width / im.height - objetivo) > 1e-3:
            if im.width / im.height > objetivo:
                w = int(im.height * objetivo)
                im = im.crop(((im.width - w) // 2, 0, (im.width - w) // 2 + w, im.height))
            else:
                h = int(im.width / objetivo)
                im = im.crop((0, (im.height - h) // 2, im.width, (im.height - h) // 2 + h))
        im = im.resize((ANCHO, ALTO), Image.LANCZOS)
        im.save(DEST / salida, quality=86, optimize=True, progressive=True)
        print(f"{salida:20s} <- {origen}  {caja}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

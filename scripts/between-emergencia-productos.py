#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cambia los dos productos de la vitrina de la ST «EMERGENCIA BETWEEN» (S2, 9-sep).

⭐ RONDA 10 — 04-09-2026. Comentario del cliente en `STORIES!I15`, sin tachar, o
sea PENDIENTE (el otro comentario de esa celda, el de la diagramación, ya está
tachado y resuelto en la ronda 8):

    «Cambiaría que el salado sea un crosant jamon queso y que el dulce sea un
     muffin»

Qué cambia, y de dónde sale:

    compartimento 2 · DULCE   croissant simple  →  **muffin de chocolate**
    compartimento 3 · SALADO  sándwich baguette →  **croissant de jamón queso**

Los dos son **fotografía real del cliente**, recortada de la sesión
`25 jul 2025` con `scripts/between-recortes-reales.py`:

    muffin              Double Tree 25 jul 25-266.jpg
    croissant j/q       Double Tree 25 jul 25-278.jpg

No se genera comida: el cliente lleva tres rondas reclamando producto inventado
(vasos con logo falso, tazas con marca ajena). La regla del sistema es que la IA
hace ambiente, nunca producto — y acá el producto existe fotografiado.

Los productos viejos se borran con `cv2.inpaint`: el fondo del nicho es un panel
crema con un degradado suave y una diagonal de luz, que es el caso fácil. Las
molduras verticales del vidrio quedan fuera de la máscara para no comérselas.

Uso:
    python scripts/between-emergencia-productos.py
    python scripts/between-emergencia-productos.py --revisar
"""
import argparse
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

FONDO = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-fondo.png"
DESTINO = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-fondo-r10.png"
RECORTES = RAIZ / "public/assets/hilton/between/recortes"

#: cajas MEDIDAS sobre `emergencia-fondo.png` (2250×4000) con zoom al 1:1.
#: ⚠️ La primera pasada las estimó sobre una rejilla reducida y salieron 150 px
#: corridas: el inpaint se comió las molduras doradas del vidrio y dejó medio
#: croissant asomando. Se vuelven a medir sobre el recorte a tamaño real.
VIEJO_DULCE = (1008, 1582, 1268, 2112)     # el croissant simple
VIEJO_SALADO = (1392, 1586, 1638, 2108)    # el sándwich de baguette

#: ⚠️ Las molduras doradas del vidrio corren en x≈890-915, 980-1005, 1275-1300,
#: 1370-1395 y 1665+. Las cajas de arriba pasan POR DENTRO de esos huecos: si el
#: inpaint las toca, se lleva el vidrio.
HUECO = 268                                 # ancho libre entre molduras

#: cada producto nuevo, con ALTO objetivo. El ancho sale de la proporción del
#: recorte y se limita al hueco entre molduras — el producto no se deforma
#: jamás, se elige el giro que lo hace caber.
NUEVOS = [
    # (archivo, centro x, centro y, alto objetivo, giro en grados)
    ("muffin-chocolate.png", 1138, 1858, 470, 0),
    # el croissant se pone casi vertical, que es lo que ya hacía la vitrina con
    # el croissant anterior: los nichos son altos y angostos y un croissant
    # acostado mide 18 cm, tres veces el hueco. −86° deja la punta arriba y el
    # queso escurriendo hacia el mismo lado que la luz.
    ("croissant-jamon-queso.png", 1512, 1852, 470, -86),
]

#: la luz del nicho entra por arriba a la izquierda: la sombra cae abajo-derecha
SOMBRA_DESPLAZA = (24, 26)
SOMBRA_OPACIDAD = 0.30
SOMBRA_DIFUSA = 26


def borra(bgr, cajas):
    """Borra los productos viejos del panel del nicho."""
    mascara = np.zeros(bgr.shape[:2], np.uint8)
    for x0, y0, x1, y1 in cajas:
        # se agranda hacia abajo y a la derecha para llevarse también la sombra
        cv2.rectangle(mascara, (x0 - 12, y0 - 12), (x1 + 46, y1 + 40), 255, -1)
    return cv2.inpaint(bgr, mascara, 17, cv2.INPAINT_TELEA)


def pega(lienzo, ruta, cx, cy, alto_objetivo, giro):
    """Pega un recorte con su sombra de contacto, sin deformarlo."""
    p = Image.open(ruta).convert("RGBA")
    if giro:
        p = p.rotate(giro, resample=Image.BICUBIC, expand=True)
    # escala UNIFORME: se busca el alto pedido y, si el ancho no cabe entre las
    # molduras, manda el ancho. Nunca se estira un eje contra el otro.
    escala = min(alto_objetivo / p.height, HUECO / p.width)
    ancho, alto = round(p.width * escala), round(p.height * escala)
    p = p.resize((ancho, alto), Image.LANCZOS)

    sombra = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    tinta = Image.new("RGBA", p.size, (58, 44, 32, 255))
    tinta.putalpha(p.getchannel("A"))
    sombra.alpha_composite(tinta, (cx - ancho // 2 + SOMBRA_DESPLAZA[0],
                                   cy - alto // 2 + SOMBRA_DESPLAZA[1]))
    sombra = sombra.filter(ImageFilter.GaussianBlur(SOMBRA_DIFUSA))
    canal = sombra.getchannel("A").point(lambda v: int(v * SOMBRA_OPACIDAD))
    sombra.putalpha(canal)

    lienzo.alpha_composite(sombra)
    lienzo.alpha_composite(p, (cx - ancho // 2, cy - alto // 2))
    return lienzo, (ancho, alto)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true")
    a = ap.parse_args()
    if not FONDO.exists():
        sys.exit(f"⛔ Falta {FONDO}")

    bgr = cv2.imread(str(FONDO))
    limpio = borra(bgr, [VIEJO_DULCE, VIEJO_SALADO])
    lienzo = Image.fromarray(cv2.cvtColor(limpio, cv2.COLOR_BGR2RGB)).convert("RGBA")
    for archivo, cx, cy, alto_obj, giro in NUEVOS:
        lienzo, medida = pega(lienzo, RECORTES / archivo, cx, cy, alto_obj, giro)
        print(f"  · {archivo}  {medida[0]}×{medida[1]} px  giro {giro}°")

    lienzo.convert("RGB").save(DESTINO)
    print(f"✓ {DESTINO.relative_to(RAIZ)}  {lienzo.size}")

    if a.revisar:
        ruta = RAIZ / "out/hilton-between-r10/emergencia-vitrina.png"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        lienzo.convert("RGB").crop((150, 1150, 2100, 2650)).resize((975, 750)).save(ruta)
        print(f"→ revisión: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

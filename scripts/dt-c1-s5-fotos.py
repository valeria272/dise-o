#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 (FEED col M · 28-09) — recorta y revela las fotos.

Cada slide es un VIDEO 4:5. El recorte se exporta a **1620×2025** —1,5× de la
mesa de 1080×1350— para que el movimiento de cámara (zoom 1,00→1,07 y deriva)
tenga sobrante y NUNCA muestre borde.

  python scripts/dt-c1-s5-fotos.py            # todas
  python scripts/dt-c1-s5-fotos.py --previo   # hoja de contacto de los encuadres

⭐ `fx`/`fy` son el CENTRO de la ventana de recorte en fracción del ancho/alto
del original. Se eligen mirando, y quedan escritos acá para que la próxima ronda
mueva un número y no vuelva a adivinar.
"""
import argparse
import sys
from pathlib import Path

from PIL import Image, ImageEnhance

try:                                              # Windows decodifica en cp1252
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                 # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/dt/s5-sept/fotos"
DESTINO = RAIZ / "public/assets/hilton/dt/s5"
ANCHO, ALTO = 1620, 2025                       # 1,5 × (1080×1350)

# archivo · fx · fy · zoom del recorte (1 = la ventana 4:5 más grande que cabe)
# c contraste · s saturación · b brillo · w calidez (>1 calienta, <1 enfría)
#
# ⭐ POR QUÉ CADA FOTO, medido sobre el banco el 17-09-2026:
#   portada  HDT_43 es el ÚNICO frontis vertical (4475×6718). Encuadre B de tres
#            probados (z 1,12 / 1,24 / 1,38 / 1,55): la esquina de la torre sube
#            como una proa y deja el cielo limpio arriba, que es donde va el
#            lockup. A z 1,38 la fachada ocupa el pie y el titular caería sobre
#            la retícula de ventanas; a z 1,12 sobra calle.
#   desayuno HDT_60 recortado a la canasta + jugo + fruta. ⚠️ La toma completa es
#            una BANDEJA DE ROOM SERVICE sobre la cama (se ven el teléfono y el
#            respaldo) y Eli fijó el 09-09 que DT va con el desayuno BUFFET del
#            restaurante. El recorte deja fuera cama y teléfono, así que lee como
#            «mesa de desayuno servida», que es lo que pide el brief. Lo que NO
#            existe en el banco es el buffet del hotel sin marca ajena — ver la
#            nota de material en la entrega.
#   salon    HDT_22, board room con el logotipo DT en la pantalla y fuga de un
#            punto: es la que mejor aguanta un acercamiento lento.
#   lobby    HDT_36, el lobby lounge con el muro verde al fondo.
#   habitacion HDT_70, cortinas, lámparas encendidas y cama tendida — la única
#            del banco que lee «fin del día» y no «mediodía».
#   gym      HDT_82. ⏸ Listo, pero NO se entrega: falta el texto de contenido.
#
# ⛔ DESCARTADAS Y POR QUÉ — para no volver a proponerlas:
#   HDT_74..78 y _MG_0839/0852 → son QB Restaurant y traen su marca en cuadro
#            (pizarra «QUOTIDIEN», platos «QB»). QB es marca INDEPENDIENTE.
#   HDT_54/55 → es BETWEEN: la vitrina de mármol lleva el cartel **KIMBO**.
#            Se probó con el método del manual (buscarle la marca adentro).
#   HDT_50/51/52/37/38/56 → espacios de Between ya identificados por Eli.
#   HDT_65 → lee «Escapada Romántica» (espumante y batas).
#   HDT_25..28 → el salón alto con vista; puede ser PISO18 y no está zanjado.
PIEZAS = {
    "portada-frontis":  dict(src="HDT_43-frontis.jpg",    fx=0.56, fy=0.36, z=1.24,
                             c=1.06, s=0.97, b=1.00, w=1.01),
    "desayuno":         dict(src="HDT_60-desayuno.jpg",   fx=0.43, fy=0.39, z=2.05,
                             c=1.06, s=1.02, b=1.02, w=1.01),
    "salon":            dict(src="HDT_22-salon.jpg",      fx=0.46, fy=0.52, z=1.12,
                             c=1.05, s=0.95, b=1.01, w=1.00),
    "lobby":            dict(src="HDT_36-lobby.jpg",      fx=0.44, fy=0.52, z=1.10,
                             c=1.04, s=0.96, b=1.00, w=1.01),
    "habitacion":       dict(src="HDT_70-habitacion.jpg", fx=0.60, fy=0.56, z=1.10,
                             c=1.08, s=0.96, b=0.90, w=1.05),
    "gym":              dict(src="HDT_82-gym.jpg",        fx=0.56, fy=0.52, z=1.06,
                             c=1.04, s=0.95, b=1.01, w=1.00),
}


def calidez(im: Image.Image, k: float) -> Image.Image:
    """Balance de blancos a mano: sube el rojo y baja el azul en la misma razón.

    ⚠️ Mano SUAVE. El reclamo transversal del cliente en Between fue justo el
    contrario —«eliminar el filtro de color cálido», «se ven quemadas»—, así que
    acá `w` no pasa de 1,05 y sólo se usa donde la escena YA es de tungsteno.
    """
    if abs(k - 1.0) < 1e-3:
        return im
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * k)))
    b = b.point(lambda v: min(255, int(v / k)))
    return Image.merge("RGB", (r, g, b))


def recorta(p: dict) -> Image.Image:
    im = Image.open(ORIGEN / p["src"]).convert("RGB")
    W, H = im.size
    # la ventana 4:5 más grande que cabe, dividida por el zoom
    lado_w = min(W, H * 4 / 5) / p["z"]
    lado_h = lado_w * 5 / 4
    cx, cy = p["fx"] * W, p["fy"] * H
    x0 = max(0, min(W - lado_w, cx - lado_w / 2))
    y0 = max(0, min(H - lado_h, cy - lado_h / 2))
    im = im.crop((int(x0), int(y0), int(x0 + lado_w), int(y0 + lado_h)))
    im = im.resize((ANCHO, ALTO), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(p["c"])
    im = ImageEnhance.Color(im).enhance(p["s"])
    im = ImageEnhance.Brightness(im).enhance(p["b"])
    im = calidez(im, p.get("w", 1.0))
    return im


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--previo", action="store_true")
    a = ap.parse_args()
    DESTINO.mkdir(parents=True, exist_ok=True)
    hechas = []
    for nombre, p in PIEZAS.items():
        im = recorta(p)
        salida = DESTINO / f"{nombre}.jpg"
        im.save(salida, quality=92, subsampling=0)
        hechas.append((nombre, im))
        print(f"  {salida.relative_to(RAIZ)}  {im.size}  ← {p['src']}")
    if a.previo:
        cel = 460
        hoja = Image.new("RGB", (cel * len(hechas), int(cel * 1.25) + 24), "#0b0b0b")
        for i, (n, im) in enumerate(hechas):
            m = im.copy(); m.thumbnail((cel - 8, int(cel * 1.25)))
            hoja.paste(m, (i * cel + 4, 0))
        prev = RAIZ / "out/hilton/dt/c1-s5/encuadres.jpg"
        prev.parent.mkdir(parents=True, exist_ok=True)
        hoja.save(prev, quality=88)
        print(f"\n  hoja de encuadres → {prev.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

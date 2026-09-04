#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bodegón REAL para la slide 4 del carrusel PROMOS TO GO (FEED 14-sep, S3).

⭐ RONDA 10 — 04-09-2026. Pedido de Eli sobre la entrega de la ronda 9:
«la slide 4 de ese mismo carrusel, mejora la foto y el vaso».

Lo que había: `togo-trio-brownie.jpg`, una escena GENERADA con el vaso dibujado
por la IA. Medido con zoom, el vaso tenía tres defectos que se leen a primera
vista —la tapa era un domo acanalado inventado, el logotipo iba estampado plano
sobre una superficie curva (se lee como una calcomanía) y el cartón no tenía
fibra—. Es el mismo reclamo que el cliente viene repitiendo desde la ronda 4.

Lo que hay ahora: **la promo entera es fotografía del cliente.** Los tres
protagonistas salen de la sesión `25 jul 2025`, la misma mesa de listones, el
mismo muro vegetal, la misma luz y el mismo 50 mm a f/3,5:

    café    ·  el vaso vigente, kraft con el logotipo IMPRESO   → 25-278 (base)
    salado  ·  croissant de jamón queso                          → 25-278 (base)
    dulce   ·  muffin de chocolate en su plato de loza verde     → 25-266 (pegado)

O sea: no se retoca un vaso generado, se usa el vaso. Y el «dulce» que se agrega
viene con su propio plato, recortado con grabCut por
`scripts/between-recortes-reales.py`, así que no hay producto flotando.

⚠️ Por qué el dulce se pega y no se buscó una foto con los tres: no existe. La
sesión tiene café+salado y café+dulce en tomas distintas. Al ser la MISMA mesa y
la MISMA luz, el montaje casa sin trucos: sólo hay que respetar la profundidad
—el plato que entra va más adelante, así que va más grande y más abajo— y darle
su sombra de contacto.

Uso:
    python scripts/between-togo4-bodegon.py
    python scripts/between-togo4-bodegon.py --revisar
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-278.jpg"
PLATO = RAIZ / "public/assets/hilton/between/recortes/plato-muffin.png"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-trio-real.jpg"

#: recorte 4:5 desde la original de 3840×5760. El desplazamiento vertical deja
#: 15 % de muro arriba, el vaso en el tercio superior y una banda de mesa libre
#: abajo para el plato que entra.
CORTE = (0, 960, 3840, 5760)
SALIDA = (2250, 2812)

#: el plato del dulce, en píxeles del lienzo de 3840×4800 (antes de reducir)
DULCE_ANCHO = 2380          # más grande que el de la base: está más adelante
DULCE_CENTRO = (2620, 3860)   # a la DERECHA: la esquina inferior
#: izquierda es de la caja de la promo, y una pila taupe sobre el plato del
#: dulce tapa justo el producto que la caja está nombrando
SOMBRA_DESPLAZA = (46, 40)
SOMBRA_OPACIDAD = 0.34
SOMBRA_DIFUSA = 44


def grada_neutro(im):
    """Perfil `neutro` del mes: sin filtro cálido y sin quemar las altas.

    ⚠️ Mano SUAVE porque el protagonista es hojaldre: el manual fija p95 ≈ 214
    para producto claro (la pasada estándar a 227 le aplanó el croissant y el
    cliente lo cazó).
    """
    arr = np.asarray(im).astype(np.float32)
    calidez = float(arr[..., 0].mean() - arr[..., 2].mean())
    if calidez > 22:
        ajuste = (calidez - 21.0) * 0.55
        arr[..., 0] -= ajuste * 0.62
        arr[..., 2] += ajuste * 0.38
    p95 = float(np.percentile(arr, 95))
    if p95 > 0:
        arr *= min(1.06, max(0.90, 214.0 / p95))
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true")
    a = ap.parse_args()
    for r in (BASE, PLATO):
        if not r.exists():
            sys.exit(f"⛔ Falta {r}")

    lienzo = Image.open(BASE).convert("RGB").crop(CORTE).convert("RGBA")
    print(f"base 4:5  {lienzo.size}")

    plato = Image.open(PLATO).convert("RGBA")
    alto = round(plato.height * DULCE_ANCHO / plato.width)   # escala uniforme
    plato = plato.resize((DULCE_ANCHO, alto), Image.LANCZOS)
    px = DULCE_CENTRO[0] - DULCE_ANCHO // 2
    py = DULCE_CENTRO[1] - alto // 2

    sombra = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    tinta = Image.new("RGBA", plato.size, (40, 26, 16, 255))
    tinta.putalpha(plato.getchannel("A"))
    sombra.alpha_composite(tinta, (px + SOMBRA_DESPLAZA[0], py + SOMBRA_DESPLAZA[1]))
    sombra = sombra.filter(ImageFilter.GaussianBlur(SOMBRA_DIFUSA))
    sombra.putalpha(sombra.getchannel("A").point(lambda v: int(v * SOMBRA_OPACIDAD)))
    lienzo.alpha_composite(sombra)
    lienzo.alpha_composite(plato, (px, py))
    print(f"dulce pegado  {plato.size} en ({px}, {py})")

    final = grada_neutro(lienzo.convert("RGB").resize(SALIDA, Image.LANCZOS))
    final.save(DESTINO, quality=95)
    print(f"✓ {DESTINO.relative_to(RAIZ)}  {final.size}")

    if a.revisar:
        ruta = RAIZ / "out/hilton-between-r10/togo4-bodegon.png"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        final.resize((700, 875), Image.LANCZOS).save(ruta)
        print(f"→ revisión: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

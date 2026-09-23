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
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402
from between_retoque import (apetitoso, informe, limpia_madera,  # noqa: E402
                             nitidez, revela, vivo)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-278.jpg"
PLATO = RAIZ / "public/assets/hilton/between/recortes/plato-muffin.png"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-trio-real.jpg"

#: ⭐ v2 — la original se ALARGA 300 px por la derecha antes de recortar. El
#: vaso termina en x=3673 y el cuadro en 3840: 167 px de aire, que a 2250 de
#: entrega son 98 y hacen que el vaso se lea pegado al canto. Alargando la mesa
#: (espejo del propio flanco) el recorte se corre y el vaso respira.
ALARGA = 160
CORTE = (160, 960, 4000, 5760)      # 3840×4800 = 4:5
SALIDA = (2250, 2812)

#: ⭐ v2 — el plato del dulce entra ENTERO. En la v1 lo cortaba el canto derecho
#: y el inferior a la vez, y Eli lo cazó: «hay un plato que se ve cortado…
#: cuando hagas montaje tiene que verse unificada la imagen, no pueden estar
#: cortadas». Un plato que el encuadre corta se lee como foto; un plato pegado
#: que además está cortado se lee como error.
#: ⚠️ y va ABAJO del croissant, no encima: en la primera pasada de la v2 el
#: plato del dulce tapaba el croissant entero. El plato de atrás llega a y=3240
#: en el lienzo recortado, así que el de adelante empieza ahí.
DULCE_ANCHO = 2050
DULCE_CENTRO = (1690, 3870)     # centro EN EL LIENZO YA RECORTADO
SOMBRA_DESPLAZA = (46, 40)
SOMBRA_OPACIDAD = 0.34
SOMBRA_DIFUSA = 44

#: el canto de la mesa contra el muro, medido en 278
BORDE_MESA = 1690
#: dónde está la comida, para el retoque (y para protegerla del limpiador)
CROISSANT = (500, 2800, 2900, 4200)
VASO_BASE = (2650, 1650, 3760, 3400)


def mascara(caja, tamano, elipse=False):
    m = Image.new("L", tamano, 0)
    d = ImageDraw.Draw(m)
    (d.ellipse if elipse else d.rectangle)(caja, fill=255)
    return np.asarray(m) > 127


def alarga_derecha(im, px):
    """Espeja el flanco derecho para darle aire al vaso. Mesa lisa: no se nota.

    ⚠️ La banda se toma DESPUÉS del vaso (termina en x=3673). Espejando los
    últimos 300 px se copiaba medio vaso y aparecía un vaso fantasma en el canto.
    """
    banda = im.crop((im.width - px, 0, im.width, im.height)).transpose(
        Image.FLIP_LEFT_RIGHT)
    salida = Image.new("RGB", (im.width + px, im.height))
    salida.paste(im, (0, 0))
    salida.paste(banda, (im.width, 0))
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true")
    a = ap.parse_args()
    for r in (BASE, PLATO):
        if not r.exists():
            sys.exit(f"⛔ Falta {r}")

    base = Image.open(BASE).convert("RGB")

    # 1 · la mesa, sin rayones ni grietas («borrar los detalles de rayones y
    #     grietas que se ven en la mesa», Eli)
    alto, ancho = base.height, base.width
    ys = np.arange(alto)[:, None]
    zona = np.repeat(ys > BORDE_MESA + 40, ancho, axis=1)
    proteger = mascara(CROISSANT, base.size) | mascara(VASO_BASE, base.size)
    base, marcas = limpia_madera(base, zona=zona, proteger=proteger,
                                 umbral=10, nucleo=61)
    print(f"mesa limpia ✓  ({marcas} px de rayones y grietas)")

    lienzo = (alarga_derecha(base, ALARGA) if ALARGA else base).crop(CORTE).convert("RGBA")
    print(f"base 4:5  {lienzo.size}")

    plato = Image.open(PLATO).convert("RGBA")
    # ⭐ v2 — el muffin sale casi negro contra la loza verde. Se le levantan las
    #    sombras y se le da cuerpo antes de pegarlo: «evita un poco los colores
    #    del muffin», Eli.
    alfa_p = plato.getchannel("A")
    plato = apetitoso(plato.convert("RGB"), claridad=0.45, cuerpo=1.12,
                      calor=4.0).convert("RGBA")
    plato.putalpha(alfa_p)
    alto_p = round(plato.height * DULCE_ANCHO / plato.width)   # escala uniforme
    plato = plato.resize((DULCE_ANCHO, alto_p), Image.LANCZOS)
    px = DULCE_CENTRO[0] - DULCE_ANCHO // 2
    py = DULCE_CENTRO[1] - alto_p // 2

    sombra = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    tinta = Image.new("RGBA", plato.size, (40, 26, 16, 255))
    tinta.putalpha(plato.getchannel("A"))
    sombra.alpha_composite(tinta, (px + SOMBRA_DESPLAZA[0], py + SOMBRA_DESPLAZA[1]))
    sombra = sombra.filter(ImageFilter.GaussianBlur(SOMBRA_DIFUSA))
    sombra.putalpha(sombra.getchannel("A").point(lambda v: int(v * SOMBRA_OPACIDAD)))
    lienzo.alpha_composite(sombra)
    lienzo.alpha_composite(plato, (px, py))
    print(f"dulce pegado ENTERO  {plato.size} en ({px}, {py})")

    # ── revelado y retoque de comida ──
    final = lienzo.convert("RGB").resize(SALIDA, Image.LANCZOS)
    final = revela(final, negros=0.010, contraste=1.05, medios=100)
    escala = SALIDA[0] / (CORTE[2] - CORTE[0])
    comida = (mascara(tuple(int((c - o) * escala) for c, o in
                            zip(CROISSANT, (CORTE[0], CORTE[1], CORTE[0], CORTE[1]))),
                      SALIDA, elipse=True)
              | mascara((int((px) * escala), int((py) * escala),
                         int((px + DULCE_ANCHO) * escala), int((py + alto_p) * escala)),
                        SALIDA, elipse=True))
    final = apetitoso(final, comida, claridad=0.50, cuerpo=1.08, calor=4.5)
    final = vivo(final, vibrancia=0.28)
    final = nitidez(final, cantidad=0.32, radio=1.4)
    informe(final, "To Go slide 4")
    final.save(DESTINO, quality=96)
    print(f"✓ {DESTINO.relative_to(RAIZ)}  {final.size}")

    if a.revisar:
        ruta = RAIZ / "out/hilton-between-r10/togo4-bodegon.png"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        final.resize((700, 875), Image.LANCZOS).save(ruta)
        print(f"→ revisión: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

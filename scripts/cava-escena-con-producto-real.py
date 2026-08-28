#!/usr/bin/env python3
"""CAVA — escena de IA + BOTELLA REAL encima. La proporción la resuelve la IA, la
etiqueta la pone el packshot oficial.

EL PROBLEMA QUE RESUELVE
------------------------
Componer el packshot sobre un fondo generado aparte tiene un techo: el barril y la
botella nunca comparten escala, porque el fondo se generó sin saber qué iba encima.
Resultado: o la botella flota delante del barril, o queda desproporcionada.
Valeria, 28-08-2026: *«la botella sigue flotando cuando debería estar sobre el
barril […] todo es desproporcional»*.

Nano Banana Pro **sí** resuelve la escena entera —apoyo real sobre la tapa, sombra
de contacto, escala coherente, bokeh— pero **redibuja la etiqueta e inventa el
texto**: en la primera prueba devolvió «SINGLE VINESARD», «VALLE DEL MALLSI» y
«WINE DE CHIVE» sobre un 7Colores. Para una viña eso es impresentable
(`clients/cava/CLAUDE.md` §2: las botellas y sus etiquetas son intocables).

LA SALIDA
---------
Se le pide a la IA la escena COMPLETA con botella, se **mide dónde y de qué tamaño**
la puso, y se pega el bottle shot oficial exactamente ahí, cubriéndola. Lo que se
aprovecha de la IA es la dirección de arte —dónde apoya, qué tamaño tiene, cómo cae
la sombra—; lo que se entrega es el producto real.

Uso:
    python3 scripts/cava-escena-con-producto-real.py --botella <nombre> [--escena N]
"""
import argparse
import os
import sys

import numpy as np
from PIL import Image, ImageChops, ImageFilter, ImageStat

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOT = os.path.join(RAIZ, "public", "assets", "cava", "bottles")
ESCENAS = os.path.join(RAIZ, "out", "cava", "escenas-ia")
SALIDA = os.path.join(RAIZ, "out", "cava", "escenas-ia")


def silueta_botella(escena):
    """Dónde puso la IA la botella: la mancha oscura, alta y central de la escena.

    La botella es lo más oscuro y lo más vertical del cuadro; el viñedo es claro y
    el barril es cálido de tono medio. Se busca por columna cuántos píxeles
    oscuros hay y se toma la banda central contigua.
    """
    g = np.asarray(escena.convert("L"), dtype=float)
    h, w = g.shape
    oscuro = g < np.percentile(g, 22)
    # sólo la mitad superior-central: abajo el barril tiene vetas oscuras
    porcol = oscuro[: int(h * 0.80)].sum(axis=0)
    porcol = np.convolve(porcol, np.ones(31) / 31, mode="same")
    umbral = porcol.max() * 0.35
    cols = np.where(porcol > umbral)[0]
    if len(cols) == 0:
        sys.exit("✗ No encontré la botella en la escena")
    # banda contigua alrededor del máximo
    pico = int(np.argmax(porcol))
    x0 = pico
    while x0 > 0 and porcol[x0 - 1] > umbral:
        x0 -= 1
    x1 = pico
    while x1 < w - 1 and porcol[x1 + 1] > umbral:
        x1 += 1

    franja = oscuro[:, x0:x1]
    porfila = franja.sum(axis=1)
    porfila = np.convolve(porfila, np.ones(15) / 15, mode="same")
    filas = np.where(porfila > (x1 - x0) * 0.30)[0]
    y0, y1 = int(filas.min()), int(filas.max())
    return x0, y0, x1, y1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--botella", default="7colores-single-vineyard-red-blend")
    ap.add_argument("--escena", default="7colores-single-vineyard-red-blend-01.png")
    ap.add_argument("--holgura", type=float, default=1.06,
                    help="cuánto más grande que la botella IA, para taparla")
    ap.add_argument("--caja", default="0.370,0.090,0.620,0.780",
                    help="x0,y0,x1,y1 en FRACCIÓN, medidos a ojo sobre la grilla "
                         "(python3 scripts/cava-escena-con-producto-real.py --grilla). "
                         "El detector automático confunde la botella con las vetas "
                         "del barril — el manual §11 ya lo dice para la tapa.")
    ap.add_argument("--auto", action="store_true", help="usar el detector (no fiable)")
    ap.add_argument("--grilla", action="store_true",
                    help="saca la escena con una grilla de %% encima, para medirla")
    a = ap.parse_args()

    ruta = os.path.join(ESCENAS, a.escena)
    if not os.path.isfile(ruta):
        sys.exit(f"✗ No existe {ruta}")
    escena = Image.open(ruta).convert("RGB")

    if a.grilla:
        from PIL import ImageDraw as _ID
        g = escena.copy()
        d = _ID.Draw(g)
        for i in range(0, 101, 5):
            x, y = int(g.width * i / 100), int(g.height * i / 100)
            col = (255, 0, 0) if i % 10 == 0 else (255, 180, 180)
            an = 3 if i % 10 == 0 else 1
            d.line([x, 0, x, g.height], fill=col, width=an)
            d.line([0, y, g.width, y], fill=col, width=an)
            if i % 10 == 0:
                d.text((x + 6, 6), str(i), fill=(255, 0, 0))
                d.text((6, y + 6), str(i), fill=(255, 0, 0))
        rg = os.path.join(SALIDA, "_grilla-" + a.escena)
        g.save(rg)
        print(f"→ {rg}\n   Mídela y pasa --caja x0,y0,x1,y1 en fracción.")
        return 0

    if a.auto:
        x0, y0, x1, y1 = silueta_botella(escena)
    else:
        fx0, fy0, fx1, fy1 = (float(v) for v in a.caja.split(","))
        x0, y0 = round(escena.width * fx0), round(escena.height * fy0)
        x1, y1 = round(escena.width * fx1), round(escena.height * fy1)
    print(f"→ La IA puso su botella en x {x0}-{x1}, y {y0}-{y1} "
          f"({x1-x0}×{y1-y0} px sobre {escena.width}×{escena.height})")
    print(f"   alto = {100*(y1-y0)/escena.height:.1f} % de la pieza")

    p2 = os.path.join(BOT, "2x", a.botella + ".png")
    real = Image.open(p2 if os.path.isfile(p2) else
                      os.path.join(BOT, a.botella + ".png")).convert("RGBA")
    real = real.crop(real.split()[-1].getbbox())

    alto = round((y1 - y0) * a.holgura)
    anc = round(alto * real.width / real.height)
    real = real.resize((anc, alto), Image.LANCZOS)

    # se alinea por la BASE y por el centro: la sombra de contacto que dibujó la IA
    # queda justo debajo, y es la que hace que se lea apoyada
    cx = (x0 + x1) // 2
    pos = (int(cx - anc / 2), int(y1 - alto))

    fuera = escena.convert("RGBA")
    fuera.alpha_composite(real, pos)
    destino = os.path.join(SALIDA, f"_final-{a.botella}.png")
    fuera.convert("RGB").save(destino)
    print(f"  ✓ {destino}")

    # ¿queda algo de la botella inventada asomando?
    print("\n  MÍRALA: si asoma un borde de la botella de la IA, sube --holgura.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

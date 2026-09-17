#!/usr/bin/env python3
"""QB · ST S5 AYCD — genera la escena del celular en la mano.

    python scripts/qb-aycd-s5-escena.py            # genera las 3 variantes
    python scripts/qb-aycd-s5-escena.py --una 2    # regenera sólo la 2

POR QUÉ SE GENERA
─────────────────
El brief pide «unas manos sosteniendo un celular en primer plano» dentro de QB, y
en todo el material propio de la marca **no existe esa foto**: las sesiones son de
coctelería, platos y rostros, y la de julio que hay en Drive es de un matrimonio.
Es el caso del manual en que la escena se PRODUCE (docs/SISTEMA-DE-MARCAS.md §2):
la IA hace ambiente y fondo, nunca el producto ni el dato.

⭐ Y el trago que se ve dentro del celular NO se genera: ahí va un recorte de la
fotografía real y aprobada de la promo. La IA pone la mano, la mesa y el bokeh.

⭐⭐ LA PANTALLA SALE EN VERDE, A PROPÓSITO
La pantalla se pide como un rectángulo VERDE plano y saturado, sin nada adentro.
Con eso:
  1. el cuadrilátero se detecta por color y se le monta la gráfica en perspectiva,
     así que la promo dentro del celular es **tipografía real, no tipografía
     alucinada** — ningún modelo escribe «POR $13.990» sin romperlo; y
  2. el bloque de marca queda intocable, que es lo que Eli dictó.

⚠️ Manos: se NOMBRA el tipo. Pedir «manos» a secas devuelve el fenotipo nórdico
por defecto (memoria `generar-personas-nombrar-el-tipo`).

SALE
────
  raw/hilton/qb/aycd/escena/escena-{1,2,3}.png
"""
import argparse
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RAIZ, "raw", "hilton", "qb", "aycd", "escena")
MAGNIFIC = os.path.join(RAIZ, "scripts", "magnific.py")

COMUN = (
    "Vertical 9:16 editorial photograph taken at night inside an upscale, dimly lit "
    "cocktail bar and restaurant. "
    "FOREGROUND SUBJECT: the two hands of a young Chilean woman — natural warm "
    "olive Latin American skin, short neat manicure, one thin gold ring — holding a "
    "modern black smartphone upright in portrait orientation, gripped from the sides, "
    "seen from the phone owner's own point of view. The phone is large in frame and "
    "is unmistakably the focal point, tack sharp. "
    "THE PHONE SCREEN IS A COMPLETELY FLAT, UNIFORM, PURE SATURATED GREEN RECTANGLE "
    "(hex 00B140) that fills the whole display edge to edge inside the bezel: no "
    "icons, no text, no picture, no reflection, no glare, no gradient, no vignetting. "
    "Absolutely blank chroma-key green. "
    "BACKGROUND: a restaurant table strongly out of focus, creamy shallow-depth-of-field "
    "bokeh — a tall cocktail glass with ice and citrus, a dark sharing plate with food, "
    "a dark wood table top, warm amber practical lights and the blurred glow of a back "
    "bar with bottles. Deep shadows, rich blacks, warm low-key cinematic lighting, "
    "elegant and moody, deep browns and amber highlights. "
    "Photographic and natural. NO text anywhere, no logos, no watermark, no UI."
)

VARIANTES = {
    "1": COMUN + (
        " Framing: the phone is centred and upright, occupying about 55% of the image "
        "height in the middle third; generous dark empty space above and below it."
    ),
    "2": COMUN + (
        " Framing: the phone sits slightly low and is tilted about 8 degrees to the "
        "left; it occupies about 60% of the image height, leaving a wide dark, quiet "
        "area across the upper third of the frame."
    ),
    "3": COMUN + (
        " Framing: shot from slightly above, looking down at the phone over the table; "
        "the phone is centred, nearly upright, occupying about 50% of the image height, "
        "and the blurred cocktail and sharing plate read clearly behind it."
    ),
}


def generar(clave, prompt):
    os.makedirs(DEST, exist_ok=True)
    salida = os.path.join(DEST, f"escena-{clave}.png")
    cmd = [sys.executable, MAGNIFIC, "pro", prompt,
           "--out", salida, "--aspecto", "story", "--resolucion", "4K"]
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    print(f"\n── variante {clave} ──", flush=True)
    r = subprocess.run(cmd, env=entorno)
    return r.returncode == 0 and os.path.exists(salida)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--una", choices=sorted(VARIANTES))
    a = ap.parse_args()
    claves = [a.una] if a.una else sorted(VARIANTES)
    for k in claves:
        generar(k, VARIANTES[k])
    print(f"\nListo en {os.path.relpath(DEST, RAIZ)}")


if __name__ == "__main__":
    main()

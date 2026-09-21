#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · slide 4 — ronda 27 (21-09-2026): la escena se GENERA.

Eli, después de ver el montaje de la ronda 26:

    «Revisa tú mismo cómo quedaron partes incompletas […] hay un pedazo de
     sándwich que desapareció, una bolsa que está media extraña, como que se
     cortó, como que se pixeleó […] el café está desapareciendo. Se ve muy mal.
     Se ve como si estuviera pegoteado. Trata de hacerlo perfecto. Cambios
     sutiles. Que se vean reales. […] Si quieres vuelve a hacer de nuevo la
     imagen. Para no estar pegoteando todo de nuevo. Mejora el prompt. Y hazlo
     de nuevo.»

⛔⛔ TENÍA RAZÓN, Y EL DIFF LO CONFIRMÓ. Comparando la pieza contra la aprobada,
   el montaje de la ronda 26 había tocado **888.000 px de x=0 a x=2249**: los
   parches escalados se comieron el canto de la bolsa, dejaron **el logotipo
   del vaso DUPLICADO** —el viejo asomando bajo el nuevo— y borraron un trozo
   del sándwich, porque el mate de grabCut le abría agujeros al pan y nadie los
   cerró. Tres defectos que ninguna receta de montaje iba a arreglar.

⭐⭐⭐ POR ESO SE CAMBIA EL MÉTODO, Y ES EL DE ELLA.
`clients/hilton/PROMPTS-DE-ELI.md`, primera línea: **«No se compone: se GENERA.»**
Su regla: *cuando algo falla varias veces con materiales distintos, lo que hay
que cambiar no es el material ni la posición: es el MÉTODO.* Ya pasó con la ST
del 28-09 —tres rechazos de montaje, resuelta generando— y acá pasó igual.

Las referencias hacen el trabajo que hacía el recorte:

    @img1  la ESCENA APROBADA — el lugar, la mesa de listones, el muro de
           plantas, la bolsa kraft, la mano y los tres productos
    @img2  el VASO real en grande — su logotipo impreso BETWEEN COFFEE & BAR
           con la Ǝ invertida, su tapa negra y su banda blanca en la base
    @img3  25-248: el vaso y el sándwich REALES en la misma toma — de ahí sale
           la proporción que pidió el cliente, fotografiada, no estimada
    @img4  25-266: el vaso y el muffin REALES en la misma toma

⭐ LA PROPORCIÓN VA DICHA, que es todo el encargo de esta ronda:
   Scarlette: «los productos no se ven proporcionales unos con otros, revisar
   los tamaños de los cafés y sus agregados». Eli: «lo que es sándwich es más
   grande solo un poco, muffin última que crezca solo un poco».
   Medido sobre las fotos reales y traducido a lenguaje del prompt: el vaso es
   el más alto de la mesa, el sándwich sólo un poco más ancho que el vaso, y el
   muffin más bajo que el vaso.

⛔ Los tres candados del manual, y uno propio de esta pieza:
   · sin texto, sin letras, sin logotipos flotantes — la tipografía la pone
     Remotion con la geometría medida;
   · el logotipo del vaso NO se inventa: llega porque va el vaso real de ref;
   · el ENCUADRE explícito franja por franja, que es lo que destraba estas
     escenas;
   · UNA sola mano, cinco dedos — «hay una mano de más» ya fue un rechazo del
     cliente en esta cuenta.

Uso:
    python scripts/between-togo4-r27-generar.py               # una tirada
    python scripts/between-togo4-r27-generar.py --sufijo b    # otra
    python scripts/between-togo4-r27-generar.py --solo-prompt
"""
import argparse
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REFS = RAIZ / "raw/hilton/between/s4/refs-gen-r27"
SALIDA = RAIZ / "raw/hilton/between/s4/gen-r27"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

#: El vaso, descrito con todo lo que el manual tiene medido de él. Va el real
#: como @img2, pero la descripción evita que el generador le invente detalles.
VASO = (
    "El vaso de cafe es exactamente el de la @img2: vaso To Go de carton kraft "
    "MATE, tapa negra de domo, su logotipo impreso BETWEEN COFFEE & BAR nitido y "
    "centrado a media altura con la E invertida, y su banda blanca en la base. "
    "No inventes letras ni cambies el logotipo. "
)

#: Las proporciones, que son el encargo de la ronda.
PROPORCION = (
    "PROPORCIONES REALES, como en la @img3 y la @img4: el VASO es el mas ALTO de "
    "los tres productos de la mesa; el SANDWICH es solo un poco mas ancho que el "
    "vaso, no el doble; el MUFFIN es el mas chico y su copa queda mas abajo que "
    "la tapa del vaso. Los tres estan apoyados en la misma mesa y a la misma "
    "distancia de la camara, ninguno flota ni se ve pegado. "
)

#: ⛔ La primera tirada salió con una mesa CLARA, casi rubia, y un seto de hoja
#: chica. La mesa de Between es madera café cálida con la veta y las marcas de
#: uso a la vista, y el muro es de hoja GRANDE. Va dicho, y en negativo.
LUGAR = (
    "El lugar es el de la @img1 y no otro: mesa de listones de madera CAFE CALIDA "
    "de tono medio, con la veta marcada y sus marcas de uso, NO una mesa clara ni "
    "rubia ni de madera nueva; y detras un muro vivo de plantas de HOJA GRANDE "
    "verde oscuro, muy desenfocado, NO un seto de hoja chica. "
)

ENCUADRE = (
    "ENCUADRE, de arriba hacia abajo: el TERCIO DE ARRIBA es el muro de plantas "
    "verde oscuro muy desenfocado, limpio y sin nada encima para poder poner un "
    "texto; en la franja del medio, de pie sobre la mesa, la bolsa de papel kraft "
    "To Go con asas planas, tomada por el asa por UNA mano que entra desde arriba "
    "a la derecha; abajo, sobre la mesa de listones de madera clara, los tres "
    "productos en una fila: el sandwich a la izquierda, el muffin al centro y el "
    "vaso a la derecha, separados entre si, sin tocarse y sin taparse. "
    "Deja la franja de mas abajo con mesa de madera limpia para dar aire. "
)

CANDADOS = (
    "Realista, fotografia de producto con luz natural de dia nublado, suave y "
    "pareja, sin flash y sin brillos duros, cada producto con su sombra de "
    "contacto sobre la mesa. UNA sola mano, con cinco dedos y el nudillo visible. "
    "Que se vea delicioso y apetitoso, alta calidad 4k, medida de 2250x2812px. "
    "Sin ningun texto, sin letras y sin logotipos flotantes."
)

PROMPT = (
    "Rehaz la escena de la @img1 entera, de una sola vez y sin pegar nada: "
    "bodegon vertical 4:5 de las promos To Go de Between sobre la mesa de "
    "listones de madera clara del local, con el muro de plantas detras. "
    "Sobre la mesa van los tres productos de la @img1: el sandwich de pan de "
    "molde tostado con relleno de palta y pollo, apoyado sobre su papel de horno "
    "blanco; el muffin de chocolate en su capacillo de papel cafe oscuro, sobre "
    "un plato de loza gris azulada; y el vaso de cafe. "
    + VASO + PROPORCION + LUGAR + ENCUADRE +
    "Realista y mejora color. " + CANDADOS
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sufijo", default="")
    ap.add_argument("--solo-prompt", action="store_true")
    a = ap.parse_args()

    #: ⚠️ `--aspecto post` es 3:4 (0,75) y el feed de Between es 4:5 (0,80): es
    #: el más cercano que da la API. La tirada en 1:1 no sirvió — el bodegón
    #: nace centrado y recortar 4:5 de un cuadrado le corta el sándwich. Del
    #: 3:4 se recorta el alto, que es donde sobra muro.
    print(f"prompt: {len(PROMPT)} caracteres (el tope de Nano Banana Pro son 3.000)\n")
    print(PROMPT)
    if a.solo_prompt:
        return

    refs = [REFS / n for n in ("escena-aprobada.jpg", "vaso-real.jpg",
                               "proporcion-real.jpg", "muffin-real.jpg")]
    faltan = [r.name for r in refs if not r.is_file()]
    if faltan:
        sys.exit(f"\nABORTA: faltan referencias en {REFS}: {faltan}")

    SALIDA.mkdir(parents=True, exist_ok=True)
    out = SALIDA / f"togo-s4-gen{('-' + a.sufijo) if a.sufijo else ''}.png"
    print(f"\n=== generando → {out.relative_to(RAIZ)}")
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
         "--out", str(out), "--aspecto", "post", "--resolucion", "4K",
         "--refs", *[str(x) for x in refs]],
        cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit("ABORTA: falló la generación")
    print("\nMÍRALA antes de usarla. Y el logotipo del vaso, al 300 %.")


if __name__ == "__main__":
    main()

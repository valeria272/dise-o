#!/usr/bin/env python3
"""Genera las DOS escenas de las stories estáticas de la S4 con el método de Eli.

⭐ 09-09-2026. Eli: «Trabajaremos con los diseños de las historias estáticas de la
s4 de grilla […] y guíate de las referencias que adjunta contenido […] No tomes
como gráficas las interacciones de contenido, solo deja aire visual o espacio
para que agreguen esas interacciones.»

Las dos columnas de la hoja STORIES (instantánea del 09-09 en
`clients/hilton/grillas/between-septiembre-2026.md`):

  col Q · 21-09 · OK PARA DISEÑAR · «ST ESTÁTICO – STRUDEL DE MANZANA»
  col R · 22-09 · OK PARA DISEÑAR · «ST ESTÁTICA – PRIMAVERA EN BETWEEN»

Referencias de contenido, bajadas y verificadas por bytes a
`raw/hilton/between/ref-s4-eli/` (Drive `1NNCSTiYNk2YTT6Ol8k77vLti8NpCjNnq`):

  `Ref S4 Storie 1.png` → mosaico de CUATRO CUADRANTES de ingredientes con el
      producto centrado encima de la cruz. Es la gramática que el brief pide
      textualmente («composición editorial dividida en 4 fotografías»).
  `Ref S4 Storie 2.jpg` → producto ALTO sostenido contra un campo de color liso,
      con aire generoso para el texto y garabatos de línea blancos.

## Por qué se GENERA, y qué es real en cada una

El método de Between está escrito en `clients/hilton/PROMPTS-DE-ELI.md`: **no se
compone, se GENERA**, y sobre todo **se EDITA la foto real** en vez de inventar la
escena. Acá eso se aplicó distinto en cada pieza, porque el material es distinto:

| | Producto | De dónde sale |
|---|---|---|
| **22-09 · Primavera** | ✅ **REAL** | `Between-214.jpg` de la sesión del 3 de enero (Canon 5D Mk III, 1500×2250, EXIF verificado). Es el milkshake del cliente: copa de vidrio con pie, borde escarchado de coco, frutilla y bombilla negra. **Sólo se cambia el fondo** — la pared de piedra oscura por la terraza real de Between |
| **21-09 · Strudel** | ⚠️ **GENERADO** | Between **no tiene ninguna foto del Strudel de manzana**. Se buscó en las 202 fotos de `3 ENERO _ PLATOS - DESAYUNOS`, en `BETWEEN DESAYUNOS AGO 2026`, en `dulces-tortas` y en la carta: no está. Lo real que entra son el **hojaldre** y el **plato de cerámica verde oliva** de `Between-28.jpg`, que van como referencia para que la masa y la loza sean las del cliente |

⚠️ **Eso hay que decirlo al entregar**, no esconderlo: la regla del estudio es que
lo generado se rotula como generado, justamente para poder reemplazarlo el día que
llegue la foto de verdad.

## Los cuadrantes NO van en el orden del brief, y es una decisión medida

El brief numera los ingredientes (1 masa · 2 manzana · 3 canela · 4 nueces) pero
**no fija sus posiciones**. Se ordenan por LUMINANCIA:

    canela (oscura)   │  nueces (oscuras)      ← el titular beige cae acá
    ──────────────────┼──────────────────
    masa dorada       │  manzana verde

El titular de Between ancla en y=441 y el mosaico parte los cuadrantes en y=960,
así que el bloque de texto cae ENTERO en la mitad de arriba. Con un cuadrante
claro y otro oscuro arriba, el titular se partiría en dos legibilidades — que es
exactamente el defecto que el manual documenta en la pieza del cowork («la foto se
PARTE y ninguna de las dos tintas se lee en todo el ancho»). Con los dos oscuros,
el beige se lee de lado a lado sin ninguna caja debajo.

## Los candados que van en los dos prompts

  · **«Sin ningún texto, sin letras, sin logotipos»** — la tipografía la pone
    Remotion con la geometría medida (logo y=271, ancla y=441, columna 810).
  · **«sin tazas»** en el Strudel — la regla KIMBO: la loza del cliente trae el
    logotipo impreso y la referencia se recortó justamente para dejarlo fuera.
  · **el ENCUADRE explícito, franja por franja** — es la frase que destrabó el
    panorama del cumpleaños y las tres de la S3.
  · **el aire de la interacción se PIDE en el prompt** («la franja de abajo queda
    tranquila»), no se resuelve apretando la diagramación después.

Uso:
    python scripts/between-st-s4-generar.py               # las dos
    python scripts/between-st-s4-generar.py 21-09         # sólo una
    python scripts/between-st-s4-generar.py --sufijo v2   # otra tirada
"""
import argparse
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
REFS = RAIZ / "raw/hilton/between/s4/refs"
SALIDA = RAIZ / "raw/hilton/between/s4"

ESCENAS = {
    # ── 21-09 · el MOSAICO de cuatro cuadrantes de la REF 1 ──────────────────
    "21-09": {
        "salida": "gen-21-09-strudel",
        "refs": ["hojaldre-plato.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 compuesta como un MOSAICO EDITORIAL "
            "de cuatro cuadrantes iguales, dos arriba y dos abajo, cada uno una macro "
            "fotografia distinta de un ingrediente, con la misma luz calida y el mismo "
            "estilo en los cuatro. ARRIBA A LA IZQUIERDA: canela, ramas de canela y "
            "canela molida, tono cafe oscuro. ARRIBA A LA DERECHA: nueces peladas, "
            "tono cafe oscuro. ABAJO A LA IZQUIERDA: masa hojaldrada dorada en capas, "
            "igual al hojaldre de la @img1. ABAJO A LA DERECHA: manzana verde cortada "
            "en gajos, fresca y jugosa. Los DOS CUADRANTES DE ARRIBA son OSCUROS y "
            "parejos entre si, sin brillos fuertes y sin detalle claro, para poder "
            "poner un texto claro encima. AL CENTRO del cuadro, sobre la cruz del "
            "mosaico, un trozo de strudel de manzana recien horneado, de masa "
            "hojaldrada dorada y en capas, espolvoreado con azucar flor, servido en el "
            "plato de ceramica verde oliva con anillos concentricos de la @img1: es el "
            "HEROE, nitido, bien iluminado y con una sombra suave propia. ENCUADRE, y "
            "es lo mas importante: EL 40% DE ARRIBA del cuadro queda OSCURO, LIMPIO y "
            "COMPLETAMENTE VACIO — ahi no hay plato, ni strudel, ni azucar, solo los "
            "dos cuadrantes oscuros de canela y nueces. El plato con el strudel ocupa "
            "como maximo el 55% del ancho del cuadro, va CENTRADO horizontalmente y su "
            "borde de arriba arranca recien despues de ese 40% de altura. La FRANJA DE "
            "ABAJO queda tranquila y sin detalle fuerte. Realista, macro, que se vea "
            "delicioso y apetitoso, "
            "alta calidad 4k. Sin ningun texto, sin letras, sin logotipos, sin tazas y "
            "sin manos."
        ),
    },
    # ── 22-09 · la foto REAL con el fondo cambiado a la terraza ──────────────
    #
    # ⛔ TIRADA 1 (`gen-22-09-primavera.png`) — DESCARTADA, y por dos defectos
    #    MEDIDOS, no por gusto:
    #
    #    1. **COSTURA.** El salto medio entre filas contiguas de la pieza es 3,48,
    #       y en y=1424 daba **23,90 — 6,9 veces la media**. Mirando el recorte se
    #       ve lo que la cifra dice: una recta perfecta de lado a lado donde el
    #       fondo de terraza termina y empieza la madera, sin perspectiva, sin
    #       sombra de contacto y sin transición de foco. Es el defecto que la
    #       skill de dirección de arte marca como inaceptable («dos imágenes
    #       pegadas dejan un salto de brillo en una fila»). Pedir «una mesa» sin
    #       más invita a pegar un plano recto — es la MISMA trampa que la del
    #       brindis del 18-09, donde «los dos tercios de abajo son MESA» produjo
    #       una costura a media pieza.
    #    2. **EL TERCIO DE ARRIBA SALIÓ DEMASIADO CLARO.** Pedir el fondo
    #       «luminoso» —que es la palabra del brief— dio bokeh verde muy claro
    #       más una lona de quitasol pálida ocupando media banda: luminancia
    #       media L=163–201 y el beige `#FFF9EB` en **1,57–1,75:1**, o sea
    #       ilegible. El café llegaba a 2,72:1, pero la lona pálida parte la
    #       banda en dos y ninguna tinta se lee de lado a lado. Es exactamente el
    #       caso de la pieza del cowork.
    #
    #    O sea: el titular de Between ancla en y=441 y necesita esa banda. Un
    #    fondo «luminoso» y un titular beige arriba son incompatibles, así que la
    #    luz se conserva PERO ENTRANDO POR DETRÁS: follaje profundo a contraluz.
    #    Se mantiene «fresca y de primavera» y el beige recupera contraste.
    "22-09": {
        "salida": "gen-22-09-primavera",
        "refs": ["milkshake.jpg", "terraza.jpg", "terraza-ancha.jpg"],
        "prompt": (
            "Extiende la escena de la @img1 a formato vertical de historia 9:16. La "
            "copa alta de milkshake queda EXACTAMENTE IGUAL a la de la @img1: la misma "
            "copa de vidrio con pie, el mismo batido cremoso de color beige, el borde "
            "escarchado de coco, la frutilla apoyada en el borde y la bombilla negra. "
            "CAMBIA EL FONDO: en vez de la pared de piedra oscura, la terraza de la "
            "@img2 y la @img3 MUY desenfocada, con las plantas, el follaje y las "
            "ampolletas convertidos en manchas de luz. La copa esta apoyada sobre una "
            "mesa de madera oscura de la terraza vista EN PERSPECTIVA y en angulo, con "
            "su propia sombra de contacto bajo el pie de la copa, y la mesa va "
            "perdiendo foco hacia el fondo. ENCUADRE, y es lo mas importante: la copa "
            "COMPLETA —vidrio, batido, borde de coco, frutilla y bombilla incluidos— "
            "ocupa SOLO EL 45% INFERIOR del cuadro y va centrada; la punta de la "
            "bombilla NO pasa del 55% de altura. EL 55% DE ARRIBA del cuadro es "
            "follaje verde PROFUNDO y OSCURO a contraluz, continuo de lado a lado, muy "
            "desenfocado y homogeneo, COMPLETAMENTE VACIO: ahi no hay copa, ni "
            "bombilla, ni frutilla, ni quitasol, ni toldo, ni cielo, ni edificios, ni "
            "ninguna superficie clara. La luz entra POR DETRAS del follaje, calida y de "
            "primavera. Es UNA SOLA fotografia "
            "continua: NINGUNA linea horizontal recta que cruce todo el cuadro, ningun "
            "borde recto y ningun plano pegado. Poca profundidad de campo. Realista, "
            "alta calidad 4k. Sin ningun texto, sin letras, sin logotipos, sin "
            "personas y sin manos."
        ),
    },
}


def generar(clave: str, sufijo: str) -> None:
    e = ESCENAS[clave]
    refs = [str(REFS / r) for r in e["refs"]]
    faltan = [r for r in refs if not Path(r).is_file()]
    if faltan:
        sys.exit("x faltan referencias:\n  " + "\n  ".join(faltan))
    out = SALIDA / f"{e['salida']}{('-' + sufijo) if sufijo else ''}.png"
    print(f"\n=== {clave} -> {out.name}")
    print(f"    refs: {', '.join(e['refs'])}")
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", e["prompt"],
         "--out", str(out), "--aspecto", "story", "--resolucion", "4K",
         "--refs", *refs],
        cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit(f"x fallo la generacion de {clave}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cuales", nargs="*", choices=list(ESCENAS), default=None,
                    help="21-09 · 22-09 (vacio = las dos)")
    ap.add_argument("--sufijo", default="", help="para no pisar una tirada anterior")
    a = ap.parse_args()
    for c in (a.cuales or list(ESCENAS)):
        generar(c, a.sufijo)
    print("\nMIRALAS antes de usarlas. El strudel, con zoom: el producto es GENERADO.")


if __name__ == "__main__":
    main()

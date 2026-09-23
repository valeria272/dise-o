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
    # ── 22-09 · el milkshake REAL de Between, en la terraza ─────────────────
    #
    # ⛔⛔ RONDA 2 (09-09-2026) — EL PRODUCTO ESTABA MAL, y no era un detalle.
    #
    # Eli: «te dejo acá la sesión que tenemos de cómo son» + «el fondo debe ser
    # mejor realizado». Las dos cosas mandaron a rehacer la pieza entera.
    #
    # La ronda 1 usó `Between-214.jpg` de la sesión del 3 de enero, que es una
    # foto REAL del cliente — pero **no es un milkshake de Between**. Comparado
    # con la sesión que dejó Eli (`raw/hilton/between/milkshakes-jun2025/`, 35
    # fotos de Ámbar Gallardo del 30-06-2025, iPhone 4284×5712):
    #
    # | | Between-214 (lo que usé) | el milkshake REAL |
    # |---|---|---|
    # | copa | *hurricane* curva, de cóctel | **acanalada, alta, con PIE ESCALONADO** de vidrio labrado |
    # | borde | escarchado de coco | limpio, sin escarchar |
    # | bombilla | negra | **no lleva** |
    # | adorno | frutilla en el borde | **brocheta de madera con moras y una frambuesa** |
    # | sabores | uno, beige | **moras (morado) · café · maracuyá · manzana** |
    # | dónde | mesa de madera, muro de piedra | **la barra**, con la estantería de botellas al fondo |
    #
    # O sea que era el mismo error de clase que la taza KIMBO y el vaso To Go
    # antiguo: **una foto real del cliente no garantiza que sea el producto
    # vigente.** La compuerta que faltó no es «¿es real?», es «¿es ESTE
    # producto?» — y se contesta pidiendo la sesión del producto, no buscando
    # por parecido en el banco general.
    #
    # Se eligió el de MORAS (`IMG_3607`, la toma más completa: copa entera, pie
    # visible, brocheta nítida) por dos razones: el morado es el que más lee
    # «primavera» junto al verde del follaje, y separa la pieza de la del 21-09,
    # que es toda marrón y verde manzana. Las otras tres están disponibles.
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
        "refs": ["milkshake-real.jpg", "terraza.jpg", "terraza-ancha.jpg"],
        "prompt": (
            "Fotografia vertical de historia 9:16 de un milkshake en la terraza de una "
            "cafeteria. EL PRODUCTO ES EL DE LA @img1 Y NO CAMBIA: la misma copa alta "
            "de vidrio transparente ACANALADA, con el mismo PIE ESCALONADO de vidrio "
            "labrado; el mismo batido espeso de MORAS, de color morado, lleno hasta el "
            "borde; y apoyada en el borde la misma brocheta de madera clara con DOS "
            "MORAS y UNA FRAMBUESA. La copa no lleva bombilla. "
            "ES UN PRIMER PLANO DE PRODUCTO: la camara esta A LA ALTURA DE LA MESA y "
            "cerca de la copa. La MESA DE MADERA OSCURA de la terraza ocupa toda la "
            "franja inferior del cuadro, de lado a lado, nitida junto al pie de la copa "
            "y perdiendo foco hacia atras. La copa esta apoyada SOBRE LA MESA, nunca en "
            "el suelo, y se ve del tamano de un vaso de mesa, no gigante. Detras de la "
            "mesa, la terraza de la @img2 y la @img3 MUY desenfocada, convertida en "
            "manchas de verde y de luz calida: NO se distingue ninguna silla, ninguna "
            "baldosa, ningun piso ni ningun mueble nitido. "
            "UNA SOLA LUZ para toda la escena: el sol de primavera entra POR DETRAS del "
            "follaje y un poco desde un costado, asi que la copa recibe un CONTRALUZ "
            "calido que le dibuja el canto del vidrio, un brillo suave en la superficie "
            "del batido, y proyecta sobre la madera una SOMBRA DE CONTACTO real bajo el "
            "pie, en la direccion contraria a la luz. "
            "ENCUADRE, y es lo mas importante: la copa COMPLETA, con su brocheta y sus "
            "moras incluidas, ocupa SOLO EL 45% INFERIOR del cuadro y va centrada; nada "
            "de la copa pasa del 55% de altura. EL 55% DE ARRIBA del cuadro es follaje "
            "verde PROFUNDO y OSCURO a contraluz, continuo de lado a lado, muy "
            "desenfocado y homogeneo, COMPLETAMENTE VACIO: ahi no hay copa, ni frutas, "
            "ni quitasol, ni toldo, ni cielo, ni edificios, ni ninguna superficie clara. "
            "NINGUNA linea horizontal recta que cruce todo el cuadro, ningun borde recto "
            "y ningun plano pegado. Poca profundidad de campo, realista, fotografia de "
            "producto de alta gama, alta calidad 4k. Sin ningun texto, sin letras, sin "
            "logotipos, sin personas y sin manos."
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

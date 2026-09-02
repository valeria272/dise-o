#!/usr/bin/env python3
"""Genera la foto de la SLIDE 2 del carrusel Cowork de Between con Magnific.

⭐ NUEVO 02-09-2026 — RONDA 7. Esta slide es «la del medio que hace ruido».

Lo que dijo el cliente por WhatsApp (Scarlette, 10:37):

    «en este carrusel siento que las fotos estan inconexas, no digo que se unan
     ni nada, pero como que no tienen el mismo estilo (quizás sea la de al medio
     que es foto montaje que hace el ruido)»
    «el resto se ve ok, pero cambiaria las fotos para que tenga mas cohesion»

Y tiene razón, se ve al ponerlas juntas. La slide 2 traía
`mesa-laptop-cafe.jpg`: un **bodegón de estudio** —macro, poca profundidad,
vapor, comida estilizada— sobre un **fondo verde bokeh INVENTADO**, mientras las
otras tres son interiores reales. Cuatro registros fotográficos distintos en un
carrusel de cuatro slides.

⛔ El diagnóstico fino: lo falso NO eran los objetos, era el FONDO
-----------------------------------------------------------------
La mesa, el notebook y el vaso Between de esa foto son reales. Lo que delataba
el montaje era el muro verde desenfocado inventado detrás, que además **imitaba
el muro vegetal de la portada** — o sea que el carrusel repetía escenario con
una copia falsa. Por eso se lee como pegote.

Así que no se tira el concepto: se rehace la escena con el ambiente REAL entrando
por referencia, que es exactamente la receta que el cliente **ya aprobó** en la
FEED G del 7-sep (`clients/hilton/CLAUDE.md`, «el ambiente se transfiere por
REFERENCIA, no con adjetivos»).

Por qué esta slide igual lleva mesa, notebook y taza
----------------------------------------------------
No es capricho: es el pedido de la RONDA 6 de Scarlette sobre esta misma slide.

    «Slide2: y acá estamos hablando de café como tal, yo cambiaria la imagen
     donde se vea una mesa con un pc y un café»

Y coincide con la regla 2 del manual —«la foto tiene que contener los sustantivos
del texto»—: el copy dice **mesa** («Encuentra tu mesa y trabaja a tu ritmo») y
**café** («Al menos que sea con buen café»). Los dos tienen que estar en cuadro.

⚠️ Y el pc+café con mesa **no existe en el banco**: quedó demostrado en la ronda
5 (`espacios/` son 12 tomas de arquitectura vacía, y de los 91 fotogramas del
2.º piso los que tienen gente son huéspedes con la cara reconocible). Ahí sí se
justifica generar. Decisión de Eli, 02-09.

Las restricciones, una por una y de dónde salen
-----------------------------------------------
  1. **CERO personas.** No las pide el copy y cada mano es una posibilidad de
     error anatómico — «hay una mano de más» ya fue un rechazo en este carrusel.
     Una mesa servida y vacía cuenta «encuentra tu mesa» mejor que alguien
     ocupándola.
  2. **El muro vegetal va MUY desenfocado.** Es el mismo rincón que la portada,
     y eso es legal —el manual permite «un plano general y un bodegón del mismo
     lugar»— pero SOLO si el fondo no compite: tiene que leerse como manchas de
     verde, no como el muro otra vez.
  3. **Taza blanca total**, sin raya, sin letras. Es la regla KIMBO: el cliente
     acaba de repetir que «ya no servimos en esas tazas».
  4. **Ningún logotipo generado.** La IA hace ambiente y fondo, nunca el
     producto ni la marca. Por eso la taza es cerámica lisa y no un vaso To Go:
     un vaso pide logo, y el logo de la IA es el que el cliente reclamó tres
     veces. Si algún día lleva vaso, se estampa con `between-logo-vaso.py`.
  5. **Luz neutra, sin filtro cálido.** Reclamo textual de Scarlette en este
     carrusel («se ven quemadas y con un filtro medio raro»). Después se grada
     con `--perfil neutro`.
  6. **El tercio de ARRIBA queda limpio.** `Cowork2` ancla el bloque arriba,
     igual que las slides 3 y 4.

Uso:
    python scripts/between-slide2-magnific.py                # genera
    python scripts/between-slide2-magnific.py --solo-prompt  # sólo imprime
"""
import argparse
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# El rincón REAL del muro vegetal, que es el que va detrás. Tres tomas del mismo
# lugar para que el generador no invente una cafetería de stock:
#   · IMG_1148-3 — el fotograma que quedó en la PORTADA (mismo encuadre, sin gente)
#   · IMG_1148-1 — la misma toma un segundo antes, otro ángulo del muro
#   · HDT_50     — la foto PROFESIONAL del Winter Garden. ⭐ Es la única de las 12
#                  de `espacios/` que Eli identificó como Between (01-09), así que
#                  es la única que se puede usar sin preguntar.
REFS = [
    RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_1148-3.jpg",
    RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_1148-1.jpg",
    RAIZ / "raw/hilton/between/espacios/HDT_50.jpg",
]

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/cowork-mesa-trabajo.png"

PROMPT = (
    # ── el lugar: el rincón del muro vegetal de las referencias ──
    "Photorealistic vertical photograph taken inside the plant-wall corner of the "
    "café shown in the reference images. Foreground: a reclaimed dark wood table "
    "top seen from the seat of someone about to work at it, shot at eye level from "
    "the chair. "
    # ── lo que hay sobre la mesa: mesa + pc + café, y nada más ──
    "On the table there is an open laptop seen from behind at a three-quarter "
    "angle, its screen dark and switched off, plain brushed aluminium, and next to "
    "it a white ceramic coffee cup on a white saucer with a rosetta in the crema. "
    "A small notebook and a pen lie beside them. Nothing else on the table: no "
    "plates of food, no sandwich, no cake, no breakfast spread, no phone. "
    # ── CERO personas ──
    "The table is set and unoccupied: there is NOBODY in the picture. No people, "
    "no faces, no heads, no hands, no arms, no fingers, no silhouettes and no "
    "reflections of people anywhere in the image. "
    # ── el fondo: el muro vivo, pero MUY desenfocado ──
    #
    # ⚠️ NO TOCAR ESTA REDACCIÓN SIN MIRAR EL RESULTADO. Se probó una 2ª versión
    # que pedía que el muro «FILLS the entire background from edge to edge» y que
    # el techo traslúcido saliera de cuadro, buscando un tercio de arriba oscuro.
    # Salió PEOR: al pedirle que llenara el fondo, el modelo lo devolvió
    # ENFOCADO —se le cuentan las hojas— y un muro nítido detrás se lee como
    # telón pegado, que es exactamente el «esto es un montaje» del que venimos
    # escapando. El bokeh es lo que hace creíble la foto, y se consigue con
    # «dissolved into soft blurred blobs», no mandándole llenar el cuadro.
    #
    # Y el motivo por el que se buscaba oscurecer arriba resultó falso: MEDIDO en
    # la banda del titular (y 0,13–0,46 del alto), esta imagen da luma 117,5 con
    # 19,3 % de píxeles sobre 180 — prácticamente lo mismo que la portada nueva
    # (103,6 · 17,3 %) y que la slide 3 (105,1 · 15,4 %), que llevan el mismo
    # titular beige y se leen bien. El techo blanco queda ARRIBA del bloque de
    # texto, no debajo.
    "Behind the table the living green plant wall of the reference images and the "
    "translucent roof light are VERY strongly out of focus, dissolved into soft "
    "blurred blobs of green and warm light. The background must read as colour and "
    "atmosphere only - individual leaves, planters and the grid of the wall must "
    "NOT be identifiable. Very shallow depth of field: only the table top, the "
    "laptop and the cup are sharp. "
    # ── luz neutra, el cliente rechazó el filtro cálido ──
    "Natural neutral daylight from the roof above, balanced white point, "
    "true-to-life colour with no warm orange cast and no colour filter, gentle "
    "contrast, no blown highlights. "
    # ── el aire de arriba, donde se apoya el bloque de texto ──
    "The upper third of the frame is calm and almost empty - just the softly "
    "blurred green and light - leaving clear negative space with no detail there. "
    "Editorial hospitality photography, 35mm, photorealistic. "
    # ── prohibiciones duras ──
    "The cup and saucer are completely plain, pure white, with no stripe, no "
    "pattern and no lettering of any kind. No brand marks on the laptop. No text, "
    "no logos, no signage, no watermark anywhere in the image."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — esta slide es la que el cliente señaló:
  1. ¿Se identifica el MURO VEGETAL detrás? Si se le cuentan las hojas o se ve
     la reja, está MUY POCO desenfocado y repite el escenario de la portada.
     Tiene que leerse como manchas de verde. Es el punto que decide la pieza.
  2. ¿Hay alguna persona, mano o dedo? Tiene que haber CERO.
  3. ¿La taza está BLANCA TOTAL, sin raya ni letras? (regla KIMBO)
  4. ¿El notebook está SIN logotipo? Ninguna marca inventada.
  5. ¿Se lee TRABAJO y no desayuno? Si aparece comida desplegada, se descarta —
     es el registro de bodegón de estudio que el cliente acaba de rechazar.
  6. ¿El tercio de arriba está limpio? Ahí va el bloque de texto.

Si pasa las seis:
  python scripts/between-gradar.py public/assets/hilton/between/ia-sept/cowork-mesa-trabajo.png \\
      --perfil neutro --recorte45 --top 0.5 --ancho 2250 \\
      --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre cowork-mesa-trabajo.jpg
  → apuntar la `foto` de Cowork2 en src/compositions/hilton/BetweenSeptiembre.tsx
  → python scripts/between-rendir.py BW-F-Cowork-2 --salida out/hilton-between-r7
  → python scripts/between-qa.py out/hilton-between-r7
  → mirar las 4 slides JUNTAS: la ronda 7 es sobre COHESIÓN, y eso no se
    verifica pieza por pieza.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-prompt", action="store_true",
                    help="imprime el prompt para pegarlo a mano en magnific.com")
    ap.add_argument("--out", default=str(SALIDA))
    a = ap.parse_args()

    if a.solo_prompt:
        print(PROMPT)
        return

    faltan = [r for r in REFS if not r.is_file()]
    if faltan:
        sys.exit("✗ Faltan las fotos de referencia del muro vegetal:\n  " +
                 "\n  ".join(str(f) for f in faltan) +
                 "\n\n`raw/` no viaja en git: se bajan con\n"
                 "  python scripts/drive-carpeta.py 1FTgwu_wHwVkKk55nlDrao-LkDdKNDwID "
                 "raw/hilton/between/espacios")

    # `pro` = Nano Banana Pro: el único modo que acepta imágenes de referencia,
    # que es justo lo que hace que el lugar sea Between y no una cafetería de
    # stock. `--aspecto post` = 3:4; la pieza es 4:5 y `FotoFondo` recorta con
    # `cover`, así que sobra alto y no se estira nada.
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--out", a.out, "--aspecto", "post", "--resolucion", "4K",
           "--refs", *[str(r) for r in REFS]]
    print("->", " ".join(cmd[:4]), "...\n")
    r = subprocess.run(cmd, cwd=RAIZ)
    if r.returncode:
        sys.exit(r.returncode)

    print(QA)


if __name__ == "__main__":
    main()

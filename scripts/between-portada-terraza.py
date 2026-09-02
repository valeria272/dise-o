#!/usr/bin/env python3
"""Genera la foto de la PORTADA del carrusel Cowork de Between — la terraza real.

⭐ NUEVO 02-09-2026 — RONDA 8. Pedido de Eli:

    «Usa de fondo la terraza de between, con café en mesa y laptop + celular
     que sea estilo cowork pero mejor editada la foto.»

De dónde sale la foto, y por qué esta vez SÍ se puede usar
-----------------------------------------------------------
La base es **`espacios/HDT_52.jpg`**, foto profesional de 6719×4479.

⚠️ El manual decía (§7) que de las 12 fotos de `espacios/` **sólo HDT_50 estaba
identificada como Between**, y advertía: «varias no son de Between —la barra de
ónix parece de QB, y varias son del hotel—: usar una ajena es repetir el error
que el cliente viene reclamando. Preguntar antes.»

**Se verificó y quedó resuelto el 02-09-2026, mirando la propia foto a
resolución completa:** en el recorte `(4900,2100)-(5900,2600)` hay un pizarrón
que dice, con el logotipo real y su **E quebrada**:

    BƎTWEEN / — COFFEE & BAR — / Desde las 17 hrs. / Promos

Y en `HDT_51`, que es la MISMA terraza desde el otro extremo, los portamenús de
mesa dicen «BƎTWEEN · CAFÉ A $1.000». O sea: **HDT_51 y HDT_52 son la terraza de
Between**, no la de QB. Queda escrito en `clients/hilton/CLAUDE.md` §7.

El recorte: (200, 900) → (3063, 4479), o sea 2863×3579 = 4:5 exacto
--------------------------------------------------------------------
Se eligió MIDIENDO contra las bandas de la gramática, no a ojo. `Cowork1` ancla
el bloque **abajo**: el texto ocupa de 0,55 a 0,92 del alto y el lockup de 0,05 a
0,14. Con ese molde encima, de los 12 encuadres 4:5 posibles éste es el único que
deja las tres cosas donde tienen que estar:

  · **0,05–0,14 → la lona de la sombrilla.** Oscura y lisa: el logo blanco lee
    sin necesidad de velo extra.
  · **0,15–0,52 → la terraza.** Vegetación, el árbol, las ampolletas Edison y el
    interior cálido al fondo. Acá va la mesa de trabajo.
  · **0,53–0,65 → la tapa de la mesa**, y de 0,65 abajo el suelo de piedra,
    parejo y sin detalle. El titular y la caja taupe caen ahí.

⛔ Los otros 11 encuadres se descartaron por lo mismo: la mesa quedaba DENTRO de
la banda del texto (0,63–0,75 a altura completa), o sea que el titular tapaba
justo lo que el pedido quiere mostrar.

Por qué la laptop y el café se GENERAN y el lugar NO
-----------------------------------------------------
La terraza de las 12 tomas de `espacios/` está **vacía**: es fotografía de
arquitectura, sin una taza ni un notebook en toda la sesión. Y el 2.º piso sólo
existe en video. O sea que «café en mesa y laptop + celular» no está en el banco
—el mismo callejón de la ronda 7 con la slide 2— y ahí sí se justifica generar.

La regla del estudio se respeta al pie: **la IA hace ambiente y objetos
genéricos, nunca el producto, el logo ni un dato.** Acá el lugar es una foto real
y lo generado son una laptop sin marca, una taza blanca lisa y un celular: cero
logotipos, cero letreros, cero cifras.

⚠️ Y la escena NO repite la slide 2. Es la lección de cohesión de la ronda 7
(«las fotos están inconexas… la del medio hace ruido»): la slide 2 es un
**bodegón a la altura del asiento**, mesa + pc + taza en primer plano. Ésta es un
**plano general del lugar** donde el puesto de trabajo es un detalle dentro de la
terraza. Portada = dónde estás; slide 2 = tu mesa. Distinto plano, mismo lugar.

Las restricciones, una por una y de dónde salen
------------------------------------------------
  1. **La foto base manda.** Se le pasa el recorte como primera referencia y se
     le pide reproducirlo; lo único que cambia es lo que hay sobre la mesa. Si
     el generador reinventa la terraza, la toma se descarta: el punto de usar
     HDT_52 es que el lugar sea el real.
  2. **CERO personas.** El cliente ya rechazó la portada anterior por «mostramos
     a esas personas» (derechos de imagen) y «hay una mano de más» fue otro
     rechazo de este mismo carrusel.
  3. **Taza blanca total**, sin raya ni letras — regla KIMBO, que el cliente
     repitió en la ronda 7.
  4. **Ningún logotipo**: ni en la laptop, ni en el celular, ni en la taza. Y
     nada de letreros nuevos: el pizarrón real de Between queda FUERA de este
     recorte, así que no hay texto que el modelo pueda romper.
  5. **Luz neutra, sin filtro cálido.** Reclamo textual de Scarlette sobre este
     carrusel («se ven quemadas y con un filtro medio raro»). Después se grada
     igual con `--perfil neutro`.
  6. **La pantalla de la laptop, apagada.** Una pantalla encendida obliga a
     inventarle contenido —y contenido inventado es texto inventado.

Uso:
    python scripts/between-portada-terraza.py                # genera
    python scripts/between-portada-terraza.py --solo-prompt  # sólo imprime
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

# El recorte 4:5 de la terraza real va PRIMERO: es la imagen que hay que
# reproducir. Las otras dos son la misma terraza desde otro punto, para que el
# modelo tenga el lugar completo y no se invente el fondo que queda fuera.
BASE = RAIZ / "raw/hilton/between/espacios/_terraza-base-45.jpg"
REFS = [
    BASE,
    RAIZ / "raw/hilton/between/espacios/HDT_52.jpg",
    RAIZ / "raw/hilton/between/espacios/HDT_51.jpg",
]

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/cowork-terraza.png"

PROMPT = (
    # ── la orden principal: esto es una EDICIÓN, no una escena nueva ──
    "Reproduce the FIRST reference image exactly as it is - the same outdoor "
    "café terrace, the same dark umbrella canopies overhead, the same hanging "
    "Edison bulbs, the same lush green planters and small tree, the same dark "
    "slatted table with its metal chairs, the same stone paved floor, the same "
    "camera position, the same framing and the same lighting. Do not redesign "
    "the place, do not move the furniture, do not change the architecture. "
    # ── el único cambio: la mesa pasa a estar en uso ──
    "The ONLY change: the dark slatted table in the foreground is now set up for "
    "someone working. On that table place ONE single open laptop - exactly one, "
    "never two - turned towards the camera at a slight three-quarter angle so "
    "that its wide switched-off dark SCREEN faces us and the keyboard is "
    "visible. Do not show the closed back of the lid. The laptop is the largest "
    "object on the table, plain brushed aluminium with no brand mark. Beside it "
    "a plain pure white ceramic coffee cup on a matching white saucer, with "
    "coffee in it; and a black "
    "smartphone lying flat on the table immediately to the RIGHT of the saucer, "
    "screen off. A small closed notebook and a pen may lie beside them. "
    # ⚠️ Sin las dos frases que siguen el modelo deja el celular en la ESQUINA
    # CERCANA de la mesa — pasó en la 1.ª generación. Ahí cae dentro de la banda
    # del titular (la script arranca en 0,53 del alto) y el texto lo tapa. El
    # celular es un objeto que Eli pidió por nombre: tapado no sirve.
    "ALL of these objects - laptop, cup, saucer, phone and notebook - are "
    "grouped together on the FAR half of the table top, beyond the middle of "
    "the table. The NEAR half of the table, the edge closest to the camera, is "
    "completely EMPTY: nothing at all rests on it. "
    "The objects are in sharp focus and lit by the same daylight as "
    "the rest of the scene, casting soft shadows onto the dark slats. "
    "Nothing else on the table: no food, no plates, no breakfast, no bottles. "
    # ── CERO personas ──
    "The table is set and unoccupied: there is NOBODY in the picture. No people, "
    "no faces, no heads, no hands, no arms, no fingers, no silhouettes, and no "
    "people visible through the glass in the background. "
    # ── las bandas de la gramática ──
    "The top of the frame stays as it is: the plain dark umbrella canopy, calm "
    "and free of detail. The bottom of the frame stays as it is: the plain stone "
    "paved floor, calm and free of detail. "
    # ── luz neutra, el cliente rechazó el filtro cálido ──
    "Natural neutral daylight, balanced white point, true-to-life colour with no "
    "warm orange cast and no colour filter, gentle contrast, no blown "
    "highlights, nothing overexposed. "
    # ── prohibiciones duras ──
    "Photorealistic architectural hospitality photography, sharp throughout, "
    "high detail. No text, no lettering, no logos, no brand marks, no signage, "
    "no menu boards, no price tags and no watermark anywhere in the image. In "
    "particular there is NO menu card and NO standing sign on the table."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — 6 puntos:
  1. ¿Es LA MISMA terraza de la foto base? Mismas sombrillas, mismas ampolletas,
     mismo árbol, misma mesa. Si el generador inventó otro local, se descarta:
     todo el punto de esta pieza es que el lugar sea el real de Between.
  2. ¿Hay alguna persona, mano o dedo? Tiene que haber CERO.
  3. ¿La taza está BLANCA TOTAL, sin raya ni letras? (regla KIMBO)
  4. ¿La laptop está SIN logotipo y con la pantalla APAGADA?
  5. ¿Apareció algún letrero, texto o número inventado? Ninguno.
  6. ¿La laptop y la taza quedan ARRIBA de 0,55 del alto? Ahí empieza el
     titular: lo que caiga más abajo lo tapa el texto.

Si pasa las seis:
  python scripts/between-gradar.py public/assets/hilton/between/ia-sept/cowork-terraza.png \\
      --perfil neutro --recorte45 --ancho 2250 \\
      --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre cowork-terraza.jpg
  → apuntar la `foto` de Cowork1 en src/compositions/hilton/BetweenSeptiembre.tsx
  → python scripts/between-rendir.py BW-F-Cowork-1 --salida out/hilton-between-r8
  → python scripts/between-qa.py out/hilton-between-r8
  → mirar las 4 slides JUNTAS: la cohesión no se verifica pieza por pieza.
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
        sys.exit("✗ Faltan fotos de referencia de la terraza:\n  " +
                 "\n  ".join(str(f) for f in faltan) +
                 "\n\n`raw/` no viaja en git: se bajan con\n"
                 "  python scripts/drive-carpeta.py 1FTgwu_wHwVkKk55nlDrao-LkDdKNDwID "
                 "raw/hilton/between/espacios\n"
                 "y el recorte base se rehace con `--rehacer-base`.")

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)

    # `pro` = Nano Banana Pro: el único modo que acepta imágenes de referencia,
    # que es justo lo que hace que el lugar sea la terraza de Between y no una
    # terraza de stock. `--aspecto post` = 3:4; la pieza es 4:5 y `FotoFondo`
    # recorta con `cover`, así que sobra alto y no se estira nada.
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--aspecto", "post", "--resolucion", "4K", "--out", a.out,
           "--refs", *[str(r) for r in REFS]]
    print("→ Nano Banana Pro · 3:4 · 4K · 3 referencias de la terraza real")
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()

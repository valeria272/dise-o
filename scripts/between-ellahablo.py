#!/usr/bin/env python3
"""La foto del post FEED J — «ELLA HABLÓ / ELLA ESCUCHÓ» (11-sep, S2).

⭐ RONDA 9 · 03-09-2026. `FEED!J16` pasó a EN CAMBIOS. Los dos comentarios están
VIGENTES enteros (la celda no trae nada tachado):

    Cliente (`FEED!J15`):
      «Pondría un café que se vea más lindo, algo con arte late y el otro se
       tiene que ver como que en algún momento hubo café en la taza jasajs.
       En cuanto al diseño, me gustaría ver textos más limpios (sin el recuadro
       atrás) y que el de Ella habló esté más cerca de su respectiva taza»

    Scarlette (nativo, 31-08):
      «esta mal desarrollada la imagen, se ve una taza casi arriba de la otra,
       la idea es que se vea la interacción de las personas imagen aun que sea
       sus manos. La taza de "ella escucho" tiene el plato enorme y se ve
       completamente limpio, se tiene que ver que una consumio más café que la
       otra.»

Son CINCO defectos y la escena nueva los ataca uno por uno:

  1. «una taza casi arriba de la otra» → las dos van **separadas en diagonal**,
     cada una con su espacio de mesa alrededor. Es lo que además hace que el
     chiste se lea: si se pisan, no se comparan.
  2. «que se vea la interacción de las personas, aunque sea sus manos» → entran
     DOS manos, una por lado, cada una junto a SU taza.
  3. «un café que se vea más lindo, algo con arte latte» → la taza llena lleva
     un rosetón nítido.
  4. «el otro… como que en algún momento hubo café» → la otra queda casi vacía,
     con el cerco de café seco en la pared interior y una gota en el platillo.
  5. «el plato enorme y completamente limpio» → mismo juego de loza en las dos,
     el platillo del tamaño que le corresponde, y con marcas de uso.

⚠️ Y las dos manos son **de mujer**. No es un detalle decorativo: el copy que
va con la pieza dice «Etiqueta a esa amiga con la que un café nunca es solo un
café», o sea que la escena es de dos amigas. La primera generación puso abajo
una mano grande y venosa que leía como masculina, y eso contradice el texto —
el manual lo tiene escrito como defecto, no como gusto (§3 bis, «la foto de una
slide contradice su texto»).

⚠️ LAS MANOS son el riesgo conocido de esta marca. El manual (ronda 6, §3) dice:
«hay una mano de más» ya fue un rechazo, y se descartaron dos versiones porque al
zoom la mano no resolvía. Acá el cliente PIDE manos, así que no se pueden evitar;
lo que sí se puede es pedir **exactamente dos**, cada una entera, con los dedos
separados y el nudillo visible, y **revisarlas al 300–400 %** antes de usar la
imagen. Dos manos y ni una más: nada de una tercera al borde del cuadro.

⛔ CERO rostros: la sesión de modelos de julio 2023 está prohibida por derechos
de imagen y el cliente ya rechazó una portada por «mostramos a esas personas».

De dónde sale el realismo
--------------------------
Se generan las tazas, pero **la mesa y la loza salen de fotos reales del
cliente**, que van como referencia: `Between-20.jpg` (cenital del café con arte
latte sobre la mesa de listones) y `Between-42.jpg`. Así la mesa es la de
Between y no una mesa de stock — que es el reclamo transversal de la ronda.

⚠️ El logotipo KIMBO de las tazas: acá no aparece porque la toma es CENITAL, que
es donde el logotipo queda en la pared exterior de la taza y la cámara no lo ve.
Ver `scripts/between-quitar-kimbo.py`.

Uso:
    python scripts/between-ellahablo.py
    python scripts/between-ellahablo.py --solo-prompt
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

REFS = [
    RAIZ / "raw/hilton/between/platos-ene/Between-20.jpg",
    RAIZ / "raw/hilton/between/platos-ene/Between-42.jpg",
]
SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/j-dos-tazas.png"

PROMPT = (
    # ── el lugar: la mesa real del cliente ──
    "A photorealistic overhead top-down photograph of a café table, shot straight "
    "from above. The table is the one in the reference images: dark stained "
    "wooden slats running vertically, with the same grain and the same warm "
    "interior light. "
    # ── las dos tazas, separadas y distintas ──
    "On it, TWO white ceramic cups on matching white saucers, clearly SEPARATED "
    "and placed on a diagonal - one in the LOWER LEFT of the frame, the other in "
    "the UPPER RIGHT - with plenty of bare table between them. They never touch "
    "and never overlap. Both cups and both saucers are the SAME size and the "
    "same plain white china. "
    "The LOWER LEFT cup is FULL to the brim with cappuccino and has a crisp, "
    "well defined leaf latte art rosetta on top: it looks freshly served and "
    "barely touched. "
    "The UPPER RIGHT cup is almost EMPTY: only a thin film of coffee left at the "
    "bottom, a dried brown tide ring staining the inside wall, a faint lipstick-"
    "free smudge on the rim, and one small dried coffee drop on its saucer. It "
    "must be obvious at a glance that this one has been drunk and the other has "
    "not. "
    # ── las manos: exactamente dos ──
    "TWO human hands, and exactly two - no more, no third hand anywhere. One "
    "hand enters from the LOWER LEFT edge and rests on the table beside the full "
    "cup; the other enters from the UPPER RIGHT edge and holds the handle of the "
    "empty cup. Each hand is complete and natural, with five fingers clearly "
    "SEPARATED from one another, visible knuckles, correct anatomy and short "
    "clean natural nails. Both hands are adult WOMEN's hands, slender and of "
    "similar size to each other. No rings, no watches, no bracelets, no sleeves with "
    "logos. "
    "NO faces, no heads, no arms beyond the wrist, no bodies, no people visible: "
    "only the two hands at the edges of the frame. "
    # ── el aire, que es lo que hace legible el chiste ──
    "The centre of the frame is calm bare table so the two cups read as a "
    "comparison. Nothing else on the table: no phones, no food, no napkins, no "
    "sugar sachets, no spoons other than what is on the saucers. "
    # ── luz ──
    "Warm natural interior light from one side, soft shadows, balanced white "
    "point, no orange colour cast, no blown highlights, sharp focus throughout, "
    "high detail food photography. "
    # ── prohibiciones ──
    "No text, no lettering, no logos, no brand marks on the cups or saucers, no "
    "signage and no watermark anywhere in the image."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — 7 puntos. Los 3 primeros son los que ya
costaron un rechazo en esta marca:

  1. ⚠️ LAS MANOS, al 300–400 % sobre cada una. ¿Son EXACTAMENTE DOS? ¿Cada una
     tiene cinco dedos separados, con nudillos y uñas creíbles? Nada de masas
     lisas ni dedos fundidos. Si una no resuelve, se descarta la imagen entera:
     «hay una mano de más» ya fue un rechazo del cliente.
  2. ¿Se ve algún ROSTRO, cabeza o cuerpo? Tiene que haber CERO.
  3. ¿Aparece algún logotipo en las tazas? Ninguno — ni KIMBO ni inventado.
  4. ¿Las dos tazas están SEPARADAS, sin pisarse, en diagonal? Ése es el
     reclamo textual de Scarlette.
  5. ¿Se distingue de un vistazo cuál se tomó y cuál no? Arte latte nítido en
     una, cerco de café seco en la otra.
  6. ¿Los dos platillos son del MISMO tamaño? El reclamo era «el plato enorme».
  7. ¿Apareció texto, número o cubierto de más?

Si pasa los siete:
  python scripts/between-gradar.py public/assets/hilton/between/ia-sept/j-dos-tazas.png \\
      --perfil neutro --recorte45 --ancho 2250 \\
      --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre j-dos-tazas.jpg
  → apuntar la `foto` de EllaHablo en src/compositions/hilton/BetweenSeptiembre.tsx
  → RECOLOCAR las dos etiquetas: el cliente pidió «que el de Ella habló esté más
    cerca de su respectiva taza». Las x/y de `Etiqueta` son de la foto vieja.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-prompt", action="store_true")
    ap.add_argument("--out", default=str(SALIDA))
    a = ap.parse_args()
    if a.solo_prompt:
        print(PROMPT)
        return
    faltan = [r for r in REFS if not r.is_file()]
    if faltan:
        sys.exit("✗ Faltan las referencias de la mesa real:\n  " +
                 "\n  ".join(str(f) for f in faltan) +
                 "\n\nSe bajan de «3 ENERO _ PLATOS - DESAYUNOS»\n"
                 "  (16OSLgXsc_KABBHbPyBRGsG6zthRAcRaW)")
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--aspecto", "post", "--resolucion", "4K", "--out", a.out,
           "--refs", *[str(r) for r in REFS]]
    print("→ Nano Banana Pro · 3:4 · 4K · la mesa real de Between como referencia")
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()

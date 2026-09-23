#!/usr/bin/env python3
"""Genera la foto de la G1 del carrusel CUMPLEAÑOS de Between.

⭐ RONDA 8 — 02-09-2026. Comentario del cliente, en rojo en la grilla:

    «La foto está extraña, hagamos algo más similar a lo que hicimos el primer
     post, algo más natural que no se vea tan IA, en este caso creo que
     **menos es más**.»

Y Eli mandó la referencia exacta —una pieza que ya se publicó y funcionó—:
`raw/hilton/between/ediciones-ia-eli/magnific_anade-en-la-img1-detalles_rluqkTnxtc.png`
(Drive `12Lxot3IaQgXtT34m5q-ZeEamTqR6muRO`), con una indicación encima:

    «pero puede ser que se vea el capuccino y no la tapa»

Qué tenía de malo la anterior, y por qué la referencia lo arregla
-------------------------------------------------------------------
`cumple-manos-logo.png` es **DOS MANOS** pasándose el vaso sobre una mesa, en un
interior cálido. Tres problemas a la vez:

  1. **Dos manos = doble posibilidad de error anatómico.** El manual ya tiene la
     regla escrita («⭐ 3. Las manos: una sola, y verificada con zoom») y «hay una
     mano de más» fue un rechazo del propio cliente en el carrusel Cowork. Es
     literalmente el «menos es más» que pide ahora.
  2. **El gesto de entrega no es el mensaje.** El copy dice «¿Estás de
     cumpleaños? ESTE CAFÉ ES PARA TI»: el sujeto es el café, no la transacción.
  3. **Se veía a IA** justamente por eso: dos manos de origen distinto, sin
     cuerpo, encontrándose en el aire.

La referencia es lo contrario y por eso funcionó: **una sola mano** sosteniendo
el vaso a cámara, muro vegetal detrás, globos dorados y blancos, serpentinas y
confeti dorado. Es una foto de teléfono, no una producción.

El cambio que pide Eli sobre la referencia
--------------------------------------------
La referencia lleva el vaso **con la tapa negra puesta**. Ella quiere que se vea
el capuccino: **vaso kraft SIN TAPA**, con la leche y el arte latte a la vista
desde arriba. Es mejor para esta pieza — el café es el regalo, y con la tapa
puesta el regalo no se ve.

⚠️ El logotipo NO se genera: se ESTAMPA
-----------------------------------------
Regla dura del manual desde la ronda 4 —«los generadores devuelven el vaso sin
marca, y a veces con un logotipo inventado»; el cliente reclamó lo mismo en tres
piezas—. Acá se pide el vaso **liso** y después se le pone el logotipo real con
`scripts/between-logo-vaso.py`. Y la pieza va **sin lockup arriba**, porque el
vaso ya firma (regla 8 del encabezado del manual).

⚠️ «Serpentinas» en el prompt sale SERPIENTES
-----------------------------------------------
Está en la memoria del estudio y en el manual. En inglés se pide
`curled paper streamers`, nunca una traducción literal.

Uso:
    python scripts/between-cumple1-magnific.py
    python scripts/between-cumple1-magnific.py --solo-prompt
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

# La referencia va PRIMERO: es la pieza que el cliente señaló como el look bueno.
# Las otras dos dan el muro vegetal real, para que el fondo sea Between y no una
# jungla de stock.
REFS = [
    RAIZ / "raw/hilton/between/ediciones-ia-eli/magnific_anade-en-la-img1-detalles_rluqkTnxtc.png",
    RAIZ / "raw/hilton/between/espacios/HDT_50.jpg",
    RAIZ / "public/assets/hilton/between/fotos-gradadas/winter-garden.jpg",
]

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/cumple-mano-vaso.png"

PROMPT = (
    # ── el encuadre: el de la referencia, que es el que el cliente aprobó ──
    "Recreate the composition of the FIRST reference image as a natural, candid "
    "smartphone photograph. "
    "ONE single human hand and forearm entering from the bottom left corner, "
    "holding up a takeaway coffee cup towards the camera, at eye level. "
    # ── el cambio que pidió Eli: sin tapa, con el capuccino a la vista ──
    "The cup is a plain kraft brown paper takeaway cup with a white rim, and it "
    "has NO LID: the cup is open and tilted slightly towards the camera so that "
    "the cappuccino inside is clearly visible - creamy milk foam with a delicate "
    "latte-art rosetta on top. "
    # ── el vaso va LISO: el logotipo se estampa después ──
    "The kraft cup is completely BLANK and unbranded: no logo, no lettering, no "
    "text, no symbol and no pattern printed on it. Plain kraft paper only. "
    # ── UNA sola mano ──
    "There is exactly ONE hand in the picture, with exactly five fingers, "
    "anatomically correct. It is a woman's hand, slender, with smooth hairless "
    "skin and neat natural manicured nails, like the hand in the first reference "
    "image. The bare forearm is smooth, with no visible arm hair. No second "
    "hand, no other arm, no face, no other person anywhere in the frame. "
    # ── el fondo: el muro vegetal REAL ──
    "Behind the hand is the living green plant wall of the reference images - "
    "dense ferns and tropical foliage - softly out of focus. "
    # ── la fiesta, sin decir «serpentinas» ──
    "Floating in the background around the cup there are a few helium balloons "
    "in white and metallic gold, some thin curled gold paper streamers hanging "
    "down, and a light scatter of gold confetti flakes. The party elements are "
    "sparse and tasteful, kept to the background, never crowding the cup. "
    # ── el look: teléfono, no producción ──
    "Natural daylight, neutral white balance, no warm orange cast, no colour "
    "filter, gentle contrast, nothing overexposed. Shallow depth of field with "
    "the cup sharp and the background soft. It must look like a real casual "
    "photo taken on a phone, not a polished studio render and not an AI image. "
    # ── prohibiciones duras ──
    "No text, no lettering, no logos, no brand marks, no signage and no "
    "watermark anywhere in the image."
)

QA = """
MÍRALA CON ZOOM ANTES DE SEGUIR — el punto 1 decide la pieza:
  1. ¿Hay UNA SOLA mano, con CINCO dedos y sin dedo de más? Revisar al 300-400 %.
     «Hay una mano de más» ya fue un rechazo de este cliente.
  2. ¿El vaso está LISO, sin logo ni letras inventadas? Si trae algo, se descarta:
     el logotipo real se estampa después.
  3. ¿Se ve el CAPUCCINO —espuma y arte latte— y NO una tapa? Es el pedido de Eli.
  4. ¿Salen serpientes en vez de serpentinas? Pasó antes.
  5. ¿Se ve natural, de teléfono? Si parece render de estudio, el cliente lo
     vuelve a devolver: el reclamo textual es «que no se vea tan IA».

Si pasa las cinco, estampar el logotipo real y gradar:
  python scripts/between-logo-vaso.py \\
      public/assets/hilton/between/ia-sept/cumple-mano-vaso.png \\
      public/assets/hilton/between/ia-sept/cumple-mano-vaso-logo.png \\
      --centro <CX> <CY> --ancho <W>
  python scripts/between-gradar.py <la estampada> --perfil neutro --recorte45 \\
      --ancho 2250 --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre cumple-mano-vaso.jpg
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
        sys.exit("✗ Faltan referencias:\n  " + "\n  ".join(str(f) for f in faltan))

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--aspecto", "post", "--resolucion", "4K", "--out", a.out,
           "--refs", *[str(r) for r in REFS]]
    print("→ Nano Banana Pro · 3:4 · 4K · la referencia que mandó Eli + el muro real")
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()

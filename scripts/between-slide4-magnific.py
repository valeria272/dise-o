#!/usr/bin/env python3
"""Genera la foto de la SLIDE 4 del carrusel Cowork de Between con Magnific.

⚠️ REESCRITO 01-09-2026. La versión anterior generaba la escena EQUIVOCADA.

Venía escrito sobre un pedido de pasillo —«que se enfoque solo la mano
preparando café y se vea el espacio del bar»— y con eso la slide mostraba el
BAR. Pero el brief de la grilla (FEED, SLIDE 4 – SERVICIO) pide otra cosa:

    Visual: «Persona trabajando mientras un colaborador deja un café o plato
    sobre la mesa. El usuario continúa trabajando sin tener que levantarse.»

Son dos personas y una MESA, no un mesón: lo que se vende es el servicio a la
mesa, y por eso la escena tiene que pasar donde el cliente trabaja. Una mano
sola preparando café en el bar cuenta justo lo contrario —que el café se busca—
y además repite el escenario de la portada.

Todo lo que el cliente ya rechazó, convertido en restricción del prompt
-----------------------------------------------------------------------
Ronda 4, comentario C15 de Scarlette sobre esta misma slide:

    «el "A tu mesa" le tapa la cara a la chica y parece más que están
     desayunando que trabajando. Hay una mano de más en la imagen.»

De ahí salen las tres reglas que manda el prompt:

  1. **Ninguna cara.** La persona que trabaja va de espaldas o de tres cuartos
     desde atrás, y del colaborador sólo entran los brazos, cortados por el
     borde. Así el texto no puede taparle la cara a nadie —el defecto se vuelve
     imposible por construcción, no por diagramación— y de paso se esquiva el
     problema de derechos de imagen que el manual marca ⛔ para las sesiones con
     huéspedes reconocibles.
  2. **Trabajo, no desayuno.** El notebook abierto manda la mesa. Se prohíbe
     explícitamente el despliegue de desayuno: nada de platos de huevos, canastos
     de pan ni jugos. Lo que se deja es UNA taza o UN plato, que es el gesto del
     servicio.
  3. **Contar las manos.** «Hay una mano de más» es el error clásico del
     generador. El prompt lo prohíbe y el QA de abajo obliga a contarlas con
     zoom antes de usar la imagen.

Y las reglas permanentes del manual:

  - ⛔ **La taza KIMBO**: blanca total, sin raya negra y sin ninguna letra.
  - La IA hace **ambiente y fondo**, nunca el producto ni el logo.
  - «Debe verse como es Between realmente» → no se describe una cafetería
    genérica: se le pasan las fotos REALES del 2.º piso como `--refs` para que
    el lugar sea ése y no uno de stock.
  - **Sin filtro cálido.** Scarlette lo reclamó en este mismo carrusel, así que
    el prompt pide luz neutra y después se grada con `--perfil neutro`.

Uso:
    python scripts/between-slide4-magnific.py                # genera
    python scripts/between-slide4-magnific.py --solo-prompt  # sólo imprime

Necesita la clave de Freepik/Magnific en `~/.magnific_key`. ⚠️ Al 01-09 ese
archivo sigue teniendo texto de ejemplo (17 caracteres, empieza en «DISEÑO»), y
la API responde 401. La clave buena se saca en
`magnific.com/developers/dashboard/api-key` — **no es la de Freepik**.
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

# Las fotos REALES del 2.º piso: mesas de madera clara, sillones gris topo,
# muro de listones azul retroiluminado, fotos en blanco y negro enmarcadas,
# lámpara de arco con pantalla de fibra y piso de espiga. Son la referencia que
# evita que el generador invente una cafetería de stock.
REFS = [
    RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_8544.jpg",   # sala con mesas
    RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_8534-3.jpg",  # mesa y banqueta
    RAIZ / "public/assets/hilton/between/fotos-gradadas/mesa-cafe-2piso.jpg",  # mesa + taza
]

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/cowork-servicio-mesa.png"

PROMPT = (
    # ── el lugar: el 2.º piso real, no una cafetería genérica ──
    "Photorealistic vertical photograph taken inside the café work area shown in "
    "the reference images. Keep that exact room and nothing generic: light oak "
    "tables, soft grey-taupe upholstered armchairs, a wall of dark navy vertical "
    "slats lit from behind, framed black and white city photographs, a tall arc "
    "floor lamp with a woven fibre shade, herringbone floor. "
    # ── la acción: servicio A LA MESA, que es lo que vende la slide ──
    "At one of these tables, a person seen FROM BEHIND over the shoulder, working "
    "on an open laptop, hands on the keyboard, absorbed in the screen and not "
    "looking up. Their head is turned away from camera: the face is NOT visible, "
    "no facial features at all, only the back of the head and shoulders. "
    "A member of staff is setting down a single white ceramic cup on a white "
    "saucer onto the table beside the laptop. Of this second person only the "
    "FOREARMS AND HANDS enter the frame from the side, cropped by the edge above "
    "the elbows: no face, no head, no torso. "
    "Exactly two hands are placing the cup and exactly two hands rest on the "
    "laptop keyboard: four hands in total in the frame, all anatomically correct, "
    "five fingers each, no extra or duplicated limbs. "
    # ── trabajo, NO desayuno ──
    "The table is a work surface, not a breakfast table: the open laptop is the "
    "main object, with at most a notebook and a pen beside it. No plates of food, "
    "no breakfast spread, no bread baskets, no juice glasses, no cutlery. "
    # ── luz: neutra, el cliente rechazó el filtro cálido ──
    "Natural neutral daylight from a window, balanced white point, true-to-life "
    "colour with no warm orange cast and no colour filter, gentle contrast, "
    "nothing blown out. "
    # ── el aire de arriba, donde se apoya el bloque de texto ──
    "The upper third of the frame is calm and uncluttered - quiet wall and the "
    "softly blurred room behind - leaving clear negative space with no faces and "
    "no busy detail there. Shallow depth of field: the table, the laptop and the "
    "cup are sharp, the room behind is softly out of focus. "
    "Editorial hospitality photography, 35mm, photorealistic. "
    # ── prohibiciones duras ──
    "The cup is completely plain, pure white, with no stripe, no pattern and no "
    "lettering of any kind. No visible faces, no text, no logos, no signage, "
    "no watermark, no brand marks on the laptop."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — esta slide ya la rechazó el cliente una vez:
  1. ¿Se ve alguna CARA? Tiene que haber cero. Si asoma un perfil, se descarta.
  2. CUENTA LAS MANOS: tienen que ser cuatro y ninguna suelta. «Hay una mano de
     más» fue el reclamo textual de la ronda 4.
  3. ¿La taza está BLANCA TOTAL, sin raya ni letras? (regla KIMBO)
  4. ¿Se lee TRABAJO y no desayuno? Si hay comida desplegada, se descarta.
  5. ¿El tercio de arriba está limpio? Ahí va el bloque de texto.

Si pasa las cinco:
  python scripts/between-gradar.py <la imagen> --perfil neutro --recorte45 \\
      --top 0.5 --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre cowork-servicio-mesa.jpg
  → apuntar FOTO_SERVICIO en src/compositions/hilton/BetweenSeptiembre.tsx
  → python scripts/between-rendir.py BW-F-Cowork-4 --salida out/hilton-between-cowork-r7
  → python scripts/between-qa.py out/hilton-between-cowork-r7
  → descomentar BW-F-Cowork-4 en scripts/between-entrega.py
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
        sys.exit("✗ Faltan las fotos de referencia del 2.º piso:\n  " +
                 "\n  ".join(str(f) for f in faltan))

    # `pro` = Nano Banana Pro: es el único modo que acepta imágenes de
    # referencia, que es justo lo que hace que el lugar sea el de Between.
    # `--aspecto post` = 3:4; la pieza es 4:5 y `FotoFondo` recorta con `cover`,
    # así que sobra alto y no se estira nada.
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

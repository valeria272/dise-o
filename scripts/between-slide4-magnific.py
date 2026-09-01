#!/usr/bin/env python3
"""Genera la foto de la SLIDE 4 del carrusel Cowork de Between con Magnific.

Pedido de Eli (01-09-2026):
    «que se enfoque solo la mano preparando café y se vea el espacio del bar
     de Between»

Y la regla dura del manual, que manda sobre el prompt:
  - ⛔ Rostros de la sesión julio 2023 → acá directamente NO HAY PERSONA: sólo
    las manos. Nadie reconocible, ningún problema de derechos de imagen.
  - «Siempre enfocándose en cómo es Between realmente… debe verse realista» →
    por eso NO se describe un bar genérico: se le pasan las fotos REALES del bar
    como referencia (`--refs`) y el prompt describe ese bar y no otro.
  - La IA hace AMBIENTE y FONDO, nunca el producto ni el logo. La taza va
    blanca y SIN marca — la taza real de Between es blanca completa (y por eso
    también se prohíbe explícitamente cualquier logotipo en el prompt).
  - ⛔ La taza KIMBO: si sale una raya negra o un logo en la taza, la imagen se
    descarta o se limpia. Blanca total.

Uso:
    python scripts/between-slide4-magnific.py            # genera
    python scripts/between-slide4-magnific.py --solo-prompt   # sólo imprime

Necesita la clave de Freepik/Magnific en `~/.magnific_key` (hoy ese archivo
tiene el texto de ejemplo `PEGA-AQUI-TU-CLAVE-FREEPIK`, así que hay que pegar la
clave real) o `FREEPIK_API_KEY` en el .env compartido.
"""
import argparse
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Las fotos REALES del bar de Between. Son la referencia que evita que el
# generador invente un bar de stock: mesón de ónix retroiluminado, rack de
# bronce con cristalería colgada, estantería de botellas y piso de espiga.
REFS = [
    RAIZ / "raw/hilton/between/espacios/HDT_40.jpg",   # el bar, tres cuartos
    RAIZ / "raw/hilton/between/espacios/HDT_39.jpg",   # el bar, de frente
]

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/cowork-servicio-mano.png"

PROMPT = (
    "Photorealistic vertical photograph taken inside the coffee bar shown in the "
    "reference images. Keep that exact bar and nothing generic: the long counter "
    "whose front panel is backlit onyx marble glowing warm cream and pale green, "
    "the dark timber counter top, the brass overhead rack with rows of hanging "
    "stemware, the backlit brass shelving behind it and the herringbone oak floor. "
    "In the foreground, close to camera and the ONLY thing in sharp focus, a "
    "barista's HANDS ONLY: no face, no head, no shoulders, no body, the person is "
    "cropped out of frame above the wrists. The hands hold a stainless steel milk "
    "pitcher and pour steamed milk into a plain white ceramic cup on a white "
    "saucer resting on the counter, latte art just beginning to form on the "
    "surface. The bar behind is clearly recognisable but softly out of focus, "
    "shallow depth of field, creamy bokeh on the brass and the glassware. "
    "Warm ambient evening light with brass highlights, rich medium-dark warm "
    "tonality, cosy and editorial rather than bright and clinical. "
    "The upper third of the frame is darker and uncluttered - shadowed upper wall "
    "and ceiling - leaving quiet negative space. "
    "Editorial hospitality photography, 50mm, natural colour, photorealistic. "
    "The cup is completely plain and unbranded, pure white with no stripe and no "
    "lettering. No faces, no people visible, no text, no logos, no signage, "
    "no watermark."
)


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
        sys.exit("✗ Faltan las fotos de referencia del bar:\n  " +
                 "\n  ".join(str(f) for f in faltan))

    # `pro` = Nano Banana Pro: es el único modo que acepta imágenes de
    # referencia, que es justo lo que hace que el bar sea el de Between.
    # `--aspecto post` = 3:4; la pieza es 4:5 y `FotoFondo` recorta con `cover`,
    # así que sobra alto y no se estira nada.
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--out", a.out, "--aspecto", "post", "--resolucion", "4K",
           "--refs", *[str(r) for r in REFS]]
    print("→", " ".join(cmd[:4]), "…\n")
    r = subprocess.run(cmd, cwd=RAIZ)
    if r.returncode:
        sys.exit(r.returncode)

    print("\nAhora, en este orden:")
    print("  1. MÍRALA con zoom: la taza tiene que estar BLANCA TOTAL, sin raya")
    print("     ni logo (regla KIMBO), y no puede asomar ninguna cara.")
    print("  2. En src/compositions/hilton/BetweenSeptiembre.tsx, apuntar")
    print("     FOTO_SERVICIO a esta imagen.")
    print("  3. python scripts/between-rendir.py BW-F-Cowork-4 --salida out/hilton-between-cowork-r6")
    print("  4. python scripts/between-qa.py out/hilton-between-cowork-r6")
    print("  5. Descomentar BW-F-Cowork-4 en scripts/between-entrega.py")


if __name__ == "__main__":
    main()

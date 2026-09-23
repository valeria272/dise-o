#!/usr/bin/env python3
"""Genera el fondo de la G2 del post CAFÉ DE CUMPLEAÑOS de Between.

⭐ NUEVO 02-09-2026 — RONDA 7. Pedido literal del cliente (FEED!E15):

    «Para la segunda slide proponer otra foto de fondo, distinta a G1»

Por qué hacía falta: las DOS gráficas del post usaban el MISMO archivo
(`cumple-manos-logo.png`), la G2 sólo con otro recorte (`posicion="60% center"`).
Eso es exactamente lo que el manual prohíbe en la regla 1 —«dentro de un carrusel
no se repite el escenario; si dos slides comparten fondo, el lector cree que se
trabó el deslizamiento»— y el cliente lo notó.

Qué tiene que ser esta imagen
-----------------------------
La G2 es el LISTADO de condiciones del beneficio: encima va un `<Checklist>` de
cuatro líneas en caja taupe más cuatro adornos de cumpleaños. O sea que el fondo
es **soporte, no protagonista**: mientras más tranquilo, mejor se lee el listado.

Así que no se pide otra escena con producto —competiría con la caja del
checklist y repetiría el vaso de la G1—, se pide el **rincón de la cafetería,
cálido y muy desenfocado**. Es la misma receta que el cliente ya aprobó en la
FEED G del 7-sep: el ambiente se transfiere por REFERENCIA, no con adjetivos.

Las restricciones y de dónde salen
----------------------------------
  1. **Nada de manos ni vasos.** La G1 ya es «dos manos y el vaso»; repetir el
     motivo sería volver a compartir escena por otra vía. Y cero personas: «hay
     una mano de más» ya fue un rechazo en esta cuenta.
  2. **Ningún logotipo generado.** La IA hace ambiente, nunca marca. Por eso no
     entra ningún vaso: un vaso pide logo, y el logo inventado es lo que el
     cliente reclamó tres veces.
  3. **El centro queda LIMPIO.** El checklist arranca en y=392 de 1350 y baja;
     ahí no puede haber detalle que compita.
  4. **Luz neutra**, sin filtro cálido — reclamo repetido de Scarlette este mes.
     Después se grada con `--perfil neutro`.
  5. **Distinta a la G1 también en encuadre:** la G1 es un plano corto sobre una
     mesa clara de madera; ésta es el fondo del local, más profundo y más oscuro,
     para que el par se lea como dos imágenes y no como un zoom.

Uso:
    python scripts/between-cumple2-magnific.py                # genera
    python scripts/between-cumple2-magnific.py --solo-prompt  # sólo imprime
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

# El local REAL. HDT_50 es la única de las 12 de `espacios/` que Eli identificó
# como Between (01-09), así que es la única que se puede usar sin preguntar; los
# dos fotogramas son del mismo rincón del muro vegetal.
REFS = [
    RAIZ / "raw/hilton/between/espacios/HDT_50.jpg",
    RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_1148-3.jpg",
    RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_1146-1.jpg",
]

SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/cumple-fondo-local.png"

PROMPT = (
    "Photorealistic vertical photograph of the interior of the café shown in the "
    "reference images, seen from a seat at a table: warm wood surfaces, the living "
    "green plant wall, woven rattan armchairs and soft warm lamps. "
    # ── es FONDO: todo desenfocado ──
    "The whole scene is softly OUT OF FOCUS, shot at a wide aperture, dissolved "
    "into gentle blurred shapes and warm colour. No single object is sharp and "
    "nothing is identifiable in detail: it reads as the atmosphere of the place, "
    "not as a picture of any one thing. "
    # ── el centro limpio, que ahí va el listado ──
    "The middle of the frame is calm and even, with no bright highlights and no "
    "busy detail, so that a block of text can be laid over it and stay readable. "
    # ── prohibiciones ──
    "There is NOBODY in the picture: no people, no faces, no hands, no arms. "
    "No cups, no glasses, no mugs, no takeaway cups, no plates, no food and no "
    "drinks anywhere in the image. "
    # ── luz ──
    "Soft natural neutral daylight, balanced white point, true-to-life colour "
    "with no warm orange cast and no colour filter, gentle contrast, nothing "
    "blown out. "
    "Editorial hospitality photography, 35mm, photorealistic. "
    "No text, no logos, no signage, no watermark anywhere in the image."
)

QA = """
MÍRALA ANTES DE USARLA:
  1. ¿Está TODO desenfocado? Si algún objeto está nítido, compite con el
     checklist y la pieza se lee sucia.
  2. ¿Se parece a la G1? Tiene que leerse como OTRA imagen, no como un zoom de
     la misma mesa. Es el pedido textual del cliente.
  3. ¿Hay alguna taza, vaso, mano o persona? Tiene que haber CERO.
  4. ¿El centro está limpio y sin brillos? Ahí cae la caja del listado.

Si pasa las cuatro:
  python scripts/between-gradar.py public/assets/hilton/between/ia-sept/cumple-fondo-local.png \\
      --perfil neutro --recorte45 --top 0.5 --ancho 2250 \\
      --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre cumple-fondo-local.jpg
  → apuntar el `FotoFondo` de Cumple2 en src/compositions/hilton/BetweenSeptiembre.tsx
  → python scripts/between-rendir.py BW-F-Cumple-2 --salida out/hilton-between-r7
  → python scripts/between-qa.py out/hilton-between-r7
  → mirar la G1 y la G2 JUNTAS: el reclamo es que compartían fondo.
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
        sys.exit("✗ Faltan referencias del local:\n  " +
                 "\n  ".join(str(f) for f in faltan))

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

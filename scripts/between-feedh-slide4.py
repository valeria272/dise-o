#!/usr/bin/env python3
"""Slide 4 del carrusel FEED H — «¡NOOO! Se me olvidó la foto.» (9-sep, S2).

⭐ RONDA 9 · 03-09-2026. Es la única de las cuatro que no sale de un recorte: hay
que EDITAR la foto para que el postre se vea **empezado**. Los dos comentarios:

    Cliente (`FEED!H15`, vigente):
      «G4: Aquí la idea es que se vea más vacío el plato, veamos otra opción de
       foto, que sea desde arriba también como los 2 anteriores (como la refe)»

    Scarlette (nativo, 31-08):
      «Slid4: lo mismo acá se tiene que ver más natural, que la persona se comió
       la comida y no le sacó la foto, se ve muy limpia la cucharada del poster
       y el lugar no se parece en nada a Between.»

Son tres reclamos y la foto base los contesta todos de una:

  · «desde arriba» → `Between-179.jpg` es **cenital**, igual que las slides 1, 2
    y 3, así que el carrusel entero queda en el mismo punto de vista.
  · «el lugar no se parece en nada a Between» → es una foto REAL del cliente,
    tomada sobre su mesa de madera, de la sesión `3 ENERO _ PLATOS - DESAYUNOS`.
    El crème brûlée es un postre de su carta.
  · «se comió la comida» / «más vacío el plato» → eso es lo ÚNICO que edita este
    script: la costra quebrada, dos cucharadas menos y la cuchara adentro.

⭐ Y es la regla del estudio aplicada al pie: **cuando existe la foto, se EDITA
la foto — no se recrea la escena.** Recrear un crème brûlée con IA habría dado
un postre genérico en una mesa genérica, que es justo lo que el cliente viene
rechazando hace tres rondas.

El recorte 4:5: (535, 0) → (1735, 1500)
----------------------------------------
`Between-179.jpg` es 2250×1500 apaisada. El recorte de 1200×1500 va **centrado
en el plato** (su eje está en x≈1135) y con eso deja fuera **la copa de vino**
del borde derecho — que además de sobrar en una pieza de desayuno mete alcohol
en una publicación que no lo lleva.

⚠️ CERO cubiertos en la foto base: `Between-179` no los trae (sí `Between-178`,
pero ahí no hay recorte 4:5 que deje el plato entero y los cubiertos a la vez).
La cuchara la pone la edición, dentro de la fuente y con crema encima: es un
objeto genérico, que es lo único que el sistema permite generar.

Uso:
    python scripts/between-feedh-slide4.py
    python scripts/between-feedh-slide4.py --solo-prompt
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

FUENTE = RAIZ / "raw/hilton/between/platos-ene/Between-179.jpg"
BASE = RAIZ / "raw/hilton/between/platos-ene/_h4-base-45.jpg"
RECORTE = (535, 0, 1735, 1500)
SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/h4-postre-empezado.png"


def base_45():
    if BASE.is_file():
        return
    if not FUENTE.is_file():
        sys.exit(f"✗ Falta {FUENTE}\n\n`raw/` no viaja en git. Se baja de la carpeta "
                 "«3 ENERO _ PLATOS - DESAYUNOS» del Drive de Between\n"
                 "  (16OSLgXsc_KABBHbPyBRGsG6zthRAcRaW)")
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(FUENTE).convert("RGB").crop(RECORTE)
    im.save(BASE, quality=97)
    print(f"· recorte base desde Between-179 → {BASE.name} ({im.width}×{im.height})")


PROMPT = (
    "Reproduce the FIRST reference image exactly as it is: the same overhead "
    "top-down shot of a crème brûlée in its white oval baking dish, resting on a "
    "black cloth on a wide grey ceramic plate, on the same dark wood table with "
    "the same visible grain. Same camera angle straight from above, same "
    "framing, same distance, same soft directional light and the same shadows. "
    "Do not change the dish, the plate, the cloth or the table. "
    # ── el único cambio: el postre EMPEZADO ──
    "The ONLY change: the dessert has been started. On the near-right side of "
    "the dish the caramelised sugar crust is BROKEN, and two spoonfuls are "
    "missing, leaving an irregular hollow where the pale creamy custard shows "
    "underneath, with a few loose shards of caramel at its edge. The rest of the "
    "crust stays exactly as it is, glossy amber with its darker scorched patches. "
    "Resting inside the dish, its handle over the near rim, there is ONE plain "
    "stainless steel dessert spoon with a little custard on it. Exactly one "
    "spoon, no fork, no knife, no other cutlery. "
    "It has to look like a real person took two spoonfuls and only then "
    "remembered the photo: uneven, a bit messy, not a neat styled scoop. "
    # ── nada más se mueve ──
    "Nothing else changes: no new food, no berries, no mint, no icing sugar, no "
    "napkin, no glass, no drink, no crumbs on the table. "
    "There is NOBODY in the picture: no people, faces, hands, arms or fingers. "
    "Photorealistic food photography, sharp, high detail, warm natural light, "
    "balanced white point, no blown highlights. No text, lettering, logos, brand "
    "marks or watermark anywhere in the image."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — 6 puntos:
  1. ¿Es LA MISMA fuente blanca sobre el mismo plato gris y la misma mesa de
     madera? Si el generador inventó otro plato u otra mesa, se descarta: el
     reclamo del cliente es justamente que «el lugar no se parece a Between».
  2. ¿Se ve EMPEZADO de verdad? Tiene que leerse el hueco y la crema pálida
     debajo de la costra, no una cucharada prolija.
  3. ¿Hay UNA sola cuchara, sin tenedor ni cuchillo?
  4. ¿Sigue siendo CENITAL? Las otras tres slides lo son y el cliente lo pidió
     por escrito.
  5. ¿Apareció comida nueva, servilleta, copa o miguitas? No debe.
  6. ¿Algún texto, número o logotipo inventado? Ninguno.

Si pasa las seis:
  python scripts/between-gradar.py public/assets/hilton/between/ia-sept/h4-postre-empezado.png \\
      --perfil neutro --recorte45 --ancho 2250 \\
      --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre h4-postre-empezado.jpg
  → apuntar la `foto` de Foto4 en src/compositions/hilton/BetweenSeptiembre.tsx
  → rendir las CUATRO y mirarlas juntas: la cohesión no se verifica pieza a pieza.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-prompt", action="store_true")
    ap.add_argument("--out", default=str(SALIDA))
    a = ap.parse_args()
    if a.solo_prompt:
        print(PROMPT)
        return
    base_45()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--aspecto", "post", "--resolucion", "4K", "--out", a.out,
           "--refs", str(BASE), str(FUENTE)]
    print("→ Nano Banana Pro · 3:4 · 4K · el crème brûlée real de Between")
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()

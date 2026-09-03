#!/usr/bin/env python3
"""Slide 4 del carrusel FEED L — «¿POR QUÉ ELEGIR UNO? ¡Llévate los 3!» (14-sep, S3).

⭐ RONDA 9 · 03-09-2026. `FEED!L16` está EN CAMBIOS. De la celda `L15` sólo está
VIGENTE el primer bloque (el segundo va TACHADO, o sea ya se tomó), y el
comentario nativo de Scarlette del 31-08 agrega el detalle por slide:

    «Slide4: La información de la promo esta mala deberia quedar como esta en la
     slide 1 y 2. Acá se ven casí los mismos productos, ajustesmos, pongamos
     como dulce un browne aun que sea y el vaso de café nada que ver jajajaja»

De los tres reclamos, **dos ya están resueltos**: la pila de la promo se unificó
con las slides 2 y 3 en la ronda 5 (`PilaEsquina` con `igualarAncho`), y el vaso
lleva desde la ronda 5 el logotipo real estampado. Queda el del medio, y es
cierto: la escena entregada muestra **un croissant de jamón y queso y un
croissant simple**, o sea «casi los mismos productos». La slide dice «Café +
Salado + Dulce» y el dulce no se distingue del salado.

Qué cambia, y qué NO
---------------------
Cambia **sólo el producto dulce**: el croissant simple sale y entra un
**brownie**, que es lo que el cliente nombró. Todo lo demás se queda igual — la
mesa de madera, la silla, la planta desenfocada, los dos platos verdes, el
croissant de jamón y queso, y sobre todo **el vaso To Go con su logotipo**, que
costó tres rondas dejar bien.

Por eso esto es una EDICIÓN sobre la imagen entregada y no una escena nueva: la
regla del estudio desde el C2 del cumpleaños es que **cuando el cliente señala
una pieza y objeta UN elemento, se edita ese elemento**. Recrear la escena
obligaría a re-estampar el vaso y a volver a discutir un encuadre aprobado.

⚠️ QA obligatoria del vaso. El generador puede redibujar el logotipo y
devolverlo torcido o inventado — es el defecto que este manual documenta desde
la ronda 4. Si el logotipo sale distinto, NO se acepta: se vuelve a estampar el
real con `scripts/between-logo-vaso.py` sobre esta misma salida.

⚠️ Y OJO CON LAS ETIQUETAS. La pieza lleva «Salado» en (330, 832) y «Dulce» en
(716, 1150), cada una con su flecha de bucle naciendo del producto. Si el brownie
queda en otro sitio que el croissant que reemplaza, **hay que volver a medir esas
coordenadas**: una flecha que no toca su producto es un defecto del manual.

Uso:
    python scripts/between-togo4-brownie.py
    python scripts/between-togo4-brownie.py --solo-prompt
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

BASE = RAIZ / "public/assets/hilton/between/ia-sept/togo-trio-45-logo.png"
SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/togo-trio-brownie.png"

PROMPT = (
    "Reproduce the reference image exactly as it is: the same round light wooden "
    "café table seen at a slight angle, the same wooden chair back on the left, "
    "the same blurred green indoor plant and pale wall behind, the same soft warm "
    "light and the same shadows. Keep the same camera position, the same framing "
    "and the same depth of field. "
    # ── lo que NO se toca ──
    "Keep the takeaway coffee cup EXACTLY as it is: same kraft paper cup, same "
    "black plastic lid, same position on the table, same size, and the same "
    "printed wordmark on it, unchanged, undistorted and in the same place. Do not "
    "redraw it, do not restyle it, do not move it. "
    "Keep the ham and cheese croissant on its round sage-green plate on the LEFT "
    "exactly as it is, same plate, same position. "
    # ── el único cambio ──
    "The ONLY change is the sweet item on the RIGHT-hand sage-green plate: the "
    "plain croissant is replaced by a single square CHOCOLATE BROWNIE - a thick "
    "dark chocolate brownie square with a slightly cracked shiny crust and a "
    "moist, dense crumb, no icing, no berries, no mint, no dusting of sugar. The "
    "brownie sits in the same spot on the same plate, at the same scale as the "
    "item it replaces, casting the same kind of soft shadow. It must read as "
    "clearly DIFFERENT from the savoury croissant on the other plate. "
    "Nothing else changes: no new food, no cutlery, no napkins, no crumbs, no "
    "extra plates. "
    "There is NOBODY in the picture: no people, faces, hands or fingers. "
    "Photorealistic food photography, sharp on the table, warm natural light, "
    "balanced white point, no blown highlights. No new text, no lettering, no "
    "extra logos and no watermark anywhere in the image."
)

QA = """
MÍRALA CON ZOOM ANTES DE USARLA — 6 puntos:
  1. ⚠️ EL VASO. ¿Está IGUAL que en la referencia — mismo kraft, misma tapa,
     misma posición, y el logotipo entero, derecho y sin deformar? Si el modelo
     lo redibujó, NO se acepta tal cual: se re-estampa el real con
     `scripts/between-logo-vaso.py`. Es el defecto que esta marca arrastra desde
     la ronda 4.
  2. ¿El dulce es un BROWNIE reconocible y claramente distinto del croissant
     salado? Ése es el reclamo textual: «se ven casi los mismos productos».
  3. ¿El croissant de jamón y queso quedó intacto, en su plato y su sitio?
  4. ¿Es la MISMA mesa, la misma silla y la misma planta? Si cambió el lugar, se
     descarta: el encuadre ya está aprobado.
  5. ¿Apareció comida, cubierto o texto de más?
  6. ⚠️ ¿DÓNDE quedó el brownie? Las etiquetas «Salado» (330, 832) y «Dulce»
     (716, 1150) llevan flechas que TOCAN su producto. Si el brownie se movió,
     hay que volver a medir esas coordenadas en la pieza rendida.

Si pasa los seis:
  python scripts/between-gradar.py public/assets/hilton/between/ia-sept/togo-trio-brownie.png \\
      --perfil neutro --recorte45 --ancho 2250 \\
      --salida public/assets/hilton/between/fotos-gradadas \\
      --nombre togo-trio-brownie.jpg
  → apuntar la `foto` de ToGo4 en src/compositions/hilton/BetweenSeptiembre.tsx
  → rendir las CUATRO slides del To Go y mirarlas juntas.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-prompt", action="store_true")
    ap.add_argument("--out", default=str(SALIDA))
    a = ap.parse_args()
    if a.solo_prompt:
        print(PROMPT)
        return
    if not BASE.is_file():
        sys.exit(f"✗ Falta la imagen entregada que se va a editar: {BASE}")
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--aspecto", "post", "--resolucion", "4K", "--out", a.out,
           "--refs", str(BASE)]
    print("→ Nano Banana Pro · 3:4 · 4K · edición sobre la slide 4 entregada")
    r = subprocess.run(cmd, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.returncode)
    print(QA)


if __name__ == "__main__":
    main()

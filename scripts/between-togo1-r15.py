#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTADA del carrusel PROMOS TO GO — ronda 15: el vaso, más abajo y entero.

Eli, por CUARTA vez sobre el mismo logotipo:

    ronda 12  «el logo se ve poco centrado»
    ronda 13  «tienes que mejorar el logo del vaso TOGO»
    ronda 14  «el logo del vaso debes centrarlo según el vaso. Arréglalo»
    ronda 15  «la portada el logo del vaso **sigue igual**. Utiliza magnific»

⛔⛔ Y tiene razón. La ronda 14 corrigió la medición —el cuerpo del vaso mide
   199 px, no los 240 que decía la constante— y aun así la pieza quedó mal, por
   una razón que ninguna ronda había mirado: **no cabe**.

   Medido columna a columna sobre la generación, el cartón limpio del vaso:

       x         835   855   875   885   915   935  1015
       arriba   1236  1239  1243  1243  1244  1240  1227
       abajo    1269  1274  1287  1337  1341  1399  1399

   O sea que el canto de la tapa entra por arriba y los dedos suben por abajo, y
   **la banda de cartón despejada a lo ancho del logotipo mide 25 px**. El lockup
   de marca (0,86 del ancho del vaso = 171 px) necesita **56**. Por eso las tres
   rondas anteriores sólo pudieron elegir por dónde cortarlo:

       ronda 12  206 px → más ancho que el vaso; la máscara le comió la B
       ronda 13  175 px → pegado al canto derecho (5 px de aire contra 19)
       ronda 14  171 px centrado → **la tapa le cortó los remates de arriba**

   Ajustar el centro y el ancho sobre una banda de 25 px es mover el problema.

⭐ LA SALIDA: cambiar la FOTO, no el estampado. Se regenera la escena con Nano
   Banana Pro pasándole la portada actual como referencia y pidiendo lo único
   que hay que cambiar: **que la mano tome el vaso más abajo**, de modo que el
   cuerpo del vaso quede entero y despejado entre la tapa y los dedos. Con eso
   el logotipo entra al tamaño de marca, centrado en el eje y sin que nada lo
   corte.

⚠️ Y se verifica lo que importa antes de usarla: que la mujer, el encuadre, el
   muro vegetal y la luz sigan siendo los de la portada que Eli **no** objetó —
   ella reclamó el logo, no la foto. Si la persona cambia, esta generación se
   descarta y se vuelve a pedir. Por eso el script deja la comparación en
   `out/hilton-between-r15/pasos/`.

Uso:
    python scripts/between-togo1-r15.py generar     # pide la escena a Magnific
    python scripts/between-togo1-r15.py medir       # dónde quedó el vaso
    python scripts/between-togo1-r15.py componer    # recorta 4:5 y estampa
"""
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import hombro, informe, vivo  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
REF = RAIZ / "out/hilton-between-r15/pasos/ref-portada-r14.jpg"
GEN = RAIZ / "public/assets/hilton/between/ia-sept/togo-portada-gen-r15.png"
BASE = RAIZ / "public/assets/hilton/between/ia-sept/togo-portada-gen-2x.jpg"
VENTANA = (360, 1116, 2880, 3600)

PROMPT = (
    # ── lo que NO cambia: es la misma foto ──
    "Recreate the reference photograph as faithfully as possible: the SAME young "
    "woman, same face, same hair, same beige shirt and camel trousers, same "
    "standing pose, same terrace of a coffee shop with the dense green plant "
    "wall and the warm hanging bulbs behind her, same natural daylight, same "
    "framing and same camera angle. It must read as the same photograph. "
    # ── lo único que cambia, y es la razón de la ronda ──
    "The ONE difference: she holds the takeaway coffee cup LOWER and further "
    "from her body, and her hand grips the cup near its BASE, so that the whole "
    "upper two thirds of the cup are completely unobstructed. Her fingers must "
    "NOT cover the middle of the cup. Between the black plastic lid and the top "
    "of her fingers there is a wide, clean, uninterrupted band of kraft paper. "
    "The cup is held upright and square to the camera, not tilted. "
    # ── el vaso va LISO: el logotipo se estampa después, nunca se genera ──
    "The cup is a plain kraft brown paper takeaway cup with a black plastic lid "
    "and a white rim at the base. It is completely BLANK and unbranded: no logo, "
    "no lettering, no text, no symbol, no pattern of any kind printed on it. "
    "Plain kraft paper only. "
    # ── la bolsa sigue en su sitio ──
    "In her other hand, hanging down at her side, she carries a plain kraft "
    "paper bag, also completely blank and unbranded. "
    # ── manos correctas: es un rechazo conocido de esta marca ──
    "Both hands are anatomically correct, with exactly five fingers each, "
    "natural neat nails. No extra hands, no extra people in the frame. "
    # ── el look ──
    "Natural daylight, neutral white balance, no warm orange cast, no colour "
    "filter, shallow depth of field with the background softly out of focus. "
    "Candid lifestyle photograph, 50mm lens look, sharp on the woman and the cup."
)


def genera():
    REF.parent.mkdir(parents=True, exist_ok=True)
    if not REF.exists():
        im = Image.open(BASE).convert("RGB")
        x0, y0, w, h = VENTANA
        im.crop((x0, y0, x0 + w, y0 + h)).resize((1440, 1800), Image.LANCZOS).save(
            REF, quality=94)
        print(f"referencia -> {REF.relative_to(RAIZ)}")
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "pro", PROMPT,
           "--out", str(GEN), "--aspecto", "post", "--resolucion", "4K",
           "--refs", str(REF)]
    print("→ Nano Banana Pro, 4K, 1 referencia")
    r = subprocess.run(cmd, cwd=RAIZ)
    if r.returncode:
        sys.exit("la generación falló")
    print(f"-> {GEN.relative_to(RAIZ)}")


def mide():
    """Dónde quedó el cuerpo del vaso y cuánta banda limpia hay, fila a fila.

    Misma máscara de cartón que la ronda 12 (`B/R < 0,58 & R > 115`) y corrida
    contigua más larga, que es lo único que funciona: un barrido de píxeles
    cálidos se corta con cualquier sombra."""
    if not GEN.exists():
        sys.exit(f"todavía no existe {GEN}")
    im = Image.open(GEN).convert("RGB")
    print(f"generación {im.width}x{im.height}")
    a = np.asarray(im).astype(np.float32)
    kr = ((a[..., 2] / np.maximum(a[..., 0], 1.0)) < 0.58) & (a[..., 0] > 115)
    print("  fila: corrida de cartón más larga")
    for y in range(0, im.height, max(1, im.height // 60)):
        xs = np.where(kr[y])[0]
        if len(xs) < 20:
            continue
        best = (0, 0, 0)
        s = p = xs[0]
        for x in xs[1:]:
            if x - p > 4:
                if p - s > best[2]:
                    best = (s, p, p - s)
                s = x
            p = x
        if p - s > best[2]:
            best = (s, p, p - s)
        if best[2] > 60:
            print(f"   y={y:5d}: {best[0]:5d}-{best[1]:5d} ancho {best[2]:4d} "
                  f"eje {(best[0] + best[1]) // 2}")




# ─────────────────────────── el montaje de la pieza ──────────────────────────
#: Ventana 4:5 sobre la generación de 3.584×4.800. Se resuelve con las mismas dos
#: condiciones que la ronda 12, para que el bloque de texto YA APROBADO siga
#: calzando: la cabeza con aire arriba y el vaso cerrado antes de que arranque la
#: script (y≈1.595 en el lienzo de 2.812).
#:   · cabeza  y=352 en la generación → 127 px de aire (la r12 tenía 130)
#:   · vaso    cierra en y=2.530      → y=1.494 en la pieza (la r12, 1.490)
VENTANA_PIEZA = (0, 150, 3584, 4480)
SALIDA_PX = (2250, 2812)
PIEZA = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-portada-r15.jpg"
LOGO = RAIZ / "public/assets/hilton/between/logo-negro-vector.png"

#: ⭐ EL VASO, medido con cuadrícula sobre la generación nueva y llevado a la
#: escala de la pieza (2250/3584 = 0,6278):
#:
#:     cuerpo del vaso   x 1256-1633 (gen)  →  789-1025 (pieza), ancho 236
#:     canto de la tapa  y 1995      (gen)  →  1158     (pieza)
#:     primer dedo       y 2127      (gen)  →  1241     (pieza)
#:
#: o sea **83 px de cartón limpio a todo el ancho del vaso**. El lockup de marca
#: (0,86 × 236 = 203 px de ancho) mide 67 px de alto: **entra entero, con 16 px
#: de aire**. Es exactamente lo que no pasaba en la portada anterior, donde la
#: banda limpia medía 25 px y el logotipo pedía 56 — de ahí las cuatro rondas.
VASO_CUERPO = (789, 1158, 1025, 1241)
LOGO_ANCHO = 203
LOGO_CENTRO = (907, 1200)


def estampa(base):
    """Multiplica el logotipo real sobre el cartón, con escala UNIFORME.

    ⭐ RONDA 15 — dos cosas nuevas respecto de la portada anterior, y las dos
    salen del reclamo «los logos se ven extraños»:

      · **el sello se desenfoca a la nitidez de SU zona de la foto.** El vector
        entra con canto matemático y la fotografía tiene profundidad de campo:
        un logotipo más nítido que el cartón sobre el que está impreso se lee
        como calcomanía. Se mide la varianza del laplaciano del cartón y se le
        aplica al sello el desenfoque que le corresponde;
      · **el sello recibe el grano de la foto.** Una impresión comparte el ruido
        del sensor con la superficie; un vector no tiene ninguno.

    Ya no hace falta enmascarar los dedos: el logotipo cae entero en la banda
    limpia del cartón, así que no hay nada que recortar."""
    logo = Image.open(LOGO).convert("RGBA")
    ratio = logo.width / logo.height
    alto = int(round(LOGO_ANCHO / ratio))
    logo = logo.resize((LOGO_ANCHO, alto), Image.LANCZOS)
    cx, cy = LOGO_CENTRO
    x1, y1 = cx - LOGO_ANCHO // 2, cy - alto // 2
    print(f"   logo {LOGO_ANCHO}x{alto} (ratio {ratio:.4f}) en x {x1}-{x1 + LOGO_ANCHO} · "
          f"y {y1}-{y1 + alto}")
    bx0, by0, bx1, by1 = VASO_CUERPO
    print(f"   aire lateral: {x1 - bx0} izq · {bx1 - (x1 + LOGO_ANCHO)} der   "
          f"(cuerpo {bx1 - bx0} px, ratio {LOGO_ANCHO / (bx1 - bx0):.3f})")
    print(f"   aire vertical: {y1 - by0} arriba · {by1 - (y1 + alto)} abajo")

    zona = np.asarray(base.crop((x1, y1, x1 + LOGO_ANCHO, y1 + alto))).astype(np.float64)
    lg = np.asarray(logo).astype(np.float64)
    tinta = lg[:, :, :3].mean(axis=2) / 255.0
    densidad = (lg[:, :, 3] / 255.0) * (1.0 - tinta) * 0.95

    #: ── la nitidez de la zona, para no dejar el sello más definido que la foto
    gris = cv2.cvtColor(np.asarray(base.crop(
        (bx0, by0, bx1, by1))), cv2.COLOR_RGB2GRAY)
    nit = cv2.Laplacian(gris, cv2.CV_64F).var()
    #: calibrado sobre esta toma: cartón a ~90 de varianza pide ~0,7 px de
    #: desenfoque; cuanto más blando el cartón, más blando el sello.
    radio = float(np.clip(1.6 - nit / 90.0, 0.35, 1.6))
    densidad = cv2.GaussianBlur(densidad, (0, 0), radio)
    print(f"   nitidez del cartón {nit:.0f} → el sello se funde a {radio:.2f} px")

    #: ── la luz: la tinta se apaga donde el cartón está en sombra
    lum = (0.299 * zona[..., 0] + 0.587 * zona[..., 1] + 0.114 * zona[..., 2]) / 255.0
    densidad *= np.clip(lum * 1.25, 0.25, 1.0)

    #: ── el grano del sensor, medido en el propio cartón
    grano = float(np.std(gris.astype(np.float64) - cv2.GaussianBlur(
        gris.astype(np.float64), (0, 0), 1.5)))
    rnd = np.random.default_rng(2026)
    ruido = rnd.normal(0.0, grano, size=densidad.shape) * (densidad > 0.02)
    print(f"   grano del cartón: sigma {grano:.2f}")

    fuera = zona * (1.0 - densidad[..., None] * (1.0 - 0.18)) + ruido[..., None]
    salida = base.copy()
    salida.paste(Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)), (x1, y1))
    return salida


def compone():
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN} — corre `generar` primero")
    im = Image.open(GEN).convert("RGB")
    x0, y0, w, h = VENTANA_PIEZA
    im = im.crop((x0, y0, x0 + w, y0 + h)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"ventana 4:5 {w}x{h} desde y={y0} -> {im.width}x{im.height}")
    informe(im, "generada")

    im = estampa(im)

    # retoque MÍNIMO: la generación ya viene expuesta. Misma mano que la r12.
    im = vivo(im, vibrancia=0.12)
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    informe(im, "final")
    im.save(PIEZA, quality=95, subsampling=0)
    print(f"-> {PIEZA.relative_to(RAIZ)}")


if __name__ == "__main__":
    accion = sys.argv[1] if len(sys.argv) > 1 else "componer"
    {"generar": genera, "medir": mide, "componer": compone}[accion]()

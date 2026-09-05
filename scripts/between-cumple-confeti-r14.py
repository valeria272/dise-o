#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Siembra las serpentinas doradas REALES sobre las dos slides del cumpleaños.

⭐ RONDA 14 (05-09-2026) — Eli:

    «debes quitar esos "plátanos dorados" del carrusel de cumpleaños, puedes
     añadir alguna de [vector de confeti dorado] sutiles en el slide 1 y 2.
     Hazlo realista y mantén el resultado de la foto de togo y medialuna.»

⭐⭐ DÓNDE ESTABAN LOS «PLÁTANOS», que es lo que costó encontrar. La ronda 13 ya
   había sacado las cintas dibujadas de la foto de la slide 1 — pero la **ventana
   del mock de la slide 2 seguía apuntando a `cumple-r12-1.jpg`**, la foto de la
   ronda 12, la que las tiene sembradas. O sea: las cintas plátano estaban vivas
   dentro del post de la slide 2 mientras la slide 1 ya estaba limpia. Eli las vio
   ahí. Se corrige apuntando la ventana a la foto de esta ronda.

   Lección: cuando se cambia el fondo de una slide hay que buscar **todos** los
   sitios donde esa foto se usa. Un mock de post enseña otra pieza adentro.

⭐ Y POR QUÉ AHORA SÍ PUEDE SER REALISTA, después de que la ronda 12 fracasara
   por exactamente eso. El aprendizaje de la 12 era: «un adorno que quiere ser
   fotografía se mide contra la fotografía que lo rodea, y una forma dibujada de
   40 px no aguanta a un croissant de 900 px hecho con un 50 mm». Sigue siendo
   verdad. Lo que cambió es el MATERIAL:

   | | ronda 12 | ronda 14 |
   |---|---|---|
   | origen | `ImageDraw` — yo dibujando una cinta | vector de 4.998×3.540, el que eligió Eli |
   | volumen | un degradado a lo largo + una veta | cinta con vuelta, cara interior y exterior, especular propia |
   | forma | arco afinado en las puntas | rizo real (27 piezas distintas) |

   No es que ahora se dibuje mejor: es que **ya no se dibuja**. La pieza es una
   ilustración de calidad hecha por un ilustrador, y sobre ella sí vale la pena
   aplicar la receta de montaje del manual.

La receta de montaje (§ «la foto de banco se revela y el montaje se delata por
la luz»), aplicada a cada serpentina:

  1. **tamaño por cercanía** — la que cae más cerca de cámara es mayor;
  2. **desenfoque según el DOF REAL de la toma**, medido con la varianza del
     laplaciano por bloques (el plano de foco es el hojaldre, y la mesa cercana
     está a 15-25 de varianza contra 400-500 del foco: una serpentina nítida ahí
     grita «pegada»);
  3. **armonización contra el ILUMINANTE**, no contra la superficie — la trampa
     de este montaje y la que me costó una pasada; ver la nota de `ILUMINANTE`;
  4. **sombra de contacto** corta y pequeña, desplazada según la luz de la toma
     (que entra por arriba a la izquierda: mirar la sombra del plato);
  5. y **nada de tinta en el margen de marca** (84 px de lienzo = 175 px acá).

⚠️ SUTIL quiere decir POCAS. El manual pide los adornos «en poca proporción», y
   el reclamo de la ronda 11 fue «se ve muy infantil». Van 4 en la slide 1 y 2 en
   la slide 2, todas apoyadas en la mesa, ninguna sobre el producto ni sobre el
   texto — y los doodles de Eli se quedan donde están, porque la slide 1 se
   aprobó con ellos.

Entrada:  fotos-gradadas/cumple-r13-{1,2}.jpg  (las de la ronda 13, intactas)
Salida:   fotos-gradadas/cumple-r14-{1,2}.jpg
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import borrosa, informe

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
FOTOS = RAIZ / "public/assets/hilton/between/fotos-gradadas"
PIEZAS = RAIZ / "public/assets/hilton/between/recursos/confeti-oro"
PASOS = RAIZ / "out/hilton-between-r14/pasos"

#: La luz de la toma entra por ARRIBA A LA IZQUIERDA — se lee en la sombra del
#: plato, que cae hacia abajo y a la derecha. La sombra de contacto va en esa
#: dirección, y corta: una serpentina apoyada no proyecta lejos.
LUZ = (0.42, 1.0)

#: ⛔⛔ EL ERROR DE LA PRIMERA PASADA, y vale para cualquier montaje: armonicé el
#: oro contra el color LOCAL DE LA MADERA (balance 1,38 / 1,00 / 0,67) y las
#: serpentinas salieron NARANJA MANDARINA, plástico. Y la que iba en el aire,
#: armonizada contra el muro vegetal, salió verde-amarilla.
#:
#: La madera es naranja porque la madera ES naranja, no porque la luz lo sea. El
#: iluminante se mide sobre un NEUTRO ILUMINADO de la propia toma —acá el anillo
#: blanco de la base del vaso, en x 1500-1900 · y 1960-2040— y da:
#:
#:     [182,1  185,2  190,7]  ->  balance 0,983 / 1,000 / 1,030
#:
#: o sea la luz de esta escena es prácticamente neutra, con una pizca de frío.
#: Un objeto agregado se corrige contra ESO, no contra la superficie donde cae.
ILUMINANTE = (0.983, 1.000, 1.030)
#: y se asienta bajando la luminancia: el vector está pensado para fondo claro y
#: a tope se lee como calcomanía sobre una mesa oscura.
ASIENTO = 0.88

#: Siembra de la SLIDE 1. Cada entrada: (pieza, x, y, ancho, rotación, desenfoque,
#: sombra). Las coordenadas son del lienzo de 2250×2812 y salen de la cuadrícula
#: medida sobre `cumple-r13-1.jpg`:
#:   · muro vegetal (desenfocado)      y 0-1300
#:   · bloque de texto de la pieza     y 300-720
#:   · vaso To Go                      x 1290-2110 · y 890-2060
#:   · plato + medialunas              x 0-1650 · y 1550-2280
#:   · reflejo del vaso en la mesa     x 1300-2100 · y 2060-2250
#: Zonas libres usadas: la mesa a la derecha y debajo del vaso, y la mesa a la
#: izquierda por debajo del plato. NINGUNA pisa el producto ni el texto.
#: ⛔ La pieza que iba EN EL AIRE contra el muro vegetal se cayó de la siembra.
#: El muro está muy desenfocado y muy oscuro: una serpentina ahí, con el
#: desenfoque que le corresponde, deja de leerse como cinta y queda una MANCHA
#: amarilla. Y además el pedido del cliente es sobre la mesa, literal: «quizás en
#: la mesa poner como esos papelitos de colores que se lanzan» (`FEED!E15`).
#: Todo el confeti va apoyado en la madera.
#:
#: ⭐ Y van REPARTIDAS a lo largo de la mesa, no amontonadas en la esquina. En la
#: primera pasada las cuatro cayeron en el mismo cuadrante y se leía como un
#: montoncito barrido, no como confeti lanzado.
SIEMBRA1 = [
    # (pieza, x,    y,    ancho, rot,  blur, sombra)
    # ⚠️ Los anchos subieron un 25 % después de mirar la pieza al TAMAÑO REAL DE
    #    FEED (430 px de ancho en el teléfono): a 170/150/108/126 el confeti se
    #    veía como motas y la corrección que pidió Eli no se leía. A 212/188/135/158
    #    se reconocen como serpentinas y siguen ocupando menos del 9 % del ancho.
    #    Una pieza se juzga al tamaño en que se publica, no al 100 %.
    ("06",   1652, 2098,  212,   -14,  3.0,  0.34),   # mesa, bajo la base del vaso
    ("23",   1046, 2330,  188,    22,  4.2,  0.30),   # mesa, al centro
    ("17",    560, 2496,  135,   -34,  5.4,  0.24),   # mesa, al centro-izquierda
    # ⚠️ medido tras la 2.ª pasada: el canto del plato baja hasta y≈2435 a la
    #    altura de x 200-600, así que en y=2330 esta serpentina quedaba APOYADA
    #    EN EL BORDE DEL PLATO, no en la mesa. Baja a 2540, que ya es madera.
    ("07",    196, 2540,  158,    16,  5.4,  0.26),   # mesa, por debajo del plato
]

#: Siembra de la SLIDE 2. Acá el mock de post tapa el centro —medido: lienzo
#: 1080 x 196-878 · y 203-1095, o sea x 408-1829 · y 422-2281 en la foto—, así
#: que la foto sólo se ve por las bandas. Las dos serpentinas van en la BANDA DE
#: ABAJO, sobre la misma mesa que en la slide 1, para que al deslizar el confeti
#: continúe: es la misma toma y la mesa sigue.
#:
#: ⛔ No van arriba, contra el muro: es la misma razón por la que se cayó la del
#: aire en la slide 1, y acá peor, porque esta foto además lleva 4 px de
#: desenfoque de fondo encima.
#:
#: Y el confeti de esta slide se ve sobre todo DENTRO del mock, porque la ventana
#: del post enseña la foto de la slide 1 — que ahora es `cumple-r14-1.jpg`.
SIEMBRA2 = [
    ("15",   1888, 2372,  165,    18,  4.6,  0.26),
    ("21",    206, 2456,  120,   -26,  5.0,  0.22),
]


def dof(gris, x, y, w, h):
    """Varianza del laplaciano de la zona — cuán nítido está ESE trozo de foto."""
    x0, y0 = max(0, x), max(0, y)
    b = gris[y0:y0 + h, x0:x0 + w]
    return cv2.Laplacian(b, cv2.CV_64F).var() if b.size else 0.0


def balance(a, x, y, w, h):
    """El balance de blancos LOCAL de la escena, normalizado al verde."""
    z = a[max(0, y):y + h, max(0, x):x + w].reshape(-1, 3)
    m = z.mean(axis=0)
    return m / max(m[1], 1.0)


def una(n, siembra):
    origen = FOTOS / f"cumple-r13-{n}.jpg"
    if not origen.exists():
        sys.exit(f"falta la foto de la ronda 13: {origen}")
    base = Image.open(origen).convert("RGB")
    a = np.asarray(base).astype(np.float32)
    gris = cv2.cvtColor(np.asarray(base), cv2.COLOR_RGB2GRAY)
    print(f"\n-- slide {n}: {base.width}x{base.height}")

    capa = Image.new("RGBA", base.size, (0, 0, 0, 0))
    sombras = np.zeros((base.height, base.width), np.float32)

    for pieza, x, y, ancho, rot, blur, fuerza in siembra:
        p = PIEZAS / f"confeti-oro-{pieza}.png"
        if not p.exists():
            sys.exit(f"falta la serpentina {p.name} — corre between-confeti-recortar.py")
        im = Image.open(p).convert("RGBA")
        alto = int(round(ancho * im.height / im.width))
        im = im.resize((ancho, alto), Image.LANCZOS)
        im = im.rotate(rot, resample=Image.BICUBIC, expand=True)

        # ── 3. armonización de luz: contra el ILUMINANTE de la toma, no contra
        #    el color de la superficie donde cae (ver la nota de ILUMINANTE).
        arr = np.asarray(im).astype(np.float32)
        arr[..., :3] *= np.array(ILUMINANTE, np.float32)[None, None, :] * ASIENTO
        im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

        nit = dof(gris, x, y, im.width, im.height)
        print(f"   {pieza}: {im.width}x{im.height} en ({x},{y}) rot {rot:+d}° · "
              f"nitidez local {nit:.0f} · desenfoque {blur:.1f} px · "
              f"superficie {balance(a, x, y, im.width, im.height).round(3)}")

        # ── 4. sombra de contacto: la silueta desplazada según la luz, corta y
        #    densa. Sólo para las que se APOYAN (las del aire van con fuerza 0).
        if fuerza > 0:
            alfa = np.asarray(im)[..., 3].astype(np.float32) / 255.0
            dx = int(round(0.055 * im.width * LUZ[0]))
            dy = int(round(0.055 * im.height * LUZ[1]))
            sx, sy = x + dx, y + dy
            h, w = alfa.shape
            y0, x0 = max(0, sy), max(0, sx)
            y1, x1 = min(base.height, sy + h), min(base.width, sx + w)
            if y1 > y0 and x1 > x0:
                trozo = alfa[y0 - sy:y1 - sy, x0 - sx:x1 - sx]
                sombras[y0:y1, x0:x1] = np.maximum(sombras[y0:y1, x0:x1], trozo * fuerza)

        # ── 2. desenfoque del DOF: se aplica a la pieza YA armonizada, con su
        #    alfa, para que el canto se funda igual que el resto de la escena.
        if blur > 0:
            arr = np.asarray(im).astype(np.float32)
            arr = np.dstack([borrosa(arr[..., :3], blur),
                             borrosa(arr[..., 3:4], blur)[..., 0]])
            im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        capa.alpha_composite(im, (x, y))

    # ── la sombra se desenfoca y se multiplica: es CONTACTO, no objeto.
    # ⛔ En la primera pasada iba a radio 9 y fuerza 0,34 y dejaba nubarrones
    #    grises del tamaño de un plato alrededor de cada serpentina — más sombra
    #    que la que proyecta el vaso entero. Una cinta de papel apoyada proyecta
    #    una sombra CORTA y pequeña. Radio 5 y fuerza 0,20.
    if sombras.any():
        sombras = borrosa(sombras[..., None], 5.0)[..., 0]
        a = a * (1.0 - 0.20 * sombras[..., None])
        print(f"   sombras de contacto: {100 * (sombras > 0.02).mean():.2f} % del cuadro")

    salida = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGBA")
    salida.alpha_composite(capa)
    salida = salida.convert("RGB")
    informe(salida, f"slide {n} con serpentinas")
    destino = FOTOS / f"cumple-r14-{n}.jpg"
    salida.save(destino, quality=95, subsampling=0)
    PASOS.mkdir(parents=True, exist_ok=True)
    salida.resize((salida.width // 3, salida.height // 3), Image.LANCZOS).save(
        PASOS / f"cumple-r14-{n}.jpg", quality=88)
    print(f"   -> {destino.name}")


if __name__ == "__main__":
    una(1, SIEMBRA1)
    una(2, SIEMBRA2)
    print("\nlisto.")

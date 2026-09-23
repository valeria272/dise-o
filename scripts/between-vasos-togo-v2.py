# -*- coding: utf-8 -*-
"""
BETWEEN · los vasos To Go, versión del 22-09-2026 — REEMPLAZA la entrega del 21-09
=================================================================================

Eli rehizo los vasos en Magnific desde claude.ai y el resultado está mejor logrado
que el recorte fotográfico del día anterior. Space «BETWEEN_VASOS TOGO»:
https://www.magnific.com/app/spaces/a2ce7bd4-9df0-47db-b7b2-d96f5c81079c

⚠️ QUÉ SON ESTOS VASOS, DICHO SIN ADORNO
----------------------------------------
NO son la foto del vaso real recortada: son **generados** con Google Nano Banana 2
(texto→imagen, 2k) pidiéndole replicar el envase de la foto de referencia. El
logotipo, por lo tanto, está **redibujado por el modelo**, no es el archivo
vectorial de la marca. Contradice la regla del estudio «la IA hace ambiente y
fondo, nunca el producto ni el logotipo» (docs/SISTEMA-DE-MARCAS.md §2), y entra
igual porque **lo decidió la diseñadora de la cuenta**. Queda escrito acá para que
nadie lo descubra dentro de seis meses.

Lo que sí mejora, medido contra el recorte del 21-09:
  · el logotipo se lee ENTERO en los tres. El vaso grande real sale «ƎTWEEN» en las
    nueve tomas de las dos sesiones — ese era el problema abierto de ayer.
  · el canto de la tapa no tiene muescas: no hubo que reconstruirlo por tono.
  · los tres vienen a plomo de fábrica, sin enderezar.
  · el recorte no deja orla: el canto está a 166–184 de distancia del beige del
    fondo, o sea no quedó nada del fondo pegado.

Y LOS TAMAÑOS TIENEN NOMBRE NUEVO — el Space los rotula por onzas, que era
justamente el dato que quedó pendiente ayer:

      ayer «chico»    →  MEDIANO  8 oz
      ayer «mediano»  →  GRANDE  12 oz
      ayer «grande»   →  EXTRA   16 oz

POR QUÉ v2 Y NO v1
------------------
El Space trae dos versiones de cada vaso. Se eligió **v2**, y no a ojo:

  · molde de la tapa (alto/ancho) entre los tres vasos —lo que hace que se lean
    como familia—: v2 dispersa **0,014**; v1 dispersa **0,077**, cinco veces y
    media más. En v1 el vaso del medio trae una tapa notoriamente más alta.
  · tono del kraft dentro del trío: v2 se desvía 8,3/255, v1 13,7/255.
  · ancho del lockup sobre el ancho del vaso, contra el vaso REAL (0,702):
    v2 da 0,635, v1 da 0,606.

LO QUE ESTE SCRIPT ARREGLA — dos cosas, las dos medidas
--------------------------------------------------------
1. **NO VENÍAN A ESCALA COMÚN.** Cada vaso se generó en su propio encuadre, así que
   el alto en píxeles no dice nada del producto: el MEDIANO salía más alto que el
   GRANDE en v1. Se reescalan a la proporción **real** del envase —0,712 / 0,861 /
   1,000—, que el 21-09 se midió sobre las fotos con dos reglas independientes (el
   horizonte de los listones de la mesa y la tapa compartida entre dos vasos). El
   trío nuevo, que sí se generó de una sola vez, la confirma: da 0,705 / 0,832 /
   1,000, dentro del 1,5–3 %.

   El factor se ata al EXTRA, que es el que menos alto nativo tiene (1217 px). Así
   **todo baja de tamaño y nada se inventa**: no hay un solo píxel interpolado
   hacia arriba.

2. **EL KRAFT NO ERA EL MISMO.** Tres generaciones son tres superficies: entre los
   tres vasos sueltos había 11/255 de diferencia, que se ve apenas los pones uno al
   lado del otro. Se iguala con **UNA** ganancia multiplicativa por canal, medida
   sobre el cuerpo limpio (26–40 % del alto, encima del logotipo) y aplicada al
   vaso entero. Multiplicativa y no aditiva para que la tapa negra y la tinta del
   logotipo conserven su relación con el kraft. Un retoque, no cinco — la lección
   de ayer fue «está sobreprocesado».

QUÉ SALE
--------
  BW-ToGo-mediano-8oz.png   ·  los tres sueltos, YA a escala común entre sí: si se
  BW-ToGo-grande-12oz.png      colocan los tres al 100 % quedan proporcionados sin
  BW-ToGo-extra-16oz.png       tocar nada
  BW-ToGo-tres-tamanos.png            ·  los tres juntos, de chico a grande
  BW-ToGo-tres-tamanos-invertido.png  ·  el mismo, de grande a chico
  BW-ToGo-trio-original.png   ·  el trío TAL COMO lo generó el modelo, de una sola
                                 vez. Una luz, una superficie, una toma. Cuando la
                                 pieza muestre los tres juntos, **este es el bueno**;
                                 los compuestos son para cuando haga falta otro
                                 orden o separarlos.

⛔ El invertido se COMPONE de nuevo, no se espeja: espejar el archivo deja el
   logotipo al revés.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw" / "hilton" / "between" / "vasos-togo-v2"
SALIDA = RAIZ / "out" / "hilton" / "between" / "vasos-togo"
BANCO = RAIZ / "public" / "assets" / "hilton" / "between" / "togo-sep2026"

# nombre corto · archivo del Space · proporción REAL del envase (medida el 21-09
# sobre las fotos, con el horizonte y con la tapa compartida)
VASOS = [
    ("mediano-8oz", "MEDIANO-8oz__PNG-transparente-v2.png", 0.712),
    ("grande-12oz", "GRANDE-12oz__PNG-transparente-v2.png", 0.861),
    ("extra-16oz", "EXTRA-16oz__PNG-transparente-v2.png", 1.000),
]
TRIO = "3-VASOS__PNG-transparente-v2.png"

MARGEN = 24  # aire alrededor de la silueta, en px


def recorte_ajustado(ruta: Path, margen: int = MARGEN) -> Image.Image:
    """Abre el PNG y lo recorta a su silueta, dejando `margen` de aire."""
    im = Image.open(ruta).convert("RGBA")
    a = np.array(im.getchannel("A"))
    ys, xs = np.nonzero(a > 8)
    caja = (
        max(0, int(xs.min()) - margen),
        max(0, int(ys.min()) - margen),
        min(im.width, int(xs.max()) + 1 + margen),
        min(im.height, int(ys.max()) + 1 + margen),
    )
    return im.crop(caja)


def tono_del_cuerpo(im: Image.Image) -> np.ndarray:
    """RGB mediano del kraft limpio: la franja 26–40 % del alto, encima del logotipo."""
    arr = np.array(im)
    a = arr[..., 3] > 250
    ys = np.nonzero(a.any(1))[0]
    y0, y1 = int(ys.min()), int(ys.max())
    alto = y1 - y0 + 1
    franja = np.zeros(a.shape, bool)
    franja[y0 + int(alto * 0.26) : y0 + int(alto * 0.40)] = True
    franja &= a
    return np.median(arr[..., :3][franja].astype(float), axis=0)


def iguala_el_kraft(im: Image.Image, objetivo: np.ndarray) -> Image.Image:
    """UNA ganancia por canal, medida en el cuerpo y aplicada al vaso entero."""
    actual = tono_del_cuerpo(im)
    ganancia = objetivo / np.maximum(actual, 1.0)
    arr = np.array(im).astype(np.float64)
    arr[..., :3] = np.clip(arr[..., :3] * ganancia, 0, 255)
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def alto_de_silueta(im: Image.Image) -> int:
    a = np.array(im.getchannel("A")) > 8
    ys = np.nonzero(a.any(1))[0]
    return int(ys.max() - ys.min() + 1)


def compone_trio(piezas: list[Image.Image], aire: int = 90) -> Image.Image:
    """Los pone en fila sobre una misma línea de base, con aire parejo."""
    alto = max(p.height for p in piezas)
    ancho = sum(p.width for p in piezas) + aire * (len(piezas) - 1)
    lienzo = Image.new("RGBA", (ancho + aire, alto + aire), (0, 0, 0, 0))
    x = aire // 2
    for p in piezas:
        # las bases se alinean: el borde inferior de la silueta, no el del lienzo
        a = np.array(p.getchannel("A")) > 8
        base = int(np.nonzero(a.any(1))[0].max())
        y = alto + aire // 2 - base - 1
        lienzo.alpha_composite(p, (x, y))
        x += p.width + aire
    # recortar el lienzo a la silueta compuesta, con el mismo margen de siempre
    a = np.array(lienzo.getchannel("A"))
    ys, xs = np.nonzero(a > 8)
    return lienzo.crop(
        (
            max(0, int(xs.min()) - MARGEN),
            max(0, int(ys.min()) - MARGEN),
            min(lienzo.width, int(xs.max()) + 1 + MARGEN),
            min(lienzo.height, int(ys.max()) + 1 + MARGEN),
        )
    )


def main() -> int:
    faltan = [n for _, n, _ in VASOS if not (ORIGEN / n).exists()]
    if faltan or not (ORIGEN / TRIO).exists():
        print("Faltan los originales del Space en %s" % ORIGEN)
        for n in faltan + ([TRIO] if not (ORIGEN / TRIO).exists() else []):
            print("   ·", n)
        return 1

    SALIDA.mkdir(parents=True, exist_ok=True)
    BANCO.mkdir(parents=True, exist_ok=True)

    crudos = [recorte_ajustado(ORIGEN / n) for _, n, _ in VASOS]

    # ── 1. el kraft de los tres, igualado a la mediana de los tres ──────────────
    tonos = np.array([tono_del_cuerpo(im) for im in crudos])
    objetivo = np.median(tonos, axis=0)
    print("Kraft antes  :", [list(t.astype(int)) for t in tonos])
    print("  desvío máximo: %.1f/255" % np.abs(tonos - tonos.mean(0)).max())
    print("Kraft objetivo:", list(objetivo.astype(int)))
    iguales = [iguala_el_kraft(im, objetivo) for im in crudos]
    despues = np.array([tono_del_cuerpo(im) for im in iguales])
    print("Kraft después:", [list(t.astype(int)) for t in despues])
    print("  desvío máximo: %.1f/255" % np.abs(despues - despues.mean(0)).max())

    # ── 2. a escala común, atado al vaso que menos alto nativo tiene ────────────
    altos = [alto_de_silueta(im) for im in iguales]
    # si cada uno estuviera al 100 %, ¿qué alto tendría la familia? el mínimo manda,
    # así todos bajan y ninguno se interpola hacia arriba
    techo = min(h / p for h, (_, _, p) in zip(altos, VASOS))
    print("\nAlto nativo de la silueta:", altos)
    print("Techo de la familia (el EXTRA al 100 %%): %.0f px" % techo)

    finales = []
    for im, (nombre, _, prop), alto in zip(iguales, VASOS, altos):
        deseado = techo * prop
        k = deseado / alto
        nuevo = im.resize(
            (max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS
        )
        finales.append(nuevo)
        print(
            "  %-12s x%.4f  silueta %4d -> %4d px   (proporción %.3f)"
            % (nombre, k, alto, alto_de_silueta(nuevo), prop)
        )

    comprobacion = [alto_de_silueta(f) for f in finales]
    print(
        "  ► proporción entregada: %s"
        % [round(h / max(comprobacion), 4) for h in comprobacion]
    )

    # ── 3. escribir ────────────────────────────────────────────────────────────
    for (nombre, _, _), im in zip(VASOS, finales):
        p = SALIDA / ("BW-ToGo-%s.png" % nombre)
        im.save(p)
        (BANCO / ("togo-vaso-%s-nobg.png" % nombre)).write_bytes(p.read_bytes())
        print("escrito %s  %dx%d" % (p.name, im.width, im.height))

    for archivo, orden in (
        ("BW-ToGo-tres-tamanos.png", finales),
        ("BW-ToGo-tres-tamanos-invertido.png", finales[::-1]),
    ):
        t = compone_trio(list(orden))
        t.save(SALIDA / archivo)
        print("escrito %s  %dx%d" % (archivo, t.width, t.height))

    # el trío tal cual salió del modelo: una luz, una superficie, una toma
    original = recorte_ajustado(ORIGEN / TRIO)
    original.save(SALIDA / "BW-ToGo-trio-original.png")
    (BANCO / "togo-vaso-trio-nobg.png").write_bytes(
        (SALIDA / "BW-ToGo-trio-original.png").read_bytes()
    )
    print(
        "escrito BW-ToGo-trio-original.png  %dx%d"
        % (original.width, original.height)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

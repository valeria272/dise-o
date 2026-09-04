#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SLIDE 4 del carrusel PROMOS TO GO (S3) — ronda 12: los tres, en formato To Go.

Eli, sobre la slide 4 de la ronda 11:

    «se ve quemada y mal. Vuelve a hacer ese diseño: Los tres productos juntos
     en formato To Go: café, alternativa salada y dulce. Una mano tomando la
     bolsa o el café refuerza la idea de llevar.»

⛔ Dos cosas estaban mal, y la segunda es la de fondo:

1. **Quemada.** El bodegón de la ronda 11 pasó por `apetitoso()` + `nitidez()`
   globales encima de un revelado que ya subía los medios. Acá el retoque es
   mínimo: la escena viene expuesta y sólo se le pone el hombro de las altas.
2. ⛔⛔ **No era «formato To Go».** La pieza mostraba un croissant y un muffin
   en PLATOS DE CERÁMICA sobre la mesa: eso es consumo en local, y el brief pide
   los tres productos *para llevar*. Y no había ninguna mano, que es la mitad de
   la indicación («una mano tomando la bolsa o el café refuerza la idea de
   llevar»). Se cambia la escena entera, no el revelado.

⭐ De dónde sale la escena: **de un editable de Eli.**
`raw/hilton/between/ediciones-ia-eli/magnific_haz-que-la-tapa-de-la-img_YVjNsSNWeC.png`
es su propio montaje —bolsa de papel kraft, vaso To Go, sándwich sobre el papel y
una mano tomando el asa—, o sea que el 80 % del brief ya estaba resuelto por la
diseñadora. Faltaba **el dulce**. Así que no se generó de cero: se editó SU
imagen con Nano Banana Pro pasándola como referencia, y hicieron falta cuatro
pasadas por razones de diagramación y de marca, todas anotadas porque cada una
descarta un camino:

  1. **el muffin** de chocolate en su pirotín, sobre el papel;
  2. **bajar los productos a la mitad inferior**: en su versión la mano y el asa
     llegaban al tercio superior, que es donde va el titular de esta slide
     (`anclaje="arriba"`), y el texto les caía encima;
  3. **la mano, rehecha**. Al mover la escena, el modelo dejó una mano con el
     pulgar suelto y sin dedos — el defecto que esta marca ya rechazó una vez
     («hay una mano de más»). Se pidió explícitamente «los cuatro dedos
     envolviendo el vaso, anatómicamente correctos» y se verificó al 300 %;
  4. ⛔⛔ **la bolsa y el vaso, LISOS.** Y ésta es la importante: el modelo
     conservaba los logotipos de la referencia, pero **redibujados**. Se
     comparó contra el vector oficial y contra la foto real del cliente: la
     silueta general acierta —incluso la «Ǝ» invertida— pero el trazo y el
     tracking no son los de la marca. Un logotipo redibujado por IA es
     exactamente lo que el cliente reclamó en la ronda 5 («el logo de between
     completamente distinto»). Así que se pidió el envase **sin ninguna letra**
     y el logotipo se ESTAMPA con el vector real, en la bolsa y en el vaso.

Proporciones del estampado, medidas — no elegidas:

  · **bolsa**: en el editable de Eli el logotipo mide **0,58 del ancho de la
    cara** y su centro cae al **54 % del alto** de la cara. Se replica.
  · **vaso**: **0,86 del ancho del cuerpo**, que es la proporción medida en el
    vaso oficial (`clients/hilton/CLAUDE.md § EL TAMAÑO del logo sobre el vaso`).
  · y en el vaso la tinta va **enmascarada al cartón**, porque los dedos van
    delante: sin eso las letras quedan pintadas sobre la mano.

Salida: public/assets/hilton/between/fotos-gradadas/togo-trio-r12.jpg
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import hombro, informe, vivo

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
#: la generación se guarda en JPEG q96 por peso: tiene que viajar en el repo
#: para que la pieza se pueda reproducir (una generación no es determinista).
GEN = RAIZ / "public/assets/hilton/between/ia-sept/togo-trio-gen.jpg"
LOGO = RAIZ / "public/assets/hilton/between/logo-negro-vector.png"
SALIDA = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-trio-r12.jpg"

#: la generación es 3:4 y la pieza 4:5: se recortan 160 px de alto, por ARRIBA,
#: que es muro oscuro desenfocado y no aporta nada.
RECORTE_ARRIBA = 160
SALIDA_PX = (2250, 2812)

#: geometría medida sobre la pieza final (2250×2812)
CARA_BOLSA = (730, 590, 1960, 2010)      # la cara frontal de la bolsa
CUERPO_VASO = (250, 1180, 690, 1990)     # el cuerpo del vaso, con la mano encima


def estampa(base, centro, ancho, mascarar_carton=False, fuerza=0.95, absorcion=0.18):
    """Multiplica el logotipo real, con escala UNIFORME (el alto sale de la
    proporción del archivo: no hay forma de achatarlo)."""
    logo = Image.open(LOGO).convert("RGBA")
    ratio = logo.width / logo.height
    alto = int(round(ancho / ratio))
    logo = logo.resize((ancho, alto), Image.LANCZOS)
    cx, cy = centro
    x1, y1 = cx - ancho // 2, cy - alto // 2

    zona = np.asarray(base.crop((x1, y1, x1 + ancho, y1 + alto))).astype(np.float64)
    lg = np.asarray(logo).astype(np.float64)
    tinta = lg[:, :, :3].mean(axis=2) / 255.0
    densidad = (lg[:, :, 3] / 255.0) * (1.0 - tinta) * fuerza
    lum = (0.299 * zona[..., 0] + 0.587 * zona[..., 1] + 0.114 * zona[..., 2]) / 255.0
    densidad *= np.clip(lum * 1.25, 0.25, 1.0)
    fuera = zona * (1.0 - densidad[..., None] * (1.0 - absorcion))

    if mascarar_carton:
        # los dedos van DELANTE: la tinta sólo cae donde hay cartón. El separador
        # es la razón B/R —el kraft queda por debajo de 0,62 y la piel por
        # encima—, con un piso de luminancia para que la sombra del pliegue no
        # cuente como vaso.
        razon = zona[..., 2] / np.maximum(zona[..., 0], 1.0)
        carton = ((razon < 0.62) & (zona[..., 0] > 100)).astype(np.uint8) * 255
        carton = cv2.morphologyEx(carton, cv2.MORPH_CLOSE,
                                  cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
        carton = cv2.morphologyEx(carton, cv2.MORPH_OPEN,
                                  cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
        m = (cv2.GaussianBlur(carton.astype(np.float32), (0, 0), 1.6) / 255.0)[:, :, None]
        fuera = zona * (1 - m) + fuera * m
        print(f"      cartón en la caja: {100 * (carton > 0).mean():.0f} %")

    salida = base.copy()
    salida.paste(Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)), (x1, y1))
    print(f"   logo {ancho}x{alto} (ratio {ratio:.4f}) en x {x1}-{x1 + ancho} · "
          f"y {y1}-{y1 + alto}")
    return salida


def main():
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN}")
    im = Image.open(GEN).convert("RGB")
    print(f"generación {im.width}x{im.height}")
    alto = int(round(im.width / 0.8))
    y0 = min(RECORTE_ARRIBA, im.height - alto)
    im = im.crop((0, y0, im.width, y0 + alto)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"recorte 4:5 desde y={y0} ({im.width}x{im.height})")
    informe(im, "generada")

    bx0, by0, bx1, by1 = CARA_BOLSA
    print("   BOLSA:")
    im = estampa(im, ((bx0 + bx1) // 2, int(by0 + 0.544 * (by1 - by0))),
                 int(round(0.58 * (bx1 - bx0))))

    print("   VASO:")
    # ⭐ El logo va por ENCIMA de los dedos, que arrancan en y=1420: la banda
    #    libre del cuerpo mide 240 px y el lockup pide 106 de alto.
    # ⚠️ Y va a 320 px de ancho, no a los 378 que salen de aplicar el 0,86 del
    #    vaso oficial. Medido: la CARA VISIBLE del cilindro en esta toma va de
    #    x=360 a x=680 (320 px) porque el vaso está cerca y girado; a 378 el
    #    logotipo se pasaba de la silueta y la máscara de cartón lo cortaba —
    #    quedaba «ƎTWEEN / OFFEE & BAR», que se lee como un error de impresión.
    #    La proporción de marca se mide sobre la cara visible, no sobre la
    #    silueta: un logo CORTADO es peor que un logo 15 % más chico.
    im = estampa(im, (520, 1300), 320, mascarar_carton=True)

    # retoque MÍNIMO: es lo que evita el «se ve quemada»
    im = vivo(im, vibrancia=0.12)
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    informe(im, "final")
    im.save(SALIDA, quality=95, subsampling=0)
    print(f"-> {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

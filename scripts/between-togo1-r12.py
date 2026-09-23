#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTADA del carrusel PROMOS TO GO (S3) — ronda 12: la escena se GENERA ENTERA.

Eli, sobre la portada de la ronda 11:

    «mira hiciste que la chica tiene recortes se ve muy mal editado. Por favor
     vuelve a editarlo […] recuerda que los textos están bien en el diseño,
     solo la foto de fondo estaba extraño»

⛔⛔ LA CAUSA, y es de método: la portada era un MONTAJE — una figura recortada
   pegada sobre un fotograma del local. Da igual cuánto se pula el canto
   (la ronda 11 le fundió el borde con un mapa de nitidez): un recorte sobre un
   fondo que no es el suyo **nunca comparte la luz**, y eso se lee. Van tres
   rondas de reclamos sobre esta misma pieza por el mismo motivo.

⭐ La salida es dejar de montar: **la escena se genera COMPLETA en una pasada**,
   con la figura y el fondo en la misma luz, y después se le estampa el
   logotipo real al vaso. No hay canto que fundir porque no hay canto.

Brief de la portada, literal de la grilla (`FEED!L11`):

    «Persona saliendo de Between con café y bolsa To Go en mano. Sensación de
     mañana en movimiento, luz natural y estética urbana.»

Cómo se hizo, paso por paso
---------------------------
1. **Se agotó el material real primero** (regla del estudio). Se sacaron 75
   fotogramas de los 25 clips `.MOV` del cliente: son TODOS interiores del hotel
   y del cowork —lobby, butacas, el muro vegetal— y **no hay ni un plano de una
   persona saliendo con un vaso**. La sesión de julio son bodegones de mesa. Así
   que la escena no existe y hay que generarla.
2. **Nano Banana Pro**, aspecto `post`, 2K, con un fotograma del MURO VEGETAL
   real del local como referencia (`IMG_1148.MOV`), y el prompt pidiendo el vaso
   **kraft LISO, sin logo ni texto** — porque el logotipo lo pone el estudio, no
   el generador (la IA se lo inventa; es el reclamo de la ronda 4).
3. **Upscaler de Magnific ×2** antes de recortar. El 4:5 que necesita la pieza
   sale de una ventana de 2.880 px del archivo de 3.584: sin el ×2 había que
   ampliar 1.440 → 2.250 (un 56 %) y la piel se empastaba.
4. **El encuadre está calculado, no elegido a ojo.** Los textos están aprobados
   («los textos están bien en el diseño»), así que la foto tiene que dejarles el
   sitio: la script del bloque arranca en y≈1.595, de modo que el vaso tiene que
   terminar antes de y≈1.500 y la cabeza tiene que quedar en el tercio alto.
   Resolviendo las dos condiciones sale una ventana de 1.440×1.800 desde y=558
   sobre el original: el vaso cierra en y=1.490 y quedan 130 px de aire sobre la
   cabeza.
5. **El logotipo se estampa en el EJE del vaso** y después se le devuelven los
   DEDOS por encima. Sin ese paso la tinta queda pintada sobre la mano: el
   estampador multiplica sobre la caja completa y no sabe qué es cartón. Los
   dedos se aíslan por la razón B/R —la piel de esta escena da 0,78 y el kraft
   0,59—, que separa las dos cosas sin tocar el vaso.

⚠️ Y lo que NO se retoca: la generación ya viene bien expuesta. Aplicarle el
   revelado del mes por costumbre es lo que dejó el vaso «un poco blanco» en el
   cumpleaños. Acá sólo va vibrancia corta y el hombro de las altas.

Salida: public/assets/hilton/between/fotos-gradadas/togo-portada-r12.jpg
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
FOTOS = RAIZ / "public/assets/hilton/between/fotos-gradadas"
#: la generación ×2 se guarda en JPEG q96, no en PNG: el PNG pesaba 29 MB y en
#: el repo tiene que VIAJAR —sin ella la portada no se reproduce, porque una
#: generación no es determinista—. Tras el recorte y la bajada a 2250 px la
#: diferencia con el PNG no es medible.
GEN = RAIZ / "public/assets/hilton/between/ia-sept/togo-portada-gen-2x.jpg"
LOGO = RAIZ / "public/assets/hilton/between/logo-negro-vector.png"
SALIDA = FOTOS / "togo-portada-r12.jpg"

#: ventana 4:5 sobre el archivo ×2 (coordenadas del original ×2)
VENTANA = (360, 1116, 2880, 3600)
SALIDA_PX = (2250, 2812)

#: el vaso en la pieza final. ⚠️ Esta caja estaba MAL MEDIDA y ése es el origen
#: de tres rondas de reclamos por el logo: decía que el cuerpo va de x=800 a
#: x=1040 (240 px) y el cuerpo real, medido a la altura del logotipo sobre la
#: generación SIN estampar, va de **825 a 1024: 199 px**. Ver LOGO_ANCHO.
VASO_CUERPO = (825, 1227, 1024, 1465)
#: ⭐⭐ RONDA 14 — Eli, por tercera vez sobre este mismo logo: «el logo del vaso
#: debes centrarlo según el vaso. Arréglalo.»
#:
#: ⛔⛔ LA CAUSA RAÍZ, y no era de centrado sino de MEDICIÓN. El manual fija el
#: tamaño en 0,86 del ancho visible del vaso (§ «El TAMAÑO del logo sobre el
#: vaso»), y las dos rondas anteriores aplicaron ese 0,86 sobre un ancho de
#: cuerpo equivocado:
#:
#:   | ronda | ancho supuesto | logo | ratio REAL sobre 199 px | qué se veía |
#:   |---|---:|---:|---:|---|
#:   | 12 | 240 px | 206 | **1,03** | el logo era MÁS ANCHO que el vaso |
#:   | 13 | «cara visible» 183 | 175 | **0,88**, centrado en 932 | la N pegada al canto derecho |
#:   | 14 | **199 px, 825-1024** | **171** | **0,86**, centrado en 924 | ✅ |
#:
#: Con 175 px centrados en 932 la tinta iba de 844 a 1019 sobre un cuerpo que
#: termina en 1024: **5 px de aire a la derecha contra 19 a la izquierda**. Eso
#: es lo que Eli lee como «no está centrado según el vaso», y tiene razón.
#:
#: ⚠️ Cómo se midió, porque el barrido de píxeles cálidos NO sirve (el manual ya
#: lo dice): se corre la máscara de cartón `B/R < 0,58 & R > 115` sobre la
#: generación **antes de estampar** —con el logo puesto, la tinta oscura corta
#: las corridas y devuelve 31 px— y se toma la corrida contigua más larga fila a
#: fila. El cuerpo entero sólo está a la vista entre y=1245 y y=1270; de ahí para
#: abajo los dedos se lo van comiendo (825 → 875 en 40 px de caída).
LOGO_ANCHO = 171
#: El centro es el EJE DEL CUERPO: (825 + 1024) / 2 = 924,5 → 924.
#: Y la altura, medida columna a columna: el cartón libre empieza en y=1244 (el
#: punto más bajo del canto de la tapa, en x=915) y el primer dedo entra en
#: y=1271 por la izquierda. El logotipo mide 56 px de alto, así que NO cabe
#: entero en la banda limpia: se apoya el borde superior en 1244 y el pie de la
#: «B» queda por detrás del dedo.
#:
#: ⭐ Y eso es lo correcto, no un mal menor. Las dos salidas alternativas son
#: peores y ya se probaron las dos: achicar el logo para que quepa rompe el
#: tamaño de marca (fue la ronda 13, y es lo que Eli devolvió), y correrlo a la
#: derecha lo saca del eje (fue la ronda 12). Un logotipo impreso que una mano
#: tapa en parte es lo que pasa de verdad al sostener un vaso. Lo que NO puede
#: pasar es que se lea descentrado.
#: Contra la ronda 13, la «B» pasa de 24 % a 52 % a la vista.
LOGO_CENTRO = (924, 1272)


def estampa(base):
    """Multiplica el logotipo real sobre el cartón, con escala UNIFORME."""
    logo = Image.open(LOGO).convert("RGBA")
    ratio = logo.width / logo.height
    alto = int(round(LOGO_ANCHO / ratio))
    logo = logo.resize((LOGO_ANCHO, alto), Image.LANCZOS)
    cx, cy = LOGO_CENTRO
    x1, y1 = cx - LOGO_ANCHO // 2, cy - alto // 2
    print(f"   logo {LOGO_ANCHO}x{alto} (ratio {ratio:.4f}) en x {x1}-{x1 + LOGO_ANCHO} · "
          f"y {y1}-{y1 + alto}")

    zona = np.asarray(base.crop((x1, y1, x1 + LOGO_ANCHO, y1 + alto))).astype(np.float64)
    lg = np.asarray(logo).astype(np.float64)
    tinta = lg[:, :, :3].mean(axis=2) / 255.0
    alfa = lg[:, :, 3] / 255.0
    densidad = alfa * (1.0 - tinta) * 0.95
    lum = (0.299 * zona[..., 0] + 0.587 * zona[..., 1] + 0.114 * zona[..., 2]) / 255.0
    densidad *= np.clip(lum * 1.25, 0.25, 1.0)
    fuera = zona * (1.0 - densidad[..., None] * (1.0 - 0.18))

    salida = base.copy()
    salida.paste(Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)), (x1, y1))
    return salida, (x1, y1, x1 + LOGO_ANCHO, y1 + alto)


def solo_sobre_el_carton(base, estampada, caja):
    """La tinta cae SÓLO donde hay cartón. Los dedos van delante del vaso.

    ⛔ El estampador multiplica sobre la caja completa y no sabe qué es cartón:
       sin este paso las letras quedan PINTADAS SOBRE LA MANO, que es peor que
       un logo tapado. Se vio a la primera pasada.

    El separador es la razón **B/R**, y está medido sobre esta escena:

        cartón kraft (claro y en sombra)   0,523 · 0,527 · 0,373
        dedos iluminados                   0,660 · 0,710

    O sea que `B/R < 0,58` aísla el cartón —incluida su sombra— y deja fuera la
    piel. Se le suma `R > 115` para que la sombra profunda del pliegue, que
    también da B/R bajo, no cuente como vaso.

    ⭐ Y el logo se queda del TAMAÑO DE MARCA (0,86 del ancho del cuerpo,
    centrado en el eje), aunque la mano tape la primera letra y media. Las dos
    alternativas eran peores: subirlo a la franja despejada de arriba obliga a
    bajarlo a 0,60 del ancho —y el tamaño del logo sobre el vaso está medido en
    el vaso oficial, no es negociable— y correrlo a la derecha lo saca del eje.
    Un logotipo impreso que una mano tapa en parte es lo que pasa de verdad al
    sostener un vaso; un logotipo achicado es un error de marca.
    """
    x1, y1, x2, y2 = caja
    a = np.asarray(base.crop((x1, y1, x2, y2))).astype(np.float32)
    b = np.asarray(estampada.crop((x1, y1, x2, y2))).astype(np.float32)
    razon = a[..., 2] / np.maximum(a[..., 0], 1.0)
    carton = ((razon < 0.58) & (a[..., 0] > 115)).astype(np.uint8) * 255
    carton = cv2.morphologyEx(carton, cv2.MORPH_CLOSE,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
    carton = cv2.morphologyEx(carton, cv2.MORPH_OPEN,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    m = (cv2.GaussianBlur(carton.astype(np.float32), (0, 0), 1.6) / 255.0)[:, :, None]
    print(f"   cartón en la caja del logo: {100 * (carton > 0).mean():.1f} % "
          f"(el resto son los dedos y quedan limpios)")
    salida = estampada.copy()
    salida.paste(Image.fromarray(np.clip(a * (1 - m) + b * m, 0, 255).astype(np.uint8)),
                 (x1, y1))
    return salida


def main():
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN}")
    im = Image.open(GEN).convert("RGB")
    print(f"generación ×2  {im.width}x{im.height}")
    x0, y0, w, h = VENTANA
    im = im.crop((x0, y0, x0 + w, y0 + h)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"ventana 4:5 {w}x{h} -> {im.width}x{im.height}")
    informe(im, "generada")

    estampada, caja = estampa(im)
    im = solo_sobre_el_carton(im, estampada, caja)

    # retoque MÍNIMO: la generación ya viene expuesta
    im = vivo(im, vibrancia=0.12)
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    informe(im, "final")
    im.save(SALIDA, quality=95, subsampling=0)
    print(f"-> {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · PORTADA (FEED 14-sep, S3 slide 1) — ronda 18: el logotipo, al fin
donde va, porque la MANO se movió.

Eli, 07-09-2026, con su propia pieza aprobada como referencia
(`C1 n°1 BW CUMPLE.png`, carpeta 1SpqdhshmBEElNZSiFnLC7pEXK3lGnKnE):

    «el logo se ve erróneo, no se ve centrado según el vaso. Tiene que ser un
     poquitito más grande, abarcando lo que es el vaso. Igual que las
     referencias reales que tiene el cliente»

⭐⭐⭐ QUÉ ESTABA MAL, MEDIDO SOBRE SU REFERENCIA

|                                   | su referencia | la ronda 16 |
|-----------------------------------|--------------:|------------:|
| ancho del logo / ancho del cuerpo |         0,795 |       0,907 |
| **centro del logo / alto del cuerpo** | **0,496** | **0,320** |
| aire lateral                      |     simétrico | **6 izq · 15 der** |

O sea que el logotipo **no era más chico de ancho — era más ancho**. Lo que
estaba mal era la ALTURA: a 0,32 queda en el tercio superior y deja media taza
de cartón vacío debajo, y eso es lo que se lee como «no centrado» y «no abarca
el vaso». Su referencia lo pone al medio, igual que el vaso oficial (0,474).

Y de paso, el aire lateral asimétrico era un error de medición mío: había puesto
el cuerpo en x 787..1027 cuando de verdad iba de 798 a 1025.

⛔⛔ Y POR QUÉ HICIERON FALTA CUATRO GENERACIONES DE ESTA MISMA FOTO

Porque el tope no era el logotipo, era la MANO. Medido, generación por
generación, la banda de cartón libre de dedos:

    r15  «agarre cerca de la base»                    83 px  → centro 0,158
    r16  «agarre en la base, dedos en el quinto bajo» 107 px  → centro 0,178
    r17  «tomado desde abajo como la referencia»       60 px  → centro 0,220
    r18  «LA MANO ENTERA POR DEBAJO DEL VASO»         293 px  → centro 0,485 ✓

⚠️ Y una que conviene no volver a pensar: **recortar más cerca NO ayuda.** La
proporción logo/cuerpo es una propiedad de la FOTO, no del encuadre: al recortar
crecen los dos igual. Lo único que mueve esa cifra es dónde está la mano.

Lo que desbloqueó la r18 fue dejar de pedir «más abajo» y pedir una condición
verificable: *la mano entera por debajo del aro blanco de la base, ni una yema
al costado del cartón*. Medido en el resultado: **0 px de piel** en todo el
cuerpo, de y=1120 a y=1300.

> **Regla: a un generador no se le pide un grado («más abajo»), se le pide una
> condición que se pueda comprobar después.** «Más abajo» dio tres fotos
> distintas y ninguna servía.

⭐ POR ESO ESTE SCRIPT ES MÁS SIMPLE QUE EL DE LA RONDA 16

Sin máscara de piel y sin la maquinaria de «los dedos tapan el logotipo»: no hay
dedos que tapen. Queda el desenfoque por nitidez del cartón limpio, el grano del
sensor, la luz local y la comba del cilindro — que ésos sí eran correctos.

Geometría medida sobre la ventana 4:5 de esta generación:

    cuerpo del vaso ....... y 1115..1408 (293)  ·  x 959..1168 (209) a media altura
    eje del vaso .......... x 1063
    logotipo a 0,90 ....... 188 × 62 px, centrado en (1063, 1257)
    aire lateral .......... 10 izq · 11 der   (simétrico)
    centro / alto ......... 0,485             (el vaso oficial: 0,474)

Se usa 0,90 y no el 0,86 del manual porque Eli pidió «un poquitito más grande»,
y el vaso oficial mide 0,89-0,92: 0,90 está dentro de la regla de marca.

Salida: public/assets/hilton/between/fotos-gradadas/togo-portada-r18.jpg
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from between_retoque import hombro, informe, vivo  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

GEN = RAIZ / "public/assets/hilton/between/ia-sept/togo-portada-gen-r18.png"
LOGO = RAIZ / "public/assets/hilton/between/logo-negro-vector.png"
PIEZA = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-portada-r18.jpg"

# Misma ventana 4:5 que las rondas 15-17, para que el bloque de texto no se
# re-flujee.
VENTANA_PIEZA = (0, 150, 3584, 4480)
SALIDA_PX = (2250, 2812)

# ── el vaso, medido fila a fila sobre la ventana de esta generación ──────────
CUERPO_Y0, CUERPO_Y1 = 1115, 1408      # de bajo la tapa al aro blanco (293)
EJE = 1063                             # el eje del vaso; el logo se centra acá
ANCHO_CARA = 209                       # la cara visible a la altura del logo

RATIO_ANCHO = 0.90     # Eli pidió «un poquitito más grande»; el oficial da 0,89-0,92
RATIO_ALTO = 0.485     # el del vaso oficial (0,474) y el de su referencia (0,496)
COMBA = 8              # px de caída al centro, del aro de la tapa

# la nitidez se mide en cartón LIMPIO, no en todo el cuerpo (lección de la r16)
CARTON_LIMPIO = (1000, 1140, 1140, 1215)


def geometria():
    logo = Image.open(LOGO).convert("RGBA")
    ratio = logo.width / logo.height
    anc = int(round(ANCHO_CARA * RATIO_ANCHO))
    alt = int(round(anc / ratio))
    alto_cuerpo = CUERPO_Y1 - CUERPO_Y0
    cy = int(round(CUERPO_Y0 + alto_cuerpo * RATIO_ALTO))
    return logo, ratio, anc, alt, EJE - anc // 2, cy - alt // 2, cy, alto_cuerpo


def comba(dens, px):
    """Curva el sello siguiendo el cilindro: cada columna se desplaza en Y.
    NO deforma — conserva escala y proporción, que es lo que el manual prohíbe
    tocar."""
    al, an = dens.shape
    salida = np.zeros((al + px + 2, an), np.float64)
    xs = np.linspace(-1.0, 1.0, an)
    caida = (1.0 - xs ** 2) * px
    for x in range(an):
        d = int(round(caida[x]))
        salida[d:d + al, x] = dens[:, x]
    return salida


def estampa(base):
    logo, ratio, anc, alt, x1, y1, cy, alto_cuerpo = geometria()
    logo = logo.resize((anc, alt), Image.LANCZOS)
    print(f"   logo {anc}×{alt} en x {x1}..{x1 + anc} · y {y1}..{y1 + alt}")
    print(f"   ancho/cara {anc / ANCHO_CARA:.3f} · "
          f"centro/alto {(cy - CUERPO_Y0) / alto_cuerpo:.3f} "
          f"(vaso oficial 0,474 · su referencia 0,496)")

    lg = np.asarray(logo).astype(np.float64)
    tinta = lg[:, :, :3].mean(axis=2) / 255.0
    densidad = (lg[:, :, 3] / 255.0) * (1.0 - tinta) * 0.95
    densidad = comba(densidad, COMBA)
    alt_c = densidad.shape[0]
    zona = np.asarray(base.crop((x1, y1, x1 + anc, y1 + alt_c))).astype(np.float64)

    gris = cv2.cvtColor(np.asarray(base.crop(CARTON_LIMPIO)), cv2.COLOR_RGB2GRAY)
    nit = cv2.Laplacian(gris, cv2.CV_64F).var()
    radio = float(np.clip(1.6 - nit / 90.0, 0.35, 1.6))
    # ⛔⛔ EL DESENFOQUE TIENE UN TOPE QUE DEPENDE DEL TAMAÑO DEL SELLO, y sin él
    # la fórmula se pasa. Acá el cartón mide 11 de varianza —está muy fuera de
    # foco— así que pedía 1,47 px. Pero el lockup entra a 62 px de alto: la línea
    # «COFFEE & BAR» mide ~8 px con trazos de 1 px, y 1,47 px de desenfoque los
    # borra. Comparado con la referencia de Eli, la tinta salía clara y blanda.
    #
    # Regla: el desenfoque no puede pasar de ~1/80 del alto del lockup, que es el
    # orden del trazo más fino que tiene que sobrevivir.
    tope = alt_c / 80.0
    if radio > tope:
        print(f"   desenfoque {radio:.2f} px recortado al tope {tope:.2f} px "
              f"(lockup de {alt_c} px: el trazo fino no aguanta más)")
        radio = tope
    densidad = cv2.GaussianBlur(densidad, (0, 0), max(radio, 0.25))
    print(f"   nitidez del cartón limpio {nit:.0f} → el sello se funde a {radio:.2f} px")

    lum = (0.299 * zona[..., 0] + 0.587 * zona[..., 1] + 0.114 * zona[..., 2]) / 255.0
    densidad *= np.clip(lum * 1.25, 0.25, 1.0)

    grano = float(np.std(gris.astype(np.float64) - cv2.GaussianBlur(
        gris.astype(np.float64), (0, 0), 1.5)))
    ruido = np.random.default_rng(2026).normal(0.0, grano, size=densidad.shape)
    print(f"   grano del cartón: sigma {grano:.2f}")

    fuera = (zona * (1.0 - densidad[..., None] * (1.0 - 0.18))
             + (ruido * (densidad > 0.02))[..., None])
    salida = base.copy()
    salida.paste(Image.fromarray(np.clip(fuera, 0, 255).astype(np.uint8)), (x1, y1))
    return salida


def main():
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN}")
    im = Image.open(GEN).convert("RGB")
    x0, y0, w, h = VENTANA_PIEZA
    im = im.crop((x0, y0, x0 + w, y0 + h)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"ventana 4:5 {w}×{h} desde y={y0} -> {im.width}×{im.height}")
    informe(im, "generada")

    im = estampa(im)
    im = vivo(im, vibrancia=0.12)
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    informe(im, "final")
    PIEZA.parent.mkdir(parents=True, exist_ok=True)
    im.save(PIEZA, quality=95, subsampling=0)
    print(f"-> {PIEZA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

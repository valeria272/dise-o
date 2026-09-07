#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · PORTADA (FEED 14-sep, S3 slide 1) — ronda 16: el logotipo, donde va.

Eli, 07-09-2026: «Arregla el logo del slide 1 [de la S3]».

⭐⭐⭐ LA CAUSA, MEDIDA — Y ES LA MISMA QUE ELLA YA RECLAMÓ UNA VEZ

Medido con cuadrícula sobre la entrega de la ronda 15:

    cuerpo visible del vaso ........ y 1155..1440  (285 px)
    centro del logotipo ............ y 1200
    ratio (centro − tapa) / cuerpo .. 0,158

Y en el manual, de la ronda 9, con las palabras de Eli:

    ancho del lockup / ancho del cuerpo ..... vaso real 0,92 · aceptado 0,72
    centro del lockup / alto del cuerpo ..... vaso real 0,485 · aceptado 0,32
    «centrar más el logo en el vaso, que se vea real, como en las imágenes
     reales de Between» — Eli, 03-09
    «El defecto que Eli vio era la ALTURA: el logo iba pegado a la tapa, y eso
     es lo que lo delata como calcomanía.»

O sea: **la ronda 15 volvió a 0,158 — una regresión sobre el 0,32 que ya se había
aceptado.** No es un problema de grano ni de desenfoque (los dos están aplicados
y medidos: 1,36 px y sigma 2,01). Es la posición.

⛔⛔ Y POR QUÉ LAS CUATRO RONDAS ANTERIORES NO PUDIERON ARREGLARLO

Porque todas trataron de **esquivar la mano**: buscaban el rectángulo de cartón
limpio más grande y metían el logotipo ahí. Ese rectángulo está siempre arriba,
pegado a la tapa — porque los dedos cruzan el centro del vaso. Y cruzan el centro
por una razón que ninguna ronda podía cambiar: **así se toma un vaso.**

    generación r15 · banda limpia bajo la tapa .....  83 px
    generación r16 · banda limpia bajo la tapa ..... 107 px  (el agarre más abajo)

Ni bajando el agarre alcanza: 107 px de banda sobre un cuerpo de 297 dan un
centro en 0,178. El camino estaba agotado.

⭐⭐⭐ LA SALIDA: EL LOGOTIPO NO ESQUIVA LOS DEDOS — LOS DEDOS LO TAPAN

En un vaso real impreso, la mano **oculta parte del logotipo**. Es lo normal y es
justo lo que le falta a un estampado para no parecer calcomanía: un logotipo que
esquiva la mano se lee pegado; uno parcialmente escondido detrás de un dedo se
lee impreso.

Así que el logotipo va donde le corresponde —centrado en el eje del vaso, a 0,86
de su ancho, a 0,38 de su alto— y donde los dedos pasan por delante, **se
enmascara**. La piel se separa del cartón por color, medido en esta toma:

    zona                  G/R     B/G
    cartón limpio        0,736   0,793
    cartón bajo (der)    0,742   0,798
    piel · yema índice   0,572   0,897
    piel · dedo 2        0,573   0,884
    piel · dedo 3        0,582   0,873

`G/R` separa los dos sin ambigüedad: el umbral va en 0,665.

⭐ Y LA COMBA, que también sale de la cuadrícula. El aro inferior de la tapa cae
**14 px** del canto al centro (y=1120 en x=800, y=1135 en x=907, y=1122 en
x=1020): la toma mira el vaso ligeramente desde arriba, así que una línea que da
la vuelta al cilindro se ve **combada hacia abajo**. El sello se comba 8 px, la
mitad — es el efecto a media altura del cuerpo, no en el canto.
⚠️ Combar NO es deformar: cada columna del logotipo se desplaza en Y, y el
logotipo conserva su escala y su proporción. Eso lo prohíbe el manual y sigue
prohibido.

Se conservan del r15 el desenfoque por nitidez de la zona y el grano del sensor,
que ésos sí estaban bien.

Uso:
    python scripts/between-togo1-r16.py            # compone la pieza
    python scripts/between-togo1-r16.py medir      # sólo imprime la geometría

Salida: public/assets/hilton/between/fotos-gradadas/togo-portada-r16.jpg
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from between_retoque import hombro, informe, vivo  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

GEN = RAIZ / "public/assets/hilton/between/ia-sept/togo-portada-gen-r16.png"
LOGO = RAIZ / "public/assets/hilton/between/logo-negro-vector.png"
PIEZA = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-portada-r16.jpg"

# Misma ventana 4:5 que la ronda 15, para que el bloque de texto YA APROBADO
# siga calzando sin re-flujar nada.
VENTANA_PIEZA = (0, 150, 3584, 4480)
SALIDA_PX = (2250, 2812)

# ── el vaso, medido con cuadrícula sobre la ventana de esta generación ───────
CUERPO_Y0, CUERPO_Y1 = 1128, 1425        # de bajo la tapa al anillo blanco (297)
CUERPO_X0, CUERPO_X1 = 787, 1027         # a media altura (240)
EJE = (CUERPO_X0 + CUERPO_X1) // 2       # 907 — el logo se centra acá, siempre

RATIO_ANCHO = 0.86      # del ancho del cuerpo. Regla del manual, medida en el vaso oficial
# ⚠️ 0,32 y no 0,38, y la razón salió de mirar el render al 400 %: a 0,38 la
# segunda línea del lockup caía sobre la yema del índice y la máscara de piel se
# comía el «CO» de COFFEE. El dedo tapando la base de la «B» se lee IMPRESO —es
# el efecto que se buscaba— pero «COFFEE» leyéndose «FFEE» se lee como un typo,
# no como una oclusión, porque ahí el canto del dedo es pálido y de bajo
# contraste y el ojo no lo acepta como algo que tape dos letras enteras.
# 0,32 es además el valor que el manual registra como ACEPTADO en la ronda 9.
RATIO_ALTO = 0.32       # del alto del cuerpo. El vaso real da 0,485; con mano, 0,32
COMBA = 8               # px de caída del centro respecto de los cantos
UMBRAL_PIEL = 0.665     # G/R por debajo de esto es piel, por encima es cartón

# ⚠️ La nitidez del cartón se mide en un parche LIMPIO, no en todo el cuerpo.
# Medido en todo el cuerpo daba 125 de varianza —porque ahí entran los cantos de
# los dedos y el aro blanco de la base, que son estructura de alto contraste— y
# con eso la fórmula pedía 0,35 px de desenfoque, o sea ninguno: volvía el canto
# matemático que es justo lo que se lee como calcomanía. Sobre cartón limpio la
# cifra es la del papel, que es lo que el sello tiene que igualar.
CARTON_LIMPIO = (900, 1150, 1020, 1225)


def geometria():
    anc_cuerpo = CUERPO_X1 - CUERPO_X0
    alto_cuerpo = CUERPO_Y1 - CUERPO_Y0
    logo = Image.open(LOGO).convert("RGBA")
    ratio = logo.width / logo.height
    anc = int(round(anc_cuerpo * RATIO_ANCHO))
    alt = int(round(anc / ratio))
    cy = int(round(CUERPO_Y0 + alto_cuerpo * RATIO_ALTO))
    x0, y0 = EJE - anc // 2, cy - alt // 2
    return logo, ratio, anc, alt, x0, y0, cy, anc_cuerpo, alto_cuerpo


def mide():
    logo, ratio, anc, alt, x0, y0, cy, ac, al = geometria()
    print(f"cuerpo del vaso   x {CUERPO_X0}..{CUERPO_X1} ({ac})   "
          f"y {CUERPO_Y0}..{CUERPO_Y1} ({al})   eje x={EJE}")
    print(f"logotipo          {anc}×{alt} (ratio {ratio:.4f})   "
          f"x {x0}..{x0 + anc}   y {y0}..{y0 + alt}")
    print(f"  ancho / cuerpo  {anc / ac:.3f}   (el manual pide 0,86)")
    print(f"  centro / alto   {(cy - CUERPO_Y0) / al:.3f}   "
          f"(vaso real 0,485 · ronda 15 entregó 0,158)")
    print(f"  aire lateral    {x0 - CUERPO_X0} izq · {CUERPO_X1 - (x0 + anc)} der")
    print(f"  comba           {COMBA} px de caída al centro")


def comba(dens, px):
    """Desplaza cada columna en Y siguiendo una parábola: el centro cae `px`.

    Es la curvatura de una línea que da la vuelta al cilindro visto un poco desde
    arriba. NO cambia la escala ni la proporción del logotipo — sólo lo curva—,
    así que no viola la regla de que el logotipo no se deforma."""
    al, an = dens.shape
    salida = np.zeros((al + px + 2, an), np.float64)
    xs = np.linspace(-1.0, 1.0, an)
    caida = ((1.0 - xs ** 2) * px)            # 0 en los cantos, px en el centro
    for x in range(an):
        d = int(round(caida[x]))
        salida[d:d + al, x] = dens[:, x]
    return salida


def mascara_piel(zona):
    """1 donde hay PIEL (los dedos delante del vaso), 0 donde hay cartón.
    Se suaviza el canto: un recorte binario de piel deja un diente visible."""
    a = zona.astype(np.float32)
    gr = a[..., 1] / np.maximum(a[..., 0], 1.0)
    piel = (gr < UMBRAL_PIEL).astype(np.float32)
    piel = cv2.morphologyEx(piel, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    piel = cv2.morphologyEx(piel, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    return cv2.GaussianBlur(piel, (0, 0), 2.2)


def estampa(base):
    logo, ratio, anc, alt, x1, y1, cy, ac, al = geometria()
    logo = logo.resize((anc, alt), Image.LANCZOS)
    print(f"   logo {anc}×{alt} en x {x1}..{x1 + anc} · y {y1}..{y1 + alt}")
    print(f"   ancho/cuerpo {anc / ac:.3f} · centro/alto {(cy - CUERPO_Y0) / al:.3f}")

    lg = np.asarray(logo).astype(np.float64)
    tinta = lg[:, :, :3].mean(axis=2) / 255.0
    densidad = (lg[:, :, 3] / 255.0) * (1.0 - tinta) * 0.95

    # ── la comba del cilindro
    densidad = comba(densidad, COMBA)
    alt_c = densidad.shape[0]
    zona = np.asarray(base.crop((x1, y1, x1 + anc, y1 + alt_c))).astype(np.float64)

    # ── el desenfoque, desde la nitidez del propio cartón (igual que la r15)
    gris = cv2.cvtColor(np.asarray(base.crop(CARTON_LIMPIO)), cv2.COLOR_RGB2GRAY)
    nit = cv2.Laplacian(gris, cv2.CV_64F).var()
    radio = float(np.clip(1.6 - nit / 90.0, 0.35, 1.6))
    densidad = cv2.GaussianBlur(densidad, (0, 0), radio)
    print(f"   nitidez del cartón {nit:.0f} → el sello se funde a {radio:.2f} px")

    # ── ⭐ LOS DEDOS TAPAN EL LOGOTIPO: se resta la piel de la densidad de tinta
    piel = mascara_piel(zona)
    cubierto = float((densidad * piel).sum() / max(densidad.sum(), 1e-6))
    densidad = densidad * (1.0 - piel)
    print(f"   los dedos tapan el {100 * cubierto:.1f} % de la tinta del logotipo")

    # ── la luz: la tinta se apaga donde el cartón está en sombra
    lum = (0.299 * zona[..., 0] + 0.587 * zona[..., 1] + 0.114 * zona[..., 2]) / 255.0
    densidad *= np.clip(lum * 1.25, 0.25, 1.0)

    # ── el grano del sensor, medido en el propio cartón
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
        sys.exit(f"falta la generación: {GEN}")
    im = Image.open(GEN).convert("RGB")
    x0, y0, w, h = VENTANA_PIEZA
    im = im.crop((x0, y0, x0 + w, y0 + h)).resize(SALIDA_PX, Image.LANCZOS)
    print(f"ventana 4:5 {w}×{h} desde y={y0} -> {im.width}×{im.height}")
    informe(im, "generada")

    im = estampa(im)

    # retoque MÍNIMO: la generación ya viene expuesta. Misma mano que la r15.
    im = vivo(im, vibrancia=0.12)
    im = Image.fromarray(
        np.clip(hombro(np.asarray(im).astype(np.float32)), 0, 255).astype(np.uint8))
    informe(im, "final")
    PIEZA.parent.mkdir(parents=True, exist_ok=True)
    im.save(PIEZA, quality=95, subsampling=0)
    print(f"-> {PIEZA.relative_to(RAIZ)}")


if __name__ == "__main__":
    accion = sys.argv[1] if len(sys.argv) > 1 else "componer"
    {"medir": mide, "componer": compone}[accion]()

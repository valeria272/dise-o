#!/usr/bin/env python3
"""QB · banner web 1920×300 octubre — franja «¡SÁBADOS DE OCTUBRE!» del momento 40 % CMR.

El banner vive en el Canva de Eli (DAHWyTySL9g) y es animado: 20 % → 40 %/30 % → Banco de
Chile. La franja verde original es una imagen aplanada y borrosa, así que su texto no se
edita. Este script la REDIBUJA NÍTIDA completa (degradado, rótulo, bajada y logos)
al doble de la resolución del export, para subirla como PNG y ponerla encima.

Ronda 1 (01-10): se calzó el texto nuevo al desenfoque del original → Eli: «se ve
desenfocado y mal». Lo que se agrega va nítido, no imitando el defecto de la base.

Uso:
    python scripts/qb-banner-web-franja-sabados.py out/qb/oct/banner-web/_antes/cuadro-200-momento-40.png <salida.png>

El cuadro es uno quieto del export mp4 de Canva (3642×568), p. ej. el 200.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "public/assets/fonts/Montserrat.ttf"
LOGOS = RAIZ / "public/assets/hilton/qb/oct/logo-club-restaurantes-bf.png"

# Medido sobre el export de Canva (3642×568).
Y0, Y1 = 468, 568                 # la franja, ya en verde pleno (100 filas)
CUERPO, BASE = 55.5, 537.5        # Montserrat Bold; línea base de los dos textos
X_ROTULO = 272                    # el original parte en 295; se corre 23 px para dejar aire antes del punto
X_LOGOS, ANCHO_LOGOS = 2845, 488  # los logos no se mueven
CENTRO_Y = 516.5                  # eje de la franja (ahí van los puntos de Eli y los logos)
CUERPO_ROTULO = 50.0              # el original mide 55,5; «¡SÁBADOS DE OCTUBRE!» no cabe antes del punto (x 993)
X_BAJADA = 1110                   # donde parte la bajada en las otras franjas
ROTULO = "¡SÁBADOS DE OCTUBRE!"
BAJADA = "Ven y disfruta tu beneficio con Banco Falabella"
BLANCO, S = (250, 250, 250), 2    # S = sobremuestreo de salida
# Canva calcula el encuadre con una miniatura de 800 px de ancho y alto ENTERO: si la
# proporción no da un alto exacto, agranda la imagen para cubrir la caja (2,8 % en la
# ronda 2). 7200×198 = 800×22 exacto → caja de 1920×52,8 en la página, sin recorte.
SALIDA = (7200, 198)


def main() -> None:
    ref = np.asarray(Image.open(sys.argv[1]).convert("RGB")).astype(float)
    ancho = ref.shape[1]

    # Degradado horizontal del fondo: mediana de filas sin texto, suavizada.
    fila = np.median(ref[470:478], axis=0)
    k = 121
    nucleo = np.ones(k) / k
    fila = np.stack([np.convolve(np.pad(fila[:, c], k // 2, mode="edge"), nucleo, "valid") for c in range(3)], 1)
    fondo = np.repeat(fila[None], Y1 - Y0, axis=0).clip(0, 255).astype("uint8")
    im = Image.fromarray(fondo).resize((ancho * S, (Y1 - Y0) * S), Image.BICUBIC)
    d = ImageDraw.Draw(im)

    fuente = ImageFont.truetype(str(FUENTE), CUERPO * S)
    fuente.set_variation_by_axes([700])
    f_rotulo = ImageFont.truetype(str(FUENTE), CUERPO_ROTULO * S)
    f_rotulo.set_variation_by_axes([700])
    base = (BASE - Y0) * S

    # Rótulo: el «¡» se apoya en la línea base, como en el original.
    x = X_ROTULO * S
    d.text((x, base), ROTULO[0], font=f_rotulo, fill=BLANCO, anchor="lb")
    x += f_rotulo.getlength(ROTULO[0])
    d.text((x, base), ROTULO[1:], font=f_rotulo, fill=BLANCO, anchor="ls")
    fin_rotulo = (x + f_rotulo.getlength(ROTULO[1:])) / S

    # Ronda 3 (Eli): sin los dos puntos (son elementos aparte en su Canva) y con la bajada
    # donde va en las otras franjas; el rótulo baja de cuerpo para terminar antes del punto.
    d.text((X_BAJADA * S, base), BAJADA, font=fuente, fill=BLANCO, anchor="ls")

    logos = Image.open(LOGOS).convert("RGBA")
    logos = logos.crop(logos.getbbox())
    alto = round(ANCHO_LOGOS * S * logos.height / logos.width)
    logos = logos.resize((ANCHO_LOGOS * S, alto), Image.LANCZOS)
    im.paste(logos, (X_LOGOS * S, round((CENTRO_Y - Y0) * S - alto / 2)), logos)

    im = im.resize(SALIDA, Image.LANCZOS)
    im.save(sys.argv[2])
    print(f"{sys.argv[2]} {im.size} - rotulo hasta {fin_rotulo:.0f} (punto de Eli en 993-1016)")
    alto_pag = 1920 * SALIDA[1] / SALIDA[0]
    print(f"en la pagina: left 0, top {300 - alto_pag:.2f}, ancho 1920, alto {alto_pag:.2f}")


if __name__ == "__main__":
    main()

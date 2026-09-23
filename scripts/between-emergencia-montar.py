#!/usr/bin/env python3
"""Monta el fondo definitivo de la ST «EMERGENCIA BETWEEN»: la vitrina a escala.

⭐ RONDA 8 — 02-09-2026. Por qué existe este paso y no se usa la generación tal cual.

El generador devuelve la vitrina ocupando el **61 % del alto** del 9:16. Se ve
imponente sola, pero con ese tamaño **no queda sitio para los textos fuera de la
caja**, y eso es justo lo que pidieron los dos comentarios de esta ronda:

    Cliente: «No se cacha bien al tapar la vitrina con el texto.»
    Scarlette: «ojo con la diagramación de los textos: tapa mucho la caja.»

Medido sobre la generación, llevada a lienzo de 1080×1920:

    banda libre ARRIBA de la caja   250 → 373   =  123 px   ← no cabe el titular
    banda libre ABAJO de la caja   1542 → 1580  =   38 px   ← no cabe nada

O sea: o la caja es enorme y el texto la pisa, o el texto respira y la caja baja
de tamaño. **No hay una tercera opción dentro de las zonas seguras de Meta**
(250 px arriba, 340 px abajo en historias).

Así que la caja se monta a la escala que deja las dos bandas:

    titular       268 →  470
    LA VITRINA    560 → 1235      (675 px de alto y ~686 de ancho, 64 % del ancho)
    bajada       1290
    encuesta     1350 → 1546      (termina antes de la zona segura inferior, 1580)

⚠️ Los 675 px de alto NO son estéticos, salen de una resta: el sticker de la
encuesta mide 196 px y la zona segura inferior de Meta empieza en 1580, así que
la encuesta no puede arrancar después de 1384 y la caja tiene que haber
terminado antes. Con la generación tal cual —la caja llega a y=1355— el QA
marcaba «entra 52 px en la zona segura».

Sigue siendo el único objeto de la pieza, centrado y sobre fondo liso: eso es el
«protagonismo» que pide Scarlette. Lo que se sacrifica son 370 px de alto que
sólo servían para que el texto le cayera encima.

⚠️ Por qué se monta en PIL y no se escala el `<Img>` en Remotion: el fondo trae
un degradado vertical suave. Si se encoge la imagen entera queda un canto visible
donde termina; acá se reconstruye el degradado a lienzo completo y la caja se
pega con un desvanecido de 70 px, así no hay costura.

Entrada:  la generación YA con el logotipo estampado en el vaso.
Salida:   `public/assets/hilton/between/ia-sept/emergencia-fondo.png` (2250×4000).
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ENTRADA = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-caja-4-logo.png"
SALIDA = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-fondo.png"

W, H = 2250, 4000          # el lienzo de entrega (1080×1920 × 2,0833)
K = W / 1080.0

#: Recorte de la vitrina en la generación, con aire para que entre su sombra.
CAJA = (380, 1640, 2740, 3960)
#: Dónde va, en px de 1080. Ver la tabla del encabezado.
CAJA_TOP, CAJA_ALTO = 560, 675
DESVANECIDO = 70           # px de borde difuminado, para que no se note la costura


def main():
    if not ENTRADA.is_file():
        sys.exit(f"✗ Falta {ENTRADA}\n  Genera antes con "
                 f"scripts/between-emergencia-magnific.py y estampa el logotipo.")
    src = Image.open(ENTRADA).convert("RGB")
    a = np.asarray(src).astype(np.float64)

    # 1. El degradado del fondo: la mediana de los 120 px de la izquierda, fila a
    #    fila. Es fondo puro (la vitrina está centrada), así que da el degradado
    #    real sin contaminarse con el objeto.
    col = np.median(a[:, :120], axis=1)                      # (alto_src, 3)
    filas = np.linspace(0, col.shape[0] - 1, H)
    grad = np.empty((H, 3))
    for c in range(3):
        grad[:, c] = np.interp(filas, np.arange(col.shape[0]), col[:, c])
    lienzo = Image.fromarray(
        np.repeat(grad[:, None, :], W, axis=1).round().astype(np.uint8), "RGB")

    # 2. La vitrina, recortada y llevada a su alto de destino
    caja = src.crop(CAJA)
    alto = int(round(CAJA_ALTO * K))
    ancho = int(round(caja.width * alto / caja.height))
    caja = caja.resize((ancho, alto), Image.LANCZOS)

    # 3. ⭐ MONTAJE ADITIVO — no se pega un rectángulo, se suma la DIFERENCIA.
    #
    # ⛔ Lo que no funcionó: pegar el recorte con el canto desvanecido. El
    #    recorte trae su propio trozo de fondo y, sobre todo, **la sombra de la
    #    caja**, que sigue cayendo más abajo del recorte. Al pegarlo quedaba una
    #    banda horizontal visible donde la sombra se cortaba de golpe. Igualar el
    #    fondo fila a fila tampoco bastó: el problema no era el tono del fondo,
    #    era que la sombra terminaba en un canto recto.
    #
    # ✅ Lo que sí: para cada fila se estima el fondo del propio recorte (la
    #    mediana de sus 30 px de la izquierda, que son crema puro) y se suma al
    #    lienzo **sólo lo que el recorte se aparta de ese fondo**. Donde el
    #    recorte es fondo, la diferencia es 0 y queda el lienzo intacto; donde
    #    hay caja o sombra, se traslada tal cual con su intensidad. La sombra se
    #    desvanece sola y no hay ningún borde que disimular.
    cj = np.asarray(caja).astype(np.float64)
    y0 = int(round(CAJA_TOP * K))
    x0 = (W - ancho) // 2
    fondo_recorte = np.median(cj[:, :30], axis=1)             # (alto, 3)
    delta = cj - fondo_recorte[:, None, :]

    # un desvanecido suave en los cantos, sólo para matar el ruido residual de la
    # estimación (no para tapar una costura: ya no la hay)
    m = np.zeros((alto, ancho), np.float64)
    d = int(DESVANECIDO)
    m[d:alto - d, d:ancho - d] = 1.0
    m = np.asarray(Image.fromarray((m * 255).astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(d / 2.2))).astype(np.float64) / 255.0

    base = np.asarray(lienzo).astype(np.float64)
    base[y0:y0 + alto, x0:x0 + ancho] += delta * m[:, :, None]
    lienzo = Image.fromarray(np.clip(base, 0, 255).round().astype(np.uint8), "RGB")
    x, y = x0, y0
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(SALIDA)

    print(f"{SALIDA.name}  {W}×{H}")
    print(f"  vitrina {ancho}×{alto} px  en ({x},{y})")
    print(f"  en lienzo de 1080: x {x/K:.0f}–{(x+ancho)/K:.0f} · "
          f"y {y/K:.0f}–{(y+alto)/K:.0f}  ({ancho/K/1080:.0%} del ancho)")
    print("  bandas libres:  arriba hasta y=%.0f · abajo desde y=%.0f"
          % (y / K, (y + alto) / K))


if __name__ == "__main__":
    main()

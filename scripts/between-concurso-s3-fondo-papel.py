#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cambia la PARED de las dos láminas del carrusel del concurso por UNA hoja de
papel beige, plana y continua entre las dos.

Pedido de Eli, 16-09-2026 (ronda 4):

    «El fondo debe ser el mismo beige papel para ambas slides, que sea plano y
     transicione.»

## Qué estaba mal, medido

Las dos escenas se generaron por separado y traían **dos paredes distintas**: la
portada, una pared lisa gris-beige; la slide 2, un panel de **veta vertical de
madera** más rosado. La ronda 3 igualó la ILUMINACIÓN de las dos (salto en la
costura de 18,7 → 0,95) pero no podía igualar el MATERIAL: la veta seguía ahí y
seguían siendo dos superficies.

    fondo de la portada      mediana  RGB 220 · 202 · 187
    fondo del escritorio     mediana  RGB 226 · 201 · 187
    desviación de luminancia dentro de cada lámina: 7,0 y 7,5 niveles

## Qué hace este script

**No** se vuelve a generar nada: el retrato y el bodegón están aprobados y
regenerar significa perderlos. Se cambia sólo la superficie de atrás.

1. **La máscara de pared, por componentes conexas a resolución completa.**
   ⛔ El crecimiento desde el canto que usaba `between-concurso-s3-fondo-continuo.py`
   **no sirve acá**: crece sobre la imagen reducida a ¼ con `binary_dilation(12)`,
   o sea saltos de 48 px reales, y **salta por encima del borde blanco del
   recorte**. Para corregir la iluminación daba igual (la fuga se comía una
   corrección de baja frecuencia); para REEMPLAZAR el fondo es fatal: pintaba
   papel encima del escritorio y del portacredencial. Medido, la fuga metía el
   escritorio entero en el «fondo» (89,1 % del cuadro en vez de 84,2 %).
   Acá se etiqueta `pared` con `scipy.ndimage.label` a resolución completa y se
   **conservan sólo las componentes que tocan el canto SUPERIOR**. La pared toca
   el canto de arriba en las dos láminas; el escritorio, que se va por el canto
   de abajo y por el derecho, no lo toca nunca. Sin fugas y sin lista de
   excepciones.

2. **La hoja de papel se SINTETIZA y se corta en dos**, que es la forma de que
   «transicione»: se genera UNA sola hoja de 4500 × 2813 —el ancho de las dos
   láminas juntas— y cada lámina se queda con su mitad. La continuidad no se
   corrige, existe por construcción: el grano de la columna 2249 de la portada y
   el de la columna 0 de la slide 2 son vecinos de la misma hoja.

   La receta es la de `between-st-s3-materiales.py`, la misma que Eli aprobó para
   el cartel de la story del 18-09: grano fino + fibra horizontal + un manchado
   muy leve, con semilla fija para que esto se reproduzca byte a byte.
   ⚠️ El **manchado baja de 2,8 a 1,4**: a 2,8 funciona en un cartel de 1700 px,
   pero a sangre en 4500 px se lee como nubes y ella pidió **plano**.

3. **El tono no se inventa: es la mediana de las dos paredes aprobadas**,
   `#DFC9BB`. Así el papel entra en el sitio exacto que ocupaba la pared y NINGÚN
   contraste ya medido de la pieza se mueve.
   ⛔ Y por eso **no** se usa el `papel-beige.png` de la story, que está tintado
   en el beige de marca `#FFF9EB`: a sangre, ese crema deja el borde blanco del
   recorte en 1,05:1 —el sticker deja de existir— y la tarjeta crema de la slide
   2, que no tiene contorno, se funde con el fondo. Con `#DFC9BB`:

       café #675B49 (titular)   4,17 : 1     (la marca pide 3:1)
       blanco del contorno      1,59 : 1
       crema #FFF9EB (tarjeta)  1,51 : 1

4. **La sombra de contacto se rehace con el peso que ya tenía.** Al sacar la
   pared se va también la sombra que el generador había puesto bajo el recorte, y
   sin ella el sticker es un papel pegado (la misma regla que el manual ya tiene
   escrita para los montajes). Se vuelve a poner desde la silueta, y **no a ojo**:
   se midió el perfil que traían las láminas aprobadas —cociente contra su propio
   campo de iluminación, por franjas de distancia al recorte— y se ajustó la
   síntesis a ese perfil.

       distancia al recorte    1–6 px    6–12 px   12–25 px   >25 px
       aprobado (medido)       0,948     0,977     0,998      1,000
       este script             0,946     0,984     0,999      1,000

   Es una sombra CORTA y pegada al filo, no un halo: a 25 px ya no existe.

Uso:  python scripts/between-concurso-s3-fondo-papel.py

Entra   `c1-portada.jpg` · `c1-escritorio.jpg`      (las escenas aprobadas)
Sale    `c1-portada-papel.jpg` · `c1-escritorio-papel.jpg`
        Las escenas NO se tocan — son la fuente y quedan para la próxima ronda.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import (binary_dilation, distance_transform_edt,
                           gaussian_filter, label)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
DIR = RAIZ / "public/assets/hilton/between/concurso-s3"
LAMINAS = [("c1-portada.jpg", "c1-portada-papel.jpg"),
           ("c1-escritorio.jpg", "c1-escritorio-papel.jpg")]

#: Mediana medida de las DOS paredes aprobadas. Ver el punto 3 de la cabecera.
TONO = np.array([223.0, 201.0, 187.0])          # #DFC9BB
SEMILLA = 20260916

#: Amplitudes del papel, en niveles sobre 255. Grano y fibra son los de
#: `between-st-s3-materiales.py`; el manchado baja a 1,4 (punto 2).
AMP_GRANO, AMP_FIBRA, AMP_MANCHA = 2.4, 3.6, 1.4

#: La luz de la hoja: un campo radial MUY suave sobre el par completo, +3 en el
#: centro y −4 en los cantos de afuera. Son 7 niveles sobre 223 (3 %): no se lee
#: como degradado —ella pidió plano— pero evita el color de relleno muerto y, al
#: estar definido sobre el PAR, al deslizar la luz sigue de largo.
LUZ_CENTRO, LUZ_CAIDA = 3.0, 7.0

#: Sombra de contacto: amplitud y radio. Calibrados contra el perfil medido de
#: las láminas aprobadas (punto 4).
SOMBRA_FUERZA, SOMBRA_RADIO = 0.16, 6.5


def mascara_pared(a: np.ndarray) -> np.ndarray:
    """Pared conectada al canto SUPERIOR del cuadro. Ver el punto 1."""
    lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    mx, mn = a.max(2), a.min(2)
    sat = (mx - mn) / np.maximum(mx, 1)
    # Generoso a propósito: la veta de la slide 2 llega a saturación 0,30 en el
    # canto superior derecho y con el umbral estrecho de la ronda 3 esa esquina
    # se quedaba sin máscara y habría sobrevivido como un parche de madera.
    pared = (lum > 140) & (lum < 243) & (sat < 0.32) & (a[..., 0] >= a[..., 2] - 4)
    etiquetas, _ = label(pared)
    arriba = set(np.unique(etiquetas[0, :]))
    arriba.discard(0)
    return np.isin(etiquetas, list(arriba))


def hoja_de_papel(W: int, H: int) -> tuple[np.ndarray, float, float]:
    """UNA hoja de papel beige de W×H. Receta de `between-st-s3-materiales.py`."""
    rng = np.random.default_rng(SEMILLA)

    # 1) grano fino: el poro del papel
    grano = rng.normal(0.0, 1.0, (H, W)).astype(np.float32)

    # 2) fibra: el mismo ruido ESTIRADO en horizontal. El desenfoque asimétrico
    #    es lo que convierte grano en fibra; con uno isótropo queda ruido borroso.
    f = Image.fromarray(((rng.normal(0, 1, (H, W)) * 40) + 128)
                        .clip(0, 255).astype(np.uint8))
    f = f.filter(ImageFilter.GaussianBlur(0.6))
    f = f.resize((W // 14, H), Image.BILINEAR).resize((W, H), Image.BILINEAR)
    fibra = (np.asarray(f).astype(np.float32) - 128) / 40.0

    # 3) manchado: baja frecuencia, para que la hoja no sea un plano de color
    m = Image.fromarray(((rng.normal(0, 1, (H // 40, W // 40)) * 40) + 128)
                        .clip(0, 255).astype(np.uint8))
    m = m.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(18))
    mancha = (np.asarray(m).astype(np.float32) - 128) / 40.0

    trama = grano * AMP_GRANO + fibra * AMP_FIBRA + mancha * AMP_MANCHA

    ys, xs = np.mgrid[0:H, 0:W]
    X = xs / (W - 1) * 2 - 1
    Y = ys / (H - 1) * 2 - 1
    luz = LUZ_CENTRO - LUZ_CAIDA * (0.55 * X ** 2 + 0.45 * Y ** 2)

    hoja = np.clip(TONO[None, None, :] + (trama + luz)[:, :, None], 0, 255)
    return hoja, float(trama.std()), float(luz.max() - luz.min())


def lum(x: np.ndarray) -> np.ndarray:
    return 0.2126 * x[..., 0] + 0.7152 * x[..., 1] + 0.0722 * x[..., 2]


def main() -> int:
    escenas = []
    for origen, _ in LAMINAS:
        p = DIR / origen
        if not p.is_file():
            sys.exit(f"✗ falta {p}\n"
                     f"  corre antes: python scripts/between-concurso-s3-fotos.py")
        escenas.append(np.asarray(Image.open(p).convert("RGB")).astype(np.float32))

    H, W, _ = escenas[0].shape
    hoja, desvio, vaiven = hoja_de_papel(W * 2, H)
    print(f"  hoja de papel  {W * 2}×{H}  base #{int(TONO[0]):02x}{int(TONO[1]):02x}"
          f"{int(TONO[2]):02x}  trama {desvio:.2f}/255  luz {vaiven:.1f} niveles"
          f"  semilla {SEMILLA}")

    salidas = []
    for i, (a, (origen, destino)) in enumerate(zip(escenas, LAMINAS)):
        m = mascara_pared(a)

        # sombra de contacto, desde la silueta del recorte
        sombra = 1 - SOMBRA_FUERZA * gaussian_filter((~m).astype(np.float32),
                                                     SOMBRA_RADIO)
        papel = hoja[:, i * W:(i + 1) * W] * sombra[:, :, None]

        # ⚠️ La máscara se dilata 1 px ANTES de difuminarla: su borde cae justo
        # donde empieza el contorno blanco (lum ≥ 243), así que sin dilatar queda
        # un anillo de 1 px de la pared vieja alrededor de todo el recorte.
        alfa = gaussian_filter(binary_dilation(m, iterations=1).astype(np.float32),
                               1.0)[:, :, None]
        out = np.clip(papel * alfa + a * (1 - alfa), 0, 255)
        salidas.append(out)

        # control: el perfil de la sombra que quedó
        base = lum(hoja[:, i * W:(i + 1) * W])
        d = distance_transform_edt(m)
        perfil = []
        for lo, hi in ((1, 6), (6, 12), (12, 25), (25, 10 ** 6)):
            s = m & (d >= lo) & (d < hi)
            perfil.append(f"{lo}–{hi if hi < 10 ** 6 else '∞'} px {(lum(out)[s] / base[s]).mean():.3f}")
        Image.fromarray(out.astype(np.uint8)).save(DIR / destino, quality=96,
                                                   subsampling=0)
        print(f"  ✓ {destino:26} pared {m.mean() * 100:4.1f} % del cuadro"
              f"   ·  sombra  {'  '.join(perfil)}")

    der = lum(salidas[0][:, -10:]).mean(1)
    izq = lum(salidas[1][:, :10]).mean(1)
    salto = float(np.abs(der - izq).mean())
    print(f"\n  salto en la costura: {salto:.2f} de luminancia — el umbral de la "
          f"cuenta es 1,5 → {'✓ invisible' if salto < 1.5 else '⚠️ se vería'}")
    print("    (es ruido de grano entre dos columnas vecinas de la MISMA hoja;\n"
          "     la continuidad no se corrigió, existe por construcción)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

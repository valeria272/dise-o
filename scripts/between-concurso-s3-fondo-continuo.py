#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hace que la PARED BEIGE sea continua entre las dos láminas del carrusel.

Pedido de Eli, 16-09-2026 (ronda 3):

    «Quiero que la textura beige del fondo hagan transición en ambas slides del
     carrusel del concurso.»

Es el mismo criterio que ella ya había dado para el carrusel del cumpleaños —«que
sea una continuidad con la slide dos, puede ser solamente el fondo mismo»— y que
allá se resolvió generando UN panorama y cortándolo en dos. **Acá no se puede
hacer así**: las dos escenas ya están generadas y aprobadas (la persona la aprobó
ella en esta misma sesión), y volver a generar un panorama significaría perder el
retrato aprobado. Así que la continuidad se construye sobre lo que ya hay.

## Cómo, y por qué esto NO es «pegotear»

No se mueve ni un píxel del sujeto. Lo único que cambia es el CAMPO DE BAJA
FRECUENCIA de la pared, y cambia por un campo que es continuo a lo largo de las
dos láminas puestas una al lado de la otra:

  1. **La máscara de fondo** sale por crecimiento desde el borde del cuadro sobre
     los píxeles «beige de pared» (luminancia 150–242, saturación baja, R≥G≥B).
     El borde blanco del recorte —que está en 243+— corta el crecimiento solo,
     así que el sujeto y su contorno quedan intactos. Después se erosiona 6 px
     para no tocar el filo.
  2. **El campo actual** de cada lámina es un polinomio de grado 3 ajustado por
     mínimos cuadrados sobre SUS píxeles de fondo.
     ⛔ Antes esto se estimaba con un desenfoque gaussiano ancho y NO servía: un
     gaussiano se sesga contra el canto del cuadro (la normalización por la
     máscara tira los valores hacia adentro), así que el campo salía mal justo
     en la costura y la corrección la empeoraba — medido, dejaba un salto de
     **18,7** de luminancia. Dos polinomios no tienen ese problema.
  3. **El campo nuevo** es un polinomio de grado 3 en x e y ajustado sobre los
     píxeles de fondo de las DOS láminas juntas (4500 × 2813). Un polinomio es
     continuo por construcción: al deslizar del slide 1 al 2 no hay escalón.
  4. Se aplica `delta = campo_nuevo − campo_actual` **sólo a los píxeles de
     fondo**. Como es una diferencia de baja frecuencia, el grano y la textura
     de la pared se conservan exactos: no se sustituye el fondo, se le corrige
     la iluminación.
  5. **La convergencia de costura**, que es lo que hace un panorama de verdad.
     Después del paso 4 el salto bajó de 18,7 a 3,3 pero no a cero: lo que queda
     es la diferencia de contenido REAL entre los dos cantos —viñeteo, sombreado
     local— y un polinomio de grado 3 no la describe. Se mide la diferencia fila
     a fila en la costura, se suaviza en vertical y se reparte **mitad a cada
     lado**, con una caída horizontal de 500 px hacia adentro. Es de muy baja
     frecuencia y no toca la textura.

Al final se imprime el **salto en la costura**: la diferencia media entre la
columna derecha de la lámina 1 y la izquierda de la lámina 2. El umbral que usa
la cuenta es 1,5 de luminancia (§ ronda «bajar la escena», S5).

Uso:  python scripts/between-concurso-s3-fondo-continuo.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.ndimage import binary_dilation, binary_erosion, gaussian_filter1d

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
DIR = RAIZ / "public/assets/hilton/between/concurso-s3"
LAMINAS = ["c1-portada.jpg", "c1-escritorio.jpg"]

#: Grado del polinomio. 3 basta para una pared: describe el degradado vertical,
#: la caída hacia los cantos y la asimetría de la luz lateral. Con grado 5 el
#: ajuste empieza a seguir manchas locales y deja de ser «continuo y tranquilo».
GRADO = 3


def mascara_fondo(a: np.ndarray) -> np.ndarray:
    """Pared beige conectada al borde del cuadro. Ver el punto 1 de la cabecera."""
    lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    mx, mn = a.max(2), a.min(2)
    sat = (mx - mn) / np.maximum(mx, 1)
    pared = (lum > 150) & (lum < 242) & (sat < 0.26) & (a[..., 0] >= a[..., 2])

    # crecimiento desde el borde, en una versión reducida (rápido y suficiente)
    ch = pared[::4, ::4]
    semilla = np.zeros_like(ch)
    semilla[0, :] = ch[0, :]
    semilla[-1, :] = ch[-1, :]
    semilla[:, 0] = ch[:, 0]
    semilla[:, -1] = ch[:, -1]
    prev = -1
    while semilla.sum() != prev:
        prev = semilla.sum()
        semilla = binary_dilation(semilla, iterations=12) & ch
    m = np.kron(semilla, np.ones((4, 4), bool))[: pared.shape[0], : pared.shape[1]]
    # 6 px de erosión para no tocar el filo del contorno blanco.
    # ⚠️ `border_value=1`: sin eso la erosión come también el CANTO del cuadro y
    # la máscara queda vacía justo en la costura, que es donde hay que medir.
    return binary_erosion(m, iterations=6, border_value=1)


def polinomio(a: np.ndarray, m: np.ndarray, x0: float = -1, x1: float = 1) -> np.ndarray:
    """Polinomio de grado `GRADO` en x,y ajustado sobre los píxeles de `m`.

    `x0`/`x1` son el tramo del eje horizontal que ocupa esta imagen dentro del
    par: así el ajuste de cada lámina y el del par comparten sistema de
    coordenadas y sus deltas son comparables.
    """
    H, W, _ = a.shape
    ys, xs = np.mgrid[0:H, 0:W]
    X = x0 + (xs / max(W - 1, 1)) * (x1 - x0)
    Y = (ys / max(H - 1, 1)) * 2 - 1
    bases = [X ** i * Y ** j for i in range(GRADO + 1) for j in range(GRADO + 1 - i)]
    A = np.stack([b[m] for b in bases], 1)
    salida = np.empty_like(a, dtype=np.float32)
    for c in range(3):
        coef, *_ = np.linalg.lstsq(A, a[..., c][m], rcond=None)
        salida[..., c] = sum(k * b for k, b in zip(coef, bases))
    return salida


def main() -> int:
    imgs, mascaras = [], []
    for n in LAMINAS:
        p = DIR / n
        if not p.is_file():
            sys.exit(f"✗ falta {p}\n  corre antes: python scripts/between-concurso-s3-fotos.py")
        a = np.asarray(Image.open(p).convert("RGB")).astype(np.float32)
        m = mascara_fondo(a)
        print(f"  {n:20} fondo detectado: {m.mean() * 100:5.1f} % del cuadro")
        imgs.append(a)
        mascaras.append(m)

    par = np.concatenate(imgs, 1)
    mpar = np.concatenate(mascaras, 1)
    nuevo = polinomio(par, mpar)                       # continuo sobre las dos
    # el campo de cada lámina, en el MISMO sistema de coordenadas del par
    actuales = [polinomio(imgs[0], mascaras[0], -1.0, 0.0),
                polinomio(imgs[1], mascaras[1], 0.0, 1.0)]
    W1 = imgs[0].shape[1]
    H = imgs[0].shape[0]
    corr = [nuevo[:, i * W1:(i + 1) * W1] - actuales[i] for i in range(2)]
    prev = [np.where(m[..., None], a + d, a)
            for a, m, d in zip(imgs, mascaras, corr)]

    # ── convergencia de costura (paso 5) ─────────────────────────────────────
    ANCHO_CAIDA = 500
    filas_ok = mascaras[0][:, -10:].all(1) & mascaras[1][:, :10].all(1)
    dif = prev[0][:, -10:].mean(1) - prev[1][:, :10].mean(1)      # H×3
    dif[~filas_ok] = 0
    dif = gaussian_filter1d(dif, 60, axis=0)                      # suave en vertical
    caida = np.clip(1 - np.arange(W1) / ANCHO_CAIDA, 0, 1)        # 1 en el canto
    peso0 = caida[::-1][None, :, None]                            # cae hacia la izquierda
    peso1 = caida[None, :, None]                                  # cae hacia la derecha
    corr[0] = corr[0] - 0.5 * dif[:, None, :] * peso0
    corr[1] = corr[1] + 0.5 * dif[:, None, :] * peso1

    salidas = []
    for i, (a, m, n) in enumerate(zip(imgs, mascaras, LAMINAS)):
        d = corr[i]
        out = np.where(m[..., None], a + d, a)
        salidas.append(np.clip(out, 0, 255))
        Image.fromarray(salidas[i].astype(np.uint8)).save(DIR / n, quality=95, subsampling=0)
        print(f"  ✓ {n}   corrección media {np.abs(d[m]).mean():.2f} · máxima {np.abs(d[m]).max():.2f}")

    def lum(x):
        return 0.2126 * x[..., 0] + 0.7152 * x[..., 1] + 0.0722 * x[..., 2]

    # sólo se compara donde LAS DOS tienen pared, fila a fila
    der = lum(salidas[0][:, -10:]).mean(1)
    izq = lum(salidas[1][:, :10]).mean(1)
    ok = mascaras[0][:, -10:].all(1) & mascaras[1][:, :10].all(1)
    salto = np.abs(der[ok] - izq[ok]).mean()
    print(f"  filas comparables en la costura: {ok.sum()} de {len(ok)}")
    print(f"\n  salto en la costura (45 % de arriba): {salto:.2f} de luminancia "
          f"— el umbral de la cuenta es 1,5 → {'✓ invisible' if salto < 1.5 else '⚠️ se vería'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

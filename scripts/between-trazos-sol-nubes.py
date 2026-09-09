#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dibuja el SOL y las NUBES de Between con la mano de Eli.

⭐ 09-09-2026. Eli, sobre la ST del 22-09: «la referencia de la ST tenía líneas
de dibujo como BW, debes añadir sol y nubes como ilustración, **guíate de mis
editables para dibujarlo correctamente**».

## Por qué este script existe, y por qué NO contradice el manual

El manual dice que los trazos de Between «no se dibujan a mano ni con IA: ya
existen». Y es cierto para los ocho que existen — pero **el sol y las nubes NO
están** en su editable. Se comprobó rindiendo la plancha completa
(`Flechas y trazados, globos BETWEEN.svg`, `1EZHJab1Rp8c8vuTHqAehF6tCk-CiRsXa`)
con la composición `BW-Plancha-Trazos`: lo que hay es confeti, un corazón, tres
flechas (bucle, grande, círculo), una flecha abajo y tres globos. Nada de sol ni
de nubes.

Así que «guíate de mis editables» no es «cópialos»: es **dibújalos con MI mano**.
Y su mano se puede medir, que es lo que hace este script.

## La mano de Eli, medida sobre su propio SVG

| qué | valor | de dónde |
|---|---|---|
| tinta | **`#fffaee`** | la clase `.st2` de su SVG (⚠️ NO es el beige `#fff9eb` del texto) |
| construcción | **contorno RELLENO, no trazo** | 1811 `<path>` y 178 `<polygon>` con `fill`, cero `stroke`: el pincel está expandido a contornos en Illustrator |
| sombra | `dx 4 · dy 4 · blur 3 · negro 25 %` | su filtro `drop-shadow-2` (el otro, `-1`, es 3/3/4/15 %) |
| grosor del trazo | **~4,5 px** sobre su lienzo de 2660 | transformada de distancia sobre el alfa de la plancha rendida |

Y el TAMAÑO sale de la referencia que mandó contenido, no de la plancha:
midiendo los doodles blancos de `Ref S4 Storie 2.jpg` normalizados a 1080 de
ancho, el sol mide 263 px y las nubes 192 y 342, con un grosor de **4–5,5 px**.
O sea que el trazo pesa ~2 % del ancho del dibujo. Estos PNG se generan a ~460 px
con 9 px de trazo para dar ese 2 % cuando se pintan a ~230 px en la historia.

## Cómo se imita un pincel expandido

Un `stroke` de ancho constante se ve de vector y se nota al lado de los suyos.
Acá cada trazo se construye como **polígono relleno**: se recorre la línea
central y se ofrecen los dos costados a una semi-anchura que
  1. **se afina en las puntas** (perfil `sin(πt)^0,35`: gordo casi todo el
     recorrido y afilado en los extremos, que es como muerde un pincel), y
  2. **respira** con un ruido suave de baja frecuencia (±18 %),
más un temblor igual de suave en la propia línea central, para que no se lea
compás. Se dibuja a 4× y se baja con LANCZOS, así el borde queda limpio.

Uso:  python scripts/between-trazos-sol-nubes.py
Salida: public/assets/hilton/between/recursos/{sol,nube,nube-chica}.png
"""
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
DEST = RAIZ / "public/assets/hilton/between/recursos"
DEST.mkdir(parents=True, exist_ok=True)

TINTA = (255, 250, 238)          # .st2 de su SVG
SOMBRA = (0, 0, 0, 64)           # negro 25 %
SOMBRA_DXY, SOMBRA_BLUR = 4, 3   # su filtro drop-shadow-2
SS = 4                           # supermuestreo

rng = np.random.default_rng(20260909)


def ruido_suave(n: int, amplitud: float, tramos: int = 5) -> np.ndarray:
    """Ruido de baja frecuencia en [-amplitud, +amplitud], suave en los bordes."""
    base = rng.uniform(-1.0, 1.0, tramos)
    x = np.linspace(0, tramos - 1, n)
    return np.interp(x, np.arange(tramos), base) * amplitud


def trazo(dib: ImageDraw.ImageDraw, pts, grosor: float, cerrado=False) -> None:
    """Pinta una línea central como CONTORNO RELLENO con punta afilada."""
    p = np.asarray(pts, dtype=float)
    if cerrado:
        p = np.vstack([p, p[:1]])
    # remuestreo uniforme para que el ruido no dependa del paso original
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    if d[-1] <= 0:
        return
    n = max(24, int(d[-1] / 2))
    t = np.linspace(0, d[-1], n)
    cx = np.interp(t, d, p[:, 0]) + ruido_suave(n, grosor * 0.20)
    cy = np.interp(t, d, p[:, 1]) + ruido_suave(n, grosor * 0.20)
    # normal unitaria
    dx = np.gradient(cx)
    dy = np.gradient(cy)
    ln = np.hypot(dx, dy)
    ln[ln == 0] = 1
    nx, ny = -dy / ln, dx / ln
    u = np.linspace(0, 1, n)
    # afilado en las puntas + respiración del pincel
    perfil = np.sin(np.pi * u) ** 0.35 if not cerrado else np.ones(n) * 0.92
    semi = (grosor / 2) * perfil * (1 + ruido_suave(n, 0.18, 7))
    izq = np.c_[cx + nx * semi, cy + ny * semi]
    der = np.c_[cx - nx * semi, cy - ny * semi][::-1]
    dib.polygon([tuple(v) for v in np.vstack([izq, der])], fill=TINTA + (255,))


def lienzo(w: int, h: int):
    im = Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def cerrar(im: Image.Image, w: int, h: int, nombre: str) -> None:
    """Baja de resolución y le pone la sombra de su filtro."""
    tinta = im.resize((w, h), Image.LANCZOS)
    sombra = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sombra.paste(SOMBRA, (0, 0), tinta.split()[3])
    sombra = sombra.filter(ImageFilter.GaussianBlur(SOMBRA_BLUR))
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.alpha_composite(sombra, (SOMBRA_DXY, SOMBRA_DXY))
    out.alpha_composite(tinta)
    out.save(DEST / nombre)
    print(f"  {nombre}  {out.size}  trazo {GROSOR/SS:.1f} px")


# ── EL SOL ───────────────────────────────────────────────────────────────────
# Círculo ABIERTO (el trazo no cierra: se cruza un poco, como cuando se dibuja
# de un tirón) + ocho rayos rectos, cada uno su propio trazo con su afilado.
W = H = 460
GROSOR = 9 * SS
im, dib = lienzo(W, H)
cx = cy = W * SS / 2
r = W * SS * 0.215
a0 = math.radians(-100)
arco = [(cx + r * math.cos(a0 + 2 * math.pi * s * 1.06),
         cy + r * math.sin(a0 + 2 * math.pi * s * 1.06)) for s in np.linspace(0, 1, 90)]
trazo(dib, arco, GROSOR)
for k in range(8):
    a = a0 + k * 2 * math.pi / 8 + 0.12
    r1, r2 = r * 1.42, r * 1.42 + W * SS * (0.105 if k % 2 == 0 else 0.082)
    trazo(dib, [(cx + r1 * math.cos(a), cy + r1 * math.sin(a)),
                (cx + r2 * math.cos(a), cy + r2 * math.sin(a))], GROSOR * 0.92)
cerrar(im, W, H, "sol.png")


# ── LAS NUBES ────────────────────────────────────────────────────────────────
def nube(w: int, h: int, bollos, nombre: str, grosor_px: float) -> None:
    """Nube de un solo trazo: lomos redondos arriba y base casi recta.

    ⛔ El primer intento dibujaba cada lomo como un medio círculo suelto, de π a
    0, y los lomos se juntaban ABAJO: quedaban muescas en V entre uno y otro y la
    silueta se leía como una fila de arcos, no como una nube.

    Lo correcto es la **envolvente superior** de los círculos: para cada x, el
    contorno es el más alto de todos los lomos que pasan por ahí. Así los lomos
    se sueldan por el flanco de arriba, que es donde se sueldan en una nube.
    """
    global GROSOR
    GROSOR = grosor_px * SS
    im, dib = lienzo(w, h)
    W2, H2 = w * SS, h * SS
    base_y = H2 * 0.74
    x0, x1 = W2 * 0.10, W2 * 0.90
    xs = np.linspace(x0, x1, 220)
    alto = np.zeros_like(xs)
    for cxf, rf in bollos:
        bx, br = W2 * cxf, W2 * rf
        dentro = np.abs(xs - bx) < br
        h_i = np.zeros_like(xs)
        h_i[dentro] = np.sqrt(br ** 2 - (xs[dentro] - bx) ** 2) * 1.06
        alto = np.maximum(alto, h_i)
    pts = list(zip(xs, base_y - alto))
    trazo(dib, pts, GROSOR)
    # la base: un trazo suelto y un poco más corto, como la cierra a mano
    trazo(dib, [(W2 * 0.155, base_y + GROSOR * 0.10),
                (W2 * 0.52, base_y + GROSOR * 0.30),
                (W2 * 0.86, base_y + GROSOR * 0.05)], GROSOR * 0.95)
    cerrar(im, w, h, nombre)


nube(520, 400, [(0.30, 0.170), (0.51, 0.235), (0.72, 0.175)], "nube.png", 9)
nube(400, 320, [(0.34, 0.195), (0.63, 0.240)], "nube-chica.png", 8.5)

print("\nMÍRALAS al lado de las suyas antes de usarlas:")
print("  python scripts/hoja-contacto.py public/assets/hilton/between/recursos out/_verif/trazos.png")

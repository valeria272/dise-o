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

# ⭐ RONDA 6 (09-09-2026). Eli: «recuerda usar el color beige de BW para las
# ilustraciones». Se venía usando `#fffaee`, que es el hex EXACTO de la clase
# `.st2` de su editable — o sea que estaba medido, no inventado. Pero el color de
# la marca es `#FFF9EB` (`BETWEEN.colores.beige`), el mismo del texto, y manda
# ella: la ilustración y la tipografía tienen que ser la misma tinta.
# ⚠️ Queda una diferencia de 2 puntos en verde y 3 en azul contra los OCHO trazos
# que salieron recortados de su plancha (globo, confeti, corazón y las flechas),
# que conservan su `#fffaee` porque son su obra y no se re-tiñen.
TINTA = (255, 249, 235)          # BETWEEN.colores.beige
SOMBRA = (0, 0, 0, 64)           # negro 25 %
SOMBRA_DXY, SOMBRA_BLUR = 4, 3   # su filtro drop-shadow-2
SS = 4                           # supermuestreo

rng = np.random.default_rng(20260909)


def ruido_suave(n: int, amplitud: float, tramos: int = 5) -> np.ndarray:
    """Ruido de baja frecuencia en [-amplitud, +amplitud], suave en los bordes."""
    base = rng.uniform(-1.0, 1.0, tramos)
    x = np.linspace(0, tramos - 1, n)
    return np.interp(x, np.arange(tramos), base) * amplitud


def trazo(dib: ImageDraw.ImageDraw, pts, grosor: float, cerrado=False,
          pasadas: int = 1, separacion: float = 0.0) -> None:
    """Pinta una línea central como CONTORNO RELLENO con punta afilada.

    ⭐ `pasadas=2` dibuja la MISMA línea dos veces. Como el temblor y la
    respiración del pincel se sortean en cada pasada, las dos salen parecidas y
    no iguales — que es exactamente lo que hace una mano cuando repasa un
    contorno. Es el rasgo que Eli marcó en su boceto del 09-09: sus nubes tienen
    doble contorno, no una línea sola. `separacion` corre la segunda pasada por
    la normal, en múltiplos del grosor.
    """
    for k in range(pasadas):
        # ⚠️ La pasada repasada va MÁS FINA: cuando la mano vuelve sobre el
        # trazo aprieta menos. Y `separacion` tiene que ser MAYOR que 1, o las
        # dos pasadas se funden en un solo trazo gordo — medido: con 0,85 el
        # `canto/tinta` caía a 0,14 contra el 0,28–0,34 de los trazos de Eli,
        # que es la firma de un trazo grueso y liso, no de dos líneas.
        _una_pasada(dib, pts, grosor * (1.0 if k == 0 else 0.78), cerrado,
                    separacion * grosor * k)


def _octavas(n: int, octavas) -> np.ndarray:
    """Ruido de varias octavas sumadas: la textura del pincel no es una sola
    escala. La baja hace que el trazo engorde y adelgace a lo largo, y las altas
    son las que muerden el borde."""
    out = np.zeros(n)
    for tramos, amplitud in octavas:
        out = out + ruido_suave(n, amplitud, tramos)
    return out


def _una_pasada(dib: ImageDraw.ImageDraw, pts, grosor: float, cerrado: bool,
                corrimiento: float) -> None:
    """Un trazo de pincel: contorno relleno con el BORDE ASERRADO.

    ⭐ RONDA 5 (09-09-2026). Eli: «necesito esas ilustraciones más irregulares y
    no tan bien hechas, que sea orgánica pero bien dibujada, como textura de
    pincel». Tenía razón y el defecto era medible: la versión anterior ofrecía
    los DOS costados con la MISMA semi-anchura y con una sola octava de ruido
    suave (5–7 tramos), así que el trazo salía como una cinta lisa con un vaivén
    — regular, justo lo que ella no quiere.

    Mirando sus trazos originales al 400 % (`globo.png`, `confeti.png`) la
    textura real tiene tres rasgos, y son los tres que faltaban:

      1. **el borde va aserrado a ALTA frecuencia** — muescas de 1 a 3 px que se
         repiten cada pocos píxeles, no un vaivén largo;
      2. **los dos costados son INDEPENDIENTES** — un lado abulta donde el otro
         no, así que el eje del trazo se mueve solo;
      3. **el ancho varía mucho** a lo largo del recorrido, bastante más que el
         ±18 % que tenía.

    Así que la semi-anchura se sortea por separado para cada costado y suma tres
    octavas: una larga que engorda y adelgaza el trazo, y dos cortas —**en píxeles
    absolutos**— que son las que muerden el canto.

    ⛔ Y se probó agregarle «claros» del pincel (motas transparentes dentro del
    trazo). Se descartó: salían círculos perfectos y del mismo porte, o sea que
    se leían como lunares y no como un salto de pincel. El rasgo que de verdad
    da la textura es el CANTO, no los huecos.
    """
    p = np.asarray(pts, dtype=float)
    if cerrado:
        p = np.vstack([p, p[:1]])
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    if d[-1] <= 0:
        return
    # paso de 1,5 px a 4×: sin muestreo denso la octava alta no alcanza a morder
    n = max(40, int(d[-1] / 1.5))
    t = np.linspace(0, d[-1], n)
    cx = np.interp(t, d, p[:, 0]) + ruido_suave(n, grosor * 0.18)
    cy = np.interp(t, d, p[:, 1]) + ruido_suave(n, grosor * 0.18)
    dx, dy = np.gradient(cx), np.gradient(cy)
    ln = np.hypot(dx, dy)
    ln[ln == 0] = 1
    nx, ny = -dy / ln, dx / ln
    if corrimiento:
        cx, cy = cx + nx * corrimiento, cy + ny * corrimiento
    u = np.linspace(0, 1, n)
    # la punta se afina, pero MENOS que antes: sus trazos acaban romos y
    # deshilachados, no en aguja
    perfil = np.sin(np.pi * u) ** 0.22 if not cerrado else np.full(n, 0.94)
    largo = max(6, int(d[-1] / max(grosor, 1)))
    # ⭐ LA MUESCA VA EN PÍXELES ABSOLUTOS, no en porcentaje del grosor.
    # Fue el error de la primera pasada: una octava alta de «±10 % de la
    # semi-anchura» son 2 px a 4×, o sea MEDIO píxel en la imagen final — se la
    # come el remuestreo y el trazo vuelve a salir liso. Medidas sobre sus
    # propios trazos, las muescas son de 1 a 3 px del PNG, así que a 4× hay que
    # pedir 6–10 px y da igual lo gordo que sea el trazo.
    MUESCA_MEDIA, MUESCA_FINA = 2.1 * SS, 1.2 * SS
    def _canto() -> np.ndarray:
        return (
            # octava larga: el trazo engorda y adelgaza a lo largo (relativa)
            (grosor / 2) * _octavas(n, ((max(5, largo // 3), 0.22),))
            # octavas cortas: las que muerden el canto (absolutas)
            + ruido_suave(n, MUESCA_MEDIA, max(14, largo * 2))
            + ruido_suave(n, MUESCA_FINA, max(40, largo * 8))
        )
    base = (grosor / 2) * perfil
    semi_l = np.clip(base + _canto(), grosor * 0.10, grosor)
    semi_r = np.clip(base + _canto(), grosor * 0.10, grosor)
    izq = np.c_[cx + nx * semi_l, cy + ny * semi_l]
    der = np.c_[cx - nx * semi_r, cy - ny * semi_r][::-1]
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
# ⭐ el círculo NO es un círculo: el radio respira, así que sale un óvalo de mano
_ts = np.linspace(0, 1, 120)
_rr = r * (1 + ruido_suave(len(_ts), 0.055, 4))
arco = [(cx + rr * math.cos(a0 + 2 * math.pi * t * 1.06),
         cy + rr * math.sin(a0 + 2 * math.pi * t * 1.06)) for t, rr in zip(_ts, _rr)]
trazo(dib, arco, GROSOR)
for k in range(8):
    a = a0 + k * 2 * math.pi / 8 + 0.12 + rng.uniform(-0.10, 0.10)
    r1 = r * rng.uniform(1.34, 1.50)
    r2 = r1 + W * SS * (0.105 if k % 2 == 0 else 0.082) * rng.uniform(0.82, 1.18)
    trazo(dib, [(cx + r1 * math.cos(a), cy + r1 * math.sin(a)),
                (cx + r2 * math.cos(a), cy + r2 * math.sin(a))], GROSOR * rng.uniform(0.82, 1.0))
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
    # ⭐ los lomos NO son iguales: cada uno corre su centro y su radio, y el
    #    perfil entero respira. Una nube de tres semicírculos exactos se lee
    #    dibujada con compás — que es justo lo que Eli marcó.
    for cxf, rf in bollos:
        bx = W2 * cxf * rng.uniform(0.975, 1.025)
        br = W2 * rf * rng.uniform(0.88, 1.12)
        dentro = np.abs(xs - bx) < br
        h_i = np.zeros_like(xs)
        h_i[dentro] = np.sqrt(br ** 2 - (xs[dentro] - bx) ** 2) * rng.uniform(1.0, 1.14)
        alto = np.maximum(alto, h_i)
    alto = alto * (1 + ruido_suave(len(xs), 0.045, 6))
    pts = list(zip(xs, base_y - alto + ruido_suave(len(xs), GROSOR * 0.22, 5)))
    trazo(dib, pts, GROSOR)
    # la base: un trazo suelto y un poco más corto, como la cierra a mano
    trazo(dib, [(W2 * 0.155, base_y + GROSOR * 0.10),
                (W2 * 0.52, base_y + GROSOR * 0.30),
                (W2 * 0.86, base_y + GROSOR * 0.05)], GROSOR * 0.95)
    cerrar(im, w, h, nombre)


nube(520, 400, [(0.30, 0.170), (0.51, 0.235), (0.72, 0.175)], "nube.png", 9)
nube(400, 320, [(0.34, 0.195), (0.63, 0.240)], "nube-chica.png", 8.5)


# ══════════════════════════════════════════════════════════════════════════════
# ⭐⭐ SEGUNDA TANDA — el boceto que mandó Eli el 09-09
# ══════════════════════════════════════════════════════════════════════════════
# Su captura pide MUCHA más presencia que la primera tanda: dibujos grandes que
# sangran por los cuatro bordes, **doble contorno** (la mano repasa la línea) y
# unas rayitas de acento sueltas. Los tres rasgos se leen en el boceto y los tres
# se pueden construir; lo que NO cambia es la mano medida sobre su editable —
# tinta `#fffaee`, su sombra y el grosor al 2 % del ancho del dibujo.

# ── EL SOL GRANDE ────────────────────────────────────────────────────────────
# Mismo dibujo que el `sol`, pero grande y con el círculo REPASADO. Va pensado
# para poner el centro casi fuera del cuadro: lo que se ve entonces es un arco
# enorme en la esquina con sus rayos, que es justo lo que hace su boceto.
W = H = 700
GROSOR = 11 * SS
im, dib = lienzo(W, H)
cx = cy = W * SS / 2
r = W * SS * 0.225
a0 = math.radians(-96)
_ts = np.linspace(0, 1, 150)
_rr = r * (1 + ruido_suave(len(_ts), 0.06, 4))
arco = [(cx + rr * math.cos(a0 + 2 * math.pi * t * 1.04),
         cy + rr * math.sin(a0 + 2 * math.pi * t * 1.04)) for t, rr in zip(_ts, _rr)]
trazo(dib, arco, GROSOR, pasadas=2, separacion=1.55)
for k in range(9):
    a = a0 + k * 2 * math.pi / 9 + 0.10 + rng.uniform(-0.11, 0.11)
    r1 = r * rng.uniform(1.32, 1.48)
    r2 = r1 + W * SS * (0.115 if k % 2 == 0 else 0.085) * rng.uniform(0.80, 1.22)
    trazo(dib, [(cx + r1 * math.cos(a), cy + r1 * math.sin(a)),
                (cx + r2 * math.cos(a), cy + r2 * math.sin(a))], GROSOR * rng.uniform(0.80, 1.0))
cerrar(im, W, H, "sol-grande.png")


# ── NUBES DE DOBLE CONTORNO ──────────────────────────────────────────────────
def nube_doble(w, h, bollos, nombre, grosor_px):
    """Igual que `nube`, pero con el contorno REPASADO (dos pasadas)."""
    global GROSOR
    GROSOR = grosor_px * SS
    im, dib = lienzo(w, h)
    W2, H2 = w * SS, h * SS
    base_y = H2 * 0.76
    xs = np.linspace(W2 * 0.08, W2 * 0.92, 240)
    alto = np.zeros_like(xs)
    for cxf, rf in bollos:
        bx = W2 * cxf * rng.uniform(0.975, 1.025)
        br = W2 * rf * rng.uniform(0.88, 1.12)
        dentro = np.abs(xs - bx) < br
        h_i = np.zeros_like(xs)
        h_i[dentro] = np.sqrt(br ** 2 - (xs[dentro] - bx) ** 2) * rng.uniform(1.02, 1.16)
        alto = np.maximum(alto, h_i)
    alto = alto * (1 + ruido_suave(len(xs), 0.05, 6))
    trazo(dib, list(zip(xs, base_y - alto + ruido_suave(len(xs), GROSOR * 0.20, 5))),
          GROSOR, pasadas=2, separacion=1.85)
    trazo(dib, [(W2 * 0.14, base_y + GROSOR * 0.10),
                (W2 * 0.52, base_y + GROSOR * 0.32),
                (W2 * 0.88, base_y + GROSOR * 0.04)], GROSOR * 0.95,
          pasadas=2, separacion=1.70)
    cerrar(im, w, h, nombre)


nube_doble(640, 440, [(0.28, 0.150), (0.50, 0.215), (0.73, 0.160)], "nube-doble.png", 11)
nube_doble(470, 340, [(0.33, 0.180), (0.62, 0.225)], "nube-doble-chica.png", 10)


# ── LAS RAYITAS DE ACENTO ────────────────────────────────────────────────────
# En su boceto hay grupos de dos o tres trazos cortos y curvos, sueltos, que
# rellenan el aire sin dibujar nada concreto. Son el equivalente del confeti que
# ya existe en su plancha, pero más discretos.
GROSOR = 10 * SS
W, H = 260, 220
im, dib = lienzo(W, H)
for i, (x0, y0, largo, curva) in enumerate((
        (0.16, 0.16, 0.52, -0.16),
        (0.30, 0.48, 0.44, -0.13),
        (0.20, 0.78, 0.34, -0.10))):
    px = [(W * SS * (x0 + largo * t),
           H * SS * (y0 + curva * math.sin(math.pi * t)))
          for t in np.linspace(0, 1, 26)]
    trazo(dib, px, GROSOR * (1.0 - 0.12 * i))
cerrar(im, W, H, "rayitas.png")

print("\nMÍRALAS al lado de las suyas antes de usarlas.")

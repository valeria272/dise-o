#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara la foto del ESTÁTICO HILTON HONORS (FEED col K · 23-09 · 18:00).

Encargo de Eli, 15-09-2026: «Trabajaremos diseñando el post estático de la
grilla de Doubletree by Hilton […] la S4, debes tomar de referencia [la carpeta
REFERENCIAS S4 DT]».

## Qué pide el brief, LITERAL (FEED col K, estado `OK PARA DISEÑO`)

    SECCIÓN 1 – FONDO Y TÍTULO (GANCHO)
    Visual: Fotografía real de alta calidad ocupando todo el fondo (idealmente
    una perspectiva cenital o angular elegante de las instalaciones, piscina,
    lobby o habitación de DoubleTree by Hilton Santiago Vitacura).

⛔ Dos cosas que el brief pide y este banco NO tiene, y por eso no se inventan:

  · **cenital** — no hay ninguna toma aérea del hotel en las 48 fotos de la
    sesión profesional ni en las 96 de las carpetas de muestra. El brief ofrece
    la alternativa en la misma frase («o angular elegante»), así que se toma esa.
  · **piscina** — el complejo no tiene piscina fotografiada en ningún banco. El
    brief ofrece tres alternativas más («instalaciones, lobby o habitación»).

⛔ Y no se genera nada con IA: la foto existe (`no-generar-producto-que-existe`).

## De dónde sale la foto, y por qué ésta

`HDT_36.jpg` de la sesión profesional (`JPG DT,QB,BW,HABITACIÓNES`,
`1XhKQS8XlQTLCSk_59ZVjbs8tqnAroz7n`) — **el lobby lounge**, 6719×4479, en alta.
Es «lobby» tal cual lo nombra el brief y su perspectiva en fuga es lo más
cercano a la «angular elegante» que pide.

⭐ Cómo se encontró: la hoja de contacto con las MINIATURAS de Drive
(`drive.google.com/thumbnail?id=…&sz=w600`), que pesan ~30 KB, en vez de bajar 48
archivos de 20-37 MB a ciegas. Es la misma técnica con la que apareció el frontis
el 09-09.

## El encuadre: se recorta en LOS DOS EJES, y por qué

La foto es 3:2 (1,5001) y el post es 4:5 (0,8). **No se estira nada** — se recorta.

**Horizontal, fracción 0,30.** Se midió, para cada offset, la luminancia relativa
por tercios en las cuatro bandas donde va a caer algo, con el velo azul ya
aplicado (`la-tinta-la-manda-el-fondo`). Los cuatro offsets pasaban con holgura,
así que el contraste NO decidía; decidió la composición: 0,30 deja la fuga del
pasillo centrada y el muro verde completo detrás de la caja, sin cortar los
sillones de la izquierda.

⭐ **Vertical: se corta el 16 % de ARRIBA, y ése fue el arreglo de la ronda 1.**
La primera pasada tomó el alto completo, y el resultado tenía razón en los
números y estaba mal a la vista: la mitad superior era **cielorraso vacío** —el
soffit de madera cruzando el borde de arriba como si fuera un error de recorte—
y el muro verde, que es lo que hace de fondo a la caja, quedaba aplastado en una
franja de la mitad. Cortando 16 % desde arriba el muro verde entra completo, la
fuga del piso de madera llena el tercio inferior (que es justo donde va la caja
de cristal) y al cielorraso le queda lo necesario para el logotipo.

⛔ No se corta más: a 22 % el cielorraso se acaba y **el logotipo cae sobre el
cuadro rojo** de la pared, que es el elemento más saturado de la escena.

El recorte queda en 3009×3762 — sigue siendo más grande que el máster de
2250×2813, así que se REDUCE. Nunca se amplía.

## ⭐ LA TINTA DEL LOGOTIPO: AZUL, Y ESTÁ MEDIDO

El logotipo cae en y 111-241 @1080, o sea sobre el **cielorraso blanco** del
lobby, donde el velo todavía va en α≈0,14. Medido ahí:

    logo BLANCO  →  3,29:1   ⛔ no llega a 4,5
    logo AZUL    →  4,84:1   ✅

Y las otras tres bandas, con el mismo método (todas en blanco):

    titular  6,13:1   ·   caja  7,54:1   ·   pie  9,89:1

Es exactamente el caso de la §B.4 del manual: «va en azul DoubleTree cuando el
fondo es demasiado blanco y el logo se pierde». El mismo criterio de la historia
del Día del Turismo, por la misma razón medida.

## El realce

La toma ya viene reveladada y pareja (es sesión profesional con luz de tungsteno
y ventanal al fondo). Se le da **1,06** de contraste, apenas para que el velo
azul no la aplane. Medido el recorte de tonos sobre el máster final, se imprime
al correr.

Uso:
    python scripts/dt-ft-honors-foto.py            # la elegida (suite)
    python scripts/dt-ft-honors-foto.py king       # una alternativa
    python scripts/dt-ft-honors-foto.py lobby      # la foto de las rondas 1-6
"""
import argparse
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

import numpy as np
from PIL import Image, ImageEnhance

RAIZ = Path(__file__).resolve().parent.parent

# ══════════════════════════════════════════════════════════════════════════
# ⭐⭐ RONDA 7 (16-09) — LA FOTO PASA DE LOBBY A HABITACIÓN
# ══════════════════════════════════════════════════════════════════════════
# Grilla FEED col K, comentario SIN TACHAR: **«Cambiemos foto por habitación de
# categoría superior y ok!»**. Es el único pendiente de la celda; los otros dos
# comentarios están tachados.
#
# ⚠️ Es un cambio de FOTO, no de diagramación: el titular justificado de la
# ronda 5, el panel apretado de la ronda 6 y la regla del pie quedan intactos.
#
# «Categoría superior» en este hotel son Corner, Junior Suite y Suite — lo que
# las separa de la estándar es el ESTAR: sofá, escritorio y ventanal. Por eso
# las tres candidatas salen de la sesión profesional y no del banco de muestra,
# y ninguna es generada (`no-generar-producto-que-existe`).
#
# Cada variante trae su encuadre YA MEDIDO: `fx` corre la ventana 4:5 dentro de
# la foto apaisada, `alto` descarta cielorraso de arriba y `fy` ancla el recorte.
VARIANTES = {
    # ⭐ LA ELEGIDA — la SUITE. En una sola toma se ven los DOS ambientes: el
    # estar con escritorio y ventanal en primer plano, y la habitación al otro
    # lado del vano. Eso es exactamente lo que separa una categoría superior de
    # una estándar en este hotel, y la única candidata donde se ve entero.
    #
    # `fx 0.80` no es gusto. La foto es 3:2 y el post 4:5, así que la ventana de
    # recorte se lleva **el 53 % del ancho** y hay que elegir qué entra:
    #
    #   0,30-0,45  sólo el escritorio y el ventanal → lee «oficina», no habitación
    #   0,60       entra el cuadro y asoma la cama por el canto — se pierde
    #   **0,80**   el cuadro y el escritorio a la izquierda, **la cama entera a la
    #              derecha**: se lee habitación, y de las grandes
    #   1,00       sólo la cama, y se va el estar que es lo que la hace superior
    "suite": {
        "origen": "raw/hilton/dt/sesion-real/alta/HDT_68-hab.jpg",
        "destino": "public/assets/hilton/dt/ft-honors-habitacion.jpg",
        "fx": 0.80, "alto": 1.00, "fy": 0.50,
    },
    # Alternativa — la misma suite corrida al estar. Se ve mejor el escritorio con
    # el desayuno servido y el ventanal, y la cama queda asomada en el canto.
    # Lista por si Eli la prefiere: `python scripts/dt-ft-honors-foto.py estar68`.
    "estar68": {
        "origen": "raw/hilton/dt/sesion-real/alta/HDT_68-hab.jpg",
        "destino": "public/assets/hilton/dt/_pruebas/ft-honors-estar68.jpg",
        "fx": 0.60, "alto": 1.00, "fy": 0.50,
    },
    # ⛔ DESCARTADAS, y por qué — MEDIDO con el velo real de la composición
    # (convexo, pie 0,50), no con el de historia. La diagramación de esta pieza
    # pone tinta BLANCA sobre el tercio medio de la foto, donde el velo todavía
    # va en α≈0,20: una habitación clara se come el titular.
    #
    #   HDT_66 (cama king + visillo)  titular **2,1:1**  ⛔ ni con reencuadre
    #   HDT_65 (cama + bienvenida)    titular **2,8:1**  ⛔ y lee «Escapada Romántica»
    #   HDT_67 (estar con sofá)       titular **3,3:1** pero logo DT 2,1:1  ⛔
    #   HDT_57 / HDT_59               pasan, pero son **dos camas**: eso es la
    #                                 categoría estándar, justo lo contrario
    #
    # Se dejan declaradas para que la próxima ronda no las vuelva a probar.
    "king": {
        "origen": "raw/hilton/dt/sesion-real/alta/HDT_66-hab.jpg",
        "destino": "public/assets/hilton/dt/_pruebas/ft-honors-king.jpg",
        "fx": 0.65, "alto": 1.00, "fy": 0.50,
    },
    "bienvenida": {
        "origen": "raw/hilton/dt/sesion-real/alta/HDT_65-hab.jpg",
        "destino": "public/assets/hilton/dt/_pruebas/ft-honors-bienvenida.jpg",
        "fx": 0.45, "alto": 1.00, "fy": 0.50,
    },
    "estar": {
        "origen": "raw/hilton/dt/sesion-real/alta/HDT_67-hab-vista.jpg",
        "destino": "public/assets/hilton/dt/_pruebas/ft-honors-estar.jpg",
        "fx": 0.45, "alto": 1.00, "fy": 0.50,
    },
    # El lobby de las rondas 1-6, que el cliente mandó cambiar. Se deja para poder
    # reconstruir la entrega vieja byte a byte.
    "lobby": {
        "origen": "raw/hilton/dt/sesion-real/alta/HDT_36-lobby.jpg",
        "destino": "public/assets/hilton/dt/ft-honors-lobby.jpg",
        "fx": 0.30, "alto": 0.84, "fy": 1.00,
    },
}

# El máster del FEED 4:5 es 2250×2813 — el tamaño de las tres piezas aprobadas
# (`C1 FT N1`, `C1 FT N2`, `DT FT S3`) y el de la plantilla `logo-post.png`.
ANCHO_MASTER, ALTO_MASTER = 2250, 2813
BYTES_MINIMOS = 1_000_000
CONTRASTE = 1.06

# Las bandas donde va a caer algo, @1080 sobre un lienzo de 1350.
BANDAS = {
    "logotipo": (111, 241),
    "titular": (592, 777),
    "caja": (842, 1148),
    "honors": (1150, 1230),
    "pie": (1240, 1320),
}
# ⛔⛔ CORREGIDO EN LA RONDA 7 — ESTA RAMPA NO ERA LA DE ESTA PIEZA.
# Hasta acá el script medía con la rampa **cóncava** de la historia del Día del
# Turismo (pie 0,58), y la pieza usa desde la ronda 2 la rampa **convexa** del
# feed (`VELO` en `DtFtHonors.tsx`, pie 0,50), que casi no pesa hasta pasada la
# mitad. Con la foto oscura del lobby la diferencia no se notaba; al cambiar a
# una habitación clara, la rampa vieja daba el titular en 6,3:1 cuando de verdad
# estaba en 2,8:1 — o sea aprobaba piezas que `dt-qa.py` rechaza.
#
# Ahora mide con la rampa de verdad. **La compuerta sigue siendo `dt-qa.py`**;
# esto es para elegir la foto sin tener que rendir.
RAMPA = [(0, 0), (10, .01), (20, .03), (30, .08), (40, .15), (50, .23),
         (60, .31), (70, .38), (80, .44), (90, .48), (100, .50)]


def relativa(c) -> np.ndarray:
    c = np.asarray(c, dtype=float) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contraste(y1: float, y2: float) -> float:
    hi, lo = max(y1, y2), min(y1, y2)
    return (hi + 0.05) / (lo + 0.05)


def alfa(pct: float) -> float:
    return float(np.interp(pct, [p[0] for p in RAMPA], [p[1] for p in RAMPA]))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("variante", nargs="?", default="suite", choices=sorted(VARIANTES))
    a = ap.parse_args()
    v = VARIANTES[a.variante]
    ORIGEN = RAIZ / v["origen"]
    DESTINO = RAIZ / v["destino"]
    FRACCION_X, FRACCION_ALTO, FRACCION_Y = v["fx"], v["alto"], v["fy"]
    print(f"variante      {a.variante}  ←  {v['origen'].rsplit('/', 1)[-1]}")

    if not ORIGEN.exists():
        print(f"⛔ No está la foto original: {ORIGEN}")
        print("   Bájala con:")
        print("   curl -sL 'https://drive.usercontent.google.com/download"
              "?id=19NnC9XyEo0Cyn5exMNlhigiR92gmzR2q&export=download&confirm=t' \\")
        print(f"        -o '{ORIGEN}'")
        return 1

    peso = ORIGEN.stat().st_size
    if peso < BYTES_MINIMOS:
        print(f"⛔ La foto pesa {peso} B. Eso es una página de login de Google "
              "guardada con nombre de foto, no la foto. Abortando.")
        return 1

    im = Image.open(ORIGEN).convert("RGB")
    W, H = im.size
    print(f"original      {W}×{H}  ratio {W / H:.4f}  {peso // 1024} KB")

    alto_recorte = int(round(H * FRACCION_ALTO))
    ancho_recorte = int(round(alto_recorte * ANCHO_MASTER / ALTO_MASTER))
    offset_x = int(round((W - ancho_recorte) * FRACCION_X))
    offset_y = int(round((H - alto_recorte) * FRACCION_Y))
    caja = (offset_x, offset_y, offset_x + ancho_recorte, offset_y + alto_recorte)
    rec = im.crop(caja)
    print(f"recorte 4:5   {rec.width}×{rec.height}  offset x={offset_x} "
          f"(fracción {FRACCION_X}) · y={offset_y} (corta {(1 - FRACCION_ALTO) * 100:.0f} % "
          "de cielorraso arriba)")

    # Se REDUCE a máster. Nunca se amplía: ampliar es entregar una foto blanda.
    if rec.width < ANCHO_MASTER:
        print(f"⛔ El recorte es más chico que el máster ({rec.width} < {ANCHO_MASTER}).")
        return 1

    final = rec.resize((ANCHO_MASTER, ALTO_MASTER), Image.LANCZOS)
    final = ImageEnhance.Contrast(final).enhance(CONTRASTE)

    b = np.asarray(final).astype(int)
    print(f"realce        contraste ×{CONTRASTE}  →  sombras pegadas "
          f"{(b.max(axis=2) <= 2).mean() * 100:.2f} %  luces quemadas "
          f"{(b.min(axis=2) >= 253).mean() * 100:.2f} %")

    # ── la medición que decide la tinta, sobre el máster ya revelado
    print("\n   banda        α velo   Y peor tercio   blanco    azul DT")
    k = ALTO_MASTER / 1350.0
    for nombre, (y0, y1) in BANDAS.items():
        reg = b[int(y0 * k):int(y1 * k)]
        al = alfa((y0 + y1) / 2 / 1350 * 100)
        vel = reg * (1 - al) + np.array([9, 25, 78]) * al
        w = max(1, reg.shape[0] // 3)
        peor = max(relativa(vel[i * w:(i + 1) * w]).mean() for i in range(3))
        cb = contraste(peor, relativa(np.array([250, 250, 250])))
        ca = contraste(peor, relativa(np.array([9, 25, 78])))
        print(f"   {nombre:12} {al:5.2f}    {peor:.3f}          "
              f"{cb:5.2f}:1   {ca:5.2f}:1")

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    final.save(DESTINO, quality=95, subsampling=0)
    print(f"\n→ {DESTINO.relative_to(RAIZ)}  {final.width}×{final.height}  "
          f"{DESTINO.stat().st_size // 1024} KB")
    print(f"   reducción {rec.width}→{ANCHO_MASTER} (×{ANCHO_MASTER / rec.width:.3f}) "
          "— sin ampliar, sin estirar")
    return 0


if __name__ == "__main__":
    sys.exit(main())

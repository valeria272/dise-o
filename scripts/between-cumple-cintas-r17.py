#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAFÉ DE CUMPLEAÑOS (FEED 03-sep, S1) — ronda 17: la cinta dorada, BRILLANTE.

Eli, 07-09-2026:

    «el café se ve bien, el problema es la serpentina que se ve fea, se ve como
     si fuera dibujada a mano. No se ve realista, y se ve de un color dorado
     opaco. Tiene que verse mejor realizado, con un dorado brillante»

Dos defectos en una frase, y son distintos:

**«dibujada a mano»** — porque lo está. El adorno era el VECTOR de Eli
(`recursos/confeti-oro/`), una ilustración. Sobre una fotografía de 2.250 px, una
forma vectorial se lee como lo que es.

**«dorado opaco»** — y esto es peor, porque es una corrección propia que se pasó
de largo. Historial:

    ronda 11  papelitos de color plano       → «se ve muy infantil»
    ronda 12  oro metálico dibujado          → «parece un plátano»
    ronda 13  fuera de la foto, sólo doodle  → aprobado a medias
    ronda 14  el vector de Eli, sembrado     → «lo dorado se ve quemado»
    ronda 15  ASIENTO 0,88 → 0,80 + hombro() → **«dorado opaco»**

Medido sobre la entrega y sobre su pieza aprobada:

    material              L p5-p95     especular (L>200)
    el vector, como iba    77-180           0,0 %
    su pieza aprobada      89-197           3,4 %
    cinta fotográfica     41-237          15-26 %   ← el material de esta ronda

**Cero especular.** Apagar los brillos para arreglar «quemado» produjo «opaco»:
el problema nunca fue el brillo máximo, era que el vector no tiene RANGO. Un
metal alterna entre casi blanco y bronce oscuro, y eso no se pinta.

⭐ Así que el material pasa a ser FOTOGRÁFICO —cinta metálica que gira sobre su
eje, generada con Nano Banana Pro sobre blanco y recortada por
`between-cintas-recortar.py`— y el ASIENTO vuelve a 1,0: el `hombro()` de la
marca ya impide que nada llegue a blanco puro, no hace falta apagarlo antes.

⚠️ **La receta de montaje NO se reescribe.** Se importa la de la ronda 14 y se le
cambian tres cosas por entorno (material, prefijo y asiento). Esa receta lleva
cuatro rondas de correcciones del cliente encima —alfa premultiplicado, DOF
medido por bloques, armonización contra el ILUMINANTE y no contra la superficie,
sombra de contacto corta— y cada línea está justificada en su archivo. Cambiarla
sería tirar todo eso.

⚠️ Y las POSICIONES tampoco se mueven: son las de la ronda 14, ya refinadas
(repartidas a lo largo de la mesa, ninguna sobre el plato ni sobre el producto,
ninguna en el aire contra el muro). Eli no objetó dónde están — objetó cómo se
ven. Lo único que cambia es la rotación: la cinta se generó colgando en vertical
y acá va TENDIDA en la mesa, así que gira ~75-100°.

Salidas: cumple-r17-1.jpg y cumple-r17-2.jpg en fotos-gradadas/
"""
import importlib.util
import os
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ── los tres parámetros que cambian, ANTES de cargar el módulo de la r14 ─────
os.environ["BW_CINTA_PIEZAS"] = str(
    RAIZ / "public/assets/hilton/between/recursos/cintas-oro")
os.environ["BW_CINTA_PREFIJO"] = "cinta-oro"
os.environ["BW_CINTA_ASIENTO"] = "1.0"
os.environ.setdefault("BW_CUMPLE_RONDA", "r16pre")     # de qué revelado lee
os.environ.setdefault("BW_CUMPLE_RONDA_OUT", "r17")    # a qué ronda escribe

_spec = importlib.util.spec_from_file_location(
    "between_cumple_confeti_r14", RAIZ / "scripts/between-cumple-confeti-r14.py")
_r14 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_r14)

# ── la siembra ──────────────────────────────────────────────────────────────
# Posiciones de la ronda 14, intactas. Los anchos suben porque una cinta con
# volumen necesita más sitio que un papelito plano para que se lea el giro — y
# el giro es lo que la hace metal. Las rotaciones la tienden sobre la mesa.
#
# Zonas ocupadas del lienzo 2250×2812 (medidas en la r14):
#   muro vegetal desenfocado  y 0-1300   ·  bloque de texto  y 300-720
#   vaso To Go  x 1290-2110 · y 890-2060 ·  plato+medialunas  x 0-1650 · y 1550-2280
# ⛔⛔ OJO CON `ancho`: SE APLICA ANTES DE ROTAR, y acá eso importa muchísimo.
# La cinta se generó COLGANDO (vertical), así que su eje largo es el ALTO. Al
# tenderla en la mesa con una rotación de ~80°, el alto pasa a ser el largo
# visible. Pedí `ancho=260` para la pieza 01 (814×2292) y el resultado midió
# **762 px de largo** sobre un lienzo de 2.250: una cinta de un tercio del ancho
# de la pieza, que se leía como un resorte gigante y competía con las medialunas.
#
# Regla: cuando un recorte se va a ROTAR ~90°, se dimensiona por el eje que va a
# quedar largo, no por `ancho`. Acá `ancho = largo_deseado / (alto/ancho)`.
#
#   pieza  recorte      alto/ancho   largo buscado   → ancho
#     01   814×2292        2,816          250            89
#     03   719×2302        3,201          230            72
#     06   621× 980        1,578          190           120
#     08   757× 921        1,217          170           140
SIEMBRA1 = [
    # (pieza, x,    y,    ancho, rot,  blur, sombra)
    ("01",   1640, 2090,   89,    82,  3.0,  0.16),   # mesa, bajo la base del vaso
    ("03",   1020, 2330,   72,   -96,  4.2,  0.15),   # mesa, al centro
    ("06",    560, 2470,  120,    74,  5.4,  0.13),   # mesa, centro-izquierda
    # ⚠️ x=240 y no 170: el margen de marca son 84 px de lienzo lógico = 175 px
    # acá, y a 170 la cinta quedaba CORTADA por el canto de la pieza.
    ("08",    250, 2545,  140,   -80,  5.4,  0.13),   # mesa, por debajo del plato
]

# Slide 2: el mock de post tapa el centro (x 408-1829 · y 422-2281), así que las
# cintas van en la BANDA DE ABAJO, sobre la misma mesa, para que al deslizar el
# adorno continúe.
#     04   778×1382        1,776          210           118
#     07   719× 783        1,089          160           147
SIEMBRA2 = [
    ("04",   1900, 2380,  118,    88,  4.6,  0.14),
    ("07",    250, 2450,  147,   -84,  5.0,  0.13),
]


def main():
    print(f"material: {_r14.PIEZAS.name}/  ·  prefijo {_r14.PREFIJO}  ·  "
          f"asiento {_r14.ASIENTO}")
    _r14.una(1, SIEMBRA1)
    _r14.una(2, SIEMBRA2)
    print("\nlisto.")


if __name__ == "__main__":
    main()

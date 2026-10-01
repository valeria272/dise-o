#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 13 (01-10) — Eli: en café + opción dulce, el vaso Grande.

Uso:  python scripts/between-oct-r13-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
R = B + "oct-r13/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 13",
           "Café + opción dulce: el vaso Grande",
           "01-10-2026 · carrusel To Go FEED 01-10 (S1), lámina n°4",
           R + "revision-r13.html")
p.pedido("Solo en el café más dulce el vaso creo que sea más grande. Como la opción de café grande, ya que no se ve la "
         "diferencia con el chico, que este sería el slide de los cafés más sándwich.", "Eli", "01-10")
p.comparar((R + "antes/C1 n°4 togo S1.png", "vaso mediano (igual al de café + sándwich)"),
           (R + "C1 n°4 togo S1.png", "vaso Grande"),
           titulo="n°4 · Café + opción dulce",
           notas=("Qué cambió", [
               "<b>Sólo el vaso</b>: ahora es el <b>Grande</b>, más alto y esbelto, sin el anillo blanco del chico. Los vigilantes, "
               "el muffin, el brownie y los papeles quedan donde estaban.",
               "<b>Medido</b>: el chico de café + sándwich tiene alto/tapa 1,33; éste quedó en <b>1,61</b>, que es la proporción "
               "del Grande (1,21 veces el chico con la misma tapa). El XL de la última es 1,87.",
               "⚠️ <b>La API de Magnific se quedó sin créditos</b> a mitad de esta ronda. La única toma que alcanzó a salir traía "
               "el vaso casi del alto del XL y la tapa se metía en los precios, así que lo ajusté sin IA: le saqué un tramo de "
               "cartón liso entre la tapa y el logo. <b>Mira la zona bajo la tapa</b> por si notas algo raro.",
               "<b>Ya reemplazada en Drive</b> (S1/BW/FEED/C1 togo S1, n°4), mismo nombre y enlace, md5 = local.",
           ]))
p.laminas([(R + "C1 n°3 togo S1.png", "n°3 · café + sándwich — vaso chico"),
           (R + "C1 n°4 togo S1.png", "n°4 · café + dulce — vaso Grande"),
           (R + "C1 n°5 togo S1.png", "n°5 · los tres — vaso XL")],
          titulo="Los tres tamaños, lado a lado", ancho=320,
          notas=("Ojo", ["La n°5 es una toma más abierta (entra la bolsa), por eso su XL se ve más chico en el cuadro que el "
                         "Grande de la n°4, aunque el vaso es más alto en proporción."]))
print(p.escribir())

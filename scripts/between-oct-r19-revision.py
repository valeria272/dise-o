#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 19 (01-10) — Eli: lámina 2 con los rótulos en la línea de precios de las
láminas 3 y 4 y las flechas cortas junto a cada precio.

Uso:  python scripts/between-oct-r19-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

R = "out/hilton/between/oct-r19/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 19",
           "Carrusel To Go: lámina 2 en la línea de precios",
           "01-10-2026 · FEED 01-10 (S1), lámina n°2",
           R + "revision-r19.html")
p.pedido("Las flechas más arriba, junto; no importa si no están cerca de los cafés, solo que apunten.", "Eli", "01-10")
p.comparar((R + "antes/C1 n°2 togo S1.png", "flechas sobre las tapas"),
           (R + "C1 n°2 togo S1.png", "flechas junto a cada precio"),
           titulo="n°2 · Tu café To Go", detalle=(40, 250, 1040, 700), escala=1.0,
           notas=("Qué cambió", [
               "Las tres flechas subieron: ahora van <b>pegadas bajo cada caja de precio</b>, cortas, con un rulo chico y la "
               "punta hacia su vaso.",
               "Los rótulos siguen en la línea de precios de las láminas 3 y 4.",
               "<b>Ya reemplazada en Drive</b> (S1/BW/FEED/C1 togo S1, n°2), mismo nombre y enlace, md5 = local.",
           ]))
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="La secuencia completa", ancho=300)
print(p.escribir())

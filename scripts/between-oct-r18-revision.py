#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 18 (01-10) — Eli: lámina 2 con los rótulos en la línea de precios de las
láminas 3 y 4 (su captura con la franja roja) y flechas más cortas.

Uso:  python scripts/between-oct-r18-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

R = "out/hilton/between/oct-r18/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 18",
           "Carrusel To Go: lámina 2 en la línea de precios",
           "01-10-2026 · FEED 01-10 (S1), lámina n°2",
           R + "revision-r18.html")
p.pedido("No, ajústalo según lo que marqué [franja roja sobre la fila de precios de las láminas 2, 3 y 4]. "
         "Y las flechas se ven muy largas.", "Eli", "01-10")
p.comparar((R + "antes/C1 n°2 togo S1.png", "rótulos demasiado arriba, flechas largas"),
           (R + "C1 n°2 togo S1.png", "rótulos en la línea de precios, flechas cortas"),
           titulo="n°2 · Tu café To Go",
           notas=("Qué cambió", [
               "Los rótulos (nombre + precio) quedan <b>exactamente a la altura de la fila de precios</b> de las láminas 3 y 4, "
               "la franja que marcaste.",
               "<b>Flechas más cortas</b>: ya no nacen en la caja del precio; parten un poco sobre cada tapa, hacen el rulo y "
               "entran al vaso.",
               "<b>Ya reemplazada en Drive</b> (S1/BW/FEED/C1 togo S1, n°2), mismo nombre y enlace, md5 = local.",
           ]))
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="La secuencia completa", ancho=300)
print(p.escribir())

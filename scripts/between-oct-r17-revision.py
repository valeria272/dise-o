#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 17 (01-10) — Eli: en la lámina 2, los cafés y las flechas más arriba.

Uso:  python scripts/between-oct-r17-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

R = "out/hilton/between/oct-r17/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 17",
           "Carrusel To Go: lámina 2 pareja con la secuencia",
           "01-10-2026 · FEED 01-10 (S1), lámina n°2",
           R + "revision-r17.html")
p.pedido("Para el slide 2, sube un poco más lo de los cafés, y las flechas, hasta donde dice «De lunes a viernes», "
         "para que todo quede parejo y quede una secuencia bien. La cuarta foto del inicio me parece bien, dejémoslo "
         "así. Todo lo demás lo veo bien, solamente ese temita.", "Eli", "01-10")
p.comparar((R + "antes/C1 n°2 togo S1.png", "rótulos a 374, hueco bajo el título"),
           (R + "C1 n°2 togo S1.png", "rótulos a 206, como la portada"),
           titulo="n°2 · Tu café To Go",
           notas=("Qué cambió", [
               "Los tres rótulos (nombre + precio) <b>subieron 168 px</b>: el nombre queda a la altura de «De lunes a viernes» "
               "y la caja del precio a la altura de la caja del horario de la portada.",
               "<b>Las flechas</b> salen ahora de más arriba y siguen haciendo el rulo sobre la tapa y entrando a cada vaso, "
               "donde estaban.",
               "El acento del XL subió con su rótulo.",
               "<b>Ya reemplazada en Drive</b> (S1/BW/FEED/C1 togo S1, n°2), mismo nombre y enlace, md5 = local.",
           ]))
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="La secuencia completa", ancho=300)
print(p.escribir())

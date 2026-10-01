#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 16 (01-10) — Eli: el carrusel To Go vuelve a las fotos del inicio.

Uso:  python scripts/between-oct-r16-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
R = B + "oct-r16/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 16",
           "Carrusel To Go: de vuelta a las fotos del inicio",
           "01-10-2026 · FEED 01-10 (S1)",
           R + "revision-r16.html")
p.pedido("No lograste un buen resultado en las fotos del carrusel, más como las del inicio, déjalas así; solo la "
         "portada y última ajústalas. Vuelve a eso y obvio tomando los comentarios de cliente. Para el video bien.",
         "Eli", "01-10")
p.laminas([(R + f"C1 n°{k} togo S1.png", pie) for k, pie in (
    (1, "n°1 · portada (pedida por el cliente)"), (2, "n°2 · foto del inicio"), (3, "n°3 · foto del inicio"),
    (4, "n°4 · foto del inicio"), (5, "n°5 · última, con la bolsa con logo"))],
          titulo="El carrusel", ancho=300,
          notas=("Cómo quedó", [
              "<b>n°2, n°3 y n°4</b>: las mismas fotos que aprobaste el 30-09 (los tres vasos, café + sándwich con ave palta y "
              "jamón queso, café + dulce con vigilantes, muffin y brownie). Lo único distinto es el comentario del cliente: "
              "<b>sin la línea de horarios</b>, que ahora vive en la portada.",
              "<b>n°1 portada</b> (la «slide de introducción» del cliente): «Promos To Go · De lunes a viernes · De 8:00 a 10:00 hrs» "
              "sobre la toma lifestyle que pediste: mano con el café chico destapado, cappuccino a la vista, sándwich ave palta "
              "y la bolsa con logo.",
              "<b>n°5 última</b>: café XL, sándwich, muffin y la <b>bolsa blanca del cliente con el logo vigente</b> calzado en "
              "perspectiva; las asas van caídas hacia atrás para que la bolsa quepa bajo los precios.",
              "Las versiones sobre fotos reales de la sesión quedaron guardadas en <code>out/hilton/between/oct-r15/</code>, fuera de Drive.",
              "<b>Ya reemplazado en Drive</b> (S1/BW/FEED/C1 togo S1), las 5 con el mismo nombre y enlace, md5 = local.",
          ]))
print(p.escribir())

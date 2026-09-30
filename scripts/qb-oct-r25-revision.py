#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 25 (Eli 30-09): Sunset con plato para compartir y luz natural.

    python scripts/qb-oct-r25-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

R = "out/qb/oct/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 25", "Sunset: plato para compartir y luz natural",
           "30-09-2026 · 1 archivo reemplazado en Drive (md5 igual) · lo demás de la r24, aprobado",
           R + "r25/revision-r25.html", origen="scripts/qb-oct-r25-revision.py")
p.comparar((R + "r25/_antes/ST n°5 S1 QB OCT 26.png", "antes (r24)"), (R + "r25/ST n°5 S1 QB OCT 26.png", "ahora (r25)"),
           titulo="ST 09-10 · Sunset QB  (ST n°5 S1)", ancho=400,
           que="Eli: «ese plato no me convence, que se vea más lifestyle, un plato mejor como para compartir, y el "
               "naranja es demasiado saturado: la luz debe ser natural y sutil» · «lo demás okey».",
           notas=("Qué cambió", ["Plato: TABLA ARGENTINA, de «Platos para compartir» de la carta de Terraza (bife, "
                                 "brochetas de choricillo, papas fritas y salsas de la casa), con su foto de la carta como "
                                 "referencia. Salen las empanadas.",
                                 "Lifestyle: manos de amigos sacando papas y carne de la tabla, sin tapar el trago.",
                                 "Luz: fuera el baño naranja de la r24; la foto se corrigió en origen (balance más neutro y "
                                 "saturación −10 %). Queda una calidez de tarde sutil en la madera y el trago.",
                                 "Terraza, trago, composición y velos: los mismos de la r24.",
                                 "Textos: sin cambios."]))
p.escribir()

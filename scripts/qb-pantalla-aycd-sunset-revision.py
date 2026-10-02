# -*- coding: utf-8 -*-
"""Página de revisión de la pantalla digital AYCD + Sunset QB (02-10-2026)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina

R = sys.argv[1] if len(sys.argv) > 1 else "r1"
D = f"out/qb/oct/pantalla-aycd-sunset/{R}"
p = Pagina("qb", f"QB · PANTALLA DIGITAL · {R.upper()}",
           "All You Can Drink + Sunset QB, con el Sunset nuevo",
           "02-10-2026 · 1080×1920 y 1230×720 (ascensor)",
           f"{D}/revision-{R}.html")
A = "out/qb/oct/pantalla-aycd-sunset/r2"
p.pedido("Agrega los horarios en ambos y que en jerarquía quede parejo y bien. Baja un poco la opacidad "
         "al Sunset QB, ese recuadro, que quede como el del AYCD.", "Eli", "02-10")
p.comparar((f"{A}/72ppp_PANTALLA AYCD+SUNSET.jpg", "r2: sin horarios, recuadro de Sunset más oscuro"),
           (f"{D}/72ppp_PANTALLA AYCD+SUNSET.jpg", "r3: horario bajo cada precio, recuadro más liviano"),
           titulo="Pantalla 1080×1920")
p.comparar((f"{A}/72ppp_ASCENSOR AYCD+SUNSET.jpg", "r2"),
           (f"{D}/72ppp_ASCENSOR AYCD+SUNSET.jpg", "r3"),
           titulo="Ascensor 1230×720")
p.comparar(("out/qb/oct/pantalla-aycd-sunset/r1/_antes/antes-pantalla-1080x1920.jpg", "Tu editable (QB TIME)"),
           (f"{D}/72ppp_PANTALLA AYCD+SUNSET.jpg", "Ahora"), titulo="Contra tu editable original")
p.notas([
    "Horario bajo la franja de precio en las dos promos, con la misma letra de tu pantalla sola de AYCD "
    "(«18:00 a 21:00 hrs», Raleway Medium con tracking): <b>18:00 a 21:00 hrs</b> en AYCD y <b>16:00 a 21:00 hrs</b> en Sunset.",
    "Las dos mitades leen igual, de arriba hacia abajo: día → nombre → precio → horario → tragos.",
    "Para hacerle espacio al horario, el listado de tragos de AYCD bajó 29 px en la vertical y 2 px en la de ascensor. Es lo único que se movió en esa mitad.",
    "El velo del recuadro de Sunset bajó de 66 % a 40 %.",
])
print(p.escribir())

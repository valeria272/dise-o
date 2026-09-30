#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · ST Sunset V2 · RONDA 1 (Eli 30-09): caja sutil detrás del rótulo y botón
al ancho de la bajada.

    python scripts/qb-oct-sunset-v2-r1-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/sunset-v2/", "out/qb/oct/sunset-v2/r1/"
F = "ST n°5 S1 QB OCT 26 - SUNSET V2.png"
p = Pagina("qb", "QB · OCTUBRE 2026 · ST SUNSET V2 · RONDA 1", "El rótulo se lee y el botón se acorta",
           "30-09-2026 · reemplazado en Drive (S1 / QB / STS)", N + "revision-sunset-v2-r1.html",
           origen="scripts/qb-oct-sunset-v2-r1-revision.py")
p.comparar((A + F, "antes"), (N + F, "ahora"), titulo="ST 09-10 · Sunset QB v2", ancho=400,
           detalle=(0, 640, 1080, 1780),
           que="Eli: «el texto que dice cócteles seleccionados al mejor precio no se ve: deja una cajita oscurecida o "
               "una transparencia detrás, que sea sutil» · «de 16 a 21 horas tiene demasiado sobrante de caja: que sea "
               "como el corte donde dice Tu after office, a otro nivel… eso es como regla para todos».",
           notas=("Qué cambió", ["Detrás de «Cocktails seleccionados al mejor precio / DESDE $3.990»: una caja negra "
                                 "translúcida (38 %) con un desenfoque leve de las luces de fondo.",
                                 "El botón «DE 16:00 A 21:00 HRS» pasa de 520 a 392 px: empieza y termina donde "
                                 "empieza y termina «Tu after office, a otro nivel».",
                                 "Foto, logo, titular y legal: iguales.",
                                 "Textos: sin cambios."]))
p.escribir()

#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 10 (01-10) — ST 01-10 ganador del concurso: línea del premio.

Uso:  python scripts/between-oct-r10-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
N = "BW ST 01-10 Anuncio ganador concurso.png"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 10",
           "Ganador del concurso: línea del premio",
           "01-10-2026 · ST 01-10 (S1) · urgente, se publica hoy",
           B + "oct-r10/revision-r10.html")

p.pedido("Cambiemos el texto de abajo por este → Te contactaremos por interno con la información "
         "de tu premio.", "Nicolás, hilo en la grilla (STORIES C12)", "01-10")

p.comparar((B + "oct-r10/antes/" + N, "aprobada 29-09"),
           (B + "oct-r10/" + N, "ronda 10"),
           titulo="ST 01-10 · Anuncio ganador concurso", detalle=(200, 920, 880, 1230), escala=1.2,
           notas=("Qué cambió", [
               "<b>La línea bajo el premio</b>: «Te contactaremos para entregarte la información de tu premio» → "
               "«Te contactaremos por interno / con la información de tu premio».",
               "<b>Corte antes de «con»</b>, para que la primera línea no termine en preposición. Sin punto final, "
               "como todas las bajadas de Hilton (Nicolás lo escribió con punto).",
               "<b>Nada más se movió</b>: misma voz (Raleway SemiBold 36), mismos aires; la diferencia entre las dos "
               "versiones cae sólo dentro de esas dos líneas.",
               "<b>Ya reemplazada en Drive</b> en S1/BW/STS, con el mismo nombre y enlace (md5 = local).",
           ]))

print(p.escribir())

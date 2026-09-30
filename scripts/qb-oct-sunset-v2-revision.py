#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · ST Sunset VERSIÓN 2 (Eli 30-09): la foto de Magnific con un solo cóctel,
al lado de la r28 aprobada, para mostrársela a contenido.

    python scripts/qb-oct-sunset-v2-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

R, N, S = "out/qb/oct/r28/", "out/qb/oct/sunset-v2/", "raw/hilton/qb/sunset-v2/"
p = Pagina("qb", "QB · OCTUBRE 2026 · ST SUNSET V2", "Un solo cóctel, el del centro",
           "30-09-2026 · alternativa a la r28 aprobada (que no se toca)", N + "revision-sunset-v2.html",
           origen="scripts/qb-oct-sunset-v2-revision.py")
p.comparar((R + "ST n°5 S1 QB OCT 26.png", "antes · r28 aprobada"),
           (N + "ST n°5 S1 QB OCT 26 - SUNSET V2.png", "ahora · versión 2"),
           titulo="ST 09-10 · Sunset QB  (ST n°5 S1)", ancho=400,
           que="Eli: «lo más similar [a la foto de Magnific] pero con un solo cóctel, que sea el del centro, "
               "cosa que destaque… una copia del anterior para ver el antes y el después».",
           notas=("Qué cambió", ["Foto: la «AA — v7 Post 3:4» del Space de Magnific de Eli en vez de la foto real de la terraza.",
                                 "Fuera la flauta de espumante y el mojito (con sus sombras): queda sólo el spritz del centro, nítido.",
                                 "Fuera la tabla para compartir: la mesa de adelante queda vacía, sólo el trago.",
                                 "La foto se extendió a historia (9:16): más pérgola y lámparas arriba, la misma mesa abajo.",
                                 "El rótulo «Cocktails… DESDE $3.990» va a la izquierda, a la altura de la copa; la flecha llega al trago.",
                                 "El bloque de texto baja 20 px para no tocar el pie de la copa. Logo, botón y legal: iguales.",
                                 "Textos: sin cambios."]))
p.laminas([(S + "AA-v7-post-3x4.jpg", "<b>1 · Magnific</b> — la original (3 tragos)"),
           (S + "paso1-un-coctel.png", "<b>2 · un solo cóctel</b> — sin espumante ni mojito"),
           (S + "09-sunset-v2.jpg", "<b>3 · extendida a 9:16</b> — la que usa la v2")],
          titulo="Cómo se llegó a la foto", ancho=330)
p.notas(["La foto es generada (Magnific), así que el legal mantiene «*Imagen referencial».",
         "Ojo: la terraza de esta foto (pérgola con lámparas de mimbre) no es la de la sesión de QB; "
         "la r28 usa la foto real. Vale la pena que contenido lo vea al comparar."])
p.escribir()

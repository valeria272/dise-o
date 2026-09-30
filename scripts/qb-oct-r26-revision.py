#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 26 (Eli 30-09): Sunset sin manos y con una sola mesa.

    python scripts/qb-oct-r26-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

R = "out/qb/oct/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 26", "Sunset: foto nueva, sin manos y una sola mesa",
           "30-09-2026 · 1 archivo reemplazado en Drive (md5 igual) · lo demás de la r24, aprobado",
           R + "r26/revision-r26.html", origen="scripts/qb-oct-r26-revision.py")
p.comparar((R + "r26/_antes/ST n°5 S1 QB OCT 26.png", "antes (r25)"), (R + "r26/ST n°5 S1 QB OCT 26.png", "ahora (r26)"),
           titulo="ST 09-10 · Sunset QB  (ST n°5 S1)", ancho=400,
           que="Eli: «sin manos, y aparece otra mesa extraña: vuelve a hacer esa foto mejor».",
           notas=("Qué cambió", ["Foto nueva desde cero: UNA sola mesa de listones, vista un poco desde arriba, que llega "
                                 "hasta el borde de abajo. Sin manos.",
                                 "Plato: la misma Tabla Argentina de la carta de Terraza, completa, y el spritz.",
                                 "Terraza de QB a nivel de calle: tela beige con ventiladores, ventanales de marco negro "
                                 "y, detrás, la vereda con árboles y autos (sin techos ni vista de altura).",
                                 "Luz natural y sutil, sin baño naranja.",
                                 "El bloque «EL VIERNES CAMBIA de mood», la pastilla y la bajada bajan 134 px para quedar "
                                 "sobre la mesa vacía y no tapar la comida. La flecha apunta al trago. El legal no se mueve.",
                                 "Textos: sin cambios."]))
p.escribir()

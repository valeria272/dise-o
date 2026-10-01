#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 31 (Eli 01-10): carrusel AYCD — «Imagen referencial» abajo al
centro y el cóctel centrado en la portada.

    python scripts/qb-oct-r31-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r31/_antes/", "out/qb/oct/r31/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 31", "Carrusel All You Can Drink — leyenda al centro y cóctel centrado",
           "01-10-2026 · 2 archivos reemplazados en Drive (md5 igual)", N + "revision-r31.html",
           origen="scripts/qb-oct-r31-revision.py")
p.pedido("Lo de imagen referencial abajo al centro y mejora la posición del cóctel", "Eli", "01-10-2026")
p.comparar((A + "C2 S1 N°1 QB OCT 26.png", "r30: vaso cargado a la izquierda, leyenda al costado"),
           (N + "C2 S1 N°1 QB OCT 26.png", "r31: vaso centrado, leyenda abajo al centro"),
           titulo="G1 · Portada  (C2 S1 N°1)", ancho=420,
           notas=("Qué cambió", ["El vaso queda centrado en la lámina (antes estaba corrido a la izquierda).",
                                 "«*Imagen referencial» va abajo al centro. Ahí la barra tiene puntos de luz, así que lleva una cajita translúcida muy sutil para que se lea.",
                                 "Textos: sin cambios."]))
p.comparar((A + "C2 S1 N°2 QB OCT 26.png", "r30"), (N + "C2 S1 N°2 QB OCT 26.png", "r31: la foto se corre lo mismo que la portada"),
           titulo="G2 · Promo  (C2 S1 N°2)", ancho=420,
           notas=("Qué cambió", ["El fondo se corrió junto con la portada para que el panorama siga calzando; entra un poco más del romero por la izquierda.",
                                 "Logo, nombre, botón, horario y legal: mismas posiciones y mismos textos."]))
p.opciones([(N + "_panorama-al-deslizar.jpg", "G1 + G2 una al lado de la otra, como se ven al deslizar")],
           titulo="El carrusel como panorama", ancho=1000, elige=False)
p.notas(["El vaso no se puede subir más: la foto real termina justo debajo de su base.",
         "Drive: S1 HILTON OCT 2026 / QB / FEED / C2 S1 AYCD — mismos nombres y enlaces."], titulo="Notas")
p.escribir()

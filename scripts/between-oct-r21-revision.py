#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 21 (01-10) — Eli: la bolsa de la última lámina del carrusel To Go pasa a
ser la misma de la portada (vertical, con las asas de papel torcido paradas).

Uso:  python scripts/between-oct-r21-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

R = "out/hilton/between/oct-r21/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 21",
           "Carrusel To Go: la bolsa de la última lámina, igual a la de la portada",
           "01-10-2026 · FEED 01-10 (S1), lámina n°5",
           R + "revision-r21.html")
p.pedido("La última slide del carrusel, ajusta la bolsa, no se parece a la de la portada; con eso tenemos listo el carrusel.",
         "Eli", "01-10")
p.comparar((R + "antes/C1 n°5 togo S1.png", "bolsa ancha, sin asas a la vista"),
           (R + "C1 n°5 togo S1.png", "la bolsa de la portada"),
           titulo="n°5 · Café + sándwich + dulce", detalle=(420, 400, 1060, 1100), escala=1.0,
           notas=("Qué cambió", [
               "La bolsa es ahora <b>la misma de la portada</b>: vertical, con las dos asas de papel torcido paradas y el "
               "logotipo vigente calzado en perspectiva sobre su cara.",
               "Queda <b>detrás del muffin</b> y separada del vaso; las asas terminan justo bajo la fila de precios, sin tocar "
               "la caja del Café XL.",
               "<b>Nada más se movió</b>: vaso, sándwich, muffin, mesa, muro, título, precios y acento son los mismos de la r20.",
               "<b>Ya reemplazada en Drive</b> (S1/BW/FEED/C1 togo S1, n°5), mismo nombre y enlace, md5 = local.",
           ]))
p.comparar((R + "C1 n°1 togo S1.png", "portada"),
           (R + "C1 n°5 togo S1.png", "última lámina"),
           titulo="La bolsa de la portada y la de la última, lado a lado", escala=1.0)
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="La secuencia completa", ancho=300)
print(p.escribir())

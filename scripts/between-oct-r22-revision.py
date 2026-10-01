#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 22 (01-10) — Eli: la bolsa de la última lámina del carrusel To Go, un poco más
grande (0,80 → 0,88) — con eso el carrusel queda OK.

Uso:  python scripts/between-oct-r22-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

R = "out/hilton/between/oct-r22/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 22",
           "Carrusel To Go: la bolsa de la última lámina, igual a la de la portada",
           "01-10-2026 · FEED 01-10 (S1), lámina n°5",
           R + "revision-r22.html")
p.pedido("La bolsita un poco más grande y ok.", "Eli", "01-10")
p.comparar((R + "antes/C1 n°5 togo S1.png", "r21 · bolsa de la portada, chica"),
           (R + "C1 n°5 togo S1.png", "r22 · un 10 % más grande"),
           titulo="n°5 · Café + sándwich + dulce", detalle=(420, 380, 1060, 1180), escala=1.0,
           notas=("Qué cambió", [
               "La bolsa es <b>un 10 % más grande</b>. Como las asas no pueden subir (tocarían la caja del Café XL), "
               "crece hacia abajo y a los lados: queda apoyada un poco más adelante en la mesa, siempre detrás del muffin.",
               "El logotipo creció con ella, calzado en la misma perspectiva.",
               "<b>Nada más se movió</b>: vaso, sándwich, muffin, mesa, muro, título, precios y acento.",
               "<b>Ya reemplazada en Drive</b> (S1/BW/FEED/C1 togo S1, n°5), mismo nombre y enlace, md5 = local.",
           ]))
p.comparar((R + "C1 n°1 togo S1.png", "portada"),
           (R + "C1 n°5 togo S1.png", "última lámina"),
           titulo="La bolsa de la portada y la de la última, lado a lado", escala=1.0)
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="La secuencia completa", ancho=300)
print(p.escribir())

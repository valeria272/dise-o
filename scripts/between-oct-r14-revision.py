#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 14 (01-10) — Eli: tamaños de vaso coherentes entre las láminas.

Uso:  python scripts/between-oct-r14-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
R, A = B + "oct-r14/", B + "oct-r14/antes/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 14",
           "Carrusel To Go: tamaños coherentes",
           "01-10-2026 · FEED 01-10 (S1), láminas n°3, n°4 y n°5",
           R + "revision-r14.html")
p.pedido("Vuelve a hacer las imágenes para que se vean coherentes los tamaños, es lo que más comentarios tendré.",
         "Eli", "01-10")
p.laminas([(A + "C1 n°3 togo S1.png", "ANTES n°3 · chico"), (A + "C1 n°4 togo S1.png", "ANTES n°4 · Grande"),
           (A + "C1 n°5 togo S1.png", "ANTES n°5 · XL")],
          titulo="Antes: cada lámina a una distancia distinta", ancho=320,
          notas=("El problema, medido", [
              "Alto del vaso en la lámina (de 1350 px): chico <b>397</b> · Grande <b>593</b> · XL <b>370</b>. "
              "El XL se veía más bajo que el chico, y el Grande era el más grande de todos.",
          ]))
p.laminas([(R + "C1 n°3 togo S1.png", "AHORA n°3 · café + sándwich — chico"),
           (R + "C1 n°4 togo S1.png", "AHORA n°4 · café + dulce — Grande"),
           (R + "C1 n°5 togo S1.png", "AHORA n°5 · los tres — XL")],
          titulo="Ahora: la misma distancia de cámara en las tres", ancho=320,
          notas=("Qué cambió", [
              "<b>Una sola escala</b> para las tres láminas de producto. Alto del vaso ahora: chico <b>324</b> · Grande "
              "<b>374</b> · XL <b>440</b> px: crecen en orden y en la proporción real de los vasos aprobados "
              "(0,71 · 0,86 · 1). Los tres se apoyan en la misma línea de mesa.",
              "<b>n°3 café + sándwich</b>: toma nueva con la cámara más lejos, mismo vaso chico y los dos sándwiches.",
              "<b>n°4 café + dulce</b>: el vaso Grande es el <b>recorte aprobado</b> puesto a su tamaño exacto y después "
              "integrado a la luz de la escena; vigilantes, muffin y brownie son los mismos. Ya no lleva el retoque a mano de la ronda anterior.",
              "<b>n°5 los tres</b>: misma escena, más cerca. ⚠️ Para que la bolsa cupiera bajo los precios a esta escala, "
              "<b>las asas van caídas hacia atrás</b> (no se ven). Si las quieres arriba, la única forma es alejar las tres láminas otro poco.",
              "El logo de la bolsa sigue calzado en perspectiva sobre la cara.",
          ]))
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="El carrusel completo", ancho=260,
          notas=("Para que lo tengas presente", [
              "<b>n°2 (los tres vasos)</b> no la toqué: es un plano más cercano, de detalle, y ahí los vasos se ven más "
              "grandes que en las otras. Si te van a comentar eso también, la alejo a la misma escala (hay que recalzar rótulos y flechas).",
              "<b>Portada</b>: el vaso en la mano ya estaba a una escala parecida; no cambió.",
              "<b>Ya reemplazado en Drive</b> (S1/BW/FEED/C1 togo S1), las 5 con el mismo nombre y enlace, md5 = local.",
          ]))
print(p.escribir())

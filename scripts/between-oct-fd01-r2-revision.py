#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · FEED 01-10 · RONDA 2 (30-09) — «Café» + rótulos al eje + flechas de la ref.

Uso:  python scripts/between-oct-fd01-r2-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

E = "out/hilton/between/oct-fd01/"
A = E + "antes/"
N = ["1 cafe to go", "2 cafe sandwich", "3 cafe dulce", "4 cafe sandwich dulce"]
f = lambda d, n: d + f"BW FEED 01-10 Promos To Go {n}.png"  # noqa: E731

p = Pagina("between", "BETWEEN · OCTUBRE · FEED 01-10 · RONDA 2",
           "Promos To Go: «Café», rótulos al eje y flechas",
           "30-09-2026 · S1 · ya reemplazado en Drive",
           E + "revision-fd01-r2.html")

p.pedido("Antes de Mediano, etc., va «Café» […] quiero que la portada centre según cada vaso ese texto de "
         "café y el precio […] añade unas flechitas como guía visual, igual a la referencia, una de las "
         "primeras que hay. Me gustó mucho la imagen de fondo y los textos.", "Eli", "30-09")

p.comparar((f(A, N[0]), "primera entrega"), (f(E, N[0]), "ronda 2"),
           titulo="1 · Portada", detalle=(40, 330, 1060, 760), escala=1.0,
           notas=("Qué cambió", [
               "<b>«Café Mediano · Café Grande · Café XL»</b> en las cuatro láminas.",
               "<b>Cada rótulo centrado en el eje de SU vaso</b>, medido sobre la tapa: 225 · 531 · 844 px "
               "(antes 205 · 488 · 770, corridos a la izquierda).",
               "<b>Flecha punteada con rulo</b> que baja al primer rótulo y <b>rayitas de acento</b> junto al XL, "
               "como la referencia.",
           ]))
for i, t in ((1, "2 · Café + sándwich"), (2, "3 · Café + opción dulce"), (3, "4 · Café + sándwich + dulce")):
    p.comparar((f(A, N[i]), "primera entrega"), (f(E, N[i]), "ronda 2"), titulo=t)

p.notas([
    "En la 2, 3 y 4 las tres columnas de precio tienen ahora el <b>mismo ancho</b>: con «Café Mediano» más "
    "largo, la separación pareja corría los ejes.",
    "Flechas: una a cada sándwich en la 2, a los vigilantes en la 3 y al sándwich en la 4, siempre por el "
    "costado, sin pasar por encima del texto ni del producto.",
    "<b>Ya reemplazado en Drive</b>, en S1 HILTON OCT 2026 / BW / FEED, con los mismos nombres y enlaces "
    "(md5 = local). La entrega anterior quedó respaldada en <code>oct-fd01/antes/</code>.",
], titulo="Notas")

print(p.escribir())

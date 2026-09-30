#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · FEED 01-10 (30-09) — carrusel Promos To Go, primera entrega.

Uso:  python scripts/between-oct-fd01-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
E = B + "oct-fd01/"
p = Pagina("between", "BETWEEN · OCTUBRE · FEED 01-10",
           "Carrusel Promos To Go — propuesta nueva",
           "30-09-2026 · S1 · grilla col E, OK PARA DISEÑAR",
           E + "revision-fd01.html")

p.pedido("Que sea propuesta nueva para todo lo que es To Go, ya que el último carrusel es reciclado y "
         "necesitamos uno nuevo […] Que sea mismo formato que el diseño que subimos ahora último, pero con "
         "diseño actualizado (respetar la misma info de cada slide que tenemos). Mucho ojo que si usamos IA "
         "ver que las proporciones de los vasos y las comidas sean adecuadas.",
         "Comentarios de diseño en la grilla", "col E",
         que="Y el hilo de Scarlette → Nicolás (29-09): «ajustar carrusel con info de PROMOS TO GO»; "
             "Nicolás lo dejó listo hoy a las 14:42. Se diseñó el brief ya ajustado: 4 láminas con sus textos literales.")

p.laminas([
    (E + "BW FEED 01-10 Promos To Go 1 cafe to go.png", "1 · Tu café to go"),
    (E + "BW FEED 01-10 Promos To Go 2 cafe sandwich.png", "2 · Café + sándwich"),
    (E + "BW FEED 01-10 Promos To Go 3 cafe dulce.png", "3 · Café + opción dulce"),
    (E + "BW FEED 01-10 Promos To Go 4 cafe sandwich dulce.png", "4 · Café + sándwich + dulce"),
], titulo="Las 4 láminas", notas=("Cómo se armó", [
    "<b>La referencia</b> (vasos en fila con un rótulo encima de cada uno) se tradujo en la lámina 1: "
    "cada tamaño lleva su nombre y su precio sobre el vaso. En la 2, 3 y 4 los tres precios van en fila "
    "bajo el título, con la misma pieza gráfica.",
    "<b>Mismo formato que el carrusel de septiembre</b> (4 láminas, mesa de madera y muro verde, sin logo "
    "porque el vaso ya lo trae), pero con escenas nuevas: nada es foto reciclada.",
    "<b>Proporciones</b>: los vasos son los que aprobaste el 22-09, ya a escala real entre sí "
    "(0,71 · 0,86 · 1). La comida se generó con la sesión real del 25-jul-2025 como referencia "
    "(sándwich ave palta, vigilantes, muffin). Logotipo revisado al 300 % en cada lámina: dice BƎTWEEN bien.",
    "<b>Tipografía</b> con las reglas nuevas: 3 voces Raleway (título, cajas de precio, texto), "
    "precios con números alineados, cajas del mismo ancho, sin punto final.",
    "<b>Ya está en Drive</b>: S1 HILTON OCT 2026 / BW / FEED (md5 = local).",
]))

p.notas([
    "<b>Lámina 1 · «variar el tipo de café en cada vaso»</b>: los vasos van tapados (así son los aprobados), "
    "así que la variedad no se ve. Si la quieres, puedo destapar uno y mostrar el latte art.",
    "<b>Lámina 2 · jamón queso</b>: no hay foto real del sándwich de jamón queso en triángulo; salió "
    "generado con el mismo pan del de ave palta. Si tienes foto real, lo cambio.",
    "<b>Lámina 3 · brownie</b>: tampoco hay foto real del brownie de Between con el vaso nuevo; está "
    "generado sobre el de la foto de septiembre.",
    "<b>Lámina 4</b>: en la primera tirada salió un vigilante que parecía un croissant chico. Lo "
    "borré, y la lámina queda con sándwich + muffin, que es lo que pide el brief.",
    "<b>Horario</b>: la 1 dice literal «De lunes a viernes desde las 8:00 a 10:00 hrs» y la 2–4 «De 8:00 a "
    "10:00 hrs», como en el brief.",
    "<b>Nombres de productos</b>: en septiembre el cliente pidió no nombrar platos hasta que saliera la carta "
    "nueva (R-62). Como el brief de ahora los escribe, los dejé.",
    "La grilla trae «REF - REF 2 - REF 3», pero en la celda sólo hay un enlace (el pin de los tres "
    "vasos). Si había dos refs más, pásamelas.",
], titulo="Dudas")

print(p.escribir())

#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 15 (01-10) — Eli: fondo real y proporción real en el carrusel To Go;
legal chico al pie en el reel de cumpleaños.

Uso:  python scripts/between-oct-r15-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
R, A = B + "oct-r15/", B + "oct-r15/antes/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 15",
           "Carrusel To Go sobre fotos reales",
           "01-10-2026 · FEED 01-10 (S1) · y el legal al pie del reel 02-10",
           R + "revision-r15.html")
p.pedido("Ahora sigamos mejorando lo del fondo de las promos, ya que no lograste que se vieran realista tanto en proporción.",
         "Eli", "01-10")
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="El carrusel, ahora sobre fotos reales de Between", ancho=300,
          notas=("Qué cambió", [
              "<b>El fondo ya no es generado.</b> Las cinco láminas parten de la sesión To Go real del 25-jul-2025: la mesa de "
              "madera gastada, el muro verde oscuro, la loza y la comida son los de la foto.",
              "<b>La proporción sale de la foto</b>, no de un prompt: el vaso está fotografiado junto al sándwich y al muffin. "
              "Lo único que cambié en esas fotos es el vaso (el de la sesión es el modelo anterior): puse el recorte aprobado "
              "del vaso vigente a su tamaño exacto y la IA sólo lo integró a la luz.",
              "<b>n°3 café + sándwich</b>: foto real del ave palta en su plato + vaso chico. Ya no aparece el jamón queso "
              "(no hay foto real de ese sándwich en la sesión); el texto sigue diciendo «Ave Palta o Jamón Queso».",
              "<b>n°4 café + dulce</b>: foto real del muffin + vaso Grande. Ya no van vigilantes ni brownie generados.",
              "<b>n°2 los tres vasos</b>: los recortes aprobados sobre la misma mesa real, en el mismo lugar que antes "
              "(rótulos y flechas no se movieron).",
          ]))
p.comparar((A + "C1 n°5 togo S1.png", "fondo generado, bolsa chica sin asas"),
           (R + "C1 n°5 togo S1.png", "foto real ampliada, bolsa a tamaño real"),
           titulo="n°5 · Café + sándwich + dulce",
           notas=("Una decisión que tienes que mirar", [
               "A la escala de las láminas 2, 3 y 4 el cuadro mide unos 26 cm de ancho: <b>no caben dos platos ni una bolsa de "
               "verdad</b>. La bolsa de antes medía apenas un poco más que el vaso, y eso es lo que no era real.",
               "Por eso la n°5 (y la portada) son un <b>plano más abierto</b>, como lo tomaría el fotógrafo: sándwich y muffin "
               "reales en sus platos, café XL, y la bolsa detrás a 1,4 veces el alto del vaso, con sus asas.",
               "⚠️ El costo: en la n°5 el XL se ve <b>más chico en el cuadro</b> que el vaso de la n°4 (es un plano más lejano). "
               "Dentro de cada foto la proporción es la real. Si prefieres que todas vayan a la misma distancia, hay que "
               "abrir también las láminas 2, 3 y 4 y los productos se verán más chicos.",
               "El logo de la bolsa va calzado en perspectiva sobre su cara, en café de marca.",
           ]))
p.comparar((A + "C1 n°1 togo S1.png", "fondo generado"),
           (R + "C1 n°1 togo S1.png", "misma mesa y muro reales"),
           titulo="n°1 · Portada", ancho=380,
           notas=("Qué cambió", [
               "Misma idea lifestyle (mano con el café chico destapado, cappuccino a la vista, tapa en la mesa, sándwich ave "
               "palta y bolsa), ahora sobre la escena real de la n°5.",
               "La mano, la bolsa y la extensión de la mesa hacia la derecha sí son generadas.",
           ]))

p.pedido("El legal del *Presenta tu… *Extras y… eso va en modo legal abajo en pequeño, en el video de cumpleaños.",
         "Eli", "01-10", titulo="Reel café de cumpleaños · legal al pie")
p.comparar((B + "oct-r12/BW FEED 02-10 Cafe de cumpleanos - PORTADA.png", "6 botones"),
           (R + "BW FEED 02-10 Cafe de cumpleanos - PORTADA.png", "5 botones + legal chico al pie"),
           titulo="Reel · cierre", ancho=320, detalle=(0, 1560, 1080, 1920), escala=0.9,
           notas=("Qué cambió", [
               "Al pie, chico y en dos líneas: «*Presenta tu cédula de identidad para canjear tu café el día de tu cumpleaños.» "
               "y «*Extras y personalizaciones no incluidas.» (verbatim de la captura del cliente). Entra con «Ven por tu café "
               "de regalo» y se queda hasta el final.",
               "Los botones vuelven a ser los cinco del beneficio, al tamaño que ya habías aprobado, y sin asterisco "
               "(los asteriscos quedaron en el legal chico). Si lo quieres también en «Beneficio…», lo pongo.",
               "Lo dejé bajo las manos para que no pise el vaso ni los dedos; queda cerca del borde inferior.",
               "<b>Ya reemplazado en Drive</b> (MP4 + GIF + PORTADA, md5 = local).",
           ]))
print(p.escribir())

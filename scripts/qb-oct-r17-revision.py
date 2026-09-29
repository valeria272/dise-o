#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 17 (Eli 29-09): en la ST 13-10 AYCD, el legal entero en una
línea y la lista de tragos aparte, más grande y ordenada.

    python scripts/qb-oct-r17-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 17", "El legal en una línea",
           "29-09-2026 · ST 13-10 All You Can Drink · reemplazada en Drive", "out/qb/oct/r17/revision-r17.html",
           origen="scripts/qb-oct-r17-revision.py")
p.pedido("En la ST del 13-10, que «Imagen referencial», «Sujeto a consumo de alimentos» y «Promoción no acumulable» "
         "estén en la misma línea, desde imagen hasta beneficios. Y luego los tragos, porque son distintos del legal. "
         "Los cócteles no son tanto legal: aumenta un poco el tamaño y ordénalos mejor, o en una sola línea, de manera "
         "que se vea bien. Las demás ST están ok.", "Eli", "29-09")
p.comparar(("out/qb/oct/r17/_antes/AP-AYCD13.png", "ronda 16"), ("out/qb/oct/r17/AP-AYCD13.png", "ronda 17"),
           titulo="ST 13-10 · All You Can Drink  (ST n°2 S2)", que="Legal en una línea y tragos aparte.",
           detalle=(40, 1200, 1040, 1640), escala=1.0, ancho=420,
           notas=("Qué cambió", [
               "El legal completo, de «*Imagen referencial» a «beneficios.», va en UNA sola línea (18 px)",
               "Debajo, con margen, los tragos: de 20 a 24 px y en letra recta, no itálica, para que no se lean como legal",
               "Reordenados en dos líneas parejas con «·»: «Schop Heineken · Piscola 35° (Mistral o Alto del Carmen)» / «Ramazzotti · Sangría · Copa de espumante (opción de la casa)». En una sola línea no cabían a un tamaño legible",
               "Todo cierra a 1563 px, dentro de la zona segura. Nada más cambió en la pieza"]))
p.notas(["La ST 27-10 del mismo diseño no se tocó (verificado: idéntica a lo entregado).",
         "Las demás historias quedan como en la ronda 16.",
         "QA de QB: 0 bloqueantes. Reemplazada en Drive con el mismo nombre (mismo enlace); si la vista previa muestra la vieja, es caché."],
        titulo="Lo demás")
p.escribir()

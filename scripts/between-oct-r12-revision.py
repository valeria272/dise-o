#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 12 (01-10) — Eli: portada lifestyle, vasos que varían de tamaño, bolsa
mejor diagramada con el logo en perspectiva, y «*» en el legal del reel.

Uso:  python scripts/between-oct-r12-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
R, A = B + "oct-r12/", B + "oct-r12/antes/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 12",
           "Carrusel To Go: portada, tamaños y bolsa",
           "01-10-2026 · FEED 01-10 (S1) · y el «*» del reel 02-10",
           R + "revision-r12.html")

p.pedido("Siento que la portada y la bolsa podrían mejorar. Me gustaría que la portada tenga algo más lifestyle, "
         "como que se vea el café con la tapa abierta y se note el cappuccino, y que sea el café mediano, con un "
         "sándwich ave palta, de manera que se vea mucho más atractivo. En la última slide de café + sándwich + dulce "
         "la bolsa también está mal diagramada. El logo tiene que verse más realista en perspectiva de la bolsa, "
         "igual en la portada. La última quiero que sea el café XL. La de opción dulce podría ser el mediano, como "
         "para que vayan variando los tamaños.", "Eli", "01-10")

p.comparar((A + "C1 n°1 togo S1.png", "mano con la bolsa"),
           (R + "C1 n°1 togo S1.png", "café mediano destapado + ave palta + bolsa"),
           titulo="n°1 · Portada",
           notas=("Qué cambió", [
               "<b>Más lifestyle</b>: una mano levanta el café <b>mediano destapado</b>, con el cappuccino y su latte art a la vista; "
               "la tapa queda sobre la mesa y al lado va el <b>sándwich ave palta</b> en dos triángulos.",
               "<b>Bolsa</b> blanca atrás, con el logo calzado en perspectiva (ver el detalle más abajo).",
               "⚠️ El pulgar tapa la «B» del logo del vaso (se lee «ƎTWEEN»). La marca se lee completa en la bolsa; si te "
               "molesta, tengo otra toma sin mano con el logo entero.",
           ]))
p.comparar((A + "C1 n°4 togo S1.png", "vaso alto"),
           (R + "C1 n°4 togo S1.png", "café mediano"),
           titulo="n°4 · Café + opción dulce", ancho=380,
           notas=("Qué cambió", ["Sólo el vaso: ahora es el <b>mediano</b> (más bajo, con el anillo blanco en la base). "
                                 "Vigilantes, muffin, brownie y papeles quedan donde estaban."]))
p.comparar((A + "C1 n°5 togo S1.png", "bolsa detrás del vaso, logo girado"),
           (R + "C1 n°5 togo S1.png", "café XL + bolsa despejada"),
           titulo="n°5 · Café + sándwich + dulce", detalle=(380, 420, 1060, 1180), escala=1.1,
           notas=("Qué cambió", [
               "<b>Café XL</b>, a la izquierda de la bolsa y sin taparla.",
               "<b>Bolsa rediagramada</b>: apaisada como la real, con la cara despejada; el muffin va delante de su parte baja "
               "y el sándwich adelante a la izquierda. Cada cosa con su espacio.",
               "<b>Logo en perspectiva</b>: antes sólo estaba girado; ahora se proyecta sobre las cuatro esquinas de la cara "
               "de la bolsa, así que fuga con ella y hereda su sombra y sus pliegues.",
               "El acento pasó a la tapa del vaso para no tocar la bolsa.",
           ]))
p.laminas([(R + f"C1 n°{k} togo S1.png", f"n°{k}") for k in range(1, 6)],
          titulo="El carrusel completo", ancho=300,
          notas=("Tamaños", [
              "Portada: <b>mediano</b> · n°2: los tres · n°3 café + sándwich: <b>sin tocar</b> (¿lo paso al Grande para que "
              "varíe del todo?) · n°4 dulce: <b>mediano</b> · n°5: <b>XL</b>.",
              "<b>Ya reemplazado en Drive</b> (S1/BW/FEED/C1 togo S1), las 5 con el mismo nombre y enlace, md5 = local.",
          ]))

p.pedido("Añadiría al inicio de cada texto un signo «*», de manera de que se aluda a que desde ahí inicia. Como un punteo.",
         "Eli", "01-10", titulo="Reel café de cumpleaños · el «*» del legal")
p.comparar((B + "oct-r11/BW FEED 02-10 Cafe de cumpleanos - PORTADA.png", "sin asterisco"),
           (R + "BW FEED 02-10 Cafe de cumpleanos - PORTADA.png", "con «*» en cada texto legal"),
           titulo="Reel · cierre", ancho=320, detalle=(140, 230, 1000, 760), escala=1.0,
           notas=("Qué cambió", [
               "«<b>*</b>Beneficio válido únicamente…» y «<b>*</b>Extras y personalizaciones no incluidas.»: un asterisco al inicio "
               "de cada uno de los dos textos legales (no en cada botón, porque los del medio son la continuación del primero).",
               "Nada más cambió: mismos tiempos y misma pista. <b>Ya reemplazado en Drive</b> (MP4 + GIF + PORTADA, md5 = local).",
           ]))
print(p.escribir())

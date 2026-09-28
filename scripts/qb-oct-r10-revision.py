#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 10 (Eli 28-09 tarde): ajustes de Eli sobre la ronda 9 —
tragos del AYCD en el carrusel, titular del Sunset como la aprobada, flores en la
palma, cumpleaños con Bell + íconos, mesa del pulpo limpia, marco de septiembre y
fotos más abajo en la dinámica.

    python scripts/qb-oct-r10-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/_antes-r9/"
N = "out/qb/oct/r9/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 10", "Tus ajustes a lo nuevo de la grilla",
           "28-09-2026 · 8 láminas corregidas", "out/qb/oct/r9/revision-r10.html",
           origen="scripts/qb-oct-r10-revision.py")
p.pedido("La portada de la G1 no es con los cócteles que van en el All You Can Drink… haz la misma foto de la "
         "referencia pero con un cóctel que va en el AYCD, y la G2 lo mismo, vista cenital o más bonita. En el "
         "Sunset, el texto igual a la referencia y más abajo, 5 px de espacio con el de 16 a 21 hrs, en puntas "
         "redondeadas y verde clarito de QB, y el legal más abajo. En el trago de autor, las flores en la palma. "
         "En el cumpleaños, Bell y Raleway, íconos como la referencia y detalles verdes en la torta. La ST del "
         "12-10 aprobada, con la leyenda centrada y la mesa más limpia. En la del 16-10, las líneas discontinuas "
         "más similares. Y en la dinámica, baja la imagen para colocar los textos.", "Eli", "28-09")

def par(archivo, titulo, que, notas, detalle=None, escala=1.3):
    p.comparar((A + archivo, "ronda 9"), (N + archivo, "ronda 10"), titulo=titulo, que=que,
               detalle=detalle, escala=escala, ancho=420, notas=("Qué cambió", notas))

par("C1 S1 N°1 QB OCT 26.png", "FEED 07-10 · AYCD · G1", "La foto de la referencia, con un trago del AYCD.",
    ["Antes eran tragos de la selección de dioses. Ahora es la escena de la ref (bartender sirviendo en la barra) "
     "preparando un Ramazzotti Rosato en su copa",
     "Tragos del AYCD según la ST aprobada de septiembre: schop, piscola, Ramazzotti, sangría y espumante",
     "Es generada → «Imagen referencial» chica al pie"])
par("C1 S1 N°2 QB OCT 26.png", "FEED 07-10 · AYCD · G2", "Los tragos del AYCD, más bonito.",
    ["Sangría, Ramazzotti, espumante, schop y piscola sobre la barra, con limón y menta",
     "La pedí en vista cenital y el generador la entregó en 3/4, que luce bien las copas con pie. "
     "Si la quieres estrictamente cenital (desde arriba), la genero de nuevo",
     "Franja de arriba más oscura para que «ALL YOU CAN DRINK» lea sobre la copa rosada"])
par("C1 S2 N°2 QB OCT 26.png", "FEED 12-10 · Sunset · G2", "El texto como el Sunset aprobado, más abajo.",
    ["Titular en Raleway fina grande con el interlineado apretado, como «TUS FAVORITOS AL MEJOR PRECIO». Va en 3 líneas porque la frase es más larga",
     "Pastilla a 5 px bajo el titular, redondeada, en el verde claro de QB (#66886B)",
     "Legal al pie, sobre la zona oscura"], detalle=(0, 850, 1080, 1350), escala=1.0)
par("Post n°1 S2 QB OCT 26.png", "FEED 16-10 · Trago de autor", "Las flores caen en la palma.",
    ["El vaso en los dedos y las tres flores (pensamiento amarillo, crisantemo y pensamiento morado) apoyadas en la palma"])
par("ST n°3 S1 QB OCT 26.png", "ST 07-10 · Cumpleaños", "Bell + Raleway, íconos y torta con verde QB.",
    ["«Convierte tu cumpleaños» en Bell MT y «en una noche inolvidable» en Raleway fina",
     "Cada beneficio en su línea con un ícono de línea fino, como los de ubicación y teléfono de la ref «CHEERS»: copa, shot, postre, cuenta y torta",
     "Torta con cinta verde QB, flores de azúcar verde salvia y servilleta verde"], detalle=(100, 500, 1000, 900), escala=1.2)
par("ST n°1 S2 QB OCT 26.png", "ST 12-10 · Pulpo ✅ aprobada", "Leyenda centrada y mesa limpia.",
    ["«Imagen referencial» centrada",
     "Mesa limpia: fuera las pintitas claras, las vetas anaranjadas y el nudo gris de la madera. Plato, copa y hojas intactos (se limpió sobre la misma foto, sin IA, porque la IA movía el plato)"],
    detalle=(0, 700, 1080, 1300), escala=1.0)
par("ST n°5 S2 QB OCT 26.png", "ST 16-10 · Primavera", "El filete punteado como el de septiembre.",
    ["Medido en la ST3-S3: trazo de 1,5 px, guion corto, verde menta claro",
     "El marco corrido a la izquierda de la copa: nace afuera y termina dentro de ella, como en «Afrodita»"],
    detalle=(300, 500, 1000, 1200), escala=1.2)
par("ST n°3 S4 QB OCT 26.png", "ST 28-10 · ¿Este o este?", "Las fotos más abajo, con la instrucción arriba.",
    ["Las fotos bajan 100 px y bajo el titular va «¿Cuál pedirías hoy? Vota en la encuesta»",
     "Queda el espacio de 1290 a 1450 para el sticker de ENCUESTA"])

p.notas(["<b>Cómo funciona «¿Este o este?»:</b> es una encuesta de Instagram. La CM pone el sticker de encuesta en el espacio bajo las fotos, con las dos opciones «Medusa» y «Perséfone». La gente vota con un toque (no tiene que escribir nada, por eso participa más que con la caja de preguntas). QB ve quién votó por cada uno y, entre los que votaron, sortea el premio sorpresa. Además sirve para saber qué trago gusta más.",
         "⚠️ El texto del premio sigue siendo propuesta: el brief decía «El primero en acertar gana un premio sorpresa». Hay que confirmarlo con contenido.",
         "Sin cambios: FEED 12-10 G1 (te gustó como quedó).",
         "QA de QB: 0 bloqueantes. Los 2 avisos son falsos positivos del spritz (desenfoque real y plantas leídas como croma).",
         "Nada subido a Drive todavía: con tu visto, lo subo."], titulo="Lo demás")
p.escribir()

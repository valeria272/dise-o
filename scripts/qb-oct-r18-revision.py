#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 18 (Eli 29-09): «haz algo similar en los otros legales de QB,
verifica que no se vean tan pequeños». Legal en UNA línea en todas las piezas de octubre,
al tamaño más grande que cabe (19 px con «Imagen referencial», 22 sin); el CMR 40 %,
que es el doble de largo, en dos líneas exactas a 21.

    python scripts/qb-oct-r18-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/r18/_antes/"
N = "out/qb/oct/r18/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 18", "Todos los legales en una línea",
           "29-09-2026 · 14 piezas · para revisar antes de subir a Drive", "out/qb/oct/r18/revision-r18.html",
           origen="scripts/qb-oct-r18-revision.py")
p.pedido("¿Puedes hacer algo similar en los otros legales de QB? Verifica que no se vean tan pequeños y me muestras.",
         "Eli", "29-09")

ST = (40, 1400, 1040, 1680)


def par(nombre, titulo, que, notas, detalle=ST):
    p.comparar((A + nombre + ".png", "antes"), (N + nombre + " QB OCT 26.png", "ahora"), titulo=titulo, que=que,
               detalle=detalle, escala=1.0, ancho=420, notas=("Qué cambió", notas))


L19 = "Legal en UNA línea a 19 px (con «Imagen referencial» es el tamaño más grande que cabe con 60 px de margen por lado)"
L22 = "Legal en UNA línea y más grande: de 19 a 22 px, el tamaño del CMR 08-10 que ya estaba aprobado"
par("ST n°1 S1", "ST 01-10 · Banco de Chile  (ST n°1 S1)", "De dos líneas a una.",
    ["Antes 22 px en dos líneas; ahora " + L19[0].lower() + L19[1:]])
par("ST n°2 S1", "ST 06-10 · All You Can Drink  (ST n°2 S1)", "De dos líneas a una.", [L19, "Sigue abajo, donde lo pediste en la ronda 16"])
par("ST n°5 S1", "ST 09-10 · Sunset QB  (ST n°5 S1)", "De dos líneas a una.", [L19, "Sigue abajo, donde lo pediste en la ronda 16"])
par("ST n°2 S3", "ST 20-10 · AYCD llamada  (ST n°2 S3)", "Más grande.", ["Estaba a 17 px, el más chico de octubre: ahora 19 px, en una línea"])
par("C1 S1 N°2", "FEED 07-10 · Carrusel AYCD · G2  (C1 S1 N°2)", "De dos líneas a una.", [L19], detalle=(40, 950, 1040, 1250))
par("C1 S2 N°2", "FEED 12-10 · Carrusel Sunset · G2  (C1 S2 N°2)", "Más grande.", [L22], detalle=(40, 1100, 1040, 1350))
par("ST n°2 S2", "ST 13-10 · All You Can Drink  (ST n°2 S2)", "De 18 a 19 px.",
    ["El legal que aprobaste en la ronda 17, un punto más grande (19 px) para quedar igual que los demás. Los tragos no cambian"])
par("ST n°2 S4", "ST 27-10 · All You Can Drink  (ST n°2 S4)", "Igual que la 13-10.",
    [L22, "La lista de tragos, como en la 13-10: 24 px, letra recta y en dos líneas parejas con «·»"])
for n, t in (("ST n°6 S2", "Sunset S2"), ("ST n°5 S3", "Sunset S3"), ("ST n°4 S4", "Sunset S4")):
    par(n, f"ST aprobada · {t}  ({n})", "Más grande.", [L22])
for n, t in (("ST n°7 S2", "CMR 40 % · 17-10"), ("ST n°6 S3", "CMR 40 % · 25-10"), ("ST n°5 S4", "CMR 40 % · 31-10")):
    par(n, f"ST aprobada · {t}  ({n})", "Más grande y en dos líneas exactas.",
        ["Este legal es el doble de largo (cuatro frases): en una línea quedaría a ~12 px, ilegible",
         "De 20 a 21 px, en dos líneas cortadas por frase: «Válido… con CMR. *Excluye compras con factura.» / «*No contempla tope de descuento. *Promoción no acumulable… beneficios.»"])

p.medido([
    ("Legal con «Imagen referencial» (~110 caracteres)", "19 px · 1 línea", "ok", "mide 935–945 px; columna de 960"),
    ("Legal sin «Imagen referencial» (~88 caracteres)", "22 px · 1 línea", "ok", "mide 892 px"),
    ("Legal del CMR 40 % (~165 caracteres)", "21 px · 2 líneas", "ok", "cierra a 1563 px, dentro de la zona segura"),
    ("Zona que cambió en cada pieza", "sólo el legal", "ok", "diferencia píxel a píxel contra lo entregado (y la lista de tragos en la 27-10)"),
], titulo="Lo medido (en px de 1080 × 1920)")
p.notas(["Sin cambios: el CMR 08-10 (ya estaba en una línea a 22 px), el estacionamiento 21-10 (su nota es información, no legal) y las piezas que sólo dicen «*Imagen referencial».",
         "⏸️ NADA subido a Drive todavía: con tu visto, reemplazo las 14 en su carpeta con el mismo nombre."], titulo="Lo demás")
p.escribir()

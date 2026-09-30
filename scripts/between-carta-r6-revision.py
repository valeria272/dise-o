#!/usr/bin/env python3
"""BETWEEN · carta oficial R6 (30-09-2026) — página de revisión para Eli: antes (R5) y ahora (R6).

    python scripts/between-carta-r6-revision.py
Salida: out/hilton/between/carta-oficial/r6/REVISAR-R6.html (se abre en Chrome)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/carta-oficial"
r5 = lambda op, n: f"{B}/r5/png/BW-CARTA-OFICIAL-R5-OP{op}-{n}.png"
r6 = lambda op, n: f"{B}/r6/png/BW-CARTA-OFICIAL-R6-OP{op}-{n}.png"
info = json.loads(Path(f"{B}/r6/paginas.json").read_text(encoding="utf-8"))

p = Pagina("between", "BETWEEN · CARTA OFICIAL · R6", "A, B nueva y D con las reglas de impreso",
           "30-09-2026 · parte de la R5 aprobada · formato 17 × 30 cm + 3 mm de sangrado por lado",
           f"{B}/r6/REVISAR-R6.html", origen="scripts/between-carta-oficial-r6.py")
p.pedido("Vamos a ir con la A, la D y vamos a hacer una opción como B… la A que está en fondo café sea "
         "con fondo beige y textos en café… el párrafo no tiene que solapar con los precios, tiene que "
         "existir un margen visual… que quede el mismo margen hacia abajo para todas las descripciones… "
         "los textos huérfanos… si en la primera tiene una letra I y en la segunda también al último… "
         "presiones Enter y dejes abajo la I… que las descripciones del producto sean un punto más "
         "pequeño que el título del producto… el fondo tiene que tener un excedente de 0,3 cm por lado",
         "Eli", "30-09-2026")

p.comparar((r5("A", 2), "R5: «Omelette… acompañado» corre bajo el precio"),
           (r6("A", 2), "R6: la descripción termina 4 mm antes de la columna de precios"),
           titulo="A · la descripción ya no pisa el precio", detalle=(740, 400, 1830, 1400),
           escala=0.8, lienzo=0,
           notas=("Qué cambió", ["El borde derecho de las descripciones es el MISMO en toda la sección: "
                                 "lo marca el precio más ancho de esa sección + 4 mm de aire.",
                                 "«y», «o», «e», «a» nunca cierran una línea: bajan pegadas a la palabra "
                                 "siguiente («…pechuga de pollo / y mayonesa»).",
                                 "Ningún párrafo termina con una palabra sola.",
                                 "Textos: sin cambios (sólo saltos de línea)."]))

p.laminas([(r6("B", n), f"B · hoja {n}") for n in range(1, info["B"]["paginas"] + 1)],
          titulo=f"B nueva · la A al revés · {info['B']['paginas']} hojas",
          que="Fondo beige con el papel de la casa; textos, filetes, logo y dibujos en café. "
              "«MAÑANA / ALMUERZO / BAR» en café aclarado (#8D8272), como el café claro de la A. "
              "Misma secuencia y mismas reglas que la A.")

p.comparar((r5("D", 4), "R5: la descripción de las ensaladas cruza bajo NORMAL y MINI"),
           (r6("D", 4), "R6: la descripción queda antes de los dos precios"),
           titulo="D · columnas con dos precios", detalle=(0, 300, 1929, 1800), escala=0.55, lienzo=0,
           notas=("Ojo, decisión tuya", [
               "En la D las columnas miden 67 mm: con dos precios la descripción queda en ~33 mm y se "
               "alarga (Ensalada Rainbow, 6 líneas). Por eso la D pasa de 5 a 6 hojas.",
               "Compacté la columna de precio (15,5 → 14 mm, lo justo para «$12.500») y dejé 2,5 mm entre "
               "los dos precios, que en la R6 aparecían pegados.",
               "Si prefieres menos líneas, la salida es que en la D la descripción pase bajo el PRIMER precio "
               "y sólo respete el último; no lo hice porque contradice la regla que me diste."]))

for op, nom in (("A", "A · café, índice lateral"), ("D", "D · portada partida, hojas alternadas")):
    p.laminas([(r6(op, n), f"{op} · hoja {n}") for n in range(1, info[op]["paginas"] + 1)],
              titulo=f"{nom} · {info[op]['paginas']} hojas")

p.medido([
    ("Descripción que pisa la columna del precio", "0 en A, B y D", "ok", "R5: casi todas las largas"),
    ("Párrafos con palabra sola en la última línea", "0", "ok", "control en cada hoja paginada"),
    ("Líneas que terminan en «y», «o», «e», «a», «u»", "0", "ok", "R5: varias por hoja"),
    ("Texto a menos de 10 mm del corte", "0", "ok", "margen de seguridad de imprenta"),
    ("Plato / descripción", "9,5 pt Bold / 8,5 pt Regular", "ok", "un punto menos, pedido"),
    ("Sangrado del fondo", "3 mm por lado (176 × 306 mm)", "ok", "PDF en «pdf-sangrado», TrimBox 170 × 300"),
    ("Hojas", f"A {info['A']['paginas']} · B {info['B']['paginas']} · D {info['D']['paginas']}", "ojo",
     "D sube de 5 a 6 por las descripciones angostas"),
])
p.escribir()

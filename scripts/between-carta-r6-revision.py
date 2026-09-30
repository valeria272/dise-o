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

p.pedido("Revisa que esté todo de acuerdo al Word que entregó el cliente. Revisa la ortografía… cuando se "
         "comienza un párrafo se comienza con mayúscula, y las que no son nombres de algo importante van en baja… "
         "chef sería en baja… cuando dice simple o doble… que los precios estén acorde a esa palabra, justificada "
         "hacia la izquierda… pollo veggie o filete… sándwich y burger y ensaladas y entradas se ven muy extraño, "
         "trata de que algunos textos queden en una sola línea… (es para todas las cartas)… Si una sección es de "
         "cafetería no puede estar la misma sección en otra página", "Eli", "30-09-2026", titulo="Segunda vuelta")

p.notas([
    "<b>Contra el Word del cliente:</b> todos los platos, en orden, y todos los precios coinciden. Las erratas del "
    "Word ya venían corregidas (Salmon → Salmón, manquilla → mantequilla, Muffinn, Colection, Kuntsmann, Cesar → César).",
    "Crema o sopa del día a elección del <b>chef</b> · Pasta del día… del <b>chef</b>",
    "Huevos fritos, tocino, <b>hotcake</b> con mantequilla y syrup",
    "Poroto verde, tomate <b>y</b> ají verde (sin la coma antes de «y»)",
    "Sabores disponibles: <b>pistacho</b>… · Acompañamiento a elección entre: <b>papas fritas</b>… "
    "(<b>agregados</b> no incluidos…) · Opciones de pan: <b>marraqueta / pan de campo</b>… (después de dos puntos, minúscula)",
    "Croissant blanco / <b>integral / molde blanco / molde integral / marraqueta</b>",
    "Tradicional, <b>menta, menta jengibre o berries</b> · Carmenere, <b>oporto, gin</b>, naranja y <b>syrup</b> especiado · "
    "Carmenere, <b>cabernet sauvignon, chardonnay, sauvignon blanc</b> (las cepas van en minúscula)",
    "5 und <b>rellenas</b> (concordancia con «5 und»)",
    "Galletitas <b>100 g</b> · Hamburguesa casera <b>100 g</b> (el símbolo del gramo es «g»)",
    "<b>Affogato</b> (el Word decía «Afogatto»)",
    "Se quedan con mayúscula por ser nombres propios: César, Calafate, Cáhuil, Between, Flat White, Golden Milk…",
    "<b>Pendiente tuyo:</b> «Elija 2 opciones» trata de usted y «Elige tu tamaño» de tú. No lo cambié porque es texto del cliente.",
], titulo="Ortografía y mayúsculas · lo que cambió en TEXTO")

p.comparar((r5("A", 3), "R5: SIMPLE / DOBLE cargados a la derecha, sin columna clara"),
           (r6("A", 3), "R6: cada precio parte del mismo borde izquierdo que su rótulo"),
           titulo="Columnas de precio alineadas con su rótulo", detalle=(740, 400, 1830, 1400), escala=0.8, lienzo=0,
           notas=("Qué cambió (en las tres opciones)", [
               "Simple/Doble, Croissant/Molde, Pollo·Veggie/Filete, Normal/Mini, Normal/Catedral: cada columna mide lo "
               "que su rótulo o su precio más ancho, y rótulo y precios parten del MISMO borde izquierdo.",
               "El precio único va en su columna (Ristretto → Simple, Sour Premium → Normal).",
               "Lo que viene después de un filete (Tostadas, Cheeseburger, Empanadas) ya no queda bajo «Molde», "
               "«Filete» o «Mini»: lleva su precio a la derecha, como cualquier plato.",
               "Si un rótulo ancho no deja caber el nombre del plato, el rótulo pasa a dos líneas («Molde /» sobre "
               "«Marraqueta»), en vez de partir el nombre."]))

p.comparar((r5("D", 1), "R5: rótulos de distinto ancho y alto, portada con columna de 63 mm"),
           (r6("D", 1), "R6: todos los rótulos a lo ancho de la columna, del mismo cuerpo"),
           titulo="D · rótulos de sección parejos", escala=0.55, lienzo=0,
           notas=("Qué cambió", [
               "Todos los rótulos en caja ocupan el ancho de la columna, a 11 pt ExtraBold, y quedan en UNA línea "
               "(Sándwich y burgers, Ensaladas y entradas, Complemento desayuno, Jugos, aguas y bebidas…). Sólo "
               "«Tentaciones de nuestra vitrina» no cabe ni cerrando el espaciado, así que va en dos.",
               "Portada: la columna de la carta pasa de 63 a 71 mm (con dos precios los nombres se partían todos) y el "
               "panel del logo se corre 8 mm. El logo queda un poco más chico (~57 mm de ancho).",
               "La D sigue en 5 hojas."]))

p.notas([
    "Ninguna sección cambia de hoja, en ninguna de las tres. Una sección larga puede seguir en la otra columna de la "
    "MISMA hoja (Complemento desayuno en la D); si no alcanza, parte entera en la hoja siguiente.",
    "Si por eso una hoja de dos columnas queda con la derecha vacía, la última sección pasa a la derecha para equilibrar.",
    "El script lo revisa solo en cada vuelta y avisa si algo se parte entre hojas.",
], titulo="Una sección, una hoja")

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
    ("Hojas", f"A {info['A']['paginas']} · B {info['B']['paginas']} · D {info['D']['paginas']}", "ok", "igual que la R5"),
    ("Secciones partidas entre hojas", "0", "ok", "regla de Eli 30-09"),
    ("Nombre a menos de 3 mm de su precio", "0", "ok", "control en cada fila"),
    ("Contenido y precios contra el Word", "coinciden", "ok", "Word corregido del cliente, 28-09"),
])
p.escribir()

#!/usr/bin/env python3
"""BETWEEN · CARTA OFICIAL Desayuno/Almuerzo 2026 — PROPUESTAS R1 (28-09-2026).

Ya no es el ejercicio interno (`between-carta-opciones-r*.py`): el cliente mandó el menú
corregido (Drive 1gAZNJkaw5SKAHEmLo1yIctD-MNCE1p6v, «Carta Between Des-Almuerzo 2026
(corregida).docx») y 3 referencias (Loká de óvalos, «Menú» con índice lateral y Bad Lobo).

Lo que dijo el cliente:
  · la ref es inspiración: algo MÁS LIMPIO, sin tanta ilustración, más líneas
  · propuestas diferentes: quizás una igual a la ref y otra con otra distribución,
    siempre con la lógica limpia
  · formato: el actual (17 × 30 cm)
  · un teaser de 3 páginas con la info enviada, para ver si queda justo, corto o largo
  · a diferencia de QB, la carta no destaca por ilustraciones: alguna en una esquina, no más;
    se puede jugar con leyendas
  · es la carta de mañana/almuerzo → cafés y beige

Las tres opciones (el contenido y el orden son los del Word; cambia la distribución):
  A · ÍNDICE LATERAL — la ref «Menú»: sección + notas a la izquierda, filete vertical,
      platos a la derecha. Fondo café, texto beige. Una ilustración chica por hoja, en la
      columna de índice, que es donde sobra aire.
  B · ÓVALOS A DOS COLUMNAS — la ref Loká: fondo beige, secciones en óvalo, dos columnas
      con filete al medio, leyenda al pie. Sin ilustración. Es la más densa.
  C · FRANJAS — otra distribución: secciones a lo ancho, título en Brushwell (lo que la
      separa de QB) con filete, listas cortas a 3 columnas; marco fino. Ilustración sólo
      en la portada.

Texto: literal del Word, salvo erratas evidentes (se reportan a Eli para confirmar) y los
precios, que el Word trae mezclados ($6,900 / $2.300) y aquí van todos con punto.

    python scripts/between-carta-oficial-r1.py [A B C]
Salida: out/hilton/between/carta-oficial/r1/{html,png,pdf}/  +  index.html comparativo
"""
import importlib.util, re, subprocess, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_s = importlib.util.spec_from_file_location(
    "r2", Path(__file__).with_name("between-carta-opciones-r2.py"))
r2 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(r2)
BEIGE, CAFE, R, BASE, u, CHROME = r2.BEIGE, r2.CAFE, r2.R, r2.BASE, r2.u, r2.CHROME
OUT = r2.RAIZ / "out/hilton/between/carta-oficial/r1"
C_ = r2.BW / "carta"
ILU = {k: u(C_ / f"ilu-{k}.png") for k in ("taza-croissant", "cafetera", "mano-taza", "desayuno-plato")}

# ═══════════════ CONTENIDO — Word corregido del cliente, 28-09-2026 ═══════════════
# sección: (título, [notas], [cabeceras de columnas de precio], [(plato, descripción, [precios])])
def S(titulo, items, notas=(), cols=()):
    return {"t": titulo, "notas": list(notas), "cols": list(cols), "items": items}


def I(nom, *precios, d=""):
    return (nom, d, list(precios))


HORARIO = [("Lunes a viernes", "08:00 a 22:00 hrs"), ("Cierre de cocina", "21:30 hrs"),
           ("Cierre de bar", "22:00 hrs"), ("Sábados, domingos y festivos", "Cerrado")]

SANDWICHES = S("Sándwiches y tostadas", [
    I("Salmón palta", "$6.900", "$5.900"),
    I("Ave palta", "$6.300", "$5.300"),
    I("Jamón queso", "$6.100", "$5.100"),
    I("Solo palta", "$6.100", "$5.100"),
    I("Huevo revuelto", "$6.000", "$5.000"),
    ("—",),
    I("Tostadas con palta", "$5.900", d="Tostadas, palta y mantequilla."),
    I("Tostadas a elección", "$5.500", d="Elija 2 opciones: mermelada o manjar o miel. Acompañado de mantequilla."),
], notas=["Croissant blanco / Integral / Molde blanco / Molde Integral / Marraqueta"],
   cols=["Croissant", "Molde / Marraqueta"])

VITRINA = S("Tentaciones de nuestra vitrina", [
    I("Yogurt con granola", "$5.500"), I("Fruta con miel", "$5.200"),
    I("Cheesecake / Torta a elección", "$4.900"), I("Strudel de manzana", "$4.700"),
    I("Kuchen / Pie", "$4.500"), I("Opciones sin azúcar", "$5.200"),
    I("Galletitas 100gr", "$3.900"), I("Brownie casero", "$2.900"),
    I("Muffin a elección", "$2.900"), I("Vigilantes con manjar 2 unidades", "$2.500"),
    I("Galletón chips y nueces", "$2.500"), I("Queque a elección", "$2.300"),
])

DESAYUNO = S("Desayuno", [
    I("Between", "$9.500", d="Pocillo de palta, jamón pierna y queso gouda. Pan a elección."),
    I("2727", "$9.500", d="Omelette relleno de jamón, queso y tomate, acompañado de lechuga. Pan a elección."),
    I("Buen día", "$8.500", d="Huevos revueltos o fritos. Pan a elección."),
    I("Good Morning", "$10.900", d="Huevos fritos, tocino, Hotcake con mantequilla y syrup."),
    I("Keto", "$10.500", d="Huevos fritos o revueltos, tocino, tomate tostado, palta y lechuga."),
    I("Bonjour", "$8.500", d="Croissant relleno de jamón y queso."),
], notas=["08:00 a 11:30 hrs",
          "Todos los desayunos incluyen jugo del día + opción de: café a elección, chocolate caliente, té o infusión.",
          "Opciones de pan: Marraqueta / Pan de campo / Tostadas blancas / Tostadas integrales."])

COMPLEMENTO = S("Complemento desayuno", [
    I("Refill de café (1 por cliente)", "$2.300"), I("Pocillo de palta", "$3.000"),
    I("Salmón ahumado (3 und)", "$3.000"), I("Prosciutto (3 und)", "$3.000"),
    I("2 huevos fritos o revueltos", "$3.000"), I("3 tostadas (blancas o integrales)", "$2.500"),
    I("Extra jamón y queso (2 und c/u)", "$3.000"), I("Extra jamón (3 und)", "$2.500"),
    I("Extra tocino (3 und)", "$2.000"), I("Extra queso (3 und)", "$2.000"),
    I("Vaso con fruta de la estación", "$2.000"), I("Vaso de yogurt con granola", "$2.000"),
    I("Miel o mermeladas", "$1.000"),
], notas=["Asociado a la compra de desayuno."])

CAFETERIA = S("Cafetería", [
    I("Ristretto", "$2.700"), I("Espresso", "$2.700", "$3.300"), I("Lungo", "$2.700"),
    I("Macchiato", "$2.900", "$3.500"), I("Americano", "$2.900", "$3.500"),
    I("Cortado", "$3.200", "$3.900"), I("Cappuccino", "$3.200", "$3.900"),
    I("Latte", "$3.400", "$4.300"), I("Latte sabor", "$3.700", "$4.600"),
    I("Moccaccino", "$3.700", "$4.600"), I("Flat White", "$3.900"),
    I("Latte Bombón", "$4.100"), I("Afogatto", "$3.900"), I("Café con helado", "$5.900"),
    I("Chocolate caliente", "$4.800"), I("Chai Masala", "$4.900"), I("Matcha Latte", "$4.700"),
    I("Golden Milk", "$4.700"), I("Té e Infusiones", "$3.200"), I("MilkShake", "$4.900"),
    I("Irish Coffee", "$4.900"),
], notas=["Sabores disponibles: Pistacho, dulce de leche, amaretto, vainilla, caramelo salado o avellana."],
   cols=["Simple", "Doble"])

ADICIONALES = S("Adicionales", [
    I("Leche de almendra", "$1.200"), I("Leche de soya", "$700"), I("Crema batida", "$700")])

JUGOS = S("Jugos, aguas y bebidas", [
    I("Jugo de fruta", "$3.700"), I("Bebidas", "$2.900"),
    I("Acqua Panna S/Gas", "$4.200"), I("San Pellegrino C/Gas", "$4.200"),
    I("Agua Porvenir S/Gas", "$2.900"), I("Agua Porvenir C/Gas", "$2.900")])

CARNES = S("Carnes, pescados y pastas", [
    I("Lomo liso a la plancha", "$16.900", d="Aderezado con sal de Cáhuil."),
    I("Salmón o pescado del día", "$15.500", d="Con salsa de mantequilla y alcaparras."),
    I("Plateada casera", "$14.500", d="Al vino tinto servida en su salsa."),
    I("Milanesa de res gratinada", "$13.900", d="Salsa de tomate, jamón y mozzarella."),
    I("Pechuga a la plancha", "$12.900", d="Salsa mostaza antigua y toques de miel."),
    I("Pasta del día", "$13.900", d="Pasta del día con salsa a elección del chef."),
], notas=["Acompañamiento a elección entre: Papas fritas, vegetales salteados, puré, arroz, "
          "ensalada de lechuga, tomate, palmito. (Agregados no incluidos en la pasta del día)."])

BURGERS = S("Sándwich y burgers", [
    I("Italiano", "$11.500", "$12.900", d="Palta molida, tomate y mayonesa."),
    I("Chacarero", "$11.500", "$12.900", d="Poroto verde, tomate, y ají verde."),
    I("Luco", "$11.100", "$12.500", d="Queso mantecoso fundido."),
    ("—",),
    I("Cheeseburger", "$12.900", d="Smash burger, queso cheddar, tocino, tomate, cebolla, pepinillo, lechuga y salsa BBQ."),
    I("Hamburguesa Italiana", "$12.500", d="Smash burger, palta, tomate y mayonesa."),
], notas=["Acompañados de papas fritas."], cols=["Pollo / Veggie", "Filete"])

EXTRAS = S("Extras", [I("Hamburguesa casera 100grs", "$3.500"), I("Tocino", "$2.000"),
                      I("Queso (cheddar/gouda)", "$2.000")])

ENSALADAS = S("Ensaladas y entradas", [
    I("Ensalada Between", "$12.500", "$7.500", d="Salmón ahumado y camarones, mix de hojas, tomate cherry, queso parmesano y almendras con dressing de yogurt."),
    I("Ensalada mexicana", "$12.300", "$7.400", d="Camarones y pollo, mix de hojas, palta, tomate, choclo, palmito y nachos con dressing de yogurt."),
    I("Palta reina", "$11.900", "$7.200", d="Palta rellena de pechuga de pollo y mayonesa, mix verde, ensalada chilena y aceitunas."),
    I("Ensalada César", "$11.500", "$6.900", d="Pechuga de pollo, mix de hojas, queso parmesano y crutones con dressing César."),
    I("Ensalada rainbow", "$11.500", "$6.900", d="Huevo duro o croqueta de porotos negros, mix de hojas, palta, tomate, pepino, zanahoria, poroto verde, frutos secos y limoneta."),
    ("—",),
    I("Empanada de lomo saltado", "$9.900", d="5 und rellena de carne, tomate y cebolla."),
    I("Empanadas de queso", "$9.500", d="5 und rellena de queso mantecoso."),
    I("Sopa del día", "$5.900", d="Crema o sopa del día a elección del Chef."),
], notas=["Elige tu tamaño"], cols=["Normal", "Mini"])

VEGGIE = S("Veggie", [
    I("Arroz chaufa", "$11.900", d="Arroz salteado con vegetales, champiñones, sésamo y palta."),
    I("Hamburguesa de poroto", "$11.900", d="Con guarnición a elección.")])

GUARNICIONES = S("Guarniciones", [
    I("Palta y palmito", "$5.500"), I("Lechuga, tomate y palmito", "$4.900"),
    I("Papas fritas, puré o vegetales", "$4.900"), I("Arroz blanco", "$4.500")])

POSTRES = S("Postres", [
    I("Brownie con helado", "$5.900", d="De chocolate con helado de vainilla."),
    I("Strudel con helado", "$5.900", d="Manzana canela con helado de vainilla."),
    I("Cheesecake o torta", "$4.900"), I("Fruta de la estación", "$4.900"),
    I("Kuchen o Pie", "$4.500"), I("Copa de helado", "$4.500"), I("Postre del día", "$4.200"),
    I("Opciones sin azúcar", "$5.200"), I("Galletitas 100gr", "$3.900")])

# ── lo que sigue en el Word es el bloque de bar (vinos, sin alcohol, spritz, sours, schop, botella):
#    se mide para estimar el total, no se diseña todavía.
RESTO_ITEMS = {"Vinos y espumantes": 5, "Bebidas sin alcohol": 7, "Spritz": 5, "Sours": 7,
               "Schop": 2, "Cerveza en botella": 3}


# ═══════════════ HTML común ═══════════════
def precios_html(pr, ncols):
    if ncols <= 1:
        return f'<span class="p">{pr[0]}</span>'
    celdas = pr + [""] * (ncols - len(pr))
    return '<span class="pp">' + "".join(f"<span>{c}</span>" for c in celdas) + "</span>"


def items_html(sec, reglas=False):
    n = len(sec["cols"]) or 1
    h = []
    for it in sec["items"]:
        if it == ("—",):
            h.append('<div class="corte"></div>')
            continue
        nom, d, pr = it
        # precio único en sección de dos columnas: va en la última (el plato no es
        # de ninguna de las dos variantes, p. ej. las tostadas o la Cheeseburger)
        if n > 1 and len(pr) == 1 and sec["t"] not in ("Cafetería",):
            pr = [""] * (n - 1) + pr
        dd = f'<div class="d">{d}</div>' if d else ""
        rg = '<div class="rg"></div>' if reglas else ""
        h.append(f'<div class="it{" cd" if d else ""}"><div class="f"><span class="n">{nom}</span>'
                 f'{precios_html(pr, n)}</div>{dd}{rg}</div>')
    return "".join(h)


def cabcols(sec):
    if len(sec["cols"]) < 2:
        return ""
    return ('<div class="cabcol">' + "".join(f"<span>{c}</span>" for c in sec["cols"]) + "</div>")


def notas_html(sec, desde=0):
    return "".join(f'<div class="nt">{n}</div>' for n in sec["notas"][desde:])


def logo(color, css):
    return r2.tinta(R["logo"], color, css)


def ilu(k, color, css, op=1):
    return r2.tinta(ILU[k], color, css + f";opacity:{op}")


PAPEL = (f'<div class="abs" style="inset:0;background:url(\'{R["papel"]}\') center/cover;'
         f'mix-blend-mode:multiply;opacity:{{op}}"></div>')

COMUN = """
.it{break-inside:avoid}
.it .f{display:flex;justify-content:space-between;align-items:baseline;gap:3mm}
.it .p{white-space:nowrap}
.it .pp{display:flex;white-space:nowrap}
.corte{height:0;border-top:.2mm solid currentColor;opacity:.3;margin:1.6mm 0 2.4mm}
.cabcol{display:flex;justify-content:flex-end;margin:0;font-size:5.8pt;font-weight:600;letter-spacing:.12em;
        text-transform:uppercase;opacity:.75;margin-bottom:1.6mm;line-height:1.15}
.nt{font-size:7pt;line-height:1.35;font-style:italic;opacity:.85}
.leyenda{font-size:6.2pt;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
"""
# chequeo de desborde: el render marca en el DOM toda caja que no alcance a contener su texto
CHEQUEO = """<script>addEventListener('load',()=>{const m=[];document.querySelectorAll('[data-caja]')
.forEach(e=>{if(e.scrollHeight>e.clientHeight+1)m.push(e.dataset.caja+':'+(e.scrollHeight-e.clientHeight))});
document.body.dataset.desborde=m.join(',')||'ok'})</script>"""


def pag(css, cuerpo):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{BASE}{COMUN}{css}</style>'
            f'</head><body><div class="hoja">{cuerpo}</div>{CHEQUEO}</body></html>')


# ═════════════ A · ÍNDICE LATERAL — ref «Menú» ═════════════
def op_a():
    IX, LX, TOP = 44, 62, 0   # ancho de la columna índice · x de la lista (mm)
    css = f"""
    .hoja{{background:{CAFE};color:{BEIGE}}}
    .fila{{display:grid;grid-template-columns:{IX}mm 1fr;column-gap:12mm;position:relative}}
    .fila+.fila{{margin-top:9mm}}
    .fila+.fila::before{{content:"";position:absolute;left:0;right:0;top:-3mm;height:.25mm;background:{BEIGE};opacity:.55;
                         -webkit-mask:linear-gradient(90deg,#000 {IX}mm,transparent {IX}mm,transparent {IX+12}mm,#000 {IX+12}mm);top:-4.5mm}}
    .ix h2{{font-weight:500;font-size:10.5pt;letter-spacing:.12em;text-transform:uppercase;line-height:1.25}}
    .ix .nt{{margin-top:2mm;font-size:6.9pt}}
    .ix .hr{{font-style:normal;font-weight:700;letter-spacing:.12em;font-size:7pt;opacity:1}}
    .it{{margin-bottom:3.5mm}}
    .it.cd{{margin-bottom:4.4mm}}
    .it .f{{font-size:9pt;font-weight:500;letter-spacing:.06em;text-transform:uppercase;line-height:1.2}}
    .it .p,.it .pp{{font-weight:600;letter-spacing:.02em}}
    .it .pp span{{min-width:17mm;text-align:right}}
    .cabcol span{{min-width:17mm;text-align:right}}
    .it .d{{font-size:7.5pt;line-height:1.36;opacity:.8;margin-top:.7mm;max-width:88%}}
    .vl{{position:absolute;width:.25mm;background:{BEIGE};opacity:.55}}
    """
    def fila(sec, extra_ix="", notas_desde=0, hora=None):
        hr = f'<div class="nt hr">{hora}</div>' if hora else ""
        return (f'<div class="fila"><div class="ix"><h2>{sec["t"]}</h2>{hr}{notas_html(sec, notas_desde)}{extra_ix}</div>'
                f'<div>{cabcols(sec)}{items_html(sec)}</div></div>')

    def cuerpo(top, filas, alto, clave):
        return (f'<div class="vl" style="left:{12+IX+6}mm;top:{top}mm;height:{alto}mm"></div>'
                f'<div class="abs" data-caja="{clave}" style="left:12mm;right:12mm;top:{top}mm;height:{alto}mm;overflow:hidden">{filas}</div>')

    hor = "".join(f'<div><b style="font-weight:700">{a}</b> · {b}</div>' for a, b in HORARIO)
    p1 = f"""
    {logo(BEIGE, 'left:11mm;top:13mm;width:62mm;height:20mm;-webkit-mask-position:left center')}
    <div class="abs" style="right:12mm;top:14mm;text-align:right;font-size:6.6pt;letter-spacing:.1em;text-transform:uppercase;line-height:1.75">{hor}</div>
    <div class="abs" style="left:0;right:0;top:44mm;height:.3mm;background:{BEIGE};opacity:.8"></div>
    {cuerpo(52, fila(SANDWICHES) + fila(VITRINA, ilu('mano-taza', BEIGE, 'position:relative;margin-top:14mm;width:40mm;height:42mm', .5)), 236, 'A1')}"""
    p2 = f"""
    {logo(BEIGE, 'left:12mm;top:12mm;width:30mm;height:9mm;-webkit-mask-position:left center')}
    <div class="abs leyenda" style="right:12mm;top:15mm">Mañana</div>
    <div class="abs" style="left:0;right:0;top:27mm;height:.3mm;background:{BEIGE};opacity:.8"></div>
    {cuerpo(35, fila(DESAYUNO, notas_desde=1, hora=DESAYUNO['notas'][0], extra_ix=ilu('desayuno-plato', BEIGE, 'position:relative;margin-top:10mm;width:40mm;height:34mm', .5)) + fila(COMPLEMENTO), 253, 'A2')}"""
    p3 = f"""
    {logo(BEIGE, 'left:12mm;top:12mm;width:30mm;height:9mm;-webkit-mask-position:left center')}
    <div class="abs leyenda" style="right:12mm;top:15mm">Mañana</div>
    <div class="abs" style="left:0;right:0;top:27mm;height:.3mm;background:{BEIGE};opacity:.8"></div>
    {cuerpo(35, fila(CAFETERIA, extra_ix=ilu('cafetera', BEIGE, 'position:relative;margin-top:12mm;width:30mm;height:40mm', .5)) + fila(ADICIONALES) + fila(JUGOS), 253, 'A3')}"""
    return [pag(css, p) for p in (p1, p2, p3)]


# ═════════════ B · ÓVALOS A DOS COLUMNAS — ref Loká ═════════════
def op_b():
    css = f"""
    .hoja{{background:{BEIGE};color:{CAFE}}}
    .col{{position:absolute;overflow:hidden}}
    .ov{{display:inline-block;border:.3mm solid currentColor;border-radius:50%;padding:1.9mm 6mm 1.7mm;
         font-weight:600;font-size:7.6pt;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap}}
    .ov.largo{{font-size:6.8pt;letter-spacing:.1em;padding:1.9mm 4.5mm 1.7mm}}
    .sb{{margin-bottom:6.5mm}}
    .sb .cab{{margin-bottom:3.2mm}}
    .sb .nt{{margin:-1mm 0 2.6mm;font-size:6.8pt}}
    .it{{margin-bottom:2.1mm}}
    .it.cd{{margin-bottom:2.8mm}}
    .it .f{{font-size:8.2pt;font-weight:500;letter-spacing:.05em;text-transform:uppercase;line-height:1.2}}
    .it .p,.it .pp{{font-weight:600}}
    .it .pp span{{min-width:15mm;text-align:right}}
    .cabcol span{{min-width:15mm;text-align:right}}
    .it .d{{font-size:6.9pt;line-height:1.3;opacity:.78;margin-top:.5mm;max-width:90%}}
    .vl{{position:absolute;left:50%;width:.25mm;background:{CAFE};opacity:.45}}
    .pie{{position:absolute;left:12mm;right:12mm;bottom:10mm;text-align:center}}
    .pie .l{{height:.25mm;background:{CAFE};opacity:.45;margin-bottom:3mm}}
    """
    def bloque(sec, notas_desde=0, hora=None):
        hr = f'<div class="nt" style="font-style:normal;font-weight:700;letter-spacing:.12em;opacity:1;margin-bottom:1.4mm">{hora.upper()}</div>' if hora else ""
        return (f'<div class="sb"><div class="cab"><span class="ov{' largo' if len(sec['t']) > 24 else ''}">{sec["t"]}</span></div>{hr}{notas_html(sec, notas_desde)}'
                f'{cabcols(sec)}{items_html(sec)}</div>')

    def dos(top, izq, der, clave, bottom=24):
        alto = 300 - top - bottom
        return (f'<div class="vl" style="top:{top}mm;height:{alto - 4}mm"></div>'
                f'<div class="col" data-caja="{clave}i" style="left:12mm;width:67mm;top:{top}mm;height:{alto}mm">{izq}</div>'
                f'<div class="col" data-caja="{clave}d" style="right:12mm;width:67mm;top:{top}mm;height:{alto}mm">{der}</div>')

    def pie(txt):
        return f'<div class="pie"><div class="l"></div><div class="leyenda">{txt}</div></div>'

    ley = "Cierre de cocina 21:30 hrs · Cierre de bar 22:00 hrs · Sábados, domingos y festivos cerrado"
    p1 = f"""{PAPEL.format(op=.55)}
    {logo(CAFE, 'left:0;right:0;top:14mm;height:19mm')}
    <div class="abs" style="left:0;right:0;top:38mm;text-align:center"><span class="ov">Lunes a viernes · 08:00 a 22:00 hrs</span></div>
    {dos(56, bloque(SANDWICHES) + bloque(VITRINA), bloque(DESAYUNO, 1, DESAYUNO['notas'][0]) + bloque(COMPLEMENTO), 'B1')}
    {pie(ley)}"""
    p2 = f"""{PAPEL.format(op=.55)}
    {logo(CAFE, 'left:0;right:0;top:12mm;height:9mm')}
    {dos(30, bloque(CAFETERIA) + bloque(ADICIONALES) + bloque(JUGOS),
         '<div class="sb" style="margin-bottom:4mm"><div class="leyenda" style="font-size:7pt">Almuerzo ejecutivo · 12:00 a 16:00 hrs</div></div>'
         + bloque(CARNES) + bloque(BURGERS) + bloque(EXTRAS), 'B2')}
    {pie(ley)}"""
    p3 = f"""{PAPEL.format(op=.55)}
    {logo(CAFE, 'left:0;right:0;top:12mm;height:9mm')}
    {dos(30, bloque(ENSALADAS) + bloque(VEGGIE), bloque(GUARNICIONES) + bloque(POSTRES), 'B3')}
    {pie(ley)}"""
    return [pag(css, p) for p in (p1, p2, p3)]


# ═════════════ C · FRANJAS — otra distribución ═════════════
def op_c():
    css = f"""
    .hoja{{background:{BEIGE};color:{CAFE}}}
    .marco{{position:absolute;inset:6mm;border:.25mm solid {CAFE};opacity:.6}}
    .fr{{margin-bottom:7mm}}
    .fr .cab{{display:flex;align-items:baseline;gap:4mm;margin-bottom:3.4mm}}
    .fr .cab h2{{font-family:Brushwell;font-weight:400;font-size:21pt;letter-spacing:.03em;line-height:1;white-space:nowrap}}
    .fr .cab .l{{flex:1;height:.25mm;background:{CAFE};opacity:.6;transform:translateY(-1.2mm)}}
    .fr .cab .hr{{font-size:6.8pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase;white-space:nowrap}}
    .fr .nt{{margin:-1.4mm 0 2.8mm;font-size:6.8pt}}
    .g2{{display:grid;grid-template-columns:1fr 1fr;column-gap:9mm}}
    .g3{{display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:7mm}}
    .it{{margin-bottom:2.2mm}}
    .it.cd{{margin-bottom:2.8mm}}
    .it .f{{font-size:8.4pt;font-weight:700;line-height:1.2}}
    .g3 .it .f{{font-size:7.8pt;font-weight:600}}
    .it .pp span{{min-width:13mm;text-align:right}}
    .cabcol span{{min-width:13mm;text-align:right}}
    .it .d{{font-size:6.9pt;line-height:1.3;opacity:.78;margin-top:.4mm;max-width:92%}}
    """
    def franja(sec, grilla="g2", hora=None, notas_desde=0, partir=None):
        hr = f'<span class="hr">{hora}</span>' if hora else ""
        its = sec["items"]
        n = {"g2": 2, "g3": 3}[grilla]
        if partir is None:
            k = -(-len(its) // n)
            partes = [its[i * k:(i + 1) * k] for i in range(n)]
        else:
            partes, a = [], 0
            for b in partir + [len(its)]:
                partes.append(its[a:b]); a = b
        def col(p):
            p = [x for x in p if x != ("—",)]
            dual = any(len(x[2]) > 1 for x in p)
            sub = dict(sec, items=p, cols=sec["cols"] if dual else [])
            # sin cabecera propia, se deja el hueco para que las columnas partan parejas
            hueco = cabcols(sec).replace('class="cabcol"', 'class="cabcol" style="visibility:hidden"') if sec["cols"] and not dual else ""
            return f'<div>{cabcols(sub) or hueco}{items_html(sub)}</div>'
        cols = "".join(col(p) for p in partes)
        return (f'<div class="fr"><div class="cab"><h2>{sec["t"]}</h2><div class="l"></div>{hr}</div>'
                f'{notas_html(sec, notas_desde)}<div class="{grilla}">{cols}</div></div>')

    def cuerpo(top, html, clave, bottom=14):
        return f'<div class="abs" data-caja="{clave}" style="left:13mm;right:13mm;top:{top}mm;height:{300-top-bottom}mm;overflow:hidden">{html}</div>'

    hor = " · ".join(f"{a} {b}" for a, b in HORARIO[:1])
    p1 = f"""{PAPEL.format(op=.55)}<div class="marco"></div>
    {logo(CAFE, 'left:13mm;top:16mm;width:58mm;height:18mm;-webkit-mask-position:left center')}
    <div class="abs" style="right:13mm;top:16mm;text-align:right;font-size:6.6pt;letter-spacing:.12em;text-transform:uppercase;line-height:1.75">
      {"".join(f'<div><b style="font-weight:700">{a}</b> · {b}</div>' for a, b in HORARIO)}</div>
    {cuerpo(46, franja(SANDWICHES, partir=[5]) + franja(VITRINA, 'g3') + franja(DESAYUNO, hora=DESAYUNO['notas'][0], notas_desde=1), 'C1', 40)}
    {ilu('taza-croissant', CAFE, 'right:12mm;bottom:11mm;width:40mm;height:27mm', .55)}"""
    p2 = f"""{PAPEL.format(op=.55)}<div class="marco"></div>
    {logo(CAFE, 'left:0;right:0;top:12mm;height:9mm')}
    {cuerpo(28, franja(COMPLEMENTO) + franja(CAFETERIA, 'g3', partir=[10, 16]) + franja(ADICIONALES, 'g3') + franja(JUGOS, 'g3') + franja(CARNES, hora='Almuerzo ejecutivo · 12:00 a 16:00 hrs'), 'C2')}"""
    p3 = f"""{PAPEL.format(op=.55)}<div class="marco"></div>
    {logo(CAFE, 'left:0;right:0;top:12mm;height:9mm')}
    {cuerpo(28, franja(BURGERS, partir=[3]) + franja(EXTRAS, 'g3') + franja(ENSALADAS, partir=[5]) + franja(VEGGIE) + franja(GUARNICIONES), 'C3')}"""
    return [pag(css, p) for p in (p1, p2, p3)]


OPCIONES = {"A": op_a, "B": op_b, "C": op_c}


def render(h, png, pdf):
    base = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--allow-file-access-from-files", "--virtual-time-budget=4000"]
    subprocess.run(base + ["--force-device-scale-factor=3", "--window-size=643,1134",
                           f"--screenshot={png}", h.as_uri()], check=True, capture_output=True)
    subprocess.run(base + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", h.as_uri()],
                   check=True, capture_output=True)
    dom = subprocess.run(base + ["--dump-dom", h.as_uri()], capture_output=True, text=True,
                         encoding="utf-8").stdout
    m = re.search(r'data-desborde="([^"]*)"', dom)
    return m.group(1) if m else "?"


def main():
    for d in ("html", "png", "pdf"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    for k in (sys.argv[1:] or list(OPCIONES)):
        for i, html in enumerate(OPCIONES[k](), 1):
            n = f"BW-CARTA-OFICIAL-R1-OP{k}-{i}"
            h = OUT / "html" / f"{n}.html"
            h.write_text(html, encoding="utf-8")
            print(("✓" if (r := render(h, OUT / "png" / f"{n}.png", OUT / "pdf" / f"{n}.pdf")) == "ok" else "⚠"), n, r)


if __name__ == "__main__":
    main()

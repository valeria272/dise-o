#!/usr/bin/env python3
"""BETWEEN · CARTA OFICIAL Desayuno/Almuerzo 2026 — PROPUESTAS R3 (28-09-2026).

Comentarios de Eli sobre la R2 (`between-carta-oficial-r2.py`, que queda de registro):
  PARA TODAS
  · mejorar jerarquías y TAMAÑOS MÍNIMOS: que se lea sin problema a la vista. Nombres de
    plato más en negrita, descripciones en regular, lo importante marcado
      → escala nueva: plato 9–9,5 pt Bold · descripción 8 pt Regular · notas 7,8 pt ·
        cabeceras de columna 6,8 pt · leyenda 7 pt (en la R2 había 5,8–6,9 pt)
  · párrafos sin palabras sueltas en la última línea → `text-wrap: pretty`
  · que no se corten letras (la J de «Jugos» en la C) → cajas con holgura a los lados
  · al final van los editables
  · la SECUENCIA se respeta hoja a hoja → PAGINADOR: el contenido corre en el orden del
    Word, columna a columna y hoja a hoja; una sección de ≤ 8 platos no se parte, una
    más larga se parte con al menos 3 platos por lado. Como corre la carta ENTERA (bar
    incluido), la cuenta de hojas ya no es estimada: es la real.
  A · «MAÑANA» sin miedo: grande, en una esquina, en un matiz del café al 75 %
      (75 % beige + 25 % café = #D9D2C3). Ilustraciones más grandes y bonitas; una que
      diga «vitrina» (campana de vidrio, mano-vitrina2.png); la de cafetería se queda
  B · ojo con tamaños, jerarquía y diagramación; las ilustraciones se quedan
  C · tamaños mínimos; la J cortada
  D · ilustraciones menos difuminadas: sólo degradé, sutil, y un poco más grandes.
      Secciones en RECTÁNGULO (no óvalo): beige con texto café sobre café, y al revés.
      Hojas alternadas café / beige / café… Portada con contactos (Instagram, web)

    python scripts/between-carta-oficial-r3.py [A B C D]
Salida: out/hilton/between/carta-oficial/r3/{html,png,pdf}/ + index.html
"""
import importlib.util, json, re, subprocess, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_s = importlib.util.spec_from_file_location(
    "r2", Path(__file__).with_name("between-carta-opciones-r2.py"))
r2 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(r2)
BEIGE, CAFE, R, BASE, u, CHROME, tinta = r2.BEIGE, r2.CAFE, r2.R, r2.BASE, r2.u, r2.CHROME, r2.tinta
OUT = r2.RAIZ / "out/hilton/between/carta-oficial/r3"
C_ = r2.BW / "carta"
ILU = {k: u(C_ / f"mano-{k}.png") for k in ("vitrina", "vitrina2", "desayuno", "cafeteria", "almuerzo", "ensalada")}
FILETE = ".15mm"
CLARO75 = "#D9D2C3"   # A: 75 % beige + 25 % café
CONTACTO = [("Instagram", "@between.coffeebar"), ("Web", "cafeteriabetween.cl")]

# ═══════════════ CONTENIDO — Word corregido del cliente, 28-09-2026 ═══════════════
def S(t, items, notas=(), cols=(), tramo="Mañana", hora="", unico="ultima"):
    return {"t": t, "items": items, "notas": list(notas), "cols": list(cols),
            "tramo": tramo, "hora": hora, "unico": unico}


def I(nom, *precios, d=""):
    return (nom, d, list(precios))


CORTE = ("—",)
HORARIO = [("Lunes a viernes", "08:00 a 22:00 hrs"), ("Cierre de cocina", "21:30 hrs"),
           ("Cierre de bar", "22:00 hrs"), ("Sábados, domingos y festivos", "Cerrado")]
LEYENDA = "Cierre de cocina 21:30 hrs · Cierre de bar 22:00 hrs · Sábados, domingos y festivos cerrado"
ALM = "Almuerzo ejecutivo · 12:00 a 16:00 hrs"

SEC = {}
SEC["sandwiches"] = S("Sándwiches y tostadas", [
    I("Salmón palta", "$6.900", "$5.900"), I("Ave palta", "$6.300", "$5.300"),
    I("Jamón queso", "$6.100", "$5.100"), I("Solo palta", "$6.100", "$5.100"),
    I("Huevo revuelto", "$6.000", "$5.000"), CORTE,
    I("Tostadas con palta", "$5.900", d="Tostadas, palta y mantequilla."),
    I("Tostadas a elección", "$5.500", d="Elija 2 opciones: mermelada o manjar o miel. Acompañado de mantequilla."),
], notas=["Croissant blanco / Integral / Molde blanco / Molde Integral / Marraqueta"],
   cols=["Croissant", "Molde / Marraqueta"])
SEC["vitrina"] = S("Tentaciones de nuestra vitrina", [
    I("Yogurt con granola", "$5.500"), I("Fruta con miel", "$5.200"),
    I("Cheesecake / Torta a elección", "$4.900"), I("Strudel de manzana", "$4.700"),
    I("Kuchen / Pie", "$4.500"), I("Opciones sin azúcar", "$5.200"),
    I("Galletitas 100gr", "$3.900"), I("Brownie casero", "$2.900"),
    I("Muffin a elección", "$2.900"), I("Vigilantes con manjar 2 unidades", "$2.500"),
    I("Galletón chips y nueces", "$2.500"), I("Queque a elección", "$2.300")])
SEC["desayuno"] = S("Desayuno", [
    I("Between", "$9.500", d="Pocillo de palta, jamón pierna y queso gouda. Pan a elección."),
    I("2727", "$9.500", d="Omelette relleno de jamón, queso y tomate, acompañado de lechuga. Pan a elección."),
    I("Buen día", "$8.500", d="Huevos revueltos o fritos. Pan a elección."),
    I("Good Morning", "$10.900", d="Huevos fritos, tocino, Hotcake con mantequilla y syrup."),
    I("Keto", "$10.500", d="Huevos fritos o revueltos, tocino, tomate tostado, palta y lechuga."),
    I("Bonjour", "$8.500", d="Croissant relleno de jamón y queso."),
], hora="08:00 a 11:30 hrs",
   notas=["Todos los desayunos incluyen jugo del día + opción de: café a elección, chocolate caliente, té o infusión.",
          "Opciones de pan: Marraqueta / Pan de campo / Tostadas blancas / Tostadas integrales."])
SEC["complemento"] = S("Complemento desayuno", [
    I("Refill de café (1 por cliente)", "$2.300"), I("Pocillo de palta", "$3.000"),
    I("Salmón ahumado (3 und)", "$3.000"), I("Prosciutto (3 und)", "$3.000"),
    I("2 huevos fritos o revueltos", "$3.000"), I("3 tostadas (blancas o integrales)", "$2.500"),
    I("Extra jamón y queso (2 und c/u)", "$3.000"), I("Extra jamón (3 und)", "$2.500"),
    I("Extra tocino (3 und)", "$2.000"), I("Extra queso (3 und)", "$2.000"),
    I("Vaso con fruta de la estación", "$2.000"), I("Vaso de yogurt con granola", "$2.000"),
    I("Miel o mermeladas", "$1.000")], notas=["Asociado a la compra de desayuno."])
SEC["cafeteria"] = S("Cafetería", [
    I("Ristretto", "$2.700"), I("Espresso", "$2.700", "$3.300"), I("Lungo", "$2.700"),
    I("Macchiato", "$2.900", "$3.500"), I("Americano", "$2.900", "$3.500"),
    I("Cortado", "$3.200", "$3.900"), I("Cappuccino", "$3.200", "$3.900"),
    I("Latte", "$3.400", "$4.300"), I("Latte sabor", "$3.700", "$4.600"),
    I("Moccaccino", "$3.700", "$4.600"), I("Flat White", "$3.900"),
    I("Latte Bombón", "$4.100"), I("Afogatto", "$3.900"), I("Café con helado", "$5.900"),
    I("Chocolate caliente", "$4.800"), I("Chai Masala", "$4.900"), I("Matcha Latte", "$4.700"),
    I("Golden Milk", "$4.700"), I("Té e Infusiones", "$3.200"), I("MilkShake", "$4.900"),
    I("Irish Coffee", "$4.900")],
    notas=["Sabores disponibles: Pistacho, dulce de leche, amaretto, vainilla, caramelo salado o avellana."],
    cols=["Simple", "Doble"], unico="primera")
SEC["adicionales"] = S("Adicionales", [
    I("Leche de almendra", "$1.200"), I("Leche de soya", "$700"), I("Crema batida", "$700")])
SEC["jugos"] = S("Jugos, aguas y bebidas", [
    I("Jugo de fruta", "$3.700"), I("Bebidas", "$2.900"),
    I("Acqua Panna S/Gas", "$4.200"), I("San Pellegrino C/Gas", "$4.200"),
    I("Agua Porvenir S/Gas", "$2.900"), I("Agua Porvenir C/Gas", "$2.900")])
SEC["carnes"] = S("Carnes, pescados y pastas", [
    I("Lomo liso a la plancha", "$16.900", d="Aderezado con sal de Cáhuil."),
    I("Salmón o pescado del día", "$15.500", d="Con salsa de mantequilla y alcaparras."),
    I("Plateada casera", "$14.500", d="Al vino tinto servida en su salsa."),
    I("Milanesa de res gratinada", "$13.900", d="Salsa de tomate, jamón y mozzarella."),
    I("Pechuga a la plancha", "$12.900", d="Salsa mostaza antigua y toques de miel."),
    I("Pasta del día", "$13.900", d="Pasta del día con salsa a elección del chef."),
], notas=["Acompañamiento a elección entre: Papas fritas, vegetales salteados, puré, arroz, "
          "ensalada de lechuga, tomate, palmito. (Agregados no incluidos en la pasta del día)."],
   tramo="Almuerzo", hora=ALM)
SEC["burgers"] = S("Sándwich y burgers", [
    I("Italiano", "$11.500", "$12.900", d="Palta molida, tomate y mayonesa."),
    I("Chacarero", "$11.500", "$12.900", d="Poroto verde, tomate, y ají verde."),
    I("Luco", "$11.100", "$12.500", d="Queso mantecoso fundido."), CORTE,
    I("Cheeseburger", "$12.900", d="Smash burger, queso cheddar, tocino, tomate, cebolla, pepinillo, lechuga y salsa BBQ."),
    I("Hamburguesa Italiana", "$12.500", d="Smash burger, palta, tomate y mayonesa."),
], notas=["Acompañados de papas fritas."], cols=["Pollo / Veggie", "Filete"], tramo="Almuerzo")
SEC["extras"] = S("Extras", [I("Hamburguesa casera 100grs", "$3.500"), I("Tocino", "$2.000"),
                             I("Queso (cheddar/gouda)", "$2.000")], tramo="Almuerzo")
SEC["ensaladas"] = S("Ensaladas y entradas", [
    I("Ensalada Between", "$12.500", "$7.500", d="Salmón ahumado y camarones, mix de hojas, tomate cherry, queso parmesano y almendras con dressing de yogurt."),
    I("Ensalada mexicana", "$12.300", "$7.400", d="Camarones y pollo, mix de hojas, palta, tomate, choclo, palmito y nachos con dressing de yogurt."),
    I("Palta reina", "$11.900", "$7.200", d="Palta rellena de pechuga de pollo y mayonesa, mix verde, ensalada chilena y aceitunas."),
    I("Ensalada César", "$11.500", "$6.900", d="Pechuga de pollo, mix de hojas, queso parmesano y crutones con dressing César."),
    I("Ensalada rainbow", "$11.500", "$6.900", d="Huevo duro o croqueta de porotos negros, mix de hojas, palta, tomate, pepino, zanahoria, poroto verde, frutos secos y limoneta."),
    CORTE,
    I("Empanada de lomo saltado", "$9.900", d="5 und rellena de carne, tomate y cebolla."),
    I("Empanadas de queso", "$9.500", d="5 und rellena de queso mantecoso."),
    I("Sopa del día", "$5.900", d="Crema o sopa del día a elección del Chef."),
], notas=["Elige tu tamaño"], cols=["Normal", "Mini"], tramo="Almuerzo")
SEC["veggie"] = S("Veggie", [
    I("Arroz chaufa", "$11.900", d="Arroz salteado con vegetales, champiñones, sésamo y palta."),
    I("Hamburguesa de poroto", "$11.900", d="Con guarnición a elección.")], tramo="Almuerzo")
SEC["guarniciones"] = S("Guarniciones", [
    I("Palta y palmito", "$5.500"), I("Lechuga, tomate y palmito", "$4.900"),
    I("Papas fritas, puré o vegetales", "$4.900"), I("Arroz blanco", "$4.500")], tramo="Almuerzo")
SEC["postres"] = S("Postres", [
    I("Brownie con helado", "$5.900", d="De chocolate con helado de vainilla."),
    I("Strudel con helado", "$5.900", d="Manzana canela con helado de vainilla."),
    I("Cheesecake o torta", "$4.900"), I("Fruta de la estación", "$4.900"),
    I("Kuchen o Pie", "$4.500"), I("Copa de helado", "$4.500"), I("Postre del día", "$4.200"),
    I("Opciones sin azúcar", "$5.200"), I("Galletitas 100gr", "$3.900")], tramo="Almuerzo")
SEC["vinos"] = S("Vinos y espumantes", [
    I("Ensamblaje Coyam", "$7.500"), I("Carmenere Founders Collection", "$6.500"),
    I("Cabernet Sauvignon 1865", "$6.500"),
    I("Veramonte Gran Reserva", "$5.500", d="Carmenere, Cabernet Sauvignon, Chardonnay, Sauvignon Blanc."),
    I("Espumante Brut", "$4.900")], tramo="Bar")
SEC["sinalcohol"] = S("Bebidas sin alcohol", [
    I("Spring Garden", "$7.300", d="Frutilla, menta, limón, syrup de especias y soda."),
    I("Green Bloom", "$7.300", d="Pepino, limón, jazmín, syrup de albahaca y soda."),
    I("Limonada", "$3.900", d="Tradicional, Menta, Menta Jengibre o Berries."),
    I("Jugo de fruta", "$3.700"), I("Acqua Panna S/Gas", "$4.200"), I("San Pellegrino C/Gas", "$4.200"),
    I("Agua Porvenir S/Gas", "$2.900"), I("Agua Porvenir C/Gas", "$2.900"), I("Bebidas", "$2.900")],
    tramo="Bar")
SEC["spritz"] = S("Spritz", [I("Aperol", "$7.500"), I("Ramazzotti", "$7.500"), I("St. Germain", "$9.900"),
                             I("Chambord", "$7.900"), I("Limoncello", "$7.500")], tramo="Bar")
SEC["sours"] = S("Sours", [
    I("Sour Premium", "$9.500"), I("Pisco Sour", "$5.500", "$9.900"), I("Sour Peruano", "$6.500", "$11.900"),
    I("Disaronno Sour", "$7.200"), I("Whisky Sour", "$6.700"), I("Chardonnay Sour", "$5.300"),
    I("Loica Sour", "$7.900", d="Carmenere, Oporto, Gin, naranja y Syrup especiado."),
], notas=["Tradicional, mango, maracuyá o berries."], cols=["Normal", "Catedral"], tramo="Bar", unico="primera")
SEC["schop"] = S("Schop", [I("Schop Austral Calafate", "$5.800"), I("Schop Heineken", "$5.200")], tramo="Bar")
SEC["botella"] = S("Cerveza en botella", [
    I("Kunstmann", "$4.300", d="Torobayo, lager o sin alcohol."), I("Austral", "$4.300", d="Lager o Calafate."),
    I("Heineken", "$3.900", d="Clásica o 0,0.")], tramo="Bar")
ORDEN = ["sandwiches", "vitrina", "desayuno", "complemento", "cafeteria", "adicionales", "jugos",
         "carnes", "burgers", "extras", "ensaladas", "veggie", "guarniciones", "postres",
         "vinos", "sinalcohol", "spritz", "sours", "schop", "botella"]


# ═══════════════ HTML común ═══════════════
def precios(pr, n, unico):
    if n <= 1:
        return f'<span class="p">{pr[0]}</span>'
    if len(pr) == 1:
        if unico != "primera":
            return f'<span class="p">{pr[0]}</span>'
        pr = pr + [""] * (n - 1)
    return '<span class="pp">' + "".join(f"<span>{c}</span>" for c in pr) + "</span>"


def items(sec):
    n = len(sec["cols"]) or 1
    h = []
    for it in sec["items"]:
        if it == CORTE:
            h.append('<div class="it corte"></div>')
            continue
        nom, d, pr = it
        dd = f'<div class="d">{d}</div>' if d else ""
        h.append(f'<div class="it{" cd" if d else ""}"><div class="f"><span class="n">{nom}</span>'
                 f'{precios(pr, n, sec["unico"])}</div>{dd}</div>')
    return "".join(h)


def cabcol(sec):
    if len(sec["cols"]) < 2:
        return ""
    return '<div class="cabcol fijo">' + "".join(f"<span>{c}</span>" for c in sec["cols"]) + "</div>"


def notas(sec):
    return "".join(f'<div class="nt">{n}</div>' for n in sec["notas"])


SALTOS = {"vinos"}


def attrs(sec, k, extra=""):
    salto = ' data-salto="1"' if k in SALTOS else ""
    return f'class="sc s-{k} {extra}" data-t="{sec["t"]}" data-tramo="{sec["tramo"]}"{salto}'


def ilu(k, color, css, op=1):
    return tinta(ILU[k], color, css + f";opacity:{op}")


def logo(color, css):
    return tinta(R["logo"], color, css)


PAPEL = (f'<div class="abs" style="inset:0;background:url(\'{R["papel"]}\') center/cover;'
         f'mix-blend-mode:multiply;opacity:.55"></div>')

COMUN = """
html,body{height:auto!important;overflow:visible!important}
.hoja{break-after:page}
.caja{position:absolute;overflow:hidden;display:flex;flex-direction:column}
.it{break-inside:avoid}
.it .f{display:flex;justify-content:space-between;align-items:baseline;gap:3mm;font-weight:700}
.it .n{text-wrap:balance}
.it .p{white-space:nowrap}
.it .pp{display:flex;white-space:nowrap}
.it .d{font-size:8pt;font-weight:400;line-height:1.32;opacity:.88;margin-top:.6mm;max-width:92%;text-wrap:pretty}
.corte{height:0;border-top:.15mm solid currentColor;opacity:.35;margin:1.2mm 0 2.6mm}
.cabcol{display:flex;justify-content:flex-end;margin:0 0 1.6mm;font-size:6.8pt;font-weight:600;
        letter-spacing:.1em;text-transform:uppercase;opacity:.8;line-height:1.15}
.nt{font-size:7.8pt;line-height:1.35;font-style:italic;opacity:.9;text-wrap:pretty}
.leyenda{font-size:7pt;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.blk-ilu{margin-top:auto;flex:none}
body[data-solo] .hoja{display:none}
body[data-solo] .hoja.ver{display:block}
.hoja.vacia{display:none}
"""

# El paginador: vierte las secciones del <template> en las .caja, en orden
PAGINADOR = r"""<script>
function paginar(){
 const cajas=[...document.querySelectorAll('.caja')].sort((a,b)=>a.dataset.orden-b.dataset.orden);
 const fuente=[...document.getElementById('fuente').content.children];
 const lleno=b=>b.scrollHeight>b.clientHeight+0.5;
 let bi=0; const sobra=[]; let pend=null;
 // la ilustración de un tramo va al pie de la columna donde terminó ese tramo, si cabe
 const cerrar=()=>{if(pend&&pend.bi===bi){const c=pend.el.cloneNode(true);cajas[bi].append(c);if(lleno(cajas[bi]))c.remove();pend=null}};
 for(const s of fuente){
  if(bi>=cajas.length){sobra.push(s.dataset.t||'ilu');continue}
  if(s.classList.contains('blk-ilu')){pend={el:s,bi};continue}
  if(s.dataset.salto){const h=cajas[bi].closest('.hoja');
    if(h.querySelector('.sc')){while(bi<cajas.length&&cajas[bi].closest('.hoja')===h){cerrar();bi++}}
    if(bi>=cajas.length){sobra.push(s.dataset.t);continue}}
  const its=[...s.querySelector('.items').children].filter(e=>!e.classList.contains('fijo'));
  const n=its.length, partible=n>10; let i=0, primero=true;
  while(i<n && bi<cajas.length){
   const caja=cajas[bi], vacia=!caja.querySelector('.sc');
   const c=s.cloneNode(true), ic=c.querySelector('.items');
   [...ic.children].forEach(e=>{if(!e.classList.contains('fijo'))e.remove()});
   if(!primero)c.classList.add('cont');
   caja.append(c);
   if(lleno(caja)){c.remove();cerrar();bi++;continue}
   let puestos=0;
   while(i<n){const it=its[i].cloneNode(true);ic.append(it);if(lleno(caja)){it.remove();break}i++;puestos++}
   if(i<n){
    const minimo=partible?3:n;
    if(primero && puestos<minimo && !vacia){c.remove();i-=puestos;cerrar();bi++;continue}
    if(n-i<2 && puestos>3){ic.lastElementChild.remove();i--}
    while(ic.lastElementChild&&ic.lastElementChild.classList.contains('corte')){ic.lastElementChild.remove()}
    if(its[i]&&its[i].classList.contains('corte'))i++;
    primero=false;cerrar();bi++;
   }
  }
  if(i<n)sobra.push(s.dataset.t);
 }
 cerrar();
 const hojas=[...document.querySelectorAll('.hoja')]; let usadas=0;
 hojas.forEach((h,k)=>{const s=h.querySelector('.caja .sc');
   if(!s&&k>0){h.classList.add('vacia');return} usadas++;
   h.querySelectorAll('.tramo').forEach(t=>t.textContent=s?s.dataset.tramo:'')});
 document.body.dataset.paginas=usadas; document.body.dataset.sobra=sobra.join('|')||'ok';
 const p=new URLSearchParams(location.search).get('p');
 if(p){document.body.dataset.solo=1;hojas[p-1]&&hojas[p-1].classList.add('ver')}
}
document.fonts.ready.then(paginar);
</script>"""


def documento(css, hojas, fuente):
    cuerpo = "".join(f'<div class="hoja {cls}">{h}</div>' for cls, h in hojas)
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{BASE}{COMUN}{css}</style>'
            f'</head><body>{cuerpo}<template id="fuente">{fuente}</template>{PAGINADOR}</body></html>')


def caja(orden, css):
    return f'<div class="caja" data-orden="{orden}" style="{css}"></div>'


NHOJAS = 10


# ═════════════ A · ÍNDICE LATERAL ═════════════
A_ILU = {"vitrina": ("vitrina2", 50, 70), "desayuno": ("desayuno", 50, 38),
         "cafeteria": ("cafeteria", 44, 50), "carnes": ("almuerzo", 50, 31),
         "ensaladas": ("ensalada", 46, 41), "sinalcohol": ("cafeteria", 0, 0)}


def op_a():
    global SALTOS
    SALTOS = {"vinos", "carnes"}
    IX = 44
    css = f"""
    .hoja{{background:{CAFE};color:{BEIGE}}}
    .caja{{display:block}}
    .fila{{display:grid;grid-template-columns:{IX}mm 1fr;column-gap:12mm;position:relative}}
    .fila+.fila{{margin-top:9mm}}
    .fila+.fila::before{{content:"";position:absolute;left:0;right:0;top:-4.5mm;height:{FILETE};background:{BEIGE};opacity:.55;
      -webkit-mask:linear-gradient(90deg,#000 {IX}mm,transparent {IX}mm,transparent {IX+12}mm,#000 {IX+12}mm)}}
    .ix h2{{font-weight:700;font-size:11.5pt;letter-spacing:.1em;text-transform:uppercase;line-height:1.25;text-wrap:balance}}
    .ix .hr{{font-weight:700;font-size:8pt;letter-spacing:.12em;text-transform:uppercase;margin-top:2mm}}
    .ix .nt{{margin-top:2mm}}
    .cont .ix>*{{display:none}}
    .cont .ix h2{{display:block}}
    .it{{margin-bottom:3.2mm}}
    .it.cd{{margin-bottom:4mm}}
    .it .f{{font-size:9pt;letter-spacing:.05em;text-transform:uppercase;line-height:1.22}}
    .it .pp span{{min-width:17mm;text-align:right}}
    .cabcol span{{min-width:17mm;text-align:right}}
    .vl{{position:absolute;width:{FILETE};background:{BEIGE};opacity:.55}}
    .tramo{{position:absolute;right:12mm;top:11.5mm;font-size:23pt;font-weight:600;letter-spacing:.2em;
            text-transform:uppercase;color:{CLARO75};line-height:1}}
    """
    def sec_html(k):
        s = SEC[k]
        hr = f'<div class="hr">{s["hora"]}</div>' if s["hora"] else ""
        ex = ""
        if k in A_ILU and A_ILU[k][1]:
            key, w, h = A_ILU[k]
            ex = ilu(key, BEIGE, f"position:relative;margin:12mm 0 0 {IX - w}mm;width:{w}mm;height:{h}mm", .75)
        return (f'<div {attrs(s, k, "fila")}><div class="ix"><h2>{s["t"]}</h2>{hr}{notas(s)}{ex}</div>'
                f'<div class="items">{cabcol(s)}{items(s)}</div></div>')
    fuente = "".join(sec_html(k) for k in ORDEN)

    hor = "".join(f'<div><b style="font-weight:700">{a}</b> · {b}</div>' for a, b in HORARIO)
    vl = lambda top, alto: f'<div class="vl" style="left:{12 + IX + 6}mm;top:{top}mm;height:{alto}mm"></div>'
    hojas = [("", f"""
    {logo(BEIGE, 'left:11mm;top:13mm;width:62mm;height:20mm;-webkit-mask-position:left center')}
    <div class="abs" style="right:12mm;top:14mm;text-align:right;font-size:7.4pt;letter-spacing:.1em;text-transform:uppercase;line-height:1.75">{hor}</div>
    <div class="abs" style="left:0;right:0;top:44mm;height:{FILETE};background:{BEIGE};opacity:.7"></div>
    {vl(52, 236)}{caja(0, 'left:12mm;right:12mm;top:52mm;height:236mm')}""")]
    for i in range(1, NHOJAS):
        hojas.append(("", f"""
    {logo(BEIGE, 'left:12mm;top:12mm;width:30mm;height:9mm;-webkit-mask-position:left center')}
    <div class="tramo"></div>
    <div class="abs" style="left:0;right:0;top:30mm;height:{FILETE};background:{BEIGE};opacity:.7"></div>
    {vl(38, 250)}{caja(i, 'left:12mm;right:12mm;top:38mm;height:250mm')}"""))
    return documento(css, hojas, fuente)


# ═════════════ B · ÓVALOS A DOS COLUMNAS ═════════════
def ov_css(fg):
    return f"""
    .ov{{display:inline-block;border:.2mm solid currentColor;border-radius:50%;padding:2mm 6mm 1.8mm;
         font-weight:700;font-size:8pt;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap}}
    .ov.largo{{font-size:7.2pt;letter-spacing:.1em;padding:2mm 4.5mm 1.8mm}}
    .sc{{margin-bottom:7mm;flex:none}}
    .sc .cab{{margin-bottom:3.2mm}}
    .sc .hr{{font-size:8pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin:-1mm 0 1.6mm}}
    .sc .pre{{font-size:7.6pt;font-weight:700;letter-spacing:.06em;white-space:nowrap;text-transform:uppercase;margin-bottom:3mm}}
    .sc .nt{{margin:-.6mm 0 2.6mm}}
    .cont .pre,.cont .hr,.cont .nt{{display:none}}
    .it{{margin-bottom:2.6mm}}
    .it.cd{{margin-bottom:3.2mm}}
    .it .f{{font-size:9pt;letter-spacing:.04em;text-transform:uppercase;line-height:1.22}}
    .it .pp span{{min-width:15.5mm;text-align:right}}
    .cabcol span{{min-width:15.5mm;text-align:right}}
    .vl{{position:absolute;left:50%;width:{FILETE};background:{fg};opacity:.45}}
    .pie{{position:absolute;left:12mm;right:12mm;bottom:10mm;text-align:center}}
    .pie .l{{height:{FILETE};background:{fg};opacity:.45;margin-bottom:3mm}}
    .pie .leyenda{{letter-spacing:.08em;white-space:nowrap}}
    """


def sec_ov(k, etiqueta):
    s = SEC[k]
    pre = f'<div class="pre">{s["hora"]}</div>' if s["hora"] == ALM else ""
    hr = f'<div class="hr">{s["hora"]}</div>' if s["hora"] and s["hora"] != ALM else ""
    return (f'<div {attrs(s, k)}>{pre}<div class="cab">{etiqueta(s["t"])}</div>{hr}{notas(s)}'
            f'<div class="items">{cabcol(s)}{items(s)}</div></div>')


def dos_cajas(o, top, bottom=24):
    alto = 300 - top - bottom
    return (f'<div class="vl" style="top:{top}mm;height:{alto - 4}mm"></div>'
            + caja(o, f"left:12mm;width:67mm;top:{top}mm;height:{alto}mm")
            + caja(o + 1, f"right:12mm;width:67mm;top:{top}mm;height:{alto}mm"))


def op_b():
    global SALTOS
    SALTOS = {"vinos"}
    css = f".hoja{{background:{BEIGE};color:{CAFE}}}" + ov_css(CAFE)
    ov = lambda t: f'<span class="ov{" largo" if len(t) > 24 else ""}">{t}</span>'
    blk = lambda k, w, h, al="flex-start": (f'<div class="blk-ilu" style="align-self:{al};width:{w}mm;height:{h}mm;position:relative">'
                                            f'{ilu(k, CAFE, "inset:0", .75)}</div>')
    tras = {"complemento": blk("desayuno", 52, 40), "extras": blk("almuerzo", 56, 36, "flex-end"),
            "postres": blk("ensalada", 48, 46, "flex-end")}
    fuente = "".join(sec_ov(k, ov) + tras.get(k, "") for k in ORDEN)
    pie = f'<div class="pie"><div class="l"></div><div class="leyenda">{LEYENDA}</div></div>'
    hojas = [("", f"""{PAPEL}
    {logo(CAFE, 'left:0;right:0;top:14mm;height:19mm')}
    <div class="abs" style="left:0;right:0;top:38.5mm;text-align:center;font-size:10.5pt;font-weight:700;letter-spacing:.18em;text-transform:uppercase">Lunes a viernes · 08:00 a 22:00 hrs</div>
    {dos_cajas(0, 54)}{pie}""")]
    for i in range(1, NHOJAS):
        hojas.append(("", f"""{PAPEL}{logo(CAFE, 'left:0;right:0;top:12mm;height:9mm')}{dos_cajas(2 * i, 30)}{pie}"""))
    return documento(css, hojas, fuente)


# ═════════════ C · FRANJAS ═════════════
C_COLS = {"vitrina": 3, "adicionales": 3, "jugos": 3, "extras": 3, "spritz": 3, "schop": 2}


def op_c():
    global SALTOS
    SALTOS = {"vinos"}
    css = f"""
    .hoja{{background:{BEIGE};color:{CAFE}}}
    .caja{{padding:0 3mm}}
    .marco{{position:absolute;inset:6mm;border:{FILETE} solid {CAFE};opacity:.6}}
    .sc{{margin-bottom:7mm;flex:none}}
    .sc .cab{{display:flex;align-items:baseline;gap:4mm;margin-bottom:3.4mm;padding-left:1mm}}
    .sc .cab h2{{font-family:Brushwell;font-weight:400;font-size:23pt;letter-spacing:.03em;line-height:1.1;white-space:nowrap}}
    .sc .cab .l{{flex:1;height:{FILETE};background:{CAFE};opacity:.6;transform:translateY(-1.2mm)}}
    .sc .cab .hr{{font-size:7.6pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap}}
    .sc .nt{{margin:-1.2mm 0 2.8mm}}
    .cont .nt,.cont .cab .hr{{display:none}}
    .items{{column-gap:9mm}}
    .items.c2{{column-count:2}} .items.c3{{column-count:3;column-gap:7mm}}
    .items .corte{{break-before:column;border:0;margin:0}}
    .it{{margin-bottom:2.6mm}}
    .it.cd{{margin-bottom:3.2mm}}
    .it .f{{font-size:9.5pt;line-height:1.22}}
    .c3 .it .f{{font-size:9pt}}
    .it .pp span{{min-width:14mm;text-align:right}}
    .cabcol span{{min-width:14mm;text-align:right}}
    """
    def sec_html(k):
        s = SEC[k]
        hr = f'<span class="hr">{s["hora"]}</span>' if s["hora"] else ""
        return (f'<div {attrs(s, k)}><div class="cab"><h2>{s["t"]}</h2><div class="l"></div>{hr}</div>{notas(s)}'
                f'<div class="items c{C_COLS.get(k, 2)}">{cabcol(s)}{items(s)}</div></div>')
    fuente = "".join(sec_html(k) for k in ORDEN)
    hor = "".join(f'<div><b style="font-weight:700">{a}</b> · {b}</div>' for a, b in HORARIO)
    hojas = [("", f"""{PAPEL}<div class="marco"></div>
    {logo(CAFE, 'left:13mm;top:16mm;width:58mm;height:18mm;-webkit-mask-position:left center')}
    <div class="abs" style="right:13mm;top:16mm;text-align:right;font-size:7.4pt;letter-spacing:.1em;text-transform:uppercase;line-height:1.75">{hor}</div>
    {caja(0, 'left:10mm;right:10mm;top:46mm;height:200mm')}
    {ilu('desayuno', CAFE, 'right:13mm;bottom:12mm;width:52mm;height:39mm', .7)}""")]
    for i in range(1, NHOJAS):
        hojas.append(("", f"""{PAPEL}<div class="marco"></div>{logo(CAFE, 'left:0;right:0;top:12mm;height:9mm')}
    {caja(i, 'left:10mm;right:10mm;top:28mm;height:258mm')}"""))
    return documento(css, hojas, fuente)


# ═════════════ D · PORTADA PARTIDA, HOJAS ALTERNADAS ═════════════
def esquina(k, esq, w, h, op):
    """Dibujo a mano que sale por la esquina y se funde en degradé (sin desenfoque)."""
    v, hz = esq
    pos = f"{'bottom' if v == 'b' else 'top'}:-4mm;{'left' if hz == 'l' else 'right'}:-4mm"
    foco = f"{'left' if hz == 'l' else 'right'} {'bottom' if v == 'b' else 'top'}"
    return (f'<div class="abs" style="{pos};width:{w}mm;height:{h}mm;'
            f'-webkit-mask-image:radial-gradient(ellipse at {foco},#000 50%,transparent 92%)">'
            f'{tinta(ILU[k], "var(--fg)", f"inset:0;-webkit-mask-position:{foco};opacity:{op}")}</div>')


def op_d():
    global SALTOS
    SALTOS = {"vinos"}
    css = f"""
    .hoja.cafe{{--bg:{CAFE};--fg:{BEIGE}}} .hoja.beige{{--bg:{BEIGE};--fg:{CAFE}}}
    .hoja{{background:var(--bg);color:var(--fg)}}
    {ov_css('var(--fg)')}
    .rect{{display:inline-block;background:var(--fg);color:var(--bg);padding:2mm 3.6mm 1.8mm;font-weight:700;
           font-size:8pt;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap}}
    .rect.largo{{font-size:7.4pt;letter-spacing:.1em}}
    """
    rect = lambda t: f'<span class="rect{" largo" if len(t) > 24 else ""}">{t}</span>'
    fuente = "".join(sec_ov(k, rect) for k in ORDEN)
    pie = f'<div class="pie"><div class="l"></div><div class="leyenda">{LEYENDA}</div></div>'
    hor = "".join(f'<div><b style="font-weight:700">{a}</b></div><div style="margin-bottom:2.2mm">{b}</div>'
                  for a, b in HORARIO)
    con = "".join(f'<div style="font-size:6.6pt;font-weight:600;letter-spacing:.2em;text-transform:uppercase;opacity:.8">{a}</div>'
                  f'<div style="font-size:9.5pt;font-weight:700;letter-spacing:.04em;margin:.6mm 0 3mm">{b}</div>'
                  for a, b in CONTACTO)
    hojas = [("cafe", f"""
    <div class="vl" style="left:85mm;top:0;height:300mm"></div>
    {caja(0, 'left:12mm;width:63mm;top:14mm;height:274mm')}
    <div class="abs" style="left:85mm;right:0;top:16mm;text-align:center">{rect('Menú')}</div>
    {logo('var(--fg)', 'left:95mm;right:10mm;top:100mm;height:24mm')}
    <div class="abs" style="left:85mm;right:0;top:134mm;text-align:center;font-size:7.6pt;letter-spacing:.14em;text-transform:uppercase;line-height:1.5">{hor}</div>
    <div class="abs" style="left:85mm;right:0;top:188mm;text-align:center">{con}</div>
    {esquina('cafeteria', 'br', 70, 80, .5)}""")]
    esq = [("desayuno", "tr", 62, 48), ("almuerzo", "tl", 66, 44), ("ensalada", "tr", 56, 52),
           ("vitrina2", "tl", 46, 60), ("cafeteria", "tr", 50, 56)]
    for i in range(1, NHOJAS):
        k, e, w, h = esq[(i - 1) % len(esq)]
        hojas.append(("beige" if i % 2 else "cafe", f"""
    {esquina(k, e, w, h, .42)}
    {logo('var(--fg)', 'left:0;right:0;top:12mm;height:9mm')}{dos_cajas(2 * i - 1, 30)}{pie}"""))
    return documento(css, hojas, fuente)


OPCIONES = {"A": op_a, "B": op_b, "C": op_c, "D": op_d}
CH = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
      "--allow-file-access-from-files", "--virtual-time-budget=6000"]


def main():
    for d in ("html", "png", "pdf"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    info = {}
    for k in (sys.argv[1:] or list(OPCIONES)):
        n = f"BW-CARTA-OFICIAL-R3-OP{k}"
        h = OUT / "html" / f"{n}.html"
        h.write_text(OPCIONES[k](), encoding="utf-8")
        dom = subprocess.run(CH + ["--dump-dom", h.as_uri()], capture_output=True, text=True, encoding="utf-8").stdout
        pags = int(re.search(r'data-paginas="(\d+)"', dom).group(1))
        sobra = re.search(r'data-sobra="([^"]*)"', dom).group(1)
        subprocess.run(CH + ["--no-pdf-header-footer", f"--print-to-pdf={OUT / 'pdf' / (n + '.pdf')}", h.as_uri()],
                       check=True, capture_output=True)
        for p in range(1, pags + 1):
            subprocess.run(CH + ["--force-device-scale-factor=3", "--window-size=643,1134",
                                 f"--screenshot={OUT / 'png' / f'{n}-{p}.png'}", h.as_uri() + f"?p={p}"],
                           check=True, capture_output=True)
        info[k] = {"paginas": pags, "sobra": sobra}
        print(("✓" if sobra == "ok" else "⚠"), n, f"{pags} hojas", "" if sobra == "ok" else f"SOBRA: {sobra}")
    (OUT / "paginas.json").write_text(json.dumps(info, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()

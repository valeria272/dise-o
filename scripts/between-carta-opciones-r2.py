#!/usr/bin/env python3
"""BETWEEN · rediseño de la carta — RONDA 2 (25-09-2026). 3 opciones × 3 hojas, 17 × 30 cm.

Feedback de Eli sobre la ronda 1 (`between-carta-opciones.py`):
  · referencias que mandan: Grainhaus (ref08), Honeycomb Bakery stories (ref02),
    Café & Brunch MENU (ref07)
  · «mejora las jerarquías»
  · «que al inicio parta la info de la carta de desayuno»
  · «la idea es que quepa harta info en cada página, para achicar»

Qué cambia:
  1. DENSIDAD — el bloque Desayuno completo (hoy 6 hojas en la carta impresa) entra en 3:
       portada   = título compacto + Desayunos · Croissant · Complementa · Triángulos y tostadas
       interior  = Tentaciones (16) + Jugos, bebidas y aguas
       contrap.  = Cafetería (simple/doble) + Adicionales + contactos/QR al pie
     A dos columnas, como Café & Brunch.
  2. JERARQUÍA en 4 niveles, con saltos claros entre nivel y nivel:
       N1 título: Brushwell «Menú» montada sobre la caja alta ExtraBold enorme
       N2 sección: caja alta SemiBold chica y muy espaciada + filete (el «BREAKFAST
          FAVORITES» liviano de la ref) — contrasta con el nombre del plato por peso y tracking
       N3 plato: Raleway Bold, precio Bold alineado a la derecha, SIN línea punteada
       N4 descripción: Raleway Regular chica, al 75 %
  3. La información parte arriba: el título ocupa ~20 % de la portada, no la mitad.

    python scripts/between-carta-opciones-r2.py
Salida: out/hilton/between/carta-opciones/r2/{html,png,pdf}/
"""
import subprocess, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
BW = RAIZ / "public/assets/hilton/between"
CARTA = RAIZ / "raw/hilton/between/carta"
OUT = RAIZ / "out/hilton/between/carta-opciones/r2"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BEIGE, CAFE, TAUPE = "#FFF9EB", "#675B49", "#5C5447"


def u(p):
    return Path(p).resolve().as_uri()


# ───────── contenido LITERAL de la carta impresa feb-2026 (hojas 3, 4 y 5) ─────────
DESAYUNOS = [
    ("Buen día", "Huevos revueltos o fritos acompañados de pan a elección.", "$7.500"),
    ("Between", "Pocillo de palta, jamón pierna y queso gouda acompañado de pan a elección.", "$8.900"),
    ("Bonjour", "Croissant relleno de jamón y queso. (Blanco o Multigrano)", "$7.500"),
    ("2727", "Omelette relleno de jamón, queso y tomate, acompañado de ensaladilla mixta y tostadas.", "$7.900"),
    ("Keto", "Huevos fritos o revueltos, tocino, tomate tostado, palta y ensalada verde.", "$9.900"),
]
INCLUYE = "Incluye Café con leche, Chocolate caliente, Té o infusión, más Jugo del día."
PAN = ("Pan a elección entre: Baguette tradicional, Croissant tradicional, Croissant "
       "Multigrano, Tostadas blanca o Tostadas integrales.")
CROISSANT = [
    ("Croissant Italiano", "Croissant relleno de prosciutto, huevo mollet, salsa holandesa, tomate cóctel al pesto y rúcula.", "$7.500"),
    ("Croissant Danés", "Croissant relleno de pasta de salmón con queso crema al ciboulette, huevo mollet, salsa holandesa y mix de hojas.", "$7.500"),
    ("Croissant Jamón & Queso", "Croissant relleno con jamón y queso.", "$5.900"),
]
TRIANGULOS = [
    ("Triángulo ave Palta", "Pan de molde relleno de pasta de pollo, mayonesa y palta fresca.", "$4.900"),
    ("Triángulo de salmón queso crema", "Pan de molde relleno con pasta de salmón, queso crema al ciboulette y lechuga fresca.", "$5.300"),
    ("Triángulo jamón queso", "Pan de molde relleno con jamón y queso.", "$4.900"),
    ("Tostadas huevo y palta", "Tostadas con palta y huevo mollet bañadas de salsa holandesa.", "$6.300"),
    ("Tostadas con palta", "Tostadas a elección con pocillo de palta y mantequilla.", "$5.300"),
    ("Tostadas con mermelada", "Tostadas a elección con opciones de mermelada y mantequilla.", "$4.900"),
]
COMPLEMENTA = [
    ("Complemento dulce", "Vaso de fruta de la estación, Vaso de yogur con granola o 2 Vigilantes argentinos tibios.", "$1.900"),
    ("Refill de café", "Máximo 1 por cliente, solo asociado a la compra de desayuno.", "$1.900"),
]
TENTACIONES = [
    ("Yogur natural con granola", "Copa de yogur natural con fruta de la estación y mermelada de berries.", "$5.500"),
    ("Frutas de la estación", "Compotero de frutas frescas de la estación con miel y frutos secos.", "$4.900"),
    ("Selección de Galletas", "Selección de galletas rellenas simples y rellenas (100 gr).", "$3.900"),
    ("Vigilantes argentinos", "2 Vigilantes tibios cubiertos con azúcar y salsa de manjar.", "$2.500"),
    ("Pastel de Nata", "Clásico pastel portugués relleno de crema pastelera.", "$2.300"),
    ("Cinnamon Roll", "Clásico rollo de canela.", "$2.300"),
    ("Galletón DoubleTree", "Clásico galletón con chips de chocolate y nueces.", "$2.500"),
    ("Muffins", "Muffins de chocolate belga, arándano o frambuesa.", "$2.900"),
    ("Brownie Casero", "Brownie casero. (Consultar disponibilidad)", "$2.900"),
    ("Cheesecake NY", "Con salsa a elección: Maracuyá con pepas, Frutos rojos o Manjar.", "$4.900"),
    ("Torta", "Porción de torta casera. (Consultar disponibilidad)", "$4.900"),
    ("Strudell de Manzana", "Clásica receta austriaca rellena de manzana, canela y nueces.", "$4.700"),
    ("Tarta de Fruta", "Tarta de fruta del día. (Consultar disponibilidad)", "$4.700"),
    ("Kuchen", "Porción de Kuchen casero. (Consultar disponibilidad)", "$4.500"),
    ("Pie de Limón", "Suave crema de limón coronada con merengue suizo caramelizado.", "$4.500"),
    ("Opciones sin Azúcar", "Consultar por nuestra pastelería sin azúcar.", "$5.200"),
]
JUGOS = [
    ("Jugo de fruta", "(consultar disponibilidad)", "$3.700"),
    ("Bebidas", "", "$2.900"),
    ("Acqua Panna natural 505cc", "", "$4.200"),
    ("San Pellegrino con gas 505cc", "", "$4.200"),
    ("Agua Porvenir con o sin gas 330cc", "", "$2.900"),
]
# (nombre, descripción, simple, doble)
CAFETERIA = [
    ("Ristretto", "Una carga de espresso en 15ml de agua.", "$2.700", ""),
    ("Espresso", "Una carga de espresso en 30ml de agua.", "$2.700", "$3.300"),
    ("Lungo", "Una carga de espresso en 60ml de agua.", "$2.700", ""),
    ("Macchiato", "Espresso más espuma de leche.", "$2.900", "$3.500"),
    ("Americano", "Una parte de espresso y dos partes de agua.", "$2.900", "$3.500"),
    ("Cortado", "Simple: partes iguales de café y leche. Doble: Espresso doble y una medida de leche.", "$3.200", "$3.900"),
    ("Cappuccino", "Partes iguales de espresso, leche y espuma.", "$3.200", "$3.900"),
    ("Moccaccino", "Espresso, leche texturizada y salsa de chocolate.", "$3.700", "$4.600"),
    ("Latte", "Simple: una parte de espresso y dos partes de leche. Doble: dos cargas de espresso y tres partes de leche.", "$3.400", "$4.300"),
    ("Latte de sabores", "Sabores a elección: leche condensada, dulce de leche, pistacho, amaretto, vainilla o avellana.", "$3.700", "$4.600"),
    ("Latte Bombón", "Café espresso, leche condensada y leche texturizada.", "$4.100", ""),
    ("Afogatto", "Helado de vainilla con una carga de espresso.", "$4.100", ""),
    ("Café con helado", "Café americano, leche fría, dos bolas de helado y crema batida.", "$5.900", ""),
    ("Chocolate caliente", "", "$4.700", ""),
    ("Chocolate caliente de sabores", "Sabores a elección: leche condensada, dulce de leche, pistacho, amaretto, vainilla o avellana.", "$4.900", ""),
    ("Chai latte Masala o Cardamomo", "", "$4.200", ""),
    ("Variedad de Té e Infusiones", "", "$3.100", ""),
    ("MilkShake", "Dos bolas de helado de vainilla, leche y sabor a elección: Berries o Plátano.", "$5.300", ""),
    ("Leche con plátano", "Leche fresca, plátano y hielo.", "$4.200", ""),
    ("Irish Coffee", "Café americano, whisky, crema de leche y azúcar.", "$4.900", ""),
]
ADICIONALES = [("Leche de soja", "", "$700"), ("Leche de almendra", "", "$1.200"), ("Crema batida", "", "$700")]

R = {
    "logo": u(BW / "logo-blanco.png"), "qr": u(BW / "carta/qr-mask.png"),
    "ilu_taza": u(BW / "carta/ilu-taza-croissant.png"),
    "ilu_plato": u(BW / "carta/ilu-desayuno-plato.png"),
    "ilu_cafetera": u(BW / "carta/ilu-cafetera.png"),
    "papel": u(BW / "papel-beige.png"),
    "st_croissant": u(BW / "carta/croissant-sticker.png"),
    "st_latte": u(BW / "carta/latte-sticker.png"),
    "f_portada": u(BW / "fotos-gradadas/croissant-latte-cenital.jpg"),
    "f_yogur": u(BW / "fotos-gradadas/h1-desayuno-cenital.jpg"),
    "f_tazas": u(BW / "fotos-gradadas/j-dos-tazas.jpg"),
}
F = BW / "fonts"

BASE = f"""
@font-face{{font-family:Brushwell;src:url('{u(F/'Brushwell.ttf')}')}}
@font-face{{font-family:Raleway;font-weight:400;src:url('{u(F/'Raleway-Regular.ttf')}')}}
@font-face{{font-family:Raleway;font-weight:400;font-style:italic;src:url('{u(F/'Raleway-Italic.ttf')}')}}
@font-face{{font-family:Raleway;font-weight:500;src:url('{u(F/'Raleway-Medium.ttf')}')}}
@font-face{{font-family:Raleway;font-weight:600;src:url('{u(F/'Raleway-SemiBold.ttf')}')}}
@font-face{{font-family:Raleway;font-weight:700;src:url('{u(F/'Raleway-Bold.ttf')}')}}
@font-face{{font-family:Raleway;font-weight:800;src:url('{u(F/'Raleway-ExtraBold.ttf')}')}}
@page{{size:170mm 300mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:170mm;height:300mm;overflow:hidden}}
body{{font-family:Raleway,sans-serif;font-feature-settings:"lnum" 1;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.hoja{{position:relative;width:170mm;height:300mm;overflow:hidden}}
.abs{{position:absolute}}
.tinta{{-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center}}
.script{{font-family:Brushwell;font-weight:400;letter-spacing:.036em;line-height:1}}
.titulo{{font-weight:800;text-transform:uppercase;letter-spacing:.015em;line-height:.9}}
/* N2 · sección */
.sec{{margin:0 0 3.2mm}}
.sec h2{{font-weight:600;font-size:11pt;letter-spacing:.24em;text-transform:uppercase;line-height:1.1}}
.sec .sub{{font-size:7.6pt;font-style:italic;font-weight:400;opacity:.8;margin-top:1mm}}
.sec .filete{{height:.3mm;background:currentColor;margin-top:2mm;opacity:.9}}
/* N3 · plato  ·  N4 · descripción */
.it{{break-inside:avoid;margin:0 0 3.1mm}}
.it .f{{display:flex;justify-content:space-between;align-items:baseline;gap:3mm;font-weight:700;font-size:10pt;line-height:1.15}}
.it .p{{white-space:nowrap}}
.it .p2{{display:flex;gap:2.6mm;white-space:nowrap}}
.it .p2 span{{min-width:10.5mm;text-align:right}}
.it .d{{font-size:7.6pt;line-height:1.28;opacity:.78;margin-top:.5mm;max-width:92%}}
.cols{{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm}}
.cabcol{{display:flex;justify-content:flex-end;gap:2.6mm;font-size:6.2pt;font-weight:600;letter-spacing:.14em;text-transform:uppercase;opacity:.8;margin:-1.4mm 0 2.4mm}}
.cabcol span{{min-width:10.5mm;text-align:right}}
.nota{{font-size:7.5pt;line-height:1.35}}
.foto-ref{{font-size:5.4pt;opacity:.75}}
"""


def tinta(url, color, css):
    return (f'<div class="tinta abs" style="-webkit-mask-image:url(\'{url}\');'
            f'background:{color};{css}"></div>')


def sec(titulo, sub=""):
    s = f'<div class="sub">{sub}</div>' if sub else ""
    return f'<div class="sec"><h2>{titulo}</h2>{s}<div class="filete"></div></div>'


def lista(items, reglas=False, gap=None):
    h = []
    for it in items:
        if len(it) == 4:
            nom, des, s, d = it
            pre = f'<span class="p2"><span>{s}</span><span>{d}</span></span>'
        else:
            nom, des, p = it
            pre = f'<span class="p">{p}</span>'
        st = f' style="margin-bottom:{gap}"' if gap else ""
        regla = ('<div style="height:.2mm;background:currentColor;opacity:.25;margin-top:2mm"></div>'
                 if reglas else "")
        dd = f'<div class="d">{des}</div>' if des else ""
        h.append(f'<div class="it"{st}><div class="f"><span>{nom}</span>{pre}</div>{dd}{regla}</div>')
    return "".join(h)


def cab_simple_doble():
    return '<div class="cabcol"><span>Simple</span><span>Doble</span></div>'


def pag(css, cuerpo):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{BASE}{css}</style>'
            f'</head><body><div class="hoja">{cuerpo}</div></body></html>')


def contactos(color, fondo_qr, tinta_qr, borde):
    """Franja de cierre: QR + redes + horario. Se usa al pie de la contraportada."""
    return f"""
    <div class="abs" style="left:12mm;right:12mm;bottom:12mm;display:flex;align-items:center;gap:7mm;color:{color}">
      <div style="width:33mm;height:33mm;flex:none;background:{fondo_qr};border:{borde};border-radius:2.5mm;padding:2.6mm">
        <div class="tinta" style="-webkit-mask-image:url('{R['qr']}');background:{tinta_qr};width:100%;height:100%"></div></div>
      <div style="flex:1">
        <div class="script" style="font-size:19pt">#Síguenos</div>
        <div style="font-size:9pt;font-weight:700;line-height:1.7;margin-top:1mm">@between.coffeebar<br>cafeteriabetween.cl</div>
        <div style="font-size:6.4pt;font-weight:600;letter-spacing:.2em;margin-top:2mm">HORARIO DE APERTURA · 8:00 - 16:30 HRS</div>
      </div>
      <div class="tinta" style="-webkit-mask-image:url('{R['logo']}');background:{color};width:34mm;height:11mm;flex:none"></div>
    </div>"""


def lockup(color, top, horario_pill=False, alinear="left"):
    """N1 · «Menú» en Brushwell montada sobre DESAYUNO en caja alta enorme (ref Café & Brunch)."""
    hor = ('<span style="display:inline-block;border:.35mm solid currentColor;border-radius:50%;'
           'padding:1.6mm 5mm;font-size:8pt;font-weight:700;letter-spacing:.14em">8:00 A 11:30 HRS</span>'
           if horario_pill else
           '<span style="font-size:8pt;font-weight:700;letter-spacing:.2em">8:00 A 11:30 HRS</span>')
    return f"""
    <div class="abs" style="left:12mm;right:12mm;top:{top};color:{color};text-align:{alinear}">
      <div class="titulo" style="font-size:56pt;margin-top:13mm">Desayuno</div>
      <div class="script abs" style="font-size:50pt;top:0;{'left:-1mm' if alinear=='left' else 'left:0;right:0'}">Menú</div>
      <div style="margin-top:3.4mm">{hor}</div>
    </div>"""


# ═════════════ PÁGINAS · el contenido es el mismo en las 3 opciones; cambia la piel ═════════════
def portada_contenido(reglas=False):
    return f"""
      <div class="cols">
        <div>{sec('Desayunos', 'Pan a elección')}{lista(DESAYUNOS, reglas)}
          <div class="nota" style="margin-top:1.2mm"><b style="font-weight:700">{INCLUYE}</b><br>{PAN}</div></div>
        <div>{sec('Croissant', 'Blanco o Multigrano')}{lista(CROISSANT, reglas)}
          <div style="height:3.6mm"></div>
          {sec('Complementa tu desayuno')}{lista(COMPLEMENTA, reglas)}</div>
      </div>
      <div style="height:5mm"></div>
      {sec('Triángulos y tostadas', 'Tostadas Blancas o Integrales')}
      <div class="cols"><div>{lista(TRIANGULOS[:3], reglas)}</div><div>{lista(TRIANGULOS[3:], reglas)}</div></div>"""


def interior_contenido(reglas=False):
    return f"""
      {sec('Tentaciones')}
      <div class="cols"><div>{lista(TENTACIONES[:8], reglas)}</div><div>{lista(TENTACIONES[8:], reglas)}</div></div>
      <div style="height:4mm"></div>
      <div class="cols"><div>{sec('Jugos, bebidas y aguas')}{lista(JUGOS, reglas, '1.8mm')}</div><div></div></div>"""


def contra_contenido(reglas=False):
    return f"""
      {sec('Cafetería')}
      <div class="cols"><div>{cab_simple_doble()}{lista(CAFETERIA[:10], reglas)}</div>
                        <div>{cab_simple_doble()}{lista(CAFETERIA[10:], reglas)}</div></div>
      <div style="height:3mm"></div>
      <div class="cols"><div>{sec('Adicionales de cafetería')}{lista(ADICIONALES, reglas, '1.6mm')}</div><div></div></div>"""


# ═════════════ A · PAPEL Y TRAZO — Café & Brunch ═════════════
def op_a():
    css = f".hoja{{background:{BEIGE} url('{R['papel']}') center/cover;color:{CAFE}}}"
    cab = tinta(R["logo"], CAFE, "left:12mm;top:11mm;width:30mm;height:9mm;-webkit-mask-position:left center")
    p1 = f"""{cab}
    {tinta(R['ilu_taza'], CAFE, 'right:10mm;top:8mm;width:42mm;height:29mm')}
    {lockup(CAFE, '24mm')}
    <div class="abs" style="left:12mm;right:12mm;top:84mm">{portada_contenido()}</div>"""
    p2 = f"""{cab}
    <div class="script abs" style="right:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    <div class="abs" style="left:12mm;right:12mm;top:30mm">{interior_contenido()}</div>
    {tinta(R['ilu_plato'], CAFE, 'right:14mm;bottom:16mm;width:58mm;height:50mm;transform:rotate(-8deg)')}"""
    p3 = f"""{cab}
    <div class="script abs" style="right:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    {tinta(R['ilu_cafetera'], CAFE, 'right:16mm;top:212mm;width:30mm;height:36mm')}
    <div class="abs" style="left:12mm;right:12mm;top:30mm">{contra_contenido()}</div>
    <div class="abs" style="left:12mm;right:12mm;bottom:52mm;height:.3mm;background:{CAFE}"></div>
    {contactos(CAFE, 'transparent', CAFE, f'.3mm solid {CAFE}')}"""
    return [pag(css, p1), pag(css, p2), pag(css, p3)]


# ═════════════ B · BLOQUE Y TARJETA — Grainhaus ═════════════
def op_b():
    css = f"""
    .hoja{{background:{TAUPE};color:{CAFE}}}
    .foto{{position:absolute;left:0;right:0;top:0;height:78mm;object-fit:cover;width:100%}}
    .tarjeta{{position:absolute;left:12mm;right:12mm;bottom:12mm;background:{BEIGE};padding:9mm 9mm 0}}
    .bloque{{position:absolute;left:12mm;top:12mm;background:{TAUPE};color:{BEIGE};padding:7mm 8mm 6mm}}
    """
    p1 = f"""
    <img class="foto" src="{R['f_portada']}" style="object-position:50% 45%">
    <div class="bloque" style="width:84mm;height:62mm">
      {tinta(R['logo'], BEIGE, 'left:8mm;top:7mm;width:32mm;height:9mm;-webkit-mask-position:left center')}
      <div class="script abs" style="left:7mm;top:20mm;font-size:34pt">Menú</div>
      <div class="titulo abs" style="left:8mm;top:36mm;font-size:30pt">Desayuno</div>
      <div class="abs" style="left:8mm;bottom:5.5mm;font-size:7.4pt;font-weight:700;letter-spacing:.2em">8:00 A 11:30 HRS</div>
    </div>
    <div class="foto-ref abs" style="right:13mm;top:72mm;color:{BEIGE}">* Foto referencial</div>
    <div class="tarjeta" style="top:78mm">{portada_contenido()}</div>"""
    p2 = f"""
    <img class="foto" src="{R['f_yogur']}" style="height:62mm;object-position:50% 40%">
    <div class="bloque" style="width:62mm;height:44mm">
      {tinta(R['logo'], BEIGE, 'left:8mm;top:7mm;width:30mm;height:8mm;-webkit-mask-position:left center')}
      <div class="script abs" style="left:7mm;top:19mm;font-size:30pt">Tentaciones</div>
    </div>
    <div class="foto-ref abs" style="right:13mm;top:56mm;color:{BEIGE}">* Foto referencial</div>
    <div class="tarjeta" style="top:62mm">{interior_contenido()}
      {tinta(R['ilu_plato'], CAFE, 'right:10mm;bottom:10mm;width:52mm;height:44mm;transform:rotate(-8deg)')}</div>"""
    p3 = f"""
    <img class="foto" src="{R['f_tazas']}" style="height:46mm;object-position:50% 70%">
    <div class="bloque" style="width:62mm;height:34mm;top:6mm;padding:0">
      {tinta(R['logo'], BEIGE, 'left:8mm;top:7mm;width:30mm;height:8mm;-webkit-mask-position:left center')}
      <div class="script abs" style="left:7mm;top:17mm;font-size:28pt">Cafetería</div>
    </div>
    <div class="foto-ref abs" style="right:13mm;top:41mm;color:{BEIGE}">* Foto referencial</div>
    <div class="tarjeta" style="top:46mm;bottom:55mm;padding-top:7mm">{contra_contenido()}</div>
    {contactos(BEIGE, BEIGE, CAFE, 'none')}"""
    return [pag(css, p1), pag(css, p2), pag(css, p3)]


# ═════════════ C · TAUPE Y STICKER — Honeycomb Bakery ═════════════
def op_c():
    def patron():  # trazos tenues de fondo, como la ref
        t = []
        for url, css in [(R['ilu_taza'], 'left:-10mm;top:120mm;width:70mm;height:50mm;transform:rotate(-14deg)'),
                         (R['ilu_cafetera'], 'right:-8mm;top:150mm;width:46mm;height:60mm;transform:rotate(12deg)'),
                         (R['ilu_plato'], 'left:40mm;top:245mm;width:70mm;height:60mm;transform:rotate(9deg)')]:
            t.append(tinta(url, BEIGE, css + ';opacity:.07'))
        return "".join(t)
    css = f".hoja{{background:{TAUPE};color:{BEIGE}}} .sticker{{position:absolute;filter:drop-shadow(0 1.2mm 1.6mm rgba(20,14,8,.35))}}"
    cab = tinta(R["logo"], BEIGE, "left:12mm;top:11mm;width:30mm;height:9mm;-webkit-mask-position:left center")
    p1 = f"""{patron()}{cab}
    <img class="sticker" src="{R['st_croissant']}" style="right:8mm;top:20mm;width:56mm;transform:rotate(-6deg)">
    <div class="abs" style="left:12mm;top:26mm;color:{BEIGE}">
      <div class="script" style="font-size:44pt">Menú</div>
      <div class="titulo" style="font-size:40pt;margin-top:1mm">Desayuno</div>
      <div style="margin-top:4mm"><span style="display:inline-block;border:.35mm solid {BEIGE};border-radius:50%;padding:1.6mm 5mm;font-size:8pt;font-weight:700;letter-spacing:.14em">8:00 A 11:30 HRS</span></div>
    </div>
    <div class="foto-ref abs" style="right:12mm;top:70mm">* Foto referencial</div>
    <div class="abs" style="left:12mm;right:12mm;top:84mm">{portada_contenido(reglas=True)}</div>"""
    p2 = f"""{patron()}{cab}
    <div class="script abs" style="right:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    <div class="abs" style="left:12mm;right:12mm;top:30mm">{interior_contenido(reglas=True)}</div>
    {tinta(R['ilu_plato'], BEIGE, 'right:14mm;bottom:16mm;width:56mm;height:48mm;transform:rotate(-8deg)')}"""
    p3 = f"""{patron()}{cab}
    <div class="script abs" style="right:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    <img class="sticker" src="{R['st_latte']}" style="right:12mm;top:203mm;width:40mm;transform:rotate(8deg)">
    <div class="abs" style="left:12mm;right:12mm;top:30mm">{contra_contenido(reglas=True)}</div>
    <div class="abs" style="left:12mm;right:12mm;bottom:52mm;height:.3mm;background:{BEIGE};opacity:.6"></div>
    {contactos(BEIGE, BEIGE, TAUPE, 'none')}"""
    return [pag(css, p1), pag(css, p2), pag(css, p3)]


OPCIONES = {"A": op_a, "B": op_b, "C": op_c}
HOJAS = ["1-portada", "2-interior", "3-contraportada"]


def render(h, png, pdf):
    base = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--allow-file-access-from-files", "--virtual-time-budget=4000"]
    subprocess.run(base + ["--force-device-scale-factor=3", "--window-size=643,1134",
                           f"--screenshot={png}", h.as_uri()], check=True, capture_output=True)
    subprocess.run(base + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", h.as_uri()],
                   check=True, capture_output=True)


def main():
    for d in ("html", "png", "pdf"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    for k in (sys.argv[1:] or list(OPCIONES)):
        for hoja, html in zip(HOJAS, OPCIONES[k]()):
            n = f"BW-CARTA-R2-OP{k}-{hoja}"
            h = OUT / "html" / f"{n}.html"
            h.write_text(html, encoding="utf-8")
            render(h, OUT / "png" / f"{n}.png", OUT / "pdf" / f"{n}.pdf")
            print("✓", n)


if __name__ == "__main__":
    main()

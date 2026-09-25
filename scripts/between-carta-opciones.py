#!/usr/bin/env python3
"""BETWEEN · rediseño de la carta — 3 opciones × 3 hojas (portada · interior · contraportada).

Pedido de Eli (25-09-2026): ejercicio para afinar cómo diseñamos la carta ANTES de que
el cliente mande sus referencias. Formato de la carta vigente: 17 × 30 cm vertical.
Contenido LITERAL de la carta impresa `CARTA-ES-DESAYUNO-ALMUERZO BW 2026.pdf` (feb-2026),
bloque Desayuno. Referencias de Eli: Drive «referencias carta BW DISEÑO».

    python scripts/between-carta-opciones.py            # HTML + PNG + PDF de las 9 hojas

Salida: out/hilton/between/carta-opciones/{html,png,pdf}/  +  index.html (comparación)

Tres direcciones, todas dentro del sistema (beige #FFF9EB · café #675B49 · taupe de la
carta #5C5447 · Brushwell sólo en palabra clave · Raleway para todo lo demás):
  A · Papel y trazo    — una tinta café sobre beige + ilustración de línea (refs Coffee,
                         Coaster, Café & Brunch). Sin fotos.
  B · Arco editorial   — evoluciona la carta actual: foto real dentro del arco, panel beige
                         (refs SOLA, Cafeteria, Grainhaus).
  C · Taupe y tarjeta  — fondo taupe, tarjeta crema con filete doble, trazo beige
                         (refs oak&cocoa, Bonbon).
"""
import subprocess, sys, shutil
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BW = RAIZ / "public/assets/hilton/between"
CARTA = RAIZ / "raw/hilton/between/carta"
OUT = RAIZ / "out/hilton/between/carta-opciones"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

BEIGE, CAFE, TAUPE = "#FFF9EB", "#675B49", "#5C5447"


def u(p):  # file URL
    return Path(p).resolve().as_uri()


# ───────────────────────── contenido (literal de la carta impresa) ─────────────────────────
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

# ───────────────────────── recursos ─────────────────────────
A = {
    "logo": u(BW / "logo-blanco.png"),
    "qr": u(BW / "carta/qr-mask.png"),
    "ilu_taza": u(BW / "carta/ilu-taza-croissant.png"),
    "ilu_plato": u(BW / "carta/ilu-desayuno-plato.png"),
    "ilu_cafetera": u(BW / "carta/ilu-cafetera.png"),
    "flecha": u(BW / "recursos/flecha-bucle.png"),
    "papel": u(BW / "papel-beige.png"),
    "f_portada": u(BW / "fotos-gradadas/croissant-latte-cenital.jpg"),
    "f_croissant": u(BW / "fotos-gradadas/h3-croissant-jamon.jpg"),
    "f_tazas": u(BW / "fotos-gradadas/j-dos-tazas.jpg"),
    "f_desayuno": u(BW / "fotos-gradadas/desayuno-completo-2.jpg"),
}
F = BW / "fonts"

BASE_CSS = f"""
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
.tinta{{-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center}}
.logo{{-webkit-mask-image:url('{A['logo']}');}}
.script{{font-family:Brushwell;font-weight:400;letter-spacing:.036em;line-height:1}}
.caps{{font-weight:800;text-transform:uppercase;letter-spacing:.06em;line-height:1.05}}
.item{{break-inside:avoid}}
.item .fila{{display:flex;align-items:baseline;gap:2mm}}
.item .nom{{font-weight:700}}
.item .lid{{flex:1;border-bottom:.25mm dotted currentColor;opacity:.55;transform:translateY(-.8mm)}}
.item .pre{{font-weight:700;white-space:nowrap}}
.item .des{{font-weight:400;line-height:1.32}}
"""


def tinta(url, color, css):
    return (f'<div class="tinta" style="-webkit-mask-image:url(\'{url}\');'
            f'background:{color};{css}"></div>')


def items(lista, t_nom, t_des, gap, desc_ancho="88%"):
    h = []
    for nom, des, pre in lista:
        h.append(f'<div class="item" style="margin-bottom:{gap}">'
                 f'<div class="fila" style="font-size:{t_nom}"><span class="nom">{nom}</span>'
                 f'<span class="lid"></span><span class="pre">{pre}</span></div>'
                 f'<div class="des" style="font-size:{t_des};max-width:{desc_ancho};margin-top:.9mm">{des}</div></div>')
    return "".join(h)


def pagina(css, cuerpo):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<style>{BASE_CSS}{css}</style></head><body><div class="hoja">{cuerpo}</div></body></html>')


# ═════════════════════════ OPCIÓN A · PAPEL Y TRAZO ═════════════════════════
def op_a():
    css = f"""
    .hoja{{background:{BEIGE} url('{A['papel']}') center/cover;color:{CAFE}}}
    .sec{{display:flex;align-items:baseline;gap:3mm;margin:0 0 4.2mm}}
    .sec .caps{{font-size:17pt}} .sec .sub{{font-size:8.6pt;font-weight:500;font-style:italic}}
    .regla{{height:.35mm;background:{CAFE};margin:0 0 5mm}}
    """
    logo = tinta(A["logo"], CAFE, "position:absolute;left:0;right:0;top:15mm;height:13mm")
    # ── portada
    p1 = f"""{logo}
    {tinta(A['ilu_taza'], CAFE, 'position:absolute;right:9mm;top:34mm;width:60mm;height:46mm')}
    <div style="position:absolute;left:15mm;top:44mm">
      <div class="script" style="font-size:80pt">Menú</div>
      <div class="caps" style="font-size:34pt;letter-spacing:.07em;margin-top:1mm">DESAYUNO</div>
      <div style="font-size:10pt;font-weight:600;letter-spacing:.14em;margin-top:3.6mm">8:00 A 11:30 HRS</div>
    </div>
    <div style="position:absolute;left:15mm;right:15mm;top:112mm">
      <div class="regla"></div>
      {items(DESAYUNOS, '14pt', '10pt', '7.4mm')}
      <div style="border:.35mm solid {CAFE};border-radius:3mm;padding:5mm 6mm;margin-top:3mm;font-size:9.6pt;line-height:1.4">
        <b style="font-weight:700">{INCLUYE}</b><br>{PAN}</div>
    </div>
    <div style="position:absolute;left:0;right:0;bottom:12mm;text-align:center;font-size:8.2pt;font-weight:600;letter-spacing:.2em">
      HORARIO DE APERTURA · 8:00 - 16:30 HRS</div>"""
    # ── interior
    p2 = f"""
    <div style="position:absolute;left:15mm;right:15mm;top:16mm">
      <div class="sec"><span class="caps">Croissant</span><span class="sub">Blanco o Multigrano</span></div>
      <div class="regla"></div>
      {items(CROISSANT, '12.6pt', '9.2pt', '5.4mm')}
    </div>
    {tinta(A['ilu_plato'], CAFE, 'position:absolute;right:15mm;top:92mm;width:50mm;height:42mm;transform:rotate(-8deg)')}
    <div style="position:absolute;left:15mm;top:98mm">
      <div class="script" style="font-size:40pt;line-height:.9">para</div>
      <div class="script" style="font-size:40pt;line-height:.9;margin-left:9mm">acompañar</div>
    </div>
    <div style="position:absolute;left:15mm;right:15mm;top:140mm">
      <div class="sec"><span class="caps">Triángulos y tostadas</span><span class="sub">Blancas o Integrales</span></div>
      <div class="regla"></div>
      {items(TRIANGULOS, '11.6pt', '8.6pt', '4.1mm')}
    </div>
    <div style="position:absolute;left:15mm;right:15mm;bottom:12mm;border:.35mm solid {CAFE};border-radius:3mm;padding:4.2mm 5mm 1mm">
      <div class="caps" style="font-size:10pt;margin-bottom:3mm">Complementa tu desayuno</div>
      {items(COMPLEMENTA, '10.6pt', '8.2pt', '3.2mm')}
    </div>"""
    # ── contraportada
    p3 = f"""
    {tinta(A['ilu_cafetera'], CAFE, 'position:absolute;left:0;right:0;top:30mm;height:74mm')}
    <div style="position:absolute;left:0;right:0;top:114mm;text-align:center">
      <div class="script" style="font-size:44pt">Gracias por</div>
      <div class="caps" style="font-size:23pt;margin-top:1.5mm">ser parte de Between</div>
    </div>
    <div style="position:absolute;left:50%;top:162mm;transform:translateX(-50%);width:56mm;height:56mm;border:.35mm solid {CAFE};border-radius:3mm;padding:4.5mm">
      {tinta(A['qr'], CAFE, 'width:100%;height:100%')}
    </div>
    <div class="script" style="position:absolute;left:0;right:0;top:225mm;text-align:center;font-size:24pt"># Síguenos</div>
    <div style="position:absolute;left:0;right:0;top:242mm;text-align:center;font-size:10.5pt;font-weight:700;letter-spacing:.04em;line-height:1.9">
      @between.coffeebar<br>cafeteriabetween.cl</div>
    <div style="position:absolute;left:15mm;right:15mm;bottom:34mm;height:.35mm;background:{CAFE}"></div>
    {tinta(A['logo'], CAFE, 'position:absolute;left:0;right:0;bottom:15mm;height:12mm')}"""
    return [pagina(css, p1), pagina(css, p2), pagina(css, p3)]


# ═════════════════════════ OPCIÓN B · ARCO EDITORIAL ═════════════════════════
def op_b():
    css = f"""
    .hoja{{background:{TAUPE};color:{CAFE}}}
    .arco{{position:absolute;overflow:hidden;border-radius:80mm 80mm 0 0}}
    .arco img{{width:100%;height:100%;object-fit:cover;display:block}}
    .panel{{position:absolute;background:{BEIGE}}}
    .sec{{margin:0 0 4mm}} .sec .caps{{font-size:16.5pt}} .sec .sub{{font-size:8.4pt;font-weight:500;font-style:italic;margin-top:1.2mm}}
    .ref{{position:absolute;font-size:5.6pt;color:{BEIGE};opacity:.8}}
    """
    # ── portada: arco con foto arriba, panel beige abajo que empieza con el desayuno
    p1 = f"""
    <div class="arco" style="left:11mm;right:11mm;top:11mm;height:118mm">
      <img src="{A['f_portada']}" style="object-position:40% 50%">
      <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(36,26,18,.55),rgba(36,26,18,0) 45%)"></div>
    </div>
    {tinta(A['logo'], BEIGE, 'position:absolute;left:0;right:0;top:26mm;height:11mm')}
    <div class="panel" style="left:11mm;right:11mm;top:129mm;bottom:11mm;padding:9mm 11mm 0">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:5mm">
        <div><div class="script" style="font-size:44pt">Menú</div>
             <div class="caps" style="font-size:25pt;margin-top:.5mm">Desayuno</div></div>
        <div style="text-align:right;font-size:9.4pt;font-weight:700;letter-spacing:.12em;line-height:1.5;padding-bottom:1mm">8:00 A<br>11:30 HRS</div>
      </div>
      {items(DESAYUNOS, '12.8pt', '9.2pt', '6.6mm')}
      <div style="font-size:8.4pt;line-height:1.35;padding-top:2.6mm;border-top:.3mm solid {CAFE}">
        <b style="font-weight:700">{INCLUYE}</b> {PAN}</div>
    </div>
    <div class="ref" style="left:14mm;top:124mm;color:{BEIGE}">* Foto referencial</div>"""
    # ── interior: columna de foto en arco a la derecha + contenido
    p2 = f"""
    <div class="panel" style="left:11mm;right:11mm;top:11mm;bottom:11mm"></div>
    <div class="arco" style="right:17mm;top:17mm;width:52mm;height:80mm;border-radius:26mm 26mm 0 0">
      <img src="{A['f_croissant']}" style="object-position:55% 50%"></div>
    <div style="position:absolute;left:21mm;top:22mm;width:68mm">
      <div class="script" style="font-size:30pt">el favorito</div>
      <div class="sec" style="margin-top:2mm"><div class="caps">Croissant</div><div class="sub">Blanco o Multigrano</div></div>
    </div>
    <div style="position:absolute;left:21mm;right:21mm;top:103mm">
      {items(CROISSANT, '11.4pt', '8.4pt', '4.4mm')}
      <div style="height:.3mm;background:{CAFE};margin:3mm 0 5mm"></div>
      <div class="sec"><div class="caps">Triángulos y tostadas</div><div class="sub">Tostadas Blancas o Integrales</div></div>
      {items(TRIANGULOS, '11pt', '8.2pt', '3.6mm')}
    </div>
    <div style="position:absolute;left:11mm;right:11mm;bottom:11mm;background:{CAFE};color:{BEIGE};padding:4.5mm 10mm 1.2mm">
      <div class="caps" style="font-size:10.4pt;margin-bottom:2.8mm">Complementa tu desayuno</div>
      {items(COMPLEMENTA, '10pt', '7.8pt', '2.8mm')}
    </div>
    <div class="ref" style="right:17mm;top:98mm;color:{CAFE}">* Foto referencial</div>"""
    # ── contraportada: arco con foto de las dos tazas + contactos
    p3 = f"""
    <div class="arco" style="left:11mm;right:11mm;top:11mm;bottom:11mm;border-radius:80mm 80mm 0 0">
      <img src="{A['f_tazas']}" style="object-position:50% 50%">
      <div style="position:absolute;inset:0;background:rgba(36,26,18,.58)"></div>
    </div>
    <div style="position:absolute;left:11mm;right:11mm;top:11mm;bottom:11mm;border-radius:80mm 80mm 0 0;border:.4mm solid {BEIGE};margin:5mm"></div>
    {tinta(A['logo'], BEIGE, 'position:absolute;left:0;right:0;top:40mm;height:11mm')}
    <div style="position:absolute;left:0;right:0;top:78mm;text-align:center;color:{BEIGE}">
      <div class="script" style="font-size:40pt">Relaja tu</div>
      <div class="caps" style="font-size:25pt;margin-top:1mm">momento</div>
    </div>
    <div style="position:absolute;left:50%;top:128mm;transform:translateX(-50%);width:54mm;height:54mm;background:{BEIGE};padding:5mm">
      {tinta(A['qr'], CAFE, 'width:100%;height:100%')}</div>
    <div class="script" style="position:absolute;left:0;right:0;top:190mm;text-align:center;font-size:23pt;color:{BEIGE}"># Síguenos</div>
    <div style="position:absolute;left:0;right:0;top:207mm;text-align:center;font-size:10.5pt;font-weight:700;letter-spacing:.04em;line-height:1.9;color:{BEIGE}">
      @between.coffeebar<br>cafeteriabetween.cl</div>
    <div style="position:absolute;left:0;right:0;bottom:30mm;text-align:center;font-size:7.4pt;font-weight:600;letter-spacing:.2em;color:{BEIGE}">
      HORARIO DE APERTURA · 8:00 - 16:30 HRS</div>
    <div class="ref" style="left:14mm;bottom:5mm">* Foto referencial</div>"""
    return [pagina(css, p1), pagina(css, p2), pagina(css, p3)]


# ═════════════════════════ OPCIÓN C · TAUPE Y TARJETA ═════════════════════════
def op_c():
    franja = (f"repeating-linear-gradient(90deg,{BEIGE} 0 1.6mm,transparent 1.6mm 3.2mm)")
    css = f"""
    .hoja{{background:{TAUPE};color:{BEIGE}}}
    .tarjeta{{position:absolute;background:{BEIGE};color:{CAFE};outline:.35mm solid {CAFE};outline-offset:-2.4mm}}
    .franja{{position:absolute;height:3.4mm;background:{franja};opacity:.9}}
    .sec{{text-align:center;margin:0 0 4mm}} .sec .caps{{font-size:16pt}} .sec .sub{{font-size:8.2pt;font-weight:500;font-style:italic;margin-top:1.2mm}}
    """
    # ── portada: cabecera taupe con ilustración beige, tarjeta crema con el desayuno
    p1 = f"""
    <div class="franja" style="left:0;right:0;top:0"></div>
    {tinta(A['logo'], BEIGE, 'position:absolute;left:0;right:0;top:14mm;height:11mm')}
    {tinta(A['ilu_taza'], BEIGE, 'position:absolute;left:12mm;top:36mm;width:70mm;height:50mm')}
    <div style="position:absolute;right:14mm;top:40mm;text-align:right">
      <div class="script" style="font-size:62pt">Menú</div>
      <div class="caps" style="font-size:26pt;margin-top:1mm">Desayuno</div>
      <div style="font-size:8.4pt;font-weight:600;letter-spacing:.14em;margin-top:3mm">8:00 A 11:30 HRS</div>
    </div>
    <div class="tarjeta" style="left:12mm;right:12mm;top:96mm;bottom:16mm;padding:13mm 12mm 0">
      {items(DESAYUNOS, '13.6pt', '9.8pt', '9.6mm')}
      <div style="text-align:center;font-size:8.8pt;line-height:1.4;margin-top:1.5mm;padding:3.4mm 4mm;background:{CAFE};color:{BEIGE}">
        <b style="font-weight:700">{INCLUYE}</b><br>{PAN}</div>
    </div>
    <div class="franja" style="left:0;right:0;bottom:0"></div>"""
    # ── interior: dos tarjetas escalonadas + ilustración en el hueco
    p2 = f"""
    <div class="franja" style="left:0;right:0;top:0"></div>
    <div class="tarjeta" style="left:12mm;right:12mm;top:14mm;height:84mm;padding:10mm 11mm 0">
      <div class="sec"><div class="caps">Croissant</div><div class="sub">Blanco o Multigrano</div></div>
      {items(CROISSANT, '11.2pt', '8.2pt', '4.2mm')}
    </div>
    <div class="script" style="position:absolute;left:14mm;top:103mm;font-size:32pt">recién hecho</div>
    {tinta(A['ilu_plato'], BEIGE, 'position:absolute;right:8mm;top:99mm;width:48mm;height:40mm')}
    <div class="tarjeta" style="left:12mm;right:12mm;top:141mm;bottom:52mm;padding:10mm 11mm 0">
      <div class="sec"><div class="caps">Triángulos y tostadas</div><div class="sub">Tostadas Blancas o Integrales</div></div>
      {items(TRIANGULOS, '10.6pt', '7.9pt', '3.4mm')}
    </div>
    <div style="position:absolute;left:16mm;right:16mm;bottom:12mm">
      <div class="caps" style="font-size:10.4pt;text-align:center;margin-bottom:3mm">Complementa tu desayuno</div>
      {items(COMPLEMENTA, '10pt', '7.8pt', '2.8mm')}
    </div>
    <div class="franja" style="left:0;right:0;bottom:0"></div>"""
    # ── contraportada
    p3 = f"""
    <div class="franja" style="left:0;right:0;top:0"></div>
    {tinta(A['ilu_cafetera'], BEIGE, 'position:absolute;left:0;right:0;top:24mm;height:56mm')}
    <div style="position:absolute;left:0;right:0;top:88mm;text-align:center">
      <div class="caps" style="font-size:22pt">Nuestros contactos</div>
    </div>
    <div class="tarjeta" style="left:50%;top:108mm;transform:translateX(-50%);width:66mm;height:66mm;padding:9mm">
      {tinta(A['qr'], CAFE, 'width:100%;height:100%')}</div>
    <div class="script" style="position:absolute;left:0;right:0;top:184mm;text-align:center;font-size:24pt"># Síguenos</div>
    <div style="position:absolute;left:0;right:0;top:201mm;text-align:center;font-size:10.5pt;font-weight:700;letter-spacing:.04em;line-height:1.9">
      @between.coffeebar<br>cafeteriabetween.cl</div>
    <div style="position:absolute;left:0;right:0;bottom:46mm;text-align:center;font-size:7.4pt;font-weight:600;letter-spacing:.2em">
      HORARIO DE APERTURA · 8:00 - 16:30 HRS</div>
    {tinta(A['logo'], BEIGE, 'position:absolute;left:0;right:0;bottom:20mm;height:12mm')}
    <div class="franja" style="left:0;right:0;bottom:0"></div>"""
    return [pagina(css, p1), pagina(css, p2), pagina(css, p3)]


OPCIONES = {"A": op_a, "B": op_b, "C": op_c}
HOJAS = ["1-portada", "2-interior", "3-contraportada"]


def render(html_path, png, pdf):
    base = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--allow-file-access-from-files", "--virtual-time-budget=4000"]
    subprocess.run(base + ["--force-device-scale-factor=3", "--window-size=643,1134",
                           f"--screenshot={png}", html_path.as_uri()], check=True,
                   capture_output=True)
    subprocess.run(base + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                           html_path.as_uri()], check=True, capture_output=True)


def main():
    for d in ("html", "png", "pdf"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    solo = sys.argv[1:] or list(OPCIONES)
    for k in solo:
        for hoja, html in zip(HOJAS, OPCIONES[k]()):
            n = f"BW-CARTA-OP{k}-{hoja}"
            h = OUT / "html" / f"{n}.html"
            h.write_text(html, encoding="utf-8")
            render(h, OUT / "png" / f"{n}.png", OUT / "pdf" / f"{n}.pdf")
            print("✓", n)


if __name__ == "__main__":
    main()

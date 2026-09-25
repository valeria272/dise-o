#!/usr/bin/env python3
"""BETWEEN · rediseño de la carta — RONDA 3 (25-09-2026). Mismo contenido y jerarquía que la
ronda 2 (se importa de `between-carta-opciones-r2.py`); cambian las tres pieles.

Feedback de Eli sobre la ronda 2:
  · A «me gusta, pero no destaca, es demasiado plano, le falta diseño». Variar el estilo de
    ilustración y sumar abajo una imagen ilustrativa de ~1/4–1/5 de la página.
      → banda ilustrada al pie de cada hoja (desayuno · pastelería · barra de café), en otro
        estilo que la línea sola: trazo + manchas, pasado a duotono café sobre el beige.
      → secciones en etiqueta café con texto beige: le da contraste y ritmo a la lista.
  · «En todas las opciones sale dos veces el logo» → en la contraportada, sólo abajo.
      Regla que queda: UN logo por hoja (portada e interior arriba, contraportada abajo).
  · B «se parece mucho a la actual y es extraño» → todo el fondo café con textos beige;
      sólo el bloque de arriba va beige con texto café.
  · C «me gusta mucho» → en la hoja 2 fuera la ilustración que más sobresale (el plato);
      fondo de trazos que VARÍE por hoja según lo que se ofrece: desayuno · pastelería · café.
  · «* Foto referencial» se deja en todas las fotos, porque los productos van cambiando.

    python scripts/between-carta-opciones-r3.py
Salida: out/hilton/between/carta-opciones/r3/{html,png,pdf}/
"""
import importlib.util, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_spec = importlib.util.spec_from_file_location(
    "r2", Path(__file__).with_name("between-carta-opciones-r2.py"))
r2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(r2)
from_r2 = ("BEIGE", "CAFE", "TAUPE", "R", "CARTA", "tinta", "pag", "sec", "lista", "lockup",
           "portada_contenido", "interior_contenido", "contra_contenido", "render", "u")
BEIGE, CAFE, TAUPE, R, CARTA, tinta, pag, sec, lista, lockup, portada_contenido, \
    interior_contenido, contra_contenido, render, u = (getattr(r2, n) for n in from_r2)

OUT = r2.RAIZ / "out/hilton/between/carta-opciones/r3"
A_ = r2.BW / "carta"   # recursos versionados (antes en raw/, que no viaja)
R3 = {
    "banda_desayuno": u(A_ / "banda-desayuno.png"),
    "banda_pasteleria": u(A_ / "banda-pasteleria.png"),
    "banda_cafe": u(A_ / "banda-cafe.png"),
    "fondo_desayuno": u(A_ / "fondo-desayuno.png"),
    "fondo_pasteleria": u(A_ / "fondo-pasteleria.png"),
    "fondo_cafe": u(A_ / "fondo-cafe.png"),
}


def contactos(color, fondo_qr, tinta_qr, borde, logo=True):
    """Pie de la contraportada: QR + redes + horario + EL logo (el único de la hoja)."""
    lg = (f'<div class="tinta" style="-webkit-mask-image:url(\'{R["logo"]}\');background:{color};'
          f'width:38mm;height:12mm;flex:none"></div>') if logo else ""
    return f"""
    <div class="abs" style="left:12mm;right:12mm;bottom:12mm;display:flex;align-items:center;gap:7mm;color:{color}">
      <div style="width:33mm;height:33mm;flex:none;background:{fondo_qr};border:{borde};border-radius:2.5mm;padding:2.6mm">
        <div class="tinta" style="-webkit-mask-image:url('{R['qr']}');background:{tinta_qr};width:100%;height:100%"></div></div>
      <div style="flex:1">
        <div class="script" style="font-size:19pt">#Síguenos</div>
        <div style="font-size:9pt;font-weight:700;line-height:1.7;margin-top:1mm">@between.coffeebar<br>cafeteriabetween.cl</div>
        <div style="font-size:6.2pt;font-weight:600;letter-spacing:.1em;margin-top:2mm;white-space:nowrap">HORARIO DE APERTURA · 8:00 - 16:30 HRS</div>
      </div>{lg}
    </div>"""


def logo_arriba(color):
    return tinta(R["logo"], color, "left:12mm;top:11mm;width:30mm;height:9mm;-webkit-mask-position:left center")


def fondo_trazos(url, color, opacidad):
    return (f'<div class="tinta abs" style="inset:0;-webkit-mask-image:url(\'{url}\');'
            f'-webkit-mask-size:cover;background:{color};opacity:{opacidad}"></div>')


# ═════════════ A · PAPEL Y TRAZO — con banda ilustrada y secciones en etiqueta ═════════════
def op_a():
    css = f"""
    .hoja{{background:{BEIGE} url('{R['papel']}') center/cover;color:{CAFE}}}
    .sec h2{{display:inline-block;background:{CAFE};color:{BEIGE};padding:1.5mm 3.2mm 1.3mm;border-radius:1mm;font-weight:700;letter-spacing:.2em}}
    .sec .filete{{margin-top:1.6mm}}
    .banda{{position:absolute;left:8mm;right:8mm;-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center bottom;background:{CAFE}}}
    """
    def banda(url, bottom, alto):
        return f'<div class="banda" style="-webkit-mask-image:url(\'{url}\');bottom:{bottom};height:{alto}"></div>'
    p1 = f"""{logo_arriba(CAFE)}
    {tinta(R['ilu_taza'], CAFE, 'right:10mm;top:7mm;width:40mm;height:27mm')}
    {lockup(CAFE, '20mm')}
    <div class="abs" style="left:12mm;right:12mm;top:73mm">{portada_contenido()}</div>
    {banda(R3['banda_desayuno'], '8mm', '38mm')}"""
    p2 = f"""{logo_arriba(CAFE)}
    <div class="script abs" style="right:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    <div class="abs" style="left:12mm;right:12mm;top:30mm">{interior_contenido()}</div>
    {banda(R3['banda_pasteleria'], '12mm', '40mm')}"""
    p3 = f"""
    <div class="script abs" style="left:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    <div class="abs" style="left:12mm;right:12mm;top:25mm">{contra_contenido()}</div>
    {banda(R3['banda_cafe'], '56mm', '36mm')}
    <div class="abs" style="left:12mm;right:12mm;bottom:52mm;height:.3mm;background:{CAFE}"></div>
    {contactos(CAFE, 'transparent', CAFE, f'.3mm solid {CAFE}')}"""
    return [pag(css, p1), pag(css, p2), pag(css, p3)]


# ═════════════ B · FONDO CAFÉ — texto beige, bloque beige arriba sobre la foto ═════════════
def op_b():
    css = f"""
    .hoja{{background:{CAFE};color:{BEIGE}}}
    .foto{{position:absolute;left:0;right:0;top:0;width:100%;object-fit:cover}}
    .bloque{{position:absolute;left:12mm;top:12mm;background:{BEIGE};color:{CAFE}}}
    .it .d{{opacity:.82}}
    """
    p1 = f"""
    <img class="foto" src="{R['f_portada']}" style="height:74mm;object-position:50% 45%">
    <div class="bloque" style="width:86mm;height:62mm">
      {tinta(R['logo'], CAFE, 'left:8mm;top:7mm;width:32mm;height:9mm;-webkit-mask-position:left center')}
      <div class="script abs" style="left:7mm;top:20mm;font-size:34pt">Menú</div>
      <div class="titulo abs" style="left:8mm;top:36mm;font-size:30pt">Desayuno</div>
      <div class="abs" style="left:8mm;bottom:5.5mm;font-size:7.4pt;font-weight:700;letter-spacing:.2em">8:00 A 11:30 HRS</div>
    </div>
    <div class="foto-ref abs" style="right:12mm;top:69mm;color:{BEIGE}">* Foto referencial</div>
    <div class="abs" style="left:12mm;right:12mm;top:84mm">{portada_contenido()}</div>"""
    p2 = f"""
    <img class="foto" src="{R['f_yogur']}" style="height:58mm;object-position:50% 40%">
    <div class="bloque" style="width:64mm;height:40mm">
      {tinta(R['logo'], CAFE, 'left:8mm;top:7mm;width:30mm;height:8mm;-webkit-mask-position:left center')}
      <div class="script abs" style="left:7mm;top:18mm;font-size:30pt">Tentaciones</div>
    </div>
    <div class="foto-ref abs" style="right:12mm;top:53mm;color:{BEIGE}">* Foto referencial</div>
    <div class="abs" style="left:12mm;right:12mm;top:68mm">{interior_contenido()}</div>
    {tinta(R3['banda_pasteleria'], BEIGE, 'left:8mm;right:8mm;bottom:12mm;height:36mm;-webkit-mask-position:center bottom')}"""
    p3 = f"""
    <img class="foto" src="{R['f_tazas']}" style="height:50mm;object-position:50% 70%">
    <div class="bloque" style="width:64mm;height:26mm;top:12mm">
      <div class="script abs" style="left:7mm;top:5mm;font-size:30pt">Cafetería</div>
    </div>
    <div class="foto-ref abs" style="right:12mm;top:45mm;color:{BEIGE}">* Foto referencial</div>
    <div class="abs" style="left:12mm;right:12mm;top:60mm">{contra_contenido()}</div>
    <div class="abs" style="left:12mm;right:12mm;bottom:52mm;height:.3mm;background:{BEIGE};opacity:.6"></div>
    {contactos(BEIGE, BEIGE, CAFE, 'none')}"""
    return [pag(css, p1), pag(css, p2), pag(css, p3)]


# ═════════════ C · TAUPE Y STICKER — trazos de fondo por tema ═════════════
def op_c():
    css = (f".hoja{{background:{TAUPE};color:{BEIGE}}} "
           ".sticker{position:absolute;filter:drop-shadow(0 1.2mm 1.6mm rgba(20,14,8,.35))}")
    p1 = f"""{fondo_trazos(R3['fondo_desayuno'], BEIGE, .075)}{logo_arriba(BEIGE)}
    <img class="sticker" src="{R['st_croissant']}" style="right:8mm;top:20mm;width:56mm;transform:rotate(-6deg)">
    <div class="abs" style="left:12mm;top:26mm;color:{BEIGE}">
      <div class="script" style="font-size:44pt">Menú</div>
      <div class="titulo" style="font-size:40pt;margin-top:1mm">Desayuno</div>
      <div style="margin-top:4mm"><span style="display:inline-block;border:.35mm solid {BEIGE};border-radius:50%;padding:1.6mm 5mm;font-size:8pt;font-weight:700;letter-spacing:.14em">8:00 A 11:30 HRS</span></div>
    </div>
    <div class="foto-ref abs" style="right:12mm;top:70mm">* Foto referencial</div>
    <div class="abs" style="left:12mm;right:12mm;top:84mm">{portada_contenido(reglas=True)}</div>"""
    p2 = f"""{fondo_trazos(R3['fondo_pasteleria'], BEIGE, .075)}{logo_arriba(BEIGE)}
    <div class="script abs" style="right:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    <div class="abs" style="left:12mm;right:12mm;top:30mm">{interior_contenido(reglas=True)}</div>"""
    p3 = f"""{fondo_trazos(R3['fondo_cafe'], BEIGE, .075)}
    <div class="script abs" style="left:12mm;top:10mm;font-size:20pt">Menú Desayuno</div>
    <img class="sticker" src="{R['st_latte']}" style="right:12mm;top:200mm;width:40mm;transform:rotate(8deg)">
    <div class="foto-ref abs" style="right:12mm;top:243mm">* Foto referencial</div>
    <div class="abs" style="left:12mm;right:12mm;top:28mm">{contra_contenido(reglas=True)}</div>
    <div class="abs" style="left:12mm;right:12mm;bottom:52mm;height:.3mm;background:{BEIGE};opacity:.6"></div>
    {contactos(BEIGE, BEIGE, TAUPE, 'none')}"""
    return [pag(css, p1), pag(css, p2), pag(css, p3)]


OPCIONES = {"A": op_a, "B": op_b, "C": op_c}
HOJAS = ["1-portada", "2-interior", "3-contraportada"]


def main():
    for d in ("html", "png", "pdf"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    for k in (sys.argv[1:] or list(OPCIONES)):
        for hoja, html in zip(HOJAS, OPCIONES[k]()):
            n = f"BW-CARTA-R3-OP{k}-{hoja}"
            h = OUT / "html" / f"{n}.html"
            h.write_text(html, encoding="utf-8")
            render(h, OUT / "png" / f"{n}.png", OUT / "pdf" / f"{n}.pdf")
            print("✓", n)


if __name__ == "__main__":
    main()

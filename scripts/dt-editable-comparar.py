#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la página de comparación del editable: aprobada vs Illustrator.

⭐ Por qué en HTML y con recortes a tamaño real: el editable se juzga MIRÁNDOLO
y comparado, no por un número (memoria `antes-y-despues-en-html`). Los números
van abajo.

Lo que compara es el efecto del ajuste que Illustrator le pone solo a todo SVG
que abre — **Efectos de rasterizado a 72 ppi y con el suavizado apagado**—, que
es lo que ensucia la sombra paralela del titular.
"""
import base64
import io
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
DIR = RAIZ / "out/hilton/dt/ft-honors"
VER = DIR / "editable/_verificacion"

FUENTES = [
    ("La aprobada", "El render de Remotion que aprobaste el 15-09", DIR / "Post n°1 S4 DT.png"),
    ("Illustrator · 72 ppi", "Como abre el SVG por defecto — la sombra rasterizada a 72 ppi y SIN suavizado",
     VER / "desde-illustrator.png"),
    ("Illustrator · 300 ppi", "Con Efectos de rasterizado en 300 ppi y suavizado activado",
     VER / "desde-illustrator-300ppi.png"),
]

# Recortes en píxeles del máster (2250×2813).
RECORTES = [
    ("El titular, a tamaño real", (330, 1150, 1930, 1520), 1.0),
    ("Detalle al 300 % — acá se ve la sombra", (600, 1150, 1000, 1290), 3.0),
    ("Un rótulo del cuadro al 300 %", (455, 1770, 855, 1910), 3.0),
]


def png64(im: Image.Image) -> str:
    b = io.BytesIO()
    im.save(b, "PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode("ascii")


def main() -> int:
    ims = {}
    for nom, _, ruta in FUENTES:
        if not ruta.exists():
            print(f"⛔ falta {ruta}")
            return 1
        ims[nom] = Image.open(ruta).convert("RGB")

    F = []
    F.append("<!doctype html><meta charset=utf-8><title>Editable DT — calidad</title>")
    F.append("""<style>
      :root{--tinta:#09194E;--papel:#F2F4F6}
      body{margin:0;background:var(--papel);color:var(--tinta);
           font:15px/1.55 -apple-system,'Segoe UI',system-ui,sans-serif}
      .caja{max-width:1180px;margin:0 auto;padding:40px 24px 80px}
      h1{font-size:30px;margin:0 0 6px;letter-spacing:-.02em}
      .bajada{opacity:.72;margin:0 0 36px;max-width:64ch}
      h2{font-size:14px;letter-spacing:.09em;text-transform:uppercase;opacity:.6;
         margin:44px 0 14px;border-top:1px solid rgba(9,25,78,.16);padding-top:14px}
      .fila{display:flex;gap:14px;flex-wrap:wrap}
      .col{flex:1 1 320px;min-width:0}
      .rot{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
           margin-bottom:5px}
      .nota{font-size:12px;opacity:.62;margin:0 0 8px;min-height:2.6em}
      img{width:100%;display:block;border-radius:5px;background:#000}
      .mal{color:#CF4800}.bien{color:#2E7D32}
      table{border-collapse:collapse;font-size:13.5px;width:100%;margin-top:8px}
      th,td{text-align:left;padding:7px 12px 7px 0;border-bottom:1px solid rgba(9,25,78,.12)}
      th{font-weight:600;opacity:.6;font-size:12px;letter-spacing:.05em;text-transform:uppercase}
      code{background:rgba(9,25,78,.07);padding:1px 6px;border-radius:4px;font-size:.92em}
      @media (prefers-color-scheme:dark){
        :root{--tinta:#E8EBF0;--papel:#0B1220}
        th,td{border-color:rgba(232,235,240,.14)}
        h2{border-color:rgba(232,235,240,.14)}
        code{background:rgba(232,235,240,.1)}}
    </style>""")
    F.append('<div class="caja">')
    F.append("<h1>El editable en Illustrator — de dónde venía la mala calidad</h1>")
    F.append('<p class="bajada">Illustrator le pone a <b>todo SVG que abre</b> los '
             "Efectos de rasterizado en <b>72 ppi con el suavizado apagado</b>. La sombra "
             "paralela del titular es un efecto, así que se calculaba a 1080 px y con el "
             "canto duro — y al exportar al 208 % esa sombra se amplía. La geometría "
             "nunca estuvo mal: Illustrator puso las doce líneas base exactamente donde "
             "el archivo las manda.</p>")

    for titulo, caja, zoom in RECORTES:
        F.append(f"<h2>{titulo}</h2>")
        F.append('<div class="fila">')
        for nom, nota, _ in FUENTES:
            im = ims[nom].crop(caja)
            if zoom != 1.0:
                im = im.resize((int(im.width * zoom), int(im.height * zoom)), Image.NEAREST)
            clase = "mal" if "72" in nom else ("bien" if "300" in nom else "")
            F.append(f'<div class="col"><div class="rot {clase}">{nom}</div>'
                     f'<p class="nota">{nota}</p><img src="{png64(im)}"></div>')
        F.append("</div>")

    F.append("<h2>Los números</h2>")
    F.append("<table><tr><th>Zona</th><th>72 ppi</th><th>300 ppi</th></tr>"
             "<tr><td>Titular y su sombra — diferencia media contra la aprobada</td>"
             "<td class=mal>17,54</td><td class=bien>10,52</td></tr>"
             "<tr><td>Titular y su sombra — píxeles que se despegan más de 16</td>"
             "<td class=mal>15,43 %</td><td class=bien>11,35 %</td></tr>"
             "<tr><td>Pieza entera — diferencia media</td>"
             "<td>7,54</td><td class=bien>6,19</td></tr></table>")
    F.append("<p class=nota style='margin-top:14px'>Lo que queda de diferencia no se "
             "corrige con ajustes: Illustrator y Chrome no dibujan igual ni las letras "
             "ni un desenfoque gaussiano. Las líneas base coinciden a tres decimales.</p>")

    F.append("<h2>Cómo dejarlo así en cualquier archivo</h2>")
    F.append("<p><b>Efecto › Ajustes de efectos de rasterizado del documento</b> → "
             "Resolución <b>Alta (300 ppi)</b> y marcar <b>Suavizado</b>. "
             "En este archivo ya quedó guardado así.</p>")
    F.append("<p class=nota>Y ojo con el zoom: la mesa es de 1080 pt y entregas a 2250, "
             "así que al 49 % estabas viendo un cuarto del tamaño real. "
             "Para juzgar nitidez, <code>Ver › Tamaño real</code> y de ahí al 208 %.</p>")
    F.append("</div>")

    salida = DIR / "editable/CALIDAD - antes y despues.html"
    salida.write_text("\n".join(F), encoding="utf-8")
    print(f"✅ {salida.relative_to(RAIZ)}  ({salida.stat().st_size / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

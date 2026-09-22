#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión — BETWEEN, la dirección al pie de la portada PROMOS TO GO.

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
Acá hay que mirar tres cosas y las tres están una al lado de la otra:

  1. el antes y el después de la portada (la única diferencia es la línea del pie);
  2. la LÁMINA DE ELI de la que se calcó la dirección, al mismo aumento;
  3. lo medido, que es lo que dice que el calco está bien y no «parecido».

    python scripts/between-revision-direccion-22-09.py
"""
import base64
import io
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "out/hilton/between/revision-direccion-22-09.html"

ANTES = "out/hilton/between/entrega-togo-r25/BW FEED 22-09 Promos To Go 1 portada.png"
DESPUES = "out/hilton-between-togo-r30/BW-F-ToGo-1-Direccion.png"
LAMINA_ELI = "raw/hilton/between/de-eli/cumple-s2-v2/C1 S2 CUMPLE N1.png"


def dato(ruta, ancho=880, recorte=None, calidad=86):
    p = RAIZ / ruta
    if not p.is_file():
        return None
    im = Image.open(p).convert("RGB")
    if recorte:
        im = im.crop(recorte)
    if im.width > ancho:
        im = im.resize((ancho, round(ancho * im.height / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def fig(ruta, pie, ancho=880, recorte=None):
    d = dato(ruta, ancho, recorte)
    if not d:
        return f'<figure class="falta"><div>falta {ruta}</div></figure>'
    return f'<figure><img src="{d}" alt=""><figcaption>{pie}</figcaption></figure>'


# el pie de las láminas, al mismo aumento: 700 px de alto desde el canto inferior
PIE_PORTADA = (0, 2812 - 700, 2250, 2812)
PIE_ELI = (0, 2813 - 700, 2250, 2813)

CSS = """
:root{
  --papel:#F3F0EA; --superficie:#FFFFFF; --tinta:#2A231B; --tinta2:#6C6252;
  --linea:#E0D9CD; --ok:#4F7A3A; --ojo:#A8571E;
  --sombra:0 1px 2px rgba(42,35,27,.06), 0 10px 30px rgba(42,35,27,.07);
  --sans:'Helvetica Neue',Arial,sans-serif;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --papel:#14110D; --superficie:#1D1913; --tinta:#F0EAE0; --tinta2:#A79C8A;
    --linea:#332C22; --ok:#9CC47F; --ojo:#E0A263;
    --sombra:0 1px 2px rgba(0,0,0,.45), 0 10px 30px rgba(0,0,0,.3);
  }
}
:root[data-theme="dark"]{
  --papel:#14110D; --superficie:#1D1913; --tinta:#F0EAE0; --tinta2:#A79C8A;
  --linea:#332C22; --ok:#9CC47F; --ojo:#E0A263;
}
*{box-sizing:border-box}
body{margin:0;background:var(--papel);color:var(--tinta);font-family:var(--sans);
     line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:48px 16px 96px}
h1{font-size:clamp(26px,4.2vw,42px);line-height:1.1;margin:0 0 10px;letter-spacing:-.02em}
h2{font-size:clamp(19px,2.4vw,26px);margin:56px 0 6px;letter-spacing:-.01em}
p{margin:8px 0 0;max-width:72ch;color:var(--tinta2)}
p.fuerte{color:var(--tinta)}
.par{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:22px;margin-top:22px}
figure{margin:0;background:var(--superficie);border:1px solid var(--linea);
       border-radius:14px;overflow:hidden;box-shadow:var(--sombra)}
figure img{display:block;width:100%;height:auto}
figcaption{padding:11px 14px;font-size:13px;color:var(--tinta2);border-top:1px solid var(--linea)}
.falta{padding:30px;text-align:center;color:var(--ojo);font-size:14px}
table{border-collapse:collapse;margin-top:18px;font-size:14px;width:100%;max-width:760px}
th,td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--linea)}
th{color:var(--tinta2);font-weight:600}
td.ok{color:var(--ok)}
.nota{margin-top:26px;padding:14px 16px;border-left:3px solid var(--ojo);
      background:var(--superficie);border-radius:0 10px 10px 0;font-size:14px}
"""

HTML = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Between · la direccion al pie</title>
<style>{CSS}</style></head>
<body><div class="wrap">

<h1>La direccion al pie de la portada To Go</h1>
<p class="fuerte">Scarlette, por Slack: «le puedes sumar la direccion a esta portada
porfiss». Es lo unico que cambia — el resto de la lamina esta intacto pixel a pixel.</p>
<p>Sube a <strong>C1 S4 como archivo aparte</strong>: la portada que ya estaba ahi no
se toco, asi que ningun enlace que circule cambia de contenido.</p>

<h2>Antes y despues</h2>
<div class="par">
  {fig(ANTES, "ANTES — la portada del 16-09, la que tiene Scarlette a la vista")}
  {fig(DESPUES, "DESPUES — la misma, con la direccion al pie")}
</div>

<h2>El pie, de cerca — y de donde salio</h2>
<p>La linea no se invento: esta <strong>calcada</strong> de la lamina
<code>C1 S2 CUMPLE N1</code> que hizo Eli el 07-09, que es el unico antecedente de
direccion sobre una pieza de feed y nacio del mismo pedido del cliente.</p>
<div class="par">
  {fig(DESPUES, "La portada nueva — ultimos 700 px", recorte=PIE_PORTADA)}
  {fig(LAMINA_ELI, "La lamina de Eli — mismos 700 px, mismo aumento", recorte=PIE_ELI)}
</div>

<h2>Lo medido</h2>
<table>
  <tr><th>&nbsp;</th><th>Lamina de Eli</th><th>Portada nueva</th></tr>
  <tr><td>Altura de versal</td><td>43 px</td><td class="ok">43 px</td></tr>
  <tr><td>Ancho de la linea</td><td>879 px</td><td class="ok">877 px</td></tr>
  <tr><td>Linea de base</td><td>a 79 px del canto</td><td class="ok">a 78 px</td></tr>
  <tr><td>Centro de la tinta</td><td>1123</td><td class="ok">1123</td></tr>
  <tr><td>Ancho de asta</td><td>5 / 5,4</td><td class="ok">6 / 5,9</td></tr>
</table>
<p>El peso salio de ahi: el semibold del resto del sistema daba 7 px de asta y un
35 % mas de tinta que la de ella. Queda <strong>Medium</strong>.</p>
<p>Contraste de la linea sobre su fondo, por el peor tramo: <strong>5,0:1</strong>
(la vara del texto chico son 4,5:1). Margenes: 685 px por lado, contra los 175 de
minimo. QA automatico: limpia.</p>

<div class="nota">
  <strong>Lo que sigue igual y hay que tener a la vista:</strong> esta portada es la
  del vaso sobre la mesa, no la de la entrada — esa sigue publicada al lado, sin
  tocar. Y el aviso de carrusel de siempre: contra sus tres hermanas queda 20 puntos
  mas oscura y 16 mas calida. Es la foto, no la direccion.
</div>

</div></body></html>
"""

SALIDA.parent.mkdir(parents=True, exist_ok=True)
SALIDA.write_text(HTML, encoding="utf-8")
print(f"✅ {SALIDA}  ({SALIDA.stat().st_size / 1024:.0f} KB)")

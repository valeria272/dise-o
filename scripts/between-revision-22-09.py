#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión del 22-09-2026 de BETWEEN — la portada del carrusel
PROMOS TO GO vuelve a la foto de la entrada.

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
Acá hay poco que mirar —es una reversión— pero igual se entrega la página, porque
lo que SÍ hay que mirar es el carrusel completo con la portada nueva puesta.

Estilo y utilidades copiados de `between-revision-16-09.py`.

    python scripts/between-revision-22-09.py
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
SALIDA = RAIZ / "out/hilton/between/revision-22-09.html"

ENTREGA = "out/hilton-between-togo-r29/BW-F-ToGo-1.png"
ANTES = "out/hilton/between/entrega-togo-r25/BW FEED 22-09 Promos To Go 1 portada.png"
CRUDA = "raw/hilton/between/vasos-togo-sep2026/jpg/IMG_4170.jpg"
SLIDES = [
    ("out/hilton/between/entrega-togo-r26/BW FEED 22-09 Promos To Go 2 sandwich.png", "2 · Café + Sándwich"),
    ("out/hilton/between/entrega-togo-r26/BW FEED 22-09 Promos To Go 3 dulce.png", "3 · Café + Dulce"),
    ("out/hilton/between/entrega-togo-r26/BW FEED 22-09 Promos To Go 4 los tres.png", "4 · Los tres"),
]


def img(ruta, ancho=880, calidad=84):
    p = RAIZ / ruta if not Path(ruta).is_absolute() else Path(ruta)
    if not p.is_file():
        return None
    im = Image.open(p).convert("RGB")
    if im.width > ancho:
        im = im.resize((ancho, round(ancho * im.height / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def lam(ruta, pie, ancho=880):
    d = img(ruta, ancho)
    if not d:
        return f'<figure class="falta"><div>falta {ruta}</div></figure>'
    return f'<figure><img src="{d}" alt=""><figcaption>{pie}</figcaption></figure>'


CSS = """
:root{
  --papel:#F3F0EA; --superficie:#FFFFFF; --tinta:#2A231B; --tinta2:#6C6252;
  --cafe:#675B49; --beige:#FFF9EB; --linea:#E0D9CD; --ok:#4F7A3A; --ojo:#A8571E;
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
header h1{font-size:clamp(28px,4.4vw,44px);line-height:1.1;margin:0 0 8px;letter-spacing:-.02em}
header p.sub{margin:0;color:var(--tinta2);font-size:17px}
.tag{display:inline-block;background:var(--cafe);color:var(--beige);font-size:12px;
     letter-spacing:.16em;text-indent:.16em;padding:7px 14px;border-radius:999px;
     font-weight:800;margin-bottom:18px}
section{background:var(--superficie);border:1px solid var(--linea);border-radius:18px;
        padding:28px;margin-top:34px;box-shadow:var(--sombra)}
section h2{font-size:clamp(20px,2.6vw,28px);margin:0 0 6px;letter-spacing:-.01em}
section .que{color:var(--tinta2);margin:0 0 22px;font-size:16px}
blockquote{margin:0 0 22px;padding:12px 18px;border-left:3px solid var(--cafe);
           background:rgba(103,91,73,.07);border-radius:0 10px 10px 0;
           color:var(--tinta);font-size:16px}
blockquote small{display:block;color:var(--tinta2);margin-top:6px;font-size:13px}
.fila{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));align-items:start}
figure{margin:0}
figure img{width:100%;display:block;border-radius:12px;border:1px solid var(--linea);background:#0000}
figcaption{margin-top:9px;font-size:13.5px;color:var(--tinta2)}
figcaption b{color:var(--tinta)}
.falta{padding:40px;border:1px dashed var(--linea);border-radius:12px;color:var(--ojo);text-align:center}
.notas{margin:24px 0 0;padding:18px 20px;background:rgba(103,91,73,.06);border-radius:12px}
.notas h3{margin:0 0 10px;font-size:13px;letter-spacing:.14em;text-indent:.14em;
          text-transform:uppercase;color:var(--tinta2)}
.notas ul{margin:0;padding-left:20px}
.notas li{margin:5px 0;font-size:15px}
.notas li b{color:var(--tinta)}
table{width:100%;border-collapse:collapse;margin-top:12px;font-size:14.5px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--linea)}
th{color:var(--tinta2);font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:.06em}
td.n{font-variant-numeric:tabular-nums}
.ok{color:var(--ok);font-weight:700}
.ojo{color:var(--ojo);font-weight:700}
a{color:var(--cafe)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) a{color:#D9C7A8}}
footer{margin-top:40px;color:var(--tinta2);font-size:14px}
"""


def main() -> int:
    cuerpo = f"""
<section>
  <h2>1 · La portada vuelve a la foto de la entrada</h2>
  <p class="que">Carrusel <b>PROMOS TO GO</b> · FEED 22-09 · el archivo
     <b>BW FEED 22-09 Promos To Go 1 portada.png</b> de <b>C1 S4</b> ya está reemplazado.
     Mismo archivo de Drive, así que el enlace de la grilla sigue sirviendo.</p>
  <blockquote>«Vuelve a la imagen en la portada que yo había puesto primero […]
     el cliente quiere volver a esa.» <small>Eli, 22-09</small></blockquote>
  <div class="fila">
    {lam(ANTES, '<b>ANTES</b> — lo que estaba en Drive desde el 16-09: el vaso sobre la mesa de listones (IMG_4146)', 430)}
    {lam(ENTREGA, '<b>AHORA</b> — la de la entrada, con el vaso en mano (IMG_4170)', 430)}
  </div>
  <div class="notas">
    <h3>Qué se tocó, y qué no</h3>
    <ul>
      <li><b>Sólo la placa de fondo.</b> Los textos son los que cerraste tú en la ronda 24
          —script y titular en beige sobre la foto, la caja taupe sólo en «PROMOS TO GO»—
          y no se movió ni una línea.</li>
      <li><b>No es «volver a la ronda 23».</b> Aquella llevaba TODO el bloque dentro de una
          caja taupe, que es justo lo que pediste sacar. Esa parte se queda como está hoy.</li>
      <li><b>El degradado del pie vuelve a 0,72</b>, que es el que se calibró contra ESTA foto.
          El 0,60 de ahora se había medido contra la del vaso sobre la mesa, que abajo es clara
          y pareja; acá el tercio inferior son los pantalones crema.</li>
      <li><b>El archivo entregado es el mismo que ya estaba rendido</b> del 14-09
          (<code>out/hilton-between-togo-r25/BW-F-ToGo-1.png</code>), verificado por md5. El
          código quedó apuntando a esa foto, así que la pieza se vuelve a rendir igual si hace falta.</li>
    </ul>
  </div>
  <table>
    <tr><th>Contraste de la tinta beige sobre la foto</th><th>Peor tramo</th><th>Criterio</th></tr>
    <tr><td>Script «¿Vas con poco tiempo?»</td><td class="n">4,49:1</td><td>la marca pide 3:1 <span class="ok">✓</span></td></tr>
    <tr><td>Titular «TU DESAYUNO VA CONTIGO»</td><td class="n">5,48:1</td><td><span class="ok">✓</span></td></tr>
    <tr><td>Horario «LUNES A VIERNES · 08:00 A 10:00 HRS.»</td><td class="n">6,51:1</td><td><span class="ok">✓</span></td></tr>
    <tr><td>Con el degradado en 0,60 (el de la foto anterior)</td><td class="n">3,59 · 4,28 · 5,01</td>
        <td>pasa, pero el script queda al filo <span class="ojo">→ se deja 0,72</span></td></tr>
  </table>
</section>

<section>
  <h2>2 · El carrusel completo, con la portada puesta</h2>
  <p class="que">Las slides 2, 3 y 4 son las del 21-09 y no se tocaron.</p>
  <div class="fila">
    {lam(ENTREGA, '<b>1 · portada</b>', 270)}
    {''.join(lam(r, f'<b>{t}</b>', 270) for r, t in SLIDES)}
  </div>
  <div class="notas">
    <h3>⚠️ Lo que hay que saber: la portada se sale del tono del carrusel</h3>
    <ul>
      <li>Medido por <code>between-qa.py --carrusel</code>: la portada queda en
          <b>mediana 73 · saturación 23</b> contra <b>102–104 · 37–47</b> de sus tres hermanas.
          El tope del QA son 14 puntos y acá hay 31.</li>
      <li><b>No es un defecto nuevo ni es arreglable con revelado.</b> Ya estaba medido el 14-09:
          es una toma de calle, cromáticamente pobre (croma 9,7 contra 21,5 del set). Igualarle
          el color al carrusel obliga a subir la calidez a 38, o sea a devolverle el
          <i>«filtro cálido»</i> que el cliente mandó eliminar el 31-08.</li>
      <li>La portada anterior tampoco pasaba el chequeo (mediana 84, calidez 37): las dos se
          salen, esta un poco más. <b>Se entrega igual porque la foto la eligió el cliente</b>,
          pero queda anotado.</li>
    </ul>
  </div>
</section>

<section>
  <h2>3 · La foto que mandaste, tal cual</h2>
  <div class="fila">
    {lam(CRUDA, '<b>IMG_4170</b> — sesión del vaso To Go, 09-09. Es la misma que usó la ronda 23.', 430)}
  </div>
  <div class="notas">
    <h3>Las dos cosas que esta portada no trae, y ya estaban informadas</h3>
    <ul>
      <li><b>No se le ve la cara:</b> las 18 tomas del bloque tienen la cabeza cortada por el encuadre.</li>
      <li><b>No hay bolsa To Go</b>, que el brief pedía («café y bolsa To Go en mano»).</li>
    </ul>
  </div>
</section>
"""

    html = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Between · Portada To Go</title>
<style>{CSS}</style></head>
<body><div class="wrap">
<header>
  <div class="tag">BETWEEN · 22-09-2026</div>
  <h1>La portada del carrusel Promos To Go vuelve a la foto de la entrada</h1>
  <p class="sub">Reemplazada en Drive sobre el mismo archivo · carpeta <b>C1 S4</b></p>
</header>
{cuerpo}
<footer>Página generada por <code>scripts/between-revision-22-09.py</code>.</footer>
</div></body></html>
"""
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(html, encoding="utf-8")
    print(f"-> {SALIDA}  ({SALIDA.stat().st_size/1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

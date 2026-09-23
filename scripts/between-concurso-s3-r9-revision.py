#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión de la RONDA 9 del carrusel CONCURSO de Between (21-09-2026).

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
El rótulo pierde la caja y crece; el titular va en las tres versiones que pidió Eli,
que son los dos recursos de la REF 1 más la variante sin Brushwell. La página las pone
al tamaño de publicación y ampliadas, que es donde se decide.

Las imágenes van EMBEBIDAS en JPEG: la página es un solo archivo y se abre con
doble clic, sin servidor.

    python scripts/between-concurso-s3-r9-revision.py
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
DIR = "out/hilton/between/concurso-s3-r9/"
SALIDA = RAIZ / DIR / "revision-r9.html"

#: ⚠️ El «antes» de esta ronda es la opción A de la ronda 6 —lo que Eli miró y
#: eligió—, copiada a esta carpeta para que no se la lleve un re-render.
ANTES = DIR + "antes-r8-op3.png"
FINAL = DIR + "final-1.png"
SLIDE2 = DIR + "slide2.png"


def _data(im, calidad=86):
    b = io.BytesIO()
    im.save(b, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def img(ruta, ancho=880, calidad=86):
    p = RAIZ / ruta
    if not p.is_file():
        return None
    im = Image.open(p).convert("RGB")
    if im.width > ancho:
        im = im.resize((ancho, round(ancho * im.height / im.width)), Image.LANCZOS)
    return _data(im, calidad)


def recorte(ruta, caja1080, escala=1.6, calidad=90):
    """Un detalle de la lámina. `caja1080` va en coordenadas del lienzo de 1080."""
    p = RAIZ / ruta
    if not p.is_file():
        return None
    im = Image.open(p).convert("RGB")
    k = im.width / 1080
    x0, y0, x1, y1 = [round(v * k) for v in caja1080]
    im = im.crop((x0, y0, x1, y1))
    im = im.resize((round((x1 - x0) * escala), round((y1 - y0) * escala)), Image.LANCZOS)
    return _data(im, calidad)


def lam(ruta, pie, ancho=880):
    d = img(ruta, ancho)
    if not d:
        return '<figure class="falta"><div>falta %s</div></figure>' % ruta
    return '<figure><img src="%s" alt=""><figcaption>%s</figcaption></figure>' % (d, pie)


def det(ruta, caja1080, pie, escala=1.6, caja_directa=None):
    """`caja_directa` va en pixeles del archivo (la referencia no mide 1080)."""
    if caja_directa:
        q = RAIZ / ruta
        if not q.is_file():
            return '<figure class="falta"><div>falta %s</div></figure>' % ruta
        im = Image.open(q).convert("RGB").crop(caja_directa)
        if im.width > 900:
            im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
        d = _data(im, 88)
    else:
        d = recorte(ruta, caja1080, escala)
    if not d:
        return '<figure class="falta"><div>falta %s</div></figure>' % ruta
    return '<figure><img src="%s" alt=""><figcaption>%s</figcaption></figure>' % (d, pie)


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
.tres{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));align-items:start}
.dos{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));align-items:start}
figure{margin:0}
figure img{width:100%;display:block;border-radius:12px;border:1px solid var(--linea)}
figcaption{margin-top:9px;font-size:13.5px;color:var(--tinta2)}
figcaption b{color:var(--tinta)}
.falta{padding:40px;border:1px dashed var(--linea);border-radius:12px;color:var(--ojo);text-align:center}
.notas{margin:24px 0 0;padding:18px 20px;background:rgba(103,91,73,.06);border-radius:12px}
.notas h3{margin:0 0 10px;font-size:13px;letter-spacing:.14em;text-indent:.14em;
          text-transform:uppercase;color:var(--tinta2)}
.notas ul{margin:0;padding-left:20px}
.notas li{margin:7px 0;font-size:15px}
.notas li b{color:var(--tinta)}
.elige{border:2px solid var(--cafe);background:rgba(103,91,73,.09)}
table{width:100%;border-collapse:collapse;margin-top:12px;font-size:14.5px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--linea)}
th{color:var(--tinta2);font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:.06em}
td.n{font-variant-numeric:tabular-nums}
.ok{color:var(--ok);font-weight:700}
.ojo{color:var(--ojo);font-weight:700}
code{background:rgba(103,91,73,.12);padding:1px 6px;border-radius:5px;font-size:.92em}
a{color:var(--cafe)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) a{color:#D9C7A8}}
footer{margin-top:40px;color:var(--tinta2);font-size:14px}
"""


def main() -> int:
    partes = []

    partes.append("""
<section>
  <h2>Lo que pediste</h2>
  <blockquote>&laquo;Quiero la <b>opci&oacute;n 3</b>, pero con lo del CEO ese texto <b>en cajita con un leve
    &aacute;ngulo como la referencia</b>, y el &ldquo;se busca&rdquo; <b>aumenta un poco el grosor del beige</b>.&raquo;
    <small>Eli &middot; 21-09</small></blockquote>
  <p class="que">Los tres cambios est&aacute;n aplicados: la l&iacute;nea de arriba sigue siendo la de la opci&oacute;n 3
     &mdash;Raleway, una sola tipograf&iacute;a, como el referente&mdash; con el halo m&aacute;s grueso, y
     &laquo;CEO DEL CAF&Eacute;&raquo; baja al bloque de color inclinado que es el otro recurso de la REF 1.</p>
</section>""")

    l_antes = lam(ANTES, "<b>ANTES</b> &mdash; opci&oacute;n 3: las dos l&iacute;neas con halo de 12", 420)
    l_fin = lam(FINAL, "<b>AHORA</b> &mdash; halo de 16 arriba, y el CEO en cajita inclinada &minus;3&deg;", 420)
    d_antes = det(ANTES, (280, 400, 820, 600), "<b>ANTES</b>", 1.5)
    d_fin = det(FINAL, (280, 400, 820, 600), "<b>AHORA</b>", 1.5)
    partes.append("""
<section class="elige">
  <h2>El titular</h2>
  <div class="dos">
    %s
    %s
  </div>
  <div class="dos" style="margin-top:22px">
    %s
    %s
  </div>
  <div class="notas">
    <h3>Los tres n&uacute;meros, medidos</h3>
    <ul>
      <li><b>El &aacute;ngulo sale de la referencia, no de la intuici&oacute;n.</b> Aisl&eacute; el azul de la caja de
          la REF 1 y le ajust&eacute; los bordes: el superior da <b>&minus;2,20&deg;</b> y el inferior
          <b>&minus;3,34&deg;</b>. Se tom&oacute; <b>&minus;3&deg;</b>, que cae dentro del rango y coincide con el
          registro que la marca ya usa en sus etiquetas (el sello de la ronda 4 gira &minus;4&deg;).</li>
      <li><b>El halo de &laquo;SE BUSCA:&raquo; sube de 12 a 16 px</b>, o sea 8 por fuera de la letra.</li>
      <li><b>La cajita va taupe con tinta beige</b>, como el bloque de color del referente: 4,19:1
          contra el papel y 6,31:1 por dentro.</li>
      <li>La caja rotada <b>no ocupa lo que dice su alto</b>: sobresale <code>ancho&middot;sen(3&deg;)/2</code>
          &mdash;10 px&mdash; por arriba y por abajo, y eso hubo que descontarlo del aire para que no se le
          acercara a &laquo;&iquest;El sueldo?&raquo;.</li>
    </ul>
  </div>
</section>""" % (l_antes, l_fin, d_antes, d_fin))

    partes.append("""
<section>
  <h2>Lo medido en la l&aacute;mina final</h2>
  <table>
    <tr><th>Control</th><th>Valor</th><th>Vara</th></tr>
    <tr><td>CONCURSO contra el papel</td><td class="n ok">4,14 : 1</td><td>la caja beige daba 1,50 : 1</td></tr>
    <tr><td>Cajita del titular contra el papel</td><td class="n ok">4,19 : 1</td><td>tinta por dentro 6,31 : 1</td></tr>
    <tr><td>Bajada</td><td class="n ok">4,16 : 1</td><td>el contraste del titular aprobado</td></tr>
    <tr><td>Aire r&oacute;tulo &rarr; bajada</td><td class="n">32 px</td>
        <td>1,5&times; el aire entre las l&iacute;neas de la bajada, que es la proporci&oacute;n del manual</td></tr>
    <tr><td>Aire cajita &rarr; &laquo;&iquest;El sueldo?&raquo;</td><td class="n ok">26 px</td>
        <td>con la rotaci&oacute;n ya descontada</td></tr>
    <tr><td>&Uacute;ltima l&iacute;nea de la CTA</td><td class="n">y = 827</td>
        <td>el halo del recorte entra en 847 &rarr; <span class="ok">20 px</span></td></tr>
    <tr><td>Carrusel en el mismo tono</td><td class="n ok">s&iacute;</td><td>mediana 196 / 201</td></tr>
  </table>
</section>""")

    l2 = lam(SLIDE2, "<b>SLIDE 2</b> &mdash; sin cambios desde que la aprobaste", 420)
    partes.append("""
<section>
  <h2>El carrusel completo</h2>
  <div class="dos">
    %s
    %s
  </div>
  <div class="notas">
    <h3>Listo para subir</h3>
    <ul>
      <li>Las dos l&aacute;minas est&aacute;n empaquetadas con el nombre del portal
          &mdash;<code>C1 S3 CONCURSO N1.png</code> y <code>N2.png</code>, 2250&times;2812 a 150 ppp&mdash; en
          <code>out/hilton/between/entrega-c1-s3-concurso/</code>.</li>
      <li><b>No sub&iacute; nada todav&iacute;a.</b> Con tu OK las subo reemplazando el contenido de los
          archivos que ya est&aacute;n en Drive, as&iacute; <b>los enlaces de la grilla no cambian</b>.</li>
      <li>Sigue sin el visto de Scarlette el texto, y el copy de la grilla todav&iacute;a dice
          &laquo;Si yo fuera CEO de Between&raquo;.</li>
    </ul>
  </div>
</section>""" % (lam(FINAL, "<b>SLIDE 1</b>", 420), l2))

    cuerpo = ("<title>Concurso Between &middot; Final</title>\n<style>" + CSS + "</style>\n"
              """<div class="wrap">
<header>
  <div class="tag">BETWEEN &middot; CARRUSEL CONCURSO &middot; RONDA 9</div>
  <h1>La cajita inclinada de la referencia</h1>
  <p class="sub">21-09-2026 &middot; FEED del <b>24 de septiembre</b> (S4) &middot; carrusel completo,
     listo para subir</p>
</header>
""" + ''.join(partes) + """
<footer>P&aacute;gina generada por <code>scripts/between-concurso-s3-r9-revision.py</code>.</footer>
</div>""")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    titulo, resto = cuerpo.split("\n", 1)
    SALIDA.write_text(
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + titulo + "\n</head>\n<body>\n" + resto + "\n</body>\n</html>",
        encoding="utf-8")
    print("ok local: %s (%d KB)" % (SALIDA, SALIDA.stat().st_size // 1024))

    ART = SALIDA.with_name("revision-r9-artefacto.html")
    ART.write_text(cuerpo, encoding="utf-8")
    print("ok artefacto: %s (%d KB)" % (ART, ART.stat().st_size // 1024))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

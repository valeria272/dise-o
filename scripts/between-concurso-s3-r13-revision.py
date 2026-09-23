#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión de la RONDA 13 del carrusel CONCURSO de Between (21-09-2026).

Los dos cambios que mandó Nicolás son de TEXTO, así que lo que hay que mirar no
es el color ni la foto sino si el legal completo cabe y si la frase larga sigue
entrando en dos líneas. Por eso la página va con el antes y el después de la
lámina entera y, debajo, los dos detalles ampliados — que es donde se decide.

Eli aprueba mirando y comparado (memoria `antes-y-despues-en-html`).
Las imágenes van EMBEBIDAS en JPEG: un solo archivo, se abre con doble clic.

    python scripts/between-concurso-s3-r13-revision.py
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
DIR = "out/hilton/between/concurso-s3-r13/"
SALIDA = RAIZ / DIR / "revision-r13.html"

#: El «antes» es la lámina que está HOY en el Drive (la ronda 12), copiada a
#: esta carpeta para que no se la lleve un re-render.
ANTES = DIR + "antes-r12.png"
DESPUES = DIR + "slide2.png"
SLIDE1 = DIR + "slide1.png"


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


def recorte(ruta, caja1080, escala=1.5, calidad=92):
    """Un detalle de la lámina. `caja1080` va en coordenadas del lienzo de 1080."""
    p = RAIZ / ruta
    if not p.is_file():
        return None
    im = Image.open(p).convert("RGB")
    k = im.width / 1080
    x0, y0, x1, y1 = [round(v * k) for v in caja1080]
    im = im.crop((x0, y0, x1, y1))
    ancho = round((x1 - x0) * escala)
    im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    return _data(im, calidad)


def lam(ruta, pie, ancho=880):
    d = img(ruta, ancho)
    if not d:
        return '<figure class="falta"><div>falta %s</div></figure>' % ruta
    return '<figure><img src="%s" alt=""><figcaption>%s</figcaption></figure>' % (d, pie)


def det(ruta, caja1080, pie, escala=1.5):
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
.dos{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));align-items:start}
.una{display:grid;gap:22px}
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
td.n{font-variant-numeric:tabular-nums;text-align:right}
.ok{color:var(--ok);font-weight:700}
.ojo{color:var(--ojo);font-weight:700}
code{background:rgba(103,91,73,.12);padding:1px 6px;border-radius:5px;font-size:.92em}
a{color:var(--cafe)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) a{color:#D9C7A8}}
footer{margin-top:40px;color:var(--tinta2);font-size:14px}
"""


def main() -> int:
    partes = []

    # ── 1 · LA LÁMINA ENTERA ──────────────────────────────────────────────
    partes.append("""
<section class="elige">
  <h2>Los dos cambios, en la l&aacute;mina entera</h2>
  <blockquote>
    &laquo;Agregar este Legal: *Concurso v&aacute;lido del 21 al 30 de septiembre. El ganador ser&aacute;
    anunciado el 1 de octubre. Premio: un caf&eacute; diario, para disfrutar en local o en formato To Go
    durante todo el mes de octubre de 2026. Premio personal e intransferible.<br><br>
    Y pidieron cambiar otra vez esto jajaja &ldquo;Si yo fuera CEO del caf&eacute; en Between, mi primera
    acci&oacute;n ser&iacute;a&hellip;&rdquo;&raquo;
    <small>Nicol&aacute;s &Aacute;vila &middot; Slack &middot; 21-09-2026</small>
  </blockquote>
  <div class="dos">
    %s
    %s
  </div>
  <div class="notas">
    <h3>Lo importante</h3>
    <ul>
      <li><b>La slide 1 no se toca.</b> Los dos cambios son de la slide 2.</li>
      <li><b>La l&aacute;mina es la misma que aprobaste.</b> Titular en 150, tarjeta en 320,
          separadores en 18: <b>lo &uacute;nico distinto son los dos textos</b>. Con el legal en tres
          l&iacute;neas ya no hay que mover nada para que quepa.</li>
      <li><b>Nada de abajo se movi&oacute;.</b> La tarjeta cerraba en y=975,0 y cierra en
          <b>y=978,2</b> &mdash; 3 px. La polaroid y el vaso quedan donde estaban, con 25,8 px
          de aire.</li>
    </ul>
  </div>
</section>""" % (
        lam(ANTES, "<b>ANTES</b> &mdash; lo que est&aacute; hoy en el Drive (ronda 12)", 520),
        lam(DESPUES, "<b>AHORA</b> &mdash; legal completo y &laquo;en Between&raquo; en la frase", 520),
    ))

    # ── 2 · LA FRASE, DE CERCA ────────────────────────────────────────────
    partes.append("""
<section>
  <h2>1 &middot; La frase que se completa en los comentarios</h2>
  <p class="que">Va literal como la mand&oacute; contenido. <b>El cuerpo baja de 36 a 34</b> y eso no es
     una licencia: con &laquo;en Between&raquo; adentro, a 36 la primera l&iacute;nea mide <b>645 px</b> y el
     ancho &uacute;til de la tarjeta es <b>630</b> &mdash; Chrome la parte y la cita queda en TRES l&iacute;neas,
     que la subir&iacute;a de nivel por encima del titular. A 34 mide 608 y sigue en las dos l&iacute;neas
     que aprobaste.</p>
  <div class="una">
    %s
    %s
  </div>
  <table>
    <tr><th>Corte</th><th>Cuerpo</th><th class="n">L&iacute;nea larga</th><th>Veredicto</th></tr>
    <tr><td>en la coma</td><td>36</td><td class="n">645,1</td><td class="ojo">se parte &rarr; 3 l&iacute;neas</td></tr>
    <tr><td>antes de &laquo;en Between&raquo;</td><td>36</td><td class="n">654,1</td><td class="ojo">se parte, y corta la marca</td></tr>
    <tr><td><b>en la coma</b></td><td><b>34</b></td><td class="n"><b>608,5</b></td><td class="ok">entra, 21,5 px de aire</td></tr>
  </table>
</section>""" % (
        det(ANTES, (190, 395, 890, 565), "<b>ANTES</b> &mdash; &laquo;CEO del caf&eacute;&raquo;, cuerpo 36"),
        det(DESPUES, (190, 395, 890, 565),
            "<b>AHORA</b> &mdash; &laquo;CEO del caf&eacute; en Between&raquo;, cuerpo 34, dos l&iacute;neas"),
    ))

    # ── 3 · EL LEGAL, DE CERCA ────────────────────────────────────────────
    partes.append("""
<section>
  <h2>2 &middot; El legal completo, en tres l&iacute;neas</h2>
  <p class="que">Palabra por palabra, incluido el asterisco de apertura y el &laquo;de 2026&raquo; que
     s&oacute;lo lleva octubre. Entra el premio &mdash;caf&eacute; diario, en local o To Go, todo octubre&mdash; y la
     intransferibilidad, que no estaban en ninguna de las dos l&aacute;minas. <b>Sigue dentro de la
     tarjeta</b> y no al pie: al pie cruzaba el vaso y le part&iacute;a el logotipo.</p>
  <p class="que"><b>El cuerpo baja de 21 a 17</b>, y 17 no es un n&uacute;mero al azar: es el m&aacute;s grande
     al que el p&aacute;rrafo entero todav&iacute;a entra en tres l&iacute;neas, sin quitar una palabra. A 18 ya son
     cuatro &mdash;la primera l&iacute;nea se pasa por 4 px&mdash; y a 16 pierdes tama&ntilde;o sin ganar nada.</p>
  <div class="una">
    %s
    %s
  </div>
  <table>
    <tr><th>Cuerpo</th><th class="n">L&iacute;neas</th><th class="n">Alto</th><th>Veredicto</th></tr>
    <tr><td>21 (el primer intento)</td><td class="n">4</td><td class="n">112,6</td>
        <td class="ojo">obligaba a mover la l&aacute;mina entera</td></tr>
    <tr><td>18</td><td class="n">4</td><td class="n">96,5</td>
        <td class="ojo">se pasa por 4 px y salta de l&iacute;nea</td></tr>
    <tr><td><b>17</b></td><td class="n"><b>3</b></td><td class="n"><b>68,3</b></td>
        <td class="ok">el mayor que entra en tres</td></tr>
    <tr><td>16</td><td class="n">3</td><td class="n">64,3</td><td>m&aacute;s chico sin ganar l&iacute;neas</td></tr>
  </table>
</section>""" % (
        det(ANTES, (190, 850, 890, 990), "<b>ANTES</b> &mdash; dos frases, cuerpo 21"),
        det(DESPUES, (190, 850, 890, 990),
            "<b>AHORA</b> &mdash; el legal entero en tres l&iacute;neas, cuerpo 17"),
    ))

    # ── 4 · DE DÓNDE SALIERON LOS PÍXELES ─────────────────────────────────
    partes.append("""
<section>
  <h2>Cu&aacute;nto creci&oacute; la tarjeta: 3 px</h2>
  <p class="que">Abajo no hay nada que ceder &mdash;el marco blanco del recorte entra en y=1004 y el
     vaso, con el logotipo impreso, va de 990 a 1341&mdash;, as&iacute; que lo que cabe lo decide el
     cuerpo del legal, no la l&aacute;mina. Con tres l&iacute;neas el crecimiento es de 12 px, la cita
     devuelve 5, y no hay que mover absolutamente nada.</p>
  <table>
    <tr><th>Cambio</th><th class="n">px</th><th>Efecto</th></tr>
    <tr><td>El legal, de 2 l&iacute;neas a 21 px a <b>3 l&iacute;neas a 17</b></td><td class="n">+12,1</td>
        <td>Entra el texto completo ocupando menos alto del que le sobraba</td></tr>
    <tr><td>La cita, 36 &rarr; 34</td><td class="n">&minus;5,0</td>
        <td>Obligada: a 36 se parte en tres l&iacute;neas</td></tr>
    <tr><td><b>Total</b></td><td class="n"><b>+7,1</b></td>
        <td class="ok">Nada m&aacute;s se toca: titular 150, tarjeta 320, separadores 18/14</td></tr>
  </table>
  <div class="notas">
    <h3>Medido sobre el render</h3>
    <ul>
      <li>Tarjeta <b>y 320,2 &rarr; 978,2</b> &middot; antes 320,2 &rarr; 975,0.
          <b>3,2 px m&aacute;s abajo.</b></li>
      <li>Aire tarjeta &rarr; marco del recorte: <b>25,8 px</b>. Nada se toca ni se tapa.</li>
      <li>Tinta del titular <b>y 148,8 &rarr; 295,7</b>, igual que en la l&aacute;mina aprobada
          &middot; margen de marca 84.</li>
      <li>QA de Between: <b class="ok">slide 2 limpia</b> &middot; carrusel en el mismo tono (197 / 201)
          &middot; <code>npm run typecheck</code> limpio.</li>
      <li>Todo esto se vuelve a correr con
          <code>python scripts/between-concurso-s3-r13-medir.py</code>.</li>
    </ul>
  </div>
</section>""")

    # ── 5 · LO QUE HAY QUE MIRAR ──────────────────────────────────────────
    partes.append("""
<section>
  <h2>Tres cosas para que decidas t&uacute;</h2>
  <div class="notas">
    <h3>Ninguna bloquea la entrega</h3>
    <ul>
      <li><b>El asterisco queda.</b> Nicol&aacute;s lo escribi&oacute; abriendo el legal y los textos de cliente
          van literales, as&iacute; que lo dej&eacute;. <b>Pero no tiene a qui&eacute;n referirse:</b> no hay otro
          asterisco en el carrusel. Si quieres, se lo pongo a &laquo;1 MES DE CAF&Eacute; GRATIS&raquo; en la
          portada &mdash;que es el dato que el legal matiza&mdash; o lo saco. Un minuto cualquiera de las
          dos.</li>
      <li><b>Las cifras del legal bajan de la l&iacute;nea base</b> (&laquo;30&raquo;, &laquo;2026&raquo;) &mdash; es lo mismo que
          marcaste en el carrusel To Go. Lo intent&eacute; arreglar y <b>no se puede</b>: la it&aacute;lica de
          Raleway no trae la funci&oacute;n <code>lnum</code>, s&oacute;lo la redonda. Verificado con fontTools
          sobre los .ttf del repo. La &uacute;nica salida ser&iacute;a poner el legal en redonda; no lo hice
          porque la it&aacute;lica es la que aprobaste y el defecto ya viene en la l&aacute;mina publicada.</li>
      <li><b>La slide 1 tiene un aviso viejo del QA</b> &mdash;&laquo;texto a 74 px del borde derecho&raquo;&mdash;
          que ya estaba en la versi&oacute;n que se entreg&oacute; y aprob&oacute;. No lo toqu&eacute;: cambiarlo mueve una
          l&aacute;mina cerrada. Queda anotado.</li>
    </ul>
  </div>
</section>""")

    # ── 6 · EL CARRUSEL ───────────────────────────────────────────────────
    partes.append("""
<section>
  <h2>El carrusel como se publica</h2>
  <div class="dos">
    %s
    %s
  </div>
  <div class="notas">
    <h3>Entrega</h3>
    <ul>
      <li><code>C1 S3 CONCURSO N1.png</code> y <code>C1 S3 CONCURSO N2.png</code>, 2250&times;2812 a
          150 ppp.</li>
      <li>Se suben <b>reemplazando los mismos archivos</b> de la carpeta del Drive, para que no
          cambien los enlaces.</li>
    </ul>
  </div>
</section>""" % (
        lam(SLIDE1, "<b>SLIDE 1</b> &mdash; sin cambios", 420),
        lam(DESPUES, "<b>SLIDE 2</b> &mdash; ronda 13", 420),
    ))

    cuerpo = ("<title>Concurso Between &middot; Ronda 13</title>\n<style>" + CSS + "</style>\n"
              """<div class="wrap">
<header>
  <div class="tag">BETWEEN &middot; CARRUSEL CONCURSO &middot; RONDA 13</div>
  <h1>El legal completo y la frase con la marca adentro</h1>
  <p class="sub">21-09-2026 &middot; los dos cambios que mand&oacute; Nicol&aacute;s por Slack</p>
</header>
""" + ''.join(partes) + """
<footer>P&aacute;gina generada por <code>scripts/between-concurso-s3-r13-revision.py</code>.</footer>
</div>""")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    titulo, resto = cuerpo.split("\n", 1)
    SALIDA.write_text(
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + titulo + "\n</head>\n<body>\n" + resto + "\n</body>\n</html>",
        encoding="utf-8")
    print("ok local: %s (%d KB)" % (SALIDA, SALIDA.stat().st_size // 1024))
    ART = SALIDA.with_name("revision-r13-artefacto.html")
    ART.write_text(cuerpo, encoding="utf-8")
    print("ok artefacto: %s (%d KB)" % (ART, ART.stat().st_size // 1024))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

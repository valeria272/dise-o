#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión de la RONDA 7 del carrusel CONCURSO de Between (21-09-2026).

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
Eli eligió la opción A y pidió tres ajustes. La página pone lo que ella vio al lado
de las dos salidas nuevas —el sello beige y el sello taupe—, que es la única decisión
que queda abierta, con el detalle de la cabecera y del sticker del titular.

Las imágenes van EMBEBIDAS en JPEG: la página es un solo archivo y se abre con
doble clic, sin servidor.

    python scripts/between-concurso-s3-r7-revision.py
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
DIR = "out/hilton/between/concurso-s3-r7/"
SALIDA = RAIZ / DIR / "revision-r7.html"

#: ⚠️ El «antes» de esta ronda es la opción A de la ronda 6 —lo que Eli miró y
#: eligió—, copiada a esta carpeta para que no se la lleve un re-render.
ANTES = DIR + "antes-r6-1.png"
BEIGE, TAUPE = DIR + "beige-1.png", DIR + "taupe-1.png"
SLIDE2 = DIR + "slide2.png"
ANTES2 = "out/hilton/between/concurso-s3-r6/antes-2.png"


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

    # -- 1 - LO QUE PEDISTE ----------------------------------------------
    partes.append("""
<section>
  <h2>Lo que pediste sobre la A</h2>
  <blockquote>&laquo;Me gusta la opci&oacute;n A, apilado todo, como centrado. Lo que s&iacute;, yo creo que
    <b>el texto del concurso podr&iacute;a ir un poco m&aacute;s destacado</b>. Y el texto del &ldquo;se acerca el D&iacute;a
    Internacional&rdquo; s&oacute;lo <b>sumarle un poquitito m&aacute;s de tama&ntilde;o, porque se lee muy poco</b>, no es tan
    visible. Y &ldquo;se busca CEO del caf&eacute;&rdquo; que sea el que <b>est&eacute; en un marco beige</b> [&hellip;] que sea
    <b>como el sticker, igual que la referencia</b>. As&iacute; se achica m&aacute;s el &ldquo;se busca CEO del caf&eacute;&rdquo;
    y el concurso se ve m&aacute;s destacado [&hellip;] En la segunda slide qued&oacute; perfecta.&raquo;
    <small>Eli &middot; 21-09</small></blockquote>
  <table>
    <tr><th>Qu&eacute;</th><th>Antes</th><th>Ahora</th><th>Qu&eacute; significa en la l&aacute;mina</th></tr>
    <tr><td>CONCURSO</td><td class="n">52</td><td class="n"><b>68</b> (+31 %)</td>
        <td>la caja pasa a 515 px de ancho: es el objeto m&aacute;s ancho de la pieza</td></tr>
    <tr><td>Bajada</td><td class="n">30</td><td class="n"><b>36</b> (+20 %)</td>
        <td>a 36 las dos l&iacute;neas miden 654 y 625 px y siguen dentro de la columna de 810</td></tr>
    <tr><td>Titular</td><td class="n">88</td><td class="n"><b>64</b> (&minus;27 %)</td>
        <td>419 px de ancho contra los 515 del r&oacute;tulo</td></tr>
    <tr><td>Marco del titular</td><td>&mdash;</td><td><b>contorno beige de 8 px</b></td>
        <td>el recurso de la REF 1, no una caja rectangular</td></tr>
  </table>
</section>""")

    # -- 2 - EL STICKER --------------------------------------------------
    d_ref = det("raw/hilton/between/refs-concurso-s3/REF1.jpg", None,
                "<b>LA REFERENCIA</b> &mdash; el titular no va en una caja: lleva un contorno claro "
                "pegado a las letras. La caja plana rellena es para el r&oacute;tulo",
                caja_directa=(150, 120, 1050, 530))
    d_stick = det(BEIGE, (250, 408, 830, 602),
                  "<b>AHORA</b> &mdash; el mismo recurso en beige de marca: 8 px de contorno, "
                  "4 por fuera del glifo", 1.5)
    partes.append("""
<section>
  <h2>El &laquo;marco&raquo; es el sticker de la referencia</h2>
  <p class="que">Mir&eacute; la REF 1 antes de tocar nada, porque &laquo;marco beige&raquo; pod&iacute;a ser una caja
     rectangular. No lo es: en la referencia el titular lleva un <b>contorno pegado a las letras</b>
     &mdash;una calcoman&iacute;a&mdash; y la caja plana rellena est&aacute; reservada para el r&oacute;tulo. Ac&aacute; queda igual,
     con el beige de la marca; y el grosor no es a ojo: 8 px a un cuerpo de 64 es la misma
     proporci&oacute;n que tiene el contorno blanco del recorte de la foto, as&iacute; que el titular y la figura
     se leen como piezas del mismo collage.</p>
  <div class="dos">
    %s
    %s
  </div>
</section>""" % (d_ref, d_stick))

    # -- 3 - LA DECISION QUE QUEDA ---------------------------------------
    l_antes = lam(ANTES, "<b>LO QUE VISTE</b> &mdash; CONCURSO 52, bajada 30, titular 88 suelto", 340)
    l_beige = lam(BEIGE, "<b>1 &middot; SELLO BEIGE</b> &mdash; la caja que ya aprobaste, m&aacute;s grande", 340)
    l_taupe = lam(TAUPE, "<b>2 &middot; SELLO TAUPE</b> &mdash; la misma caja invertida: salta m&aacute;s contra el papel", 340)
    d_beige = det(BEIGE, (60, 180, 1020, 600), "<b>BEIGE</b> &mdash; 1,50:1 contra el papel; manda por tama&ntilde;o y por sitio")
    d_taupe = det(TAUPE, (60, 180, 1020, 600), "<b>TAUPE</b> &mdash; 4,15:1 contra el papel; manda adem&aacute;s por contraste")
    partes.append("""
<section class="elige">
  <h2>Lo &uacute;nico que queda por elegir: el color del sello</h2>
  <p class="que">&laquo;Que destaque m&aacute;s&raquo; se puede leer de dos maneras y las dos est&aacute;n rendidas.
     <b>Crecer</b> &mdash;el beige que ya aprobaste, ahora a 68&mdash; o <b>invertirse</b>: contra el papel el
     taupe salta de 1,50:1 a <b>4,15:1</b>, casi tres veces el salto. Todo lo dem&aacute;s es id&eacute;ntico en
     las dos.</p>
  <div class="tres">
    %s
    %s
    %s
  </div>
  <div class="dos" style="margin-top:22px">
    %s
    %s
  </div>
  <div class="notas">
    <h3>Lo que hay que saber para elegir</h3>
    <ul>
      <li><b>El taupe repite el color de &laquo;1 MES DE CAF&Eacute; GRATIS&raquo;.</b> Es justo lo que la ronda 5
          hab&iacute;a resuelto separando los dos colores &mdash; pero ah&iacute; las dos cajas med&iacute;an casi lo mismo y
          hoy son 68 contra 45, con el sticker beige del titular entremedio.</li>
      <li><b>El beige deja una sola familia de color arriba</b> (caja beige + contorno beige del
          titular), as&iacute; que la cabecera se lee como un bloque y el taupe queda s&oacute;lo para el premio.</li>
      <li>Si quieres que destaque todav&iacute;a m&aacute;s, lo que queda por mover es el <b>ancho</b>: una banda
          beige de columna completa (810) en vez de una caja ajustada al texto. No cuesta ni un
          p&iacute;xel de alto &mdash; d&iacute;melo y la rindo.</li>
    </ul>
  </div>
</section>""" % (l_antes, l_beige, l_taupe, d_beige, d_taupe))

    # -- 4 - SLIDE 2 -----------------------------------------------------
    l2 = lam(SLIDE2, "<b>SLIDE 2</b> &mdash; exactamente la que aprobaste: 0 p&iacute;xeles de diferencia", 420)
    d2 = det(SLIDE2, (170, 420, 910, 590), "&laquo;Si yo fuera CEO <b>del caf&eacute;</b>,&raquo;", 1.4)
    partes.append("""
<section>
  <h2>Slide 2 &mdash; no se toc&oacute;</h2>
  <p class="que">Dijiste que qued&oacute; perfecta, as&iacute; que se congel&oacute;: el render nuevo tiene
     <b>0 p&iacute;xeles de diferencia</b> contra el que miraste. Y hay una raz&oacute;n de sistema para que no
     bajara con la portada: la regla del carrusel es &laquo;un carrusel, un cuerpo de titular&raquo;, pero en
     la portada el titular pas&oacute; a ser un <b>r&oacute;tulo enmarcado</b> &mdash;otro objeto&mdash;, as&iacute; que ya no son
     comparables. El titular de esta l&aacute;mina se queda en los 88 que aprobaste.</p>
  <div class="dos">
    %s
    %s
  </div>
</section>""" % (l2, d2))

    # -- 5 - LO MEDIDO ---------------------------------------------------
    partes.append("""
<section>
  <h2>Lo medido</h2>
  <table>
    <tr><th>Control</th><th>Valor</th><th>Vara</th></tr>
    <tr><td>&Uacute;ltima l&iacute;nea de la CTA cierra en</td><td class="n">y = 827</td>
        <td>el halo del recorte entra en <b>847</b> &rarr; <span class="ok">20 px de holgura</span></td></tr>
    <tr><td>Contraste de la bajada (peor tercio)</td><td class="n ok">4,16 : 1</td>
        <td>el mismo del titular aprobado</td></tr>
    <tr><td>Caja beige sobre el papel</td><td class="n">1,50 : 1</td>
        <td>igual que la tarjeta crema de la N2, ya publicada</td></tr>
    <tr><td>Caja taupe sobre el papel</td><td class="n ok">4,15 : 1</td><td>&mdash;</td></tr>
    <tr><td>Tinta dentro de la caja, en las dos</td><td class="n ok">6,31 : 1</td><td>&mdash;</td></tr>
    <tr><td>Caf&eacute; del titular contra su contorno beige</td><td class="n ok">6,31 : 1</td>
        <td>el contorno adem&aacute;s lo despega del papel</td></tr>
    <tr><td>Aires de la cabecera</td><td class="n">30 &middot; 20 &middot; 20 &middot; 29</td>
        <td>interno 20 y salto al mensaje 29: el salto entre niveles manda</td></tr>
    <tr><td>Carrusel en el mismo tono</td><td class="n ok">s&iacute;</td>
        <td>mediana 198 / 201</td></tr>
  </table>
  <div class="notas">
    <h3>Sobre el QA</h3>
    <ul>
      <li><code>between-qa.py</code> vuelve a marcar &laquo;texto a 74 px del borde derecho&raquo; en la
          portada. <b>Es el falso positivo conocido</b>: lo da tambi&eacute;n la l&aacute;mina aprobada de la
          ronda 5 &mdash; lo que detecta es el halo blanco del recorte contra el pelo, no texto.</li>
      <li>Ning&uacute;n texto cae sobre la cara ni sobre el vaso. El contorno del sticker no cruza el
          margen: la tinta del titular va de x 331 a 749.</li>
    </ul>
  </div>
</section>""")

    # -- 6 - QUE FALTA ---------------------------------------------------
    partes.append("""
<section>
  <h2>Qu&eacute; falta</h2>
  <div class="notas">
    <h3>Antes de subir</h3>
    <ul>
      <li><b>Elegir el sello: beige o taupe.</b> Con eso rindo la entrega y reemplazo el contenido
          de los archivos que ya est&aacute;n en Drive, as&iacute; <b>los enlaces de la grilla no cambian</b>.</li>
      <li><b>El texto sigue sin el visto de Scarlette.</b> Nicol&aacute;s le pregunt&oacute; &laquo;conf&iacute;rmame si te
          gusta ese texto o para ver otro&raquo;. Est&aacute; aplicado literal.</li>
      <li><b>El copy de la grilla todav&iacute;a dice &laquo;Si yo fuera CEO de Between&raquo;</b> (columna del
          24-09). Es de contenido; si se publica as&iacute;, la gr&aacute;fica y el pie no dicen lo mismo.</li>
      <li><b>Nada subido al Drive.</b> Los renders est&aacute;n en
          <code>out/hilton/between/concurso-s3-r7/</code>.</li>
    </ul>
  </div>
</section>""")

    cuerpo = ("<title>Concurso Between &middot; Ronda 7</title>\n<style>" + CSS + "</style>\n"
              """<div class="wrap">
<header>
  <div class="tag">BETWEEN &middot; CARRUSEL CONCURSO &middot; RONDA 7</div>
  <h1>CONCURSO manda, y el titular pasa a sticker</h1>
  <p class="sub">21-09-2026 &middot; FEED del <b>24 de septiembre</b> (S4) &middot; los tres ajustes
     aplicados &middot; queda por elegir el color del sello</p>
</header>
""" + ''.join(partes) + """
<footer>P&aacute;gina generada por <code>scripts/between-concurso-s3-r7-revision.py</code>.
  Las l&aacute;minas van al tama&ntilde;o en que se publican; los detalles, ampliados.</footer>
</div>""")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    titulo, resto = cuerpo.split("\n", 1)
    SALIDA.write_text(
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + titulo + "\n</head>\n<body>\n" + resto + "\n</body>\n</html>",
        encoding="utf-8")
    print("ok local: %s (%d KB)" % (SALIDA, SALIDA.stat().st_size // 1024))

    ART = SALIDA.with_name("revision-r7-artefacto.html")
    ART.write_text(cuerpo, encoding="utf-8")
    print("ok artefacto: %s (%d KB)" % (ART, ART.stat().st_size // 1024))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

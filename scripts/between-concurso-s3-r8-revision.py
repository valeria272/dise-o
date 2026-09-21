#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión de la RONDA 8 del carrusel CONCURSO de Between (21-09-2026).

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
El rótulo pierde la caja y crece; el titular va en las tres versiones que pidió Eli,
que son los dos recursos de la REF 1 más la variante sin Brushwell. La página las pone
al tamaño de publicación y ampliadas, que es donde se decide.

Las imágenes van EMBEBIDAS en JPEG: la página es un solo archivo y se abre con
doble clic, sin servidor.

    python scripts/between-concurso-s3-r8-revision.py
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
DIR = "out/hilton/between/concurso-s3-r8/"
SALIDA = RAIZ / DIR / "revision-r8.html"

#: ⚠️ El «antes» de esta ronda es la opción A de la ronda 6 —lo que Eli miró y
#: eligió—, copiada a esta carpeta para que no se la lleve un re-render.
ANTES = DIR + "antes-r7-1.png"
CAJA, STICKER, SANS = DIR + "caja.png", DIR + "sticker.png", DIR + "stickerSans.png"
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
  <blockquote>&laquo;Que el concurso, la letra del concurso, <b>se mantenga caf&eacute;, pero borra el
    recuadro beige que tiene, para que destaque mucho m&aacute;s</b>. Un poco m&aacute;s grande el texto del
    concurso&hellip; necesito que se vea <b>m&aacute;s grueso, m&aacute;s grande, incluso como la referencia</b>.
    Y que el &ldquo;se busca CEO del caf&eacute;&rdquo; sea el sticker&hellip; o incluso que quede
    <b>como el texto de &ldquo;menos organizar mis archivos&rdquo;</b>. Quiero ver esa opci&oacute;n. Y uno
    <b>como el que dice &ldquo;estoy haciendo de todo&hellip;&rdquo;</b>. Esas dos opciones.&raquo;<br><br>
    &laquo;Haz otra donde el <b>se busca no sea Brushwell</b>, tal vez con eso se pueda ver mejor tambi&eacute;n.&raquo;
    <small>Eli &middot; 21-09</small></blockquote>
  <p class="que">Las tres opciones de abajo son, literal, los dos recursos de la REF 1 &mdash;la caja
     plana rellena y el contorno pegado a las letras&mdash; m&aacute;s la variante sin Brushwell. Todo lo
     dem&aacute;s de la l&aacute;mina es id&eacute;ntico en las tres.</p>
</section>""")

    d_antes = det(ANTES, (150, 170, 930, 330), "<b>ANTES</b> &mdash; en caja beige, cuerpo 68", 1.25)
    d_ahora = det(SANS, (150, 170, 930, 330), "<b>AHORA</b> &mdash; suelto, caf&eacute;, Black 900, cuerpo 104", 1.25)
    partes.append("""
<section>
  <h2>1 &middot; CONCURSO: fuera el recuadro</h2>
  <p class="que">Ten&iacute;as raz&oacute;n y los n&uacute;meros lo confirman: <b>una caja beige sobre un papel beige
     aporta 1,50:1 de salto</b>, o sea casi nada. Lo que hac&iacute;a destacar a la palabra era el canto de
     la caja, no la palabra. Sacada la caja, la que trabaja es la tipograf&iacute;a &mdash; y ah&iacute; s&iacute; se puede
     crecer sin que el objeto se coma la l&aacute;mina: de <b>68 a 104</b> y de ExtraBold a
     <b>Black (900)</b>, que es el peso del titular de la referencia. Queda en
     <b>4,17:1</b> contra el papel: casi tres veces el contraste que daba la caja.</p>
  <div class="dos">
    %s
    %s
  </div>
  <p class="que" style="margin-top:18px">A 104 mide 610 px de tinta. El titular m&aacute;s grande de las
     tres opciones mide 480, as&iacute; que CONCURSO manda por tama&ntilde;o, por peso y por sitio.
     <b>El Black es del r&oacute;tulo, no del titular</b>: el titular de Between es ExtraBold y eso est&aacute;
     medido en el manual.</p>
</section>""" % (d_antes, d_ahora))

    l_caja = lam(CAJA, "<b>1 &middot; CAJA</b> &mdash; como &laquo;menos organizar mis archivos&raquo;", 340)
    l_stick = lam(STICKER, "<b>2 &middot; STICKER</b> &mdash; como &laquo;estoy haciendo de todo&hellip;&raquo;, con Brushwell", 340)
    l_sans = lam(SANS, "<b>3 &middot; STICKER SIN BRUSHWELL</b> &mdash; una sola tipograf&iacute;a, como el referente", 340)
    d_caja = det(CAJA, (200, 400, 880, 600), "<b>CAJA</b> &mdash; taupe con tinta beige: el bloque de color lleno del referente", 1.35)
    d_stick = det(STICKER, (200, 400, 880, 600), "<b>STICKER</b> &mdash; halo beige de 12 px, con la script en Brushwell", 1.35)
    d_sans = det(SANS, (200, 400, 880, 600), "<b>SIN BRUSHWELL</b> &mdash; las dos l&iacute;neas en Raleway ExtraBold, como la REF", 1.35)
    d_ref = det("raw/hilton/between/refs-concurso-s3/REF1.jpg", None,
                "<b>LA REFERENCIA</b> &mdash; arriba el contorno, abajo la caja plana rellena. Las tres "
                "opciones salen de ac&aacute;", caja_directa=(150, 120, 1050, 530))
    partes.append("""
<section class="elige">
  <h2>2 &middot; Las tres del &laquo;Se busca: CEO del caf&eacute;&raquo;</h2>
  <div class="tres">
    %s
    %s
    %s
  </div>
  <div class="tres" style="margin-top:22px">
    %s
    %s
    %s
  </div>
  <div style="margin-top:22px">%s</div>
  <div class="notas">
    <h3>C&oacute;mo leer las tres</h3>
    <ul>
      <li><b>1 &middot; Caja</b> &mdash; es el recurso de &laquo;menos organizar mis archivos&raquo;: tinta clara sobre
          color saturado. Va taupe y no beige porque una caja beige vuelve al 1,50:1 que acabamos de
          sacar del r&oacute;tulo. Su cuerpo es 64 y no 72: la caja suma 36 px de relleno propio y a 72
          quedaba a 9 px de &laquo;&iquest;El sueldo?&raquo;.</li>
      <li><b>2 &middot; Sticker</b> &mdash; el recurso de &laquo;estoy haciendo de todo&hellip;&raquo;, con la script en
          Brushwell arriba. Es la que conserva la firma de la portada.</li>
      <li><b>3 &middot; Sin Brushwell</b> &mdash; la m&aacute;s parecida al referente, que resuelve sus dos l&iacute;neas
          con <b>una sola tipograf&iacute;a</b> y s&oacute;lo cambia el tama&ntilde;o. &laquo;SE BUSCA:&raquo; va en Raleway
          ExtraBold, al mismo peso que el titular.</li>
      <li>El halo mide <b>12 px</b> en las dos de sticker, y el aire entre las dos l&iacute;neas tuvo que
          abrirse de 9 a 27 px: el halo crece 6 px por lado y los dos se tocaban.</li>
    </ul>
  </div>
</section>""" % (l_caja, l_stick, l_sans, d_caja, d_stick, d_sans, d_ref))

    partes.append("""
<section>
  <h2>Lo medido</h2>
  <table>
    <tr><th>Control</th><th>Valor</th><th>Vara</th></tr>
    <tr><td>CONCURSO contra el papel</td><td class="n ok">4,17 : 1</td>
        <td>la caja beige daba <b>1,50 : 1</b></td></tr>
    <tr><td>Ancho de CONCURSO</td><td class="n">610 px</td>
        <td>el titular m&aacute;s ancho de las tres opciones mide 480</td></tr>
    <tr><td>&Uacute;ltima l&iacute;nea de la CTA</td><td class="n">y = 827</td>
        <td>el halo del recorte entra en 847 &rarr; <span class="ok">20 px de holgura</span></td></tr>
    <tr><td>Aire entre las dos l&iacute;neas del sticker</td><td class="n">27 px</td>
        <td>9 de la marca + 12 de halo + 6 &mdash; si no, los halos se tocan</td></tr>
    <tr><td>Gap del titular a &laquo;&iquest;El sueldo?&raquo;</td><td class="n">19 &middot; 24 &middot; 38 px</td>
        <td>caja &middot; sticker &middot; sin Brushwell</td></tr>
    <tr><td>Contraste de la bajada</td><td class="n ok">4,16 : 1</td><td>sin cambios</td></tr>
    <tr><td>Carrusel en el mismo tono</td><td class="n ok">s&iacute;</td><td>mediana 197 / 201</td></tr>
  </table>
  <div class="notas">
    <h3>Un hallazgo t&eacute;cnico que vale la pena saber</h3>
    <ul>
      <li>El contorno del sticker <b>no se puede hacer con <code>text-stroke</code></b>: Chrome lo
          pinta glifo a glifo y el contorno de cada letra cruza por encima de la anterior &mdash; con el
          tracking del titular de Between se nota en toda la l&iacute;nea. Se ve&iacute;a en el render ampliado.
          Ahora es un <b>halo de 24 copias</b>, que se pinta entero detr&aacute;s del texto y queda continuo,
          como en la referencia.</li>
      <li>La <b>slide 2 no se toc&oacute;</b>: sigue siendo exactamente la que aprobaste.</li>
      <li><code>between-qa.py</code> repite el falso positivo conocido del borde derecho (es el halo
          del recorte contra el pelo, no texto).</li>
    </ul>
  </div>
</section>""")

    partes.append("""
<section>
  <h2>Qu&eacute; falta</h2>
  <div class="notas">
    <h3>Antes de subir</h3>
    <ul>
      <li><b>Elegir 1, 2 o 3.</b> Con eso subo, reemplazando el contenido de los archivos que ya
          est&aacute;n en Drive para que <b>los enlaces de la grilla no cambien</b>.</li>
      <li><b>El texto sigue sin el visto de Scarlette.</b></li>
      <li><b>El copy de la grilla todav&iacute;a dice &laquo;Si yo fuera CEO de Between&raquo;</b> (columna del 24-09).</li>
      <li>Renders en <code>out/hilton/between/concurso-s3-r8/</code>.</li>
    </ul>
  </div>
</section>""")

    cuerpo = ("<title>Concurso Between &middot; Ronda 8</title>\n<style>" + CSS + "</style>\n"
              """<div class="wrap">
<header>
  <div class="tag">BETWEEN &middot; CARRUSEL CONCURSO &middot; RONDA 8</div>
  <h1>CONCURSO sin caja, y tres titulares</h1>
  <p class="sub">21-09-2026 &middot; FEED del <b>24 de septiembre</b> (S4) &middot; el r&oacute;tulo ya est&aacute;
     resuelto &middot; queda elegir el titular</p>
</header>
""" + ''.join(partes) + """
<footer>P&aacute;gina generada por <code>scripts/between-concurso-s3-r8-revision.py</code>.
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

    ART = SALIDA.with_name("revision-r8-artefacto.html")
    ART.write_text(cuerpo, encoding="utf-8")
    print("ok artefacto: %s (%d KB)" % (ART, ART.stat().st_size // 1024))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión de la RONDA 6 del carrusel CONCURSO de Between (21-09-2026).

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
Esta ronda vuelve a tener una DECISIÓN ABIERTA —contenido reordenó la jerarquía de
la portada y la lámina no tiene sitio para todo—, así que la página pone el antes y
las dos salidas al lado, al tamaño en que se publica, con el detalle de la cabecera
al 2× que es donde se ve la diferencia.

Las imágenes van EMBEBIDAS en JPEG: la página es un solo archivo y se abre con
doble clic, sin servidor.

    python scripts/between-concurso-s3-r6-revision.py
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
DIR = "out/hilton/between/concurso-s3-r6/"
SALIDA = RAIZ / DIR / "revision-r6.html"

#: ⚠️ El «antes» NO apunta a la entrega ni a la carpeta de renders: las dos se
#: sobrescriben al re-rendir y la página pasaría a compararse consigo misma. Son
#: copias de la ronda 5 guardadas en la carpeta de esta ronda.
ANTES1, ANTES2 = DIR + "antes-1.png", DIR + "antes-2.png"
A1, A2 = DIR + "A-1.png", DIR + "A-2.png"
B1, B2 = DIR + "B-1.png", DIR + "B-2.png"


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


def det(ruta, caja1080, pie, escala=1.6):
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

    # ── 1 · LO QUE LLEGÓ ─────────────────────────────────────────────────
    partes.append("""
<section>
  <h2>Lo que llegó hoy</h2>
  <blockquote>«Nos pidieron algunos cambios para el carrusel del concurso. Son principalmente
    ajustes de texto […] <b>La idea es darle mayor relevancia a la efeméride.</b><br><br>
    Por lo que en la <b>Slide 1</b> agregaríamos:<br>
    CONCURSO<br>
    <b>SE ACERCA EL DÍA INTERNACIONAL DEL CAFÉ Y SE ABRIÓ LA VACANTE MÁS IMPORTANTE.</b><br>
    SE BUSCA: CEO DEL CAFÉ · ¿El sueldo? · 1 MES DE CAFÉ GRATIS ·
    ¿Quieres el puesto? → Desliza para tu entrevista<br><br>
    Y en la <b>Slide 2</b>, cambiar: “SI YO FUERA CEO DE BETWEEN” → <b>“SI YO FUERA CEO DEL
    CAFÉ”</b>.»
    <small>Nicolás Ávila · Slack, 21-09</small></blockquote>
  <blockquote>«Sí, dejaría como principal <b>CONCURSO</b>, para que se entienda de inmediato que es
    un concurso y que deben participar. Después, como <b>segunda jerarquía, las bajadas</b>:
    SE ACERCA EL DÍA INTERNACIONAL DEL CAFÉ Y SE ABRIÓ LA VACANTE MÁS IMPORTANTE.
    Y desde ahí seguiría con <b>“SE BUSCA: CEO DEL CAFÉ”</b> y los otros textos.»
    <small>Nicolás Ávila · Slack, 21-09</small></blockquote>
  <p class="que">O sea que no es un texto que se agrega: es el <b>orden de lectura</b> de la portada
     el que cambia. Hoy la lámina abre con el titular y el sello va debajo; lo que piden es que
     abra con <b>CONCURSO</b>, siga la bajada y recién ahí entre «Se busca: CEO del café».</p>
</section>""")

    # ── 2 · EL PROBLEMA: NO SOBRA SITIO ──────────────────────────────────
    partes.append("""
<section>
  <h2>El problema, medido</h2>
  <p class="que">La portada ya estaba llena. Estas son las tres cotas que mandan, medidas sobre el
     render aprobado y sobre la foto (no estimadas):</p>
  <table>
    <tr><th>Qué</th><th>Dónde</th><th>Por qué manda</th></tr>
    <tr><td>El lockup cierra su tinta</td><td class="n">y = 180</td>
        <td>arriba de eso no hay nada que usar</td></tr>
    <tr><td>El halo blanco del recorte entra en la columna de la CTA</td><td class="n">y = 847</td>
        <td>ningún texto se apoya en el sticker: la última línea no puede pasar de <b>y ≈ 827</b></td></tr>
    <tr><td>Entremedio quedan</td><td class="n">662 px</td>
        <td>y ahí tienen que caber, con su aire: sello 84 + bajada 78 + titular + «¿El sueldo?» 44
            + caja taupe 66 + CTA 78</td></tr>
  </table>
  <div class="notas">
    <h3>La cuenta</h3>
    <ul>
      <li>Con el titular en los <b>103</b> de la ronda 5, sumando todo quedan <b>80 px para cuatro
          aires</b> — 20 px cada uno. Eso es una portada apretada, que es justo lo que marcas como
          «desordenado».</li>
      <li>Por eso las dos salidas de abajo <b>no discuten el texto</b> (va literal): discuten
          <b>qué cede</b> para que la jerarquía nueva entre.</li>
    </ul>
  </div>
</section>""")

    # ── 3 · LAS DOS SALIDAS ──────────────────────────────────────────────
    l_antes = lam(ANTES1, "<b>HOY</b> — lo que el cliente está mirando. Abre con el titular; "
                          "CONCURSO va debajo, encabezando la pila", 360)
    l_a = lam(A1, "<b>OPCIÓN A · apilado</b> — CONCURSO arriba y centrado, bajada centrada, "
                  "y el titular baja de 103 a <b>88</b>", 360)
    l_b = lam(B1, "<b>OPCIÓN B · banda</b> — CONCURSO a la izquierda con la bajada al lado, "
                  "en tres líneas. El titular <b>se queda en 103</b>", 360)
    d_antes = det(ANTES1, (60, 180, 1020, 620), "<b>HOY</b> — el orden es titular → CONCURSO")
    d_a = det(A1, (60, 180, 1020, 620), "<b>A</b> — el orden es CONCURSO → bajada → titular, todo en el eje")
    d_b = det(B1, (60, 180, 1020, 620), "<b>B</b> — la cabecera pasa a dos columnas; el eje se rompe, el titular no")
    partes.append(f"""
<section class="elige">
  <h2>Slide 1 — las dos salidas <span class="ojo">(hay que elegir)</span></h2>
  <p class="que">Las dos cumplen lo que pidió contenido y las dos llevan el texto literal. La
     diferencia es una sola: <b>A obedece la jerarquía completa</b> —el titular deja de ser lo más
     grande de la lámina, que es justamente lo que implica bajarlo a tercer lugar— y
     <b>B protege el titular aprobado</b> a cambio de partir la cabecera en dos columnas.</p>
  <div class="tres">
    {l_antes}
    {l_a}
    {l_b}
  </div>
  <div class="tres" style="margin-top:22px">
    {d_antes}
    {d_a}
    {d_b}
  </div>
  <div class="notas">
    <h3>Lo que hay que saber para elegir</h3>
    <ul>
      <li><b>A mueve tu decisión de la ronda 5.</b> La caja beige grande que elegiste sigue siendo
          la misma caja y el mismo cuerpo (52); lo que cambia es que sube a rótulo de la lámina, que
          es lo que pide contenido. Si prefieres que no se mueva de la pila, esa es la B — pero ahí
          el sello deja de ser lo primero que se lee.</li>
      <li><b>En A el titular baja a 88</b> (−15 %). Y como un carrusel lleva <b>un</b> cuerpo de
          titular, la slide 2 baja con él: si no, al deslizar el titular cambia de tamaño.</li>
      <li><b>En B la bajada tuvo que cortarse a mano</b> (424 · 264 · 382 px): corrida dejaba
          «importante» sola en la tercera línea.</li>
      <li>La bajada va en <b>caja baja</b>, no en versales como llegó: en esta marca las versales
          son del titular y de la caja taupe. Es la misma traducción que ya se le hizo a
          «SE BUSCA:» → «Se busca:», y el punto final se va (los títulos de Between no lo llevan).</li>
      <li>Los dos trazos <b>se movieron</b>: el canal que ocupaban ahora es del titular. En A
          flanquean el rótulo; en B bajan al papel vacío de abajo a la izquierda.</li>
    </ul>
  </div>
</section>""")

    # ── 4 · SLIDE 2 ──────────────────────────────────────────────────────
    d2_antes = det(ANTES2, (170, 420, 910, 590), "<b>ANTES</b> — «Si yo fuera CEO de Between,»", 1.4)
    d2_dsp = det(A2, (170, 420, 910, 590), "<b>DESPUÉS</b> — «Si yo fuera CEO del café,»", 1.4)
    l2_antes = lam(ANTES2, "<b>ANTES</b> — titular 103", 420)
    l2_dsp = lam(A2, "<b>DESPUÉS</b> (con la opción A) — titular 88, misma tarjeta, mismo legal", 420)
    partes.append(f"""
<section>
  <h2>Slide 2 — sólo la frase</h2>
  <p class="que">El cambio es una línea y va literal. Lo demás de la tarjeta no se toca: el rótulo,
     las tres filas con casilla, el avatar, el handle y el legal quedan igual. El corte de línea
     tampoco se movió — la frase nueva es más corta.</p>
  <div class="dos">
    {d2_antes}
    {d2_dsp}
  </div>
  <div class="dos" style="margin-top:22px">
    {l2_antes}
    {l2_dsp}
  </div>
  <p class="que" style="margin-top:18px">⚠️ Ojo: <b>el copy de la grilla sigue diciendo «Si yo fuera
     CEO de Between»</b> (columna del 24-09). Es de contenido, no se toca desde acá, pero si se
     publica así la gráfica y el pie no van a decir lo mismo.</p>
</section>""")

    # ── 5 · LO MEDIDO ────────────────────────────────────────────────────
    partes.append("""
<section>
  <h2>Lo medido</h2>
  <table>
    <tr><th>Control</th><th>Opción A</th><th>Opción B</th><th>Vara</th></tr>
    <tr><td>Última línea de la CTA cierra en</td><td class="n">y = 827</td><td class="n">y = 817</td>
        <td>el halo del recorte entra en <b>847</b></td></tr>
    <tr><td>Holgura contra el recorte</td><td class="n ok">20 px</td><td class="n ok">30 px</td>
        <td>la lámina aprobada tiene 26</td></tr>
    <tr><td>Contraste de la bajada (peor tercio)</td><td class="n ok">4,17 : 1</td>
        <td class="n ok">4,19 : 1</td><td>el mismo del titular aprobado</td></tr>
    <tr><td>Caja beige sobre el papel</td><td class="n">1,51 : 1</td><td class="n">1,51 : 1</td>
        <td>igual que la tarjeta crema de la N2, ya publicada</td></tr>
    <tr><td>Tinta café dentro de la caja</td><td class="n ok">6,31 : 1</td><td class="n ok">6,31 : 1</td>
        <td>—</td></tr>
    <tr><td>Cuerpo del titular (las dos slides)</td><td class="n">88</td><td class="n">103</td>
        <td>uno solo por carrusel</td></tr>
    <tr><td>Carrusel en el mismo tono</td><td class="n ok">sí</td><td class="n ok">sí</td>
        <td>mediana 197 / 201 · calidez 37,7 / 33,1</td></tr>
  </table>
  <div class="notas">
    <h3>Sobre el QA</h3>
    <ul>
      <li><code>between-qa.py</code> marca «texto a 74 px del borde derecho» en la portada.
          <b>Es el mismo aviso que da la lámina ya aprobada</b>: lo que detecta no es texto, es el
          halo blanco del recorte contra el pelo. Se verificó corriéndolo sobre la pieza de la
          ronda 5.</li>
      <li>Ningún texto cae sobre la cara ni sobre el vaso, en ninguna de las dos.</li>
    </ul>
  </div>
</section>""")

    # ── 6 · QUÉ FALTA ────────────────────────────────────────────────────
    partes.append("""
<section>
  <h2>Qué falta</h2>
  <div class="notas">
    <h3>Antes de subir</h3>
    <ul>
      <li><b>Elegir A o B.</b> Con eso se rinde la entrega y se reemplaza el contenido de los
          archivos que ya están en Drive, así que <b>los enlaces de la grilla no cambian</b>.</li>
      <li><b>El texto todavía no está confirmado por Scarlette.</b> En el mismo mensaje Nicolás le
          pregunta «confírmame si te gusta ese texto o para ver otro». Está aplicado literal, pero
          conviene esperar ese visto antes de publicar.</li>
      <li><b>Nada se subió al Drive todavía.</b> Los renders están en
          <code>out/hilton/between/concurso-s3-r6/</code>.</li>
      <li>La pieza es del <b>24 de septiembre</b> (FEED, S4) y está <code>EN REVISIÓN</code>. El
          brief de la grilla no trae estos textos: llegaron por Slack.</li>
    </ul>
  </div>
</section>""")

    cuerpo = f"""<title>Concurso Between · Ronda 6</title>
<style>{CSS}</style>
<div class="wrap">
<header>
  <div class="tag">BETWEEN · CARRUSEL CONCURSO · RONDA 6</div>
  <h1>Contenido reordenó la portada</h1>
  <p class="sub">21-09-2026 · FEED del <b>24 de septiembre</b> (S4) · dos slides ·
     hay que elegir entre dos salidas</p>
</header>
{''.join(partes)}
<footer>Página generada por <code>scripts/between-concurso-s3-r6-revision.py</code>.
  Las láminas van al tamaño en que se publican; los detalles, al 1,6×.</footer>
</div>"""

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    # El archivo local se abre con doble clic, así que lleva el documento entero.
    titulo, resto = cuerpo.split("\n", 1)
    SALIDA.write_text(
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + titulo + "\n</head>\n<body>\n" + resto + "\n</body>\n</html>",
        encoding="utf-8")
    print(f"✓ {SALIDA}  ({SALIDA.stat().st_size // 1024} KB)")

    # ⚠️ La versión que se publica como artefacto NO lleva doctype/html/head/body:
    # la plataforma envuelve el archivo y los duplicaría.
    ART = SALIDA.with_name("revision-r6-artefacto.html")
    ART.write_text(cuerpo, encoding="utf-8")
    print(f"✓ {ART}  ({ART.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

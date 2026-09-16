#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión de la RONDA 5 del carrusel CONCURSO de Between (16-09-2026).

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
Esta ronda además tiene una DECISIÓN ABIERTA —cuál de las dos cajas del sello— así
que la página pone las dos al lado del antes, al tamaño en que se publica y con un
detalle al 2×, que es donde se ve la diferencia real.

Las imágenes van EMBEBIDAS en JPEG: la página es un solo archivo y se abre con
doble clic, sin servidor.

    python scripts/between-concurso-s3-r5-revision.py
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
SALIDA = RAIZ / "out/hilton/between/concurso-s3-r5/revision-r5.html"

#: ⚠️ El «antes» NO puede apuntar a la entrega: la entrega se SOBRESCRIBE con la
#: pieza corregida y la página pasaría a comparar el después contra sí mismo.
#: Apunta a la copia de la ronda 4, guardada antes de re-rendir.
ANTES = "out/hilton/between/concurso-s3-r5/r4-N1-respaldo.png"
TAG = "out/hilton/between/concurso-s3-r5/opcion-tag.png"
CAJA = "out/hilton/between/concurso-s3-r5/opcion-caja.png"


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


def recorte(ruta, caja1080, escala=2.0, calidad=90):
    """Un detalle de la lámina. `caja1080` va en coordenadas del lienzo de 1080."""
    p = RAIZ / ruta
    if not p.is_file():
        return None
    im = Image.open(p).convert("RGB")
    k = im.width / 1080
    x0, y0, x1, y1 = [round(v * k) for v in caja1080]
    im = im.crop((x0, y0, x1, y1))
    destino = (round((x1 - x0) * escala), round((y1 - y0) * escala))
    im = im.resize(destino, Image.LANCZOS)
    return _data(im, calidad)


def lam(ruta, pie, ancho=880):
    d = img(ruta, ancho)
    if not d:
        return '<figure class="falta"><div>falta %s</div></figure>' % ruta
    return '<figure><img src="%s" alt=""><figcaption>%s</figcaption></figure>' % (d, pie)


def det(ruta, caja1080, pie, escala=2.0):
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
.fila{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));align-items:start}
.tres{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));align-items:start}
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

    # ── 1 · LO QUE PIDIÓ EL CLIENTE ──────────────────────────────────────
    partes.append("""
<section>
  <h2>Lo que llegó</h2>
  <blockquote>«En la primera gráfica, donde dice <b>“Se busca…”</b>, darle más protagonismo a la
    palabra <b>“CONCURSO”</b>. Que sea más grande y quizás usar otro tono de café, o algún recurso
    visual que haga que destaque más y se vea llamativo de inmediato.»<br><br>
    «Cambiar el texto <b>“POSTULA AQUÍ → DESLIZA”</b> por: <b>“¿Quieres el puesto? → Desliza para
    tu entrevista”</b>.»
    <small>Nicolás Ávila, con Scarlette · Slack, 16-09</small></blockquote>
  <blockquote>«Haz una opción donde CONCURSO esté en una <b>caja beige más grande estilo la ref</b>.
    Tal vez así mejora.» <small>Eli, 16-09</small></blockquote>
  <p class="que">Los dos cambios son de la <b>portada</b> (N1); la N2 no se toca.
     El texto de la CTA va <b>literal</b> como lo escribieron y ya está aplicado en las dos
     opciones de abajo — lo único que queda por decidir es la caja del sello.</p>
</section>""")

    # ── 2 · EL SELLO: LAS DOS OPCIONES ───────────────────────────────────
    b_hoy = lam(ANTES, "<b>HOY</b> — caja taupe, cuerpo 28", 360)
    b_tag = lam(TAG, "<b>OPCIÓN A</b> — caja beige en el mismo sitio, cuerpo <b>36</b>", 360)
    b_caja = lam(CAJA, "<b>OPCIÓN B ✅ ELEGIDA</b> — caja beige grande, encabeza la pila, cuerpo <b>52</b>", 360)
    d_hoy = det(ANTES, (60, 80, 700, 200),
                "<b>HOY</b> — el sello y la caja del sueldo son la MISMA caja taupe, así que ninguna manda sobre la otra")
    d_tag = det(TAG, (60, 80, 700, 200),
                "<b>OPCIÓN A</b> — invertida: beige de fondo, café de tinta. La palabra crece 29 % y deja de ser gemela de la caja del sueldo")
    d_caja = det(CAJA, (60, 430, 700, 600),
                 "<b>OPCIÓN B ✅ ELEGIDA</b> — la caja plana de la REF 1, bajo el titular. La palabra crece 86 %")
    partes.append(f"""
<section class="elige">
  <h2>1 · El sello CONCURSO — <span class="ok">elegida la B</span></h2>
  <p class="que"><b>Eli eligió la opción B</b> y es la que está entregada: CONCURSO a 52 px en caja
     beige plana, encabezando la pila del mensaje. Las tres quedan abajo como registro de la ronda,
     al tamaño en que se publica; el detalle es la misma zona al 2×.</p>
  <div class="tres">
    {b_hoy}
    {b_tag}
    {b_caja}
  </div>
  <div class="tres" style="margin-top:22px">
    {d_hoy}
    {d_tag}
    {d_caja}
  </div>

  <div class="notas">
    <h3>Por qué beige y no un café nuevo</h3>
    <ul>
      <li>El cliente propone «otro tono de café». La paleta de Between son <b>dos</b> tintas —beige
          <code>#FFF9EB</code> y café <code>#675B49</code>—, así que un tercer marrón no es corregir
          una pieza: es cambiarle la paleta a la marca. <b>La inversión da el mismo salto sin
          inventar nada</b>, y es exactamente lo que hace la caja de color plano de la REF 1.</li>
      <li>Y de paso arregla algo que ellos están viendo sin nombrarlo: <b>hoy el sello y la caja
          «1 MES DE CAFÉ GRATIS» son la misma caja taupe</b>. Dos cajas iguales en la misma lámina
          no tienen jerarquía entre sí — por eso el sello «no destaca» aunque esté arriba del todo.
          En las dos opciones queda <b>beige contra taupe</b>.</li>
      <li>Si aun así quieren el marrón más oscuro, se puede: <code>#4C4133</code> da 6,13:1 contra
          el papel (hoy 4,08:1). Pero eso lo aprueba la marca, no la pieza.</li>
    </ul>
  </div>

  <div class="notas">
    <h3>La diferencia entre A y B, medida</h3>
  </div>
  <table>
    <tr><th></th><th>Hoy</th><th>Opción A · tag</th><th>Opción B · caja</th></tr>
    <tr><td>Cuerpo de «CONCURSO»</td><td class="n">28 px</td><td class="n">36 px <b>(+29 %)</b></td><td class="n">52 px <b>(+86 %)</b></td></tr>
    <tr><td>Alto de la caja</td><td class="n">54</td><td class="n">70</td><td class="n">84</td></tr>
    <tr><td>Ancho de la caja</td><td class="n">258</td><td class="n">287</td><td class="n">398</td></tr>
    <tr><td>Fondo contra el papel <code>#DFC9BB</code></td><td class="n">4,08:1</td><td class="n">1,50:1</td><td class="n">1,50:1</td></tr>
    <tr><td>Tinta dentro de la caja</td><td class="n">6,31:1</td><td class="n">6,31:1 <span class="ok">✓</span></td><td class="n">6,31:1 <span class="ok">✓</span></td></tr>
    <tr><td>Dónde va</td><td>línea del lockup</td><td>línea del lockup</td><td>encabeza la pila del mensaje</td></tr>
    <tr><td>Aire al logotipo</td><td class="n">150 px</td><td class="n">39 px</td><td>—</td></tr>
  </table>
  <div class="notas">
    <ul>
      <li><b>El 1,50:1 de la caja no es un defecto.</b> Es el mismo contraste que la tarjeta crema
          de la N2, que ya está aprobada y publicada. Una caja plana de este tipo no se lee por su
          canto sino por la tinta que lleva dentro, y ésa es la que crece.</li>
      <li><b>36 px es el techo de la opción A, y está medido:</b> la caja da 287 px y el lockup
          arranca en x=408, así que con el giro quedan 39 px de aire. A 40 px el sello toca el
          logotipo. Si se quiere más grande que eso hay que bajarlo — que es la opción B.</li>
      <li><b>La opción B cabe sin apretar nada:</b> el titular cierra su tinta en y=450, la figura
          entra en la columna izquierda en y=869, y la pila completa ocupa 492–825. Quedan 42 px de
          aire arriba y 44 abajo. Los dos aires del sello son distintos a propósito —42 contra el
          titular y 23 contra «¿El sueldo?»— porque la caja <b>encabeza</b> la pila: con 30 y 30
          flotaba entre los dos y no se leía como cabecera de nada.</li>
      <li><b>Lo que se pierde en B:</b> la esquina de arriba a la izquierda queda vacía y el sello
          deja de ser el rótulo de la lámina —la posición que tiene en la REF 1— para pasar a ser
          la cabecera del mensaje.</li>
      <li>⭐ <b>Por qué la B es la correcta, y yo había recomendado la A.</b> El cliente pidió
          <i>tamaño</i>, y en la posición del rótulo el techo son 36 px porque el lockup arranca en
          x=408. Contra los 28 de hoy, 36 no es un cambio que se vea «de inmediato», que es
          literalmente lo que pidieron. <b>La posición que limita el tamaño es la que se cede, no
          el tamaño.</b></li>
    </ul>
  </div>
</section>""")

    # ── 3 · LA CTA ───────────────────────────────────────────────────────
    c_antes = det(ANTES, (60, 690, 700, 780), "<b>ANTES</b> — «Postula aquí → Desliza»", 2.2)
    c_ahora = det(TAG, (60, 690, 700, 810),
                  "<b>AHORA</b> — «¿Quieres el puesto? → Desliza para tu entrevista»", 2.2)
    partes.append(f"""
<section>
  <h2>2 · La CTA — texto nuevo, literal</h2>
  <p class="que">Aplicado en las dos opciones. Acá no hay nada que elegir.</p>
  <div class="fila">
    {c_antes}
    {c_ahora}
  </div>
  <div class="notas">
    <h3>Las dos decisiones que trae</h3>
    <ul>
      <li><b>Va en dos líneas, y el corte cae en la flecha.</b> A 32 px la frase entera mide 700 px
          y el canal limpio de esa franja termina en x≈630: no cabe. Partida por la flecha —arriba
          la pregunta, abajo la acción— la línea larga mide 435 px y cierra en 519, con 111 px de
          aire contra el recorte.</li>
      <li><b>El interlineado sube de 1,1 a 1,22.</b> Con 1,1 las dos líneas se leían como un
          párrafo pegado. El cuerpo no se tocó: sigue en 32.</li>
      <li>⭐ <b>El remate ahora enlaza con la N2</b>, que se titula «TU ENTREVISTA EMPIEZA AHORA».
          Conviene no romper ese enganche si el texto se vuelve a tocar.</li>
    </ul>
  </div>
</section>""")

    # ── 4 · LO QUE NO SE TOCÓ, Y LO QUE QUEDA ────────────────────────────
    partes.append("""
<section>
  <h2>Lo que NO se tocó</h2>
  <div class="notas">
    <ul>
      <li><b>La N2 va igual.</b> Los dos comentarios son de la portada.</li>
      <li><b>La foto, el recorte, la hoja de papel y su sombra:</b> intactos. Esta ronda es
          tipografía y color de caja, nada de imagen.</li>
      <li><b>Los dos trazos de la portada</b> —la chispa y las cuñas— siguen donde estaban: con el
          sello en opción B la pila baja 38 px y la caja taupe pasa a 656–722, así que las cuñas
          —516–589, en el canal de la derecha— no las toca.</li>
      <li><b>El QA de Between</b> marca las dos opciones con su falso positivo conocido: acusa
          «texto a 74 px del borde derecho» y esa tinta está en las filas 1024–1047, que es el
          hombro de la figura. Todo el texto de la lámina vive entre y=93 y y=825.</li>
    </ul>
  </div>
  <div class="notas">
    <h3>Abierto</h3>
    <ul>
      <li><span class="ok">✅ Resuelto:</span> Eli eligió la <b>B</b>. La N1 se re-rindió a
          2250×2812 a 150 ppp y <b>reemplaza el mismo archivo</b> del Drive
          (<code>1A9Kf…27mB</code>, carpeta <code>C1 S3 CONCURSO</code>), así que <b>el enlace de la
          grilla no cambió</b>. Verificado con el conector: 5.118.684 bytes, los mismos que el
          local, y el <code>createdTime</code> sigue siendo el de la ronda 4.</li>
      <li>La <b>N2 no se tocó</b> ni se volvió a subir: los dos comentarios eran de la portada.</li>
      <li>Sigue pendiente pedirle a contenido la <b>fecha</b> del concurso: la grilla dice
          <code>X DEFINIR</code> y el concurso corre del 21 al 30-09.</li>
    </ul>
  </div>
</section>""")

    html = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Between · Concurso S3 · ronda 5</title>
<style>@@CSS@@</style></head><body><div class="wrap">
<header>
  <span class="tag">BETWEEN · S3 · RONDA 5</span>
  <h1>Carrusel CONCURSO — el sello y la CTA</h1>
  <p class="sub">16-09-2026 · comentarios de Nicolás y Scarlette sobre la portada ·
     <b>entregada</b> con el sello en caja beige grande (opción B)</p>
</header>
@@PARTES@@
<footer>Piezas: <code>out/hilton/between/concurso-s3-r5/</code> ·
  composición: <code>src/compositions/hilton/BetweenC1S3Concurso.tsx</code> ·
  se rinde con <code>npx remotion still src/index.ts BW-F-Concurso-1 &lt;salida&gt; --scale=2.0833 --props</code></footer>
</div></body></html>""".replace("@@CSS@@", CSS).replace("@@PARTES@@", "".join(partes))

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(html, encoding="utf-8")
    print("✓ %s  (%d KB)" % (SALIDA, SALIDA.stat().st_size // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())

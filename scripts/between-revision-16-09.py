#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página de revisión de la jornada 16-09-2026 de BETWEEN.

Por qué existe: Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`).
Cada ronda se entrega como una página con el antes, el después y la referencia, y
los números van abajo. Las imágenes van EMBEBIDAS en JPEG, así que la página es un
solo archivo y se abre sin servidor, con doble clic.

    python scripts/between-revision-16-09.py
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
SALIDA = RAIZ / "out/hilton/between/revision-16-09.html"


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
    partes = []

    # ── 1 · EL CONCURSO ──────────────────────────────────────────────────
    partes.append(f"""
<section>
  <h2>1 · Carrusel CONCURSO — «Se busca: CEO del café»</h2>
  <p class="que">FEED, columna 10 de la grilla · estado <b>OK PARA DISEÑAR</b> · pieza nueva.
     Entregada como <b>C1 S3 CONCURSO N1/N2.png</b> en <b>S3 HILTON SEP 2026 / BW / C1 S3 CONCURSO</b>.</p>
  <div class="fila">
    {lam('out/hilton/between/entrega-c1-s3-concurso/C1 S3 CONCURSO N1.png', '<b>N1</b> — portada · 2250×2812')}
    {lam('out/hilton/between/entrega-c1-s3-concurso/C1 S3 CONCURSO N2.png', '<b>N2</b> — la dinámica · 2250×2812')}
  </div>

  <div class="notas">
    <h3>Ronda 4 — el fondo es UNA sola hoja de papel</h3>
  </div>
  <blockquote>«El fondo debe ser el <b>mismo beige papel</b> para ambas slides, que sea
    <b>plano</b> y <b>transicione</b>.» <small>Eli, 16-09</small></blockquote>
  <div class="fila">
    {lam('out/hilton/between/concurso-s3-antes/BW-F-Concurso-1.png', '<b>ANTES</b> — pared lisa gris-beige', 430)}
    {lam('out/hilton/between/concurso-s3-antes/BW-F-Concurso-2.png', '<b>ANTES</b> — panel de <b>veta de madera</b>, más rosado', 430)}
  </div>
  <div class="fila" style="margin-top:14px">
    {lam('out/hilton/between/entrega-c1-s3-concurso/C1 S3 CONCURSO N1.png', '<b>AHORA</b> — papel beige plano', 430)}
    {lam('out/hilton/between/entrega-c1-s3-concurso/C1 S3 CONCURSO N2.png', '<b>AHORA</b> — la MISMA hoja, su otra mitad', 430)}
  </div>
  <div class="notas">
    <h3>Qué se hizo, y qué no</h3>
    <ul>
      <li><b>Eran dos superficies distintas, no dos tonos.</b> La ronda 3 igualó la
          <i>iluminación</i> de las dos paredes (salto en la costura 18,7 → 0,95) pero no podía
          igualar el <i>material</i>: la portada era una pared lisa y la slide 2 un panel de veta
          vertical de madera. Eso es lo que se seguía viendo.</li>
      <li><b>No se regeneró nada.</b> El retrato y el bodegón están aprobados; regenerarlos era
          perderlos. Se cambió sólo la superficie de atrás, con el recorte intacto píxel a píxel.</li>
      <li><b>«Que transicione»: es una sola hoja cortada en dos.</b> El papel se sintetiza de una
          vez a 4500 px de ancho —las dos láminas juntas— y cada slide se queda con su mitad. La
          continuidad no se corrige, existe por construcción: la última columna de la N1 y la
          primera de la N2 son vecinas de la misma hoja.</li>
      <li><b>«Que sea plano»:</b> grano fino + fibra horizontal, y el manchado bajó de 2,8 a 1,4
          niveles — a sangre en 4500 px, con 2,8 la hoja se lee como nubes.</li>
      <li><b>El tono no se eligió a ojo:</b> es la mediana medida de las dos paredes aprobadas,
          <b>#DFC9BB</b>. Así el papel entra en el sitio exacto que ocupaba la pared y ningún
          contraste ya aprobado de la pieza se mueve.
          ⚠️ Por eso <b>no</b> se usó el papel crema <code>#FFF9EB</code> de la story del 18-09:
          a sangre, con ese crema el borde blanco del recorte queda en 1,05:1 —el sticker deja de
          existir— y la tarjeta crema de la N2, que no tiene contorno, se funde con el fondo.</li>
      <li><b>La sombra del sticker se rehizo con el peso que ya tenía.</b> Al sacar la pared se iba
          también su sombra, y sin ella el recorte es un papel pegado. Se midió el perfil de las
          láminas aprobadas y la síntesis se ajustó a él: 0,948 · 0,977 · 0,998 contra
          0,946 · 0,984 · 0,999 a 1–6, 6–12 y 12–25 px del filo.</li>
    </ul>
  </div>
  <table>
    <tr><th>Ronda 4 — qué se midió</th><th>Antes</th><th>Ahora</th></tr>
    <tr><td>Salto en la costura entre las dos láminas</td><td class="n">0,95</td>
        <td class="n">0,97 <span class="ok">✓ invisible</span> — y ahora en las <b>2.812</b> filas, no sólo en el 45 % de arriba</td></tr>
    <tr><td>Franja del titular por tercios · N1</td><td class="n">215,9 · 208,9 · 196,9</td>
        <td class="n">203,7 · 204,7 · 205,7</td></tr>
    <tr><td>Franja del titular por tercios · N2</td><td class="n">209,9 · 204,1 · 194,0</td>
        <td class="n">204,7 · 204,7 · 202,7</td></tr>
    <tr><td>Dispersión entre tercios (peor caso)</td><td class="n">19,0 niveles</td>
        <td class="n">3,0 niveles <span class="ok">✓</span></td></tr>
    <tr><td>Contraste del titular café sobre el fondo</td><td class="n">—</td>
        <td class="n">4,17:1 <span class="ok">✓</span> (la marca pide 3:1)</td></tr>
  </table>

  <div class="notas">
    <h3>Las dos referencias del cliente, y qué se tomó de cada una</h3>
  </div>
  <div class="fila" style="margin-top:14px">
    {lam('raw/hilton/between/refs-concurso-s3/REF1.jpg', '<b>REF 1</b> — recorte tipo sticker con borde blanco sobre pared lisa, titular grande y el remate dentro de una caja de color plano', 560)}
    {lam('raw/hilton/between/refs-concurso-s3/REF2.jpg', '<b>REF 2</b> — collage: rótulo arriba, figura recortada y una hoja pegada con la LISTA de ítems', 560)}
  </div>
  <div class="notas">
    <h3>Cómo se tradujo a Between</h3>
    <ul>
      <li>El <b>recorte con borde blanco</b> de las dos referencias no se pegó por código: la escena
          se <b>generó ya recortada</b> con Nano Banana Pro, con la foto real del segundo piso y las
          del vaso To Go vigente como referencia. Es el método de Eli: no se compone, se genera.</li>
      <li>La <b>caja de color plano</b> de la REF 1 es, literal, la <b>caja taupe #675B49</b> que la
          marca ya tiene. No se inventó ningún recurso.</li>
      <li>La <b>hoja con la lista</b> de la REF 2 es la <b>tarjeta crema con filas taupe y casillas ✓</b>,
          la misma que se aprobó en <b>C1 S2 CUMPLE N2</b>.</li>
      <li>El <b>sello CONCURSO</b> que pide el brief es la caja taupe girada 4°, no un sello dibujado:
          dibujarlo sí habría sido inventarle un recurso a la marca.</li>
      <li>⚠️ <b>No</b> se tomaron el papel arrugado, la cinta, las polaroids ni los garabatos de la
          REF 2: el repertorio de línea de Between son los trazos de tu <code>.svg</code>.</li>
    </ul>
  </div>
  <table>
    <tr><th>Qué se midió</th><th>Valor</th><th>Criterio</th></tr>
    <tr><td>Franja del titular, por tercios (portada)</td><td class="n">203,7 · 204,7 · 205,7</td>
        <td>sobre L≈150 → <b>tinta café</b> <span class="ok">✓</span></td></tr>
    <tr><td>Franja del titular, por tercios (slide 2)</td><td class="n">204,7 · 204,7 · 202,7</td>
        <td>sobre L≈150 → <b>tinta café</b> <span class="ok">✓</span></td></tr>
    <tr><td>Caja alta del titular, tinta</td><td class="n">74,4 · 74,4 · 73,9 px</td>
        <td>un carrusel, <b>un solo cuerpo</b> <span class="ok">✓</span></td></tr>
    <tr><td>Tono entre slides</td><td class="n">mediana 197 · 201</td>
        <td>QA de carrusel <span class="ok">✓ mismo tono</span></td></tr>
    <tr><td>Logotipo del vaso, al 300 %</td><td>BƎTWEEN / COFFEE & BAR</td>
        <td>completo <span class="ok">✓</span> (las tiradas 1 y 2 salieron rotas y se re-tiraron)</td></tr>
  </table>
</section>""")

    # ── 2 · STRUDEL ──────────────────────────────────────────────────────
    partes.append(f"""
<section>
  <h2>2 · ST 21-09 · Strudel de manzana</h2>
  <blockquote>«Eliminar MASA y agregar legal Imagen referencial»
    <small>grilla viva, hoja STORIES · estado EN CAMBIOS</small></blockquote>
  <div class="fila">
    {lam('out/hilton/between/togo-r25/_antes-BW-S4-Strudel.png', '<b>ANTES</b>', 520)}
    {lam('out/hilton/between/entrega-st-s4-21-22-09/BW ST 21-09 Strudel de manzana.png', '<b>AHORA</b> — sin MASA y con el legal', 520)}
  </div>
  <div class="notas">
    <h3>Lo que cambió</h3>
    <ul>
      <li>El listado pasa de «Masa · Manzana · Canela · Nueces» a <b>«Manzana · Canela · Nueces»</b>,
          y la pila sube 35 px porque la línea es más corta.</li>
      <li>El legal va <b>beige dentro de caja taupe</b>. Esa franja son los dos cuadrantes claros
          —hojaldre y manzana— y mide <b>159 · 162 · 165</b> por tercios: ninguna tinta suelta aguanta
          ahí (beige 1,5:1 · café 1,8:1). Con la caja el contraste deja de depender de la foto y da
          <b>6,3:1</b>. Es la salida que el propio cliente dejó escrita: «cuando no se logra visualizar
          los textos, puedes dejarlo en una caja del color café #675B49».</li>
      <li>La zona del ícono 🍎 sube a 1345–1495 para que el sticker del CM no tape el legal.</li>
      <li>⚠️ <b>Queda una discrepancia y es del cliente, no de diseño:</b> el titular dice
          «CUATRO INGREDIENTES» y el mosaico tiene cuatro cuadrantes, pero el listado quedó en tres.
          Confirmaste que el cambio es sólo eliminar la palabra; queda informado.</li>
    </ul>
  </div>
</section>""")

    # ── 3 · PRIMAVERA ────────────────────────────────────────────────────
    partes.append(f"""
<section>
  <h2>3 · ST 22-09 · Primavera en Between</h2>
  <blockquote>«Agregar legal Imagen referencial» <small>grilla viva, hoja STORIES · EN CAMBIOS</small></blockquote>
  <blockquote>«ajusta el legal abajo donde indica la flecha porque no se lee bien»
    <small>Eli, 16-09 · marcado en rojo sobre el render</small></blockquote>
  <div class="fila">
    {lam('out/hilton/between/togo-r25/_antes-BW-S4-Primavera.png', '<b>ANTES</b> — sin legal', 430)}
    {lam('out/hilton/between/togo-r25/_medio-primavera.png', '<b>1.ª pasada</b> — el legal caía sobre el vidrio de la copa', 430)}
    {lam('out/hilton/between/entrega-st-s4-21-22-09/BW ST 22-09 Primavera en Between.png', '<b>AHORA</b> — bajo la base, sobre la mesa', 430)}
  </div>
  <div class="notas">
    <h3>Dónde quedó, y por qué ahí</h3>
    <ul>
      <li>La base de la copa cierra en <b>y=1796</b>. Las bandas de abajo, por tercios:
          1750–1780 → 87 · 115 · 112 (todavía pisa la base) · <b>1810–1840 → 92 · 92 · 120</b> (madera limpia).</li>
      <li>Queda en el <b>margen de marca (84 px del pie)</b>: la tinta cae en 1808–1836,
          12 px bajo la copa y sobre madera oscura.</li>
      <li>⚠️ Entra <b>256 px</b> en la franja inferior de 340 de Meta. Tiene precedente en la cuenta
          (el legal del cumpleaños entra 122 y tu plantilla con logo abajo entra 104).
          <b>Si esta pieza pasara a pauta, hay que rehacer el pie.</b></li>
    </ul>
  </div>
</section>""")

    # ── 4 · TO GO ────────────────────────────────────────────────────────
    partes.append(f"""
<section>
  <h2>4 · Carrusel PROMOS TO GO · la portada</h2>
  <blockquote>«Perdón, se puso mal el enlace: es esta en la G1 …/1ZUClVyKcfy_WNcXw8eKhSxe46H7Dpv3i»
    <small>grilla viva, FEED · el comentario más nuevo de la columna</small></blockquote>
  <p class="que">Las otras tres slides quedan como están: las diste por OK.</p>
  <div class="fila">
    {lam('out/hilton/between/togo-r25/antes.png', '<b>ANTES</b> — ronda 23, la foto de la entrada (IMG_4170)', 430)}
    {lam('public/assets/hilton/between/togo-sep2026/togo-en-mano-mesa.jpg', '<b>La foto que enlazaste</b> — IMG_4146, sin tocar', 430)}
    {lam('out/hilton/between/entrega-togo-r25/BW FEED 22-09 Promos To Go 1 portada.png', '<b>AHORA</b>', 430)}
  </div>
  <div class="notas">
    <h3>Las dos decisiones que hubo que tomar, y sus números</h3>
    <ul>
      <li><b>La foto NO se grada.</b> Entra tal cual el enlace: sin revelado, sin vibrancia y sin
          calor. Lo único que se hace es el recorte 4:5, que no es opcional (la toma es 3:4).
          ⚠️ Queda anotado que el set del carrusel está en mediana 101 y esta toma en 116: la portada
          va a leer más clara que las otras tres. Es lo que pediste.</li>
      <li><b>El degradado bajó de 0,72 a 0,60, y 0,60 es el piso.</b> Se barrió midiendo el contraste
          de la tinta beige —la marca pide 3:1— sobre script · titular · horario:<br>
          0,72 → 5,41 · 5,54 · 4,77 &nbsp;·&nbsp; 0,65 → 3,92 · 4,98 · 4,05 &nbsp;·&nbsp;
          <b>0,60 → 3,27 · 4,79 · 3,95</b> &nbsp;·&nbsp; 0,55 → <b>2,91</b> · 4,28 · 3,84.
          Bajo 0,60 el script se cae del mínimo, así que lo que se aclaró fue la FOTO y no la
          transparencia: se levantaron las sombras de la mitad de arriba, que es donde dijiste que
          se veía oscura, y eso no toca el contraste del bloque.</li>
      <li><b>La raya del cartón.</b> `cv2.inpaint` dejaba un parche liso —sobre kraft se ve más que la
          raya— así que se clonó el grano real del propio vaso 150 px a la derecha, trasplantando sólo
          la alta frecuencia y conservando el sombreado del cilindro.</li>
      <li><b>El encuadre no es libre, y esta vez se midió contra el logotipo COMPLETO.</b> El lockup
          impreso son dos bandas: el wordmark en la fila 2239–2513 y «COFFEE & BAR» en 2617–2685.
          La primera pasada calculó contra el wordmark y el script terminaba rozando el «COFFEE &amp;
          BAR». Con el logotipo entero cerrando en 2685, la ventana no puede medir más de
          2 × (4032 − 2685) = <b>2694</b> de alto: queda 2155×2694 desde la fila 1338, con el
          logotipo en 33–50 % y el texto entrando en 53,2 %.</li>
      <li>⚠️ <b>El precio:</b> la tapa del vaso se corta por el canto de arriba. Es inevitable —
          con la tapa entera haría falta un alto de 2882 y el máximo que cabe en la toma es 2788.</li>
    </ul>
  </div>
</section>""")

    html = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Between · revisión 16-09-2026</title>
<style>{CSS}</style></head><body><div class="wrap">
<header>
  <span class="tag">BETWEEN · 16 DE SEPTIEMBRE 2026</span>
  <h1>Concurso CEO del café, y los ajustes de la S3 y la S4</h1>
  <p class="sub">Todo lo de esta página ya está subido al Drive. Las stories y la portada del To Go
     reemplazan el MISMO archivo, así que los enlaces de la grilla no cambiaron.</p>
  <div class="notas" style="margin-top:22px">
    <h3>Ronda 4 — lo último que pediste</h3>
    <ul>
      <li>«el fondo debe ser el <b>mismo beige papel</b> para ambas slides, que sea <b>plano</b> y
          <b>transicione</b>» → las dos paredes generadas (una lisa, la otra con veta de madera) se
          reemplazaron por <b>una sola hoja de papel beige</b> sintetizada a 4500 px y cortada en dos.
          El recorte no se tocó y la sombra del sticker se rehizo con el peso que ya tenía.
          Está todo en el apartado 1, con el antes y el después.</li>
    </ul>
  </div>
  <div class="notas" style="margin-top:14px">
    <h3>Ronda 3 — lo anterior</h3>
    <ul>
      <li>«que la <b>textura beige del fondo haga transición</b> en ambas slides» → la pared es ahora
          un solo campo continuo a lo largo de las dos láminas. Salto en la costura: <b>0,95</b> de
          luminancia (el umbral de la cuenta es 1,5). No se tocó ni un píxel de los sujetos.</li>
      <li>«añade la <b>polaroid</b> de la misma chica de frente, feliz» → generada con la portada
          aprobada como referencia de personaje, y puesta abajo a la izquierda, que es el único hueco
          de la lámina sin texto ni producto.</li>
      <li>«el último carrusel <b>muy oscuro y con una raya</b>» → la raya era un pliegue del cartón y
          se quitó clonando el grano real del propio vaso; y se levantaron las sombras <b>sólo arriba</b>,
          apagándose en y=0,45 para no tocar el contraste del texto.</li>
    </ul>
  </div>
  <div class="notas" style="margin-top:14px">
    <h3>Ronda 2 — las cuatro correcciones anteriores</h3>
    <ul>
      <li>«la chica debe verse <b>más blanca chilena, pelo ondulado y con gafas lifestyle</b>» →
          escena regenerada. ⚠️ «Más blanca» se pidió <b>nombrando el tipo</b> («chilena de piel clara,
          rasgos latinoamericanos»): pedir «menos morena» empuja el fenotipo al nórdico.</li>
      <li>«la segunda slide no se parece a la referencia 2, <b>añade esas ilustraciones sencillas</b>» →
          cuatro motivos dibujados en la tinta café de la marca: las tres cuñas que recortaste,
          una chispa, una estrella de contorno y una flecha. Dos en la portada, cuatro en la 2.</li>
      <li>«<b>legal del strudel en beige o con caja</b>, que no se ve nada» → beige dentro de caja taupe.
          Es la salida que el propio cliente dejó escrita para este caso.</li>
      <li>«la portada del To Go muy oscura y quemada, <b>no edites la foto original</b>» →
          fuera toda la gradación: la foto entra tal cual el enlace. Y el degradado bajó de 0,72 a 0,60.</li>
    </ul>
  </div>
</header>
{''.join(partes)}
<footer>
  Generada por <code>scripts/between-revision-16-09.py</code> · las imágenes van embebidas,
  la página se abre con doble clic y no necesita internet.
</footer>
</div></body></html>"""

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(html, encoding="utf-8")
    print(f"✓ {SALIDA}  ({SALIDA.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la página de revisión del ESTÁTICO HILTON HONORS (FEED col K · 23-09).

Regla del estudio (`antes-y-despues-en-html`): **Eli aprueba mirando y
comparado.** Cada ronda se entrega como una página HTML con la referencia al
lado de la pieza; los números van abajo, no arriba.

La página es UN SOLO ARCHIVO: las imágenes van embebidas como `data:` URI
reducidas a 1100 px, así se puede mandar por WhatsApp o Drive sin que se rompan
los enlaces. El máster de 2250 px se entrega aparte.

Uso:
    python scripts/dt-ft-honors-revision.py
"""
import base64
import io
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "out/hilton/dt/ft-honors"
DESTINO = SALIDA / "Post n°1 S4 DT - revision.html"

PIEZA = SALIDA / "Post n°1 S4 DT.png"
RONDA1 = SALIDA / "_rondas/ronda1.png"
GUIA = SALIDA / "GUIAS QA/Post n°1 S4 DT - GUIA.png"
REFERENCIA = RAIZ / "raw/hilton/dt/ref-s4/ref-post-s4-1080.jpg"
FOTO = RAIZ / "public/assets/hilton/dt/ft-honors-lobby.jpg"


def uri(ruta: Path, ancho: int = 1100, calidad: int = 82) -> str:
    im = Image.open(ruta).convert("RGB")
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


HTML = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Post n°1 S4 DT — Hilton Honors</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@400;500;700&family=Archivo:wght@400;500;600&display=swap">
<style>
  :root {
    --azul:#09194E; --verde:#6F9418; --rojo:#B3261E; --ambar:#8A6516;
    --papel:#F1F2F6; --superficie:#FFFFFF; --tinta:#111A33; --tinta-2:#5C6480;
    --linea:#D6D9E3; --linea-fina:#E7E9F0;
    --sombra:0 1px 2px rgba(9,25,78,.06), 0 8px 24px rgba(9,25,78,.05);
    --display:'Zilla Slab',Georgia,serif; --cuerpo:'Archivo','Helvetica Neue',Arial,sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --azul:#9FB4EC; --verde:#A3CD39; --rojo:#FF9C92; --ambar:#E0AE4A;
      --papel:#080C18; --superficie:#101731; --tinta:#E6E9F4; --tinta-2:#97A0BC;
      --linea:#26304F; --linea-fina:#1B2440;
      --sombra:0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.28);
    }
  }
  :root[data-theme="dark"] {
    --azul:#9FB4EC; --verde:#A3CD39; --rojo:#FF9C92; --ambar:#E0AE4A;
    --papel:#080C18; --superficie:#101731; --tinta:#E6E9F4; --tinta-2:#97A0BC;
    --linea:#26304F; --linea-fina:#1B2440;
    --sombra:0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.28);
  }
  *{box-sizing:border-box}
  body{background:var(--papel);color:var(--tinta);font-family:var(--cuerpo);
       font-size:16px;line-height:1.6;margin:0;padding-inline:24px;padding-block:0 96px}
  .caja{max-width:1180px;margin-inline:auto}
  header{padding-block:56px 12px}
  .sello{font-family:var(--cuerpo);font-weight:600;font-size:12px;letter-spacing:.14em;
         text-transform:uppercase;color:var(--azul)}
  h1{font-family:var(--display);font-weight:500;font-size:clamp(30px,5vw,46px);
     line-height:1.1;margin:8px 0 10px}
  .sub{color:var(--tinta-2);max-width:62ch;margin:0}
  h2{font-family:var(--display);font-weight:500;font-size:clamp(21px,3vw,27px);
     margin:56px 0 6px;padding-top:22px;border-top:1px solid var(--linea)}
  h3{font-family:var(--display);font-weight:500;font-size:19px;margin:26px 0 6px}
  .nota{color:var(--tinta-2);margin:0 0 18px;max-width:70ch}
  .par{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px}
  figure{margin:0;background:var(--superficie);border:1px solid var(--linea-fina);
         border-radius:14px;overflow:hidden;box-shadow:var(--sombra)}
  figure img{display:block;width:100%;height:auto}
  figcaption{padding:12px 16px 14px;font-size:13.5px;color:var(--tinta-2);
             border-top:1px solid var(--linea-fina)}
  figcaption b{color:var(--tinta);font-weight:600}
  .tabla{width:100%;border-collapse:collapse;font-size:14.5px;margin-top:8px}
  .tabla th,.tabla td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--linea-fina);
                      vertical-align:top}
  .tabla th{font-weight:600;color:var(--tinta-2);font-size:12.5px;letter-spacing:.06em;
            text-transform:uppercase}
  .tabla td.n{font-variant-numeric:tabular-nums;white-space:nowrap}
  .ok{color:var(--verde);font-weight:600}
  .ojo{color:var(--ambar);font-weight:600}
  .mal{color:var(--rojo);font-weight:600}
  .aviso{background:var(--superficie);border:1px solid var(--linea);border-left:4px solid var(--ambar);
         border-radius:12px;padding:18px 20px;margin:18px 0;box-shadow:var(--sombra)}
  .aviso h3{margin-top:0}
  .aviso p:last-child{margin-bottom:0}
  pre{background:var(--superficie);border:1px solid var(--linea-fina);border-radius:12px;
      padding:16px 18px;overflow-x:auto;font-size:13px;line-height:1.55;margin:0}
  code{font-family:ui-monospace,Menlo,Consolas,monospace}
  ul{margin:8px 0 0;padding-left:20px}
  li{margin-bottom:6px}
  .tachado{text-decoration:line-through;color:var(--tinta-2)}
  .pie{margin-top:64px;padding-top:20px;border-top:1px solid var(--linea);
       color:var(--tinta-2);font-size:14px}
  .envoltorio{overflow-x:auto}
</style>
</head>
<body>
<div class="caja">

<header>
  <div class="sello">DoubleTree by Hilton Santiago–Vitacura · Semana 4</div>
  <h1>Estático Hilton Honors</h1>
  <p class="sub">FEED columna K · publica el <b>23-09 a las 18:00</b> · estado de la grilla
  <b>OK PARA DISEÑO</b>. <b>Ronda 2.</b> Máster a 2250×2813.</p>
</header>

<h2>Antes, después y la referencia</h2>
<p class="nota">En el medio la <b>ronda 2</b>, con tus seis marcas aplicadas. A la
izquierda la ronda 1 para comparar. A la derecha <b>Ref post s4.jpg</b>, la que subiste
hoy a las 13:43 — que resulta ser el mismo pin que enlaza el brief en su celda LINKS.</p>
<div class="par" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">
  <figure>
    <img src="__RONDA1__" alt="Ronda 1">
    <figcaption><b>Ronda 1</b> — titular a la izquierda, logotipo azul, rótulos en Trade
    Gothic, velo fuerte desde arriba.</figcaption>
  </figure>
  <figure style="outline:3px solid var(--verde)">
    <img src="__PIEZA__" alt="Ronda 2">
    <figcaption><b>Ronda 2 — la que va</b>. Titular centrado, logotipo blanco con sombra,
    tus íconos, velo más abajo y más suave.</figcaption>
  </figure>
  <figure>
    <img src="__REF__" alt="Referencia">
    <figcaption><b>Tu referencia</b> — de ahí salen la caja de cristal con cuadrantes, los
    íconos de línea con su rótulo al lado y la regla fina al pie.</figcaption>
  </figure>
</div>

<h2>Tus seis marcas, una por una</h2>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Lo que pediste</th><th>Qué se hizo</th></tr>
  <tr><td><b>«Te falta el logo de Hilton Honors»</b></td>
      <td class="mal">⚠️ <b>Es lo único que quedó pendiente</b>, y no por olvido — ver el
      aviso de abajo. El hueco ya está reservado donde lo dibujaste.</td></tr>
  <tr><td><b>«Usa íconos ya utilizados en mis piezas»</b></td>
      <td><b>La cama es tuya, literal:</b> extraída de <code>C1 FT N2</code>
      («Habitación doble») a resolución completa. Los otros tres no existen en ningún
      editable al que pueda llegar, así que se dibujaron <b>calcando tu trazo</b> —medido
      en esa cama: 2,4 px, esquinas redondeadas, caja de 71×57—. También entró tu
      <b>regla vertical</b> entre ícono y rótulo, que yo no tenía.</td></tr>
  <tr><td><b>«El título déjalo centrado»</b></td><td>Centrado. Medido: los tres centros
      caen en 538-539 sobre 540.</td></tr>
  <tr><td><b>«Logo blanco»</b></td><td>Blanco. Era azul por la §B.4 del manual («va en
      azul cuando el fondo es demasiado blanco»); tu criterio la levanta para esta pieza
      y queda anotado como excepción de pieza, no como cambio de la marca.</td></tr>
  <tr><td><b>«Conserva la imagen del fondo»</b></td><td>Intacta: mismo encuadre, mismo
      revelado.</td></tr>
  <tr><td><b>«La transparencia azul más abajo y sutil»</b></td>
      <td>El velo baja de <b>0,58 a 0,50</b> al pie y, sobre todo, <b>arranca mucho más
      abajo</b>: en el 20 % de la altura iba en 0,22 y ahora va en <b>0,03</b>; en la
      mitad, de 0,48 a <b>0,23</b>. Se curvó la rampa en vez de cortarla, para que no
      aparezca el codo que te molestó en el Día del Turismo.</td></tr>
  <tr><td><b>«Sombra paralela muy sutil»</b></td>
      <td>En todas las tintas blancas, en azul DoubleTree (no negro, que ensucia sobre
      foto cálida). Subió el titular de 3,76:1 a <b>4,2-5,3:1</b>.</td></tr>
</table>
</div>

<div class="aviso">
  <h3>⭐ Un hallazgo de paso: los rótulos del panel van en Stag, no en Trade Gothic</h3>
  <p>Al medir tu cama aproveché de medir el texto que va al lado. Glifo a glifo sobre
  «Desayuno buffet» de <code>DT FT S3</code> (14 letras, IoU 2D):</p>
  <p style="font-variant-numeric:tabular-nums"><b>Stag Regular 0,701</b> · Stag Medium
  0,608 · Stag Light 0,476 · Arial 0,389 · <b>Trade Gothic 0,285</b></p>
  <p>Yo los tenía en Trade siguiendo la regla «Trade para el cuerpo». <b>Están
  corregidos.</b> En tu panel el texto corrido va en Stag y Trade se queda con las
  versales y las cifras — en esa misma pieza, «IVA INCLUIDO» y la dirección sí son Trade.</p>
</div>

<h2>Lo que necesito que decidas</h2>

<div class="aviso">
  <h3>0 · El logo de Hilton Honors: necesito el archivo</h3>
  <p>Lo ubiqué en tu Drive —<i>GRILLA IA DT › Logos › Hilton Honors Logo_White PNG.png</i>,
  14 KB, ya es la versión blanca— pero <b>no logro bajarlo</b>: las tres rutas directas de
  Drive devuelven la pantalla de login, el token del estudio sólo ve lo que subió él, y el
  conector me entrega los archivos chicos de una forma que no queda en disco (lo intenté
  dos veces y llegó cortado; preferí borrarlo antes que montar un logotipo roto).</p>
  <p><b>Cópialo a mano a</b> <code>EDITOR VIDEOS/raw/hilton/dt/identidad/logos/</code>
  y lo monto en una corrida. El hueco ya está reservado en y 1186, centrado, entre la caja
  y la regla del pie — donde lo dibujaste.</p>
  <p class="mal">⛔ <b>Y ojo con una trampa de esa misma carpeta:</b> el archivo
  <code>hilton honors.png</code> (43 KB) <b>no es el logo de Hilton Honors</b> — es el
  logotipo <b>Hilton «For The Stay»</b>. Está mal rotulado. Ése sí lo pude bajar, lo miré,
  y por eso no lo usé.</p>
</div>

<div class="aviso">
  <h3>1 · El brief dice 6 cuadrantes y dejó 4 rótulos</h3>
  <p>No es un error de lectura: los otros dos existían y <b>el cliente los tachó</b> en la
  grilla, junto con el titular viejo. La línea que dice «6» quedó sin actualizar.</p>
  <ul>
    <li class="tachado">(Ícono señal wifi) «WiFi Premium»</li>
    <li class="tachado">(Ícono smartphone) «Check-in Digital»</li>
  </ul>
  <p style="margin-top:12px">Armé la caja con <b>4 cuadrantes (2×2)</b>, que es lo único
  que el brief permite sin inventar contenido. <b>Si el cliente quiere los 6</b>, la caja
  pasa a 3×2 y vuelven esos dos — es un cambio de media hora. <b>No lo resolví yo</b>:
  en esta cuenta el contenido no es nuestro.</p>
</div>

<div class="aviso">
  <h3>2 · El brief pide «cenital» y «piscina», y el banco no los tiene</h3>
  <p>Busqué en las 48 fotos de la sesión profesional en alta y en las 96 de las carpetas
  de muestra: <b>no hay ninguna toma aérea del hotel y no hay piscina</b>. El propio brief
  ofrece las alternativas en la misma frase —«o angular elegante», «instalaciones, lobby o
  habitación»— así que usé el <b>lobby</b>, con su fuga. Nada generado con IA.</p>
</div>



<h2>La guía de control</h2>
<p class="nota">Las bandas medidas, dibujadas encima. <b>No se entrega</b> — es para
revisar. Rosado el logotipo, celeste el titular, verde la caja, amarillo el pie; la línea
vertical es el eje y las dos blancas son el margen de 100 px.</p>
<div class="par" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr))">
  <figure>
    <img src="__GUIA__" alt="Guía de QA">
    <figcaption><b>Guía de bandas</b> — el titular es el único elemento alineado a la
    izquierda; el logotipo, la caja y el pie van centrados en el eje.</figcaption>
  </figure>
  <figure>
    <img src="__FOTO__" alt="La foto sin nada encima">
    <figcaption><b>La foto sola</b> — <code>HDT_36</code> de la sesión profesional, el
    lobby lounge. Original 6719×4479; recorte 3009×3762 <b>reducido</b> a 2250×2813, sin
    ampliar y sin estirar.</figcaption>
  </figure>
</div>

<h2>La geometría, medida contra la referencia</h2>
<p class="nota">La referencia es 1080×1350 y la pieza también, así que sus medidas se
trasladan <b>1:1</b> en vez de proporcionalmente. Todo lo de abajo está medido sobre
píxeles, no estimado.</p>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Elemento</th><th>Referencia</th><th>La pieza</th><th>De dónde sale</th></tr>
  <tr><td>Caja</td><td class="n">x 100→980 · ancho 880<br>y 842→1148 · alto 306</td>
      <td class="n">x 100→980 · ancho 880<br>y 842→1148 · alto 306</td>
      <td>Medida en el pin. <b>Más ancha que el panel de DT</b> (730 en <code>DT FT S3</code>):
      se adopta la de la referencia, como en el Día del Turismo.</td></tr>
  <tr><td>Altura de versal del titular</td><td class="n">49</td><td class="n">48</td>
      <td>Stag da versal = 0,700 × cuerpo, medido. Cuerpo 68.</td></tr>
  <tr><td>Eje del titular</td><td class="n">alineado a la izquierda</td>
      <td class="n">centrado · 538-539</td>
      <td><b>Ronda 2</b>: lo pediste centrado. La referencia lo lleva a la izquierda.</td></tr>
  <tr><td>Salto entre líneas</td><td class="n">68 (1,39 de versal)</td>
      <td class="n">66 (1,38 de versal)</td><td>Se calca la proporción, no el número.</td></tr>
  <tr><td>Regla del pie</td><td class="n">y 1258</td><td class="n">y 1258</td>
      <td>Calcada. Al ancho de la caja.</td></tr>
  <tr><td>Logotipo DT</td><td>—</td><td class="n">ancho 160 · tope 111 · centrado · <b>blanco</b></td>
      <td><b>No sale de la referencia</b>: sale de tu plantilla de márgenes
      <code>logo-post.png</code>. Escalado uniforme desde su proporción real 1,2254.</td></tr>
</table>
</div>

<h2>Las tintas, medidas sobre el PNG final</h2>
<p class="nota">Luminancia relativa <b>por tercios</b> de cada banda, con la sombra
paralela ya puesta, quedándose con el peor tercio. Son las cifras del archivo que se
entrega, no de una simulación.</p>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Elemento</th><th>Ronda 1</th><th>Ronda 2</th><th>Vara</th><th></th></tr>
  <tr><td>Logotipo DT</td><td class="n">4,84:1 <span style="color:var(--tinta-2)">(azul)</span></td>
      <td class="n ojo">3,61:1 <b>(blanco)</b></td><td class="n">4,5</td>
      <td>⚠️ <b>La única cifra que queda bajo la vara, y es consecuencia de dos cosas que
      pediste:</b> blanco + velo más suave, sobre el cielorraso, que es lo más claro de la
      foto. La sombra lo subió de 2,83 a 3,61 y <b>a la vista se lee bien</b> (la medición
      promedia toda la caja del logotipo y la sombra va pegada a la tinta). Si lo quieres
      en regla, la salida medida es volver al azul: 4,84:1.</td></tr>
  <tr><td>Titular</td><td class="n">6,13:1</td><td class="n ok">4,22 – 5,31:1</td>
      <td class="n">3,0</td><td>Vara de <b>texto grande</b>, que es la que fija tu propio
      manual desde el Día del Turismo.</td></tr>
  <tr><td>Rótulos de la caja</td><td class="n">8,1 – 11,9:1</td><td class="n ok">7,0 – 10,1:1</td>
      <td class="n">4,5</td><td></td></tr>
  <tr><td>Llamado del pie</td><td class="n">9,38:1</td><td class="n ok">8,60:1</td>
      <td class="n">4,5</td><td></td></tr>
</table>
</div>
<p class="nota" style="margin-top:14px"><b>El velo.</b> Sigue naciendo en 0 en el borde de
arriba —el codo que te molestó en el Día del Turismo no vuelve—, pero ahora la rampa es
convexa: casi no pesa hasta pasada la mitad. Y la caja va <b>de cristal (0,30)</b> y no
maciza como el panel de Family Time —medido, ése está en 0,84-0,90— porque el brief la
pide así con todas sus letras: «estilo cristal o translúcida».</p>
<p class="nota"><b>Probé y descarté</b> un halo suave detrás del logotipo, que es el
recurso que funcionó en el Día del Turismo para tapar el rótulo de la fachada: allá caía
sobre un cielo con textura y acá cae sobre un cielorraso plano, donde se veía como una
mancha gris. Se cambió por tres sombras paralelas apiladas sobre el propio logotipo.</p>

<h2>La compuerta de calidad</h2>
<p class="nota"><code>python scripts/dt-qa.py "out/hilton/dt/ft-honors/*.png"</code></p>
<pre><code>__QA__</code></pre>
<p class="nota" style="margin-top:14px">Cuatro cosas que este QA <b>aprendió con esta
pieza</b> y que quedan para las que vengan: que <b>el máster depende del formato</b>
(2250×4000 en historia, 2250×2813 en feed, y la zona segura de 340 px es sólo de historia);
que la huella de fuente por perfil de columnas <b>no sirve para un titular corto en
versales</b> —acusaba a esta pieza de sustitución de fuente estando perfecta— y ahora se
compara <b>glifo a glifo en 2D</b>; que <b>la vara de contraste depende del tamaño de la
tinta</b> (3:1 en titulares, 4,5 en el resto), que es lo que tu manual ya decía y el QA no
sabía; y que una <b>desviación que decidiste tú</b> —el logotipo blanco— se declara con su
número a la vista en vez de arreglarse por detrás o de dejar la compuerta en rojo.</p>

<h2>El texto, verbatim de la grilla</h2>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Dónde</th><th>Qué dice la pieza</th></tr>
  <tr><td>Titular</td><td>MÁS BENEFICIOS / EN CADA ESTADÍA / CON HILTON HONORS</td></tr>
  <tr><td>Cuadrante 1</td><td>Tarifas exclusivas</td></tr>
  <tr><td>Cuadrante 2</td><td>Upgrades de habitación</td></tr>
  <tr><td>Cuadrante 3</td><td>Canje de noches gratis</td></tr>
  <tr><td>Cuadrante 4</td><td>Acumula puntos en cada estadía</td></tr>
  <tr><td>Pie</td><td>Inscríbete gratis en el link de la bio</td></tr>
</table>
</div>
<p class="nota" style="margin-top:14px">No entra dirección, ni correo, ni legal: el brief no
los pide y agregarlos sería inventar contenido. Los cortes de línea sí son míos —eso es
diagramación—; las palabras no se tocaron.</p>

<div class="pie">
  <b>Máster:</b> <code>Post n°1 S4 DT.png</code> · 2250×2813 · subido a
  <i>S4 HILTON SEP 2026 › DT</i>.<br>
  <b>En el repo:</b> <code>src/compositions/hilton/DtFtHonors.tsx</code> ·
  <code>scripts/dt-ft-honors-foto.py</code> · <code>scripts/dt-rendir.py</code> ·
  <code>scripts/dt-qa.py</code>.
</div>

</div>
</body>
</html>
"""


def main() -> int:
    faltan = [p for p in (PIEZA, GUIA, FOTO, RONDA1) if not p.exists()]
    if faltan:
        for p in faltan:
            print(f"⛔ falta {p}")
        print("   Corre antes: python scripts/dt-ft-honors-foto.py && "
              "python scripts/dt-rendir.py DT-F-HiltonHonors DT-F-HiltonHonors-Guia "
              "--salida out/hilton/dt/ft-honors")
        return 1

    qa = SALIDA / "_qa.txt"
    salida_qa = qa.read_text(encoding="utf-8") if qa.exists() else "(sin correr)"

    html = (HTML
            .replace("__REF__", uri(REFERENCIA))
            .replace("__RONDA1__", uri(RONDA1))
            .replace("__PIEZA__", uri(PIEZA))
            .replace("__GUIA__", uri(GUIA))
            .replace("__FOTO__", uri(FOTO))
            .replace("__QA__", salida_qa.replace("&", "&amp;")
                     .replace("<", "&lt;").replace(">", "&gt;")))
    DESTINO.write_text(html, encoding="utf-8")
    print(f"→ {DESTINO.relative_to(RAIZ)}  {DESTINO.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())

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
  <b>OK PARA DISEÑO</b>. Ronda 1. Máster entregado a 2250×2813.</p>
</header>

<h2>La referencia y la pieza</h2>
<p class="nota">A la izquierda, <b>Ref post s4.jpg</b> — la que subiste hoy a
<i>REFERENCIAS S4 DT</i> a las 13:43, y que resulta ser el mismo pin que enlaza el
brief en su celda LINKS. A la derecha, la pieza.</p>
<div class="par">
  <figure>
    <img src="__REF__" alt="Referencia">
    <figcaption><b>Referencia</b> — foto a sangre, titular en versales a la izquierda,
    caja de cristal con cuadrantes e íconos de línea, regla fina al pie.</figcaption>
  </figure>
  <figure>
    <img src="__PIEZA__" alt="Pieza">
    <figcaption><b>La pieza</b> — la misma gramática, con la tipografía, el color, el
    velo y el logotipo de DoubleTree.</figcaption>
  </figure>
</div>

<h2>Lo que necesito que decidas</h2>

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

<div class="aviso">
  <h3>3 · Dónde va el titular</h3>
  <p>El brief dice «zona superior izquierda» y la referencia lo pone <b>a la izquierda, al
  49 % de la altura, justo encima de la caja</b>. Seguí la referencia, que es lo que me
  mandaste hoy para esta pieza. Queda a la izquierda como pide el brief. <b>Si lo quieres
  más arriba</b>, sube sin tocar nada más.</p>
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
  <tr><td>Canto izquierdo del titular</td><td class="n">116</td><td class="n">101</td>
      <td>En la referencia el titular y la caja van desfasados 16 px; acá se alinean.</td></tr>
  <tr><td>Salto entre líneas</td><td class="n">68 (1,39 de versal)</td>
      <td class="n">66 (1,38 de versal)</td><td>Se calca la proporción, no el número.</td></tr>
  <tr><td>Regla del pie</td><td class="n">y 1258</td><td class="n">y 1258</td>
      <td>Calcada. Al ancho de la caja.</td></tr>
  <tr><td>Logotipo</td><td>—</td><td class="n">ancho 160 · tope 111 · centrado</td>
      <td><b>No sale de la referencia</b>: sale de tu plantilla de márgenes
      <code>logo-post.png</code>. Escalado uniforme desde su proporción real 1,2254.</td></tr>
</table>
</div>

<h2>Las tintas — por qué el logotipo va azul</h2>
<p class="nota">Luminancia relativa <b>por tercios</b> de cada banda, sobre la foto ya
recortada y con el velo azul encima, quedándose con el peor tercio.</p>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Banda</th><th>α del velo</th><th>Tinta blanca</th><th>Tinta azul DT</th><th>Qué se usó</th></tr>
  <tr><td>Logotipo</td><td class="n">0,14</td><td class="n mal">3,29:1</td>
      <td class="n ok">4,84:1</td><td><b>Azul</b> — §B.4 del manual: va en azul cuando el
      fondo es demasiado blanco. El cielorraso del lobby es ese caso.</td></tr>
  <tr><td>Titular</td><td class="n">0,48</td><td class="n ok">6,13:1</td><td class="n">2,60:1</td><td>Blanco</td></tr>
  <tr><td>Caja</td><td class="n">0,55</td><td class="n ok">7,54:1</td><td class="n">2,12:1</td><td>Blanco</td></tr>
  <tr><td>Pie</td><td class="n">0,58</td><td class="n ok">9,89:1</td><td class="n">1,61:1</td><td>Blanco</td></tr>
</table>
</div>
<p class="nota" style="margin-top:14px">El velo es <b>el mismo que aprobaste en el Día del
Turismo</b>: nace en 0 en el borde de arriba y sube cóncavo hasta 0,58 al pie, sin ningún
codo. Y la caja va <b>de cristal (0,30)</b> y no maciza como el panel de Family Time
—medido, ése está en 0,84— porque el brief la pide así con todas sus letras: «estilo
cristal o translúcida».</p>

<h2>La compuerta de calidad</h2>
<p class="nota"><code>python scripts/dt-qa.py "out/hilton/dt/ft-honors/*.png"</code></p>
<pre><code>__QA__</code></pre>
<p class="nota" style="margin-top:14px">Dos cosas que este QA <b>aprendió con esta pieza</b>,
y que quedan para las que vengan: que <b>el máster depende del formato</b> (2250×4000 en
historia, 2250×2813 en feed, y la zona segura de 340 px es sólo de historia), y que la
huella de fuente por perfil de columnas <b>no sirve para un titular corto en versales</b> —
acusaba a esta pieza de sustitución de fuente estando perfecta. Ahora se comparan
<b>glifo a glifo en 2D</b>, que es la regla del estudio: Stag-Light dio 0,900 contra 0,630
del mejor señuelo.</p>

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
    faltan = [p for p in (PIEZA, GUIA, FOTO) if not p.exists()]
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

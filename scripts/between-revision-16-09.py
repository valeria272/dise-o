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
    <tr><td>Franja del titular, por tercios (portada)</td><td class="n">215,9 · 208,9 · 196,9</td>
        <td>sobre L≈150 → <b>tinta café</b> <span class="ok">✓</span></td></tr>
    <tr><td>Franja del titular, por tercios (slide 2)</td><td class="n">209,9 · 204,1 · 194,0</td>
        <td>sobre L≈150 → <b>tinta café</b> <span class="ok">✓</span></td></tr>
    <tr><td>Caja alta del titular, tinta</td><td class="n">74,4 · 74,4 · 73,9 px</td>
        <td>un carrusel, <b>un solo cuerpo</b> <span class="ok">✓</span></td></tr>
    <tr><td>Tono entre slides</td><td class="n">mediana 195 · 202</td>
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
      <li>El legal <b>va en café y no en beige</b>, y es medido: en esa franja los tercios dan
          <b>159 · 162 · 165</b> y sobre L≈150 la tinta que se lee es la café. Con el beige del
          sistema salía lavado sobre el hojaldre.</li>
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
      <li><b>El encuadre no es libre.</b> El bloque de texto —el que cerraste en la ronda 24— arranca
          en y=718 de 1350, y el logotipo impreso del vaso tiene que cerrar por encima de eso. Con la
          ventana a ancho completo el logotipo caía en el 60–66 % y <b>el titular se le montaba encima</b>.
          La ventana 2344×2930 desde la fila 1070 lo deja al 52 % y la tapa al 6 %.</li>
      <li><b>La gradación de la ronda 23 no se copió.</b> Aquella empuja calor porque la toma de la
          entrada venía fría (calidez 9,7). Ésta es madera al sol y entra en <b>50,9</b>: con la receta
          anterior subía a <b>66,3</b>, o sea el «filtro de color cálido» que mandaste eliminar.
          Queda en <b>33,1</b> — el set está en 25,9 y la portada aprobada de la r23 cerró en 34,2.</li>
    </ul>
  </div>
  <table>
    <tr><th></th><th>Portada r23 (la que estaba)</th><th>Portada r25 (ahora)</th><th>Set del carrusel</th></tr>
    <tr><td>mediana</td><td class="n">73</td><td class="n">71</td><td class="n">103</td></tr>
    <tr><td>calidez</td><td class="n">18,6</td><td class="n">17,2</td><td class="n">24,6</td></tr>
    <tr><td>saturación</td><td class="n">23,5</td><td class="n">30,3</td><td class="n">39,8</td></tr>
  </table>
  <p class="que" style="margin-top:14px">La diferencia de mediana contra el set viene del degradado al pie,
     que es parte del diseño que aprobaste: la portada anterior daba lo mismo (73 contra 71).
     En saturación la nueva se acerca más al set que la anterior.</p>
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

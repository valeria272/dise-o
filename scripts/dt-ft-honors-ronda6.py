#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la página de la RONDA 6 del ESTÁTICO HILTON HONORS (FEED col K · 23-09).

Regla del estudio (`antes-y-despues-en-html`): **se aprueba mirando y comparado.**
El antes, el después y la referencia arriba; los números abajo.

⚠️ Esta ronda es distinta de las anteriores: el cambio lo pidió una superior por
la grilla y **lo resolvió Eli en su editable**, no este repo. Acá se documenta y
se verifica, no se propone.

La página es UN SOLO ARCHIVO: las imágenes van embebidas como `data:` URI, así
se puede mandar por WhatsApp o Drive sin que se rompan los enlaces.

Uso:
    python scripts/dt-ft-honors-ronda6.py
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
DESTINO = SALIDA / "Post n°1 S4 DT - ronda 6.html"

DESPUES = SALIDA / "Post n°1 S4 DT.png"
ANTES = SALIDA / "_rondas/Post n°1 S4 DT - r5 titular justificado 15-09 (Illustrator).png"

# La escala del máster: la mesa es 1080 y se entrega a 2250.
E = 2250 / 1080

# El recorte de la caja, en píxeles del máster. Se toma generoso y el MISMO para
# las dos versiones: si se recortara cada una a su propia caja, el antes y el
# después saldrían del mismo tamaño y justamente no se vería lo que cambió.
CAJA_RECORTE = (int(85 * E), int(795 * E), int(995 * E), int(1140 * E))


def uri(im: Image.Image, calidad: int = 88) -> str:
    buf = io.BytesIO()
    im.convert("RGB").save(buf, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def entera(ruta: Path, ancho: int = 900) -> str:
    im = Image.open(ruta)
    return uri(im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS))


def recorte(ruta: Path, ancho: int = 1000) -> str:
    im = Image.open(ruta).crop(CAJA_RECORTE)
    return uri(im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS))


CSS = (RAIZ / "scripts/_revision.css").read_text(encoding="utf-8")

HTML = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Post n°1 S4 DT — ronda 6</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@400;500;700&family=Archivo:wght@400;500;600&display=swap">
<style>
__CSS__
  .cita{background:var(--superficie);border:1px solid var(--linea);border-left:4px solid var(--azul);
        border-radius:12px;padding:16px 20px;margin:10px 0;box-shadow:var(--sombra)}
  .cita p{margin:0 0 6px;font-family:var(--display);font-size:18px;line-height:1.45}
  .cita p:last-child{margin-bottom:0}
  .cita .quien{font-family:var(--cuerpo);font-size:12px;letter-spacing:.12em;
               text-transform:uppercase;color:var(--tinta-2);margin-top:10px}
</style>
</head>
<body>
<div class="caja">

<header>
  <div class="sello">DoubleTree by Hilton Santiago–Vitacura · Semana 4</div>
  <h1>Estático Hilton Honors — ronda 6</h1>
  <p class="sub">FEED columna K · publica el <b>23-09 a las 18:00</b> · máster 2250×2813.
  Dos cambios, los dos pedidos por la grilla. <b>Los resolvió Eli en el editable</b>;
  acá están verificados y medidos.</p>
</header>

<h2>Lo que se pidió</h2>
<div class="cita">
  <p>«donde dice canje podría ser así porfis — <b>Canje de / noches gratis</b>»</p>
  <p>«y el <b>recuadro en cada item sin tanto aire</b>, se ve como muy pelaitoo»</p>
  <p>«solo eso baby, lo demás lo veo todo oki en grillass»</p>
  <div class="quien">Comentario de la grilla · 16-09</div>
</div>

<h2>Antes y después</h2>
<p class="nota">A la izquierda la ronda 5, que es la que estaba entregada. A la derecha
la que va.</p>
<div class="par">
  <figure>
    <img src="__ANTES__" alt="Ronda 5">
    <figcaption><b>Ronda 5</b> — «gratis» colgando sola y el recuadro suelto.</figcaption>
  </figure>
  <figure style="outline:3px solid var(--verde)">
    <img src="__DESPUES__" alt="Ronda 6">
    <figcaption><b>Ronda 6 — la que va</b>.</figcaption>
  </figure>
</div>

<h2>El recuadro, de cerca</h2>
<p class="nota">El mismo recorte en las dos, para que se vea cuánto se apretó. Es el
cambio grande: la caja baja de 880×306 a <b>764×260</b> y se corre a y 842.</p>
<div class="par" style="grid-template-columns:1fr">
  <figure>
    <img src="__ANTES_CAJA__" alt="El recuadro antes">
    <figcaption><b>Antes</b> — celda de 153 con 61 de tinta: el <b>40 %</b>. Sobra caja,
    no falta tipografía.</figcaption>
  </figure>
  <figure style="outline:3px solid var(--verde)">
    <img src="__DESPUES_CAJA__" alt="El recuadro después">
    <figcaption><b>Después</b> — celda de 130 con 62 de tinta: el <b>47,4 %</b>. Y
    «Canje de / noches gratis» llena su celda en vez de dejar una línea huérfana.</figcaption>
  </figure>
</div>

<div class="aviso">
  <h3>⭐ La densidad a la que llegaste es la de tu propia pieza aprobada</h3>
  <p>Medí <code>DT FT S3</code>, que es la única pieza aprobada con esta misma estructura
  —ícono · regla vertical · rótulo de dos líneas, dentro de una celda cerrada por
  filetes—. Su celda mide <b>110,4</b> y su tinta <b>54,7</b>: el <b>49,5 %</b>.</p>
  <p>La ronda 5 de ésta iba en <b>40,1 %</b> y la ronda 6 quedó en <b>47,4 %</b>. O sea
  que «pelaitoo» tenía un número detrás, y el ajuste devolvió la pieza a la densidad con
  la que ya trabaja la cuenta.</p>
</div>

<h2>Todo lo que cambió, medido</h2>
<p class="nota">Medido sobre los dos PNG de entrega, en píxeles de la mesa de 1080.</p>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Elemento</th><th>Ronda 5</th><th>Ronda 6</th><th>Qué significa</th></tr>
  <tr><td>Rótulo del regalo</td><td>«Canje de noches» / «gratis»</td>
      <td><b>«Canje de» / «noches gratis»</b></td>
      <td>El texto del brief no se toca: sólo cambia dónde corta. Partido por el sentido,
      las dos líneas quedan parejas.</td></tr>
  <tr><td>Caja de cristal</td><td class="n">880 × 306 · y 812</td>
      <td class="n"><b>764 × 260 · y 842</b></td>
      <td>El ancho nuevo <b>es la medida a la que se justificó el titular</b> en la ronda
      5: el cuadro se apretó hasta su columna. Las tres líneas y la caja cierran ahora en
      la misma vertical.</td></tr>
  <tr><td>Celda · tinta</td><td class="n">153 · 40,1 %</td>
      <td class="n ok">130 · 47,4 %</td>
      <td>El aire por lado baja de <b>45,8 a ~32</b>.</td></tr>
  <tr><td>Logotipo Hilton Honors</td><td class="n">64 de alto · y 1156</td>
      <td class="n">81,6 de alto · y 1136</td>
      <td>Creció y quedó centrado solo en el hueco nuevo. Ancho 190,6 sobre los 189,4 que
      da su proporción real (2,3213): <b>no está deformado</b>.</td></tr>
  <tr><td>Titular</td><td class="n">base 608 · 697 · 774</td>
      <td class="n">base 620 · 709 · 786</td>
      <td>Mismo cuerpo y misma medida: <b>bajó 12 px en bloque</b>.</td></tr>
  <tr><td>Regla del pie</td><td class="n">880 · y 1252</td><td class="n">880 · y 1252</td>
      <td><b>No siguió a la caja.</b> Se quedó donde estaba, así que la pieza mantiene su
      margen de 100 abajo.</td></tr>
  <tr><td>Foto · logotipo DT · llamado</td><td colspan="2" class="n ok">idénticos</td>
      <td>Verificado píxel a píxel antes de reemplazar la entrega: diferencia máxima
      <b>0</b>.</td></tr>
</table>
</div>

<h2>La compuerta</h2>
<p class="nota">El QA por programa, con las bandas re-medidas sobre esta entrega.</p>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Chequeo</th><th>Resultado</th></tr>
  <tr><td>Máster</td><td class="n ok">2250×2813 ✓</td></tr>
  <tr><td>Sustitución de fuente (huella por glifos)</td>
      <td class="ok">Stag-Medium 0,918 · Stag-Light 0,879 y 0,901 · Stag-Regular 0,878 —
      todas ganan a su mejor señuelo por más de 0,20 ✓</td></tr>
  <tr><td>Contraste de las tintas</td>
      <td class="ok">titular 3,87–5,65:1 (vara 3,0 de texto grande) · rótulos 6,3–9,5:1 ·
      Honors 6,36:1 · llamado 8,33:1 ✓</td></tr>
  <tr><td>Logotipo DT</td>
      <td class="ojo">silueta ✓ · contraste 3,01:1, <b>desviación declarada</b>: blanco y
      sin sombra ni halo, decisión tuya de la ronda 3.</td></tr>
  <tr><td>Filetes de la caja</td><td class="n ok">tope y pie, centrados en 540 ✓</td></tr>
</table>
</div>

<div class="aviso">
  <h3>Dónde vive la pieza ahora</h3>
  <p>La entrega <b>se exporta del editable</b>
  (<code>editable/Post n°1 S4 DT - EDITABLE.ai</code>), no de Remotion. Ésa es la fuente
  de verdad desde la ronda 5.</p>
  <p>La composición del repo
  (<code>src/compositions/hilton/DtFtHonors.tsx</code>) quedó <b>sincronizada contra ese
  export</b>: rinde la misma pieza dentro de <b>±2 px</b> en todos sus elementos y pasa el
  mismo QA con los mismos números. Sirve de respaldo reproducible; la que se entrega es
  la del <code>.ai</code>.</p>
</div>

<p class="pie">Generado por <code>scripts/dt-ft-honors-ronda6.py</code>. Las imágenes van
embebidas: el archivo se puede mandar tal cual.</p>

</div>
</body>
</html>
"""


def main() -> int:
    for r in (ANTES, DESPUES):
        if not r.exists():
            print(f"⛔ falta {r}")
            return 1
    h = (HTML
         .replace("__CSS__", CSS)
         .replace("__ANTES__", entera(ANTES))
         .replace("__DESPUES__", entera(DESPUES))
         .replace("__ANTES_CAJA__", recorte(ANTES))
         .replace("__DESPUES_CAJA__", recorte(DESPUES)))
    DESTINO.write_text(h, encoding="utf-8")
    print(f"✅ {DESTINO}  ({DESTINO.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

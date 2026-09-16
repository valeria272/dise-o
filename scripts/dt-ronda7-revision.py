#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la página de la RONDA 7 de DOUBLETREE — los DOS estáticos de S3 y S4.

Regla del estudio (`antes-y-despues-en-html`): **se aprueba mirando y comparado.**
El antes, el después y el detalle arriba; los números abajo.

⭐ Esta ronda es **del cliente**, no de Eli ni de una superior:

  · ST 18-09 (S3) — Javier Meza por WhatsApp: «2 ajustes · Quitar punto final ·
    Hacerle más zoom a foto de animadores para que se vean más grandes» y
    «el resto ok!».
  · FEED 23-09 (S4) — grilla, comentario SIN TACHAR y en rojo: «Cambiemos foto
    por habitación de categoría superior y ok!».

⛔ La tercera pieza de la ronda —la ST animada del 21-09 (Escapada Romántica)—
**la hace Eli**, decisión suya del 16-09. Acá no entra.

La página es UN SOLO ARCHIVO: las imágenes van embebidas como `data:` URI, así
se puede mandar por WhatsApp o subir a Drive sin que se rompan los enlaces.

Uso:
    python scripts/dt-ronda7-revision.py
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
DESTINO = RAIZ / "out/hilton/dt/DT S3-S4 - ronda 7.html"

ST = RAIZ / "out/hilton/dt/st-18sep-fiestas"
FT = RAIZ / "out/hilton/dt/ft-honors"

ST_DESPUES = ST / "DT ST 18-09 Felices Fiestas Patrias.png"
ST_ANTES = ST / "_rondas/DT ST 18-09 Felices Fiestas Patrias - ronda 6.png"
FT_DESPUES = FT / "Post n°1 S4 DT.png"
FT_ANTES = FT / "_rondas/Post n°1 S4 DT - r6 ENTREGADA 16-09 (Illustrator).png"

# Las alternativas de foto que se midieron y se descartaron, para que la decisión
# quede a la vista y no haya que creerle a una tabla.
PRUEBAS = RAIZ / "public/assets/hilton/dt/_pruebas"

# Escalas de máster: la mesa es 1080 de ancho.
E_ST = 4000 / 1920      # historia 2250×4000  →  2,0833
E_FT = 2813 / 1350      # feed     2250×2813  →  2,0837

# Recortes, en coordenadas de la MESA (1080×1920 y 1080×1350). Se toman generosos
# y los MISMOS para el antes y el después: recortar cada uno a su propia caja
# haría que los dos salieran iguales y justamente no se vería lo que cambió.
CAJA_ANIMADORES = (401, 1133, 1080, 1438)     # el cuadro del escenario, en el mosaico
CAJA_PUNTO = (280, 880, 800, 1000)            # la última línea de la bajada


def uri(im: Image.Image, calidad: int = 88) -> str:
    buf = io.BytesIO()
    im.convert("RGB").save(buf, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def entera(ruta: Path, ancho: int = 760) -> str:
    im = Image.open(ruta)
    return uri(im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS))


def recorte(ruta: Path, caja, escala: float, ancho: int = 1000) -> str:
    x0, y0, x1, y1 = (round(v * escala) for v in caja)
    im = Image.open(ruta).crop((x0, y0, x1, y1))
    return uri(im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS))


CSS = (RAIZ / "scripts/_revision.css").read_text(encoding="utf-8")

HTML = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DT S3 y S4 — ronda 7</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@400;500;700&family=Archivo:wght@400;500;600&display=swap">
<style>
__CSS__
  .cita{background:var(--superficie);border:1px solid var(--linea);border-left:4px solid var(--azul);
        border-radius:12px;padding:16px 20px;margin:10px 0 22px;box-shadow:var(--sombra)}
  .cita p{margin:0 0 6px;font-family:var(--display);font-size:18px;line-height:1.45}
  .cita p:last-child{margin-bottom:0}
  .cita .quien{font-family:var(--cuerpo);font-size:12px;letter-spacing:.12em;
               text-transform:uppercase;color:var(--tinta-2);margin-top:10px}
  .tira{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px;margin-top:8px}
  .tira figure{border-radius:10px}
  .tira figcaption{padding:9px 11px 11px;font-size:12.5px}
  .desc{outline:2px solid var(--rojo)}
  .elegida{outline:3px solid var(--verde)}
</style>
</head>
<body>
<div class="caja">

<header>
  <div class="sello">DoubleTree by Hilton Santiago–Vitacura · Septiembre 2026</div>
  <h1>Los dos estáticos de S3 y S4 — ronda 7</h1>
  <p class="sub">Ronda <b>del cliente</b>. Son dos piezas y tres cambios, todos pedidos
  por escrito. Nada más se tocó: una ronda no es la oportunidad de re-diseñar.</p>
</header>

<h2>1 · Historia 18-09 · Saludo Fiestas Patrias</h2>
<div class="cita">
  <p>«2 ajustes»</p>
  <p>· <b>Quitar punto final</b></p>
  <p>· <b>Hacerle más zoom a foto de animadores</b> para que se vean más grandes</p>
  <p>«el resto ok!»</p>
  <div class="quien">Javier Meza · WhatsApp · 16-09 10:22</div>
</div>

<div class="par">
  <figure>
    <img src="__ST_ANTES__" alt="Historia, ronda 6">
    <figcaption><b>Ronda 6</b> — la que está en el Drive.</figcaption>
  </figure>
  <figure class="elegida">
    <img src="__ST_DESPUES__" alt="Historia, ronda 7">
    <figcaption><b>Ronda 7 — la que va.</b></figcaption>
  </figure>
</div>

<h3>Los animadores, de cerca</h3>
<p class="nota">El mismo recorte en las dos, para que se vea cuánto se acercaron. Es un
zoom dentro del cuadro del mosaico: la foto no se deforma, se recorta.</p>
<div class="par" style="grid-template-columns:1fr">
  <figure>
    <img src="__ST_ANIM_ANTES__" alt="Los animadores antes">
    <figcaption><b>Antes</b> — la pareja ocupaba <b>368 px de los 1415</b> de ancho del
    cuadro: el <b>26 %</b>. Se leía el escenario, no ellos.</figcaption>
  </figure>
  <figure class="elegida">
    <img src="__ST_ANIM_DESPUES__" alt="Los animadores después">
    <figcaption><b>Después</b> — zoom <b>1,45×</b>: quedan en <b>534 px</b>, el
    <b>38 %</b>. El corte cae a media caña de la bota, que es un plano americano.
    Más zoom los subiría hasta la cintura y se perdería el traje de huaso, que es
    justo lo que hace la foto.</figcaption>
  </figure>
</div>

<h3>El punto final</h3>
<div class="par" style="grid-template-columns:1fr">
  <figure>
    <img src="__ST_PUNTO_ANTES__" alt="Antes, con punto">
    <figcaption><b>Antes</b> — «DOUBLETREE<b>.</b>» · ancho de tinta <b>340 px</b>.</figcaption>
  </figure>
  <figure class="elegida">
    <img src="__ST_PUNTO_DESPUES__" alt="Después, sin punto">
    <figcaption><b>Después</b> — «DOUBLETREE» · <b>335 px</b>, y el bloque queda
    re-centrado solo.</figcaption>
  </figure>
</div>

<div class="aviso">
  <h3>⚠️ Ojo con una cosa, porque es la regla de la cuenta</h3>
  <p>En DT los textos van <b>literales del brief</b> y no los edita diseño. El brief dice
  «Gracias por ser parte de nuestra familia DoubleTree<b>.</b>», con punto. Se sacó
  porque <b>lo pidió el cliente por escrito</b>, no por criterio nuestro. Queda anotado
  para que nadie lo lea como que el texto se puede tocar.</p>
</div>

<h2>2 · Post 23-09 · Estático Hilton Honors</h2>
<div class="cita">
  <p>«<b>Cambiemos foto por habitación de categoría superior</b> y ok!»</p>
  <div class="quien">Grilla · FEED columna K · el único comentario sin tachar</div>
</div>

<p class="nota">Es un cambio <b>de foto y de nada más</b>: el titular justificado de la
ronda 5 y el recuadro apretado de la ronda 6 quedan exactamente como los dejaste.</p>
<div class="par">
  <figure>
    <img src="__FT_ANTES__" alt="Post, ronda 6">
    <figcaption><b>Ronda 6</b> — el lobby. Es la que está en el Drive.</figcaption>
  </figure>
  <figure class="elegida">
    <img src="__FT_DESPUES__" alt="Post, ronda 7">
    <figcaption><b>Ronda 7 — la que va.</b> La suite: cama entera a la derecha y el
    estar con escritorio y ventanal a la izquierda.</figcaption>
  </figure>
</div>

<h3>Por qué ésta y no otra</h3>
<p class="nota">Se probaron <b>once habitaciones</b> del banco. La diagramación de esta
pieza pone tinta <b>blanca</b> sobre el tercio medio de la foto, donde el velo azul
todavía casi no pesa — o sea que una habitación clara se come el titular. Medido con el
velo real de la pieza, no con el de historia:</p>
<div class="tira">
  <figure class="elegida">
    <img src="__P_SUITE__" alt="La elegida">
    <figcaption><b>HDT_68 · la que va</b><br>titular <b>3,4:1</b> ✓</figcaption>
  </figure>
  <figure>
    <img src="__P_ESTAR68__" alt="Alternativa">
    <figcaption><b>HDT_68 corrida al estar</b><br>pasa también — la tienes a un comando
    si la prefieres</figcaption>
  </figure>
  <figure class="desc">
    <img src="__P_KING__" alt="Descartada">
    <figcaption><b>HDT_66</b> cama king<br>titular <b>2,1:1</b> ⛔</figcaption>
  </figure>
  <figure class="desc">
    <img src="__P_BIENV__" alt="Descartada">
    <figcaption><b>HDT_65</b> con bienvenida<br>titular <b>2,8:1</b> ⛔ y lee «Escapada
    Romántica»</figcaption>
  </figure>
</div>

<div class="aviso">
  <h3>⛔⛔ Y acá hay algo que tienes que decidir tú: el editable quedó atrás</h3>
  <p>Desde la ronda 5 la entrega salía de tu <code>.ai</code>. Esta ronda <b>se rindió
  desde el repo</b> (<code>DtFtHonors.tsx</code>), porque el cambio es la foto de fondo y
  ahí la composición reproduce tu pieza dentro de <b>±2 px</b> y pasa el mismo QA.</p>
  <p>O sea que <code>editable/Post n°1 S4 DT - EDITABLE.ai</code> <b>sigue con el lobby</b>.
  Si la próxima ronda la trabajas ahí, hay que cambiarle la foto primero — está lista en
  <code>public/assets/hilton/dt/ft-honors-habitacion.jpg</code>, ya recortada a
  2250×2813.</p>
</div>

<h2>Los números</h2>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Pieza</th><th>Qué cambió</th><th>Antes</th><th>Después</th></tr>
  <tr><td rowspan="2"><b>ST 18-09</b></td>
      <td>Bajada en versales</td><td class="n">«DOUBLETREE.» · 340</td>
      <td class="n ok">«DOUBLETREE» · 335</td></tr>
  <tr><td>Cuadro del escenario</td><td class="n">pareja 368 px · 26 %</td>
      <td class="n ok">zoom 1,45× → 534 px · 38 %</td></tr>
  <tr><td rowspan="4"><b>Post 23-09</b></td>
      <td>Foto de fondo</td><td class="n">HDT_36 · lobby</td>
      <td class="n ok">HDT_68 · suite (fx 0,80)</td></tr>
  <tr><td>Contraste del titular</td><td class="n">6,52 / 4,96 / 4,48:1</td>
      <td class="n">3,36 / 3,52 / 4,05:1</td></tr>
  <tr><td>Logotipo DT</td><td class="n ojo">2,42:1 (desviación aceptada)</td>
      <td class="n ok">4,32:1</td></tr>
  <tr><td>Logotipo Hilton Honors</td><td class="n">6,70:1</td><td class="n ok">8,60:1</td></tr>
  <tr><td colspan="2"><b>Todo lo demás</b></td>
      <td colspan="2" class="ok">sin tocar — titular, recuadro, íconos, rótulos, regla del
      pie, llamado, logotipos y sus posiciones</td></tr>
</table>
</div>

<h2>La compuerta</h2>
<p class="nota"><code>scripts/dt-qa.py</code> sobre las dos entregas.</p>
<div class="envoltorio">
<table class="tabla">
  <tr><th>Chequeo</th><th>ST 18-09</th><th>Post 23-09</th></tr>
  <tr><td>Máster</td><td class="n ok">2250×4000 ✓</td><td class="n ok">2250×2813 ✓</td></tr>
  <tr><td>Sustitución de fuente</td>
      <td class="ok">Stag Medium/Light Italic, r = 0,92 y 0,98 ✓</td>
      <td class="ok">Stag Medium/Light/Regular, IoU 0,71–0,92 ✓</td></tr>
  <tr><td>Contraste de las tintas</td>
      <td class="ok">titular 8,4 y 11,3:1 · bajada 5,7–8,1:1 ✓</td>
      <td class="ok">titular 3,4–4,1:1 (vara 3,0) · rótulos 6,9–9,4:1 · Honors 8,6:1 ✓</td></tr>
  <tr><td>Logotipo DT</td>
      <td class="ok">silueta 0,603 · 12,29:1 ✓</td>
      <td class="ojo">silueta 0,631 · 4,32:1 — bajo 4,5, <b>desviación declarada</b>:
      blanco y sin sombra ni halo, decisión tuya de la ronda 3. Subió desde 2,42:1</td></tr>
  <tr><td>Zona segura</td><td class="ok">y&gt;1580 limpia ✓</td>
      <td class="n">no aplica (feed orgánico)</td></tr>
  <tr><td>Veredicto</td><td class="n ok">✅ limpia</td><td class="n ok">✅ limpia</td></tr>
</table>
</div>

<div class="aviso">
  <h3>La tercera pieza de la ronda no está acá</h3>
  <p>La <b>ST animada del 21-09</b> (Escapada Romántica) también está <code>EN
  CAMBIOS</code> y tiene los suyos: sacar dos fotos, «Habitación para dos / Botella de
  espumante», que la foto del café caiga sobre el desayuno buffet y transiciones sin
  rebote y más lentas. <b>La haces tú</b>, según lo que dijiste el 16-09.</p>
</div>

<p class="pie">Generado por <code>scripts/dt-ronda7-revision.py</code>. Las imágenes van
embebidas: el archivo se puede mandar tal cual.</p>

</div>
</body>
</html>
"""


def main() -> int:
    faltan = [r for r in (ST_ANTES, ST_DESPUES, FT_ANTES, FT_DESPUES) if not r.exists()]
    if faltan:
        for r in faltan:
            print(f"⛔ falta {r}")
        return 1

    h = (HTML
         .replace("__CSS__", CSS)
         .replace("__ST_ANTES__", entera(ST_ANTES))
         .replace("__ST_DESPUES__", entera(ST_DESPUES))
         .replace("__ST_ANIM_ANTES__", recorte(ST_ANTES, CAJA_ANIMADORES, E_ST))
         .replace("__ST_ANIM_DESPUES__", recorte(ST_DESPUES, CAJA_ANIMADORES, E_ST))
         .replace("__ST_PUNTO_ANTES__", recorte(ST_ANTES, CAJA_PUNTO, E_ST, 900))
         .replace("__ST_PUNTO_DESPUES__", recorte(ST_DESPUES, CAJA_PUNTO, E_ST, 900))
         .replace("__FT_ANTES__", entera(FT_ANTES))
         .replace("__FT_DESPUES__", entera(FT_DESPUES))
         .replace("__P_SUITE__", entera(RAIZ / "public/assets/hilton/dt/ft-honors-habitacion.jpg", 360))
         .replace("__P_ESTAR68__", entera(PRUEBAS / "ft-honors-estar68.jpg", 360))
         .replace("__P_KING__", entera(PRUEBAS / "ft-honors-king.jpg", 360))
         .replace("__P_BIENV__", entera(PRUEBAS / "ft-honors-bienvenida.jpg", 360)))

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(h, encoding="utf-8")
    print(f"→ {DESTINO.relative_to(RAIZ)}  ({DESTINO.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

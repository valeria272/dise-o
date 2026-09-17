#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la página de revisión de la HISTORIA DE PRUEBA de DT (17-09-2026).

⚠️ NO es una pieza de grilla. Es el banco de pruebas que pidió Eli para ver si
su edición de Premiere se puede mejorar desde código.

Regla del estudio (`antes-y-despues-en-html`): **Eli aprueba mirando y
comparado.** Acá el antes y el después son VIDEO, así que la página los pone
lado a lado reproduciéndose en bucle, más una tira de fotogramas para comparar
momento a momento sin tener que pausar.

Los dos .mp4 quedan como archivos hermanos de la página (embeberlos en base64
daría un HTML de ~12 MB). La carpeta viaja completa.

Uso:
    python scripts/dt-st-prueba-revision.py
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
SALIDA = RAIZ / "out/hilton/dt/prueba-st"
DESTINO = SALIDA / "ST PRUEBA — antes y despues.html"
CSS = (RAIZ / "scripts/_revision.css").read_text(encoding="utf-8")


def uri(ruta: Path, ancho: int = 1400, calidad: int = 84) -> str:
    im = Image.open(ruta).convert("RGB")
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


TIRA = uri(SALIDA / "tira-comparacion.png", ancho=1800)

# ───────────────────────────────────────────────────────────────────────────

PROBLEMAS = [
    ("1", "El corte de los 3,00 s no dice nada",
     "Ningún texto cambia ahí. El titular y «Habitación para dos» siguen hasta "
     "5,24 y cruzan por encima de DOS fotos, así que el corte del bar entra sin "
     "anunciar ni cerrar nada.",
     "El corte pasa a llevar un relevo de texto: sale «Habitación para dos» y "
     "entra «+Botella de espumante.» justo cuando aparece el bar."),
    ("2", "Los incluidos caen sobre la foto equivocada",
     "«+Botella de espumante.» va de 0,52 a 3,00 — o sea sobre la CAMA — y la "
     "foto del BAR, que es justo la del espumante, se queda sin texto propio.",
     "Cada incluido cae sobre la foto que lo muestra: cama → habitación, "
     "bar → espumante, desayuno → desayuno. El orden de fotos ya contaba bien "
     "la historia; era la edición la que no lo seguía."),
    ("3", "Cero movimiento",
     "0 keyframes en todo el proyecto. Las tres fotos están clavadas y lo único "
     "que se mueve en 9,6 s es la tipografía.",
     "Las tres llevan cámara lenta con frenada, con direcciones alternadas para "
     "que dos planos seguidos no se lean iguales."),
    ("4", "Cuatro transiciones y tres son la misma",
     "Máquina de escribir ×3 —el preset más reconocible de Premiere— y es "
     "lineal: con 1,00 s fijo escribe «Habitación para dos» (19 caracteres) y "
     "«Incluye desayuno buffet para dos.» (33) a cadencias muy distintas.",
     "Sale el preset. Entra un solo recurso para toda la pieza —fundido + "
     "subida— y lo que distingue a cada texto es el RETARDO, no un efecto "
     "distinto."),
    ("5", "Todo pasa en el primer segundo y medio",
     "Tres animaciones encimadas entre 0,00 y 1,52 s, y después nada hasta 5,24.",
     "Escalonado en el orden en que se lee una oferta: titular (0,20 s) → "
     "incluido (0,67) → precio (1,27) → CTA (1,93)."),
    ("6", "Ningún texto tiene salida",
     "Los seis cortan seco al terminar su clip. Entran con gracia y desaparecen "
     "de golpe.",
     "Cada texto entra y SALE. La salida es más corta que la entrada (12 "
     "fotogramas contra 24), que es como se siente natural."),
    ("7", "El segundo titular aparece sin animación",
     "El clip de «Escapada Romántica» no tiene transición: hace <i>pop</i> en el "
     "fotograma de 5,24.",
     "Entra con el mismo recurso que el primero, seis fotogramas después de que "
     "la foto del desayuno termine de resolver."),
]

CONTRASTE = [
    ("cama",     "5,56", "5,23", "5,72", "5,12"),
    ("bar",      "6,33", "8,30", "8,50", "4,15"),
    ("desayuno", "8,10", "5,05", "5,63", "4,25"),
]

filas_problemas = "\n".join(
    f"""<tr>
      <td class="n"><b>{n}</b></td>
      <td><b>{titulo}</b><div class="nota" style="margin:4px 0 0">{antes}</div></td>
      <td>{despues}</td>
    </tr>"""
    for n, titulo, antes, despues in PROBLEMAS
)

filas_contraste = "\n".join(
    f"""<tr><td>{f}</td><td class="n ok">{a}</td><td class="n ok">{b}</td>
        <td class="n ok">{c}</td><td class="n mal">{d}</td></tr>"""
    for f, a, b, c, d in CONTRASTE
)

HTML = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ST de prueba DT — antes y después</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@400;500;700&family=Archivo:wght@400;500;600&display=swap">
<style>
{CSS}
  .videos {{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px;
            align-items:start}}
  .videos figure video {{display:block;width:100%;height:auto;background:#000}}
  .etiqueta {{display:inline-block;font-size:11.5px;font-weight:600;letter-spacing:.12em;
              text-transform:uppercase;padding:3px 9px;border-radius:999px;margin-right:8px}}
  .et-antes {{background:rgba(179,38,30,.12);color:var(--rojo)}}
  .et-despues {{background:rgba(111,148,24,.14);color:var(--verde)}}
  .tira {{width:100%;height:auto;display:block;border-radius:12px}}
</style>
</head>
<body>
<div class="caja">

<header>
  <div class="sello">DoubleTree by Hilton · banco de pruebas · 17-09-2026</div>
  <h1>La historia de prueba, antes y después</h1>
  <p class="sub">Mismas fotos, mismos textos, misma tipografía, mismo velo y misma
  diagramación. <b>Lo único que cambia es la edición</b> — los cortes, la cámara,
  los tiempos y las transiciones de texto. Se dejó así a propósito para que la
  comparación aísle exactamente lo que preguntaste.</p>
</header>

<div class="aviso">
  <h3>Esto no es una pieza de grilla</h3>
  <p>Es la <code>ST PRUEBA CLOUDE.prproj</code> de la carpeta de pruebas, que a su
  vez es copia de la ST n°2 de la S2. No se subió a ninguna parte y no reemplaza
  nada entregado. <b>Los textos van literales</b>: no se corrigió el punto final
  de «+Botella de espumante.» ni se tocó ningún copy (§G — en DT sólo se diseña).</p>
</div>

<h2>Las dos, corriendo</h2>
<p class="nota">Las dos duran <b>9,64 s</b>, que es la duración exacta de tu
proyecto. Se reproducen en bucle y sin sonido.</p>
<div class="videos">
  <figure>
    <video src="ANTES.mp4" autoplay loop muted playsinline></video>
    <figcaption><span class="etiqueta et-antes">Antes</span>
    Tu edición, reconstruida fotograma a fotograma desde el <code>.prproj</code>:
    los tres cortes secos, las cuatro transiciones y los tiempos exactos de cada
    gráfico.</figcaption>
  </figure>
  <figure>
    <video src="DESPUES.mp4" autoplay loop muted playsinline></video>
    <figcaption><span class="etiqueta et-despues">Después</span>
    Misma duración, mismos elementos. Cortes sincronizados con el texto, cámara
    en las tres fotos, disolvencias de 10 fotogramas y entradas escalonadas con
    salida.</figcaption>
  </figure>
</div>

<h2>Momento a momento</h2>
<p class="nota">Arriba el antes, abajo el después. Mira el tercer y cuarto
fotograma: en el antes el espumante está sobre la cama y el bar se queda mudo.</p>
<div class="envoltorio">
  <img class="tira" src="{TIRA}" alt="Tira comparativa de fotogramas">
</div>

<h2>Lo que estaba pasando, y qué se hizo</h2>
<div class="envoltorio">
<table class="tabla">
  <thead><tr><th></th><th>En tu edición</th><th>En la nueva</th></tr></thead>
  <tbody>
{filas_problemas}
  </tbody>
</table>
</div>

<div class="aviso">
  <h3>Y una octava, que es de exportación y no de edición</h3>
  <p><code>image (26).png</code> en la pista V7 es la <b>guía de zona segura de
  Reels</b> —la de los rectángulos rosado, azul y verde—, es opaca y está por
  encima de casi todo. Va apagada al exportar; si se queda encendida se come la
  historia entera.</p>
</div>

<h2>El velo, medido</h2>
<p class="nota">Luminancia por tercios de la columna del texto, manda el tercio
más claro. <b>Sin velo la tinta blanca no da:</b> el plumón de la foto de la cama
deja el bloque bajo en 1,59–1,69:1. Se aplicó la rampa <b>ya aprobada</b> de la
ST del Día del Turismo (0 arriba → 0,58 al pie, cóncava). Se probaron rampas más
cargadas —0,73 y 0,80— y se descartaron: la aprobada ya pasa, y un velo que tapa
la foto contradice el encargo.</p>
<div class="envoltorio">
<table class="tabla">
  <thead><tr><th>Foto</th><th>Titular <small>(vara 3:1)</small></th>
  <th>Incluido <small>(4,5:1)</small></th><th>Precio <small>(4,5:1)</small></th>
  <th>Logotipo <small>(6,7–9,3)</small></th></tr></thead>
  <tbody>
{filas_contraste}
  </tbody>
</table>
</div>

<h2>Dos cosas que decides tú</h2>

<div class="aviso">
  <h3>1 · El logotipo queda bajo la vara, y arreglarlo cambiaría una regla tuya</h3>
  <p>Cae en <b>4,15–5,12:1</b> sobre las tres fotos, contra el 6,7–9,3 que pide
  §B.4. La rampa de DT nace en <b>0 arriba</b> y ahí el logotipo no recibe ayuda
  ninguna. Para llegar a 6,7 haría falta α ≈ <b>0,36–0,46</b> en esa banda, o sea
  un velo superior de verdad — y eso es exactamente lo que marcaste como
  «forzado» en la ronda 4 del Día del Turismo. En azul es peor (3,13–3,86:1).</p>
  <p>Queda medido y sin tocar: cambiar la regla del velo no lo decide una pieza
  de prueba.</p>
</div>

<div class="aviso">
  <h3>2 · Stag no tiene el signo <code>+</code></h3>
  <p>Verificado glifo a glifo con <code>fontTools</code> sobre los nueve cortes
  que tenemos: comparten el mismo subconjunto de 354 glifos y a todos les falta
  <code>U+002B</code>, además del <code>$ % @ € º ª # *</code> que ya estaba
  documentado. O sea que <b>«+Botella de espumante.» en Stag-Regular no puede
  dibujar su primer carácter</b> — al componerlo, el «+» desaparece.</p>
  <p>En Premiere no se nota porque el sistema mete una fuente de reemplazo para
  ese carácter, pero entonces ese «+» <b>no es Stag</b>. Acá se compuso en
  <b>Trade Gothic</b>, que sí lo trae: la misma salida que ya usa la marca para
  el <code>$</code> del precio y para <code>¡</code>/<code>¿</code>. Vale la pena
  revisar si aparece en otras piezas.</p>
</div>

<h2>Cómo se rehace</h2>
<pre><code>npx remotion render src/DtEntry.tsx DT-Prueba-Antes   out/hilton/dt/prueba-st/ANTES.mp4   --codec=h264
npx remotion render src/DtEntry.tsx DT-Prueba-Despues out/hilton/dt/prueba-st/DESPUES.mp4 --codec=h264
python scripts/dt-st-prueba-revision.py</code></pre>
<p class="nota">La composición vive en
<code>src/compositions/hilton/DtStPrueba.tsx</code> y está registrada en
<code>src/DtEntry.tsx</code>, carpeta <b>DT-Prueba-ST</b>. Hay una tercera
composición, <code>DT-Prueba-Guia</code>, que dibuja encima las zonas seguras y
el margen de 88 px.</p>

<p class="pie">DoubleTree by Hilton Santiago–Vitacura · banco de pruebas del
17-09-2026 · no es material de grilla</p>

</div>
</body>
</html>
"""

DESTINO.write_text(HTML, encoding="utf-8")
print(f"→ {DESTINO}  ({len(HTML) / 1024:.0f} KB)")

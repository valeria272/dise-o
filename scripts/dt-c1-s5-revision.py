#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — la página que mira Eli.

    python scripts/dt-c1-s5-revision.py

⭐ Por qué existe (memoria `antes-y-despues-en-html`): Eli aprueba MIRANDO y
comparado. Cada ronda se entrega como una página con la pieza al lado de su
referencia, al tamaño de publicación, y con las decisiones escritas para que
pueda decir que sí o que no a cada una por separado.

Ronda 1: todavía no hay «antes», así que la comparación es contra las dos
referencias que ella misma dejó en el Drive.

Ronda 2 (17-09): seis correcciones de Eli, cada una con lo que se midió para
resolverla. Ver el bloque «Ronda 2» de la página.

Ronda 3 (21-09): un solo ajuste, en la portada — el trazo tapaba la tilde de
«día» y el bloque estaba despegado del titular. Va con ANTES / DESPUÉS al
tamaño real y con el detalle a 2×, porque el arreglo es de píxeles.

Ronda 4 (21-09, tarde): contenido escribió el slide del GYM y el carrusel pasa a
SEIS láminas. Acá no hay antes/después que mostrar —la lámina es nueva— pero sí
hay que enseñar la RENUMERACIÓN, porque el cierre cambia de n°5 a n°6 y el
portal levanta por nombre.
"""
import shutil
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
BASE = RAIZ / "out/hilton/dt/c1-s5"
REFS = RAIZ / "raw/hilton/dt/s5-sept/refs"

LAMINAS = [
    ("C1 S5 DT n°1.mp4", "PORTADA", "—",
     "«Tu día» en el trazo · «en DoubleTree» · «by Hilton Santiago–Vitacura» · DESLIZA",
     "<code>CONTENIDO HOTEL 2026 / Exterior hotel / IMG_1640</code> · 11,7 s a 1,0×"),
    ("C1 S5 DT n°2.mp4", "SLIDE 1", "8:30 · DESAYUNO ANTES DE LA REUNIÓN",
     "Empieza el día / con la energía correcta.",
     "<code>DESAYUNO BUFFET QB / IMG_5700</code> · 3,64 s a 0,72×"),
    ("C1 S5 DT n°3.mp4", "SLIDE 2", "9:30 · REUNIÓN EN SALÓN",
     "Un espacio a la altura / de tus reuniones.",
     "<code>SALÓNES / IMG_5785</code> · 2,37 s a 0,47×"),
    ("C1 S5 DT n°4.mp4", "SLIDE 3", "12:00 · TIEMPO PARA TI",
     "Entre reunión y reunión, / un momento para respirar.",
     "<code>COWORK / IMG_5736</code> · 5,97 s a 1,0×"),
    ("C1 S5 DT n°5.mp4", "SLIDE 4 · NUEVA", "16:00 · SIGUE CON TU RUTINA DIARIA",
     "Un espacio para mantenerte / en movimiento.",
     "<code>CONTENIDO HOTEL 2026 / GYM / IMG_1700</code> · 4,99 s a 1,0×"),
    ("C1 S5 DT n°6.mp4", "SLIDE 5 · era la n°5", "sin hora · CIERRE EN LA HABITACIÓN",
     "El día termina como debe: / con comodidad.",
     "<code>HABITACIONES / IMG_5741</code> · 6,37 s a 1,0×"),
]

PENDIENTES = [
    ("⏸ Falta la <b>hora del cierre</b>",
     "El comentario da tres horas (8:30 desayuno, 9:30 salones, 12 cowork) y la "
     "cuarta es la del gym. Para «cierre en la habitación» no hay hora, y "
     "ponerle una sería escribir contenido. La lámina va sin sello de hora; es "
     "un dato y entra en un render."),
    ("⚠️ Los <b>cinco</b> textos <b>terminan en punto</b>",
     "La regla de DT dice que los títulos no llevan punto, pero los textos salen "
     "literales de la grilla y corregirlos sería editarle el copy al cliente. "
     "Van con punto. Si el cliente los quiere sin punto, lo pide."),
    ("⚠️ «12» se compuso <b>12:00</b>",
     "Para que la columna de horas sea una sola serie junto a 8:30 y 9:30. Es "
     "formateo de una cifra, no redacción — pero queda dicho."),
    ("⚠️ Dos personas al fondo del <b>salón</b>",
     "En <code>IMG_5785</code> hay dos personas de pie al fondo. A 1080 de ancho "
     "miden unos 20 px y no se les distingue el rostro. Si prefieres el salón "
     "vacío, <code>IMG_5783</code> y <code>IMG_5784</code> son de la misma sala."),
]

DECISIONES = [
    ("La letra manuscrita de la referencia va en <b>Stag Itálica</b>",
     "Las dos referencias resuelven su acento con una tipografía manuscrita. En "
     "DT la tipografía la manda el manual —<b>Stag + Trade, y nada más</b>— y "
     "meter una tercera familia es abrirle una fuente a la marca, que no lo "
     "decide una pieza. El <b>gesto</b> de la referencia sí entra: el trazo que "
     "rodea la palabra está dibujado y se dibuja solo en pantalla. Si la quieres "
     "manuscrita de verdad, eso lo apruebas tú como marca."),
    ("Las seis láminas firman con la <b>versalita</b> al pie",
     "Y ninguna lleva el logotipo sobrepuesto. §B del manual dice que en feed el "
     "logotipo por defecto no va —«ensucia el feed»— y que sólo aparece en "
     "programas del hotel y piezas importantes; un carrusel de experiencia no es "
     "ninguno de los dos. Además el clip de la portada trae el logotipo grabado "
     "en el cristal de la entrada, así que la marca ya está en la fotografía. "
     "<b>Si prefieres el lockup en la portada, se pone y listo.</b>"),
    ("El clip del salón se toma a <b>0,47×</b>, que es el tope",
     "Dura 2,37 s y la lámina 5. Más lento que eso deja de leerse como movimiento "
     "de cámara y se lee como cámara lenta."),
    ("El <b>sello de hora</b> es el recurso que pidió el comentario de diseño",
     "La cifra en Trade Gothic (en DT las cifras y las versales son de Trade, "
     "Stag ni siquiera trae el <code>$</code>), el rótulo del propio brief en "
     "versalitas, y entre los dos un guion blanco."),
    ("Cada frase va a <b>dos pesos y un mismo cuerpo</b>",
     "Arriba Stag Medium, abajo Stag Light. Es el recurso de DT y no cambia el "
     "texto: sólo decide dónde parte la línea."),
    ("<b>5,0 segundos</b> cada una, y sin sonido",
     "Bajo el tope de 6 s que pusiste. Los clips cortos se bajan de velocidad en "
     "vez de repetirse: el origen es de 60 fps y la salida de 30, así que cada "
     "fotograma sigue siendo uno capturado — no hay cámara lenta falsa."),
]

QA = """CONTRASTE — cada tinta contra su fondo real, en el peor fotograma
  Portada      «Tu día» 3,35:1 · titular 4,05:1 · bajada 9,15:1 · DESLIZA 9,48:1 · firma 4,69:1
  Desayuno     sello 5,21:1 · titular 4,80:1 · firma 4,57:1
  Salón        sello 5,72:1 · titular 3,75:1 · firma 6,99:1
  Lobby        sello 6,50:1 · titular 3,98:1 · firma 6,76:1
  GYM          sello 5,26:1 · titular 4,39:1 · firma 4,54:1   ← la nueva
  Habitación   sello 5,08:1 · titular 4,32:1 · firma 4,74:1
  Las varas: 3:1 para el titular (es texto grande) y 4,5:1 para el texto chico.

  ⚠️ La firma del gym pasa por poco (4,54 contra 4,5). Midiendo el fondo de
     verdad —enmascarando la letra— da 5,5:1, o sea que el margen real es mayor;
     el número de arriba es el del chequeo, que mide a la baja. Ver más abajo.

CANTO IZQUIERDO — las 18 franjas de texto, contra el margen de DT (88 px)
  las 18 en x = 88 ✅

DURACIÓN Y LIENZO — las 6 láminas
  2160 × 2700 · 5,06 s cada una · bajo el tope de 6 s

HOLGURA DEL TRAZO — cada glifo de «Tu día» contra el círculo (ronda 3)
  «T» +20,2  «u» +31,3  «d» +27,1  «í» +20,8  «a» +16,3 px
  en la ronda 2 la «í» iba en −1,9 y la «a» en −2,0 — o sea el trazo las pisaba"""


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)
    (BASE / "refs").mkdir(exist_ok=True)
    for f in REFS.glob("*.jpg"):
        shutil.copy2(f, BASE / "refs" / f.name)

    laminas = "\n".join(
        f"""  <figure class="lam">
    <video src="entrega/{a}" autoplay loop muted playsinline></video>
    <figcaption>
      <b>{b}</b> <span class="n">{a}</span>
      <div class="sello">{c}</div>
      <div class="txt">{d}</div>
      <div class="src">{e}</div>
    </figcaption>
  </figure>"""
        for a, b, c, d, e in LAMINAS)

    bloque = lambda items, clase: "\n".join(
        f'    <li class="{clase}"><b>{t}</b><p>{c}</p></li>' for t, c in items)

    html = f"""<!doctype html>
<html lang="es"><meta charset="utf-8">
<title>DT · Carrusel S5 · 28-09 — ronda 4</title>
<style>
  :root {{ --azul:#09194E; --verde:#A3CD39; --papel:#F4F5F7; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--papel); color:#16202F;
    font:15px/1.55 -apple-system,"Segoe UI",Roboto,sans-serif; }}
  header {{ background:var(--azul); color:#fff; padding:34px 40px 30px; }}
  header h1 {{ margin:0 0 6px; font-size:27px; font-weight:650; letter-spacing:-.01em; }}
  header p {{ margin:0; opacity:.78; font-size:14px; }}
  main {{ padding:34px 40px 70px; max-width:1680px; margin:0 auto; }}
  h2 {{ font-size:13px; letter-spacing:.16em; text-transform:uppercase;
    color:#5A6675; margin:44px 0 16px; font-weight:650; }}
  h2:first-of-type {{ margin-top:8px; }}
  .fila {{ display:flex; gap:20px; overflow-x:auto; padding-bottom:10px; }}
  .lam {{ margin:0; flex:0 0 306px; }}
  .lam video, .lam img {{ width:306px; height:382px; object-fit:cover;
    border-radius:9px; background:#0b1220; display:block;
    box-shadow:0 5px 22px rgba(9,25,78,.16); }}
  figcaption {{ padding:11px 2px 0; font-size:12.5px; }}
  figcaption b {{ font-size:13px; }}
  .n {{ color:#8A94A3; font-size:11px; }}
  .sello {{ color:var(--azul); font-weight:600; margin-top:5px; }}
  .txt {{ color:#38414F; margin-top:3px; }}
  .src {{ color:#8A94A3; margin-top:5px; font-size:11.5px; }}
  .src code, li code {{ background:#E3E7EC; padding:1px 5px; border-radius:4px;
    font-size:11px; }}
  ul {{ list-style:none; padding:0; margin:0; display:grid;
    grid-template-columns:repeat(auto-fill,minmax(400px,1fr)); gap:14px; }}
  li {{ background:#fff; border-radius:9px; padding:15px 17px;
    border-left:3px solid var(--verde); }}
  li.pend {{ border-left-color:#E0A21A; }}
  li.r2 {{ border-left-color:var(--azul); }}
  li p {{ margin:5px 0 0; color:#4A5462; font-size:13.5px; }}
  pre {{ background:#fff; border-radius:9px; padding:16px 18px; overflow-x:auto;
    font-size:12.5px; color:#38414F; border-left:3px solid var(--verde); }}
  .refs {{ display:flex; gap:20px; }}
  .refs figure {{ margin:0; }}
  .refs img {{ width:262px; height:auto; border-radius:9px;
    box-shadow:0 5px 22px rgba(9,25,78,.16); }}
  .refs figcaption {{ color:#5A6675; }}
  .par {{ display:flex; gap:20px; margin-bottom:18px; flex-wrap:wrap; }}
  .par figure {{ margin:0; }}
  .par img {{ width:430px; max-width:100%; height:auto; border-radius:9px;
    box-shadow:0 5px 22px rgba(9,25,78,.16); display:block; }}
  .par figcaption {{ color:#5A6675; padding-top:8px; font-size:12.5px; }}
</style>
<header>
  <h1>DoubleTree · Carrusel de videos «Tu día en DoubleTree»</h1>
  <p>FEED columna N · 28 de septiembre 12:00 · <b>6 láminas</b> de 5,0 s ·
     <b>2160×2700</b> · <b>ronda 4: entró el slide del GYM</b> ·
     el cierre pasa de n°5 a <b>n°6</b></p>
</header>
<main>
  <h2>Las seis láminas — se reproducen solas, en bucle</h2>
  <div class="fila">
{laminas}
  </div>

  <h2>Contra las referencias que dejaste</h2>
  <div class="refs">
    <figure><img src="refs/REF-PORTADA-CARRUSEL.jpg">
      <figcaption>REF PORTADA CARRUSEL</figcaption></figure>
    <figure><img src="refs/REF-SLIDE2-Y-SIGUIENTES.jpg">
      <figcaption>SLIDE 2 Y SIGUIENTES</figcaption></figure>
  </div>

  <h2>Lo que falta y lo que hay que avisarle a contenido</h2>
  <ul>
{bloque(PENDIENTES, "pend")}
  </ul>

  <h2>Ronda 2 — lo que pediste, y qué se hizo con cada cosa</h2>
  <ul>
    <li class="r2"><b>«Usa los videos de los links»</b><p>Las cinco láminas son
      video. La portada era la única que seguía siendo foto porque la sesión de
      video no tiene exterior — pero el <b>segundo</b> enlace sí:
      <code>CONTENIDO HOTEL 2026 / Exterior hotel</code>, que tiene un solo clip
      y es la llegada al hotel.</p></li>
    <li class="r2"><b>«No uses el verde de DT»</b><p>Fuera. El trazo de la
      portada y el guion del sello pasaron a blanco. No quedó ningún acento de
      color en el carrusel.</p></li>
    <li class="r2"><b>«Espacio entre letras, muy sutil»</b><p>Los titulares iban
      en <b>−0,014em</b>, o sea apretados a propósito. Pasaron a <b>+0,014em</b>:
      a cuerpo 74-108 es cerca de 1 px por letra.</p></li>
    <li class="r2"><b>«Alinea a la izquierda bien»</b><p>Tenías razón y era
      medible: poner todo en el mismo margen no alinea, porque cada letra trae su
      propio hueco. La tinta arrancaba entre <b>88 y 92</b> según el glifo — el
      peor era el <code>12:00</code> del lobby, que empieza con el <code>1</code>
      de Trade Gothic Condensed. Ahora las <b>quince</b> franjas caen en 88
      exacto, y el QA lo verifica en cada ronda.<br>
      Y la marca roja de la derecha era otra cosa real: el <code>letter-spacing</code>
      agrega el espacio <b>también después de la última letra</b>, así que la
      firma moría en <b>x=984</b> con el margen en 992. Ahora llega a 991.</p></li>
    <li class="r2"><b>«¿Por qué se ve tan mal la calidad?»</b><p>Había <b>dos
      compresiones encadenadas</b>: los clips se reescalaban y comprimían, y
      Remotion volvía a comprimir ese archivo. Ahora los clips no se reescalan
      —salen a su tamaño nativo de recorte— y la entrega sube de 1080×1350 a
      <b>2160×2700</b>.<br>
      ⚠️ Aun así, <b>la vista previa de Drive recomprime fuerte</b>: para juzgar
      calidad hay que descargar el archivo, no verlo en el navegador.</p></li>
    <li class="r2"><b>«La portada más igual a la referencia»</b><p>Cinco cambios:
      video en vez de foto, velo y tinta blanca en vez de tinta azul, el trazo
      arriba con el titular y una <b>bajada</b> debajo, píldora clara en vez de
      azul, y <b>fuera el logotipo sobrepuesto</b> — firma con la versalita al
      pie, como la referencia y como las otras cuatro.</p></li>
  </ul>

  <h2>Ronda 3 — la portada, lo único que se tocó</h2>
  <div class="par">
    <figure><img src="r3/antes.png">
      <figcaption><b>ANTES</b> — lo entregado el 17-09</figcaption></figure>
    <figure><img src="r3/despues.png">
      <figcaption><b>DESPUÉS</b> — 21-09</figcaption></figure>
  </div>
  <div class="par">
    <figure><img src="r3/antes-tilde.png">
      <figcaption>Detalle a 2× — el trazo pisa la tilde de «día» y la «a»</figcaption></figure>
    <figure><img src="r3/despues-tilde.png">
      <figcaption>Detalle a 2× — la palabra entra entera en el trazo</figcaption></figure>
  </div>
  <ul>
    <li class="r2"><b>«Se tapa la i»</b><p>No estaba mal dibujado el trazo:
      <b>la palabra no cabía</b>. La tinta de «Tu día» llegaba a x=327,6 y el
      canto derecho del círculo estaba en x=319,1, así que «día» se salía 8,5 px
      por la derecha y la curva pasaba justo por la tilde y por la «a». Medido
      glifo por glifo, la «í» iba en <b>−1,9 px</b> y la «a» en <b>−2,0 px</b> —
      negativo es que se tocan.<br>
      Por eso no se arregló corriendo la palabra: <b>el círculo creció un 19 %</b>
      (258×130 → 306×154) y la palabra se quedó exactamente donde estaba de lado.
      Ahora el peor glifo tiene <b>16,3 px</b> de aire.</p></li>
    <li class="r2"><b>«Baja un poco y junta con el título»</b><p>El trazo baja
      <b>34 px</b> y el titular <b>no se movió</b>: el hueco entre el círculo y la
      tinta de «en DoubleTree» pasa de <b>57,6 px a 24 px</b>. Las dos líneas son
      una sola frase —«Tu día en DoubleTree»— y venían con más aire adentro de
      la frase que entre el titular y la bajada.</p></li>
    <li class="r2"><b>Y de paso apareció un contraste mal medido</b><p>El QA leía
      la banda de «Tu día» desde x=162 y la tinta arranca en <b>140,5</b>: se
      saltaba la «T», que es justo la letra que caía sobre la viga clara del
      cielo. Medida donde de verdad está, la ronda 2 daba <b>2,71:1</b> —bajo la
      vara de 3— y se entregó así. Con el bloque más abajo entra en la parte del
      velo que ya pesa y sube a <b>3,35:1</b>. La banda del QA queda corregida y
      ahora sale del contorno de los glifos, no de mirar el render.</p></li>
  </ul>

  <h2>Ronda 4 — el slide del GYM, que es lo único nuevo</h2>
  <ul>
    <li class="r2"><b>Contenido lo escribió, y va tal cual</b><p>El brief de la
      grilla pasó de cuatro slides a cinco. El nuevo es
      <b>«SLIDE 4 – SIGUE CON TU RUTINA DIARIA (GYM)»</b>, visual
      «mostrar espacio disponible del GYM (sin personas)» y texto
      <b>«Un espacio para mantenerte en movimiento.»</b> Comparado palabra por
      palabra contra la versión del 15-09: <b>ése es el único cambio del brief</b>,
      lo demás está idéntico.</p></li>
    <li class="r2"><b>⭐ Y es VIDEO, no una foto — se encontró material filmado
      del gimnasio</b><p>El 17-09 quedó anotado que no había video del gym en
      ninguna carpeta y que esta lámina tendría que salir de la foto
      <code>HDT_82</code>, siendo la única sin movimiento real. <b>Estaba mal</b>:
      <code>CONTENIDO HOTEL 2026 › GYM</code> tiene <b>7 clips</b> y se habían
      descartado por ser «de iPhone» — cuando los otros cinco clips de este mismo
      carrusel son exactamente eso. Medidos, traen la misma ficha técnica que la
      sesión del 16-09 y entran por la misma cadena. Las seis láminas son
      video.</p></li>
    <li class="r2"><b>De los 7 se eligió <code>IMG_1700</code></b><p>Y no por
      contraste: los siete pasan las varas de sobra. Lo que decide es qué queda
      <b>detrás del texto</b> y qué pide el brief («mostrar el espacio»).
      En <code>1699</code> el brazo de la torre de poleas y el rack de balones
      cruzan el titular; <code>1698</code> es un detalle precioso de mancuernas
      pero no es «el espacio»; <code>1697</code> abre sobre una pared vacía;
      <code>1694/95/96</code> son planos cortos de cintas y elípticas.
      <b><code>1700</code> recorre la sala entera</b> —bicicleta, torre, espejo,
      mancuernas— con el techo y la pared limpios justo donde vive el texto. Y
      dura <b>4,99 s</b> para una lámina de 5: es el único clip del carrusel que
      va a velocidad real, sin ralentizar.</p></li>
    <li class="r2"><b>El rótulo va «SIGUE CON TU RUTINA DIARIA», sin el «(GYM)»</b>
      <p>Misma regla que ya aplicamos en el slide 3: el brief dice «TIEMPO PARA TI
      (COWORK / LOBBY)» y el sello dice «TIEMPO PARA TI». El paréntesis del brief
      nombra el <b>espacio</b>, que es lo que muestra la imagen, no el rótulo. Los
      otros cuatro rótulos van textuales porque no traen paréntesis.
      <b>Si lo quieres con el «(GYM)» adentro, se pone.</b></p></li>
    <li class="r2"><b>El titular va a cuerpo 68 y no 74 — a propósito</b><p>Esta
      frase es la más larga del brief. A 74 no cabe en una línea y Chrome la
      parte: el bloque se iba a <b>tres</b> líneas y sus cinco hermanas son de
      dos. Bajando a 68 entra en una y el <b>bloque queda del mismo ancho</b> que
      el del lobby (892 px) y el del cierre (884 px) — el suyo mide 885. Es tu
      propio criterio de DT del 15-09: la medida manda y el cuerpo es la
      consecuencia. Al deslizar, lo que el ojo compara es el ancho del bloque, no
      el tamaño de la letra.</p></li>
    <li class="r2"><b>El gimnasio se gradó un punto más abajo</b><p>Tiene <b>el
      piso más claro del carrusel</b>, y la versalita de la firma caía a
      <b>4,35:1</b> — bajo la vara de 4,5 que se le exige al texto chico. Se
      bajaron brillo y gamma del clip, como ya hace la portada por la misma
      razón, y sube a <b>4,9:1</b>. No se tocó el velo: esa rampa vale para las
      seis láminas y cambiarla por una sería mover lo aprobado.</p></li>
    <li class="pend"><b>⚠️ Encontré algo que revisar en el control de calidad —
      y NO lo toqué</b><p>Al medir esta lámina apareció que el chequeo de
      contraste promedia la franja <b>con la letra blanca adentro</b>, así que el
      número que canta depende de lo apretada que esté la franja, no sólo del
      fondo. El sesgo es hacia el lado seguro —da falsas alarmas, no esconde
      problemas—, pero significa que <b>tres de las láminas ya entregadas tienen
      la franja corrida y no se está midiendo el fondo de sus últimas
      palabras</b>. Arreglarlo cambia los números de una pieza ya aprobada y
      puede destapar algo en lo que ya está en el Drive, así que <b>eso merece
      una pasada propia, con su antes y después. ¿La hacemos?</b></p></li>
    <li class="pend"><b>⚠️ OJO AL SUBIR AL DRIVE: hay que renumerar</b><p>El gym
      entra en el lugar 4 del brief, o sea entre el cowork y el cierre. Eso
      significa que <b>el archivo <code>n°5</code> ya no es el cierre: es el
      gym</b>, y el cierre pasa a ser <code>n°6</code>. El portal levanta por
      nombre y ordena por número, así que hay que <b>reemplazar</b> el
      <code>n°5</code> que ya está arriba y <b>subir</b> el <code>n°6</code>
      nuevo. Las cuatro primeras no se tocan.</p></li>
  </ul>

  <h2>Decisiones que siguen en pie — dime cuál cambio</h2>
  <ul>
{bloque(DECISIONES, "dec")}
  </ul>

  <h2>QA — contraste de cada tinta sobre su fondo real, medido en el peor fotograma</h2>
  <pre>{QA}</pre>
</main>
</html>"""
    salida = BASE / "revision-r4.html"
    salida.write_text(html, encoding="utf-8")
    print(f"  {salida.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

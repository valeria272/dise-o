#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escribe la página de revisión de la RONDA 4 de la S4 de PISO18.

    python scripts/p18-s4-r4-pagina.py

Las imágenes las prepara `p18-s4-r4-revision.py`. Acá sólo va el texto.

⭐ La hoja de estilo NO se duplica: se lee de la página de la ronda 3. Una ronda
se compara con la anterior, y si cambia el estilo entre rondas el antes/después
deja de ser comparable.
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
RONDA3 = RAIZ / "out/piso18/s4/revision/index.html"
DESTINO = RAIZ / "out/piso18/s4/revision-r4/index.html"


def estilo() -> str:
    s = io.open(RONDA3, encoding="utf-8").read()
    i = s.index('<link rel="preconnect"')
    j = s.index("</style>") + len("</style>")
    return s[i:j]


CUERPO = """<title>Piso18 S4 ronda 4</title>
{estilo}
<div class="wrap">

<header>
  <p class="marca">Piso18 Centro de Eventos &middot; ronda 4 &middot; 16-09-2026</p>
  <h1>Los cuatro cambios que <em>dej&oacute; el cliente</em> en la S4</h1>
  <p class="entrada">Le&iacute; la grilla viva de hoy y la compar&eacute; con la copia del 15-09 para separar
  lo nuevo de lo ya resuelto. Aparecieron <b>cuatro cambios de la S4</b>, y los cuatro est&aacute;n
  aplicados y subidos a Drive. <b>La S3 no la toqu&eacute;</b>: la hiciste t&uacute;.</p>
</header>

<section class="pieza">
  <div class="cuando"><span class="fecha">21&middot;09</span><span class="canal">Feed &middot; carrusel &middot; G3 corregida</span></div>
  <h2>Menos mes&oacute;n, el arreglo entero</h2>

  <p class="pedido"><span>Lo que pidi&oacute;</span>
  &laquo;Hag&aacute;mosle + zoom a la G3 para que no sea tan protagonista el mes&oacute;n, el resto OK!&raquo;</p>

  <p class="nota">Ten&iacute;a raz&oacute;n y se med&iacute;a: el recorte anterior entraba a <b>ancho completo</b> de la
  foto, y por eso cab&iacute;a el mes&oacute;n con patas y todo &mdash; el tablero ca&iacute;a al <b>63&nbsp;%</b> del alto.
  El nuevo cierra sobre el arreglo y el tablero baja al <b>85&nbsp;%</b>: queda de base, no de
  protagonista. <b>Y el arreglo no se toca</b>: en vez de bajar el corte de arriba, el recorte sube
  a y=0, as&iacute; que las pampas siguen enteras.</p>

  <div class="duo">
    <figure><span class="marca-et et-antes">antes &middot; ronda 3</span>
      <img src="img/a-g3.jpg" alt="G3 anterior: el mes&oacute;n con patas ocupa el tercio inferior">
      <figcaption>El mes&oacute;n entero. El tablero al 63&nbsp;% y las patas hasta el borde.</figcaption></figure>
    <figure><span class="marca-et et-ahora">ahora</span>
      <img src="img/g3.jpg" alt="G3 nueva: el arreglo domina y el mes&oacute;n queda de base">
      <figcaption>El arreglo manda. El tablero al 85&nbsp;%, las pampas intactas arriba.</figcaption></figure>
  </div>

  <p class="nota">Las otras tres no se tocaron &mdash; <b>&laquo;el resto OK!&raquo;</b>. As&iacute; queda el carrusel completo:</p>
  <div class="tira">
    <figure><img src="img/g1.jpg" alt="G1"><figcaption><b>G1</b> portada con logotipo</figcaption></figure>
    <figure><img src="img/g2.jpg" alt="G2"><figcaption><b>G2</b> sin cambios</figcaption></figure>
    <figure><img src="img/g3.jpg" alt="G3"><figcaption><b>G3</b> corregida</figcaption></figure>
    <figure><img src="img/g4.jpg" alt="G4"><figcaption><b>G4</b> sin cambios</figcaption></figure>
  </div>
</section>

<section class="pieza">
  <div class="cuando"><span class="fecha">25&middot;09</span><span class="canal">Historia &middot; encuesta &middot; opci&oacute;n B</span></div>
  <h2>La B ahora tambi&eacute;n es mesa puesta</h2>

  <p class="pedido"><span>Lo que pidi&oacute;</span>
  &laquo;En la B, pongamos una opci&oacute;n m&aacute;s de mesa para cenar, ya que las otras 2 propuestas son m&aacute;s de esa onda.&raquo;</p>

  <p class="nota">El defecto no era la foto: era que <b>no se pod&iacute;an comparar</b>. La A y la C son
  centros de mesa <b>puestos</b>, con copas, platos y mantel. La B era el arreglo del <b>mes&oacute;n
  suelto</b>, con patas y piso &mdash; otro tipo de montaje. La B nueva es mantel negro, bajoplato
  dorado, copas moradas y un centro bajo de rosas crema y palo rosa con vela.</p>

  <div class="trio">
    <figure><span class="marca-et et-antes">antes</span>
      <img src="img/a-tira-b.jpg" alt="Tira B anterior: el mes&oacute;n con patas">
      <figcaption>El mes&oacute;n con patas y piso.</figcaption></figure>
    <figure><span class="marca-et et-ahora">ahora</span>
      <img src="img/tira-b.jpg" alt="Tira B nueva: mesa puesta con mantel negro y bajoplato dorado">
      <figcaption>Mesa puesta, a la misma escala que la A y la C.</figcaption></figure>
    <figure><span class="marca-et et-ref">por qu&eacute; &eacute;sta</span>
      <img src="img/g1.jpg" alt="G1 del carrusel: la mesa larga con tulipanes">
      <figcaption>La primera candidata era la mesa de tulipanes&hellip; pero <b>es el mismo montaje de
      la G1 del carrusel</b>. Carrusel el 21 y encuesta el 25 con la misma escena es repetir el
      feed, as&iacute; que fui a un tercer montaje.</figcaption></figure>
  </div>

  <div class="duo">
    <figure><span class="marca-et et-antes">antes</span>
      <img src="img/a-st4.jpg" alt="Encuesta anterior"><figcaption>La B romp&iacute;a la serie.</figcaption></figure>
    <figure><span class="marca-et et-ahora">ahora</span>
      <img src="img/st4.jpg" alt="Encuesta nueva"><figcaption>Tres mesas puestas, tres estilos florales
      distintos: pampa seca, rosas cl&aacute;sicas y blanco con verde.</figcaption></figure>
  </div>
</section>

<section class="pieza">
  <div class="cuando"><span class="fecha">23&middot;09</span><span class="canal">Historia animada &middot; texto nuevo</span></div>
  <h2>El cliente reescribi&oacute; el texto en la grilla</h2>

  <p class="nota">Ac&aacute; no hubo comentario: <b>cambi&oacute; el brief</b>. Lo detect&eacute; comparando la grilla de
  hoy contra la copia del 15-09. El montaje, los cinco planos y el ritmo quedan igual &mdash; s&oacute;lo cambia
  lo que dice.</p>

  <dl class="ficha">
    <div><dt>Antes &mdash; texto principal</dt><dd>As&iacute; se monta un evento en Piso18, paso a paso.</dd></div>
    <div><dt>Ahora &mdash; texto principal</dt><dd>Arreglos florales que le dan vida al matrimonio de tus sue&ntilde;os en Piso18.</dd></div>
    <div><dt>Antes &mdash; bajada</dt><dd>Dejando todo listo, para que solo te preocupes de celebrar.</dd></div>
    <div><dt>Ahora &mdash; bajada</dt><dd><b>La borr&oacute;.</b> El brief pas&oacute; de dos l&iacute;neas a una.</dd></div>
  </dl>

  <div class="trio" style="margin-top:26px">
    <figure><span class="marca-et et-antes">antes</span>
      <img src="img/a-st3.jpg" alt="Titular anterior"><figcaption>&laquo;As&iacute; se monta un evento&hellip;&raquo;</figcaption></figure>
    <figure><span class="marca-et et-ahora">ahora</span>
      <img src="img/st3.jpg" alt="Titular nuevo"><figcaption>El texto nuevo, literal de la grilla.
      Entra en dos l&iacute;neas y no toca la zona segura.</figcaption></figure>
    <figure><span class="marca-et et-ahora">cierre</span>
      <img src="img/st3-cierre.jpg" alt="Cierre de la animada"><figcaption>Sin la bajada, el cierre
      queda logotipo + bot&oacute;n. El bot&oacute;n sube a y=1100 para ocupar el sitio.</figcaption></figure>
  </div>

  <div class="duo">
    <figure><span class="marca-et et-antes">antes &middot; 13,0 s</span>
      <video src="img/a-st3.mp4" controls muted playsinline></video>
      <figcaption>Ronda 3.</figcaption></figure>
    <figure><span class="marca-et et-ahora">ahora &middot; 13,0 s</span>
      <video src="img/st3.mp4" controls muted playsinline></video>
      <figcaption>Ronda 4. Mismo montaje, texto nuevo.</figcaption></figure>
  </div>

  <p class="pedido" style="margin-top:22px"><span>Lo decides t&uacute;</span>
  El comentario &laquo;Podr&iacute;a ser un texto orientado a ''Dejando todo listo, para que solo te preocupes
  de celebrar''&raquo; <b>sigue en la celda y sin tachar</b>, y es el que hab&iacute;a producido la bajada. Como
  la grilla la borr&oacute;, la quit&eacute;. Si la quieres de vuelta se repone y el bot&oacute;n baja otra vez.</p>
</section>

<section class="pieza">
  <div class="cuando"><span class="fecha">25&middot;09</span><span class="canal">Feed &middot; post &middot; pieza nueva</span></div>
  <h2>La foto que eligi&oacute; el cliente, con logotipo</h2>

  <p class="pedido"><span>Lo que pidi&oacute;</span>
  &laquo;Que sea esta foto, con logo y estamos:
  <a href="https://drive.google.com/file/d/1XIfam4-nFartLYN3yrf0iCumzQt-s6EP/view">drive.google.com/file/d/1XIfam4&hellip;</a>&raquo;</p>

  <p class="nota">Ese enlace es <code>piso_18-128.jpg</code>, de tu sesi&oacute;n del 28/AGO &mdash; ya estaba en
  el estudio, as&iacute; que no hubo que pedir nada. Es horizontal y el feed va 4:5, as&iacute; que el recorte
  abre hacia la <b>izquierda</b>, que es donde est&aacute; el sal&oacute;n: mesas vestidas, sillas y los
  ventanales. Eso adem&aacute;s responde lo que ven&iacute;a pidiendo en el mismo hilo &mdash;<b>&laquo;planos m&aacute;s amplios&hellip;
  mostrar el espacio&raquo;</b> y <b>&laquo;que sean de ambiente, sin caras directas&raquo;</b>: no hay una sola
  persona en cuadro.</p>

  <div class="duo">
    <figure><span class="marca-et et-ref">la foto que mand&oacute;</span>
      <img src="img/ref-post.jpg" alt="piso_18-128.jpg completa">
      <figcaption><code>piso_18-128.jpg</code> &middot; 5760&times;3840 &middot; sesi&oacute;n 28/AGO.</figcaption></figure>
    <figure><span class="marca-et et-ahora">ahora</span>
      <img src="img/post.jpg" alt="Post nuevo con logotipo">
      <figcaption>2250&times;2813. Logotipo 568&nbsp;px en y=218, centrado &mdash; el mismo de la G1 aprobada.</figcaption></figure>
  </div>

  <p class="nota">Y el recorte izquierdo resuelve de paso el logotipo: la banda donde va queda en
  <b>luminancia 20&ndash;35</b> &mdash;techo oscuro&mdash; contra 88 si el recorte fuera centrado, que cae sobre las
  flores claras. Blanco sobre eso no se lee.</p>
</section>

<section class="pieza">
  <div class="cuando"><span class="canal">Tres cosas que decides t&uacute;</span></div>
  <h2>Antes de darlo por cerrado</h2>

  <dl class="ficha">
    <div><dt>1 &middot; El nombre del post</dt><dd>El archivo <code>Post S4 PISO18 25-09.png</code> que ya
    estaba en Drive es el de <b>&laquo;Piso18 de noche&raquo;</b>, y la grilla lo movi&oacute; al <b>23-09</b>. El 25-09
    ahora lo ocupa este post nuevo. Para no romper ning&uacute;n enlace no renombr&eacute; nada: sub&iacute; el nuevo como
    <code>Post n&deg;2 S4 PISO18 25-09.png</code>. Si prefieres renombrar el viejo a 23-09 y dejar el
    nuevo con el nombre limpio, se hace en un minuto.</dd></div>

    <div><dt>2 &middot; La foto repetida</dt><dd><code>piso_18-128</code> es tambi&eacute;n el <b>tercer plano de
    la historia animada del 23-09</b>. El cliente eligi&oacute; esa foto con nombre y apellido, as&iacute; que la
    us&eacute;; pero quedar&iacute;an la misma escena el 23 y el 25. Si quieres, cambio el plano de la animada.</dd></div>

    <div><dt>3 &middot; La bajada de la animada</dt><dd>La quit&eacute; porque la grilla la borr&oacute;, pero el
    comentario que la ped&iacute;a sigue vivo. Tu llamado.</dd></div>
  </dl>
</section>

<section class="pieza">
  <div class="cuando"><span class="canal">Lo que no toqu&eacute;</span></div>
  <h2>Y por qu&eacute;</h2>

  <dl class="ficha">
    <div><dt>Toda la S3</dt><dd>Tuya. Las piezas de la S3 en Drive las subiste t&uacute; desde tus
    editables, y el token del estudio no puede reemplazar archivos que subiste a mano. Los dos
    cambios que dej&oacute; el cliente ah&iacute; son: <b>16-09</b> &laquo;Quitemos Sujeto a disponibilidad y OK&raquo; y
    <b>20-09</b> &laquo;Quitar ese CTA, que sea foco reacci&oacute;n&raquo;. En el feed, el reel del 17-09 tambi&eacute;n
    cambi&oacute; de texto en el brief: ahora pide &laquo;La atm&oacute;sfera indicada&raquo; en grande y &laquo;puede cambiar por
    completo tu celebraci&oacute;n&raquo; en chico.</dd></div>

    <div><dt>ST N&deg;2 S4 &middot; 22-09</dt><dd>Pas&oacute; a <b>APROBADO</b>. Sin comentarios nuevos.</dd></div>

    <div><dt>Post &laquo;Piso18 de noche&raquo;</dt><dd>Sigue en <b>EN REVISI&Oacute;N</b> y sin comentario nuevo. S&oacute;lo
    se movi&oacute; de fecha, del 25-09 al 23-09.</dd></div>

    <div><dt>Carrusel de cumplea&ntilde;os &middot; 22-09</dt><dd>Pas&oacute; de CORREGIDO a <b>APROBADO</b>.</dd></div>
  </dl>
</section>

<section class="pieza" style="border-bottom:none">
  <div class="cuando"><span class="canal">Estado</span></div>
  <h2>Las cuatro, en Drive</h2>

  <dl class="ficha">
    <div><dt>Carrusel G3</dt><dd>Reemplazada en <code>C1 S4 PISO18</code>, <b>mismo enlace</b>.</dd></div>
    <div><dt>Historia animada</dt><dd>Reemplazada en <code>STS</code>, <b>mismo enlace</b>. 1080&times;1920, 13,0 s.</dd></div>
    <div><dt>Encuesta</dt><dd>Reemplazada en <code>STS</code>, <b>mismo enlace</b>. 2250&times;4000.</dd></div>
    <div><dt>Post 25-09</dt><dd>Nuevo, en la ra&iacute;z de <code>PISO18</code>. 2250&times;2813.</dd></div>
    <div><dt>QA</dt><dd>Las 8 piezas de la S4 pasan <code>qa/motor.py --marca piso18</code>.</dd></div>
    <div><dt>Lo que no sub&iacute;</dt><dd>Las tres piezas sin cambios conservan su fecha en Drive, para que
    se vea de un vistazo qu&eacute; se toc&oacute; hoy.</dd></div>
  </dl>

  <footer>
    Carpeta: <a href="https://drive.google.com/drive/folders/1xHin8e7Iw4gdGR5x-Z_akFCokOzy4wE3">S4 HILTON SEP 2026 &rsaquo; PISO18</a><br>
    Piezas en <code>out/piso18/s4/entrega/</code> &middot; aparato en <code>src/compositions/piso18/</code> &middot;
    recortes en <code>scripts/p18-s4-r4.py</code><br>
    16 de septiembre de 2026 &middot; ronda 4
  </footer>
</section>

</div>
"""


def main() -> int:
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
        CUERPO.format(estilo=estilo()))
    print(f"  ✓ {DESTINO.relative_to(RAIZ)}  ({DESTINO.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

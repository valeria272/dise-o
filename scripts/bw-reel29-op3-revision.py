#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETWEEN · Reel n°1 S3 «La razón» (29-09) — página de revisión de la opción 3.

Los dos videos (edición 2 aprobada y edición 3 retocada) van como archivos al
lado de la página, en 720×1280, y se reproducen sincronizados. Los cuadros
fijos y los detalles salen de `out/hilton/between/reel29-op3/cuadros/`.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

C = "out/hilton/between/reel29-op3/cuadros/"
p = Pagina("between", "BETWEEN · REEL 29-09 · OPCIÓN 3",
           "La razón, sin temblor",
           "28-09-2026 · Reel n°1 S3 «La razón» · parte de la edición 2 que eligió el cliente",
           "out/hilton/between/reel29-op3/revision-op3.html",
           origen="scripts/bw-reel29-op3-revision.py")

p.pedido("Eliminar o disminuir el temblor de la cámara. Hacer que la Pauli se vea un poco "
         "más estática. También se alcanza a ver una sombra que habría que intentar "
         "eliminar (aprox en el segundo 00:2 y 00:4).", "Cliente, vía KAM", "28-09")

p.bruto("""
<section class="elige"><h2>Los dos videos, sincronizados</h2>
<p class="que">Dale a <b>Reproducir los dos</b>: parten juntos y van al mismo cuadro. Mira el cinturón y la falda: en la edición 3 quedan quietos.</p>
<div class="rejilla">
  <figure style="margin:0"><video id="v2" src="web-ed2.mp4" playsinline muted loop preload="auto" style="width:100%;border-radius:6px;display:block"></video>
  <figcaption><b>ANTES</b> — edición 2</figcaption></figure>
  <figure style="margin:0"><video id="v3" src="web-ed3.mp4" playsinline muted loop preload="auto" style="width:100%;border-radius:6px;display:block"></video>
  <figcaption><b>AHORA</b> — edición 3</figcaption></figure>
</div>
<p style="display:flex;gap:10px;flex-wrap:wrap;margin-top:16px">
  <button id="play" type="button" style="font:inherit;padding:10px 18px;border-radius:6px;border:0;background:var(--acento);color:var(--sobre-acento);cursor:pointer">Reproducir los dos</button>
  <button id="lento" type="button" style="font:inherit;padding:10px 18px;border-radius:6px;border:1px solid currentColor;background:transparent;color:inherit;cursor:pointer">Ver a mitad de velocidad</button>
</p>
<script>
(function(){
  var a=document.getElementById('v2'), b=document.getElementById('v3');
  var play=document.getElementById('play'), lento=document.getElementById('lento'), rate=1;
  function sync(){ if(Math.abs(a.currentTime-b.currentTime)>0.05) b.currentTime=a.currentTime; }
  play.addEventListener('click',function(){
    if(a.paused){ b.currentTime=a.currentTime; a.play(); b.play(); play.textContent='Pausar'; }
    else { a.pause(); b.pause(); play.textContent='Reproducir los dos'; }
  });
  lento.addEventListener('click',function(){
    rate = rate===1 ? 0.5 : 1; a.playbackRate=rate; b.playbackRate=rate;
    lento.textContent = rate===1 ? 'Ver a mitad de velocidad' : 'Volver a velocidad normal';
  });
  a.addEventListener('timeupdate',sync);
})();
</script>
</section>
""")

p.comparar((C + "ed2-120.png", "segundo 4"), (C + "ed3-120.png", "segundo 4"),
           titulo="La sombra de la palma",
           que="La figura de luz y sombra con cantos duros que cruza la palma (segundos 2 a 4) "
               "se suavizó con Magnific. <b>No desapareció entera</b>: queda más tenue. Mírala en el detalle.",
           detalle=(1150, 400, 2160, 1550), escala=1.0, lienzo=0)

p.comparar((C + "ed2-60.png", "segundo 2"), (C + "ed3-60.png", "segundo 2"),
           titulo="El texto",
           que="El texto venía pegado en la imagen, así que se borró con Magnific y se volvió a poner "
               "encima del video ya estabilizado. Es la misma letra, el mismo color y el mismo lugar que en la edición 2.",
           detalle=(500, 1400, 1700, 1800), escala=1.0, lienzo=0)

p.medido([
    ("Desplazamiento del cuerpo (cinturón y falda) en todo el video",
     "16 × 17 px", "ok", "edición 2: 84 × 45 px"),
    ("Temblor de un cuadro a otro (p95)", "1,0 px", "ok", "edición 2: 2,7 px"),
    ("Zoom que exige la estabilización", "5 %", "ok", "se pierde un 2,5 % por lado, sin cortar a la Pauli"),
    ("Texto contra el original", "Raleway SemiBold 128", "ok", "coincidencia de la tinta: 87 %"),
    ("Sombra de la palma", "más tenue", "ojo", "no se borró del todo"),
], titulo="Lo medido")

p.notas([
    "<b>La Pauli más estática:</b> no se congeló su gesto. Se ancló la imagen a su cuerpo (del cinturón para abajo): el cuerpo queda quieto y las manos siguen moviéndose, porque ese movimiento es el gesto.",
    "<b>Las 3 tomas</b> (manos, muffin, vaso) se estabilizaron por separado, así los cortes quedan donde estaban.",
    "<b>Todo lo demás es el 4K original:</b> de Magnific sólo entran la zona del texto y la piel de la mano. El muffin, el plato, el vaso y el logo de Between no pasaron por IA.",
    "<b>Máscara en la falda:</b> no la hice. Con la estabilización la falda ya no se mueve. Si lo que molesta es otra cosa de la falda, dime qué y lo veo.",
    "Audio, duración (8,3 s) y formato (2160 × 3840, 30 cps) son los mismos de la edición 2.",
], titulo="Qué se hizo y qué no")

p.escribir()

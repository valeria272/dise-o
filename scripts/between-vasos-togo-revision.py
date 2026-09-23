#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETWEEN · pagina de revision de los vasos To Go sin fondo (para Eli)."""
import json
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

SALIDA = RAIZ / "out/hilton/between/vasos-togo"
TRABAJO = SALIDA / "_trabajo"
WEB = SALIDA / "_web"


def jpg(origen, destino, ancho, fondo=None):
    im = Image.open(origen).convert("RGBA")
    if fondo:
        bg = Image.new("RGBA", im.size, fondo + (255,))
        bg.alpha_composite(im)
        im = bg
    im.thumbnail((ancho, 4000), Image.LANCZOS)
    im.convert("RGB").save(WEB / destino, quality=88)
    return destino


def main():
    WEB.mkdir(parents=True, exist_ok=True)
    prop = json.load(open(TRABAJO / "proporcion.json"))
    rel = prop["proporcion"]

    jpg(RAIZ / "raw/hilton/between/cafes-sep2026/IMG_5715.jpg", "fuente.jpg", 900)
    jpg(TRABAJO / "proporcion-verificacion.jpg", "horizonte.jpg", 900)
    for n in ("chico", "mediano", "grande"):
        jpg(SALIDA / ("BW-ToGo-vaso-%s.png" % n), "solo-%s.jpg" % n, 700, (247, 247, 245))
        jpg(SALIDA / ("BW-ToGo-vaso-%s.png" % n), "solo-%s-osc.jpg" % n, 700, (17, 21, 25))
    jpg(SALIDA / "BW-ToGo-tres-tamanos.png", "trio.jpg", 1600, (247, 247, 245))
    jpg(SALIDA / "BW-ToGo-tres-tamanos-osc.jpg".replace("-osc.jpg", ".png"),
        "trio-osc.jpg", 1600, (17, 21, 25))
    jpg(SALIDA / "BW-ToGo-tres-tamanos-invertido.png", "trio-inv.jpg", 1600, (247, 247, 245))

    tabla = "".join(
        "<tr><td>%s</td><td class=n>%.3f</td><td class=n>%.3f</td>"
        "<td class=n>%.3f</td><td class=n>%d px</td></tr>" %
        (n.capitalize(), prop["por_horizonte"][n], prop["por_tapa"][n], rel[n],
         Image.open(SALIDA / ("BW-ToGo-vaso-%s.png" % n)).height)
        for n in ("chico", "mediano", "grande"))

    html = """<!DOCTYPE html>
<html lang="es-CL"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Between · vasos To Go sin fondo</title>
<style>
 :root{--tinta:#14181c;--suave:#6b7380;--linea:#e3e5e8;--fondo:#faf9f7;--ok:#1f7a4d;--ojo:#b4541c}
 *{box-sizing:border-box}
 body{margin:0;background:var(--fondo);color:var(--tinta);
      font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif}
 .caja{max-width:1180px;margin:0 auto;padding:46px 26px 90px}
 h1{font-size:30px;margin:0 0 4px;letter-spacing:-.4px}
 h2{font-size:15px;text-transform:uppercase;letter-spacing:1.4px;color:var(--suave);
    margin:54px 0 16px;padding-bottom:9px;border-bottom:1px solid var(--linea)}
 .bajada{color:var(--suave);margin:0 0 6px}
 .rej{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
 figure{margin:0;background:#fff;border:1px solid var(--linea);border-radius:12px;
        padding:14px;text-align:center}
 figure img{max-width:100%;height:auto;display:block;margin:0 auto;border-radius:6px}
 figcaption{margin-top:10px;font-size:13px;color:var(--suave)}
 .ancho figure img{width:100%}
 table{border-collapse:collapse;width:100%;background:#fff;border:1px solid var(--linea);
       border-radius:12px;overflow:hidden}
 th,td{padding:10px 14px;text-align:left;border-bottom:1px solid var(--linea);font-size:14px}
 th{background:#f3f2ef;font-weight:600;font-size:12px;text-transform:uppercase;
    letter-spacing:.8px;color:var(--suave)}
 td.n{font-variant-numeric:tabular-nums;text-align:right}
 tr:last-child td{border-bottom:0}
 .nota{background:#fff;border:1px solid var(--linea);border-left:3px solid var(--ojo);
       border-radius:10px;padding:16px 18px;margin:14px 0}
 .nota.ok{border-left-color:var(--ok)}
 .nota b{display:block;margin-bottom:4px}
 ul{margin:8px 0 0;padding-left:20px}
 code{background:#f0efec;padding:1px 6px;border-radius:5px;font-size:13px}
</style></head><body><div class="caja">

<h1>Between · los tres vasos To Go, sin fondo</h1>
<p class="bajada">Sesion <code>cafes-sep2026 / IMG_5715</code> — la que mandaste.
Ronda 2, 21-09-2026. PNG con transparencia real, sin sombra.</p>
<div class="nota ok"><b>Esta ronda: se le sac&oacute; proceso, no se le puso</b>
Veredicto tuyo sobre la anterior: <b>&laquo;est&aacute; sobreprocesado&raquo;</b>. Ten&iacute;as
raz&oacute;n — se le hab&iacute;an ido encima aplanado de sombras, igualado del grano del
cart&oacute;n, compresi&oacute;n de brillos, suavizado y un upscaler. Cada paso arreglaba algo
real, y entre todos le sacaron el aspecto de fotograf&iacute;a.<br><br>
<b>Lo que queda, y nada m&aacute;s:</b> balance de blancos medido, croma de la tapa a la mitad
(el pl&aacute;stico negro espejaba la muralla de plantas y sal&iacute;a verdosa), lo mismo con el
aro blanco del chico, los tres igualados en tono entre s&iacute;, y un enfoque suave.
<b>El cuerpo del vaso no se toca:</b> la sombra proyectada y la veta del cart&oacute;n son de
la foto y se quedan.<br><br>
<b>Lo que S&Iacute; se mantiene de las rondas anteriores</b>, porque lo diste por bueno: los
tres a plomo, el recorte rehecho por tono, la base del chico reconstruida, la proporci&oacute;n
medida y el mediano tra&iacute;do de IMG_5719 (en IMG_5715 ese vaso tiene un pliegue).</div>

<h2>Los tres juntos</h2>
<div class="ancho"><figure><img src="_web/trio.jpg" alt="">
<figcaption>BW-ToGo-tres-tamanos.png</figcaption></figure></div>
<div class="rej" style="grid-template-columns:1fr 1fr;margin-top:18px">
 <figure><img src="_web/trio-osc.jpg" alt=""><figcaption>Sobre fondo oscuro — control de orla</figcaption></figure>
 <figure><img src="_web/trio-inv.jpg" alt=""><figcaption>De grande a chico, por si la promo va asi</figcaption></figure>
</div>

<h2>Cada uno solo</h2>
<div class="rej">
 <figure><img src="_web/solo-chico.jpg" alt=""><figcaption>Chico</figcaption></figure>
 <figure><img src="_web/solo-mediano.jpg" alt=""><figcaption>Mediano</figcaption></figure>
 <figure><img src="_web/solo-grande.jpg" alt=""><figcaption>Grande</figcaption></figure>
</div>
<div class="rej" style="margin-top:18px">
 <figure><img src="_web/solo-chico-osc.jpg" alt=""><figcaption>Chico</figcaption></figure>
 <figure><img src="_web/solo-mediano-osc.jpg" alt=""><figcaption>Mediano</figcaption></figure>
 <figure><img src="_web/solo-grande-osc.jpg" alt=""><figcaption>Grande</figcaption></figure>
</div>

<h2>De donde salen</h2>
<div class="rej" style="grid-template-columns:1fr 1fr">
 <figure><img src="_web/fuente.jpg" alt=""><figcaption>IMG_5715 — la unica toma con los tres
 completos, separados y con los tres logotipos de frente</figcaption></figure>
 <figure><img src="_web/horizonte.jpg" alt=""><figcaption>IMG_4153 — de aca sale la proporcion:
 el horizonte (rosado) corrige que cada vaso estaba a distinta distancia</figcaption></figure>
</div>

<h2>La proporcion entre los tres, medida</h2>
<p class="bajada">En la foto los tres <b>no</b> estan a la misma distancia de la camara <b>ni se
ven desde el mismo angulo</b>, asi que sus altos en pixeles no son su proporcion. Se midio con dos
reglas independientes:</p>
<ul style="margin:0 0 14px">
 <li><b>El horizonte</b>, sobre IMG_4153: los listones de esa mesa estan igualmente espaciados,
     y de ahi sale el horizonte; con el horizonte, el alto real de un objeto parado en la mesa
     es exacto.</li>
 <li><b>La tapa</b>, sobre IMG_5715: el mediano y el grande <b>comparten tapa</b>, asi que en la
     entrega sus tapas tienen que medir lo mismo. Eso fija la escala entre esos dos sin depender
     de ninguna otra foto.</li>
</ul>
<table><tr><th>Vaso</th><th>Regla 1 · horizonte</th><th>Regla 2 · tapa</th>
<th>Entregado</th><th>Alto en px</th></tr>__TABLA__</table>

<div class="nota"><b>Las dos reglas discrepan 5 % en el mediano, y eso no es un error mio</b>
Es el angulo distinto desde el que quedo fotografiado cada vaso: ninguna escala pareja puede
dejar bien el alto Y el diametro a la vez. Lo entregado es la <b>media geometrica</b> de las dos,
que reparte el error en &plusmn;2,4 % en vez de cargarselo entero a una. En la version anterior
la tapa del mediano salia 4,8 % mas chica que la del grande <b>siendo la misma tapa</b>; ahora
esa diferencia es 2,4 %.
<br><br><b style="font-weight:600">Esto se puede dejar exacto en un minuto:</b> dime de cuantas
onzas son los tres vasos (o mide uno con regla) y lo dejo clavado sin estimar nada.</div>

<h2>Lo que tienes que mirar</h2>
<div class="nota"><b>El logotipo del grande sale cortado: se lee &laquo;&#398;TWEEN&raquo;</b>
No es el recorte — el vaso grande quedo <b>girado</b> en toda la sesion, y la B se le va por
detras del canto. Lo revise en las dos sesiones que me pasaste (IMG_5714, 5715, 5716, 5717 y
IMG_4149-4157) y <b>en ninguna</b> se le ve entera. Se arregla de una sola forma: una foto
nueva del grande con el logotipo al frente. Estamparselo no, que el manual lo prohibe en
tomas frontales.</div>

<div class="nota"><b>El aro blanco del chico esta reconstruido, no recortado</b>
Contra el marmol blanco el modelo de recorte no lo ve y se lo comia. La silueta de abajo esta
<b>medida</b>: una recta a cada flanco del cono (error de 0,8 a 1,4 px) y una elipse al fondo.
El perfil de la foto dice que el aro termina en y=5100 y la elipse ajustada cayo en 5103.</div>

<h2>Que se hizo en el revelado</h2>
<ul>
 <li>Balance de blancos medido sobre el marmol, no a ojo.</li>
 <li>Sombra proyectada aplanada en luz <b>y en color</b>, dejando vivo el degrade del
     cilindro — de ahi se fue la mancha verde que la muralla de plantas dejaba en el mediano.</li>
 <li>Tapa: croma al 16 %. El plastico negro espejaba las plantas y salia verdosa.</li>
 <li>Los tres igualados al mismo kraft (L 68,3 &middot; a +15,3 &middot; b +31,4).</li>
 <li>Canto rematado 3 px hacia adentro y descontaminado, para que no quede orla verde ni blanca.</li>
 <li>Ruido del papel suavizado antes de enfocar: textura limpia, no crujiente.</li>
 <li><b>Brillos apagados con tangente hiperbolica</b>, no con umbral: lo suave queda igual y
     solo lo que se dispara se satura, asi no queda el borde que deja un recorte duro. En el
     kraft se comprimen <b>solo los excesos</b> de luz, para no aclarar el logotipo impreso.</li>
 <li>Los vasos se giraron midiendo el eje por la bisectriz de sus dos flancos (rectas con
     error de 0,4 a 1,4 px), no a ojo.</li>
</ul>

<h2>Los archivos</h2>
<table><tr><th>Archivo</th><th>Para que</th></tr>
<tr><td><code>BW-ToGo-vaso-chico.png</code></td><td>El chico solo</td></tr>
<tr><td><code>BW-ToGo-vaso-mediano.png</code></td><td>El mediano solo</td></tr>
<tr><td><code>BW-ToGo-vaso-grande.png</code></td><td>El grande solo</td></tr>
<tr><td><code>BW-ToGo-tres-tamanos.png</code></td><td>Los tres, de chico a grande</td></tr>
<tr><td><code>BW-ToGo-tres-tamanos-invertido.png</code></td><td>Los tres, de grande a chico</td></tr>
</table>
<p class="bajada" style="margin-top:12px">Los tres sueltos ya vienen <b>a escala comun</b>:
si los pones a los tres al 100 % quedan proporcionados entre si sin tocarles nada.</p>

</div></body></html>"""

    html = html.replace("__TABLA__", tabla)
    p = SALIDA / "revision.html"
    p.write_text(html, encoding="utf-8")
    print("->", p)


if __name__ == "__main__":
    main()

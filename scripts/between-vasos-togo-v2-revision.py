#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETWEEN · vasos To Go v2 (22-09) — página de revisión para Eli.

Antes (el recorte fotográfico del 21-09) · Después (los generados del Space) ·
y la foto real como referencia. Las tres cosas en la misma página y a la misma
escala, que es como se aprueba acá.
"""
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ  # noqa: E402

Image.MAX_IMAGE_PIXELS = None

SALIDA = RAIZ / "out/hilton/between/vasos-togo"
VIEJO = SALIDA / "_reemplazado-21-09"
WEB = SALIDA / "_web"
BANCO = RAIZ / "public/assets/hilton/between/togo-sep2026"

NUEVOS = ["mediano-8oz", "grande-12oz", "extra-16oz"]
VIEJOS = ["chico", "mediano", "grande"]
ROTULO = ["MEDIANO 8 oz", "GRANDE 12 oz", "EXTRA 16 oz"]


def jpg(origen, destino, ancho, fondo=None):
    im = Image.open(origen).convert("RGBA")
    if fondo:
        bg = Image.new("RGBA", im.size, fondo + (255,))
        bg.alpha_composite(im)
        im = bg
    im.thumbnail((ancho, 5000), Image.LANCZOS)
    im.convert("RGB").save(WEB / destino, quality=90)
    return destino


def fila_a_escala(rutas, destino, alto, fondo, aire=70):
    """Los tres vasos sobre una línea de base común, RESPETANDO su escala relativa."""
    ims = [Image.open(r).convert("RGBA") for r in rutas]
    altos = []
    for im in ims:
        a = np.array(im.getchannel("A")) > 8
        ys = np.nonzero(a.any(1))[0]
        altos.append(int(ys.max() - ys.min() + 1))
    k = alto / max(altos)
    ims = [im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))),
                     Image.LANCZOS) for im in ims]
    W = sum(i.width for i in ims) + aire * (len(ims) + 1)
    H = alto + aire * 2
    lienzo = Image.new("RGBA", (W, H), fondo + (255,))
    x = aire
    for im in ims:
        a = np.array(im.getchannel("A")) > 8
        base = int(np.nonzero(a.any(1))[0].max())
        lienzo.alpha_composite(im, (x, H - aire - base - 1))
        x += im.width + aire
    lienzo.convert("RGB").save(WEB / destino, quality=90)
    return destino


def alto_silueta(ruta):
    a = np.array(Image.open(ruta).convert("RGBA").getchannel("A")) > 8
    ys = np.nonzero(a.any(1))[0]
    return int(ys.max() - ys.min() + 1)


def main():
    WEB.mkdir(parents=True, exist_ok=True)
    claro, oscuro = (247, 247, 245), (17, 21, 25)

    jpg(BANCO / "togo-tres-tamanos.jpg", "real.jpg", 1100)

    fila_a_escala([SALIDA / ("BW-ToGo-%s.png" % n) for n in NUEVOS],
                  "nuevos.jpg", 900, claro)
    fila_a_escala([VIEJO / ("BW-ToGo-vaso-%s.png" % n) for n in VIEJOS],
                  "viejos.jpg", 900, claro)
    fila_a_escala([SALIDA / ("BW-ToGo-%s.png" % n) for n in NUEVOS],
                  "nuevos-osc.jpg", 900, oscuro)

    for n, r in zip(NUEVOS, ROTULO):
        jpg(SALIDA / ("BW-ToGo-%s.png" % n), "solo-%s.jpg" % n, 640, claro)
    jpg(SALIDA / "BW-ToGo-tres-tamanos.png", "trio.jpg", 1500, claro)
    jpg(SALIDA / "BW-ToGo-tres-tamanos-invertido.png", "trio-inv.jpg", 1500, claro)
    jpg(SALIDA / "BW-ToGo-trio-original.png", "trio-orig.jpg", 1500, claro)

    altos = [alto_silueta(SALIDA / ("BW-ToGo-%s.png" % n)) for n in NUEVOS]
    viejos_altos = [alto_silueta(VIEJO / ("BW-ToGo-vaso-%s.png" % n)) for n in VIEJOS]
    real = {"chico": 0.712, "mediano": 0.861, "grande": 1.000}

    filas = "".join(
        "<tr><td><b>%s</b><div class=s>antes: «%s»</div></td>"
        "<td class=n>%.3f</td><td class=n>%.3f</td><td class=n>%d px</td>"
        "<td class=n s>%d px</td></tr>"
        % (r, v, list(real.values())[i], altos[i] / max(altos), altos[i],
           viejos_altos[i])
        for i, (r, v) in enumerate(zip(ROTULO, VIEJOS)))

    html = """<!DOCTYPE html>
<html lang="es-CL"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Between · vasos To Go v2 (22-09)</title>
<style>
 :root{--tinta:#14181c;--suave:#6b7380;--linea:#e3e5e8;--fondo:#faf9f7;
       --ok:#1f7a4d;--ojo:#b4541c;--alto:#a02020}
 *{box-sizing:border-box}
 body{margin:0;background:var(--fondo);color:var(--tinta);
      font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif}
 .caja{max-width:1180px;margin:0 auto;padding:40px 24px 90px}
 h1{font-size:30px;line-height:1.15;margin:0 0 6px;letter-spacing:-.02em}
 .bajada{color:var(--suave);margin:0 0 34px;font-size:16px}
 h2{font-size:19px;margin:46px 0 4px;letter-spacing:-.01em}
 h2 .num{color:var(--suave);font-weight:400;margin-right:8px}
 p.nota{color:var(--suave);margin:2px 0 16px;max-width:75ch}
 figure{margin:0 0 12px}
 img{max-width:100%;display:block;border-radius:10px;border:1px solid var(--linea)}
 figcaption{color:var(--suave);font-size:13px;margin-top:7px}
 .par{display:grid;grid-template-columns:1fr 1fr;gap:18px}
 .tres{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
 @media(max-width:860px){.par,.tres{grid-template-columns:1fr}}
 table{border-collapse:collapse;width:100%;margin:12px 0 4px;font-size:14px}
 th,td{border-bottom:1px solid var(--linea);padding:9px 10px;text-align:left}
 th{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--suave)}
 td.n{text-align:right;font-variant-numeric:tabular-nums}
 td.s,th.s{color:var(--suave)}
 .s{font-size:12.5px;color:var(--suave)}
 .av{background:#fff6ed;border:1px solid #f0d8bd;border-left:3px solid var(--ojo);
     border-radius:8px;padding:14px 16px;margin:18px 0}
 .av b{color:var(--ojo)}
 .ok{background:#f1f8f3;border:1px solid #cfe6d8;border-left:3px solid var(--ok);
     border-radius:8px;padding:14px 16px;margin:18px 0}
 .ok b{color:var(--ok)}
 ul{margin:8px 0 0;padding-left:20px}li{margin:4px 0}
 code{background:#eef0f2;border-radius:4px;padding:1px 5px;font-size:13px}
</style></head><body><div class=caja>

<h1>Los vasos To Go, rehechos</h1>
<p class=bajada>22 de septiembre de 2026 · reemplazan la entrega de ayer ·
Space <b>BETWEEN_VASOS TOGO</b></p>

<div class=av>
<b>Lee esto antes de aprobar.</b> Estos vasos <b>no son la foto del vaso recortada</b>:
están <b>generados</b> con Google Nano Banana 2 a partir de la foto de referencia.
El logotipo lo <b>redibujó el modelo</b>, no es el vector de la marca. Se ve mejor
que el recorte —y por eso entra—, pero es una pieza de producto hecha por IA y eso
en el estudio normalmente no se hace. Queda dicho para que lo decidas mirándolo,
no para descubrirlo después.
</div>

<div class=ok>
<b>Lo que sí resuelve.</b>
<ul>
<li>El logotipo se lee <b>entero en los tres</b>. En el vaso grande real sale
    «ƎTWEEN» en las nueve tomas de las dos sesiones — era el problema abierto de ayer.</li>
<li>El canto de la tapa no tiene muescas y el recorte no deja orla del fondo.</li>
<li>Los tres vienen a plomo, sin enderezar.</li>
<li>Y el Space les puso <b>las onzas</b>, que era el otro dato pendiente.</li>
</ul>
</div>

<h2><span class=num>1</span>Antes y después, a la misma escala</h2>
<p class=nota>Arriba lo de ayer (recorte de la foto real), abajo lo de hoy. Los dos
grupos están a escala relativa correcta entre sí y sobre una línea de base común.</p>
<figure><img src="viejos.jpg" alt="antes">
<figcaption><b>ANTES</b> — 21-09, recortados de la foto. Chico · mediano · grande</figcaption></figure>
<figure><img src="nuevos.jpg" alt="despues">
<figcaption><b>DESPUÉS</b> — 22-09, del Space. MEDIANO 8 oz · GRANDE 12 oz · EXTRA 16 oz</figcaption></figure>

<h2><span class=num>2</span>La referencia: el vaso real</h2>
<p class=nota>La foto del producto. Fíjate en el vaso chico: el real es un vaso
blanco con una <b>faja de cartón</b> separada, y arriba y abajo asoma el papel
blanco. El generado lleva el kraft <b>hasta la tapa</b> — se le pidió así en el
prompt, o sea es una decisión, no un error del modelo.</p>
<figure><img src="real.jpg" alt="foto real">
<figcaption>La foto que mandó el local, sin tocar</figcaption></figure>

<h2><span class=num>3</span>La proporción, que es lo que había que arreglar</h2>
<p class=nota>Cada vaso se generó en su propio encuadre, así que venían sin escala
común —el MEDIANO llegaba a salir más alto que el GRANDE—. Se reescalaron a la
proporción <b>real</b> del envase, la que se midió ayer sobre las fotos con dos
reglas independientes. El trío nuevo, que sí se generó de una sola vez, la
confirma: da 0,705 / 0,832 / 1,000.</p>
<table>
<!--FILAS-->
<tr><th>Vaso</th><th class=n>Proporción real</th><th class=n>Entregada</th>
    <th class=n>Alto hoy</th><th class="n s">Alto ayer</th></tr>
{FILAS}
</table>
<p class=s>El alto de hoy es menor: los generados salen a 2k y los de ayer venían de
fotos de 4284×5712 pasadas por el escalador. Para el máster de 2250 alcanza —el trío
entra a ancho completo—; si un día un vaso tiene que ocupar la pieza entera, se pasa
por el escalador de precisión y queda sobre lo de ayer.</p>

<h2><span class=num>4</span>Los tres sueltos</h2>
<p class=nota>Ya están a escala común: si los pones los tres al 100 % quedan
proporcionados sin tocar nada. El kraft también se igualó — venían con 11/255 de
diferencia entre ellos, que se nota apenas los juntas.</p>
<div class=tres>
<figure><img src="solo-mediano-8oz.jpg"><figcaption>MEDIANO 8 oz</figcaption></figure>
<figure><img src="solo-grande-12oz.jpg"><figcaption>GRANDE 12 oz</figcaption></figure>
<figure><img src="solo-extra-16oz.jpg"><figcaption>EXTRA 16 oz</figcaption></figure>
</div>

<h2><span class=num>5</span>Sobre fondo oscuro</h2>
<p class=nota>La prueba del recorte: si quedó orla del fondo beige, acá se ve.</p>
<figure><img src="nuevos-osc.jpg"><figcaption>Los tres sobre fondo oscuro</figcaption></figure>

<h2><span class=num>6</span>Los tríos</h2>
<p class=nota>Los dos primeros están <b>compuestos</b> por código desde los tres
sueltos, en los dos órdenes. El tercero es el que generó el modelo <b>de una sola
vez</b>: una luz, una superficie, una toma. Cuando la pieza muestre los tres juntos
y el orden sirva, ese es el más honesto.</p>
<figure><img src="trio.jpg"><figcaption><code>BW-ToGo-tres-tamanos.png</code> — de chico a grande</figcaption></figure>
<figure><img src="trio-inv.jpg"><figcaption><code>BW-ToGo-tres-tamanos-invertido.png</code> — de grande a chico (recompuesto, <b>no espejado</b>)</figcaption></figure>
<figure><img src="trio-orig.jpg"><figcaption><code>BW-ToGo-trio-original.png</code> — el trío tal como salió del modelo</figcaption></figure>

<h2><span class=num>7</span>Por qué la versión 2 y no la 1</h2>
<p class=nota>El Space trae dos de cada vaso. Se eligió la v2 por medida, no a ojo:</p>
<table>
<tr><th>Qué se midió</th><th class=n>v1</th><th class=n>v2</th><th>Manda</th></tr>
<tr><td>Molde de la tapa entre los tres (alto/ancho) — lo que hace que se lean como familia</td>
    <td class=n>0,077</td><td class=n><b>0,014</b></td><td>v2, 5,5× más pareja</td></tr>
<tr><td>Tono del kraft dentro del trío</td>
    <td class=n>13,7/255</td><td class=n><b>8,3/255</b></td><td>v2</td></tr>
<tr><td>Ancho del logotipo sobre el del vaso, en el chico (el real da 0,702)</td>
    <td class=n>0,606</td><td class=n><b>0,635</b></td><td>v2, más cerca</td></tr>
</table>

<h2><span class=num>8</span>Lo que queda abierto</h2>
<ul>
<li><b>Los nombres cambiaron</b> y eso hay que confirmarlo: lo que ayer era
    «chico / mediano / grande» hoy es <b>MEDIANO 8 oz / GRANDE 12 oz / EXTRA 16 oz</b>.
    Si el local los llama distinto en la carta, se renombran los archivos.</li>
<li>El vaso chico generado <b>no muestra la faja de cartón</b> del real (§2).
    Si quieres que la muestre, se vuelve a generar cambiando esa línea del prompt.</li>
<li>Falta subirlos al Drive de Between si el CM los va a usar este mes.</li>
</ul>

</div></body></html>""".replace("{FILAS}", filas)

    (SALIDA / "revision.html").write_text(html, encoding="utf-8")
    print("escrito", SALIDA / "revision.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())

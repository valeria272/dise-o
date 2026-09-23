# -*- coding: utf-8 -*-
"""PISO 18 - reel de primavera: la pagina de antes y despues del ajuste de luz.

Eli aprueba mirando y comparado, asi que cada ronda se entrega como pagina con
el antes, el despues y el numero que lo respalda. Esto arma esa pagina desde
los dos archivos - no desde la memoria de lo que se hizo.

    python scripts/p18-reel-primavera-antesydespues.py
"""
import os, sys, base64, subprocess
import numpy as np
import cv2

sys.stdout.reconfigure(encoding="utf-8")
cv2.setNumThreads(4)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANTES = os.path.join(RAIZ, "raw", "piso18", "video-ajuste-luz", "original.mp4")
DESPUES = os.path.join(RAIZ, "out", "piso18", "reel-primavera", "reel-primavera-luz.mp4")
OUT = os.path.join(RAIZ, "out", "piso18", "reel-primavera", "antes-y-despues.html")
FFMPEG = (r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib"
          r"\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe")

W, H = 432, 768
PLANOS = [
    (  0, 100, "Interior con cortina",  "El negro estaba pegado al cero: las sombras no tenian nada adentro."),
    (100, 138, "Mesa montada",          "Tungsteno de la arana, +24 de dominante calida."),
    (138, 165, "Arco floral",           "Sin problema de luz; solo respira un poco mas."),
    (165, 192, "Cuadro y ventana",      "La ventana empujaba fuerte contra el interior."),
    (192, 333, "Ella habla",            "Estaba media parada en penumbra contra el fondo."),
    (333, 377, "Madera y flores",       "+25 de dominante: la madera se comia el azul de las flores."),
    (377, 433, "Flores y ella",         "Misma correccion de temperatura, mas suave."),
    (433, 648, "Ventanal a contraluz",  "EL PLANO DEL PROBLEMA: 2,3 % de la imagen quemada y ella a 113 contra un contraluz de 250."),
    (648, 718, "Cierre con el logo",    "Intacto: el negro y el logotipo no se tocan."),
]


def fotograma(src, i, w=W, h=H):
    p = subprocess.run([FFMPEG, "-v", "error", "-ss", "%.6f" % (i/30.), "-i", src,
                        "-frames:v", "1", "-vf", "scale=%d:%d:flags=area" % (w, h),
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1"], capture_output=True)
    return np.frombuffer(p.stdout, np.uint8)[:w*h*3].reshape(h, w, 3)


def jpg(rgb, q=86):
    ok, buf = cv2.imencode(".jpg", cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR),
                           [cv2.IMWRITE_JPEG_QUALITY, q])
    return "data:image/jpeg;base64," + base64.b64encode(buf.tobytes()).decode()


def stats(rgb):
    y = (.2126*rgb[..., 0] + .7152*rgb[..., 1] + .0722*rgb[..., 2]).astype(np.float32)
    return dict(p5=np.percentile(y, 5), p50=np.percentile(y, 50), p99=np.percentile(y, 99),
                quema=100*np.count_nonzero(y >= 245)/y.size,
                rb=float(rgb[..., 0].astype(np.float32).mean() - rgb[..., 2].astype(np.float32).mean()))


def main():
    for f in (ANTES, DESPUES):
        if not os.path.exists(f):
            raise SystemExit("falta %s" % f)

    filas, pares = [], []
    for a, b, nom, nota in PLANOS:
        i = (a + b)//2
        fa, fd = fotograma(ANTES, i), fotograma(DESPUES, i)
        sa, sd = stats(fa), stats(fd)
        pares.append((nom, nota, jpg(fa), jpg(fd), sa, sd, a/30., (b-1)/30.))
        filas.append((nom, sa, sd))

    # tira de recorrido: un fotograma cada medio segundo, antes arriba y despues abajo
    tira = []
    for i in range(0, 718, 30):
        tira.append((i/30., jpg(fotograma(ANTES, i, 150, 267), 80),
                     jpg(fotograma(DESPUES, i, 150, 267), 80)))

    pa, pd = os.path.getsize(ANTES)/1e6, os.path.getsize(DESPUES)/1e6
    html = PLANTILLA(pares, tira, pa, pd)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("pagina: %s  (%.1f MB)" % (OUT, os.path.getsize(OUT)/1e6))


def PLANTILLA(pares, tira, pa, pd):
    css = """
:root{--bg:#F7F5F2;--tinta:#1A1A1A;--fucsia:#D4145A;--linea:#d8d2ca;--tenue:#8a8177;
--card:#fff;--sombra:0 1px 3px rgba(0,0,0,.08);--ok:#1d7a4c}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
--bg:#121110;--tinta:#EFE6D9;--linea:#33302c;--tenue:#8f877d;--card:#1c1a18;
--sombra:0 1px 3px rgba(0,0,0,.5);--ok:#4cc38a}}
:root[data-theme="dark"]{--bg:#121110;--tinta:#EFE6D9;--linea:#33302c;--tenue:#8f877d;
--card:#1c1a18;--sombra:0 1px 3px rgba(0,0,0,.5);--ok:#4cc38a}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tinta);
font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;padding:0 16px 80px}
.wrap{max-width:1180px;margin:0 auto}
header{padding:44px 0 12px;border-bottom:2px solid var(--fucsia);margin-bottom:26px}
h1{font-size:clamp(24px,4vw,34px);margin:0 0 6px;letter-spacing:-.02em}
h1 em{color:var(--fucsia);font-style:normal}
.sub{color:var(--tenue);margin:0;font-size:14px}
h2{font-size:19px;margin:46px 0 6px;letter-spacing:-.01em}
h2::before{content:"";display:inline-block;width:10px;height:10px;background:var(--fucsia);
margin-right:9px;vertical-align:middle}
.nota{color:var(--tenue);font-size:13px;margin:0 0 18px;max-width:74ch}
.pieza{background:var(--card);border:1px solid var(--linea);border-radius:10px;
padding:18px;margin:16px 0;box-shadow:var(--sombra)}
.pieza h3{margin:0 0 3px;font-size:15px}
.pieza h3 span{color:var(--tenue);font-weight:400;font-size:12px;
font-variant-numeric:tabular-nums;margin-left:8px}
.pieza p{margin:0 0 14px;color:var(--tenue);font-size:13px}
.comp{position:relative;max-width:432px;margin:0 auto;border-radius:6px;overflow:hidden;
background:#000;touch-action:none;cursor:ew-resize;user-select:none}
.comp img{display:block;width:100%}
.comp .sup{position:absolute;inset:0;overflow:hidden;width:50%}
.comp .sup img{width:var(--anchoComp);max-width:none}
.comp .mango{position:absolute;top:0;bottom:0;width:2px;background:var(--fucsia);
left:50%;pointer-events:none}
.comp .mango::after{content:"";position:absolute;top:50%;left:50%;width:34px;height:34px;
transform:translate(-50%,-50%);border-radius:50%;background:var(--fucsia);
box-shadow:0 2px 10px rgba(0,0,0,.35)}
.comp b{position:absolute;bottom:8px;font:600 10px/1 system-ui;letter-spacing:.1em;
color:#fff;background:rgba(0,0,0,.55);padding:5px 8px;border-radius:3px}
.comp b.a{left:8px}.comp b.d{right:8px}
.cifras{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px;font-size:12px;
font-variant-numeric:tabular-nums;color:var(--tenue);justify-content:center}
.cifras i{font-style:normal;color:var(--tinta);font-weight:600}
.baja{color:var(--ok);font-weight:600}
.tira{display:flex;gap:6px;overflow-x:auto;padding-bottom:14px}
.tira .col{flex:0 0 auto;text-align:center}
.tira .t{font-size:10px;color:var(--tenue);font-variant-numeric:tabular-nums;margin-bottom:3px}
.tira img{display:block;width:96px;border-radius:3px;background:#000;box-shadow:var(--sombra)}
.tira img+img{margin-top:4px;outline:2px solid var(--fucsia);outline-offset:-2px}
table{border-collapse:collapse;width:100%;font-size:13px;margin-top:8px}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--linea)}
th{font-size:11px;letter-spacing:.06em;color:var(--tenue);text-transform:uppercase}
td.n{font-variant-numeric:tabular-nums;white-space:nowrap}
ul{padding-left:20px;max-width:76ch}li{margin:6px 0}
.pie{margin-top:52px;padding-top:18px;border-top:1px solid var(--linea);
color:var(--tenue);font-size:12px}
@media(max-width:560px){.comp{max-width:100%}}
"""
    piezas = []
    for k, (nom, nota, ja, jd, sa, sd, t0, t1) in enumerate(pares):
        piezas.append("""
<div class="pieza">
  <h3>%s<span>%.2f - %.2f s</span></h3>
  <p>%s</p>
  <div class="comp" data-c="%d">
    <img src="%s" alt="">
    <div class="sup"><img src="%s" alt=""></div>
    <div class="mango"></div>
    <b class="a">CORREGIDO</b><b class="d">ORIGINAL</b>
  </div>
  <div class="cifras">
    <span>quemado <i>%.2f %%</i> &rarr; <i class="%s">%.2f %%</i></span>
    <span>p99 <i>%.0f</i> &rarr; <i>%.0f</i></span>
    <span>ella / los medios <i>%.0f</i> &rarr; <i>%.0f</i></span>
    <span>R-B <i>%+.0f</i> &rarr; <i>%+.0f</i></span>
  </div>
</div>""" % (nom, t0, t1, nota, k, ja, jd,
             sa["quema"], "baja" if sd["quema"] <= sa["quema"] else "", sd["quema"],
             sa["p99"], sd["p99"], sa["p50"], sd["p50"], sa["rb"], sd["rb"]))

    cols = "".join("""<div class="col"><div class="t">%.0f s</div>
<img src="%s" alt=""><img src="%s" alt=""></div>""" % (t, a, d) for t, a, d in tira)

    js = """
document.querySelectorAll('.comp').forEach(function(c){
  var sup=c.querySelector('.sup'), man=c.querySelector('.mango');
  function poner(x){
    var r=c.getBoundingClientRect();
    var p=Math.max(0,Math.min(1,(x-r.left)/r.width));
    sup.style.width=(p*100)+'%';
    sup.style.setProperty('--anchoComp', r.width+'px');
    man.style.left=(p*100)+'%';
  }
  var arrastra=false;
  c.addEventListener('pointerdown',function(e){arrastra=true;c.setPointerCapture(e.pointerId);poner(e.clientX);});
  c.addEventListener('pointermove',function(e){if(arrastra)poner(e.clientX);});
  c.addEventListener('pointerup',function(){arrastra=false;});
  new ResizeObserver(function(){
    sup.style.setProperty('--anchoComp', c.getBoundingClientRect().width+'px');
  }).observe(c);
  sup.style.setProperty('--anchoComp', c.getBoundingClientRect().width+'px');
});
"""
    return """<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luz del reel</title>
<style>%s</style></head><body><div class="wrap">
<header>
<h1>Reel n&deg;1 S4 &middot; <em>Piso 18</em> &middot; ajuste de luz</h1>
<p class="sub">22-09-2026 &middot; misma edici&oacute;n, mismos textos, misma locuci&oacute;n &mdash; solo luz y calidad</p>
</header>

<p class="nota">Arrastra sobre cada imagen: a la izquierda queda el
<strong>corregido</strong> y a la derecha el <strong>original</strong>.
El encargo era que nada se viera quemado, as&iacute; que la vara del trabajo fue esa
y se comprueba sola: <strong>ning&uacute;n plano puede quedar con m&aacute;s p&iacute;xeles pegados
al blanco de los que ya ten&iacute;a</strong>. El video sali&oacute; de %.0f MB a %.0f MB, en 4K
y 10 bits, con el audio original copiado tal cual.</p>

<h2>Plano por plano</h2>
<p class="nota">Cada plano lleva su propia correcci&oacute;n: no es un filtro parejo
encima de todo. El del ventanal, que era el problema, es el que m&aacute;s se mueve;
el cierre con el logotipo no se toc&oacute; en absoluto.</p>
%s

<h2>El recorrido completo</h2>
<p class="nota">Un fotograma por segundo. Arriba el original, abajo el corregido
(marcado en fucsia).</p>
<div class="tira">%s</div>

<h2>Qu&eacute; se hizo, en una l&iacute;nea cada cosa</h2>
<ul>
<li><strong>Se abri&oacute; a quien estaba en penumbra</strong> con una campana estrecha sobre
los medios, no subiendo la exposici&oacute;n entera: por eso el cielo del ventanal sigue
donde estaba y ella deja de ser una silueta.</li>
<li><strong>Se le puso techo a las altas luces</strong> (rodilla con tope en 250). Lo que
estaba pegado al blanco baja y vuelve a tener tono; nada queda plano.</li>
<li><strong>Se corrigi&oacute; la dominante por plano</strong>: se enfri&oacute; el tungsteno de los
interiores (+25 de rojo sobre azul) y se templ&oacute; el azul del contraluz, siempre
sobre sombras y medios para no te&ntilde;ir el cielo.</li>
<li><strong>Claridad y nitidez con freno</strong>: el realce no entra en las altas. Sin ese
freno, la propia correcci&oacute;n dejaba m&aacute;s quemado del que hab&iacute;a.</li>
<li><strong>El texto no se toc&oacute;.</strong> La pastilla fucsia y la caja blanca del CTA
vuelven al original por m&aacute;scara: el fucsia de marca no se corre y el blanco del
texto sigue siendo blanco.</li>
</ul>

<p class="pie">La receta vive en <code>scripts/p18-reel-primavera-luz.py</code> con
cada decisi&oacute;n y su medici&oacute;n. Esta p&aacute;gina la arma
<code>scripts/p18-reel-primavera-antesydespues.py</code> leyendo los dos archivos.</p>
</div><script>%s</script></body></html>""" % (css, pa, pd, "".join(piezas), cols, js)


if __name__ == "__main__":
    main()

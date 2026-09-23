#!/usr/bin/env python3
"""Antes y después de la RONDA 26 de la ST del 28-09 (col T) de Between: el vaso.

Por qué existe
--------------
Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`): cada ronda
se entrega como una página con el antes, el después y la referencia, y los
números van abajo. Las imágenes van EMBEBIDAS en JPEG, así que la página es un
solo archivo y se abre sin servidor.

Acá la referencia no es una pieza: es la **sesión real de vasos To Go del
09-09**, que es lo que Eli pidió usar.

    python scripts/between-s5-revision-r26.py
"""
import base64
import io
import sys
from pathlib import Path

import numpy as np
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "out/hilton-between-s5-r26/revision-vaso.html"

ANTES_PIEZA = RAIZ / "out/hilton-between-s5/BW-S5-HumorToGo.png"
DESPUES_A = RAIZ / "out/hilton-between-s5-r26/BW-S5-HumorToGo-A.png"
DESPUES_B = RAIZ / "out/hilton-between-s5-r26/BW-S5-HumorToGo-B.png"
BASE_ANTES = RAIZ / "raw/hilton/between/s5/r4-togo-sin-costura.png"
BASE_CARTON = RAIZ / "raw/hilton/between/s5/r5-togo-carton.png"
SESION = RAIZ / "public/assets/hilton/between/togo-sep2026/togo-grande-frontal.jpg"
SESION_MANO = RAIZ / "public/assets/hilton/between/togo-sep2026/togo-en-local-qr.jpg"

# recortes 1:1 comparables — el vaso de la pieza mide 1 790 px de ancho y el de
# la sesión 1 970, así que un cuadrado de 820 px muestra la misma cantidad de
# cartón en los dos
CORTE_PIEZA = (1300, 4680, 2120, 5500)
CORTE_SESION = (900, 850, 1720, 1670)


def b64(ruta, ancho, corte=None, calidad=88):
    if not Path(ruta).exists():
        print("  falta " + str(ruta))
        return None
    im = Image.open(ruta).convert("RGB")
    if corte:
        im = im.crop(corte)
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=calidad, optimize=True)
    return base64.b64encode(b.getvalue()).decode()


def sat_y_tono(ruta, corte):
    """Saturación HSV y R/G medios de un parche de cartón liso."""
    a = np.asarray(Image.open(ruta).convert("RGB").crop(corte)).astype(np.float32)
    p = a.reshape(-1, 3).mean(axis=0)
    return (p.max() - p.min()) / p.max(), p[0] / p[1], p @ np.array([.2126, .7152, .0722])


def marco(dato, rotulo, nota, destacado=False):
    if not dato:
        return ""
    cls = "marco destacado" if destacado else "marco"
    return ('<figure class="' + cls + '">'
            '<div class="rotulo">' + rotulo + "</div>"
            '<img src="data:image/jpeg;base64,' + dato + '" alt="' + rotulo + '">'
            "<figcaption>" + nota + "</figcaption></figure>")


CSS = """
  :root{--tinta:#241a12;--papel:#f4f1ec;--taupe:#6d6455;--beige:#fff9eb;
        --linea:#ddd6ca;--rojo:#a8392b;--kraft:#b3773f;}
  *{box-sizing:border-box;}
  body{margin:0;background:var(--papel);color:var(--tinta);
       font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}
  .env{max-width:1180px;margin:0 auto;padding:48px 24px 90px;}
  h1{font-size:30px;letter-spacing:-.01em;margin:0 0 6px;text-wrap:balance;}
  .sub{color:#7a7268;margin:0 0 34px;}
  .pedido{background:#fff;border:1px solid var(--linea);border-left:4px solid var(--rojo);
          border-radius:10px;padding:18px 22px;margin:0 0 38px;}
  .pedido .quien{font-size:13px;color:#7a7268;margin-bottom:6px;}
  .pedido q{font-size:18px;font-style:italic;}
  .fila{display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start;}
  .marco{flex:1 1 300px;margin:0;background:#fff;border:1px solid var(--linea);
         border-radius:12px;overflow:hidden;}
  .marco.destacado{border-color:var(--kraft);box-shadow:0 10px 34px rgba(36,26,18,.14);}
  .rotulo{padding:11px 15px;font-size:12px;font-weight:700;letter-spacing:.09em;
          text-transform:uppercase;background:#faf8f5;border-bottom:1px solid var(--linea);}
  .destacado .rotulo{background:var(--kraft);color:var(--beige);border-bottom:0;}
  .marco img{display:block;width:100%;height:auto;}
  figcaption{padding:12px 15px;font-size:13px;color:#6b6359;border-top:1px solid var(--linea);}
  h2{font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
     color:#7a7268;margin:52px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--linea);}
  .tabla-env{overflow-x:auto;}
  table{border-collapse:collapse;width:100%;font-size:14px;background:#fff;
        border:1px solid var(--linea);border-radius:10px;overflow:hidden;}
  th,td{padding:9px 13px;text-align:left;border-bottom:1px solid #ece7de;}
  th{background:#faf8f5;font-size:12px;letter-spacing:.06em;text-transform:uppercase;
     color:#7a7268;}
  tr:last-child td{border-bottom:0;}
  td.n{font-variant-numeric:tabular-nums;}
  .gana{color:#2f6b3d;font-weight:700;}
  .pierde{color:#a8392b;}
  ul{padding-left:20px;} li{margin:7px 0;}
  .ojo{background:#fff8e8;border:1px solid #e8d9b4;border-radius:10px;
       padding:16px 20px;margin:16px 0;}
  .decide{background:#fff;border:1px solid var(--kraft);border-radius:10px;
          padding:16px 20px;margin:16px 0;}
  code{background:#efece5;padding:1px 5px;border-radius:4px;font-size:13px;}
  .nota{margin:0 0 14px;font-size:14px;color:#6b6359;max-width:72ch;}
"""


def main():
    SALIDA.parent.mkdir(parents=True, exist_ok=True)

    im = {
        "antes": b64(ANTES_PIEZA, 620),
        "desA": b64(DESPUES_A, 620),
        "desB": b64(DESPUES_B, 620),
        "corteAntes": b64(BASE_ANTES, 430, CORTE_PIEZA),
        "corteDesp": b64(BASE_CARTON, 430, CORTE_PIEZA),
        "corteSesion": b64(SESION, 430, CORTE_SESION),
        "sesion": b64(SESION, 430),
        "sesionMano": b64(SESION_MANO, 430),
        "logoA": b64(DESPUES_A, 560, (330, 2180, 2200, 3380)),
        "logoB": b64(DESPUES_B, 560, (330, 2180, 2200, 3380)),
        "logoAntes": b64(ANTES_PIEZA, 560, (330, 2180, 2200, 3380)),
    }

    sA = sat_y_tono(BASE_ANTES, CORTE_PIEZA)
    sD = sat_y_tono(BASE_CARTON, CORTE_PIEZA)
    sR = sat_y_tono(SESION, CORTE_SESION)

    p = ["<!doctype html>", '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         "<title>El vaso To Go de la ST del 28-09</title>",
         "<style>" + CSS + "</style>", '<div class="env">']

    p.append("<h1>Between · ST del 28-09 · el vaso, con la sesión real</h1>")
    p.append('<p class="sub">Columna T de la hoja STORIES · ronda 26 · 14-09-2026 · '
             "la escena, el tamaño del vaso, las tipografías y la persona "
             "<strong>no se tocaron</strong></p>")

    p.append('<div class="pedido"><div class="quien">Eli · hoy</div>'
             "<q>Debemos mejorar el vaso y trata de utilizar una foto como la sesión "
             "nueva de vasos ToGo.</q></div>")

    p.append('<p class="nota"><strong>Lo que pasa acá no es un retoque de gusto.</strong> '
             "Puesto el vaso de la pieza al lado del vaso de la sesión del 09-09 y "
             "normalizados al mismo ancho, el generado se delata en tres cosas que se "
             "pueden medir: el cartón está <strong>desaturado</strong> (es crema, no "
             "kraft), tiene <strong>motas gruesas de pulpa reciclada</strong> que el vaso "
             "real no tiene, y el <strong>logotipo mide menos de la mitad</strong> de lo "
             "que mide en el vaso real. Se cambió la SUPERFICIE del vaso aprobado; no se "
             "volvió a generar nada.</p>")

    p.append("<h2>La pieza entera</h2>")
    p.append('<div class="fila">')
    p.append(marco(im["antes"], "Antes · lo que está en Drive",
                   "Cartón crema con motas, logotipo chico. Es la versión del 11-09, "
                   "ronda 3."))
    p.append(marco(im["desA"], "Después · opción A (recomendada)",
                   "Cartón kraft de la sesión, con su fibra. Logotipo al máximo que "
                   "permite el brazo: se lee entero.", destacado=True))
    p.append(marco(im["desB"], "Después · opción B",
                   "Lo mismo, con el logotipo a la proporción exacta del vaso real. "
                   "La mano le tapa parte de «COFFEE &amp; BAR»."))
    p.append("</div>")

    p.append("<h2>El cartón, a tamaño real</h2>")
    p.append('<p class="nota">Los tres recortes son de 820 × 820 px sin reescalar, y los '
             "dos vasos miden casi lo mismo en pantalla (1 790 px el de la pieza, 1 970 px "
             "el de la sesión), así que muestran la misma cantidad de cartón.</p>")
    p.append('<p class="nota">⚠️ <strong>La trama del packshot se ve más marcada, y '
             "corresponde:</strong> esa foto está a pleno sol y de costado, que es la luz "
             "que más levanta el relieve del cartón. El vaso de la pieza está en la "
             "penumbra del patio, donde el tramado se aplana — como se ve en "
             "<code>togo-en-local-qr.jpg</code>, la toma de luz interior. Si la trama se "
             "subiera para igualar el packshot, el vaso dejaría de pertenecer a su escena."
             "</p>")
    p.append('<div class="fila">')
    p.append(marco(im["corteAntes"], "Antes · cartón generado",
                   "Motas oscuras de 5 a 15 px repartidas por todo el cuerpo. "
                   "Saturación " + f"{sA[0]:.2f}".replace(".", ",") + "."))
    p.append(marco(im["corteDesp"], "Después · cartón de la sesión",
                   "La trama del kraft real, sin una sola mota. "
                   "Saturación " + f"{sD[0]:.2f}".replace(".", ",") + ".", destacado=True))
    p.append(marco(im["corteSesion"], "La sesión · 09-09",
                   "<code>togo-grande-frontal.jpg</code> (IMG_4150), el packshot del vaso "
                   "grande. Saturación " + f"{sR[0]:.2f}".replace(".", ",") + "."))
    p.append("</div>")

    p.append("<h2>El logotipo: hay que elegir</h2>")
    p.append('<p class="nota">El bloque del logotipo <strong>mide 0,42 del ancho del vaso '
             "en la pieza y 0,91 en el vaso real</strong>. No es una impresión: sale de "
             "medir la altura de las letras contra el diámetro del vaso en las fotos de la "
             "sesión, y de la proporción del archivo oficial (3,0278 : 1). Por eso el "
             "logotipo de la pieza se lee como una calcomanía pegada y no como algo "
             "impreso en el vaso.</p>")
    p.append('<p class="nota">El problema es que, a la proporción real, el logotipo baja '
             "hasta donde va la mano. En las fotos de la sesión eso pasa igual —la mano "
             "tapa parte del logotipo y se ve natural—, pero acá el vaso es el "
             "protagonista de la historia y «COFFEE &amp; BAR» queda a medias.</p>")
    p.append('<div class="fila">')
    p.append(marco(im["logoAntes"], "Antes · 0,42 del ancho",
                   "Alto del bloque: 0,140 del ancho del vaso."))
    p.append(marco(im["logoA"], "A · 0,76 del ancho (recomendada)",
                   "Lo más grande que cabe entero entre la tapa y el brazo: 2 px de holgura "
                   "con la sombra de la tapa. Alto 0,294 — el doble que antes.", destacado=True))
    p.append(marco(im["logoB"], "B · 0,88 del ancho — el real",
                   "La proporción del vaso de la sesión. Alto 0,386. La mano le come "
                   "5 149 px de tinta en «COFFEE &amp; BAR»."))
    p.append("</div>")
    p.append('<div class="decide"><strong>Mi recomendación es la A.</strong> Llega al 84 % '
             "del ancho del vaso real —o sea deja de leerse como calcomanía— y no pierde "
             "una sola letra. La B es más fiel al vaso, y si prefieres esa la dejo: es "
             "cambiar un número en el comando, no rehacer la pieza.</div>")

    p.append("<h2>De dónde sale cada cosa</h2>")
    p.append('<div class="fila">')
    p.append(marco(im["sesion"], "IMG_4150 · el vaso grande",
                   "De acá salen la trama del cartón y las dos proporciones del logotipo. "
                   "Es la toma más nítida de las 39."))
    p.append(marco(im["sesionMano"], "IMG_4142 · el vaso en el local",
                   "Luz interior difusa, la más parecida a la penumbra del patio. De acá "
                   "salió el tono del kraft y acá se ve que la mano tapando parte del "
                   "logotipo es lo normal."))
    p.append("</div>")

    p.append("<h2>Los números</h2>")
    p.append('<div class="tabla-env"><table>'
             "<tr><th>Qué se midió</th><th>Antes</th><th>Vaso real (sesión 09-09)</th>"
             "<th>Después</th></tr>")
    filas = [
        ("Saturación del cartón", f"{sA[0]:.2f}", f"{sR[0]:.2f}", f"{sD[0]:.2f}"),
        ("Tono del cartón (R/G)", f"{sA[1]:.2f}", f"{sR[1]:.2f}", f"{sD[1]:.2f}"),
        ("Luminancia del parche", f"{sA[2]:.0f}", f"{sR[2]:.0f}", f"{sD[2]:.0f}"),
        ("Motas de pulpa", "5 a 15 px, por todo el vaso", "ninguna", "ninguna"),
        ("Logotipo / ancho del vaso", "0,42", "0,91", "A 0,76 · B 0,88"),
        ("Alto del bloque / ancho", "0,140", "0,377", "A 0,294 · B 0,386"),
    ]
    for q, a, r, d in filas:
        p.append('<tr><td>' + q + '</td><td class="n pierde">' + a.replace(".", ",") +
                 '</td><td class="n">' + r.replace(".", ",") +
                 '</td><td class="n gana">' + d.replace(".", ",") + "</td></tr>")
    p.append("</table></div>")

    p.append("<h2>Cómo se hizo</h2>")
    p.append("<ul>"
             "<li><strong>No se generó nada.</strong> Se partió de la misma base limpia de "
             "la ronda 4 (<code>r4-togo-sin-costura.png</code>, sin logotipo y sin la "
             "costura) y se le cambió la superficie al cuerpo del vaso.</li>"
             "<li><strong>La luz de la escena se conserva entera.</strong> El campo de luz "
             "sale del propio vaso con una mediana de 21 px, que borra las motas —miden 5 "
             "a 15 px— y deja intactos el pliegue del cartón y la sombra de contacto de "
             "los dedos, que es lo que hace que la mano se vea apoyada.</li>"
             "<li><strong>El cartón y su fibra salen de la foto.</strong> A la trama se le "
             "divide su propia iluminación, así que viaja el material y no el sol duro de "
             "esa toma. Va a 0,45 de escala: a 1:1 la trama se leía como damasco, porque "
             "el vaso de la pieza es 1,4 veces más ancho que el de la foto.</li>"
             "<li><strong>El color es el kraft real bajo la luz de esta escena.</strong> "
             "El tono medido en tres tomas de la sesión, corregido a medias por el "
             "iluminante frío del patio: la tapa negra, que es neutra, da B/G 1,16 acá y "
             "≈1,00 en la sesión. A medias y no del todo, porque la gradación de la pieza "
             "ya está aprobada.</li>"
             "<li><strong>Las manos no se recortaron a mano.</strong> Se marca su núcleo "
             "por tono (bajo 8°, que sólo tiene la piel) y se deja crecer hasta donde el "
             "tono sigue siendo de piel. Es reproducible: si mañana hay que rehacerlo, sale "
             "igual.</li>"
             "</ul>")

    p.append("<h2>Lo que NO se tocó</h2>")
    p.append("<ul>"
             "<li>La escena, el encuadre y el patio.</li>"
             "<li><strong>El tamaño del vaso, la tipografía y la persona</strong> — lo que "
             "cerraste en la ronda 3.</li>"
             "<li>La tapa, las manos, el pelo y el fondo.</li>"
             "<li>El titular y su diagramación. La banda limpia sigue en y = 300 a 880 y el "
             "contraste del beige no se movió: el texto va sobre el muro, no sobre el "
             "vaso.</li>"
             "</ul>")

    p.append('<div class="ojo"><strong>⚠️ Lo que queda distinto del vaso real, y no lo '
             "arreglé.</strong> La <strong>tapa</strong> de la pieza es mate y de plástico "
             "modelado; la de la sesión es <strong>brillante</strong>, con un reflejo vivo "
             "en el reborde enrollado y el pico de la boquilla en el canto, no en el medio. "
             "Cambiarla es rehacer geometría, no es un retoque de superficie, y no entraba "
             "en «mejorar el vaso» sin volver a tocar algo que ya aprobaste. Si quieres que "
             "vaya, es una ronda aparte.</div>")

    p.append("</div>")
    SALIDA.write_text("\n".join(p), encoding="utf-8")
    print("pagina -> " + str(SALIDA))
    print(f"  antes  sat {sA[0]:.3f}  R/G {sA[1]:.3f}  lum {sA[2]:.1f}")
    print(f"  despues sat {sD[0]:.3f}  R/G {sD[1]:.3f}  lum {sD[2]:.1f}")
    print(f"  sesion sat {sR[0]:.3f}  R/G {sR[1]:.3f}  lum {sR[2]:.1f}")


if __name__ == "__main__":
    main()

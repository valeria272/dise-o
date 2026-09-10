#!/usr/bin/env python3
"""Version publicable de la revision de la ronda 10 (ST Cowork 16-09, Between).

Es la misma pagina que `between-cowork-r10-html.py` deja en `out/`, pero escrita
para publicarse como Artifact: sin `<!doctype>`, `<head>` ni `<body>` (el
publicador los envuelve), con tokens de color para tema claro y oscuro, y con
las tipografias de la marca desde Google Fonts.

Por que existe: la memoria `antes-y-despues-en-html` dice que Eli revisa mirando
GRANDE y comparado, y que la pagina se PUBLICA — un archivo en el disco no le
sirve. Las imagenes van embebidas como data URI porque el visor bloquea
imagenes externas.

    python scripts/between-cowork-r10-artifact.py
"""
import base64
import io
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "out/hilton/between/ronda10-artifact.html"

FUENTES = {
    "antes":      (RAIZ / "out/hilton/between/ronda10-antes.jpg", 720),
    "despues":    (RAIZ / "out/hilton/between/st-s3/BW-S3-Cowork.png", 720),
    "refeli":     (RAIZ / "raw/hilton/between/ediciones-ia-eli"
                   / "magnific_agrega-una-laptop-en-la-m_iAi90W63uK.png", 460),
    "fondo":      (RAIZ / "public/assets/hilton/between/st-s3/st-16-09-cowork-escena.jpg", 460),
    "crudo":      (RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_8539.jpg", 360),
    "limpia":     (RAIZ / "out/hilton/between/st-s3/BW-S3-Cowork-sin-vaso.png", 360),
    "montaje":    (RAIZ / "out/hilton/between/ronda11-montaje-rechazado.jpg", 360),
    "variante":   (RAIZ / "out/hilton/between/ronda11-variante-v2.jpg", 460),
}


def b64(ruta, ancho, calidad=84):
    im = Image.open(ruta).convert("RGB")
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=calidad, optimize=True)
    return base64.b64encode(b.getvalue()).decode()


CSS = """
:root{
  --papel:#f6f3ee; --superficie:#fffdfa; --tinta:#241a12; --tinta-2:#6b6054;
  --linea:#e2dbcf; --taupe:#6d6455; --beige:#fff9eb;
  --pide:#a8392b; --sube:#3d6b45; --baja:#a8392b;
  --sombra:0 1px 2px rgba(36,26,18,.05), 0 12px 32px rgba(36,26,18,.07);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --papel:#17110c; --superficie:#211a13; --tinta:#f0e8dc; --tinta-2:#a89b8a;
    --linea:#332921; --taupe:#8a7f6c; --beige:#fff9eb;
    --pide:#e08573; --sube:#8fc79b; --baja:#e08573;
    --sombra:0 1px 2px rgba(0,0,0,.4), 0 12px 32px rgba(0,0,0,.34);
  }
}
:root[data-theme="dark"]{
  --papel:#17110c; --superficie:#211a13; --tinta:#f0e8dc; --tinta-2:#a89b8a;
  --linea:#332921; --taupe:#8a7f6c; --beige:#fff9eb;
  --pide:#e08573; --sube:#8fc79b; --baja:#e08573;
  --sombra:0 1px 2px rgba(0,0,0,.4), 0 12px 32px rgba(0,0,0,.34);
}
*{box-sizing:border-box;}
body{
  margin:0; background:var(--papel); color:var(--tinta);
  font-family:"Source Serif 4",Georgia,"Times New Roman",serif;
  font-size:17px; line-height:1.62;
  -webkit-font-smoothing:antialiased;
}
.env{max-width:1120px; margin:0 auto; padding-inline:20px; padding-block:56px 96px;}

.eyebrow{
  font-family:Raleway,"Helvetica Neue",Arial,sans-serif;
  font-weight:700; font-size:12px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--tinta-2); margin:0 0 12px;
}
h1{
  font-family:Raleway,"Helvetica Neue",Arial,sans-serif;
  font-weight:800; font-size:clamp(30px,5vw,44px); line-height:1.08;
  letter-spacing:-.015em; margin:0 0 10px; text-wrap:balance;
}
.bajada{margin:0 0 40px; color:var(--tinta-2); font-size:18px; max-width:62ch;}
h2{
  font-family:Raleway,"Helvetica Neue",Arial,sans-serif;
  font-weight:700; font-size:13px; letter-spacing:.14em; text-transform:uppercase;
  color:var(--tinta-2); margin:64px 0 18px; padding-bottom:10px;
  border-bottom:1px solid var(--linea);
}
p{max-width:68ch;}
.nota{color:var(--tinta-2); font-size:16px; margin:0 0 18px;}

/* el pedido del cliente: es la razon de la ronda, lleva el unico acento fuerte */
.pedido{
  border-left:3px solid var(--pide); padding:4px 0 4px 22px; margin:0 0 44px;
}
.pedido .quien{
  font-family:Raleway,"Helvetica Neue",Arial,sans-serif;
  font-size:12px; letter-spacing:.09em; text-transform:uppercase;
  color:var(--tinta-2); margin-bottom:8px;
}
.pedido q{font-size:22px; line-height:1.42; font-style:italic; quotes:"\\201C" "\\201D";}

.fila{display:grid; gap:26px; grid-template-columns:repeat(auto-fit,minmax(280px,1fr));}
.fila.tres{grid-template-columns:repeat(auto-fit,minmax(220px,1fr));}
figure{margin:0; display:flex; flex-direction:column;}
figure img{
  display:block; width:100%; max-width:100%; height:auto; border-radius:3px;
  border:1px solid var(--linea);
}
figure.hero img{box-shadow:var(--sombra);}
.rotulo{
  font-family:Raleway,"Helvetica Neue",Arial,sans-serif;
  font-weight:700; font-size:12px; letter-spacing:.11em; text-transform:uppercase;
  margin:0 0 10px; display:flex; align-items:baseline; gap:9px;
}
.rotulo .paso{
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-weight:500;
  font-size:11px; color:var(--tinta-2); letter-spacing:0;
}
.rotulo em{font-style:normal; color:var(--taupe);}
figcaption{margin-top:11px; font-size:15px; line-height:1.5; color:var(--tinta-2);}

table{
  border-collapse:collapse; width:100%; font-size:16px; margin:0;
  font-variant-numeric:tabular-nums;
}
th,td{padding:10px 14px 10px 0; text-align:left; border-bottom:1px solid var(--linea);}
th{
  font-family:Raleway,"Helvetica Neue",Arial,sans-serif;
  font-weight:700; font-size:11px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--tinta-2);
}
tr:last-child td{border-bottom:0;}
td.n{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:15px;}
.sube{color:var(--sube); font-weight:600;}
.baja{color:var(--baja);}
.tabla-envoltura{overflow-x:auto; margin-bottom:8px;}

ul{padding-left:0; list-style:none; max-width:70ch;}
li{margin:0 0 14px; padding-left:20px; position:relative;}
li::before{
  content:""; position:absolute; left:0; top:.72em;
  width:7px; height:1px; background:var(--taupe);
}
li strong{font-weight:600;}

.ojo{
  background:var(--superficie); border:1px solid var(--linea);
  border-radius:4px; padding:20px 24px; margin:22px 0; max-width:74ch;
}
.ojo p{margin:0;}
.ojo p + p{margin-top:12px;}

code{
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:.86em;
  background:var(--superficie); border:1px solid var(--linea);
  padding:1px 5px; border-radius:3px; word-break:break-word;
}

.cierre{
  margin-top:72px; padding-top:26px; border-top:2px solid var(--tinta);
  display:grid; gap:20px; grid-template-columns:repeat(auto-fit,minmax(190px,1fr));
}
.dato .k{
  font-family:Raleway,"Helvetica Neue",Arial,sans-serif;
  font-size:11px; letter-spacing:.11em; text-transform:uppercase;
  color:var(--tinta-2); margin-bottom:5px;
}
.dato .v{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:15px;}
@media (prefers-reduced-motion: reduce){*{animation:none!important; transition:none!important;}}
"""


def fig(dato, rotulo, nota, paso=None, hero=False):
    if not dato:
        return ""
    p = ('<span class="paso">%s</span>' % paso) if paso else ""
    cls = ' class="hero"' if hero else ""
    return (
        "<figure%s>" % cls
        + '<div class="rotulo">' + p + rotulo + "</div>"
        + '<img src="data:image/jpeg;base64,' + dato + '" alt="' + rotulo + '">'
        + "<figcaption>" + nota + "</figcaption></figure>"
    )


def main():
    im = {}
    for k, (ruta, ancho) in FUENTES.items():
        im[k] = b64(ruta, ancho) if ruta.exists() else None
        if im[k] is None:
            print("  falta " + str(ruta))

    h = []
    a = h.append
    a("<title>Cowork 16-09 · ronda 11</title>")
    a('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      "family=IBM+Plex+Mono:wght@400;500&"
      "family=Raleway:wght@500;600;700;800&"
      'family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">')
    a("<style>" + CSS + "</style>")
    a('<div class="env">')

    a('<p class="eyebrow">Between · Coffee &amp; Bar — historia del 16 de septiembre</p>')
    a("<h1>La escena del Cowork, producida entera</h1>")
    a('<p class="bajada">Columna N de la hoja STORIES, ronda 11. El fondo es el '
      "segundo piso real de Between, fotografiado por el cliente; el vaso, la "
      "laptop y el desayuno se agregaron dentro de la escena en vez de pegarse "
      "encima.</p>")

    a('<div class="pedido"><div class="quien">Eli · sobre la entrega anterior</div>'
      "<q>Me parece que el montaje está mal logrado, la foto de fondo original "
      "debes añadir un vaso togo, un notebook con logo apple, da lo mismo si "
      "aparece que sea sutil. Un desayuno de sándwich, como se ven en las fotos. "
      "Hazlo nuevamente y recuerda hacer un buen prompt, en magnific.</q></div>")
    a('<p class="nota" style="margin:-24px 0 40px;">Y antes, lo que abrió la ronda: '
      "Scarlette Muñoz sobre <code>STORIES!N</code>, «podemos cambiar la imagen a "
      "una real de cowork?».</p>")

    a('<div class="fila">')
    a(fig(im["antes"], "Antes", "La escena entera —mesa, taza, croissant, notebook y "
          "planta— salió de un prompt. No es Between.", hero=True))
    a(fig(im["despues"], "Después <em>· en Drive</em>",
          "El segundo piso real. El vaso To&nbsp;Go, la laptop con su manzana y el "
          "desayuno de sándwich se pintaron dentro de la escena, con su luz y su "
          "profundidad de campo.", hero=True))
    a("</div>")

    a("<h2>Tu edición de Magnific fue la referencia</h2>")
    a('<p class="nota">En <code>raw/hilton/between/ediciones-ia-eli/</code> hay 42 '
      "ediciones tuyas y <strong>el nombre de cada archivo guarda tu propio "
      "prompt</strong>. Una decía <code>magnific_agrega-una-laptop-en-la-m…</code>: "
      "de ahí salió el tratamiento de la laptop —material, color, escala respecto de "
      "la mesa y luz cálida.</p>")
    a('<div class="fila">')
    a(fig(im["refeli"], "Tu referencia",
          "Mesa de madera, portátil, el vaso Between real con arte latte, follaje "
          "detrás."))
    a(fig(im["fondo"], "El fondo nuevo",
          "La foto real del cowork con la laptop y la libreta agregadas, y el vaso "
          "real montado encima. Sin texto."))
    a("</div>")

    a("<h2>El camino</h2>")
    a('<div class="fila tres">')
    a(fig(im["crudo"], "El material", "IMG_8539 tal como salió del teléfono. Al "
          "reencuadrar se le quitó techo: el cielo de la sala es lo peor de la toma.",
          paso="01"))
    a(fig(im["limpia"], "Sólo la foto", "La mesa queda vacía y la mitad de abajo es "
          "una tabla sin nada. El manual §4 pide mesa servida.", paso="02"))
    a(fig(im["montaje"], "El montaje, descartado", "Aquí el vaso se pegaba encima con "
          "el script de montaje. Se veía pegado, y es lo que mandaste a rehacer.",
          paso="03"))
    a("</div>")

    a("<h2>La otra variante, por si prefieres ese desayuno</h2>")
    a('<p class="nota">Se generaron tres. Elegí la del sándwich: los cuatro '
      "triángulos de la otra salen algo secos y repetidos, y acá el vaso queda más "
      "legible. Pero el desayuno es decisión tuya y cambiarlo es una línea.</p>")
    a('<div class="fila">')
    a(fig(im["variante"], "Variante · triángulos de tostada",
          "Es más literal respecto de las fotos de desayuno del cliente, que sirven "
          "los triángulos en abanico sobre plato blanco."))
    a(fig(im["fondo"], "La elegida, sin texto",
          "El fondo tal como quedó: sándwich tostado, el vaso con su logotipo y la "
          "laptop con la manzana apenas sugerida."))
    a("</div>")

    a("<h2>Por qué esta foto y no otra de las 91</h2>")
    a("<ul>"
      "<li>El cliente <strong>tiene el espacio fotografiado</strong>: 22 videos y 20 "
      "HEIC del segundo piso, de los que salen <strong>91 fotogramas, todos "
      "verticales 9:16 nativos</strong>. Compuerta de material: 91 válidos, 0 rotos.</li>"
      "<li>Se midió en los 91 cuán plana tienen la zona del titular. Los más limpios "
      "—8551, 8554, 8555, 8558— son pared beige lisa con una mesa delante, y "
      "<strong>son los que menos sirven</strong>: se leen como sala de espera vacía, "
      "que es lo que el cliente rechazó el 31-08.</li>"
      "<li><strong>La restricción que de verdad decide es el cartel</strong>, no el "
      "texto: cierra en y≈1906 de 4000, así que la mesa tiene que estar en la mitad "
      "de abajo o se pierde detrás. De 91 fotogramas, sólo 8539 cumple.</li>"
      "<li>Y es el encuadre del brief: «fotografía vertical tomada desde una de las "
      "mesas de Between. En primer plano, una mesa de madera. Al fondo, parte de la "
      "cafetería».</li>"
      "</ul>")

    a("<h2>El contraste, que era la duda</h2>")
    a('<p class="nota">Toda la geometría del titular está calibrada contra la foto '
      "vieja, así que cambiar la foto podía obligar a rehacerla. Medido el beige "
      "<code>#fff9eb</code> en las filas donde va el texto, pasa lo contrario: "
      "<strong>mejora</strong>. El peor tercio sube de 2,08 a 3,02 y el resto del "
      "bloque va entre 3,4 y 17,6, así que <strong>no se movió ninguna "
      "medida</strong>.</p>")
    a('<div class="tabla-envoltura"><table>'
      "<tr><th>y</th><th>tercio</th><th>foto generada</th><th>foto real</th></tr>")
    for y, ter, viejo, nuevo in [("200", "centro", "2,17", "3,02"),
                                 ("300", "izquierdo", "2,08", "3,42"),
                                 ("400", "izquierdo", "2,08", "5,58"),
                                 ("400", "centro", "2,12", "10,49"),
                                 ("470", "izquierdo", "2,10", "3,75"),
                                 ("540", "centro", "2,30", "6,30")]:
        a('<tr><td class="n">%s</td><td>%s</td><td class="n baja">%s</td>'
          '<td class="n sube">%s</td></tr>' % (y, ter, viejo, nuevo))
    a("</table></div>")

    a('<p class="nota" style="margin-top:26px;">Lo único que cambió de tinta es el '
      "<strong>lockup</strong>: iba en el café de marca y sobre el cielo gris se cae. "
      "Pasa a beige, que es el <code>logoTono</code> por defecto del sistema — el café "
      "era la excepción que pedía la pared clara de la foto generada.</p>")
    a('<div class="tabla-envoltura"><table>'
      "<tr><th>zona del lockup</th><th>café #675b49</th><th>beige #fff9eb</th></tr>"
      '<tr><td>y 200 · tres tercios</td><td class="n baja">2,00 · 1,80 · 1,54</td>'
      '<td class="n sube">3,16 · 3,51 · 4,09</td></tr>'
      '<tr><td>y 300 · tres tercios</td><td class="n baja">1,99 · 1,92 · 2,09</td>'
      '<td class="n sube">3,17 · 3,29 · 3,02</td></tr>'
      "</table></div>")

    a("<h2>El paso de IA, y el prompt</h2>")
    a("<ul>"
      "<li><strong>Nano Banana Pro</strong> con <strong>cuatro referencias</strong> "
      "a 4K, que salió a 3072 × 5504: resolución de sobra para los 2250 × 4000 de "
      "la entrega. Es lo que manda la tabla de decisión cuando la escena tiene que "
      "parecerse a una foto real del cliente.</li>"
      "<li>Se probó antes el modelo imagen→imagen y <strong>se descartó por "
      "resolución</strong>: devuelve 768 × 1344, un tercio de lo que pide una "
      "story.</li>"
      "<li><strong>Cada referencia hace un trabajo:</strong> la foto real del cowork "
      "es la escena que se conserva; tu edición de Magnific da el tratamiento; el "
      "recorte del vaso real da el logotipo; y una foto de la sesión de desayunos "
      "da el plato y el pan.</li>"
      "<li>El prompt va estructurado —qué es cada referencia, lo que <em>no</em> se "
      "toca, lo que se agrega objeto por objeto, la luz medida, la composición y al "
      "final las negaciones— y <strong>lo que no se toca va antes de lo que se "
      "agrega</strong>: puesto al final, el modelo ya reescribió la escena.</li>"
      "<li>⚠️ <strong>El prompt topa en 3000 caracteres.</strong> El primero medía "
      "4087 y la API devolvía un 400 sin más explicación. Quedó en 2988.</li>"
      "<li>La composición se le pide por la restricción real: «todos los objetos en "
      "la mitad de abajo del cuadro», porque el cartel taupe cierra en y≈1906 y todo "
      "lo que quede más arriba se pierde detrás.</li>"
      "</ul>")

    a("<h2>Lo que hizo que el logotipo saliera bien</h2>")
    a('<p class="nota">Es la diferencia con la ronda 4, cuando el cliente rechazó un '
      "logotipo estampado sobre un vaso generado: <strong>pasarle el vaso real como "
      "referencia</strong>. Con él entre las referencias, dos de las tres variantes "
      "escribieron la <strong>Ǝ invertida</strong> y la W angular de la marca. La "
      "que no la tomó bien escribió un «BETWEEN» con E normal y se descartó.</p>")

    a("<h2>Lo que queda abierto</h2>")
    a('<div class="ojo"><p><strong>Una foto real de alguien trabajando en el '
      "cowork.</strong> El brief pide «notebook abierto + café Between + libreta» y "
      "el cliente no tiene ningún notebook fotografiado ahí: los únicos fotogramas "
      "con notebook son del lounge del hotel, con caras reconocibles y en otro "
      "espacio. Con esa foto, esta pieza dejaría de necesitar el paso de IA.</p>"
      "<p><strong>El QA marca cuatro avisos y los cuatro son falsos positivos</strong>, "
      "verificado imprimiendo dónde están los píxeles: son <strong>29 píxeles</strong> "
      "del foco del cielo en la primera fila de la imagen, y en los otros tres bordes "
      "hay <strong>cero</strong>. Van <strong>cinco piezas seguidas</strong> con el "
      "mismo defecto: al script le falta distinguir un brillo de foto de un trazo de "
      "letra.</p></div>")

    a('<div class="cierre">')
    for k, v in [("Entrega", "2250 × 4000 · 150 ppp"),
                 ("Peso", "7 350 797 B"),
                 ("En Drive", "mismo archivo · el enlace no cambió"),
                 ("Reproducible", "byte a byte (cmp)")]:
        a('<div class="dato"><div class="k">%s</div><div class="v">%s</div></div>' % (k, v))
    a("</div>")

    a("</div>")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text("\n".join(h), encoding="utf-8")
    print("OK " + str(SALIDA) + "  ·  %.0f KB" % (SALIDA.stat().st_size / 1024))


if __name__ == "__main__":
    main()

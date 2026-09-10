#!/usr/bin/env python3
"""Antes y despues de la RONDA 10 de la ST de Cowork (col N, 16-09) de Between.

Por que existe
--------------
Eli aprueba MIRANDO y comparado (memoria `antes-y-despues-en-html`): cada ronda
se entrega como una pagina con el antes, el despues y la referencia, y los
numeros van abajo. Las imagenes van EMBEBIDAS en JPEG, asi que la pagina es un
solo archivo y se abre sin servidor.

    python scripts/between-cowork-r10-html.py
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
SALIDA = RAIZ / "out/hilton/between/ronda10-cowork-antes-despues.html"


def b64(ruta, ancho, calidad=86):
    im = Image.open(ruta).convert("RGB")
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=calidad, optimize=True)
    return base64.b64encode(b.getvalue()).decode()


def marco(dato, rotulo, nota, destacado=False):
    if not dato:
        return ""
    cls = "marco destacado" if destacado else "marco"
    return (
        '<figure class="' + cls + '">'
        '<div class="rotulo">' + rotulo + "</div>"
        '<img src="data:image/jpeg;base64,' + dato + '" alt="' + rotulo + '">'
        "<figcaption>" + nota + "</figcaption>"
        "</figure>"
    )


def main():
    fuentes = {
        "antes": (RAIZ / "out/hilton/between/ronda10-antes.jpg", 760),
        "despues": (RAIZ / "out/hilton/between/st-s3/BW-S3-Cowork.png", 760),
        "limpia": (RAIZ / "out/hilton/between/st-s3/BW-S3-Cowork-sin-vaso.png", 520),
        "crudo": (RAIZ / "raw/hilton/between/cowork-2do-piso/fotos/IMG_8539.jpg", 520),
    }
    p = {}
    for k, (ruta, ancho) in fuentes.items():
        p[k] = b64(ruta, ancho) if ruta.exists() else None
        if p[k] is None:
            print("  falta " + str(ruta))

    css = """
  :root{--tinta:#241a12;--papel:#f4f1ec;--taupe:#6d6455;--beige:#fff9eb;
        --linea:#ddd6ca;--rojo:#a8392b;}
  *{box-sizing:border-box;}
  body{margin:0;background:var(--papel);color:var(--tinta);
       font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}
  .env{max-width:1180px;margin:0 auto;padding:48px 24px 90px;}
  h1{font-size:30px;letter-spacing:-.01em;margin:0 0 6px;}
  .sub{color:#7a7268;margin:0 0 34px;}
  .pedido{background:#fff;border:1px solid var(--linea);border-left:4px solid var(--rojo);
          border-radius:10px;padding:18px 22px;margin:0 0 38px;}
  .pedido .quien{font-size:13px;color:#7a7268;margin-bottom:6px;}
  .pedido q{font-size:18px;font-style:italic;}
  .fila{display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start;}
  .marco{flex:1 1 300px;margin:0;background:#fff;border:1px solid var(--linea);
         border-radius:12px;overflow:hidden;}
  .marco.destacado{border-color:var(--taupe);box-shadow:0 10px 34px rgba(36,26,18,.14);}
  .rotulo{padding:11px 15px;font-size:12px;font-weight:700;letter-spacing:.09em;
          text-transform:uppercase;background:#faf8f5;border-bottom:1px solid var(--linea);}
  .destacado .rotulo{background:var(--taupe);color:var(--beige);border-bottom:0;}
  .marco img{display:block;width:100%;height:auto;}
  figcaption{padding:12px 15px;font-size:13px;color:#6b6359;border-top:1px solid var(--linea);}
  h2{font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
     color:#7a7268;margin:52px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--linea);}
  table{border-collapse:collapse;width:100%;font-size:14px;background:#fff;
        border:1px solid var(--linea);border-radius:10px;overflow:hidden;}
  th,td{padding:9px 13px;text-align:left;border-bottom:1px solid #ece7de;}
  th{background:#faf8f5;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:#7a7268;}
  tr:last-child td{border-bottom:0;}
  td.n{font-variant-numeric:tabular-nums;}
  .gana{color:#2f6b3d;font-weight:700;}
  .pierde{color:#a8392b;}
  ul{padding-left:20px;} li{margin:7px 0;}
  .ojo{background:#fff8e8;border:1px solid #e8d9b4;border-radius:10px;padding:16px 20px;margin:16px 0;}
  code{background:#efece5;padding:1px 5px;border-radius:4px;font-size:13px;}
  .nota{margin:0 0 10px;font-size:14px;color:#6b6359;}
"""

    partes = []
    partes.append("<!doctype html>")
    partes.append('<meta charset="utf-8">')
    partes.append("<title>Between · ST Cowork 16-09 · ronda 10</title>")
    partes.append("<style>" + css + "</style>")
    partes.append('<div class="env">')

    partes.append("<h1>Between · ST Cowork del 16-09</h1>")
    partes.append('<p class="sub">Columna N de la hoja STORIES · ronda 10 · '
                  "10-09-2026 · estado <strong>EN CAMBIOS</strong></p>")

    partes.append('<div class="pedido">'
                  '<div class="quien">Scarlette Munoz · hoy 12:55 · comentario nativo '
                  "sobre <code>STORIES!N</code></div>"
                  "<q>@elisabet.soto podemos cambiar la imagen a una real de cowork?</q>"
                  "</div>")

    partes.append('<div class="fila">')
    partes.append(marco(p["antes"], "Antes · foto generada",
                        "La escena entera —mesa, taza, croissant, notebook y planta— "
                        "salio de un prompt. No es Between."))
    partes.append(marco(p["despues"], "Despues · foto real del 2.º piso",
                        "IMG_8539 reencuadrado, con el vaso To Go real del cliente montado "
                        "sobre la mesa. Es lo que quedo en Drive.", destacado=True))
    partes.append("</div>")

    partes.append("<h2>La alternativa, por si prefieres la foto sin intervenir</h2>")
    partes.append('<div class="fila">')
    partes.append(marco(p["limpia"], "Sin el vaso",
                        "La foto real tal cual. La mesa queda vacia: la mitad de abajo es "
                        "una tabla sin nada, y el manual §4 pide mesa servida."))
    partes.append(marco(p["crudo"], "El material, sin tocar",
                        "IMG_8539 completo. Al reencuadrar se le saco techo por arriba: "
                        "el cielo de la sala es lo peor de la toma."))
    partes.append("</div>")

    partes.append("<h2>Por que esta foto y no otra de las 91</h2>")
    partes.append("<ul>"
                  "<li>El cliente <strong>tiene el espacio fotografiado</strong>: 22 videos y "
                  "20 HEIC del segundo piso, de los que salen <strong>91 fotogramas, todos "
                  "verticales 9:16 nativos</strong>. Pasaron la compuerta de material: 91 "
                  "validos, 0 rotos.</li>"
                  "<li>Se midio en los 91 cuan plana tienen la zona del texto. Los mas limpios "
                  "—8551, 8554, 8555, 8558— son <strong>pared beige lisa con una mesa delante, "
                  "y son los que menos sirven</strong>: se leen como sala de espera vacia, que "
                  "es justo lo que el cliente rechazo el 31-08 («mesas altas vacias»).</li>"
                  "<li><strong>8539 es el unico fotograma con la mesa en la mitad de "
                  "abajo</strong>, que es lo que esta diagramacion necesita: el cartel taupe "
                  "cierra en y≈1906 y todo lo que quede mas arriba se pierde detras.</li>"
                  "<li>Y es el encuadre que pide el brief: «fotografia vertical tomada desde una "
                  "de las mesas de Between. En primer plano, una mesa de madera. Al fondo, parte "
                  "de la cafeteria».</li>"
                  "</ul>")

    partes.append('<div class="ojo">'
                  "<strong>⚠️ El notebook del brief no esta, y es un hueco de material.</strong> "
                  "El brief pide «notebook abierto + cafe Between + libreta». El cliente "
                  "<strong>no tiene ningun notebook fotografiado</strong>: los unicos fotogramas "
                  "con notebook son del <em>lounge del hotel</em>, con caras reconocibles, y no "
                  "son el cowork. No se genero uno — se pide la foto."
                  "</div>")

    partes.append("<h2>Los numeros</h2>")
    partes.append('<p class="nota">Contraste del titular beige <code>#fff9eb</code> contra la '
                  "foto, medido en las filas donde va el texto. <strong>La foto real lo "
                  "mejora</strong>, que era la duda: por eso no se movio ninguna medida de la "
                  "geometria que aprobaste en las rondas 5, 6 y 7.</p>")
    filas = [("400", "izquierdo", "2,08", "3,18"),
             ("400", "centro", "2,12", "3,30"),
             ("400", "derecho", "2,69", "4,09"),
             ("470", "izquierdo", "2,10", "3,38"),
             ("540", "centro", "2,30", "3,60")]
    t = ["<table><tr><th>y</th><th>tercio</th><th>beige · foto generada</th>"
         "<th>beige · foto real</th></tr>"]
    for y, ter, a, b in filas:
        t.append('<tr><td class="n">' + y + "</td><td>" + ter + '</td>'
                 '<td class="n pierde">' + a + '</td><td class="n gana">' + b + "</td></tr>")
    t.append("</table>")
    partes.append("".join(t))

    partes.append('<p class="nota" style="margin-top:26px;">Lo unico que cambio de tinta es el '
                  "<strong>lockup</strong>: iba en el cafe de marca y sobre el cielo gris de la "
                  "foto real se cae. Pasa a beige, que es el <code>logoTono</code> por defecto "
                  "del sistema — el cafe era la excepcion que pedia la pared clara de la foto "
                  "generada.</p>")
    partes.append("<table>"
                  "<tr><th>Zona del lockup</th><th>cafe <code>#675b49</code></th>"
                  "<th>beige <code>#fff9eb</code></th></tr>"
                  '<tr><td>y 200 · tres tercios</td><td class="n pierde">2,00 · 1,80 · 1,54</td>'
                  '<td class="n gana">3,16 · 3,51 · 4,09</td></tr>'
                  '<tr><td>y 300 · tres tercios</td><td class="n pierde">1,99 · 1,92 · 2,09</td>'
                  '<td class="n gana">3,17 · 3,29 · 3,02</td></tr>'
                  "</table>")

    partes.append("<h2>El montaje del vaso</h2>")
    partes.append("<ul>"
                  "<li>Es el recorte <strong>real</strong> del cliente "
                  "(<code>togo-vaso-real-nobg.png</code>, de la sesion del 25-07), montado con "
                  "<code>scripts/between-montar-vaso.py</code>: iguala nitidez, nivel y "
                  "temperatura, y dibuja la sombra de contacto.</li>"
                  "<li><strong>Luz medida en la mesa: viene de la derecha</strong> — brillo "
                  "174–192 a x≈1500–1890 contra 80–138 en el borde izquierdo. Por eso la sombra "
                  "cae a la izquierda.</li>"
                  "<li>Desenfoque aplicado al recorte: 1,3 px, para bajarlo a la nitidez de la "
                  "escena.</li>"
                  "<li>El vaso <strong>no se espeja</strong>: invertiria el logotipo.</li>"
                  "</ul>")

    partes.append("<h2>QA y entrega</h2>")
    partes.append("<ul>"
                  "<li><code>between-qa.py</code> marca dos avisos y los dos son <strong>falsos "
                  "positivos</strong>, verificado imprimiendo donde estan los pixeles: "
                  "<strong>7 pixeles</strong> en el borde derecho (un brillo especular del muro "
                  "de listones, a y 1 461) y <strong>2 pixeles</strong> en la zona segura "
                  "superior (el foco del cielo). El texto real esta dentro de margenes.</li>"
                  "<li>Entrega: 2250 × 4000 a 150 ppp · 6 775 199 B.</li>"
                  "<li>Subida <strong>reemplazando el mismo archivo</strong> de "
                  "<code>S3 HILTON SEP 2026/BW/STORIES</code>, asi que <strong>el enlace no "
                  "cambio</strong>. Verificado contra Drive: <code>fileSize</code> 6 775 199 B, "
                  "en la carpeta STORIES (no cayo en «Mi unidad»).</li>"
                  "<li>Las otras dos piezas de la S3 (14-09 y 18-09) <strong>no se "
                  "tocaron</strong>: siguen en 8 077 154 B y 7 249 755 B.</li>"
                  "</ul>")

    partes.append("<h2>Y una de metodo, que vale para toda la cuenta</h2>")
    partes.append('<div class="ojo">'
                  "El <code>.xlsx</code> que baja <code>uc?export=download</code> de la grilla de "
                  "Between <strong>esta congelado desde el 09-09</strong>: hoy bajo con el md5 "
                  "identico. La ronda del cliente vive en la <strong>capa viva de Sheets</strong> "
                  "y se lee con<br><code>docs.google.com/spreadsheets/d/&lt;id&gt;/export?"
                  "format=csv&amp;gid=&lt;gid&gt;</code><br>Ahi si aparecen los dos comentarios "
                  "de la celda N tachados y el estado real. Es la respuesta al misterio que "
                  "quedo abierto ayer."
                  "</div>")

    partes.append("</div>")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text("\n".join(partes), encoding="utf-8")
    print("OK " + str(SALIDA) + "  ·  %.0f KB" % (SALIDA.stat().st_size / 1024))


if __name__ == "__main__":
    main()

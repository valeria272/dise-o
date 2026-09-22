#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El molde de la página de revisión — antes, después y lo medido, en un archivo.

Eli aprueba MIRANDO y comparado, así que cada ronda termina en una página HTML
(memoria `antes-y-despues-en-html`). Hasta el 22-09-2026 esa página se escribía
entera cada vez: 21 scripts, 6.356 líneas, ~300 por ronda, y entre dos rondas
seguidas de la MISMA pieza sólo cambiaban 160. El resto era siempre lo mismo
—incrustar el JPEG en base64, recortar un detalle, la hoja de estilo, el
envoltorio del HTML— reescrito a mano una y otra vez.

Eso es lo que este módulo se lleva. Una ronda pasa de ~300 líneas a ~40, y lo
que queda escrito es lo único que de verdad cambia: qué pediste, qué cambió y
qué se midió.

    from _revision import Pagina

    p = Pagina("between", "BETWEEN · CONCURSO · RONDA 9",
               "La cajita inclinada de la referencia",
               "21-09-2026 · FEED del 24-09 (S4)",
               "out/hilton/between/concurso-s3-r9/revision-r9.html")
    p.pedido("Quiero la opción 3, pero con lo del CEO en cajita...", "Eli", "21-09")
    p.comparar(("antes.png", "halo de 12"), ("final.png", "halo de 16"),
               titulo="El titular", detalle=(280, 400, 820, 600), elige=True)
    p.medido([("CONCURSO contra el papel", "4,14 : 1", "ok", "la caja beige daba 1,50")])
    p.escribir()

Tres cosas que el molde hace y los scripts sueltos no hacían:

· **Se escribe en español, no en entidades HTML.** Las páginas viejas llevaban
  `&oacute;` y `&laquo;` a mano porque se armaron a pedazos. El archivo sale en
  UTF-8 y declara el charset, así que las tildes van tal cual. Las etiquetas
  (`<b>`, `<code>`) siguen valiendo dentro del texto: esto NO escapa HTML, a
  propósito.

· **Avisa de la imagen que falta en vez de reventar.** Un `antes` mal escrito
  dejaba una página a medias; acá sale un recuadro naranjo que dice qué ruta
  faltó. La ronda se manda igual y se corrige el nombre, no se pierde la vuelta.

· **Deja las dos salidas.** El archivo local que se abre con doble clic y la
  versión sin `<html>` para publicar como artefacto, que es como se entregan las
  revisiones desde la ronda 10 de Between (memoria `antes-y-despues-en-html`).

⚠️ Los 21 scripts viejos NO se migraron y no hay que migrarlos: son entregables
que ya se mandaron y funcionan. El molde es para las rondas nuevas.
"""
from __future__ import annotations

import base64
import io
import pathlib

from PIL import Image

from _entorno import RAIZ  # trae además el arreglo de la consola de Windows

Image.MAX_IMAGE_PIXELS = None

# ──────────────────────────────────────────────────────────────────────────────
# Temas — los colores salen del kit de cada marca, no de la intuición
# ──────────────────────────────────────────────────────────────────────────────
#: Cada tema es sólo la paleta de la PÁGINA (el papel sobre el que Eli mira), no
#: la de la pieza. Se toma de la marca para que la revisión se sienta del cliente
#: que se está revisando, que es como venían las páginas sueltas.
#:
#: El café y el beige de Between salen de `src/brand/hilton-between.ts`
#: (#675b49, #fff9eb); los azules y el verde de DT, de `scripts/_revision.css`,
#: que a su vez salió de la página de la ronda 4 del estático de Honors; el
#: fucsia de Piso18, de `src/brand/piso18.ts` (#D4145A, el medido sobre los JPG
#: aprobados, no el del PNG); el verde de QB, del degradado del botón.
TEMAS = {
    "between": dict(
        acento="#675B49", sobre_acento="#FFF9EB",
        papel="#F3F0EA", superficie="#FFFFFF", tinta="#2A231B", tinta2="#6C6252",
        linea="#E0D9CD", ok="#4F7A3A", ojo="#A8571E",
        papel_o="#14110D", superficie_o="#1D1913", tinta_o="#F0EAE0",
        tinta2_o="#A79C8A", linea_o="#332C22", ok_o="#9CC47F", ojo_o="#E0A263",
        enlace_o="#D9C7A8",
    ),
    "dt": dict(
        acento="#09194E", sobre_acento="#FFFFFF",
        papel="#F1F2F6", superficie="#FFFFFF", tinta="#111A33", tinta2="#5C6480",
        linea="#D6D9E3", ok="#6F9418", ojo="#8A6516",
        papel_o="#0A0E1C", superficie_o="#141A2E", tinta_o="#E8EBF5",
        tinta2_o="#9AA3BF", linea_o="#262D45", ok_o="#A3CD39", ojo_o="#E0AE4A",
        enlace_o="#9FB4EC",
    ),
    "piso18": dict(
        acento="#D4145A", sobre_acento="#FFFFFF",
        papel="#F7F5F2", superficie="#FFFFFF", tinta="#1A1A1A", tinta2="#6B6560",
        linea="#E6DACA", ok="#4F7A3A", ojo="#A8571E",
        papel_o="#141211", superficie_o="#1E1B19", tinta_o="#F0ECE6",
        tinta2_o="#A69E94", linea_o="#332C24", ok_o="#9CC47F", ojo_o="#E0A263",
        enlace_o="#FF8FB4",
    ),
    "qb": dict(
        acento="#354A3A", sobre_acento="#FFFFFF",
        papel="#F2F3F0", superficie="#FFFFFF", tinta="#1C221C", tinta2="#5E665E",
        linea="#DCE0DA", ok="#4F7A3A", ojo="#A8571E",
        papel_o="#101310", superficie_o="#191D19", tinta_o="#ECEFE9",
        tinta2_o="#9AA396", linea_o="#2A302A", ok_o="#9CC47F", ojo_o="#E0A263",
        enlace_o="#A9C4A6",
    ),
    "generico": dict(
        acento="#3A3A3A", sobre_acento="#FFFFFF",
        papel="#F4F4F5", superficie="#FFFFFF", tinta="#1B1B1D", tinta2="#63636A",
        linea="#DEDEE2", ok="#4F7A3A", ojo="#A8571E",
        papel_o="#121213", superficie_o="#1B1B1D", tinta_o="#ECECEF",
        tinta2_o="#9C9CA4", linea_o="#2C2C30", ok_o="#9CC47F", ojo_o="#E0A263",
        enlace_o="#C7C7CF",
    ),
}

#: La tipografía es la misma en todos los temas: la página es el SOPORTE donde se
#: mira la pieza, no la pieza. Si la revisión usara la tipografía de la marca,
#: competiría con lo que se está revisando.
SANS = "'Helvetica Neue',Arial,sans-serif"

_HOJA = """
:root{
  --acento:%(acento)s; --sobre-acento:%(sobre_acento)s;
  --papel:%(papel)s; --superficie:%(superficie)s; --tinta:%(tinta)s; --tinta2:%(tinta2)s;
  --linea:%(linea)s; --ok:%(ok)s; --ojo:%(ojo)s;
  --sombra:0 1px 2px rgba(0,0,0,.06), 0 10px 30px rgba(0,0,0,.07);
  --sans:%(sans)s;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){ %(oscuro)s } }
:root[data-theme="dark"]{ %(oscuro)s }
*{box-sizing:border-box}
body{margin:0;background:var(--papel);color:var(--tinta);font-family:var(--sans);
     line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:48px 16px 96px}
header h1{font-size:clamp(28px,4.4vw,44px);line-height:1.1;margin:0 0 8px;letter-spacing:-.02em}
header p.sub{margin:0;color:var(--tinta2);font-size:17px}
.tag{display:inline-block;background:var(--acento);color:var(--sobre-acento);font-size:12px;
     letter-spacing:.16em;text-indent:.16em;padding:7px 14px;border-radius:999px;
     font-weight:800;margin-bottom:18px}
section{background:var(--superficie);border:1px solid var(--linea);border-radius:18px;
        padding:28px;margin-top:34px;box-shadow:var(--sombra)}
section h2{font-size:clamp(20px,2.6vw,28px);margin:0 0 6px;letter-spacing:-.01em}
section .que{color:var(--tinta2);margin:0 0 22px;font-size:16px}
blockquote{margin:0 0 22px;padding:12px 18px;border-left:3px solid var(--acento);
           background:color-mix(in srgb, var(--acento) 8%%, transparent);
           border-radius:0 10px 10px 0;color:var(--tinta);font-size:16px}
blockquote small{display:block;color:var(--tinta2);margin-top:6px;font-size:13px}
.rejilla{display:grid;gap:20px;align-items:start;
         grid-template-columns:repeat(auto-fit,minmax(min(300px,100%%),1fr))}
.rejilla.tres{grid-template-columns:repeat(auto-fit,minmax(min(250px,100%%),1fr))}
figure{margin:0}
figure img{width:100%%;display:block;border-radius:12px;border:1px solid var(--linea)}
figcaption{margin-top:9px;font-size:13.5px;color:var(--tinta2)}
figcaption b{color:var(--tinta)}
.falta{padding:40px;border:1px dashed var(--linea);border-radius:12px;color:var(--ojo);
       text-align:center;font-size:14px}
.notas{margin:24px 0 0;padding:18px 20px;
       background:color-mix(in srgb, var(--acento) 7%%, transparent);border-radius:12px}
.notas h3{margin:0 0 10px;font-size:13px;letter-spacing:.14em;text-indent:.14em;
          text-transform:uppercase;color:var(--tinta2)}
.notas ul{margin:0;padding-left:20px}
.notas li{margin:7px 0;font-size:15px}
.notas li b{color:var(--tinta)}
.elige{border:2px solid var(--acento);
       background:color-mix(in srgb, var(--acento) 9%%, var(--superficie))}
table{width:100%%;border-collapse:collapse;margin-top:12px;font-size:14.5px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--linea)}
th{color:var(--tinta2);font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:.06em}
td.n{font-variant-numeric:tabular-nums}
.ok{color:var(--ok);font-weight:700}
.ojo{color:var(--ojo);font-weight:700}
code{background:color-mix(in srgb, var(--acento) 12%%, transparent);padding:1px 6px;
     border-radius:5px;font-size:.92em}
a{color:var(--acento)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) a{color:%(enlace_o)s}}
:root[data-theme="dark"] a{color:%(enlace_o)s}
footer{margin-top:40px;color:var(--tinta2);font-size:14px}
@media (max-width:640px){ .wrap{padding:32px 16px 72px} section{padding:20px} }
"""

_OSCURO = ("--papel:%(papel_o)s; --superficie:%(superficie_o)s; --tinta:%(tinta_o)s;"
           " --tinta2:%(tinta2_o)s; --linea:%(linea_o)s; --ok:%(ok_o)s; --ojo:%(ojo_o)s;"
           " --sombra:0 1px 2px rgba(0,0,0,.45), 0 10px 30px rgba(0,0,0,.3);")


def _css(t: dict) -> str:
    """La hoja, con los tokens de la marca puestos.

    Claro y oscuro: se definen en `:root`, se redefinen bajo el esquema del
    sistema —protegido con `:not([data-theme="light"])`— y otra vez para
    `[data-theme="dark"]`, que es como se comporta el visor de artefactos.
    """
    return _HOJA % dict(t, sans=SANS, oscuro=_OSCURO % t)


# ──────────────────────────────────────────────────────────────────────────────
# Imágenes — incrustadas, para que la página sea UN archivo
# ──────────────────────────────────────────────────────────────────────────────
def _data(im: Image.Image, calidad: int = 86) -> str:
    b = io.BytesIO()
    im.save(b, "JPEG", quality=calidad, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def _abrir(ruta) -> Image.Image | None:
    p = pathlib.Path(ruta)
    if not p.is_absolute():
        p = RAIZ / p
    return Image.open(p).convert("RGB") if p.is_file() else None


def img(ruta, ancho: int = 880, calidad: int = 86) -> str | None:
    """La lámina completa, reducida al ancho con que se va a mirar."""
    im = _abrir(ruta)
    if im is None:
        return None
    if im.width > ancho:
        im = im.resize((ancho, round(ancho * im.height / im.width)), Image.LANCZOS)
    return _data(im, calidad)


def recorte(ruta, caja, escala: float = 1.6, calidad: int = 90,
            lienzo: int = 1080) -> str | None:
    """Un detalle ampliado.

    `caja` va en coordenadas del lienzo de diseño (1080 por omisión), no del
    archivo: así el mismo recorte sirve para el render de trabajo y para la
    entrega a 2250 px. Con `lienzo=0` se toma como píxeles del archivo, que es
    lo que hace falta cuando el recorte es sobre una referencia del cliente,
    que no mide 1080.
    """
    im = _abrir(ruta)
    if im is None:
        return None
    k = im.width / lienzo if lienzo else 1
    x0, y0, x1, y1 = [round(v * k) for v in caja]
    im = im.crop((x0, y0, x1, y1))
    if escala != 1:
        im = im.resize((round((x1 - x0) * escala), round((y1 - y0) * escala)), Image.LANCZOS)
    if im.width > 900:
        im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
    return _data(im, calidad)


def _falta(ruta) -> str:
    return '<figure class="falta"><div>falta <code>%s</code></div></figure>' % ruta


def lam(ruta, pie: str, ancho: int = 880) -> str:
    """Una lámina con su pie. Si el archivo no está, lo dice en vez de reventar."""
    d = img(ruta, ancho)
    return (_falta(ruta) if not d else
            '<figure><img src="%s" alt=""><figcaption>%s</figcaption></figure>' % (d, pie))


def det(ruta, caja, pie: str, escala: float = 1.6, lienzo: int = 1080) -> str:
    """Un detalle ampliado con su pie."""
    d = recorte(ruta, caja, escala, lienzo=lienzo)
    return (_falta(ruta) if not d else
            '<figure><img src="%s" alt=""><figcaption>%s</figcaption></figure>' % (d, pie))


# ──────────────────────────────────────────────────────────────────────────────
# La página
# ──────────────────────────────────────────────────────────────────────────────
class Pagina:
    """Una revisión. Se le van agregando secciones y al final se escribe.

    `marca` elige el tema (`between`, `dt`, `piso18`, `qb` o `generico`).
    `salida` es la ruta del HTML, relativa a la raíz del repo.
    `origen` es el script que la generó, y sale en el pie: sin eso, la ronda
    siguiente no sabe de dónde salió la página que está corrigiendo.
    """

    def __init__(self, marca: str, rotulo: str, titulo: str, sub: str, salida: str,
                 origen: str | None = None):
        self.tema = TEMAS.get(marca, TEMAS["generico"])
        self.rotulo, self.titulo, self.sub = rotulo, titulo, sub
        self.salida = RAIZ / salida
        self.origen = origen
        self.partes: list[str] = []

    # ── secciones ────────────────────────────────────────────────────────────
    def pedido(self, cita: str, quien: str, fecha: str, que: str | None = None,
               titulo: str = "Lo que pediste"):
        """Lo que pidió la diseñadora, en sus palabras.

        Va primero y va VERBATIM: la página tiene que poder leerse como respuesta
        a algo concreto, no como una entrega suelta. Es la misma disciplina que
        el motor de QA le exige a una regla — sin cita, es una opinión.
        """
        self.partes.append(
            '<section><h2>%s</h2><blockquote>«%s»<small>%s · %s</small></blockquote>%s</section>'
            % (titulo, cita, quien, fecha,
               '<p class="que">%s</p>' % que if que else ""))

    def comparar(self, antes: tuple, ahora: tuple, titulo: str = "Antes y ahora",
                 que: str | None = None, detalle: tuple | None = None,
                 ancho: int = 420, escala: float = 1.5, elige: bool = False,
                 lienzo: int = 1080, notas: tuple | None = None):
        """El par antes/después, y opcionalmente el mismo par recortado al detalle.

        `antes` y `ahora` son `(ruta, pie)`. `detalle` es la caja que se amplía
        en las DOS, que es lo que hace visible un cambio de 4 px — mirar la
        lámina entera no lo muestra.
        """
        fils = ['<div class="rejilla">%s%s</div>'
                % (lam(antes[0], "<b>ANTES</b> — " + antes[1], ancho),
                   lam(ahora[0], "<b>AHORA</b> — " + ahora[1], ancho))]
        if detalle:
            fils.append('<div class="rejilla" style="margin-top:22px">%s%s</div>'
                        % (det(antes[0], detalle, "<b>ANTES</b>", escala, lienzo),
                           det(ahora[0], detalle, "<b>AHORA</b>", escala, lienzo)))
        self._seccion(titulo, que, "".join(fils), notas, elige)

    def opciones(self, items, titulo: str = "Las opciones", que: str | None = None,
                 ancho: int = 420, elige: bool = True, notas: tuple | None = None):
        """Varias alternativas lado a lado, para elegir una.

        `items` son `(ruta, pie)`. Con tres o más se aprieta la rejilla, que es
        como se mandaron las tres versiones del titular del concurso.
        """
        clase = "rejilla tres" if len(items) > 2 else "rejilla"
        cuerpo = '<div class="%s">%s</div>' % (
            clase, "".join(lam(r, p, ancho) for r, p in items))
        self._seccion(titulo, que, cuerpo, notas, elige)

    def laminas(self, items, titulo: str = "El carrusel completo",
                que: str | None = None, ancho: int = 420, notas: tuple | None = None):
        """Las láminas tal como se publican. Mismo molde que `opciones`, sin marco."""
        self.opciones(items, titulo, que, ancho, elige=False, notas=notas)

    def medido(self, filas, titulo: str = "Lo medido en la lámina final",
               que: str | None = None):
        """La tabla de controles.

        Cada fila es `(control, valor, estado, vara)`. `estado` es `"ok"`,
        `"ojo"` o `""`. Existe porque un número sin su vara no dice nada: 4,14:1
        sólo significa algo al lado de lo que daba antes.
        """
        tr = "".join(
            '<tr><td>%s</td><td class="n %s">%s</td><td>%s</td></tr>'
            % (c, e or "", v, vara) for c, v, e, vara in filas)
        self._seccion(titulo, que,
                      "<table><tr><th>Control</th><th>Valor</th><th>Vara</th></tr>%s</table>"
                      % tr)

    def notas(self, items, titulo: str = "Notas"):
        """Una sección que es sólo notas, sin imagen."""
        self.partes.append("<section>%s</section>" % self._notas((titulo, items)))

    def bruto(self, html: str):
        """Una sección a mano, para lo que el molde no cubra."""
        self.partes.append(html)

    # ── armado ───────────────────────────────────────────────────────────────
    def _notas(self, notas) -> str:
        if not notas:
            return ""
        titulo, items = notas
        return ('<div class="notas"><h3>%s</h3><ul>%s</ul></div>'
                % (titulo, "".join("<li>%s</li>" % i for i in items)))

    def _seccion(self, titulo, que, cuerpo, notas=None, elige=False):
        self.partes.append(
            '<section%s><h2>%s</h2>%s%s%s</section>'
            % (' class="elige"' if elige else "", titulo,
               '<p class="que">%s</p>' % que if que else "",
               cuerpo, self._notas(notas)))

    def _cuerpo(self) -> str:
        pie = ("Página generada por <code>%s</code>." % self.origen) if self.origen else ""
        return ("<title>%s</title>\n<style>%s</style>\n"
                '<div class="wrap">\n<header>\n  <div class="tag">%s</div>\n'
                '  <h1>%s</h1>\n  <p class="sub">%s</p>\n</header>\n%s\n'
                "<footer>%s</footer>\n</div>"
                % (self.titulo, _css(self.tema), self.rotulo, self.titulo, self.sub,
                   "".join(self.partes), pie))

    def escribir(self) -> pathlib.Path:
        """Deja el archivo local y, al lado, la versión para publicar como artefacto."""
        cuerpo = self._cuerpo()
        titulo, resto = cuerpo.split("\n", 1)
        self.salida.parent.mkdir(parents=True, exist_ok=True)
        self.salida.write_text(
            '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            + titulo + "\n</head>\n<body>\n" + resto + "\n</body>\n</html>",
            encoding="utf-8")
        art = self.salida.with_name(self.salida.stem + "-artefacto.html")
        art.write_text(cuerpo, encoding="utf-8")
        print("ok local:     %s (%d KB)" % (self.salida, self.salida.stat().st_size // 1024))
        print("ok artefacto: %s (%d KB)" % (art, art.stat().st_size // 1024))
        if self.salida.stat().st_size > 16 * 1024 * 1024:
            print("⚠️  pasa los 16 MB: baja el `ancho` o la `calidad` antes de publicarla")
        return self.salida

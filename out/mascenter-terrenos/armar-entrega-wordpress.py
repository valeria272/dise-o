# -*- coding: utf-8 -*-
"""Arma ENTREGA-WORDPRESS para la landing de terrenos de Más Center."""
import io, os, re, shutil, pathlib

BASE = pathlib.Path("/Users/Vale/Desktop/COPYLAB PROJECTS/EDITOR VIDEOS/out/mascenter-terrenos")
DEST = BASE / "ENTREGA-WORDPRESS"
SEC  = DEST / "secciones"
REC  = DEST / "recursos"

# ⚠️ Estos tres se escriben a mano y el script NO los regenera: si se borran con
# el rmtree, la entrega sale sin instructivo. Se guardan y se reponen.
# (Pasó el 09-09-2026 al rehacer el paquete.)
A_MANO = ("INSTRUCTIVO.html", "LEEME.txt", "TEXTOS-PARA-COPIAR.txt")
# Las capturas de secciones/vista-previa/ tampoco las genera el script: son
# fotos de cada bloque, y el LEEME las promete. Se guardan igual que las de arriba.
_guardados, _vistas = {}, {}
if DEST.exists():
    for _n in A_MANO:
        if (DEST / _n).exists():
            _guardados[_n] = (DEST / _n).read_bytes()
    for _f in (SEC / "vista-previa").glob("*"):
        if _f.is_file():
            _vistas[_f.name] = _f.read_bytes()
    shutil.rmtree(DEST)
for d in (SEC, SEC/"vista-previa", REC/"tipografias", REC/"logos",
          REC/"imagenes", REC/"imagenes"/"centros"):
    d.mkdir(parents=True, exist_ok=True)

# ── recursos ──────────────────────────────────────────────────────────
for f in (BASE/"assets"/"fonts").glob("*.woff2"):
    shutil.copy2(f, REC/"tipografias"/f.name)
for n in ("logo-mascenter-blanco.svg", "logo-ifb.png", "favicon.png"):
    shutil.copy2(BASE/"assets"/"img"/n, REC/"logos"/n)
for n in ("terreno-hero.jpg", "aerea-2.jpg"):
    shutil.copy2(BASE/"assets"/"img"/n, REC/"imagenes"/n)
for f in (BASE/"assets"/"img"/"centros").glob("*.jpg"):
    shutil.copy2(f, REC/"imagenes"/"centros"/f.name)

src = io.open(BASE/"index.html", encoding="utf-8").read()

def repaths(t, pre):
    """assets/... → <pre>recursos/... y saca los ?v=N"""
    t = t.replace("assets/fonts/",        pre+"recursos/tipografias/")
    t = t.replace("assets/img/centros/",  pre+"recursos/imagenes/centros/")
    for n in ("logo-mascenter-blanco.svg", "logo-ifb.png", "favicon.png"):
        t = t.replace("assets/img/"+n, pre+"recursos/logos/"+n)
    t = t.replace("assets/img/",          pre+"recursos/imagenes/")
    t = re.sub(r"\.jpg\?v=\d+", ".jpg", t)
    return t

# ── sitio-completo.html ───────────────────────────────────────────────
io.open(DEST/"sitio-completo.html", "w", encoding="utf-8").write(repaths(src, ""))

# ── troceo por marcadores ─────────────────────────────────────────────
# ⚠️ Antes esto cortaba por números de línea quemados —tramo(263, 292)— y
# cualquier edición al CSS o al HTML de una sección corría todas las de abajo:
# la entrega salía con bloques mezclados y sin ningún error. Ahora cada bloque
# se ubica por su propio rótulo (09-09-2026 el JS, 10-09-2026 el resto).
L = src.split("\n")                      # L[0] == línea 1

def linea(patron, desde=0):
    """1ª línea (1-indexada) que empieza con `patron`."""
    for i in range(desde, len(L)):
        if L[i].startswith(patron):
            return i + 1
    raise SystemExit("✗ No encontré el rótulo %r en index.html — no puedo trocear." % patron)

def tramo(a, b):                         # 1-indexado, inclusivo
    return "\n".join(L[a-1:b]).rstrip()

def bloques(rotulos, primero, ultimo):
    """rotulos: [(clave, rótulo)] en el ORDEN del archivo. Cada bloque termina
    donde empieza el siguiente; el último, en `ultimo`."""
    partidas = [primero] + [linea(r) for _, r in rotulos[1:]]
    out = {}
    for i, (clave, _) in enumerate(rotulos):
        fin = (partidas[i+1] - 1) if i+1 < len(partidas) else ultimo
        out[clave] = tramo(partidas[i], fin)
        if not out[clave].strip():
            raise SystemExit("✗ El bloque %r salió vacío — revisa los rótulos." % clave)
    return out

CSS = bloques([
    ("base",       None),
    ("cabecera",   "/* ── CABECERA ──"),
    ("hero",       "/* ── HERO ──"),
    ("titulos",    "/* ── TÍTULOS DE SECCIÓN ──"),
    ("intro",      "/* ── INTRO ──"),
    ("buscamos",   "/* ── QUÉ BUSCAMOS ──"),
    ("valor",      "/* ── VALOR / CIFRAS ──"),
    ("centros",    "/* ── CENTROS EN OPERACIÓN ──"),
    ("variables",  "/* ── MÁS QUE UN TERRENO"),
    ("proceso",    "/* ── PASO A PASO"),
    ("formulario", "/* ── FORMULARIO ──"),
    ("pie",        "/* ── PIE ──"),
    ("flotante",   "/* ── BOTÓN FLOTANTE ──"),
    ("responsive", "/* ── RESPONSIVE ──"),
], primero=linea("<style>") + 1, ultimo=linea("</style>") - 1)

_flot = linea('<a href="#contacto" class="flotante"')
HTML = bloques([
    ("cabecera",   None),
    ("hero",       "<!-- ════════════ HERO ═"),
    ("intro",      "<!-- ════════════ INTRO ═"),
    ("buscamos",   "<!-- ════════════ QUÉ BUSCAMOS ═"),
    ("valor",      "<!-- ════════════ EL VALOR DE MÁS CENTER ═"),
    ("centros",    "<!-- ════════════ CENTROS EN OPERACIÓN ═"),
    ("variables",  "<!-- ════════════ MÁS QUE UN TERRENO ═"),
    ("proceso",    "<!-- ════════════ PASO A PASO ═"),
    ("formulario", "<!-- ════════════ FORMULARIO ═"),
    ("pie",        "<!-- ════════════ PIE ═"),
], primero=linea("<!-- ════════════ CABECERA ═"), ultimo=_flot - 1)
HTML["flotante"] = tramo(_flot, linea("</a>", _flot))

for clave, txt in HTML.items():
    if not txt.lstrip().startswith("<"):
        raise SystemExit("✗ El bloque HTML %r no empieza con una etiqueta." % clave)
for clave, txt in CSS.items():
    if "<" in txt:
        raise SystemExit("✗ El bloque CSS %r trae HTML adentro — los rótulos se corrieron." % clave)

# ⚠️ El bloque <script> se localiza SOLO, no por número de línea fija.
# Estaba quemado como tramo(776, 927) y al crecer el JS la entrega salió con el
# JavaScript cortado a la mitad, sin aviso (09-09-2026). Los demás tramos van
# antes del <script>, así que a esos no los mueve editar el JS.
_ini = next(i for i, l in enumerate(L) if l.strip() == "<script>")
_fin = next(i for i, l in enumerate(L) if l.strip() == "</script>")
SCRIPTS = "\n".join(L[_ini:_fin + 1]).rstrip()
if not SCRIPTS.rstrip().endswith("</script>") or "})();" not in SCRIPTS:
    raise SystemExit("✗ El bloque <script> salió incompleto — la entrega quedaría rota. "
                     "Revisa index.html antes de seguir.")

RAYA = "════════════════════════════════════════════════════════════════════════"
def cabecera_archivo(num, titulo, previa, usa, nota, cierre):
    lin = ["<!-- " + RAYA,
           "     SECCIÓN %s — %s" % (num, titulo),
           "     " + "─"*68]
    if previa:
        lin.append("     Vista previa:  vista-previa/%s-*.jpg" % num)
    if usa:
        lin.append("     Archivos que usa:")
        lin += ["       · " + u for u in usa]
    if nota:
        lin.append("     Nota: " + nota)
    lin.append("     " + "═"*68)
    lin += ["     " + c for c in cierre]
    lin.append("     " + RAYA + " -->")
    return "\n".join(lin)

PEGA = ["Pega TODO este archivo dentro de un bloque «HTML personalizado».",
        "Antes tiene que estar pegado UNA sola vez 00-estilos-base.html."]

fuentes = ["recursos/tipografias/poppins-%s.woff2" % p
           for p in ("light","regular","medium","semibold","bold")]

# ── 00 estilos base ───────────────────────────────────────────────────
c00 = cabecera_archivo(
    "00", "ESTILOS BASE (VA UNA SOLA VEZ)", False, fuentes,
    "Tipografía Poppins, la paleta de Más Center, el contenedor, los botones, los "
    "títulos de sección, las animaciones de entrada y TODO el responsive. Sin esto, "
    "las demás secciones se ven mal.",
    ["Va PRIMERO, antes de cualquier sección. Se pega una sola vez.",
     "Puede ir en un bloque «HTML personalizado» al inicio de la página,",
     "o en Apariencia → Personalizar → CSS adicional (sin las etiquetas <style>).",
     "Si el tema ya carga Poppins en los 5 pesos, se puede borrar el bloque @font-face."])
cuerpo00 = "\n\n".join([CSS["base"],
                        "/* ── TÍTULOS DE SECCIÓN ───────────────────────────────────────── */\n"
                        + CSS["titulos"].split("\n",1)[1] if CSS["titulos"].startswith("/*") else CSS["titulos"],
                        CSS["responsive"]])
io.open(SEC/"00-estilos-base.html","w",encoding="utf-8").write(
    c00 + "\n<style>\n" + repaths(cuerpo00, "../") + "\n</style>\n")

# ── secciones ─────────────────────────────────────────────────────────
CENTROS = sorted(p.name for p in (REC/"imagenes"/"centros").glob("*.jpg"))
SECCIONES = [
 ("01","cabecera","CABECERA FIJA (MENÚ)",
  ["recursos/logos/logo-mascenter-blanco.svg"],
  "Barra transparente sobre la foto que se vuelve oscura al bajar. Si el tema de "
  "WordPress ya tiene su propio menú, se puede usar ese y saltarse esta sección."),
 ("02","hero","PORTADA — «Postula tu terreno»",
  ["recursos/imagenes/terreno-hero.jpg"],
  "La foto de fondo tiene un movimiento leve al hacer scroll (parallax). El botón "
  "rojo baja al formulario."),
 ("03","intro","INTRO — quiénes somos y qué buscamos",
  ["recursos/imagenes/aerea-2.jpg"], "Texto a la izquierda, foto aérea a la derecha."),
 ("04","buscamos","QUÉ BUSCAMOS — las condiciones del terreno",
  [], "Las tarjetas con superficie, ubicación, accesos y uso de suelo."),
 ("05","valor","NUESTRO RESPALDO — las cifras",
  [], "Los números suben solos cuando la sección aparece en pantalla."),
 ("06","centros","CENTROS EN OPERACIÓN — el carrusel",
  ["recursos/imagenes/centros/ (%d fotos)" % len(CENTROS)],
  "Carrusel con los 23 centros. Se arrastra con el mouse y con el dedo; las flechas "
  "y los puntos también funcionan."),
 ("07","variables","MÁS QUE UN TERRENO — las variables que evaluamos",
  [], "Listado de lo que mira el equipo de desarrollo antes de decidir."),
 ("08","proceso","CÓMO POSTULAR — el paso a paso",
  [], "Los 4 pasos del proceso de evaluación."),
 ("09","formulario","CONVERSEMOS — datos de contacto y formulario",
  [], "ACÁ ESTÁ EL CORREO terrenos@ifbinversiones.cl. El formulario valida los campos "
      "—incluidos los adjuntos: tipo y peso— pero todavía NO envía correo ni sube el "
      "archivo: hay que conectarlo a Contact Form 7 (paso 7 del instructivo)."),
 ("10","pie","PIE DE PÁGINA",
  ["recursos/logos/logo-mascenter-blanco.svg","recursos/logos/logo-ifb.png"],
  "Incluye la barra de copyright, con el año que se pone solo."),
 ("11","flotante","BOTÓN FLOTANTE «Postula tu terreno»",
  [], "Aparece al bajar y acompaña al visitante hasta el formulario. Va al final del "
      "cuerpo de la página, después del pie."),
]
for num, clave, titulo, usa, nota in SECCIONES:
    txt = cabecera_archivo(num, titulo, True, usa, nota, PEGA)
    txt += "\n<style>\n" + repaths(CSS[clave], "../") + "\n</style>\n\n"
    txt += repaths(HTML[clave], "../") + "\n"
    io.open(SEC/("%s-%s.html" % (num, clave)),"w",encoding="utf-8").write(txt)

# ── 99 scripts ────────────────────────────────────────────────────────
c99 = cabecera_archivo(
    "99","SCRIPTS (VA UNA SOLA VEZ, AL FINAL)", False, [],
    "Hace funcionar: las apariciones al hacer scroll, la cabecera que se oscurece, el "
    "menú de celular, el parallax de la portada, los contadores, el carrusel de centros "
    "y la validación del formulario.",
    ["Va ÚLTIMO, después de todas las secciones, en su propio bloque «HTML personalizado».",
     "Se pega una sola vez. No usa jQuery ni ninguna librería externa."])
io.open(SEC/"99-scripts.html","w",encoding="utf-8").write(c99 + "\n" + SCRIPTS + "\n")

print("OK — secciones:", len(list(SEC.glob('*.html'))))
print("centros:", len(CENTROS))

# ── reponer lo que se escribe a mano ──────────────────────────────────
for _n, _b in _guardados.items():
    (DEST / _n).write_bytes(_b)
for _n, _b in _vistas.items():
    (SEC / "vista-previa" / _n).write_bytes(_b)
if _vistas:
    print("vistas previas repuestas:", len(_vistas))
else:
    print("⚠️ OJO: la entrega quedó SIN las capturas de secciones/vista-previa/.")
if _guardados:
    print("repuestos a mano:", ", ".join(sorted(_guardados)))
else:
    print("⚠️ OJO: no había INSTRUCTIVO.html / LEEME.txt / TEXTOS-PARA-COPIAR.txt "
          "que reponer — la entrega queda incompleta hasta escribirlos.")

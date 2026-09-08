# -*- coding: utf-8 -*-
"""Arma ENTREGA-WORDPRESS para la landing de terrenos de Más Center."""
import io, os, re, shutil, pathlib

BASE = pathlib.Path("/Users/Vale/Desktop/COPYLAB PROJECTS/EDITOR VIDEOS/out/mascenter-terrenos")
DEST = BASE / "ENTREGA-WORDPRESS"
SEC  = DEST / "secciones"
REC  = DEST / "recursos"

if DEST.exists():
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

# ── troceo por líneas ─────────────────────────────────────────────────
L = src.split("\n")                      # L[0] == línea 1
def tramo(a, b):                         # 1-indexado, inclusivo
    return "\n".join(L[a-1:b]).rstrip()

CSS = {
    "base":       tramo(15, 69),
    "titulos":    tramo(139, 147),
    "responsive": tramo(319, 346),
    "cabecera":   tramo(70, 92),
    "hero":       tramo(93, 138),
    "intro":      tramo(148, 157),
    "buscamos":   tramo(158, 175),
    "valor":      tramo(176, 194),
    "centros":    tramo(195, 220),
    "variables":  tramo(221, 240),
    "proceso":    tramo(241, 262),
    "formulario": tramo(263, 292),
    "pie":        tramo(293, 308),
    "flotante":   tramo(309, 318),
}
HTML = {
    "cabecera":   tramo(351, 368),
    "hero":       tramo(370, 396),
    "intro":      tramo(398, 424),
    "buscamos":   tramo(426, 468),
    "valor":      tramo(470, 501),
    "centros":    tramo(503, 553),
    "variables":  tramo(555, 603),
    "proceso":    tramo(605, 650),
    "formulario": tramo(652, 734),
    "pie":        tramo(736, 769),
    "flotante":   tramo(771, 774),
}
SCRIPTS = tramo(776, 927)

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
      "pero todavía NO envía correo: hay que conectarlo a Contact Form 7 (paso 8 del "
      "instructivo)."),
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

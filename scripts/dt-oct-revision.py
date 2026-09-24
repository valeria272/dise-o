#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · OCTUBRE 2026 — página de revisión de la ronda 1 (las 3 historias).

Uso:  python scripts/dt-oct-revision.py
"""
import base64
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina, RAIZ  # noqa: E402

E = "out/hilton/dt/entrega-oct"
R = "out/hilton/dt/oct-revision"
REF = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None  # carpeta de refs

p = Pagina("dt", "DOUBLETREE · OCTUBRE 2026 · RONDA 3",
           "Octubre DT, ronda 3 — las cuatro piezas",
           "24-09-2026 · 3 historias + el feed de la opinión",
           f"{R}/index.html", origen="scripts/dt-oct-revision.py")
REF = pathlib.Path("raw/hilton/dt/ref-oct")

p.pedido("Se trata de ver alguna familia… lo único que no me gusta es la transición de oscuro a color. "
         "Servicios está ok. En la ST del 30-10 me gustaría que todo fuera centrado… o hacer una guía, "
         "unas líneas, de las que ya hemos tenido antes. Feed: diseña, avanza con eso. "
         "Guíate bien de las referencias dejadas", "Eli", "24-09")

# ── Family Time ──
import _revision as rv
video = base64.b64encode((RAIZ / R / "ft-preview.mp4").read_bytes()).decode()
p.bruto(
    '<section class="elige"><h2>ST 01-10 · Family Time (animada, 15 s)</h2>'
    '<p class="que">Ahora sí calcado de la referencia: la foto se ve sola, entra el cristal <b>alto</b> '
    'con esmerilado claro y el texto se escribe arriba; <b>barridos con desenfoque</b> encadenan tomas '
    'cortas (familia, familia de cerca, habitación, desayuno) y cierra el cristal con el programa, que ahora queda <b>~6,7 s</b> en pantalla (antes ~4). '
    '<b>Sin el paso de gris a color.</b> La familia es tu foto de septiembre, en la misma habitación, '
    'con cuatro rostros nuevos (Seedream 5 Pro).</p>'
    '<div class="rejilla"><figure><video src="data:video/mp4;base64,%s" autoplay loop muted playsinline '
    'controls style="width:100%%;border-radius:10px"></video><figcaption><b>AHORA</b> — vista previa; '
    'máster 1080×1920</figcaption></figure>%s</div></section>'
    % (video, rv.lam(REF / "ft-familytime.jpg", "<b>REFERENCIA</b> — primer cuadro del pin", 420)))
p.laminas([(f"{R}/ft-tira.jpg", "AHORA · f15 familia · f90 se escribe · f150 barrido · f175 familia · f205 habitación · f280 programa · f445 final"),
           (REF / "ft-ref-tira.jpg", "REFERENCIA · el pin a 4 cuadros por segundo")],
          titulo="Family Time · tira contra la referencia", ancho=880)
p.comparar(("out/hilton/dt/oct/_rondas/r1/ft-r1-final.png", "ronda 1, sin familia"),
           (f"{E}/../oct/_pruebas/ft2-f410.png", "ronda 2, último cuadro"),
           titulo="Family Time · el cuadro final")

# ── Honors ──
p.comparar(("out/hilton/dt/oct/_rondas/r1/honors-r1.png", "a la izquierda, como la ref"),
           (f"{E}/DT ST 30-10 Hilton Honors beneficios.png", "centrado + la cruz de líneas de septiembre"),
           titulo="ST 30-10 · Hilton Honors", elige=True,
           que="Titular, beneficios y logo de Hilton Honors centrados, con las líneas guía del estático de "
               "Honors de septiembre: la cruz de divisores (sin la caja) y la regla sobre el logo.")

# ── Opinión ──
p.opciones([(f"{E}/Post n°1 S2 DT.png", "<b>AHORA</b> — la de Google, 2250×2813"),
            (REF / "opinion-expedia-aprobada.png", "<b>LA PLANTILLA</b> — tu opinión de Expedia aprobada")],
           titulo="FEED 10-10 · Opinión (Google)", elige=True,
           que="Calcada de tu opinión de Expedia, medida sobre el PNG: tarjeta clara partida, pestaña azul "
               "con el logo, «Nombre: “cita”», la valoración montada en el corte con la línea que la une, "
               "cuerpo en Stag itálica azul y el logo de la plataforma a color al pie. Por ser Google: su "
               "logo y ESTRELLAS en vez de círculos (mismo verde y contorno).")
# ── Servicios ──
p.laminas([(f"{E}/DT ST 13-10 Servicios del hotel.png", "Aprobada en la ronda 1 — sin cambios")],
          titulo="ST 13-10 · Servicios del hotel", ancho=420)

p.notas([
    "<b>Opinión — el nombre «Silvana Brasil»</b> no viene en el brief: sale de la captura de la reseña, "
    "y la referencia de Tripadvisor firmaba con el nombre. Si prefieres sin nombre o sólo «Silvana», se cambia.",
    "<b>Opinión — sin bandera:</b> la de Expedia marcaba el país de Gabriel; de Silvana la reseña no dice el país.",
    "<b>Opinión — foto:</b> el lounge, la más cálida del banco («colores cálidos»). Probé dos habitaciones: una se leía "
    "a Escapada Romántica (champaña y batas) y la otra salía fría.",
    "<b>Opinión — nombre del archivo «Post n°1 S2 DT»</b>: es el único post estático de la S2 (el 07-10 es carrusel).",
    "<b>Honors — los cuatro beneficios</b> siguen siendo los del estático aprobado en septiembre.",
    "<b>Pendiente:</b> el reel Hilton Honors POV del 14-10 sigue sin material grabado.",
], titulo="Lo que tienes que saber")

p.medido([
    ("QA de marca · Honors", "0 bloqueantes", "ok", "qa/motor.py --marca hilton"),
    ("QA de marca · Opinión", "«texto al borde» 11 %", "ojo",
     "falsa alarma: la regla mide texto BLANCO y esta pieza no tiene (va azul); cuenta los brillos de la foto. Tu opinión de Expedia pasa la misma regla"),
    ("Family Time", "15,00 s · 1080×1920 · sin audio", "ok", "tope de 15 s"),
    ("Másteres", "2250×4000 · 2250×2813 · MP4 1080×1920", "ok", "los de la cuenta"),
], titulo="Lo medido")

p.escribir()

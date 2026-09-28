#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · OCTUBRE 2026, segunda tanda — página de revisión de la ronda 1.

Las 6 piezas que pasaron a OK PARA DISEÑO el 28-09, cada una contra su referencia.
Uso:  python scripts/dt-oct2-revision.py
"""
import base64
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _revision as rv  # noqa: E402
from _revision import Pagina, RAIZ  # noqa: E402

E = "out/hilton/dt/entrega-oct2"
R = "out/hilton/dt/oct2-revision"
REF = pathlib.Path("raw/hilton/dt/ref-oct2")

p = Pagina("dt", "DOUBLETREE · OCTUBRE 2026 · SEGUNDA TANDA · RONDA 1",
           "Octubre DT: las 6 piezas nuevas en OK",
           "28-09-2026 · 3 historias de feriado · Coworking animada · Family Time feed · carrusel «5 cosas»",
           f"{R}/index.html", origen="scripts/dt-oct2-revision.py")

p.pedido("Avanza diseñando lo okey para diseñar de la grilla de DT… recuerda guiarte de las referencias "
         "y comentarios de cliente para diseño", "Eli", "28-09")

# ── Feriado ──
p.opciones([(f"{E}/DT ST 05-10 Feriado ER y FT.png", "<b>AHORA</b> — ST 05-10 · ER + FT"),
            (REF / "st-05-10-feriado-er-ft-0.jpg", "<b>REFERENCIA</b> — la de la grilla")],
           titulo="ST 05-10 · Feriado, los dos planes", elige=True,
           que="De la ref se toma el titular centrado con la flecha fina que baja y las <b>tarjetas claras de "
               "resultado</b> con miniatura. La «pantalla dividida» del brief son esas dos tarjetas, una por "
               "programa: la pareja brindando y la familia en el desayuno. Fondo: la fachada real. "
               "La barra de búsqueda de la ref no va, porque pediría un texto que el brief no trae.")
p.opciones([(f"{E}/DT ST 05-10 Feriado Escapada Romantica.png", "<b>AHORA</b> — ST 05-10 · Escapada"),
            (f"{E}/DT ST 05-10 Feriado Family Time.png", "<b>AHORA</b> — ST 05-10 · Family Time"),
            (REF / "st-05-10-feriado-er-y-ft-solas-0.jpg", "<b>REFERENCIA</b> — la misma para las dos")],
           titulo="ST 05-10 · Feriado, Escapada sola y Family Time sola", elige=True,
           que="Panel vertical translúcido a la izquierda con el titular, la lista en <b>píldoras de contorno</b> "
               "y el botón lleno con el correo, como la ref, en azul DT. Escapada: la habitación real "
               "<b>HDT_65</b> con la cubeta, la copa y las batas («copas con espumante junto a la cama»), sin gente. "
               "Family Time: la familia del banco en la habitación de dos camas; el panel baja y se pone a lo "
               "ancho, porque en todas las escenas del banco la familia ocupa el centro y el panel vertical la tapaba.")

# ── Coworking ──
video = base64.b64encode((RAIZ / R / "cw-preview.mp4").read_bytes()).decode()
p.bruto(
    '<section class="elige"><h2>ST 22-10 · Coworking (animada, 15 s)</h2>'
    '<p class="que">La grilla <b>no trae referencia</b> para esta pieza, así que va con el aparato de tu Family '
    'Time del 01-10, que ya está aprobado: la toma se ve sola, entra el cristal alto esmerilado con el titular, '
    'y los barridos encadenan tres tomas reales (el café servido a la mesa con el portátil, que es el clip de '
    '«Tiempo para ti» de «Tu día», y los dos lounges). El bloque final queda <b>~7 s</b> en pantalla. '
    'MP4 1080×1920 + GIF 720×1280.</p>'
    '<div class="rejilla"><figure><video src="data:video/mp4;base64,%s" autoplay loop muted playsinline '
    'controls style="width:100%%;border-radius:10px"></video><figcaption><b>AHORA</b> — vista previa</figcaption>'
    '</figure></div></section>' % video)
p.laminas([(f"{R}/cw-tira.jpg", "un cuadro por segundo, de 0 a 14 s")], titulo="Coworking · la tira", ancho=880)

# ── Family Time feed ──
p.opciones([(f"{E}/Post n°1 S5 DT.png", "<b>AHORA</b> — FEED 28-10"),
            (REF / "fd-28-10-familytime-0.jpg", "<b>REFERENCIA</b>"),
            ("raw/hilton/dt/aprobadas-sept/C1 FT N2.png", "<b>EL BLOQUE</b> — tu C1 FT N2 aprobado")],
           titulo="FEED 28-10 · Family Time", elige=True,
           que="Como la ref: la habitación a sangre y el titular <b>arriba a la derecha</b>, a dos pesos. Es el "
               "título nuevo del comentario. La foto es la guerra de almohadas del banco de la familia. Abajo va el "
               "bloque del programa de tu C1 FT N2. El logo queda en su lugar de plantilla (arriba) y no abajo como "
               "en la ref, porque abajo vive el programa.")

# ── Carrusel ──
p.laminas([(f"{E}/C1 S4 DT n°{n}.png", f"n°{n}") for n in range(1, 8)],
          titulo="FEED 21-10 · Carrusel «5 cosas que hacen especial tu estadía» (7 láminas)", ancho=300)
p.opciones([(f"{E}/C1 S4 DT n°1.png", "<b>AHORA</b> — portada"),
            (REF / "fd-21-10-carrusel-5cosas-a-0.jpg", "<b>REF 1</b>"),
            (REF / "fd-21-10-carrusel-5cosas-b-0.jpg", "<b>REF 2</b>")],
           titulo="Carrusel · la portada contra sus dos referencias",
           que="Las dos refs son portadas: foto con velo, titular serif <b>centrado</b> y la invitación a deslizar. "
               "En DT la flecha es la píldora de tu C1 FT N1. Las interiores no traen ref y siguen «Tu día»: foto "
               "real a sangre, velo que nace en cero y el texto a la izquierda. El logo va sólo en la portada.")

p.notas([
    "<b>Carrusel 21-10: la fila DISEÑOS de la grilla dice «REEL»</b>, pero el brief y el comentario son de un "
    "carrusel de 7 láminas. Diseñé el carrusel. Si contenido lo quiere como reel, se arma con las mismas tomas.",
    "<b>Carrusel · las bajadas van sin punto</b> (regla del cliente, R-60). El «01.» es la numeración del brief y se deja.",
    "<b>Carrusel · hospitalidad:</b> es la escena de check-in con cookie del banco de la familia (la única con "
    "recibimiento, galleta y staff). Todas las demás son fotos reales de la sesión HDT.",
    "<b>Feriado ER + FT · la pareja</b> es IA puesta sobre la habitación real HDT_65 (Nano Banana, el mismo método "
    "del banco de la familia): sonrisa suave y nadie mira a cámara. Es distinta de la familia.",
    "<b>Feriado ER + FT · «(confirmar tarifa vigente)»</b> es nota a contenido: no va en la pieza. Los precios son los "
    "del carrusel vigente ($99.000 y $125.000).",
    "<b>Los stickers</b> (countdown al 10-10, CTA de reservas y del cowork) los pone el CM: se dejó el aire.",
    "<b>Coworking · ubicación:</b> «1er y 2do nivel de la cafetería», literal del brief.",
    "<b>Sin subir a Drive</b>: esperan tu visto bueno. Nombres de entrega: DT ST 05-10 ×3, DT ST 22-10 Coworking "
    "(MP4 + GIF), Post n°1 S5 DT, C1 S4 DT n°1–7.",
    "<b>Sigue pendiente:</b> el reel Hilton Honors POV del 14-10 (sin material grabado). La Escapada del 07-10 "
    "está en REVISAR CONTENIDO y no se tocó.",
], titulo="Lo que tienes que saber")

p.medido([
    ("QA de marca · 4 estáticos", "0 bloqueantes", "ok", "qa/motor.py --marca hilton, con textos declarados"),
    ("QA · ER + FT", "1 aviso: la banda del cielo sin foco", "ojo", "es el cielo real, liso; no hay desenfoque aplicado"),
    ("QA · carrusel", "«Café XL» sin verificar", "ok", "es una regla de Between; no aplica a DT"),
    ("Coworking", "15,00 s · 1080×1920 · GIF 720×1280 a 12,5 fps", "ok", "tope de 15 s (R-25)"),
    ("Másteres", "2250×4000 · 2250×2813", "ok", "los de la cuenta"),
], titulo="Lo medido")

p.escribir()

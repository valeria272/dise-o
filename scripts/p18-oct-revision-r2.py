#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ronda 2: antes/después de lo que Eli pidió cambiar el 28-09.
La ronda 1 quedó copiada en `out/piso18/oct/r1/` antes de volver a rendir.

    python scripts/p18-oct-revision-r2.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

A = "out/piso18/oct/r1/"
E = "out/piso18/oct/entrega/"
R = "raw/hilton/piso18/oct/refs/"

p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 2",
    "Color, cifras, portada del atardecer y Tex-Mex",
    "28-09-2026 · las cinco piezas con cambios; el resto quedó aprobado",
    "out/piso18/oct/revision-r2.html",
    origen="scripts/p18-oct-revision-r2.py",
)
p.pedido(
    "el feed del 6 del 10 necesito que edites un poco el color para que se vea muy similar a la "
    "referencia (…) en vez de ciertos rosados que sean esos tonos como azulitos · para el feed 9 del 10 "
    "(…) los números y la tipografía de Raleway tiene que verse armónica · al carrusel [13-10] la "
    "portada (…) en la ventana se ve como dos tipos de atardeceres · [16-10] si está Raleway recuerda "
    "que el texto se vea mucho más armónico (…) las cositas de archivadora en color fucsia de piso 18 · "
    "el carrusel de Tex-Mex tiene que cambiar las imágenes, que se vean mucho más realistas",
    "Eli", "28-09-2026",
    que="Aprobadas sin cambios: 13-10 S2, 27-10, y las cinco historias.",
)

p.opciones([(R + "fd-06-10-arreglos-0.jpg", "<b>REFERENCIA</b>"),
            (A + "S2/FEED/P18 FEED 06-10 Arreglos florales.png", "<b>ANTES</b>"),
            (E + "S2/FEED/P18 FEED 06-10 Arreglos florales.png", "<b>AHORA</b>")],
           titulo="FEED 06-10 · los rosados pasan a azul empolvado", elige=False, ancho=420,
           notas=("Qué cambió", ["La misma foto: rosas y dalia pasan a azul empolvado, como las hortensias de la ref; "
                                 "hojas rojas, pampas, vela, copas y encuadre quedan iguales."]))

p.comparar((A + "S2/FEED/P18 FEED 09-10 Fechas 2027 2.png", "cifras de estilo antiguo"),
           (E + "S2/FEED/P18 FEED 09-10 Fechas 2027 2.png", "cifras de caja alta"),
           titulo="FEED 09-10 S2 · Raleway y el calendario", detalle=(0, 150, 1080, 640), escala=1,
           notas=("Qué cambió", [
               "Raleway trae por defecto cifras de <b>estilo antiguo</b>: en «2027» el 0 queda chico y el 7 baja de la "
               "línea base. Ahora todas sus cifras son de caja alta (<code>lnum</code>), en toda la grilla de octubre.",
               "Las cifras del calendario pasan a IvyPresto Thin, finas como las de la ref, y ya no pesan más que el titular."]))

p.comparar((A + "S3/FEED/P18 FEED 13-10 Atardecer 1.png", "dos atardeceres"),
           (E + "S3/FEED/P18 FEED 13-10 Atardecer 1.png", "un solo cielo"),
           titulo="FEED 13-10 S1 · la portada",
           notas=("Qué cambió", ["Se volvió a producir la misma sala real con un solo cielo continuo detrás de todos los "
                                 "vidrios, con la luz y la paleta de la S2 aprobada."]))

p.laminas([(A + "S3/FEED/P18 FEED 16-10 Tu proxima celebracion 1.png", "<b>ANTES</b> · S1"),
           (E + "S3/FEED/P18 FEED 16-10 Tu proxima celebracion 1.png", "<b>AHORA</b> · S1")],
          titulo="FEED 16-10 · clips fucsia y jerarquía", ancho=560)
p.comparar((A + "S3/FEED/P18 FEED 16-10 Tu proxima celebracion 1.png", "S1"),
           (E + "S3/FEED/P18 FEED 16-10 Tu proxima celebracion 1.png", "S1"),
           titulo="El clip y la hoja, de cerca", detalle=(240, 370, 840, 920), escala=1.2,
           notas=("Qué cambió", [
               "Los clips pasan al fucsia de Piso18 (#D4145A), con el pliegue más hondo, brillo de metal pintado y alambre plateado.",
               "«EN PISO18» sube de 19 a 24 px: era el tercer nivel de la hoja y no se leía. Con cifras de caja alta el «18» ya no baja.",
               "En la S5 la línea «Cotiza tu evento en piso18.cl» sube de 28 a 34 px."]))
p.laminas([(E + "S3/FEED/P18 FEED 16-10 Tu proxima celebracion %d.png" % n, "<b>AHORA</b> · S%d" % n) for n in range(2, 6)],
          titulo="FEED 16-10 · slides 2 a 5", ancho=420)

p.laminas([(A + "S4/FEED/P18 FEED 23-10 Estacion Tex Mex %d.png" % n, "<b>ANTES</b> · S%d" % n) for n in range(1, 5)],
          titulo="FEED 23-10 · Tex-Mex, ronda 1", ancho=420)
p.laminas([(E + "S4/FEED/P18 FEED 23-10 Estacion Tex Mex %d.png" % n, "<b>AHORA</b> · S%d" % n) for n in range(1, 5)],
          titulo="FEED 23-10 · Tex-Mex, ronda 2", ancho=420,
          notas=("Qué cambió", [
              "Las cuatro fotos se rehicieron como <b>foto documental del fotógrafo del evento</b>, con el mismo color y la "
              "misma luz del buffet real de Piso18: mini tacos de cóctel en fila, porciones desparejas, casi todo nítido, "
              "sin el desenfoque ni el brillo de estudio que las hacía ver generadas.",
              "Portada, textos y «Desliza» quedan como estaban."]))

p.comparar(("out/piso18/oct/r2/S4/FEED/P18 FEED 23-10 Estacion Tex Mex 2.png", "igual a la portada, demasiados tacos"),
           (E + "S4/FEED/P18 FEED 23-10 Estacion Tex Mex 2.png", "cenital, cuatro tacos"),
           titulo="FEED 23-10 S2 · segunda vuelta",
           que="«se ve muy similar a la portada (…) tal vez la vista más cenital y se ve demasiada cantidad de tacos»",
           notas=("Qué cambió", ["Toma cenital sobre la misma cubierta y con la misma luz: cuatro tacos distintos "
                                 "(carne, pollo, vegetales, camarón), guacamole, pico de gallo y limón, con aire alrededor."]))

p.notas([
    "Las historias no cambiaron de diseño. Sólo se rindieron de nuevo para que el «18» de piso18.cl salga con cifras de "
    "caja alta, igual que el resto de la grilla.",
    "En Drive se reemplazaron los mismos archivos, así que cada enlace sigue siendo el mismo.",
], titulo="Entrega")
p.escribir()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · FEED 07-10 · carrusel Escapada Romántica — ronda 2 (29-09) para revisar; la ronda 1 queda abajo como registro."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/oct3-revision"
p = Pagina("dt", "DOUBLETREE · FEED 07-10 · CARRUSEL ESCAPADA ROMÁNTICA · RONDA 4",
           "Escapada Romántica 07-10, ronda 4",
           "29-09-2026 · portada 1080×1350 · no subido", f"{R}/r4.html",
           origen="scripts/dt-oct3-escapada-revision.py")
p.pedido("Una corrección para la foto de la portada del carrusel Escapada Romántica: la pareja se ve extraña, debe ser "
         "realista y una foto actual de sesión de habitación mejor lograda", "Eli", "29-09")
p.comparar((f"{R}/r3/escapada-1.png", "ronda 3 · habitación 505 con atardecer pintado"),
           (f"{R}/r4/escapada-1.png", "habitación 476 de la sesión SEP 2026, pareja nueva con la luz real de la foto"),
           titulo="Portada · la foto nueva")
p.comparar((f"{R}/r3/escapada-1.png", "ronda 3"), (f"{R}/r4/escapada-1.png", "ronda 4"),
           titulo="Portada · la pareja de cerca", detalle=(300, 520, 800, 960))
p.pedido("(ronda 3) Agregar sunset y agregar masaje, que tengan el mismo peso. Están muy juntos los textos, en todos, cuando se "
         "trata de stack. En los beneficios (son punteos) van puntos finales y un punteo. Dice +21, entonces también "
         "+100. La portada me gustó mucho, el desde así está bien", "Eli", "29-09")
p.comparar((f"{R}/r2/escapada-2.png", "ronda 2"), (f"{R}/r3/escapada-2.png", "mismo peso, punteo con punto final, +$100.000, más interlínea"),
           titulo="Lámina 2", detalle=(88, 380, 1080, 960))
p.comparar((f"{R}/r2/escapada-1.png", "ronda 2"), (f"{R}/r3/escapada-1.png", "titular con interlínea 1,3"),
           titulo="Portada · el titular apilado", detalle=(0, 260, 1080, 560))
p.pedido("(ronda 1) No lo dejaría taan romántico, parece más de Noche de Bodas, algo más de escaparse, hacer algo distinto "
         "(tachado: contenido lo resolvió con el titular nuevo y el post atemporal)", "cliente, grilla DT", "28-09")
p.laminas([(f"{R}/r4/escapada-1.png", "1 · portada (ronda 4)"), (f"{R}/r3/escapada-2.png", "2 · personaliza tu experiencia")],
          titulo="El carrusel · ronda 4", ancho=520)
p.laminas([("raw/hilton/dt/ref-oct2/fd-07-10-escapada-1.jpg", "REF 1 · el pin"),
           ("raw/hilton/dt/ref-oct2/fd-07-10-escapada-2.jpg", "REF 2 · la otra lámina de la misma cuenta")],
          titulo="Las referencias", ancho=420)
p.notas([
    "<b>Portada</b> calcada de la REF 1: antetítulo en versales, titular Stag a dos pesos centrado, la escena al "
    "medio y la píldora de contorno abajo (con la dirección). «Desde» arriba del precio, todo centrado (ronda 2).",
    "<b>Ronda 4 · la foto de la portada</b> ahora es la habitación REAL <code>sep_26-476</code> de la sesión SEP 2026 "
    "(king con banqueta y ventanal), sin usar en el feed. Se sacó el atardecer naranja pintado: queda la luz de tarde "
    "de la propia foto. La pareja nueva está sentada en la banqueta, brindando, con ropa de fin de semana; se revisó "
    "con zoom: manos, cuatro pies apoyados y miradas. La cubeta con el espumante quedó sobre la cama.",
    "(ronda 3) La foto anterior era la habitación <code>sep_26-505</code> de la sesión SEP 2026, sin usar en el feed. "
    "La IA sólo agregó la pareja, la cubeta con el espumante en primer plano y el atardecer en la ventana (R-69). "
    "Tono de escapada de fin de semana: ropa de calle, sin pétalos ni batas (R-74). Pareja nueva, distinta de la del feriado.",
    "<b>Lámina 2</b> calcada de la REF 2, con el nombre del programa arriba en Stag itálica a dos pesos (ronda 2): foto oscurecida en azul DT, titular y la tabla con filetes: "
    "sunset +$21.000 y masajes $100.000, con el detalle de cada uno y el legal abajo.",
    "⚠️ <b>La mesa del sunset es GENERADA.</b> No hay foto real de la terraza de QB en alta (sólo miniaturas de noche). "
    "Se hizo tomando como referencia el visual del Sunset QB ya aprobado. Si tienes una foto real, la cambio.",
    "Logo sólo en la portada (R-10, R-11). Sin punto en títulos (R-60); el legal conserva el suyo.",
])
p.escribir()

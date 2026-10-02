#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · campaña ARMY (02-10) — KV de post 4:5 de PREVENTA, ronda 8: tres opciones."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/army"
N = "DT ARMY KV Post PREVENTA - "
O1, O2, O3 = N + "Opción 1 Ciudad.png", N + "Opción 2 Habitación.png", N + "Opción 3 Ciudad logo morado.png"
p = Pagina("dt", "DOUBLETREE · CAMPAÑA ARMY",
           "KV de post · preventa: tres opciones",
           "02-10-2026 · ronda 11 · sólo preventa, post 4:5 (2250 × 2813) · en Drive, carpeta GRÁFICAS DT ARMY",
           f"{R}/revision.html", origen="scripts/dt-army-revision.py")

p.opciones([(f"{R}/{O1}", "1 · ciudad"), (f"{R}/{O2}", "2 · habitación doble"), (f"{R}/{O3}", "3 · ciudad con el logo morado")],
           titulo="Las tres opciones")

p.pedido("en la op 2, en texto blanco sin botón y queda · y noches en la op 3, ese texto a blanco",
         "Eli", "02-10 · ronda 11 · opciones 2 y 3",
         que="<b>Qué cambió:</b> en la <b>opción 2</b>, la dirección va en texto blanco suelto, sin la placa blanca. En la "
             "<b>opción 3</b>, «Noches del 16 y 17 de octubre» volvió de morado a blanco, igual que en la opción 1. La "
             "opción 1 no cambió.")
p.comparar((f"{R}/r10/{O2}", "ronda 10 · dirección en placa"), (f"{R}/{O2}", "ahora · en blanco, sin placa"),
           titulo="Opción 2 · el pie", detalle=(60, 1040, 1020, 1340))
p.comparar((f"{R}/r10/{O3}", "ronda 10 · fecha en morado"), (f"{R}/{O3}", "ahora · fecha en blanco"),
           titulo="Opción 3 · la fecha", detalle=(60, 940, 1020, 1340))

p.pedido("olvidaste añadir abajo del correo el texto de la ubicación del hotel, es muy importante",
         "Eli", "02-10 · ronda 10 · en las tres (ya aprobadas)",
         que="<b>Qué cambió en las tres:</b> bajo el botón del correo va la dirección, <b>«Av. Vitacura 2727, Las Condes»</b> "
             "(como la trae el brief), con un ícono de ubicación. En las opciones 1 y 3 va en blanco sobre el negro; para "
             "abrirle sitio, la fecha, los íconos y el botón subieron entre 24 y 30 px. En la opción 2 va en azul DT "
             "dentro de una placa blanca, bajo el botón.")
p.comparar((f"{R}/r9/{O1}", "aprobada · sin dirección"), (f"{R}/{O1}", "ahora · con dirección"),
           titulo="Opción 1 · el pie", detalle=(60, 940, 1020, 1340))
p.comparar((f"{R}/r9/{O2}", "aprobada · sin dirección"), (f"{R}/{O2}", "ahora · con dirección"),
           titulo="Opción 2 · el pie", detalle=(60, 1040, 1020, 1340))
p.comparar((f"{R}/r9/{O3}", "aprobada · sin dirección"), (f"{R}/{O3}", "ahora · con dirección"),
           titulo="Opción 3 · el pie", detalle=(60, 940, 1020, 1340))

p.pedido("los textos no en negro sino en azul DT o morado en la op 2… me refiero a los que son negros, que pasen a azul DT "
         "en la op2", "Eli", "02-10 · ronda 9 · opción 2",
         que="<b>Qué cambió:</b> en la opción 2, todo lo que estaba en negro —PREVENTA, «ANTES», el precio, «para 2 "
             "personas · IVA incluido», la fecha, los íconos con sus rótulos, los filetes y el legal— pasó a <b>azul "
             "DoubleTree (#09194E)</b>. El morado no se tocó: logo, titular, «Tarifa ARMY» y tachado. Las opciones 1 y 3 "
             "quedan como estaban.")
p.comparar((f"{R}/r8/{O2}", "ronda 8 · textos en negro"), (f"{R}/{O2}", "ahora · textos en azul DT"),
           titulo="Opción 2 · habitación doble")

p.pedido("En las tres opciones necesito que el tachado sea con dos líneas, porque así generalmente se hace.",
         "Eli", "02-10 · ronda 8 · en las tres",
         que="<b>Qué cambió en las tres:</b> «ANTES $185.000» va tachado con <b>dos líneas</b> paralelas, en el morado del "
             "hotel. Nada más se movió en las opciones 1 y 3.")
p.comparar((f"{R}/r7/{O1}", "ronda 7 · una línea"), (f"{R}/{O1}", "ahora · dos líneas"),
           titulo="El tachado, de cerca (opción 1)", detalle=(300, 420, 780, 500))

p.pedido("En la opción 2 necesito que lo vuelvas a diseñar… el morado que utilizaste en los textos de DoubleTree se viste "
         "de morado es distinto. Quitémosle definitivamente el morado que tiene, todo ese como transición, para que no nos "
         "dificulte tanto; sólo que quede como un desenfoque más sutil. DoubleTree se viste de morado, o sea el mismo color "
         "que unificamos, para que se note, e igual el logo sea morado. Podría ser todo como un blanco sutil, ese recuadro "
         "con un poquito de opacidad… y el botón sea como el de las tres opciones, así vamos unificando.",
         "Eli", "02-10 · ronda 8 · opción 2",
         que="<b>Qué cambió en la opción 2:</b> el recuadro ya no tiene morado: es <b>blanco con algo de transparencia</b> "
             "(80 %) y un desenfoque suave, así que la habitación se adivina detrás. El logo y «DOUBLETREE SE VISTE DE "
             "MORADO» van en <b>el mismo morado del hotel</b> que las otras dos. Como el fondo es claro, el resto del "
             "texto (PREVENTA, precio, fecha, íconos, legal) pasó a <b>negro</b>, y el morado queda de acento en "
             "«Tarifa ARMY» y en el tachado. El botón es el <b>metálico morado</b> de las opciones 1 y 3.")
p.comparar((f"{R}/r7/{O2}", "ronda 7 · recuadro morado"), (f"{R}/{O2}", "ahora · recuadro blanco"),
           titulo="Opción 2 · habitación doble")

p.medido([
    ("Morado en las tres", "#9639F4", "ok", "el del hotel: titular, logo (op. 2 y 3), fecha (op. 3), «Tarifa ARMY» (op. 2), tachado"),
    ("Recuadro de la opción 2", "blanco al 80 %, desenfoque 3 px", "ok", "sin morado"),
    ("Botón", "el mismo en las tres", "ok", "metal morado, correo en blanco"),
    ("QA de la marca (qa/motor.py --marca hilton)", "3 de 3", "ok", "las tres piezas pasan"),
], titulo="Lo medido")

p.notas([
    "<b>Para que lo sepas:</b>",
    "1 · En la opción 2, «Tarifa ARMY» va en morado liso (sobre blanco la textura metálica clara no se leía).",
    "2 · Sigue resumido «2 tragos en QB Restaurant» (el brief dice «Experiencia pre o post concierto en QB Restaurant "
    "con 2 tragos»).",
    "<b>Lo que sigue cuando elijas:</b> ST, post para paid (1:1) y ST para paid, y después la línea de venta.",
])
p.escribir()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · campaña ARMY (02-10) — KV de post 4:5 de PREVENTA, ronda 15: las opciones 1 y 3 con la diagramación de la 2 (botón liso, fecha e íconos arriba, precio más grande)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/army"
N = "DT ARMY KV Post PREVENTA - "
O1, O2, O3 = N + "Opción 1 Ciudad.png", N + "Opción 2 Habitación.png", N + "Opción 3 Ciudad logo morado.png"
O2F = N + "Opción 2 Fachada morada.png"
O2C = N + "Opción 2 Hotel al atardecer.png"
p = Pagina("dt", "DOUBLETREE · CAMPAÑA ARMY",
           "KV de post · preventa, y las adaptaciones de las opciones 1 y 2",
           "02-10-2026 · ronda 15 · sólo preventa, post 4:5 (2250 × 2813) · en Drive, carpeta GRÁFICAS DT ARMY",
           f"{R}/revision.html", origen="scripts/dt-army-revision.py")

p.opciones([(f"{R}/{O1}", "1 · ciudad"), (f"{R}/{O2C}", "2 · la foto de la clienta, con filtro morado"), (f"{R}/{O3}", "3 · ciudad con el logo morado")],
           titulo="Las tres opciones")

p.pedido("quitemos el antes $185 tachado · en todo", "Eli", "02-10 (noche) · posts y adaptaciones",
         que="<b>Qué cambió en todas:</b> salió <b>«ANTES $185.000»</b> tachado. El precio quedó entre sus dos filetes, "
             "28 px más abajo para repartir el aire entre el rótulo y la fecha; en la opción 1 el hotel subió lo mismo. "
             "Nada más se movió.")
p.comparar((f"{R}/r16-con-antes/{O1}", "antes · con «ANTES $185.000»"), (f"{R}/{O1}", "ahora"), titulo="Opción 1")
p.comparar((f"{R}/r16-con-antes/{O2C}", "antes · con «ANTES $185.000»"), (f"{R}/{O2C}", "ahora"), titulo="Opción 2")

A = f"{R}/adaptaciones/DT ARMY "
C1, C2 = "PREVENTA - Opción 1 Ciudad.png", "PREVENTA - Opción 2 Hotel al atardecer.png"
p.pedido("OP 1 y 2 quedaron, por favor ten las adaptaciones listas para todas cuando te diga cuál quede",
         "Eli", "02-10 · adaptaciones de las opciones 1 y 2",
         que="<b>Qué hay:</b> el mismo KV del post llevado a <b>historia</b> (2250 × 4000), <b>historia para paid</b> "
             "(1080 × 1920, con la zona segura de Meta: nada en los 250 px de arriba ni en los 340 de abajo) y <b>post "
             "para paid</b> (1080 × 1080), para la opción 1 y para la opción 2. Están sólo en local: <b>no se subieron a "
             "Drive</b> hasta que digas cuál queda.")
p.opciones([(A + "ST " + C1, "historia · opción 1"), (A + "ST " + C2, "historia · opción 2")], titulo="Historia")
p.opciones([(A + "ST Paid " + C1, "historia para paid · opción 1"), (A + "ST Paid " + C2, "historia para paid · opción 2")],
           titulo="Historia para paid (zona segura de Meta)")
p.opciones([(A + "Post Paid " + C1, "post para paid · opción 1"), (A + "Post Paid " + C2, "post para paid · opción 2")],
           titulo="Post para paid (1:1)")

p.pedido("Quiero que el botón quede igual como está en la opción 2, para que todo se vea centrado. Sube un poco más "
         "«Noches del 16 y 17 de octubre» y los íconos, al igual que está en la opción 2. Y necesito que el antes y el "
         "precio y todo eso quede un poco más grande… las tres tal cual como está en la opción 2… para que se vea todo "
         "bien unificado", "Eli", "02-10 · ronda 15 · opciones 1 y 3",
         que="<b>Qué cambió en las opciones 1 y 3:</b> toman la <b>diagramación de la 2</b>. El botón es el <b>morado liso</b>. "
             "«PREVENTA», «ARMY», el <b>«ANTES» y el precio</b> crecieron al tamaño de la 2. La <b>fecha y los íconos</b> "
             "van más grandes y <b>126 px más arriba</b>, sobre el hotel. Botón, dirección y legal quedan a la misma altura "
             "en las tres. La opción 2 no cambió.")
p.comparar((f"{R}/r14/{O1}", "ronda 14"), (f"{R}/{O1}", "ahora · diagramada como la 2"), titulo="Opción 1 · ciudad")
p.comparar((f"{R}/r14/{O3}", "ronda 14"), (f"{R}/{O3}", "ahora · diagramada como la 2"),
           titulo="Opción 3 · ciudad con el logo morado")

p.pedido("quieren literal el army con el corazón. Y que «Tarifa» déjalo en las tres más pequeño, arriba de army. "
         "PREVENTA en los tres menos grueso", "Eli", "02-10 · ronda 14 · en las tres",
         que="<b>Qué cambió en las tres:</b> «ARMY» es <b>el rótulo de la clienta, calcado, con su corazón</b> y en su "
             "mismo lila. <b>«Tarifa»</b> va más chica, arriba a la izquierda del rótulo. <b>«PREVENTA»</b> bajó de peso "
             "(de seminegra a regular). Para hacerle sitio al rótulo, el precio bajó unos 15–20 px en las opciones 1 y 3.")
p.comparar((f"{R}/r13/{O1}", "ronda 13"), (f"{R}/r14/{O1}", "ronda 14 · ARMY literal, Tarifa chica, PREVENTA liviana"),
           titulo="Opción 1 · ciudad")
p.comparar((f"{R}/r13/{O3}", "ronda 13"), (f"{R}/r14/{O3}", "ronda 14 · ARMY literal, Tarifa chica, PREVENTA liviana"),
           titulo="Opción 3 · ciudad con el logo morado")
p.comparar((f"{R}/r13/{O1}", "ronda 13"), (f"{R}/r14/{O1}", "ronda 14"), titulo="El sello, de cerca (opción 1)",
           detalle=(180, 150, 900, 480))

p.pedido("la foto de la op 2 literal del de la clienta que mandó, en un filtro morado · así la dos mejor y queda "
         "[maqueta de Scarlette] · botón sin lo metálico", "Eli / Scarlette", "02-10 · ronda 14 · opción 2",
         que="<b>Qué cambió en la opción 2:</b> el fondo es <b>la foto de la clienta</b> (el hotel al atardecer), limpia de "
             "los textos del teaser y con un <b>filtro morado</b>. La distribución es la de la maqueta: <b>sin recuadro</b>, "
             "logo blanco arriba, todo el texto al centro sobre la foto y el <b>botón morado liso</b>, sin el metálico. "
             "Los textos son los del brief: <b>«ANTES $185.000»</b> (la maqueta decía $135.000).")
p.comparar((f"{R}/r13/{O2F}", "ronda 13 · fachada con tarjeta blanca"), (f"{R}/{O2C}", "ahora · la foto de la clienta"),
           titulo="Opción 2")
p.comparar((f"{R}/refs/ref-clienta.jpg", "la imagen de la clienta"), (f"{R}/{O2C}", "la opción 2"),
           titulo="Opción 2 · junto a la referencia")

p.pedido("esta ref mandó clienta… por ende ésta sería la base, para que sigamos usando el «Army» de la misma forma, "
         "mantener el logo · para las 3 opciones", "Eli", "02-10 · ronda 13 · en las tres",
         que="<b>Qué cambió en las tres:</b> «ARMY» va con <b>trazo de pincel</b>, como en la referencia de la clienta, en el "
             "morado del hotel y apenas inclinado hacia arriba. «Tarifa» sigue en la itálica de DT. Los logos quedan como "
             "estaban.")
p.pedido("yo no usaría esto bajo del logo [«DOUBLETREE SE VISTE DE MORADO»] · eso para los 3",
         "Scarlette / Eli", "02-10 · ronda 13 · en las tres",
         que="<b>Qué cambió en las tres:</b> salió el titular «DOUBLETREE SE VISTE DE MORADO» de debajo del logo. Del logo se "
             "pasa directo a «PREVENTA / Tarifa ARMY», que creció un poco con el sitio que quedó.")
p.comparar((f"{R}/r11/{O1}", "antes"), (f"{R}/r13/{O1}", "ronda 13 · sin titular, ARMY de pincel"), titulo="Opción 1 · ciudad")
p.comparar((f"{R}/r11/{O3}", "antes"), (f"{R}/r13/{O3}", "ronda 13 · sin título, ARMY de pincel"), titulo="Opción 3 · ciudad con el logo morado")

p.pedido("la 2 tiene unos globos muy wtf, pero haría otra opción cambiando ésa. Con la imagen de fachada que usamos para el "
         "Día del Turismo, la dejaría completa en MORADO como la ref… · la op 2 que se parezca al fondo de la clienta · "
         "con esta distribución la 2 [tarjeta blanca al centro sobre la foto morada]",
         "Scarlette / Eli", "02-10 · rondas 12 y 13 · opción 2",
         que="<b>Qué cambió en la opción 2:</b> sale la habitación con globos y entra la <b>fachada del hotel</b> (la foto de "
             "la portada del Día del Turismo) <b>al atardecer y entera en morado</b>, como el fondo de la clienta. La "
             "distribución es la del post que mandaste: foto morada a sangre y una <b>tarjeta blanca</b> al centro, con el "
             "logo arriba; el cielo y la cornisa del hotel se ven sobre la tarjeta. El atardecer se hizo con IA sobre la "
             "foto real, sin cambiar el edificio; el <b>letrero «DoubleTree» de la fachada es el real</b> (la IA lo había "
             "reescrito y se repuso desde la foto).")
p.comparar((f"{R}/r11/{O2}", "antes · habitación con globos"), (f"{R}/r13/{O2F}", "ronda 13 · fachada al atardecer"),
           titulo="Opción 2")
p.comparar((f"{R}/r12/{O2F}", "ronda 12 · fachada de día teñida"), (f"{R}/r13/{O2F}", "ronda 13 · atardecer, tarjeta blanca"),
           titulo="Opción 2 · de la ronda 12 a ésta")

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

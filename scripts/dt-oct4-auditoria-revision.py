#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · octubre · auditoría del resto de la grilla con las reglas R-132–R-136 (29-09)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/hilton/dt/oct4-auditoria"
A, D = f"{R}/antes", f"{R}/despues"
p = Pagina("dt", "DOUBLETREE · OCTUBRE · AUDITORÍA CON LO APRENDIDO",
           "El resto de octubre, revisado",
           "29-09-2026 · 11 piezas revisadas · 3 corregidas", f"{R}/revision.html",
           origen="scripts/dt-oct4-auditoria-revision.py")

p.pedido("Ahora revisa las demás de la grilla para que podamos corregir según lo aprendido, para tenerlo al día",
         "Eli", "29-09",
         que="<b>Qué se revisó:</b> todo lo de octubre que no se tocó en las dos rondas de hoy: FEED 10-10 Opinión, "
             "post Family Time S5, carrusel «5 cosas» (7 láminas) y la lámina 2 de Escapada. Con las reglas nuevas: "
             "sin letras separadas, bullets en Stag, título alineado al panel y lo chico sobre foto con fondo. "
             "<b>Las 3 correcciones son de espaciado y a tamaño de celular son sutiles</b>: por eso van ampliadas.")

p.comparar((f"{A}/Post n°1 S5 DT.png", "antes · IVA INCLUIDO a 0,16 em"),
           (f"{D}/Post n°1 S5 DT.png", "ahora · 0,03 em y un punto más grande"),
           titulo="FEED Family Time S5 · «IVA INCLUIDO»", detalle=(330, 930, 750, 1060), escala=2.2,
           notas=("Por qué", ["Es exactamente el recurso que Constanza marcó en la portada Escapada: letras muy separadas."]))
p.comparar((f"{A}/Post n°1 S2 DT.png", "antes · «Silvana:» a 0,07 em"),
           (f"{D}/Post n°1 S2 DT.png", "ahora · 0,03 em, como la cita"),
           titulo="FEED 10-10 Opinión · el nombre", detalle=(120, 300, 960, 440), escala=2.0,
           notas=("Ojo", ["La plantilla de opiniones (la de Expedia que aprobaste) no cambia: sólo el espaciado del nombre."]))
p.comparar((f"{A}/C1 S2 DT n°2.png", "antes · mucho aire entre palabras"),
           (f"{D}/C1 S2 DT n°2.png", "ahora · espacio normal"),
           titulo="Carrusel Escapada · lámina 2 · el legal", detalle=(200, 1170, 880, 1270), escala=2.2,
           notas=("Por qué", ["Constanza: «las tipografías separadas en cada palabra». Acá era el espacio entre palabras."]))

p.laminas([(f"{D}/Post n°1 S5 DT.png", "FEED Family Time S5"), (f"{D}/Post n°1 S2 DT.png", "FEED 10-10 Opinión"),
           (f"{D}/C1 S2 DT n°2.png", "Escapada · lámina 2")], titulo="Las tres, completas", ancho=420)

p.notas([
    "<b>Sin cambios (ya cumplían):</b> el carrusel «5 cosas que hacen especial tu estadía» completo (7 láminas: "
    "nada supera 0,02 em, los textos van en Stag y alineados a un margen) y la portada Escapada (su «Desde» tiene "
    "0,04 em, que no se distingue de 0,03).",
    "<b>Coworking</b>: el título va dentro del cristal al centro, no bajo el logo, así que no entra en la regla de "
    "distancia al logo. Ya se le había quitado el espaciado de «UBICACIÓN».",
    "Se compararon las piezas nuevas contra las entregadas: fuera de la zona corregida no cambió ningún otro píxel "
    "relevante (foto, colores y demás textos iguales).",
    "<b>En Drive (reemplazadas, md5 verificado):</b> S2/FEED Post n°1 S2 DT · S5/FEED Post n°1 S5 DT · "
    "S2/FEED C1 S2 DT n°2.",
    "Sigue abierta la interlínea de la portada Escapada: 1,16 (entre tu 1,3 y lo que pidió Constanza).",
])
p.escribir()

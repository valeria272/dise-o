#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisión del Reel DJ S2 OCT de QB: lo reemplazado en el editable de Canva de Eli
(DAHWxIFbuvA), página por página. Las imágenes son las vistas previas del borrador."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina

R = "out/qb/oct/reel-dj-s2/revision/"
p = Pagina("qb", "QB · REEL DJ · SEMANA 2 DE OCTUBRE",
           "Tu plantilla, con las tres noches reemplazadas",
           "01-10-2026 · FEED del 09-10 · guardado en tu editable de Canva (9 páginas)",
           R + "revision-reel-dj-s2.html")
p.pedido("No es hacer algo nuevo sino ir reemplazando. Recuerda ajustar según la capa del DJ y los textos bien.", "Eli", "01-10")
p.pedido("Agrega uno extra de Felipe, con cualquier foto; después reemplazamos. Y me parece que Seba Soto ahora el logo es de SEBSS.", "Eli", "01-10")
p.seccion("Martes — página nueva, foto PROVISORIA") if hasattr(p,"seccion") else None
p.comparar((R + "antes-1-jueves.png", "No existía: se duplicó la página del jueves"), (R + "despues-0-martes.png", "Martes 6 · Felipe Saxofonista · la foto es de Isa Serafini, PROVISORIA hasta que llegue la real"), titulo="Martes (nueva)")
p.comparar((R + "antes-1-jueves.png", "Jueves 1 · DJ Flo Veloso"),
           (R + "despues-1-jueves.png", "Jueves 8 · DJ Isa Serafini · foto _DSC5260 recortada + su logo blanco"),
           titulo="Jueves")
p.comparar((R + "antes-2-viernes.png", "Viernes 2 · DJ Nacho Mella"),
           (R + "despues-2-viernes.png", "Viernes 9 · DJ Seba Soto · foto «Flyers» + logo SEBSS blanco"),
           titulo="Viernes")
p.comparar((R + "antes-3-sabado.png", "Sábado 3 · DJ Ignacio Peñafiel"),
           (R + "despues-3-sabado.png", "Sábado 10 · DJ Nacho Mella · la misma foto y el mismo encuadre que usaste el 2-oct"),
           titulo="Sábado")
p.pedido("Añade al Sunset QB «DESDE $3.990» como botón, en el banner final.", "Eli", "01-10")
p.comparar((R + "antes-9-sunset.png", "Sunset QB sin precio"), (R + "despues-9-sunset.png", "Botón «DESDE $3.990» bajo el arco, con el verde del botón del banner de Sunset"), titulo="Página final · Sunset QB")
p.escribir()

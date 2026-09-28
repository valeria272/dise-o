#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 6 (Eli 28-09): copas a la misma altura en el AYCD, legal y
velo en Sunset, y el ticket de Eli sostenido en la mano sobre QB real.

    python scripts/qb-oct-r6-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A = "out/qb/oct/_antes-r5/"
N = "out/qb/oct/r4/"

p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 6", "Copas alineadas, legal legible y el ticket en la mano",
           "28-09-2026 · 3 historias corregidas · 08 CMR aprobada",
           "out/qb/oct/r4/revision-r6.html", origen="scripts/qb-oct-r6-revision.py")

p.pedido("La altura de las tres copas de la ST del 6 del 10 tiene que ser la misma… El Sunset QB lo veo "
         "perfecto; aumenta un poco el tamaño de los legales y déjalo un poco más abajo… y oscurece un poco "
         "hacia arriba para que se pueda leer Sunset QB… La del 21 no está aprobada: usa el ticket de la imagen "
         "que te mostré… una mano sujetando el ticket con el fondo de lo que describe el brief respecto a cómo "
         "es QB realmente.", "Eli", "28-09")

p.comparar((A + "ST n°2 S1 QB OCT 26.png", "ronda 5"), (N + "ST n°2 S1 QB OCT 26.png", "ronda 6"),
           titulo="ST 06-10 · All You Can Drink", que="Las tres copas con el borde en la misma línea.",
           detalle=(60, 600, 1020, 1300), ancho=420, escala=0.9,
           notas=("Qué cambió", ["La sangría real se queda; la copa del centro sube su pie para quedar a la altura del spritz y del espumante",
                                  "Mismo encuadre, mismo bloque AYCD"]))

p.comparar((A + "ST n°5 S1 QB OCT 26.png", "ronda 5"), (N + "ST n°5 S1 QB OCT 26.png", "ronda 6"),
           titulo="ST 09-10 · Sunset QB", que="Legal más grande y la parte de arriba más oscura.",
           detalle=(60, 1380, 1020, 1600), ancho=420, escala=1.0,
           notas=("Qué cambió", ["Legal de 14 a 19 px (+35 %), en dos líneas que cierran en y 1578: lo más abajo que permite la zona segura de Instagram y paid (1580). Para que quepa, el bloque de abajo sube 30 px",
                                  "Oscurecido de arriba más alto y más denso (820 px al 80 %, antes 560 px al 45 %): Sunset QB se lee limpio"]))

p.opciones([("raw/hilton/qb/ref-oct/R-21-ticket-eli-28sep.png", "<b>TU TICKET</b>"),
            ("raw/hilton/qb/ref-oct/R-21-estacionamiento.jpg", "<b>REF DEL BRIEF</b>"),
            (N + "ST n°3 S3 QB OCT 26.png", "<b>AHORA</b> — ronda 6")],
           titulo="ST 21-10 · Estacionamiento", ancho=300, elige=False,
           que="Mano sosteniendo el ticket (brief y ref), con tu diseño de ticket y el fondo de QB.",
           notas=("Cómo se armó", [
               "Foto: una mano sostiene un ticket en blanco sobre la terraza de QB de noche, generada tomando de referencia la foto real «QB oct-15» (sesión terraza 10-10: lámparas de mimbre, plantas) → «Imagen referencial»",
               "Tu ticket impreso sobre el papel de la foto: flechas, código de barras, la P, TICKET / ESTACIONAMIENTO, 50 % con el OFF apilado. Abajo, «Ingreso por Encomenderos 275» a la izquierda, porque el pulgar toma la esquina derecha",
               "Todo el texto dentro de la zona segura"]))

p.medido([("QA de QB sobre las 3", "0 bloqueantes", "ok", "2 avisos: la franja que el velo lleva a negro (09 arriba, 21 abajo)"),
          ("Legal del Sunset", "19 px · cierra en 1578", "ok", "zona segura 1580")], titulo="Lo medido")
p.notas(["Aprobadas por ti en esta vuelta: 08 CMR y 09 Sunset (con este ajuste). Sin cambios: Banco de Chile, 14, 15 y el post de cumpleaños.",
         "Nada subido a Drive todavía."], titulo="Lo demás")
p.escribir()

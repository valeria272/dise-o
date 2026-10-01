#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisión de los Reels DJ S3 (15-10) y S5 (23-10) de QB: copias de la plantilla del S2
en Canva (DAHWygD5dcQ y DAHWyh1dYY0), con las noches reemplazadas. Las imágenes son
cuadros del MP4 final (tiempos y música ya ajustados).

    python scripts/qb-oct-reel-dj-s3-s5-revision.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina

S3, S5 = "out/qb/oct/reel-dj-s3/", "out/qb/oct/reel-dj-s5/"
p = Pagina("qb", "QB · REELS DJ · SEMANAS 3 Y 5 DE OCTUBRE", "La plantilla del S2 con las noches de cada semana",
           "01-10-2026 · FEED del 15-10 y del 23-10 · en Canva · MP4 + GIF subidos a Drive (S3 y S5 / QB / FEED)",
           S3 + "revision/revision-reel-dj-s3-s5.html", origen="scripts/qb-oct-reel-dj-s3-s5-revision.py")
p.pedido("Si ves que hay algo de octubre a corregir o diseñar que está okey para diseñar, tómalo", "Eli", "01-10-2026",
         que="En la grilla de QB lo único en OK PARA DISEÑAR que no tenía pieza eran estos dos reels. Se armaron con la "
             "receta del S2: misma plantilla, sólo cambian la capa del DJ, el logo, el día y el nombre.")
p.laminas([(S3 + "cuadros/t1.6.png", "<b>Martes 13</b> · Felipe Saxofonista · foto PROVISORIA (la de Isa)"),
           (S3 + "cuadros/t4.2.png", "<b>Jueves 15</b> · DJ Seba Soto · foto de la chaqueta de mezclilla + logo SEBSS"),
           (S3 + "cuadros/t7.6.png", "<b>Viernes 16</b> · DJ Juanjo · foto y logo JOTA (confirmado por Eli)"),
           (S3 + "cuadros/t11.4.png", "<b>Sábado 17</b> · DJ Nacho Mella · foto nueva (camisa blanca)")],
          titulo="Semana 3 · FEED 15-10", ancho=300,
          notas=("Para revisar", ["Seba Soto y Nacho Mella van con una foto distinta a la del S2, para no repetir la semana anterior.",
                                  "Viernes: el logo es JOTA (confirmado). El rótulo dice «DJ JUANJO», como la grilla.",
                                  "Video: 31,3 s · portada 2,8 s · segunda noche 2,5 s · música de principio a fin, sin silencios (medido)."]))
p.pedido("Revisa a DJ Seba Soto (SEBSS), que su foto tiene la cabeza cortada… Ojo, desapareció su cuerpo abajo, eso no debe pasar", "Eli", "01-10-2026",
         titulo="Correcciones de Seba Soto")
p.opciones([(S3 + "_antes/t4.2-seba-v1.png", "<b>1.</b> foto de gran angular: la cabeza se leía cortada"),
            (S3 + "_antes/t4.2-seba-v2-sin-cuerpo.png", "<b>2.</b> foto de mezclilla: cabeza bien, pero el cuerpo se desvanecía"),
            (S3 + "cuadros/t4.2.png", "<b>3. AHORA</b> — misma foto, con el cuerpo completo bajo los textos")],
           titulo="Jueves 15 · DJ Seba Soto", ancho=330, elige=False,
           notas=("Qué cambió", ["La foto de mezclilla llega sólo hasta el pecho. Se extendió hacia abajo (chaqueta, polera y cintura) y encima se pegó la foto real: la cara, el pelo y las manos son los originales; sólo el torso de abajo es generado.",
                                 "El cuerpo ya no se desvanece: sigue bajo la fecha, el nombre y el horario, como en los otros DJ. Detrás de los textos la ropa va un poco más oscura para que se lean.",
                                 "Logo SEBSS, textos y banners: iguales."]))
p.laminas([(S5 + "cuadros/t1.6.png", "<b>Martes 20</b> · Felipe Saxofonista · foto PROVISORIA (la de Isa)"),
           (S5 + "cuadros/t4.2.png", "<b>Jueves 22</b> · DJ Isa Serafini · la misma del S2"),
           (S5 + "cuadros/t7.6.png", "<b>Viernes 23</b> · DJ Flo Veloso · foto de estudio + su logo en blanco"),
           (S5 + "cuadros/t11.4.png", "<b>Sábado 24</b> · DJ Paula Achurra · IMG_1574")],
          titulo="Semana 5 · FEED 23-10", ancho=300,
          notas=("Para revisar", ["Martes 20: el brief dice «Falta horario». Quedó «Desde las 19:00 hrs», como los otros martes.",
                                  "El martes y el jueves muestran la misma foto de Isa, una después de la otra: se nota. Se arregla cuando llegue la foto de Felipe.",
                                  "El logo de Flo Veloso viene en fucsia; va en blanco, como los otros logos de la plantilla.",
                                  "Video: 31,3 s · portada 2,8 s · segunda noche 2,5 s · música de principio a fin, sin silencios (medido)."]))
for n, d, t in (("Seba Soto", S3, "seba5"), ("Jota / Juanjo", S3, "jota"), ("Nacho Mella", S3, "mella2"),
                ("Flo Veloso", S5, "flo"), ("Paula Achurra", S5, "paula")):
    p.opciones([(d + "_trabajo/_%s-vs.jpg" % t, "foto original · recorte sobre verde · recorte sobre negro")],
               titulo="Recorte · " + n, ancho=1000, elige=False)
p.notas(["Las láminas de bancos y promos (CMR, Falabella, Banco de Chile, All You Can Drink, Sunset QB) no se tocaron: son las del S2.",
         "Los dos editables son COPIAS de tu plantilla del S2, hechas por el conector: «Reel DJ 2026 S3 OCT QB 26» y «Reel DJ 2026 S5 OCT QB 26». Tu archivo del S2 no se tocó.",
         "Tiempos y música no quedan en Canva: están en los MP4 «tiempos ajustados» de out/qb/oct/reel-dj-s3 y reel-dj-s5.",
         "En Drive: S3 HILTON OCT 2026 / QB / FEED y S5 HILTON OCT 2026 / QB / FEED → «Reel n°1 S<n> QB OCT 26» en .mp4 y .gif (md5 verificado). Felipe Saxofonista sigue con foto provisoria."], titulo="Notas")
p.escribir()

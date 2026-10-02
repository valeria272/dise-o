#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisión de los Reels DJ S2, S3 y S5 de QB con la foto real de Felipe Saxofonista
(antes iba una provisoria). Las imágenes son cuadros del MP4 final.

    python scripts/qb-oct-reel-dj-felipe-revision.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina

F = "out/qb/oct/reel-dj-felipe/"
R = F + "revision/"
p = Pagina("qb", "QB · REELS DJ · FELIPE SAXOFONISTA", "La foto real de Felipe en los martes de las semanas 2, 3 y 5",
           "02-10-2026 · FEED del 09-10, 15-10 y 23-10 · en Canva · MP4 + GIF en Drive (S2, S3 y S5 / QB / FEED)",
           R + "revision-reel-dj-felipe.html", origen="scripts/qb-oct-reel-dj-felipe-revision.py")
p.pedido("Ya tenemos para QB las fotos de Felipe saxofonista, ahora ajusta todo de reels DJ de él", "Eli", "02-10-2026",
         que="Se reemplazó la foto provisoria de la página del martes en los tres reels. Lo demás (otras noches, bancos, "
             "promos, tiempos y música) no cambió.")
for n, dia in ((2, "Martes 6"), (3, "Martes 13"), (5, "Martes 20")):
    p.comparar((R + "antes-s%d.png" % n, "foto provisoria"), (R + "despues-s%d.png" % n, "foto real de Felipe"),
               titulo="Semana %d · %s" % (n, dia), ancho=400, detalle=(0, 600, 1080, 1560), escala=1.0)
p.opciones([(F + "_trabajo/_felipe-compuesta-ver.jpg", "foto original · foto sin el micrófono · zona que se reconstruyó")],
           titulo="El micrófono", ancho=1000, elige=False,
           notas=("Qué se hizo", ["De las dos fotos se eligió la vertical (IMG_5326): está de frente, con la cabeza despegada del fondo y el cuerpo hasta la cintura.",
                                  "El pedestal del micrófono cruzaba justo por la fecha y el nombre. Se quitó y se reconstruyó sólo lo que tapaba (la manga, el borde de la campana del saxo y el canto de la chaqueta).",
                                  "La cara, el pelo, los lentes, las manos y el saxo son los de la foto real."]))
p.opciones([(F + "_trabajo/_felipe2-vs.jpg", "foto · recorte sobre verde · recorte sobre negro")],
           titulo="Recorte", ancho=1000, elige=False,
           notas=("Calce", ["Cabeza a la altura de los otros DJ (tope en y 660, cara centrada en el arco).",
                            "El cuerpo sigue bajo los textos hasta los banners; detrás de la fecha la ropa y el saxo van un poco más oscuros para que se lea."]))
p.notas(["Video de cada semana: 31,3 s · portada 2,8 s · segunda noche 2,5 s · música de principio a fin, sin silencios (medido).",
         "Las otras páginas se compararon contra el video anterior: no cambiaron.",
         "En Drive: S2, S3 y S5 HILTON OCT 2026 / QB / FEED → «Reel n°1 S<n> QB OCT 26» en .mp4 y .gif (md5 verificado). El S2 se sube por primera vez; S3 y S5 se reemplazaron (mismo enlace).",
         "Editables guardados en Canva: S2 (tu plantilla), S3 y S5 (las copias). Tiempos y música no quedan en Canva."], titulo="Notas")
p.escribir()

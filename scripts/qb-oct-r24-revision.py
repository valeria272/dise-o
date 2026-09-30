#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDAS 22–24 (Eli + Nicolás 30-09): Banco de Chile, Sunset, carrusel CMR
y ST CMR 40 %.

    python scripts/qb-oct-r24-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

R = "out/qb/oct/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDAS 22–24", "Banco, Sunset, carrusel CMR y ST 40 %",
           "30-09-2026 · 6 archivos reemplazados en Drive (md5 igual)", R + "r24/revision-r24.html",
           origen="scripts/qb-oct-r24-revision.py")

p.comparar((R + "r22/_antes/ST n°1 S1 QB OCT 26.png", "antes (r20)"), (R + "r23/ST n°1 S1 QB OCT 26.png", "ahora (r23)"),
           titulo="ST 01-10 · Banco de Chile  (ST n°1 S1) — APROBADA", ancho=400,
           que="Eli: «las tarjetas y el legal están demasiado arriba… baja el legal junto a las tarjetas, oscurece ese "
               "lado del legal» · «junta un poco más las tarjetas al legal pero que no solape, sube un poco la imagen "
               "para que no tape el texto y deja oscuro abajo» · «okey».",
           notas=("Qué cambió", ["Tarjetas y legal bajan: el legal cierra en ≈1852 (antes ≈1806).",
                                 "Las tarjetas bajan hasta que su reflejo termina 12 px sobre el legal, sin tocarlo.",
                                 "La foto sube 60 px: el plato ya no queda detrás del legal y las copas no chocan con las cajas.",
                                 "Pie más oscuro: velo de abajo más alto y denso y una sombra baja sobre el plato.",
                                 "Textos: sin cambios."]))

p.comparar((R + "r24/_antes/ST n°5 S1 QB OCT 26.png", "antes (r20)"), (R + "r24/ST n°5 S1 QB OCT 26.png", "ahora (r24)"),
           titulo="ST 09-10 · Sunset QB  (ST n°5 S1)", ancho=400,
           que="Nicolás: «siento que está muy oscura en general la imagen. ¿Podríamos ver la forma de que se vea más "
               "sunset y cálida la foto?» · Eli: «que no esté tan oscuro abajo, que se vea el tono de atardecer, y usa un "
               "plato de la carta de terraza».",
           notas=("Qué cambió", ["Plato: EMPANADAS DE MECHADA, de la carta de Terraza de qbrestaurant.cl (Entradas), con la "
                                 "foto de la carta como referencia. Salen las papas trufadas, que no están en esa carta.",
                                 "Foto regenerada sobre la anterior (la terraza de QB se mantiene) con luz de atardecer real: "
                                 "sol bajo desde la calle, el trago a contraluz, reflejos cálidos en la mesa.",
                                 "La mesa se extendió hacia abajo: la foto llena toda la historia y ya no hay bloque negro al pie.",
                                 "Velos más livianos (arriba 86 % → 70 %, abajo 85 % → 55 %) y un baño cálido suave.",
                                 "Textos: sin cambios. Sigue con «Imagen referencial»."]))

p.laminas([(R + "r24/_antes/C3 S1 N°%d QB OCT 26.png" % i, "<b>antes (r19)</b> — N°%d" % i) for i in (1, 2, 3)],
          titulo="FEED 09-10 · Carrusel CMR — ANTES", ancho=330)
p.laminas([(R + "r24/C3 S1 N°%d QB OCT 26.png" % i, "<b>ahora (r24)</b> — N°%d" % i) for i in (1, 2, 3)],
          titulo="FEED 09-10 · Carrusel CMR — AHORA", ancho=330,
          que="Eli: «en los tres tenemos el logo, solamente en la portada» · «coherencia en jerarquía con los títulos en "
              "posiciones, que se vea recto hacia los siguientes slides y con continuidad, puede ser la portada con la "
              "segunda» · «un plato o escena del shooting de platos; la última puede variar».",
          notas=("Qué cambió", ["Logo: sólo en la N°1 (sale de la N°2 y la N°3).",
                                "Titulares: los tres empiezan a la misma altura (y=200) y en el mismo cuerpo, Raleway 68 "
                                "(ExtraBold arriba, Light abajo). Antes eran 92 / 58 / 60 a alturas distintas.",
                                "N°1 + N°2: una sola foto del shooting de la carta («American Baby ribs 11»: schop, spritz y "
                                "dos manos tomando las ribs), partida entre las dos láminas: al deslizar, la foto continúa.",
                                "N°2: sombra suave detrás de la promo para que la mano no se vea dentro del marco. El bloque "
                                "CMR aprobado no se toca; baja 30 px para dejar aire bajo el titular.",
                                "N°3: la misma foto del brindis.",
                                "Textos: sin cambios."]))

p.comparar((R + "r24/_antes/ST n°4 S1 QB OCT 26.png", "antes (r20)"), (R + "r24/ST n°4 S1 QB OCT 26.png", "ahora (r24)"),
           titulo="ST 08-10 · CMR 40 % sábados  (ST n°4 S1)", ancho=400,
           que="Eli: «el texto “tu panorama” no se lee mucho, que sea más grueso y bájalo un poco».",
           notas=("Qué cambió", ["«Tu panorama de sábado ahora / tiene un nuevo beneficio»: de Raleway Regular a SemiBold.",
                                 "Baja 50 px (se despega de las tarjetas).",
                                 "Texto: el mismo."]))
p.escribir()

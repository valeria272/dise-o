#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 21 (Eli 29-09): copas del AYCD alineadas de verdad y carrusel de
cumpleaños con la portada igual a la referencia y fotos actuales.

    python scripts/qb-oct-r21-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r21/_antes/", "out/qb/oct/r21/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 21", "Copas alineadas y carrusel de cumpleaños",
           "29-09-2026 · 5 archivos reemplazados en Drive (md5 igual)", "out/qb/oct/r21/revision-r21.html",
           origen="scripts/qb-oct-r21-revision.py")
p.comparar((A + "ST n°2 S1 QB OCT 26.png", "r20"), (N + "ST n°2 S1 QB OCT 26.png", "r21"),
           titulo="ST 06-10 · All you can drink  (ST n°2 S1)", ancho=400, detalle=(0, 650, 1080, 1350), escala=0.75,
           que="Eli: «esos cócteles aún no se alinean, haz de nuevo esa imagen».",
           notas=("Qué cambió", ["Con tres modelos de copa distintos la IA no logra igualarlos (medí 4 versiones: el alto de la "
                                 "copa iba de 662 a 832 px). Ahora los tres tragos van en el MISMO modelo de copón: spritz, "
                                 "sangría y espumante.",
                                 "Medido sobre la foto (5504 px de alto): bordes en 2750 / 2745 / 2752 y fondos de copa en "
                                 "3545 / 3540 / 3560 → una sola línea arriba y otra abajo, como tus rayas.",
                                 "Todo lo demás de la escena (campana, guante, telón, bandeja) y los textos se mantienen."]))
p.laminas([(A + "C1 S1 N°%d QB OCT 26.png" % i, "<b>r20</b> — N°%d" % i) for i in range(1, 5)],
          titulo="FEED 05-10 · Carrusel cumpleaños — ANTES (r20)", ancho=300)
p.laminas([(N + "C1 S1 N°%d QB OCT 26.png" % i, "<b>r21</b> — N°%d" % i) for i in range(1, 5)],
          titulo="FEED 05-10 · Carrusel cumpleaños — AHORA (r21)", ancho=300,
          que="Eli: «se ve muy saturado y mal. Quiero que la portada sea igual a la referencia y las demás slides como la "
              "de la torta, con mejores fotos; ya que está en el ojo, utiliza fotos más actuales».",
          notas=("Qué cambió", ["N°1 = la referencia: polaroids con flash alrededor de la tarjeta de lino, con «Tu cumpleaños / "
                                "SE CELEBRA EN QB» y la bajada.",
                                "N°2–N°4 = como la portada de la torta: una foto a sangre y el texto blanco directo, sin "
                                "recuadros ni tarjetas. Íconos finos sólo en la lista de extras y el botón verde del CTA.",
                                "Fotos más actuales: la sesión «Fotos 4 agosto» (editadas, agosto 2026), la más reciente de "
                                "QB. N°2 amigos brindando en la mesa (IMG_4988), N°3 el grupo grande (IMG_4877), N°4 la torta "
                                "de la historia (lleva «Imagen referencial»).",
                                "Textos iguales al brief."]))
p.escribir()

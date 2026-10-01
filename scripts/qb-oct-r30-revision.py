#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 30 (Eli 01-10): carrusel AYCD sobre la foto REAL «QB oct-31»
partida en panorama (G1 + G2), para que al deslizar sea una transición.

    python scripts/qb-oct-r30-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r30/_antes/", "out/qb/oct/r30/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 30", "Carrusel All You Can Drink — la foto real en panorama",
           "01-10-2026 · 2 archivos reemplazados en Drive (md5 igual)", N + "revision-r30.html",
           origen="scripts/qb-oct-r30-revision.py")
p.pedido("Para el All You Can Drink sería usar como referencia el material real que dejaste, porque esa es la más "
         "similar. En la segunda slide yo pondría todo lo mismo, ya que esa misma foto del octubre 31 sirve para "
         "ambas y que sea una transición bonita",
         "Eli", "01-10-2026")
p.opciones([(N + "_ref-pin-cliente.jpg", "<b>Referencia del cliente</b>"),
            (N + "_foto-real-QB-oct-31.jpg", "<b>Foto real «QB oct-31»</b> — la que se usa en las dos láminas")],
           titulo="La referencia y la foto real", ancho=380, elige=False)
p.opciones([(N + "_panorama-al-deslizar.jpg", "G1 + G2 una al lado de la otra, como se ven al deslizar")],
           titulo="El carrusel como panorama", ancho=1000, elige=False,
           que="La barra, las luces y el romero siguen de una lámina a la otra; el velo de la G2 parte en cero en el borde, "
               "así que no hay salto de tono en la unión.")
p.comparar((A + "C2 S1 N°1 QB OCT 26.png", "r29: copa de sangría generada"),
           (N + "C2 S1 N°1 QB OCT 26.png", "r30: la foto real de la barra de QB"),
           titulo="G1 · Portada  (C2 S1 N°1)", ancho=420,
           notas=("Qué cambió", ["La portada es la foto real «QB oct-31»: mismo vaso tallado, mismo romero, misma barra y mismas luces.",
                                 "Único retoque: el líquido. El trago de la foto es de autor y no entra en el All You Can Drink, así que se cambió por sangría dentro del mismo vaso (salen las moras, entra una rodaja de naranja).",
                                 "«*Imagen referencial» va a la izquierda del vaso, sobre el fondo oscuro.",
                                 "Textos: sin cambios."]))
p.comparar((A + "C2 S1 N°2 QB OCT 26.png", "r29: cinco tragos en fila"),
           (N + "C2 S1 N°2 QB OCT 26.png", "r30: la misma foto, que sigue hacia la derecha"),
           titulo="G2 · Promo  (C2 S1 N°2)", ancho=420,
           notas=("Qué cambió", ["Salen los cinco tragos: el fondo es la continuación de la misma foto (la barra y las luces fuera de foco).",
                                 "Con eso se resuelve el comentario de las proporciones: ya no hay tragos en la G2.",
                                 "Logo, «ALL YOU CAN DRINK», botón verde, horario y legal: mismas posiciones y mismos textos."]))
p.opciones([(N + "_alternativa-G1-foto-tal-cual.jpg", "<b>Alternativa</b> — la foto sin tocar, con el trago de autor original")],
           titulo="Si prefieres la foto tal cual", ancho=380, elige=False,
           que="Queda lista: es cambiar un archivo y volver a rendir. Ojo: ese trago no es del All You Can Drink.")
p.notas(["La foto mide 3000 px de ancho y el panorama necesita 4500: está ampliada 1,67 veces. En Instagram se ve bien; no sirve para impresos.",
         "El brief sigue pidiendo «3 a 4 tragos diferentes» y la G2 ahora no muestra ninguno: si contenido lo extraña, la fila de la r29 está guardada.",
         "QA de QB: sin bloqueantes; dos chequeos de agencia no corrieron por la falla de scipy en esta máquina (revisados a ojo).",
         "Drive: S1 HILTON OCT 2026 / QB / FEED / C2 S1 AYCD — mismos nombres y enlaces."], titulo="Dudas y notas")
p.escribir()

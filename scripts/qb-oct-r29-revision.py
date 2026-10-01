#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 29 (01-10): carrusel AYCD según el comentario del cliente
(FEED!E14): G1 más simple, como el pin nuevo; G2 con los tragos en proporción.

    python scripts/qb-oct-r29-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

A, N = "out/qb/oct/r29/_antes/", "out/qb/oct/r29/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 29", "Carrusel All You Can Drink — comentario del cliente",
           "01-10-2026 · 2 archivos reemplazados en Drive (md5 igual)", N + "revision-r29.html",
           origen="scripts/qb-oct-r29-revision.py")
p.pedido("Están fuera de proporciones los tragos en la G2, en la G1, mantener más simple, creo que está muy literal "
         "con la refe, veamos algo más de este estilo: cl.pinterest.com/pin/1068760555331775825",
         "Cliente, celda COMENTARIOS CLIENTE del FEED 06-10 (estado EN CAMBIOS)", "01-10-2026",
         que="El comentario anterior de esa celda («que la G1 esté limpia y luego venga la promo») está tachado en la "
             "grilla; igual se mantiene esa estructura porque el brief sigue pidiendo portada + promo.",
         titulo="Lo que pidió el cliente")
p.opciones([(N + "_ref-pin-cliente.jpg", "<b>Referencia nueva del cliente</b> — un vaso solo en la barra, fondo cálido fuera de foco"),
            (N + "_foto-real-QB-oct-31.jpg", "<b>Foto real de QB</b> («QB oct-31», sesión terraza 10-oct) — la base de la G1 nueva")],
           titulo="La referencia y el material real", ancho=380, elige=False)
p.comparar((A + "C2 S1 N°1 QB OCT 26.png", "r19: bartender sirviendo, botella y jigger"),
           (N + "C2 S1 N°1 QB OCT 26.png", "r29: una copa de sangría sola en la barra de QB"),
           titulo="G1 · Portada  (C2 S1 N°1)", ancho=420,
           notas=("Qué cambió", ["Sale la escena del bartender (manos, botella, jigger, menta, frasco): queda UN trago solo, como la referencia nueva.",
                                 "El trago es la sangría, que está en el All You Can Drink, en copón.",
                                 "El lugar es la barra de QB: se partió de la foto real «QB oct-31» (barra perforada con luz, lámparas de mimbre); la IA la llevó a vertical y cambió el trago de autor por la sangría.",
                                 "«*Imagen referencial» pasa a la derecha de la copa, sobre el fondo oscuro (al centro caía sobre los puntos de luz).",
                                 "Textos: sin cambios."]))
p.comparar((A + "C2 S1 N°2 QB OCT 26.png", "r19: cinco tragos en perspectiva, piscola y schop gigantes adelante"),
           (N + "C2 S1 N°2 QB OCT 26.png", "r29: los cinco en una fila, de frente, a su tamaño real"),
           titulo="G2 · Promo  (C2 S1 N°2)", ancho=420,
           notas=("Qué cambió", ["Los cinco tragos del AYCD (sangría, piscola, Ramazzotti, schop, espumante) van en UNA fila, en el mismo plano y sobre la misma barra: los dos copones son iguales, la flauta es angosta, el vaso alto y el schop quedan más bajos.",
                                 "La fila queda libre entre «ALL YOU CAN DRINK» y «TODOS LOS MARTES»: ningún texto tapa un trago.",
                                 "Misma barra de QB que la G1, para que las dos láminas se lean como un solo lugar.",
                                 "Con el fondo ya oscuro se bajó el velo negro; sin limones, hielos ni menta sueltos.",
                                 "El bloque de la promo (logo, nombre, botón verde, horario, legal) no se movió. Textos: sin cambios."]))
p.opciones([(N + "_alternativa-G1-rosato.jpg", "<b>Alternativa de G1</b> — Ramazzotti Rosato en vez de sangría (sin montar)")],
           titulo="Si prefieren otro trago en la portada", ancho=380, elige=False,
           que="Quedó generada y se monta en un minuto si la prefieren.")
p.notas(["La G2 es generada completa (por eso lleva «Imagen referencial» en el legal); la G1 parte de una foto real de QB con el trago cambiado por IA.",
         "El comentario dice «fuera de proporciones» sin decir cuál: se entendió como el tamaño relativo entre los vasos (la piscola y el schop se veían más grandes que los copones).",
         "QA de QB: sin bloqueantes; dos chequeos de agencia (texto al borde y foco por bandas) no corrieron porque scipy está roto en esta máquina — se revisaron a ojo.",
         "Drive: S1 HILTON OCT 2026 / QB / FEED / C2 S1 AYCD — mismos nombres y enlaces."], titulo="Dudas y notas")
p.escribir()

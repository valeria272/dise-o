#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QB · octubre · RONDA 9 (28-09 tarde): lo que pasó a OK PARA DISEÑAR en la grilla
después de las 14:00 — 3 posts de feed (2 carruseles) y 4 historias, cada una al
lado de su referencia.

    python scripts/qb-oct-r9-revision.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _revision import Pagina

N = "out/qb/oct/r9/"
R = "raw/hilton/qb/ref-oct/"
S = "raw/hilton/qb/sep-entregadas/"
p = Pagina("qb", "QB · OCTUBRE 2026 · RONDA 9", "Lo nuevo de la grilla: feed y stories",
           "28-09-2026 · 3 posts de feed + 4 historias", "out/qb/oct/r9/revision-r9.html",
           origen="scripts/qb-oct-r9-revision.py")
p.pedido("Diseña lo nuevo en feed y stories, haz los ajustes que solicitó el cliente.", "Eli", "28-09")

p.laminas([(R + "FEED-07-aycd.jpg", "Referencia"), (N + "C1 S1 N°1 QB OCT 26.png", "G1 limpia"),
           (N + "C1 S1 N°2 QB OCT 26.png", "G2 promo")], ancho=300,
          titulo="FEED 07-10 · All You Can Drink (carrusel)",
          que="«Que sea como esos carruseles que hicimos antes, en que la G1 está limpia y luego viene la promo».",
          notas=("Cómo se hizo", ["G1: foto REAL «QB 13 oct-57», cinco tragos distintos en la mesa de listones, sin texto",
                                  "G2: el post AYCD aprobado de junio (logo, nombre del KV, botón verde) sobre la toma hermana «-54»",
                                  "Todo real: sin «Imagen referencial»"]))
p.laminas([(R + "FEED-12-sunset-imagen.jpg", "Ref. imagen"), (N + "C1 S2 N°1 QB OCT 26.png", "G1 limpia"),
           (N + "C1 S2 N°2 QB OCT 26.png", "G2 promo")], ancho=300,
          titulo="FEED 12-10 · Sunset QB (carrusel)", que="«Mismo comentario que para AYCD».",
          notas=("Cómo se hizo", ["G1: foto REAL «Fotos 4 agosto» IMG_4796, cuatro tragos brindando",
                                  "G2: el post Sunset aprobado (logo Sunset QB, titular fino, pastilla verde) sobre IMG_4797"]))
p.laminas([(R + "FEED-16-autor.jpg", "Referencia"), (N + "Post n°1 S2 QB OCT 26.png", "Post")], ancho=400,
          titulo="FEED 16-10 · Trago de autor", que="«Ok pero dejemos gráfica + limpia, sin los textos y estrellas».",
          notas=("Cómo se hizo", ["AFRODITA (lo elegiste tú: Zeus, Artemisa y Eros no están en la sesión 11-09)",
                                  "La foto real del Afrodita puesta en una mano con IA: vaso, humo y flores iguales → «Imagen referencial»",
                                  "Limpio: sólo el logo arriba"]))
p.laminas([(R + "E-07-cumple-1.jpg", "Referencia"), (N + "ST n°3 S1 QB OCT 26.png", "Historia")], ancho=400,
          titulo="ST 07-10 · Cumpleaños", que="«Veamos opción más simple, siendo una story mostraría la información más importante de inmediato».",
          notas=("Cómo se hizo", ["Sin collage: una foto (la torta del post del 05-10) y toda la información arriba",
                                  "Aire abajo para el sticker «ARMA EL GRUPO Y RESERVA AHORA»",
                                  "«Cuenta separadas» va literal del brief: ¿«Cuentas separadas»? → contenido"]))
p.laminas([(R + "I-12-pulpo.jpg", "Referencia"), (S + "ST5-S2.jpg", "Septiembre"),
           (N + "ST n°1 S2 QB OCT 26.png", "Historia")], ancho=300,
          titulo="ST 12-10 · Pulpo al chimichurri",
          que="«Que el vino sea blanco y cambiar escenario, le ponemos el nombre al plato… arriba Conoce nuestra carta».",
          notas=("Cómo se hizo", ["El pulpo REAL de QB (carta jul-2024) con el plato intacto: la IA cambió la mesa a negra con hojas, como la ref, y el tinto por blanco → «Imagen referencial»",
                                  "Arriba, «Conoce nuestra carta» como la de septiembre; el nombre en cursiva entre filetes"]))
p.laminas([(S + "ST3-S3.jpg", "Septiembre"), (N + "ST n°5 S2 QB OCT 26.png", "Historia")], ancho=400,
          titulo="ST 16-10 · La primavera se sirve en copa",
          que="«Una opción similar a la de trago de autor en septiembre… texto único… sólo la foto de un spritz».",
          notas=("Cómo se hizo", ["El spritz REAL de la sesión de la carta, aislado con IA (sin la cerveza ni las costillas), a luz de tarde → «Imagen referencial»",
                                  "El molde de septiembre: logo, antetítulo + serif en caja alta y el filete punteado"]))
p.laminas([(R + "AD-28-dinamica.jpg", "Ref. original"), (N + "ST n°3 S4 QB OCT 26.png", "Propuesta")], ancho=400,
          titulo="ST 28-10 · Dinámica «¿Este o este?»",
          que="«Busquemos opción de dinámica más afín con QB… últimamente tenemos muy mala participación».",
          notas=("Cómo se hizo", ["Lo elegiste tú: dos tragos de autor REALES (Medusa y Perséfone) y encuesta de un toque",
                                  "Aire al medio para el sticker de encuesta",
                                  "⚠️ El texto del premio es propuesta: el brief decía «El primero en acertar gana un premio sorpresa»"]))
p.notas(["QA de QB: 0 bloqueantes. Los 5 avisos son falsos positivos (desenfoque real de las fotos y las plantas leídas como croma).",
         "Nombres según tu nomenclatura: carrusel C1 S<n> N°<lámina>, historia ST n°<n> S<n>. El post del 16-10 va como «Post n°1 S2» — confírmame si lo numeras distinto.",
         "Nada subido a Drive todavía: con tu visto, lo subo a S<n> HILTON OCT 2026 / QB / STS y FEED."], titulo="Lo demás")
p.escribir()

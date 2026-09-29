#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ronda 5: los dos comentarios de Constanza Lizana en la grilla (29-09).

    python scripts/p18-oct-revision-r5.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/piso18/oct/r5-respaldo/"
E = "out/piso18/oct/entrega/S2/"

p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 5",
    "Los dos comentarios de Constanza, corregidos",
    "29-09-2026 · FEED 09-10 Fechas 2027 (G2) y ST 07-10 Estación favorita · ya reemplazadas en Drive",
    "out/piso18/oct/revision-r5.html",
    origen="scripts/p18-oct-revision-r5.py",
)
p.pedido(
    "Aquí en el slide 2 \"Temporada alta 2027\" Ojo con esa separación de letra x letra en las palabras, "
    "es demasiado ia :(",
    "Constanza Lizana, comentario en la grilla (FEED C9)", "29-09-2026",
    titulo="1 · Lo que pidió Constanza en el carrusel Fechas 2027")
p.comparar(
    (R + "P18 FEED 09-10 Fechas 2027 2.png", "espaciado de 7 px entre letras"),
    (E + "FEED/P18 FEED 09-10 Fechas 2027 2.png", "espaciado de 2 px"),
    titulo="FEED 09-10 · Fechas 2027 · lámina 2",
    detalle=(200, 150, 880, 240), escala=1.3,
    notas=("Qué cambió", [
        "<b>«TEMPORADA ALTA 2027»</b>: la separación entre letras bajó de 7 px a 2 px (de 0,27 a 0,08 del "
        "cuerpo). Ahora se lee como una palabra y no como letras sueltas.",
        "Mismo tamaño, peso, color y posición. El resto de la lámina (titular, calendario, fondo) no se tocó.",
        "La G1 no cambió."]))

p.pedido(
    "Se pierde mucho el texto \"dulce\" \"salada\" en delineado, prueba con la línea más gruesa o bien "
    "mejor sólido",
    "Constanza Lizana, comentario en la grilla (STORIES D8)", "29-09-2026",
    titulo="2 · Lo que pidió Constanza en la encuesta")
p.comparar(
    (R + "P18 ST 07-10 Estacion favorita.png","rótulos calados (solo contorno)"),
    (E + "STS/P18 ST 07-10 Estacion favorita.png", "rótulos en fucsia sólido"),
    titulo="ST 07-10 · ¿Cuál es tu estación favorita?",
    detalle=(230, 380, 1060, 1100), escala=1.0,
    notas=("Qué cambió", [
        "<b>«Dulce» y «Salada»</b> pasaron de contorno fucsia a <b>relleno fucsia sólido</b> (la opción que "
        "Constanza marcó como mejor). Mantienen la misma tipografía itálica, tamaño y sombra.",
        "Las fotos, las flechas, el fondo y el titular siguen igual."]))

p.notas([
    "Con el criterio de Constanza revisé el resto de octubre. Hay <b>otros cinco rótulos</b> con espaciado "
    "abierto (de 4 a 9 px) en piezas ya aprobadas: Atardecer 13-10 (dos rótulos), Tu próxima celebración, "
    "Tex-Mex 23-10 y ST Visita virtual 27-10. <b>No los toqué</b> porque el comentario es de esta lámina. "
    "Si quieres que lo aplique en todo el mes, avísame y lo hago en la misma pasada.",
    "Las versiones anteriores quedaron respaldadas en <code>out/piso18/oct/r5-respaldo/</code>."],
    titulo="Para decidir")
p.escribir()

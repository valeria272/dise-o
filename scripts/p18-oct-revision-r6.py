#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ronda 6: el criterio de Constanza (R-57) aplicado a todo el mes.

    python scripts/p18-oct-revision-r6.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

R = "out/piso18/oct/r6-respaldo/"
E = "out/piso18/oct/entrega/"

p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 6",
    "El criterio de Constanza, aplicado al resto de octubre",
    "29-09-2026 · 4 láminas ya aprobadas · reemplazadas en Drive",
    "out/piso18/oct/revision-r6.html",
    origen="scripts/p18-oct-revision-r6.py",
)
p.pedido(
    "ahora sabiendo ese aprendizaje, ve si hay algo que corregir a futuro de grilla de oct para no "
    "cometer lo mismo en las demás",
    "Eli", "29-09-2026",
    que="El criterio de Constanza (ronda 5): «Ojo con esa separación de letra x letra en las palabras, es "
        "demasiado ia» y «mejor sólido» en vez de delineado. Revisé todo el código de octubre: el delineado "
        "sólo estaba en Dulce/Salada (ya corregido). El espaciado abierto estaba en 5 rótulos de 4 piezas.")

p.comparar(
    (R + "P18 FEED 13-10 Atardecer 2.png", "0,36 y 0,19"),
    (E + "S3/FEED/P18 FEED 13-10 Atardecer 2.png", "0,08"),
    titulo="FEED 13-10 · Atardecer · lámina 2", detalle=(90, 855, 990, 935), escala=1.0,
    notas=("Qué cambió", [
        "<b>«ESCRIBE TU HISTORIA DE AMOR»</b>: era el más abierto del mes (9 px, 0,36 del cuerpo) → 2 px.",
        "<b>«PISO18.CL»</b> (arriba, junto a «Cotiza tu evento»): 4 px → 1,7 px.",
        "Nada más cambió en la lámina."]))
p.comparar(
    (R + "P18 FEED 16-10 Tu proxima celebracion 1.png", "0,25"),
    (E + "S3/FEED/P18 FEED 16-10 Tu proxima celebracion 1.png", "0,08"),
    titulo="FEED 16-10 · Tu próxima celebración · portada", detalle=(240, 760, 840, 830), escala=1.2,
    notas=("Qué cambió", ["<b>«EN PISO18»</b>: 6 px → 2 px. Lo demás igual."]))
p.comparar(
    (R + "P18 ST 15-10 Cumpleanos sonado.png", "0,16"),
    (E + "S3/STS/P18 ST 15-10 Cumpleanos sonado.png", "0,08"),
    titulo="ST 15-10 · Cumpleaños soñado", detalle=(40, 1080, 1040, 1160), escala=1.0,
    notas=("Qué cambió", ["<b>«RETRO · TROPICAL · BLANCO Y DORADO»</b> bajo las fotos: 3 px → 1,5 px. "
                          "Era el más leve de los cinco."]))
p.comparar(
    (R + "P18 ST 27-10 Visita virtual.png", "0,30"),
    (E + "S5/STS/P18 ST 27-10 Visita virtual.png", "0,08"),
    titulo="ST 27-10 · Visita virtual", detalle=(160, 370, 920, 440), escala=1.2,
    notas=("Qué cambió", [
        "<b>«VISITA VIRTUAL 360°»</b>: 6,5 px → 1,8 px.",
        "Los celulares quedaron exactamente como los aprobaste: sólo se reemplazó la franja del rótulo."]))

p.notas([
    "<b>«TEX MEX»</b> (FEED 23-10) se queda como está: su espaciado ya es discreto (0,07).",
    "Las cuatro <b>ya están reemplazadas en Drive</b> con el mismo nombre (enlaces conservados, md5 verificado). "
    "",
    "Desde ahora, en Piso18 los rótulos en mayúscula van con espaciado ~0,08 y el texto sobre foto en "
    "sólido (reglas R-57 y R-58 en el cerebro de la cuenta).",
    "Respaldo de lo anterior: <code>out/piso18/oct/r6-respaldo/</code>."],
    titulo="Notas")
p.escribir()

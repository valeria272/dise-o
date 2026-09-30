#!/usr/bin/env python3
"""BETWEEN · OCTUBRE · RONDA 9 (30-09) — FEED 14-10: titular menos junto y corte de la bajada.

Uso:  python scripts/between-oct-r9-revision.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _revision import Pagina  # noqa: E402

B = "out/hilton/between/"
p = Pagina("between", "BETWEEN · OCTUBRE · RONDA 9",
           "Espacios Between: titular y bajada",
           "30-09-2026 · FEED 14-10 (S3)",
           B + "oct-r9/revision-r9.html")

p.pedido("«Espacios que invitan a quedarse» están muy juntos, sepáralo solo un poco; y escribe «Café, "
         "comodidad y buenos» y abajo «momentos en Between», porque se está viendo un poco extraño. "
         "Lo demás lo veo bien.", "Eli", "30-09")

p.comparar((B + "oct-r8/BW FEED 14-10 Espacios Between.png", "ronda 8"),
           (B + "oct-r9/BW FEED 14-10 Espacios Between.png", "ronda 9"),
           titulo="FEED 14-10 · Espacios Between", detalle=(140, 190, 940, 490), escala=1.2,
           notas=("Qué cambió", [
               "<b>Titular un poco más separado</b>: ~5 px más entre «ESPACIOS QUE INVITAN» y «A QUEDARSE». Queda a medio camino entre la entrega del 24-09 y la ronda 8.",
               "<b>Bajada con el corte que pediste</b>: «Café, comodidad y buenos» / «momentos en Between». Las dos líneas quedan más parejas.",
               "<b>Ya reemplazado en Drive</b> en S3/BW/FEED, con el mismo nombre y enlace (md5 = local).",
           ]))

p.medido([
    ("S3/BW/STS", "ST 19-10 Cowork · ST 20-10 Lo dicen ustedes", "ok", ""),
    ("S3/BW/FEED", "Reel 12-10 (MP4 + GIF + PORTADA) · FEED 14-10 Espacios", "ok", ""),
    ("S4/BW/STS", "ST 27-10 Espacio para tu evento", "ok", "ST 26-10 WTF pasó a POR GRABAR"),
    ("S5/BW/STS", "ST 28-10 Desayuno Bonjour", "ok", "ST 29-10 spooky, PENDIENTE POR CLIENTE"),
], titulo="Drive contra la grilla viva de las 15:00")

print(p.escribir())

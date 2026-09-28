#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · ST 01-10 FAMILY TIME — antes (fotos, 24-09) y ahora (familia en video, 28-09).

Uso:  python scripts/dt-oct-ft-video-revision.py
"""
import base64
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _revision as rv  # noqa: E402
from _revision import Pagina, RAIZ  # noqa: E402

R = "out/hilton/dt/oct/_rondas/r4-video"
p = Pagina("dt", "DOUBLETREE · OCTUBRE 2026 · ST 01-10",
           "Family Time — la familia en video",
           "28-09-2026 · reemplaza a la de fotos en S1/DT/STS",
           f"{R}/index.html", origen="scripts/dt-oct-ft-video-revision.py")
p.pedido("Utiliza los nuevos personajes que tenemos para DT… las imágenes ya realizadas las puedes volver "
         "videos para que se vea más realista, más bonito, más sutil… sigue totalmente el brief", "Eli", "28-09")


def vid(nombre):
    b = base64.b64encode((RAIZ / R / nombre).read_bytes()).decode()
    return (f'<video src="data:video/mp4;base64,{b}" autoplay loop muted playsinline controls '
            f'style="width:100%;border-radius:10px"></video>')


p.bruto('<section class="elige"><h2>Antes y ahora, en bucle</h2>'
        '<div class="rejilla">'
        f'<figure>{vid("antes-prev.mp4")}<figcaption><b>ANTES</b> — 24-09, fotos fijas con zoom</figcaption></figure>'
        f'<figure>{vid("ahora-prev.mp4")}<figcaption><b>AHORA</b> — la familia del banco, en video</figcaption></figure>'
        '</div></section>')
p.laminas([(f"{R}/tira-antes.jpg", "ANTES · f15 · f90 · f150 · f190 · f220 · f250 · f300 · f445"),
           (f"{R}/tira-ahora.jpg", "AHORA · mismos cuadros")],
          titulo="Tira de fotogramas", ancho=880)
p.notas([
    "<b>Las cinco tomas son las fotos aprobadas del banco (25-09)</b>, animadas con Kling 2.5 Pro: vista a Santiago "
    "(«Días más largos, clima perfecto»), llegada por el lobby, guerra de almohadas, desayuno buffet y la habitación "
    "con la tablet, que sostiene el programa. Un movimiento de cámara lento y un gesto por toma.",
    "<b>Se mantuvo todo lo aprobado:</b> textos literales del brief, cristal alto, barridos, bloque del programa, "
    "íconos, logo y 15 s. Sin paso de gris a color.",
    "<b>La familia de la habitación queda detrás del cristal</b>, así que se ve sola ~1 s antes de que entre (como la foto "
    "sola de la referencia). El programa queda ~5,9 s en pantalla; antes eran ~6,7. Si quieres más tiempo de lectura, "
    "se acortan las tomas rápidas.",
    "<b>Descartada:</b> la toma de la cookie en la cama (a mitad del clip la niña desaparece y el papá cambia de cara).",
    "<b>Premiere:</b> en <code>F:/…/OCTUBRE/DT/S1/ST n°1 S1 DT OCT 26/</code> está la secuencia (.xml) con los clips "
    "en V1, la gráfica con transparencia en V2 y el render final apagado en V3. En Premiere: Archivo › Importar el .xml "
    "y guardar como .prproj. El esmerilado del cristal no viaja: en V2 el cristal va como velo y filete.",
], titulo="Lo que tienes que saber")
p.medido([
    ("Duración", "15,00 s · 1080×1920 · 30 fps · sin audio", "ok", "tope de 15 s"),
    ("GIF", "720×1280 · 12,5 fps · 54 MB", "ojo", "misma especificación que el anterior; pesa más porque ahora todo se mueve"),
    ("Drive", "MP4 + GIF reemplazados en S1/DT/STS", "ok", "md5 verificado contra el local"),
], titulo="Lo medido")
p.escribir()

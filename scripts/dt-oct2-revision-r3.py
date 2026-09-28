#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · octubre 2026, segunda tanda — ronda 3 (28-09): el coworking para revisar + lo subido."""
import base64, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _revision import Pagina, RAIZ  # noqa: E402

E = "out/hilton/dt/entrega-oct2"; R = "out/hilton/dt/oct2-revision"
p = Pagina("dt", "DOUBLETREE · OCTUBRE 2026 · SEGUNDA TANDA · RONDA 3",
           "Octubre DT, ronda 3: coworking para revisar",
           "28-09-2026 · carrusel 21-10 y Family Time 28-10 SUBIDOS", f"{R}/r3.html", origen="scripts/dt-oct2-revision-r3.py")
p.pedido("Achicar un poco ese recuadro… si es el mismo texto no es necesario que dure tanto, que sea una "
         "transición más rápida para el texto, así queda más tiempo mostrándose lo del fondo", "Eli", "28-09")
video = base64.b64encode((RAIZ / R / "cw-preview.mp4").read_bytes()).decode()
p.bruto('<section class="elige"><h2>ST 22-10 · Coworking · ronda 3</h2><p class="que">Dos cristales <b>ajustados a su '
        'texto</b> en vez de uno alto todo el rato: el titular entra a los 0,9 s, se lee ~3 s y sale; la foto queda '
        '<b>sola ~4 s</b>; y el cristal final trae la bajada y la ubicación desde los 8,3 s hasta el final (~6,5 s de '
        'lectura). 15 s, MP4 1080×1920 + GIF 720×1280.</p><div class="rejilla"><figure><video src="data:video/mp4;base64,%s" '
        'autoplay loop muted playsinline controls style="width:100%%;border-radius:10px"></video><figcaption><b>AHORA</b>'
        '</figcaption></figure></div></section>' % video)
p.laminas([(f"{R}/cw-tira.jpg", "un cuadro por segundo, de 0 a 14 s")], titulo="Coworking · la tira", ancho=880)
p.laminas([(f"{E}/C1 S4 DT n°{n}.png", f"n°{n}") for n in range(1, 8)], titulo="SUBIDO · carrusel 21-10 (S4 / DT / FEED)", ancho=300)
p.laminas([(f"{E}/Post n°1 S5 DT.png", "SUBIDO · S5 / DT / FEED")], titulo="SUBIDO · Family Time 28-10", ancho=420)
p.escribir()

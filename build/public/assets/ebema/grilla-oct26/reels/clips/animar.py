#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anima los fotogramas clave de los reels de grilla de octubre 2026 — Kling 2.5 Pro.

Regla medida en los 5 reels de septiembre (manual §4-bis): dentro del cuerpo NO hay
cortes rápidos, «la imagen avanza con movimiento continuo». Por eso cada plano pide un
movimiento de cámara lento y un gesto chico, nunca acción brusca. Los planos del
celular (click_k2, cat_k2) y el mapa NO pasan por Kling: la pantalla real se compone
encima en Remotion, y un teléfono que se mueve no deja calzarla.
Uso: python clips/animar.py [id ...]     (sin argumentos: todos)
"""
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

AQUI = os.path.dirname(os.path.abspath(__file__))
KF = os.path.join(AQUI, "..", "keyframes")
RAIZ = os.path.abspath(os.path.join(AQUI, "../../../../../.."))

QUIETO = (" Cámara estable, movimiento lento y continuo, sin cortes. No aparece texto, ni letreros, "
          "ni logos. Las personas y los objetos conservan exactamente su forma y su ropa.")

P = {
    "click_k1": (5, "Lento acercamiento de cámara. El contratista habla por el celular con fastidio, se "
                    "presiona el otro oído con la mano por el ruido de la obra; al fondo la grúa se mueve "
                    "apenas y un obrero camina en el andamio." + QUIETO),
    "click_k3": (5, "Cámara fija con leve paneo acompañando. El camión blanco de reparto avanza despacio por "
                    "el patio de despacho hacia la cámara, las ruedas giran de forma natural." + QUIETO),
    "cat_k1": (10, "Lento acercamiento de cámara. El maestro revisa el plano, anota con el lápiz en la lista "
                   "de la tabla y vuelve a mirar el plano, concentrado y tranquilo. Luz de mañana estable."
                   + QUIETO),
    "cat_k1b": (5, "Lento acercamiento de cámara. La mano del maestro avanza con el lápiz y marca con un visto "
                   "los ítems de la lista, uno tras otro, con calma." + QUIETO),
    "cat_k4": (5, "Lento paneo lateral de cámara. El maestro, satisfecho, mira el avance de los muros de la "
                  "obra y asiente levemente con una sonrisa; respira tranquilo." + QUIETO),
    "aza_k1": (5, "Lento travelling lateral de cámara a lo largo de la estructura de perfiles de acero, al "
                  "atardecer; la luz cálida recorre las aristas del metal y la vegetación se mueve apenas con "
                  "el viento. La estructura queda rígida, sin deformarse." + QUIETO),
    "aza_k2": (10, "Lento travelling de cámara a lo largo del atado de perfiles ángulo de acero apilados, "
                   "con las puntas pintadas de verde; la luz lateral se desliza sobre las aristas. Los perfiles "
                   "no se mueven ni cambian de forma." + QUIETO),
    "aza_k3": (5, "Cámara fija con leve acercamiento. El soldador avanza despacio el cordón de soldadura sobre "
                  "la unión de los perfiles, con chispas moderadas y resplandor intermitente." + QUIETO),
    "lp_k1": (5, "Lento movimiento de cámara ascendente frente a la estructura de techumbre de madera bajo el "
                 "sol intenso de mediodía; destellos de sol y un leve brillo de calor en el aire." + QUIETO),
    "lp_k2": (10, "Lento acercamiento de cámara. El maestro asienta y acomoda el tablero de cara plateada sobre "
                  "la estructura de la techumbre; el sol se refleja en la lámina de aluminio. El tablero "
                  "conserva su cara plateada perforada y su canto naranjo." + QUIETO),
    "lp_k3": (5, "Cámara fija con leve acercamiento. El carpintero avanza la sierra circular despacio y recto "
                 "por el tablero, sale un poco de aserrín; el tablero conserva su canto naranjo." + QUIETO),
}


def run(k):
    dur, prompt = P[k]
    out = os.path.join(AQUI, k + ".mp4")
    if os.path.exists(out):
        return k, 0, "ya existe"
    cmd = [sys.executable, os.path.join(RAIZ, "scripts/magnific-video.py"), os.path.join(KF, k + ".jpg"),
           "--out", out, "--prompt", prompt, "--dur", str(dur), "--minutos", "40", "--modelo", "kling-v2-5-pro"]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return k, r.returncode, (r.stdout + r.stderr)[-400:]


if __name__ == "__main__":
    ids = sys.argv[1:] or list(P)
    fallas = 0
    with ThreadPoolExecutor(len(ids)) as ex:
        for k, rc, log in ex.map(run, ids):
            print(("OK  " if rc == 0 else "FALLA ") + k, log if rc else "", flush=True)
            fallas += rc != 0
    sys.exit(1 if fallas else 0)

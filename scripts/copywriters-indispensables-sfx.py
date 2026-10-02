#!/usr/bin/env python3
"""COPYWRITERS · reel «Indispensables de oficina» (01-10-2026) — efectos de sonido (Freepik `sound-effects`).

El reel no lleva voz: el audio del trend se agrega en la app al publicar (R-42). Estos efectos
marcan el truco —el objeto aparece en las manos— y van en las dos versiones.

Reusa el pedido y la espera de `gcl-cap02-sfx.py` (mismo endpoint, mismo User-Agent).

    python scripts/copywriters-indispensables-sfx.py            # los que falten
    python scripts/copywriters-indispensables-sfx.py pop_a --rehacer

Salida: public/assets/copywriters/indispensables/sfx/<id>.mp3
"""
import argparse, importlib.util, os
from concurrent.futures import ThreadPoolExecutor

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("gcl_sfx", os.path.join(RAIZ, "scripts", "gcl-cap02-sfx.py"))
gcl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gcl)

gcl.OUT = os.path.join(RAIZ, "public", "assets", "copywriters", "indispensables", "sfx")
gcl.SFX = {
    "pop_a":  ("A short satisfying magic pop as an object appears out of thin air, crisp and playful, "
               "tiny sparkle tail, clean, no music", 1),
    "pop_b":  ("Quick cartoon-free 'poof' appearance sound, soft airy puff with a bright click, short, "
               "premium social media transition, no music", 1),
    "whoosh": ("A fast short whoosh swipe transition, airy and clean, modern social media edit, no music", 1),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()
    os.makedirs(gcl.OUT, exist_ok=True)
    ids = a.ids or list(gcl.SFX)
    ids = [k for k in ids if a.rehacer or not os.path.isfile(os.path.join(gcl.OUT, f"{k}.mp3"))]
    with ThreadPoolExecutor(max_workers=5) as ex:
        for linea in ex.map(gcl.hacer, ids):
            print(linea, flush=True)


if __name__ == "__main__":
    main()

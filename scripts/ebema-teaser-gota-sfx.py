#!/usr/bin/env python3
"""EBEMA · teaser «La Gota de Color» (29-09-2026) — efectos de sonido (Freepik `sound-effects`).

El guion de Carlos Figueroa no lleva voz ni música: el audio es diseño sonoro puro.
  0–2 s zumbido grave · 2–4 s el zumbido se corta (silencio) · 4–6 s golpe de bajo + gota
  6–8 s whoosh suave · 8–10 s remate sonoro corto (entra con el logo blanco sobre negro)

Reusa el pedido y la espera de `gcl-cap02-sfx.py` (mismo endpoint, mismo User-Agent).

    python scripts/ebema-teaser-gota-sfx.py            # los que falten
    python scripts/ebema-teaser-gota-sfx.py golpe --rehacer

Salida: public/assets/ebema/teaser-gota/sfx/<id>.mp3
"""
import argparse, importlib.util, os
from concurrent.futures import ThreadPoolExecutor

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("gcl_sfx", os.path.join(RAIZ, "scripts", "gcl-cap02-sfx.py"))
gcl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gcl)

gcl.OUT = os.path.join(RAIZ, "public", "assets", "ebema", "teaser-gota", "sfx")
gcl.SFX = {
    "zumbido": ("Deep low cinematic drone hum building tension in a dark silent room, subtle sub-bass rumble, "
                "steady and suspenseful, no melody", 4),
    "gota":    ("A single water drop falling and hitting a still surface in extreme close-up, clean crisp "
                "plip with a tiny resonant tail, very quiet room", 1),
    "golpe":   ("A deep cinematic bass impact boom with a soft shimmering tail, premium and elegant, "
                "short, not aggressive", 3),
    # RONDA 2 (Paulina, 29-09): «que suene como una gota cuando está a punto de tocar la zona
    # inferior» → gotas realistas, sin reverb de efecto; se elige la más limpia.
    "gota_real_a": ("A single real water droplet falling into a still shallow puddle, close microphone, "
                    "clean natural 'plip' with a short watery resonance, silent room, realistic, no music", 1),
    "gota_real_b": ("One water drop dripping from a faucet into water in a quiet kitchen, crisp realistic "
                    "drip sound, close mic, natural, no reverb effect", 1),
    "gota_real_c": ("Macro recording of a single clear water drop hitting calm water, soft bright bloop "
                    "with tiny splash detail, very clean and quiet, realistic", 2),
    # RONDA 3 (Paulina, 29-09): «el sonido de la gota debería ser como cuando una gota toca otra
    # gota, cuando la gota toca el agua, para que sea más realista» → gota sobre agua: el
    # «plop» tonal de la burbuja que resuena. Se elige midiendo (un golpe, tono que sube, limpio).
    "agua_a": ("A single water drop falling into a glass bowl of still water, classic resonant 'bloop' "
               "plop with a rising tonal bubble ring, close mic, silent room, realistic", 1),
    "agua_b": ("One droplet dripping into a calm pool of water in a quiet cave, clear musical 'plink' "
               "with a short natural echo, realistic, only one drop", 2),
    "agua_c": ("Macro sound of a water droplet hitting water surface: crisp liquid 'plop' with a small "
               "bubble pop and tiny ripple, very clean, one single drop, no background", 1),
    "agua_d": ("A single drop of water falling from a height into a still puddle, deep round 'bloop' "
               "with a resonant water tone, clean studio recording, no other sounds", 1),
    "whoosh":  ("A soft smooth airy whoosh swirling gently, silky and premium, subtle", 2),
    "remate":  ("A short elegant cinematic logo sting: soft low hit with a bright glassy shimmer that "
                "fades out, minimal, premium", 3),
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

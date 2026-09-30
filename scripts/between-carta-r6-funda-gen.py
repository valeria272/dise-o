#!/usr/bin/env python3
"""BETWEEN · carta R6 (30-09-2026) — fotos de FUNDA de menú con la hoja EN BLANCO (Mystic).

Eli: «quiero un mockup más realista, tal vez en una funda para menú y dentro la portada». La IA sólo
hace la funda y la escena; la hoja va en blanco puro para después calzarle el render exacto de la
portada en perspectiva (`between-carta-r6-funda.py`), con la luz y los brillos de la foto.

    python scripts/between-carta-r6-funda-gen.py [nombre ...]
Salida: out/hilton/between/carta-oficial/r6/mockup/funda/_<nombre>.jpg
"""
import importlib.util
import sys
from pathlib import Path

_s = importlib.util.spec_from_file_location("ia", Path(__file__).with_name("between-ia-ronda4.py"))
ia = importlib.util.module_from_spec(_s)
_s.loader.exec_module(ia)
OUT = ia._RAIZ / "out/hilton/between/carta-oficial/r6/mockup/funda"

HOJA = ("a completely blank plain white paper sheet, tall and narrow (proportion 17 by 30), with no print, "
        "no text and no pattern, all four corners of the sheet clearly visible")
FIN = ("Photorealistic product photography, natural soft daylight from a window, realistic reflections, "
       "sharp focus on the menu, shallow depth of field. No text, no logos, no lettering anywhere.")
# Eli 30-09: «se ven poco profesionales, debes seguir la proporción y la perspectiva, que no se vea
# falso» → vista CENITAL (flat lay de estudio, sin ángulo) para que la hoja de la foto tenga la proporción
# real 17 × 30 medible, y se descarta toda foto cuya hoja no mida 1,76 ± 2 %
HOJA_ALTA = ("a completely blank plain white paper sheet with an exact tall narrow proportion of 17 by 30 "
             "centimetres (almost twice as tall as it is wide), no print, no text, all four corners visible")
PLANO = ("Professional flat lay product mockup photograph shot perfectly straight from directly above, camera "
         "parallel to the table, no perspective distortion, soft even diffused studio daylight, subtle natural "
         "soft shadows, high-end editorial look, ultra realistic, sharp. No text, no logos, no lettering.")
ESCENAS_PLANO = {
    "plano-abierto": ("widescreen_16_9",
                      f"An open tall narrow dark brown leather menu folder lying flat and centred on a warm light "
                      f"oak wooden table, each of its two tall pages has a clear transparent plastic sleeve holding "
                      f"{HOJA_ALTA}, fine stitched leather border, lots of empty table around it. {PLANO}"),
    "plano-abierto-2": ("widescreen_16_9",
                        f"Flat lay of an open slim tall leather menu cover in chocolate brown, two tall narrow "
                        f"pockets side by side each with {HOJA_ALTA}, on a light natural oak table, a small espresso "
                        f"cup far in one corner. {PLANO}"),
    "plano-cerrado": ("portrait_2_3",
                      f"A single tall narrow dark brown leather menu holder with a full clear plastic front sleeve "
                      f"holding {HOJA_ALTA}, lying flat and centred on a warm light oak wooden table. {PLANO}"),
    "plano-cerrado-2": ("portrait_2_3",
                        f"A slim tall leather menu board in chocolate brown with a clear acrylic front sleeve "
                        f"holding {HOJA_ALTA}, lying flat and centred on a light natural oak table, generous "
                        f"empty space around. {PLANO}"),
}
ESCENAS = {**ESCENAS_PLANO,
    "cuero": ("portrait_2_3",
              f"A closed dark brown leather menu cover holder lying slightly angled on a warm oak wooden cafe "
              f"table, its front has a large clear transparent plastic window pocket holding {HOJA}, stitched "
              f"leather edges, a cup of latte and green plant leaves softly out of focus in the background. {FIN}"),
    "acrilico": ("portrait_2_3",
                 f"A clear transparent acrylic menu sleeve with thin clean edges lying flat on a warm oak "
                 f"wooden cafe table, seen from a slight three-quarter top angle, holding {HOJA}, soft glare "
                 f"on the acrylic, a latte cup and plant leaves at the edges of the frame. {FIN}"),
    "atril": ("portrait_2_3",
              f"A clear acrylic L-shaped menu stand standing upright on a warm oak wooden cafe table, holding "
              f"{HOJA}, three-quarter front view, cozy specialty coffee shop with green plants blurred behind, "
              f"a latte cup beside it. {FIN}"),
    "cuero-abierto": ("widescreen_16_9",
                      f"An open dark brown leather menu folder lying on a warm oak wooden cafe table, seen from "
                      f"above at a slight angle, each of its two pages has a clear transparent plastic sleeve "
                      f"holding {HOJA}, a latte cup and plant leaves at the corners of the frame. {FIN}"),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for n in (sys.argv[1:] or ESCENAS):
        ratio, prompt = ESCENAS[n]
        res = ia.generar(n, {"prompt": prompt, "ratio": ratio})
        ia.guardar(res, OUT / f"_{n}.jpg")


if __name__ == "__main__":
    main()

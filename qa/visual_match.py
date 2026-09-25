#!/usr/bin/env python3
"""VISUAL MATCH TEST — pone una pieza al lado de la lámina maestra del Look & Feel.

    python3 qa/visual_match.py out/copylab/pieza.png [otra.png ...]

Deja `<pieza>__vs_lookandfeel.jpg` al lado de cada pieza. La pregunta que se contesta
mirándola: ¿podría esta pieza haber aparecido en la lámina? Si parece de otra marca,
FAIL, aunque qa/motor.py la apruebe (creative-system/MASTER/09_QA_CHECKLIST.md).
"""
import sys
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
LAMINA = RAIZ / "creative-system/MASTER/reference/LOOK_AND_FEEL_REFERENCE.png"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ref = Image.open(LAMINA).convert("RGB")
    h = 1200
    ref = ref.resize((int(ref.width * h / ref.height), h), Image.LANCZOS)
    for p in sys.argv[1:]:
        pieza = Image.open(p).convert("RGB")
        ph = int(h * 0.62)
        pieza = pieza.resize((int(pieza.width * ph / pieza.height), ph), Image.LANCZOS)
        hoja = Image.new("RGB", (ref.width + pieza.width + 60, h), (255, 255, 255))
        hoja.paste(ref, (0, 0))
        hoja.paste(pieza, (ref.width + 30, (h - ph) // 2))
        salida = Path(p).with_name(Path(p).stem + "__vs_lookandfeel.jpg")
        hoja.save(salida, quality=88)
        print(salida)


if __name__ == "__main__":
    main()

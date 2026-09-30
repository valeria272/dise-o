#!/usr/bin/env python3
"""BETWEEN · carta oficial R6 (30-09-2026) — mockup físico de portada y contraportada por opción.

Pedido de Eli: «prepara el Drive para presentar los PDF como muestra y su mockup de cómo se vería la
portada y la contraportada en físico, de manera que se puedan visualizar las tres opciones».

La MESA es una foto generada (Mystic, una sola vez, queda en caché); las CARTAS son el render exacto
de la R6 (hoja 1 y última hoja) montado encima con sombra, luz de la escena y un leve giro: la IA no
toca ni una letra de la carta.

    python scripts/between-carta-r6-mockup.py            # genera la mesa si falta y arma A, B, D
Salida: out/hilton/between/carta-oficial/r6/mockup/BW-CARTA-BETWEEN-OPCION-<X>-MOCKUP.jpg
"""
import importlib.util
import json
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter, ImageOps

sys.path.insert(0, str(Path(__file__).parent))
_s = importlib.util.spec_from_file_location("ia", Path(__file__).with_name("between-ia-ronda4.py"))
ia = importlib.util.module_from_spec(_s)
_s.loader.exec_module(ia)

R6 = ia._RAIZ / "out/hilton/between/carta-oficial/r6"
OUT = R6 / "mockup"
MESA = OUT / "_mesa.jpg"
PROMPT = ("Overhead top-down photograph of an empty warm honey-toned oak wooden cafe table, natural wood grain, "
          "soft diffused daylight from a window on the left, gentle natural shadows, a white ceramic cup of latte "
          "on a saucer just touching the top right corner and a few green plant leaves entering from the bottom "
          "left corner, the whole centre of the table completely empty and clear, calm cozy specialty coffee "
          "shop mood, photorealistic, sharp, natural colours. No text, no logos, no paper, no menu, no lettering.")


def mesa():
    if MESA.exists():
        return Image.open(MESA).convert("RGB")
    OUT.mkdir(parents=True, exist_ok=True)
    res = ia.generar("mesa", {"prompt": PROMPT, "ratio": "widescreen_16_9"})
    if not ia.guardar(res, MESA):
        sys.exit("x no se pudo generar la mesa")
    return Image.open(MESA).convert("RGB")


def carta(png, alto, giro):
    """La hoja con esquinas levemente redondeadas (papel cortado), girada, y su sombra."""
    im = Image.open(png).convert("RGB")
    w = round(alto * im.width / im.height)
    im = im.resize((w, alto), Image.LANCZOS)
    m = Image.new("L", im.size, 0)
    from PIL import ImageDraw
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, alto - 1), radius=max(2, alto // 400), fill=255)
    im = im.convert("RGBA")
    im.putalpha(m)
    im = im.rotate(giro, resample=Image.BICUBIC, expand=True)
    return im


def montar(bg, piezas):
    """piezas: [(png, centro_x_rel, giro)]. Sombra de contacto + sombra suave, y la luz de la mesa encima."""
    W, Hh = bg.size
    alto = round(Hh * 0.80)
    lienzo = bg.convert("RGBA")
    luz = bg.convert("L").filter(ImageFilter.GaussianBlur(Hh // 12))
    luz = ImageOps.autocontrast(luz, cutoff=2)
    for png, cx, giro in piezas:
        c = carta(png, alto, giro)
        x, y = round(W * cx - c.width / 2), round(Hh / 2 - c.height / 2)
        a = c.getchannel("A")
        for off, blur, op in ((Hh // 90, Hh // 45, 0.40), (Hh // 400, Hh // 300, 0.55)):
            sh = Image.new("RGBA", c.size, (25, 18, 10, 0))
            sh.putalpha(a.point(lambda v, op=op: int(v * op)))
            capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
            capa.paste(sh, (x + off // 2, y + off), sh)
            lienzo = Image.alpha_composite(lienzo, capa.filter(ImageFilter.GaussianBlur(blur)))
        # la luz de la escena cae también sobre el papel (suave, sin ensuciar la tinta)
        l = luz.crop((x, y, x + c.width, y + c.height)).point(lambda v: int(214 + v * 41 / 255))
        rgb = ImageChops.multiply(c.convert("RGB"), Image.merge("RGB", (l, l, l)))
        rgb.putalpha(a)
        lienzo.alpha_composite(rgb, (x, y))
    return lienzo.convert("RGB")


def main():
    bg = mesa()
    if bg.width < 3000:
        bg = bg.resize((3200, round(3200 * bg.height / bg.width)), Image.LANCZOS)
    info = json.loads((R6 / "paginas.json").read_text(encoding="utf-8"))
    for op in [a for a in sys.argv[1:]] or ["A", "B", "D"]:
        n = info[op]["paginas"]
        png = lambda k: R6 / "png" / f"BW-CARTA-OFICIAL-R6-OP{op}-{k}.png"
        im = montar(bg, [(png(1), 0.36, 2.2), (png(n), 0.64, -1.6)])
        dst = OUT / f"BW-CARTA-BETWEEN-OPCION-{op}-MOCKUP.jpg"
        im.save(dst, quality=90)
        print("✓", dst.name, im.size, f"portada + hoja {n} (contraportada)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Rinde y controla la prueba Biotop 700 + 911 de Selfie en sus 5 formatos.

    ~/copylab-venv/bin/python3 scripts/selfie-biotop-qa.py            # todo
    ~/copylab-venv/bin/python3 scripts/selfie-biotop-qa.py Mail Post  # algunos

Por formato hace tres renders —la pieza, la pieza SIN flechas y la máscara de las
flechas— y comprueba lo que pidió Coni el 24-09:
  1. NINGUNA flecha toca nada: bajo cada trazo (con margen) sólo puede haber fondo
     plano coral #FF4374 o salmón #FF8C93. Ni frasco, ni su sombra, ni texto, ni caja.
  2. Mail y banners pesan ≤ 1 MB. Si la PNG se pasa, sale JPG de alta calidad.
Sale a out/selfie/prueba/ con el nombre de entrega.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "out/selfie/prueba"
TMP = OUT / "_qa"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FORMATOS = {
    "Post": ("post", "POST", None),
    "Story": ("story", "HISTORIA", None),
    "Mail": ("mail", "MAIL", 1_000_000),
    "BannerDesk": ("bannerDesk", "BANNER_DESK", 1_000_000),
    "BannerMobile": ("bannerMobile", "BANNER_MOBILE", 1_000_000),
}
FONDOS = np.array([[0xFF, 0x43, 0x74], [0xFF, 0x8C, 0x93]], dtype=float)
MARGEN_PX = 10  # holgura alrededor del trazo, en px de salida


def still(comp, destino, formato, capa):
    props = '{"formato":"%s","capa":"%s"}' % (formato, capa)
    r = subprocess.run(
        [str(RAIZ / "node_modules/.bin/remotion"), "still", f"SelfiePruebaBiotop-{comp}", str(destino),
         f"--props={props}", f"--browser-executable={CHROME}", "--log=error"],
        cwd=RAIZ, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-2000:])


def choques(sin, masc):
    m = np.array(Image.open(masc).convert("L").filter(ImageFilter.MaxFilter(2 * MARGEN_PX + 1))) > 40
    px = np.array(Image.open(sin).convert("RGB")).astype(float)[m]
    # distancia al SEGMENTO coral–salmón: el borde antialiasado de la curva es mezcla
    # de los dos fondos y no es un choque
    a, b = FONDOS
    t = np.clip(((px - a) @ (b - a)) / ((b - a) @ (b - a)), 0, 1)
    dist = np.linalg.norm(px - (a + t[:, None] * (b - a)), axis=1)
    malos = int((dist > 14).sum())
    return malos, int(m.sum())


def exporta(png, nombre, tope):
    if tope is None or png.stat().st_size <= tope:
        dest = OUT / f"PRUEBA_BIOTOP_700-911_{nombre}.png"
        dest.write_bytes(png.read_bytes())
        return dest
    im = Image.open(png).convert("RGB")
    for q in (95, 93, 90, 88, 85):
        dest = OUT / f"PRUEBA_BIOTOP_700-911_{nombre}.jpg"
        im.save(dest, quality=q, subsampling=0, optimize=True, progressive=True)
        if dest.stat().st_size <= tope:
            return dest
    return dest


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    pedidos = sys.argv[1:] or list(FORMATOS)
    fallas = 0
    for comp in pedidos:
        formato, nombre, tope = FORMATOS[comp]
        base = TMP / f"{comp}.png"
        still(comp, base, formato, "todo")
        still(comp, TMP / f"{comp}-sin.png", formato, "sinFlechas")
        still(comp, TMP / f"{comp}-masc.png", formato, "flechas")
        malos, total = choques(TMP / f"{comp}-sin.png", TMP / f"{comp}-masc.png")
        dest = exporta(base, nombre, tope)
        peso = dest.stat().st_size / 1e6
        ok_peso = tope is None or dest.stat().st_size <= tope
        estado = "✓" if malos == 0 and ok_peso else "✗"
        fallas += estado == "✗"
        print(f"{estado} {comp:13} flechas: {malos:5d} px chocan de {total}  ·  {dest.name}  {peso:.2f} MB")
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()

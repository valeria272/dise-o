#!/usr/bin/env python3
"""Rinde y controla la prueba Biotop 700 + 911 de Selfie en sus 5 formatos.

    ~/copylab-venv/bin/python3 scripts/selfie-biotop-qa.py            # todo
    ~/copylab-venv/bin/python3 scripts/selfie-biotop-qa.py Mail Post  # algunos

Por formato hace tres renders —la pieza, la pieza SIN flechas y la máscara de las
flechas— y comprueba lo que pidió Coni el 24-09:
  1. NINGUNA flecha toca nada: bajo cada trazo (con margen) sólo puede haber fondo
     plano coral #FF4374 o salmón #FF8C93. Ni frasco, ni su sombra, ni texto, ni caja.
  2. NINGÚN producto se corta: cada frasco queda entero y con ≥ 40 px de mesa a
     cualquier borde (Coni 24-09: «el producto no se puede cortar, se deben ver enteros»).
  3. Mail y banners pesan ≤ 1 MB. Si la PNG se pasa, sale JPG de alta calidad.
Sale a out/selfie/prueba/ con el nombre de entrega.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _selfie_biotop import obstaculos  # noqa: E402
import json  # noqa: E402

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
# campo izquierdo coral #FF4374 y derecho salmón #FF8C93
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


def choques(sin, masc, formato):
    """Píxeles bajo el trazo (con margen) que no son fondo libre. El resplandor de
    las fichas cuenta como fondo; la sombra de los frascos, no (ver _selfie_biotop)."""
    L = json.loads((RAIZ / "src/compositions/selfie/biotop-prueba.json").read_text())[formato]
    m = np.array(Image.open(masc).convert("L").filter(ImageFilter.MaxFilter(2 * MARGEN_PX + 1))) > 40
    obst = obstaculos(np.array(Image.open(sin).convert("RGB")).astype(float), formato, L)
    return int((m & obst).sum()), int(m.sum())


def cortes(formato):
    """Margen mínimo (en px de mesa) de cada frasco a los cuatro bordes."""
    L = json.loads((RAIZ / "src/compositions/selfie/biotop-prueba.json").read_text())[formato]
    u = L["outW"] / L["mesaW"]
    H, W = round(L["alto"] * u), L["outW"]
    peor = []
    for k in ("700", "911"):
        p = L[f"p{k}"]
        im = Image.open(RAIZ / f"public/assets/selfie/2026-nuevo-estilo/biotop/{formato}-{k}.png")
        bb = im.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox()
        x0, y0 = p["cx"] * u - im.width / 2, p["cy"] * u - im.height / 2
        m = min(x0 + bb[0], y0 + bb[1], W - (x0 + bb[2]), H - (y0 + bb[3])) / u
        peor.append((m, k))
    return min(peor)


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
        malos, total = choques(TMP / f"{comp}-sin.png", TMP / f"{comp}-masc.png", formato)
        dest = exporta(base, nombre, tope)
        peso = dest.stat().st_size / 1e6
        ok_peso = tope is None or dest.stat().st_size <= tope
        margen, cual = cortes(formato)
        ok_corte = margen >= 40
        estado = "✓" if malos == 0 and ok_peso and ok_corte else "✗"
        fallas += estado == "✗"
        print(f"{estado} {comp:13} flechas: {malos:5d} px chocan  ·  frasco más al borde: {cual} a {margen:4.0f}  ·  {dest.name}  {peso:.2f} MB")
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()

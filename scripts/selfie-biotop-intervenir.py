#!/usr/bin/env python3
"""PRUEBA aparte (24-09-2026): interviene los frascos Biotop para el post.

    ~/copylab-venv/bin/python3 scripts/selfie-biotop-intervenir.py

Coni: «la tapa es transparente y se ve con fondo blanco; el líquido debería verse con
la inclinación del frasco». Dos intervenciones, calculadas sobre la foto real (sin IA:
la IA ya reescribió estas etiquetas una vez):
  1. TAPA TRANSPARENTE. La carcasa de plástico se pasa de «sobre blanco» a alfa
     (color-a-alfa respecto del blanco): conserva brillos y cantos y deja ver el fondo.
     La bomba esmerilada sale con la misma regla; el anillo metálico queda opaco.
  2. LÍQUIDO A NIVEL. El frasco va girado, la gravedad no: sobre una línea HORIZONTAL
     en el mundo (inclinada en el frasco según su giro) queda una cámara de aire. Ahí se
     le quita el tinte al líquido (vidrio vacío → transparente) y se marca un menisco.
     La tinta blanca impresa de la etiqueta se protege: no se toca ni un píxel de ella.
Sale a public/assets/selfie/2026-nuevo-estilo/biotop/post-<k>-intervenido.png, listo
para SelfiePruebaBiotop-PostIntervenido. NO toca las piezas ya entregadas.
"""
import importlib.util
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "raw/selfie/prueba-biotop"
DEST = RAIZ / "public/assets/selfie/2026-nuevo-estilo/biotop"
spec = importlib.util.spec_from_file_location("prod", RAIZ / "scripts/selfie-biotop-productos.py")
prod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prod)

# geometría medida en la foto de 1000 px (columna central y recortes a 2×)
GEO = {
    "700": {"base": "BP_700_Keratin_Kale_Serum", "anillo": (240, 345, 420, 582)},
    "911": {"base": "BP_911Quinoa_Serum", "anillo": (250, 355, 420, 582)},
}
AIRE_CENTRO = 48  # px de cámara de aire al centro del cuerpo, bajo el anillo


def interviene(k, rot):
    g = GEO[k]
    rgb = np.array(Image.open(FUENTE / f"{g['base']}.webp").convert("RGB")).astype(float)
    alfa = np.array(Image.open(FUENTE / f"{g['base']}-nobg.png").convert("RGBA"))[:, :, 3].astype(float) / 255
    H, W = alfa.shape
    Y, X = np.mgrid[0:H, 0:W]
    a0, a1, ax0, ax1 = g["anillo"]
    dentro = alfa > 0.5
    out_rgb = rgb.copy()
    out_a = alfa.copy()

    # ---- 1. carcasa transparente: UNA sola regla para todo lo que está sobre el cuerpo
    # (plástico y bomba esmerilada), salvo el anillo metálico, que es opaco
    anillo = (Y >= a0) & (Y < a1) & (X >= ax0) & (X < ax1)
    carcasa = dentro & (Y < a1) & ~anillo
    m = rgb.min(2)
    ak = np.clip((252 - m) / (252 - 170), 0.06, 1.0)  # blanco → transparente, cantos → opacos
    col = (rgb - (1 - ak[..., None]) * 255) / ak[..., None]
    out_rgb[carcasa] = np.clip(col[carcasa], 0, 255)
    out_a[carcasa] = ak[carcasa] * alfa[carcasa]

    # ---- 2. cámara de aire con la superficie horizontal EN EL MUNDO
    filas = np.where(dentro.any(1))[0]
    cuerpo = dentro & (Y >= a1)
    xs = np.where(cuerpo.any(0))[0]
    cx = (xs.min() + xs.max()) / 2
    # CSS rotate(θ) horario: y_mundo = x·sinθ + y·cosθ → en el frasco, pendiente −tanθ
    pend = -np.tan(np.radians(rot))
    y_sup = a1 + AIRE_CENTRO + pend * (X - cx)  # línea de la superficie, por columna
    izq = np.full(H, W); der = np.full(H, -1)
    for y in filas:
        c = np.where(cuerpo[y])[0]
        if len(c):
            izq[y], der[y] = c.min(), c.max()
    pared = (X > izq[:, None] + 5) & (X < der[:, None] - 5)
    tinta = (rgb.min(2) > 236) & (Y > a1 + 20)  # tinta blanca impresa por fuera: intocable
    lum = rgb @ np.array([0.30, 0.59, 0.11])
    liq = cuerpo & pared & (Y > y_sup + 40) & ~tinta & (Y < a1 + 260)
    lum_liq = np.median(lum[liq])
    # vidrio vacío = la misma estructura (tubo, impresión del reverso, cantos) sin el
    # color del líquido: gris neutro normalizado a casi blanco, y de ahí a alfa
    g = np.clip(lum / lum_liq * 242, 0, 255)
    va = np.clip((252 - g) / (252 - 120), 0.10, 1.0)
    vg = np.clip((g - (1 - va) * 255) / va, 0, 255)
    peso = np.clip((y_sup - Y) / 3.0, 0, 1) * (cuerpo & pared & ~tinta)  # borde suave
    for c in range(3):
        out_rgb[..., c] = out_rgb[..., c] * (1 - peso) + vg * peso
    out_a = out_a * (1 - peso) + (va * alfa) * peso

    # menisco sutil: canto claro sobre la superficie y leve sombra bajo ella
    d = Y - y_sup
    borde = cuerpo & pared & ~tinta
    claro = borde & (d >= 0) & (d < 2.5)
    out_rgb[claro] = np.clip(rgb[claro] * 0.7 + 255 * 0.3, 0, 255)
    sombra = borde & (d >= 2.5) & (d < 9)
    out_rgb[sombra] = rgb[sombra] * 0.93

    im = Image.fromarray(np.dstack([out_rgb, out_a * 255]).astype(np.uint8), "RGBA")
    # sin el reflejo bajo la base, igual que en la versión entregada
    base_y = np.where((alfa > 0.8).sum(1) > 0.6 * (alfa > 0.8).sum(1).max())[0].max()
    arr = np.array(im)
    arr[base_y + 2:, :, 3] = 0
    im = Image.fromarray(arr, "RGBA")
    return im.crop(im.getchannel("A").point(lambda v: 255 if v > 3 else 0).getbbox())


def main():
    L = json.loads((RAIZ / "src/compositions/selfie/biotop-prueba.json").read_text())["post"]
    u = L["outW"] / L["mesaW"]
    for k in ("700", "911"):
        p = L[f"p{k}"]
        im = interviene(k, p["rot"])
        im.save(FUENTE / f"{k}-intervenido-plano.png")
        out = prod.prepara(im, round(p["h"] * u), p["rot"])
        out.save(DEST / f"post-{k}-intervenido.png", optimize=True)
        print(f"post {k}: intervenido → post-{k}-intervenido.png {out.size}")


if __name__ == "__main__":
    main()

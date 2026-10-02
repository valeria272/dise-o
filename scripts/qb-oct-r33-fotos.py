"""QB · OCT 2026 · r33 — fotos del POST / ST «20 % dcto. almuerzo» (FEED col. D, S1).

Dos tomas CENITALES reales del shooting de la carta (enero 2026), sin IA:
  · post  → «Risotto de camarones al azafrán 3»
  · story → «Trucha arcoíris 4»

Qué se les hace (y nada más):
  1. Se borra el SALERO, que cae detrás del bloque de texto (R-92: lo que estorba
     detrás de un bloque se borra de la foto, no se tapa con negro). Local, sin IA:
     la baja frecuencia sale de un inpaint y el grano se trae de la misma mesa, al
     lado (clonado por separación de frecuencias; un inpaint solo deja parche liso).
  2. La mesa se alarga hacia ARRIBA con la misma mesa (franja limpia reflejada),
     para dejar el aire del texto sin agrandar ni tapar el plato.
  3. Se deja en el tamaño de entrega: 2250×2813 (feed) y 2250×4000 (story).

    python scripts/qb-oct-r33-fotos.py
"""
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "raw/hilton/qb/oct-r33"
OUT = RAIZ / "public/assets/hilton/qb/oct"

# caja del salero (con su sombra) en fracción de la foto, y de dónde se trae el grano
PIEZAS = {
    # r33 (1.ª vuelta): tomas cenitales — Eli 02-10: «usa una foto más instagram y bonita»
    "feed-cenital": dict(src="risotto-3.jpg", salero=(0.265, 0.185, 0.435, 0.335), dx=0.36,
                         sube=60, mesa=(1080, 1350), out="alm20-feed-risotto3.jpg"),
    "story-cenital": dict(src="trucha-4.jpg", salero=(0.250, 0.175, 0.430, 0.330), dx=0.36,
                          sube=525, mesa=(1080, 1920), out="alm20-st-trucha4.jpg"),
    # r34: el brindis de vino blanco sobre la mesa de almuerzo («Ostiones parmesanos a la
    # batayaki 16»: copas, manos, follaje; risotto y trucha abajo). Sin borrar nada.
    "feed": dict(src="brindis-16.jpg", salero=None, dx=0, sube=0, franja=0.26,
                 mesa=(1080, 1350), out="alm20-feed-brindis16.jpg"),
    "story": dict(src="brindis-16.jpg", salero=None, dx=0, sube=300, franja=0.26,
                  mesa=(1080, 1920), out="alm20-st-brindis16.jpg"),
}
ANCHO = 2250
FRANJA_LIMPIA = 0.13  # arriba de esto no hay copa ni salero: es lo que se refleja


def borra_salero(a: np.ndarray, caja, dx) -> np.ndarray:
    h, w = a.shape[:2]
    x0, y0, x1, y1 = int(caja[0] * w), int(caja[1] * h), int(caja[2] * w), int(caja[3] * h)
    mask = np.zeros((h, w), np.uint8)
    cv2.ellipse(mask, ((x0 + x1) // 2, (y0 + y1) // 2), ((x1 - x0) // 2, (y1 - y0) // 2), 0, 0, 360, 255, -1)
    # baja frecuencia: inpaint a 1/8 y de vuelta
    ch = cv2.resize(a, (w // 8, h // 8), interpolation=cv2.INTER_AREA)
    mch = cv2.resize(mask, (w // 8, h // 8), interpolation=cv2.INTER_NEAREST)
    mch = cv2.dilate(mch, np.ones((5, 5), np.uint8))
    baja = cv2.resize(cv2.inpaint(ch, mch, 9, cv2.INPAINT_TELEA), (w, h), interpolation=cv2.INTER_CUBIC)
    baja = cv2.GaussianBlur(baja, (0, 0), 14)
    # alta frecuencia: el grano de la misma mesa, corrida a la derecha
    d = int(dx * w)
    donante = np.roll(a, -d, axis=1).astype(np.float32)
    alta = donante - cv2.GaussianBlur(donante, (0, 0), 14)
    parche = np.clip(baja.astype(np.float32) + alta, 0, 255)
    pluma = cv2.GaussianBlur(cv2.dilate(mask, np.ones((31, 31), np.uint8)), (0, 0), 22).astype(np.float32)[..., None] / 255
    return (a * (1 - pluma) + parche * pluma).astype(np.uint8)


def arma(nombre: str, p: dict) -> None:
    im = ImageOps.exif_transpose(Image.open(RAW / p["src"])).convert("RGB")
    a = np.asarray(im)
    if p["salero"]:
        a = borra_salero(a, p["salero"], p["dx"])
    k = ANCHO / a.shape[1]
    a = cv2.resize(a, (ANCHO, round(a.shape[0] * k)), interpolation=cv2.INTER_AREA)
    esc = ANCHO / p["mesa"][0]
    sube = round(p["sube"] * esc)
    alto = round(p["mesa"][1] * esc)
    if sube < 0:  # la foto sube: se recorta por arriba
        a, sube = a[-sube:], 0
    franja = a[: int(p.get("franja", FRANJA_LIMPIA) * a.shape[0])]
    tiras, falta, vuelta = [], sube, True
    while falta > 0:  # reflejo en espejo, las veces que haga falta
        t = franja[::-1] if vuelta else franja
        tiras.append(t[-falta:] if vuelta else t[:falta])
        falta -= len(tiras[-1]); vuelta = not vuelta
    lienzo = np.vstack(tiras[::-1] + [a])[:alto]
    Image.fromarray(lienzo).save(OUT / p["out"], quality=93, subsampling=0)
    print(f"✓ {p['out']}  {lienzo.shape[1]}×{lienzo.shape[0]}")


# r36 (Eli 02-10: «está demasiado oscuro abajo, no se ve el plato; que el almuerzo con el
# vino destaquen»): toma HORIZONTAL «QB_enero_26-103» (entraña + copa de tinto sobre la mesa
# de madera). Al ser apaisada entra completa —copa, plato y cuchillo— entre el bloque de
# arriba y el grupo de abajo. `esc` = ancho de la foto / ancho de la mesa; `x0` = desde qué
# fracción del ancho se recorta; `top` = dónde cae el borde superior de la foto en la mesa.
BANDAS = {
    "feed": dict(src="entrana-h103.jpg", esc=1.2, x0=0.083, top=320, mesa=(1080, 1350),
                 out="alm20-feed-entrana103.jpg"),
    "story": dict(src="entrana-h103.jpg", esc=1.1, x0=0.07, top=600, mesa=(1080, 1920),
                  out="alm20-st-entrana103.jpg"),
}
FUNDE = 150      # px de mesa en que el borde de arriba de la foto se funde al negro del fondo
FUNDE_PIE = 120  # idem abajo: la mesa se pierde en sombra bajo el grupo de texto.
# ⛔ No se alarga la madera en espejo: los listones van en perspectiva y el reflejo los deja
#    en zigzag (probado el 02-10). La mesa se funde a negro y el texto va sobre esa base.


def arma_banda(p: dict) -> None:
    im = ImageOps.exif_transpose(Image.open(RAW / p["src"])).convert("RGB")
    k = ANCHO / p["mesa"][0]
    w = round(p["mesa"][0] * p["esc"] * k)
    a = cv2.resize(np.asarray(im), (w, round(im.height * w / im.width)), interpolation=cv2.INTER_AREA)
    x = round(p["x0"] * w)
    a = a[:, x:x + ANCHO].astype(np.float32)
    f, g = round(FUNDE * k), round(FUNDE_PIE * k)
    a[:f] *= (np.linspace(0, 1, f) ** 1.5)[:, None, None]
    a[-g:] *= (np.linspace(1, 0, g) ** 1.3)[:, None, None]
    alto, top = round(p["mesa"][1] * k), round(p["top"] * k)
    lienzo = np.zeros((alto, ANCHO, 3), np.float32)
    lienzo[top:top + len(a)] = a[: alto - top]
    Image.fromarray(lienzo.astype(np.uint8)).save(OUT / p["out"], quality=93, subsampling=0)
    print(f"ok {p['out']}  {ANCHO}x{alto}")


if __name__ == "__main__":
    for n, p in BANDAS.items():
        arma_banda(p)

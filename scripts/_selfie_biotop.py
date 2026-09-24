"""Piezas comunes de los scripts de la prueba Biotop de Selfie (flechas y QA)."""
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

RAIZ = Path(__file__).resolve().parent.parent
PROD = RAIZ / "public/assets/selfie/2026-nuevo-estilo/biotop"
# campo izquierdo coral #FF4374 y derecho salmón #FF8C93
FONDOS = np.array([[0xFF, 0x43, 0x74], [0xFF, 0x8C, 0x93]], dtype=float)


def mascara_producto(fmt, k, L, H, W):
    """Alfa del frasco `k` tal como queda puesto en la pieza (px de salida)."""
    u = L["outW"] / L["mesaW"]
    p = L[f"p{k}"]
    im = Image.open(PROD / f"{fmt}-{k}.png")
    al = np.array(im.getchannel("A")) > 40
    x0 = int(round(p["cx"] * u - im.width / 2))
    y0 = int(round(p["cy"] * u - im.height / 2))
    m = np.zeros((H, W), bool)
    ys, xs = np.where(al)
    ok = (ys + y0 >= 0) & (ys + y0 < H) & (xs + x0 >= 0) & (xs + x0 < W)
    m[ys[ok] + y0, xs[ok] + x0] = True
    return m


def obstaculos(px, fmt, L):
    """Todo lo que NO es fondo libre. Fondo libre = coral, salmón o su mezcla en el
    borde de la curva, y también el RESPLANDOR de las fichas (negro en multiplicar
    conserva la proporción del color). La sombra de los frascos NO es fondo libre:
    todo lo que esté a menos de 70·t de un frasco cuenta como frasco."""
    H, W = px.shape[:2]
    u = L["outW"] / L["mesaW"]
    a, b = FONDOS
    t = np.clip(((px - a) @ (b - a)) / ((b - a) @ (b - a)), 0, 1)
    plano = np.linalg.norm(px - (a + t[..., None] * (b - a)), axis=2) <= 14
    # cromaticidad: dividir por el rojo (255 en los dos fondos) quita el oscurecido
    R = np.maximum(px[..., 0:1], 1)
    n = px / R
    na, nb = a / 255, b / 255
    tn = np.clip(((n - na) @ (nb - na)) / ((nb - na) @ (nb - na)), 0, 1)
    tinte = (np.linalg.norm(n - (na + tn[..., None] * (nb - na)), axis=2) <= 0.05) & (px[..., 0] >= 150)
    frascos = mascara_producto(fmt, "700", L, H, W) | mascara_producto(fmt, "911", L, H, W)
    cerca = ndimage.distance_transform_edt(~frascos) < 70 * L["t"] * u
    libre = plano | (tinte & ~cerca)
    return ~libre

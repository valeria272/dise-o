#!/usr/bin/env python3
"""MyZoo · post 20/10 Parque Pet — monta el logo oficial en el stand y lo devuelve a la imagen.

La IA (Nano Banana Pro) rehízo el puesto con la pancarta y el panel EN BLANCO y los
productos sobre el mesón; acá se pone el logo real (PNG oficial) en perspectiva, con
la luz de la escena, y el recorte editado vuelve a la imagen completa con máscara difusa.

Uso: python scripts/myzoo-parquepet-stand.py
"""
import cv2, numpy as np, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
R = RAIZ / "raw/myzoo/2026-10_parquepet"
O = RAIZ / "out/myzoo/octubre-2026/20_parquepet"
LOGO = RAIZ / "public/assets/myzoo/marca/logo.png"
BASE = O / "myzoo_post_parquepet_imagen-limpia_ALTA_3536x4421.png"   # v1, se conserva
X0, Y0, CW, CH = 0, 2180, 1326, 1768                                   # recorte del puesto en la ALTA

# Cuadriláteros medidos sobre stand/ed_7.png (3584x4800): TL, TR, BR, BL
PANCARTA = np.float32([[624, 615], [2329, 1027], [2314, 1467], [624, 1141]])
PANEL    = np.float32([[812, 2975], [2214, 3015], [2176, 4265], [743, 4365]])


def leer(p, flag=cv2.IMREAD_COLOR):
    return cv2.imdecode(np.fromfile(str(p), np.uint8), flag)

def guardar(p, im):
    ok, buf = cv2.imencode(pathlib.Path(p).suffix, im); assert ok
    tmp = pathlib.Path(str(p) + ".tmp"); buf.tofile(str(tmp)); tmp.replace(p)

def montar_logo(img, quad, u0, u1, vc, luz):
    """Pone el logo en el plano `quad` ocupando u0..u1 del ancho y centrado en vc del alto."""
    logo = leer(LOGO, cv2.IMREAD_UNCHANGED)
    lh, lw = logo.shape[:2]
    ancho = np.linalg.norm(quad[1] - quad[0]); alto = np.linalg.norm(quad[3] - quad[0])
    w = (u1 - u0) * ancho; h = w * lh / lw
    v0, v1 = vc - h / alto / 2, vc + h / alto / 2
    plano = cv2.getPerspectiveTransform(np.float32([[0, 0], [1, 0], [1, 1], [0, 1]]), quad)
    dst = cv2.perspectiveTransform(np.float32([[[u0, v0], [u1, v0], [u1, v1], [u0, v1]]]), plano)[0]
    Hm = cv2.getPerspectiveTransform(np.float32([[0, 0], [lw, 0], [lw, lh], [0, lh]]), dst)
    H, W = img.shape[:2]
    wl = cv2.warpPerspective(logo, Hm, (W, H), flags=cv2.INTER_AREA, borderValue=(0, 0, 0, 0))
    wl = cv2.GaussianBlur(wl, (0, 0), 1.6)                    # la foto es blanda: el logo no puede ser más nítido
    a = (wl[..., 3:4].astype(np.float32) / 255.0) * 0.97
    tinta = wl[..., :3].astype(np.float32) * luz              # la luz de la escena sobre la tinta
    return (img.astype(np.float32) * (1 - a) + tinta * a).clip(0, 255).astype(np.uint8)


ed = leer(R / "stand/ed_7.png")
H, W = ed.shape[:2]

# 0 · v3: el mesón se regeneró aparte y más de cerca (stand/me_b.png) con sólo los dos Odor
#     Eliminator, para que la luz, la transparencia y el reflejo salgan del generador.
MX, MY, ML = 300, 1750, 1650
mes = cv2.resize(leer(R / "stand/me_b.png"), (ML, ML), interpolation=cv2.INTER_AREA)
mm = np.zeros((ML, ML), np.float32); mm[60:-60, 60:-60] = 1
mm = cv2.GaussianBlur(mm, (0, 0), 25)[..., None]
ed[MY:MY + ML, MX:MX + ML] = (ed[MY:MY + ML, MX:MX + ML] * (1 - mm) + mes * mm).astype(np.uint8)

# 1 · La pancarta salió gris: se lleva a blanco conservando su sombreado.
m = np.zeros((H, W), np.uint8)
cv2.fillConvexPoly(m, np.int32(PANCARTA + [[6, 8], [-6, 8], [-6, -8], [6, -8]]), 255)
med = np.median(ed[m > 0], axis=0)
blanca = (ed.astype(np.float32) * (np.float32([244, 244, 244]) / med)).clip(0, 255)
mf = cv2.GaussianBlur(m, (0, 0), 3)[..., None].astype(np.float32) / 255
ed = (ed * (1 - mf) + blanca * mf).astype(np.uint8)

# 2 · Logo oficial en la pancarta (centrado).
ed = montar_logo(ed, PANCARTA, 0.36, 0.64, 0.50, luz=0.95)
# v3 (Paulina, 01-10): el panel rosado va SIN logo.
guardar(R / "stand/ed_7_logo.png", ed)

# 3 · El recorte vuelve a la imagen completa: sólo la zona del puesto, con borde difuso.
base = leer(BASE)
chico = cv2.resize(ed, (CW, CH), interpolation=cv2.INTER_AREA)
orig = base[Y0:Y0 + CH, X0:X0 + CW]
masc = np.zeros((CH, CW), np.float32)
x1, x2, y1, y2 = int(.03 * CW), int(.665 * CW), int(.07 * CH), int(.945 * CH)
masc[y1:y2, x1:x2] = 1
masc = cv2.GaussianBlur(masc, (0, 0), 14)[..., None]
fuera = (masc[..., 0] < 0.01)
print("diferencia media fuera del puesto (0-255):", round(float(np.abs(chico.astype(int) - orig.astype(int))[fuera].mean()), 2))
base[Y0:Y0 + CH, X0:X0 + CW] = (orig * (1 - masc) + chico * masc).astype(np.uint8)

guardar(O / "myzoo_post_parquepet_imagen-limpia_v3_ALTA_3536x4421.png", base)
guardar(O / "myzoo_post_parquepet_imagen-limpia_v3_2250x2813.png", cv2.resize(base, (2250, 2813), interpolation=cv2.INTER_AREA))
guardar(R / "stand/_v3_ver.jpg", cv2.resize(base, (900, 1125), interpolation=cv2.INTER_AREA))
guardar(R / "stand/_v3_zoom.jpg", base[Y0 + 60:Y0 + 1700, 0:1300])
print("listo")

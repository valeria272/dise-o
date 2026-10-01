#!/usr/bin/env python3
"""MyZoo · post 20/10 Parque Pet — opción «perros de pie»: recorta a 4:5 y monta el logo
oficial, chico, en el letrero en blanco de una de las carpas (MyZoo como un stand más).

Uso: python scripts/myzoo-parquepet-depie.py
"""
import cv2, numpy as np, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
R = RAIZ / "raw/myzoo/2026-10_parquepet/v4"
O = RAIZ / "out/myzoo/octubre-2026/20_parquepet"
LOGO = RAIZ / "public/assets/myzoo/marca/logo.png"
# Letrero blanco de la carpa de la izquierda, medido sobre s_b_2x.png (3536x4720): TL, TR, BR, BL
LETRERO = np.float32([[298, 3154], [478, 3184], [476, 3282], [296, 3242]])

def leer(p, flag=cv2.IMREAD_COLOR):
    return cv2.imdecode(np.fromfile(str(p), np.uint8), flag)

def guardar(p, im):
    ok, buf = cv2.imencode(pathlib.Path(p).suffix, im); assert ok
    tmp = pathlib.Path(str(p) + ".tmp"); buf.tofile(str(tmp)); tmp.replace(p)

img = leer(R / "s_b_2x.png"); H, W = img.shape[:2]
logo = leer(LOGO, cv2.IMREAD_UNCHANGED); lh, lw = logo.shape[:2]
ancho = np.linalg.norm(LETRERO[1] - LETRERO[0]); alto = np.linalg.norm(LETRERO[3] - LETRERO[0])
h = 0.80; w = h * alto * lw / lh / ancho                      # el logo ocupa el 80 % del alto del letrero
u0, u1, v0, v1 = 0.5 - w / 2, 0.5 + w / 2, 0.5 - h / 2, 0.5 + h / 2
plano = cv2.getPerspectiveTransform(np.float32([[0, 0], [1, 0], [1, 1], [0, 1]]), LETRERO)
dst = cv2.perspectiveTransform(np.float32([[[u0, v0], [u1, v0], [u1, v1], [u0, v1]]]), plano)[0]
Hm = cv2.getPerspectiveTransform(np.float32([[0, 0], [lw, 0], [lw, lh], [0, lh]]), dst)
wl = cv2.GaussianBlur(cv2.warpPerspective(logo, Hm, (W, H), flags=cv2.INTER_AREA), (0, 0), 1.4)
a = wl[..., 3:4].astype(np.float32) / 255 * 0.95
img = (img * (1 - a) + wl[..., :3].astype(np.float32) * 0.92 * a).clip(0, 255).astype(np.uint8)

alto45 = round(W * 2813 / 2250); corte = H - alto45              # se recorta cielo, no patas
img = img[corte:corte + alto45]
guardar(O / "_descartadas" / f"myzoo_post_parquepet_imagen-limpia_opcion2-depie_ALTA_{W}x{alto45}.png", img)
guardar(O / "_descartadas" / "myzoo_post_parquepet_imagen-limpia_opcion2-depie_2250x2813.png", cv2.resize(img, (2250, 2813), interpolation=cv2.INTER_AREA))
v = cv2.resize(img, (900, 1125), interpolation=cv2.INTER_AREA); cv2.line(v, (0, int(1125 * .46)), (900, int(1125 * .46)), (90, 0, 255), 2)
guardar(R / "_final_ver.jpg", v)
guardar(R / "_final_logo.jpg", img[2832 - corte - 150:2832 - corte + 900, 0:1200])
print("listo", img.shape)

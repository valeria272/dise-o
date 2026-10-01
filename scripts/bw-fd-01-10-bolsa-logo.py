"""BETWEEN · FEED 01-10 carrusel To Go — calza el logotipo vigente sobre la bolsa blanca, EN PERSPECTIVA.

Cliente, grilla FEED E15 (01-10): «en la G4 debemos poner logo Between a la bolsa, les dejo ejemplo
de bolsa que se usa, debe ser con logo actual». La escena trae la bolsa EN BLANCO: la IA no escribe
el logotipo (R-49), se calza el archivo de marca en café #675B49.

Eli, 01-10 (tarde): «el logo tiene que verse más realista en perspectiva de la bolsa». La primera
versión sólo giraba el logo; ahora se le dan las CUATRO esquinas de la cara frontal de la bolsa y el
logo se proyecta con esa homografía: fuga, se achica hacia el lado que se aleja y sigue la
inclinación de los bordes. Va multiplicado sobre el papel (hereda sombra, pliegues y grano) y con el
desenfoque de la foto.

    py scripts/bw-fd-01-10-bolsa-logo.py <escena> <salida.jpg> "x,y x,y x,y x,y" [u v ancho] [--guia]
        esquinas de la cara frontal: arriba-izq, arriba-der, abajo-der, abajo-izq (px de la escena)
        u, v   = centro del logo dentro de la cara, de 0 a 1 (por omisión 0.5 0.5)
        ancho  = ancho del logo como fracción del ancho de la cara (por omisión 0.5)
        --guia = dibuja la cara y la caja del logo en rojo, para comprobar el calce
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
arg = [a for a in sys.argv[1:] if a != "--guia"]
guia = "--guia" in sys.argv
src, out = arg[0], arg[1]
cara = np.array([[float(n) for n in p.split(",")] for p in arg[2].split()], np.float32)
u, v, frac = (float(arg[3]), float(arg[4]), float(arg[5])) if len(arg) > 5 else (0.5, 0.5, 0.5)

esc = np.asarray(Image.open(src).convert("RGB")).astype(np.float32) / 255
H, W = esc.shape[:2]
logo = Image.open(RAIZ / "public/assets/hilton/between/logo-cafe-marca.png").convert("RGBA")
logo = logo.crop(logo.getchannel("A").getbbox())

# La cara de la bolsa como un plano de proporción real: ancho = promedio de sus bordes de arriba y
# abajo, alto = promedio de los laterales. El logo se dibuja plano ahí y recién después se proyecta.
ancho_c = (np.linalg.norm(cara[1] - cara[0]) + np.linalg.norm(cara[2] - cara[3])) / 2
alto_c = (np.linalg.norm(cara[3] - cara[0]) + np.linalg.norm(cara[2] - cara[1])) / 2
PW, PH = int(ancho_c * 2), int(alto_c * 2)  # plano a 2× para que la proyección no pierda filo
lw = int(PW * frac)
lh = int(lw * logo.height / logo.width)
plano = np.zeros((PH, PW), np.float32)
x0, y0 = int(PW * u - lw / 2), int(PH * v - lh / 2)
plano[y0:y0 + lh, x0:x0 + lw] = np.asarray(logo.resize((lw, lh), Image.LANCZOS).getchannel("A")).astype(np.float32) / 255
M = cv2.getPerspectiveTransform(np.array([[0, 0], [PW, 0], [PW, PH], [0, PH]], np.float32), cara)
alfa = cv2.warpPerspective(plano, M, (W, H), flags=cv2.INTER_AREA)
alfa = cv2.GaussianBlur(alfa, (0, 0), max(0.8, ancho_c * frac / 850))  # la nitidez de la foto, no la del vector
alfa = (alfa * 0.9)[..., None]  # tinta impresa: no tapa del todo el papel
tinta = np.array([0x67, 0x5B, 0x49], np.float32) / 255
res = esc * (1 - alfa) + esc * tinta * alfa  # multiplicar: la sombra del papel pasa por la tinta
sal = (np.clip(res, 0, 1) * 255).astype(np.uint8)
if guia:
    sal = np.ascontiguousarray(sal)
    cv2.polylines(sal, [cara.astype(np.int32)], True, (255, 0, 0), 6)
    caja = cv2.perspectiveTransform(np.array([[[x0, y0], [x0 + lw, y0], [x0 + lw, y0 + lh], [x0, y0 + lh]]], np.float32), M)
    cv2.polylines(sal, [caja[0].astype(np.int32)], True, (255, 0, 0), 3)
Path(out).parent.mkdir(parents=True, exist_ok=True)
Image.fromarray(sal).save(out, quality=93)
print("ok", out, f"cara {ancho_c:.0f}×{alto_c:.0f} px · logo {ancho_c * frac:.0f} px de ancho")

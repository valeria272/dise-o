#!/usr/bin/env python3
"""MyZoo · post 20/10 Parque Pet, opción «perros de pie» — limpia la gente y los perros del fondo.

Paulina (01-10-2026): «la gente del fondo y animales tienen malformaciones». El fondo se
rehízo por zonas con Nano Banana Pro (recortes cerrados → más píxeles por persona) y acá
cada zona vuelve a la imagen SÓLO donde cambió: los dos perros principales, el cielo y
el letrero con el logo oficial quedan con sus píxeles originales.

Uso: python scripts/myzoo-parquepet-depie-fondo.py
"""
import cv2, numpy as np, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
V = RAIZ / "raw/myzoo/2026-10_parquepet/v4"
O = RAIZ / "out/myzoo/octubre-2026/20_parquepet"
BASE = O / "_descartadas" / "myzoo_post_parquepet_imagen-limpia_opcion2-depie_ALTA_3536x4421.png"
# zona editada → (x, y, lado) en la imagen ALTA
ZONAS = {"t0_e.png": (0, 2500, 1200), "t1_c.png": (1450, 2650, 900), "t2_d.png": (2400, 2500, 1136)}
LETRERO = (286, 2846, 488, 2988)          # x0, y0, x1, y1 en la ALTA: no se toca

def leer(p):
    return cv2.imdecode(np.fromfile(str(p), np.uint8), cv2.IMREAD_COLOR)

def guardar(p, im):
    ok, buf = cv2.imencode(pathlib.Path(p).suffix, im); assert ok
    tmp = pathlib.Path(str(p) + ".tmp"); buf.tofile(str(tmp)); tmp.replace(p)

img = leer(BASE); antes = img.copy()
for nombre, (x, y, L) in ZONAS.items():
    ed = cv2.resize(leer(V / nombre), (L, L), interpolation=cv2.INTER_AREA).astype(np.float32)
    orig = img[y:y + L, x:x + L].astype(np.float32)
    dif = cv2.GaussianBlur(np.abs(ed - orig).mean(2), (0, 0), 5)
    igual = dif < np.percentile(dif, 40)                       # lo que no cambió sirve para igualar el tono
    for c in range(3):
        g, b = np.polyfit(ed[..., c][igual], orig[..., c][igual], 1)
        ed[..., c] = ed[..., c] * g + b
    dif = cv2.GaussianBlur(np.abs(ed - orig).mean(2), (0, 0), 5)
    m = (dif > 13).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((41, 41), np.uint8))
    m = cv2.dilate(m, np.ones((31, 31), np.uint8)).astype(np.float32)
    borde = np.zeros((L, L), np.float32); borde[30:-30, 30:-30] = 1
    if x == 0: borde[30:-30, :30] = 1
    if x + L >= img.shape[1]: borde[30:-30, -30:] = 1
    m *= borde
    m = cv2.GaussianBlur(m, (0, 0), 10)
    # El letrero se protege DESPUÉS del difuminado y con borde corto: con el borde largo
    # la cabeza de la clienta, que queda justo debajo, salía medio transparente.
    lx0, ly0, lx1, ly1 = LETRERO
    prot = np.zeros((L, L), np.float32)
    prot[max(ly0 - y, 0):max(ly1 - y, 0), max(lx0 - x, 0):max(lx1 - x, 0)] = 1
    m = (m * (1 - cv2.GaussianBlur(prot, (0, 0), 2.5)))[..., None]
    print(nombre, "cubre", round(float(m.mean()) * 100), "% de la zona")
    img[y:y + L, x:x + L] = (orig * (1 - m) + ed * m).clip(0, 255).astype(np.uint8)

# Paulina (01-10, última ronda): «elimina el logo de MyZoo del stand». El letrero vuelve a
# quedar en blanco, tal como salió de la generación (s_b_2x.png, antes de montar el logo).
limpia = leer(V / "s_b_2x.png"); corte = limpia.shape[0] - img.shape[0]
lx0, ly0, lx1, ly1 = LETRERO
ml = np.zeros(img.shape[:2], np.float32); ml[ly0 + 4:ly1 - 4, lx0 + 4:lx1 - 4] = 1
ml = cv2.GaussianBlur(ml, (0, 0), 2)[..., None]
img = (img * (1 - ml) + limpia[corte:] * ml).clip(0, 255).astype(np.uint8)

# Repaso «¿qué se ve muy IA?» (01-10): 1) pecho y patas del beagle, lisos y gruesos → se
# rehicieron en un recorte (bg.png → bg_a.png) y vuelven sólo dentro del perro.
bx, by, bL = 1800, 2921, 1500
ed = cv2.resize(leer(V / "bg_a.png"), (bL, bL), interpolation=cv2.INTER_AREA).astype(np.float32)
orig = img[by:by + bL, bx:bx + bL].astype(np.float32)
mb = (cv2.GaussianBlur(np.abs(ed - orig).mean(2), (0, 0), 5) > 9).astype(np.uint8)
mb = cv2.dilate(cv2.morphologyEx(mb, cv2.MORPH_CLOSE, np.ones((61, 61), np.uint8)), np.ones((25, 25), np.uint8)).astype(np.float32)
caja = np.zeros((bL, bL), np.float32); caja[110:-25, 230:1190] = 1          # sólo la zona del beagle
mb = cv2.GaussianBlur(mb * caja, (0, 0), 12)
mb *= np.clip((np.arange(bL, dtype=np.float32)[:, None] - 60) / 200, 0, 1)  # entra suave desde arriba
mb = mb[..., None]
img[by:by + bL, bx:bx + bL] = (orig * (1 - mb) + ed * mb).clip(0, 255).astype(np.uint8)

# 2) cositas sueltas que delatan: cabinas del teleférico con forma de tambor, una mancha
#    blanca flotando en el cerro, un pilar rosado y una rama cortada en el borde izquierdo.
quita = np.zeros(img.shape[:2], np.uint8)
for cx, cy, r in [(3175, 2158, 26), (3249, 2176, 26), (3502, 2244, 28), (2844, 2180, 20), (2407, 2318, 30), (1875, 2380, 18)]:
    cv2.circle(quita, (cx, cy), r, 255, -1)
quita[2240:2350, 0:50] = 255
img = cv2.inpaint(img, quita, 7, cv2.INPAINT_TELEA)

guardar(O / "myzoo_post_parquepet_perros-de-pie_ALTA_3536x4421.png", img)
guardar(O / "myzoo_post_parquepet_perros-de-pie_2250x2813.png", cv2.resize(img, (2250, 2813), interpolation=cv2.INTER_AREA))
guardar(V / "_fondo_ver.jpg", cv2.resize(img, (900, 1125), interpolation=cv2.INTER_AREA))
guardar(V / "_fondo_izq.jpg", img[2500:3700, 0:1300])
guardar(V / "_fondo_cen.jpg", img[2600:3600, 1350:2450])
guardar(V / "_fondo_der.jpg", img[2500:3650, 2300:3536])
guardar(V / "_rep_beagle.jpg", cv2.resize(img[2700:4421, 1850:3150], (906, 1200)))
guardar(V / "_rep_cerro.jpg", cv2.resize(img[1900:2700, 1800:3536], (1300, 599)))

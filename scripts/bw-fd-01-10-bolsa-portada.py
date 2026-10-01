"""BETWEEN · FEED 01-10 carrusel To Go — la bolsa de la ÚLTIMA lámina pasa a ser la de la PORTADA.

Eli, 01-10 (r21): «la última slide del carrusel, ajusta la bolsa, no se parece a la de la portada».
La n°5 traía una bolsa apaisada con las asas caídas (5h-a); la portada (0h-b), la bolsa vertical con
las asas de papel torcido paradas. No se le describe la bolsa a la IA: se le da la GEOMETRÍA (R-186).

    py scripts/bw-fd-01-10-bolsa-portada.py lienzo   → refs-gen/gen-fd01-n6-lienzo.jpg
        la bolsa de la portada, recortada, pegada a su tamaño y lugar sobre la n5; lo que sobra de la
        bolsa vieja queda en gris para que la IA lo rellene (muro y mesa).
    py scripts/bw-fd-01-10-bolsa-portada.py final <gen.png>   → gen/gen-fd01-n6-final.png
        iguala el color de la tirada a la n5 y devuelve los píxeles ORIGINALES fuera de la bolsa.
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
G = RAIZ / "raw/hilton/between/oct/gen"
REFS = RAIZ / "raw/hilton/between/oct/refs-gen"
W, H = 3712, 4608

# bolsa de la portada (0h-b): punta de las asas y=1239, canto izquierdo x≈1842, hasta donde la tapa el sándwich
PX0, PY0, PX1, PY1 = 1820, 1225, 3505, 3180
ESC = 0.935          # la punta de las asas queda en y=1470: bajo la fila de precios (≈1365)
DX, DY = 1850, 1470  # dónde caen (1842, 1239) de la portada
GRIS = (128, 128, 128)


def blanco(a):
    a = a.astype(np.int32)
    return ((a.min(2) > 172) & ((a.max(2) - a.min(2)) < 30)).astype(np.uint8)


def mascaras():
    n5 = np.asarray(Image.open(G / "gen-fd01-n5-final.png").convert("RGB"))
    port = np.asarray(Image.open(G / "gen-fd01-0h-b.png").convert("RGB"))
    # bolsa de la portada: el cuerpo se cierra (pliegues y sombras), las asas no (se ve el muro entre ellas)
    m = blanco(port)
    m[:PY0], m[PY1:], m[:, :PX0], m[:, PX1:] = 0, 0, 0, 0
    cuerpo = m.copy()
    cuerpo[:1900] = 0
    cuerpo = cv2.morphologyEx(cuerpo, cv2.MORPH_CLOSE, np.ones((61, 61), np.uint8))
    m = np.maximum(m, cuerpo)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    m = (lab == 1 + st[1:, cv2.CC_STAT_AREA].argmax()).astype(np.uint8)
    rec = np.dstack([port, m * 255])[PY0:PY1, PX0:PX1]
    rec = cv2.resize(rec, None, fx=ESC, fy=ESC, interpolation=cv2.INTER_AREA)
    x0, y0 = round(DX + (PX0 - 1842) * ESC), round(DY + (PY0 - 1239) * ESC)
    nueva = np.zeros((H, W), np.float32)
    nueva[y0:y0 + rec.shape[0], x0:x0 + rec.shape[1]] = rec[..., 3] / 255
    capa = np.zeros((H, W, 3), np.uint8)
    capa[y0:y0 + rec.shape[0], x0:x0 + rec.shape[1]] = rec[..., :3]
    # bolsa vieja de la n5: lo blanco a la derecha del vaso o sobre su tapa (no el papel del sándwich)
    v = blanco(n5)
    yy, xx = np.mgrid[:H, :W]
    borde_vaso = 1700 - (yy - 2100) * 0.08  # el vaso se angosta hacia abajo
    v[(yy < 1440) | (yy > 3790) | (xx < 1400) | ((xx < borde_vaso) & (yy > 2010)) | ((xx < 1960) & (yy > 3440))] = 0
    v = cv2.dilate(v, np.ones((25, 25), np.uint8))
    return n5, capa, nueva, v, y0 + rec.shape[0]


if sys.argv[1] == "lienzo":
    n5, capa, nueva, vieja, corte = mascaras()
    out = n5.copy()
    # debajo del corte (donde la portada trae el sándwich) se conserva la n5: papel blanco de la bolsa + muffin
    xs = np.where(nueva[corte - 5] > 0.5)[0]
    franja = np.zeros((H, W), bool)
    franja[corte:3520, xs.min():xs.max()] = True
    sobra = (vieja > 0) & (nueva < 0.5) & ~franja
    out[sobra] = GRIS
    a = cv2.GaussianBlur(nueva, (0, 0), 1.2)[..., None]
    out = (out * (1 - a) + capa * a).astype(np.uint8)
    REFS.mkdir(parents=True, exist_ok=True)
    Image.fromarray(out).save(REFS / "gen-fd01-n6-lienzo.jpg", quality=95)
    print("ok lienzo · bolsa nueva x", xs.min(), xs.max(), "· corte y", corte)

if sys.argv[1] == "final":
    n5, capa, nueva, vieja, corte = mascaras()
    gen = np.asarray(Image.open(sys.argv[2]).convert("RGB").resize((W, H), Image.LANCZOS)).astype(np.float32)
    zona = cv2.dilate(np.maximum((nueva > 0.5).astype(np.uint8), vieja), np.ones((121, 121), np.uint8))
    xs = np.where(nueva[corte - 5] > 0.5)[0]
    zona[corte - 60:3600, xs.min() - 80:xs.max() + 80] = 1
    fuera = zona == 0
    gan = n5[fuera].astype(np.float32).mean(0) / gen[fuera].mean(0)
    print("diferencia fuera de la zona:", np.abs(n5[fuera] - gen[fuera]).mean(0).round(1), "· ganancia", gan.round(3))
    gen = np.clip(gen * gan, 0, 255)
    a = cv2.GaussianBlur(zona.astype(np.float32), (0, 0), 22)[..., None]
    Image.fromarray((n5 * (1 - a) + gen * a).astype(np.uint8)).save(G / "gen-fd01-n6-final.png")
    print("ok gen-fd01-n6-final.png")

# ── r21, segunda vuelta ───────────────────────────────────────────────────────────────────────────
# Con las zonas grises la IA integró bien la bolsa de la portada (n6-a) pero la AGRANDÓ: las asas
# llegaban a y≈930 (canvas 272), encima de la fila de precios. Se separa en dos pasos sin margen:
#   1. `gen-fd01-n6-fondo-a.png` = la n5 SIN bolsa (misma escena, una sola instrucción);
#   2. la bolsa ya integrada de la n6-a se recorta, se achica a 0,80 con ancla en la mesa y se pega
#      sobre ese fondo DETRÁS del muffin; la IA sólo integra (sombra de contacto), sin mover nada.
# r22 (Eli: «la bolsita un poco más grande y ok»): 0,80 → 0,88. Las asas no pueden subir (fila de precios),
# así que el ancla va bajo la mesa: la punta queda en y≈1430 (canvas 419) y la bolsa crece hacia abajo y a los lados.
ANCLA, ESC2 = (2480, 5112), 0.88   # r21: (2480, 3600), 0.80 → punta en 1462 (canvas 428)


def igualar(img, ref, donde):
    return np.clip(img * (ref[donde].mean(0) / img[donde].mean(0)), 0, 255)


def bolsa_n6():
    n5 = np.asarray(Image.open(G / "gen-fd01-n5-final.png").convert("RGB")).astype(np.float32)
    fondo = np.asarray(Image.open(G / "gen-fd01-n6-fondo-a.png").convert("RGB")).astype(np.float32)
    a = np.asarray(Image.open(G / "gen-fd01-n6-a.png").convert("RGB")).astype(np.float32)
    lejos = np.zeros((H, W), bool)
    lejos[:800], lejos[3900:] = True, True       # muro de arriba y mesa de abajo: iguales en las tres
    fondo, a = igualar(fondo, n5, lejos), igualar(a, n5, lejos)
    dif = np.abs(a - fondo).max(2)
    clara = (a.min(2) > 120) & ((a.max(2) - a.min(2)) < 45)
    m = ((dif > 28) & clara).astype(np.uint8)
    m[:, :1700] = 0
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    cuerpo = m.copy()
    cuerpo[:1620] = 0                             # sobre el cuerpo sólo van las asas: no se cierran
    cuerpo = cv2.morphologyEx(cuerpo, cv2.MORPH_CLOSE, np.ones((41, 41), np.uint8))
    m = np.maximum(m, cuerpo)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    m = (lab == 1 + st[1:, cv2.CC_STAT_AREA].argmax()).astype(np.uint8)
    # el hueco del muffin: casco convexo del cuerpo menos la bolsa
    pts = cv2.findNonZero((m * (np.arange(H)[:, None] > 1700)).astype(np.uint8))
    casco = np.zeros((H, W), np.uint8)
    cv2.fillConvexPoly(casco, cv2.convexHull(pts), 1)
    muffin = ((casco == 1) & (m == 0) & (np.arange(H)[:, None] > 2700)).astype(np.uint8)
    muffin = cv2.morphologyEx(muffin, cv2.MORPH_OPEN, np.ones((15, 15), np.uint8))
    llena = cv2.inpaint(a.astype(np.uint8), cv2.dilate(muffin, np.ones((9, 9), np.uint8)), 9, cv2.INPAINT_TELEA)
    return n5, fondo, llena, np.maximum(m, muffin), muffin


if sys.argv[1] == "lienzo2":
    n5, fondo, llena, m, muffin = bolsa_n6()
    M = np.float32([[ESC2, 0, ANCLA[0] * (1 - ESC2)], [0, ESC2, ANCLA[1] * (1 - ESC2)]])
    capa = cv2.warpAffine(llena, M, (W, H), flags=cv2.INTER_AREA)
    alfa = cv2.warpAffine(m.astype(np.float32), M, (W, H), flags=cv2.INTER_AREA)
    alfa = cv2.GaussianBlur(alfa, (0, 0), 1.0)
    # el muffin real queda DELANTE: se saca del alfa lo que en el fondo es muffin (más oscuro que el papel)
    yy, xx = np.mgrid[:H, :W]
    front = ((fondo.max(2) < 125) & (fondo[..., 0] >= fondo[..., 1]) & (yy > 3080) & (xx > 2030) & (xx < 2950)).astype(np.uint8)
    front = cv2.morphologyEx(front, cv2.MORPH_CLOSE, np.ones((45, 45), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(front)
    front = (lab == 1 + st[1:, cv2.CC_STAT_AREA].argmax()).astype(np.float32)
    alfa = alfa * (1 - cv2.GaussianBlur(front, (0, 0), 1.5))
    alfa = alfa[..., None]
    out = fondo * (1 - alfa) + capa * alfa
    ys, xs = np.where(alfa[..., 0] > 0.5)
    print("bolsa pegada: x %d–%d · y %d–%d (canvas y %d–%d)" % (xs.min(), xs.max(), ys.min(), ys.max(), ys.min() / 3.413, ys.max() / 3.413))
    Image.fromarray(out.astype(np.uint8)).save(REFS / "gen-fd01-n6-lienzo2.jpg", quality=95)
    Image.fromarray((alfa[..., 0] * 255).astype(np.uint8)).save(REFS / "gen-fd01-n6-lienzo2-alfa.png")

if sys.argv[1] == "final2":
    # py scripts/bw-fd-01-10-bolsa-portada.py final2 <gen-fd01-n6-int-X.png>  → gen/gen-fd01-n6-final.png
    # Fuera de la bolsa vuelven los píxeles ORIGINALES de la n5 (vaso, sándwich, muffin, mesa, muro);
    # la sombra del muffin sobre el papel se deja a la mitad (la tirada la trae muy cargada).
    n5 = np.asarray(Image.open(G / "gen-fd01-n5-final.png").convert("RGB")).astype(np.float32)
    lz = np.asarray(Image.open(REFS / "gen-fd01-n6-lienzo2.jpg").convert("RGB")).astype(np.float32)
    alfa = np.asarray(Image.open(REFS / "gen-fd01-n6-lienzo2-alfa.png")).astype(np.float32) / 255
    gen = np.asarray(Image.open(sys.argv[2]).convert("RGB").resize((W, H), Image.LANCZOS)).astype(np.float32)
    lejos = np.zeros((H, W), bool)
    lejos[:800], lejos[3900:] = True, True
    mesa = np.zeros((H, W), bool)
    mesa[4100:] = True  # se iguala sólo con la mesa: con el muro el blanco del papel se va a verde
    print('ganancia', (n5[mesa].mean(0) / gen[mesa].mean(0)).round(3))
    gen = igualar(gen, n5, mesa)
    yy, xx = np.mgrid[:H, :W]
    vieja = blanco(n5)
    vieja[(yy < 1440) | (yy > 3790) | (xx < 1400) | ((xx < 1700 - (yy - 2100) * 0.08) & (yy > 2010)) | ((xx < 1960) & (yy > 3440))] = 0
    zona = cv2.dilate(np.maximum(vieja, (alfa > 0.5).astype(np.uint8)), np.ones((141, 141), np.uint8))
    # la sombra del muffin: dentro del papel, mitad tirada y mitad lienzo
    dentro = cv2.GaussianBlur(cv2.erode((alfa > 0.5).astype(np.uint8), np.ones((91, 91), np.uint8)).astype(np.float32), (0, 0), 20)[..., None]
    mez = gen * (1 - 0.5 * dentro) + lz * (0.5 * dentro)
    mez[..., 0] *= 1 + 0.05 * alfa  # el papel salía frío y verdoso (214·225·224): al blanco de la portada
    mez[..., 2] *= 1 + 0.025 * alfa
    z = cv2.GaussianBlur(zona.astype(np.float32), (0, 0), 24)[..., None]
    out = n5 * (1 - z) + mez * z
    # el muffin ORIGINAL delante: arriba se recorta contra la bolsa vieja (blanca), abajo contra la mesa
    caja = (xx > 2065) & (xx < 2980)  # r22: a la izquierda de 2065 asomaba el canto de la bolsa vieja
    arriba = (blanco(n5) == 0) & caja & (yy > 2650) & (yy < 3520)
    abajo = (n5.max(2) < 125) & (n5[..., 0] >= n5[..., 1]) & caja & (yy >= 3520) & (yy < 4080)
    # r22: con la bolsa más abajo, las marcas oscuras de la mesa pegadas al muffin asomaban sobre el papel
    abajo = cv2.morphologyEx(abajo.astype(np.uint8), cv2.MORPH_OPEN, np.ones((41, 41), np.uint8)).astype(bool)
    k = cv2.morphologyEx((arriba | abajo).astype(np.uint8), cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    k = cv2.morphologyEx(k, cv2.MORPH_CLOSE, np.ones((35, 35), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(k)
    k = (lab == 1 + st[1:, cv2.CC_STAT_AREA].argmax()).astype(np.uint8)
    print("muffin: desvío de la tirada respecto del original %.1f · fuera de la zona %.1f" % (
        np.abs(gen - n5)[k == 1].mean(), np.abs(gen - n5)[zona == 0].mean()))
    k = cv2.GaussianBlur(cv2.erode(k, np.ones((7, 7), np.uint8)).astype(np.float32), (0, 0), 1.6)[..., None]
    out = out * (1 - k) + n5 * k
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(G / "gen-fd01-n6-final.png")
    print("ok gen-fd01-n6-final.png")

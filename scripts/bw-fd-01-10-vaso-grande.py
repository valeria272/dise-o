"""BETWEEN · FEED 01-10 carrusel To Go, lámina «café + opción dulce» — deja el vaso en el tamaño GRANDE.

Eli, 01-10: «en el café + dulce el vaso que sea más grande, como la opción de café Grande, ya que no
se ve la diferencia con el chico, que sería el del slide de café + sándwich».
La edición `gen-fd01-3g-b` cambió el vaso pero lo dejó con alto/tapa 1,83 (casi el XL, 1,87) y la
tapa se metía en la fila de precios; y la API se quedó sin créditos («Error consuming credits») antes
de poder corregirla. El Grande es 1,21× el mediano con la misma tapa → alto/tapa ≈ 1,61.

Sin IA: al vaso se le saca una franja de cartón LISO entre la tapa y el logotipo (el logo no se
deforma), la parte de arriba baja y se angosta lo que pide la conicidad, y donde estaba queda el muro
de la escena original `gen-fd01-3-a` (la edición no movió nada más: se comprueba).

    py scripts/bw-fd-01-10-vaso-grande.py   →  raw/hilton/between/oct/gen/gen-fd01-3g-grande.png
"""
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
G = RAIZ / "raw/hilton/between/oct/gen"
A = np.asarray(Image.open(RAIZ / "public/assets/hilton/between/oct/gen/gen-fd01-3-a.jpg").convert("RGB")).astype(np.float32)
B = np.asarray(Image.open(G / "gen-fd01-3g-b.png").convert("RGB")).astype(np.float32)
H, W = B.shape[:2]
dif = np.abs(A - B).mean(2)
print("la edición no movió el resto: diferencia media fuera del vaso =", round(float(dif[:, :900].mean()), 1),
      "(izq) ·", round(float(dif[:, 2800:].mean()), 1), "(der)")

# silueta del vaso nuevo sobre el muro (arriba del vaso viejo): donde B se aparta de A.
# Borde fino (sin dilatar) y suavizado a lo largo del vaso: una máscara ancha arrastra un filo de muro.
m = cv2.GaussianBlur(dif, (0, 0), 2) > 20
filas = np.where(cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))[:, 1000:2800].sum(1) > 300)[0]
tope = int(filas.min())
ys = list(range(tope, 2150))
izq = np.array([1000 + np.where(m[y, 1000:2800])[0].min() for y in ys], np.float32)
der = np.array([1000 + np.where(m[y, 1000:2800])[0].max() for y in ys], np.float32)
izq, der = (cv2.medianBlur(v.reshape(-1, 1), 5).ravel() for v in (izq, der))
izq = cv2.blur(izq.reshape(-1, 1), (1, 25)).ravel()
der = cv2.blur(der.reshape(-1, 1), (1, 25)).ravel()
bordes = {y: (int(round(a)) + 3, int(round(b)) - 3) for y, a, b in zip(ys, izq, der)}
tapa = max(b - a for a, b in bordes.values())
base = 3418  # borde inferior del vaso, medido con regla sobre la toma (debajo hay papel, vigilante y brownie)
alto = base - tope
print(f"vaso: tope {tope} · base {base} · alto {alto} · tapa {tapa} · alto/tapa {alto / tapa:.2f}")
obj = 1.61 * tapa
delta = int(round(alto - obj))
y_corte = tope + int(0.44 * tapa)  # bajo la tapa, en cartón liso y lejos del logotipo
print(f"se sacan {delta} px en y = {y_corte}…{y_corte + delta} → alto/tapa {(alto - delta) / tapa:.2f}")

C = B.copy()
# 1 · donde estaba la parte alta del vaso vuelve el muro original, sólo dentro de su silueta y difuminado
#     (pegar la franja entera dejaba una línea: el muro de la edición es ~5 niveles distinto)
hueco = np.zeros((H, W), np.float32)
for y in range(tope, y_corte + delta):
    a, b = bordes[y]
    hueco[y, a - 30: b + 30] = 1
hueco[max(0, tope - 30): tope] = hueco[tope]
hueco = cv2.GaussianBlur(hueco, (0, 0), 14)
# cerca de la costura el interior del vaso NO vuelve al muro: ahí la franja se funde con el cartón
# del cuerpo (si no, el muro asoma como una banda oscura a través del fundido)
ia, ib = bordes[y_corte + delta]
hueco[y_corte + delta - 130:, ia: ib] = 0
hueco = hueco[..., None]
C = C * (1 - hueco) + A * hueco
# 2 · la parte de arriba baja `delta` y se angosta lo que pide la conicidad del vaso
SOL = 40  # la franja entra 40 px bajo el corte y se funde con el cuerpo en 80 px: sin línea de tono
x0, x1 = bordes[y_corte]
a2, b2 = bordes[y_corte + delta]
k = (b2 - a2) / (x1 - x0)
cx = (a2 + b2) / 2
pad = 60
xa = min(bordes[y][0] for y in range(tope, y_corte + SOL)) - pad  # la tapa es más ancha que el cartón del corte
xb = max(bordes[y][1] for y in range(tope, y_corte + SOL)) + pad
franja = B[tope - pad: y_corte + SOL, xa: xb]
masc = np.zeros(franja.shape[:2], np.float32)
for y in range(tope, y_corte + SOL):
    a, b = bordes[y]
    masc[y - tope + pad, a - xa: b - xa] = 1
masc = cv2.GaussianBlur(masc, (0, 0), 1.6)
masc[-2 * SOL:] *= np.linspace(1, 0, 2 * SOL, dtype=np.float32)[:, None]
nw = int(round(franja.shape[1] * k))
franja = cv2.resize(franja, (nw, franja.shape[0]), interpolation=cv2.INTER_AREA)
masc = cv2.resize(masc, (nw, masc.shape[0]), interpolation=cv2.INTER_AREA)[..., None]
X = int(round(cx - ((x0 + x1) / 2 - xa) * k))  # el eje del vaso de la franja cae sobre el eje del cuerpo
Y = tope - pad + delta
zona = C[Y: Y + franja.shape[0], X: X + nw]
C[Y: Y + franja.shape[0], X: X + nw] = zona * (1 - masc) + franja * masc
Image.fromarray(np.clip(C, 0, 255).astype(np.uint8)).save(G / "gen-fd01-3g-grande.png")
print(f"ok gen-fd01-3g-grande.png · tapa nueva en y = {tope + delta} ({(tope + delta) / H:.0%} del alto)")

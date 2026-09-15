# -*- coding: utf-8 -*-
"""QA del carrusel: mide el render y lo compara con las cifras de §4-bis del manual.

No mira la pieza «a ojo»: saca las medidas del PNG entregado, normalizadas a 1080,
y las contrasta con lo que Paulina dejó medido en las referencias de septiembre.

Uso:  python qa.py editables/salida
"""
import sys
import pathlib
import numpy as np
from PIL import Image

SALIDA = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "editables/salida")

# lo que dice §4-bis (todo a 1080 de ancho)
ESPERADO = {
    "pastilla_x0": (71.0, 1.5), "pastilla_ancho": (118.4, 1.5), "pastilla_alto": (121.9, 1.5),
    "capsula_y0": (154.6, 2.0),
    "caja_cx": (539.8, 3.0),
    "anillo_ancho": (298.6, 3.0), "anillo_alto": (307.2, 3.0),
    "boton_ancho": (653.8, 3.0), "boton_alto": (79.7, 2.0), "boton_y": (916.3, 3.0),
}
fallos, avisos = [], []


def ok(nombre, valor):
    esp, tol = ESPERADO[nombre]
    d = abs(valor - esp)
    marca = "OK " if d <= tol else "FALLA"
    if d > tol:
        fallos.append(f"{nombre}: {valor:.1f} (se esperaba {esp} ±{tol})")
    print(f"   {marca} {nombre:15s} {valor:8.1f}   esperado {esp:7.1f}  desvio {d:5.2f}")


def canales(p):
    a = np.asarray(Image.open(p).convert("RGB")).astype(int)
    return a, a[:, :, 0], a[:, :, 1], a[:, :, 2], 1080 / a.shape[1]


print(f"QA · §4-bis · {SALIDA}\n")

# ---------------------------------------------------------------- portada ---
p = SALIDA / "masisa1_feed.png"
a, r, g, b, esc = canales(p)
print(f"L1 portada  {p.name}  ({a.shape[1]}x{a.shape[0]})")

rojo = (r > 200) & (g < 70) & (b < 75)
zona = rojo[:900, :700]                       # la pastilla del logo, en la capsula
ys, xs = np.where(zona)
ok("pastilla_x0", xs.min() * esc)
ok("pastilla_ancho", (xs.max() - xs.min() + 1) * esc)
ok("pastilla_alto", (ys.max() - ys.min() + 1) * esc)

blanco = (r > 245) & (g > 245) & (b > 245)
filas = np.where(blanco[:1200, :200].sum(axis=1) > 100)[0]
ok("capsula_y0", filas.min() * esc)

# caja roja del titular: la banda ancha bajo la capsula
ancho_fila = rojo[1200:, :].sum(axis=1)
f = np.where(ancho_fila > a.shape[1] * 0.25)[0]
cols = np.where(rojo[1200 + f.min():1200 + f.max() + 1].sum(axis=0) > 0)[0]
ok("caja_cx", ((cols.min() + cols.max()) / 2) * esc)

# ----------------------------------------------------------------- cierre ---
p = SALIDA / "masisa5_feed.png"
a, r, g, b, esc = canales(p)
print(f"\nL5 cierre   {p.name}")
rojo = (r > 200) & (g < 70) & (b < 75)

# el anillo: banda roja de la mitad superior
arriba = rojo[:1900, :]
ys, xs = np.where(arriba)
ok("anillo_ancho", (xs.max() - xs.min() + 1) * esc)
ok("anillo_alto", (ys.max() - ys.min() + 1) * esc)

# el boton: bloque rojo macizo de la mitad inferior
abajo = rojo[1900:, :]
filas = np.where(abajo.sum(axis=1) > a.shape[1] * 0.4)[0]
cols = np.where(abajo[filas.min():filas.max() + 1].sum(axis=0) > 0)[0]
ok("boton_ancho", (cols.max() - cols.min() + 1) * esc)
ok("boton_alto", (filas.max() - filas.min() + 1) * esc)
ok("boton_y", (filas.min() + 1900) * esc)

# ------------------------------------------------- reglas que no son medida ---
print("\nReglas de §4-bis que no son geometria:")
for n in range(1, 6):
    a, r, g, b, esc = canales(SALIDA / f"masisa{n}_feed.png")
    rojo = (r > 200) & (g < 70) & (b < 75)
    if n == 1:
        rojo[:900, :700] = False        # la pastilla del logo no cuenta
    # Una fila «es de caja» si entre su primer y su último píxel rojo hay un tramo
    # ancho y mayoritariamente rojo. Contar sólo píxeles rojos no sirve: el texto
    # BLANCO de adentro vacía la franja, y una caja de dos renglones se leía como tres.
    ancho_min = a.shape[1] * 0.20
    marca = np.zeros(a.shape[0], bool)
    for y in np.where(rojo.any(axis=1))[0]:
        xs_ = np.where(rojo[y])[0]
        tramo = xs_.max() - xs_.min() + 1
        if tramo >= ancho_min and len(xs_) >= tramo * 0.35:
            marca[y] = True
    idx = np.where(marca)[0]
    n_cajas = 1 + (np.diff(idx) > 25).sum() if len(idx) else 0
    estado = "OK " if n_cajas <= 1 else "FALLA"
    if n_cajas > 1:
        fallos.append(f"L{n}: {n_cajas} cajas rojas (§4-bis: una sola por lamina)")
    print(f"   {estado} L{n}: {n_cajas} caja roja")

    if a.shape[1] != 2250 or abs(a.shape[0] - 2813) > 2:
        avisos.append(f"L{n}: entrega {a.shape[1]}x{a.shape[0]}, el estandar es 2250x2813")

print()
for x in avisos:
    print("   aviso  " + x)
if fallos:
    print("\n".join("   FALLA  " + f for f in fallos))
    sys.exit(1)
print("Sin fallos.")

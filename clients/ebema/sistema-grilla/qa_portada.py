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

# El nombre del carrusel sale de la propia carpeta: de `<algo>1_feed.png` se toma
# el `<algo>`. Antes estaba quemado al nombre de una pieza concreta y el QA se
# caía con cualquier otra — justo lo que un control de calidad no puede hacer.
_p1 = sorted(SALIDA.glob("*1_feed.png"))
if not _p1:
    sys.exit(f"No hay ninguna portada (*1_feed.png) en {SALIDA}")
PREFIJO = _p1[0].name[:-len("1_feed.png")]
print(f"carrusel: {PREFIJO}")

# lo que dice §4-bis (todo a 1080 de ancho)
ESPERADO = {
    "pastilla_x0": (71.0, 1.5), "pastilla_ancho": (118.4, 1.5), "pastilla_alto": (121.9, 1.5),
    "capsula_y0": (154.6, 2.0),
    "caja_cx": (539.8, 3.0),
    "anillo_ancho": (298.6, 3.0), "anillo_alto": (307.2, 3.0),
    # ⭐ EL BOTÓN CAMBIÓ EN LA RONDA 1 DE OCTUBRE (23-09-2026). Paulina: «el cuadro
    # rojo debe ser más pequeño, no debe sobresalir tanto hacia los lados del texto».
    # Pasó de un ancho fijo de 653,8 a abrazar su propio texto. Medido sobre los 6
    # cierres del lote: 430,1 en los seis, con el mismo alto y la misma y de antes.
    "boton_ancho": (430.1, 3.0), "boton_alto": (79.7, 2.0), "boton_y": (916.3, 3.0),
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
p = SALIDA / f"{PREFIJO}1_feed.png"
a, r, g, b, esc = canales(p)
print(f"L1 portada  {p.name}  ({a.shape[1]}x{a.shape[0]})")

rojo = (r > 200) & (g < 70) & (b < 75)
zona = rojo[:900, :700]                       # la pastilla del logo, en la capsula

# ⛔ EL ANILLO EBEMA ES EL PRIMER BLOQUE CONTIGUO DE ROJO, no todo el rojo de la
# ventana. Corregido el 23-09-2026: el logo de VOLCÁN también lleva rojo, y medir
# el recuadro de todo el rojo juntaba el anillo con el logo del proveedor — daba
# pastilla_ancho 264,5 en vez de 118,4 y el QA reprobaba una portada correcta.
# Entre el anillo y el logo del proveedor siempre hay aire blanco: ahí se corta.
_cols = np.where(zona.sum(axis=0) > 0)[0]
_hueco = np.where(np.diff(_cols) > 8)[0]      # 8 px del render (~4 sobre 1080)
if len(_hueco):
    _cols = _cols[:_hueco[0] + 1]
x0, x1 = int(_cols.min()), int(_cols.max())
ys = np.where(zona[:, x0:x1 + 1].sum(axis=1) > 0)[0]
ok("pastilla_x0", x0 * esc)
ok("pastilla_ancho", (x1 - x0 + 1) * esc)
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
# Un carrusel a medias NO es un fallo: mientras se trabaja la portada, las laminas
# 2-5 todavia no existen y el QA tiene que poder correr igual sobre lo que hay.
p = SALIDA / f"{PREFIJO}5_feed.png"
if not p.exists():
    avisos.append(f"L5 todavia no existe ({p.name}) - carrusel a medias")
else:
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
    # El umbral bajó de 0,4 a 0,10 del ancho: con el botón ajustado a su texto (430,1
    # sobre 1080, o sea el 40 %) ninguna fila llegaba al 40 % del lienzo y el QA se
    # caía con «zero-size array» en vez de medir.
    filas = np.where(abajo.sum(axis=1) > a.shape[1] * 0.10)[0]
    cols = np.where(abajo[filas.min():filas.max() + 1].sum(axis=0) > 0)[0]
    ok("boton_ancho", (cols.max() - cols.min() + 1) * esc)
    ok("boton_alto", (filas.max() - filas.min() + 1) * esc)
    ok("boton_y", (filas.min() + 1900) * esc)

# ------------------------------------------------- reglas que no son medida ---
print("\nReglas de §4-bis que no son geometria:")
for n in range(1, 6):
    _pn = SALIDA / f"{PREFIJO}{n}_feed.png"
    if not _pn.exists():
        continue
    a, r, g, b, esc = canales(_pn)
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
    # ⛔ UNA CAJA ALTA CON DOS RENGLONES SE PARTE EN VARIOS GRUPOS y se contaba
    # como varias cajas. Corregido el 23-09-2026 sobre la portada de Masisa: ahí el
    # rojo muerde la línea de arriba y encierra dos renglones, y las filas que caen
    # sobre las letras BLANCAS dejan de ser «mayoritariamente rojas» y desmarcan —
    # daban 3 cajas donde hay 1. Dos grupos con el MISMO tramo horizontal son el
    # mismo rectángulo, así que se funden; uno de verdad distinto arranca en otra x.
    if len(idx):
        grupos = np.split(idx, np.where(np.diff(idx) > 25)[0] + 1)
        tramos = []
        for gr in grupos:
            xs_ = np.where(rojo[gr.min():gr.max() + 1].sum(axis=0) > 0)[0]
            tramos.append((xs_.min(), xs_.max()))
        tol = a.shape[1] * 0.02
        n_cajas = 1
        for i in range(1, len(tramos)):
            if not (abs(tramos[i][0] - tramos[i - 1][0]) <= tol
                    and abs(tramos[i][1] - tramos[i - 1][1]) <= tol):
                n_cajas += 1
    else:
        n_cajas = 0
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

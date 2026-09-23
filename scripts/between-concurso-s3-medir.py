#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las mediciones del CARRUSEL CONCURSO de Between, en un solo aparato.

Existe porque los comentarios de la pieza y el manual citan estos números —el
hueco limpio de la foto, la holgura contra el recorte, los contrastes, el ángulo
de la caja de la REF 1 y el de los garabatos rojos de Eli— y un número citado que
no se puede volver a correr es un número que nadie puede discutir.

    python scripts/between-concurso-s3-medir.py papel      # hueco limpio de la portada
    python scripts/between-concurso-s3-medir.py holgura    # dónde entra el recorte bajo la CTA
    python scripts/between-concurso-s3-medir.py contraste   # tinta contra el FONDO
    python scripts/between-concurso-s3-medir.py angulo-ref # la caja plana de la REF 1
    python scripts/between-concurso-s3-medir.py rojo <pantallazo.png>
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
PORTADA = RAIZ / "public/assets/hilton/between/concurso-s3/c1-portada-papel.jpg"
REF1 = RAIZ / "raw/hilton/between/refs-concurso-s3/REF1.jpg"

CAFE, BEIGE, PAPEL = "#675b49", "#fff9eb", "#dfc9bb"


# ── la foto: qué parte es papel limpio ──────────────────────────────────────
def _mascara_no_papel(escala=(1080, 1350)):
    """True donde la foto YA NO es papel liso: el recorte, su halo y su sombra."""
    a = np.asarray(Image.open(PORTADA).convert("RGB").resize(escala, Image.LANCZOS)).astype(float)
    papel = np.median(a[:200].reshape(-1, 3), axis=0)
    d = np.sqrt(((a - papel) ** 2).sum(axis=2))
    g = np.pad(np.abs(np.diff(a.mean(axis=2), axis=1)), ((0, 0), (0, 1)))
    # ⚠️ Los umbrales son flojos a propósito: el halo del sticker es casi del
    # tono del papel y con umbrales duros no aparece — que es justo el borde
    # contra el que no puede apoyarse un texto.
    return ndimage.binary_opening((d > 12) | (g > 3.5), structure=np.ones((3, 3)))


def papel():
    m = _mascara_no_papel()
    print("hasta qué x llega el papel limpio, por franjas de 25 px:")
    for y0 in range(500, 1000, 25):
        col = m[y0:y0 + 25].mean(axis=0)
        libre = next((x for x in range(84, 1080) if col[x] > 0.35), 1080)
        print(f"  y {y0:4d}-{y0 + 24:4d}   x ≤ {libre}")


def holgura(x0=84, x1=520, desde=800, hasta=900):
    """Primera fila donde el recorte invade la columna de la CTA."""
    m = _mascara_no_papel()
    for y in range(desde, hasta):
        if m[y, x0:x1].sum() > 3:
            xs = np.where(m[y, x0:x1])[0] + x0
            print(f"el recorte entra en y={y}  (x {xs.min()}–{xs.max()})")
            print("→ ninguna tinta puede pasar de y≈%d si se quieren 20 px de aire" % (y - 20))
            return
    print("no entra en esa franja")


# ── contrastes ──────────────────────────────────────────────────────────────
def _rel(c):
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def _lum(h):
    return float(_rel(np.array([int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]).reshape(1, 1, 3))[0, 0])


def _ratio(a, b):
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def contraste():
    """Contraste de cada tinta contra el papel, por TERCIOS de su franja.

    Por tercios y no en promedio: el promedio de una franja miente cuando el
    fondo tiene gradiente (memoria `la-tinta-la-manda-el-fondo`).

    ⛔ SE MIDE SOBRE LA FOTO, NUNCA SOBRE LA PIEZA RENDIDA. En el render la
    franja ya contiene la propia tinta, así que el «fondo» sale contaminado y el
    número baja sin que nada haya empeorado: el rótulo daba 4,14:1 contra el
    papel y 2,26:1 medido sobre sí mismo. Lo que se quiere saber es el contraste
    de la tinta contra el fondo SOBRE EL QUE SE VA A PINTAR.
    """
    a = np.asarray(Image.open(PORTADA).convert("RGB").resize((1080, 1350), Image.LANCZOS)).astype(float) / 255
    for nombre, (x0, x1, y0, y1), tinta in [
        ("rótulo CONCURSO (café)", (235, 846, 225, 300), CAFE),
        ("bajada (café)", (215, 865, 330, 408), CAFE),
        ("cajita del titular (taupe)", (313, 766, 474, 584), CAFE),
        ("caja del premio (beige)", (84, 616, 659, 725), BEIGE),
    ]:
        L = _rel(a[y0:y1, x0:x1])
        n = (x1 - x0) // 3
        cs = [_ratio(_lum(tinta), L[:, i * n:(i + 1) * n].mean()) for i in range(3)]
        print(f"{nombre:28s} por tercios {[round(c, 2) for c in cs]}  · peor {min(cs):.2f}:1")
    print(f"{'café dentro de beige':28s} {_ratio(_lum(CAFE), _lum(BEIGE)):.2f}:1")


# ── ángulos ─────────────────────────────────────────────────────────────────
def angulo_ref():
    """El ángulo de la caja plana azul de la REF 1, ajustando sus bordes."""
    a = np.asarray(Image.open(REF1).convert("RGB")).astype(float)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    azul = (b > 100) & (b - r > 45) & (b - g > 30)
    franja = azul[280:560]
    top, bot = [], []
    for x in range(franja.shape[1]):
        col = np.where(franja[:, x])[0]
        if len(col) > 40:
            top.append((x, col.min()))
            bot.append((x, col.max()))
    for nombre, datos in (("borde superior", top), ("borde inferior", bot)):
        d = np.array(datos)
        m = np.polyfit(d[:, 0], d[:, 1], 1)[0]
        print(f"{nombre}: {np.degrees(np.arctan(m)):+.2f}°")
    print("→ se tomó −3°, dentro del rango y en el registro de la marca")


def rojo(pantallazo):
    """Orientación de cada trazo ROJO que dibujó la diseñadora sobre un render.

    La regla del manual: si ella DIBUJA la corrección, el ángulo se mide en su
    dibujo — deducirlo de la referencia original puede dar el signo cambiado.
    """
    a = np.asarray(Image.open(pantallazo).convert("RGB")).astype(float)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    lab, n = ndimage.label((r > 120) & (r - g > 55) & (r - b > 55), structure=np.ones((3, 3)))
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        if len(xs) < 60:
            continue
        cov = np.cov(np.vstack([xs - xs.mean(), ys - ys.mean()]))
        w, v = np.linalg.eigh(cov)
        ang = np.degrees(np.arctan2(v[1, -1], v[0, -1])) % 180
        print(f"  trazo de {len(xs):5d} px en ({xs.mean():6.1f},{ys.mean():6.1f}) · "
              f"largo {4 * np.sqrt(w[-1]):5.1f} · ángulo {ang:6.1f}°")


if __name__ == "__main__":
    orden = sys.argv[1] if len(sys.argv) > 1 else "papel"
    arg = sys.argv[2] if len(sys.argv) > 2 else None
    {"papel": papel, "holgura": holgura, "contraste": contraste,
     "angulo-ref": angulo_ref, "rojo": rojo}[orden](*( [arg] if arg else [] ))

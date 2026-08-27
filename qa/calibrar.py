#!/usr/bin/env python3
"""Calibrador de topes — saca el número de las piezas reales, no de la intuición.

    python3 qa/calibrar.py --marca casablanca \
        --aprobadas "raw/casablanca/ref/*.png" \
        --rechazadas "out/casablanca/sep2026/_ronda1/*.png"

Un tope inventado a ojo produce una de dos cosas, las dos malas: marca piezas buenas
(y la gente aprende a ignorar el QA) o deja pasar las malas (y no sirve de nada). El
tope correcto es el que **separa** dos grupos que ya sabemos cómo se clasifican: lo
que la diseñadora del cliente firmó, y lo que rechazó.

Para cada métrica imprime las dos distribuciones y propone un corte. Y dice cuándo
NO hay corte posible — que es la información más valiosa: significa que la
comprobación mide algo que no es lo que decide, y la regla hay que retirarla.
Pasó con el contraste de texto: aprobadas 1,30–2,21 contra rechazadas 1,39–2,39.
"""
from __future__ import annotations

import argparse
import glob
import pathlib
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import checks  # noqa: E402

Image.MAX_IMAGE_PIXELS = None
VERDE, ROJO, AMARILLO, GRIS, NEGRITA, FIN = (
    "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[1m", "\033[0m")


def carga(p):
    im = Image.open(p).convert("RGB")
    if im.width > 1080:
        im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS)
    return np.asarray(im).astype(int)


# ── métricas crudas ───────────────────────────────────────────────────────────
# Cada una devuelve el número que la regla compara contra su tope, sin juzgarlo.
# `sentido` dice de qué lado está el defecto: "alto" = más es peor.

def m_costura(a):
    g = checks._luminancia(a.astype(float))
    dif = np.abs(np.diff(g, axis=0)).mean(axis=1)
    std = g.std(axis=1)
    foto = (std[:-1] > 4.0) & (std[1:] > 4.0)
    dif = np.where(foto, dif, 0.0)
    m = max(4, int(len(dif) * 0.06))
    dif = dif[m:-m]
    if dif.size < 10 or not np.any(dif > 0):
        return None
    return float(dif.max() / max(float(np.median(dif[dif > 0])), 0.4))


def m_desenfoque(a):
    from scipy.ndimage import laplace
    g = checks._luminancia(a.astype(float))
    n, lap = 10, None
    bordes = np.linspace(0, g.shape[0], n + 1).astype(int)
    lap = laplace(g)
    nit = np.array([lap[bordes[i]:bordes[i + 1]].var() for i in range(n)])
    foto = ~checks._bandas_planas(g, bordes, 4.0)
    if foto.sum() < 3:
        return None
    med = float(np.median(nit[foto]))
    if med < 5.0:
        return None
    return float(np.min(np.where(foto, nit / med, np.inf)))


def m_estirada(a):
    g = checks._luminancia(a.astype(float))
    dif = np.abs(np.diff(g, axis=0)).mean(axis=1)
    clon = (dif < 0.35) & (g.std(axis=1)[:-1] > 4.0)
    mejor = racha = 0
    for c in clon:
        racha = racha + 1 if c else 0
        mejor = max(mejor, racha)
    return mejor / g.shape[0]


def m_paleta(a, colores=("#626260", "#FFFFFF", "#FDFDFD")):
    h, s, v = checks._hsv(a)
    graf = (s < 0.18) & (v > 0.12) & (v < 0.94) & checks._mascara_plana(a)
    if graf.sum() < 2000:
        return None
    ok = checks._rgb_a_lab(np.array(
        [[int(c[i:i + 2], 16) for i in (1, 3, 5)] for c in colores], dtype=float))
    lab = checks._rgb_a_lab(a[graf])
    d = np.linalg.norm(lab[:, None, :] - ok[None, :, :], axis=2).min(axis=1)
    return float((d > 14.0).mean())


def m_respiro(a, margen_px=60):
    H, W = a.shape[:2]
    m = int(margen_px * W / 1080)
    t = checks._mascara_tinta(a)
    t[:int(0.17 * H), int(0.36 * W):int(0.64 * W)] = False   # excepción del logo
    if t.sum() < 400:
        return None
    marco = np.zeros_like(t)
    marco[:m, :] = marco[-m:, :] = True
    marco[:, :m] = marco[:, -m:] = True
    return float((t & marco).sum()) / t.sum()


METRICAS = {
    "costura → razon_max": (m_costura, "alto"),
    "desenfoque-parcial → razon_min": (m_desenfoque, "bajo"),
    "foto-estirada → max_fraccion_alto": (m_estirada, "alto"),
    "paleta-cerrada → max_fraccion": (m_paleta, "alto"),
    "respiro-borde → max_fraccion_tinta": (m_respiro, "alto"),
}


def resumen(v):
    v = np.array(v, dtype=float)
    return (f"n={len(v):3d}  min {v.min():7.3f}  p50 {np.median(v):7.3f}  "
            f"p95 {np.percentile(v, 95):7.3f}  max {v.max():7.3f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--marca", required=True)
    ap.add_argument("--aprobadas", required=True,
                    help="patrón de piezas que la diseñadora del cliente FIRMÓ")
    ap.add_argument("--rechazadas",
                    help="patrón de piezas que se rechazaron (opcional pero es lo "
                         "que permite saber si el corte separa de verdad)")
    a = ap.parse_args()

    buenas = sorted(glob.glob(a.aprobadas))
    malas = sorted(glob.glob(a.rechazadas)) if a.rechazadas else []
    if not buenas:
        print(f"{ROJO}✖ no encontré piezas aprobadas en {a.aprobadas}{FIN}")
        return 2

    print(f"\n{NEGRITA}Calibración · {a.marca}{FIN}")
    print(f"{GRIS}{len(buenas)} aprobadas · {len(malas)} rechazadas{FIN}\n")

    ib = [carga(p) for p in buenas]
    im = [carga(p) for p in malas]

    for nombre, (fn, sentido) in METRICAS.items():
        vb = [x for x in (fn(i) for i in ib) if x is not None]
        vm = [x for x in (fn(i) for i in im) if x is not None]
        if not vb:
            continue
        print(f"{NEGRITA}{nombre}{FIN}   {GRIS}(defecto = valor {sentido}){FIN}")
        print(f"  aprobadas   {resumen(vb)}")
        if vm:
            print(f"  rechazadas  {resumen(vm)}")

        vb_a = np.array(vb)
        if sentido == "alto":
            # el tope debe dejar pasar TODAS las aprobadas, con holgura
            propuesto = float(np.percentile(vb_a, 99)) * 1.15
            atrapa = np.mean(np.array(vm) > propuesto) if vm else None
        else:
            propuesto = float(np.percentile(vb_a, 1)) * 0.85
            atrapa = np.mean(np.array(vm) < propuesto) if vm else None

        falsos = (np.mean(vb_a > propuesto) if sentido == "alto"
                  else np.mean(vb_a < propuesto))
        col = VERDE if falsos == 0 else AMARILLO
        print(f"  {col}tope propuesto {propuesto:.3f}{FIN} → "
              f"{falsos * 100:.0f}% de falsos positivos", end="")
        if atrapa is not None:
            print(f" · atrapa {atrapa * 100:.0f}% de las rechazadas")
            if atrapa == 0:
                print(f"  {ROJO}⚠ no atrapa ninguna rechazada: esta métrica no mide "
                      f"lo que decide.{FIN}")
                print(f"  {GRIS}  Si los dos rangos se solapan, la regla hay que "
                      f"retirarla, no ajustarla.{FIN}")
        else:
            print()
        print()

    print(f"{GRIS}Los topes propuestos dejan pasar el 99 % de lo aprobado con 15 % de\n"
          f"holgura. Cópialos al YAML sólo si además atrapan las rechazadas.{FIN}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

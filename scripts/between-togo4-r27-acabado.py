#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROMOS TO GO · slide 4 — ronda 27: recorte 4:5 y revelado de la escena
generada, para que entre al carrusel con el tono de sus hermanas.

La generación sale en **3:4 (3584×4800)**, que es lo más cercano al 4:5 del
feed que da la API. Se recortan 320 filas y se lleva a 2250×2812.

⭐ De dónde se recortan las 320 filas: de ARRIBA. Es donde sobra muro vegetal,
y bajando el encuadre el bloque de texto —que cierra en y=660— sigue cayendo
sobre verde oscuro, mientras la franja de mesa limpia del pie, donde va la
pastilla del precio (y 2609–2721), se conserva entera.

El revelado apunta a los percentiles de las hermanas, no sólo a la mediana:
igualar la mediana no dice nada del PIE de la curva, y el pie es lo que se ve
como densidad (fue el «se ve muy blanca» de la slide 3).

Salida: public/assets/hilton/between/fotos-gradadas/togo-s4-r27.jpg
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

from between_retoque import hombro  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = RAIZ / "raw/hilton/between/s4/gen-r27/togo-s4-gen-b.png"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-s4-r27.jpg"
SALIDA = (2250, 2812)

RECORTE_ARRIBA = 320        # 4800 − 320 = 4480 = 3584 / 0,8

#: Los percentiles de luma de las hermanas del carrusel, medidos sobre los
#: archivos entregados. El objetivo es el promedio de la 2 y la 3.
OBJETIVO = {"p5": 8.0, "p25": 60.4, "p50": 120.4, "p75": 157.2, "p95": 205.3,
            "calidez": 27.5}

NEGRO_PCT, CONTRASTE, PIVOTE = 1.0, 1.0, 120.0
GAMMA_OBJ = 120.4


def cifras(im, nom):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    g = a[..., 0] * .299 + a[..., 1] * .587 + a[..., 2] * .114
    gris = a.mean(2)
    q = np.percentile(g, [5, 25, 50, 75, 95])
    print(f"   {nom:14s} p5 {q[0]:6.1f} · p25 {q[1]:5.1f} · p50 {q[2]:5.1f} · p75 {q[3]:5.1f} "
          f"· p95 {q[4]:5.1f} · calidez {(a[..., 0] - a[..., 2]).mean():5.1f} "
          f"· croma {np.abs(a - gris[..., None]).max(2).mean():5.1f} "
          f"· blanco {(a > 250).mean() * 100:4.2f} %")
    return q


def main():
    if not ORIGEN.exists():
        sys.exit(f"falta la generación: {ORIGEN}\n"
                 f"Córrela con scripts/between-togo4-r27-generar.py")
    src = Image.open(ORIGEN).convert("RGB")
    print(f"generación .... {src.width}×{src.height}")
    im = src.crop((0, RECORTE_ARRIBA, src.width, RECORTE_ARRIBA + int(src.width / 0.8)))
    im = im.resize(SALIDA, Image.LANCZOS)
    print(f"recorte 4:5 ... {im.size[0]}×{im.size[1]} desde y={RECORTE_ARRIBA}")
    cifras(im, "de la IA")

    a = np.asarray(im).astype(np.float32)

    #: ⛔ EL ORDEN IMPORTA, y la primera pasada lo tuvo mal.
    #: · el gamma se resolvía contra `np.median(a)` —la mediana de los TRES
    #:   canales— y el objetivo está en LUMA: pedía 120 y aterrizaba en 137,
    #:   con el p75 en 191 contra los 157 de sus hermanas.
    #: · y la calidez se corregía ANTES del punto negro, que la vuelve a mover:
    #:   quedaba en 21,4 cuando se había pedido 27,5.
    #: Ahora: punto negro → gamma sobre LUMA → calidez al final.

    def luma(x):
        return x[..., 0] * .299 + x[..., 1] * .587 + x[..., 2] * .114

    # 1 · punto negro: es lo que da densidad, y va antes del gamma
    p = float(np.percentile(a, NEGRO_PCT))
    a = np.clip(a - p, 0, None) * (255.0 / max(1.0, 255.0 - p))
    print(f"   punto negro: percentil {NEGRO_PCT} ({p:.0f}) -> 0")

    # 2 · gamma por los MEDIOS, resuelto sobre la luma
    med = max(1.0, float(np.median(luma(a))))
    gamma = float(np.clip(np.log(GAMMA_OBJ / 255.0) / np.log(med / 255.0), 0.55, 1.6))
    a = np.power(np.clip(a / 255.0, 0, 1), gamma) * 255.0
    print(f"   mediana de luma {med:.0f} -> {GAMMA_OBJ} (gamma {gamma:.3f})")

    # 3 · calidez, al final
    cal = float(a[..., 0].mean() - a[..., 2].mean())
    d = cal - OBJETIVO["calidez"]
    a[..., 0] -= d * 0.55
    a[..., 2] += d * 0.45
    print(f"   calidez {cal:.1f} -> {OBJETIVO['calidez']:.1f}")

    if CONTRASTE != 1.0:
        a = (a - PIVOTE) * CONTRASTE + PIVOTE
    out = Image.fromarray(np.clip(hombro(np.clip(a, 0, 320)), 0, 255).astype(np.uint8))
    cifras(out, "revelada")
    print(f"   {'objetivo':14s} p5 {OBJETIVO['p5']:6.1f} · p25 {OBJETIVO['p25']:5.1f} "
          f"· p50 {OBJETIVO['p50']:5.1f} · p75 {OBJETIVO['p75']:5.1f} · p95 {OBJETIVO['p95']:5.1f} "
          f"· calidez {OBJETIVO['calidez']:5.1f}")

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    out.save(DESTINO, "JPEG", quality=95, subsampling=0)
    print(f"\n-> {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

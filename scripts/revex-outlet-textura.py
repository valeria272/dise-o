#!/usr/bin/env python3
"""
REVEX · outlet septiembre 2026 — arregla la textura de tableta del fondo rojo.

Feedback de Serena (27-08-2026): *«en la gráfica del outlet veo como que quedaron
unos cuadrados»*.

Diagnóstico sobre el PNG de Versión 3: el fondo tiene TRES tonos, no uno.

    #D31418  rojo de marca            85,9 % del área roja   -> se conserva
    #C81317  tableta de otro tono      11,1 %                -> ES EL DEFECTO
    #D62326  junta clara                2,7 %                -> se atenúa

El problema no es la textura, es que **algunas tabletas quedaron de otro tono** y eso
se lee como error de render, no como material. La corrección uniforma las tabletas al
rojo de marca y deja sólo la junta, muy tenue: queda retícula de tableta —que además
es coherente, Revex vende revestimientos— sin el bloque raro.

Se corrige sobre el PNG entregado y NO se re-renderiza, porque el código que produjo
Versión 3 no está en el repo (ver clients/revex/CLAUDE.md § NO SE PUEDE REPRODUCIR).
Cuando ese código aparezca, esto se muda al render y este script se puede borrar.

    python3 scripts/revex-outlet-textura.py
"""
import os
import numpy as np
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN  = os.path.join(RAIZ, "raw/revex/v3")
DESTINO = os.path.join(RAIZ, "out/revex/sep2026")

BASE   = np.array([0xD3, 0x14, 0x18], dtype=np.float64)   # rojo de marca
TABLETA= np.array([0xC8, 0x13, 0x17], dtype=np.float64)   # el tono intruso
JUNTA  = np.array([0xD6, 0x23, 0x26], dtype=np.float64)   # junta clara

ATENUAR_JUNTA = 0.62      # 0 = junta intacta · 1 = fondo plano sin retícula


def corregir(ruta_png, atenuar=ATENUAR_JUNTA):
    a = np.asarray(Image.open(ruta_png).convert("RGB")).astype(np.float64)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]

    # Sólo el rojo de fondo. Los rangos excluyen el blanco, el amarillo #FFD400, la
    # tinta #1A1A1A y —importante— los bordes rosados del antialias del texto, que
    # tienen G y B altos: si se tocaran, el texto blanco quedaría con orla roja.
    fondo = (R >= 175) & (R <= 228) & (G >= 8) & (G <= 55) & (B >= 8) & (B <= 58)

    # Cada pixel del fondo se asigna al tono de referencia más cercano. Así entran
    # también los pixeles de antialias del borde de cada tableta, que si no quedarían
    # como hilos visibles.
    d_tab = np.linalg.norm(a - TABLETA, axis=2)
    d_jun = np.linalg.norm(a - JUNTA,   axis=2)
    d_bas = np.linalg.norm(a - BASE,    axis=2)
    es_tableta = fondo & (d_tab <  d_jun) & (d_tab <= d_bas)
    es_junta   = fondo & (d_jun <  d_tab) & (d_jun <  d_bas)

    out = a.copy()
    for c in range(3):
        ch = out[:, :, c]
        ch[es_tableta] = BASE[c]
        ch[es_junta]   = BASE[c] + (a[:, :, c][es_junta] - BASE[c]) * (1 - atenuar)
        out[:, :, c] = ch
    return (Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)),
            int(es_tableta.sum()), int(es_junta.sum()))


if __name__ == "__main__":
    os.makedirs(DESTINO, exist_ok=True)
    for nombre in ("rvx_sep_outlet_feed.png", "rvx_sep_outlet_story.png"):
        origen = os.path.join(ORIGEN, nombre)
        if not os.path.exists(origen):
            print(f"  ⚠️  falta {origen} — bájalo de la carpeta «Versión 3» del Drive")
            continue
        img, n_tab, n_jun = corregir(origen)
        destino = os.path.join(DESTINO, nombre)
        img.save(destino)
        print(f"  {nombre:28} {img.size}  tabletas={n_tab:>9,}  juntas={n_jun:>9,}")
    print(f"\n-> {DESTINO}")

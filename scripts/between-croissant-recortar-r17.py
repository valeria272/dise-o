#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta el CROISSANT DE JAMÓN QUESO de la sesión profesional de platos.

⭐ RONDA 17 (07-09-2026) — Eli, sobre la ST de Emergencia:

    «se ve de mala calidad el muffin, al igual que el croissant de queso y
     jamón. Tiene que verse atractivo visualmente […] ya que son alimentos, son
     productos.»

⛔ El croissant que se usaba salía de la sesión del 25-jul-2025
(`recortes/croissant-jamon-queso-limpio.png`): un croissant TENDIDO con un blob
grande de queso derretido desbordando por la izquierda. Recortado y reducido a
360 px en la pieza, ese blob domina y el conjunto se lee como un bulto pálido,
no como un sándwich de croissant.

⭐ Y había material mejor en la casa, que es lo primero que había que mirar:
`platos-ene/_recortes/h3-croissant-jamon.jpg` es de la sesión PROFESIONAL de
platos — croissant partido, jamón y queso a la vista, luz de estudio, tomado de
frente y desde abajo, dorado y apetitoso. Es la misma familia de fotografía que
las slides 2 y 3 del carrusel To Go.

    material                         mediana   p95
    25-jul (el que se usaba)           139     207
    platos-ene h3 (profesional)         83     209   ← más rango, luz de estudio

**Regla, otra vez: antes de arreglar un producto con revelado, búscalo en las
otras sesiones.** El manual ya lo dice para generar; vale igual para recortar.

⛔⛔ Y POR QUÉ NO SE PUEDE LLAVEAR POR COLOR, que fue mi primer intento y falló
dos veces. Medido sobre la propia toma:

    zona                          calidez (R−B)    L
    croissant, corteza                  98,4     129,4
    MESA de madera desenfocada          88,0     126,3   ← igual de cálida
    mesa desenfocada (derecha)          60,2      82,0
    jamón                               67,3     117,6
    queso                               66,8      93,7
    plato                               20,1      82,4   ← esto sí se separa

O sea: el plato se separa perfecto, pero **la mesa de madera es tan cálida como
la masa del croissant**. Cualquier umbral que deje entrar el jamón y el queso
deja entrar también la mesa, y como el croissant TOCA la mesa por arriba —el
plato está detrás y abajo— quedan pegados en el mismo componente. Por eso las dos
primeras pasadas salieron con vetas de madera en las esquinas.

⭐ La separación tiene que ser GEOMÉTRICA, no de color: `grabCut` inicializado con
el rectángulo del croissant. Todo lo de fuera del rectángulo queda marcado como
fondo por definición, y dentro el algoritmo usa modelos de color Y coherencia
espacial. Es la herramienta que ya usa la casa (`between-recortes-reales.py`).

Salida: public/assets/hilton/between/recortes/croissant-h3-nobg.png
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ORIGEN = RAIZ / "raw/hilton/between/platos-ene/_recortes/h3-croissant-jamon.jpg"
SALIDA = RAIZ / "public/assets/hilton/between/recortes/croissant-h3-nobg.png"
PASOS = RAIZ / "out/hilton-between-r17/pasos"

#: la caja donde vive el croissant, leída sobre la toma de 1500×1875
# ⚠️ Acotada tras la primera pasada: a (150,590,...) entraba la veta de MADERA
# desenfocada de arriba a la izquierda, que también es cálida y quedaba pegada al
# componente del croissant.
CAJA = (172, 612, 1350, 1285)
UMBRAL_CALIDEZ = 26        # R − B por encima de esto es producto, no plato


def main():
    if not ORIGEN.exists():
        sys.exit(f"falta la toma: {ORIGEN}")
    im = Image.open(ORIGEN).convert("RGB")
    print(f"toma {im.size}")
    z = im.crop(CAJA)
    a = np.asarray(z).astype(np.float32)

    calidez = a[..., 0] - a[..., 2]
    bgr = cv2.cvtColor(np.asarray(z), cv2.COLOR_RGB2BGR)
    gc = np.zeros(bgr.shape[:2], np.uint8)
    bg = np.zeros((1, 65), np.float64)
    fg = np.zeros((1, 65), np.float64)
    # el rectángulo del croissant DENTRO de la caja recortada, con 6 px de aire:
    # todo lo de fuera es fondo por definición y ahí muere la veta de madera.
    r = (6, 6, z.width - 12, z.height - 12)
    cv2.grabCut(bgr, gc, r, bg, fg, 6, cv2.GC_INIT_WITH_RECT)
    m = np.isin(gc, (cv2.GC_FGD, cv2.GC_PR_FGD)).astype(np.uint8)
    print(f"caja {z.size} · grabCut: {100 * m.mean():.1f} % de la caja es producto")

    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    n, et, est, _ = cv2.connectedComponentsWithStats(m, 8)
    if n > 1:
        mayor = 1 + int(np.argmax(est[1:, 4]))
        m = (et == mayor).astype(np.uint8)
        print(f"componente mayor: {est[mayor, 4]:,} px")

    # Rellenar los huecos internos (la sombra bajo el queso, el hueco del jamón).
    #
    # ⛔⛔ BUG QUE ARRUINÓ LA PRIMERA PASADA, y es de los silenciosos: el
    # `floodFill` arrancaba en (0,0) de la máscara. Pero la esquina de este
    # recorte es MADERA, que también es cálida, así que ahí la máscara ya valía 1
    # — el relleno no propagaba nada, `relleno == 0` marcaba TODO el fondo y el
    # recorte salió con el plato y la mesa incluidos.
    #
    # Se acolcha la máscara con un marco de ceros y se inunda desde ese marco:
    # así la semilla está garantizada como fondo, sea lo que sea la esquina.
    h, w = m.shape
    pad = np.zeros((h + 2, w + 2), np.uint8)
    pad[1:-1, 1:-1] = m
    cap = np.zeros((h + 4, w + 4), np.uint8)
    cv2.floodFill(pad, cap, (0, 0), 1)
    huecos = (pad[1:-1, 1:-1] == 0).astype(np.uint8)
    m = ((m | huecos) > 0).astype(np.uint8)

    # ⚠️ Y se le quita al alfa lo que el relleno de huecos metió de más: trozos
    # del PLATO que la silueta irregular del croissant encierra por abajo. Se
    # reconocen porque son oscuros Y neutros — la corteza tostada del croissant
    # también es oscura, pero es cálida.
    L = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114
    plato = (calidez < 10) & (L < 105)
    quitados = int((m > 0).sum() - ((m > 0) & ~plato).sum())
    m = ((m > 0) & ~plato).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    print(f"plato quitado del alfa: {quitados:,} px")

    x, y, ww, hh = cv2.boundingRect(m)
    pad = 10
    x0, y0 = max(0, x - pad), max(0, y - pad)
    x1, y1 = min(w, x + ww + pad), min(h, y + hh + pad)

    alfa = (m[y0:y1, x0:x1] * 255).astype(np.uint8)
    # ⚠️ el canto se SUAVIZA: un alfa binario es lo que delata un recorte, y el
    # manual pide revisar el canto al 300 % antes de montar.
    alfa = np.asarray(Image.fromarray(alfa).filter(ImageFilter.GaussianBlur(1.6)))
    rgb = a[y0:y1, x0:x1].astype(np.uint8)
    fig = Image.merge("RGBA", (*Image.fromarray(rgb).split(),
                               Image.fromarray(alfa)))

    suave = ((alfa > 8) & (alfa < 247)).sum() / max((alfa > 8).sum(), 1)
    print(f"recorte {fig.size} · canto suave {100 * suave:.2f} % "
          f"(el vaso real, la referencia buena, da 2,50 %)")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.save(SALIDA)
    PASOS.mkdir(parents=True, exist_ok=True)
    prueba = Image.new("RGB", fig.size, (150, 125, 95))
    prueba.paste(fig, (0, 0), fig)
    prueba.save(PASOS / "croissant-h3-sobre-nicho.jpg", quality=92)
    print(f"-> {SALIDA.relative_to(RAIZ)}")
    print(f"   prueba: {(PASOS / 'croissant-h3-sobre-nicho.jpg').relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

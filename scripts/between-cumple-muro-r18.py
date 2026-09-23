#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAFÉ DE CUMPLEAÑOS (FEED 09-sep, S1) — ronda 18: el dorado se va AL FONDO.

Eli, 07-09-2026:

    «Para el carrusel de cumpleaños, necesito que generes una mejor imagen de
     fondo. No se ve la transición del primer y el segundo slide […] Tiene que
     ser una composición armónica. Además, el detalle que agregaste de
     serpentina dorada se ve falsa, se ve mal, quemada. Tienes que mejorarlo
     para que se vea de mejor calidad y lujo.»

⛔⛔ EL ERROR DE FONDO, Y LO VENÍA REPITIENDO EN TRES MATERIALES DISTINTOS

Cuatro intentos de poner el adorno dorado y los cuatro rechazados:

    ronda 11  papelitos de color plano, sembrados en la mesa  → «infantil»
    ronda 12  oro metálico dibujado, sembrado en la mesa      → «parece un plátano»
    ronda 14  el vector de Eli, sembrado en la mesa           → «quemado»
    ronda 17  cinta FOTOGRÁFICA, sembrada en la mesa          → «falsa, quemada»

El material fue mejorando cada vez —de color plano a vector a fotografía con
especular medido— y el veredicto no cambió. Así que el material no era el
problema: **el problema es que iba SOBRE LA MESA, en foco.**

⭐ Y la respuesta estaba en la propia pieza aprobada de Eli (`C1 n°1 BW CUMPLE`):
ahí el dorado **no está sobre ninguna superficie**. Está en el AIRE, detrás del
producto, fuera de foco, disuelto en el bokeh junto a los globos. Un objeto
dorado nítido apoyado en una mesa compite con la fotografía que lo rodea y pierde
siempre; el mismo objeto desenfocado en el fondo se lee como ambiente, y ahí sí
se ve lujo.

> **Regla: un adorno agregado a una fotografía va DONDE NO COMPITA — al fondo y
> fuera de foco. Si tiene que ir en foco, no se agrega: se fotografía.**

⭐ CÓMO SE HACE ACÁ

  1. el dorado va DENTRO de la escena generada (`cumple-fondo-r18.png`): cintas
     metálicas colgando en el aire, globos champán y destellos, todo en el
     desenfoque del muro vegetal, con la mesa GENERADA VACÍA;
  2. de esa generación se toma **sólo el muro** y se compone sobre la toma real
     `Double Tree 25 jul 25-257.jpg`, que es la que trae el vaso nuevo, el plato
     y las dos medialunas REALES;
  3. la máscara es de COLOR, no un rectángulo: se reemplaza donde el píxel es
     VERDE (follaje). Así el vaso —que es kraft, o sea R>G— queda intacto por
     construcción, sin tener que recortarlo;
  4. y **la siembra de serpentinas en la mesa se elimina**: ya no se llama a
     `between-cumple-confeti-r14.py`. El adorno vive en el fondo.

⚠️ La continuidad 1→2 sigue saliendo de **dos recortes 4:5 REALES** de la misma
toma (x 1830-4902 y x 2688-5760), nunca de tejer ni espejar. Con el muro nuevo el
dorado se reparte a lo largo del par, así que cada slide ve cintas distintas y la
transición se lee.

Salida: raw/hilton/between/togo-25jul2025/base-r18-muro.jpg (5760×3840),
con la MISMA geometría que la 257: todos los recortes del pipeline siguen valiendo.
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

BASE = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-257.jpg"
GEN = RAIZ / "public/assets/hilton/between/ia-sept/cumple-fondo-r18.png"
SALIDA = RAIZ / "raw/hilton/between/togo-25jul2025/base-r18-muro.jpg"
PASOS = RAIZ / "out/hilton-between-r18/pasos"

#: el canto de la mesa en la toma real: por encima es muro
MURO_Y1 = 1883        # medido: la fila donde la calidez de la mesa se impone
DESVANECE = 160        # px de transición sobre el canto de la mesa

#: cuánto se aclara el muro nuevo respecto del que había. El muro real está en
#: mediana 51 (muy oscuro) y era parte de lo que el cliente leía como «no se
#: parece a Between»; el generado viene de día. Se deja MÁS CLARO a propósito,
#: pero no a tope: 0,80 de su propio brillo, para que no pelee con la mesa.
ASIENTO = 0.80


def mediana_verde(a):
    """Mediana de luminancia del FOLLAJE (los píxeles verdes)."""
    L = a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114
    verde = a[..., 1] > a[..., 0]
    return float(np.median(L[verde])) if verde.any() else float(np.median(L))


def main():
    if not BASE.exists():
        sys.exit(f"falta la toma original: {BASE}")
    if not GEN.exists():
        sys.exit(f"falta la generación: {GEN}")

    base = Image.open(BASE).convert("RGB")
    gen = Image.open(GEN).convert("RGB")
    W, H = base.size
    print(f"toma real {base.size} · generación {gen.size}")

    # la generación se lleva al ancho de la toma; su muro ocupa la parte alta
    fac = W / gen.width
    gen = gen.resize((W, int(round(gen.height * fac))), Image.LANCZOS)
    print(f"generación escalada a {gen.size} (×{fac:.3f})")

    a = np.asarray(base).astype(np.float32)
    b = np.asarray(gen).astype(np.float32)[:H]
    if b.shape[0] < H:
        b = np.vstack([b, np.repeat(b[-1:], H - b.shape[0], axis=0)])

    print(f"muro real: mediana del follaje {mediana_verde(a[:MURO_Y1]):.1f}")
    print(f"muro nuevo: mediana del follaje {mediana_verde(b[:MURO_Y1]):.1f} "
          f"→ se asienta a {ASIENTO}")
    b = np.clip(b * ASIENTO, 0, 255)

    # ── la máscara: TODO el muro menos el producto ──────────────────────────
    # ⛔⛔ EL ERROR DE LA PRIMERA PASADA, y salió a la vista de inmediato: la
    # máscara era «donde hay VERDE» (G > R+4). Pero las sombras profundas del
    # muro real no son verdes —son casi neutras y muy oscuras—, así que se
    # quedaban SIN reemplazar, y contra un muro nuevo más claro se leían como
    # **agujeros negros** repartidos por todo el follaje.
    #
    # El criterio correcto es el inverso: se reemplaza todo lo que NO es
    # producto. El único producto que sube al muro es el vaso, que es kraft
    # (R ≫ G); el follaje y sus sombras no lo son. Así la máscara cubre el muro
    # completo, sombras incluidas, y el vaso queda fuera.
    # ⛔ Y EL SEGUNDO ERROR, que dejó un CANTO HORIZONTAL DURO al medio: después
    # de invertir el criterio le agregué un paso de «proteger el producto» que
    # dibujaba el bbox de las componentes cálidas grandes. La componente grande
    # es la MESA (x 0..5760 · y 1533..3840), así que ese rectángulo bloqueaba el
    # muro entero por debajo de y=1533 y ahí quedaba el muro viejo, oscuro,
    # contra el nuevo: una línea recta de lado a lado.
    #
    # No hace falta ningún rectángulo. Medida la calidez fila a fila:
    #     y ≤1550  →   0 % cálido   (muro puro)
    #     y 1600-1850 → 18 %        (aparece el vaso)
    #     y ≥1900  →  71-97 %       (la mesa)
    # o sea que «no cálido» ya excluye el vaso y la mesa por sí solo, y el canto
    # de la mesa está en y≈1883 (no en 1820, que era una estimación mía).
    calido = (a[..., 0] > a[..., 1] + 10).astype(np.uint8)
    calido = cv2.morphologyEx(calido, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    verde = (1.0 - calido).astype(np.float32)
    verde = cv2.morphologyEx(verde, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))

    # y sólo por encima del canto de la mesa, con desvanecido
    banda = np.ones(H, np.float32)
    banda[MURO_Y1:] = 0.0
    r = np.linspace(1.0, 0.0, DESVANECE)
    banda[MURO_Y1 - DESVANECE:MURO_Y1] = r
    m = verde * banda[:, None]
    m = cv2.GaussianBlur(m, (0, 0), 9)
    print(f"máscara del muro: {100 * (m > 0.5).mean():.1f} % del cuadro "
          f"(el vaso queda fuera por su kraft)")

    salida = a * (1 - m[..., None]) + b * m[..., None]
    im = Image.fromarray(np.clip(salida, 0, 255).astype(np.uint8))

    # un remate de unificación: el canto de la mesa se suaviza apenas
    print(f"muro final: mediana del follaje {mediana_verde(np.asarray(im).astype(np.float32)[:MURO_Y1]):.1f}")

    im.save(SALIDA, quality=96, subsampling=0)
    PASOS.mkdir(parents=True, exist_ok=True)
    im.resize((W // 4, H // 4), Image.LANCZOS).save(
        PASOS / "muro-r18.jpg", quality=90)
    print(f"✓ {SALIDA.relative_to(RAIZ)}  {im.size}")
    print(f"  vista: {(PASOS / 'muro-r18.jpg').relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

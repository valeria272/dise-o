#!/usr/bin/env python3
"""QB · AYCD — deja limpia la fotografía aprobada del KV, sin su texto.

    python scripts/qb-aycd-limpiar-foto.py

POR QUÉ EXISTE
──────────────
La S5 pide una historia **animada** de ALL YOU CAN DRINK, y Eli dictó que el
bloque de marca —logotipo, el nombre y el botón verde con su degradado— no puede
variar respecto del KV. O sea: la pieza es el KV, pero con el bloque en
movimiento.

El problema es que el único archivo que tengo de ese KV es el PNG aplanado
(`PROMOS QB 2026 AYCD 2026 ST.png`, 2250×4000): la fotografía viene con el texto
ya quemado encima. Si animo el bloque sobre esa imagen, en cuanto el texto se
mueve aparece debajo el texto viejo.

⛔ Y NO se resuelve generando otra foto: QB tiene material propio y la regla del
estudio es que no se genera lo que ya está fotografiado. Ésta ES la foto aprobada
de la promo. Lo que hay que hacer es **quitarle el texto**, no reemplazarla.

CÓMO
────
El texto de QB es blanco puro sobre un fondo de barra oscuro y desenfocado, que
es el caso fácil del inpainting: se levanta una máscara por luminancia dentro de
las cajas donde SÉ que hay texto (las tengo medidas en `src/brand/qb.ts`), se
dilata para tomar el antialias, y se rellena con Telea.

⚠️ Sólo se toca dentro de las cajas medidas. Sin esa restricción la máscara se
come los brillos del vaso de espumante y la espuma del schop, que también son
blancos.

SALE
────
  raw/hilton/qb/aycd/AYCD-foto-limpia.png     2250×4000, lista para animar
  raw/hilton/qb/aycd/_control-limpieza.jpg    antes / máscara / después
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, "raw", "hilton", "qb", "aycd")
ORIGEN = os.path.join(BASE, "AYCD-ST-sep2026.png")
SALIDA = os.path.join(BASE, "AYCD-foto-limpia.png")
MATE = os.path.join(BASE, "AYCD-foto-copas.png")
CONTROL = os.path.join(BASE, "_control-limpieza.jpg")

# Cajas donde hay texto, medidas sobre el propio PNG a 2250×4000.
# (x0, y0, x1, y1) — con holgura para que entre la sombra suave del titular.
CAJAS = [
    (900, 410, 1350, 680),    # logotipo
    (480, 760, 1770, 1180),   # ALL YOU / CAN DRINK
    (600, 2700, 1650, 2830),  # TODOS LOS MARTES
    (600, 2830, 1650, 3030),  # botón verde + POR $13.990
    (680, 3060, 1570, 3170),  # 18:00 a 21:00 hrs
    # El pie va sobre negro puro: acá el inpainting simplemente devuelve negro,
    # que es exactamente lo que quiero — el legal y la lista se vuelven a
    # componer como texto vivo.
    (60, 3370, 2190, 3470),   # legal
    (300, 3700, 1950, 3870),  # lista de tragos
]


def main():
    if not os.path.exists(ORIGEN):
        sys.exit(f"No encuentro {ORIGEN}")

    rgb = np.asarray(Image.open(ORIGEN).convert("RGB"))
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    alto, ancho = bgr.shape[:2]

    lum = rgb.mean(axis=2)
    mascara = np.zeros((alto, ancho), np.uint8)

    for (x0, y0, x1, y1) in CAJAS:
        zona = lum[y0:y1, x0:x1]
        # El texto es blanco puro; el fondo de barra no pasa de ~120.
        mascara[y0:y1, x0:x1] = (zona > 150).astype(np.uint8) * 255

    # El botón verde es un plano de color, no texto: se borra entero para que el
    # inpainting no tenga que adivinar su borde recto.
    bx0, by0, bx1, by1 = 620, 2835, 1630, 3028
    mascara[by0:by1, bx0:bx1] = 255

    # Dilatar para tomarse el antialias y la sombra suave del titular.
    mascara = cv2.dilate(mascara, np.ones((13, 13), np.uint8), iterations=2)
    mascara = cv2.GaussianBlur(mascara, (9, 9), 0)
    mascara = (mascara > 40).astype(np.uint8) * 255

    limpio = cv2.inpaint(bgr, mascara, 9, cv2.INPAINT_TELEA)
    # Segunda pasada corta: Telea deja costuras finas en zonas de bokeh.
    limpio = cv2.inpaint(limpio, cv2.dilate(mascara, np.ones((3, 3), np.uint8)),
                         5, cv2.INPAINT_NS)

    Image.fromarray(cv2.cvtColor(limpio, cv2.COLOR_BGR2RGB)).save(SALIDA)
    print(f"✓ {os.path.relpath(SALIDA, RAIZ)}  {ancho}×{alto}")

    # ── El mate de las copas ────────────────────────────────────────────────
    # La referencia del brief tiene la tipografía CORTADA por el objeto del
    # primer plano. Acá el objeto son las copas, así que hace falta una capa que
    # vuelva a montarse encima del texto en movimiento.
    #
    # Las copas son lo brillante de la escena y el fondo es barra desenfocada y
    # oscura, así que el mate se saca de la propia luminancia, con una curva dura
    # para que el bokeh de las botellas —que también tiene luces— no se cuele.
    rgb_limpio = cv2.cvtColor(limpio, cv2.COLOR_BGR2RGB)
    lum_limpia = rgb_limpio.mean(axis=2)

    alfa = np.clip((lum_limpia - 26) / 58.0, 0, 1)  # negro hasta 26, opaco en 84
    alfa = alfa ** 1.35
    # Las copas viven en la mitad de la pieza. Arriba (pared de botellas) y abajo
    # (mesón) se apaga el mate para no reconstruir el fondo entero encima.
    alto_img = alfa.shape[0]
    yy = np.arange(alto_img)[:, None].astype(float)
    ventana = np.clip((yy - 1180) / 260.0, 0, 1) * np.clip((3420 - yy) / 300.0, 0, 1)
    alfa = alfa * ventana
    alfa = cv2.GaussianBlur(alfa, (0, 0), 1.2)

    copas = np.dstack([rgb_limpio, (alfa * 255).astype(np.uint8)])
    Image.fromarray(copas.astype(np.uint8), "RGBA").save(MATE)
    print(f"OK {os.path.relpath(MATE, RAIZ)}")

    # Hoja de control: antes | máscara | después, a un tercio.
    def mini(a):
        return Image.fromarray(a).resize((ancho // 4, alto // 4), Image.LANCZOS)

    hoja = Image.new("RGB", (3 * (ancho // 4) + 24, alto // 4), (18, 18, 18))
    hoja.paste(mini(rgb), (0, 0))
    hoja.paste(mini(np.stack([mascara] * 3, axis=2)), (ancho // 4 + 12, 0))
    hoja.paste(mini(cv2.cvtColor(limpio, cv2.COLOR_BGR2RGB)), (2 * (ancho // 4) + 24, 0))
    hoja.save(CONTROL, quality=88)
    print(f"✓ {os.path.relpath(CONTROL, RAIZ)}")


if __name__ == "__main__":
    main()

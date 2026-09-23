#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cambia los dos productos de la vitrina de la ST «EMERGENCIA BETWEEN» (S2, 9-sep).

⭐ RONDA 10 — 04-09-2026. Comentario del cliente en `STORIES!I15`, sin tachar, o
sea PENDIENTE (el otro comentario de esa celda, el de la diagramación, ya está
tachado y resuelto en la ronda 8):

    «Cambiaría que el salado sea un crosant jamon queso y que el dulce sea un
     muffin»

Qué cambia, y de dónde sale:

    compartimento 2 · DULCE   croissant simple  →  **muffin de chocolate**
    compartimento 3 · SALADO  sándwich baguette →  **croissant de jamón queso**

Los dos son **fotografía real del cliente**, recortada de la sesión
`25 jul 2025` con `scripts/between-recortes-reales.py`:

    muffin              Double Tree 25 jul 25-266.jpg
    croissant j/q       Double Tree 25 jul 25-278.jpg

No se genera comida: el cliente lleva tres rondas reclamando producto inventado
(vasos con logo falso, tazas con marca ajena). La regla del sistema es que la IA
hace ambiente, nunca producto — y acá el producto existe fotografiado.

Los productos viejos se borran con `cv2.inpaint`: el fondo del nicho es un panel
crema con un degradado suave y una diagonal de luz, que es el caso fácil. Las
molduras verticales del vidrio quedan fuera de la máscara para no comérselas.

Uso:
    python scripts/between-emergencia-productos.py
    python scripts/between-emergencia-productos.py --revisar
"""
import argparse
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402
from between_retoque import apetitoso, hombro, informe  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

FONDO = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-fondo.png"
DESTINO = RAIZ / "public/assets/hilton/between/ia-sept/emergencia-fondo-r10.png"
RECORTES = RAIZ / "public/assets/hilton/between/recortes"

#: cajas MEDIDAS sobre `emergencia-fondo.png` (2250×4000) con zoom al 1:1.
#: ⚠️ La primera pasada las estimó sobre una rejilla reducida y salieron 150 px
#: corridas: el inpaint se comió las molduras doradas del vidrio y dejó medio
#: croissant asomando. Se vuelven a medir sobre el recorte a tamaño real.
VIEJO_DULCE = (1008, 1582, 1268, 2112)     # el croissant simple
VIEJO_SALADO = (1392, 1586, 1638, 2108)    # el sándwich de baguette

#: ⚠️ Las molduras doradas del vidrio corren en x≈890-915, 980-1005, 1275-1300,
#: 1370-1395 y 1665+. Las cajas de arriba pasan POR DENTRO de esos huecos: si el
#: inpaint las toca, se lleva el vidrio.
HUECO = 268                                 # ancho libre entre molduras

#: el vaso generado del compartimento 1, que en la v2 también se reemplaza
VIEJO_CAFE = (566, 1584, 838, 2122)
#: el interior del cristal, donde —y sólo donde— va el reflejo
CRISTAL = (470, 1310, 1720, 2440)

#: ⭐ 3.ª pasada — EL FONDO, guiándose del brief. El brief pide «todo
#: fotografiado de forma atractiva y con ESTÉTICA BETWEEN, evitando que parezca
#: una caja de emergencia real», y el fondo que traía la generación era un
#: degradado ROSA-NARANJA que no está en la paleta de la marca: Between es beige
#: cálido (#FFF9EB) y café (#675B49). Se corrige el tiro de color hacia esos dos
#: y se le pone hombro a las altas, que estaban clipeando en un 3 % — o sea el
#: crema se iba a blanco puro y la pieza se veía lavada y quemada a la vez.
BEIGE_MARCA = (247, 240, 224)

#: cada producto nuevo, con ALTO objetivo. El ancho sale de la proporción del
#: recorte y se limita al hueco entre molduras — el producto no se deforma
#: jamás, se elige el giro que lo hace caber.
#: ⭐ v2: los tres se apoyan en una MISMA LÍNEA DE BASE en vez de centrarse cada
#: uno a su altura. Flotando a media altura y con masas distintas, la vitrina se
#: leía como tres recortes sueltos; alineados abajo se leen como una repisa, que
#: es lo que el ojo espera dentro de una caja. Es la mitad del «armonioso».
BASE = 2055

NUEVOS = [
    # (archivo, centro x, alto objetivo, giro en grados, luz, comida)
    # ⭐ v2: el café TAMBIÉN pasa a ser el vaso real. Con dos productos
    #    fotografiados y uno generado, la vitrina se leía disparejo — que es
    #    exactamente el «se ve pegoteado» de Eli.
    ("vaso-248.png", 702, 470, 0, 1.00, False),
    # ⭐ v2: el muffin sale MUY oscuro contra el panel crema y se lee como un
    #    borrón. Se le levantan las sombras un 34 % — es lo que pidió Eli
    #    («edita el muffin porque se ve muy oscuro») y además lo devuelve al
    #    rango del resto.
    ("muffin-chocolate.png", 1138, 300, 0, 1.26, True),
    # el croissant se pone casi vertical, que es lo que ya hacía la vitrina con
    # el croissant anterior: los nichos son altos y angostos y un croissant
    # acostado mide 18 cm, tres veces el hueco. −86° deja la punta arriba y el
    # queso escurriendo hacia el mismo lado que la luz.
    ("croissant-jamon-queso.png", 1512, 430, -78, 1.02, True),
]

#: la luz del nicho entra por arriba a la izquierda: la sombra cae abajo-derecha
SOMBRA_DESPLAZA = (24, 26)
SOMBRA_OPACIDAD = 0.30
SOMBRA_DIFUSA = 26


def borra(bgr, cajas):
    """Borra los productos viejos del panel del nicho."""
    mascara = np.zeros(bgr.shape[:2], np.uint8)
    for x0, y0, x1, y1 in cajas:
        # se agranda hacia abajo y a la derecha para llevarse también la sombra
        cv2.rectangle(mascara, (x0 - 12, y0 - 12), (x1 + 46, y1 + 40), 255, -1)
    return cv2.inpaint(bgr, mascara, 17, cv2.INPAINT_TELEA)


def campo_de_luz(bgr):
    """La luz que hay DENTRO del nicho, como un campo suave.

    Es la pieza que faltaba en la v1 y la razón de que se viera pegoteado: los
    recortes entraban con la luz de la mesa del local (sol lateral, cálido) a un
    nicho iluminado en diagonal desde arriba a la izquierda. Multiplicando cada
    producto por este campo, los tres reciben la MISMA luz que la caja.
    """
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB).astype(np.float32)
    suave = cv2.GaussianBlur(rgb, (0, 0), 90)
    lum = suave.mean(axis=2, keepdims=True)
    ref = float(np.median(lum[1500:2300, 500:1700]))
    return np.clip(lum / max(ref, 1.0), 0.72, 1.28)


def brillo_del_vidrio(bgr):
    """Los reflejos del cristal, para volver a ponerlos ENCIMA de los productos.

    Sin esto los recortes quedan pegados sobre el vidrio en vez de detrás. Es el
    detalle que más hace por la ilusión y cuesta tres líneas.
    """
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB).astype(np.float32)
    return np.clip(rgb - cv2.GaussianBlur(rgb, (0, 0), 28), 0, None)


def pega(lienzo, ruta, cx, base, alto_objetivo, giro, luz=1.0, campo=None,
         comida=False):
    """Pega un recorte apoyado en `base`, con su sombra, sin deformarlo."""
    p = Image.open(ruta).convert("RGBA")
    if comida:
        # claridad y cuerpo: dentro de un nicho crema, el chocolate sin retoque
        # se lee como una mancha parda. Es el «edita el muffin» de Eli.
        alfa = p.getchannel("A")
        p = apetitoso(p.convert("RGB"), claridad=0.5, cuerpo=1.22,
                      calor=5.0).convert("RGBA")
        p.putalpha(alfa)
    if luz != 1.0:
        # se levantan las sombras sin quemar las luces (curva de raíz)
        a = np.asarray(p).astype(np.float32)
        rgb = a[..., :3] / 255.0
        a[..., :3] = np.power(rgb, 1.0 / luz) * 255.0
        p = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    if giro:
        p = p.rotate(giro, resample=Image.BICUBIC, expand=True)
    # escala UNIFORME: se busca el alto pedido y, si el ancho no cabe entre las
    # molduras, manda el ancho. Nunca se estira un eje contra el otro.
    escala = min(alto_objetivo / p.height, HUECO / p.width)
    ancho, alto = round(p.width * escala), round(p.height * escala)
    p = p.resize((ancho, alto), Image.LANCZOS)
    cy = base - alto // 2

    sombra = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    tinta = Image.new("RGBA", p.size, (58, 44, 32, 255))
    tinta.putalpha(p.getchannel("A"))
    sombra.alpha_composite(tinta, (cx - ancho // 2 + SOMBRA_DESPLAZA[0],
                                   cy - alto // 2 + SOMBRA_DESPLAZA[1]))
    sombra = sombra.filter(ImageFilter.GaussianBlur(SOMBRA_DIFUSA))
    canal = sombra.getchannel("A").point(lambda v: int(v * SOMBRA_OPACIDAD))
    sombra.putalpha(canal)

    lienzo.alpha_composite(sombra)

    if campo is not None:
        # el producto recibe la luz del nicho antes de entrar
        px, py = cx - ancho // 2, cy - alto // 2
        trozo = campo[py:py + alto, px:px + ancho]
        a = np.asarray(p).astype(np.float32)
        a[..., :3] *= trozo
        p = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

    lienzo.alpha_composite(p, (cx - ancho // 2, cy - alto // 2))
    return lienzo, (ancho, alto)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true")
    a = ap.parse_args()
    if not FONDO.exists():
        sys.exit(f"⛔ Falta {FONDO}")

    bgr = cv2.imread(str(FONDO))
    campo = campo_de_luz(bgr)
    vidrio = brillo_del_vidrio(bgr)
    limpio = borra(bgr, [VIEJO_CAFE, VIEJO_DULCE, VIEJO_SALADO])
    lienzo = Image.fromarray(cv2.cvtColor(limpio, cv2.COLOR_BGR2RGB)).convert("RGBA")
    for archivo, cx, alto_obj, giro, luz, comida in NUEVOS:
        lienzo, medida = pega(lienzo, RECORTES / archivo, cx, BASE, alto_obj, giro,
                              luz=luz, campo=campo, comida=comida)
        print(f"  · {archivo}  {medida[0]}×{medida[1]} px  giro {giro}°  luz ×{luz}")

    # ⭐ y el cristal vuelve ENCIMA: los productos quedan detrás del vidrio, que
    #    es donde están. Sin este paso la vitrina se lee como tres calcomanías.
    # ⚠️ Al 0,85 y sobre TODO el lienzo, esto lava la pieza entera y la deja
    #    lechosa. Va sólo dentro del cristal y a un tercio de fuerza: el reflejo
    #    tiene que insinuarse, no protagonizar.
    plano = np.asarray(lienzo.convert("RGB")).astype(np.float32)
    dentro = np.zeros(plano.shape[:2], np.float32)
    cv2.rectangle(dentro, CRISTAL[:2], CRISTAL[2:], 1.0, -1)
    dentro = cv2.GaussianBlur(dentro, (0, 0), 12)[:, :, None]
    velo = 255.0 - (255.0 - plano) * (255.0 - vidrio * 0.30) / 255.0    # trama screen
    plano = plano * (1 - dentro) + velo * dentro
    lienzo = Image.fromarray(np.clip(plano, 0, 255).astype(np.uint8)).convert("RGBA")

    # ── el fondo, a la paleta de la marca y sin quemar ──
    lienzo_np = np.asarray(lienzo.convert("RGB")).astype(np.float32)
    # el tiro de color se mide sobre el crema del propio fondo (esquina superior)
    muestra = lienzo_np[200:600, 120:520].reshape(-1, 3).mean(axis=0)
    correccion = np.clip(np.array(BEIGE_MARCA, np.float32) / np.maximum(muestra, 1.0),
                         0.90, 1.10)
    lienzo_np = hombro(lienzo_np * correccion[None, None, :])
    lienzo = Image.fromarray(np.clip(lienzo_np, 0, 255).astype(np.uint8)).convert("RGBA")
    informe(lienzo.convert("RGB"), "ST Emergencia")

    lienzo.convert("RGB").save(DESTINO)
    print(f"✓ {DESTINO.relative_to(RAIZ)}  {lienzo.size}")

    if a.revisar:
        ruta = RAIZ / "out/hilton-between-r10/emergencia-vitrina.png"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        lienzo.convert("RGB").crop((150, 1150, 2100, 2650)).resize((975, 750)).save(ruta)
        print(f"→ revisión: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAFÉ DE CUMPLEAÑOS (FEED 09-sep, S1) — las dos fotos base de la ronda 11.

Lo que pide la ronda:

· Cliente, comentario nativo en `FEED!E15` (Scarlette, 03-09 22:25, VIVO):
    «usemos la imagen que te adjunto acá igual hay que retocarla, cambiar el
     vaso al nuevo, sacar el plato de los vigilantes, y poderle algo que haga
     ref a cumpleaños al rededor (quizas en la mesa poner como esos PAPELITOS
     DE COLORES que se lanzan) y la imagen de la slide 2 tiene que tener
     relación igual con la primera»
· Eli, ronda 10: «se ve mal diagramadas», «el color está muy oscuro», «no se ve
  un retoque que se vea apetitosa», «borrar los rayones de la mesa».
· Eli, hoy: el editable de la slide 2 —el post de IG con el listado— para
  mejorarlo.

⛔⛔ LO QUE SE CAE, Y ES EL DEFECTO GRANDE DE LA RONDA 10: EL PANORAMA TEJIDO.

`between-cumple-panorama.py` alargaba la escena a 4500 px espejando el flanco
derecho de la original. Pero la original mide 5760 y la slide 1 ya se lleva
hasta x=4902: de la slide 2 sólo **858 px son reales** y los otros 2.214 son el
mismo flanco espejado una y otra vez. Medido sobre la entrega: el fondo de la
slide 2 es un AZULEJO SIMÉTRICO — el follaje dibuja mariposas repetidas cinco
veces y la veta de la mesa traza un festón ondulado que se refleja en el eje. Es
exactamente lo que el cliente lleva un mes pidiendo que no pase («que no se vea
tan IA»), y es lo que Eli vio como «mal diagramada».

⭐ La salida: **las dos slides son dos recortes REALES de la misma toma.** La
original (`25-257`, 5760×3840) da dos 4:5 de 3072 px:

    slide 1 → x 1830-4902   (el café CON las medialunas, como pidió Eli)
    slide 2 → x 2688-5760   (la mesa sigue hacia la derecha)

Se superponen 2.214 px, o sea que el vaso sale en las dos. **No es un problema,
es la solución:** en la slide 2 el vaso cae justo detrás del mock del post de
Instagram, así que lo que queda a la vista es la mesa abierta y el muro de la
derecha — la franja que la slide 1 no muestra. La continuidad la da el recorte;
el mock tapa la repetición. Cero espejo, cero IA, cero producto inventado.

⭐ Y los PAPELITOS. Es un pedido literal del cliente que la ronda 10 anotó pero
no se ve en la entrega. Se siembran con `papelitos()`, que es lo que hace
creíble un elemento agregado:
  · el TAMAÑO crece hacia el borde inferior (lo cercano se ve más grande);
  · el DESENFOQUE sigue la profundidad de campo REAL de la toma —un 50 mm a
    f/3,5 tiene el plano de foco en el plato, así que un papelito al canto de la
    mesa va tan blando como la madera que lo rodea—;
  · cada uno deja una SOMBRA de contacto corta y difusa. Sin sombra, un papel
    sobre una mesa flota y se lee como pegado.
  · paleta CORTA y apagada (coral, dorado, crema, rosa viejo, salvia): son
    papelitos de fiesta, no un confeti de plantilla que le pelee el cuadro al
    café.

Salidas: cumple-r11-1.jpg y cumple-r11-2.jpg en fotos-gradadas/.
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from between_retoque import apetitoso, informe, nitidez, revela, vivo

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/between/togo-25jul2025/Double Tree 25 jul 25-257.jpg"
FOTOS = RAIZ / "public/assets/hilton/between/fotos-gradadas"
PASOS = RAIZ / "out/hilton-between-r11/pasos"

W0, H0 = 5760, 3840
SALIDA = (2250, 2812)
ESC = SALIDA[0] / 3072                      # 0,7324 — del recorte a la entrega

#: los dos recortes 4:5 REALES de la original
RECORTES = {
    1: (1830, 0, 1830 + 3072, 3840),
    2: (5760 - 3072, 0, 5760, 3840),
}

#: el canto de la mesa contra el muro vegetal, medido sobre la original
BORDE_IZQ, BORDE_DER = 1843, 1786

#: geometría en la ORIGINAL (x, y de la toma completa)
PLATO = (487, 1990, 4076, 3330)             # el plato de las medialunas
COMIDA = (1050, 1880, 3620, 2760)           # las dos medialunas
VASO = (3560, 1120, 4800, 2920)             # el vaso To Go

#: paleta de los papelitos — corta y apagada, a propósito
COLORES = [(214, 106, 83), (214, 170, 92), (238, 226, 203),
           (196, 137, 145), (150, 166, 133)]


# --------------------------- utilidades de máscara ---------------------------
def caja_mask(forma, x0, y0, x1, y1):
    h, w = forma
    yy, xx = np.mgrid[0:h, 0:w]
    return (xx >= x0) & (xx <= x1) & (yy >= y0) & (yy <= y1)


def elipse_mask(forma, x0, y0, x1, y1):
    h, w = forma
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    rx, ry = max(1, (x1 - x0) / 2), max(1, (y1 - y0) / 2)
    yy, xx = np.mgrid[0:h, 0:w]
    return ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1.0


def zona_mesa(forma, x0_recorte):
    """La mesa dentro del recorte ya escalado a la entrega."""
    h, w = forma
    xs = np.arange(w, dtype=np.float32) / ESC + x0_recorte
    borde = (BORDE_IZQ + (BORDE_DER - BORDE_IZQ) * xs / W0) * ESC
    ys = np.arange(h, dtype=np.float32)[:, None]
    return ys > (borde[None, :] + 24)


def local(caja, x0_recorte):
    """Pasa una caja de la ORIGINAL a coordenadas de la entrega."""
    x0, y0, x1, y1 = caja
    return (int((x0 - x0_recorte) * ESC), int(y0 * ESC),
            int((x1 - x0_recorte) * ESC), int(y1 * ESC))


# ------------------------- limpieza de la mesa --------------------------------
def limpia(im, zona, calidez=40, dilata=15, radio=12):
    """Rayones y grietas por CROMA — igual que en el carrusel To Go: la madera
    de Between es cálida (R−B alto) y las marcas son grises."""
    rgb = np.asarray(im.convert("RGB"))
    a = rgb.astype(np.float32)
    marcas = ((a[..., 0] - a[..., 2]) < calidez) & zona
    m = marcas.astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21)))
    m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (dilata, dilata)))
    out = cv2.inpaint(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), m, radio, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB)), int((m > 0).sum())


def realza_impresion(im, region, claridad=0.75, radio=15):
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    base = cv2.GaussianBlur(a, (0, 0), radio)
    m = cv2.GaussianBlur(region.astype(np.float32) * 255, (0, 0), 25)[:, :, None] / 255.0
    return Image.fromarray(np.clip(a + (a - base) * claridad * m, 0, 255).astype(np.uint8))


# ----------------------------- los papelitos ---------------------------------
def papelitos(im, permitido, y_foco, semilla, cuantos=17):
    """Siembra papelitos de fiesta sobre la mesa.

    `permitido` es la máscara de dónde pueden caer (mesa libre, sin plato, sin
    vaso, sin comida). `y_foco` es la fila del plano de foco: cuanto más lejos
    de ahí cae un papelito, más blando va — es la profundidad de campo de la
    toma, y sin eso el papel se lee como una calcomanía sobre una foto.
    """
    rnd = np.random.default_rng(semilla)
    base = im.convert("RGBA")
    W, H = base.size
    puestos = 0
    intentos = 0
    ys, xs = np.where(permitido)
    if len(ys) == 0:
        return im
    while puestos < cuantos and intentos < cuantos * 40:
        intentos += 1
        i = int(rnd.integers(0, len(ys)))
        cy, cx = int(ys[i]), int(xs[i])
        # tamaño por cercanía: al canto inferior el papel se ve más grande
        prof = cy / H
        lado = int(rnd.integers(18, 34) * (0.50 + 1.05 * prof))
        largo = int(lado * float(rnd.uniform(2.4, 4.3)))
        if cx - largo < 4 or cx + largo > W - 4 or cy - largo < 4 or cy + largo > H - 4:
            continue
        # no se siembra encima de nada que no sea mesa libre
        if not permitido[cy - lado:cy + lado, cx - lado:cx + lado].all():
            continue

        col = COLORES[int(rnd.integers(0, len(COLORES)))]
        ang = float(rnd.uniform(0, 180))
        sup = 4                                     # se dibuja a 4x y se baja
        tira = Image.new("RGBA", (largo * sup, lado * sup), (0, 0, 0, 0))
        ImageDraw.Draw(tira).rounded_rectangle(
            [0, 0, largo * sup - 1, lado * sup - 1], radius=lado * sup // 3,
            fill=col + (222,))
        tira = tira.resize((largo, lado), Image.LANCZOS).rotate(ang, expand=True,
                                                                resample=Image.BICUBIC)
        # la profundidad de campo: blando si está lejos del plano de foco
        desenfoque = min(6.0, abs(cy - y_foco) / (H * 0.20) * 3.4)
        if desenfoque > 0.4:
            tira = tira.filter(ImageFilter.GaussianBlur(desenfoque))

        # sombra de contacto: corta, difusa y desplazada apenas hacia abajo
        sombra = Image.new("RGBA", tira.size, (0, 0, 0, 0))
        sombra.putalpha(tira.getchannel("A").point(lambda v: int(v * 0.42)))
        sombra = sombra.filter(ImageFilter.GaussianBlur(max(2.0, desenfoque + 2.4)))
        px, py = cx - tira.width // 2, cy - tira.height // 2
        base.alpha_composite(sombra, (px + 2, py + max(3, lado // 6)))
        base.alpha_composite(tira, (px, py))
        puestos += 1
    print(f"   papelitos sembrados: {puestos}")
    return base.convert("RGB")


# --------------------------------- la pieza ----------------------------------
def una(n):
    x0, y0, x1, y1 = RECORTES[n]
    im = Image.open(ORIGEN).convert("RGB").crop((x0, y0, x1, y1)).resize(
        SALIDA, Image.LANCZOS)
    forma = (im.height, im.width)
    print(f"\n-- slide {n} - recorte real x {x0}-{x1} -> {im.width}x{im.height}")
    informe(im, "crudo")

    plato = elipse_mask(forma, *local(PLATO, x0))
    comida = caja_mask(forma, *local(COMIDA, x0))
    vaso = caja_mask(forma, *local(VASO, x0))
    mesa = zona_mesa(forma, x0) & ~plato & ~comida & ~vaso

    im, marcas = limpia(im, mesa)
    print(f"   rayones y grietas borrados: {marcas:,} px")

    # el revelado: «el color está muy oscuro» se arregla por MEDIOS
    im = revela(im, medios=104, negros=0.008, contraste=1.05, calidez_max=21.0)
    informe(im, "revelada")
    if comida.any():
        im = apetitoso(im, mascara=comida.astype(np.float32),
                       claridad=0.50, cuerpo=1.08, calor=3.5)
    im = realza_impresion(im, vaso, claridad=0.70)
    im = vivo(im, vibrancia=0.20)
    im = nitidez(im, cantidad=0.32, radio=1.4)

    # y los papelitos, encima de la mesa ya limpia y revelada
    libre = mesa.copy()
    libre[:, :90] = False
    libre[:, -90:] = False
    libre[-70:, :] = False
    y_foco = int((PLATO[1] + PLATO[3]) / 2 * ESC)
    im = papelitos(im, libre, y_foco, semilla=1830 + n)

    if n == 2:
        # ⭐ La slide 2 es FONDO DE SOPORTE, no protagonista, y eso resuelve de
        #    paso el único pero del recorte: las dos slides comparten 2.214 px
        #    de la misma toma, así que a igual nitidez se leerían como «la misma
        #    foto dos veces». Desenfocada, la slide 2 pasa a ser el escenario
        #    del post —igual que hizo la ronda 7 con el rincón del local— y
        #    encima se lee mucho mejor el listado, que es lo que esta gráfica
        #    tiene que comunicar.
        im = im.filter(ImageFilter.GaussianBlur(9))
        print("   desenfoque de fondo aplicado (9 px)")

    informe(im, "final")
    destino = FOTOS / f"cumple-r11-{n}.jpg"
    im.save(destino, quality=95, subsampling=0)
    PASOS.mkdir(parents=True, exist_ok=True)
    im.resize((im.width // 3, im.height // 3), Image.LANCZOS).save(
        PASOS / f"cumple-r11-{n}.jpg", quality=88)
    print(f"   -> {destino.name}")


if __name__ == "__main__":
    if not ORIGEN.exists():
        sys.exit(f"falta la original: {ORIGEN}")
    for n in (int(x) for x in (sys.argv[1:] or ["1", "2"])):
        una(n)
    print("\nlisto.")

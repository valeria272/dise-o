#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rehace la PORTADA del carrusel PROMOS TO GO (FEED 14-sep, S3) con material real.

⭐ RONDA 10 — 04-09-2026. Dos pedidos que apuntan a lo mismo.

El del cliente, en `FEED!L15` y SIN TACHAR, o sea el único vivo de esa celda:

    «Mismo comentario que antes sobre la G1, el fondo no tiene nada que ver con
     BT, tenemos algunos videos que hemos hecho en la entrada de BT, saquemos el
     fondo de ahí?»

Y el de Eli hoy: «el carrusel de la S3 tiene errores del fondo con la chica,
debes hacerlo mejor editado ya que el vaso está erróneo».

Qué se cambia
-------------
1. **EL FONDO ES EL LOCAL DE VERDAD.** Sale de `raw/hilton/between/espacios/
   HDT_56.jpg`, la fotografía de arquitectura del propio Between: la barra de
   mármol con la cubierta de madera a la derecha, el mural dorado a la
   izquierda y el pasillo de parquet que va hacia el muro vegetal de la entrada.
   Es literalmente «la entrada de BT» que pide el cliente, y es una foto suya.
   Va desenfocado a la profundidad de campo de la escena y regradado a su luz.
   ⚠️ No se usó video: las únicas grabaciones que viajan en el repo son del 2.º
      piso (`cowork-2do-piso/`). Si aparece el metraje de la entrada, se cambia
      la placa y nada más — el resto del montaje no depende de ella.

2. **EL VASO ES EL VASO.** Se reemplaza el generado por el REAL, recortado de
   `Double Tree 25 jul 25-248.jpg` con grabCut. El generado tenía tres defectos
   que se leen a primera vista, medidos con zoom sobre la entrega de la ronda 9:
     · la tapa era un domo acanalado con una pestaña inventada; la de Between es
       una tapa lisa con un agujero ovalado y faldón limpio;
     · la proporción estaba mal — cuerpo 665 px de ancho por 837 de alto (0,79)
       cuando el vaso real mide 1,01: el generado era un vaso alto y angosto que
       no existe;
     · el cartón no tenía fibra y el logotipo se leía como calcomanía.
   Los DEDOS se devuelven encima del vaso nuevo. Se separan por color, que en
   esta escena es limpio y medido:
       piel   G−B ≈ 12–14     cartón kraft  G−B ≈ 38–41     fondo  G−B ≈ −1

⚠️ La chica se mantiene: el cliente objetó el FONDO y el vaso, no a la modelo
   («me gusta que sea otra propuesta la G1» está tachado, o sea resuelto).

Uso:
    python scripts/between-togo1-real.py
    python scripts/between-togo1-real.py --revisar
"""
import argparse
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402
from between_retoque import luz_envolvente, nitidez, revela  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ESCENA = RAIZ / "public/assets/hilton/between/ia-sept/togo-salida-3.png"   # 3584×4800
LOCAL = RAIZ / "raw/hilton/between/espacios/HDT_56.jpg"                     # 6718×4479
VASO = RAIZ / "public/assets/hilton/between/recortes/vaso-248.png"
DESTINO = RAIZ / "public/assets/hilton/between/fotos-gradadas/togo-salida-real.jpg"

LIENZO = (3584, 4480)          # 4:5 de trabajo
SALIDA = (2250, 2812)
CORTE_ESCENA = (0, 160, 3584, 4640)

# ── el vaso generado, MEDIDO sobre `togo-salida-3.png` ───────────────────────
#: cuerpo: bordes 930→1595 en y=2049 (665 px de ancho) y hasta y=2886; tapa
#: 1830→2055. La silueta completa, para borrarla antes de pegar el real.
VASO_VIEJO_CUERPO = (2049, 2886)
VASO_VIEJO_DER_ARRIBA = 1595
VASO_VIEJO_ANCHO_ARRIBA = 665
#: la SILUETA del vaso generado, ceñida: la tapa y el tronco del cuerpo. Ceñida
#: y no una caja holgada, porque lo que se borra fuera de ella son la camiseta y
#: el abrigo de la chica, y el inpaint los deja como una mancha.
VASO_VIEJO_TAPA = (868, 1786, 1636, 2062)
VASO_VIEJO_POLIGONO = [(928, 2040), (1598, 2040), (1534, 2906), (1046, 2906)]
#: el recorte real: cuerpo de y=534 a y=1648, bordes 59→1188 arriba (1129 px)
VASO_REAL_CUERPO = (534, 1648)
VASO_REAL_DER_ARRIBA = 1188
VASO_REAL_ANCHO_ARRIBA = 1129

# ⛔ Primer intento: escalar el vaso real igualando el ALTO del cuerpo (0,751).
#    Salió mal y la razón es interesante: el vaso generado está DESPROPORCIONADO
#    —cuerpo 665 de ancho por 837 de alto (0,79) contra 1,01 del real—, así que
#    igualando el alto el vaso real sale un 70 % más ancho, se le come la mano y
#    los dedos le tapan el logotipo. Manda el ANCHO: es lo que fija la relación
#    entre la mano y el vaso, que es lo que el ojo lee. Y como entonces el vaso
#    queda más bajo que el generado, el generado hay que BORRARLO antes.

#: dónde están los dedos, para devolverlos encima del vaso nuevo
DEDOS_CAJA = (800, 2120, 1680, 2940)

#: el mural dorado a la izquierda, el pasillo al centro y la barra de mármol a
#: la derecha — el mismo reparto que tenía la escena generada, así que la luz
#: sobre la chica sigue calzando
LOCAL_CORTE_X = 1700
#: ⚠️ y se recorta desde y=380: con la placa a altura completa, un plafón del
#: techo del local caía EXACTAMENTE sobre su cabeza y se leía como un error de
#: montaje, no como una luminaria. Bajando el recorte, el techo sale de cuadro.
LOCAL_CORTE_Y = 380


def recorta_local():
    """La placa real del local: 4:5, desenfocada y regradada a la escena."""
    im = Image.open(LOCAL).convert("RGB")
    alto = im.height - LOCAL_CORTE_Y
    ancho = round(alto * LIENZO[0] / LIENZO[1])
    placa = im.crop((LOCAL_CORTE_X, LOCAL_CORTE_Y,
                     LOCAL_CORTE_X + ancho, LOCAL_CORTE_Y + alto))
    placa = placa.resize(LIENZO, Image.LANCZOS)
    # ⭐ v2 — 26 px de desenfoque era demasiado: el fondo quedaba en puré y la
    #    chica encima se leía como un cartón pegado sobre una mancha. A 13 px el
    #    local todavía se reconoce —la barra de mármol, el pasillo— y la figura
    #    tiene contra qué apoyarse. El «se ve mal montada» empieza acá.
    placa = placa.filter(ImageFilter.GaussianBlur(13))
    arr = np.asarray(placa).astype(np.float32)
    # HDT_56 es una foto de arquitectura muy contrastada; se aplana un poco y se
    # sube el punto negro para que no compita con la figura
    arr = 24 + arr * 0.88
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def cambia_vaso(escena):
    """Reemplaza el vaso generado por el real y devuelve los dedos encima."""
    original = np.asarray(escena).astype(np.int16)
    vaso = Image.open(VASO).convert("RGBA")

    escala = VASO_VIEJO_ANCHO_ARRIBA / VASO_REAL_ANCHO_ARRIBA
    nuevo = vaso.resize((round(vaso.width * escala), round(vaso.height * escala)),
                        Image.LANCZOS)
    # ⭐ 22 px a la izquierda del calce exacto: la tapa del vaso generado era
    #   más ancha por ese lado y, si no se tapa, la franja que queda se rellena
    #   por inpaint y se lee como un manchón de cartón al costado del vaso.
    px = round(VASO_VIEJO_DER_ARRIBA - VASO_REAL_DER_ARRIBA * escala) - 22
    py = round(VASO_VIEJO_CUERPO[0] - VASO_REAL_CUERPO[0] * escala)

    # ⭐ Se borra SÓLO lo que el vaso nuevo no va a tapar. Borrar la silueta
    #    entera y después pegar encima parece equivalente, pero no lo es: el
    #    vaso nuevo es más bajo, así que quedaba una franja inpaintada sobre la
    #    camiseta y el abrigo, y se veía como un manchón rosado. Así el resto de
    #    la chica conserva sus píxeles originales.
    alto_v, ancho_v = np.asarray(escena).shape[:2]
    silueta = np.zeros((alto_v, ancho_v), np.uint8)
    cv2.rectangle(silueta, VASO_VIEJO_TAPA[:2], VASO_VIEJO_TAPA[2:], 255, -1)
    cv2.fillPoly(silueta, [np.array(VASO_VIEJO_POLIGONO, np.int32)], 255)
    tapado = np.zeros((alto_v, ancho_v), np.uint8)
    alfa_nuevo = np.asarray(nuevo.getchannel("A"))
    y1v, x1v = min(alto_v, py + nuevo.height), min(ancho_v, px + nuevo.width)
    tapado[max(0, py):y1v, max(0, px):x1v] = (
        alfa_nuevo[:y1v - max(0, py), :x1v - max(0, px)] > 24) * 255
    sobra = cv2.dilate(cv2.bitwise_and(silueta, cv2.bitwise_not(tapado)),
                       cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))
    if sobra.any():
        bgr = cv2.cvtColor(np.asarray(escena), cv2.COLOR_RGB2BGR)
        bgr = cv2.inpaint(bgr, sobra, 19, cv2.INPAINT_TELEA)
        escena = Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
        print(f"  sobra del vaso viejo borrada ({int((sobra > 0).sum())} px)")

    lienzo = escena.convert("RGBA")
    lienzo.alpha_composite(nuevo, (px, py))
    print(f"  vaso real {nuevo.size} en ({px}, {py})  escala {escala:.3f}")

    # ── los dedos vuelven encima ──
    x0, y0, x1, y1 = DEDOS_CAJA
    zona = original[y0:y1, x0:x1]
    R, G, B = zona[..., 0], zona[..., 1], zona[..., 2]
    piel = ((G - B) < 26) & ((R - B) > 55) & (R > 90)
    piel = cv2.morphologyEx(piel.astype(np.uint8) * 255, cv2.MORPH_CLOSE,
                            cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
    piel = cv2.morphologyEx(piel, cv2.MORPH_OPEN,
                            cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    n, lab, st, _ = cv2.connectedComponentsWithStats(piel, 8)
    if n > 1:
        # la mano es una sola mancha: se descartan las motas
        grandes = [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 4000]
        piel = np.isin(lab, grandes).astype(np.uint8) * 255
    piel = cv2.GaussianBlur(piel, (0, 0), 1.6)
    parche = Image.fromarray(np.dstack([zona.astype(np.uint8), piel]))
    lienzo.alpha_composite(parche, (x0, y0))
    print(f"  dedos devueltos ({int((piel > 128).sum())} px)")
    return lienzo.convert("RGB")


def recorta_figura(escena_4x5):
    """Silueta de la chica con el vaso, por grabCut."""
    bgr = cv2.cvtColor(np.asarray(escena_4x5), cv2.COLOR_RGB2BGR)
    h, w = bgr.shape[:2]
    mask = np.full((h, w), cv2.GC_BGD, np.uint8)
    cv2.rectangle(mask, (680, 460), (2980, h - 1), cv2.GC_PR_FGD, -1)
    # torso y piernas: frente seguro
    cv2.rectangle(mask, (1250, 1500), (2200, h - 1), cv2.GC_FGD, -1)
    # el vaso también, que si no grabCut lo lee como objeto aparte
    cv2.rectangle(mask, (900, 1900), (1600, 2900), cv2.GC_FGD, -1)
    # la cabeza, para que no se le vaya el pelo
    cv2.rectangle(mask, (1630, 800), (2000, 1400), cv2.GC_FGD, -1)
    # ⛔ y AQUÍ estaba el defecto de la primera pasada: con «probable frente» en
    #    todo el rectángulo, grabCut se quedó con un trozo del muro vegetal
    #    generado alrededor de la cabeza y quedó pegado como un parche verde.
    #    Sobre y bajo la cabeza el fondo es fondo SEGURO, sin discusión.
    cv2.rectangle(mask, (0, 0), (w - 1, 640), cv2.GC_BGD, -1)
    cv2.rectangle(mask, (0, 640), (1330, 1520), cv2.GC_BGD, -1)
    cv2.rectangle(mask, (2320, 640), (w - 1, 1520), cv2.GC_BGD, -1)
    # los flancos son fondo seguro
    cv2.rectangle(mask, (0, 0), (660, h - 1), cv2.GC_BGD, -1)
    cv2.rectangle(mask, (3000, 0), (w - 1, h - 1), cv2.GC_BGD, -1)
    bg, fg = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(bgr, mask, None, bg, fg, 6, cv2.GC_INIT_WITH_MASK)
    b = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    b = cv2.morphologyEx(b, cv2.MORPH_CLOSE,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25)))
    n, lab, st, _ = cv2.connectedComponentsWithStats(b, 8)
    if n > 1:
        mayor = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
        b = np.where(lab == mayor, 255, 0).astype(np.uint8)
    relleno = b.copy()
    cv2.floodFill(relleno, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 255)
    b = b | cv2.bitwise_not(relleno)
    alfa = cv2.GaussianBlur(b, (0, 0), 2.2)
    return Image.fromarray(np.dstack([np.asarray(escena_4x5), alfa]))


def grada_neutro(im):
    arr = np.asarray(im).astype(np.float32)
    calidez = float(arr[..., 0].mean() - arr[..., 2].mean())
    if calidez > 22:
        ajuste = (calidez - 21.0) * 0.55
        arr[..., 0] -= ajuste * 0.62
        arr[..., 2] += ajuste * 0.38
    p95 = float(np.percentile(arr, 95))
    if p95 > 0:
        arr *= min(1.06, max(0.90, 216.0 / p95))
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true")
    a = ap.parse_args()
    for r in (ESCENA, LOCAL, VASO):
        if not r.exists():
            sys.exit(f"⛔ Falta {r}")

    escena = Image.open(ESCENA).convert("RGB")
    print("1 · el vaso real entra en la escena")
    escena = cambia_vaso(escena)
    escena = escena.crop(CORTE_ESCENA)

    print("2 · silueta de la figura")
    figura = recorta_figura(escena)

    print("3 · la placa real del local")
    fondo = recorta_local()

    # ⭐ v2 — luz envolvente: la luz del local moja el canto de la figura. Es lo
    #    que separa un montaje creíble de una calcomanía, y era lo que faltaba.
    montaje = luz_envolvente(fondo, figura, radio=30, fuerza=0.6)

    final = montaje.convert("RGB").resize(SALIDA, Image.LANCZOS)
    final = revela(final, luces=222.0, negros=0.008, contraste=1.03, medios=103)
    final = nitidez(final, cantidad=0.28, radio=1.5)
    final.save(DESTINO, quality=96)
    print(f"✓ {DESTINO.relative_to(RAIZ)}  {final.size}")

    if a.revisar:
        ruta = RAIZ / "out/hilton-between-r10/togo1-portada.png"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        final.resize((700, 875), Image.LANCZOS).save(ruta)
        print(f"→ revisión: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

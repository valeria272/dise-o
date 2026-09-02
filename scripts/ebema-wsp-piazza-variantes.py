#!/usr/bin/env python3
"""
EBEMA CLICK — campañas WhatsApp ARIEL septiembre 2026 (A1–A6, línea Portezuelo).

Genera las variantes a partir de la pieza madre de Paulina Bustamante
(`ebema_wtsp_piazza.png`, 2500x4510, armada con la info de A1) parchando SOLO
las tres cosas que cambian entre campañas:

    1. el enunciado    FERRETEROS / CONTRATISTAS
    2. los 4 precios   (dígitos; el "$" y el "+IVA" no se tocan)
    3. la dirección    Santiago (2 líneas) / Concepción / Rancagua (1 línea)

Todo lo demás es el píxel original de la diseñadora.

GEOMETRÍA Y TIPOGRAFÍA: medidas sobre la madre, no supuestas.
  · Precios ......... Helvetica Bold 151 px, blanco. Dígitos tabulares, así que
                      el string nuevo ocupa exactamente el mismo avance.
                      Calce contra el original: IoU 0,86–0,90.
  · Enunciado ....... Raleway wght 600 (SemiBold), 65 px, tracking -0,45 px,
                      color #6D6F72, caja blanca de esquinas rectas con padding
                      lateral de 93 px, centrada en el eje x=1249.
                      Identificación glifo a glifo: IoU 0,917 sobre 286 fuentes.
  · Dirección ....... Raleway wght 450, 80 px, tracking +3,0 px, color #333333,
                      centrada en x=1249. Identificación: IoU 0,81, curva de peso
                      unimodal con pico plano en 440–460.
  · Una sola línea de dirección va CENTRADA entre los dos baselines de la madre
    (4272 y 4371 → 4322). Es la regla que el cliente ya aprobó en la v2 de
    agosto (ver memoria `ebema-click-campanas-ariel-solo-diseno`).

Uso:  python3 scripts/ebema-wsp-piazza-variantes.py
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENTREGA = RAIZ / "out/ebema/20260901_wsp_A1-A12_piazza"
MADRE = RAIZ / "public/assets/ebema/wsp-ariel/A1_portezuelo_sept2026.png"
DESTINO = ENTREGA / "piezas"
FONTS = RAIZ / "clients/ebema/sistema/fonts"

ROJO = (236, 28, 35)        # #EC1C23 — el único rojo de la marca
GRIS_ENUNCIADO = (109, 111, 114)   # #6D6F72
GRIS_DIRECCION = (51, 51, 51)      # #333333
EJE_X = 1249                # eje de composición de la pieza (2500 / 2)

# --- cajas de precio: (x0,y0,x1,y1) de la caja roja + (dx0,dx1) de los dígitos
PRECIOS = {
    "tina":      dict(caja=(213, 1152, 889, 1324),  digitos=(321, 769)),
    "ducha":     dict(caja=(1437, 1152, 2114, 1324), digitos=(1546, 1990)),
    "lavaplato": dict(caja=(258, 3338, 888, 3512),  digitos=(382, 751)),
    "lavatorio": dict(caja=(1437, 3338, 2067, 3512), digitos=(1558, 1927)),
}
PRECIO_SIZE = 151

CAJA_ENUNCIADO = dict(y0=797, y1=925, padding=93, baseline=889, size=65,
                      wght=600, track=-0.452)

DIRECCION = dict(size=80, wght=450, track=4.0,
                 baseline_l1=4272, baseline_l2=4371, baseline_unica=4322,
                 limpiar=(4190, 4400), umbral=150, dilatar=9, radio_inpaint=12)

# ---------------------------------------------------------------- campañas
PRODUCTOS = ["tina", "ducha", "lavaplato", "lavatorio"]

TARIFA = {   # verbatim del Sheet, bloque CAMPAÑAS ARIEL
    "ferretero":   {"tina": "12.224", "ducha": "10.077", "lavaplato": "7.628", "lavatorio": "6.257"},
    "contratista": {"tina": "12.830", "ducha": "10.651", "lavaplato": "8.052", "lavatorio": "6.583"},
}

DIRECCIONES = {   # verbatim del Sheet
    "santiago":   ["Ebema Santiago: Galvarino 8501, Quilicura",
                   "Av. General Velásquez 10985, San Bernardo."],
    "concepcion": ["Ebema Concepción: General Bonilla 2098."],
    "rancagua":   ["Ebema Rancagua: Diego de Almagro 1783."],
}

ENUNCIADO = {"ferretero":   "OFERTA EXCLUSIVA PARA FERRETEROS",
             "contratista": "OFERTA EXCLUSIVA PARA CONTRATISTAS"}

CAMPANAS = [
    ("A1", "ferretero",   "santiago"),    # = la madre
    ("A2", "contratista", "santiago"),
    ("A3", "ferretero",   "concepcion"),
    ("A4", "ferretero",   "rancagua"),
    ("A5", "contratista", "concepcion"),
    ("A6", "contratista", "rancagua"),
]


# ---------------------------------------------------------------- utilidades
def raleway(size, wght):
    f = ImageFont.truetype(str(FONTS / "Raleway-Variable.ttf"), size)
    f.set_variation_by_axes([wght])
    return f


def helvetica(size):
    return ImageFont.truetype(str(FONTS / "Helvetica-Bold.ttf"), size)


def ancho_con_track(txt, font, track):
    """Ancho de avance del string dibujado glifo a glifo con tracking."""
    return sum(font.getlength(c) for c in txt) + track * (len(txt) - 1)


def dibujar_track(draw, xy, txt, font, fill, track):
    """Dibuja glifo a glifo aplicando tracking. xy es el pen (izquierda, top)."""
    x, y = xy
    for ch in txt:
        draw.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + track


def tinta(arr, x0, x1, y0, y1, claro=True, thr=200):
    s = arr[y0:y1 + 1, x0:x1 + 1]
    if claro:
        return (s[..., 0] > thr) & (s[..., 1] > thr) & (s[..., 2] > thr)
    return (s[..., 0] < thr) & (s[..., 1] < thr) & (s[..., 2] < thr)


def buscar_pen(arr, txt, font, caja, digitos):
    """Encuentra el pen (x,y) con que la diseñadora dibujó estos dígitos:
    prueba offsets y se queda con el de mayor IoU contra la tinta original."""
    cx0, cy0, cx1, cy1 = caja
    dx0, dx1 = digitos
    orig = tinta(arr, dx0, dx1, cy0, cy1)
    orows = np.where(orig.sum(1) > 0)[0]
    ocols = np.where(orig.sum(0) > 0)[0]
    mejor = None
    for dy in range(-6, 7):
        for dx in range(-6, 7):
            img = Image.new("L", (dx1 - dx0 + 200, cy1 - cy0 + 200), 0)
            ImageDraw.Draw(img).text((80 + dx, 80 + dy), txt, font=font, fill=255)
            m = np.asarray(img) > 128
            r = np.where(m.sum(1) > 0)[0]
            c = np.where(m.sum(0) > 0)[0]
            if not len(r):
                continue
            crop = m[r[0]:r[-1] + 1, c[0]:c[-1] + 1]
            og = orig[orows[0]:orows[-1] + 1, ocols[0]:ocols[-1] + 1]
            H, W = max(crop.shape[0], og.shape[0]), max(crop.shape[1], og.shape[1])
            A = np.zeros((H, W), bool); B = np.zeros((H, W), bool)
            A[:crop.shape[0], :crop.shape[1]] = crop
            B[:og.shape[0], :og.shape[1]] = og
            iou = (A & B).sum() / (A | B).sum()
            penx = dx0 + int(ocols[0]) - (int(c[0]) - 80 - dx)
            peny = cy0 + int(orows[0]) - (int(r[0]) - 80 - dy)
            if mejor is None or iou > mejor[0]:
                mejor = (iou, penx, peny)
    return mejor


# ---------------------------------------------------------------- parches
def parchar_precios(im, arr, segmento, informe):
    d = ImageDraw.Draw(im)
    f = helvetica(PRECIO_SIZE)
    for prod in PRODUCTOS:
        g = PRECIOS[prod]
        cx0, cy0, cx1, cy1 = g["caja"]
        dx0, dx1 = g["digitos"]
        viejo = TARIFA["ferretero"][prod]      # la madre siempre trae el de ferretero
        nuevo = TARIFA[segmento][prod]
        iou, penx, peny = buscar_pen(arr, viejo, f, g["caja"], g["digitos"])
        if nuevo == viejo:
            informe.append(f"    {prod:10s} {viejo} = sin cambio (calce {iou:.3f})")
            continue
        # el string nuevo debe ocupar el mismo avance (dígitos tabulares)
        av_v = sum(f.getlength(c) for c in viejo)
        av_n = sum(f.getlength(c) for c in nuevo)
        assert abs(av_v - av_n) < 0.6, f"{prod}: el avance cambia {av_v}->{av_n}"
        # borrar sólo la mancha de dígitos, sin tocar el "$" ni el "+IVA"
        d.rectangle([dx0 - 10, cy0 + 2, dx1 + 3, cy1 - 2], fill=ROJO)
        d.text((penx, peny), nuevo, font=f, fill=(255, 255, 255))
        informe.append(f"    {prod:10s} ${viejo} -> ${nuevo}  (calce {iou:.3f}, pen {penx},{peny})")


def parchar_enunciado(im, segmento, informe):
    c = CAJA_ENUNCIADO
    txt = ENUNCIADO[segmento]
    f = raleway(c["size"], c["wght"])
    d = ImageDraw.Draw(im)
    ancho_txt = ancho_con_track(txt, f, c["track"])
    ancho_caja = ancho_txt + 2 * c["padding"]
    x0 = round(EJE_X - ancho_caja / 2)
    x1 = round(x0 + ancho_caja)
    # la caja es blanca y crece: basta pintarla encima, no hay fondo que reconstruir
    d.rectangle([x0, c["y0"], x1, c["y1"]], fill=(255, 255, 255))
    # baseline: el bottom de las mayúsculas de la madre
    asc = f.getbbox("O")[1]          # top de la mayúscula respecto del pen
    alto = f.getbbox("O")[3] - f.getbbox("O")[1]
    peny = c["baseline"] - alto - asc + 1
    penx = round(EJE_X - ancho_txt / 2)
    dibujar_track(d, (penx, peny), txt, f, GRIS_ENUNCIADO, c["track"])
    informe.append(f"    enunciado '{txt}'  caja x{x0}-{x1} ({ancho_caja:.0f} px)")


def limpiar_direccion(im):
    """Borra las líneas de dirección con inpainting sobre la máscara del texto.

    Se borra SÓLO la mancha de las letras (dilatada), no la banda entera: el
    mármol de alrededor queda intacto y Telea lo reconstruye con su textura.
    Aplanar la banda por interpolación dejaba un parche liso y rayado — probado
    y descartado el 01-09.
    """
    D = DIRECCION
    a = np.asarray(im).copy()
    y0, y1 = D["limpiar"]
    sub = a[y0:y1 + 1].copy()
    gris = cv2.cvtColor(sub, cv2.COLOR_RGB2GRAY)
    m = (gris < D["umbral"]).astype(np.uint8) * 255
    k = np.ones((D["dilatar"], D["dilatar"]), np.uint8)
    m = cv2.dilate(m, k, iterations=2)
    a[y0:y1 + 1] = cv2.inpaint(sub, m, D["radio_inpaint"], cv2.INPAINT_TELEA)
    return Image.fromarray(a)


def parchar_direccion(im, ciudad, informe):
    lineas = DIRECCIONES[ciudad]
    if ciudad == "santiago":
        informe.append("    dirección Santiago = la de la madre, no se redibuja")
        return im
    im = limpiar_direccion(im)
    d = ImageDraw.Draw(im)
    D = DIRECCION
    f = raleway(D["size"], D["wght"])
    bases = ([D["baseline_unica"]] if len(lineas) == 1
             else [D["baseline_l1"], D["baseline_l2"]])
    alto_may = f.getbbox("E")[3] - f.getbbox("E")[1]
    asc = f.getbbox("E")[1]
    for txt, base in zip(lineas, bases):
        w = ancho_con_track(txt, f, D["track"])
        penx = round(EJE_X - w / 2)
        peny = base - alto_may - asc + 1
        dibujar_track(d, (penx, peny), txt, f, GRIS_DIRECCION, D["track"])
        informe.append(f"    dirección '{txt}'  ancho {w:.0f} px, baseline {base}")
    return im


# ---------------------------------------------------------------- main
def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    madre = Image.open(MADRE).convert("RGB")
    arr = np.asarray(madre).astype(int)
    print(f"madre: {MADRE.name}  {madre.size}\n")
    for cid, segmento, ciudad in CAMPANAS:
        informe = []
        im = madre.copy()
        if cid == "A1":
            informe.append("    = la pieza madre, se copia sin tocar")
        else:
            parchar_precios(im, arr, segmento, informe)
            if segmento == "contratista":
                parchar_enunciado(im, segmento, informe)
            else:
                informe.append("    enunciado FERRETEROS = el de la madre, no se redibuja")
            im = parchar_direccion(im, ciudad, informe)
        nombre = f"ebema_wsp_{cid}_portezuelo_{segmento}_{ciudad}.png"
        im.save(DESTINO / nombre)
        print(f"{cid}  {segmento:11s} {ciudad}")
        for l in informe:
            print(l)
        print(f"    -> piezas/{nombre}\n")


if __name__ == "__main__":
    main()

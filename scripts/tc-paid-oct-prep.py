"""
TIERRA CALMA · PAID OCTUBRE 2026 — prepara los fondos de 02-A y 02-B.

Brief: «Brief Diseño Tierra Calma - Octubre 2026.xlsx» (Ignacio Retamal,
PERFORMANCE/Octubre 2026, 1PguPpqzNIkxWKOv4BInI8ep7_R-EI57l).

Sale todo de FOTOS REALES del rodaje del 07-08 (raw/tierracalma/fotos-reales/dron):

  · 02-A «Tu casa cabe» → DJI_..._0335 (cenital casi a 90° del lote de la
    caseta verde, el mismo de la pieza «5.000 m²» de septiembre).
  · 02-B «Mapa 30 min»  → DJI_..._0324 (oblicuo: parcelas verdes con casas y
    caminos en primer plano, los cerros atrás). ⛔ Se probó 0331 (el mismo lote
    de 02-A con el llano al fondo) y se descartó: el llano está ANEGADO, con
    manchas blancas de agua — en un aviso inmobiliario se lee «se inunda».

Lo que hace:
  1. Recorta a la medida exacta del lienzo (1080×1080 y 1080×1350), de modo
     que la fila del JPG ES la fila del lienzo (manual § 4 sexies).
  2. Corrección cálida y suave. El rodaje fue una mañana nublada de invierno:
     se le saca el gris, NO se finge un atardecer.
  3. Proyecta el deslinde medido sobre la foto y calcula la casa de 150 m²
     A ESCALA REAL: su área es 150/5.000 = 3 % del área del deslinde.
     Escribe todo en paid-oct.json para que el TSX no estime nada.

Uso:  ~/copylab-venv/Scripts/python.exe scripts/tc-paid-oct-prep.py
"""
import json
import math
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
DRON = RAIZ / "raw/tierracalma/fotos-reales/dron"
SALIDA = RAIZ / "public/assets/tierracalma/paid-oct"
SALIDA.mkdir(parents=True, exist_ok=True)

CENITAL = DRON / "DJI_20260807094454_0335_D.JPG"  # 4032×3024
OBLICUO = DRON / "DJI_20260807093929_0324_D.JPG"

# Deslinde medido sobre 0335 (px de la foto original), verificado dibujándolo
# encima: calza con el cerco izquierdo, la línea del seto, el cerco a la derecha
# del camino de ripio y el borde del camino público.
LOTE = [(1134, 1044), (2700, 900), (3009, 2226), (1275, 2454)]


def calido(im: Image.Image, fuerza: float = 1.0) -> Image.Image:
    """Saca el gris de la mañana nublada: +contraste, +saturación, balance tibio."""
    im = im.convert("RGB")
    im = ImageEnhance.Contrast(im).enhance(1.0 + 0.10 * fuerza)
    im = ImageEnhance.Color(im).enhance(1.0 + 0.06 * fuerza)
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * (1 + 0.05 * fuerza) + 3 * fuerza)))
    b = b.point(lambda v: int(v * (1 - 0.07 * fuerza)))
    return Image.merge("RGB", (r, g, b))


def recorte(src: Image.Image, cx: float, cy: float, escala: float, w: int, h: int):
    """Recorte de (w/escala × h/escala) px de la foto, centrado en (cx, cy) y
    empujado para no salirse. Devuelve la imagen a w×h y la función que lleva
    un punto de la foto al lienzo."""
    cw, ch = w / escala, h / escala
    x0 = min(max(cx - cw / 2, 0), src.width - cw)
    y0 = min(max(cy - ch / 2, 0), src.height - ch)
    im = src.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((w, h), Image.LANCZOS)
    return im, (lambda p: (round((p[0] - x0) * escala, 1), round((p[1] - y0) * escala, 1)))


def area(poly):
    return abs(sum(poly[i][0] * poly[i - 1][1] - poly[i - 1][0] * poly[i][1] for i in range(len(poly)))) / 2


def casa(lote, u0: float, v0: float):
    """Planta en L de 150 m² dentro del lote, alineada con sus bordes.

    La L es un rectángulo de 15×8 m más un ala de 6×5 m = 150 m². Se escala con
    la raíz de (área del lote / 5.000 m²), o sea: el lote se toma como la
    parcela de 5.000 m² y la casa ocupa exactamente el 3 % de su superficie.
    (u0, v0) es la esquina de la L en coordenadas relativas del lote (0-1).
    """
    tl, tr, br, bl = lote
    px_por_m = math.sqrt(area(lote) / 5000)
    # ejes del lote: a lo largo del borde superior y del izquierdo
    ex = ((tr[0] - tl[0]), (tr[1] - tl[1]))
    ey = ((bl[0] - tl[0]), (bl[1] - tl[1]))
    lx, ly = math.hypot(*ex), math.hypot(*ey)
    ux, uy = (ex[0] / lx, ex[1] / lx), (ey[0] / ly, ey[1] / ly)
    o = (tl[0] + ex[0] * u0 + ey[0] * v0, tl[1] + ex[1] * u0 + ey[1] * v0)
    forma_m = [(0, 0), (15, 0), (15, 8), (6, 8), (6, 13), (0, 13)]  # 120 + 30 = 150 m²
    pts = [
        (round(o[0] + (a * ux[0] + b * uy[0]) * px_por_m, 1), round(o[1] + (a * ux[1] + b * uy[1]) * px_por_m, 1))
        for a, b in forma_m
    ]
    return pts, round(px_por_m, 3)


datos = {"fuente": {"02A": CENITAL.name, "02B": OBLICUO.name}}

# ---------------------------------------------------------------- 02-A cenital
cen = Image.open(CENITAL)
cen = calido(cen)
cx = sum(p[0] for p in LOTE) / 4
# El recorte se pega al borde INFERIOR de la foto: es lo que sube el lote en el
# lienzo y deja libre la esquina de abajo a la izquierda para el titular (la
# misma disposición de la pieza «5.000 m²» de septiembre). La escala mínima la
# fija el alto de la foto: 1080/3024 y 1350/3024.
# El desplazamiento en x deja el lote a ~70 px de los filetes verticales (x 65 y 1016).
for nombre, w, h, escala, dx in (("1x1", 1080, 1080, 0.40, 120), ("4x5", 1080, 1350, 0.45, 42)):
    im, a_lienzo = recorte(cen, cx + dx, cen.height, escala, w, h)
    im.save(SALIDA / f"a-cenital-{nombre}.jpg", quality=92)
    lote = [a_lienzo(p) for p in LOTE]
    planta, ppm = casa(lote, 0.12, 0.13)
    datos[f"02A_{nombre}"] = {
        "lote": lote,
        "casa": planta,
        "px_por_m": ppm,
        "control_area_casa_m2": round(area(planta) / ppm**2, 1),
        "control_pct": round(100 * area(planta) / area(lote), 2),
    }

# ---------------------------------------------------------------- 02-B oblicuo
obl = Image.open(OBLICUO)
# Mañana con neblina: autocontraste suave (corta el 0,6 % de cada punta) antes
# del balance tibio, para que los cerros no queden como una mancha gris.
obl = calido(ImageOps.autocontrast(obl.convert("RGB"), cutoff=0.6), 1.1)
for nombre, w, h in (("1x1", 1080, 1080), ("4x5", 1080, 1350)):
    escala = h / obl.height  # todo el alto: cielo arriba, el lote abajo
    im, _ = recorte(obl, obl.width * 0.5, obl.height / 2, escala, w, h)
    im.save(SALIDA / f"b-oblicuo-{nombre}.jpg", quality=92)

# ------------------------------------------------------- marco 1:1 (derivado)
# El diseñador no entregó marco cuadrado. NO se redibuja (manual § 4 quinquies):
# se le quitan 270 filas del medio al MARCO-POST. Entre las filas 400 y 1100 cada
# fila es idéntica —sólo los filetes verticales en x 65-66 y 1016, verificado
# leyendo el alfa—, así que el corte no deja ninguna costura. Todo lo de abajo
# sube 270: regla inferior 966, píldora y 942–994.
marco = Image.open(RAIZ / "public/assets/tierracalma/marcos/MARCO-POST.png")
cuadrado = Image.new("RGBA", (1080, 1080))
cuadrado.paste(marco.crop((0, 0, 1080, 600)), (0, 0))
cuadrado.paste(marco.crop((0, 870, 1080, 1350)), (0, 600))
cuadrado.save(SALIDA / "MARCO-POST-1x1.png")

(SALIDA / "paid-oct.json").write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(datos, indent=2, ensure_ascii=False))

# ------------------------------------------------ D1 (reemplazo de B4, 23-09)
# B4 «La primavera» no tiene foto: el rodaje es de invierno. El brief manda
# reemplazarla por D1, que es «un cambio de tipografía sobre el archivo
# existente»: la pieza «alcance» de septiembre (el asado). No hay foto limpia en
# el repo ni en Drive, así que se parte del PNG entregado y se BORRAN sólo las
# líneas 1 y 2 del titular (filas 275–329 y 354–395, medidas: iguales en 9:16 y
# 4:5). La línea 3 —«TIERRA CALMA.» en serif— es la misma en D1 y no se toca.
# Se borran los píxeles blancos de esas dos líneas, dilatados 4 px, con
# inpainting de Telea; el texto nuevo va encima y tapa el resto.
import cv2  # noqa: E402
import numpy as np  # noqa: E402

REF = RAIZ / "raw/tierracalma/paid-oct2026/ref-sep"
for nombre in ("9x16", "4x5"):
    src = cv2.imread(str(REF / f"alcance-{nombre}.png"))
    src = src[:, :1080]  # la pieza de sept mide 1081 de ancho
    banda = np.zeros(src.shape[:2], np.uint8)
    banda[268:402, 300:790] = 255  # 268: la tilde de la «Ó» sube hasta la fila 275
    blanco = (src.min(axis=2) > 170).astype(np.uint8) * 255
    mascara = cv2.dilate(cv2.bitwise_and(blanco, banda), np.ones((9, 9), np.uint8))
    limpio = cv2.inpaint(src, mascara, 9, cv2.INPAINT_TELEA)
    cv2.imwrite(str(SALIDA / f"d1-{nombre}.png"), limpio)

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
# RONDA 2 (23-09, Diego): «que se vea distinto, más limpio el terreno, quizás una
# vista dron más arriba». La v1 usaba DJI_0335, la misma toma de la pieza
# «5.000 m²» de septiembre. Ninguna foto real del rodaje es más alta ni más
# limpia, y el manual (§ 4 bis, Valeria 19-08) dice que el dron es para video y
# los estáticos van con IA. Así que el fondo es DJI_0281 —la cenital más alta y
# limpia del rodaje— IDEALIZADA con Nano Banana Pro usándola como referencia:
# conserva la traza real (caminos, cercos, senderos, la casa con piscina) vista a
# 90° y le pone pasto verde, nativos y luz de golden hour. Prompt y variantes en
# raw/tierracalma/paid-oct2026/ia/.
# RONDA 3 (23-09, Diego): «para la generación de imágenes utiliza seedream 5
# pro». Se rehízo con Seedream 5 Pro edit y la misma referencia (sd5-cenital-1):
# es la que más respeta la traza real — deja grises los caminos pavimentados.
#
# El deslinde sigue los cercos que se ven EN la imagen: el superior, el
# izquierdo, el inferior y el borde del sendero a la derecha. La casa sigue
# siendo el 3 % del área del deslinde.
# RONDA 5 (24-09, comentario de Diego en Drive sobre casacabe_4x5): «imagen de
# fondo más realista». Se deja la idealización fuerte (sd5-cenital-1) y se usa
# la foto real DJI_0281 recortada en vertical (x 1500–4467, alto completo) con
# Seedream 5 Pro edit de CAMBIO MÍNIMO: sin bruma, luz de tarde, sin los autos
# (sd5-real-0281-1). Queda menos verde, porque ése es el terreno real.
CENITAL_IA = RAIZ / "raw/tierracalma/paid-oct2026/ia/sd5-real-0281-1.png"  # 1770×2360
# Lote: cerco del medio arriba, cerco inferior junto al camino, borde del
# sendero a la derecha. El lado izquierdo no tiene cerco visible: va en x 300
# para quedar lejos del filete del marco (Diego: nada «tan al borde»).
LOTE_IA = [(300, 1286), (1378, 1258), (1182, 1972), (300, 1994)]
cen = Image.open(CENITAL_IA).convert("RGB")
escala = 1080 / cen.width
# El lote está en la mitad baja de la imagen: el titular sube bajo el logo y el
# lote queda abajo (1:1: filas 408–857; 4:5: 678–1127), sin cruzar el texto.
for nombre, w, h, y0 in (("1x1", 1080, 1080, 590), ("4x5", 1080, 1350, 147)):
    ch = h / escala
    im, a_lienzo = recorte(cen, cen.width / 2, y0 + ch / 2, escala, w, h)
    im.save(SALIDA / f"a-cenital-{nombre}.jpg", quality=92)
    lote = [a_lienzo(p) for p in LOTE_IA]
    planta, ppm = casa(lote, 0.14, 0.16)
    datos[f"02A_{nombre}"] = {
        "lote": lote,
        "casa": planta,
        "px_por_m": ppm,
        "control_area_casa_m2": round(area(planta) / ppm**2, 1),
        "control_pct": round(100 * area(planta) / area(lote), 2),
    }

# ---------------------------------------------------------------- 02-B oblicuo
# RONDA 5 (24-09, Diego): «la imagen se ve demasiado falsa, básate en las reales,
# sólo toma la idea de la parcela, no de Santiago de fondo». Se descarta la
# ronda 4 (sd5-mapa-1: llano de cultivos con skyline inventado). Ahora es la
# foto real DJI_0324 pasada por Seedream 5 Pro edit con un prompt de CAMBIO
# MÍNIMO: mismo encuadre, mismo terreno, mismas casas; sólo sin neblina, luz de
# tarde y el pasto un poco más fresco (sd5-real-0324-2). Nada agregado.
OBLICUO_IA = RAIZ / "raw/tierracalma/paid-oct2026/ia/sd5-real-0324-2.png"
obl = Image.open(OBLICUO_IA).convert("RGB")
esc_b = 1080 / obl.width
for nombre, h in (("1x1", 1080), ("4x5", 1350)):
    ch = h / esc_b
    im, _ = recorte(obl, obl.width / 2, obl.height / 2, esc_b, 1080, h)
    im.save(SALIDA / f"b-oblicuo-{nombre}.jpg", quality=92)
datos["fuente"]["02B"] = OBLICUO_IA.name

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
# RONDA 2 (23-09, Diego): «la del fin de semana, generar una imagen nueva». La v1
# recomponía el titular sobre la pieza del asado de septiembre; ahora el fondo
# es una generación nueva de Mystic (finde-1: gente de lejos y de espaldas, casa
# de madera, el tercio de arriba despejado para el titular). Se recorta a 9:16 y
# a 4:5 desde la MISMA imagen para que la pieza sea una sola.
# Ronda 3: Seedream 5 Pro, texto a imagen. sd5-finde-1/2 tenían la familia
# grande y abajo: la píldora del 9:16 le caía encima y el titular del 4:5
# pisaba el techo. sd5-finde-3 se pidió con la composición escrita en el prompt
# (40 % de cielo arriba, escena en la franja central, 25 % de pasto abajo).
FINDE = RAIZ / "raw/tierracalma/paid-oct2026/ia/sd5-finde-3.png"  # 1520×2736
fin_ = Image.open(FINDE).convert("RGB")
esc = 1080 / fin_.width
for nombre, h, y0 in (("9x16", 1920, 17), ("4x5", 1350, 400)):
    ch = h / esc
    im, _ = recorte(fin_, fin_.width / 2, y0 + ch / 2, esc, 1080, h)
    im.save(SALIDA / f"d1-{nombre}.jpg", quality=92)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma láminas EN LA PLANTILLA DE ELI, para pegarlas en «MoodBoard Hotel sesión».

    python scripts/dt-moodboard-laminas-eli.py

⭐ POR QUÉ EXISTE. El 09-09-2026 Eli rearmó el moodboard con su propia dirección de
arte (44 láminas, portada COPYWRITERS 2026) y su nomenclatura: **«REFERENTES» en
bold + el espacio en regular**, y los locales rotulados CON su marca —«CAFETERÍA BW»,
«RESTAURANT QB», «TERRAZA DE QB»—. Su rótulo manda: lo que ella pidió antes de
tratarlos «no como marca» era sobre el TRATAMIENTO de la foto, no sobre el título.

Este script NO toca su archivo. Genera un .pptx aparte con las láminas que faltan,
calcadas a su plantilla, para que ella copie y pegue la diapositiva.

⚠️ GEOMETRÍA MEDIDA sobre su diapositiva 38 (no estimada):

    lámina            10 × 5,625 in
    título            x 0,41  y 0,28   9,19 × 0,54   Helvetica Neue 35 pt
                      «REFERENTES» bold + espacio regular
    línea             x 0,41  y 0,94   largo 9,19
    fotos             y 1,18   alto FIJO 3,90   gap 0,10
                      ancho por proporción, justificado a 9,30 de ancho útil
                      (2,60 + 2,60 + 3,90 + 2 gaps = 9,30 ✓)
"""
import io
import json
import os

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Emu, Inches, Pt

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = os.path.join(RAIZ, "raw", "hilton", "dt", "moodboard-pin")
CACHE = os.path.join(RAIZ, "out", "hilton", "dt", "_cache-eli")

# Medidas de la plantilla de Eli, en pulgadas.
T_X, T_Y, T_W, T_H = 0.41, 0.28, 9.19, 0.54
LINEA_Y = 0.94
F_Y, F_H, F_GAP = 1.18, 3.90, 0.10
F_X0, F_ANCHO = 0.35, 9.30
TIPO = "Helvetica Neue"
PT = 35


def _liviana(ruta, lado=1400, calidad=80):
    import hashlib
    os.makedirs(CACHE, exist_ok=True)
    clave = hashlib.md5(os.path.abspath(ruta).encode("utf-8")).hexdigest()[:16]
    destino = os.path.join(CACHE, clave + ".jpg")
    if os.path.exists(destino) and os.path.getmtime(destino) >= os.path.getmtime(ruta):
        return destino
    with Image.open(ruta) as im:
        im = im.convert("RGB")
        if max(im.size) > lado:
            im.thumbnail((lado, lado), Image.LANCZOS)
        im.save(destino, "JPEG", quality=calidad, optimize=True)
    return destino


def lamina(prs, espacio, fotos):
    """Una lámina calcada a la plantilla de Eli."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    tb = s.shapes.add_textbox(Inches(T_X), Inches(T_Y), Inches(T_W), Inches(T_H))
    p = tb.text_frame.paragraphs[0]
    r1 = p.add_run()
    r1.text = "REFERENTES "
    r1.font.bold = True
    r2 = p.add_run()
    r2.text = espacio
    r2.font.bold = False
    for r in (r1, r2):
        r.font.size = Pt(PT)
        r.font.name = TIPO
        r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    ln = s.shapes.add_connector(1, Inches(T_X), Inches(LINEA_Y),
                                Inches(T_X + T_W), Inches(LINEA_Y))
    ln.line.color.rgb = RGBColor(0x00, 0x00, 0x00)
    ln.line.width = Pt(0.75)

    # Fila justificada: altura fija, anchos por proporción. Nada se deforma.
    props = []
    for f in fotos:
        with Image.open(f) as im:
            props.append(im.size[0] / float(im.size[1]))
    libre = F_ANCHO - F_GAP * (len(fotos) - 1)
    escala = min(1.0, libre / (F_H * sum(props)))   # si se pasa de ancho, se achica
    h = F_H * escala
    x = F_X0
    for f, pr in zip(fotos, props):
        w = h * pr
        s.shapes.add_picture(_liviana(f), Inches(x), Inches(F_Y + (F_H - h) / 2),
                             width=Inches(w), height=Inches(h))
        x += w + F_GAP
    return s


def p(esp, *nums):
    return [os.path.join(PIN, esp, "%s-%s.jpg" % (esp, n)) for n in nums]


# Lo que NO está en el moodboard de Eli y ella sí pidió durante la sesión.
LAMINAS = [
    # ⛔ Pidió: «referencias de los salones, no los que ya existen sino de MESAS
    # REDONDAS, para hacer post y historias». En sus 6 de SALONES no hay ninguna.
    ("MESAS REDONDAS", p("15-salones-redondas", "03", "05", "13")),
    ("MESAS REDONDAS", p("15-salones-redondas", "11", "10", "09")),
    ("MESAS REDONDAS", p("15-salones-redondas", "08", "12", "02")),
    # ⛔ Pidió: «estilo corporativo de ENTRADA al salón».
    ("ENTRADA SALÓN", p("17-salon-entrada", "01", "02", "05")),
    ("SEÑALÉTICA SALÓN", p("17-salon-entrada", "07", "08", "09")),
    # ⛔ El hotel tiene Wellness Lounge / SPA by Scape y no aparece en el moodboard.
    ("WELLNESS SPA", p("09-wellness-spa", "01", "03", "04")),
    ("WELLNESS SPA", p("09-wellness-spa", "07", "08", "10")),
]


def main():
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(10), Inches(5.625)
    n = 0
    for espacio, fotos in LAMINAS:
        fotos = [f for f in fotos if os.path.exists(f)]
        if not fotos:
            print("  [!] sin fotos:", espacio)
            continue
        lamina(prs, espacio, fotos)
        n += 1
        print("  REFERENTES %-20s %d fotos" % (espacio, len(fotos)))
    out = os.path.join(RAIZ, "out", "hilton", "dt", "MoodBoard-DT-faltantes.pptx")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    prs.save(out)
    print("\n%d laminas -> %s (%.1f MB)" % (n, out, os.path.getsize(out) / 1e6))


if __name__ == "__main__":
    main()

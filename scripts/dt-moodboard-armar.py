#!/usr/bin/env python3
"""Arma el PPTX de laminas del MoodBoard de la sesion de DoubleTree.

    python scripts/dt-moodboard-armar.py [--seleccion sel.json] [--refs DIR] [--out ruta.pptx]

Lee raw/hilton/dt/moodboard-refs/<espacio>/ y arma UNA lamina 16:9 por espacio:
titular del espacio + la regla de rostros que aplica + una retícula de fotos.

⚠️ El formato calza con 'MoodBoard Hotel sesion' de Eli: 10 x 5.625 pulgadas
(720 x 405 pt), que es lo que declara el PDF exportado de su presentacion.
Asi la lamina se copia y se pega en su archivo sin reescalar.

Drive convierte el .pptx a Slides al subirlo, y en Slides se copian diapositivas
entre presentaciones conservando las imagenes.
"""
import hashlib
import io
import json
import os
import sys

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Emu, Inches, Pt

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(RAIZ, "raw", "hilton", "dt", "moodboard-pin")

# Paleta DT: el azul del manual y la tinta. Fondo claro para que la foto mande.
AZUL = RGBColor(0x09, 0x19, 0x4E)
GRIS = RGBColor(0x6B, 0x70, 0x7B)
FONDO = RGBColor(0xF4, 0xF5, 0xF7)

# La regla de rostros por espacio, dictada por Eli el 09-09-2026.
# En imagen los rostros de trabajadores NO van, salvo recepcion y barra.
REGLA = {
    "01-entrada":      "Sin personas. Si aparece un huésped, de espaldas o desenfocado",
    "02-recepcion":    "Recepcionista SÍ puede aparecer. El huésped, de espaldas o del torso hacia abajo",
    "03-lobby":        "Sin personas. Se permite silueta desenfocada de paso",
    "04-habitaciones": "Sin personas, nunca. La habitación vacía y montada",
    "05-cowork":       "Sin rostros. Manos sobre el teclado o torso hacia abajo. PRIMER Y SEGUNDO PISO",
    "06-cafeteria":    "Barista SÍ puede aparecer. Manos preparando; el cliente sin rostro",
    "07-restaurant":   "Sin rostros. Manos sirviendo o montaje de mesa sin comensales",
    "08-gimnasio":     "Sin personas. Equipos y sala vacía",
    "09-wellness-spa": "Sin rostros. Manos, detalle y sala vacía",
    "10-salones":      "Sin personas. Salón montado, vacío",
}

TITULO = {
    "01-entrada":      "ENTRADA / ACCESO",
    "02-recepcion":    "RECEPCIÓN",
    "03-lobby":        "LOBBY",
    "04-habitaciones": "HABITACIONES",
    "05-cowork":       "COWORK  ·  1er y 2do piso",
    "06-cafeteria":    "CAFETERÍA",
    "07-restaurant":   "RESTAURANT / DESAYUNO",
    "08-gimnasio":     "GIMNASIO",
    "09-wellness-spa": "WELLNESS LOUNGE / SPA",
    "10-salones":      "SALONES DE EVENTOS",
}



# ⚠️ Las fotos de la sesión real del hotel son de 1920x1280 y ~1,6 MB cada una.
# Insertadas tal cual dejaban el deck en 31 MB, y con eso Drive ya NO lo exporta
# ("This file is too large to be exported") y Slides tarda en abrirlo. Para un
# moodboard de referencia no se gana nada: se recomprimen a 1600 px de lado mayor
# y JPEG 82, que en una lámina de 10 pulgadas no se distingue.
CACHE = os.path.join(RAIZ, "out", "hilton", "dt", "_cache-laminas")


def _liviana(ruta, lado=1200, calidad=76):
    """Devuelve una copia recomprimida; si ya existe y está fresca, la reusa."""
    os.makedirs(CACHE, exist_ok=True)
    clave = hashlib.md5(os.path.abspath(ruta).encode("utf-8")).hexdigest()[:16]
    destino = os.path.join(CACHE, clave + ".jpg")
    if os.path.exists(destino) and os.path.getmtime(destino) >= os.path.getmtime(ruta):
        return destino
    try:
        with Image.open(ruta) as im:
            im = im.convert("RGB")
            if max(im.size) > lado:
                im.thumbnail((lado, lado), Image.LANCZOS)
            im.save(destino, "JPEG", quality=calidad, optimize=True, progressive=True)
        return destino
    except Exception:
        return ruta


def _caja(prs, x, y, w, h, texto, tam, color, bold=False):
    tb = prs.slides[-1].shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = texto
    r.font.size = Pt(tam)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.name = "Trebuchet MS"
    return tb


def lamina(prs, espacio, archivos, titulo=None, regla=None):
    """Una lamina por espacio: titular, regla, y el mosaico de fotos.

    ⭐ EL MOSAICO VA POR FILAS JUSTIFICADAS, y la fila se cierra cuando la suma de
    proporciones alcanza la que llena el ancho a la altura objetivo. Recien ahi se
    resuelve la altura exacta con h = ancho_libre / suma_de_proporciones, asi que
    cada fila termina midiendo el ancho util COMPLETO y ninguna foto se deforma
    ni se recorta (la regla del estudio: una foto no se estira para llenar nada).

    ⚠️ Por que no una grilla 3x2: en un area de 9,3 x 4,35 pulgadas las celdas de
    una 3x2 quedan de proporcion 1,43 --apaisadas--, y estas fotos de hoteleria son
    verticales 2:3. Encajarlas dejaba dos bandas vacias enormes a los lados, y
    recortarlas a 1,43 se come la doble altura, que es justo lo que hay que mostrar.
    Con este algoritmo seis verticales entran en UNA fila que si llena el ancho, y
    cuando las fotos son apaisadas salen dos filas solas.
    """
    s = prs.slides.add_slide(prs.slide_layouts[6])  # en blanco
    fondo = s.background.fill
    fondo.solid()
    fondo.fore_color.rgb = FONDO

    _caja(prs, Inches(0.35), Inches(0.18), Inches(9.3), Inches(0.4),
          titulo or TITULO.get(espacio, espacio.upper()), 19, AZUL, bold=True)
    _caja(prs, Inches(0.35), Inches(0.56), Inches(9.3), Inches(0.3),
          regla if regla is not None else REGLA.get(espacio, ""), 10, GRIS)

    top0, left0 = Inches(0.95), Inches(0.35)
    ancho_util, alto_util = Inches(9.3), Inches(4.35)
    gap = Inches(0.10)

    fotos = []
    for ruta in archivos:
        try:
            with Image.open(ruta) as im:
                iw, ih = im.size
            fotos.append((ruta, iw / float(ih)))
        except Exception:
            continue
    if not fotos:
        return s

    # A dos filas: la suma de proporciones que llena el ancho a esa altura.
    alto_obj = (alto_util - gap) / 2.0
    objetivo = (ancho_util - gap) / alto_obj

    filas, fila, suma = [], [], 0.0
    for f in fotos:
        fila.append(f)
        suma += f[1]
        if suma >= objetivo:
            filas.append(fila)
            fila, suma = [], 0.0
    if fila:
        filas.append(fila)

    # Altura real de cada fila: la que justifica el ancho, con techo.
    medidas = []
    for fl in filas:
        libre = ancho_util - gap * (len(fl) - 1)
        h = min(libre / sum(r for _, r in fl), alto_util)
        medidas.append(h)

    # Si no cabe todo a lo alto, se reparte proporcionalmente.
    total = sum(medidas) + gap * (len(medidas) - 1)
    if total > alto_util:
        k = (alto_util - gap * (len(medidas) - 1)) / sum(medidas)
        medidas = [h * k for h in medidas]
        total = alto_util

    y = top0 + (alto_util - total) / 2.0     # el bloque queda centrado a lo alto
    for fl, h in zip(filas, medidas):
        anchos = [h * r for _, r in fl]
        x = left0 + (ancho_util - (sum(anchos) + gap * (len(fl) - 1))) / 2.0
        for (ruta, _), w in zip(fl, anchos):
            s.shapes.add_picture(_liviana(ruta), Emu(int(x)), Emu(int(y)),
                                 width=Emu(int(w)), height=Emu(int(h)))
            x += w + gap
        y += h + gap
    return s


def main():
    """Arma el deck desde un JSON de LAMINAS explicitas.

    Formato:  [{"titulo": "...", "regla": "...", "fotos": ["ruta", ...]}, ...]

    ⚠️ Antes esto iba por carpeta (una lámina por espacio). Se cambió cuando el
    deck empezó a mezclar REFERENCIAS de Pinterest con FOTOS REALES de la sesión
    del hotel en una misma lámina, y a separar POST (horizontal) de HISTORIA
    (vertical): la carpeta ya no describe la lámina.
    """
    a = sys.argv[1:]
    laminas_path = a[a.index("--laminas") + 1] if "--laminas" in a else None
    out = a[a.index("--out") + 1] if "--out" in a else os.path.join(
        RAIZ, "out", "hilton", "dt", "MoodBoard-DT-espacios.pptx")
    if not laminas_path:
        sys.exit("uso: --laminas <json> [--out <pptx>]")

    laminas = json.load(io.open(laminas_path, encoding="utf-8"))

    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(10), Inches(5.625)

    s0 = prs.slides.add_slide(prs.slide_layouts[6])
    s0.background.fill.solid()
    s0.background.fill.fore_color.rgb = AZUL
    _caja(prs, Inches(0.6), Inches(2.1), Inches(8.8), Inches(0.8),
          "MOODBOARD  ·  SESIÓN DE FOTOS", 30, RGBColor(0xFF, 0xFF, 0xFF), bold=True)
    _caja(prs, Inches(0.6), Inches(2.95), Inches(8.8), Inches(1.1),
          "DoubleTree by Hilton Santiago-Vitacura   ·   referencias por espacio\n"
          "Material de referencia únicamente: define encuadre, luz, formato y presencia "
          "humana. Las fotos finales salen de la sesión propia.",
          11, RGBColor(0xC9, 0xCE, 0xD8))

    n = 0
    for L in laminas:
        fotos = [f for f in L["fotos"] if os.path.exists(f)]
        faltan = [f for f in L["fotos"] if not os.path.exists(f)]
        if faltan:
            print("   [!] no existe:", faltan)
        if not fotos:
            print("   [!] lamina sin fotos:", L["titulo"]); continue
        lamina(prs, "", fotos, titulo=L["titulo"], regla=L.get("regla", ""))
        n += 1
        print("  %-54s %d fotos" % (L["titulo"][:54], len(fotos)))

    os.makedirs(os.path.dirname(out), exist_ok=True)
    prs.save(out)
    print("\n%d laminas + portada -> %s (%.1f MB)" % (n, out, os.path.getsize(out) / 1e6))


if __name__ == "__main__":
    main()

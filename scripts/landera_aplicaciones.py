#!/usr/bin/env python3
"""
Landera — página de aplicaciones sobre fondo blanco.

El cliente pidió «ver el juego de colores sobre una slide o documento de fondo
blanco». El manual no tiene esa página: hay que componerla.

Cómo está hecha, y por qué así:

· El logotipo NO se redibuja. Se recorta del propio PDF original con show_pdf_page,
  así que la marca que aparece en los ejemplos es la vectorial real, no una copia.
· La tipografía es la de la marca: los TTF completos de Aptos que trae Microsoft
  Office. Los subsets embebidos en el PDF NO sirven — Illustrator los guarda con
  codificación propia y al componer salen palabras con huecos ("Inversión" →
  "nversi n"), aunque has_glyph diga que el glifo está.
· Los ejemplos van sobre blanco puro, igual que las láminas de contenido: en este
  manual sólo las tapas son crema.
· Las franjas del borde llevan extremo redondeado, porque es lo que el propio
  manual exige en la pág. 5 («SIEMPRE USAR TERMINACIONES REDONDEADAS»).

Uso:
    python3 scripts/landera_aplicaciones.py
"""

import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Falta PyMuPDF. Instálalo con: python3 -m pip install pymupdf")

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw" / "landera" / "PROPUESTA-BASE-V2.pdf"
SALIDA = RAIZ / "out" / "landera"

# Geometría medida sobre el original (pág. 2)
LOGO_PRINCIPAL = fitz.Rect(68.14, 232.18, 303.47, 287.03)

# Cabecera, medida sobre las páginas 3 y 5
CAB_X = 60.19
CAB_TITULO_SIZE = 18.0
CAB_BAJADA_SIZE = 14.0
ETIQUETA_SIZE = 12.88

TERRACOTA = "E4361F"
GRIS_PIEDRA = "666461"
CREMA = "FAF1E8"
BLANCO = "FFFFFF"


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def mezclar(hex_a, hex_b, t):
    """Interpola dos colores; se usa para los tonos suaves de la tabla."""
    a, b = rgb(hex_a), rgb(hex_b)
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


# Aptos viene con Microsoft Office. Las fuentes embebidas en el PDF NO sirven para
# escribir texto nuevo: Illustrator las embebe como subsets con codificación propia,
# así que `has_glyph` da un falso positivo y al componer salen palabras con huecos
# ("Inversión" → "nversi n"). Se usan los TTF completos del bundle de Word.
DFONTS = Path("/Applications/Microsoft Word.app/Contents/Resources/DFonts")

PRUEBA_GLIFOS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                 "0123456789 .,:%·áéíóúÁÉÍÓÚñ–")


def localizar_fuentes():
    """Devuelve las rutas de Aptos y confirma que cubren los glifos que usamos."""
    pedidas = {"Aptos": "Aptos.ttf",
               "Aptos-Bold": "Aptos-Bold.ttf",
               "Aptos-SemiBold": "Aptos-SemiBold.ttf",
               "Aptos-Light": "Aptos-Light.ttf"}
    encontradas = {}
    for clave, archivo in pedidas.items():
        ruta = DFONTS / archivo
        if not ruta.exists():
            continue
        fo = fitz.Font(fontfile=str(ruta))
        faltan = [c for c in PRUEBA_GLIFOS if not fo.has_glyph(ord(c))]
        if faltan:
            print(f"    aviso: {archivo} no trae {''.join(faltan)}")
            continue
        encontradas[clave] = str(ruta)
    return encontradas


def construir(origen, destino, primario_hex, titulo_variante):
    doc = fitz.open(origen)
    # show_pdf_page no admite el mismo documento como origen y destino,
    # así que el logotipo se recorta de una segunda instancia del archivo.
    fuente_logo = fitz.open(origen)
    fuentes = localizar_fuentes()

    regular = fuentes.get("Aptos")
    bold = fuentes.get("Aptos-Bold") or fuentes.get("Aptos-SemiBold")
    semi = fuentes.get("Aptos-SemiBold") or bold
    if not (regular and bold):
        doc.close()
        fuente_logo.close()
        raise RuntimeError(
            "No encuentro Aptos completa. Debería estar en "
            f"{DFONTS} (viene con Microsoft Office).")

    primario = rgb(primario_hex)
    terracota = rgb(TERRACOTA)
    gris = rgb(GRIS_PIEDRA)

    # El fondo se copia de una página INTERIOR, no de la portada. En este manual
    # sólo las tapas (1 y 6) son crema; las láminas de contenido ya van en blanco.
    # Copiarlo de la portada dejaba esta lámina crema entre páginas blancas.
    fondo_pagina = doc[1].get_pixmap(clip=fitz.Rect(2, 2, 6, 6)).pixel(0, 0)
    fondo_pagina = tuple(v / 255 for v in fondo_pagina)

    pag = doc.new_page(width=1008, height=612)
    pag.draw_rect(fitz.Rect(0, 0, 1008, 612), color=None, fill=fondo_pagina)

    def texto(x, y, txt, size, color, fuente=regular, nombre="apt"):
        pag.insert_text((x, y), txt, fontname=nombre, fontfile=fuente,
                        fontsize=size, color=color)

    def centrado(cx, y, txt, size, color, fuente=regular, nombre="apt"):
        fo = fitz.Font(fontfile=fuente)
        ancho = fo.text_length(txt, fontsize=size)
        texto(cx - ancho / 2, y, txt, size, color, fuente, nombre)

    # ── Cabecera, idéntica a la del resto del manual ────────────────────────
    texto(CAB_X, 56.9, "Aplicaciones", CAB_TITULO_SIZE, primario, bold, "aptb")
    texto(CAB_X, 80.0, "El sistema sobre fondo blanco", CAB_BAJADA_SIZE,
          terracota, bold, "aptb")

    # ── Divisoria entre las dos columnas ────────────────────────────────────
    pag.draw_line(fitz.Point(630, 120), fitz.Point(630, 500),
                  color=mezclar(GRIS_PIEDRA, BLANCO, 0.75), width=0.7)

    # ═══ Columna izquierda · SLIDE 16:9 ═════════════════════════════════════
    centrado(330, 138, "SLIDE DE PRESENTACIÓN", ETIQUETA_SIZE, gris)

    slide = fitz.Rect(60, 162, 585, 457)  # 525 × 295 = 16:9
    pag.draw_rect(slide, color=mezclar(GRIS_PIEDRA, BLANCO, 0.8),
                  fill=rgb(BLANCO), width=0.7)

    # Franjas del borde izquierdo, con extremo redondeado como exige la pág. 5
    for i in range(5):
        x = slide.x0 + 22 + i * 7.5
        tono = mezclar(primario_hex, BLANCO, i * 0.16)
        pag.draw_line(fitz.Point(x, slide.y0 + 34), fitz.Point(x, slide.y1 - 34),
                      color=tono, width=3.4, lineCap=1)

    tx = slide.x0 + 88
    texto(tx, slide.y0 + 62, "Inversión agrícola", 27, primario, bold, "aptb")
    texto(tx, slide.y0 + 94, "con gestión propia", 27, primario, bold, "aptb")
    texto(tx, slide.y0 + 122, "Reporte de gestión · Primer trimestre 2026",
          12.5, gris)
    pag.draw_line(fitz.Point(tx, slide.y0 + 141), fitz.Point(tx + 62, slide.y0 + 141),
                  color=terracota, width=2.6, lineCap=1)

    # Fila de cifras — es donde mejor se ve el juego de los tres colores
    datos = [("12.400", "ha administradas"), ("38", "campos"), ("6", "regiones")]
    dx = tx
    for cifra, etiqueta in datos:
        texto(dx, slide.y0 + 196, cifra, 33, primario, bold, "aptb")
        texto(dx, slide.y0 + 214, etiqueta, 10.5, gris)
        fo = fitz.Font(fontfile=bold)
        dx += max(fo.text_length(cifra, fontsize=33), 76) + 46

    # El logotipo real, recortado del original
    alto = 26
    ancho = alto * LOGO_PRINCIPAL.width / LOGO_PRINCIPAL.height
    destino_logo = fitz.Rect(slide.x1 - 26 - ancho, slide.y1 - 24 - alto,
                             slide.x1 - 26, slide.y1 - 24)
    pag.show_pdf_page(destino_logo, fuente_logo, 1, clip=LOGO_PRINCIPAL)

    # ═══ Columna derecha · DOCUMENTO ════════════════════════════════════════
    centrado(806, 138, "DOCUMENTO / INFORME", ETIQUETA_SIZE, gris)

    hoja = fitz.Rect(692, 162, 920, 457)  # proporción carta
    pag.draw_rect(hoja, color=mezclar(GRIS_PIEDRA, BLANCO, 0.8),
                  fill=rgb(BLANCO), width=0.7)

    # Encabezado del documento
    alto_l = 15
    ancho_l = alto_l * LOGO_PRINCIPAL.width / LOGO_PRINCIPAL.height
    pag.show_pdf_page(fitz.Rect(hoja.x0 + 18, hoja.y0 + 18,
                                hoja.x0 + 18 + ancho_l, hoja.y0 + 18 + alto_l),
                      fuente_logo, 1, clip=LOGO_PRINCIPAL)
    pag.draw_line(fitz.Point(hoja.x0 + 18, hoja.y0 + 46),
                  fitz.Point(hoja.x1 - 18, hoja.y0 + 46),
                  color=primario, width=1.6, lineCap=1)

    texto(hoja.x0 + 18, hoja.y0 + 68, "Informe de gestión", 12.5, primario,
          bold, "aptb")
    texto(hoja.x0 + 18, hoja.y0 + 82, "Temporada 2025 – 2026", 8.5, gris)

    # Párrafos simulados
    y = hoja.y0 + 100
    for ancho_rel in (1.0, 0.96, 0.99, 0.62):
        pag.draw_line(fitz.Point(hoja.x0 + 18, y),
                      fitz.Point(hoja.x0 + 18 + (hoja.width - 36) * ancho_rel, y),
                      color=mezclar(GRIS_PIEDRA, BLANCO, 0.62), width=2.4)
        y += 9

    # Tabla — encabezado en primario, filas alternas en crema
    ty = y + 14
    fila_h = 15
    pag.draw_rect(fitz.Rect(hoja.x0 + 18, ty, hoja.x1 - 18, ty + fila_h),
                  color=None, fill=primario)
    texto(hoja.x0 + 24, ty + 10.5, "CAMPO", 7.5, rgb(BLANCO), semi, "apts")
    texto(hoja.x0 + 104, ty + 10.5, "SUPERFICIE", 7.5, rgb(BLANCO), semi, "apts")
    texto(hoja.x0 + 168, ty + 10.5, "ESTADO", 7.5, rgb(BLANCO), semi, "apts")

    filas = [("Los Maitenes", "1.240 ha", "Operativo"),
             ("El Roble", "980 ha", "Operativo"),
             ("Santa Elena", "2.115 ha", "En revisión"),
             ("Las Nieves", "760 ha", "Operativo")]
    for i, (campo, sup, estado) in enumerate(filas):
        fy = ty + fila_h * (i + 1)
        if i % 2 == 0:
            pag.draw_rect(fitz.Rect(hoja.x0 + 18, fy, hoja.x1 - 18, fy + fila_h),
                          color=None, fill=rgb(CREMA))
        texto(hoja.x0 + 24, fy + 10.5, campo, 7.5, gris)
        texto(hoja.x0 + 104, fy + 10.5, sup, 7.5, gris)
        color_estado = terracota if estado == "En revisión" else gris
        texto(hoja.x0 + 168, fy + 10.5, estado, 7.5, color_estado)

    # Pie del documento
    py = ty + fila_h * (len(filas) + 1) + 16
    for ancho_rel in (1.0, 0.88):
        pag.draw_line(fitz.Point(hoja.x0 + 18, py),
                      fitz.Point(hoja.x0 + 18 + (hoja.width - 36) * ancho_rel, py),
                      color=mezclar(GRIS_PIEDRA, BLANCO, 0.62), width=2.4)
        py += 9
    pag.draw_line(fitz.Point(hoja.x0 + 18, hoja.y1 - 20),
                  fitz.Point(hoja.x0 + 42, hoja.y1 - 20),
                  color=terracota, width=2.2, lineCap=1)

    # ── Nota al pie de la página ────────────────────────────────────────────
    texto(CAB_X, 500, f"Color primario en esta versión: {titulo_variante}",
          10.5, gris)
    texto(CAB_X, 516,
          "Los dos ejemplos van sobre blanco puro, que es el fondo que ya usan las "
          "láminas de contenido del manual.", 10.5, gris)

    doc.save(destino, garbage=3, deflate=True)
    doc.close()
    fuente_logo.close()


VARIANTES = [
    ("00-original", "687B5D", "Verde oliva 687B5D (propuesta actual)"),
    ("A-gris-piedra", "666461", "Gris piedra 666461"),
    ("B-blue-grey", "33353E", "Blue Grey 33353E"),
    ("C-gris-profundo", "4A4744", "Gris piedra profundo 4A4744"),
]


def main():
    if not ORIGEN.exists():
        sys.exit(f"No encuentro el original en {ORIGEN}")

    for clave, primario, titulo in VARIANTES:
        for sufijo in ("", "-fondo-blanco"):
            base = SALIDA / f"{clave}{sufijo}.pdf"
            if not base.exists():
                print(f"  (falta {base.name}, se omite)")
                continue
            destino = SALIDA / f"{clave}{sufijo}-con-aplicaciones.pdf"
            construir(base, destino, primario, titulo)
            print(f"  {destino.name:<48} {destino.stat().st_size // 1024:>4} KB")


if __name__ == "__main__":
    main()

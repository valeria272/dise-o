#!/usr/bin/env python3
"""
Landera — reconstruye el paquete de logo completo, con la paleta aprobada.

El problema que resuelve
------------------------
El editable que entregó la diseñadora (`LOGO_LANDERA.ai`, 24-08-2026) y sus 4 PNG
exportados están **con la paleta vieja**: el isotipo va en verde oscuro `#1C4907`.
El manual que el cliente aprobó el 03-09 usa el **verde oliva `#687B5D`**. El logo
se recoloreó entre el editable y el manual, y el editable nunca se actualizó.

Además el editable tiene 4 mesas —horizontal y vertical, cada una con sus dos
bajadas— y el contrato pide **principal, secundaria, isotipo y monocromática**.
Faltan el isotipo suelto y todas las monocromáticas.

Esto toma el `.ai` como fuente (está todo trazado, sin fuentes embebidas: no
depende de tener Barkentina instalada), le corrige el verde y genera el juego
completo en vector y en web.

⚠️ Esto NO reemplaza el `.ai` maestro. El entregable «archivos abiertos» del
contrato tiene que salir del archivo de Coni con sus capas; lo que se genera acá
es para poder componer el manual y las plantillas sin esperar esa pasada.

Uso:
    python3 scripts/landera_kit_logo.py
"""

import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Falta PyMuPDF. Instálalo con: python3 -m pip install pymupdf")

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw" / "landera" / "editables" / "LOGO_LANDERA.ai"
SALIDA = RAIZ / "public" / "assets" / "landera" / "kit-logo"

# Los 4 colores que el .ai escribe con `scn`, medidos sobre su content stream.
TINTA = "33353E"
GRIS = "666461"
TERRACOTA = "E4361F"
VERDE_VIEJO = "1C4907"   # el que hay que jubilar
VERDE = "687B5D"         # verde oliva, el aprobado

# Las cinco monocromáticas que declara el manual (pág. 2), más dos técnicas.
MONOS = {
    "TINTA": TINTA,
    "TERRACOTA": TERRACOTA,
    "GRIS": GRIS,
    "CREMA": "FAF1E8",
    "VERDE": VERDE,
    # ⚠️ Estas dos NO están en el manual. Se agregan porque un kit sin blanco puro
    # no sirve sobre fotografía oscura y sin negro puro no sirve para impresión a
    # una tinta. Van marcadas aparte hasta que el cliente las apruebe.
    "BLANCO": "FFFFFF",
    "NEGRO": "000000",
}
MONOS_FUERA_DE_MANUAL = {"BLANCO", "NEGRO"}

# mesa del .ai → nombre, siguiendo la nomenclatura que ya usa la diseñadora
MESAS = {
    0: "HOR-FARM",
    1: "HOR-GESA",
    2: "VER-FARM",
    3: "VER-GESA",
}
# El isotipo no tiene mesa propia: se recorta de la horizontal-farmland.
ISOTIPO_DESDE = 0

# El PNG se dimensiona por el LADO LARGO, no por el ancho: el isotipo es vertical
# y fijando el ancho salía de 2000 × 3377 px, un archivo absurdo para una marca
# que se usa chica.
LADO_LARGO_PNG = 2000


def rgb(hex_str):
    h = hex_str.lstrip("#")
    return tuple(round(int(h[i:i + 2], 16) / 255, 3) for i in (0, 2, 4))


def literal(hex_str):
    return " ".join(f"{v:g}" for v in rgb(hex_str))


def repintar(doc, cambios):
    """Sustituye tripletas de color en los content streams de todas las páginas.

    `cambios` es {hex_origen: hex_destino}. Se usa un centinela por cambio para
    que las sustituciones no se pisen entre sí cuando un destino es también
    origen de otro (pasa al aplanar a monocromo).
    """
    marcas = {o: f"\x00{i}\x00" for i, o in enumerate(cambios)}

    for pagina in doc:
        for xref in pagina.get_contents():
            s = doc.xref_stream(xref).decode("latin-1")
            original = s
            for o in cambios:
                s = re.sub(rf"(?<![\d.]){re.escape(literal(o))}(\s+)(scn|SCN)\b",
                           rf"{marcas[o]}\1\2", s)
            for o, dest in cambios.items():
                s = s.replace(marcas[o], literal(dest))
            if s != original:
                doc.update_stream(xref, s.encode("latin-1"))


def caja_de(pagina):
    """Caja real del dibujo, sin el aire de la mesa de trabajo."""
    rs = [d["rect"] for d in pagina.get_drawings()]
    return fitz.Rect(min(r.x0 for r in rs), min(r.y0 for r in rs),
                     max(r.x1 for r in rs), max(r.y1 for r in rs))


def caja_isotipo(pagina):
    """El isotipo es el racimo de trazos más a la izquierda de la horizontal."""
    rs = [d["rect"] for d in pagina.get_drawings()]
    izq = min(r.x0 for r in rs)
    propios = [r for r in rs if r.x0 < izq + 110]
    return fitz.Rect(min(r.x0 for r in propios), min(r.y0 for r in propios),
                     max(r.x1 for r in propios), max(r.y1 for r in propios))


def exportar(doc, pagina, clip, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)
    out = fitz.open()
    pg = out.new_page(width=clip.width, height=clip.height)
    pg.show_pdf_page(pg.rect, doc, pagina, clip=clip)

    out.save(destino.with_suffix(".pdf"), garbage=3, deflate=True)
    destino.with_suffix(".svg").write_text(pg.get_svg_image(), encoding="utf-8")

    esc = LADO_LARGO_PNG / max(clip.width, clip.height)
    pix = pg.get_pixmap(matrix=fitz.Matrix(esc, esc), alpha=True)
    pix.save(destino.with_suffix(".png"))
    out.close()


def construir(cambios, sufijo, carpeta):
    doc = fitz.open(ORIGEN)
    repintar(doc, cambios)

    piezas = []
    for mesa, nombre in MESAS.items():
        piezas.append((mesa, caja_de(doc[mesa]), f"LOGO_LANDERA_{nombre}{sufijo}"))
    piezas.append((ISOTIPO_DESDE, caja_isotipo(doc[ISOTIPO_DESDE]),
                   f"LOGO_LANDERA_ISO{sufijo}"))

    for mesa, clip, nombre in piezas:
        exportar(doc, mesa, clip, SALIDA / carpeta / nombre)
    doc.close()
    return len(piezas)


def main():
    if not ORIGEN.exists():
        sys.exit(f"No encuentro el editable en {ORIGEN}\n"
                 f"Bájalo de Drive: ONE SHOT LANDERA / LOGO")

    total = construir({VERDE_VIEJO: VERDE}, "", "policromo")
    print(f"  policromo/                    {total} piezas   "
          f"(verde {VERDE_VIEJO} → {VERDE})")

    for nombre, hexa in MONOS.items():
        cambios = {c: hexa for c in (TINTA, GRIS, TERRACOTA, VERDE_VIEJO)}
        carpeta = ("monocromo-fuera-de-manual" if nombre in MONOS_FUERA_DE_MANUAL
                   else "monocromo")
        n = construir(cambios, f"_MONO-{nombre}", carpeta)
        marca = "  ⚠️ pendiente de OK" if nombre in MONOS_FUERA_DE_MANUAL else ""
        print(f"  {carpeta}/{nombre:<12s}      {n} piezas   #{hexa}{marca}")

    print(f"\n  Todo en {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Landera — saca los 10 bloqueos de logo del PDF del cliente, en vector.

Por qué existe: el manual completo son 22 láminas y hoy existen 6. Para componer
las 16 que faltan hace falta el logotipo, y la tipografía con la que está
construido (Barkentina) no está en ninguna máquina del estudio — además de tener
la licencia comercial sin resolver (ver `clients/landera/CLAUDE.md` §2).

Resulta que no hace falta: **el logo está trazado**. En las págs. 1, 2 y 6 del PDF
no hay ni una imagen rasterizada, son 30, 256 y 30 objetos vectoriales. O sea que
el logotipo se reproduce sin instalar nada.

Los bloqueos NO se recortan a ojo: se agrupan los trazos por proximidad y cada
racimo es un bloqueo. Así las medidas salen del archivo y no de mirar la pantalla,
que es justo el dato que necesitan las láminas de área de reserva y tamaño mínimo.

Uso:
    python3 scripts/landera_extraer_logos.py
"""

import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Falta PyMuPDF. Instálalo con: python3 -m pip install pymupdf")

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw" / "landera" / "PROPUESTA-BASE-V2.pdf"
SALIDA = RAIZ / "public" / "assets" / "landera" / "logos"

PAGINA = 1  # índice 1 = pág. 2, la de las versiones del logo

# Los rótulos de columna viven arriba de y=165; debajo empiezan los bloqueos.
TECHO = 165

# Nombres en el orden en que salen al ordenar por columna y luego por altura.
NOMBRES = [
    "01-principal-farmland-management",
    "02-principal-gestion-agricola",
    "03-secundaria-farmland-management",
    "04-secundaria-gestion-agricola",
    "05-isotipo",
    "06-mono-blue-grey-farmland",
    "07-mono-terracota-gestion",
    "08-mono-gris-piedra-farmland",
    "09-mono-crema-gestion",
    "10-mono-verde-oliva-farmland",
]


def cerca(a, b, gx=26, gy=16):
    """¿Dos trazos son del mismo bloqueo?

    Los huecos son distintos por eje y por eso no sirve un solo umbral: dentro de
    un bloqueo, la separación horizontal más grande es la que hay entre el isotipo
    y la «L», y la vertical es la que separa «Landera» de su bajada. Entre dos
    bloqueos distintos el hueco es mucho mayor que ambas.
    """
    return (a.x0 - gx < b.x1 and b.x0 - gx < a.x1 and
            a.y0 - gy < b.y1 and b.y0 - gy < a.y1)


def agrupar(rects):
    grupos = []
    for r in rects:
        tocados = [g for g in grupos if any(cerca(r, q) for q in g)]
        nuevo = [r]
        for g in tocados:
            grupos.remove(g)
            nuevo += g
        grupos.append(nuevo)

    # Una sola pasada no basta: dos racimos pueden quedar unidos por un tercero
    # que se agregó después. Se fusiona hasta que ya no cambie nada.
    cambio = True
    while cambio:
        cambio = False
        for i in range(len(grupos)):
            for j in range(i + 1, len(grupos)):
                if any(cerca(a, b) for a in grupos[i] for b in grupos[j]):
                    grupos[i] += grupos[j]
                    grupos.pop(j)
                    cambio = True
                    break
            if cambio:
                break
    return grupos


def bloqueos(pagina):
    rects = [d["rect"] for d in pagina.get_drawings() if d["rect"].y0 > TECHO]
    # Las divisorias entre columnas son líneas altísimas y finísimas.
    rects = [r for r in rects if not (r.height > 200 and r.width < 3)]

    cajas = []
    for g in agrupar(rects):
        r = fitz.Rect(min(q.x0 for q in g), min(q.y0 for q in g),
                      max(q.x1 for q in g), max(q.y1 for q in g))
        if r.width > 25 and r.height > 15:
            cajas.append(r)

    # Por columna (redondeando para que la misma columna caiga junta) y luego
    # de arriba abajo.
    cajas.sort(key=lambda r: (round(r.x0 / 60), r.y0))
    return cajas


def main():
    if not ORIGEN.exists():
        sys.exit(f"No encuentro el original en {ORIGEN}")

    src = fitz.open(ORIGEN)
    cajas = bloqueos(src[PAGINA])

    if len(cajas) != len(NOMBRES):
        sys.exit(f"Esperaba {len(NOMBRES)} bloqueos y encontré {len(cajas)}. "
                 f"Cambió el PDF: revisa los umbrales de cerca() antes de seguir.")

    SALIDA.mkdir(parents=True, exist_ok=True)

    for nombre, clip in zip(NOMBRES, cajas):
        out = fitz.open()
        pg = out.new_page(width=clip.width, height=clip.height)
        pg.show_pdf_page(pg.rect, src, PAGINA, clip=clip)

        out.save(SALIDA / f"landera-{nombre}.pdf", garbage=3, deflate=True)
        (SALIDA / f"landera-{nombre}.svg").write_text(pg.get_svg_image(),
                                                      encoding="utf-8")
        out.close()
        print(f"  landera-{nombre:38s} {clip.width:6.1f} × {clip.height:5.1f} pt")

    src.close()
    print(f"\n  {len(cajas)} bloqueos en {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Landera — ensambla la entrega del manual: PDF completo, hoja de contacto y ZIP
de editables. Todas las láminas salen de clients/landera/manual/*.html vía
render.sh, salvo la 15 (iconografía), que sigue siendo la del PDF del cliente
y se toma de la v1.0 ya entregada.

    python3 scripts/landera_ensamblar.py            # arma v1.1
"""
import io, re, sys, zipfile
from pathlib import Path

import fitz
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
MAN = RAIZ / "clients/landera/manual"
PLA = RAIZ / "clients/landera/plantillas"
OUT = RAIZ / "out/landera/manual"
VERSION = "1.1"
ANTERIOR = OUT / "LANDERA-manual-de-marca-v1.0.pdf"
HEREDADAS = {15: (ANTERIOR, 14)}          # nº de lámina → (pdf, índice de página)

LEEME = f"""LANDERA — Manual de marca v{VERSION} · archivos editables
====================================================

laminas-editables/   Las 25 láminas, una por archivo PDF.
                     Se abren y se editan en Illustrator: el texto está VIVO
                     (no trazado) y Aptos va incrustada. Para editarlo hay que
                     tener Aptos instalada — viene con Microsoft Office.

fuente-html/         El código que genera las láminas. Editar el .html y correr
                     ./render.sh <nombre>  para volver a sacar el PDF.
                     base.css tiene la anatomía: posiciones, cuerpos y colores.

plantillas/          Las piezas digitales: firmas de correo (HTML, listas para
                     pegar), banners, feed, historias, fondos de escritorio y las
                     4 maestras de presentación. ./render.sh <nombre> <ancho> <alto>

Qué cambió en la v{VERSION} (ronda del cliente, 05-09-2026)
------------------------------------------------------
· 03 Introducción: se sintetizó; va directo a cómo se usa el manual.
· 07 Versiones: ahora dice cuándo va cada versión y la muestra en su soporte.
· 12 Tipografía: Aptos es la principal (títulos y textos); Barkentina queda
  como secundaria, sólo para destacar un detalle. Se corrigió el «Blod Italic».
· 22 Redes sociales (nueva): feed de Instagram simulado, 3 posts y 3 historias.
· 24 Patrones en aplicación (nueva): tres fondos de escritorio y una botella.
· Señalética pasa a la 23 y la contraportada a la 25.

Pendientes conocidos
--------------------
· El logotipo de las firmas apunta a landera.cl/img/logo-landera.png, que aún
  no existe. Hay que subirlo antes de repartirlas.
· La fotografía de las láminas 11, 22 y 23 y la botella de la 24 son de
  referencia, generadas. Reemplazar por material real de Landera.
· Barkentina: la muestra de la lámina 12 se compuso con los glifos del propio
  PDF; para usarla en piezas hay que tener el archivo y su licencia comercial.
"""


def laminas():
    """Lista ordenada [(nº, ruta_html)] de las láminas numeradas."""
    r = []
    for f in sorted(MAN.glob("[0-9][0-9]-*.html")):
        r.append((int(f.name[:2]), f))
    return r


def ensamblar():
    doc = fitz.open()
    contacto = []
    for n, html in laminas():
        pdf = OUT / (html.stem + ".pdf")
        if not pdf.exists():
            sys.exit(f"falta {pdf.name}: corre ./render.sh {html.stem}")
        doc.insert_pdf(fitz.open(pdf))
        if n + 1 in HEREDADAS:
            src, idx = HEREDADAS[n + 1]
            doc.insert_pdf(fitz.open(src), from_page=idx, to_page=idx)
    salida = OUT / f"LANDERA-manual-de-marca-v{VERSION}.pdf"
    doc.set_metadata({"title": f"Landera · Manual de marca v{VERSION}",
                      "author": "Copywriters · Grupo Copylab"})
    doc.save(salida, garbage=4, deflate=True)
    print(f"✓ {salida.name} · {len(doc)} láminas")

    # hoja de contacto 4 columnas
    thumbs = []
    for p in doc:
        pix = p.get_pixmap(dpi=40)
        thumbs.append(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
    w, h = thumbs[0].size
    cols, gap = 4, 12
    filas = -(-len(thumbs) // cols)
    hoja = Image.new("RGB", (cols * w + (cols + 1) * gap, filas * h + (filas + 1) * gap), "#CFCBC4")
    for i, t in enumerate(thumbs):
        hoja.paste(t, (gap + (i % cols) * (w + gap), gap + (i // cols) * (h + gap)))
    hoja.save(OUT / f"CONTACTO-{len(doc)}-laminas.png")
    print(f"✓ CONTACTO-{len(doc)}-laminas.png")
    return salida, len(doc)


def zip_editables(n_laminas):
    salida = OUT / f"LANDERA-editables-v{VERSION}.zip"
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("_zip/LEEME.txt", LEEME)
        for n, html in laminas():
            z.write(OUT / (html.stem + ".pdf"), f"_zip/laminas-editables/{html.stem}.pdf")
            z.write(html, f"_zip/fuente-html/{html.name}")
        # la 15 heredada, como PDF suelto
        src, idx = HEREDADAS[15]
        d = fitz.open(); d.insert_pdf(fitz.open(src), from_page=idx, to_page=idx)
        z.writestr("_zip/laminas-editables/15-iconografia.pdf", d.tobytes())
        for f in ["base.css", "_comun.css", "render.sh", "T1-la-voz.html", "T2-como-escribimos.html"]:
            z.write(MAN / f, f"_zip/fuente-html/{f}")
        for f in sorted(PLA.iterdir()):
            if f.suffix in (".html", ".css", ".sh", ".md"):
                z.write(f, f"_zip/plantillas/{f.name}")
        # los fondos de escritorio van rasterizados: se usan tal cual
        for f in sorted((RAIZ / "out/landera/plantillas").glob("fondo-pc-*.png")):
            z.write(f, f"_zip/fondos-de-escritorio/{f.name}")
    print(f"✓ {salida.name} · {len(zipfile.ZipFile(salida).namelist())} archivos")


if __name__ == "__main__":
    pdf, n = ensamblar()
    zip_editables(n)

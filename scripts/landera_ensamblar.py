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
VERSION = "3.0"          # interna: sólo en el historial del repo
SUFIJO = ""              # el cliente recibe un manual sin número
ANTERIOR = OUT / "LANDERA-manual-de-marca-v1.0.pdf"
HEREDADAS = {17: (ANTERIOR, 14)}          # nº de lámina → (pdf, índice de página)

LEEME = f"""LANDERA — Manual de marca · archivos editables · septiembre 2026
==================================================================

laminas-editables/   Las 42 láminas, una por archivo PDF.
                     Se abren y se editan en Illustrator: el texto está VIVO
                     (no trazado) y Aptos va incrustada. Para editarlo hay que
                     tener Aptos instalada — viene con Microsoft Office.

fuente-html/         El código que genera las láminas. Editar el .html y correr
                     ./render.sh <nombre>  para volver a sacar el PDF.
                     base.css tiene la anatomía: posiciones, cuerpos y colores.

plantillas/          Las piezas digitales: firmas de correo (HTML, listas para
                     pegar), banners, feed, historias, fondos de escritorio y las
                     4 maestras de presentación. ./render.sh <nombre> <ancho> <alto>

Pendientes conocidos
--------------------
· El logotipo de las firmas apunta a landera.cl/img/logo-landera.png, que aún
  no existe. Hay que subirlo antes de repartirlas.
· Barkentina: la muestra de las láminas 12, 21, 27 y 34 se compuso con los glifos
  del propio PDF (_muestra-Barkentina.otf); para usarla en piezas hay que tener
  el archivo y su licencia comercial.
· Las fotografías de referencia (campos, señalética, maquinaria, prendas) son
  generadas y están rotuladas como tales: se reemplazan con el archivo real de
  Landera antes de la versión final.
"""


def laminas():
    """Lista ordenada [(nº, ruta_html)] de las láminas numeradas."""
    r = []
    for f in sorted(MAN.glob("[0-9][0-9]-*.html")):
        r.append((int(f.name[:2]), f))
    return r


APTOS = "/Applications/Microsoft Word.app/Contents/Resources/DFonts/Aptos.ttf"


def refoliar(pagina, n, seccion):
    """La lámina heredada trae el folio de la versión anterior pintado: se tapa
    y se escribe el nuevo con la misma anatomía (x 60,2 · 30 pt del pie · 8 pt)."""
    pagina.draw_rect(fitz.Rect(56, 570, 260, 590), color=None, fill=(1, 1, 1))
    pagina.insert_font(fontname="Aptos", fontfile=APTOS)
    pagina.insert_text((60.2, 582.5), f"{n:02d} · {seccion.upper()}", fontsize=8,
                       fontname="Aptos", color=(0.66, 0.64, 0.61))


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
            refoliar(doc[-1], n + 1, "Sistema")
    salida = OUT / f"LANDERA-manual-de-marca{SUFIJO}.pdf"
    doc.set_metadata({"title": "Landera · Manual de marca · septiembre 2026",
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
    salida = OUT / f"LANDERA-editables{SUFIJO}.zip"
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("_zip/LEEME.txt", LEEME)
        for n, html in laminas():
            z.write(OUT / (html.stem + ".pdf"), f"_zip/laminas-editables/{html.stem}.pdf")
            z.write(html, f"_zip/fuente-html/{html.name}")
        # la 15 heredada, como PDF suelto
        src, idx = HEREDADAS[17]
        d = fitz.open(); d.insert_pdf(fitz.open(src), from_page=idx, to_page=idx)
        z.writestr("_zip/laminas-editables/17-iconografia.pdf", d.tobytes())
        for f in ["base.css", "_comun.css", "_v2.css", "render.sh", "T1-la-voz.html", "T2-como-escribimos.html"]:
            z.write(MAN / f, f"_zip/fuente-html/{f}")
        for f in sorted(PLA.iterdir()):
            if f.suffix in (".html", ".css", ".sh", ".md"):
                z.write(f, f"_zip/plantillas/{f.name}")
        # los fondos de escritorio van rasterizados: se usan tal cual
        for f in sorted((RAIZ / "out/landera/plantillas").glob("fondo-pc-*.png")):
            z.write(f, f"_zip/fondos-de-escritorio/{f.name}")
        z.write(RAIZ / "out/landera/_fuentes/muestra/Barkentina-muestra.otf",
                "_zip/fuente-html/_muestra-Barkentina.otf")
    print(f"✓ {salida.name} · {len(zipfile.ZipFile(salida).namelist())} archivos")


if __name__ == "__main__":
    pdf, n = ensamblar()
    zip_editables(n)

# -*- coding: utf-8 -*-
"""Deja los logos de proveedores de EBEMA listos para la cápsula de co-marca.

Toma lo que Paulina dejó en `raw/ebema/3-logos-y-packshots/` (PDF vectorial, PNG,
JPG, SVG) y escribe en `clients/ebema/sistema-grilla/img/proveedores/` un PNG por
proveedor: fondo transparente y **recortado al contenido**.

El recorte no es cosmético. La cápsula de co-marca posiciona el logo por su borde
real; un margen dentro del archivo la descuadra — es el mismo defecto que el
15-09-2026 dejaba la pastilla de EBEMA un 20 % corta.

⚠️ Un logo que es un BLOQUE DE COLOR (Masisa: fondo verde con letras blancas) no
se recorta por transparencia: hay que recortarlo por su rectángulo de color, o el
bloque pierde su respiro. El script distingue los dos casos solo.

Uso:
    python scripts/ebema-logos-proveedores.py            # todos
    python scripts/ebema-logos-proveedores.py masisa     # sólo los que calcen
"""
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw" / "ebema" / "3-logos-y-packshots"
DESTINO = RAIZ / "clients" / "ebema" / "sistema-grilla" / "img" / "proveedores"
ALTO_MIN = 300          # el LEEME de la carpeta pide 300 px de alto como mínimo
LADO_PDF = 1600         # a cuántos px se rasteriza el lado mayor de un PDF
# Ojo: no se rasteriza por DPI fijo. «Logo Melon_1,5x1,5m.pdf» es una lámina de
# metro y medio: a 400 dpi son 23.000 px de lado y MuPDF se planta.

# nombre del archivo -> slug del proveedor. Lo que no esté acá se deduce.
NOMBRES = {
    "masisa-logo-blanco": "masisa",
    "logo-san-juan-horizontal-amarillo": "san-juan",
    "pointfixr": "pointfix",
    "etersol_by_gr (1)": "etersol",
    "logo_surpol_2016": "surpol",
    "logo toro": "toro",
    "cedral_logo": "cedral",
    "logo melon_1,5x1,5m": "melon",
    "logo novoplast-01": "novoplast",
    "logo owens corning (pdf)": "owens-corning",
    "logo weber2": "weber",
    "logo_cave": "cave",
    "logo-cmpc": "cmpc",
    "logo-polpaico": "polpaico",
    "logo-vinilit": "vinilit",
}
# los que no son de un proveedor: son de la propia EBEMA
SALTAR = ("ebema a color", "logo_ec_")


def slug(nombre):
    n = nombre.lower().strip()
    if n in NOMBRES:
        return NOMBRES[n]
    n = re.sub(r"^logo[\s_-]*", "", n)
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    n = re.sub(r"[^a-z0-9]+", "-", n).strip("-")
    return n


def abrir(p):
    """Devuelve la imagen RGBA. El PDF se rasteriza a DPI_PDF con fondo transparente."""
    if p.suffix.lower() == ".pdf":
        import pymupdf
        pag = pymupdf.open(p)[0]
        zoom = LADO_PDF / max(pag.rect.width, pag.rect.height)
        pix = pag.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=True)
        return Image.frombytes("RGBA", (pix.width, pix.height), pix.samples)
    return Image.open(p).convert("RGBA")


def quitar_fondo_blanco(im):
    """Si el logo viene sobre blanco opaco (JPG, o PNG sin alfa real), lo transparenta."""
    a = np.asarray(im).astype(int)
    if a[:, :, 3].min() < 250:          # ya trae alfa: no se toca
        return im, False
    menor = a[:, :, :3].min(axis=2)
    if np.percentile(menor, 90) < 245:  # casi nada es blanco: no es fondo blanco
        return im, False
    alfa = np.clip((250 - menor) * 255 / 15, 0, 255)
    out = a.copy()
    out[:, :, 3] = alfa
    return Image.fromarray(out.astype(np.uint8), "RGBA"), True


def recortar(im):
    """Recorta al contenido. Si el logo es un bloque de color macizo, lo respeta.

    Un logo como el de Masisa es un rectángulo verde con letras blancas: recortarlo
    por alfa da el rectángulo entero igual, pero si el archivo trae margen alrededor
    del bloque hay que sacarlo, no sacar el respiro interno del bloque.
    """
    a = np.asarray(im)
    ys, xs = np.where(a[:, :, 3] > 12)
    if not len(ys):
        return im, "vacío"
    caja = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
    rec = im.crop(caja)
    # ¿es un bloque macizo? casi todo opaco dentro de su propia caja
    op = np.asarray(rec)[:, :, 3] > 12
    tipo = "bloque de color" if op.mean() > 0.92 else "marca suelta"
    return rec, tipo


def main():
    filtro = sys.argv[1].lower() if len(sys.argv) > 1 else None
    DESTINO.mkdir(parents=True, exist_ok=True)
    hechos, avisos = [], []

    for p in sorted(ORIGEN.iterdir()):
        if p.suffix.lower() not in (".pdf", ".png", ".jpg", ".jpeg"):
            if p.suffix.lower() == ".svg":
                avisos.append(f"{p.name}: SVG, hay que exportarlo a mano")
            continue
        base = p.stem.lower()
        if any(base.startswith(s) for s in SALTAR):
            continue
        s = slug(p.stem)
        if filtro and filtro not in s:
            continue

        im, transparentado = quitar_fondo_blanco(abrir(p))
        rec, tipo = recortar(im)
        if rec.height < ALTO_MIN:
            f = ALTO_MIN / rec.height
            rec = rec.resize((round(rec.width * f), ALTO_MIN), Image.LANCZOS)
            avisos.append(f"{s}: venía a {im.height} px de alto, se subió a {ALTO_MIN}")

        salida = DESTINO / f"logo_{s}.png"
        rec.save(salida, optimize=True)
        hechos.append((s, p.suffix.lstrip(".").lower(), rec.size, tipo,
                       "fondo quitado" if transparentado else "ya traía alfa"))

    print(f"{len(hechos)} logos -> {DESTINO.relative_to(RAIZ)}\n")
    for s, ext, tam, tipo, nota in hechos:
        print(f"  logo_{s:16s} {ext:4s} {tam[0]:5d}x{tam[1]:<5d} {tipo:16s} {nota}")
    if avisos:
        print("\nOjo:")
        for a in avisos:
            print("  · " + a)


if __name__ == "__main__":
    main()

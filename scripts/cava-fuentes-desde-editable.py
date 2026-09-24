# -*- coding: utf-8 -*-
"""Reconstruye las Bebas Neue Pro de CAVA a partir del .ai del mes.

POR QUÉ EXISTE. `clients/cava/marca.json` lo dice: la titular de CAVA es **Bebas
Neue Pro**, de Adobe Fonts y `empaquetable: false`. No viaja en el paquete del
editable ni está en el disco del estudio — el Mac de Coni sólo tiene «Bebas Kai»,
que es otra fuente. Sin esto, una pieza de CAVA hecha por código sale con una
tipografía que no es la de la marca.

Pero el propio `.ai` lleva **incrustados los subconjuntos CFF** de los pesos que
usó esa pieza. Este script los extrae y arma una OTF utilizable por PIL.

    python3 scripts/cava-fuentes-desde-editable.py <carpeta de salida> "<ai 1>" ["<ai 2>" ...]

Se pueden pasar VARIOS .ai y los subconjuntos se FUSIONAN. Hace falta: el de
septiembre no trae la «L» mayúscula y el del Cyber no trae la «r» minúscula —
juntos cubren el alfabeto. Son el mismo diseño y las mismas métricas, así que
unirlos es seguro.

⚠️ DOS LÍMITES QUE HAY QUE TENER PRESENTES:
  1. Es un SUBCONJUNTO: trae sólo los glifos que esa pieza usó. Si el copy nuevo
     necesita una letra que no estaba, no está. El script lista lo que cubre.
  2. Es para maquetar y para pruebas. Para la entrega final lo correcto es
     activar Bebas Neue Pro en Creative Cloud, que es la licencia que el estudio
     ya paga.

Verificación hecha el 22-09-2026 contra `CAVA_SEPT_BRIEF9-16.png`: la altura de
mayúscula del render sale 167 px contra 165 px reales.
"""
import io, os, sys
from pypdf import PdfReader
from pypdf.generic import IndirectObject
from fontTools.cffLib import CFFFontSet
from fontTools.fontBuilder import FontBuilder
from fontTools.agl import AGL2UV
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.t2CharStringPen import T2CharStringPen


def subconjuntos(ai_path):
    """Saca cada FontFile3 (CFF) incrustado en el .ai, por nombre de fuente."""
    r = PdfReader(ai_path)
    out, vistos = {}, set()
    for pg in r.pages:
        fonts = (pg.get("/Resources") or {}).get("/Font") or {}
        if isinstance(fonts, IndirectObject):
            fonts = fonts.get_object()
        for _, fo in fonts.items():
            fo = fo.get_object()
            base = str(fo.get("/BaseFont", "")).lstrip("/").split("+")[-1]
            desc = fo.get("/FontDescriptor")
            if desc is None:
                dfs = fo.get("/DescendantFonts")
                if dfs:
                    desc = dfs.get_object()[0].get_object().get("/FontDescriptor")
            if desc is None:
                continue
            desc = desc.get_object()
            if "/FontFile3" in desc and base not in vistos:
                vistos.add(base)
                out[base] = desc["/FontFile3"].get_object().get_data()
    return out


def _glifos(cff_bytes):
    """Lee un subconjunto CFF y devuelve {nombre: (charstring nuevo, ancho, lsb)}."""
    cff = CFFFontSet()
    cff.decompile(io.BytesIO(cff_bytes), None)
    td = cff[cff.fontNames[0]]
    cs = td.CharStrings
    dwx = td.Private.defaultWidthX
    out = {}
    for g in [".notdef"] + list(td.charset):
        if g not in cs or g in out:
            continue
        c = cs[g]
        c.decompile()
        bp = BoundsPen(None)
        c.draw(bp)                       # ← el ancho se puebla al DIBUJAR, no al decompilar
        w = getattr(c, "width", None) or dwx
        pen = T2CharStringPen(w, None)
        c.draw(pen)
        out[g] = (pen.getCharString(), int(round(w)), int(bp.bounds[0]) if bp.bounds else 0)
    return out


def a_otf(lista_cff, destino, psname):
    """Funde varios subconjuntos del MISMO peso en una sola OTF."""
    fundido = {}
    for data in lista_cff:
        for g, v in _glifos(data).items():
            fundido.setdefault(g, v)     # gana el primero: el editable más reciente
    orden = [".notdef"] + sorted(g for g in fundido if g != ".notdef")
    orden = [g for g in orden if g in fundido]
    progs = {g: fundido[g][0] for g in orden}
    met = {g: (fundido[g][1], fundido[g][2]) for g in orden}
    cmap = {}
    for g in orden:
        uv = AGL2UV.get(g)
        if uv is not None and uv not in cmap:
            cmap[uv] = g
    fb = FontBuilder(unitsPerEm=1000, isTTF=False)
    fb.setupGlyphOrder(orden)
    fb.setupCharacterMap(cmap)
    fb.setupCFF(psname, {"FullName": psname, "FamilyName": psname}, progs, {})
    fb.setupHorizontalMetrics(met)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupNameTable({"familyName": psname, "styleName": "Regular",
                       "fullName": psname, "psName": psname, "version": "1.0"})
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=1000, usWinDescent=250)
    fb.setupPost()
    fb.save(destino)
    return orden


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    dest, ais = sys.argv[1], sys.argv[2:]
    os.makedirs(dest, exist_ok=True)
    por_peso = {}
    for ai in ais:
        for nombre, data in subconjuntos(ai).items():
            # FILTRO=Scotch para Selfie (24-09-2026); por defecto, la Bebas de CAVA.
            if os.environ.get("FILTRO", "Bebas") in nombre:
                por_peso.setdefault(nombre, []).append(data)
    for nombre, lista in sorted(por_peso.items()):
        salida = os.path.join(dest, nombre + ".otf")
        glifos = a_otf(lista, salida, nombre)
        print("%-26s %3d glifos  (de %d editable/s)" % (nombre, len(glifos), len(lista)))
        print("   cubre:", " ".join(g for g in glifos if g != ".notdef"))


if __name__ == "__main__":
    main()

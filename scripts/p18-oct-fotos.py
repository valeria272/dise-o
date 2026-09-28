"""PISO18 · OCTUBRE 2026 — prepara cada foto al tamaño en que la pieza la muestra.

R-17: la caja de recorte de cada pieza queda escrita acá. R-15: el zoom tiene tope;
donde una foto queda por debajo del máster se anota el factor (`amplía`).

Entradas:
  · reales → `raw/hilton/piso18/oct/base/<clave>.jpg` (origen en `base/ORIGEN.txt`)
  · generadas → `raw/hilton/piso18/oct/gen/<clave>.jpg` (`scripts/p18-oct-generar.py`)
Salida: `public/assets/hilton/piso18/oct/`.

Uso:  python scripts/p18-oct-fotos.py
"""
import sys
from pathlib import Path

from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
BASE = RAIZ / "raw/hilton/piso18/oct/base"
GEN = RAIZ / "raw/hilton/piso18/oct/gen"
REFS = RAIZ / "raw/hilton/piso18/oct/refs"
OUT = RAIZ / "public/assets/hilton/piso18/oct"

FEED = (2250, 2813)
STORY = (2250, 4000)

# salida: (origen, caja (x, y, ancho, alto) o None = centrada al aspecto, tamaño final)
FOTOS = {
    # FEED 06-10 · arreglos florales — piso_18-7 (deco-ago2024), vertical 3840×5760
    # Ronda 2 (Eli 28-09: «en vez de ciertos rosados, esos tonos azulitos» de la ref): la
    # misma foto recoloreada con Nano Banana Pro (rosas y dalia → azul empolvado), sobre
    # el recorte 4:5 de la ronda 1 (0, 480, 3840, 4800). La 1 queda en `deco88.jpg`.
    "f0610.jpg": (GEN / "f0610-azul.jpg", None, FEED),
    # FEED 09-10 · portada — 0161 (3-Finales 2026) extendida a 4:5 con Nano Banana Pro
    "f0910-1.jpg": (GEN / "f09-s1.jpg", None, FEED),
    # FEED 13-10 · atardecer — ventanal y lounge reiluminados (banq 0003 y 0001)
    # Ronda 2: la 1 tenía dos atardeceres en el ventanal; va la tirada `f13-s1r2` (un solo cielo)
    "f1310-1.jpg": (GEN / "f13-s1r2.jpg", None, FEED),
    "f1310-2.jpg": (GEN / "f13-s2.jpg", None, FEED),
    # FEED 16-10 · collage de la portada, cuatro cuadros 4:5 de 1125×1406
    "f1610-c1.jpg": (BASE / "banq43.jpg", None, (1125, 1406)),   # salón de noche
    "f1610-c2.jpg": (BASE / "jul5.jpg", (520, 0, 1200, 1500), (1125, 1406)),  # barra de tragos
    "f1610-c3.jpg": (BASE / "banq46.jpg", None, (1125, 1406)),   # mesa larga de matrimonio
    "f1610-c4.jpg": (BASE / "banq18.jpg", (4200, 300, 3240, 4049), (1125, 1406)),  # lounge
    # FEED 16-10 · slides 2 a 5
    "f1610-2.jpg": (BASE / "deco86.jpg", (1344, 0, 3072, 3840), FEED),   # Matrimonios
    # Cumpleaños: la ronda de trabajo usó julio evento 107 (copas oscuras a 1500 px, ampliaba
    # ×1,5); se reemplazó por la barra con torta producida sobre la barra y el salón reales.
    "f1610-3.jpg": (GEN / "f16-s3.jpg", None, FEED),
    "f1610-4.jpg": (BASE / "banq17.jpg", (1400, 0, 3200, 4000), FEED),   # Corporativos
    "f1610-5.jpg": (BASE / "deco55.jpg", (0, 463, 3701, 4626), FEED),    # Cierre, lámpara cálida
    # FEED 23-10 · Tex-Mex (generadas, 3:4 → 4:5)
    "f2310-1.jpg": (GEN / "f23r2-s1.jpg", None, FEED),  # ronda 2: foto documental
    "f2310-2.jpg": (GEN / "f23r3-s2.jpg", None, FEED),  # ronda 3: cenital, cuatro tacos
    "f2310-3.jpg": (GEN / "f23r2-s3b.jpg", None, FEED),  # ronda 2: foto documental
    "f2310-4.jpg": (GEN / "f23r2-s4.jpg", None, FEED),  # ronda 2: foto documental
    # FEED 27-10 · wedding planner (generada sobre la mesa real banq 0047)
    "f2710.jpg": (GEN / "f27.jpg", None, FEED),
    # STORIES
    "s0510.jpg": (BASE / "deco93.jpg", (300, 0, 3240, 5760), STORY),     # primavera (estática)
    "s0710-dulce.jpg": (BASE / "banq20.jpg", (900, 0, 3900, 4000), (1000, 1026)),
    "s0710-salada.jpg": (BASE / "banq51.jpg", (1000, 0, 3900, 4000), (1000, 1026)),
    "s0910.jpg": (GEN / "st09b.jpg", None, STORY),
    "s2310.jpg": (GEN / "st23.jpg", None, STORY),
    "s2710-fondo.jpg": (BASE / "deco86.jpg", (1800, 0, 2160, 3840), (1400, 2489)),
    "s2710-tour.jpg": (REFS / "matterport-movil.png", None, (900, 1950)),
    "s2710-salon.jpg": (BASE / "banq0.jpg", (3100, 0, 1842, 3990), (900, 1950)),
}


def prepara(nombre, origen, caja, tam):
    # ⭐ Si la generada ya pasó por el upscaler de PRECISIÓN ×2 (`gen/x2/`), va esa; la
    # caja se escribe sobre la original y se escala con ella.
    x2 = GEN / "x2" / origen.name
    if origen.parent == GEN and x2.is_file():
        k = Image.open(x2).width / Image.open(origen).width
        caja = None if caja is None else tuple(round(v * k) for v in caja)
        origen = x2
    if not origen.is_file():
        print(f"·  falta {origen.name} → {nombre} queda para después")
        return
    im = Image.open(origen).convert("RGB")
    if caja is None:
        ar = tam[0] / tam[1]
        if im.width / im.height > ar:
            w = round(im.height * ar)
            caja = ((im.width - w) // 2, 0, w, im.height)
        else:
            h = round(im.width / ar)
            caja = (0, (im.height - h) // 2, im.width, h)
    x, y, w, h = caja
    im = im.crop((x, y, x + w, y + h))
    factor = tam[0] / w
    im = im.resize(tam, Image.LANCZOS)
    im.save(OUT / nombre, quality=93)
    nota = f"  ⚠️ amplía ×{factor:.2f}" if factor > 1.02 else ""
    print(f"✓  {nombre:20s} ← {origen.name} caja {caja} → {tam[0]}×{tam[1]}{nota}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    solo = sys.argv[1:]
    for nombre, (origen, caja, tam) in FOTOS.items():
        if solo and not any(s in nombre for s in solo):
            continue
        prepara(nombre, origen, caja, tam)


if __name__ == "__main__":
    main()

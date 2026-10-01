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
    # Ronda 4 (cliente 29-09, FEED C13: «la G2 también es imagen, seleccionemos alguna
    # horizontal para que quede dividida de forma continua»): la MISMA 0161 horizontal,
    # sin extender, recortada a 8:5 (dos 4:5 lado a lado) y partida al medio. El corte
    # cae en el hueco entre la 3.ª y la 4.ª silla. Reduce (×0,78), no amplía.
    "f0910-p1.jpg": (BASE / "fin160.jpg", (0, 100, 2884, 3605), FEED),
    "f0910-p2.jpg": (BASE / "fin160.jpg", (2883, 100, 2884, 3605), FEED),
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
    # Ronda 4 (cliente 29-09, STORIES D14: «un fondo más entretenido, que sea de algún
    # montaje»): la mesa redonda montada con el centro alto de pampas (deco piso_18-112),
    # en vez del papel beige. 2:3 → 9:16 centrada; reduce, no amplía.
    "s0710-fondo.jpg": (BASE / "deco112.jpg", (300, 0, 3240, 5760), STORY),
    "s0710-dulce.jpg": (BASE / "banq20.jpg", (900, 0, 3900, 4000), (1000, 1026)),
    "s0710-salada.jpg": (BASE / "banq51.jpg", (1000, 0, 3900, 4000), (1000, 1026)),
    # ST 15-10 · encuesta cumpleaños: fondo = la mesa larga real (banq46) de noche, a
    # 1080×1920 porque va desenfocada (a 2250 ampliaría ×1,04); las tres temáticas se
    # generaron sobre esa misma mesa (`p18-oct-generar.py st15-*`).
    # ronda 2 (Eli 29-09: «el fondo más con las luces que tiene Piso18, una escena más
    # bonita»): esferas de vidrio con velas sobre el salón de noche (deco piso_18-143).
    # caja más cerrada (2700×4800, reduce ×0,83) y más abajo, para que las esferas queden
    # ARRIBA, alrededor del logo, y no detrás de la hoja
    "s1510-fondo.jpg": (BASE / "deco143.jpg", (570, 960, 2700, 4800), STORY),
    # la hoja: textura de papel generada (`st15-papel`), al 860×1120 de la mesa ×2,0833
    "s1510-papel.jpg": (GEN / "st15-papel.jpg", None, (1792, 2334)),
    "s1510-retro.jpg": (GEN / "st15-retro.jpg", None, (600, 800)),
    "s1510-tropical.jpg": (GEN / "st15-tropical.jpg", None, (600, 800)),
    "s1510-dorado.jpg": (GEN / "st15-dorado.jpg", None, (600, 800)),
    # ── 01-10 · ST 13, 19 y 21-10 + FEED 20-10 ──────────────────────────────────────────
    # ST 13-10 · fondo del sobre: mesa real de matrimonio con flores y esferas (deco
    # piso_18-88, vertical 3840×5760), 2:3 → 9:16 centrada; reduce, no amplía.
    "s1310-fondo.jpg": (BASE / "deco102.jpg", (300, 0, 3240, 5760), STORY),
    # ST 19-10 · fondo en blanco y negro: mesas del salón de noche (julio evento 50,
    # 1500×2250). Va desenfocado y bajo grano: a 1080×1920 (a 2250 ampliaría ×1,78).
    "s1910-fondo.jpg": (BASE / "jul56.jpg", (117, 0, 1266, 2250), (1080, 1920)),
    # la polaroid muestra 476 px de mesa ⇒ 1000×1000 alcanza (×2,08 = 992)
    # tirada b: foto robada desde atrás del grupo (la 1 era de banco de imágenes, X-12)
    "s1910-fiesta.jpg": (GEN / "st19-fiestab.jpg", None, (1000, 1000)),
    # ST 21-10 · pantalla dividida, cada mitad 1080×960 de mesa (9:8). Generadas a 2048²:
    # se recorta el alto; arriba (Japonesa) se ve el tercio alto, abajo (New York) el bajo.
    "s2110-japonesa.jpg": (GEN / "st21-japonesa.jpg", (0, 0, 2048, 1820), (2250, 2000)),
    # New York: caja corrida a la derecha y abajo para dejar fuera la tabla de quesos del
    # buffet de referencia (no es de esta estación); sobre el ×2 de precisión no amplía.
    "s2110-newyork.jpg": (GEN / "st21-newyork.jpg", (300, 380, 1748, 1554), (2250, 2000)),
    # FEED 20-10 · cumpleaños, 1856×2304 (4:5)
    "f2010.jpg": (GEN / "f20-cumple.jpg", None, FEED),
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

#!/usr/bin/env python3
"""
REVEX octubre 2026 — ambientes de los 7 carruseles del brief de Sebastián
(«Revex brief octubre 2026.xlsx», Drive 1rnAxEwixHZ5MLybEcg7SkI36FiljlBLa).

La IA hace AMBIENTE. La muestra de producto que va sobre la gráfica es SIEMPRE
la foto oficial de gruporevex.cl (raw/revex/oct2026/productos/, ver PROCEDENCIA.tsv).

Cómo se mantiene «un mismo baño, cambia sólo el revestimiento» (look and feel del brief):
  1. La tarjeta base se genera con Seedream 5 Pro edit + la foto del producto.
  2. Las demás tarjetas de la familia EDITAN la base: ref 1 = base, ref 2 = producto nuevo.
  3. La story NO se genera aparte: se expande el cuadrado con image-expand/flux-pro,
     así es la misma sala por construcción.

Idempotente: si el archivo existe, no se vuelve a pedir (cuesta créditos).

    python3 scripts/revex-oct2026-ambientes.py 01a            # una escena
    python3 scripts/revex-oct2026-ambientes.py 01             # toda la familia
    python3 scripts/revex-oct2026-ambientes.py todo --story   # y sus stories
"""
import sys, os, argparse
from pathlib import Path
from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib
M = importlib.import_module("magnific")

RAIZ = Path(__file__).resolve().parent.parent
PROD = RAIZ / "public/assets/revex/oct/productos"
OUT = RAIZ / "public/assets/revex/oct"

# Composición que exige la tarjeta de Paulina: la muestra y el texto van CENTRADOS en la
# mitad inferior. Si el mueble cae ahí, la muestra lo tapa (pasó con la primera 01a, 29-09).
LIBRE = (" COMPOSITION: keep the CENTRAL LOWER HALF of the frame calm and uncluttered, showing only "
         "the product surface (plain tiled wall, carpet or floor); place furniture and objects at the "
         "left or right edges or in the upper part.")
COMUN = LIBRE + (" Photorealistic interior photograph for a flooring and tiles retailer catalogue, "
         "bright natural daylight, soft realistic shadows, beige-greige-warm wood palette, "
         "minimalist, elegant, uncluttered. Straight-on eye-level camera, 35mm lens. "
         "No people, no text, no logos, no brand names, no watermarks.")

MANTENER = ("Keep image 1 exactly the same: identical camera angle, framing, furniture, objects, "
            "window, light, colors and every other surface. ")

# escena: (base o None, [refs de producto], prompt)
E = {
 # ── 01 · cerámicas blancas de muro: un mismo baño, cambia sólo el revestimiento
 "01a": (None, ["6910003060_0.jpg"],
   "A bright minimalist bathroom. The whole back wall, floor to ceiling, is clad in GLOSSY WHITE "
   "rectangular ceramic wall tiles 30x60 cm laid horizontally in a straight stacked grid with thin "
   "light-grey grout lines, the glaze reflecting the daylight, like the tile in the reference image. "
   "A floating light-oak vanity with a white basin and a round mirror above it stand on the RIGHT "
   "third of the frame, partially cropped by the right edge; a small olive plant and folded linen "
   "towels on the vanity. A window with daylight on the far left. The centre and left of the frame "
   "is a large uninterrupted tiled wall from floor to ceiling, with a light stone floor strip at "
   "the very bottom." + COMUN),
 "01b": ("01a", ["6910102540_0.jpg"],
   MANTENER + "Change ONLY the wall tiles: replace them with MATTE WHITE ceramic wall tiles 25x40 cm "
   "laid vertically in a straight stacked grid, thin light-grey grout, no gloss or reflections, "
   "like image 2."),
 "01c": ("01a", ["6351001020_0.jpg"],
   MANTENER + "Change ONLY the wall tiles: replace them with SMALL glossy white BEVELED subway "
   "tiles 10x20 cm — about THREE TIMES SMALLER than the current tiles, roughly 25 rows from floor to "
   "ceiling — laid horizontally in RUNNING BOND (every row offset by half a tile, like bricks), each "
   "tile with a visible beveled edge catching the light, thin light-grey grout, exactly like image 2."
   # 1ª versión salió al tamaño del 30×60 y en hileras rectas (29-09)
   ),
 "01d": ("01a", ["derivado_6353001515.png"],
   MANTENER + "Change ONLY the wall tiles: replace them with small GLOSSY WHITE SQUARE ceramic "
   "tiles 15x15 cm — perfect identical squares, about 16 rows from floor to ceiling — in a STRICTLY "
   "REGULAR straight grid: every vertical and horizontal joint continuous and aligned across the "
   "whole wall, no half tiles, no offsets, no irregular joints. Thin light-grey grout, glaze "
   "reflecting the light, like image 2."
   # 1ª versión salió con la grilla rota: cuadrados mezclados con medias piezas (29-09).
   # 2ª (Seedream, con «16 rows») salió en rectángulos verticales. La VIGENTE se hizo con
   # Nano Banana Pro (magnific.py pro, refs amb_01a + derivado): cuadrados reales, 29-09.
   ),
 "01e": ("01a", ["6355175250_0.jpg"],
   MANTENER + "Change ONLY the wall tiles: replace them with narrow GLOSSY WHITE BRICK tiles 7.5x25 cm "
   "laid horizontally in running bond, slightly cushioned edges, thin light-grey grout, exactly "
   "like image 2."),

 # ── 02 · Keraz (muro): un ambiente distinto por tarjeta
 "02a": (None, ["6954003060_0.jpg", "6954003060_1.jpg"],
   "A bright contemporary kitchen. The backsplash wall between the light-oak lower cabinets and the "
   "open shelves is covered with the patterned grey-and-white ceramic wall tiles of the reference "
   "images (encaustic-style patchwork of different grey ornamental motifs, 30x60 cm pieces), "
   "reproduced faithfully. White quartz countertop with a few ceramic bowls and a small plant. The "
   "patterned wall is the protagonist and fills the middle and upper part of the frame." + COMUN),
 "02b": (None, ["6962003060_0.jpg", "6962003060_2.jpg"],
   "A bright elegant bathroom with a walk-in shower. The shower wall and the wall behind the vanity "
   "are clad in large MARBLE-EFFECT ceramic wall tiles 30x60 cm laid vertically, white-grey marble "
   "with flowing ochre and caramel veins, exactly the veining of the reference images. Clear glass "
   "shower screen, brushed brass fittings, floating walnut vanity. The marble wall is the "
   "protagonist and fills most of the frame." + COMUN),
 "02c": (None, ["6957003060_0.jpg"],
   "A calm modern living room. The accent wall behind a low light-beige sofa is clad in GREY "
   "MARBLE-EFFECT ceramic wall tiles 30x60 cm, soft grey marble with white and subtle amber veins, "
   "exactly like the reference image, thin grout lines. Light oak floor, a round coffee table, a "
   "tall plant. The marble accent wall is the protagonist and fills the upper two thirds of the "
   "frame." + COMUN),
 "02d": (None, ["6958003060_0.jpg", "6958003060_1.jpg"],
   "A bright boutique bathroom. The wall behind a floating light-oak vanity with a white vessel "
   "basin and a round mirror is clad in WHITE MARBLE-EFFECT tiles in an elongated hexagon pattern "
   "with thin dark grout lines, exactly like the reference images. The patterned marble wall is "
   "the protagonist and fills most of the frame." + COMUN),
 "02e": (None, ["6963003060_0.jpg"],
   "A bright elegant dining area. The accent wall behind a light oak dining table with linen chairs "
   "is clad in CALACATTA GOLD marble-effect ceramic wall tiles 30x60 cm: bright white marble with "
   "thin grey and golden veins, exactly like the reference image. A pendant lamp, a vase with dry "
   "branches. The marble wall is the protagonist and fills the upper two thirds of the frame." + COMUN),

 # ── 03 · Urban: un solo ambiente, las 3 tarjetas con el mismo encuadre
 "03": (None, ["74120060120_0.jpg"],
   "A spacious bright open-plan living room with large-format light grey porcelain floor tiles "
   "60x120 cm, soft concrete-like texture with subtle veining, thin grout lines, exactly like the "
   "reference image. Low sofa, a round coffee table, a large window. The floor is the protagonist "
   "and fills the lower two thirds of the frame." + COMUN),

 # ── 04 · alfombras muro a muro: mismo dormitorio, cambia la alfombra
 "04a": (None, ["5690020092_0.jpg"],
   "A cozy bedroom with warm afternoon light. Wall-to-wall carpet covers the entire floor, edge to "
   "edge, a light pearl-grey textured loop carpet exactly like the reference image. A bed with "
   "linen bedding against the back wall, a bedside table with a lamp, sheer curtains. The camera "
   "is slightly low so the carpeted floor fills the lower half of the frame and its texture reads "
   "clearly in the foreground." + COMUN),
 "04b": ("04a", ["5690040063_0.jpg"],
   MANTENER + "Change ONLY the wall-to-wall carpet: replace it with the sand-beige and taupe "
   "patterned loop carpet of image 2, same coverage, texture clearly visible in the foreground."),
 "04c": ("04a", ["5690066600_0.jpg"],
   MANTENER + "Change ONLY the wall-to-wall carpet: replace it with the light linen-colored "
   "textured loop carpet of image 2, same coverage, texture clearly visible in the foreground."),
 "04d": ("04a", ["5690067000_0.jpg"],
   MANTENER + "Change ONLY the wall-to-wall carpet: replace it with the carpet of image 2: a MUTED "
   "greyish taupe-brown heather, mottled light-grey and brown fibres, LOW saturation — not red, "
   "not orange, not rust. Same coverage, texture clearly visible in the foreground."
   # 1ª versión decía «warm chestnut-brown» y salió óxido: S 0,54 contra 0,14 del producto (29-09)
   ),

 # ── 05 · alfombras dimensionadas: mismo living, cambia el modelo
 "05a": (None, ["5698209037_0.jpg"],
   "A bright living room with a light oak plank floor. A large rectangular area rug lies under a "
   "light linen sofa and a low coffee table, finished with a neat fabric binding tape along all "
   "its edges; the bound edge is clearly visible in the foreground. The rug is a flat-woven "
   "multicolor tweed (cream, burgundy, grey, black flecks) exactly like the reference image. The "
   "rug is the protagonist and fills the lower half of the frame." + COMUN),
 "05b": ("05a", ["5698209073_0.jpg"],
   MANTENER + "Change ONLY the rug: replace it with the rust-orange flat-woven rug of image 2, same "
   "size and position, same bound fabric edges visible in the foreground."),
 "05c": ("05a", ["5698209084_0.jpg"],
   MANTENER + "Change ONLY the rug: replace it with the dark charcoal-brown flat-woven rug of "
   "image 2, same size and position, same bound fabric edges visible in the foreground."),

 # ── 06 · adoquines de caucho: NO hay foto del producto en ningún lado.
 #    Ambiente 100 % generado y PROVISORIO hasta que llegue la foto real.
 "06": (None, [],
   LIBRE + " An outdoor residential terrace and kids play corner in daylight. The ground is paved with "
   "BLACK RECYCLED RUBBER PAVERS, square interlocking rubber tiles with a fine granular rubber "
   "texture, matte black. In the foreground two loose rubber pavers are stacked side by side "
   "showing two different thicknesses (25 mm and 45 mm) so the edges are visible. Some green "
   "plants in planters, a light wooden bench. The rubber floor is the protagonist and fills the "
   "lower two thirds of the frame. Photorealistic, natural daylight, no people, no text, no logos."),

 # ── 07 · SPC Gravity: mismo living, cambia el tono del piso
 "07a": (None, ["5903607305_0.jpg"],
   "A bright minimalist living room with a luminous oak-look SPC plank floor, long planks, very "
   "light sandy oak tone with fine grain, exactly like the reference image. Low linen sofa, a "
   "round light-wood coffee table, a tall olive tree in a pot, a large window with daylight. The "
   "floor is the protagonist and fills the lower half of the frame." + COMUN),
 "07b": ("07a", ["5903607308_0.jpg"],
   MANTENER + "Change ONLY the floor planks: replace them with the grey-taupe 'titanium' oak planks "
   "of image 2, same plank size and direction."),
 "07c": ("07a", ["5903607311_0.jpg"],
   MANTENER + "Change ONLY the floor planks: replace them with the natural mid-brown oak planks of "
   "image 2, same plank size and direction."),
}


def derivados():
    """Los SKU que el sitio no tiene, sacados por código de la foto REAL del mismo
    producto en otro formato (mismo esmalte, misma pasta). No es IA."""
    PROD.mkdir(parents=True, exist_ok=True)
    # 6353001515 Blanco Brillo 15×15: grilla cuadrada sobre el esmalte blanco brillante real
    f = PROD / "derivado_6353001515.png"
    if not f.exists():
        from PIL import ImageDraw
        base = Image.open(PROD / "6910002030_0.jpg").convert("RGB").resize((1000, 1000))
        d = ImageDraw.Draw(base)
        for i in range(1, 6):
            p = round(i * 1000 / 6)
            d.line([(p, 0), (p, 1000)], fill=(214, 216, 218), width=5)
            d.line([(0, p), (1000, p)], fill=(214, 216, 218), width=5)
        base.save(f)
    # Urban 30×60: recorte 1:2 del mismo porcelanato en 60×120, un paño por color
    for sku, src in [("7411003060", "74110060120_0.jpg"), ("7412003060", "74120060120_0.jpg"),
                     ("7413003060", "74130060120_0.jpg")]:
        f = PROD / f"derivado_{sku}.png"
        if not f.exists():
            im = Image.open(PROD / src).convert("RGB")
            w, h = im.size
            im.crop((0, h // 4, w, h // 4 + w // 2)).save(f)


def generar(k):
    base, refs, prompt = E[k]
    out = OUT / f"amb_{k}.png"
    if out.exists():
        print(f"· {k} ya existe"); return out
    rutas = []
    if base:
        b = OUT / f"amb_{base}.png"
        if not b.exists(): generar(base)
        rutas.append(str(b))
    rutas += [str(PROD / r) for r in refs]
    ruta = "/v1/ai/text-to-image/seedream-v5-pro" + ("-edit" if rutas else "")
    cuerpo = {"prompt": prompt, "aspect_ratio": "square_1_1", "resolution": "2k"}
    if rutas:
        cuerpo["reference_images"] = [f"data:{M.mime_de(r)};base64,{M.b64_de(r)}" for r in rutas]
    print(f"→ {k} · Seedream 5 Pro{' edit' if rutas else ''} · {len(rutas)} refs")
    r = M.pedir(ruta, cuerpo)
    M.guarda(M.espera(ruta, r["data"]["task_id"]), out)
    return out


EXPANDIR_BASE = ("Continue the same room naturally: ceiling above, floor below. "
                 "Same light, same materials. No people, no text.")
# La expansión inventa piso: en las 04 puso madera bajo una alfombra MURO A MURO (29-09).
EXPANDIR = {
    "04": ("Continue the same bedroom naturally: ceiling above, and below the SAME wall-to-wall "
           "carpet continuing edge to edge over the entire floor down to the bottom of the frame. "
           "No wood, no tiles, no rug border, no other flooring. Same light. No people, no text."),
}


def story(k):
    """9:16 desde el cuadrado: se expande arriba (techo) y abajo (piso)."""
    src = OUT / f"amb_{k}.png"
    out = OUT / f"amb_{k}_story.png"
    if out.exists():
        print(f"· {k} story ya existe"); return out
    tmp = OUT / f"_exp_{k}.jpg"
    im = Image.open(src).convert("RGB").resize((1440, 1440), Image.LANCZOS)
    im.save(tmp, quality=94)
    alto = round(1440 * 16 / 9)                   # 2560
    extra = alto - 1440
    arriba, abajo = extra // 2, extra - extra // 2
    ruta = "/v1/ai/image-expand/flux-pro"
    print(f"→ {k} story · expand {arriba}/{abajo}")
    r = M.pedir(ruta, {"image": M.b64_de(tmp),
                       "prompt": EXPANDIR.get(k[:2], EXPANDIR_BASE),
                       "left": 0, "right": 0, "top": arriba, "bottom": abajo})
    crudo = OUT / f"_exp_{k}_crudo.jpg"
    M.guarda(M.espera(ruta, r.get("data", r)["task_id"]), crudo)
    exp = Image.open(crudo).convert("RGB").resize((1440, alto), Image.LANCZOS)
    # el cuadrado original encima, con borde suave: la zona de producto no la toca la IA
    borde = 40
    mask = Image.new("L", (1440, 1440), 0)
    mask.paste(255, (0, borde, 1440, 1440 - borde))
    mask = mask.filter(ImageFilter.GaussianBlur(borde / 2))
    exp.paste(im, (0, arriba), mask)
    exp.save(out)
    tmp.unlink(missing_ok=True); crudo.unlink(missing_ok=True)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("que", help="escena (01a), familia (01) o 'todo'")
    ap.add_argument("--story", action="store_true")
    ap.add_argument("--solo-story", action="store_true")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    derivados()
    ks = sorted(E) if a.que == "todo" else [k for k in sorted(E) if k.startswith(a.que)]
    for k in ks:
        if not a.solo_story: generar(k)
        if a.story or a.solo_story: story(k)

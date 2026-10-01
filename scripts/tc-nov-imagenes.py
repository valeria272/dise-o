#!/usr/bin/env python3
"""Tierra Calma · noviembre 2026 — genera las imágenes del mes con Seedream 5 Pro.

    python scripts/tc-nov-imagenes.py            # genera las que falten
    python scripts/tc-nov-imagenes.py e1 h       # sólo ésas (las regenera)
    python scripts/tc-nov-imagenes.py --lista

Los prompts viven ACÁ, versionados: una imagen entregada tiene que poder
rehacerse (memoria `el-render-vuelve-al-repo`). Salida cruda en
`raw/tierracalma/nov2026/ia/<id>.png`; la que se instala en
`public/assets/tierracalma/nov/` la deja `scripts/tc-nov-instalar.py`.

Reglas del manual que mandan en cada prompt:
  · R-23 — la ESTRUCTURA del lugar es real (ladera, ripio ocre en curva, cerco de
    madera oscura horizontal, postes); la vegetación se idealiza con NATIVAS.
    Nunca pradera europea, flores masivas ni cordillera nevada.
  · R-24 — si hay foto real que sirve, cambio mínimo sobre ella (`refs`).
  · R-26 — gente de espaldas o de lejos, nunca mirando a cámara.
  · R-27 — LA IA HACE EL OBJETO, EL CÓDIGO PONE LA LETRA: letreros, afiches y
    papeles se piden EN BLANCO, y se dice tres veces.
  · La composición se escribe en el prompt (dónde va el cielo, dónde el sujeto).
"""
import pathlib
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "raw/tierracalma/nov2026/ia"
REAL = RAIZ / "raw/tierracalma/fotos-reales"
REFS = RAIZ / "raw/tierracalma/nov2026/refs"   # recortes de fotos reales ya preparados

LUGAR = (
    "Real location look: a hillside rural land subdivision in Padre Hurtado, central Chile, "
    "near Santiago. Gentle hillside, winding ochre-orange gravel roads, dark horizontal wooden "
    "rail fences, slender street-light poles along the road, native Chilean sclerophyll "
    "vegetation in fresh spring green (espino, quillay, litre, peumo trees and low shrubs), "
    "spring grass with patches of bare earth, dry ochre-brown bare hills in the background "
    "with NO snow, clean sky. "
)
FOTO = (
    "Photorealistic editorial photograph, late-afternoon golden hour, warm low sunlight, "
    "shot on 35mm, natural believable color, not oversaturated, fine film grain. "
)
SIN = " No text, no letters, no numbers, no logos, no watermark, no people looking at the camera."
BLANCO = (
    " ABSOLUTELY NO TEXT ANYWHERE: every sign, board and paper is completely blank, plain, "
    "unprinted, with no letters, no words, no numbers, no symbols and no drawings on it. "
    "Blank surfaces only. Repeat: all boards and papers are empty and blank."
)
MINIMO = (
    "Keep this real photograph almost unchanged: same framing, same terrain, same roads, same "
    "fences, same houses, same vegetation layout. Only remove the grey haze and fog, give it "
    "warm late-afternoon golden light with soft long shadows, a clear soft sky, and make the "
    "grass and native shrubs slightly fresher spring green. Do not add anything, do not remove "
    "anything, do not invent buildings, mountains or city skyline. Photorealistic, natural."
)

OBJ = (
    "Studio product photograph on a pure seamless WHITE background, soft natural daylight "
    "from the left, a soft realistic contact shadow under the object, the object centered "
    "with generous white margin all around, nothing else in the frame. Warm, natural, "
    "editorial still life. "
)

# id: (aspecto, prompt, [refs])
IMAGENES = {
    # ── c-09-11 · ¿Departamento o parcela? ───────────────────────────────────────
    "e1": ("carrusel", FOTO + LUGAR +
           "A rustic wooden signpost stands at the edge of an ochre gravel rural road, placed in "
           "the lower-center of the frame. On the single vertical post there are exactly TWO large "
           "wide horizontal wooden arrow boards, one above the other, pointing in OPPOSITE "
           "directions: the upper board is an arrow pointing LEFT, the lower board is an arrow "
           "pointing RIGHT. The signpost is CLOSE to the camera and LARGE: each arrow board spans "
           "about 65% of the frame width. The boards are flat, seen straight-on from the front, "
           "painted plain cream-white, slightly weathered. Composition: the top 40% of the image "
           "is clean open soft sky with nothing in it; the two boards sit between 48% and 78% of "
           "the frame height; the road and green hillside behind are softly out of focus." + BLANCO, []),
    "e2": ("carrusel", FOTO +
           "A single wide horizontal wooden arrow sign board pointing LEFT, mounted on a wooden "
           "post, in the lower third of the frame, seen straight-on from the front, painted plain "
           "cream-white, slightly weathered. Behind it, softly out of focus, a dense row of "
           "ordinary mid-rise residential apartment buildings of a Latin American city in muted "
           "grey-blue evening tones, many small balconies and windows, no recognizable landmark. "
           "Composition: the upper 60% of the image is the blurred buildings and plain sky with "
           "no strong detail; the arrow board sits low in the frame." + BLANCO, []),
    "e3": ("carrusel", FOTO + LUGAR +
           "A single LARGE wide horizontal wooden arrow sign board pointing RIGHT, close to the "
           "camera, spanning about 75% of the frame width, mounted on a wooden post, in the lower "
           "third of the frame, seen straight-on from the front, painted plain cream-white, "
           "slightly weathered. Behind it, softly out of focus, a wide open green "
           "hillside parcel with a dark wooden fence and an ochre gravel road under a big warm "
           "sky. Composition: the upper 60% of the image is open sky and distant hills with no "
           "strong detail; the arrow board sits low in the frame." + BLANCO, []),
    # ── c-09-11 · portada, 2ª versión (referencia de Diego, 01-10): las dos mitades ──
    # clients/tierra-calma/referencias/nov2026/c-09-11.jpg — «casa | VS | departamento».
    # Cada foto ocupa MEDIA portada: el sujeto va centrado y con cielo arriba, y la
    # parte baja se funde en el papel donde van los rótulos.
    "e6": ("carrusel", FOTO.replace("late-afternoon golden hour, warm low sunlight", "soft clear daylight") +
           "Street-level view, straight-on, of an ordinary mid-rise residential apartment "
           "building in a Latin American city: a plain grey-beige concrete facade with rows of "
           "small balconies and windows, eight floors, tightly packed, another similar building "
           "right beside it. The building is centered and fills the middle of the frame "
           "vertically; the top 25% of the frame is plain pale sky. Muted, slightly cool, "
           "realistic. No recognizable landmark." + SIN, []),
    "e7": ("carrusel", FOTO + LUGAR +
           "A contemporary single-storey country house with warm vertical wood cladding, a flat "
           "dark roof, large windows and a wooden deck, standing alone in the middle of a wide "
           "open green parcel enclosed by a dark horizontal wooden rail fence. The house is "
           "centered, seen from the front at eye level and from some distance, small against the "
           "land around it; the top 30% of the frame is clean warm sky; wide lawn and an ochre "
           "gravel path in the foreground." + SIN, []),
    # ── st-13-11 · pie en cuotas (fondo sutil bajo el vidrio) ────────────────────
    "g": ("story", FOTO + LUGAR +
          "View from a covered wooden terrace of a contemporary country house looking out over "
          "the green hillside parcel at golden hour: in the near foreground, low in the frame, the "
          "edge of a wooden table with a closed notebook and a ceramic cup; beyond, the land, a "
          "dark wooden fence and ochre hills. Calm, quiet, premium real-estate mood, shallow depth "
          "of field. Vertical composition, upper half mostly sky and soft hills." + SIN, []),
    # ── p-17-11 · afiche en el poste ─────────────────────────────────────────────
    "h": ("carrusel", FOTO +
          "A large blank white paper flyer pinned with two rusty thumbtacks to a weathered wooden "
          "utility post, photographed straight-on from the front. The flyer is a big vertical "
          "sheet of plain white paper that fills most of the frame width; its bottom edge is cut "
          "into exactly FIVE wide vertical tear-off strips of equal width, like a classic tear-off "
          "flyer. All five strips hang FLAT and straight, facing the camera, none of them curled, "
          "folded or twisted; only tiny gaps between them. The strips are tall, about one quarter "
          "of the sheet height. Real paper texture, very soft creases, a soft contact shadow on "
          "the wood. Background: a tree-lined rural gravel road in Padre Hurtado, "
          "central Chile, strongly out of focus, warm late-afternoon light, green native trees. "
          "The flyer is centered, its top edge at about 22% of the frame height and the strips "
          "ending at about 82% of the frame height." + BLANCO, []),
    # ── c-30-11 · antes de comprar tu parcela, lee esto ──────────────────────────
    # ⚠️ TRES VUELTAS, y la razón queda escrita. La 1ª (persona en una banca) y la 3ª
    # (persona en el cerco, horizonte bajo) dieron +0,877 y +0,873 de parecido contra
    # fondos de OCTUBRE: «cielo arriba, ladera abajo» es la estructura de medio mes
    # pasado, y otro sujeto no la cambia. La 2ª no repetía, pero dejaba el titular
    # encima del cerro (X-06). Ésta cambia la ESTRUCTURA: la mitad de arriba es la
    # copa en sombra de los árboles, que recibe el titular sin ser cielo ni terreno
    # (R-20, `scripts/tc-parecido.py`).
    "m1": ("carrusel", FOTO +
           "Looking along an ochre gravel rural road in Padre Hurtado, central Chile, that "
           "passes under the dense overhanging canopy of large native quillay and peumo trees. "
           "The whole upper half of the image is the dark, shaded green canopy, calm and even, "
           "with only a few small warm light speckles. In the lower third, the road glows in "
           "warm golden backlight and, far away and small, one person seen from behind walks "
           "away down the road next to a dark horizontal wooden rail fence. Deep warm contrast "
           "between the shaded canopy and the sunlit road." + SIN, []),
    # ⭐ 4ª y definitiva (Diego, 01-10, comentario en Drive sobre `c-30-11-1`): *«cambiar
    # imagen, pon una toma dron de Tierra Calma, que se vea real pero calidad
    # profesional»*. Sale la arboleda generada y entra la aérea REAL DJI_0318 del 07-08
    # (sin usar en el mes), recortada en vertical y con cambio mínimo (R-24): se le
    # saca la bruma de esa mañana y se le da luz limpia; no se agrega ni se quita nada.
    "m1d": ("carrusel",
            "Keep this real aerial drone photograph almost unchanged: same framing, same "
            "hillside, same winding ochre gravel road, same fences, same parcels and houses in "
            "the valley, same hills on the horizon. Only improve it to professional aerial "
            "photography quality: remove the grey haze and fog, clear soft late-afternoon light "
            "with gentle long shadows, a clean soft sky, crisp fine detail, rich but natural "
            "color, slightly fresher green on the grass and native shrubs. Do not add anything, "
            "do not remove anything, do not invent buildings, mountains or a city skyline. "
            "Photorealistic, natural, believable.", [REFS / "m1-0318.jpg"]),
    "m2": ("carrusel", FOTO +
           "Close-up still life on a warm wooden desk by a window: a pocket calculator, a pair of "
           "reading glasses and a closed kraft-paper folder, soft warm window light, shallow depth "
           "of field, the upper half of the image is softly blurred warm interior with a window "
           "showing green hills. Calm, tidy, premium. No screens, no printed documents." + BLANCO, []),
    "m3": ("carrusel", FOTO +
           "Close-up still life: a set of house keys with a plain round wooden keyring resting on "
           "a rustic wooden table on an outdoor terrace, beside a small potted native plant; the "
           "background is a softly blurred green hillside parcel at golden hour. Keys in the lower "
           "third; upper half is soft blurred landscape and sky." + BLANCO, []),
    "m4": ("carrusel", FOTO +
           "Close-up still life on a light wooden table: an open blank paper planner notebook with "
           "empty unprinted pages, a wooden pencil lying on it and a small ceramic cup of coffee, "
           "warm side light from a window, shallow depth of field, soft blurred warm background in "
           "the upper half." + BLANCO, []),
    "m5": ("carrusel", FOTO +
           "Close-up of two hands only (no faces): one hand passing a small plain cream envelope "
           "to another hand across a wooden table, warm window light, shallow depth of field, soft "
           "blurred warm interior in the upper half. Friendly, trustworthy, calm." + BLANCO, []),
    "m6": ("carrusel", FOTO + LUGAR +
           "Wide view at eye level of the entrance road of the subdivision: an ochre gravel road "
           "curving up the green hillside between dark horizontal wooden rail fences, a few young "
           "native trees, street-light poles, ochre hills behind, glowing golden hour sky. "
           "Composition: upper 45% is clean warm sky; road and fences in the lower half." + SIN, []),
    # ── aéreas y acceso: FOTO REAL + cambio mínimo (R-24) ────────────────────────
    "e5": ("carrusel", MINIMO, [REFS / "e5-0310.jpg"]),
    "l": ("story", MINIMO, [REFS / "l-0299.jpg"]),
    "k": ("carrusel", MINIMO, [REFS / "k-acceso.jpg"]),
    # ── st-20-11 · todo esto cabe en tu parcela ──────────────────────────────────
    "j": ("story",
          "Edit this real aerial drone photograph of empty rural land. Keep the same framing, the "
          "same roads, the same terrain and the same native shrubs around. In the central open "
          "area, enclose ONE large rectangular parcel with a dark horizontal wooden rail fence, "
          "and inside that parcel only, add: one contemporary single-storey main house with a "
          "flat roof and wooden deck, one smaller separate guest house, a tidy garden with lawn "
          "and young native trees, and a neat rectangular vegetable garden with planting rows. "
          "Exactly two buildings, no more. Leave most of the parcel as open green land so the "
          "scale of the plot is clear. Remove the grey haze, warm late-afternoon light, soft long "
          "shadows. Photorealistic aerial photograph, believable, natural color." + SIN,
          [REFS / "j-cenital.jpg"]),
    # ── c-11-11 · «Lo que nadie te cuenta» · 2ª versión, sobre la referencia de Diego ──
    # clients/tierra-calma/referencias/2026-10-01_c-11-11_editorial-dudas.jpg
    # La portada: las hojas de papel con sus clips, EN BLANCO. Los objetos de las
    # slides van sobre blanco puro: la composición los funde con `multiply` sobre el
    # papel crema, así no hace falta recortarlos.
    "f0": ("carrusel", FOTO +
           "A neat stack of three large blank cream-white paper sheets, slightly fanned so the "
           "edges of the sheets behind peek out, held together by one black metal binder clip on "
           "the right edge and one silver paperclip at the top left corner. The stack floats "
           "upright, facing the camera straight-on, centered, and fills about 82% of the frame "
           "width and 80% of its height. The top sheet is a clean, flat, matte, lightly textured "
           "paper with softly rounded corners. Behind it, strongly out of focus, a green hillside "
           "rural landscape in Padre Hurtado, central Chile, with a dark wooden rail fence, at "
           "warm golden hour. Soft realistic shadow of the paper stack." + BLANCO, []),
    "f1": ("feed", OBJ +
           "Object: a partly unrolled architect's blueprint roll of plain off-white paper with a "
           "wooden pencil and a small wooden scale ruler resting on it. The paper is blank." + BLANCO, []),
    "f2": ("feed", OBJ +
           "Object: two small minimalist solid light-wood house models side by side, one larger "
           "and one smaller, simple gabled block shapes, no windows painted." + BLANCO, []),
    "f4": ("feed", OBJ +
           "Object: a single brass house key tied with natural twine to a blank kraft-paper "
           "luggage tag, lying flat, seen from above. The tag is blank." + BLANCO, []),
    "f5": ("feed", OBJ +
           "Object: a small rustic galvanized metal well bucket full of clear water, with a "
           "short coil of natural rope tied to its handle, seen from a slightly high angle." + BLANCO, []),
    # ── r-04-11 · REEL «del terreno a tu casa» · tres fotogramas clave encadenados ──
    # Base REAL: aérea DJI_0300 del 07-08 (no se usa en ninguna otra pieza del mes).
    # Cada fotograma sale del anterior, con el mismo encuadre, para que Kling pueda
    # ir de uno a otro (`--fin`): terreno cercado → la casa → el atardecer.
    "r1": ("story",
           "Keep this real aerial drone photograph almost unchanged: same framing, same "
           "hillside, same ochre gravel paths, same native shrubs and trees. Only two changes: "
           "(1) in the central open area, enclose ONE large rectangular parcel with a dark "
           "horizontal wooden rail fence, clearly visible, with the land inside left natural and "
           "empty; (2) remove the grey haze and give it clear soft morning light. Do not add "
           "any building. Do not add anything else. Photorealistic aerial photograph." + SIN,
           [REFS / "r-0300.jpg"]),
    "r2": ("story",
           "Keep this aerial photograph exactly as it is: identical framing, identical fence, "
           "identical paths, trees, terrain and light. Only add, INSIDE the fenced parcel: one "
           "contemporary single-storey country house with a flat dark roof, warm vertical wood "
           "cladding and a wooden deck, and a short gravel driveway from the fence to the house. "
           "Exactly one house. The house is small compared to the parcel: it covers less than "
           "one tenth of the fenced area, and the rest of the parcel stays open natural land. "
           "Do not change anything outside the fence. Photorealistic aerial photograph." + SIN,
           [SALIDA / "r1.png"]),
    "r3": ("story",
           "Keep this aerial photograph exactly as it is: identical framing, identical house, "
           "fence, paths, trees and terrain. Only change the light: warm golden sunset light "
           "from the left, long soft shadows, a gentle warm glow, slightly deeper colors. Do not "
           "add anything, do not remove anything. Photorealistic aerial photograph." + SIN,
           [SALIDA / "r2.png"]),
    # ── r-19-11 · REEL «¿Y si este fuera tu día a día?» ──────────────────────────────
    # Brief: «POV y escenas de objetos, SIN personas en primer plano.» Cinco fotogramas
    # de arranque para Kling; el corte 4 no es IA: son las tres fotos reales de abajo.
    "i1": ("story", FOTO + LUGAR +
           "First-person point of view on the wooden terrace of a contemporary country house in "
           "the early morning: in the foreground, low in the frame, a steaming ceramic cup of "
           "coffee resting on a wooden railing; beyond it, softly out of focus, the open green "
           "hillside parcel in cool-warm sunrise light with light morning mist. No people, no "
           "hands. The upper 40% of the frame is soft morning sky." + SIN, []),
    "i2": ("story", FOTO + LUGAR +
           "Point of view from the driver's seat of a car, looking through the windshield: the "
           "ochre gravel access road runs straight ahead between dark horizontal wooden rail "
           "fences, towards low ochre hills, in clear morning light. Only the top edge of a plain "
           "dark dashboard is visible at the very bottom of the frame. No people, no hands, no "
           "steering wheel logo, no screens." + SIN, []),
    "i3": ("story", FOTO +
           "Still life seen from above the open boot of a car: two plain brown kraft-paper grocery "
           "bags full of fresh produce, a baguette, leafy greens and fruit, in warm midday light. "
           "The bags are plain and unbranded. No people, no hands. Calm, everyday, premium "
           "editorial look; the upper third of the frame is the soft blurred car interior." + BLANCO, []),
    "i5": ("story", FOTO +
           "Low-angle still life on the green artificial turf of an outdoor padel and football "
           "court at late afternoon: a padel racket, two yellow padel balls and a classic football "
           "resting on the turf in the foreground, with the glass wall and the net softly out of "
           "focus behind, warm low sun, long shadows. The equipment is plain and unbranded. No "
           "people." + BLANCO, []),
    "i6": ("story", MINIMO.replace("warm late-afternoon golden light with soft long shadows",
                                   "warm golden sunset light with long soft shadows"),
           [REFS / "i6-0293.jpg"]),
    # ── las TRES FOTOS REALES que mandó Diego para el corte 4 (01-10), mejoradas ──────
    # «Para los colegios y cesfam del reels del 19 usa estas imágenes, mejora la calidad.»
    # Cambio mínimo (R-24): el edificio es el dato, no se rediseña. Se limpia lo que no
    # es del lugar —cables, autos, peatones (R-26: sin personas identificables)— y se
    # sube la nitidez. Si Seedream altera una fachada o un letrero, se usa la original
    # reescalada: una foto blanda es mejor que un colegio inventado.
    "x1": ("wide",
           "Restore and enhance this real street photograph of a school building. Keep exactly "
           "the same building: the same red-brick and white facade, the same gabled entrance "
           "porch, the same windows with white grilles, the same white fence, the same trees. "
           "Same framing. Only improve the image quality: sharp detail, higher resolution, clean "
           "natural daylight with a soft clear sky, no compression artifacts, and straighten the "
           "slight wide-angle curvature. Remove the overhead cables and the car at the right "
           "edge. Do not add anything, do not redesign the facade. Photorealistic.",
           [RAIZ / "raw/tierracalma/nov2026/reel-i/adjuntas/adj01.png"]),
    "x2": ("wide",
           "Restore and enhance this real street photograph. Keep exactly the same place: the "
           "same red-brick perimeter wall, the same black gate, the same trees, the same two "
           "street lamps, the same sidewalk. Same framing. Only improve the image quality: sharp "
           "detail, higher resolution, clean natural daylight with a soft clear sky, greener "
           "healthier tree foliage, no compression artifacts. Remove the overhead cables, the "
           "trash bin and the yellow road markings. Do not add anything, do not add buildings, "
           "do not change the wall or the gate. Photorealistic.",
           [RAIZ / "raw/tierracalma/nov2026/reel-i/adjuntas/adj02.png"]),
    "x3": ("wide",
           "Restore and enhance this real street photograph of a public health center. Keep "
           "exactly the same building: the same dark grey facade with its two round signs, the "
           "same fence, the same two tall palm trees, the same trees and the same corner. Same "
           "framing. Only improve the image quality: sharp detail, higher resolution, clean "
           "natural daylight, no compression artifacts. Remove all the people, the bicycles, all "
           "the cars and the overhead cables, leaving the street and sidewalk empty and clean. "
           "Do not add anything, do not redesign the building, do not change the round signs. "
           "Photorealistic.",
           [RAIZ / "raw/tierracalma/nov2026/reel-i/adjuntas/adj03.png"]),
}


def una(clave: str) -> str:
    aspecto, prompt, refs = IMAGENES[clave]
    destino = SALIDA / f"{clave}.png"
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "seedream", prompt,
           "--aspecto", aspecto, "--out", str(destino)]
    if refs:
        faltan = [r for r in refs if not r.exists()]
        if faltan:
            return f"✗ {clave}: falta la referencia {faltan[0].name}"
        cmd += ["--refs", *map(str, refs)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    ok = destino.exists() and r.returncode == 0
    return f"{'✓' if ok else '✗'} {clave}" + ("" if ok else f"\n{(r.stdout + r.stderr)[-600:]}")


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--lista" in sys.argv:
        for k, (asp, _, refs) in IMAGENES.items():
            print(f"{k:4} {asp:9} {'real+mínimo' if refs else 'IA'}")
        return
    SALIDA.mkdir(parents=True, exist_ok=True)
    claves = args or [k for k in IMAGENES if not (SALIDA / f"{k}.png").exists()]
    malas = [k for k in claves if k not in IMAGENES]
    if malas:
        sys.exit(f"✗ no existe: {malas}")
    with ThreadPoolExecutor(max_workers=4) as ex:
        for linea in ex.map(una, claves):
            print(linea, flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()

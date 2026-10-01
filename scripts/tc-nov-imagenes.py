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

# id: (aspecto, prompt, [refs])
IMAGENES = {
    # ── c-09-11 · ¿Departamento o parcela? ───────────────────────────────────────
    "e1": ("carrusel", FOTO + LUGAR +
           "A rustic wooden signpost stands at the edge of an ochre gravel rural road, placed in "
           "the lower-center of the frame. On the single vertical post there are exactly TWO large "
           "wide horizontal wooden arrow boards, one above the other, pointing in OPPOSITE "
           "directions: the upper board is an arrow pointing LEFT, the lower board is an arrow "
           "pointing RIGHT. The boards are big, flat, seen straight-on from the front, painted "
           "plain cream-white, slightly weathered. Composition: the top 45% of the image is clean "
           "open soft sky with nothing in it; the signpost occupies the lower half; the road "
           "and green hillside behind are softly out of focus." + BLANCO, []),
    "e2": ("carrusel", FOTO +
           "A single wide horizontal wooden arrow sign board pointing LEFT, mounted on a wooden "
           "post, in the lower third of the frame, seen straight-on from the front, painted plain "
           "cream-white, slightly weathered. Behind it, softly out of focus, a dense row of "
           "ordinary mid-rise residential apartment buildings of a Latin American city in muted "
           "grey-blue evening tones, many small balconies and windows, no recognizable landmark. "
           "Composition: the upper 60% of the image is the blurred buildings and plain sky with "
           "no strong detail; the arrow board sits low in the frame." + BLANCO, []),
    "e3": ("carrusel", FOTO + LUGAR +
           "A single wide horizontal wooden arrow sign board pointing RIGHT, mounted on a wooden "
           "post, in the lower third of the frame, seen straight-on from the front, painted plain "
           "cream-white, slightly weathered. Behind it, softly out of focus, a wide open green "
           "hillside parcel with a dark wooden fence and an ochre gravel road under a big warm "
           "sky. Composition: the upper 60% of the image is open sky and distant hills with no "
           "strong detail; the arrow board sits low in the frame." + BLANCO, []),
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
          "into exactly FIVE wide vertical tear-off strips, like a classic tear-off flyer, two of "
          "the strips slightly curled forward. Real paper texture, soft creases, a soft contact "
          "shadow on the wood. Background: a tree-lined rural gravel road in Padre Hurtado, "
          "central Chile, strongly out of focus, warm late-afternoon light, green native trees. "
          "The flyer is centered, its top edge at about 22% of the frame height and the strips "
          "ending at about 82% of the frame height." + BLANCO, []),
    # ── c-30-11 · antes de comprar tu parcela, lee esto ──────────────────────────
    "m1": ("carrusel", FOTO + LUGAR +
           "A person seen from behind, far from the camera and small in the frame, sitting on a "
           "simple wooden bench on a wooden deck, looking out at the open hillside land at "
           "sunset. Warm backlight. Composition: upper 50% is soft warm sky; the person and deck "
           "are in the lower third." + SIN, []),
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

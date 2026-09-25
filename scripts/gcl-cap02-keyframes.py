#!/usr/bin/env python3
"""G.CL CAP.02 «TURNO DE NOCHE» — keyframes de continuidad (ronda 2).

Storyboard: gcl-agent/universo/06_VIDEO_REELS/CAP_02_TURNO_DE_NOCHE/STORYBOARD_V3_DEFINITIVO.md
Canon:      gcl-agent/universo/00_START_HERE/CANON_V6_STARTER_PACK_CAP02/ (locks 14–19)

Ronda 1 (24-09): 4 keyframes en Nano Banana Pro y Seedream. Valeria eligió como
MAESTRO DE G el K3 de Seedream (`01_CANON_VISUAL/G_MASTER_REFERENCE_VFINAL.png`): cabeza
grande, cuerpo corto, piernas cortas, negro + magenta.

Ronda 2 — sus correcciones:
  · G con esa proporción EXACTA, sin alargarlo ni humanizarlo.
  · Visor limpio: la G de puntos; expresiones mínimas, nunca cara de emoji.
  · Halo fino y funcional, no aureola decorativa.
  · Nivel -1 = backstage creativo real de agencia (archivo, material de campañas,
    cajas, impresos, objetos viejos), no laboratorio sci-fi.
  · Menos neón: taller oculto de agencia, no cyberpunk. El magenta es de G.
  · La ESTACIÓN DE G se bloquea como asset canon: misma mesa, misma pantalla,
    misma altura, mismos objetos en todos los planos.

    python3 scripts/gcl-cap02-keyframes.py estacion        # etapa A: la placa
    python3 scripts/gcl-cap02-keyframes.py continuidad     # etapa B: K1–K4
    python3 scripts/gcl-cap02-keyframes.py continuidad K2  # uno solo

Modelo: Seedream 5 Pro edit (el de la casa y el que eligió Valeria), dos
variantes por keyframe (-a, -b). La placa elegida se copia a
raw/gcl/cap02-v3/refs/estacion_g_canon.png antes de la etapa B.

⛔ Ningún texto se pide a la IA: post-its en blanco, paneles sin letras. El
texto (URGENTE, NO MOLESTAR, 4 %, horas) se compone en post.
"""
import argparse, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REFS = RAIZ / "raw/gcl/cap02-v3/refs"
OUT = RAIZ / "out/gcl/cap02-v3/keyframes-r2"

ESTILO = (
    "Cinematic photoreal still from a premium short documentary comedy, vertical 9:16. "
    "Warm tungsten practical lighting (desk lamps, old bulbs, amber), natural and grounded, deep "
    "shadows. NOT cyberpunk, NOT sci-fi, no neon signs, no blue light: the only magenta/pink light in "
    "the frame comes from G himself. 35mm lens, shallow depth of field, soft film grain. "
    "No legible text anywhere: labels, posters and papers may exist but their writing is illegible or "
    "out of focus. No watermarks. "
)
NIVEL_MENOS_1 = (
    "Setting: LEVEL -1, the hidden backstage of a real creative agency, underneath its office — an "
    "old basement turned into the agency's working archive and workshop: tall metal shelves with "
    "labelled cardboard archive boxes and binders, rolled campaign posters, stacks of printed proofs "
    "and mock-ups, a pinboard with pinned printouts and swatches, old cameras and props from past "
    "shoots, a worn sofa, exposed concrete and pipes, bare warm bulbs. Lived-in, creative, a bit "
    "messy, real. "
)
G = (
    "This is G. His design, proportions, materials, scale, visor and silhouette are canon. Do not "
    "reinterpret, stylize, redesign or vary his anatomy. No extra accessories. "
    "G: the small robot character from the G master reference, reproduced EXACTLY — oversized glossy "
    "black spherical helmet, SHORT stubby body, SHORT legs, dark-maroon soft suit with small 'G.CL' "
    "on the chest, pink-rimmed round headphone pods, chunky sneakers with pink soles. Keep the exact "
    "head-to-body ratio of the master (head is roughly as tall as the whole body below it). Do NOT "
    "elongate him, do NOT humanize him, no neck, no long limbs. His visor is clean black glass. "
)
VISOR_G = "On the visor: only the clean pink LED dot-matrix letter G, exactly as in the master. No face, no emoji. "
HALO = ("A THIN, delicate pink halo ring floats just above the helmet — a small functional night-mode "
        "indicator, subtle, not a big decorative aureole. ")
MARTA = (
    "MARTA: the boxy beige vintage dot-matrix printer character from the references, exactly as "
    "designed — two big cartoon eyes with heavy half-closed eyelids, continuous perforated paper, "
    "scuffed panels, small pink sticky notes, casters. Her height is about the same as G's. "
)
ROLO = (
    "ROLO: the small white-and-black courier robot from the references, exactly as designed — "
    "rounded white helmet with a black band and a small 'C/' mark, black face screen with two pink "
    "rectangular LED eyes, white body, black joints, chunky round feet with pink rims. About 60 "
    "percent of G's height. "
)
ESTACION = (
    "G's WORKSTATION, exactly as in the station reference (same desk, same monitor, same objects, "
    "same positions, same camera height): "
)

REFS_G = ["g_master_cap02.png", "g_master_cap02_full.png", "g_turn.png"]
REFS_SET = ["set_archivo.png", "set_taller.png"]

ETAPA_A = {
    "K0": dict(
        nombre="k0-estacion-g-canon",
        refs=["set_estacion_g.png", "set_archivo.png", "set_taller.png"],
        prompt=ESTILO + NIVEL_MENOS_1 + (
            "Empty establishing plate of G's WORKSTATION, no characters. Medium-wide shot, static, "
            "camera at desk-top height, frontal-3/4. A long, worn dark-oak workbench fills the lower "
            "third. On it, left to right: a black articulated desk lamp (lit, warm), a pencil cup, a "
            "plain white ceramic mug, a slim modern black monitor on a stand showing a dark screen, a "
            "stack of two notebooks, a few printed campaign proofs. The front-center of the bench is "
            "a CLEAR EMPTY AREA where a small 40 cm character will stand. Behind the bench: a cork "
            "pinboard with pinned printouts, then archive shelves with boxes and rolled posters "
            "fading into warm bokeh. Designed to be reused as the same set in every shot."),
    ),
}

ETAPA_B = {
    "K1": dict(
        nombre="k1-g-halo-activandose",
        refs=REFS_G + ["estacion_g_canon.png"],
        prompt=ESTILO + NIVEL_MENOS_1 + G + VISOR_G + HALO + ESTACION + (
            "G stands on the clear area of his workbench, 3/4 front view, medium shot. Night, "
            "00:58. He has just looked up from work and straightened up, in charge. The thin halo "
            "is just switching on — a faint ring, brighter on one side, as if powering up. Two "
            "small translucent pink holographic panels float beside him (abstract bars and boxes, "
            "no letters), softly lit, not blinding."),
    ),
    "K2": dict(
        nombre="k2-trio-nivel-menos-1",
        refs=REFS_G + ["marta_turn.png", "marta_hero.png", "rolo_turn.png", "rolo_hero.png"]
             + REFS_SET,
        prompt=ESTILO + NIVEL_MENOS_1 + G + VISOR_G + HALO + MARTA + ROLO + (
            "Wide shot, static, camera low at G's eye level, on the concrete floor between the "
            "archive shelves. The three stand together in one frame at night, in a quiet pause after "
            "hard work: MARTA on the left with paper spilling from her; G in the center, arms down; "
            "ROLO on the right. SCALE IS CRITICAL: G and Marta the same height, Rolo clearly smaller. "
            "Calm, tired, relieved."),
    ),
    "K3": dict(
        nombre="k3-g-agotado-4pc",
        refs=REFS_G + ["estacion_g_canon.png"],
        prompt=ESTILO + NIVEL_MENOS_1 + G + HALO + ESTACION + (
            "G stands on the clear area of his workbench, frontal medium shot, early morning after "
            "a whole night of work. He is EXHAUSTED: shoulders dropped, arms hanging, helmet tilted "
            "a few degrees down. The visor still shows the dot-matrix letter G but DIMMED, low "
            "brightness, a little flickery. The thin halo is dim and faint. Under the G on the visor, "
            "a thin horizontal low-battery bar, almost empty, in dull coral (no numbers, no text). "
            "Minimal expression, only posture tells he is drained."),
    ),
    "K4": dict(
        nombre="k4-g-apagado-no-molestar",
        refs=REFS_G + ["rolo_turn.png", "rolo_hero.png", "marta_hero.png", "estacion_g_canon.png"],
        prompt=ESTILO + NIVEL_MENOS_1 + G + ROLO + ESTACION + (
            "Morning. G stands on the clear area of his workbench, POWERED OFF: no halo, headphone "
            "pods completely unlit, sneaker soles completely unlit, helmet tilted slightly down. On "
            "his black visor, instead of the G, a faint dim pink dot-matrix 'X X' (two small crosses, "
            "the shutdown mark) barely glowing. ROLO stands on the bench next to him, stretching up "
            "on his toes, carefully pressing a single BLANK square yellow sticky note (no writing) "
            "onto the LOWER part of G's visor with one finger, leaving the X X visible above it. "
            "Gentle, careful. Far background, out of focus: MARTA printing, paper feeding out."),
    ),
}


def correr(clave, d, variante):
    destino = OUT / f"{d['nombre']}-{variante}.png"
    refs = [str(REFS / r) for r in d["refs"]]
    faltan = [r for r in refs if not Path(r).exists()]
    if faltan:
        return f"✗ {clave}-{variante}: faltan referencias {faltan}"
    cmd = [sys.executable, str(RAIZ / "scripts/magnific.py"), "seedream", d["prompt"],
           "--out", str(destino), "--aspecto", "reel", "--refs", *refs]
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = r.returncode == 0 and destino.exists()
    return f"{'✓' if ok else '✗'} {clave}-{variante} → {destino.name}" + ("" if ok else "\n" + (r.stdout + r.stderr)[-400:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("etapa", choices=["estacion", "continuidad"])
    ap.add_argument("claves", nargs="*")
    a = ap.parse_args()
    tabla = ETAPA_A if a.etapa == "estacion" else ETAPA_B
    claves = a.claves or list(tabla)
    OUT.mkdir(parents=True, exist_ok=True)
    trabajos = [(k, tabla[k], v) for k in claves for v in ("a", "b")]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for linea in ex.map(lambda t: correr(*t), trabajos):
            print(linea, flush=True)


if __name__ == "__main__":
    main()

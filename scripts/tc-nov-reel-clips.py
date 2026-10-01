#!/usr/bin/env python3
"""Tierra Calma · noviembre 2026 — los clips del reel del 04-11 («del terreno a tu casa»).

    python scripts/tc-nov-reel-clips.py            # los que falten
    python scripts/tc-nov-reel-clips.py d3         # sólo ése (lo regenera)

⚠️ LO QUE PASÓ EL 01-10-2026, PARA NO REPETIRLO. Este script manda los tres
planos a **Kling 2.1 Pro por la API** (`magnific-video.py --fin`), que es el único
modelo de la API que acepta fotograma final. Las tres tareas terminaron en
**FAILED sin mensaje de error** — lo mismo que le pasó a DoubleTree el 28-09.
Los clips que están en el repo se hicieron con **Kling 3.0 por el CONECTOR de
Magnific** (`video_generate`, slug `kling-30`, 9:16 · 1080p · 5 s,
`keyframes.start` + `keyframes.end`), con estos mismos prompts y estos mismos
fotogramas: 450 créditos por clip. El conector sí acepta fotograma final en 3.0.
Este archivo queda como el REGISTRO de los prompts y como el camino por API el
día que 2.1 Pro vuelva a responder.

La cadena: aérea REAL DJI_0300 → tres fotogramas clave encadenados con Seedream
5 Pro (`tc-nov-imagenes.py` r1 · r2 · r3, mismo encuadre) → Kling con
**fotograma inicial Y final**. Cada plano tiene que TERMINAR en un cuadro
conocido: el corte 2 dibuja las líneas de deslinde sobre `r1` y, si el plano
anterior terminara en otra parte, las líneas no calzarían con el cerco.

  d1  r1-cerca → r1   el dron se aleja y descubre el terreno cercado
  d3  r1 → r2         la casa se levanta sobre el terreno (el efecto de la referencia)
  d4  r2 → r3         la tarde cae sobre el terreno completo

(El corte 2 no es un clip: es `r1` quieto con las líneas de luz dibujadas en código.)
Kling entrega 24 fps: se pasan a 30 con `remotion ffmpeg -r 30 -c:v libx264 -crf 16`.

Salida: public/assets/tierracalma/nov/clips/
"""
import pathlib
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

RAIZ = pathlib.Path(__file__).resolve().parent.parent
KF = RAIZ / "raw/tierracalma/nov2026/reel-d"
OUT = RAIZ / "public/assets/tierracalma/nov/clips"

FIJO = (" Photorealistic aerial drone footage, natural motion, steady and smooth. The terrain, the "
        "paths, the fence and the trees keep exactly their shape and position. No people, no "
        "vehicles, no text.")

CLIPS = {
    "d1": ("r1-cerca.jpg", "r1.jpg",
           "Slow, smooth aerial drone pull-back: the camera rises and moves away gently, revealing "
           "the fenced parcel of land on the hillside in soft morning light. Light morning mist "
           "drifts, the trees barely move in the breeze." + FIJO),
    "d3": ("r1.jpg", "r2.jpg",
           "Locked-off aerial view, the camera does not move. Timelapse of a house being built "
           "inside the fenced parcel: the foundation appears, the timber structure rises, the "
           "walls and the dark roof are completed, and a gravel driveway forms. Smooth, elegant "
           "construction timelapse, the surrounding landscape stays still." + FIJO),
    "d4": ("r2.jpg", "r3.jpg",
           "Locked-off aerial view, the camera barely moves. Timelapse of the light: the afternoon "
           "turns into a warm golden sunset, shadows grow long across the land, the scene glows. "
           "The house and the landscape stay still." + FIJO),
}


def uno(clave: str) -> str:
    ini, fin, prompt = CLIPS[clave]
    destino = OUT / f"{clave}.mp4"
    cmd = [sys.executable, str(RAIZ / "scripts/magnific-video.py"), str(KF / ini), "--fin", str(KF / fin),
           "--prompt", prompt, "--dur", "5", "--modelo", "kling-v2-1-pro", "--minutos", "25",
           "--out", str(destino)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    ok = destino.exists() and r.returncode == 0
    return f"{'✓' if ok else '✗'} {clave}\n{(r.stdout + r.stderr)[-700:]}"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    claves = sys.argv[1:] or [k for k in CLIPS if not (OUT / f"{k}.mp4").exists()]
    with ThreadPoolExecutor(max_workers=3) as ex:
        for linea in ex.map(uno, claves):
            print(linea, flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()

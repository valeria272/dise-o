#!/usr/bin/env python3
"""
«Los de siempre» — anima los keyframes aprobados con Kling 2.1 Pro (frame final
con `image_tail`). Regla: 1 plano = 1 acción; la cámara se mueve poco.

    python3 scripts/traverso-lds-clips.py --solo c01 c02
    python3 scripts/traverso-lds-clips.py           # los que falten

Cada clip sale de 5 s y el montaje (LosDeSiempre.tsx) recorta lo que usa.
Salida: public/assets/traverso/lds/clips/<clip>.mp4
"""
import argparse, os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(RAIZ, "public", "assets", "traverso", "lds")
K = os.path.join(A, "keyframes"); C = os.path.join(A, "casting")
OUT = os.path.join(A, "clips")
VIDEO = os.path.join(RAIZ, "scripts", "magnific-video.py")

LOCK = ("The three characters keep EXACTLY the same design: the real Traverso bottle is the "
        "torso, no face, white gloves, product-colour legs and shoes, black tuxedo. Orange "
        "left, yellow centre, red right. Locked camera on a tripod, no camera shake, no zoom "
        "unless stated, no morphing, no new characters, no text.")

# clip: (inicio, fin|None, prompt, coda)
PLANOS = {
    "c01": (f"{K}/k01a.png", f"{K}/k01b.png",
        "Only legs and shoes visible. The three characters walk slowly and in perfect sync "
        "towards the lens in elegant slow motion, the shoes landing flat on the wet black "
        "floor with reflections, ending with the yellow right shoe close to camera. Low "
        "locked camera 15 cm above the floor, 85mm. " + LOCK, "fisica"),
    "c02": (f"{K}/k02a.png", f"{K}/k02b.png",
        "Three backlit black silhouettes walk slowly towards the camera through subtle haze, "
        "in sync, dignified, the strong warm backlight blooming behind them, reflections "
        "stretching on the wet floor, colours barely appearing on the bottle edges as they "
        "get closer. Locked low camera. " + LOCK, "fisica"),
    "c03": (f"{K}/k03.png", None,
        "The orange character (Aji Crema) calmly adjusts the cuff of his tuxedo with his "
        "white glove, one small effortless movement, then holds still; his warm spotlight "
        "flickers on at the very start. Locked camera, subtle haze drifting. " + LOCK, None),
    "c04": (f"{K}/k04.png", None,
        "The yellow character (Mostaza) straightens his black bow tie with both white gloves "
        "in one slow confident movement, then lowers his hands and holds still; his warm "
        "spotlight flickers on at the very start. Locked camera, subtle haze. " + LOCK, None),
    "c05": (f"{K}/k05.png", None,
        "The red character (Ketchup) smooths the lapel of his tuxedo with one white glove in a "
        "dry precise movement, then stands very upright and still; his warm spotlight flickers "
        "on at the very start. Locked camera, subtle haze. " + LOCK, None),
    "c06": (f"{C}/master_trio.png", None,
        "The three characters stand perfectly still facing camera under their three warm "
        "spotlights, only a very subtle breathing movement and the haze slowly drifting, while "
        "the camera pushes in VERY slowly and smoothly on a dolly. " + LOCK, None),
    "c07": (f"{C}/master_trio.png", f"{K}/k07b.png",
        "THE REVEAL: the three characters raise their white gloves to their lapels at the same "
        "time and pull their tuxedo jackets wide open simultaneously in one decisive movement, "
        "revealing the real Traverso bottles and labels underneath, then hold the pose "
        "proudly. Locked frontal camera, spotlights steady. " + LOCK, "fisica"),
    "c09": (f"{K}/k09a.png", f"{K}/k09b.png",
        "Seen from behind, the three characters walk slowly and in sync away from the camera "
        "down the dark corridor towards the black door; when they arrive, the yellow one in "
        "the centre pushes the door and it opens, spilling warm daylight over them and the wet "
        "floor. Locked camera at hip height, 85mm. " + LOCK, "fisica"),
    "c11": (f"{K}/k11.png", None,
        "The three characters sit perfectly still at the meeting table like serious executives "
        "waiting for a meeting to start, hands resting on the table, only a faint breathing "
        "movement, steam rising softly from a coffee cup, warm natural light. Locked camera, "
        "nothing else moves. " + LOCK, None),
}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--solo", nargs="*"); ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--modelo", default="kling-v2-1-pro")
    a = ap.parse_args(); os.makedirs(OUT, exist_ok=True)
    for k in (a.solo or PLANOS):
        ini, fin, prompt, coda = PLANOS[k]
        out = os.path.join(OUT, f"{k}.mp4")
        if os.path.isfile(out) and not a.rehacer: print(f"· {k} ya existe"); continue
        for f in (ini, fin):
            if f and not os.path.isfile(f): sys.exit(f"✗ {k}: falta {f}")
        cmd = [sys.executable, VIDEO, ini, "--out", out, "--prompt", prompt, "--dur", "5", "--modelo", a.modelo]
        if fin: cmd += ["--fin", fin]
        if coda: cmd += ["--coda", coda]
        print(f"\n=== {k}"); subprocess.run(cmd, check=True)

if __name__ == "__main__": main()

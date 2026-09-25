#!/usr/bin/env python3
"""Recupera clips de Kling que el script principal dejó de esperar.

POR QUÉ EXISTE (24-09-2026): con la cola de Freepik lenta, `magnific-video.py`
cortó a los 15 min con las tareas todavía IN_PROGRESS. Las tareas NO se pierden:
siguen en el servidor y se cobran igual. Relanzarlas es pagar dos veces.

Este script consulta las tareas vivas de un modelo, espera a que terminen,
descarga cada video y lo asigna al plano cuyo PNG se parece más a su PRIMER
cuadro (el image-to-video parte exactamente del cuadro de entrada).

    python3 scripts/magnific-video-recuperar.py \
        --planos out/gcl/cap02-v3/planos --out out/gcl/cap02-v3/video \
        --solo P05 P07 P11a P11b P16 [--minutos 60]
"""
import argparse, json, os, ssl, subprocess, sys, tempfile, time, urllib.request
from pathlib import Path

import certifi
from PIL import Image, ImageChops, ImageStat

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import clave_freepik

CTX = ssl.create_default_context(cafile=certifi.where())
BASE = "https://api.freepik.com/v1/ai/image-to-video/"
RAIZ = Path(__file__).resolve().parent.parent
FF = RAIZ / "node_modules/@remotion/compositor-darwin-arm64"


def pedir(url):
    req = urllib.request.Request(url, headers={"x-freepik-api-key": clave_freepik(),
                                               "User-Agent": "copylab-estudio/1.0"})
    return json.loads(urllib.request.urlopen(req, context=CTX, timeout=60).read())


def primer_cuadro(mp4):
    png = tempfile.mktemp(suffix=".png")
    env = dict(os.environ, DYLD_LIBRARY_PATH=str(FF))
    subprocess.run([str(FF / "ffmpeg"), "-loglevel", "error", "-y", "-i", str(mp4),
                    "-frames:v", "1", png], env=env, check=True)
    return Image.open(png).convert("L").resize((90, 160))


def distancia(a, b):
    return sum(ImageStat.Stat(ImageChops.difference(a, b)).mean)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modelo", default="kling-v2-5-pro")
    ap.add_argument("--planos", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--solo", nargs="*", help="planos candidatos (por defecto todos los PNG)")
    ap.add_argument("--minutos", type=int, default=60)
    a = ap.parse_args()
    planos, out = Path(a.planos), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    nombres = a.solo or [p.stem for p in planos.glob("P*.png")]
    refs = {n: Image.open(planos / f"{n}.png").convert("L").resize((90, 160)) for n in nombres}

    vistos, limite = set(), time.time() + a.minutos * 60
    while time.time() < limite:
        tareas = pedir(BASE + a.modelo).get("data") or []
        vivas = [t for t in tareas if t.get("status") in ("CREATED", "IN_PROGRESS")]
        for t in tareas:
            tid = t.get("task_id")
            if t.get("status") != "COMPLETED" or tid in vistos or not t.get("generated"):
                continue
            vistos.add(tid)
            tmp = Path(tempfile.mktemp(suffix=".mp4"))
            urllib.request.urlretrieve(t["generated"][0], tmp)
            cuadro = primer_cuadro(tmp)
            mejor = min(refs, key=lambda n: distancia(cuadro, refs[n]))
            d = distancia(cuadro, refs[mejor])
            if d > 40:
                print(f"  · {tid[:8]} no calza con ningún plano (d={d:.0f}), se ignora")
                continue
            destino = out / f"{mejor}.mp4"
            if destino.exists():
                destino = out / f"{mejor}-{tid[:6]}.mp4"
            tmp.replace(destino)
            print(f"✓ {tid[:8]} → {destino.name} (d={d:.0f})", flush=True)
        if not vivas:
            break
        print(f"  … {len(vivas)} en cola", flush=True)
        time.sleep(30)


if __name__ == "__main__":
    main()

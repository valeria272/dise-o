#!/usr/bin/env python3
"""
Convierte material crudo de teléfono (HEIC + MOV) en fotos utilizables.

Por qué existe
--------------
Regla del estudio: **un frame en 4K es una foto**. Antes de generar una escena
con IA o de decir «falta la foto», se agota el material que el cliente ya tiene
— y muchas veces ese material es un video de iPhone.

Caso que lo motivó (01-09-2026): el 2.º piso de Between, que el cliente reclama
en el carrusel Cowork, **no está fotografiado, solo filmado**. Eli mandó 16 HEIC
y 25 MOV; de ahí salen los planos que faltaban.

Qué hace
--------
  · HEIC → JPG de calidad, conservando la resolución original.
  · MOV  → N fotogramas repartidos por el clip, **eligiendo los más nítidos**:
    de cada tramo saca varios candidatos y se queda con el de mayor varianza
    del laplaciano, que descarta los movidos.

Lee el video con **OpenCV**, no lanzando ffmpeg. ⚠️ En el Windows de Eli el
`ffmpeg.exe` que trae Remotion lo **bloquea una directiva de Control de
aplicaciones** (`WinError 4551`), así que depender de él no es portable. OpenCV
trae sus propios decodificadores compilados y no abre ningún subproceso.

Uso:
    python scripts/material-a-fotos.py <carpeta> [--salida DIR] [--por-video 3]
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent


def nitidez_arr(gris):
    g = gris.astype(np.float64)
    lap = g[1:-1, 1:-1]*4 - g[:-2, 1:-1] - g[2:, 1:-1] - g[1:-1, :-2] - g[1:-1, 2:]
    return float(np.var(lap))


def nitidez(p):
    im = Image.open(p).convert("L"); im.thumbnail((640, 640))
    return nitidez_arr(np.asarray(im))


def de_heic(p, dst):
    import pillow_heif
    pillow_heif.register_heif_opener()
    salida = dst / f"{p.stem}.jpg"
    if salida.exists():
        return salida, True
    im = Image.open(p).convert("RGB")
    im.save(salida, quality=94, optimize=True)
    return salida, False


def de_video(v, dst, cuantos, candidatos=5):
    """Reparte `cuantos` tomas por el clip y de cada una elige la MÁS NÍTIDA.

    De un video de mano, la mitad de los fotogramas salen movidos. Por cada
    toma se miran `candidatos` vecinos y gana el de mayor varianza del
    laplaciano: es la diferencia entre una foto usable y una borrosa.
    """
    import cv2
    cap = cv2.VideoCapture(str(v))
    if not cap.isOpened():
        return []
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total <= 0:
        cap.release(); return []

    hechos = []
    for i in range(cuantos):
        centro = int(total * (i + 0.5) / cuantos)
        mejor, mejor_n = None, -1
        for k in range(candidatos):
            idx = min(max(centro + (k - candidatos//2) * 4, 0), total - 1)
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ok, frame = cap.read()
            if not ok:
                continue
            gris = cv2.cvtColor(cv2.resize(frame, (0, 0), fx=0.25, fy=0.25), cv2.COLOR_BGR2GRAY)
            n = nitidez_arr(gris)
            if n > mejor_n:
                mejor, mejor_n = frame.copy(), n
        if mejor is not None:
            final = dst / f"{v.stem}-{i+1}.jpg"
            cv2.imwrite(str(final), mejor, [cv2.IMWRITE_JPEG_QUALITY, 94])
            hechos.append((final, mejor_n))
    cap.release()
    return hechos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--salida", default=None)
    ap.add_argument("--por-video", type=int, default=3)
    a = ap.parse_args()

    src = Path(a.carpeta)
    dst = Path(a.salida) if a.salida else src / "fotos"
    dst.mkdir(parents=True, exist_ok=True)

    heics = sorted(p for p in src.iterdir() if p.suffix.lower() in (".heic", ".heif"))
    videos = sorted(p for p in src.iterdir() if p.suffix.lower() in (".mov", ".mp4", ".m4v"))
    print(f"{len(heics)} HEIC · {len(videos)} videos → {dst}\n")

    for p in heics:
        salida, ya = de_heic(p, dst)
        im = Image.open(salida)
        print(f"  {p.name:22s} → {salida.name}  {im.size[0]}x{im.size[1]}{'  (ya estaba)' if ya else ''}")

    for v in videos:
        hechos = de_video(v, dst, a.por_video)
        if not hechos:
            print(f"  {v.name:22s} — no se pudo leer", file=sys.stderr); continue
        tam = Image.open(hechos[0][0]).size
        print(f"  {v.name:22s} → {len(hechos)} fotogramas  {tam[0]}x{tam[1]}  "
              f"nitidez {' '.join(str(int(n)) for _, n in hechos)}")

    print(f"\n{len(list(dst.glob('*.jpg')))} fotos en {dst}")


if __name__ == "__main__":
    main()

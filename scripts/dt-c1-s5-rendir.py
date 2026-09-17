#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · CARRUSEL S5 — rinde las láminas a MP4 con el nombre de entrega.

    python scripts/dt-c1-s5-rendir.py            # las 5 que se entregan
    python scripts/dt-c1-s5-rendir.py --gym      # incluye la lámina pendiente

⭐⭐ **RONDA 2 — «¿por qué se ve tan mal la calidad? Ideal 1080px o 2k».**

La ronda 1 salía a 1080×1350 y con DOS compresiones encadenadas: los clips ya
venían reescalados y comprimidos, y Remotion volvía a comprimir ese archivo.
Ahora:

  · los clips intermedios **no se reescalan** y salen a su tamaño nativo de
    recorte, 2160×2700, con CRF 16 (ver `dt-c1-s5-clips.py`);
  · la mesa sigue siendo de **1080** —toda la geometría de DT está medida ahí y
    no se toca— y se rinde con **`--scale 2`**, que da **2160×2700**;
  · el CRF final baja de 18 a **16**.

⚠️ `--scale` es el mismo mecanismo con el que se entregan las estáticas de esta
cuenta a 2250: se escala el LIENZO, no la geometría.

⛔⛔ **Y LA ESCALA TIENE QUE DAR UN ENTERO **PAR**. Costó dos intentos:

  · `--scale 1.3333` → `1350 × 1,3333 = 1799,955`. `stitchFramesToVideo` exige un
    entero. Y 4/3 exacto tampoco sirve: en coma flotante da 1800,0000000000002.
  · `--scale 1.5` → 2025, que es entero pero **impar**. H.264 necesita dimensión
    par, así que Remotion baja el alto a 1349 ANTES de escalar y termina pidiendo
    2023,5. El mensaje de error habla del alto final y no dice esto.

`--scale 2` es exacta en binario y da 2160×2700, los dos pares. Y entregar por
encima de lo que sirve Instagram no se desperdicia: la plataforma reduce a 1080 y
ese remuestreo se ve MEJOR que entregarle 1080 ya comprimido.

⚠️ Y una advertencia para mirar el resultado: **el reproductor de Drive
recomprime fuerte**. Para juzgar calidad hay que descargar el archivo.

⭐ El nombre lo fija cómo entrega el equipo, no nosotros: el carrusel de Piso18 de
la S5 subió como `C1 S5 N°1.png` dentro de `C1 S5 PISO18`, y el post de DT de la
S4 como `Post n°1 S4 DT.png`. El portal de validaciones **levanta por nombre** y
ordena por número, así que la numeración es el orden de las slides.
"""
import argparse
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "src/DtEntry.tsx"
SALIDA = RAIZ / "out/hilton/dt/c1-s5/entrega"

# composición → nombre de entrega. El orden es el orden del carrusel.
PIEZAS = [
    ("DT-V-S5-Portada",    "C1 S5 DT n°1.mp4"),
    ("DT-V-S5-Desayuno",   "C1 S5 DT n°2.mp4"),
    ("DT-V-S5-Salon",      "C1 S5 DT n°3.mp4"),
    ("DT-V-S5-Lobby",      "C1 S5 DT n°4.mp4"),
    # ⏸ Entre la n°4 y la n°5 va el GYM cuando contenido escriba su texto. Al
    # insertarlo hay que RENUMERAR: el cierre pasa a ser la n°6.
    ("DT-V-S5-Habitacion", "C1 S5 DT n°5.mp4"),
]
PENDIENTE = ("DT-V-S5-Gym", "PENDIENTE - C1 S5 DT gym (falta texto).mp4")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gym", action="store_true",
                    help="rinde también la lámina que NO se entrega")
    a = ap.parse_args()

    SALIDA.mkdir(parents=True, exist_ok=True)
    piezas = list(PIEZAS) + ([PENDIENTE] if a.gym else [])
    npx = "npx.cmd" if sys.platform == "win32" else "npx"

    for comp, nombre in piezas:
        destino = SALIDA / nombre
        print(f"→ {comp}  →  {nombre}")
        r = subprocess.run(
            [npx, "remotion", "render", str(ENTRADA), comp, str(destino),
             "--codec=h264",
             "--scale=2",                 # 1080×1350 → 2160×2700 (ver cabecera)
             # Instagram recomprime igual, pero entregarle un archivo limpio
             # evita sumar generaciones de artefactos.
             "--crf=16",
             "--pixel-format=yuv420p",
             "--log=error"],
            cwd=RAIZ, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            print(f"  ⛔ falló {comp}")
            return 1
        print(f"  ✅ {destino.stat().st_size / 1e6:.1f} MB")
    print(f"\nEntrega en {SALIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

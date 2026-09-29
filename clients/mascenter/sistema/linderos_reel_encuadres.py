"""Encuadres del reel horizontal Más Center Linderos (brief BRIEF_MasCenter_Linderos_v2).

Saca de los renders oficiales (4160×2340, sin pasar por IA) las imágenes de inicio
que se animan en Wan 3.0. Los prompts de cada escena están en `linderos-reel-prompts.md`.

    ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/linderos_reel_encuadres.py

Fuentes (gitignored, en raw/): los renders los pasó Diego en el chat del 29-09-2026;
el aéreo es el de mascenter.cl/linderos.
"""
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parents[3]
REFS = RAIZ / "raw/mascenter/linderos-reel/refs"
OUT = RAIZ / "out/mascenter/linderos"

# (archivo de salida, render de origen, caja en px del original 4160×2340 o None = entero)
ENCUADRES = [
    ("escena2/2A-render-completo-1920.jpg", "render-aereo-linderos-4160.png", None),
    # enlace Ruta 5 + rotonda + Hermanos Carrera + tótem Unimarc ENTERO (la caja
    # x 2080–4160 lo cortaba y se leía «MARC»)
    ("escena2/2B-recorte-nodo-ruta5-1920.jpg", "render-aereo-linderos-4160.png", (1780, 190, 4160, 1529)),
    ("cierre/C1-render-fachada-1920.jpg", "render-fachada-linderos-4160.png", None),
]


def main() -> None:
    for salida, origen, caja in ENCUADRES:
        im = Image.open(REFS / origen).convert("RGB")
        if caja:
            im = im.crop(caja)
        destino = OUT / salida
        destino.parent.mkdir(parents=True, exist_ok=True)
        im.resize((1920, 1080), Image.LANCZOS).save(destino, quality=95)
        print(f"{salida}  ←  {origen} {caja or '(entero)'}")


if __name__ == "__main__":
    main()

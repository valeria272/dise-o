#!/usr/bin/env python3
"""Tierra Calma · noviembre 2026 — logos de los supermercados del reel del 19-11, en blanco.

    python scripts/tc-nov-logos.py

Constanza Lizana, 02-10: *«en este reel añadiría los logos de Tottus, Santa Isabel y
Líder Express. Quizás en variante blanca, pero así será más llamativo»*.

Los logos NO se dibujan ni se generan: se bajan los SVG oficiales de Wikimedia
Commons, se rasterizan con Chrome sobre blanco y se pasan a una sola tinta blanca.
Lo que en el original es blanco (las letras dentro del disco de Santa Isabel y del
sello de Express) queda CALADO, transparente: `brightness(0) invert(1)` a secas
los dejaba como una mancha sin nombre.

`tono` = el logo conserva sus planos como niveles de opacidad (el filete verde y la
banda celeste del sello de Express quedan más livianos que el cuerpo azul). Sin
`tono` va todo a blanco pleno.

Salida: public/assets/tierracalma/nov/logos/<id>.png (recortado al dibujo).
"""
import pathlib
import subprocess
import sys
import tempfile
import urllib.request

import numpy as np
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "public/assets/tierracalma/nov/logos"
CHROME = pathlib.Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CopylabStudio/1.0"
COMMONS = "https://upload.wikimedia.org/wikipedia/commons/"

# id → (ruta en Commons, ancho de rasterizado, alto, tono)
LOGOS = {
    "tottus": ("c/c8/Logotipo_Tottus.svg", 3000, 549, False),
    "santa-isabel": ("d/dd/Santa_Isabel.svg", 1200, 1200, False),
    "lider-express": ("3/32/Express_de_Lider_2025.svg", 2410, 1206, True),
}


def rasterizar(svg: pathlib.Path, w: int, h: int, png: pathlib.Path) -> None:
    html = svg.with_suffix(".html")
    html.write_text(
        f'<html><body style="margin:0;background:#fff"><img src="{svg.name}" width="{w}" height="{h}"></body></html>',
        encoding="utf-8",
    )
    subprocess.run(
        [str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars",
         f"--window-size={w},{h}", f"--screenshot={png.as_posix()}", html.as_uri()],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def a_blanco(png: pathlib.Path, tono: bool) -> Image.Image:
    a = np.asarray(Image.open(png).convert("RGB")).astype(float)
    if tono:
        # Opacidad por luminancia: el plano más oscuro del logo queda pleno.
        lum = a @ np.array([0.299, 0.587, 0.114])
        alfa = np.clip((255 - lum) / (255 - np.percentile(lum, 20)), 0, 1)
    else:
        # Todo lo que no es blanco va a blanco pleno; el borde conserva su suavizado.
        alfa = np.clip((255 - a.min(axis=2)) / 120, 0, 1)
    rgba = np.dstack([np.full(alfa.shape + (3,), 255.0), alfa * 255]).astype(np.uint8)
    img = Image.fromarray(rgba, "RGBA")
    return img.crop(img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())


def main() -> None:
    DESTINO.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        for pid, (ruta, w, h, tono) in LOGOS.items():
            svg = tmp / f"{pid}.svg"
            req = urllib.request.Request(COMMONS + ruta, headers={"User-Agent": UA})
            svg.write_bytes(urllib.request.urlopen(req).read())
            png = tmp / f"{pid}.png"
            rasterizar(svg, w, h, png)
            img = a_blanco(png, tono)
            img.save(DESTINO / f"{pid}.png")
            print(f"  ✓ {pid}.png  {img.width}×{img.height}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()

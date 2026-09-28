"""Pone el isotipo de Más Center (la flecha del logo oficial, en rojo #DC1914) dentro del círculo crema de la panza
de Localito en las ilustraciones generadas, que la IA deja vacío. El isotipo sale de los dos últimos <path> de
assets/logo-mascenter-blanco.svg, se rasteriza con Chrome y se pega centrado en el círculo, que se ubica buscando
la mancha crema casi circular más cercana al punto aproximado (medido a ojo en la vista a 1/3).

Uso: ~/copylab-venv/Scripts/python.exe clients/mascenter/sistema/localito_ilustrado.py
"""
import re, subprocess
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
D = RAIZ / "out/mascenter/2026-10/carrusel-20-10/fotos"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
# (archivo, centro aproximado en px de la imagen 1770×2360)
PANZAS = [("01-portada", (1131, 1690)), ("02-detinmarin", (855, 1240)), ("03-klab", (1356, 1263))]


def isotipo(lado=600):
    svg = (AQUI / "assets/logo-mascenter-blanco.svg").read_text(encoding="utf-8")
    d = re.findall(r'd="([^"]+)"', svg)[-2:]
    doc = (f'<html><body style="margin:0;background:transparent"><svg xmlns="http://www.w3.org/2000/svg" '
           f'viewBox="249 12 100 144" width="{lado}" height="{lado * 144 // 100}">'
           + "".join(f'<path fill="#DC1914" d="{x}"/>' for x in d) + "</svg></body></html>")
    h = D / "_isotipo.html"; h.write_text(doc, encoding="utf-8")
    png = D / "_isotipo.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
                    f"--window-size={lado},{lado * 144 // 100}", f"--screenshot={png.as_posix()}", h.as_uri()], check=True, capture_output=True)
    im = Image.open(png).convert("RGBA")
    return im.crop(im.getbbox())


def circulo(a, cx, cy, radio_busqueda=260):
    y0, x0 = max(0, cy - radio_busqueda), max(0, cx - radio_busqueda)
    r = a[y0:cy + radio_busqueda, x0:cx + radio_busqueda].astype(int)
    crema = (r.min(2) > 150) & (r[..., 0] - r[..., 2] < 100)
    crema = ndimage.binary_opening(crema, iterations=3)
    lab, n = ndimage.label(crema)
    k = lab[cy - y0, cx - x0]
    if not k:
        dist = ndimage.distance_transform_edt(lab == 0, return_indices=True)[1]
        k = lab[tuple(dist[:, cy - y0, cx - x0])]
    ys, xs = np.where(lab == k)
    return x0 + xs.min(), y0 + ys.min(), x0 + xs.max(), y0 + ys.max()


if __name__ == "__main__":
    iso = isotipo()
    for nombre, (cx, cy) in PANZAS:
        im = Image.open(D / f"{nombre}.png").convert("RGB")
        x0, y0, x1, y1 = circulo(np.asarray(im), cx, cy)
        w = x1 - x0
        print(nombre, (x0, y0, x1, y1), "ancho", w)
        s = iso.copy(); s.thumbnail((int(w * 0.52), int(w * 0.62)), Image.LANCZOS)
        im.paste(s, (int((x0 + x1) / 2 - s.width / 2 + w * 0.03), int((y0 + y1) / 2 - s.height / 2)), s)
        im.save(D / f"{nombre}-logo.png")

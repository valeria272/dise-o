#!/usr/bin/env python3
"""CAVA — monta el bodegón del KV como la referencia real de la diseñadora.

QUÉ SE MIDIÓ (28-08-2026) sobre `raw/cava/ref-sept2026/KV_FIESTAS_PATRIAS_2025.png`
------------------------------------------------------------------------------------
El KV entregado se leía como collage. Comparando la nitidez por franjas contra el
KV real de la diseñadora aparecieron TRES diferencias, y la primera es la gorda:

1. ⭐ **EL FONDO NO PUEDE COMPETIR EN NITIDEZ CON EL PRODUCTO.**
   En la referencia el fondo marca 1,4–3,0 de nitidez y las botellas 7–9: el
   viñedo y el barril están deshechos en bokeh y lo único enfocado es el vino.
   En el nuestro pasaba al revés — el barril del fondo marcaba 8,8 y las botellas
   5,9. El ojo lee dos fotos pegadas, y ninguna cantidad de sombra lo arregla.
   Es cómo se fotografía un bodegón de verdad: teleobjetivo, diafragma abierto,
   el fondo se va.

2. **Las botellas iban chicas.** La referencia las tiene al **52 % del alto** de
   la pieza (manual §11: «si la botella no llega a la mitad, está chica»). Las
   nuestras quedaban al 36 % porque se dimensionaban contra el diámetro de la
   tapa del barril, y el barril salía grande.

3. **El grupo ocupa el 72 % del ancho** y se centra en x≈1198 sobre 2250 — algo a
   la derecha del centro del lienzo.

Lo que NO cambia: las botellas son bottle shots oficiales y no se tocan
(`clients/cava/CLAUDE.md` §2). La luz se integra con capas, nunca redibujando —
ver `scripts/cava-integrar-luz.py` y la prueba fallida en `cava-prueba-relight.py`.

Uso:
    python3 scripts/cava-kv-realista.py [--fondo kv-fiestas-01.png]
"""
import argparse
import importlib.util
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "out", "cava", "kv-realista")

# ── Medidas de la referencia, en fracción de la pieza ────────────────────
ALTO_BOTELLA   = 0.519      # 1459/2813 — manual §11
BASE_BOTELLAS  = 0.880      # dónde apoya el grupo
# La referencia mide 0,723, pero ella trabaja con botellas LIMPIAS del SharePoint
# de la viña. Las nuestras son del e-commerce y traen el SELLO DE PUNTAJE
# incrustado sobre el hombro: a 0,723 los sellos de botellas contiguas se pisan y
# el grupo se lee como una fila de medallas. Se abre a 0,80 — es apartarse de la
# medida por una limitación del material, no por gusto.
ANCHO_GRUPO    = 0.800
CENTRO_GRUPO   = 0.532      # 1198/2250 — no es el centro exacto
CURVA_APOYO    = 0.018      # la del centro apoya un pelo más abajo: la tapa es
                            # elipse. Sutil, porque el barril va desenfocado.


def desenfoque_por_profundidad(fondo, y_apoyo, radio_lejos=13.0, radio_cerca=2.0):
    """Bokeh progresivo: lo lejano se deshace, el plano de apoyo queda casi nítido.

    Una sola pasada de blur uniforme se ve a plástico. Lo que hace una lente es
    desenfocar en función de la DISTANCIA, así que se interpola entre varias
    versiones borrosas según la altura: arriba (horizonte) el radio máximo, en el
    plano donde apoyan las botellas el mínimo, y de ahí abajo vuelve a subir
    suave — el borde delantero del barril también está fuera de foco.
    """
    w, h = fondo.size
    niveles = 5
    capas = [fondo.filter(ImageFilter.GaussianBlur(
        radio_cerca + (radio_lejos - radio_cerca) * (i / (niveles - 1)) ** 1.15))
        for i in range(niveles)]

    # perfil de "cuánto blur" por fila: 1 = máximo, 0 = mínimo
    ys = np.arange(h) / h
    d = np.abs(ys - y_apoyo)
    perfil = np.clip(d / max(y_apoyo, 1e-6), 0, 1) ** 0.75
    perfil = np.where(ys > y_apoyo, np.clip(d / 0.30, 0, 1) ** 1.1 * 0.75, perfil)

    salida = capas[0].copy()
    for i in range(1, niveles):
        lo, hi = (i - 1) / (niveles - 1), i / (niveles - 1)
        m = np.clip((perfil - lo) / (hi - lo), 0, 1) * 255
        mask = Image.fromarray(m.astype(np.uint8)[:, None].repeat(w, axis=1), "L")
        salida = Image.composite(capas[i], salida, mask)
    return salida


def carga(nombre):
    ruta = os.path.join(RAIZ, "scripts", nombre)
    spec = importlib.util.spec_from_file_location(nombre.replace("-", "_")[:-3], ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(RAIZ, "scripts"))
    spec.loader.exec_module(mod)
    return mod


def sombra(lienzo, cx, y, ancho, fuerza=1.0):
    """Dos sombras: la mancha de contacto dura y pequeña, y una difusa más ancha.
    Con una sola, o flota (si es suave) o parece un sticker (si es dura)."""
    for rx_f, ry_f, alfa, blur_f in ((0.46, 0.100, 185, 0.055),
                                     (0.95, 0.200, 85, 0.230)):
        capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
        rx, ry = ancho * rx_f, max(ancho * ry_f, 8)
        ImageDraw.Draw(capa).ellipse([cx - rx, y - ry, cx + rx, y + ry],
                                     fill=(26, 13, 5, int(alfa * fuerza)))
        lienzo.alpha_composite(capa.filter(
            ImageFilter.GaussianBlur(max(ancho * blur_f, 3))))


def monta(fondo_png, botellas, W=2250, H=2813, con_luz=True):
    il = carga("cava-integrar-luz.py")

    f = Image.open(os.path.join(RAIZ, "public", "assets", "cava", "kv",
                                fondo_png)).convert("RGB")
    # encuadre: se recorta al alto de la pieza sin deformar
    esc = max(W / f.width, H / f.height)
    f = f.resize((round(f.width * esc), round(f.height * esc)), Image.LANCZOS)
    f = f.crop(((f.width - W) // 2, 0, (f.width - W) // 2 + W, H))

    y_base = H * BASE_BOTELLAS
    f = desenfoque_por_profundidad(f, BASE_BOTELLAS)
    kv = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    kv.alpha_composite(f.convert("RGBA"))

    alto_bot = round(H * ALTO_BOTELLA)
    n = len(botellas)
    x0 = W * CENTRO_GRUPO - W * ANCHO_GRUPO / 2
    x1 = W * CENTRO_GRUPO + W * ANCHO_GRUPO / 2

    puestas = []
    for i, nombre in enumerate(botellas):
        # las 2x salen del upscaler DE PRECISIÓN (scripts/cava-botellas-2x.py):
        # así la botella se REDUCE para llegar a 1459 px en vez de ampliarse, y
        # el producto queda más nítido que el fondo, como en la referencia
        dosx = os.path.join(RAIZ, "public", "assets", "cava", "bottles", "2x",
                            nombre + ".png")
        base = dosx if os.path.isfile(dosx) else os.path.join(
            RAIZ, "public", "assets", "cava", "bottles", nombre + ".png")
        shot = Image.open(base).convert("RGBA")
        shot = shot.crop(shot.split()[-1].getbbox())
        cx = x0 + (x1 - x0) * ((i + 0.5) / n)
        anc = round(alto_bot * shot.width / shot.height)
        dx = (cx - W * CENTRO_GRUPO) / (W * ANCHO_GRUPO / 2)
        y = y_base + H * CURVA_APOYO * (1 - min(abs(dx), 1.0) ** 2)
        puestas.append((shot, cx, y, alto_bot, anc))

    for shot, cx, y, alto, anc in puestas:
        sombra(kv, cx, y, anc)
    # de los costados al centro: la del medio queda delante, como en la referencia
    for shot, cx, y, alto, anc in sorted(puestas, key=lambda p: -abs(p[1] - W / 2)):
        b = shot.resize((anc, alto), Image.LANCZOS)
        if con_luz:
            b = il.integra_luz(b, fuerza=0.75)
        kv.alpha_composite(b, (int(cx - anc / 2), int(y - alto)))
    return kv.convert("RGB")


def nitidez(im):
    a = np.asarray(im.convert("L"), dtype=float)
    lap = np.abs(np.diff(a, 2, axis=0))[:, ::4]
    fl = lap.shape[0]
    return [lap[int(fl * i / 10):int(fl * (i + 1) / 10)].mean() for i in range(10)]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fondo", default="kv-fiestas-01.png")
    a = p.parse_args()
    os.makedirs(SALIDA, exist_ok=True)

    botellas = ["edicion-limitada-carmenere", "7colores-limited-carmenere",
                "vitis-unica-cabernet", "seleccion-vinedos-gr-cabernet"]

    print("→ Montando el bodegón con las medidas de la referencia…")
    kv = monta(a.fondo, botellas)
    ruta = os.path.join(SALIDA, "kv-bodegon.png")
    kv.save(ruta)
    print(f"   {kv.width}×{kv.height} → {ruta}")

    ref = Image.open(os.path.join(RAIZ, "raw", "cava", "ref-sept2026",
                                  "KV_FIESTAS_PATRIAS_2025.png")).convert("RGB")
    print("\n  NITIDEZ por franja — el fondo NO debe superar al producto")
    print("  franja:      " + " ".join(f"{i*10:>5}" for i in range(10)))
    for et, im in (("referencia ", ref), ("nuestro    ", kv)):
        print(f"  {et} " + " ".join(f"{v:5.1f}" for v in nitidez(im)))
    nr, nn = nitidez(ref), nitidez(kv)
    print(f"\n  fondo (0–50%)   referencia {sum(nr[:5])/5:5.2f}   nuestro {sum(nn[:5])/5:5.2f}")
    print(f"  producto (60–80%) referencia {sum(nr[6:8])/2:5.2f}   nuestro {sum(nn[6:8])/2:5.2f}")

    h = 900
    ims = [ref, kv]
    esc = [i.resize((round(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    comp = Image.new("RGB", (sum(i.width for i in esc) + 20, h + 30), (255, 255, 255))
    d = ImageDraw.Draw(comp)
    x = 0
    for i, et in zip(esc, ["REFERENCIA de la disenadora", "NUESTRO bodegon"]):
        comp.paste(i, (x, 30)); d.text((x + 8, 9), et, fill=(0, 0, 0))
        x += i.width + 20
    rc = os.path.join(SALIDA, "_vs-referencia.jpg")
    comp.save(rc, quality=93)
    print(f"\n✓ {rc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOUBLETREE · OCTUBRE 2026, tanda del 02-10 — prepara las dos fotos de la ST Noche de Bodas.

Las dos las dejó contenido enlazadas en el brief (STORIES!H10, hilo de Carlos del 02-10):
  foto 1 · rosas + espumante  (Drive 18kiN1wv3GtwObjYdVF7oi48F1RvlIut8, PNG 1024×1536)
  foto 2 · tina con pétalos   (Drive 1pd-en6T5RR1SinWEao-JLK9oI9yxjXZM, JPG 6000×4005)

La foto 1 llega a 1024 px y en la pieza se muestra a ~2530 px de ancho: se sube ANTES con el
escalador de PRECISIÓN (no el creativo, que redibuja):
    python scripts/magnific.py escalar raw/hilton/dt/ref-oct6/nb-foto1-rgb.png \
        --out raw/hilton/dt/ref-oct6/nb-foto1-2x.png --precision --escala 2x
"""
import pathlib
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REF = RAIZ / "raw/hilton/dt/ref-oct6"
OUT = RAIZ / "public/assets/hilton/dt/oct6"
OUT.mkdir(parents=True, exist_ok=True)

# El escalador de precisión deja el ramo CRUJIENTE (grano en los pétalos y filo amarillo en el canto de las
# rosas, visto al 100 %). Se mezcla a medias con la original subida por Lanczos: queda el detalle sin el halo.
fina = Image.open(REF / "nb-foto1-2x.png").convert("RGB")
suave = Image.open(REF / "nb-foto1-rgb.png").convert("RGB").resize(fina.size, Image.LANCZOS)
rosas = Image.blend(suave, fina, 0.45)
rosas.save(OUT / "nb-rosas.jpg", quality=93, subsampling=0)
print("nb-rosas.jpg", rosas.size)

# RONDA 2 (Eli, 02-10): la toma es el conjunto completo, con la botella y las copas servidas. Sale de
# `scripts/dt-oct6-nb-brindis.py`: la tirada 6 (copas servidas, sin lámpara) pegada a medida en un lienzo y la
# tirada 8, donde la IA sólo continuó la pared y la mesa. Así el conjunto cabe entero bajo el titular.
brindis = Image.open(REF / "nb-brindis-v8.png").convert("RGB").resize((2800, 2800), Image.LANCZOS)
# La tirada salió con la pared hacia el magenta: R:G:B 150·103·98 contra 144·111·92 de la foto de contenido.
# Se le devuelve el verde (×1,08, el 70 % de la diferencia) para que la pared vuelva al beige de la habitación.
r, g, b = brindis.split()
brindis = Image.merge("RGB", (r, g.point(lambda x: min(255, round(x * 1.08))), b))
brindis.save(OUT / "nb-brindis.jpg", quality=93, subsampling=0)
print("nb-brindis.jpg", brindis.size)

tina = Image.open(REF / "nb-foto2.jpg").convert("RGB")
tina = tina.resize((3600, round(3600 * tina.height / tina.width)), Image.LANCZOS)
tina.save(OUT / "nb-tina.jpg", quality=93, subsampling=0)
print("nb-tina.jpg", tina.size)

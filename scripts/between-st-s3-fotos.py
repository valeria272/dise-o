#!/usr/bin/env python3
"""Deja listas las tres fotos de las STORIES de la S3 (14, 16 y 18-09).

⭐ RONDA 2 · 08-09-2026 — este script se reescribió entero.

En la ronda 1 las tres fotos salían de RECORTAR el banco 4:5 a 9:16, y Eli las
devolvió: «no cumplen, debes dejar mejores fotografías, mejor imagenes hazlo en
conjunto a magnific». Tenía razón, y el diagnóstico es uno solo: **una foto de
banco recortada no deja el hueco que la diagramación necesita**, así que el texto
terminaba apoyado en cajas taupe y las tres piezas se parecían entre sí. Sus tres
referentes hacen lo contrario — la foto está PRODUCIDA con el hueco adentro.

Ahora las escenas se GENERAN (`scripts/between-st-s3-generar.py`, método de Eli:
Nano Banana Pro + las fotos reales como referencia) y este script sólo hace el
trabajo de laboratorio que la IA no debe hacer:

  1. **14-09 — el sweater al café de marca.** El generador entregó un café
     `#564134`, más rojo y más oscuro que el `#675B49` de Between. Se corrige con
     una GANANCIA MULTIPLICATIVA por canal aplicada sólo al sweater: multiplicar
     conserva la textura del tejido y sus pliegues, mientras que sumar un offset
     lo aplana y el sweater se ve de plástico. La máscara es blanda y por
     luminancia — el sweater tiene su canal más alto en ~86 de 255 y la piel en
     ~215, así que se separan solos, sin recortar a mano.
  2. **16-09 — fuera el logotipo del notebook.** La escena llegó con la marca de
     un computador en la tapa. En una pieza de cliente no va la marca de un
     tercero, y el referente de Eli tampoco la lleva. Se borra con la
     interpolación horizontal de `between-quitar-kimbo.py`, que es lo correcto
     acá: la tapa es un degradado liso, así que la recta entre sus dos costados
     ES la superficie.
  3. **Las tres — el encuadre final a 2250×4000.** Nano Banana devuelve
     3072×5504, que da 0,558 y no 0,5625: sobran 43 px de alto. Se quitan del
     lado que no mueve al sujeto y después se REDUCE (×0,73). Ninguna se amplía.

Uso:
    python scripts/between-st-s3-fotos.py
    python scripts/between-st-s3-fotos.py --revisar    # deja los QA con zoom
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

Image.MAX_IMAGE_PIXELS = None

# ⚠️ Windows: la consola escribe en cp1252 y un «✓» reventaba el script DESPUÉS
# de haber hecho el trabajo. Mismo patrón que el resto de los scripts del estudio.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "raw/hilton/between/st-s3"
DESTINO = RAIZ / "public/assets/hilton/between/st-s3"

SALIDA = (2250, 4000)  # el master de Eli: 1080×1920 × 2,0833

#: El café de marca, en RGB. Es el objetivo de la corrección del sweater.
CAFE_MARCA = np.array([0x67, 0x5B, 0x49], dtype=np.float32)

#: Caja del logotipo del notebook en `gen-16-09-cowork.png`, medida sobre la tapa.
#: Generosa a propósito: mejor sobrar aluminio liso que dejar asomando un trozo.
LOGO_NOTEBOOK = (2586, 2760, 2716, 3000)

#: Las tres escenas. `recorte_alto` dice de dónde se quitan los px que sobran
#: para dar 9:16 exacto: 'arriba' cuando el sujeto está abajo (así no se mueve),
#: 'abajo' cuando está arriba.
ESCENAS = {
    "st-14-09-hora-cafe.jpg": {
        "fuente": "gen-14-09-taza-sostenida.png",
        "recorte_alto": "arriba",
        "sweater_a_cafe": True,
    },
    "st-16-09-cowork.jpg": {
        "fuente": "gen-16-09-cowork.png",
        "recorte_alto": "abajo",
        "borrar": [LOGO_NOTEBOOK],
    },
    # RONDA 3: el brindis fotográfico sale y entra AMBIENTE puro, porque el
    # brindis pasó a ser DIBUJO dentro del cartel — que es lo que hace la REF 3.
    "st-18-09-dieciocho.jpg": {
        "fuente": "gen-18-09-ambiente.png",
        "recorte_alto": "abajo",
    },
}


def borra_por_interpolacion(im, caja, apoyo=24):
    """Rellena la caja interpolando entre las columnas limpias de sus dos costados.

    Método ya probado en `between-quitar-kimbo.py`. Sirve cuando la superficie es
    un degradado suave: la recta que une los dos costados ES la superficie, así
    que no queda empalme. NO se clona una franja vecina: en una superficie con
    degradado lateral el parche llega con otra luminancia y deja un rectángulo.
    """
    x0, y0, x1, y1 = caja
    if not (apoyo <= x0 and x1 + apoyo <= im.width and 0 <= y0 <= y1 <= im.height):
        sys.exit(f"la caja {caja} no deja {apoyo} px de apoyo dentro de {im.size}")
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    izq = a[y0:y1, x0 - apoyo:x0].mean(axis=1)
    der = a[y0:y1, x1:x1 + apoyo].mean(axis=1)
    ancho = x1 - x0
    t = np.linspace(0.0, 1.0, ancho, dtype=np.float32)[None, :, None]
    a[y0:y1, x0:x1] = izq[:, None, :] * (1 - t) + der[:, None, :] * t
    fuera = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

    # Los cantos se funden con un difuminado PROPORCIONAL al ancho de la marca.
    # Nunca fijo: un inset fijo se come el borde cuando la marca es chica.
    m = max(6, int(0.30 * ancho))
    zx0, zy0 = max(0, x0 - m), max(0, y0 - m)
    zx1, zy1 = min(fuera.width, x1 + m), min(fuera.height, y1 + m)
    zona = fuera.crop((zx0, zy0, zx1, zy1))
    suave = zona.filter(ImageFilter.GaussianBlur(m / 3.0))
    mask = Image.new("L", zona.size, 0)
    ImageDraw.Draw(mask).rectangle([m, m, mask.width - m, mask.height - m], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(m / 2.0))
    fuera.paste(Image.composite(suave, zona, mask), (zx0, zy0))
    print(f"  · marca borrada: caja {caja} · apoyo {apoyo} · difuminado {m}")
    return fuera


#: Rectángulo de MEDICIÓN del sweater en `gen-14-09-taza-sostenida.png`
#: (x0, y0, x1, y1). Es tejido limpio y bien iluminado, sin piel, sin taza y sin
#: los pliegues profundos de los costados.
#:
#: ⚠️ La ganancia se calcula acá y NO sobre toda la máscara. La primera pasada la
#: calculó contra el promedio de los píxeles con peso 1 —que son el 67 % del
#: cuadro e incluyen las sombras profundas del tejido— y ese promedio da `#412f25`:
#: llevarlo a `#675B49` pedía una ganancia de ×1,57–1,97 y reventaba los medios.
#: El color de una prenda es su MEDIO TONO, no el promedio con sus sombras.
MUESTRA_SWEATER = (700, 900, 2400, 2600)


def sweater_al_cafe(im):
    """Lleva el sweater del 14-09 al café `#675B49` sin tocar piel ni taza."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    maxc = a.max(axis=2)
    # Máscara blanda por luminancia: el tejido está en Rmax≈86 y la piel en ≈215.
    w = np.clip((150.0 - maxc) / 60.0, 0.0, 1.0)[:, :, None]

    mx0, my0, mx1, my1 = MUESTRA_SWEATER
    med = a[my0:my1, mx0:mx1].reshape(-1, 3).mean(axis=0)
    gan = CAFE_MARCA / med
    hexmed = "#%02x%02x%02x" % tuple(int(v) for v in med)
    print(f"  · sweater medido {hexmed} → objetivo #675b49 · ganancia "
          f"{gan.round(3)} · máscara con peso 1 en {(w[:, :, 0] > 0.98).mean() * 100:.1f} %")

    a = a * (1 - w) + (a * gan) * w
    fin = np.clip(a, 0, 255).astype(np.uint8)
    nuevo = fin[my0:my1, mx0:mx1].reshape(-1, 3).astype(np.float32).mean(axis=0)
    hexnew = "#%02x%02x%02x" % tuple(int(v) for v in nuevo)
    print(f"  · sweater quedó  {hexnew}")
    return Image.fromarray(fin)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true",
                    help="guarda recortes con zoom de los retoques")
    a = ap.parse_args()

    DESTINO.mkdir(parents=True, exist_ok=True)
    for nombre, e in ESCENAS.items():
        src = FUENTES / e["fuente"]
        if not src.is_file():
            sys.exit(f"falta {src}\n"
                     f"  Se genera con: python scripts/between-st-s3-generar.py")
        print(f"{nombre}  <-  {e['fuente']}")
        im = Image.open(src).convert("RGB")

        if e.get("sweater_a_cafe"):
            if a.revisar:
                im.crop((300, 900, 1500, 1900)).save(
                    FUENTES / "_qa-sweater-antes.jpg", quality=94)
            im = sweater_al_cafe(im)
            if a.revisar:
                im.crop((300, 900, 1500, 1900)).save(
                    FUENTES / "_qa-sweater-despues.jpg", quality=94)

        for caja in e.get("borrar", []):
            if a.revisar:
                z = im.crop((caja[0] - 150, caja[1] - 150, caja[2] + 150, caja[3] + 150))
                z.resize((z.width * 2, z.height * 2), Image.LANCZOS).save(
                    FUENTES / "_qa-notebook-antes.jpg", quality=94)
            im = borra_por_interpolacion(im, caja)
            if a.revisar:
                z = im.crop((caja[0] - 150, caja[1] - 150, caja[2] + 150, caja[3] + 150))
                z.resize((z.width * 2, z.height * 2), Image.LANCZOS).save(
                    FUENTES / "_qa-notebook-despues.jpg", quality=94)

        # El alto que sobra para dar 9:16 exacto, quitado del lado que no mueve
        # al sujeto.
        alto_916 = int(round(im.width / 0.5625))
        sobra = im.height - alto_916
        if sobra < 0:
            sys.exit(f"{nombre}: la fuente {im.size} es MAS ANGOSTA que 9:16")
        y0 = sobra if e["recorte_alto"] == "arriba" else 0
        rec = im.crop((0, y0, im.width, y0 + alto_916))

        if rec.width < SALIDA[0]:
            sys.exit(f"{nombre}: la ventana ({rec.width}) es mas chica que la "
                     f"entrega ({SALIDA[0]}): saldria ampliada.")
        rec = rec.resize(SALIDA, Image.LANCZOS)
        dst = DESTINO / nombre
        rec.save(dst, quality=95, subsampling=1)
        print(f"  ok {im.size[0]}x{im.size[1]} -> recorte {im.width}x{alto_916}"
              f" (-{sobra} px {e['recorte_alto']}) -> {SALIDA[0]}x{SALIDA[1]}"
              f"  reduccion x{SALIDA[0] / im.width:.2f}\n")


if __name__ == "__main__":
    main()

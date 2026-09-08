#!/usr/bin/env python3
"""Las tres fotos de las STORIES de la S3 de septiembre (14, 16 y 18-09).

⭐ 08-09-2026. La grilla pide tres historias y las tres son ESTÁTICAS con foto
de fondo. El banco de Between está en 4:5 (2250×2812) y la historia es 9:16, así
que hay un problema real de encuadre: **al recortar 4:5 a 9:16 se conserva todo
el alto y se corta el ancho**, o sea que el sujeto NO se mueve de altura. En las
tres fotos el sujeto cae justo en la franja donde va el sticker de Instagram.

La salida no es estirar (`docs/SISTEMA-DE-MARCAS.md` y la skill de dirección de
arte lo prohíben: en la story de Revex Las Condes las rayas verticales ocuparon
el 34 % de la pieza). La salida es **subir la foto a 2× con el upscaler que ya
pagamos y recortar con holgura**:

    python scripts/magnific.py escalar <foto> --out raw/hilton/between/st-s3/<foto>-2x.png --escala 2x

Con la fuente a 4496×5624 se puede recortar una ventana de 9:16 MÁS CHICA que el
alto total, y ahí sí se elige a qué altura queda el sujeto. Las tres ventanas de
abajo salen a 2250×4000 **reduciendo**, nunca ampliando.

⛔ Y el KIMBO. `desayuno-completo-2.jpg` es la única de las tres con taza de loza
en 45°, así que trae el wordmark del proveedor que el cliente lleva pidiendo
sacar desde la ronda 4 («ya no servimos en esas tazas»). Se borra con el mismo
método de `between-quitar-kimbo.py` —interpolación horizontal entre el esmalte
limpio de los dos costados, NO clonado, porque la taza tiene degradado lateral y
un parche clonado deja un rectángulo visible—. La caja se midió sobre la imagen
a 2× buscando los píxeles rojos, no a ojo.

Uso:
    python scripts/between-st-s3-fotos.py
    python scripts/between-st-s3-fotos.py --revisar   # además deja los QA con zoom
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

#: Cajas del logotipo KIMBO en `desayuno-completo-2-2x.png`. La primera se midió
#: aislando los píxeles rojos (R>110, R−G>50, R−B>50) dentro de la taza —bbox del
#: wordmark 2227–2375 × 2900–3272— y se agrandó a mano para tomar también la
#: BARRA GRIS de abajo, que no es roja y por eso no sale en la máscara.
#:
#: ⚠️ Son DOS cajas y no una, y la razón es geométrica. La interpolación
#: horizontal conserva cualquier rasgo que sea HORIZONTAL, porque cada fila se
#: rellena con su propio tono; lo que no aguanta es que un rasgo CURVO cruce una
#: caja ancha. Acá lo cruza: la línea donde la taza se apoya en el platillo pasa
#: justo por la punta de la barra gris. Con una sola caja hasta y=3278 esa línea
#: salía aplanada y se veía el parche. Así que la caja grande se corta ANTES de
#: la línea (y=3258) y la punta que queda asomando se tapa con una caja chica de
#: 70 px de ancho, donde la curva casi no se mueve.
KIMBO = [
    (2215, 2880, 2390, 3258),   # wordmark rojo + casi toda la barra gris
    (2220, 3252, 2290, 3286),   # la punta de la barra, bajo la línea del platillo
]

#: Las tres ventanas 9:16. (archivo, x0, y0, ancho) — el alto sale de 16/9.
#:
#: Cómo se eligió cada una: se dibujó encima la rejilla real de la pieza (zonas
#: seguras de Meta a 250 y 1580, bloque de titular en y=441 y la zona reservada
#: del sticker) y se miró que el titular caiga sobre superficie CALMA y que la
#: zona del sticker caiga sobre superficie LIMPIA. Ver la bitácora del 08-09.
VENTANAS = {
    # 14-09 · el capuchino sube para dejar la mesa libre bajo la taza: ahí va el
    # sticker de quiz. El titular cae sobre los sillones desenfocados del lounge,
    # que son oscuros y neutros — se lee sin velo.
    "st-14-09-hora-cafe.jpg": ("mesa-cafe-2piso-2x.png", 960, 1080, 2500),
    # 16-09 · la ventana se cierra y baja por dos razones medidas. Una, dejar
    # FUERA la sombrilla blanca del toldo: con el encuadre completo el lockup
    # beige caía justo sobre ella y desaparecía. Dos, acortar la franja de sillas
    # y adoquín del pie: con la ventana ancha ocupaba media pieza y el mensaje es
    # «te esperamos», o sea que lo que tiene que pesar es la MESA SERVIDA, no el
    # suelo vacío. Acá la mesa con el notebook, la taza, la libreta y el celular
    # ocupa el centro, y abajo queda sólo lo justo para el sticker de enlace.
    "st-16-09-cowork.jpg": ("cowork-terraza-2x.png", 980, 1000, 2300),
    # 18-09 · la ventana se pega ARRIBA (y0=0) para que la mesa oscura y el muro
    # de ladrillo desenfocado ocupen el tercio superior: es el único sitio de
    # esta foto donde un titular beige se lee sin caja. El ancho es 2250 exactos,
    # o sea que esta pieza sale SIN reescalar — 1:1 desde la fuente a 2×.
    "st-18-09-dieciocho.jpg": ("desayuno-completo-2-2x.png", 375, 0, 2250),
}


def borra_kimbo(im: Image.Image, caja, apoyo: int = 20) -> Image.Image:
    """Rellena la caja interpolando entre el esmalte limpio de sus dos costados.

    Copiado del método ya probado en `between-quitar-kimbo.py`: la taza está
    fuera de foco y su superficie es un degradado suave, así que la recta que une
    los dos costados ES la superficie y no queda empalme.
    """
    x0, y0, x1, y1 = caja
    if not (apoyo <= x0 and x1 + apoyo <= im.width and 0 <= y0 <= y1 <= im.height):
        sys.exit(f"✗ la caja {caja} no deja {apoyo} px de apoyo dentro de {im.size}")
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
    print(f"  · KIMBO borrado: caja {caja} · apoyo {apoyo} · difuminado {m}")
    return fuera


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true",
                    help="guarda recortes con zoom del empalme del KIMBO")
    a = ap.parse_args()

    DESTINO.mkdir(parents=True, exist_ok=True)
    for nombre, (fuente, x0, y0, ancho) in VENTANAS.items():
        src = FUENTES / fuente
        if not src.is_file():
            sys.exit(f"✗ falta {src}\n"
                     f"  Se genera con: python scripts/magnific.py escalar "
                     f"public/assets/hilton/between/fotos-gradadas/"
                     f"{fuente.replace('-2x.png', '.jpg')} --out {src} --escala 2x")
        im = Image.open(src).convert("RGB")
        if fuente.startswith("desayuno"):
            # La ventana de QA cubre las dos cajas juntas, con 120 px de aire.
            zx0 = min(c[0] for c in KIMBO) - 120
            zy0 = min(c[1] for c in KIMBO) - 120
            zx1 = max(c[2] for c in KIMBO) + 120
            zy1 = max(c[3] for c in KIMBO) + 120
            if a.revisar:
                z = im.crop((zx0, zy0, zx1, zy1))
                z.resize((z.width * 2, z.height * 2), Image.LANCZOS).save(
                    FUENTES / "_qa-kimbo-antes.jpg", quality=94)
            for caja in KIMBO:
                im = borra_kimbo(im, caja, apoyo=18)
            if a.revisar:
                z = im.crop((zx0, zy0, zx1, zy1))
                z.resize((z.width * 2, z.height * 2), Image.LANCZOS).save(
                    FUENTES / "_qa-kimbo-despues.jpg", quality=94)

        alto = int(round(ancho * 16 / 9))
        if x0 + ancho > im.width or y0 + alto > im.height:
            sys.exit(f"✗ {nombre}: la ventana {ancho}×{alto} en ({x0},{y0}) "
                     f"se sale de {im.size}")
        # ⚠️ La comprobación que importa: la ventana tiene que ser MÁS GRANDE que
        # la salida. Si no, la pieza se entregaría ampliada y eso ya costó una
        # story rechazada en otra marca.
        if ancho < SALIDA[0]:
            sys.exit(f"✗ {nombre}: la ventana ({ancho}) es más chica que la "
                     f"entrega ({SALIDA[0]}): saldría ampliada.")
        rec = im.crop((x0, y0, x0 + ancho, y0 + alto)).resize(SALIDA, Image.LANCZOS)
        dst = DESTINO / nombre
        rec.save(dst, quality=95, subsampling=1)
        print(f"✓ {nombre}  ventana {ancho}×{alto} @({x0},{y0}) de {im.size[0]}×{im.size[1]}"
              f"  → {SALIDA[0]}×{SALIDA[1]}  (reducción ×{SALIDA[0] / ancho:.2f})")


if __name__ == "__main__":
    main()

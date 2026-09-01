#!/usr/bin/env python3
"""Hoja de contacto — ver TODO el material de una marca de una sola mirada.

Uso:  python3 scripts/hoja-contacto.py raw/<marca> out/_verificacion/<marca>.png

Para qué: el 25-08-2026 la carpeta de referencias de Casablanca tenía 13 piezas
de Between (una cafetería) y nadie lo vio, porque nunca se miró el material junto.
En una hoja de contacto se caza en cinco segundos.

Los archivos que no son imagen real salen como una casilla roja con su nombre,
así que esta hoja también delata las descargas fallidas.
"""
import os
import sys

from PIL import Image, ImageDraw

# ⚠️ Windows: la consola decodifica en cp1252 y cualquier "✅", "→" o "⭐" del
# reporte reventaba el script DESPUÉS de haber hecho el trabajo — parecía que
# había fallado y en realidad ya estaba listo. Pasó tres veces (doctor.sh,
# between-entrega.py y acá), así que va explícito.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
MINI = 320
ALTO_ETIQUETA = 30


def recolectar(raiz):
    fs = []
    for d, _, archivos in os.walk(raiz):
        for f in sorted(archivos):
            if os.path.splitext(f)[1].lower() in EXTS:
                fs.append(os.path.join(d, f))
    return sorted(fs)


def main(raiz, destino, cols=6):
    fs = recolectar(raiz)
    if not fs:
        print(f"No hay imágenes en {raiz}")
        return 1

    filas = (len(fs) + cols - 1) // cols
    hoja = Image.new("RGB", (cols * MINI, filas * (MINI + ALTO_ETIQUETA)), "white")
    dibujo = ImageDraw.Draw(hoja)
    rotos = 0

    for i, f in enumerate(fs):
        x = (i % cols) * MINI
        y = (i // cols) * (MINI + ALTO_ETIQUETA)
        etiqueta = os.path.relpath(f, raiz)
        try:
            im = Image.open(f)
            im.load()
            im = im.convert("RGB")
            ancho, alto = im.size
            im.thumbnail((MINI - 8, MINI - 8))
            hoja.paste(im, (x + (MINI - im.width) // 2, y + ALTO_ETIQUETA))
            etiqueta = f"{etiqueta}  ({ancho}x{alto})"
        except Exception:
            rotos += 1
            dibujo.rectangle(
                [x + 4, y + ALTO_ETIQUETA, x + MINI - 4, y + MINI],
                fill="#B00020",
            )
            dibujo.text((x + 14, y + ALTO_ETIQUETA + 14), "ARCHIVO ROTO", fill="white")
            etiqueta = f"✗ {etiqueta}"
        dibujo.text((x + 4, y + 8), etiqueta[:52], fill="black")

    os.makedirs(os.path.dirname(os.path.abspath(destino)), exist_ok=True)
    hoja.save(destino)
    print(f"{len(fs)} archivos · {rotos} rotos → {destino}")
    print("\nÁBRELA Y MÍRALA antes de diseñar. Dos preguntas:")
    print("  1. ¿Son TODAS de esta marca? (una pieza de otro cliente invalida el lote)")
    print("  2. ¿Reconoces la gramática — logo, titular, CTA, foto?")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))

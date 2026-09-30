#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Levanta del editable de Coni las piezas que NO se reconstruyen: se copian.

    python3 scripts/cava-cyber-oct-extraer.py

El logo CYBERWINE week y el recuadro de ADVERTENCIA son dibujo de ella. Yo los
había vuelto a componer con las fuentes, y el logo salió distinto: el titular
está en Poppins **Bold** —no ExtraBold— y con un tracking cerrado que yo no
tenía. Reconstruirlo es inventarle una versión; acá se copia.

EL MÉTODO. El .ai enlaza una foto de set que yo tengo aparte, y guarda la
matriz con que la coloca. Entonces:

    1. se renderiza la mesa de trabajo a 4×
    2. se vuelve a armar SÓLO el fondo, con la misma foto y la misma matriz
    3. lo que cambia entre las dos es exactamente lo que ella dibujó encima

De ahí sale el alfa (cuánto tapa) y la tinta (de qué color), despejando
`render = α·tinta + (1−α)·fondo`. Es lo mismo que se hace para sacar un
rótulo de una foto, pero con el fondo conocido en vez de adivinado.

⛔ El filete bajo el lockup se borra acá: Coni pidió que no vaya en ninguna
pieza. Se borra por fila, respetando la cola de la «k» de «week», que cruza el
filete y sí es parte del logo.
"""
import io
import pathlib
import sys

import fitz
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ESCRITORIO = pathlib.Path.home() / "Desktop/CAVA OCT-CYBER"
EDITABLE = ESCRITORIO / "CYBER_CAVA_OCT.ai"
FOTO_VIP = ESCRITORIO / "BRIEF/KV/REFERENCIA FOTO VIP/SyWcSOtUb8.jpg"
DESTINO = RAIZ / "public/assets/cava/cyber-oct"

S = 4.0                      # escala de render sobre la mesa de 1938,9 px
# Matriz de colocación de la foto en la mesa 0, tal como la declara el .ai.
FOTO_CAJA = (-76.9, -174.0, 2208.9, 1246.4)
# Caja del lockup, de los propios bbox de texto del .ai (CYBERWINE ∪ week)
# más holgura: CYBERWINE (126,332)-(928,591) y week (657,398)-(887,666).
CAJA_LOCKUP = (118, 325, 936, 674)


def render_y_fondo():
    pg = fitz.open(EDITABLE)[0]
    render = Image.open(io.BytesIO(
        pg.get_pixmap(matrix=fitz.Matrix(S, S), alpha=False).tobytes("png"))).convert("RGB")
    x0, y0, x1, y1 = FOTO_CAJA
    fondo = Image.new("RGB", render.size, (0, 0, 0))
    fondo.paste(Image.open(FOTO_VIP).convert("RGB").resize(
        (int(round((x1 - x0) * S)), int(round((y1 - y0) * S))), Image.LANCZOS),
        (int(round(x0 * S)), int(round(y0 * S))))
    return render, fondo


def despeja(render, fondo, caja):
    """Saca tinta y alfa de una zona, sabiendo el fondo que tenía debajo."""
    c = [int(round(v * S)) for v in caja]
    a = np.asarray(render.crop(c)).astype(float)
    b = np.asarray(fondo.crop(c)).astype(float)
    d = np.abs(a - b).max(axis=2)
    solido = np.percentile(d[d > 60], 92)          # cuánto tapa la tinta llena
    alfa = np.clip((d - 8) / (solido - 8), 0, 1)
    al = alfa[..., None]
    tinta = np.where(al > 0.02, (a - (1 - al) * b) / np.maximum(al, 0.02), 0)
    # Piso de alfa: el fondo no se reconstruye perfecto sobre los pliegues de la
    # cortina y quedan fantasmas de alfa muy bajo. Se suben desde 0 los que sí
    # son borde de letra y se hunden los que no.
    alfa = np.clip((alfa - 0.09) / 0.91, 0, 1)
    return np.concatenate([np.clip(tinta, 0, 255),
                           np.clip(alfa * 255, 0, 255)[..., None]], axis=2).astype(np.uint8)


def quita_filete(a, margen=14):
    """Borra el filete horizontal, dejando la cola de la «k» que lo cruza.

    Se separan POR COLOR, que es lo único exacto: en la franja donde está el
    filete ya no hay nada de CYBERWINE, así que ahí conviven sólo dos cosas —el
    filete, que es DORADO, y «week», que es BLANCO—. Borrar el dorado deja la
    cursiva intacta hasta el píxel.

    Antes se intentó por longitud de trazo y por posición interpolada: donde el
    filete y el palo de la «k» se cruzan forman un solo trazo, así que o le
    quedaba una muesca a la letra o sobrevivía un trocito de filete pegado a
    ella.
    """
    al = a[..., 3]
    alto = a.shape[0]
    filas = [y for y in range(int(alto * 0.6), int(alto * 0.78))
             if (al[y] > 28).sum() > 600]
    if not filas:
        return a, None
    y0, y1 = filas[0], filas[-1]
    franja = slice(max(0, y0 - margen), min(alto, y1 + margen + 1))
    z = a[franja].astype(int)
    # En esa franja lo único legítimo es el blanco de «week»: se conserva sólo
    # eso. Borrar únicamente el dorado dejaba el antialias del filete como una
    # mancha sucia, invisible sobre negro pero no sobre un fondo claro.
    # Neutro de verdad, no sólo claro: el filete es #FEF1A9 y su canal azul
    # (169) pasaba de largo un test de «claro», así que la línea sobrevivía.
    blanco = (z[..., :3].min(axis=2) > 110) & (
        z[..., :3].max(axis=2) - z[..., :3].min(axis=2) < 40)
    a[franja, ..., 3] = np.where(blanco, a[franja, ..., 3], 0)
    return a, (y0, y1)


def main():
    if not EDITABLE.exists():
        sys.exit(f"No está el editable: {EDITABLE}")
    DESTINO.mkdir(parents=True, exist_ok=True)
    render, fondo = render_y_fondo()
    a = despeja(render, fondo, CAJA_LOCKUP)
    a, filete = quita_filete(a)
    print(f"  filete borrado en las filas {filete[0]}..{filete[1]}" if filete
          else "  ojo: no se encontró el filete")
    im = Image.fromarray(a)
    # La banda del lockup: por arriba queda el gancho, por abajo la fecha.
    im = im.crop((0, 260, im.width, 1048))
    im = im.crop(im.split()[3].getbbox())
    ruta = DESTINO / "lockup-cyberwine-week.png"
    im.save(ruta)
    print(f"  ✓ {ruta.relative_to(RAIZ)}  {im.width}x{im.height}  "
          f"aspecto {im.width / im.height:.4f}")


if __name__ == "__main__":
    main()

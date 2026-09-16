#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deja las dos escenas del CARRUSEL CONCURSO en formato de entrega: 2250×2813.

El feed de Between es **4:5** y `magnific.py --aspecto` no lo tiene (manual
§ ronda 6.6), así que las escenas salen en 3:4 —3584×4800— y hay que recortar
320 filas.

⭐ SE RECORTA POR ABAJO, Y ESO SE MIDIÓ. El recorte del sticker (su borde
blanco) termina en y=4340 de 4800 en la portada y más arriba todavía en el
escritorio; de 4340 al borde sólo hay sombra. Cortando abajo (`top=0`) la franja
beige limpia de la portada pasa de 0,347 a **0,372** del alto, que son 34 px de
titular más a 1080. Cortando arriba habría pasado a 0,30 y el bloque no cabía.

⚠️ NO SE GRADA, y por la misma razón que la S4: las dos escenas salen ya bien
expuestas del generador. La pasada estándar de `between-gradar.py` apunta a
lum 118 —calibrada sobre fotos de ambiente oscuro— y sobre una pared beige de
lum 205 la dejaría sucia. Medido antes de decidirlo:

    franja 0–35 % de la portada · lum 200–211 · min 177 · plana

Uso:  python scripts/between-concurso-s3-fotos.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "raw/hilton/between/concurso-s3"
DESTINO = RAIZ / "public/assets/hilton/between/concurso-s3"
DESTINO.mkdir(parents=True, exist_ok=True)
W, H = 2250, 2813          # 1080×1350 × 2,0833 — la entrega de Eli

#: `bajar` = cuántas filas del ORIGEN se baja la escena dentro del 4:5, para
#: ganar pared limpia arriba. El recurso es el de la S5 («Mover la escena dentro
#: del cuadro no necesita otra generación: si el fondo de arriba es una
#: superficie plana, se continúa esa superficie y se baja la escena»).
#:
#: ⭐ 300 filas NO es un número redondo elegido a ojo: son 90 px en el lienzo de
#: 1080. Medido sobre la tirada, el borde blanco del recorte empezaba en y=502
#: de 1350 y el bloque de titular de Between —lockup 93, script, caja alta— cae
#: hasta y≈461: quedaban 41 px de aire. Con 90 más, la franja limpia llega a
#: y≈592 y las cajas taupe caben debajo del titular sin tocar el recorte.
#: El costo es que la base del escritorio sangra por el canto inferior, que es
#: lo que hacen las dos referencias del cliente.
PIEZAS = {
    "gen-portada-sticker-r3.png": ("c1-portada.jpg", 300),
    "gen-escritorio-2.png": ("c1-escritorio.jpg", 640),
}


def extiende_pared(im: Image.Image, filas: int) -> Image.Image:
    """Baja la escena `filas` px y rellena arriba CONTINUANDO la pared.

    La pared es un degradado vertical suave, así que se extrapola linealmente
    columna por columna con la pendiente medida en las primeras 400 filas. No
    se espeja (el espejo invierte el degradado y deja un pliegue) ni se repite
    la fila 0 (deja una banda plana con costura).
    """
    if filas <= 0:
        return im
    a = np.asarray(im).astype(np.float32)
    cab = a[:400]
    y = np.arange(400, dtype=np.float32)
    yc = y - y.mean()
    # pendiente por columna y canal: regresión lineal cerrada
    pend = (yc[:, None, None] * (cab - cab.mean(0, keepdims=True))).sum(0) / (yc ** 2).sum()
    base = cab[0]
    arriba = base[None] + pend[None] * np.arange(-filas, 0, dtype=np.float32)[:, None, None]
    nueva = np.concatenate([np.clip(arriba, 0, 255), a], 0)[: a.shape[0]]
    return Image.fromarray(nueva.astype(np.uint8))


def recorte45(im: Image.Image, bajar: int = 0) -> Image.Image:
    """4:5 conservando el ancho y cortando POR ABAJO (ver la cabecera)."""
    im = extiende_pared(im, bajar)
    alto45 = round(im.width * 5 / 4)
    if im.height > alto45:
        im = im.crop((0, 0, im.width, alto45))
    elif im.height < alto45:                       # no debería pasar; por si acaso
        sobra = round(im.height * 4 / 5)
        x = (im.width - sobra) // 2
        im = im.crop((x, 0, x + sobra, im.height))
    return im.resize((W, H), Image.LANCZOS)


def informe(nombre: str, im: Image.Image) -> None:
    """La franja donde va el titular, medida por tercios — la tinta la manda el
    fondo (memoria `la-tinta-la-manda-el-fondo`: manda el PEOR tercio)."""
    a = np.asarray(im.convert("RGB")).astype(float)
    lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    fr = lum[int(0.10 * H):int(0.36 * H)]
    t = [fr[:, int(j * W / 3):int((j + 1) * W / 3)].mean() for j in range(3)]
    print(f"  {nombre:20} franja del titular (10–36 %): media {fr.mean():5.1f} · "
          f"tercios {t[0]:5.1f} {t[1]:5.1f} {t[2]:5.1f} · peor {min(t):5.1f} → "
          f"tinta {'CAFÉ' if min(t) > 150 else 'BEIGE'}")


def main() -> int:
    for src, (dst, bajar) in PIEZAS.items():
        origen = ORIGEN / src
        if not origen.is_file():
            sys.exit(f"✗ falta {origen}\n"
                     f"  corre antes: python scripts/between-concurso-s3-generar.py")
        im = recorte45(Image.open(origen).convert("RGB"), bajar)
        im.save(DESTINO / dst, quality=95, subsampling=0)
        print(f"✓ {dst}  {im.size}  ({(DESTINO / dst).stat().st_size // 1024} KB)")
        informe(dst, im)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Sube la DENSIDAD del logotipo ya estampado sobre un vaso, sin tocar su geometría.

Por qué existe
--------------
Ronda 5 · 01-09-2026. Eli: «la imagen se ve sucia el logo. Mejóralo, ya que debe
ser el vaso original con el logo real de between».

Medida la relación **tinta / cartón** (media del 12 % más oscuro contra la del
40 % más claro, dentro de la banda del logo):

    vaso REAL, foto del cliente        0,172   ← serigrafía negra sobre kraft
    `cumple-vela-logo.png` (ronda 4)   0,581   ← café claro, no se lee
    `cumple-manos-logo.png` (ronda 5)  0,443   ← con velo, además

La causa es una línea de `between-logo-vaso.py`:
`densidad *= clip(lum * 1,25, 0,25, 1)` apaga la tinta en un vaso de tono medio,
así que la densidad efectiva no pasa de ~0,64 y el negro nunca llega a negro.

⭐ Por qué se corrige así y no re-estampando
-------------------------------------------
Re-estampar obliga a **borrar** el logotipo anterior, y borrar es inventar el
cartón que había debajo. En estos vasos el cuerpo tiene un gradiente lateral
fuerte y cualquier relleno deja un rectángulo a la vista — pasó en la ronda 5.

Acá no se mueve un píxel de geometría: los trazos ya están en su sitio y con su
proporción. Sólo se les sube la carga de tinta, que es el defecto medido.

⛔ **Sólo sirve sobre cartón LIMPIO.** Si la imagen ya trae un velo rectangular de
un borrado anterior, este script lo toma por tinta y lo oscurece con todo lo
demás. En ese caso hay que volver primero a una versión sin velo
(`git show <commit>:<ruta>`), que es lo que se hizo con las dos piezas del
cumpleaños el 01-09.

Uso:
    python scripts/between-logo-densidad.py <entrada> <salida> \\
        --caja X1 Y1 X2 Y2       # la banda del logo sobre el vaso
        [--objetivo 0.20]        # tinta/cartón que se busca
        [--gamma 0.72]           # <1 carga también los trazos finos
        [--muestra 30]           # filas limpias que se miran arriba y abajo
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def nivel_carton(gris, x1, x2, y1, y2, alto):
    """Nivel del cartón por columna, interpolado entre arriba y abajo de la caja.

    Por columna y no por fila: el vaso es un cilindro, así que el brillo depende
    de x (la curvatura) y casi nada de y. Medirlo por columna conserva el lado
    iluminado y el lado en sombra en vez de aplanarlos.
    """
    arr = gris[max(y1 - alto, 0):y1, x1:x2]
    aba = gris[y2:min(y2 + alto, gris.shape[0]), x1:x2]
    sup = arr.mean(axis=0) if arr.size else None
    inf = aba.mean(axis=0) if aba.size else None
    if sup is None and inf is None:
        raise SystemExit('no hay cartón limpio ni arriba ni abajo de la caja')
    sup = inf if sup is None else sup
    inf = sup if inf is None else inf
    rampa = np.linspace(0.0, 1.0, y2 - y1)[:, None]
    return sup[None, :] * (1 - rampa) + inf[None, :] * rampa


def relacion(gris):
    return (gris[gris < np.percentile(gris, 12)].mean()
            / gris[gris > np.percentile(gris, 60)].mean())


def densificar(entrada, salida, caja, objetivo, gamma, muestra):
    im = Image.open(entrada).convert('RGB')
    x1, y1, x2, y2 = (int(v) for v in caja)
    A = np.asarray(im).astype(np.float64)
    gris = 0.299 * A[..., 0] + 0.587 * A[..., 1] + 0.114 * A[..., 2]

    zona = A[y1:y2, x1:x2].copy()
    lum = gris[y1:y2, x1:x2]
    base = nivel_carton(gris, x1, x2, y1, y2, muestra)
    antes = relacion(lum)

    # cuánta tinta tiene cada píxel: 0 = cartón, 1 = negro
    d = np.clip(1.0 - lum / np.maximum(base, 1.0), 0.0, 1.0)
    if d.max() < 0.02:
        raise SystemExit('no se detectó tinta en la caja: revisa las coordenadas')

    # se reasigna para que el trazo más cargado llegue al objetivo. El gamma
    # conserva el borde suave del trazo en vez de recortarlo.
    k = (1.0 - objetivo) / d.max()
    d2 = np.clip((d / d.max()) ** gamma * d.max() * k, 0.0, 0.985)
    zona *= ((1.0 - d2) / np.maximum(1.0 - d, 1e-6))[..., None]

    # empalme con pluma, para no marcar el borde de la caja
    alto, ancho = y2 - y1, x2 - x1
    radio = max(2, int(min(alto, ancho) * 0.07))
    m = Image.new('L', (ancho, alto), 0)
    ImageDraw.Draw(m).rectangle((radio, radio, ancho - radio, alto - radio), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(radio * 0.9))

    fuera = im.copy()
    fuera.paste(Image.fromarray(np.clip(zona, 0, 255).astype(np.uint8)), (x1, y1), m)

    z = np.asarray(fuera.convert('L').crop((x1, y1, x2, y2))).astype(np.float64)
    print(f'tinta/cartón  antes {antes:.3f}  ->  ahora {relacion(z):.3f}'
          f'   (vaso real medido 0,172)')

    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    fuera.save(salida)
    print(f'{salida}  banda ({x1},{y1})-({x2},{y2})  geometría intacta')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--caja', nargs=4, type=int, required=True,
                    metavar=('X1', 'Y1', 'X2', 'Y2'))
    ap.add_argument('--objetivo', type=float, default=0.20)
    ap.add_argument('--gamma', type=float, default=0.72)
    ap.add_argument('--muestra', type=int, default=30)
    a = ap.parse_args()
    densificar(a.entrada, a.salida, a.caja, a.objetivo, a.gamma, a.muestra)


if __name__ == '__main__':
    main()

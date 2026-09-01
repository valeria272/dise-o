#!/usr/bin/env python3
"""
Re-estampa el logotipo de Between sobre un vaso SIN curvarlo y sin inventar cartón.

Por qué existe
--------------
Ronda 5 · 01-09-2026. Eli, mirando las dos piezas del cumpleaños:

> «No puedes curvarlo de esa manera; sutil para el mockup en el vaso sí, pero está
>  muy intervenido en los vasos. El vaso debe llevar bien el logo.»

El sello que traían esas dos imágenes es el de la **ronda 4**, hecho con la
versión vieja de `between-logo-vaso.py`, que aplicaba `curvar()`: comba sinusoidal
sobre un cilindro **más un acortado lateral del 18 %**. Eso arquea la línea de
base y aplasta las letras de los extremos — «COFFEE & BAR» quedaba irreconocible.

Se volvió a esa versión el 01-09 porque su **cartón está limpio** (la ronda 5 lo
había dejado con un velo rectangular al borrar el sello anterior). O sea: una
versión tiene el cartón bueno y el logo malo, y la otra al revés.

⭐ La salida: borrar SOLO LOS TRAZOS
-----------------------------------
Lo que hacía imposible re-estampar era el borrado: `limpiar_zona` reemplaza un
**bloque** entero de cartón, y en un vaso con gradiente lateral fuerte —en
`cumple-manos` el cuerpo va de 58 a 236 de luminancia— cualquier bloque inventado
se nota.

Pero un logotipo no es un bloque: **son líneas finas**. Rellenar trazos de 3–6 px
tomando el cartón que los rodea es el problema clásico de la raya en una foto, y
se resuelve bien con convolución normalizada: cada píxel borrado se reemplaza por
el promedio ponderado de sus vecinos CONOCIDOS. El gradiente del cilindro y el
grano del cartón se conservan porque nunca se sustituyen: se interpolan a 3 px de
distancia.

Después se estampa el logotipo **plano**:

⛔ **Sin `curvar()`, sin `resize` no uniforme, sin espejo.** El logotipo es marca
registrada; su forma es intocable (`clients/hilton/CLAUDE.md § EL VASO TO GO`).
El realismo se consigue por **tono** —multiply contra el cartón, respetando su
sombra— no por geometría. Si la curvatura del vaso se nota, la respuesta es
achicar el logo o correrlo al centro del cilindro, donde es ópticamente plano.

Fuente del logotipo: `logo-negro-vector.png`, sacado del editable oficial que
mandó Eli (`Between_logo_oficial.ai`, página 1) a 4214×1392. Proporción 3,0273.

Uso:
    python scripts/between-logo-vaso-plano.py <entrada> <salida> \
        --caja X1 Y1 X2 Y2        # la banda donde vive el logo actual
        [--centro CX CY --ancho W]  # si no, se toman del logo detectado
        [--tinta 0.20]            # densidad objetivo (vaso real medido: 0,172)
        [--umbral 0.86]           # qué tan oscuro cuenta como trazo
        [--muestra 30]
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
LOGO = RAIZ / 'public/assets/hilton/between/logo-negro-vector.png'


def arquear(logo, sag):
    """Curva SUTILMENTE la línea de base desplazando cada columna en vertical.

    ⚠️ Esto NO es `curvar()`, que es lo que costó la ronda 4. La diferencia es
    la única que importa:

        curvar()   comprimía el logo a lo ancho un 18 % y aplastaba las letras
                   de los extremos  ->  DEFORMA la marca
        arquear()  desplaza cada columna en Y y nada más  ->  cada letra
                   conserva su ancho, su alto y su forma exactos

    Es la corrección de perspectiva que pidió Eli el 01-09 («sutil para el
    mockup en el vaso sí»): un vaso visto algo desde arriba muestra sus bandas
    horizontales combadas hacia abajo en el centro, y un logotipo perfectamente
    recto encima se lee pegado.

    `sag` es la caída en px en el centro. Se topa en el 3 % del ancho: más que
    eso ya se nota como deformación y vuelve el problema de la ronda 4.
    """
    import numpy as _np
    w, h = logo.size
    sag = max(-0.03 * w, min(0.03 * w, sag))
    if abs(sag) < 0.5:
        return logo
    extra = int(abs(sag)) + 2
    lienzo = Image.new('RGBA', (w, h + extra * 2), (0, 0, 0, 0))
    a = _np.asarray(logo)
    out = _np.zeros((h + extra * 2, w, 4), _np.uint8)
    for x in range(w):
        # perfil coseno: 0 en los extremos, `sag` en el centro
        t = (x / max(w - 1, 1)) * 2.0 - 1.0
        dy = int(round(sag * (1.0 - t * t)))
        out[extra + dy:extra + dy + h, x, :] = a[:, x, :]
    return Image.fromarray(out, 'RGBA')


def nivel_carton(gris, x1, x2, y1, y2, alto):
    """Nivel del cartón por COLUMNA, interpolado entre arriba y abajo de la caja.

    Por columna porque el vaso es un cilindro: el brillo depende de x (la
    curvatura) y casi nada de y. Medirlo por fila lo aplanaría.
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


def borrar_trazos(zona, mascara, pasos=4, radio=7.0):
    """Rellena SOLO los píxeles marcados, interpolando desde sus vecinos.

    Convolución normalizada: se difumina la imagen con los píxeles conocidos
    pesados a 1 y los borrados a 0, y se divide por el difuminado de los pesos.
    Así el relleno sale del cartón que rodea cada trazo y no de un promedio
    global — el gradiente lateral y el grano quedan intactos.
    """
    img = zona.astype(np.float64).copy()
    conocido = (~mascara).astype(np.float64)
    for i in range(pasos):
        r = radio * (1.0 - 0.18 * i)
        peso = Image.fromarray((conocido * 255).astype(np.uint8)).filter(
            ImageFilter.GaussianBlur(r))
        wnum = np.asarray(peso).astype(np.float64) / 255.0
        est = np.zeros_like(img)
        for c in range(3):
            canal = Image.fromarray(
                np.clip(img[..., c] * conocido, 0, 255).astype(np.uint8)).filter(
                ImageFilter.GaussianBlur(r))
            est[..., c] = np.asarray(canal).astype(np.float64) / np.maximum(wnum, 1e-4)
        img[mascara] = est[mascara]
        conocido = np.ones_like(conocido)          # ya está todo relleno
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada'); ap.add_argument('salida')
    ap.add_argument('--caja', nargs=4, type=int, required=True,
                    metavar=('X1', 'Y1', 'X2', 'Y2'))
    ap.add_argument('--centro', nargs=2, type=int, default=None)
    ap.add_argument('--ancho', type=int, default=None)
    ap.add_argument('--tinta', type=float, default=0.20)
    ap.add_argument('--umbral', type=float, default=0.86)
    ap.add_argument('--arco', type=float, default=0.0,
                    help='caida en px al centro de la linea de base. Positivo = comba '
                         'hacia abajo, que es lo que hace un vaso visto desde arriba. '
                         'Solo desplaza columnas en Y: NO comprime ni deforma. Tope 3 %% '
                         'del ancho')
    ap.add_argument('--muestra', type=int, default=30)
    ap.add_argument('--logo', default=str(LOGO))
    a = ap.parse_args()

    im = Image.open(a.entrada).convert('RGB')
    A = np.asarray(im).astype(np.float64)
    gris = 0.299*A[..., 0] + 0.587*A[..., 1] + 0.114*A[..., 2]
    x1, y1, x2, y2 = a.caja

    base = nivel_carton(gris, x1, x2, y1, y2, a.muestra)
    zona = A[y1:y2, x1:x2].copy()
    lz = gris[y1:y2, x1:x2]

    # ── 1. máscara de los trazos ────────────────────────────────────────────
    m = lz < base * a.umbral
    if m.sum() < 50:
        raise SystemExit('no se detectó logotipo en la caja: revisa --caja/--umbral')
    ys, xs = np.where(m)
    cx_det = x1 + int((xs.min() + xs.max()) / 2)
    cy_det = y1 + int((ys.min() + ys.max()) / 2)
    w_det = int(xs.max() - xs.min() + 1)
    h_det = int(ys.max() - ys.min() + 1)
    print(f'logo actual: {w_det}x{h_det} en centro ({cx_det},{cy_det})  '
          f'proporcion {w_det/h_det:.4f}  ({int(m.sum())} px de trazo)')

    # se dilata 2 px para llevarse el antialias del borde
    m = np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(
        ImageFilter.MaxFilter(5))) > 127

    # ── 2. borrar los trazos ────────────────────────────────────────────────
    limpio = borrar_trazos(zona, m)
    A[y1:y2, x1:x2] = limpio

    # ── 3. estampar el logotipo PLANO ───────────────────────────────────────
    logo = Image.open(a.logo).convert('RGBA')
    al = np.asarray(logo)[:, :, 3]
    ly, lx = np.where(al > 8)
    logo = logo.crop((lx.min(), ly.min(), lx.max()+1, ly.max()+1))
    prop = logo.width / logo.height

    ancho = a.ancho or w_det
    alto = int(round(ancho / prop))               # escala UNIFORME, siempre
    logo = logo.resize((ancho, alto), Image.LANCZOS)
    if a.arco:
        logo = arquear(logo, a.arco)
        alto = logo.height
        print(f'arco sutil: {a.arco:+.0f} px de caida en el centro '
              f'({abs(a.arco)/ancho*100:.1f} % del ancho) — solo desplazamiento en Y')
    cx, cy = (a.centro or (cx_det, cy_det))
    px, py = int(cx - ancho/2), int(cy - alto/2)
    print(f'logo nuevo:  {ancho}x{alto} en centro ({cx},{cy})  '
          f'proporcion {prop:.4f} SIN deformar y SIN curvar')

    lg = np.asarray(logo).astype(np.float64)
    dens = (lg[:, :, 3] / 255.0) * np.clip(1.0 - lg[:, :, :3].mean(axis=2)/255.0, 0, 1)
    # la tinta cargada al máximo deja el cartón en `--tinta` de su valor
    dens = dens * (1.0 - a.tinta)

    X1, Y1 = max(px, 0), max(py, 0)
    X2, Y2 = min(px+ancho, im.width), min(py+alto, im.height)
    dens = dens[Y1-py:Y2-py, X1-px:X2-px]
    A[Y1:Y2, X1:X2] *= (1.0 - dens)[..., None]

    fuera = Image.fromarray(np.clip(A, 0, 255).astype(np.uint8))
    g2 = np.asarray(fuera.convert('L').crop((x1, y1, x2, y2))).astype(np.float64)
    r = (g2[g2 < np.percentile(g2, 6)].mean() / g2[g2 > np.percentile(g2, 60)].mean())
    print(f'tinta/cartón del trazo: {r:.3f}   (vaso real medido 0,172)')

    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    fuera.save(a.salida)
    print(f'{a.salida}')


if __name__ == '__main__':
    main()

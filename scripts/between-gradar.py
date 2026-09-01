#!/usr/bin/env python3
"""
Gradación de fotos BETWEEN hacia los números MEDIDOS en las piezas reales de Eli.

Medido sobre raw/hilton/between-adn/ref-piezas/ (zona de foto, sin texto):
    luminancia media 104–137  ·  p95 185–249  ·  calidez (R−B) +48…+72  ·  sat 39–50

Mis fotos fuente venían en lum 58–104, p95 149–210 y calidez +16…+63: más oscuras,
más planas y más frías. Encima llevaban multiply 0,30–0,34 cuando Eli usa ~0,10.
Eso es lo que hacía ver las piezas apagadas y "baratas".

Reglas de Eli que este script respeta (clients/hilton/CLAUDE.md):
  - nada quemado: se limita el p99,5 con una rodilla suave, nunca con recorte duro
  - sin luces de flash: el levante es por curva, no por ganancia plana
  - subir el contraste ~3 %, con suavidad
  - conservar el color de la comida: la saturación se toca lo mínimo

Uso:
    python3 scripts/between-gradar.py <entrada.jpg> [más entradas...] --salida <carpeta>
    python3 scripts/between-gradar.py --auditar <archivos>     # solo reporta, no escribe
"""
import argparse, os, sys
import numpy as np
from PIL import Image

# ⭐ RE-MEDIDO 27-08-2026 sobre las 19 piezas terminadas de Eli:
#     lum media 117,4 · p95 226,9 · p5 24,3 · calidez +45,6
# El p95 de 200 que había acá dejaba las piezas SIN altas: las nuestras daban
# p95 204 contra 227 de ella, y por eso se veían apagadas aunque el brillo medio
# calzara. El p5 también importa: nuestras sombras estaban MÁS LAVADAS que las de
# ella (28,7 contra 24,3), así que el negro tiene que bajar, no subir.
OBJETIVO = {'lum': 118.0, 'p95': 227.0, 'p05': 24.0, 'calidez': 50.0}

# ⭐ PERFIL «neutro» — 01-09-2026, ronda 5 del cliente.
# Scarlette reclamó DOS veces en la misma ronda, por dos piezas distintas:
#   «Eliminar el filtro de color cálido que tiene el carrusel completo» (1-sep)
#   «En general se ven quemadas las imagenes y con un filtro medio raro» (14-sep)
# El perfil de arriba está medido sobre las piezas aprobadas de Eli (+45,6 de
# calidez), así que NO se toca: es el ADN de la marca y sigue valiendo para todo
# lo demás. Pero para las piezas que el cliente devolvió por este motivo se grada
# con este perfil, que baja las dos cosas que él nombra:
#   · calidez  50 → 20   (las fotos crudas del 2.º piso vienen en +27: esto queda
#                         POR DEBAJO del natural, o sea saca filtro, no lo suma)
#   · p95     227 → 210  («quemadas»: menos techo de altas)
# Se conservan `lum` y `p05`: el reclamo es de color y de altas, no de brillo
# medio ni de sombras — y bajar el brillo apagaría las piezas, que es el error
# contrario que ya cometimos en la ronda 4.
NEUTRO = {'lum': 118.0, 'p95': 210.0, 'p05': 24.0, 'calidez': 20.0}

PERFILES = {'eli': OBJETIVO, 'neutro': NEUTRO}

TECHO = 248.0          # ningún pixel pasa de acá: "nada quemado"
CONTRASTE = 1.03       # el +3 % que pide Eli

def luminancia(a):
    return 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]

def medir(a):
    lum = luminancia(a)
    mx, mn = a.max(axis=2), a.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0)
    return {'lum': float(lum.mean()), 'p05': float(np.percentile(lum, 5)),
            'p95': float(np.percentile(lum, 95)), 'sat': float(sat.mean() * 100),
            'calidez': float((a[:, :, 0] - a[:, :, 2]).mean())}

def rodilla(x, techo=TECHO):
    """Comprime lo que pasa de 0,80·techo en vez de recortarlo — sin altas quemadas."""
    codo = 0.80 * techo
    alto = x > codo
    if alto.any():
        exceso = (x[alto] - codo) / max(x.max() - codo, 1e-6)
        x = x.copy()
        x[alto] = codo + (techo - codo) * (1 - np.exp(-2.2 * exceso))
    return x

def gradar(a, obj=None):
    obj = obj or OBJETIVO
    a = a.astype(np.float64)
    antes = medir(a)

    # 1. ganancia para llevar las altas luces al p95 objetivo
    p95 = max(np.percentile(luminancia(a), 95), 1.0)
    a *= np.clip(obj['p95'] / p95, 0.85, 1.9)

    # 2. gamma para el brillo medio (levanta sombras sin aplanar el negro)
    lum = max(luminancia(a).mean(), 1.0)
    g = np.log(np.clip(obj['lum'], 1, 254) / 255.0) / np.log(np.clip(lum, 1, 254) / 255.0)
    a = 255.0 * np.power(np.clip(a / 255.0, 0, 1), np.clip(g, 0.55, 1.6))

    # 2b. punto de negro. Las nuestras salían con las sombras LAVADAS (p5 28,7
    #     contra 24,3 de ella): mucho brillo medio pero sin negro, que es lo que
    #     se lee como "plano". Se baja el piso y se reescala para no perder las
    #     altas ya ganadas. Nunca empasta: el clip final deja el mínimo en 2.
    p05 = float(np.percentile(luminancia(a), 5))
    negro = float(np.clip(p05 - obj['p05'], -12, 18))
    if abs(negro) > 1:
        a = np.clip((a - negro) * (255.0 / max(255.0 - negro, 1.0)), 0, None)

    # 3. calidez: se reparte entre rojo y azul. Corrige en los DOS sentidos —
    #    togo-brownie ya venía en +63 y sin esto se iba a +87 (naranja falso).
    falta = np.clip(obj['calidez'] - medir(a)['calidez'], -40, 40)
    a[:, :, 0] += falta * 0.55
    a[:, :, 2] -= falta * 0.45

    # 4. contraste suave alrededor del gris medio
    a = 128.0 + (a - 128.0) * CONTRASTE

    # 5. rodilla en altas + piso: nada quemado, nada empastado
    a = rodilla(np.clip(a, 0, None))
    a = np.clip(a, 2, TECHO)
    return a, antes, medir(a)

def recortar45(im, top=None, ancho=2250):
    """Recorta 4:5 desde una fuente más alta y entrega el ancho de entrega.

    `top` es la fracción (0..1) del sobrante vertical que queda ARRIBA del
    recorte: 0 pega el recorte al techo, 1 al piso, 0,5 lo centra. Se pide a
    mano porque en un bodegón el encuadre es una decisión de dirección de arte,
    no un centrado automático.
    """
    W, H = im.size
    alto45 = int(round(W * 5 / 4))
    if alto45 <= H:
        sobra = H - alto45
        y = int(round(sobra * (0.5 if top is None else top)))
        im = im.crop((0, y, W, y + alto45))
    else:                                   # la fuente es más ANCHA que 4:5
        ancho45 = int(round(H * 4 / 5))
        x = int(round((W - ancho45) * (0.5 if top is None else top)))
        im = im.crop((x, 0, x + ancho45, H))
    return im.resize((ancho, int(round(ancho * 5 / 4))), Image.LANCZOS)


def main():
    # Windows lee la consola en cp1252 y las flechas del reporte la reventaban
    # DESPUÉS de haber escrito los archivos: parecía que había fallado y no.
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument('entradas', nargs='+')
    ap.add_argument('--salida', default=None)
    ap.add_argument('--auditar', action='store_true')
    ap.add_argument('--perfil', choices=sorted(PERFILES), default='eli',
                    help="'eli' = el ADN medido (por defecto). "
                         "'neutro' = menos calidez y menos altas, para lo que el "
                         "cliente devolvió por «filtro cálido» o «quemadas».")
    ap.add_argument('--recorte45', action='store_true',
                    help='recorta 4:5 y entrega a --ancho')
    ap.add_argument('--top', type=float, default=None,
                    help='0..1 — dónde cae el recorte 4:5 (0 arriba, 1 abajo)')
    ap.add_argument('--ancho', type=int, default=2250)
    ap.add_argument('--nombre', default=None,
                    help='nombre del archivo de salida (solo con UNA entrada)')
    args = ap.parse_args()
    obj = PERFILES[args.perfil]
    if args.salida:
        os.makedirs(args.salida, exist_ok=True)
    if args.nombre and len(args.entradas) != 1:
        sys.exit('--nombre solo vale con una entrada')
    for p in args.entradas:
        im = Image.open(p).convert('RGB')
        if args.recorte45:
            im = recortar45(im, args.top, args.ancho)
        a, antes, despues = gradar(np.asarray(im), obj)
        n = args.nombre or os.path.basename(p)
        print(f"{n:34} [{args.perfil}] "
              f"lum {antes['lum']:5.1f}->{despues['lum']:5.1f}  "
              f"p95 {antes['p95']:5.1f}->{despues['p95']:5.1f}  "
              f"calidez {antes['calidez']:5.1f}->{despues['calidez']:5.1f}  "
              f"sat {antes['sat']:4.1f}->{despues['sat']:4.1f}")
        if args.auditar or not args.salida:
            continue
        Image.fromarray(a.astype(np.uint8)).save(os.path.join(args.salida, n), quality=95)


if __name__ == '__main__':
    main()

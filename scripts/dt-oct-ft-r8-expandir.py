#!/usr/bin/env python3
"""DT · ST 01-10 Family Time · RONDA 8 — alejar la cámara sin tocar a la familia.

Eli (28-09, sobre la r7): «hay varias [fotos] en que las personas desaparecen o no se
ven completas». Dos causas: (1) el recuadro de Family Time tapaba a la familia del pecho
para abajo y (2) la foto de almohadas corta al papá en el borde.

Arreglo de la (1): se EXPANDE la foto hacia abajo y a los lados (Flux Pro expand de
Freepik) para que la familia suba y quede entera en la franja libre entre el titular
(termina en y≈700) y el recuadro (empieza en y≈1110). Lo expandido es sólo cama, mesa,
piso y muro; encima se pega la foto ORIGINAL con un borde suave, así las personas y el
hotel son los píxeles aprobados, no un redibujo.

    python scripts/dt-oct-ft-r8-expandir.py            # las dos
    python scripts/dt-oct-ft-r8-expandir.py hab        # sólo una
"""
import sys
from pathlib import Path

from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import magnific as M  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
BANCO = RAIZ / 'out/hilton/dt/familia/entrega'
TMP = RAIZ / 'raw/hilton/dt/oct/r8'
DEST = RAIZ / 'public/assets/hilton/dt/oct'

# abajo = px que se agregan bajo la foto de 1440×2560; los lados salen de mantener 9:16
ESCENAS = {
    'hab': {
        'src': 'DT-familia-hab-2camas-story-2160x3840.jpg',
        'abajo': 600,
        'prompt': 'the same hotel room continues: more of the same white bed with white duvet, '
                  'the upholstered bed base and the dark herringbone carpet at the bottom; same '
                  'beige wall panels and warm lamps on the sides. No people, no extra objects.',
    },
    'desayuno': {
        'src': 'DT-familia-restaurante-story-2160x3840.jpg',
        'abajo': 900,
        # la v3 dejó una rodilla suelta sobre la silla vacía de abajo a la derecha
        'borrar': [(1335, 2120, 1440, 2345)],  # con 520 el recuadro caía en los mentones
        # v1 inventó una quinta persona en el borde derecho: la gente se prohíbe con todas las letras
        'prompt': 'quiet empty hotel restaurant in the morning: dark table edge, empty cream '
                  'upholstered chairs, light wooden floor, empty tables on the right side. '
                  'Nobody else in the room.',
    },
}


def borrar(im, caja):
    """Relleno local de lo que la expansión inventó (un brazo, una pierna) sobre fondo liso."""
    import cv2
    import numpy as np
    a = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    m = np.zeros(a.shape[:2], np.uint8)
    x0, y0, x1, y1 = caja
    m[y0:y1, x0:x1] = 255
    a = cv2.inpaint(a, m, 9, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))


def expandir(nombre):
    e = ESCENAS[nombre]
    orig = Image.open(BANCO / e['src']).convert('RGB').resize((1440, 2560), Image.LANCZOS)
    abajo = e['abajo']
    lado = round((2560 + abajo) * 9 / 16 - 1440) // 2
    TMP.mkdir(parents=True, exist_ok=True)
    entrada = TMP / f'{nombre}-entrada.jpg'
    orig.save(entrada, quality=94)

    crudo = TMP / f'{nombre}-expandida.jpg'
    if not crudo.exists():
        print(f'→ {nombre}: expandiendo {lado}/{lado}/0/{abajo}')
        r = M.pedir('/v1/ai/image-expand/flux-pro', {
            'image': M.b64_de(entrada), 'prompt': e['prompt'],
            'left': lado, 'right': lado, 'top': 0, 'bottom': abajo,
        })
        tid = r.get('data', r).get('task_id')
        M.guarda(M.espera('/v1/ai/image-expand/flux-pro', tid), crudo)

    exp = Image.open(crudo).convert('RGB')
    W, H = 1440 + 2 * lado, 2560 + abajo
    if exp.size != (W, H):
        exp = exp.resize((W, H), Image.LANCZOS)

    # la original encima, con 40 px de borde suave hacia lo expandido (salvo arriba)
    borde = 40
    m = Image.new('L', (orig.width - 2 * borde, orig.height - borde), 255)
    mascara = Image.new('L', orig.size, 0)
    mascara.paste(m, (borde, 0))
    mascara = mascara.filter(ImageFilter.GaussianBlur(borde / 2))
    # arriba no hay expansión: la franja superior queda opaca
    tope = Image.new('L', (orig.width, borde), 255)
    mascara.paste(tope, (0, 0))
    exp.paste(orig, (lado, 0), mascara)

    final = exp.resize((1440, 2560), Image.LANCZOS)
    for caja in e.get('borrar', []):
        final = borrar(final, caja)
    salida = DEST / f'ft-r8-{nombre}.jpg'
    final.save(salida, quality=92)
    print(f'  ✓ {salida.relative_to(RAIZ)}  (la familia queda a {1440 / W:.0%} del tamaño)')


if __name__ == '__main__':
    for n in (sys.argv[1:] or ESCENAS):
        expandir(n)

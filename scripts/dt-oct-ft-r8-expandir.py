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
        'abajo': 900,  # con 520 el recuadro caía en los mentones
        # v1 inventó una quinta persona en el borde derecho: la gente se prohíbe con todas las letras
        'prompt': 'quiet empty hotel restaurant in the morning: dark table edge, empty cream '
                  'upholstered chairs, light wooden floor, empty tables on the right side. '
                  'Nobody else in the room.',
    },
}


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
    salida = DEST / f'ft-r8-{nombre}.jpg'
    final.save(salida, quality=92)
    print(f'  ✓ {salida.relative_to(RAIZ)}  (la familia queda a {1440 / W:.0%} del tamaño)')


if __name__ == '__main__':
    for n in (sys.argv[1:] or ESCENAS):
        expandir(n)

#!/usr/bin/env python3
"""DT · pendones 0,8×3 m — RONDA 4 (Eli, 29-09): la foto a la medida del pendón.

Eli ajustó a mano la bata en el .ai (foto más grande, velos más suaves, titular sobre
el QR) y pidió para las tres: «expandir la fotografía a la medida del pendón… que la
imagen choque casi en todo para que se vea la persona», velos «más sutiles, como la
referencia», y que el titular se lea mejor. La cookie cambia de foto: la de la
referencia es la 3-79 (galleta ya partida, un trozo en la mano), no la 3-80.

Cada foto se EXPANDE con Flux Pro de Freepik hasta la proporción del pendón con
sangrado (82 × 302 cm = 1 : 3,683) y encima se pega la foto aprobada con borde suave:
la persona son los píxeles de la sesión (con las caras r3), la IA sólo agrega muro,
fachada, cama o piso — salvo en la cookie, donde la cara queda fuera de cuadro y la
genera la expansión (así deja de ser la modelo, R-95).

    python scripts/dt-pendones-expandir.py            # las tres
    python scripts/dt-pendones-expandir.py cookie     # una
"""
import sys
from pathlib import Path

from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import magnific as M  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
R = RAIZ / 'raw/hilton/dt/pendones-2026'
TMP = R / 'r4'
SESION = Path('F:/SESIONES HILTON/SESION DE FOTOS DT/sesion modelos DT')
PROP = 8560 / 2324          # alto / ancho del pendón con sangrado, en pt

# x0..x1 = ventana horizontal en px de la foto de 1500×2250 (x0 < 0 → se expande a la izq.)
# arriba = px que se agregan arriba; abajo sale de completar la proporción
PENDONES = {
    'bata': {
        'src': R / 'final4-297.png', 'x0': 351, 'x1': 1141, 'arriba': 451,
        'prompt': 'bright hotel bedroom: above, more of the same beige upholstered headboard '
                  'and warm beige wall, soft daylight; below, more of the same white duvet and '
                  'white bed sheets. No text, no letters, no other people.',
    },
    'telefono': {
        'src': R / 'final3-173a.png', 'x0': 150, 'x1': 940, 'arriba': 580,
        'prompt': 'above: more of the same modern hotel glass facade with dark metal frames, '
                  'green trees reflected in the glass, bright daylight; below: more of the same '
                  'light stone tiled sidewalk. No text, no letters, no signs, nobody else.',
    },
    'cookie': {
        'src': SESION / 'sesion_3-79.jpg', 'x0': -50, 'x1': 1100, 'arriba': 1600,
        'prompt': 'the same smiling young woman, her full face visible: natural relaxed eyes '
                  'looking slightly to the side (not at the camera), shoulder-length wavy auburn '
                  'red hair, natural makeup, same cream blazer and white top; softly blurred dark '
                  'hotel lobby behind her, shallow depth of field, photorealistic, natural skin. '
                  'Nobody else.',
    },
}


def expandir(nombre, forzar=False):
    e = PENDONES[nombre]
    foto = Image.open(e['src']).convert('RGB')
    assert foto.size == (1500, 2250), foto.size
    x0, x1 = e['x0'], e['x1']
    izq, der = max(0, -x0), max(0, x1 - 1500)
    base = foto.crop((max(0, x0), 0, min(1500, x1), 2250))
    w = x1 - x0
    H = round(w * PROP)
    arriba = e['arriba']
    abajo = H - 2250 - arriba
    assert abajo >= 0, (nombre, abajo)

    TMP.mkdir(parents=True, exist_ok=True)
    entrada = TMP / f'{nombre}-entrada.jpg'
    base.save(entrada, quality=95)
    crudo = TMP / f'{nombre}-expandida.jpg'
    if forzar or not crudo.exists():
        print(f'→ {nombre}: {w}×{H} · arriba {arriba} · abajo {abajo} · izq {izq} · der {der}')
        r = M.pedir('/v1/ai/image-expand/flux-pro', {
            'image': M.b64_de(entrada), 'prompt': e['prompt'],
            'left': izq, 'right': der, 'top': arriba, 'bottom': abajo,
        })
        tid = r.get('data', r).get('task_id')
        M.guarda(M.espera('/v1/ai/image-expand/flux-pro', tid), crudo)

    exp = Image.open(crudo).convert('RGB')
    if exp.size != (w, H):
        # Freepik devuelve a menor resolución y con la proporción un poco corrida: se escala
        # por el ancho y la foto original se ubica por correlación (no se estira el lienzo)
        import cv2
        import numpy as np
        s = w / exp.width
        exp = exp.resize((w, round(exp.height * s)), Image.LANCZOS)
        g = lambda im: cv2.cvtColor(np.asarray(im.resize((im.width // 4, im.height // 4))), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(g(exp), g(base), cv2.TM_CCOEFF_NORMED)
        _, score, _, (mx, my) = cv2.minMaxLoc(res)
        dy = my * 4 - arriba
        print(f'  (volvió a {1/s:.0%}; calce {score:.3f}, corrimiento vertical {dy} px)')
        lienzo = Image.new('RGB', (w, H))
        lienzo.paste(exp, (0, -dy))
        if exp.height - dy < H:   # si falta abajo, se estira sólo la última franja expandida
            falta = exp.crop((0, exp.height - 40, w, exp.height)).resize((w, H - (exp.height - dy) + 40))
            lienzo.paste(falta, (0, exp.height - dy - 40))
        exp = lienzo

    # la foto aprobada encima, con borde suave sólo donde toca lo expandido
    borde = 36
    m = Image.new('L', base.size, 255)
    negro = Image.new('L', base.size, 0)
    interior = Image.new('L', (base.width - (borde if izq else 0) - (borde if der else 0),
                               base.height - (borde if arriba else 0) - (borde if abajo else 0)), 255)
    negro.paste(interior, (borde if izq else 0, borde if arriba else 0))
    m = negro.filter(ImageFilter.GaussianBlur(borde / 2))
    # los lados sin expansión quedan opacos hasta el filo
    px = m.load()
    for y in range(base.height):
        for x in list(range(0, borde)) * (not izq) + list(range(base.width - borde, base.width)) * (not der):
            px[x, y] = 255 if (not arriba or y >= borde) and (not abajo or y < base.height - borde) else px[x, y]
    exp.paste(base, (izq, arriba), m)
    salida = TMP / f'{nombre}-lienzo.png'
    exp.save(salida)
    print(f'  ✓ {salida.relative_to(RAIZ)}  {exp.size}')
    return salida


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    for n in (args or PENDONES):
        expandir(n, forzar='--forzar' in sys.argv)

#!/usr/bin/env python3
"""
BETWEEN · septiembre 2026 — escenas que pide la RONDA 4 del cliente (27-08).

Solo se genera lo que NO existe en el banco de fotos del cliente. Todo lo demás
de esta ronda se resolvió con fotografía real (ver BetweenSeptiembre.tsx).

  togo-trio-45      K15 · «poner un dulce y un salado en la foto y que el vaso
                    sea como el del resto de las slides». Ninguna foto del banco
                    trae los tres juntos y las que hay son apaisadas: no dan un
                    4:5 con vaso + salado + dulce. Se genera el bodegón vertical
                    y el logo se estampa después con between-logo-vaso.py, que
                    es la única forma de que el vaso salga con marca.

  togo-salida-2     K15 · «ella se ve muy derrotada y el fondo no es muy
                    Between, veamos opciones?». La actitud cambia a alguien que
                    sale contento y el fondo pasa a ser una cafetería de madera
                    y plantas — la ambientación real del local.

  humor-cafecito-2  F15 · «Tenemos que modificar el aspecto de estas modelos, ya
                    no las podemos usar tal cual». Persona distinta, y encuadre
                    que NO depende del rostro: la referencia que dejó el propio
                    cliente para el cumpleaños resuelve la escena con torso y
                    manos, sin cara.

  emergencia-caja-2 I15 · «No se cacha bien al tapar la vitrina con el texto,
                    veamos otra diagramación?». La referencia del cliente es una
                    vitrina de emergencia FRONTAL sobre fondo plano, con el
                    producto solo y centrado y el texto en las bandas del marco.
                    La escena anterior era un gabinete lejano lleno de props.

Uso:  python3 scripts/between-ia-ronda4.py [nombre ...]
      (sin argumentos genera las cuatro)
"""
import base64
import json
import os
import pathlib
import ssl
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, cargar_env as _cargar_env  # noqa: E402

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

DEST = pathlib.Path(str(_RAIZ / 'public/assets/hilton/between/ia-sept'))

KEY = os.environ.get('FREEPIK_API_KEY', '')
if not KEY:
    _cargar_env()
    KEY = os.environ.get('FREEPIK_API_KEY', '')
if not KEY:
    sys.exit('Falta FREEPIK_API_KEY (vive en ASISTENTE PERSONAL/.env)')

H = {'x-freepik-api-key': KEY, 'Content-Type': 'application/json'}

# El vaso se pide SIN marca a propósito: la IA inventa logotipos falsos. La marca
# se estampa después con el logotipo real (between-logo-vaso.py).
VASO = ('a plain kraft brown paper takeaway coffee cup with a matte black plastic '
        'lid and a clean unbranded surface, no logo, no text on the cup')
LUZ = ('soft warm natural daylight from the side, gentle realistic shadows, '
       'nothing blown out, warm inviting colour, photorealistic food photography, '
       'sharp focus, shallow depth of field. No text, no logos, no watermark, '
       'no lettering anywhere in the image.')
LOCAL = ('a warm specialty coffee shop interior with honey-toned wooden furniture '
         'and abundant green plants softly blurred in the background')

ESCENAS = {
    'togo-trio-45': dict(
        ratio='social_post_4_5',
        prompt=(
            f'Vertical still life photograph on a warm honey-brown wooden cafe table, '
            f'shot slightly from above at a natural eating height. On the table: '
            f'{VASO} standing upright at the back right; a round sage-green ceramic '
            f'plate at the centre holding one golden croissant sandwich filled with '
            f'ham and melted cheese; and, closer to the camera at the front left, a '
            f'smaller grey ceramic plate holding two flaky sugar-dusted plain '
            f'croissants. The three items are clearly separated and all fully '
            f'visible. Background: {LOCAL}. {LUZ}'
        ),
    ),
    'togo-salida-2': dict(
        ratio='social_post_4_5',
        prompt=(
            'Vertical photograph of a cheerful young woman walking out through the '
            'open wooden door of a warm specialty coffee shop into soft morning '
            f'light, seen from the front. She is smiling with a relaxed happy '
            f'expression, looking ahead, holding {VASO} in one hand and a small kraft '
            'paper takeaway bag in the other. Behind her, clearly visible through the '
            'doorway, the inside of the cafe: warm honey-toned wood, green plants and '
            'soft golden lamps. She is mid-stride and full of energy, in a hurry but '
            f'happy. {LUZ}'
        ),
    ),
    'humor-cafecito-2': dict(
        ratio='social_post_4_5',
        prompt=(
            'Vertical lifestyle photograph framed from the chest down to the table. '
            'The head and the face are completely OUTSIDE the frame, above the top '
            'edge — no face, no chin, no mouth, nobody looking at the camera. '
            'Visible: the torso of a person wearing a soft cream knit sweater, '
            'seated at a warm wooden cafe table, both hands wrapped around a small '
            'white ceramic cappuccino cup on a saucer, lifting it a little off the '
            'table. Beside it on the table, a plate with a golden croissant. '
            f'Background: {LOCAL}. Cosy, calm and unhurried. {LUZ}'
        ),
    ),
    'emergencia-caja-2': dict(
        ratio='social_story_9_16',
        prompt=(
            'Flat head-on product photograph, camera perfectly perpendicular to the '
            'wall, zero perspective, perfectly symmetrical: a wall-mounted emergency '
            'break-glass cabinet, exactly centred in the frame, occupying the middle '
            'two thirds of the image. Its outer frame is a slim warm taupe-brown '
            'rectangle. The whole front is covered by a sheet of clean glass with a '
            'single soft diagonal reflection across it, so it clearly reads as glass. '
            f'Behind the glass, in the CENTRE of the cabinet: {VASO} standing upright '
            'next to one golden croissant on a small white plate, both large, sharp '
            'and appetising. The cabinet interior is a plain warm cream panel, and '
            'above the products there is a wide band of completely empty cream space '
            'inside the cabinet. The wall around the cabinet is flat, even, warm '
            'cream, with a soft drop shadow beneath, and nothing else at all: no '
            'plants, no furniture, no shelves, no extra cups, no objects, no hooks. '
            f'Minimal, graphic, symmetrical. {LUZ}'
        ),
    ),
}


def http(url, method='GET', body=None, timeout=180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=H, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw.decode(errors='ignore')


def dig(obj, want_url=True):
    if isinstance(obj, str):
        if want_url and obj.startswith('http'):
            return obj
        if not want_url and len(obj) > 5000 and not obj.startswith('http'):
            return obj
        return None
    if isinstance(obj, dict):
        for v in obj.values():
            f = dig(v, want_url)
            if f:
                return f
    if isinstance(obj, list):
        for v in obj:
            f = dig(v, want_url)
            if f:
                return f
    return None


def poll(base, task_id, label):
    for _ in range(90):
        st, data = http(f'{base}/{task_id}')
        d = data.get('data', {}) if isinstance(data, dict) else {}
        if d.get('status') in ('COMPLETED', 'SUCCESS'):
            return dig(data, True) or dig(data, False)
        if d.get('status') == 'FAILED':
            print(f'  [{label}] falló: {json.dumps(data)[:300]}')
            return None
        time.sleep(5)
    print(f'  [{label}] timeout')
    return None


def generar(nombre, cfg):
    base = 'https://api.freepik.com/v1/ai/mystic'
    st, data = http(base, 'POST', {
        'prompt': cfg['prompt'],
        'aspect_ratio': cfg['ratio'],
        'resolution': '2k',
        'realism': True,
        'engine': 'automatic',
    })
    print(f'  [{nombre}] mystic -> HTTP {st}')
    if st not in (200, 201):
        print(f'  {json.dumps(data)[:400]}')
        return None
    return poll(base, data.get('data', {}).get('task_id'), nombre)


def guardar(res, path):
    if not res:
        return False
    if res.startswith('http'):
        with urllib.request.urlopen(res, timeout=180, context=SSL_CTX) as r:
            path.write_bytes(r.read())
    else:
        path.write_bytes(base64.b64decode(res))
    print(f'    guardado {path.name} ({path.stat().st_size // 1024} KB)')
    return True


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    pedidas = sys.argv[1:] or list(ESCENAS)
    for i, nombre in enumerate(pedidas, start=1):
        if nombre not in ESCENAS:
            print(f'{nombre}: no está definida'); continue
        print(f'\n{i}/{len(pedidas)} — {nombre}')
        guardar(generar(nombre, ESCENAS[nombre]), DEST / f'{nombre}.png')
    print(f'\nListo en {DEST}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pendones DT 0,8 × 3 m — ronda 9: alta resolución para imprenta (30-09-2026).

Eli agrandó las fotos dentro del .ai (chica de la entrada 137,6 cm de ancho, cookie 98,8 cm)
y con eso los vínculos quedaron a 60 y 83 ppp efectivos. Este script rehace los vínculos con
el DOBLE (chica) o 1,5 veces (cookie) de píxeles y el ppp declarado en la misma proporción:
el tamaño físico no cambia, así que en el .ai sólo se cambia `placedItem.file`.

Sólo se escala con IA la ventana que se ve en el pendón (más margen); lo que queda fuera de
la mesa se agranda con Lanczos. Las letras (letrero DOUBLETREE, bolsa) se revisan aparte:
el upscaler puede reescribirlas.

    python scripts/dt-pendones-alta-r9.py prueba   <recorte.png> <salida.png> [--v1]
    python scripts/dt-pendones-alta-r9.py franjas  tel|cookie
    python scripts/dt-pendones-alta-r9.py montar   tel|cookie
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import magnific as M  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
T = RAIZ / 'raw/hilton/dt/pendones-2026'


def escalar(entrada, salida, v1=False):
    if v1:
        ruta, cuerpo = '/v1/ai/image-upscaler-precision', {'image': M.b64_de(entrada)}
    else:
        ruta = '/v1/ai/image-upscaler-precision-v2'
        cuerpo = {'image': M.b64_de(entrada), 'scale_factor': 2, 'flavor': 'photo',
                  'sharpen': 7, 'smart_grain': 7, 'ultra_detail': 20}
    print(f'→ {ruta} · {Path(entrada).name}', flush=True)
    r = M.pedir(ruta, cuerpo)
    M.guarda(M.espera(ruta, r['data']['task_id'], minutos=15), salida)


# ── Franjas. El precision falla sin imagen con entradas grandes (r4 y r8): se parte en franjas
# horizontales con traslape, se escala cada una en paralelo y se cose con mezcla lineal.
# Cada franja se amarra en tono al Lanczos de la versión aprobada (sólo baja frecuencia, σ 24):
# la IA pone el detalle, el color sigue siendo el que Eli aprobó.
import cv2  # noqa: E402
import numpy as np  # noqa: E402
from concurrent.futures import ThreadPoolExecutor  # noqa: E402
from PIL import Image, ImageCms  # noqa: E402
Image.MAX_IMAGE_PIXELS = None

R8, R9 = T / 'r8', T / 'r9'
LINKS = Path('F:/SOLICITUDES 2026 HILTON/Pendon editable 2026 0,8x3m/Pendones 2026 caras nuevas/Links')
FOGRA = ImageCms.getOpenProfile(r'C:/Program Files/Common Files/Adobe/Color/Profiles/Recommended/CoatedFOGRA39.icc')

# pieza: (origen RGB, caja escalada con IA en px del origen)
# tel:    vínculo r8 3228×7170 a 137,6 cm; se ve x 433..2309 → caja con 150 px de margen.
# cookie: la ventana real de la 3-79 ya a ×2 (2120×4500); se ve entera.
PIEZAS = {
    'tel': (R8 / 'tel-r8-rgb.png', (283, 0, 2459, 7170)),
    'cookie': (R8 / '3-79-ventana-x2.png', None),
}
ALTO, TRASLAPE = 1600, 320


def cortes(h):
    ys, y = [], 0
    while True:
        y1 = min(y + ALTO, h)
        ys.append((y, y1))
        if y1 == h:
            return ys
        y = y1 - TRASLAPE


def franjas(pieza):
    src, caja = PIEZAS[pieza]
    im = Image.open(src).convert('RGB')
    if caja:
        im = im.crop(caja)
    im.save(R9 / f'{pieza}-caja.png')
    tareas = []
    for i, (y0, y1) in enumerate(cortes(im.height)):
        ent, sal = R9 / f'{pieza}-f{i}.png', R9 / f'{pieza}-f{i}-x2.png'
        if not sal.exists():
            im.crop((0, y0, im.width, y1)).save(ent)
            tareas.append((ent, sal))
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(lambda t: escalar(*t), tareas))


def coser(pieza):
    caja = np.asarray(Image.open(R9 / f'{pieza}-caja.png').convert('RGB'))
    h, w = caja.shape[:2]
    out = np.zeros((h * 2, w * 2, 3), np.float32)
    peso = np.zeros((h * 2, 1, 1), np.float32)
    ref = cv2.resize(caja, (w * 2, h * 2), interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
    cs = cortes(h)
    for i, (y0, y1) in enumerate(cs):
        f = np.asarray(Image.open(R9 / f'{pieza}-f{i}-x2.png').convert('RGB')).astype(np.float32)
        Y0, Y1 = y0 * 2, y1 * 2
        if f.shape[:2] != (Y1 - Y0, w * 2):
            f = cv2.resize(f, (w * 2, Y1 - Y0), interpolation=cv2.INTER_LANCZOS4)
        r = ref[Y0:Y1]
        f = f + cv2.GaussianBlur(r - f, (0, 0), 24)          # tono amarrado a lo aprobado
        a = np.ones(Y1 - Y0, np.float32)
        t = TRASLAPE * 2
        if i > 0:
            a[:t] = np.linspace(0, 1, t)
        if i < len(cs) - 1:
            a[-t:] = np.linspace(1, 0, t)
        out[Y0:Y1] += f * a[:, None, None]
        peso[Y0:Y1] += a[:, None, None]
    out = (out / np.maximum(peso, 1e-6)).clip(0, 255).astype(np.uint8)
    Image.fromarray(out).save(R9 / f'{pieza}-x2.png')
    return out


def guardar(img, nombre, ppp):
    t = ImageCms.buildTransform(ImageCms.createProfile('sRGB'), FOGRA, 'RGB', 'CMYK', renderingIntent=1)
    ImageCms.applyTransform(img, t).save(LINKS / nombre, quality=90, dpi=(ppp, ppp),
                                         icc_profile=FOGRA.tobytes())
    print(f'  ✓ Links/{nombre}  {img.size}  {ppp} ppp declarados')


def montar_tel():
    """Vínculo ×2 (6456×14340 a 200 ppp = mismo tamaño físico que el r8 a 100 ppp)."""
    x2 = coser('tel')
    base = Image.open(R8 / 'tel-r8-rgb.png').convert('RGB')
    lien = np.asarray(base.resize((base.width * 2, base.height * 2), Image.LANCZOS)).copy()
    x0, y0, x1, y1 = [v * 2 for v in PIEZAS['tel'][1]]
    # rampa de 120 px a los lados (quedan fuera de la mesa, pero sin costura por si Eli mueve la foto)
    a = np.ones(x1 - x0, np.float32); a[:120] = np.linspace(0, 1, 120); a[-120:] = np.linspace(1, 0, 120)
    a = a[None, :, None]
    lien[y0:y1, x0:x1] = (x2 * a + lien[y0:y1, x0:x1] * (1 - a)).astype(np.uint8)
    img = Image.fromarray(lien); img.save(R9 / 'tel-r9-rgb.png')
    guardar(img, 'pendon-2-telefono-r9.jpg', 200)


def montar_cookie():
    """Como `cookie()` de la r8, a 1,5×: 4842×17835 a 150 ppp = mismo tamaño físico."""
    S = 1.5
    PX_CM, MESA_X, MESA_Y = 32.66 * S, 224 * S, 894 * S
    AZUL = (32, 32, 73)
    WL, HL = round(3228 * S), round(11890 * S)
    foto_x2 = coser('cookie')                                   # 4240×9000 = x 180..1240 de la 3-79 ×4
    W, H = round(82 * PX_CM), round(2250 * 82 * PX_CM / 1060)
    foto = cv2.resize(foto_x2, (W, H), interpolation=cv2.INTER_AREA).astype(np.float32)
    ox, oy = round(MESA_X - PX_CM), round(MESA_Y + 40 * PX_CM)
    lien = np.zeros((HL, WL, 3), np.float32); lien[:] = AZUL
    a = np.ones(H, np.float32)
    ra, rb = round(18 * PX_CM), round(14 * PX_CM)
    a[:ra] = np.linspace(0, 1, ra) ** 1.5
    a[-rb:] = np.linspace(1, 0, rb) ** 1.5
    x0, x1, y0, y1 = max(ox, 0), min(ox + W, WL), max(oy, 0), min(oy + H, HL)
    al = a[y0 - oy:y1 - oy, None, None]
    lien[y0:y1, x0:x1] = foto[y0 - oy:y1 - oy, x0 - ox:x1 - ox] * al + lien[y0:y1, x0:x1] * (1 - al)
    img = Image.fromarray(lien.clip(0, 255).astype(np.uint8)); img.save(R9 / 'cookie-r9-rgb.png')
    guardar(img, 'pendon-3-cookie-r9.jpg', 150)


if __name__ == '__main__':
    acc = sys.argv[1]
    if acc == 'prueba':
        escalar(sys.argv[2], sys.argv[3], v1='--v1' in sys.argv)
    elif acc == 'franjas':
        franjas(sys.argv[2])
    elif acc == 'montar':
        {'tel': montar_tel, 'cookie': montar_cookie}[sys.argv[2]]()

#!/usr/bin/env python3
"""DT · pendones r4 — la cookie en DOS pasos. En un solo paso de 1.600 px hacia arriba,
Flux compuso un retrato aparte encima de la foto (dos bocas). Aquí primero se completa la
cabeza desde la sonrisa (paso 1, poco alto) y después el fondo sobre esa cabeza (paso 2)."""
import sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent))
import magnific as M  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
TMP = RAIZ / 'raw/hilton/dt/pendones-2026/r4'
SESION = Path('F:/SESIONES HILTON/SESION DE FOTOS DT/sesion modelos DT')

PASOS = [
    ('cookie-p1', 700, 'continuation of the same photo upward: the rest of the same woman\'s face '
     'above her smile — nose, relaxed natural eyes looking slightly to the side, eyebrows, forehead '
     'and wavy auburn red hair to the shoulders, same soft focus and warm light, same blurred dark '
     'wall behind. One single continuous photograph, one person.'),
    ('cookie-p2', 900, 'continuation of the same photo upward: the top of her auburn hair and the '
     'softly blurred dark hotel lobby wall above, same soft focus. One single continuous photograph, '
     'nobody else, no text.'),
]

def paso(entrada, nombre, arriba, prompt, izq=0, abajo=0):
    crudo = TMP / f'{nombre}.jpg'
    if not crudo.exists():
        print(f'→ {nombre}: arriba {arriba} izq {izq} abajo {abajo}')
        r = M.pedir('/v1/ai/image-expand/flux-pro', {'image': M.b64_de(entrada), 'prompt': prompt,
                    'left': izq, 'right': 0, 'top': arriba, 'bottom': abajo})
        M.guarda(M.espera('/v1/ai/image-expand/flux-pro', r.get('data', r).get('task_id')), crudo)
    return crudo

if __name__ == '__main__' and len(sys.argv) == 1:
    foto = Image.open(SESION / 'sesion_3-79.jpg').convert('RGB').crop((0, 0, 1100, 2250))
    e0 = TMP / 'cookie-p0.jpg'; foto.save(e0, quality=95)
    c1 = paso(e0, *PASOS[0], izq=50)
    print(Image.open(c1).size)


# ── Paso NB (29-09): Flux inventó un letrero con texto sobre la boca. Nano Banana Pro
# completa sobre un LIENZO 9:16: la foto real abajo, gris neutro arriba y a la izquierda.
IZQ, ARRIBA_NB, TROZO = 150, 1522, 700      # ventana x −150..1100 → 1250 px de ancho

def lienzo_nb():
    foto = Image.open(SESION / 'sesion_3-79.jpg').convert('RGB')
    W = 1100 + IZQ
    Hc = round(W * 16 / 9)
    c = Image.new('RGB', (W, Hc), (128, 128, 128))
    c.paste(foto.crop((0, 0, 1100, TROZO)), (IZQ, Hc - TROZO))
    ruta = TMP / 'cookie-nb-lienzo.png'
    c.save(ruta)
    return ruta, Hc

PROMPT_NB = ('Photo outpainting. Replace ONLY the flat gray area of this image with a seamless '
             'continuation of the same photograph; keep every non-gray pixel exactly as it is. '
             'Above the smiling mouth, complete the same young woman\'s face: nose, natural relaxed '
             'eyes looking slightly to the side (not at the camera), eyebrows, forehead and '
             'shoulder-length wavy light-brown hair matching the hair strands already visible, her '
             'neck and the collar of the same cream blazer. Behind her, the same softly blurred '
             'dark hotel lobby wall with a faint large white tree emblem, shallow depth of field, '
             'same warm light, same soft focus as the mouth. Photorealistic, natural skin texture, '
             'one single person, no text, no letters, no frames or borders.')

if __name__ == '__main__' and '--nb' in sys.argv:
    import subprocess
    ruta, Hc = lienzo_nb()
    out = TMP / 'cookie-nb.png'
    if not out.exists():
        subprocess.run([sys.executable, str(Path(__file__).parent / 'magnific.py'), 'pro', PROMPT_NB,
                        '--out', str(out), '--aspecto', 'story', '--refs', str(ruta)], check=True)
    print(Image.open(out).size, 'lienzo', (1100 + IZQ, Hc))


# ── Paso NB2: menos gris. La foto ENTERA al 80 % abajo y centrada en un 9:16 de 1500 px;
# gris arriba (≈1.080 px de la original) y 150 px por lado. Después se calza la original
# encima por homografía y la costura va en el cuello, no en la boca.
def lienzo_nb2():
    foto = Image.open(SESION / 'sesion_3-79.jpg').convert('RGB')
    W, Hc = 1500, 2667
    f = foto.resize((1200, 1800), Image.LANCZOS)
    c = Image.new('RGB', (W, Hc), (128, 128, 128))
    c.paste(f, (150, Hc - 1800))
    ruta = TMP / 'cookie-nb2-lienzo.png'
    c.save(ruta)
    return ruta

PROMPT_NB2 = ('Photo outpainting, zoom-out of this exact photograph. Keep the existing photo area '
              'EXACTLY as it is, same position and size: the hand holding a broken cookie piece, the '
              'purple DoubleTree cookie bag, the cream blazer, the smile. Replace ONLY the flat gray '
              'padding (top and both sides) with its seamless continuation: above her smiling mouth '
              'complete the same young woman\'s face — nose, natural relaxed eyes looking slightly to '
              'the side (not at the camera), eyebrows, forehead, shoulder-length wavy light-brown hair '
              'matching the strands already visible; on the sides more of her cream blazer and the '
              'softly blurred dark hotel lobby wall. Same warm light, same shallow depth of field, '
              'photorealistic natural skin, one single person, no text, no borders.')

if __name__ == '__main__' and '--nb2' in sys.argv:
    import subprocess
    ruta = lienzo_nb2()
    out = TMP / 'cookie-nb2.png'
    if not out.exists():
        subprocess.run([sys.executable, str(Path(__file__).parent / 'magnific.py'), 'pro', PROMPT_NB2,
                        '--out', str(out), '--aspecto', 'story', '--refs', str(ruta)], check=True)
    print(Image.open(out).size)


# ── Paso NB3: con la boca en el lienzo la IA pone una cara ENTERA encima (dos bocas). Se
# corta la original bajo el mentón (y ≥ CORTE) y la cara se genera completa; la costura
# queda en el cuello y el cuello de la chaqueta.
CORTE = 190

def lienzo_nb3():
    foto = Image.open(SESION / 'sesion_3-79.jpg').convert('RGB').crop((0, CORTE, 1500, 2250))
    W, Hc = 1500, 2667
    f = foto.resize((1200, round(1200 * foto.height / 1500)), Image.LANCZOS)
    c = Image.new('RGB', (W, Hc), (128, 128, 128))
    c.paste(f, (150, Hc - f.height))
    ruta = TMP / 'cookie-nb3-lienzo.png'
    c.save(ruta)
    return ruta

PROMPT_NB3 = ('Photo outpainting, zoom-out of this exact photograph. Keep the existing photo area '
              'EXACTLY as it is, same position and size (the hand holding a broken cookie piece, the '
              'purple DoubleTree cookie bag, the cream blazer). Replace ONLY the flat gray padding with '
              'its seamless continuation: the same young woman\'s neck with a thin gold necklace and '
              'her whole head above it — a warm natural smile, natural relaxed eyes looking slightly to '
              'the side (not at the camera), shoulder-length wavy light-brown hair continuing the '
              'strands already visible; on the sides more of her cream blazer and the softly blurred '
              'dark hotel lobby wall. Same warm light, same shallow depth of field, photorealistic '
              'natural skin, exactly one person with one face, no text, no borders.')

if __name__ == '__main__' and '--nb3' in sys.argv:
    import subprocess
    ruta = lienzo_nb3()
    out = TMP / 'cookie-nb3.png'
    if not out.exists():
        subprocess.run([sys.executable, str(Path(__file__).parent / 'magnific.py'), 'pro', PROMPT_NB3,
                        '--out', str(out), '--aspecto', 'story', '--refs', str(ruta)], check=True)
    print(Image.open(out).size)


# ── Montaje: la IA redibuja todo (y el rótulo de la bolsa sale con letras inventadas, R-80).
# Se calza la ORIGINAL sobre la NB3 por homografía (SIFT) y se repone sólo lo que es producto
# y manos: bolsa, galleta, trozo y las dos manos. Cara, pelo, chaqueta y fondo quedan de la NB3.
ZONAS = [(0, 230, 650, 450),      # mano con el trozo y el anillo
         (410, 315, 1115, 2020),  # bolsa + galleta
         (690, 1180, 1260, 1690)] # mano derecha

def montar():
    import cv2
    import numpy as np
    nb = cv2.cvtColor(np.asarray(Image.open(TMP / 'cookie-nb3.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    og = cv2.imread(str(SESION / 'sesion_3-79.jpg'))
    sift = cv2.SIFT_create(6000)
    ka, da = sift.detectAndCompute(cv2.cvtColor(og, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    buenos = [a for a, b in m if a.distance < 0.72 * b.distance]
    pa = np.float32([ka[g.queryIdx].pt for g in buenos])
    pb = np.float32([kb[g.trainIdx].pt for g in buenos])
    Hm, inl = cv2.findHomography(pa, pb, cv2.RANSAC, 4.0)
    print(f'  homografía con {int(inl.sum())}/{len(buenos)} puntos')
    h, w = nb.shape[:2]
    warp = cv2.warpPerspective(og, Hm, (w, h), flags=cv2.INTER_LANCZOS4)
    mask = np.zeros(og.shape[:2], np.float32)
    for x0, y0, x1, y1 in ZONAS:
        mask[y0:y1, x0:x1] = 1
    mw = cv2.warpPerspective(mask, Hm, (w, h))
    mw = cv2.GaussianBlur(mw, (0, 0), 14)[..., None]
    out = warp * mw + nb * (1 - mw)
    cv2.imwrite(str(TMP / 'cookie-montada.png'), out.clip(0, 255).astype(np.uint8))
    cv2.imwrite(str(TMP / 'cookie-montada-mascara.png'), (mw[..., 0] * 255).astype(np.uint8))
    return Hm

if __name__ == '__main__' and '--montar' in sys.argv:
    print(montar())


# ── Encuadre al pendón (1 : 3,683) con el titular donde lo dejó Eli en la 2 (17,6–27,8 %):
# ojos ≈ 30 %, mentón 40 %, bolsa 52–70 % (el QR parte en 67 %). En px de la NB3:
# ventana x 200..1416 (1.216) → alto 4.480; se agregan 776 arriba y 952 abajo.
VX0, VW, ARR, ABA = 200, 1216, 776, 952

def encuadrar():
    base = Image.open(TMP / 'cookie-montada.png').convert('RGB').crop((VX0, 0, VX0 + VW, 2752))
    e = TMP / 'cookie-marco-entrada.jpg'; base.save(e, quality=95)
    crudo = paso(e, 'cookie-marco-expandida', ARR,
                 'continuation of the same photograph: above, more of the same softly blurred dark '
                 'hotel lobby wall and ceiling with warm spot lights; below, more of the same cream '
                 'blazer and white trousers, softly blurred. No text, no letters, no signs, no faces, '
                 'nobody else.', abajo=ABA)
    import cv2
    import numpy as np
    exp = Image.open(crudo).convert('RGB')
    H = ARR + 2752 + ABA
    s = VW / exp.width
    exp = exp.resize((VW, round(exp.height * s)), Image.LANCZOS)
    g = lambda im: cv2.cvtColor(np.asarray(im.resize((im.width // 4, im.height // 4))), cv2.COLOR_RGB2GRAY)
    _, sc, _, (mx, my) = cv2.minMaxLoc(cv2.matchTemplate(g(exp), g(base), cv2.TM_CCOEFF_NORMED))
    dy = my * 4 - ARR
    print(f'  expansión al {1/s:.0%}, calce {sc:.3f}, corrimiento {dy}')
    lienzo = Image.new('RGB', (VW, H)); lienzo.paste(exp, (0, -dy))
    from PIL import ImageFilter
    borde = 36
    m = Image.new('L', base.size, 0)
    m.paste(Image.new('L', (VW, 2752 - 2 * borde), 255), (0, borde))
    m = m.filter(ImageFilter.GaussianBlur(borde / 2))
    lienzo.paste(base, (0, ARR), m)
    lienzo.save(TMP / 'cookie-lienzo.png')
    print('  ✓ cookie-lienzo.png', lienzo.size)

if __name__ == '__main__' and '--encuadrar' in sys.argv:
    encuadrar()


# ── Flux arma collages (otra mujer arriba y abajo) en expansiones grandes: se descarta.
# Arriba va detrás del logo (muro oscuro desenfocado) y abajo detrás del QR con velo: se
# rellena REFLEJANDO el propio borde de la foto y desenfocando más a medida que se aleja.
def encuadrar_reflejo():
    import numpy as np
    from PIL import ImageFilter
    base = Image.open(TMP / 'cookie-montada.png').convert('RGB').crop((VX0, 0, VX0 + VW, 2752))
    H = ARR + 2752 + ABA
    L = Image.new('RGB', (VW, H))
    L.paste(base, (0, ARR))
    # reflejar traía la cabeza y la bolsa como fantasmas: se ESTIRA sólo la franja de muro
    # (arriba, sobre el pelo) y la de pantalón (abajo, bajo la bolsa)
    arr_src = base.crop((0, 0, VW, 110)).resize((VW, ARR + 220), Image.BICUBIC)
    aba_src = base.crop((0, 2752 - 160, VW, 2752)).resize((VW, ABA + 220), Image.BICUBIC)
    def degradar(im, lejos_arriba):
        capas = [im.filter(ImageFilter.GaussianBlur(r)) for r in (6, 24, 60)]
        a = [np.asarray(c).astype(np.float32) for c in capas]
        t = np.linspace(1, 0, im.height) if lejos_arriba else np.linspace(0, 1, im.height)
        t = t[:, None, None]
        out = np.where(t < .5, a[0] * (1 - 2 * t) + a[1] * 2 * t, a[1] * (2 - 2 * t) + a[2] * (2 * t - 1))
        return Image.fromarray(out.clip(0, 255).astype(np.uint8))
    L.paste(degradar(arr_src, True), (0, 0))
    L.paste(degradar(aba_src, False), (0, ARR + 2752 - 220))
    # costura: 40 px de mezcla hacia la foto
    m = Image.new('L', (VW, 2752), 255)
    m.paste(Image.new('L', (VW, 2752 - 80), 255), (0, 40))
    # mezcla ancha (el corte se notaba con 40 px): rampa lineal de 220 px en cada costura
    rampa = np.ones(2752, np.float32)
    rampa[:220] = np.linspace(0, 1, 220); rampa[-220:] = np.linspace(1, 0, 220)
    g = Image.fromarray((np.repeat(rampa[:, None], VW, 1) * 255).astype(np.uint8))
    L.paste(base, (0, ARR), g)
    L.save(TMP / 'cookie-lienzo.png')
    print('  ✓ cookie-lienzo.png', L.size)

if __name__ == '__main__' and '--reflejo' in sys.argv:
    encuadrar_reflejo()


# ── Montaje por ZONA: una sola homografía no sirve (la NB movió la mano respecto de la bolsa
# y el parche de la mano cayó en el cuello). Cada zona se calza con sus propios puntos
# (afín parcial: traslación, giro y escala) y se pega con su máscara difuminada.
ZONAS2 = {'mano':   (0, 245, 640, 440),
          'bolsa':  (415, 320, 1110, 2015),
          'manoder': (700, 1190, 1255, 1685)}

def montar_zonas():
    import cv2
    import numpy as np
    nb = cv2.cvtColor(np.asarray(Image.open(TMP / 'cookie-nb3.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    og = cv2.imread(str(SESION / 'sesion_3-79.jpg'))
    sift = cv2.SIFT_create(12000)
    ka, da = sift.detectAndCompute(cv2.cvtColor(og, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    buenos = [a for a, b in m if a.distance < 0.8 * b.distance]
    h, w = nb.shape[:2]
    out = nb.astype(np.float32)
    for nombre, (x0, y0, x1, y1) in ZONAS2.items():
        sel = [g for g in buenos if x0 - 60 <= ka[g.queryIdx].pt[0] <= x1 + 60 and y0 - 60 <= ka[g.queryIdx].pt[1] <= y1 + 60]
        if len(sel) < 12:   # la NB redibujó esa zona distinta: se queda la de la NB
            print(f'  {nombre}: sólo {len(sel)} puntos, queda la de la NB'); continue
        pa = np.float32([ka[g.queryIdx].pt for g in sel]); pb = np.float32([kb[g.trainIdx].pt for g in sel])
        A, inl = cv2.estimateAffinePartial2D(pa, pb, method=cv2.RANSAC, ransacReprojThreshold=3.0)
        s = np.hypot(A[0, 0], A[1, 0])
        print(f'  {nombre}: {int(inl.sum())}/{len(sel)} puntos · escala {s:.3f} · giro {np.degrees(np.arctan2(A[1,0], A[0,0])):.1f}°')
        warp = cv2.warpAffine(og, A, (w, h), flags=cv2.INTER_LANCZOS4).astype(np.float32)
        mk = np.zeros(og.shape[:2], np.float32); mk[y0:y1, x0:x1] = 1
        mk = cv2.GaussianBlur(cv2.warpAffine(mk, A, (w, h)), (0, 0), 10)[..., None]
        out = warp * mk + out * (1 - mk)
    cv2.imwrite(str(TMP / 'cookie-montada.png'), out.clip(0, 255).astype(np.uint8))

if __name__ == '__main__' and '--zonas' in sys.argv:
    montar_zonas()
    encuadrar_reflejo()


# ── Silueta en vez de rectángulos: el rectángulo traía el muro oscuro original sobre la
# chaqueta de la NB y dejaba asomar la bolsa (más ancha) de la NB. GrabCut sobre la
# original separa bolsa + galleta + mano derecha; lo que la bolsa NB asoma fuera de la
# real se rellena desde la chaqueta NB vecina (inpaint).
def silueta():
    import cv2
    import numpy as np
    og = cv2.imread(str(SESION / 'sesion_3-79.jpg'))
    x0, y0, x1, y1 = 405, 300, 1275, 2030
    mk = np.zeros(og.shape[:2], np.uint8)
    bg, fg = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(og, mk, (x0, y0, x1 - x0, y1 - y0), bg, fg, 6, cv2.GC_INIT_WITH_RECT)
    s = np.where((mk == 1) | (mk == 3), 255, 0).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(s)
    k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    s = np.where(lab == k, 255, 0).astype(np.uint8)
    s = cv2.morphologyEx(s, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    cv2.imwrite(str(TMP / 'cookie-silueta.png'), s)
    return s

def montar_silueta():
    import cv2
    import numpy as np
    s = silueta()
    nb = cv2.cvtColor(np.asarray(Image.open(TMP / 'cookie-nb3.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    og = cv2.imread(str(SESION / 'sesion_3-79.jpg'))
    sift = cv2.SIFT_create(12000)
    ka, da = sift.detectAndCompute(cv2.cvtColor(og, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    # puntos de la zona de la bolsa (el filtro por máscara de SIFT daba un afín degenerado)
    sel = [a for a, b in m if a.distance < 0.8 * b.distance
           and 355 <= ka[a.queryIdx].pt[0] <= 1170 and 260 <= ka[a.queryIdx].pt[1] <= 2075]
    pa = np.float32([ka[g.queryIdx].pt for g in sel]); pb = np.float32([kb[g.trainIdx].pt for g in sel])
    A, inl = cv2.estimateAffinePartial2D(pa, pb, method=cv2.RANSAC, ransacReprojThreshold=3.0)
    print(f'  silueta: {int(inl.sum())}/{len(sel)} puntos · escala {np.hypot(A[0,0],A[1,0]):.3f}')
    h, w = nb.shape[:2]
    warp = cv2.warpAffine(og, A, (w, h), flags=cv2.INTER_LANCZOS4)
    sw = cv2.warpAffine(s, A, (w, h))
    # la bolsa de la NB (morada) que queda FUERA de la real se borra y se rellena
    hsv = cv2.cvtColor(nb, cv2.COLOR_BGR2HSV)
    morado = cv2.inRange(hsv, (115, 40, 30), (160, 255, 200))
    verde = cv2.inRange(hsv, (35, 80, 60), (85, 255, 255))
    zona = cv2.dilate(sw, np.ones((151, 151), np.uint8))
    fuera = cv2.bitwise_and(cv2.bitwise_or(morado, verde), cv2.bitwise_and(zona, cv2.bitwise_not(sw)))
    fuera = cv2.dilate(fuera, np.ones((9, 9), np.uint8))
    base = cv2.inpaint(nb, fuera, 15, cv2.INPAINT_TELEA)
    a = cv2.GaussianBlur(cv2.erode(sw, np.ones((3, 3), np.uint8)).astype(np.float32) / 255, (0, 0), 2.5)[..., None]
    out = warp * a + base * (1 - a)
    cv2.imwrite(str(TMP / 'cookie-montada.png'), out.clip(0, 255).astype(np.uint8))
    print(f'  bolsa NB fuera de la real: {int((fuera > 0).sum())} px rellenados')

if __name__ == '__main__' and '--silueta' in sys.argv:
    montar_silueta()
    encuadrar_reflejo()


# ── Versión que queda: rectángulos (bolsa + mano derecha, un solo afín) pero SIN el muro
# oscuro de la original (ahí queda la chaqueta NB) y borrando la bolsa NB que asoma.
def montar_final():
    import cv2
    import numpy as np
    nb = cv2.cvtColor(np.asarray(Image.open(TMP / 'cookie-nb3.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    og = cv2.imread(str(SESION / 'sesion_3-79.jpg'))
    sift = cv2.SIFT_create(12000)
    ka, da = sift.detectAndCompute(cv2.cvtColor(og, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    sel = [a for a, b in m if a.distance < 0.8 * b.distance
           and 400 <= ka[a.queryIdx].pt[0] <= 1260 and 920 <= ka[a.queryIdx].pt[1] <= 2030]
    pa = np.float32([ka[g.queryIdx].pt for g in sel]); pb = np.float32([kb[g.trainIdx].pt for g in sel])
    A, inl = cv2.estimateAffinePartial2D(pa, pb, method=cv2.RANSAC, ransacReprojThreshold=3.0)
    print(f'  bolsa: escala {np.hypot(A[0,0],A[1,0]):.3f} giro {np.degrees(np.arctan2(A[1,0],A[0,0])):.1f}°')
    h, w = nb.shape[:2]
    rect = np.zeros(og.shape[:2], np.uint8)
    # ⚠️ coordenadas en px REALES de la 3-79 (la 1ª versión leyó la grilla a 1/3 en y)
    rect[1075:2060, 430:1110] = 255         # bolsa (con la franja verde entera)
    rect[935:1095, 530:965] = 255           # galleta que sobresale
    rect[1190:1690, 700:1255] = 255         # mano derecha
    hsv = cv2.cvtColor(og, cv2.COLOR_BGR2HSV)
    oscuro = ((hsv[..., 2] < 95) & (hsv[..., 1] < 110)).astype(np.uint8) * 255
    oscuro = cv2.morphologyEx(oscuro, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    toma = cv2.bitwise_and(rect, cv2.bitwise_not(oscuro))
    # sobre la bolsa sólo galleta y papel kraft (con color); el muro gris de atrás no
    gris = ((hsv[..., 1] < 45) & (np.arange(og.shape[0])[:, None] < 1085)).astype(np.uint8) * 255
    toma = cv2.bitwise_and(toma, cv2.bitwise_not(gris))
    toma = cv2.morphologyEx(toma, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    warp = cv2.warpAffine(og, A, (w, h), flags=cv2.INTER_LANCZOS4)
    tw = cv2.warpAffine(toma, A, (w, h))
    # bolsa NB que asoma fuera de la real → inpaint
    hsvn = cv2.cvtColor(nb, cv2.COLOR_BGR2HSV)
    # el muro NB es azul grisáceo y cae en «morado» con S≥40: se exige más saturación
    bolsa_nb = cv2.bitwise_or(cv2.inRange(hsvn, (118, 85, 45), (160, 255, 210)),
                              cv2.inRange(hsvn, (30, 60, 50), (90, 255, 255)))
    hsvw = cv2.cvtColor(warp, cv2.COLOR_BGR2HSV)
    bolsa_real = cv2.bitwise_or(cv2.inRange(hsvw, (115, 40, 30), (165, 255, 210)),
                                cv2.inRange(hsvw, (35, 90, 70), (85, 255, 255)))
    bolsa_real = cv2.bitwise_and(bolsa_real, tw)
    cerca = cv2.dilate(bolsa_real, np.ones((101, 101), np.uint8))   # sólo pegado a la bolsa real
    fuera = cv2.bitwise_and(bolsa_nb, cv2.bitwise_and(cerca, cv2.bitwise_not(cv2.dilate(bolsa_real, np.ones((7, 7), np.uint8)))))
    fuera = cv2.morphologyEx(fuera, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    fuera = cv2.dilate(fuera, np.ones((11, 11), np.uint8))
    fuera = cv2.bitwise_and(fuera, cv2.bitwise_not(cv2.erode(tw, np.ones((9, 9), np.uint8))))
    base = cv2.inpaint(nb, fuera, 21, cv2.INPAINT_TELEA)
    a = cv2.GaussianBlur(tw.astype(np.float32) / 255, (0, 0), 4)[..., None]
    out = warp * a + base * (1 - a)
    cv2.imwrite(str(TMP / 'cookie-montada.png'), out.clip(0, 255).astype(np.uint8))
    cv2.imwrite(str(TMP / 'cookie-fuera.png'), fuera)
    print(f'  afín {int(inl.sum())}/{len(sel)} · bolsa NB rellenada {int((fuera>0).sum())} px')

if __name__ == '__main__' and '--final' in sys.argv:
    montar_final()
    encuadrar_reflejo()


# ── Eli 29-09 sobre la mano izquierda de la NB: «sale como otro dedo difuminado… las uñas
# como difuminado de velocidad… marcas en la mano… se ve muy falsa». La mano con el trozo
# pasa a ser la REAL de la 3-79, con su propio calce (antes no encontraba puntos porque la
# zona estaba mal medida). Máscara: la mano y el trozo (piel, uñas, anillo, galleta), sin
# el muro oscuro de atrás.
def mano_real():
    import cv2
    import numpy as np
    mo = cv2.imread(str(TMP / 'cookie-montada.png'))
    og = cv2.imread(str(SESION / 'sesion_3-79.jpg'))
    nb = cv2.cvtColor(np.asarray(Image.open(TMP / 'cookie-nb3.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    sift = cv2.SIFT_create(15000)
    ka, da = sift.detectAndCompute(cv2.cvtColor(og, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    sel = [a for a, b in m if a.distance < 0.85 * b.distance
           and ka[a.queryIdx].pt[0] <= 700 and 700 <= ka[a.queryIdx].pt[1] <= 1320]
    pa = np.float32([ka[g.queryIdx].pt for g in sel]); pb = np.float32([kb[g.trainIdx].pt for g in sel])
    A, inl = cv2.estimateAffinePartial2D(pa, pb, method=cv2.RANSAC, ransacReprojThreshold=4.0)
    print(f'  mano: {int(inl.sum())}/{len(sel)} puntos · escala {np.hypot(A[0,0],A[1,0]):.3f} '
          f'giro {np.degrees(np.arctan2(A[1,0],A[0,0])):.1f}°')
    return A, og, mo

if __name__ == '__main__' and '--mano' in sys.argv:
    mano_real()


# ── Método invertido (Eli 29-09: «la mano es crucial»): el CUERPO es la foto real entera
# (manos, galleta, bolsa en su geometría) y de la NB sólo se toma cabeza y cuello, llevada
# al marco de la original con la inversa del calce de la bolsa. Costura en el pecho, sobre
# las manos (la mano con el trozo empieza en y≈740 de la 3-79).
def cuerpo_real(costura=620, banda=160, dx=0, dy=0):
    import cv2
    import numpy as np
    nb = cv2.cvtColor(np.asarray(Image.open(TMP / 'cookie-nb3.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    og = cv2.imread(str(SESION / 'sesion_3-79.jpg'))
    sift = cv2.SIFT_create(12000)
    ka, da = sift.detectAndCompute(cv2.cvtColor(og, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    sel = [a for a, b in m if a.distance < 0.8 * b.distance
           and 400 <= ka[a.queryIdx].pt[0] <= 1260 and 920 <= ka[a.queryIdx].pt[1] <= 2030]
    pa = np.float32([ka[g.queryIdx].pt for g in sel]); pb = np.float32([kb[g.trainIdx].pt for g in sel])
    A, _ = cv2.estimateAffinePartial2D(pa, pb, method=cv2.RANSAC, ransacReprojThreshold=3.0)
    Ai = cv2.invertAffineTransform(A)
    Ai[0, 2] += dx; Ai[1, 2] += dy
    # lienzo en el marco de la original, con margen arriba y a la izquierda para la cabeza
    ARRIBA_O, IZQ_O = 1500, 200
    T = np.float32([[1, 0, IZQ_O], [0, 1, ARRIBA_O]])
    W, H = 1500 + IZQ_O, 2250 + ARRIBA_O
    M = Ai.copy(); M[:, 2] += [IZQ_O, ARRIBA_O]
    cab = cv2.warpAffine(nb, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    lienzo = cab.astype(np.float32)
    og_l = cv2.warpAffine(og, T, (W, H))
    y = np.arange(H, dtype=np.float32)[:, None]
    a = np.clip((y - (ARRIBA_O + costura)) / banda, 0, 1)            # 0 arriba (NB) → 1 abajo (real)
    a = np.repeat(a, W, 1)
    a[:, :IZQ_O] = np.clip(a[:, :IZQ_O], 0, 0)                          # franja izq. expandida: NB
    a = cv2.GaussianBlur(a, (0, 0), 3)[..., None]
    out = og_l * a + lienzo * (1 - a)
    cv2.imwrite(str(TMP / 'cookie-cuerpo-real.png'), out.clip(0, 255).astype(np.uint8))
    print(f'  lienzo {W}×{H} · costura en y={costura} de la 3-79 · banda {banda}')

if __name__ == '__main__' and '--cuerpo' in sys.argv:
    cuerpo_real()


# ── La cabeza NB calzada en la BOCA real: en la 3-79 la modelo está corrida a la izquierda
# (su boca asoma en la esquina) y la NB la centró detrás de la bolsa; calzada por la bolsa,
# la cabeza quedaba 460 px a la derecha de su cuello. Aquí la comisura derecha de la NB
# (915, 810) va a la comisura real (195, 90), escala 1,25 (boca→mentón 180 vs 210 px).
# El lienzo final se arma directo en el marco de la original y a la proporción del pendón:
# mentón al 40 %, bolsa hasta ~71 % (el QR parte en 67 %).
S_CAB, NB_BOCA, OG_BOCA = 1.25, (915, 810), (195, 90)
XL, W_F = -290, 1560
H_F = round(W_F * PROP_PENDON) if 'PROP_PENDON' in dir() else round(1560 * 8560 / 2324)
YT = 300 - round(0.40 * H_F)

def cabeza_en_boca(costura=330, banda=150):
    import cv2
    import numpy as np
    nb = cv2.cvtColor(np.asarray(Image.open(TMP / 'cookie-nb3.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    # el cuerpo es la 3-79 ensanchada 290 px a la izquierda (x −290..1500 = x 0.. del lienzo)
    og = cv2.imread(str(TMP / 'cookie-og-ancha.png'))
    s = S_CAB
    tx = OG_BOCA[0] - s * NB_BOCA[0] - XL
    ty = OG_BOCA[1] - s * NB_BOCA[1] - YT
    M = np.float32([[s, 0, tx], [0, s, ty]])
    cab = cv2.warpAffine(nb, M, (W_F, H_F), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    valido = cv2.warpAffine(np.full(nb.shape[:2], 255, np.uint8), M, (W_F, H_F))
    # donde la NB no llega (arriba a la derecha), fondo muy desenfocado
    lejos = cv2.GaussianBlur(cab, (0, 0), 40)
    v = cv2.GaussianBlur(valido.astype(np.float32) / 255, (0, 0), 25)[..., None]
    base = cab * v + lejos * (1 - v)
    # la original en su lugar; bajo su borde inferior, su última franja estirada y desenfocada
    ox, oy = 0, -YT
    lienzo = base.copy()
    alfa = np.zeros((H_F, W_F), np.float32)
    y = np.arange(2250, dtype=np.float32)[:, None]
    # costura que baja a la izquierda: el pelo NB cae sobre el hombro y se cortaba en recto
    xs = np.arange(og.shape[1], dtype=np.float32)[None, :]
    # (bajarla 220 px mezclaba los dos collares, y≈580–630: se queda sobre ellos)
    c = costura + 60 * np.clip((420 - xs) / 300, 0, 1) + 330 * np.clip((200 - xs) / 120, 0, 1)
    b = banda + 40 * np.clip((420 - xs) / 300, 0, 1) + 120 * np.clip((200 - xs) / 120, 0, 1)
    ramp = np.clip((y - c) / b, 0, 1)
    x1 = min(W_F, ox + og.shape[1])
    alfa[oy:oy + 2250, ox:x1] = ramp[:, :x1 - ox]
    og_l = np.zeros_like(base); og_l[oy:oy + 2250, ox:x1] = og[:, :x1 - ox]
    fin = oy + 2250
    if fin < H_F:
        tira = cv2.resize(og[2250 - 160:, :x1 - ox], (x1 - ox, H_F - fin + 220), interpolation=cv2.INTER_CUBIC)
        tira = cv2.GaussianBlur(tira, (0, 0), 45)
        r = np.linspace(0, 1, 220)[:, None, None]
        og_l[fin - 220:fin, ox:x1] = og_l[fin - 220:fin, ox:x1] * (1 - r) + tira[:220] * r
        og_l[fin:, ox:x1] = tira[220:]
        alfa[fin:, ox:x1] = 1
    # borde izquierdo de la original (x = ox): rampa de 60 px hacia la NB
    alfa = cv2.GaussianBlur(alfa, (0, 0), 3)[..., None]
    out = og_l * alfa + base * (1 - alfa)
    cv2.imwrite(str(TMP / 'cookie-lienzo.png'), out.clip(0, 255).astype(np.uint8))
    print(f'  lienzo {W_F}×{H_F} · boca NB→real, escala {s} · costura y={costura}+{banda}')

if __name__ == '__main__' and '--boca' in sys.argv:
    cabeza_en_boca()


# ── A la izquierda del borde de la 3-79 se colaba el cuerpo NB (su mano y su bolsa): esa
# franja sale de expandir la ORIGINAL 290 px a la izquierda (manga, antebrazo, chaqueta).
def original_izq():
    import cv2
    import numpy as np
    og = Image.open(SESION / 'sesion_3-79.jpg').convert('RGB')
    e = TMP / 'cookie-og-entrada.jpg'; og.save(e, quality=95)
    crudo = paso(e, 'cookie-og-izq', 0,
                 'continuation of the same photograph to the left: more of the same woman\'s cream '
                 'blazer sleeve, her forearm and wrist leading to the hand that holds the cookie piece, '
                 'her wavy light-brown hair on the shoulder at the top, same soft focus and warm light. '
                 'No other hands, no text, nobody else.', izq=-XL)
    exp = Image.open(crudo).convert('RGB')
    s = (1500 - XL) / exp.width
    exp = exp.resize((1500 - XL, round(exp.height * s)), Image.LANCZOS)
    g = lambda im: cv2.cvtColor(np.asarray(im.resize((im.width // 4, im.height // 4))), cv2.COLOR_RGB2GRAY)
    _, sc, _, (mx, my) = cv2.minMaxLoc(cv2.matchTemplate(g(exp), g(og), cv2.TM_CCOEFF_NORMED))
    print(f'  expansión izq: calce {sc:.3f} en ({mx*4},{my*4})')
    L = Image.new('RGB', (1500 - XL, 2250)); L.paste(exp, (0, -my * 4))
    m = Image.new('L', (1500, 2250), 255)
    import numpy as np
    r = np.ones((2250, 1500), np.float32); r[:, :40] = np.linspace(0, 1, 40)[None, :]
    L.paste(og, (-XL, 0), Image.fromarray((r * 255).astype(np.uint8)))
    L.save(TMP / 'cookie-og-ancha.png')
    return L

if __name__ == '__main__' and '--izq' in sys.argv:
    original_izq()

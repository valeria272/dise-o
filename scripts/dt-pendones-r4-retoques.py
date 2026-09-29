#!/usr/bin/env python3
"""DT · pendones r4 — retoques de Eli (29-09, tarde):
  3 cookie: «el dedo de ella se me hace muy extraño… que se vea mucho más armónico con la
            escena» → el meñique largo y desenfocado de la mano del trozo. Nano Banana edita
            el recorte de la mano (meñique recogido, mano en foco) y se pega SÓLO lo que cambió,
            sin tocar el trozo, la galleta ni la bolsa (siguen siendo los de la sesión).
  2 teléfono: «los ojos… ajústalo un poco, similar a los de la cookie» → se toman de la
            edición NB sólo dos elipses de ojos, con el tono llevado al de la cara original.
"""
import sys
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageCms
Image.MAX_IMAGE_PIXELS = None

RAIZ = Path(__file__).resolve().parent.parent
T = RAIZ / 'raw/hilton/dt/pendones-2026/r4'
LINKS = Path('F:/SOLICITUDES 2026 HILTON/Pendon editable 2026 0,8x3m/Pendones 2026 caras nuevas/Links')
FOGRA = ImageCms.getOpenProfile(r'C:/Program Files/Common Files/Adobe/Color/Profiles/Recommended/CoatedFOGRA39.icc')
SRGB = ImageCms.createProfile('sRGB')
A_CMYK = ImageCms.buildTransform(SRGB, FOGRA, 'RGB', 'CMYK', renderingIntent=1)
A_RGB = ImageCms.buildTransform(FOGRA, SRGB, 'CMYK', 'RGB', renderingIntent=1)

def alinear(orig, gen):
    ga = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    gb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    (dx, dy), _ = cv2.phaseCorrelate(ga, gb)
    H, W = orig.shape[:2]
    return cv2.warpAffine(gen, np.float32([[1, 0, -dx], [0, 1, -dy]]), (W, H), borderMode=cv2.BORDER_REFLECT), (dx, dy)

def mano(gen_png='mano-nb.png'):
    orig = np.asarray(Image.open(T / 'mano-crop.png').convert('RGB')).astype(np.float32)
    H, W = orig.shape[:2]
    gen = np.asarray(Image.open(T / gen_png).convert('RGB').resize((W, H), Image.LANCZOS)).astype(np.float32)
    gen, d = alinear(orig, gen)
    la = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    lb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    dif = np.sqrt(((cv2.GaussianBlur(la, (0, 0), 4) - cv2.GaussianBlur(lb, (0, 0), 4)) ** 2).sum(2))
    m = (dif > 10).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((41, 41), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 0.004 * H * W:
            keep[lab == i] = 1
    cnts, _ = cv2.findContours(keep, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(keep, cnts, -1, 1, -1)
    keep = cv2.dilate(keep, np.ones((31, 31), np.uint8))
    # galleta (x>1680) y cuerpo de la bolsa (y>1700): siempre los reales. El borde del papel
    # NO se protege: ahí estaba la punta del meñique original (quedaba un sexto dedo)
    keep[1190:, 1680:] = 0
    keep[1765:, 1250:] = 0
    if gen_png != 'mano-nb.png':
        # ronda 6: la NB rehízo la escena entera del recorte; la máscara por diferencia dejaba
        # el dedo viejo semitransparente (fantasma). Se toma la NB COMPLETA salvo bolsa y
        # galleta, y se funde con rampas de 160 px hacia los bordes del recorte (arriba,
        # derecha, abajo; la izquierda es el borde del pendón).
        keep = np.ones((H, W), np.uint8)
        keep[1190:, 1680:] = 0
        keep[1765:, 1250:] = 0
    a = cv2.GaussianBlur(keep.astype(np.float32), (0, 0), 14)
    if gen_png != 'mano-nb.png':
        r = 160
        yy = np.arange(H, dtype=np.float32)[:, None]; xx = np.arange(W, dtype=np.float32)[None, :]
        borde = np.minimum(np.minimum(yy / r, (H - 1 - yy) / r), (W - 1 - xx) / r).clip(0, 1)
        a = a * borde
        # tono: la NB sale un poco más clara; se ajusta su media LAB a la de la original
        la = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
        lb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
        anillo = (borde < 1) & (borde > 0.3)
        lb += (la[anillo].mean(0) - lb[anillo].mean(0))
        gen = cv2.cvtColor(lb.clip(0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB).astype(np.float32)
    a = a[..., None]
    out = gen * a + orig * (1 - a)
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(T / 'mano-final.png')
    Image.fromarray((a[..., 0] * 255).astype(np.uint8)).save(T / 'mano-mascara.png')
    print(f'mano: corrimiento {d[0]:.1f},{d[1]:.1f} · máscara {a.mean()*100:.1f} %')
    # de vuelta al lienzo ×2 y al vínculo CMYK del pendón
    big = Image.open(T / 'cookie-v2-x2.png').convert('RGB')
    big.paste(Image.fromarray(out.clip(0, 255).astype(np.uint8)), (0, 4800))
    big.save(T / 'cookie-v3-x2.png')
    fin = big.resize((3228, 11890), Image.LANCZOS)
    ImageCms.applyTransform(fin, A_CMYK).save(LINKS / 'pendon-3-cookie-r4.jpg', quality=84,
                                              dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print('  ✓ Links/pendon-3-cookie-r4.jpg')

OJOS = [((537, 429), (78, 44)), ((674, 443), (62, 38))]   # centro y radios en el recorte 1024
RECORTE = (690, 1820)

def ojos():
    orig = np.asarray(Image.open(T / 'ojos-crop.png').convert('RGB')).astype(np.float32)
    H, W = orig.shape[:2]
    gen = np.asarray(Image.open(T / 'ojos-nb.png').convert('RGB').resize((W, H), Image.LANCZOS)).astype(np.float32)
    gen, d = alinear(orig, gen)
    m = np.zeros((H, W), np.float32)
    for (cx, cy), (rx, ry) in OJOS:
        cv2.ellipse(m, (cx, cy), (rx, ry), 0, 0, 360, 1, -1)
    m = cv2.GaussianBlur(m, (0, 0), 12)
    # tono: la NB aclaró la piel; se lleva su media (LAB) a la de la original dentro de las elipses
    la = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    lb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    w = m[..., None] > 0.5
    lb += (la[w[..., 0]].mean(0) - lb[w[..., 0]].mean(0))
    gen = cv2.cvtColor(lb.clip(0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB).astype(np.float32)
    out = gen * m[..., None] + orig * (1 - m[..., None])
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(T / 'ojos-final.png')
    print(f'ojos: corrimiento {d[0]:.1f},{d[1]:.1f}')
    src = Image.open(LINKS / 'pendon-2-telefono.jpg')
    parche = ImageCms.applyTransform(Image.fromarray(out.clip(0, 255).astype(np.uint8)), A_CMYK)
    mk = Image.fromarray((m * 255).astype(np.uint8))
    src.paste(parche, RECORTE, mk)
    src.save(LINKS / 'pendon-2-telefono-r4.jpg', quality=84, dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print('  ✓ Links/pendon-2-telefono-r4.jpg (el vínculo de ayer queda intacto)')

if __name__ == '__main__':
    # ronda 6 (Eli: «natural, como cuando uno agarra una galleta, con los dedos juntos»):
    # variante 2 — índice y medio con el pulgar debajo, anular (con el anillo) y meñique recogidos
    if 'mano2' in sys.argv: mano('mano2-nb2.png')
    elif 'mano' in sys.argv: mano()
    if 'ojos' in sys.argv: ojos()


# ── Eli: «la foto de la cookie borró el árbol del logo de DT y quedó en la mitad». La copa
# del emblema (3-79, arriba a la derecha, detrás del pelo) quedó bajo el muro de la cabeza
# NB. A la derecha del pelo NB (x ≥ 560 de la 3-79) vuelve la original desde su borde de
# arriba. El emblema está muy desenfocado: basta Lanczos ×2 para llevarlo a la alta.
# Y el fantasma del trozo/dedo viejo junto al trozo nuevo se rellena con la chaqueta.
OX, OY = 290, 1998          # la 3-79 en el lienzo (px del lienzo ×1)
FANTASMA = [(1768, 5515, 1905, 5735), (1735, 5700, 1800, 5850)]   # px del ×2

def arbol_y_fantasma():
    big = np.asarray(Image.open(T / 'cookie-v3-x2.png').convert('RGB')).astype(np.float32)
    og = Image.open(Path('F:/SESIONES HILTON/SESION DE FOTOS DT/sesion modelos DT/sesion_3-79.jpg')).convert('RGB')
    x0, x1, y1 = 500, 1270, 520   # hasta el borde derecho del lienzo (x 1270 de la 3-79)                     # franja de la original a reponer (x hasta el borde del lienzo)
    parche = np.asarray(og.crop((x0, 0, x1, y1)).resize(((x1 - x0) * 2, y1 * 2), Image.LANCZOS)).astype(np.float32)
    h, w = parche.shape[:2]
    X, Y = (x0 + OX) * 2, OY * 2
    w = min(w, big.shape[1] - X); parche = parche[:, :w]
    xx = np.arange(w, dtype=np.float32)[None, :] / 2 + x0
    yy = np.arange(h, dtype=np.float32)[:, None] / 2
    a = np.clip((xx - 540) / 90, 0, 1) * np.clip(yy / 30, 0, 1) * np.clip((y1 - yy) / 60, 0, 1)
    a = a[..., None]
    zona = big[Y:Y + h, X:X + w]
    # tono: la franja superior se iguala al muro NB que la rodea
    big[Y:Y + h, X:X + w] = parche * a + zona * (1 - a)
    out = big.clip(0, 255).astype(np.uint8)
    m = np.zeros(out.shape[:2], np.uint8)
    for bx0, by0, bx1, by1 in FANTASMA:
        m[by0:by1, bx0:bx1] = 255
    # el relleno dejaba una mancha: se CLONA chaqueta real de 190 px a la derecha, con borde suave
    mf = cv2.GaussianBlur(m.astype(np.float32) / 255, (0, 0), 12)
    mf = np.clip(mf * 1.6, 0, 1)[..., None]
    fuente = np.roll(out, -190, axis=1).astype(np.float32)
    out = (fuente * mf + out.astype(np.float32) * (1 - mf)).clip(0, 255).astype(np.uint8)
    Image.fromarray(out).save(T / 'cookie-v4-x2.png')
    fin = Image.fromarray(out).resize((3228, 11890), Image.LANCZOS)
    ImageCms.applyTransform(fin, A_CMYK).save(LINKS / 'pendon-3-cookie-r4.jpg', quality=84,
                                              dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print('  ✓ árbol repuesto, fantasma rellenado → Links/pendon-3-cookie-r4.jpg')

if __name__ == '__main__' and 'arbol' in sys.argv:
    arbol_y_fantasma()


# ── La copa del emblema toca el borde de arriba de la 3-79 y quedaba cortada en recto: se
# completa hacia arriba con Flux (sólo muro y emblema, sin personas) y se funde con el muro NB.
def copa():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import magnific as M
    og = Image.open(Path('F:/SESIONES HILTON/SESION DE FOTOS DT/sesion modelos DT/sesion_3-79.jpg')).convert('RGB')
    base = og.crop((560, 0, 1500, 700)); e = T / 'copa-entrada.jpg'; base.save(e, quality=95)
    crudo = T / 'copa-expandida.jpg'
    if not crudo.exists():
        r = M.pedir('/v1/ai/image-expand/flux-pro', {'image': M.b64_de(e), 'top': 420, 'left': 0, 'right': 0, 'bottom': 0,
            'prompt': 'the same softly out-of-focus white DoubleTree tree emblem on the same dark charcoal wall: '
                      'continue upward the top of the round leafy tree crown and the thin circular D ring around it, '
                      'then plain dark wall above. Same heavy blur, same light. No text, no letters, nobody.'})
        M.guarda(M.espera('/v1/ai/image-expand/flux-pro', r.get('data', r).get('task_id')), crudo)
    exp = Image.open(crudo).convert('RGB')
    s = base.width / exp.width
    exp = exp.resize((base.width, round(exp.height * s)), Image.LANCZOS)
    arriba = exp.height - 700
    print(f'  copa: {arriba} px nuevos arriba')
    big = np.asarray(Image.open(T / 'cookie-v4-x2.png').convert('RGB')).astype(np.float32)
    parte = np.asarray(exp.crop((0, 0, base.width, arriba + 200)).resize((base.width * 2, (arriba + 200) * 2), Image.LANCZOS)).astype(np.float32)
    h, w = parte.shape[:2]
    X, Y = (560 + OX) * 2, (OY - arriba) * 2
    w = min(w, big.shape[1] - X); parte = parte[:, :w]
    yy = np.arange(h, dtype=np.float32)[:, None]; xx = np.arange(w, dtype=np.float32)[None, :]
    # entra desde arriba (se funde con el muro NB) y por la izquierda (hacia el pelo); abajo
    # cubre 40 px sobre la original para que no quede línea
    a = np.clip(yy / 420, 0, 1) * np.clip(xx / 320, 0, 1) * np.clip((h - yy) / 400, 0, 1)   # mezclas largas: la línea del borde cruzaba la copa
    # tono: igualar la media de la franja inferior (que es la original) con la original real
    ref = big[Y + h - 300:Y + h, X:X + w].reshape(-1, 3).mean(0)
    parte += ref - parte[h - 300:h].reshape(-1, 3).mean(0)
    zona = big[Y:Y + h, X:X + w]
    big[Y:Y + h, X:X + w] = parte * a[..., None] + zona * (1 - a[..., None])
    out = Image.fromarray(big.clip(0, 255).astype(np.uint8)); out.save(T / 'cookie-v5-x2.png')
    ImageCms.applyTransform(out.resize((3228, 11890), Image.LANCZOS), A_CMYK).save(
        LINKS / 'pendon-3-cookie-r4.jpg', quality=84, dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print('  ✓ copa completa → Links/pendon-3-cookie-r4.jpg')

if __name__ == '__main__' and 'copa' in sys.argv:
    copa()


# ── Eli: «la segunda tiene detalles de texturas extrañas que delatan la IA». Venían del
# upscaler de precisión ×4 (dos pasadas) de ayer: pelo y piel «pintados». Se rehace la alta
# con UNA pasada ×2 desde la foto base (final3-173a, recorte x 120..1133) + Lanczos a
# 3228×7170, y encima los mismos ojos (edición NB sobre la base nueva, sólo dos elipses).
def telefono():
    base = Image.open(T / 'tel-nuevo.png').convert('RGB')
    orig = np.asarray(Image.open(T / 'ojos2-crop.png').convert('RGB')).astype(np.float32)
    H, W = orig.shape[:2]
    gen = np.asarray(Image.open(T / 'ojos2-nb.png').convert('RGB').resize((W, H), Image.LANCZOS)).astype(np.float32)
    gen, d = alinear(orig, gen)
    m = np.zeros((H, W), np.float32)
    for (cx, cy), (rx, ry) in OJOS:
        cv2.ellipse(m, (cx, cy), (rx, ry), 0, 0, 360, 1, -1)
    m = cv2.GaussianBlur(m, (0, 0), 12)
    la = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    lb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    w = m > 0.5
    lb += (la[w].mean(0) - lb[w].mean(0))
    gen = cv2.cvtColor(lb.clip(0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB).astype(np.float32)
    out = gen * m[..., None] + orig * (1 - m[..., None])
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(T / 'ojos2-final.png')
    base.paste(Image.fromarray(out.clip(0, 255).astype(np.uint8)), RECORTE)
    ImageCms.applyTransform(base, A_CMYK).save(LINKS / 'pendon-2-telefono-r4.jpg', quality=84,
                                               dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print(f'  ojos corrimiento {d[0]:.1f},{d[1]:.1f} · ✓ Links/pendon-2-telefono-r4.jpg (alta nueva)')

if __name__ == '__main__' and 'telefono' in sys.argv:
    telefono()


# ── Eli: «el árbol quedó mal y pegoteado» (copa de Flux + muro NB + original = tres fuentes).
# Ahora el lado derecho del fondo es UNA sola pieza: la columna de muro de la 3-79
# (x 560..1500, y 0..900) expandida 1.000 px hacia arriba en una generación, puesta entera
# sobre la v4 (sin la copa anterior), con fundidos largos hacia el pelo y hacia arriba.
def muro():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import magnific as M
    og = Image.open(Path('F:/SESIONES HILTON/SESION DE FOTOS DT/sesion modelos DT/sesion_3-79.jpg')).convert('RGB')
    x0 = 560
    base = og.crop((x0, 0, 1500, 900)); e = T / 'muro-entrada.jpg'; base.save(e, quality=95)
    crudo = T / 'muro-expandido.jpg'
    if not crudo.exists():
        r = M.pedir('/v1/ai/image-expand/flux-pro', {'image': M.b64_de(e), 'top': 1000, 'left': 0, 'right': 0, 'bottom': 0,
            'prompt': 'the same dark charcoal hotel wall, heavily out of focus: the white DoubleTree tree emblem '
                      'complete with its round leafy crown inside the thin circular D ring, mounted on the same dark '
                      'wall panel; plain dark wall above it. Same blur, same soft light. No text, no letters, nobody.'})
        M.guarda(M.espera('/v1/ai/image-expand/flux-pro', r.get('data', r).get('task_id')), crudo)
    exp = Image.open(crudo).convert('RGB')
    exp = exp.resize((base.width, round(exp.height * base.width / exp.width)), Image.LANCZOS)
    arriba = exp.height - 900
    big = np.asarray(Image.open(T / 'cookie-v4-x2.png').convert('RGB')).astype(np.float32)
    parte = np.asarray(exp.resize((exp.width * 2, exp.height * 2), Image.LANCZOS)).astype(np.float32)
    X, Y = (x0 + OX) * 2, (OY - arriba) * 2
    h, w = parte.shape[:2]; w = min(w, big.shape[1] - X); parte = parte[:, :w]
    zona = big[Y:Y + h, X:X + w]
    # tono con la franja que ya es la original (y 300..900 de la 3-79, a la derecha del pelo)
    fr = slice(h - 1000, h - 200)
    parte += zona[fr, 300:].reshape(-1, 3).mean(0) - parte[fr, 300:].reshape(-1, 3).mean(0)
    yy = np.arange(h, dtype=np.float32)[:, None]; xx = np.arange(w, dtype=np.float32)[None, :]
    a = np.clip(xx / 360, 0, 1) * np.clip(yy / 500, 0, 1) * np.clip((h - yy) / 500, 0, 1)
    big[Y:Y + h, X:X + w] = parte * a[..., None] + zona * (1 - a[..., None])
    out = Image.fromarray(big.clip(0, 255).astype(np.uint8)); out.save(T / 'cookie-v6-x2.png')
    ImageCms.applyTransform(out.resize((3228, 11890), Image.LANCZOS), A_CMYK).save(
        LINKS / 'pendon-3-cookie-r4.jpg', quality=84, dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print(f'  ✓ muro de una pieza ({arriba} px nuevos) → Links/pendon-3-cookie-r4.jpg')

if __name__ == '__main__' and 'muro' in sys.argv:
    muro()


# ── La expansión del muro inventó un letrero «DoubleTree» y una D (R-80): descartada. El
# emblema se SACA: se borra de la 3-79 (relleno del propio muro, a baja resolución porque
# el fondo está muy desenfocado) y esa zona se repone sobre la v4. Sin árbol a medias.
def sin_arbol():
    og = cv2.imread('F:/SESIONES HILTON/SESION DE FOTOS DT/sesion modelos DT/sesion_3-79.jpg')
    x0, x1, y1 = 520, 1270, 820
    reg = og[0:y1, x0:1500].copy()
    hsv = cv2.cvtColor(reg, cv2.COLOR_BGR2HSV)
    claro = ((hsv[..., 2] > 95) & (hsv[..., 1] < 70)).astype(np.uint8) * 255
    claro[:, :90] = 0                                   # el pelo/chaqueta del borde izquierdo no
    claro[430:, :950 - x0] = 0                          # el hombro de la chaqueta no (se corría)
    claro = cv2.dilate(claro, np.ones((61, 61), np.uint8))
    claro[430:, :900 - x0] = 0
    chico = cv2.resize(reg, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    mch = cv2.resize(claro, (chico.shape[1], chico.shape[0]), interpolation=cv2.INTER_NEAREST)
    rell = cv2.inpaint(chico, mch, 20, cv2.INPAINT_TELEA)
    rell = cv2.GaussianBlur(rell, (0, 0), 6)
    rell = cv2.resize(rell, (reg.shape[1], reg.shape[0]), interpolation=cv2.INTER_CUBIC)
    mk = cv2.GaussianBlur(claro.astype(np.float32) / 255, (0, 0), 25)[..., None]
    limpio = (rell * mk + reg * (1 - mk)).clip(0, 255).astype(np.uint8)
    limpio = cv2.cvtColor(limpio, cv2.COLOR_BGR2RGB)[:, :x1 - x0]
    # base: la v3 (antes del parche del árbol, que dejaba el borde con 30 px de fundido)
    big = np.asarray(Image.open(T / 'cookie-v3-x2.png').convert('RGB')).astype(np.float32)
    parte = cv2.resize(limpio, (limpio.shape[1] * 2, limpio.shape[0] * 2), interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
    X, Y = (x0 + OX) * 2, OY * 2
    h, w = parte.shape[:2]; w = min(w, big.shape[1] - X); parte = parte[:, :w]
    yy = np.arange(h, dtype=np.float32)[:, None] / 2; xx = np.arange(w, dtype=np.float32)[None, :] / 2 + x0
    a = np.clip((xx - 560) / 100, 0, 1) * np.clip((y1 - yy) / 80, 0, 1) * np.clip(yy / 200, 0, 1)
    zona = big[Y:Y + h, X:X + w]
    # el muro NB de arriba (más oscuro) contra el de la foto: en vez de corte, rampa de 260 px
    # (px de la 3-79) que baja el muro de la foto al tono del NB y lo recupera hacia abajo
    arriba = big[Y - 40:Y, X:X + w].reshape(-1, 3).mean(0)
    t = np.clip(1 - yy / 260, 0, 1)[..., None]
    parte = parte + (arriba - parte[:40].reshape(-1, 3).mean(0)) * t
    big[Y:Y + h, X:X + w] = parte * a[..., None] + zona * (1 - a[..., None])
    # a la izquierda (x < 560), el muro de la foto sobre la cabeza también se lleva al tono NB
    out = big.clip(0, 255).astype(np.uint8)
    # el fantasma del trozo viejo: clon de chaqueta de 190 px a la derecha (como en arbol_y_fantasma)
    m = np.zeros(out.shape[:2], np.uint8)
    for bx0, by0, bx1, by1 in FANTASMA:
        m[by0:by1, bx0:bx1] = 255
    mf = np.clip(cv2.GaussianBlur(m.astype(np.float32) / 255, (0, 0), 12) * 1.6, 0, 1)[..., None]
    out = (np.roll(out, -190, axis=1).astype(np.float32) * mf + out.astype(np.float32) * (1 - mf)).clip(0, 255).astype(np.uint8)
    out = Image.fromarray(out); out.save(T / 'cookie-v7-x2.png')
    ImageCms.applyTransform(out.resize((3228, 11890), Image.LANCZOS), A_CMYK).save(
        LINKS / 'pendon-3-cookie-r4.jpg', quality=84, dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print('  ✓ sin emblema → Links/pendon-3-cookie-r4.jpg')

if __name__ == '__main__' and 'sinarbol' in sys.argv:
    sin_arbol()


# ── Ronda 7 (Eli: «se ven manchones donde estaba el árbol… hazla de nuevo con la imagen»):
# la zona de la persona se REGENERA entera con NB Pro 4K a partir del resultado aprobado
# (cara, pinza, galleta, bolsa) con el muro limpio: una sola foto, sin parches. Lo único que
# la NB escribe mal es la etiqueta redonda («BN KUTSI CUNTAINS»): se repone desde la 3-79.
R7_Y0, R7_Y1 = 2500, 8046      # franja del lienzo ×2 que se regeneró (ancho completo)

def r7():
    nb = cv2.cvtColor(np.asarray(Image.open(T / 'r7-nb.png').convert('RGB')), cv2.COLOR_RGB2BGR)
    og = cv2.imread('F:/SESIONES HILTON/SESION DE FOTOS DT/sesion modelos DT/sesion_3-79.jpg')
    sift = cv2.SIFT_create(15000)
    ka, da = sift.detectAndCompute(cv2.cvtColor(og, cv2.COLOR_BGR2GRAY), None)
    kb, db = sift.detectAndCompute(cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    sel = [a for a, b in m if a.distance < 0.8 * b.distance
           and 430 <= ka[a.queryIdx].pt[0] <= 1110 and 1150 <= ka[a.queryIdx].pt[1] <= 2060]
    pa = np.float32([ka[g.queryIdx].pt for g in sel]); pb = np.float32([kb[g.trainIdx].pt for g in sel])
    A, inl = cv2.estimateAffinePartial2D(pa, pb, method=cv2.RANSAC, ransacReprojThreshold=4.0)
    print(f'  bolsa: {int(inl.sum())}/{len(sel)} puntos · escala {np.hypot(A[0,0],A[1,0]):.3f}')
    # la etiqueta redonda en la 3-79 (medida): centro y radio
    mk = np.zeros(og.shape[:2], np.float32)
    cv2.ellipse(mk, (968, 1797), (70, 76), 0, 0, 360, 1, -1)
    h, w = nb.shape[:2]
    warp = cv2.warpAffine(og, A, (w, h), flags=cv2.INTER_LANCZOS4).astype(np.float32)
    mw = cv2.GaussianBlur(cv2.warpAffine(mk, A, (w, h)), (0, 0), 6)[..., None]
    out = (warp * mw + nb.astype(np.float32) * (1 - mw)).clip(0, 255).astype(np.uint8)
    cv2.imwrite(str(T / 'r7-final.png'), out)
    return out

if __name__ == '__main__' and 'r7' in sys.argv:
    r7()


def r7_montar():
    base = np.asarray(Image.open(T / 'cookie-v7-x2.png').convert('RGB')).astype(np.float32)
    nueva = cv2.cvtColor(cv2.imread(str(T / 'r7-final.png')), cv2.COLOR_BGR2RGB)
    Wb = base.shape[1]; h = R7_Y1 - R7_Y0
    nueva = cv2.resize(nueva, (Wb, h), interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
    zona = base[R7_Y0:R7_Y1]
    # tono en los bordes: se iguala la media de 200 px arriba y abajo, con rampa entre ambos
    top_d = zona[:200].reshape(-1, 3).mean(0) - nueva[:200].reshape(-1, 3).mean(0)
    bot_d = zona[-200:].reshape(-1, 3).mean(0) - nueva[-200:].reshape(-1, 3).mean(0)
    t = np.linspace(0, 1, h, dtype=np.float32)[:, None, None]
    corr = top_d * np.clip(1 - t / 0.25, 0, 1) + bot_d * np.clip((t - 0.75) / 0.25, 0, 1)
    nueva = nueva + corr
    yy = np.arange(h, dtype=np.float32)[:, None]
    a = (np.clip(yy / 260, 0, 1) * np.clip((h - 1 - yy) / 260, 0, 1))[..., None]
    base[R7_Y0:R7_Y1] = nueva * a + zona * (1 - a)
    out = Image.fromarray(base.clip(0, 255).astype(np.uint8)); out.save(T / 'cookie-v8-x2.png')
    ImageCms.applyTransform(out.resize((3228, 11890), Image.LANCZOS), A_CMYK).save(
        LINKS / 'pendon-3-cookie-r4.jpg', quality=86, dpi=(100, 100), icc_profile=FOGRA.tobytes())
    print('  ✓ ronda 7 montada → Links/pendon-3-cookie-r4.jpg')

if __name__ == '__main__' and 'r7montar' in sys.argv:
    r7_montar()

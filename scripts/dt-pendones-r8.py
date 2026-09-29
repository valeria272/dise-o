#!/usr/bin/env python3
"""DT · pendones ronda 8 (29-09, noche) — pedido de Eli:
  pendón 2 teléfono: «cambiar el color de pelo a rubio» (sobre la r4 aprobada, nada más).
  pendón 3 cookie:   «dejar la imagen original (que sale la mano con la galleta) y dejar el
                     ajuste del correo» → la sesion_3-79 REAL, sin IA (sin cara nueva, sin mano
                     regenerada), como el pendón impreso. Sólo lleva el ×2 de precisión.

Uso:
    py -3 scripts/dt-pendones-r8.py cookie            # arma Links/pendon-3-cookie-r8.jpg
    py -3 scripts/dt-pendones-r8.py pelo pelo-nbN.png # arma Links/pendon-2-telefono-r8.jpg

El vínculo nuevo tiene los MISMOS píxeles que el de la r4 (3228×11890 y 3228×7170), así que
en el .ai basta cambiar el archivo: la geometría del grupo de recorte no se toca.
"""
import sys
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageCms
Image.MAX_IMAGE_PIXELS = None

RAIZ = Path(__file__).resolve().parent.parent
T = RAIZ / 'raw/hilton/dt/pendones-2026/r8'
LINKS = Path('F:/SOLICITUDES 2026 HILTON/Pendon editable 2026 0,8x3m/Pendones 2026 caras nuevas/Links')
FOGRA = ImageCms.getOpenProfile(r'C:/Program Files/Common Files/Adobe/Color/Profiles/Recommended/CoatedFOGRA39.icc')
A_CMYK = ImageCms.buildTransform(ImageCms.createProfile('sRGB'), FOGRA, 'RGB', 'CMYK', renderingIntent=1)

def guardar(img, nombre):
    ImageCms.applyTransform(img, A_CMYK).save(LINKS / nombre, quality=84, dpi=(100, 100),
                                              icc_profile=FOGRA.tobytes())
    print(f'  ✓ Links/{nombre}')

# ── Cookie. Vínculo r4: 3228×11890 px sobre 98,8 × 364 cm (32,66 px/cm); la mesa empieza en
# x = 224 px, y = 894 px. La ventana x 180..1240 de la 3-79 (dedos, anillo, bolsa y la otra
# mano) cubre los 82 cm con sangrado; la foto parte a 40 cm del borde de arriba para que la
# mano con la galleta caiga BAJO el titular (51–83 cm) y la bolsa llegue al cuadro del QR.
PX_CM, MESA_X, MESA_Y = 32.66, 224, 894
VENTANA = (180, 1240)
TOPE_CM = 40
AZUL = (32, 32, 73)          # el azul del velo de la plantilla, medido en el PNG de Eli

def cookie():
    # el precision ×2 de la 3-79 entera falló 2 veces sin imagen; la ventana sola (1060×2250) sí
    x2 = Image.open(T / '3-79-ventana-x2.png').convert('RGB')  # 2120×4500 = x 180..1240 de la 3-79
    ancho_cm = 82
    k = (ancho_cm * PX_CM) / (VENTANA[1] - VENTANA[0])          # px del vínculo por px de la 3-79
    W, H = round((VENTANA[1] - VENTANA[0]) * k), round(2250 * k)
    foto = np.asarray(x2.resize((W, H), Image.LANCZOS)).astype(np.float32)
    ox = round(MESA_X - 1 * PX_CM)
    oy = round(MESA_Y + TOPE_CM * PX_CM)
    lienzo = np.zeros((11890, 3228, 3), np.float32); lienzo[:] = AZUL
    # fundidos largos hacia el azul arriba (bajo el logo) y abajo (bajo el QR)
    a = np.ones(H, np.float32)
    ra, rb = round(18 * PX_CM), round(14 * PX_CM)
    a[:ra] = np.linspace(0, 1, ra) ** 1.5
    a[-rb:] = np.linspace(1, 0, rb) ** 1.5
    x0, x1 = max(ox, 0), min(ox + W, 3228)
    y0, y1 = max(oy, 0), min(oy + H, 11890)
    trozo = foto[y0 - oy:y1 - oy, x0 - ox:x1 - ox]
    al = a[y0 - oy:y1 - oy, None, None]
    lienzo[y0:y1, x0:x1] = trozo * al + lienzo[y0:y1, x0:x1] * (1 - al)
    img = Image.fromarray(lienzo.clip(0, 255).astype(np.uint8))
    img.save(T / 'cookie-r8-rgb.png')
    print(f'cookie: 3-79 ×{k:.3f} en ({ox},{oy}) · {W}×{H} · '
          f'{(VENTANA[1]-VENTANA[0]) / ancho_cm * 2.54 * 2:.0f} ppi reales tras el ×2 '
          f'(la bolsa termina a {(oy + 2090 * k - MESA_Y) / PX_CM:.0f} cm)')
    guardar(img, 'pendon-3-cookie-r8.jpg')

# ── Teléfono: sólo el pelo. La NB edita el recorte (500,1700)-(1900,3100) del alta aprobada;
# vuelve SOLO lo que cambió de color (máscara por diferencia de tono), el resto es la r4.
RECORTE = (500, 1700, 1900, 3100)

# Lo que pasó: con «golden blonde» la NB dejó un cobrizo claro (nb1–3); con «ABSOLUTELY NO red,
# copper…» salió rubio miel (nb4) pero aún frutilla. Se toma la nb4, se le baja el rojo en LAB
# (a* × 0,45) y se aclara (L × 1,08 + 14), y se monta SÓLO sobre el pelo: croma > 30 y L < 160
# de la original (la piel mide croma < 27 y L > 165), donde la NB cambió algo, sin la cara
# (óvalo), sin el follaje de arriba ni las pulseras. Fuera del pelo todo es la foto aprobada.
def pelo(nb):
    base = Image.open(T / 'tel-aprobado-rgb.png').convert('RGB')
    o8 = np.asarray(Image.open(T / 'pelo-crop.png').convert('RGB'))
    o = o8.astype(np.float32)
    h, w = o.shape[:2]
    g = np.asarray(Image.open(T / nb).convert('RGB').resize((w, h), Image.LANCZOS))
    (dx, dy), _ = cv2.phaseCorrelate(cv2.cvtColor(o8, cv2.COLOR_RGB2GRAY).astype(np.float32),
                                     cv2.cvtColor(g, cv2.COLOR_RGB2GRAY).astype(np.float32))
    g = cv2.warpAffine(g, np.float32([[1, 0, -dx], [0, 1, -dy]]), (w, h), borderMode=cv2.BORDER_REFLECT)
    la = cv2.cvtColor(o8, cv2.COLOR_RGB2LAB).astype(np.float32)
    lb = cv2.cvtColor(g, cv2.COLOR_RGB2LAB).astype(np.float32)
    # máscara del pelo
    cro = np.sqrt((la[..., 1] - 128) ** 2 + (la[..., 2] - 128) ** 2)
    suave = np.clip((cro - 26) / 8, 0, 1) * np.clip((172 - la[..., 0]) / 14, 0, 1)
    zona = cv2.dilate((np.sqrt(((la - lb) ** 2).sum(-1)) > 9).astype(np.uint8), np.ones((25, 25), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(zona, 8)
    z = np.isin(lab, [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 20000]).astype(np.float32)
    m = cv2.GaussianBlur(suave * z, (0, 0), 2.5)
    b = cv2.morphologyEx((m > 0.25).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((31, 31), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(b, 8)
    comp = cv2.dilate((lab == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])).astype(np.uint8),
                      np.ones((9, 9), np.uint8)).astype(np.float32)
    cara = np.zeros((h, w), np.float32); cv2.ellipse(cara, (800, 650), (165, 235), -8, 0, 360, 1, -1)
    lim = np.zeros((h, w), np.float32); cv2.ellipse(lim, (700, 800), (470, 540), 0, 0, 360, 1, -1)
    lim[:265] = 0; cv2.rectangle(lim, (540, 990), (790, 1190), 0, -1)        # follaje · pulseras
    mm = m * comp * (1 - cv2.GaussianBlur(cara, (0, 0), 10)) * cv2.GaussianBlur(lim, (0, 0), 8)
    # color: la nb4 sin rojo y más clara
    L = lb.copy(); L[..., 0] = np.clip(L[..., 0] * 1.08 + 14, 0, 255)
    L[..., 1] = 128 + (L[..., 1] - 128) * 0.45; L[..., 2] = 128 + (L[..., 2] - 128) * 0.9
    rubio = cv2.cvtColor(L.clip(0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB).astype(np.float32)
    out = rubio * mm[..., None] + o * (1 - mm[..., None])
    Image.fromarray((mm * 255).astype(np.uint8)).save(T / 'pelo-mascara.png')
    parche = Image.fromarray(out.clip(0, 255).astype(np.uint8))
    parche.save(T / 'pelo-final.png')
    base.paste(parche, RECORTE[:2])
    base.save(T / 'tel-r8-rgb.png')
    print(f'pelo: {nb} · corrimiento {dx:.1f},{dy:.1f} · {mm.mean()*100:.0f} % del recorte es pelo')
    guardar(base, 'pendon-2-telefono-r8.jpg')

if __name__ == '__main__':
    if 'cookie' in sys.argv: cookie()
    if 'pelo' in sys.argv: pelo(sys.argv[sys.argv.index('pelo') + 1])

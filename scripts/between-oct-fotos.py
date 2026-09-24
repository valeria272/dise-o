"""BETWEEN · OCTUBRE — prepara las FOTOS REALES de las piezas (sin IA).

Todas salen de la sesión de modelos del 25-jul-2025 (la «más actualizada, con
personas y desayunos», primera opción según Eli) y de la sesión de platos de
enero. Bajadas de Drive (`1gI00XGbBV5YjqcSjG3SmmkMuxr-ev_60`) a
`raw/hilton/between/togo-25jul2025/oct/`.

Retoques, y sólo éstos (tratamiento de Eli: nada quemado, contraste ~3 %):
  · ⛔ LOGO HP de los notebooks: la IA no mete marcas de terceros y la foto real
    tampoco puede llevarlas. Se borra con `cv2.inpaint` sobre una máscara de los
    píxeles CLAROS del logotipo dentro de su caja (la tapa es lisa y oscura).
  · ⛔ taza KIMBO de Between-28: se deja FUERA del recorte.
  · recorte a la proporción del bloque, contraste +3 %.
"""
import sys
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
M = RAIZ / "raw/hilton/between/togo-25jul2025/oct"
P = RAIZ / "raw/hilton/between/platos-ene"
OUT = RAIZ / "public/assets/hilton/between/oct"
OUT.mkdir(parents=True, exist_ok=True)


def sin_logo(img: np.ndarray, caja) -> np.ndarray:
    """Borra un logotipo claro sobre una superficie oscura y lisa."""
    x0, y0, x1, y1 = caja
    zona = cv2.cvtColor(img[y0:y1, x0:x1], cv2.COLOR_BGR2GRAY)
    umbral = np.percentile(zona, 50) + 25
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y0:y1, x0:x1] = (zona > umbral).astype(np.uint8) * 255
    mask = cv2.dilate(mask, np.ones((9, 9), np.uint8), iterations=2)
    return cv2.inpaint(img, mask, 12, cv2.INPAINT_TELEA)


def guardar(img_bgr, nombre, caja=None, ancho=None):
    im = Image.fromarray(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    if caja:
        im = im.crop(caja)
    if ancho and im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.03)
    im.save(OUT / nombre, quality=93)
    print(nombre, im.size)


def leer(p):
    return cv2.cvtColor(np.array(ImageOps.exif_transpose(Image.open(p)).convert("RGB")), cv2.COLOR_RGB2BGR)


# collage 05-10 · COWORK — M107, logo HP en la tapa (≈ x 3560-3680, y 3480-3660)
m107 = sin_logo(leer(M / "M107.jpg"), (3480, 3420, 3760, 3720))
guardar(m107, "c-cowork.jpg", ancho=1400)
# collage 05-10 · CONVERSA — M17
guardar(leer(M / "M17.jpg"), "c-conversa.jpg", ancho=1400)
# collage 05-10 · DULCE — Between-28, SIN la taza KIMBO de arriba
b28 = leer(P / "Between-28.jpg")
guardar(b28, "c-dulce.jpg", caja=(0, 700, 1500, 2250), ancho=1400)
# feed 05-10 · REUNIÓN — M104, logo HP (≈ x 760-880, y 3960-4080); 4:5 sin la TV
m104 = sin_logo(leer(M / "M104.jpg"), (700, 3880, 960, 4160))
guardar(m104, "f-reunion.jpg", caja=(48, 1080, 3792, 5760), ancho=2250)
# feed 14-10 · ESPACIOS — M68 (lounge, sillones de cuero), 4:5
guardar(leer(M / "M68.jpg"), "f-espacios.jpg", caja=(0, 960, 3840, 5760), ancho=2250)
# st 27-10 · EVENTOS — M139 (terraza, grupo), 9:16
guardar(leer(M / "M139.jpg"), "s-eventos.jpg", caja=(300, 0, 3540, 5760), ancho=2250)

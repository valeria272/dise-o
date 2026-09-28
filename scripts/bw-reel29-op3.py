"""BETWEEN · Reel n°1 S3 «La razón» (29-09) — opción 3.

Parte de la edición 2 aprobada por el cliente y le aplica lo que pidieron:
  1. estabiliza la cámara (cada una de las 3 tomas por separado, cámara fija);
  2. borra el texto quemado y la sombra de la palma con parches de Magnific
     (Runway Aleph 2): sólo se reemplaza la zona del texto y la piel de la mano;
     todo lo demás es el 4K original;
  3. rearma el fondo desenfocado y vuelve a poner el texto con la misma
     tipografía, cuerpo, color y posición que la edición 2 (medidos al píxel:
     Raleway SemiBold 128 px, relleno #FEF8EA, borde #645B4A ~10 px).

Uso:
  python scripts/bw-reel29-op3.py --parche-texto raw/between/reel-29sep/mg-aleph.mp4 \
      --parche-mano raw/between/reel-29sep/mg-mano.mp4 \
      --salida out/hilton/between/reel29-op3.mp4
"""
import argparse, subprocess, os, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(RAIZ, "raw", "between", "reel-29sep")
FF = None
try:
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FF = "ffmpeg"

W, H = 2160, 3840                 # cuadro final
IX, IY, IW, IH = 30, 200, 2100, 3440   # recuadro interior en la edición 2
CORTES = [0, 86, 150]
ANCLA_Y = 1650                    # cinturón en el interior             # primer cuadro de cada toma (medido por flujo óptico)
TEXTO = [("Por esto nací", 658.5, 1271.5), ("con dos manos", 590.5, 1409.5)]  # origen PIL en el interior;
# calzado por coincidencia de la tinta contra la edición 2 (IoU 0,87 y 0,86)


def leer(ruta, tam):
    cap = cv2.VideoCapture(ruta)
    fr = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        if (f.shape[1], f.shape[0]) != tam:
            f = cv2.resize(f, tam, interpolation=cv2.INTER_LANCZOS4)
        fr.append(f)
    return fr


def movimiento(a, b, mascara=None):
    ga = cv2.resize(cv2.cvtColor(a, cv2.COLOR_BGR2GRAY), None, fx=.5, fy=.5)
    gb = cv2.resize(cv2.cvtColor(b, cv2.COLOR_BGR2GRAY), None, fx=.5, fy=.5)
    p = cv2.goodFeaturesToTrack(ga, 500, 0.01, 12, mask=mascara)
    n, st, _ = cv2.calcOpticalFlowPyrLK(ga, gb, p, None)
    m, _ = cv2.estimateAffinePartial2D(p[st == 1], n[st == 1], method=cv2.RANSAC)
    dx, dy = m[0, 2] * 2, m[1, 2] * 2
    da = np.arctan2(m[1, 0], m[0, 0])
    return dx, dy, da


def estabilizar(fr, suavizado):
    """Por toma: trayectoria acumulada → se lleva a su media (cámara fija) o a
    una versión muy suavizada; devuelve cuadros corregidos y el zoom necesario."""
    # ancla: del cinturón hacia abajo (cuerpo rígido + fondo lateral); las
    # manos se mueven a propósito y no deben arrastrar la corrección
    mask = np.zeros((IH // 2, IW // 2), np.uint8)
    mask[ANCLA_Y // 2:, :] = 255
    tomas = CORTES + [len(fr)]
    salida, zoom = [None] * len(fr), 1.0
    for t in range(len(tomas) - 1):
        a, b = tomas[t], tomas[t + 1]
        tr = [(0.0, 0.0, 0.0)]
        for i in range(a + 1, b):
            dx, dy, da = movimiento(fr[i - 1], fr[i], mask)
            x, y, r = tr[-1]
            tr.append((x + dx, y + dy, r + da))
        tr = np.array(tr)
        if suavizado <= 0:
            meta = np.repeat(tr.mean(0, keepdims=True), len(tr), 0)
        else:
            k = suavizado
            pad = np.pad(tr, ((k, k), (0, 0)), mode="edge")
            meta = np.stack([np.convolve(pad[:, j], np.ones(2 * k + 1) / (2 * k + 1), "valid") for j in range(3)], 1)
        corr = meta - tr
        for j, i in enumerate(range(a, b)):
            dx, dy, da = corr[j]
            c, s = np.cos(da), np.sin(da)
            M = np.array([[c, -s, dx], [s, c, dy]])
            # centro de rotación en el medio del cuadro
            cx, cy = IW / 2, IH / 2
            M[0, 2] += cx - (c * cx - s * cy)
            M[1, 2] += cy - (s * cx + c * cy)
            salida[i] = M
            # zoom que tapa los bordes negros
            need = 1 + 2 * max(abs(dx) / IW, abs(dy) / IH) + abs(da) * (IW + IH) / min(IW, IH) / 2
            zoom = max(zoom, need)
    return salida, zoom


def texto_rgba():
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    f = ImageFont.truetype(os.path.join(DIR, "f", "Raleway.ttf"), 128)
    f.set_variation_by_name(b"SemiBold")
    for txt, x, y in TEXTO:
        d.text((IX + x, IY + y), txt, font=f, fill=(254, 248, 234, 255),
               stroke_width=10, stroke_fill=(100, 91, 74, 235))
    return np.array(capa)


PARCHE_TEXTO_DESPLAZ = (-1.9, -1.8)   # Aleph sale corrido ~0,6 px a 666 de ancho (phaseCorrelate)
MANO = (1140, 240, 960, 1060)         # recorte que se le mandó a Magnific
MANO_HASTA = 150                      # tomas 1 y 2 (palma abierta); en la 3 la mano toma el vaso


def mascara_texto():
    """El texto de la edición 2 está fijo en pantalla: se recalca con la misma
    fuente, se engorda y se difumina el borde. Sólo esa zona se reemplaza."""
    t = texto_rgba()[IY:IY + IH, IX:IX + IW, 3]
    m = cv2.dilate((t > 0).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (29, 29)))
    return cv2.GaussianBlur(m.astype(np.float32), (0, 0), 6)


def mascara_piel(bgr):
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    h, s_, v = hsv[..., 0].astype(int), hsv[..., 1], hsv[..., 2]
    m = (((h <= 14) | (h >= 170)) & (s_ > 40) & (s_ < 150) & (v > 110)).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    m = cv2.erode(m, np.ones((7, 7), np.uint8))   # sin tocar el filo de la mano ni las uñas
    return cv2.GaussianBlur(m.astype(np.float32), (0, 0), 5)


def parchar(base, parche, m, desplaz=(0, 0)):
    """Pega `parche` sobre `base` donde manda la máscara, igualando el color
    medio en el anillo alrededor y devolviéndole el grano del original.
    Trabaja sólo en la caja de la máscara (más un margen para el anillo)."""
    ys, xs = np.nonzero(m > 0.001)
    if len(ys) == 0:
        return base
    y0, y1 = max(ys.min() - 60, 0), min(ys.max() + 61, base.shape[0])
    x0, x1 = max(xs.min() - 60, 0), min(xs.max() + 61, base.shape[1])
    out = base.copy()
    out[y0:y1, x0:x1] = _parchar(base[y0:y1, x0:x1], parche[y0:y1, x0:x1], m[y0:y1, x0:x1], desplaz)
    return out


def _parchar(base, parche, m, desplaz):
    if desplaz != (0, 0):
        M = np.float32([[1, 0, desplaz[0]], [0, 1, desplaz[1]]])
        parche = cv2.warpAffine(parche, M, (parche.shape[1], parche.shape[0]), borderMode=cv2.BORDER_REFLECT)
    b, p_ = base.astype(np.float32), parche.astype(np.float32)
    duro = m > 0.02
    anillo = (cv2.dilate(duro.astype(np.uint8), np.ones((41, 41), np.uint8)) > 0) & ~duro
    if anillo.sum() > 200:
        p_ += (b[anillo].mean(0) - p_[anillo].mean(0))
    # grano: el original tiene ruido fino que el parche reescalado perdió
    ruido = b - cv2.GaussianBlur(b, (0, 0), 1.2)
    ruido_p = p_ - cv2.GaussianBlur(p_, (0, 0), 1.2)
    if anillo.sum() > 200:
        falta = ruido[anillo].var() - ruido_p[anillo].var()
        if falta > 0:
            p_ += np.random.default_rng().normal(0, np.sqrt(falta), p_.shape[:2])[..., None]
    a = m[..., None]
    return np.clip(b * (1 - a) + p_ * a, 0, 255).astype(np.uint8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--original", default=os.path.join(DIR, "interior.mp4"))
    ap.add_argument("--parche-texto", help="interior sin texto (Magnific Aleph, mismo encuadre)")
    ap.add_argument("--parche-mano", help="recorte de la mano sin sombra (Magnific Aleph)")
    ap.add_argument("--suavizado", type=int, default=0, help="0 = cámara fija por toma")
    ap.add_argument("--sin-texto", action="store_true")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    orig = leer(a.original, (IW, IH))
    n = len(orig)
    fuente = [f.copy() for f in orig]
    if a.parche_texto:
        m = mascara_texto()
        limpio = leer(a.parche_texto, (IW, IH))
        for i in range(min(n, len(limpio))):
            fuente[i] = parchar(fuente[i], limpio[i], m, desplaz=PARCHE_TEXTO_DESPLAZ)
    if a.parche_mano:
        x, y, w, h = MANO
        mano = leer(a.parche_mano, (w, h))
        # Aleph devolvió el recorte a 24 cps (119 cuadros para 150): se toma el
        # cuadro más cercano en el tiempo; el calce medido es < 0,4 px
        for i in range(min(n, MANO_HASTA)):
            j = min(round(i * len(mano) / MANO_HASTA), len(mano) - 1)
            base = fuente[i][y:y + h, x:x + w]
            mk = mascara_piel(base)
            fuente[i][y:y + h, x:x + w] = parchar(base, mano[j], mk)
    # el movimiento se mide sobre la fuente que se va a mostrar
    Ms, zoom = estabilizar(fuente, a.suavizado)
    print(f"cuadros {n} · zoom para tapar bordes {zoom:.3f}", file=sys.stderr)

    txt = None if a.sin_texto else texto_rgba()
    alfa = None if txt is None else txt[:, :, 3:4].astype(np.float32) / 255
    rgb = None if txt is None else txt[:, :, 2::-1].astype(np.float32)  # RGBA → BGR

    tmp = a.salida + ".silencio.mp4"
    os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
    p = subprocess.Popen([FF, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                          "-r", "30", "-i", "-", "-c:v", "libx264", "-crf", "14", "-preset", "slow",
                          "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
    Z = np.array([[zoom, 0, (1 - zoom) * IW / 2], [0, zoom, (1 - zoom) * IH / 2], [0, 0, 1]])
    for i in range(n):
        M = np.vstack([Ms[i], [0, 0, 1]])
        inner = cv2.warpAffine(fuente[i], (Z @ M)[:2], (IW, IH), flags=cv2.INTER_LANCZOS4,
                               borderMode=cv2.BORDER_REFLECT)
        # fondo: el mismo cuadro estabilizado, agrandado y desenfocado (como en la edición 2)
        esc = max(W / IW, H / IH)
        fondo = cv2.resize(inner, (round(IW * esc), round(IH * esc)))
        x0, y0 = (fondo.shape[1] - W) // 2, (fondo.shape[0] - H) // 2
        fondo = fondo[y0:y0 + H, x0:x0 + W]
        fondo = cv2.GaussianBlur(fondo, (0, 0), 40)
        cuadro = fondo.copy()
        cuadro[IY:IY + IH, IX:IX + IW] = inner
        if txt is not None:
            cuadro = (cuadro * (1 - alfa) + rgb * alfa).astype(np.uint8)
        p.stdin.write(cuadro.tobytes())
    p.stdin.close(); p.wait()
    subprocess.run([FF, "-v", "error", "-y", "-i", tmp, "-i", os.path.join(DIR, "ed2.mp4"), "-map", "0:v",
                    "-map", "1:a", "-c:v", "copy", "-c:a", "copy", "-shortest", a.salida], check=True)
    os.remove(tmp)
    print(a.salida)


if __name__ == "__main__":
    main()

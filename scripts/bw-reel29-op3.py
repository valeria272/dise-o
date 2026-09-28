"""BETWEEN · Reel n°1 S3 «La razón» (29-09) — opción 3.

Parte de la edición 2 aprobada por el cliente y le aplica lo que pidieron:
  1. estabiliza la cámara (cada una de las 3 tomas por separado, cámara fija);
  2. usa el interior limpio que devuelve Magnific (sin texto y sin la sombra
     sobre la mano) si se le pasa con --limpio;
  3. rearma el fondo desenfocado y vuelve a poner el texto con la misma
     tipografía, cuerpo, color y posición que la edición 2 (medidos al píxel:
     Raleway Medium 127 px, relleno #FEF8EA, borde #645B4A ~10 px).

Uso:
  python scripts/bw-reel29-op3.py --limpio raw/between/reel-29sep/limpio.mp4 \
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
CORTES = [0, 86, 150]             # primer cuadro de cada toma (medido por flujo óptico)
TEXTO = [("Por esto nací", 670, 1302), ("con dos manos", 596, 1462)]  # x tinta, alto de la P / la c


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
    mask = None
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
    f = ImageFont.truetype(os.path.join(DIR, "f", "Raleway.ttf"), 127)
    f.set_variation_by_name(b"Medium")
    for txt, x, ytope in TEXTO:
        bx = f.getbbox(txt)
        # alinear la tinta: bbox[0] es el lado izquierdo de la tinta; bbox[1] el tope de la P/c
        ref = f.getbbox(txt[0])
        ox, oy = IX + x - bx[0], IY + ytope - ref[1]
        d.text((ox, oy), txt, font=f, fill=(254, 248, 234, 255),
               stroke_width=10, stroke_fill=(100, 91, 74, 235))
    return np.array(capa)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--original", default=os.path.join(DIR, "interior.mp4"))
    ap.add_argument("--limpio", help="interior sin texto ni sombra (Magnific)")
    ap.add_argument("--suavizado", type=int, default=0, help="0 = cámara fija por toma")
    ap.add_argument("--sin-texto", action="store_true")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    orig = leer(a.original, (IW, IH))
    fuente = leer(a.limpio, (IW, IH)) if a.limpio else orig
    n = min(len(orig), len(fuente))
    orig, fuente = orig[:n], fuente[:n]
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
        fondo = cv2.resize(inner, (W, int(IH * W / IW)))
        y0 = (fondo.shape[0] - H) // 2
        fondo = fondo[y0:y0 + H] if y0 >= 0 else cv2.resize(inner, (W, H))
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

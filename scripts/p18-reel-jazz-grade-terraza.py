# -*- coding: utf-8 -*-
"""
PISO 18 - REEL S4 JAZZ - hornea la correccion de la toma de la terraza.

IMG_4183 se rodo a contraluz contra el sol y trae velo atmosferico: el negro
esta levantado (p0.5 = 28,6 cuando deberia estar cerca de 10), hay dominante
azul pareja (R-B = -7,8 en sombras, medios y altas) y el micro contraste esta
muerto (nitidez 850 contra 7661 de la toma de las flores). Eso es lo que se ve
como "quemado": NO hay recorte (p99 = 239, 0,00 % de pixeles en 254).

Los deslizadores de CapCut no alcanzan porque su contraste pivotea en el 50 %
y la mediana de este plano esta en 144: subir contraste la empuja MAS arriba.
Asi que la correccion se hornea aca, medida, y CapCut la recibe ya aplicada.

La receta, en orden:
  1. niveles por canal   -> quita el velo Y baja el azul de una vez
  2. gamma casi neutra   -> la exposicion NO se toca
  3. claridad (radio grande) -> corta la calima
  4. nitidez (radio chico)   -> recupera micro contraste
  5. rodilla tanh al final   -> comprime las altas, NO recorta
  6. piso de negro           -> negro hondo sin aplastarlo a cero

El audio del original se copia tal cual: la pista de voz del reel sale de este
mismo archivo y tiene que seguir calzando.
"""
import os, sys, subprocess
import cv2
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")

SRC = r"F:\Carpeta de grillas Hilton 2026\SEPTIEMBRE\P18\GRILLA S3 P18\LLEGADA DE LA PRIMAVERA\IMG_4183.MOV"
OUT_DIR = r"C:\Users\Elisabet\EDITOR VIDEOS\out\piso18\reel-s4-jazz"
OUT = os.path.join(OUT_DIR, "IMG_4183-corregido.mp4")
# el ffmpeg que trae CapCut viene recortado y no acepta -crf; este si
FFMPEG = (r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib"
          r"\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe")

# Variante V. La primera (M) se rechazo: "se ve extrano y oscuro". Al medirla,
# las sombras caian de 65 a 35,7 y la piel de 135,0 a 122,6 - por eso pesaba.
# V corrige SOLO el velo y deja la exposicion como estaba:
#   piel 135,0 (identica)  ·  p50 143,5 (original 144,0)  ·  sombras 58,2 (65,0)
#   punto de negro 28,2 -> 12,0  ·  dominante azul -7,9 -> -4,0  ·  nitidez x2
# La regla: si la correccion se nota, esta mal. Solo tiene que irse la calima.
P = dict(mn=[.058, .050, .036], mx=[.980, .977, .970], gamma=1.04,
         lift=.0, lc=.46, lw=.16, claridad=.12, nitidez=.38,
         knee=.76, piso=.045, sat=.04)


def grade(f, mn, mx, gamma, lift, lc, lw, claridad, nitidez, knee, piso, sat):
    x = f.astype(np.float32) / 255.0
    x = np.clip((x - np.array(mn, np.float32)) /
                (np.array(mx, np.float32) - np.array(mn, np.float32)), 0, None)
    x = np.power(np.clip(x, 0, 2), gamma)
    if lift:
        y = cv2.cvtColor((np.clip(x, 0, 1) * 255).astype(np.uint8),
                         cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.
        x = x + lift * np.exp(-((y - lc) ** 2) / (2 * lw * lw))[..., None]
    y = cv2.cvtColor((np.clip(x, 0, 1) * 255).astype(np.uint8),
                     cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.
    b = cv2.GaussianBlur(y, (0, 0), 18)
    x = x + claridad * ((y - b)[..., None]) * 2.2
    bl = cv2.GaussianBlur(x, (0, 0), 1.4)
    x = x + nitidez * (x - bl)
    hi = x > knee
    x[hi] = knee + (1.0 - knee) * np.tanh((x[hi] - knee) / (1.0 - knee))
    x = piso + (1.0 - piso) * np.clip(x, 0, 1)
    hs = cv2.cvtColor((np.clip(x, 0, 1) * 255).astype(np.uint8),
                      cv2.COLOR_BGR2HSV).astype(np.float32)
    hs[..., 1] = np.clip(hs[..., 1] * (1 + sat), 0, 255)
    return cv2.cvtColor(hs.astype(np.uint8), cv2.COLOR_HSV2BGR)


os.makedirs(OUT_DIR, exist_ok=True)
c = cv2.VideoCapture(SRC)
fps = c.get(cv2.CAP_PROP_FPS)
W = int(c.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(c.get(cv2.CAP_PROP_FRAME_HEIGHT))
N = int(c.get(cv2.CAP_PROP_FRAME_COUNT))
print("fuente : %dx%d  %.3f fps  %d fotogramas  %.2f s" % (W, H, fps, N, N / fps))

tmp = os.path.join(OUT_DIR, "_tmp_video.mp4")
cmd = [FFMPEG, "-y", "-v", "error",
       "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", "%dx%d" % (W, H),
       "-r", "%.6f" % fps, "-i", "pipe:0",
       "-c:v", "libx264", "-preset", "slow", "-crf", "16",
       "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)

antes, despues = [], []
n = 0
while True:
    ok, f = c.read()
    if not ok:
        break
    g = grade(f, **P)
    if n % 60 == 0:
        for acc, im in ((antes, f), (despues, g)):
            y = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            xx = im.astype(np.float32)
            acc.append((np.percentile(y, 0.5), np.percentile(y, 50), np.percentile(y, 99),
                        100 * np.count_nonzero(y >= 254) / y.size,
                        xx[..., 2].mean() - xx[..., 0].mean(),
                        cv2.Laplacian(cv2.resize(y, (270, 480)), cv2.CV_64F).var()))
    pr.stdin.write(g.tobytes())
    n += 1
    if n % 90 == 0:
        print("   %d/%d" % (n, N))
pr.stdin.close()
pr.wait()
c.release()
print("codificados %d fotogramas" % n)

# el audio original se copia sin recodificar: la voz del reel sale de aca
sub = subprocess.run([FFMPEG, "-y", "-v", "error", "-i", tmp, "-i", SRC,
                      "-map", "0:v:0", "-map", "1:a:0?", "-c:v", "copy",
                      "-c:a", "aac", "-b:a", "192k", "-shortest", OUT],
                     capture_output=True, text=True)
if sub.returncode != 0:
    print("ffmpeg (mux):", sub.stderr[:400])
    raise SystemExit(1)
os.remove(tmp)

print()
print("                p0.5    p50    p99   clip%    R-B   nitidez")
for nom, acc in (("ANTES  ", antes), ("DESPUES", despues)):
    a = np.array(acc)
    print("  %s      %5.1f  %5.1f  %5.1f   %5.2f  %+5.1f    %5.0f"
          % (nom, a[:, 0].mean(), a[:, 1].mean(), a[:, 2].mean(),
             a[:, 3].mean(), a[:, 4].mean(), a[:, 5].mean()))

# verificacion sobre el ARCHIVO escrito, no sobre la memoria
v = cv2.VideoCapture(OUT)
fps2 = v.get(cv2.CAP_PROP_FPS)
n2 = int(v.get(cv2.CAP_PROP_FRAME_COUNT))
w2 = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))
h2 = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))
v.release()
print()
print("archivo : %s" % OUT)
print("          %dx%d  %.3f fps  %d fotogramas  %.2f s  %.1f MB"
      % (w2, h2, fps2, n2, n2 / fps2, os.path.getsize(OUT) / 1e6))
ok = (w2 == W and h2 == H and abs(n2 / fps2 - N / fps) < 0.05)
print("          calza con el original: %s" % ("SI" if ok else "NO - revisar"))
if not ok:
    raise SystemExit("el clip corregido no calza con el original")

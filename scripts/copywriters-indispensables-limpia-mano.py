"""Borra la mano que entra por la izquierda al final de p1-vacio-2861-largo (feedback de
Pau Bustamante, 02-10: «se ve alguien a la izquierda con sombra»).

Desde el cuadro 75 del clip alguien entra con el gimbal. La cámara está casi quieta: se
alinea el cuadro 74 (limpio) a cada cuadro por correlación de fase y se pega el muro
limpio donde aparece la mano (máscara por diferencia, sólo en el tercio izquierdo).

Todo se hace en los planos YUV del video (sin pasar por RGB): el resto del clip sale con
el mismo color que entró. También se borra la mano de las siluetas silueta-p1/
(índice = cuadro del clip − 15).

Uso: python3 scripts/copywriters-indispensables-limpia-mano.py <clip-origen-sin-limpiar.mp4>
"""
import json, subprocess, sys
from pathlib import Path
import cv2, numpy as np
import imageio_ffmpeg  # el ffmpeg de Remotion no trae rawvideo

RAIZ = Path(__file__).resolve().parent.parent
A = RAIZ / "public/assets/copywriters/indispensables"
X = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1080, 1920
LIMPIO, DESDE, BORDE = 74, 75, 430
origen = Path(sys.argv[1])

crudo = subprocess.run([X, "-v", "error", "-i", str(origen), "-f", "rawvideo", "-pix_fmt", "yuv420p", "-"], capture_output=True, check=True).stdout
T = W * H * 3 // 2
cuadros = []
for k in range(len(crudo) // T):
    a = np.frombuffer(crudo, np.uint8, T, k * T)
    y = a[: W * H].reshape(H, W).copy()
    u = a[W * H : W * H * 5 // 4].reshape(H // 2, W // 2).copy()
    v = a[W * H * 5 // 4 :].reshape(H // 2, W // 2).copy()
    cuadros.append([y, u, v])

ref = cuadros[LIMPIO][0].astype(np.float32)
mascaras = {}
for i in range(DESDE, len(cuadros)):
    y, u, v = cuadros[i]
    (dx, dy), _ = cv2.phaseCorrelate(ref[:, 500:], y[:, 500:].astype(np.float32))
    mueve = lambda p, s: cv2.warpAffine(p, np.float32([[1, 0, dx * s], [0, 1, dy * s]]), (p.shape[1], p.shape[0]), borderMode=cv2.BORDER_REFLECT)
    ly, lu, lv = mueve(cuadros[LIMPIO][0], 1), mueve(cuadros[LIMPIO][1], 0.5), mueve(cuadros[LIMPIO][2], 0.5)
    d = np.abs(y.astype(np.int16) - ly).astype(np.uint8)
    d = np.maximum(d, cv2.resize(np.maximum(np.abs(u.astype(np.int16) - lu), np.abs(v.astype(np.int16) - lv)).astype(np.uint8) * 2, (W, H)))
    m = (d > 18).astype(np.uint8)
    m[:, BORDE:] = 0
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    m = cv2.dilate(m, np.ones((41, 41), np.uint8))
    alfa = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 9)
    a2 = cv2.resize(alfa, (W // 2, H // 2))
    cuadros[i] = [
        (y * (1 - alfa) + ly * alfa).round().astype(np.uint8),
        (u * (1 - a2) + lu * a2).round().astype(np.uint8),
        (v * (1 - a2) + lv * a2).round().astype(np.uint8),
    ]
    mascaras[i] = alfa
    print(i, f"dx {dx:.1f} dy {dy:.1f}", "px", int(m.sum()))

tmp = A / "p1-vacio-2861-largo.tmp.mp4"
p = subprocess.Popen(
    [X, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "yuv420p", "-s", f"{W}x{H}", "-r", "30",
     # las etiquetas van también en la ENTRADA: si sólo están en la salida, ffmpeg convierte
     # 601→709 y el clip queda 2 niveles más oscuro
     "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-color_range", "tv", "-i", "-",
     "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-pix_fmt", "yuv420p",
     "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-color_range", "tv", str(tmp)],
    stdin=subprocess.PIPE)
for y, u, v in cuadros:
    p.stdin.write(y.tobytes() + u.tobytes() + v.tobytes())
p.stdin.close()
p.wait()
tmp.replace(A / "p1-vacio-2861-largo.mp4")

# siluetas: sacar la mano del alfa
cajas = json.load(open(A / "silueta-p1/cajas.json"))
for k, (x, y, w, h) in enumerate(cajas):
    i = k + 15
    if i not in mascaras:
        continue
    png = A / f"silueta-p1/{k:02d}.png"
    im = cv2.imread(str(png), cv2.IMREAD_UNCHANGED)
    m = cv2.resize(mascaras[i][y : y + h, x : x + w], (im.shape[1], im.shape[0]))
    im[..., 3] = (im[..., 3] * (1 - m)).astype(np.uint8)
    cv2.imwrite(str(png), im)
    print("silueta", k)

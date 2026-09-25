"""Expandir con IA un reel que trae el clip achicado sobre un fondo desenfocado.

Uso (BW «La razón», 25-09-2026):
  1. Recortar el centro nítido (CX/CY/CW/CH abajo; se miden con el gradiente del borde),
     subirlo a Higgsfield y pasarlo por reframe 9:16 (75 créditos / 8 s). Bajar el resultado como <dir>/ia.mp4
  2. python scripts/expandir-reel-ia.py <dir> <original.mp4> <ffmpeg.exe>  ->  <dir>/expandido.mp4

Reframe aleja la cámara y entrega 720p: NO se usa su encuadre. Sólo se toman las
franjas arriba/abajo y el centro original 4K va encima, a ancho completo.
Memoria: expandir-video-reframe-higgsfield.
"""
import subprocess, sys
import cv2, numpy as np

S, ORIG, FF = sys.argv[1], sys.argv[2], sys.argv[3]
IA, OUT = f"{S}/ia.mp4", f"{S}/expandido.mp4"
W, H = 2160, 3840
CX, CY, CW, CH = 34, 203, 2092, 3434
K = W / CW                       # centro a ancho completo
PH = int(round(CH * K))          # alto del centro en el lienzo
PY = (H - PH) // 2               # franja superior
FEATHER = 36

ia = cv2.VideoCapture(IA); og = cv2.VideoCapture(ORIG)
ifps = ia.get(5); ofps = og.get(5); onf = int(og.get(7))
iafr = []
while True:
    ok, f = ia.read()
    if not ok: break
    iafr.append(f)
Q = 0.25   # centros del original guardados a 1/4 para el matching
ofr = []
while True:
    ok, f = og.read()
    if not ok: break
    ofr.append(cv2.resize(f[CY:CY + CH, CX:CX + CW], None, fx=Q, fy=Q, interpolation=cv2.INTER_AREA))
print("IA", iafr[0].shape, ifps, len(iafr), "| orig", len(ofr), ofps)

def g(im): return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# escala: búsqueda fina en un frame
def match(fa, fo, scales):
    c = fo; best = None
    for s in scales:
        t = cv2.resize(c, None, fx=s / Q, fy=s / Q, interpolation=cv2.INTER_AREA)
        if t.shape[0] >= fa.shape[0] or t.shape[1] >= fa.shape[1]: continue
        r = cv2.matchTemplate(g(fa), g(t), cv2.TM_CCOEFF_NORMED)
        _, mx, _, loc = cv2.minMaxLoc(r)
        if best is None or mx > best[0]: best = (mx, s, loc)
    return best

mx, s0, _ = match(iafr[24], ofr[30], np.linspace(0.15, 0.40, 101))
_, s0, _ = match(iafr[24], ofr[30], np.linspace(s0 - 0.004, s0 + 0.004, 17))
print(f"escala {s0:.4f} match {mx:.3f}")

# posición por frame IA (la IA puede derivar); se suaviza después
pos = []
for j, fa in enumerate(iafr):
    i = min(int(round(j / ifps * ofps)), len(ofr) - 1)
    m, _, loc = match(fa, ofr[i], [s0])
    pos.append((loc[0], loc[1], m))
pos = np.array(pos, float)
print("match min/med", pos[:, 2].min().round(3), np.median(pos[:, 2]).round(3),
      "x rango", pos[:, 0].min(), pos[:, 0].max(), "y rango", pos[:, 1].min(), pos[:, 1].max())
k = 9
pad = np.pad(pos[:, :2], ((k, k), (0, 0)), mode="edge")
sm = np.array([pad[j:j + 2 * k + 1].mean(0) for j in range(len(pos))])

tw = CW * s0                      # ancho del centro en la IA
kk = W / tw                       # IA -> lienzo
m = np.ones((H, W), np.float32)
m[:PY + FEATHER] = 0; m[PY + PH - FEATHER:] = 0
m = cv2.GaussianBlur(m, (0, 0), FEATHER / 2.5)[..., None]

enc = subprocess.Popen([FF, "-v", "error", "-y", "-f", "image2pipe", "-c:v", "png",
    "-framerate", str(ofps), "-i", "-", "-i", ORIG, "-map", "0:v", "-map", "1:a",
    "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
    "-c:a", "copy", "-movflags", "+faststart", "-shortest", OUT], stdin=subprocess.PIPE)

og = cv2.VideoCapture(ORIG)
for i in range(len(ofr)):
    ok, fo = og.read()
    j = min(int(round(i / ofps * ifps)), len(iafr) - 1)
    lx, ly = sm[j]
    # rectángulo IA que equivale al lienzo: x0 = lx, y0 = ly - PY/kk
    M = np.float32([[kk, 0, -lx * kk], [0, kk, -(ly - PY / kk) * kk]])
    bg = cv2.warpAffine(iafr[j], M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    fg = bg.copy()
    fg[PY:PY + PH] = cv2.resize(fo[CY:CY + CH, CX:CX + CW], (W, PH), interpolation=cv2.INTER_LANCZOS4)
    out = bg.astype(np.float32) * (1 - m) + fg.astype(np.float32) * m
    enc.stdin.write(cv2.imencode('.png', np.clip(out, 0, 255).astype(np.uint8), [cv2.IMWRITE_PNG_COMPRESSION, 1])[1].tobytes())
enc.stdin.close(); enc.wait()
print("ok", OUT, "PY", PY, "PH", PH)

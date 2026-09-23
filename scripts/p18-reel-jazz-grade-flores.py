# -*- coding: utf-8 -*-
"""
PISO 18 - REEL S4 JAZZ - hornea y conecta la correccion del plano de flores.

La toma que abre el montaje (IMG_0849, en 3,43 s) es tecnicamente de las
mejores del material: nitidez 7652 contra una mediana de 3782 en el reel. No
habia nada que arreglarle de foco. Lo que si tenia:

  - era el plano MAS CLARO del reel (p50 = 151) y entra justo despues de la
    entrada de Jaz, que esta en p50 = 52. Un salto de 99 puntos en un corte:
    el mayor del reel, y se siente como un fogonazo.
  - el muro del fondo salia lavado, sin tono, y rozaba el recorte (0,03 %).

Correccion (variante T): punto de negro, gamma 1,22, algo de claridad y
rodilla tanh. Baja a p50 136, sin recorte, y el fondo recupera tono.

Se conecta SOLO al plano de 3,43 s. El otro uso de IMG_0849 (el plano general
en 9,07 s) es otro tramo del mismo archivo, ya esta a p50 108 y se deja como
esta - por eso el material estaba clonado.
"""
import json, io, os, sys, shutil, subprocess
import cv2
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")

SRC = (r"F:\SESIONES HILTON\SESIONES PISO18\MATRIMONIO 2025 NUEVO\22-11"
       r"\MATRIMONIO 22-11\IMG_0849.MOV")
OUT_DIR = r"C:\Users\Elisabet\EDITOR VIDEOS\out\piso18\reel-s4-jazz"
OUT = os.path.join(OUT_DIR, "IMG_0849-corregido.mp4")
FFMPEG = (r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib"
          r"\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe")
D = (r"C:\Users\Elisabet\AppData\Local\CapCut\User Data\Projects"
     r"\com.lveditor.draft\REEL n1 S4 SEP PISO18 JAZZ CAMBIO 2")
EN = 3433333          # el plano heroe, en microsegundos

P = dict(mn=[.050, .034, .034], mx=[.980, .980, .980], gamma=1.22,
         knee=.62, piso=.022, sat=.05, claridad=.05)
A_CERO = ["brightness", "contrast", "saturation", "highlight", "shadow",
          "black", "clear", "temperature", "smart_color_adjust", "color_correct"]


def grade(f, mn, mx, gamma, knee, piso, sat, claridad):
    x = f.astype(np.float32) / 255.0
    x = np.clip((x - np.array(mn, np.float32)) /
                (np.array(mx, np.float32) - np.array(mn, np.float32)), 0, None)
    x = np.power(np.clip(x, 0, 2), gamma)
    if claridad:
        y = cv2.cvtColor((np.clip(x, 0, 1) * 255).astype(np.uint8),
                         cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.
        b = cv2.GaussianBlur(y, (0, 0), 18)
        x = x + claridad * ((y - b)[..., None]) * 2.2
    hi = x > knee
    x[hi] = knee + (1.0 - knee) * np.tanh((x[hi] - knee) / (1.0 - knee))
    x = piso + (1.0 - piso) * np.clip(x, 0, 1)
    hs = cv2.cvtColor((np.clip(x, 0, 1) * 255).astype(np.uint8),
                      cv2.COLOR_BGR2HSV).astype(np.float32)
    hs[..., 1] = np.clip(hs[..., 1] * (1 + sat), 0, 255)
    return cv2.cvtColor(hs.astype(np.uint8), cv2.COLOR_HSV2BGR)


# ------------------------------------------------------------------ hornear
os.makedirs(OUT_DIR, exist_ok=True)
c = cv2.VideoCapture(SRC)
fps = c.get(cv2.CAP_PROP_FPS)
W = int(c.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(c.get(cv2.CAP_PROP_FRAME_HEIGHT))
N = int(c.get(cv2.CAP_PROP_FRAME_COUNT))
print("fuente : %dx%d  %.3f fps  %d fotogramas  %.2f s" % (W, H, fps, N, N / fps))

tmp = os.path.join(OUT_DIR, "_tmp_flores.mp4")
pr = subprocess.Popen([FFMPEG, "-y", "-v", "error", "-f", "rawvideo",
                       "-pix_fmt", "bgr24", "-s", "%dx%d" % (W, H),
                       "-r", "%.6f" % fps, "-i", "pipe:0",
                       "-c:v", "libx264", "-preset", "slow", "-crf", "16",
                       "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp],
                      stdin=subprocess.PIPE)
antes, despues = [], []
n = 0
while True:
    ok, f = c.read()
    if not ok:
        break
    g = grade(f, **P)
    if n % 45 == 0:
        for acc, im in ((antes, f), (despues, g)):
            y = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            acc.append((np.percentile(y, 0.5), np.percentile(y, 50), np.percentile(y, 99),
                        100 * np.count_nonzero(y >= 254) / y.size,
                        cv2.Laplacian(cv2.resize(y, (270, 480)), cv2.CV_64F).var()))
    pr.stdin.write(g.tobytes())
    n += 1
pr.stdin.close()
pr.wait()
c.release()

sub = subprocess.run([FFMPEG, "-y", "-v", "error", "-i", tmp, "-i", SRC,
                      "-map", "0:v:0", "-map", "1:a:0?", "-c:v", "copy",
                      "-c:a", "aac", "-b:a", "192k", "-shortest", OUT],
                     capture_output=True, text=True)
if sub.returncode != 0:
    print(sub.stderr[:300])
    raise SystemExit(1)
os.remove(tmp)
print("codificados %d fotogramas -> %.1f MB" % (n, os.path.getsize(OUT) / 1e6))
print()
print("              p0.5    p50    p99   clip%  nitidez")
for nom, acc in (("ANTES  ", antes), ("DESPUES", despues)):
    a = np.array(acc)
    print("  %s    %5.1f  %5.1f  %5.1f   %5.2f   %6.0f"
          % (nom, a[:, 0].mean(), a[:, 1].mean(), a[:, 2].mean(), a[:, 3].mean(), a[:, 4].mean()))

# ------------------------------------------------------------------ conectar
print("\nconectando SOLO el plano de 3,43 s")
destinos = [os.path.join(D, "draft_content.json")]
for carpeta in ("Timelines", "subdraft"):
    base = os.path.join(D, carpeta)
    if os.path.isdir(base):
        for sub_ in os.listdir(base):
            p = os.path.join(base, sub_, "draft_content.json")
            if os.path.isfile(p):
                destinos.append(p)

tocados = 0
for p in destinos:
    d = json.load(io.open(p, encoding="utf-8"))
    cambio = False

    def anda(o):
        global cambio, tocados
        if isinstance(o, dict):
            if isinstance(o.get("materials"), dict) and isinstance(o.get("tracks"), list):
                M = o["materials"]
                vid = {v["id"]: v for v in M.get("videos", []) or []}
                ix = {}
                for k, v in M.items():
                    if isinstance(v, list):
                        for it in v:
                            if isinstance(it, dict) and "id" in it:
                                ix[it["id"]] = it
                for t in o["tracks"]:
                    if t.get("type") != "video":
                        continue
                    for s in t.get("segments", []):
                        if abs(s["target_timerange"]["start"] - EN) > 50000:
                            continue
                        mm = vid.get(s.get("material_id"))
                        if not mm or not (mm.get("path") or "").endswith("IMG_0849.MOV"):
                            continue
                        mm["path"] = OUT
                        mm["material_name"] = os.path.basename(OUT)
                        for r in s.get("extra_material_refs", []):
                            it = ix.get(r)
                            if isinstance(it, dict) and it.get("type") in A_CERO \
                                    and it.get("value"):
                                it["value"] = 0.0
                        cambio = True
                        tocados += 1
            for v in o.values():
                anda(v)
        elif isinstance(o, list):
            for v in o:
                anda(v)

    anda(d)
    if cambio:
        shutil.copy2(p, p + ".previo")
        io.open(p, "w", encoding="utf-8").write(
            json.dumps(d, ensure_ascii=False, separators=(",", ":")))
        print("  %s  actualizado" % p.replace(D, "."))

print("\n%d segmento(s) apuntados al clip corregido" % tocados)

# el otro uso de IMG_0849 tiene que seguir intacto
d = json.load(io.open(destinos[0], encoding="utf-8"))
orig = [v for v in d["materials"]["videos"] if (v.get("path") or "").endswith("IMG_0849.MOV")]
nuev = [v for v in d["materials"]["videos"] if (v.get("path") or "") == OUT]
print("  plano general de 9,07 s sigue en el original: %s" % ("SI" if orig else "NO - REVISAR"))
print("  plano heroe apunta al corregido            : %s" % ("SI" if nuev else "NO - REVISAR"))
if not orig or not nuev:
    raise SystemExit("revisar")
print("\nLISTO.")

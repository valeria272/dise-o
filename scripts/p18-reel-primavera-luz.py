# -*- coding: utf-8 -*-
"""PISO 18 - REEL DE PRIMAVERA: ajuste de luz y calidad. Sin tocar el montaje.

El encargo de Eli (22-09-2026): "ajuste de luz y edicion, no en texto, solamente
en la calidad y luces, que nada se vea quemado" - el comentario tipico de cliente
que hay que evitar. Asi que esto NO corta, NO reordena y NO toca la grafica:
solo grada la fotografia.

QUE TRAIA EL MASTER (medido sobre los 718 fotogramas, 2160x3840 HEVC 10 bits)

  - El plano del ventanal (14,43-21,57 s) es el problema: 2,32 % de la imagen
    por encima de 245 y 0,62 % pegada al blanco, con dominante azul de -15
    (R-B) y la protagonista a 113 de luminancia contra un contraluz de 250.
    Eso es lo que un cliente llama "quemado".
  - Los interiores traen el negro aplastado contra el cero (p0.5 = 0 en el
    plano de la cortina) y dominante calida de hasta +25 (R-B) por el tungsteno.
  - La grafica (pastilla fucsia semitransparente y caja blanca del CTA) es
    marca, no fotografia.

LA RECETA, EN ORDEN, Y POR QUE ESE ORDEN

  1. levante local del sujeto - campana estrecha sobre la luminancia desenfocada.
     Abre a quien esta en penumbra sin tocar ni el negro ni las altas. La campana
     va estrecha (aw ~.18) a proposito: ancha levantaba tambien la sombra
     profunda y el plano se veia lavado (p5 subia +21 en las pruebas).
  2. temperatura por mascara - solo sombras y medios, para que el cielo del
     ventanal siga siendo azul mientras el interior se corrige.
  3. claridad y nitidez CON FRENO DE ALTAS - el freno mira el pixel, no su
     vecindad: con la vecindad desenfocada, un punto de luz sobre fondo oscuro
     recibia realce completo y se disparaba a blanco. Sin freno, la correccion
     DEJABA MAS pixeles quemados de los que habia (0,29 % -> 0,41 %).
  4. rodilla tanh con techo en 0,980 - comprime las altas y les pone tope. El
     techo es lo que impide que un borde disparado por la claridad vuelva a
     pegarse al 255.
  5. piso de negro y saturacion - minimos, para que la imagen respire.

Y al final la grafica vuelve al original por mascara: sin eso el fucsia de marca
se corria hasta dE76 = 17,7 y el blanco del texto bajaba de 250 a 239.

LA VARA (se verifica sola al terminar): ningun plano puede quedar con mas
pixeles sobre 245 de los que traia, y el p99 no puede subir.

    python scripts/p18-reel-primavera-luz.py
"""
import os, sys, subprocess, time
import numpy as np
import cv2
from multiprocessing import Pool

sys.stdout.reconfigure(encoding="utf-8")

# Un hilo de OpenCV por proceso: con 8 procesos y OpenCV repartiendo cada
# GaussianBlur entre los 16 nucleos, la maquina se pisa a si misma y el
# rendimiento cae 4x (medido: 2,5 s/fotograma en solitario, 9 s en paralelo).
cv2.setNumThreads(1)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(RAIZ, "raw", "piso18", "video-ajuste-luz", "original.mp4")
DEST = os.path.join(RAIZ, "out", "piso18", "reel-primavera")
OUT  = os.path.join(DEST, "reel-primavera-luz.mp4")
FFMPEG = (r"C:\Users\Elisabet\AppData\Local\Python\pythoncore-3.14-64\Lib"
          r"\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe")

W, H, FPS = 2160, 3840, 30.0
WD, HD = 540, 960            # escala de trabajo para detectar la grafica
NUCLEOS = 8

# ---------------------------------------------------------------- los planos
BASE = dict(claridad=.07, nitidez=.14, sat=.03, piso=.012, knee=.80, ar=90)
PLANOS = [
  (  0, 100, "interior cortina",     dict(BASE, abrir=.09, ac=.26, aw=.17, piso=.015)),
  (100, 138, "mesa montada",         dict(BASE, abrir=.09, ac=.28, aw=.18, temp=-.012, knee=.82)),
  (138, 165, "arco floral",          dict(BASE, abrir=.07, ac=.35, aw=.18, temp=-.006)),
  (165, 192, "cuadro + ventana",     dict(BASE, abrir=.10, ac=.32, aw=.18, knee=.78)),
  (192, 333, "ella habla",           dict(BASE, abrir=.12, ac=.38, aw=.20, temp=.006)),
  (333, 377, "madera y flores",      dict(BASE, abrir=.08, ac=.30, aw=.18, temp=-.018)),
  (377, 433, "flores + ella",        dict(BASE, abrir=.08, ac=.34, aw=.18, temp=-.010)),
  (433, 648, "ventanal a contraluz", dict(BASE, abrir=.16, ac=.44, aw=.20, temp=.024, knee=.76)),
  (648, 718, "cierre - logo",        None),   # el negro y el logo no se tocan
]


def params(i):
    for a, b, _, P in PLANOS:
        if a <= i < b:
            return P
    return None


# ---------------------------------------------------------------- el motor
def _lum(z):
    return 0.2126*z[..., 0] + 0.7152*z[..., 1] + 0.0722*z[..., 2]


def _blur(y, sigma, baja=4):
    """Desenfoque grande barato: en 4K una gaussiana de sigma 90 cuesta mas que
    todo el resto junto. Se calcula en 1/4 y se sube; el error medido contra la
    exacta es 0,015/255 de media y 1,05 de maximo."""
    if sigma < 6:
        return cv2.GaussianBlur(y, (0, 0), sigma)
    h, w = y.shape[:2]
    z = cv2.resize(y, (max(8, w//baja), max(8, h//baja)), interpolation=cv2.INTER_AREA)
    z = cv2.GaussianBlur(z, (0, 0), sigma/baja)
    return cv2.resize(z, (w, h), interpolation=cv2.INTER_LINEAR)


def grade(rgb, abrir=0.0, ac=0.30, aw=0.20, ar=90.0, temp=0.0, tmax=0.55,
          claridad=0.0, nitidez=0.0, protege=0.55, knee=0.80, techo=0.980,
          piso=0.0, sat=0.0, escala=1.0):
    x = rgb.astype(np.float32)

    # freno de altas: 1 en sombras y medios, 0 de `protege` para arriba
    y0 = np.maximum(_lum(np.clip(x, 0, 1)), np.clip(x, 0, 1).max(axis=2))
    freno = np.clip((1.0 - y0) / (1.0 - protege), 0, 1)[..., None]

    if abrir:                                    # 1) levante local del sujeto
        yb = _blur(_lum(np.clip(x, 0, 1)), max(0.8, ar*escala))
        w = np.exp(-((yb - ac)**2) / (2*aw*aw))[..., None]
        x = x + abrir * w * (1.0 - np.clip(x, 0, 1))

    if temp:                                     # 2) temperatura sin tocar el cielo
        yb = _blur(_lum(np.clip(x, 0, 1)), max(0.8, 30*escala))
        w = np.clip((tmax - yb)/tmax, 0, 1)[..., None]
        x = x + w * np.array([temp, temp*0.35, -temp], np.float32)

    if claridad:                                 # 3) claridad y nitidez, frenadas
        y = _lum(np.clip(x, 0, 1))
        x = x + claridad * 2.2 * ((y - _blur(y, max(0.8, 60*escala)))[..., None]) * freno
    if nitidez:
        x = x + nitidez * (x - cv2.GaussianBlur(x, (0, 0), max(0.6, 5.0*escala))) * freno

    hi = x > knee                                # 4) rodilla con techo
    x[hi] = knee + (techo - knee)*np.tanh((x[hi] - knee)/(techo - knee))

    x = np.clip(x, 0, 1)                         # 5) piso y saturacion
    if piso:
        x = piso + (1.0 - piso)*x
    if sat:
        y = _lum(x)[..., None]
        x = np.clip(y + (x - y)*(1.0 + sat), 0, 1)
    return np.clip(x, 0, 1)


# ------------------------------------------------- la grafica (texto de marca)
def rects(f8):
    """Pastilla fucsia y caja blanca del CTA, en la escala 540x960."""
    h, w = f8.shape[:2]
    out = []
    hsv = cv2.cvtColor(f8, cv2.COLOR_RGB2HSV)
    Y = (.2126*f8[..., 0] + .7152*f8[..., 1] + .0722*f8[..., 2])
    dif = f8.max(2).astype(np.int16) - f8.min(2).astype(np.int16)

    m = ((hsv[..., 0] >= 155) & (hsv[..., 0] <= 180) & (hsv[..., 1] > 100) & (hsv[..., 2] > 60))
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((7, 25), np.uint8))
    nl, _, st, _ = cv2.connectedComponentsWithStats(m, 8)
    for i in range(1, nl):
        x, y, ww, hh, a = st[i]
        if ww > 90 and 14 < hh < 90 and ww/hh > 2.5 and y > 0.66*h and a > 0.45*ww*hh:
            out.append((int(x), int(y), int(ww), int(hh)))

    b = ((Y > 225) & (dif < 26)).astype(np.uint8)
    b = cv2.morphologyEx(b, cv2.MORPH_CLOSE, np.ones((9, 35), np.uint8))
    nl, _, st, _ = cv2.connectedComponentsWithStats(b, 8)
    for i in range(1, nl):
        x, y, ww, hh, a = st[i]
        if ww > 180 and 18 < hh < 90 and ww/hh > 3.0 and y > 0.60*h and a > 0.70*ww*hh:
            out.append((int(x), int(y), int(ww), int(hh)))
    return out


def rects_estables(F, hueco=8):
    """Los huecos cortos de deteccion se rellenan con la union de los bordes:
    sin esto la deteccion se cae 1-3 fotogramas sueltos y el texto entraria y
    saldria de la correccion - parpadeo."""
    todos = [rects(F[i]) for i in range(len(F))]
    hay = [i for i, r in enumerate(todos) if r]
    for a, b in zip(hay[:-1], hay[1:]):
        if 1 < b - a <= hueco + 1:
            u = todos[a] + todos[b]
            for i in range(a+1, b):
                todos[i] = u
    return todos


def mascara(rs, margen=5, pluma=3):
    m = np.zeros((HD, WD), np.float32)
    for x, y, w, h in rs:
        m[max(0, y-margen):min(HD, y+h+margen), max(0, x-margen):min(WD, x+w+margen)] = 1.0
    if not m.any():
        return None
    m = cv2.GaussianBlur(m, (0, 0), pluma)
    return cv2.resize(m, (W, H), interpolation=cv2.INTER_LINEAR)[..., None]


# ---------------------------------------------------------------- el render
RS = None   # lo llena cada proceso hijo


def _init(rs):
    global RS
    RS = rs


def medir(o):
    y = _lum(o)*255
    return (float(np.percentile(y, 5)), float(np.percentile(y, 50)),
            float(np.percentile(y, 99)),
            100.0*np.count_nonzero(y >= 245)/y.size)


def tramo(arg):
    """Un proceso por tramo: lee su rango del master, lo grada y lo codifica."""
    k, ini, fin = arg
    parcial = os.path.join(DEST, "_p%02d.mp4" % k)
    sello = parcial + ".ok"
    if os.path.exists(sello) and os.path.exists(parcial):
        import json
        d = json.load(open(sello, encoding="utf-8"))
        # el sello vale solo si cubre EXACTAMENTE el mismo rango: si cambia el
        # reparto en lotes, reutilizarlo pegaria fotogramas de otro tramo
        if d.get("ini") == ini and d.get("fin") == fin:
            return k, parcial, d["est"]
    lector = subprocess.Popen(
        [FFMPEG, "-v", "error", "-ss", "%.6f" % (ini/FPS), "-i", SRC,
         "-frames:v", str(fin-ini), "-f", "rawvideo", "-pix_fmt", "rgb48le", "pipe:1"],
        stdout=subprocess.PIPE, bufsize=10**8)
    escritor = subprocess.Popen(
        [FFMPEG, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb48le",
         "-s", "%dx%d" % (W, H), "-r", "%.6f" % FPS, "-i", "pipe:0",
         "-an", "-c:v", "libx265", "-preset", "ultrafast", "-crf", "16",
         "-pix_fmt", "yuv420p10le",
         "-x265-params", "keyint=30:min-keyint=30:log-level=none:pools=1:frame-threads=1",
         "-tag:v", "hvc1", parcial], stdin=subprocess.PIPE)
    nbytes = W*H*3*2
    est = []
    for i in range(ini, fin):
        crudo = lector.stdout.read(nbytes)
        if len(crudo) < nbytes:
            break
        f = np.frombuffer(crudo, np.uint16).reshape(H, W, 3).astype(np.float32)/65535.
        P = params(i)
        g = f if P is None else grade(f, escala=1.0, **P)
        m = mascara(RS[i]) if RS[i] else None
        if m is not None:
            g = g*(1.0 - m) + f*m          # la grafica vuelve intacta
        if i % 10 == 0:
            est.append((i,) + medir(f) + medir(g))
        escritor.stdin.write((np.clip(g, 0, 1)*65535 + 0.5).astype(np.uint16).tobytes())
        if (i - ini) % 15 == 14:
            print("     lote %02d: %d/%d" % (k, i-ini+1, fin-ini), flush=True)
    escritor.stdin.close(); escritor.wait()
    lector.stdout.close(); lector.wait()
    import json
    json.dump({"ini": ini, "fin": fin, "est": est}, open(sello, "w", encoding="utf-8"))
    return k, parcial, est


def main():
    os.makedirs(DEST, exist_ok=True)
    t0 = time.time()

    print("1/4  leyendo el master en pequeno para ubicar la grafica...")
    p = subprocess.run([FFMPEG, "-v", "error", "-i", SRC,
                        "-vf", "scale=%d:%d:flags=area" % (WD, HD),
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1"], capture_output=True)
    b = np.frombuffer(p.stdout, np.uint8)
    n = b.size//(WD*HD*3)
    F = b[:n*WD*HD*3].reshape(n, HD, WD, 3)
    rs = rects_estables(F)
    con = sum(1 for r in rs if r)
    print("     %d fotogramas  -  grafica en %d de ellos (%.0f %%)" % (n, con, 100*con/n))

    # mas lotes que procesos: cada lote cerrado deja su sello, asi un corte a
    # media maquina no obliga a rehacer todo el video (paso 2/4 es lo caro)
    paso = -(-n // (NUCLEOS*2))
    lotes = [(k, ini, min(n, ini+paso)) for k, ini in enumerate(range(0, n, paso))]
    hechos = sum(1 for k, _, _ in lotes if os.path.exists(
        os.path.join(DEST, "_p%02d.mp4.ok" % k)))
    print("2/4  gradando: %d lotes de %d fotogramas en %d procesos%s" % (
        len(lotes), paso, min(NUCLEOS, len(lotes)),
        "" if not hechos else "  (%d ya estaban hechos)" % hechos))
    with Pool(min(NUCLEOS, len(lotes)), initializer=_init, initargs=(rs,)) as pool:
        res = sorted(pool.map(tramo, lotes))
    print("     %.1f min" % ((time.time()-t0)/60))

    print("3/4  uniendo y devolviendo el audio original...")
    lista = os.path.join(DEST, "_lista.txt")
    with open(lista, "w", encoding="utf-8") as fh:
        for _, parcial, _ in res:
            fh.write("file '%s'\n" % parcial.replace("\\", "/"))
    sub = subprocess.run([FFMPEG, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                          "-i", lista, "-i", SRC, "-map", "0:v:0", "-map", "1:a:0?",
                          "-c:v", "copy", "-c:a", "copy", "-movflags", "+faststart",
                          "-tag:v", "hvc1", OUT],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    if sub.returncode != 0:
        print("ffmpeg (union):", sub.stderr[:600])
        raise SystemExit(1)
    for _, parcial, _ in res:
        os.remove(parcial)
        if os.path.exists(parcial + ".ok"):
            os.remove(parcial + ".ok")
    os.remove(lista)

    print("4/4  la vara: ningun plano con mas quemado ni p99 mas alto\n")
    est = [e for _, _, ee in res for e in ee]
    print("  plano                  p5             p50            p99          >=245 %")
    mal = 0
    for a, bb, nom, P in PLANOS:
        d = [e for e in est if a <= e[0] < bb]
        if not d:
            continue
        v = np.array([e[1:] for e in d])
        a0, a1 = v[:, :4].mean(0), v[:, 4:].mean(0)
        sello = "  ok"
        if P is not None and (a1[3] > a0[3] + 0.005 or a1[2] > a0[2] + 0.5):
            sello = "  <-- REVISAR"
            mal += 1
        print("  %-20s %5.1f>%5.1f  %6.1f>%6.1f  %6.1f>%6.1f  %5.2f>%5.2f%s" % (
            nom, a0[0], a1[0], a0[1], a1[1], a0[2], a1[2], a0[3], a1[3], sello))

    v = cv2.VideoCapture(OUT)
    print("\n  archivo : %s" % OUT)
    print("  %dx%d  %.3f fps  %d fotogramas  %.1f MB" % (
        v.get(cv2.CAP_PROP_FRAME_WIDTH), v.get(cv2.CAP_PROP_FRAME_HEIGHT),
        v.get(cv2.CAP_PROP_FPS), v.get(cv2.CAP_PROP_FRAME_COUNT),
        os.path.getsize(OUT)/1e6))
    v.release()
    print("  total %.1f min%s" % ((time.time()-t0)/60,
          "" if not mal else "   (%d plano(s) a revisar)" % mal))


if __name__ == "__main__":
    main()

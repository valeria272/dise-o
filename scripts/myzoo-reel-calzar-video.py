#!/usr/bin/env python3
"""MyZoo — calza el packshot REAL sobre los envases de un clip de video generado.

Por qué existe (reel 14 de octubre 2026): el cuadro de partida trae la etiqueta bien,
pero al animarlo el generador deforma la letra chica cuadro a cuadro («Polaje suave»,
«Hidrotonte y desonredonte»). Es la versión en video de `myzoo-f3-calzar.py`: la escena,
la luz y el movimiento son del clip; la etiqueta es la real.

  1. Por cuadro: SIFT + homografía (RANSAC) entre el packshot y la zona del envase.
  2. Las cuatro esquinas proyectadas se SUAVIZAN en el tiempo con una parábola en una
     ventana corta: sin eso la etiqueta tirita, porque cada cuadro calza con un error distinto.
  3. Del packshot se usa SÓLO la tinta de la etiqueta (packshot ÷ su blanco) y se imprime
     por multiplicación sobre el envase generado, al que antes se le borran sus letras.
     Forma, tapas, luz, sombra y reflejo quedan los de la escena. Pegar el packshot entero
     se veía «montado» (Paulina, 01-10-2026).
  4. Se trabaja al doble de resolución para que la letra chica quede nítida.

Uso:  python scripts/myzoo-reel-calzar-video.py <clip> <salida.mp4> <json de calces>
      el json: [{"pack": "ruta.png", "lado": "izq" | "der"}, …]
"""
import json
import os
import subprocess
import sys

import cv2
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# el ffmpeg que trae Remotion viene recortado (sin `rawvideo` ni filtros): se usa el completo
import imageio_ffmpeg
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
ESCALA = 2    # el clip sale al doble: la etiqueta real aguanta esa resolución
VENTANA = 4   # cuadros a cada lado para suavizar la trayectoria de las esquinas


def blur_enmascarado(img, m, s):
    num = cv2.GaussianBlur(img * m[..., None], (0, 0), s)
    den = cv2.GaussianBlur(m, (0, 0), s)[..., None]
    return num / np.maximum(den, 1e-4)


def recortar_alfa(pack):
    ys, xs = np.where(pack[..., 3] > 16)
    return pack[ys.min():ys.max() + 1, xs.min():xs.max() + 1].copy()


def medir(cuadros, pack, lado):
    """Esquinas del packshot proyectadas en cada cuadro, ya suavizadas en el tiempo."""
    H, W = cuadros[0].shape[:2]
    sift = cv2.SIFT_create(5000)
    ph, pw = pack.shape[:2]
    esc = (H * 0.42) / ph  # el envase ocupa cerca del 40 % del alto del cuadro
    p = cv2.resize(pack, None, fx=esc, fy=esc, interpolation=cv2.INTER_AREA)
    kp1, d1 = sift.detectAndCompute(cv2.cvtColor(p[..., :3], cv2.COLOR_BGR2GRAY),
                                    (p[..., 3] > 128).astype(np.uint8) * 255)
    S = np.diag([esc, esc, 1.0])
    esquinas = np.float32([[0, 0], [pw, 0], [pw, ph], [0, ph]]).reshape(-1, 1, 2)
    puntos, pesos = [], []
    for i, f in enumerate(cuadros):
        mask = np.zeros((H, W), np.uint8)
        if lado == "izq":
            mask[int(H * 0.30):, : int(W * 0.56)] = 255
        else:
            mask[int(H * 0.30):, int(W * 0.44):] = 255
        kp2, d2 = sift.detectAndCompute(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), mask)
        pares = cv2.BFMatcher().knnMatch(d1, d2, k=2)
        buenos = [m for m, n in pares if m.distance < 0.75 * n.distance]
        ok = False
        if len(buenos) >= 12:
            src = np.float32([kp1[m.queryIdx].pt for m in buenos])
            dst = np.float32([kp2[m.trainIdx].pt for m in buenos])
            Hm, inl = cv2.findHomography(src, dst, cv2.RANSAC, 3.0)
            if Hm is not None and inl.sum() >= 12:
                puntos.append(cv2.perspectiveTransform(esquinas, Hm @ S).reshape(8))
                pesos.append(float(inl.sum()))
                ok = True
        if not ok:
            puntos.append(np.zeros(8))
            pesos.append(0.0)
        if i % 20 == 0:
            print(f"    cuadro {i}: {len(buenos)} pares, {int(pesos[-1])} inliers")
    puntos, pesos = np.array(puntos), np.array(pesos)
    t = np.linspace(-1, 1, len(cuadros))
    buenos = pesos > 0
    print(f"  {lado}: {int(buenos.sum())}/{len(cuadros)} cuadros calzados, inliers medianos {int(np.median(pesos[buenos]))}")
    # Suavizado LOCAL (parábola en una ventana corta), no un polinomio de todo el clip:
    # la cámara generada deriva de forma irregular y un ajuste global dejaba la etiqueta
    # nadando 2 px sobre el envase.
    suave = np.zeros_like(puntos)
    idx = np.arange(len(cuadros))
    for i in idx:
        v = buenos & (np.abs(idx - i) <= VENTANA)
        for k in range(8):
            c = np.polyfit(t[v], puntos[v, k], 2, w=np.sqrt(pesos[v]))
            suave[i, k] = np.polyval(c, t[i])
    desvio = np.abs(suave[buenos] - puntos[buenos]).mean()
    print(f"  {lado}: desvío medio entre el calce crudo y el suavizado {desvio:.2f} px")
    return suave.reshape(-1, 4, 2), esquinas.reshape(4, 2)


def rellenar(F, valido):
    """Rellena lo no válido con el color de lo válido de alrededor, de grueso a fino."""
    S = None
    for s in (140, 60, 24, 9):
        b = blur_enmascarado(F, valido, s)
        w = np.clip(cv2.GaussianBlur(valido, (0, 0), s) / 0.25, 0, 1)[..., None]
        S = b if S is None else S * (1 - w) + b * w
    return S


def preparar(pack):
    """Del packshot sale SÓLO la tinta de la etiqueta, como fracción de su propio blanco.

    Paulina, 01-10-2026: pegar el packshot entero «se ve montado, sin las sombras ni la
    iluminación adecuadas». El envase trae su luz de estudio; si se pega, tapa la luz de la
    escena. Acá se le saca esa luz (tinta = packshot ÷ su blanco) y queda sólo lo impreso:
    1 donde el plástico está limpio, <1 donde hay tinta. Las tapas no se tocan.
    """
    P = pack[..., :3].astype(np.float32)
    a = pack[..., 3] > 230
    mn, mx = P.min(axis=2), P.max(axis=2)
    # el cuerpo blanco: las filas donde el envase es claro (las tapas negras quedan fuera)
    # (por fracción de píxeles claros y no por mediana: el círculo negro del logo ocupa
    #  más de media fila y la mediana partía el cuerpo en dos)
    claro = np.array([(mn[y][a[y]] > 170).mean() if a[y].sum() > 10 else 0 for y in range(P.shape[0])]) > 0.2
    runs, y = [], 0
    while y < len(claro):
        if claro[y]:
            y1 = y
            while y1 < len(claro) and claro[y1]:
                y1 += 1
            runs.append((y1 - y, y, y1))
            y = y1
        else:
            y += 1
    _, r0, r1 = max(runs)
    cuerpo = np.zeros(a.shape, np.float32)
    cuerpo[r0:r1] = a[r0:r1]
    k = max(3, P.shape[1] // 60)
    cuerpo = cv2.erode(cuerpo, np.ones((k, k), np.uint8))
    limpio = cuerpo * ((mx - mn < 18) & (mn > 175))
    limpio = cv2.erode(limpio, np.ones((5, 5), np.uint8))
    blanco = rellenar(P, limpio)
    T = np.clip(P / np.maximum(blanco, 1), 0, 1)
    # todo lo que está a menos de un 7 % del blanco ES blanco: el packshot trae recuadros
    # apenas más claros alrededor de los textos y se imprimían como parches
    T = np.clip(T / 0.93, 0, 1)
    T = T * cuerpo[..., None] + (1 - cuerpo[..., None])
    return T, cuerpo


def pegar(cuadro, T, cuerpo, esq_dst, esq_src):
    """Imprime la tinta real sobre el envase GENERADO, que conserva su luz y su sombra."""
    H, W = cuadro.shape[:2]
    Hm = cv2.getPerspectiveTransform(esq_src, np.float32(esq_dst))
    Tw = cv2.warpPerspective(T, Hm, (W, H), flags=cv2.INTER_LINEAR, borderValue=(1, 1, 1))
    M = cv2.warpPerspective(cuerpo, Hm, (W, H), flags=cv2.INTER_LINEAR)
    x, y, w, h = cv2.boundingRect((M > 0.5).astype(np.uint8))
    m = 20
    x0, y0, x1, y1 = max(0, x - m), max(0, y - m), min(W, x + w + m), min(H, y + h + m)
    F = cuadro[y0:y1, x0:x1].astype(np.float32)
    Tw, M = Tw[y0:y1, x0:x1], M[y0:y1, x0:x1]
    dentro = (M > 0.99).astype(np.float32)
    # 1) plástico limpio = dentro del cuerpo y lejos de donde va la tinta real
    tinta_real = cv2.dilate((Tw.min(axis=2) < 0.97).astype(np.uint8), np.ones((13, 13), np.uint8))
    valido = dentro * (1 - tinta_real)
    S0 = rellenar(F, valido)
    # 2) la tinta que dibujó el generador no cae exactamente donde la real: se detecta
    #    contra ese primer relleno y también se borra
    tinta_gen = (F.min(axis=2) < 0.90 * S0.min(axis=2)).astype(np.uint8)
    valido = valido * (1 - cv2.dilate(tinta_gen, np.ones((7, 7), np.uint8)))
    S = rellenar(F, valido)
    # el envase generado, sin letras, con SU luz. Se usa el relleno en todo el cuerpo y no
    # sólo bajo las letras: mezclarlo con el cuadro dejaba un rectángulo más claro alrededor
    # de cada bloque de texto. El plástico es liso, no se pierde nada.
    base = S
    piso = 0.07                          # el negro impreso no es negro absoluto al sol
    impreso = base * (Tw * (1 - piso) + piso)
    mm = cv2.GaussianBlur(cv2.erode(M, np.ones((5, 5), np.uint8)), (0, 0), 2.0)[..., None]
    cuadro[y0:y1, x0:x1] = np.clip(F * (1 - mm) + impreso * mm, 0, 255).astype(np.uint8)
    return cuadro


if __name__ == "__main__":
    clip, salida, cfg_path = sys.argv[1:4]
    cap = cv2.VideoCapture(clip)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cuadros = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        cuadros.append(f)
    H, W = cuadros[0].shape[:2]
    print(f"{len(cuadros)} cuadros, {W}×{H}, {fps} fps")
    calces = []
    for c in json.load(open(cfg_path, encoding="utf-8")):
        print("→", c["pack"])
        pack = recortar_alfa(cv2.imread(os.path.join(RAIZ, c["pack"]), cv2.IMREAD_UNCHANGED))
        tray, esq = medir(cuadros, pack, c["lado"])
        # warpPerspective no promedia al achicar: el packshot se lleva antes al tamaño
        # con que va a aparecer (más un margen), o la letra chica sale con dientes
        alto = np.linalg.norm(tray[:, 3] - tray[:, 0], axis=1).max() * ESCALA * 1.15
        k = min(1.0, alto / pack.shape[0])
        pack = cv2.resize(pack, None, fx=k, fy=k, interpolation=cv2.INTER_AREA)
        T, cuerpo = preparar(pack)
        calces.append((T, cuerpo, tray, esq * k))
    W2, H2 = W * ESCALA, H * ESCALA
    tmp = salida + ".part.mp4"
    ff = subprocess.Popen([FFMPEG, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
                           "-s", f"{W2}x{H2}", "-r", str(fps), "-i", "-", "-an",
                           "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-pix_fmt", "yuv420p", tmp],
                          stdin=subprocess.PIPE)
    for i, f in enumerate(cuadros):
        g = cv2.resize(f, (W2, H2), interpolation=cv2.INTER_LANCZOS4)
        for T, cuerpo, tray, esq in calces:
            g = pegar(g, T, cuerpo, tray[i] * ESCALA, esq)
        ff.stdin.write(g.tobytes())
        if i in (0, len(cuadros) // 2, len(cuadros) - 1):
            cv2.imwrite(f"{salida}.cuadro{i:03d}.png", g)
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg falló")
    os.replace(tmp, salida)
    print("✓", salida)

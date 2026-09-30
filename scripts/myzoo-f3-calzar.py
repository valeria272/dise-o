#!/usr/bin/env python3
"""MyZoo Fase 3 — calza el packshot REAL sobre el envase que la IA puso en la escena.

Por qué existe (Paulina, 30-09-2026): pegar el packshot con sombra por código «se ve
montado encima»; pedirle a la IA que ponga el envase lo integra bien a la escena, pero
Nano Banana Pro inventa la letra chica («Paso Moecotes», «Uto fracoonte»). Las
etiquetas no se tocan. Solución: la escena y la luz son de la IA; la etiqueta es la real.

  1. SIFT + homografía (RANSAC) entre el packshot real y la zona del envase generado.
  2. Se deforma el packshot real a esa posición y perspectiva.
  3. Se le traspasa la luz de la escena: razón de baja frecuencia, por canal, entre el
     envase generado y el real deformado (con desenfoque enmascarado para no traer halo
     del fondo). El detalle —el texto— es del real; la luz y el tono, de la escena.
  4. Orden: primero los de atrás, al final el de adelante (tapa lo que tiene que tapar).

Uso:  python scripts/myzoo-f3-calzar.py <escena> <salida> <json de calces>
      el json: [{"pack": "MyZoo_wipes_azul_110u.png", "roi": [x0,y0,x1,y1], "tapar": [[..]], "modelo": "afin"?}, …]
      «afin» para envases chicos con pocos rasgos: la homografía con 16 inliers se deforma.
"""
import json
import os
import sys

import cv2
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROD = os.path.join(RAIZ, "public/assets/myzoo/producto/")


def blur_enmascarado(img, m, s):
    num = cv2.GaussianBlur(img * m[..., None], (0, 0), s)
    den = cv2.GaussianBlur(m, (0, 0), s)[..., None]
    return num / np.maximum(den, 1e-4)


def calzar(escena, lienzo, pack_rgba, roi, tapar=(), modelo="homografia", luz="canal", relieve=None, mover=None):
    """Busca y mide la luz en `escena` (la ORIGINAL de la IA); pega sobre `lienzo`."""
    H, W = escena.shape[:2]
    sift = cv2.SIFT_create(6000)
    gris_e = cv2.cvtColor(escena, cv2.COLOR_BGR2GRAY)
    mask = np.zeros((H, W), np.uint8)
    x0, y0, x1, y1 = roi
    mask[y0:y1, x0:x1] = 255
    for t in tapar:
        mask[t[1]:t[3], t[0]:t[2]] = 0
    # el packshot se reduce a la escala aproximada del ROI para que SIFT empareje mejor
    # escala por la dimensión MAYOR: un envase acostado y girado ocupa el ROI a lo ancho
    esc = max(x1 - x0, y1 - y0) / max(pack_rgba.shape[:2])
    p = cv2.resize(pack_rgba, None, fx=esc, fy=esc, interpolation=cv2.INTER_AREA)
    gris_p = cv2.cvtColor(p[..., :3], cv2.COLOR_BGR2GRAY)
    kp1, d1 = sift.detectAndCompute(gris_p, (p[..., 3] > 128).astype(np.uint8) * 255)
    kp2, d2 = sift.detectAndCompute(gris_e, mask)
    pares = cv2.BFMatcher().knnMatch(d1, d2, k=2)
    buenos = [m for m, n in pares if m.distance < 0.78 * n.distance]
    src = np.float32([kp1[m.queryIdx].pt for m in buenos])
    dst = np.float32([kp2[m.trainIdx].pt for m in buenos])
    if modelo == "afin":
        # pocos rasgos (envase chico): sólo escala + giro + traslado, no se deforma
        A, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=4.0)
        Hm = np.vstack([A, [0, 0, 1]])
    else:
        Hm, inl = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
    print(f"  {len(buenos)} pares, {int(inl.sum())} inliers")
    # también se deforma la versión a resolución completa, escalando la homografía
    S = np.diag([esc, esc, 1.0])
    Hfull = Hm @ S
    warp = cv2.warpPerspective(pack_rgba, Hfull, (W, H), flags=cv2.INTER_LANCZOS4)
    a = warp[..., 3].astype(np.float32) / 255
    a_duro = (a > 0.5).astype(np.float32)
    # luz de la escena: razón de baja frecuencia por canal (envase generado ÷ real deformado)
    E = escena.astype(np.float32)
    R = warp[..., :3].astype(np.float32)
    s = max(8, (y1 - y0) / 40)
    # Luz = BRILLO local (luminancia) × un tono cálido PAREJO. Si el envase real sobresale
    # del generado, la razón por canal traía el color de la mesa (manchas verdes y
    # naranjas, 30-09); en luminancia sólo trae luz y sombra.
    pesos = np.array([0.114, 0.587, 0.299], np.float32)  # BGR
    lum = lambda X: (X * pesos).sum(axis=2, keepdims=True)
    bE, bR = blur_enmascarado(E, a_duro, s), blur_enmascarado(R, a_duro, s)
    ratio_l = np.clip(lum(bE) / np.maximum(lum(bR), 1), 0.4, 1.4)
    dentro = a_duro > 0
    tono = (bE[dentro] / np.maximum(lum(bE)[dentro], 1)).mean(axis=0) /            (bR[dentro] / np.maximum(lum(bR)[dentro], 1)).mean(axis=0)
    tono = np.clip(tono, 0.85, 1.15)
    if luz == "canal":
        # por canal: más fiel al color de la escena cuando el envase generado y el real
        # calzan bien de contorno (de pie). Con «lum» el rosado se agrisaba (30-09).
        R2 = np.clip(R * np.clip(bE / np.maximum(bR, 1), 0.35, 1.5), 0, 255)
    elif luz == "suave":
        # R-39 (Paulina, 30-09): el envase conserva SUS colores. Sólo luz y sombra, con
        # rango corto, y un tono cálido casi imperceptible. Con «lum» el azul se iba a durazno.
        R2 = np.clip(R * np.clip(ratio_l, 0.7, 1.12) * np.clip(tono, 0.98, 1.02), 0, 255)
    else:
        R2 = np.clip(R * ratio_l * tono, 0, 255)
    # borde: se come 1 px y se suaviza para que no quede recortado a tijera
    a2 = cv2.GaussianBlur(cv2.erode(a, np.ones((3, 3))), (0, 0), 0.9)[..., None]
    if mover:
        # Se MUEVE el envase ya iluminado a otra posición de la mesa (Paulina, 30-09:
        # «deja un espacio entre los productos para el precio»). La luz se midió donde
        # la IA lo puso; se traslada junto con el envase y se le hace sombra en la mesa.
        dx, dy = mover
        T = np.float32([[1, 0, dx], [0, 1, dy]])
        R2 = cv2.warpAffine(R2, T, (W, H))
        a2 = cv2.warpAffine(a2[..., 0], T, (W, H))[..., None]
        Hfull = np.vstack([T, [0, 0, 1]]) @ Hfull
        a_n = a2[..., 0]
        corr = cv2.warpAffine(a_n, np.float32([[1, 0, 14], [0, 1, 12]]), (W, H))
        sombra = np.clip(cv2.GaussianBlur(corr, (0, 0), 14) - a_n, 0, 1)
        contacto = np.clip(cv2.GaussianBlur(a_n, (0, 0), 4) - a_n, 0, 1)
        lienzo = (lienzo.astype(np.float32) * (1 - (0.40 * sombra + 0.35 * contacto)[..., None]))
        # grosor: el envase es acolchado, no una tarjeta. Se extruye el borde hacia el
        # lado de la sombra con el mismo envase oscurecido (canto de ~1,5 cm a escala).
        for k in range(1, 12):
            Tk = np.float32([[1, 0, k * 0.9], [0, 1, k * 0.75]])
            ak = cv2.warpAffine(a2[..., 0], Tk, (W, H))[..., None]
            Rk = cv2.warpAffine(R2, Tk, (W, H)) * (0.78 - k * 0.012)
            lienzo = lienzo * (1 - ak) + Rk * ak
    L = lienzo.astype(np.float32)
    out = L * (1 - a2) + R2 * a2
    if relieve:
        out = tapa_en_relieve(out, pack_rgba, Hfull, (W, H), relieve)
    return out.astype(np.uint8)


def tapa_en_relieve(out, pack_rgba, Hfull, tam, sombra_px):
    """La tapa blanca sobresale: sombra hacia el lado contrario a la luz + brillo al lado de la luz.

    Paulina, 30-09: visto desde arriba, el packshot 3/4 deja la tapa «como hundida».
    `sombra_px` = [dx, dy] del desplazamiento de la sombra a la escala de la escena.
    """
    b = pack_rgba[..., :3].astype(int)
    blanco = ((b.min(axis=2) > 200) & ((b.max(axis=2) - b.min(axis=2)) < 25) & (pack_rgba[..., 3] > 200)).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(blanco)
    i = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    cs, _ = cv2.findContours((lab == i).astype(np.uint8) * 255, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    tapa = np.zeros(blanco.shape, np.uint8)
    cv2.drawContours(tapa, cs, -1, 255, -1)
    t = cv2.warpPerspective(tapa, Hfull, tam, flags=cv2.INTER_LINEAR).astype(np.float32) / 255
    dx, dy = sombra_px
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    corrida = cv2.warpAffine(t, M, tam)
    sombra = np.clip(cv2.GaussianBlur(corrida, (0, 0), max(abs(dx), abs(dy)) * 0.8) - t, 0, 1)
    out = out * (1 - 0.45 * sombra[..., None])
    luz = np.clip(t - cv2.warpAffine(t, np.float32([[1, 0, -dx * 0.4], [0, 1, -dy * 0.4]]), tam), 0, 1)
    luz = cv2.GaussianBlur(luz, (0, 0), 1.2)
    return np.clip(out + 60 * luz[..., None], 0, 255)


if __name__ == "__main__":
    esc_path, out_path, cfg_path = sys.argv[1:4]
    escena = cv2.imread(esc_path)
    # 4.º argumento opcional: una PLACA (la misma escena sin los envases) sobre la que
    # se pegan en otra posición con «mover». Si no hay placa, se pega sobre la escena.
    lienzo = cv2.imread(sys.argv[4]) if len(sys.argv) > 4 else escena.copy()
    # ⚠️ se busca SIEMPRE en la escena original: si se busca después de pegar el de
    # atrás, el real tapa al de adelante y éste se calza encima del equivocado (30-09).
    for c in json.load(open(cfg_path, encoding="utf-8")):
        print("→", c["pack"])
        pack = cv2.imread(PROD + c["pack"], cv2.IMREAD_UNCHANGED)
        if c.get("cortar_izq"):
            # vista desde arriba: se deja sólo la CARA de adelante del packshot 3/4
            pack = pack[:, int(pack.shape[1] * c["cortar_izq"]):].copy()
        if c.get("cortar_abajo"):
            # «base plana» (Paulina, 30-09): se saca SÓLO el sello dentado de abajo,
            # nunca etiqueta. La fracción es desde arriba: 0.92 = queda el 92 %.
            pack = pack[: int(pack.shape[0] * c["cortar_abajo"])].copy()
        lienzo = calzar(escena, lienzo, pack, c["roi"], c.get("tapar", []), c.get("modelo", "homografia"), c.get("luz", "canal"), c.get("relieve"), c.get("mover"))
    # «restaurar»: zonas donde algo de la escena va ENCIMA del envase (una toallita
    # que asoma). Se devuelven los píxeles blancos y neutros de la escena original.
    for c in json.load(open(cfg_path, encoding="utf-8")):
        for x0, y0, x1, y1 in c.get("restaurar", []):
            e = escena[y0:y1, x0:x1].astype(np.int16)
            blanco = (e.min(axis=2) > 185) & ((e.max(axis=2) - e.min(axis=2)) < 28)
            m = cv2.GaussianBlur(blanco.astype(np.float32), (0, 0), 1.2)[..., None]
            lienzo[y0:y1, x0:x1] = (lienzo[y0:y1, x0:x1] * (1 - m) + escena[y0:y1, x0:x1] * m).astype(np.uint8)
    cv2.imwrite(out_path, lienzo)
    print("✓", out_path)
